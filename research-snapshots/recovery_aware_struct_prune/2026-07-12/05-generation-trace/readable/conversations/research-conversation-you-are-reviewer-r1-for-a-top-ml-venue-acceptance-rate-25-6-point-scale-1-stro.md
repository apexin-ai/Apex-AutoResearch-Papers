# Research conversation: You are Reviewer R1 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 1
- **Tool calls:** 27
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a853eb05b34e76496.jsonl`
- **Structured JSON:** [`a37c3643178ddb8a448d.json`](../../sessions/a3/a37c3643178ddb8a448d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

63 recorded events

### User

_source line 1 · 2026-05-15T14:52:22.434Z_

You are Reviewer R1 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus: **Methods soundness** and **Experimental rigor**.

## Paper Summary

**Title**: Recovery-Aware Structured Pruning: Optimizing What to Remove for How You Recover

**Core idea**: Structured pruning of reasoning LLMs should account for the recovery method (SFT vs RLVR). The paper introduces RASP, which scores structures by S(h) = I(h) × (1−F(h))^α, where F(h) is functional overlap via linear CKA. RASP removes high-overlap (redundant) structures, preserving functionally unique ones that RLVR needs as "anchors" for exploration.

**Model**: DeepSeek-R1-Distill-Qwen-7B at 20% structured sparsity (also 25%, 30%).

**Three Claims**:
1. RASP achieves 84.1% recovery vs 63.7% for standard pruning (17pp gap, p<0.001)
2. Per-structure CKA overlap is the strongest predictor of recoverability (β=0.38, partial R²=0.22, p<0.001)
3. 25pp pruning×recovery interaction (p=0.0008): standard beats RASP under SFT (66% vs 58%) but RASP dominates under RLVR (70% vs 53%)

## Key Tables from Paper

**Table 1 (Main Results, 20% sparsity, GSM8K N=1319)**:
| Method | Post-Prune | +SFT | +GRPO | Recovery |
|---|---|---|---|---|
| Baseline | 83.2 | — | — | — |
| RASP | 31.0 | 57 | 70.0 | 84.1% |
| Standard | 27.0 | 64 | 53.0 | 63.7% |
| Bonsai | 24.0 | 50 | 47.0 | 56.5% |
| GRASPrune | 10.0 | 35 | 38.0 | 45.7% |

**Table 2 (5-seed post-prune, 20% sparsity)**:
Mean±Std: RASP 31.1±1.1, Standard 26.6±0.7, Gap 4.5±0.8, paired t p=0.0002, pruned-set overlap 87-93%.

**Table 3 (SFT→GRPO dynamics)**:
| Method | Post-Prune | Post-SFT | Post-GRPO | GRPO Δ | KL |
|---|---|---|---|---|---|
| RASP | 31 | 57 | 70 | +13 | 4.1 |
| Standard | 27 | 64 | 53 | −11 | 1.8 |

**Table 4 (2×2 Interaction)**:
| Pruning | SFT-Only | SFT+GRPO | GRPO Marginal |
|---|---|---|---|
| RASP | 58 | 70 | +12 |
| Standard | 66 | 53 | −13 |
| RASP Advantage | −8 | +17 | — |
Main effects non-significant; interaction 25pp, p=0.0008.

**Table 5 (Mixed-effects regression, N=784 MLP groups, 28 layers random effect)**:
| Predictor | β (std) | SE | p | Partial R² |
|---|---|---|---|---|
| F(h) CKA overlap | 0.38 | 0.055 | <0.001 | 0.22 |
| I(h) gradient | 0.12 | 0.052 | 0.019 | 0.04 |
| Weight norm | 0.07 | 0.050 | 0.15 | 0.01 |
| Activation mag. | 0.04 | 0.050 | 0.42 | <0.01 |
Marginal R²=0.31, Conditional R²=0.49, ICC=0.18.

**Table 6 (Scoring ablation, post-prune)**:
RASP(full) 31.0 > CKA-only 29.0 > Gradient-only 27.0 > Magnitude 25.0 > Random 18.0

**Table 7 (α sensitivity, post-prune)**:
α=0: 25%, α=0.25: 27%, α=0.5: 29%, α=1.0: 31%, α=2.0: 35%. Monotonically increasing, no peak.

**Table 8 (GRASPrune breaks linear assumption)**:
GRASPrune post-prune 10% but GRPO Δ=+3pp (vs Standard's −11pp at 27% post-prune).

**Table 9 (Multi-sparsity)**:
20%: RASP 70 vs Standard 53 (gap 17pp). 25%: RASP 55 vs Standard 32 (gap 23pp). 30%: both near-collapse.

**Table 10 (OOD)**:
GSM8K: RASP 70 vs Std 53 (+17). MATH-500: RASP 55 vs Std 42 (+13). HumanEval: RASP 40 vs Std 33 (+7).

**Table 11 (Structured vs Unstructured)**:
RASP structured: 70%, 1.28× speedup. Unstructured: 60%, 1.02× speedup.

**Table 12 (Extended baselines)**: All methods at 20% with GRPO Δ pattern: RASP(+13) >> GRASPrune(+3) > Bonsai(−3) > Standard(−11). Random and Unstructured(+5) also shown.

**Table 13 (Collapse map)**: 20-25% recoverable, 30% near-collapse, 35% collapsed.

**Section 5.12 (CKA reliability)**: Split-half ρ=0.93. Cal size: 256→29%, 512→31%, 1024→32%. Pruned-set overlap 86-95%.

**Inference (Appendix C)**: 9.7ms/tok (1.28× speedup), 18.5% memory reduction.

## Experiment Design Coverage

The full experiment design has 18 planned experiments. All 18 are represented in the paper:
- plan_001-004: Core pipeline (Tables 1, 3)
- plan_005: GRASPrune (Tables 1, 8)
- plan_006: Multi-seed (Table 2)
- plan_007: Scoring ablation (Table 6)
- plan_008: CKA-recoverability regression (Table 5)
- plan_009: 2×2 interaction (Table 4)
- plan_010-011: Multi-sparsity (Table 9)
- plan_012: OOD eval (Table 10)
- plan_013: Bonsai (Tables 1, 12)
- plan_014: CKA reliability (Section 5.12)
- plan_015: α ablation (Table 7)
- plan_016: Inference benchmark (Table 11, Appendix C)
- plan_017: Unstructured baseline (Tables 11, 12)
- plan_018: SFT OOD eval (Section 5.10)

## Your Review Task

Produce a structured review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (methods + experiments, numbered)
3. **Weaknesses** (methods + experiments, numbered, with severity: Major/Minor)
4. **Questions to Authors** (numbered)
5. **Missing Experiments or Controls** (if any from the 18-experiment design are inadequately reported)
6. **Statistical Rigor Assessment**
7. **Reproducibility Concerns**
8. **Overall Score** (1-6) with justification
9. **Confidence** (1-5, where 5 = certain)

Be rigorous. A top venue expects: multiple models/datasets, strong baselines, proper statistical testing, ablations, and clear methodology. Evaluate whether the claims are adequately supported by the evidence presented.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "55184f43-b55f-4565-92a7-857adccb29fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T14:52:22.439Z_

```json
{
  "parentUuid": "55184f43-b55f-4565-92a7-857adccb29fb",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
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
  "uuid": "9114de7a-7c13-4c30-9b72-0e9a9f42084d",
  "timestamp": "2026-05-15T14:52:22.439Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T14:52:25.304Z_



I'll start by reading the full paper and any available project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9114de7a-7c13-4c30-9b72-0e9a9f42084d",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YVhVDeuLnUbsdWc7HU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "917ef05f-d255-4364-9dc0-9f6b8efba1a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018uCFhJnSxiLEzUqajB2FWi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16229,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16229,
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

_source line 4 · 2026-05-15T14:52:25.892Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TAPe6WuNpMHPL1susjU6CM`</summary>

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
  "parentUuid": "917ef05f-d255-4364-9dc0-9f6b8efba1a0",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YVhVDeuLnUbsdWc7HU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c18f47b-24c8-4353-bc39-d3ad2e1f705b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018uCFhJnSxiLEzUqajB2FWi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16229,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16229,
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

_source line 5 · 2026-05-15T14:52:25.896Z_

<details><summary>↩ Tool result · `toolu_01TAPe6WuNpMHPL1susjU6CM`</summary>

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
  "parentUuid": "4c18f47b-24c8-4353-bc39-d3ad2e1f705b",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "a080e7f8-081d-4835-bf50-02232176767d",
  "sourceToolAssistantUUID": "4c18f47b-24c8-4353-bc39-d3ad2e1f705b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T14:52:29.277Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JaKtU8y3QAP53nFC5AE7eq`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a080e7f8-081d-4835-bf50-02232176767d",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YVxikfVQ4SegSLK46t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f4b8461-795d-45ee-800c-506b8735f256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmBnMNaUixqZeLeRQwoJr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 16229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

_source line 7 · 2026-05-15T14:52:29.301Z_

<details><summary>↩ Tool result · `toolu_01JaKtU8y3QAP53nFC5AE7eq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| grpo_stage2_rasp_20_v8 | D031: GRPO v8 RASP — v7 disk crash fix. HF cache redirected to data disk. 8-bit AdamW, max_completion_length=1024, beta=0.01, temp=0.4, rep_penalty=1.15, format_reward=0.1, gradient_checkpointing=True, 100 steps. Parent: sft_rasp_20. | — | — | [0wz7xpd5] |\\n| grpo_stage2_standard_20_v8 | D031: GRPO v8 Standard (negative control) — v7 disk crash fix + GPU mapping fix. HF cache redirected to data disk, CUDA_VISIBLE_DEVICES=1 + --gpu 0. 8-bit AdamW, max_completion_length=1024, identical params to RASP v8. Parent: sft_standard_20_retrain. | — | — | [q34vz8j2] |\\n\\n## 待处理\\n- eval-sft-alpha-1p0（准备中）\\n- sft_alpha2_0_westd: D027: α=2.0 pruned model SFT recovery on westd. α=2.0 post-prune accuracy 29%. Same SFT params as other α variants (2 epochs, lr=2e-5, batch=1, grad_accum=8). Completes α ablation sweep.（准备中）\\n- grasp_baseline_westd: D027: GraSP baseline on westd — compare GraSP pruning criterion against RASP at 20% sparsity. If RASP > GraSP post-recovery, confirms CKA-aware scoring advantage over gradient-based saliency. Critical for plan_005 and Dream reviewer concern.（准备中）\\n- sft_grasp_20_westd: D028: GraSP pruned model (8% post-prune) SFT recovery. Same params as RASP/Standard SFT (2 epochs, lr=2e-5, batch=1, grad_accum=8). Completes three-way comparison: Standard 27%→64%, RASP 31%→57%, GraSP 8%→?. Tests whether importance metric choice affects recovery potential.（准备中）\\n- grpo_stage2_standard_20_v5: D027: GRPO v5 Standard (negative control) — identical params to RASP GRPO v5: beta=0.01, temp=0.4, rep_penalty=1.15, format_reward=0.1, max_completion_length=512, gradient_checkpointing=True, monkey-patch ref_model. Direct comparison with grpo_stage2_rasp_20_v5. If RASP >> Standard, confirms CKA-aware pruning preserves RLVR-recoverable structures.（准备中）\\n- alpha_ablation_westd_cal256: α ablation sweep (calibration=256, N=100). α∈{0.0,0.5,1.0,2.0,4.0} at 20% sparsity. Phase A (prune+eval) complete, Phase B (SFT) in progress. Note: calibration=256 differs from westb original (512), causing ~5% group selection differences.（准备中）\\n- mvp_rasp_pipeline_v4: CKA functional overlap F(h) predicts structured pruning recoverability under RLVR. RASP scoring S(h)=I(h)×(1-F(h))^α selects structures whose removal is more recoverable via GRPO RLVR than standard importance-only pruning. V4: Dual sparsity probe (20% + 25%) to find viable operating point where pruned models retain >5% accuracy, then GRPO recovery comparison.（准备中）\\n\\n## 近期结论\\n- **eval-sft-alpha-0p0** (success): —\\n- **grpo_stage2_standard_20_v7** (failed): D030: GRPO v7 — v6 OOM fix. 8-bit AdamW optimizer (bitsandbytes) saves ~50% optimizer memory. max_steps=100 (~756s/step). All other params same as v6: max_completion_length=1024, beta=0.01, temp=0.4, rep_penalty=1.15, format_reward=0.1, gradient_checkpointing=True, monkey-patch ref_model. ← 基于 sft_standard_20_retrain\\n- **grpo_stage2_rasp_20_v7** (failed): D030: GRPO v7 — v6 OOM fix. 8-bit AdamW optimizer (bitsandbytes) saves ~50% optimizer memory. max_steps=100 (~756s/step). All other params same as v6: max_completion_length=1024, beta=0.01, temp=0.4, rep_penalty=1.15, format_reward=0.1, gradient_checkpointing=True, monkey-patch ref_model. ← 基于 sft_rasp_20\\n\\n## 趋势\\n成功 7 / 负向 5 / 失败 10 / 共 28\\ntrain_loss_final: 0.64 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestb-23072: 无 GPU 信息\\nwestd-11672: 无 GPU 信息\\n\\n## 告警\\n- mvp_rasp_pipeline: 训练失败 — unknown\\n- mvp_rasp_pipeline_v2: 训练失败 — unknown\\n- grpo_rasp_20: 已被终止 — unknown\\n- grpo_standard_20: 已被终止 — unknown\\n- grpo_rasp_20_4096: 训练失败 — unknown\\n- grpo_stage2_rasp_20: 已被终止 — unknown\\n- grpo_stage2_standard_20: 已被终止 — unknown\\n- grpo_stage2_standard_20_v2: 训练失败 — unknown\\n- grpo_stage2_rasp_20_v3: 训练失败 — unknown\\n- grpo_stage2_rasp_20_v4: 已被终止 — unknown\\n- grpo_stage2_rasp_20_v5: 已被终止 — unknown\\n- sft_alpha4_0_westd: 训练失败 — unknown\\n- grpo_stage2_rasp_20_v6: 训练失败 — unknown\\n- grpo_stage2_standard_20_v6: 训练失败 — unknown\\n- grpo_stage2_rasp_20_v7: 训练失败 — unknown\\n- grpo_stage2_standard_20_v7: 训练失败 — unknown\\n\", \"total_chars\": 4164, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f4b8461-795d-45ee-800c-506b8735f256",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "c0d1dea0-b398-451b-ae72-7466dc489b39",
  "sourceToolAssistantUUID": "3f4b8461-795d-45ee-800c-506b8735f256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T14:52:29.866Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01W58YPzbUkgcwcPhjtaQoiJ`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0d1dea0-b398-451b-ae72-7466dc489b39",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YVxikfVQ4SegSLK46t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db067c2d-4feb-45a7-811f-a1a00762705b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmBnMNaUixqZeLeRQwoJr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 16229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

_source line 9 · 2026-05-15T14:52:29.879Z_

<details><summary>↩ Tool result · `toolu_01W58YPzbUkgcwcPhjtaQoiJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper_framing.md\", \"content\": \"# Paper Framing — recovery_aware_struct_prune\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 submission)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Insight (Redundancy Paradox)\\nTraditional structured pruning selects structures to remove based on importance metrics alone (weight magnitude, gradient sensitivity). We show this misses a critical signal for RLVR recovery: **functional uniqueness**. Structures with high functional overlap (high CKA) can be safely pruned because RLVR redistributes their function across retained structures. Structures with low overlap are functionally irreplaceable — once removed, even RLVR cannot recreate their unique contribution. This creates a **Redundancy Paradox**: protecting functionally unique structures matters more for recovery than protecting high-importance structures.\\n\\nRASP exploits this via S(h) = I(h) × (1-F(h))^α: high overlap → low score → **pruned first**; low overlap → high score → **protected**. The result: RASP preferentially removes functionally redundant structures (whose function RLVR can recover) while Standard pruning may accidentally remove functionally unique structures that happen to have low importance scores. At 20% sparsity, this effect manifests entirely within MLP channel groups (0/112 attention GQA groups are pruned under either method; all 200 pruned structures are MLP groups), consistent with the \\\"RL Squeezes, SFT Expands\\\" mechanism (ICLR 2026).\\n\\n## Core Claims (3)\\n\\n1. **CKA-aware pruning enables superior RLVR recovery**: At matched sparsity and parameter count, RASP and Standard pruning yield comparable post-prune accuracy (31% vs 27% GSM8K at 20% sparsity, N=100, p=0.54 — D027 corrected), but diverge dramatically after RLVR recovery. The decisive evidence is the GRPO recovery gap (v7 running), not post-prune accuracy. If confirmed, this means CKA-aware structure selection preserves reasoning scaffolding that RLVR can leverage, even when immediate accuracy is similar.\\n\\n2. **Functional overlap predicts per-structure recoverability** *(scope: MLP channel groups at moderate sparsity)*: Per-structure CKA functional overlap F(h) is a stronger predictor of post-recovery accuracy retention than standard importance metrics alone, within the MLP channel groups that are actually pruned at 20-25% sparsity. At these sparsity levels, attention GQA groups consistently rank above all MLP groups in the global importance list (0/112 pruned); the CKA signal's practical effect is selecting *which* MLP groups to prune (N=784, ~200 pruned). Validated via mixed-effects regression (layer as random effect) on MLP groups, controlling for weight norm, gradient importance, and activation magnitude. Cross-component (attention + MLP) validation requires higher sparsity (~40%+).\\n\\n3. **Recovery method conditions optimal pruning order**: The relative ranking of pruning strategies changes depending on recovery method (RLVR vs SFT). Structures expendable under RLVR recovery may be critical under SFT recovery, consistent with the \\\"RL Squeezes, SFT Expands\\\" mechanism — RLVR compresses incorrect paths (tolerates removal of overlapping structures) while SFT expands correct paths (needs preserved trajectory-encoding structures).\\n\\n## Story Spine\\n\\n- **Problem**: Structured pruning for reasoning LLMs optimizes for immediate post-pruning accuracy, treating subsequent recovery as independent. But post-prune accuracy is a poor proxy for recoverability: two pruning strategies can yield similar immediate accuracy (31% vs 27%) yet produce dramatically different outcomes after RLVR recovery. The choice of *which structures* to prune — not just how many — determines whether recovery can succeed.\\n\\n- **Existing approaches & gaps**: Self-Healing (2025) shows RLVR recovers pruned reasoning models to 95%+ at 25% compression but uses standard pruning and tests only one ratio. GRASPrune (ACL 2026) provides SOTA budgeted structural pruning but doesn't study reasoning-specific recovery. RESP (Dec 2025) uses reasoning-trace calibration but has no recovery phase. No work studies how the pruning structure choice interacts with RLVR recovery quality, or whether optimal pruning differs for RLVR vs SFT recovery.\\n\\n- **Our framing**: We introduce Recovery-Aware Structured Pruning (RASP), reframing structural redundancy from a flaw to eliminate into a signal of RLVR recoverability. RASP scores structures by S(h) = I(h) × (1 - F(h))^α, protecting functionally unique reasoning scaffolding while allowing removal of structures whose function can be redistributed through RLVR. This connects to the Lottery Ticket Hypothesis at a new level: LTH asks \\\"which subnetwork trains well\\\" (binary); RASP asks \\\"which structures to remove so the remainder recovers well under a specific training paradigm\\\" (paradigm-conditioned trainability).\\n\\n- **Headline result template**: \\\"At 20% structured sparsity on DeepSeek-R1-Distill-Qwen-7B, RASP and Standard pruning achieve comparable post-prune accuracy (31% vs 27%), yet RASP enables RLVR recovery to X% while Standard recovers only to Y% (Δ=Z pp, p<0.01). Post-prune accuracy is a poor predictor of recoverability; CKA-based functional overlap explains W% of per-structure recovery variance (mixed-effects β, p < 0.001).\\\"\\n\\n## Venue Fit\\n- EMNLP Efficient Methods track: natural fit for structured pruning + reasoning model recovery\\n- Reasoning model compression is timely (DeepSeek-R1, QwQ, etc. driving demand)\\n- Empirical rigor + mechanistic analysis aligns with EMNLP's preference for thorough experimentation\\n\\n## Venue Fit Risks\\n- **\\\"Just another pruning metric\\\"**: Mitigate with Redundancy Paradox framing, LTH generalization (paradigm-conditioned trainability), and mechanistic analysis showing WHY it works\\n- **\\\"Single model\\\"**: DeepSeek-R1-Distill-Qwen-7B is the most widely-used open reasoning model; multi-sparsity + multi-method comparison compensates\\n- **\\\"MPruner already uses CKA\\\"**: Different granularity (intra-layer per-head vs inter-layer), different objective (recoverability prediction vs redundancy removal), different domain (reasoning LLM vs CNN/general transformer)\\n- **\\\"Cross-component pruning not observed\\\"**: At 20-25% sparsity, only MLP groups are pruned (0 attention groups). Framework scores both types jointly, but global ranking at moderate sparsity naturally prioritizes MLP removal. Mitigate by: (1) honest description of actual pruning distribution, (2) noting the CKA signal drives recovery gap via MLP group reranking, (3) optionally test higher sparsity where attention groups enter pruning range\\n\\n## Anticipated Reviewer Concerns & Experimental Responses\\n\\n| Concern | Response | Supporting Experiment |\\n|---------|----------|----------------------|\\n| Incremental over importance-only pruning | Post-prune gap is modest (4pp), but RLVR recovery gap is decisive; structure selection matters more for recoverability than for immediate accuracy | exp-001, exp-002 |\\n| CKA overlap might correlate with simpler metrics | Scoring ablation: CKA vs magnitude/gradient/random | exp-007 |\\n| Single model generalization | Multi-sparsity (20%, 25%, 30%) + multi-method (Standard, GRASPrune, RASP) | exp-003, exp-005 |\\n| RLVR vs SFT claim needs controlled comparison | Same pruned models, same data budget, different recovery method | exp-006 |\\n| Statistical rigor of correlation claim | Mixed-effects regression with covariates on MLP groups (N=784, ~200 pruned) | exp-008 |\\n| Only MLP groups pruned at 20% sparsity | Honest description + CKA drives recovery gap via MLP reranking + optional higher sparsity test | experiments.tex |\\n| Recovery might just reflect post-prune accuracy | Include GRASPrune (different post-prune accuracy profile) to break correlation | exp-005 |\\n\\n## Key Differentiations\\n- **vs MPruner (2024)**: inter-layer CKA for depth pruning in CNNs → RASP uses intra-layer CKA between individual heads for width pruning in reasoning LLMs, optimizing for post-recovery (not immediate) performance\\n- **vs Self-Healing (2025)**: tests RLVR recovery with standard pruning → RASP optimizes the pruning decision FOR recovery\\n- **vs RESP (Dec 2025)**: reasoning-trace calibration without recovery → RASP includes recovery-awareness in the pruning score\\n- **vs GRASPrune (ACL 2026)**: SOTA budgeted pruning without recovery study → GRASPrune is our primary baseline\\n- **vs PASER (2025)**: optimizes recovery DATA → RASP optimizes pruning STRUCTURE (complementary)\\n\", \"total_chars\": 8449, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db067c2d-4feb-45a7-811f-a1a00762705b",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "38993407-3fee-4cfd-b1bd-1661392887d8",
  "sourceToolAssistantUUID": "db067c2d-4feb-45a7-811f-a1a00762705b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T14:52:30.299Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01G4o1Jfmrfq1BASNue1rab6`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38993407-3fee-4cfd-b1bd-1661392887d8",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YVxikfVQ4SegSLK46t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27080427-5a94-47be-aa2b-04e5fd72237e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmBnMNaUixqZeLeRQwoJr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 16229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

_source line 11 · 2026-05-15T14:52:30.308Z_

<details><summary>↩ Tool result · `toolu_01G4o1Jfmrfq1BASNue1rab6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/ROADMAP.md\", \"content\": \"# recovery_aware_struct_prune — Research Dashboard\\n\\n> 最后更新: 2026-05-15 14:50 UTC | 更新原因: D032 GRPO v8 双卡稳定运行，更新工程历史和任务状态\\n\\n## 核心方向\\nRecovery-Aware Structured Pruning (RASP)：CKA functional overlap 指导结构化剪枝，在 matched sparsity 下比 importance-only 剪枝显著更好地保留推理能力（**Redundancy Paradox**）。详见 paper_framing.md。\\n\\n## 目标会议\\nEMNLP 2026 ARR May 25 提交（距今 10 天）\\n\\n## 当前阶段\\n**Research Phase** — GRPO v8 双卡稳定运行中（D032）。westd GraSP SFT + α ablation 并行推进。\\n\\n## 核心证据（D027 修正后）\\n- ~~Post-prune: RASP 29% vs Standard 1%~~ → **D027 修正: RASP 31% vs Standard 27% (4pp, p=0.54, 不显著)**\\n- Post-SFT GSM8K (N=100): RASP 57% vs Standard 64%（Standard 反超 7pp）\\n- GraSP post-prune: 8% — RASP >> GraSP 3.6x，gradient-based baseline 远劣（D027 仍成立）\\n- α ablation post-prune: α=0.0 30% / α=0.5 25% / α=1.0 27% / α=4.0 40%（CI 重叠，N=100 不足以区分）\\n- α=4.0 post-SFT: 62%，α=1.0 post-SFT: 57%——SFT 有均衡化效应\\n- **GRPO v8 是唯一尚存的核心假设验证路径**\\n\\n## Claims & 实验覆盖\\n| Claim | P0 实验 | 状态 |\\n|-------|---------|------|\\n| C1: CKA-aware pruning preserves reasoning | plan_001-006, plan_015 | ⏳ GRPO v8 运行中 |\\n| C2: F(h) predicts recoverability | plan_007-008, plan_014-015 | 待 GRPO 完成 |\\n| C3: Recovery method conditions pruning order | plan_009 | SFT: Standard>RASP (D029)；待 GRPO 确认反转 |\\n\\n## 近期任务\\n- [ ] **GRPO v8 双卡运行中** — westb cuda:0 RASP, cuda:1 Standard (~21h, ETA ~5/16 11:30 UTC)\\n- [ ] **GRPO v8 监控** — step 5 (~1h) 和 step 20 (~4h) 检查 reward/grad_norm 早期信号\\n- [ ] **GraSP SFT + eval** — westd cuda:0，接近完成\\n- [ ] **α ablation SFT sweep** — westd cuda:1, 已完成 α=0.0/0.5/1.0/4.0, α=2.0 启动中\\n- [ ] GRPO v8 完成 → eval 两模型(N=100, greedy) → 判定: |RASP-Standard| >15pp/5-15pp/<5pp\\n- [ ] 全部 α SFT+eval 完成 → α vs recovery 曲线\\n- [ ] [Dream P0] α ablation plan_015 — GRPO 完成后立即执行\\n- [ ] [Dream P1] Inference speedup plan_016 / Unstructured baseline plan_017\\n- [ ] [Dream] Multi-seed 扩展 plan_006 到 5 seeds\\n- [x] D027 definitive re-eval: RASP 31% vs Standard 27%\\n- [x] D028 kill v5 → start v6 (512→1024 fix truncation)\\n- [x] D029 SFT recovery: Standard 64% > RASP 57%\\n- [x] GraSP post-prune: 8%\\n- [x] D032 GRPO v8 启动（v6 OOM → v7 磁盘满 → v8 修复缓存+GPU映射+参数）\\n\\n## GRPO 结果 Contingency\\n| GRPO 结果 | 影响 | 行动 |\\n|-----------|------|------|\\n| RASP >> Standard (>15pp) | Recovery-pathway hypothesis 成立 | 全面推进 plan_001-017，story: CKA-guided pruning 创造更好 RL recovery dynamics |\\n| RASP > Standard (5-15pp) | Claim 1 成立但需加固 | 优先 plan_001 full eval + plan_006 multi-seed + plan_015 α ablation |\\n| RASP ≈ Standard (<5pp) | 核心假设失败 | 根本性 pivot: 转 training dynamics 分析 / 25% sparsity / 负向发现论文 |\\n| Standard > RASP | 全面失败 | Reframe 或终止 |\\n\\n## GPU 预算\\n- **westb-23072**: 2× ~98GB GPU | cuda:0 GRPO RASP v8, cuda:1 GRPO Standard v8\\n- **westd-11672**: 2× ~95GB GPU | cuda:0 GraSP SFT+eval, cuda:1 α ablation SFT sweep\\n- 约束 C001: 仅允许 westb cuda:0/1, westd cuda:0/1\\n- 总预算 ~480 GPU-hours (10 days × 2 server × 2 GPU × 24h)\\n\\n## GRPO 工程问题历史（v1-v8）\\nv1-v4: 截断/collapse/ETA过长 → v5: step 80 collapse → v6: OOM step 8 → v7: 磁盘满+参数错误+重复进程 → **v8: 缓存迁移+GPU映射+参数统一，双卡稳定运行**\\n\\n## 论文写作备忘（Dream 通用建议，给 Paper Agent）\\n- 扩展 references 到 25+，引用 FANG、FuncNet、RestoreLCC、PAT\\n- 论证 CKA vs SVCCA/CCA/MI 选择\\n- 讨论 Claim 2 潜在循环性并加以区分\\n- 报告 I(h)-F(h) correlation\\n- Temper scope claims（单模型局限性坦诚讨论）\\n\\n## 关键风险\\n1. **GRPO v8 失败 = 项目需根本性 pivot**——唯一核心风险\\n2. Post-prune 差异仅 4pp (p=0.54)——pre-recovery claim 已不成立，论文 story 完全依赖 GRPO recovery 阶段差异\\n3. 单模型限制 → Dream 三档一致标记\\n4. DDL 10 天——GRPO 结果 5/16 出，留 ~9 天写作+补实验\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D032 | 2026-05-15 | GRPO v7 双组崩溃(磁盘满+静默死亡)，v8 修复: HF cache 迁移数据盘 + GPU | grpo_stage2_rasp_20_v7, grpo_stage2_standard_20_v7 |\\n| D031 | 2026-05-15 | GRPO v6 OOM at step 8, 切 v7: 8-bit AdamW optimizer | grpo_stage2_rasp_20_v6, grpo_stage2_standard_20_v6 |\\n| D030 | 2026-05-15 | GRPO v6 双卡 OOM 崩溃(step 8)，切 v7: 8-bit optimizer +  | grpo_stage2_rasp_20_v6, grpo_stage2_standard_20_v6 |\\n| D029 | 2026-05-15 | SFT recovery 阶段 Standard 优于 RASP/α=4.0，核心假设在 SFT 层 | sft_alpha4_0_westd, sft_standard_20_retrain, grpo_stage2_rasp_20_v6, grpo_stage2_standard_20_v6 |\\n| D028 | 2026-05-15 | Kill GRPO v5 (RASP+Standard)，切 v6: max_completion_ | grpo_stage2_rasp_20_v5, grpo_stage2_standard_20_v5 |\\n| D027 | 2026-05-15 | Post-prune 核心 claim 崩塌（RASP 31% vs Standard 27%, p | reeval_postprune_definitive, grpo_stage2_rasp_20_v5 |\\n| D026 | 2026-05-15 | 将 RASP definitive re-eval 部署到 westd GPU 0 并行执行，不等  | reeval_postprune_definitive |\\n| D025 | 2026-05-15 | 挂起 D006/D014 基于 \\\"29x advantage\\\" 的所有结论，等待 definitiv | D023, D006, D014 |\\n| D024 | 2026-05-15 | CRITICAL: D023 re-eval 显示 Standard post-prune ~32% | D023, alpha_ablation_phase_a |\\n| D023 | 2026-05-15 | α ablation Phase A 暴露 importance formula confound  | alpha_ablation_phase_a |\\n\\n\\n\", \"total_chars\": 4626, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27080427-5a94-47be-aa2b-04e5fd72237e",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "77e4e6ca-4b3e-4a2b-849d-4cfb8d71fd93",
  "sourceToolAssistantUUID": "27080427-5a94-47be-aa2b-04e5fd72237e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T14:52:33.614Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0185a7Su4JdFuDptoPne6SMT`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77e4e6ca-4b3e-4a2b-849d-4cfb8d71fd93",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YWHLgber7DjLaRG35E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9a04b99-f9c3-42e1-aca7-6340097c66eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQPeFdcE3ipTzmpjgeQEci",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7719,
      "cache_read_input_tokens": 17678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7719,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 55,
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

_source line 13 · 2026-05-15T14:52:33.632Z_

<details><summary>↩ Tool result · `toolu_0185a7Su4JdFuDptoPne6SMT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/memory.md\", \"content\": \"# Memory\\n\\n## 2026-05-15: D022 — Calibration sensitivity at 20% sparsity (fragile threshold)\\n- [关键发现] westb (512 calibration samples) 和 westd (256 samples) 代码完全一致（0 行 diff），但 α=0.0 结果分别为 1% 和 30%。根因：calibration sample 数量差异导致 ~5% MLP group 选择不同。模型在 20% sparsity 处于 fragile threshold，少量 group 变化引起巨大 accuracy 差异。\\n- [验证] westb Standard 1% 是真实退化（输出 \\\"10 years, 10 years...\\\" 重复循环 316KB），不是 eval bug。同服务器、同脚本、间隔 45 分钟，RASP 输出连贯推理（91KB）。\\n- [α ablation N=100] α=0.0 (30%) / α=0.5 (25%) / α=1.0 (27%) — 95% CI 重叠，无统计显著差异。需要 N=1319 全集才能下结论。\\n- [行动项] westd 需用 n_samples=512 重算 importance scores 消除 calibration 混淆。\\n\\n## 2026-05-15: GRPO sampling collapse on pruned models\\n- [失败模式] SFT 恢复 greedy 准确率 (57-64%) 和 EOS (99%) 后，GRPO sampling (temp=0.7) 仍导致剪枝模型退化为重复循环，grad_norm=0, reward=0。根因：剪枝模型在 stochastic sampling 下脆弱。\\n- [v2 失败] beta=0 + max_completion_length=1024, 双组 step 30-35 collapse → GRPO method failure。\\n- [v3 失败] beta=0.01 触发 GRPOTrainer from_pretrained 加载 ref_model，剪枝模型 shape mismatch 崩溃。\\n- [v4 修复] monkey-patch create_model_from_path → load_pruned_model。temp 0.7→0.4, repetition_penalty=1.15, format_reward +0.1, gradient_checkpointing=True, max_completion_length=2048。TRL 1.1.0。\\n- [经验] GRPO 在剪枝模型上必须预检 sampling 生成质量。beta>0 需要手动处理 ref_model 加载。\\n\\n## 2026-05-15: GraSP vs RASP — gradient saliency 远劣于 CKA-aware pruning\\n- [关键发现] GraSP 20% post-prune accuracy = 8% (50 样本 checkpoint)，RASP 20% = 29-31%，3.6x 差距。\\n- GraSP 模型 EOS rate 仅 2%（几乎所有输出截断在 4096 token），说明 gradient-based saliency 在结构化剪枝中严重破坏生成能力。\\n- 使用 GRASPrune 库，keep_ratio=0.80, rescale_alpha=0.5, 512 samples, 4 epochs gate training。\\n- 模型路径: `/root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20/`\\n- [意义] 有力回应 Dream reviewer concern (plan_005)——RASP 显著优于主流 gradient-based baseline。\\n\\n## 2026-05-15: α ablation SFT — 非单调关系确认\\n- α=4.0: post-prune 40% → post-SFT 62% (+22pp)，为所有 α 值中最高\\n- α=1.0 (RASP default): post-prune 29% → post-SFT 57%\\n- Standard: post-prune 27% → post-SFT 64%\\n- [观察] post-prune 阶段 α=4.0 最优，但 post-SFT 阶段差距缩小（57-64% 范围）。SFT 有均衡化效应。\\n- [关键问题] GRPO 阶段是否能拉开差距？这是整个论文 narrative 的决定性验证。\\n\\n## 2026-05-15: sft_standard_20 checkpoint 已删除\\n- 磁盘清理删除了 sft_standard_20（81GB），正在 cuda:1 重训。\\n- 重训参数：pruned_standard_20 + GSM8K full train (7473) + 2 epochs + lr=2e-5，~37-40 min。\\n\\n## 2026-05-15: 代码与环境备忘\\n- α ablation: `prune.py` 支持 `--alpha`，CKA 分数缓存 `results/cka_scores.pt`\\n- Full eval: `scripts/run_full_eval.sh`（新版），`src/run_full_eval.sh`（旧版）\\n- GRASPrune: `/root/GRASPrune/`，不要 `pip install -r requirements.txt`\\n- GRPO 输出路径：`grpo_stage2_rasp_20` / `grpo_stage2_standard_20`\\n- sft_recovery.py 不支持 `--save_strategy` 和 `--overwrite_output_dir` 参数\\n- westb 磁盘：数据盘 250GB 已用 141GB，剩 110GB\\n- westd 磁盘：释放 93GB 后空间充足（原 72GB used → 大幅改善）\\n\", \"total_chars\": 2685, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9a04b99-f9c3-42e1-aca7-6340097c66eb",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "b393f62d-b76a-4265-831d-b7ea6923d24a",
  "sourceToolAssistantUUID": "a9a04b99-f9c3-42e1-aca7-6340097c66eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T14:52:34.539Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Q311jioGgDzUcBRsEsMjNs`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b393f62d-b76a-4265-831d-b7ea6923d24a",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YWHLgber7DjLaRG35E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b398abd1-a7ed-44c3-b16c-24993040a9cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQPeFdcE3ipTzmpjgeQEci",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7719,
      "cache_read_input_tokens": 17678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7719,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 55,
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

_source line 15 · 2026-05-15T14:52:34.549Z_

<details><summary>↩ Tool result · `toolu_01Q311jioGgDzUcBRsEsMjNs`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'recovery_aware_struct_prune'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b398abd1-a7ed-44c3-b16c-24993040a9cd",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "a8ac71be-7a0a-4065-a1e3-fc7c6126a5de",
  "sourceToolAssistantUUID": "b398abd1-a7ed-44c3-b16c-24993040a9cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T14:52:34.865Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BVxv29faLWVJ6cc6Ywr2LF`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8ac71be-7a0a-4065-a1e3-fc7c6126a5de",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YWHLgber7DjLaRG35E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b2857b4-87bc-42f7-bf4a-5fbd1986045f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQPeFdcE3ipTzmpjgeQEci",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7719,
      "cache_read_input_tokens": 17678,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7719
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 17678,
          "cache_creation_input_tokens": 7719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7719,
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

_source line 17 · 2026-05-15T14:52:34.880Z_

<details><summary>↩ Tool result · `toolu_01BVxv29faLWVJ6cc6Ywr2LF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/decisions.yaml\", \"content\": \"_next_id: 33\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 06:10 UTC\\n  summary: MVP 接受 35% sparsity 下 MLP-only pruning，不强制 attention 配额\\n  rationale: 全局统一排序下 attention GQA groups importance 普遍高于 MLP groups，35% sparsity\\n    自然只剪 MLP（367 groups）。这是模型结构特征的正确反映，不应人为干预。MLP-level correlation (N=367) 足以验证 CKA→recoverability\\n    假设。50% sparsity 放 Phase 2 获取 attention-level 数据。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: primary\\n    result: running\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 13:31 UTC\\n  summary: 终止无效 GRPO，改用 SFT warmup → GRPO 两阶段恢复策略\\n  rationale: 35% 结构化剪枝后两个模型 accuracy 仅 0.15%（输出退化），GRPO 150 步 loss=0/grad_norm=0，无学习信号。frac_reward_zero_std\\n    ≈ 1.0 表明几乎所有 completion 得 0 reward，GRPO 无法计算有效 advantage。SFT warmup 用 ground truth\\n    数据先恢复基本能力再转 GRPO 是解决 reward desert 的标准做法。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: motivating_failure\\n    result: GRPO 150 步 loss=0, grad_norm=0; post-prune accuracy 0.15% for both models\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 13:53 UTC\\n  summary: 暂缓 SFT warmup，优先审计剪枝实现正确性\\n  rationale: 两个不同剪枝策略产出精确相同的 accuracy（2/1319）统计上极不寻常，35% structured pruning 不应导致 7B\\n    模型完全崩溃。Reviewer 怀疑存在实现 bug（config 不匹配、全零层等）。若根因是代码问题，SFT warmup 是在错误基础上浪费算力。需先排除实现问题再决定恢复策略。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: audit_target\\n    result: both pruned models 0.15% accuracy, identical 2/1319\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 13:59 UTC\\n  summary: 修复 min_keep_mlp=4 导致的 per-layer 过度剪枝，重跑 MVP pipeline v3\\n  rationale: 根因确认：min_keep_mlp=4 允许单层 MLP 被剪至 14.3% capacity，全局排序集中破坏 early layers（0-6），两个模型均崩溃至\\n    0.15%。修复方案：min_keep_mlp 提升到 40% per layer + per-layer capacity floor。RASP scoring\\n    逻辑本身正常（产生了不同剪枝结构），核心假设仍可验证，只需收紧约束后重跑。同时补基线评估。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v2\\n    role: root_cause_identified\\n    result: min_keep_mlp=4 causes early layer collapse to 14.3% MLP capacity\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 15:13 UTC\\n  summary: 放弃 35% sparsity 作为 MVP 目标，改用 20%/25% 双 sparsity 快速探测后选优跑 GRPO\\n  rationale: v3 证实 35% structured pruning 对 DeepSeek-R1-Distill-Qwen-7B 太激进（Standard\\n    0%, RASP 1%），即使 per-layer capacity floor ≥40% 也无法挽救。蒸馏模型冗余已被压缩，比 base 模型更脆弱。RASP\\n    hypothesis 未被 falsify——只是当前 sparsity 下无法测试恢复性。策略：先在 20%/25% 快速 prune+eval（~1h），选\\n    post-prune accuracy 最合适的 sparsity 集中投入 GRPO（~15h），避免浪费 GPU 在错误 sparsity 上。35%+SFT\\n    warmup 留待 Phase 2。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v3\\n    role: negative_result\\n    result: Standard 0% / RASP 1% at 33% actual sparsity, per-layer floor working\\n      correctly\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-14 17:06 UTC\\n  summary: 20% sparsity 下 RASP 29% vs Standard 1%，Scenario B 确认，GRPO 双 GPU 并行恢复对比\\n  rationale: RASP 20% post-prune accuracy 29% vs Standard 20% 仅 1%（p<0.0001），MLP 总容量完全相同（74.5%），差异纯粹在剪枝分布。CKA\\n    overlap scoring 保护了 layer 16-22 推理关键层。落入 Scenario B（最强叙事）：RASP 不仅预测 recoverability，pruning\\n    本身就保护推理能力。下一步 GRPO 双 GPU 并行（cuda:0 RASP, cuda:1 Standard），验证 recovery 差异。25% eval\\n    继续跑完收集 sparsity 阈值数据。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v4\\n    role: primary\\n    result: RASP_20=29% vs Standard_20=1%, p<0.0001\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-14 17:37 UTC\\n  summary: Kill 270h GRPO runs，用 max_completion=1024 + 1 epoch + 2000 samples 重启，目标\\n    <10h 完成\\n  rationale: 当前 GRPO 配置 max_completion_length=4096 导致 173s/step、总计 270h，超过 EMNLP deadline。GSM8K\\n    的 R1 推理链通常 200-800 tokens，4096 严重浪费。MVP 只需证明 recovery 趋势（ρ ≥ 0.4），1 epoch + 2000\\n    samples 足够看到信号。Standard 模型 1% 起点大概率触发 RewardDesertCallback，本身就是\\\"不可恢复\\\"的证据。预估新配置\\n    ~625 steps × ~43s/step ≈ 7.5h。\\n  related_experiments:\\n  - exp_id: grpo_rasp_20\\n    role: kill_and_restart\\n    result: running_too_slow\\n  - exp_id: grpo_standard_20\\n    role: kill_and_restart\\n    result: running_too_slow\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-14 18:40 UTC\\n  summary: 正式更新 MVP 判定标准：从 per-group ρ ≥ 0.4 改为 model-level 显著性检验；扩大 eval 到 full GSM8K\\n    (1319 samples)\\n  rationale: 原 ρ ≥ 0.4 需要 per-head/per-group F(h) 与 recoverability 数据点（N≈92），但 v4\\n    实验是 model-level 对比（N=2），无法计算 Spearman ρ。Reviewer 建议改为：RASP-pruned model 在 matched\\n    sparsity + matched param count 下，post-prune accuracy 和/或 post-recovery accuracy\\n    显著优于 Standard-pruned model（p < 0.05）。post-prune 部分（29% vs 1%, p < 0.0001）已 pass。同时当前\\n    N=100 eval CI 太宽（±9pp），需扩到 full test set 1319 samples（CI ±2.4pp）。另：RewardDesertCallback\\n    在当前配置下不会提前终止（patience=500 steps = total steps），不影响实验但需修正论文叙事。\\n  related_experiments:\\n  - exp_id: grpo_rasp_20_fast\\n    role: recovery_test\\n    result: running\\n  - exp_id: grpo_standard_20_fast\\n    role: baseline\\n    result: running\\n  - exp_id: mvp_rasp_pipeline_v4\\n    role: pruning_eval\\n    result: post-prune 29% vs 1%\\n  depends_on:\\n  - D006\\n  - D007\\n- id: D009\\n  date: 2026-05-14 21:39 UTC\\n  summary: GRPO 1024-token 截断伪阴性：不接受 negative 结论，诊断性 eval + 准备 2048 重跑\\n  rationale: grpo_rasp_20_fast 和 grpo_standard_20_fast 全程 clipped_ratio=1.0，0 个 completion\\n    自然终止。DeepSeek-R1 的 think 推理链在 sampling (temp=0.7) 下远长于 greedy，剪枝后模型更冗长。1024 tokens\\n    不足以产出完整答案，导致 reward=0、grad_norm=0，GRPO 无学习信号。这是配置问题不是方法问题。需先做诊断性 eval（1024 tokens\\n    + temp=0.7）确认截断假说，再用 max_completion=2048 重跑 GRPO。\\n  related_experiments:\\n  - exp_id: grpo_rasp_20_fast\\n    role: recovery_test\\n    result: inconclusive (truncation artifact)\\n  - exp_id: grpo_standard_20_fast\\n    role: baseline\\n    result: inconclusive (truncation artifact)\\n  depends_on:\\n  - D007\\n  - D008\\n- id: D010\\n  date: 2026-05-14 21:40 UTC\\n  summary: 审批 Option A：max_completion_length=4096 重跑 GRPO 双实验，其余参数不变\\n  rationale: RASP 模型 post-prune 29% accuracy 证明它能解题，1024 截断是唯一阻碍。Option A 最快验证（~7h），失败再追加\\n    SFT warmup（Option B）。不需要同时调 lr/epochs 增加变量。2 GPU 空闲中，立即启动。\\n  related_experiments:\\n  - exp_id: grpo_rasp_20_fast\\n    role: predecessor\\n    result: inconclusive (truncation)\\n  - exp_id: grpo_standard_20_fast\\n    role: predecessor\\n    result: inconclusive (truncation)\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-14 22:56 UTC\\n  summary: 'D011: Kill standard GRPO 4096 (10步零梯度), 将GPU1转给RASP GRPO 4096立即启动'\\n  rationale: 'grpo_standard_20_4096 前10步: clipped_ratio=0.9938, grad_norm=0, completion_length=4089/4096,\\n    输出为重复数字无结构。Standard pruning 20%已摧毁模型生成连贯文本能力, GRPO无法恢复, 增加token长度无济于事。10步证据充分(与D009\\n    1024截断不同, 这次是能力丧失)。Kill后GPU1立即启动RASP GRPO 4096, 比等GPU0 baseline eval完成提前~2h。Standard\\n    10步数据保留为负对照证据。'\\n  related_experiments:\\n  - exp_id: grpo_standard_20_4096\\n    role: evidence\\n    result: 10步零梯度, clipped_ratio=0.99, 模型不可恢复\\n  - exp_id: grpo_rasp_20_4096\\n    role: next\\n    result: pending - MVP关键实验\\n  depends_on:\\n  - D010\\n  - D009\\n- id: D012\\n  date: 2026-05-14 22:56 UTC\\n  summary: 'D011: Kill grpo_standard_20_4096 early, start grpo_rasp_20_4096 on GPU1\\n    immediately'\\n  rationale: 10步数据确认Standard-pruned模型（1% accuracy）在4096 tokens下仍完全退化：clipped_ratio=0.9938,\\n    grad_norm=0, 输出为重复数字串。这不是截断问题而是模型本质退化，继续跑490步（~23h）不改变结论。Kill后释放GPU1立即启动RASP GRPO，比原计划（等GPU0\\n    baseline eval完成）提前~2h。Standard的失败本身是强力负对照：证明Standard pruning摧毁了GRPO恢复的前提条件。\\n  related_experiments:\\n  - exp_id: grpo_standard_20_4096\\n    role: negative_control\\n    result: 'confirmed unrecoverable at step 10: clipped_ratio=0.9938, grad_norm=0'\\n  - exp_id: grpo_rasp_20_4096\\n    role: mvp_critical\\n    result: pending launch on GPU1\\n  depends_on:\\n  - D009\\n  - D010\\n- id: D013\\n  date: 2026-05-14 23:33 UTC\\n  summary: 'D012: RASP GRPO 4096也零梯度, 根因是sampling下无EOS而非token长度. Kill后转SFT warmup→GRPO两阶段恢复'\\n  rationale: 'RASP模型greedy 29%但sampling(temp=0.7)下clipped_ratio=1.0/grad_norm=0/zero\\n    EOS. 剪枝破坏了概率分布导致sampling下无法收敛到EOS. GRPO依赖自主生成, 对严重剪枝模型先天不适用. SFT用teacher forcing可修复终止行为,\\n    然后GRPO在SFT基础上优化推理. 双GPU并行: RASP SFT + Standard SFT对照. SFT~2-3h, 比继续浪费24h GPU跑零梯度GRPO合理得多.\\n    Standard SFT预期仍然困难(1% accuracy残留能力极低), 将作为负对照.'\\n  related_experiments:\\n  - exp_id: grpo_rasp_20_4096\\n    role: evidence\\n    result: 10步零梯度, clipped_ratio=1.0, sampling下无EOS\\n  - exp_id: grpo_standard_20_4096\\n    role: evidence\\n    result: D011确认不可恢复\\n  depends_on:\\n  - D011\\n  - D010\\n- id: D014\\n  date: 2026-05-14 23:35 UTC\\n  summary: 'D014: MVP PASS — 接受 post-prune 29% vs 1% 作为充分证据，GRPO recovery 降为 Phase\\n    2'\\n  rationale: D008 MVP claim 允许 \\\"post-prune 和/或 post-recovery accuracy 显著优于 Standard\\\"。Post-prune\\n    RASP 29% vs Standard 1%（p<0.0001, matched params/sparsity）远超 p<0.05 门槛。GRPO 4096\\n    双模型均 100% 截断零梯度（D013），根因是 DeepSeek-R1 sampling+temp=0.7 推理链无 EOS，非假设失败。继续追加 token\\n    长度风险高且时间成本大（48h+）。SFT warmup→GRPO 作为 Phase 2 第一个实验继续推进，为 story 增色但不阻塞 MVP。EMNLP\\n    DDL 11 天，必须立即进入 research 阶段。\\n  related_experiments:\\n  - exp_id: grpo_rasp_20_4096\\n    role: evidence\\n    result: negative (truncation, but confirms RASP 5x reward vs Standard)\\n  - exp_id: grpo_standard_20_4096\\n    role: negative_control\\n    result: negative (killed D011)\\n  - exp_id: grpo_rasp_20_fast\\n    role: evidence\\n    result: inconclusive (D009 truncation)\\n  - exp_id: grpo_standard_20_fast\\n    role: negative_control\\n    result: inconclusive (D009 truncation)\\n  - exp_id: mvp_rasp_pipeline_v4\\n    role: primary\\n    result: RASP 29% vs Standard 1% post-prune\\n  depends_on:\\n  - D013\\n  - D010\\n  - D009\\n  - D008\\n- id: D015\\n  date: 2026-05-15 00:59 UTC\\n  summary: SFT 结果 Standard>RASP 不改变方向，立即启动 GRPO Stage 2 作为决定性实验\\n  rationale: SFT Standard 64% > RASP 57% 看似威胁核心假设，但：(1) SFT 是 Stage 1 warmup 不是核心测试；(2)\\n    Claim 3 本来就预测 SFT 和 GRPO 对剪枝策略的偏好不同——SFT 偏好 Standard 反而是 Claim 3 的证据；(3) 真正的决定性实验是\\n    GRPO Stage 2。如果 GRPO 也显示 Standard ≥ RASP 则需要 pivot，但在此之前不改变方向。两卡空闲，紧急启动 GRPO Stage\\n    2。\\n  related_experiments:\\n  - exp_id: sft_rasp_20\\n    role: evidence\\n    result: 57% accuracy on 100 samples\\n  - exp_id: sft_standard_20\\n    role: evidence\\n    result: 64% accuracy on 100 samples, exceeds RASP\\n  depends_on: []\\n- id: D016\\n  date: 2026-05-15 01:56 UTC\\n  summary: 'D016: Dream dream_20260514T233950 分析完成。Best=4/6, Median=3/6, Worst=3/6。5\\n    个确认行动项 + 3 个观察项。加入 plan_015(α ablation P0), plan_016(inference speedup P1), plan_017(unstructured\\n    baseline P1)，扩展 plan_006 到 5 seeds。'\\n  rationale: 三档一致的结构性问题：α ablation(Critical×3)、single model、no inference speedup、multi-seed不足、scope\\n    overclaim。两档一致：missing related work(FANG/FuncNet)、CKA justification、unstructured\\n    baseline、per-layer floor confound。数据依赖项(RASP vs GRASPrune ranking、CKA predictivity)等\\n    GRPO 结果决定。Dream best case 可达 Weak Accept，但需要上述修补。不降级 venue 目标。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20\\n    role: core\\n    result: RUNNING\\n  - exp_id: grpo_stage2_standard_20\\n    role: core\\n    result: RUNNING\\n  depends_on:\\n  - D015\\n- id: D017\\n  date: 2026-05-15 03:18 UTC\\n  summary: 'D017: Kill GRPO Stage 2 并以优化参数重启。max_completion_length 4096→1024, max_samples\\n    2000→1000。当前速度 38 天完成不可行（deadline 10 天），SFT 后 EOS 已修复使缩短 completion 安全。'\\n  rationale: GRPO Stage 2 每 step 1h51m，500 steps 需 38 天，远超 10 天 deadline。根因是 4096\\n    max_completion_length 的 generation 瓶颈。SFT warmup 后 EOS rate 99%、avg completion\\n    176 tokens，4096 是 SFT 前的防御性设置现已不需要。1024 提供 5.8x 平均长度的 headroom。max_samples 从 2000\\n    降到 1000 进一步缩短训练时间，1000 prompts 对 GRPO 足够。num_generations 需 Agent 确认当前值（W&B 显示\\n    4，Agent 说默认 8），如已是 4 则保持。预估加速到 ~2.4 天。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20\\n    role: target\\n    result: RUNNING - too slow\\n  - exp_id: grpo_stage2_standard_20\\n    role: target\\n    result: RUNNING - too slow\\n  depends_on:\\n  - D015\\n  - D016\\n- id: D018\\n  date: 2026-05-15 05:45 UTC\\n  summary: 'D018: Reviewer 发现 Redundancy Paradox 叙事逻辑矛盾 + GQA=0 + Claim 2 scope 限定。intro\\n    说\\\"保留高 overlap\\\"但公式是\\\"剪掉高 overlap\\\"。20% sparsity 下仅 MLP 组被剪(0/112 attention GQA groups)，Claim\\n    2 scope 限定为 MLP groups。'\\n  rationale: Reviewer 深度分析发现：(1) introduction.tex L17 与 method.tex L79 矛盾——intro 称\\n    RASP 保留高 overlap 结构，但公式 S(h)=I(h)×(1-F)^α 明确惩罚高 F（高 overlap → 低 S → 被剪）。method.tex\\n    正确。(2) CKA 数据证实 MLP overlap ∈[0.879,0.997]，(1-F)^α 压缩到 Attn 的 1/5~1/50，使全局排序下\\n    MLP 必然被优先剪。(3) Claim 2 说 F(h) predicts recoverability，但在 20% sparsity 下只有 MLP\\n    groups 验证了这一点。需修正 intro + scope 限定 Claim 2 + 论文诚实交代剪枝分布。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v2\\n    role: affected\\n    result: running\\n  - exp_id: grpo_stage2_standard_20_v2\\n    role: affected\\n    result: running\\n  depends_on:\\n  - D016\\n  - D017\\n- id: D019\\n  date: 2026-05-15 07:40 UTC\\n  summary: 'D019: Kill GRPO v2（双组 grad_norm=0 confirmed collapse），启动 v3：max_completion_length=2048\\n    + format_reward + β=0.01 + gradient_checkpointing。重跑 SFT Standard（checkpoint 已删）。'\\n  rationale: Step 30 数据独立验证 collapse：RASP grad_norm=0 + reward 停滞 0.0125，Standard\\n    grad_norm=0。继续 v2 浪费 ~24h GPU。v3 三项修改针对根因（reward signal 稀疏）：2048 token 给更多生成空间，format\\n    reward 提供中间梯度信号，β=0.01 防漂移。gradient_checkpointing 解决 OOM 风险。sft_standard_20 被磁盘清理删除，需重训\\n    ~40min。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v2\\n    role: killed\\n    result: collapse\\n  - exp_id: grpo_stage2_standard_20_v2\\n    role: killed\\n    result: collapse\\n  depends_on:\\n  - D017\\n- id: D020\\n  date: 2026-05-15 08:06 UTC\\n  summary: v2 全失败，合并 D019+Agent 诊断设计 v3 最终参数；拒绝 SFT-only fallback\\n  rationale: v2 双组 step 30 grad_norm=0 collapse，根因：(1) max_completion_length=1024\\n    导致 RASP 98% truncated，学习信号极弱；(2) sampling temp=0.7 下 SFT 模型退化为重复循环。v3 合并两路修复：D019\\n    的 2048/beta=0.01/dapo + Agent 的 temp 降低/repetition_penalty。拒绝 SFT-only story(Option\\n    C)——GRPO 未在公平条件下测试，结论 premature。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v2\\n    role: evidence\\n    result: 'negative: grad_norm=0 at step 30, 98% truncated'\\n  - exp_id: grpo_stage2_standard_20_v2\\n    role: evidence\\n    result: 'negative: grad_norm=0 at step 30, 73-82% truncated'\\n  depends_on: []\\n- id: D021\\n  date: 2026-05-15 08:48 UTC\\n  summary: 'D023: 核心数据可信度危机——紧急重新 eval post-prune 模型验证 29% vs 1%'\\n  rationale: α ablation 显示 α=0.0 (=Standard) 得到 30%，与原始 Standard 1% 矛盾 29pp。Reviewer\\n    假说：旧版 eval 脚本用 from_pretrained 加载剪枝模型导致权重 reinit→1% 是 artifact。如果成立，核心 claim 基础崩塌。优先级高于所有其他实验。\\n  related_experiments:\\n  - exp_id: mvp_rasp_pipeline_v4\\n    role: 原始 Standard 1% 数据来源\\n    result: 1% 可能是 eval bug artifact\\n  - exp_id: grpo_stage2_rasp_20_v3\\n    role: 基于核心 claim 的下游实验\\n    result: FAILED (ref_model crash)\\n  depends_on:\\n  - D020\\n  - D014\\n- id: D022\\n  date: 2026-05-15 09:22 UTC\\n  summary: 'D025: GRPO v4 ETA 120h 不可接受，减 max_completion_length 重启 + α=4.0 边际显著需紧急验证'\\n  rationale: GRPO v4 每步 29min×250=120h=5天，DDL 仅 10 天。不 kill 但需优化：max_completion_length\\n    2048→512（SFT 平均输出 180 tokens），预计 2-4x 加速。同时探索 vLLM 可行性。α=4.0 (40%) vs α=0.0 (30%)\\n    边际显著 p≈0.05，如果确认则 CKA 核心贡献成立（极端加权有效），但需 N=500+ 和 512 calibration 确认。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v4\\n    role: 120h ETA, 需优化重启\\n    result: step 1/250, 29min/step\\n  - exp_id: mvp_rasp_pipeline_v4\\n    role: α ablation 来源\\n    result: α=4.0 40% vs α=0.0 30%\\n  depends_on:\\n  - D023\\n- id: D023\\n  date: 2026-05-15 10:09 UTC\\n  summary: α ablation Phase A 暴露 importance formula confound 风险，暂缓 framing 调整等 Phase\\n    B + formula 验证\\n  rationale: α=0.0（纯 importance 无 CKA）post-prune 30% ≈ α=2.0 的 29%，而 Standard 仅 1%。28pp\\n    差距可能来自 importance scoring 实现差异而非 CKA。但 post-prune 不等于 post-recovery——Phase B SFT\\n    结果才是 recoverability claim 的决定性证据。同时派 Agent 验证两种 mode 的 importance formula 是否相同。在两项证据到齐前不调整\\n    framing。α=4.0（40%）作为 backup 主结果候选。\\n  related_experiments:\\n  - exp_id: alpha_ablation_phase_a\\n    role: evidence\\n    result: α=0.0:30%, α=0.5:25%, α=1.0:27%, α=2.0:29%, α=4.0:40% (post-prune)\\n  depends_on: []\\n- id: D024\\n  date: 2026-05-15 10:11 UTC\\n  summary: 'CRITICAL: D023 re-eval 显示 Standard post-prune ~32% 而非原始 1%，部署三路排查确定根因'\\n  rationale: D023 re-eval 中间结果 pruned_standard_20 准确率 32%（50/100 samples），与 α=0.0\\n    post-prune 30% 交叉验证一致。原始 1% 极可能是 eval bug（代码今天有更新，可能修复了 non-uniform MLP 加载）。如果确认，\\\"RASP\\n    29% vs Standard 1%\\\" 核心 claim 不成立。三路紧急排查：(1) eval 代码 git diff (2) westb 当前代码 re-eval\\n    原始模型 (3) re-eval pruned_rasp_20。暂不调整 framing，等排查结果 + Phase B SFT recovery 数据。\\n  related_experiments:\\n  - exp_id: D023\\n    role: trigger\\n    result: re-eval pruned_standard_20 中间结果 32% vs 原始 1%\\n  - exp_id: alpha_ablation_phase_a\\n    role: cross_validation\\n    result: α=0.0 post-prune 30% ≈ re-eval 32%\\n  depends_on:\\n  - D023\\n- id: D025\\n  date: 2026-05-15 11:02 UTC\\n  summary: 挂起 D006/D014 基于 \\\"29x advantage\\\" 的所有结论，等待 definitive re-eval 数据\\n  rationale: Reviewer 确认 pruned_standard_20 原始 1% accuracy 是 eval bug（max_new_tokens=10\\n    截断）。Definitive re-eval 中间结果 (50/100) 显示 standard accuracy ~28%，与 α=0.0 ablation\\n    (30%) 交叉验证一致。原始 RASP 29% 也用了同样有 bug 的代码，真实值未知。如果 RASP re-eval 也是 ~28-30%，\\\"RASP\\n    29% vs Standard 1%\\\" 核心 claim 完全不成立。所有基于该 advantage 的下游决策需挂起直到两个 definitive re-eval\\n    (N=100, max_new_tokens=4096, greedy) 全部完成。\\n  related_experiments:\\n  - exp_id: D023\\n    role: trigger\\n    result: 'intermediate: standard_20 accuracy ~28% at 50/100 samples'\\n  - exp_id: D006\\n    role: suspended\\n    result: conclusions based on buggy eval data\\n  - exp_id: D014\\n    role: suspended\\n    result: conclusions based on buggy eval data\\n  depends_on:\\n  - D006\\n  - D014\\n- id: D026\\n  date: 2026-05-15 11:04 UTC\\n  summary: 将 RASP definitive re-eval 部署到 westd GPU 0 并行执行，不等 westb Standard re-eval\\n    完成\\n  rationale: westd 双卡空闲是资源浪费。数据可信度危机需要尽快拿到 RASP 和 Standard 两个 definitive re-eval 结果来判断核心\\n    claim 是否成立。并行跑可节省 ~1h 等待时间。同时利用 westd GPU 1 恢复 α ablation Phase B 剩余训练。\\n  related_experiments:\\n  - exp_id: reeval_postprune_definitive\\n    role: primary\\n    result: Standard 中间结果 28%，RASP 待跑\\n  depends_on:\\n  - D023\\n- id: D027\\n  date: 2026-05-15 11:37 UTC\\n  summary: Post-prune 核心 claim 崩塌（RASP 31% vs Standard 27%, p>>0.05）。暂不 pivot，等 GRPO\\n    v5 决定性结果\\n  rationale: Definitive re-eval 证实原始 29x advantage 完全由 eval bug 造成。D006/D014/D015\\n    决策链数据基础失效。但 GRPO v5（step 50/250, ~5h）是唯一仍可能验证\\\"CKA-guided pruning 创造更好 recovery\\n    dynamics\\\"假设的实验。SFT 方向已否定（Standard 64% > RASP 57%）。Pivot 判据：|GRPO_RASP - GRPO_Standard|\\n    < 5pp → 全面 pivot；5-10pp → 降级 claim；>10pp → story 转为 recovery-pathway 假设。westd\\n    空闲卡派 GraSP baseline + α ablation 重验证，无论 pivot 与否都有价值。\\n  related_experiments:\\n  - exp_id: reeval_postprune_definitive\\n    role: definitive\\n    result: RASP 31% vs Standard 27%, 4pp 不显著\\n  - exp_id: grpo_stage2_rasp_20_v5\\n    role: decisive_pending\\n    result: step 50/250 运行中\\n  depends_on:\\n  - D023\\n  - D026\\n- id: D028\\n  date: 2026-05-15 12:40 UTC\\n  summary: 'Kill GRPO v5 (RASP+Standard)，切 v6: max_completion_length 512→1024'\\n  rationale: v5 训练崩溃：reward step 40 达峰 0.033 后归零，grad_norm 坍塌到 0.01，clipped_ratio\\n    93-97.5%。根因是 512 tokens 太短导致 R1 distill 模型无法完成推理链→无正确答案→无 reward→无梯度。Standard\\n    v5 参数相同会遇到同样问题。切 1024 tokens 平衡速度（~5 min/step vs v4 29 min/step）和信号质量。双卡同时起 RASP\\n    v6 + Standard v6 保持对照并行。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v5\\n    role: killed\\n    result: reward 归零, grad_norm 坍塞, clipped_ratio 97.5%\\n  - exp_id: grpo_stage2_standard_20_v5\\n    role: killed_before_signal\\n    result: 参数相同会遇同样问题\\n  depends_on:\\n  - D027\\n- id: D029\\n  date: 2026-05-15 13:46 UTC\\n  summary: SFT recovery 阶段 Standard 优于 RASP/α=4.0，核心假设在 SFT 层面也未得到支持\\n  rationale: 'Post-SFT: Standard 64% > α=4.0 62% > RASP 57%。Recovery Δ: Standard +37pp\\n    > RASP +26pp > α=4.0 +22pp。Standard 起点最低但恢复最多，与\\\"RASP 保留更可恢复结构\\\"叙事矛盾。Post-prune\\n    和 Post-SFT 两个阶段均未支持核心假设。GRPO v6 对照实验（westb 双卡运行中，ETA ~21h）是最后的验证机会——RL 训练可能展现与\\n    SFT 不同的 recovery dynamics。若 GRPO 也无差异，项目需根本性 pivot。'\\n  related_experiments:\\n  - exp_id: sft_alpha4_0_westd\\n    role: evidence\\n    result: Post-SFT 62%, recovery +22pp\\n  - exp_id: sft_standard_20_retrain\\n    role: evidence\\n    result: Post-SFT 64%, recovery +37pp\\n  - exp_id: grpo_stage2_rasp_20_v6\\n    role: decisive_pending\\n    result: running\\n  - exp_id: grpo_stage2_standard_20_v6\\n    role: decisive_pending\\n    result: running\\n  depends_on:\\n  - D027\\n  - D028\\n- id: D030\\n  date: 2026-05-15 14:02 UTC\\n  summary: 'GRPO v6 双卡 OOM 崩溃(step 8)，切 v7: 8-bit optimizer + 100 steps 抢时间'\\n  rationale: v6 在 step 8 首次分配 full optimizer state 时 OOM（model+ref_model+optimizer\\n    > 95GB）。用户告知只剩几小时，v7 用 AdamW8bit 节省 ~50% optimizer 显存，steps 缩减到 100（~3.5h）以在时间窗口内出结果。这是决定性实验，必须在服务器到期前完成。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v6\\n    role: predecessor\\n    result: OOM step 8\\n  - exp_id: grpo_stage2_standard_20_v6\\n    role: predecessor\\n    result: OOM step 8\\n  depends_on:\\n  - D028\\n- id: D031\\n  date: 2026-05-15 14:04 UTC\\n  summary: 'GRPO v6 OOM at step 8, 切 v7: 8-bit AdamW optimizer + 100 steps (~3.5h)'\\n  rationale: v6 在 step 8 optimizer state 分配时 OOM 崩溃（max_completion_length=1024 的 KV\\n    cache + Adam FP32 states 超出 ~98GB VRAM）。v7 改用 AdamW8bit（bitsandbytes）减少 optimizer\\n    memory ~75%，steps 从 250 缩到 100——v5 在 step 40-80 已展现完整 learning/collapse 曲线，100\\n    steps 足以判断 RASP vs Standard 是否有差异。~3.5h 完成时间适配 deadline 压力。其余参数不变：max_completion_length=1024,\\n    beta=0.01, temp=0.4, rep_penalty=1.15, format_reward=0.1, gradient_checkpointing=True。\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v6\\n    role: OOM_failure\\n    result: OOM at step 8\\n  - exp_id: grpo_stage2_standard_20_v6\\n    role: OOM_failure\\n    result: OOM at step 8\\n  depends_on:\\n  - D028\\n- id: D032\\n  date: 2026-05-15 14:31 UTC\\n  summary: 'GRPO v7 双组崩溃(磁盘满+静默死亡)，v8 修复: HF cache 迁移数据盘 + GPU 映射修正 + 顺序启动'\\n  rationale: 'v7 Standard 因 HF datasets cache 写入根分区(30GB)导致瞬时磁盘满崩溃；RASP v7 静默死亡(疑同根因)。修复:\\n    (1) HF_DATASETS_CACHE/HF_HOME 指向 /root/autodl-tmp/.hf_cache 避免根分区写入 (2) Standard\\n    GPU 映射从 --gpu 1 改为 CUDA_VISIBLE_DEVICES=1 + --gpu 0 (3) 顺序启动确认稳定性。GRPO v1-v7 连续\\n    7 版失败均为工程问题(截断/collapse/OOM/磁盘满)而非算法问题，核心假设验证路径不变。'\\n  related_experiments:\\n  - exp_id: grpo_stage2_rasp_20_v7\\n    role: failed\\n    result: silent death, no logs\\n  - exp_id: grpo_stage2_standard_20_v7\\n    role: failed\\n    result: No space left on device at dataset loading\\n  depends_on:\\n  - D031\\n\", \"total_chars\": 21535, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b2857b4-87bc-42f7-bf4a-5fbd1986045f",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "ec7748d0-f889-40b3-8d31-6f33ae45c21f",
  "sourceToolAssistantUUID": "0b2857b4-87bc-42f7-bf4a-5fbd1986045f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-15T14:52:37.970Z_

Now let me look at the actual paper and experiment artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec7748d0-f889-40b3-8d31-6f33ae45c21f",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YWcvQNXJHZPMGERoHz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33ccbbb7-15a8-4988-aa8c-91c702f579a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018PJ321UV69LapgzsivwzY6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14113,
      "cache_read_input_tokens": 25397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14113,
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

_source line 19 · 2026-05-15T14:52:39.368Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UbW17XAAsHtvXgHcH2rNai`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33ccbbb7-15a8-4988-aa8c-91c702f579a3",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YWcvQNXJHZPMGERoHz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07227576-c797-40ed-946c-00fc97ed1713",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018PJ321UV69LapgzsivwzY6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14113,
      "cache_read_input_tokens": 25397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14113,
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

_source line 20 · 2026-05-15T14:52:39.390Z_

<details><summary>↩ Tool result · `toolu_01UbW17XAAsHtvXgHcH2rNai`</summary>

```text
artifacts/dream_reports/dream_20260514T233950/best/paper.tex
artifacts/dream_reports/dream_20260514T233950/median/paper.tex
artifacts/dream_reports/dream_20260514T233950/worst/paper.tex
artifacts/_project/paper/table1_postprune.tex
artifacts/_project/paper/table2_recovery.tex
artifacts/tables/table2_recovery.tex
paper/backup/experiments.tex
paper/backup/introduction.tex
paper/backup/method.tex
paper/backup/related_work.tex
paper/abstract.tex
paper/conclusion.tex
paper/appendix.tex
artifacts/_project/paper/table3_alpha.tex
paper/method.tex
artifacts/_project/paper/method.tex
paper/related_work.tex
artifacts/_project/paper/related_work_3d75d5.tex
artifacts/_project/paper/related_work.tex
docs/paper/method.tex
docs/paper/main.tex
docs/paper/appendix.tex
artifacts/_project/paper/introduction_4ad0ba.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/experiments.tex
paper/main.tex
paper/tables/table2_recovery.tex
paper/limitations.tex
artifacts/_project/paper/limitations.tex
docs/paper/related_work.tex
paper/introduction.tex
artifacts/tables/table1_postprune.tex
paper/tables/table1_postprune.tex
paper/experiments.tex
artifacts/tables/table3_alpha.tex
paper/tables/table3_alpha.tex
docs/paper/introduction.tex
docs/paper/abstract.tex
docs/paper/conclusion.tex
docs/paper/experiments.tex
docs/paper/limitations.tex
artifacts/dream_reports/dream_20260515T140651/best/paper.tex
artifacts/dream_reports/dream_20260515T140651/median/paper.tex
artifacts/dream_reports/dream_20260515T140651/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07227576-c797-40ed-946c-00fc97ed1713",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "e4e8ed14-f2db-4ccd-b1f2-256d40510f73",
  "sourceToolAssistantUUID": "07227576-c797-40ed-946c-00fc97ed1713",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T14:52:40.341Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01GmqffyJvkmJUTwph7TKZzw`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4e8ed14-f2db-4ccd-b1f2-256d40510f73",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YWcvQNXJHZPMGERoHz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc2ed32f-427e-4020-a523-b40f16dbd0ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018PJ321UV69LapgzsivwzY6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14113,
      "cache_read_input_tokens": 25397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14113,
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

_source line 22 · 2026-05-15T14:52:40.352Z_

<details><summary>↩ Tool result · `toolu_01GmqffyJvkmJUTwph7TKZzw`</summary>

```text
src/importance_score.py
src/rasp_scoring.py
src/prune.py
src/train_grpo.py
src/eval_gsm8k.py
src/correlation_analysis.py
src/cka_overlap.py
artifacts/correlation_analysis.py
src/grasp_scoring.py
src/run_cka_reliability.py
src/model_utils.py
src/convert_graspune_to_hf.py
artifacts/plot_cka_figures.py
artifacts/_project/intermediate/plot_fig1_pipeline.py
artifacts/plot_fig1_pipeline.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc2ed32f-427e-4020-a523-b40f16dbd0ec",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "6a59ae72-21d9-4819-bd38-a3543571a7df",
  "sourceToolAssistantUUID": "fc2ed32f-427e-4020-a523-b40f16dbd0ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T14:52:41.202Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015uUkMUpPM4gP7EfTZ4DqkN`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a59ae72-21d9-4819-bd38-a3543571a7df",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YWcvQNXJHZPMGERoHz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1d2e579-19eb-4780-8c0c-efffdf9cb418",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018PJ321UV69LapgzsivwzY6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14113,
      "cache_read_input_tokens": 25397,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14113
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 25397,
          "cache_creation_input_tokens": 14113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14113,
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

_source line 24 · 2026-05-15T14:52:41.212Z_

<details><summary>↩ Tool result · `toolu_015uUkMUpPM4gP7EfTZ4DqkN`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'recovery_aware_struct_prune'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1d2e579-19eb-4780-8c0c-efffdf9cb418",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "8ecb96e5-53d9-4f2e-b5f4-ca595cfe4a27",
  "sourceToolAssistantUUID": "d1d2e579-19eb-4780-8c0c-efffdf9cb418",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T14:52:44.252Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NfqZrWuRtbVaMR8228L1fY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ecb96e5-53d9-4f2e-b5f4-ca595cfe4a27",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YX5y6eGLFRhUQJccge",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dcaaff9f-3336-4e99-bfd5-2b88a30bd544",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mk5yGDh8RSYrKchUgheUTi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1170,
      "cache_read_input_tokens": 39510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1170,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 26 · 2026-05-15T14:52:44.259Z_

<details><summary>↩ Tool result · `toolu_01NfqZrWuRtbVaMR8228L1fY`</summary>

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
11	\usepackage{graphicx}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{booktabs}
15	\usepackage{siunitx}
16	\usepackage{algorithm}
17	\usepackage[noend]{algpseudocode}
18	\usepackage{enumitem}
19	\usepackage{xcolor}
20	\usepackage{hyperref}
21	
22	\newcommand{\rasp}{\textsc{Rasp}}
23	
24	\title{Recovery-Aware Structured Pruning for Reasoning Language Models}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\begin{abstract}
32	\input{abstract}
33	\end{abstract}
34	
35	\input{introduction}
36	\input{related_work}
37	\input{method}
38	\input{experiments}
39	\input{conclusion}
40	
41	\section*{Limitations}
42	\input{limitations}
43	
44	\bibliography{references}
45	\bibliographystyle{acl_natbib}
46	
47	\appendix
48	\input{appendix}
49	
50	\end{document}
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dcaaff9f-3336-4e99-bfd5-2b88a30bd544",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "bea04312-9d5f-4ee3-89c0-40fee758d25a",
  "sourceToolAssistantUUID": "dcaaff9f-3336-4e99-bfd5-2b88a30bd544",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T14:52:44.724Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XrkcXTukW4GUbhqorXPcyP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bea04312-9d5f-4ee3-89c0-40fee758d25a",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YX5y6eGLFRhUQJccge",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d738926-2f6f-4aa5-ae30-dcd345293604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mk5yGDh8RSYrKchUgheUTi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1170,
      "cache_read_input_tokens": 39510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1170,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 28 · 2026-05-15T14:52:44.729Z_

<details><summary>↩ Tool result · `toolu_01XrkcXTukW4GUbhqorXPcyP`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Large language models trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong performance on mathematical and logical reasoning~\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.
5	Structured pruning---removing entire attention heads or MLP channels---offers a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\citep{llmpruner2023,graspprune2026}.
6	However, structured pruning at moderate sparsity severely degrades reasoning ability, necessitating a post-pruning recovery stage.
7	\citet{selfhealing2025} show that RLVR-based recovery substantially outperforms SFT-based recovery for pruned reasoning models, establishing RLVR as the preferred recovery paradigm.
8	
9	Despite this, current approaches treat pruning and recovery as independent steps: pruning methods optimize for immediate post-pruning accuracy~\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\citep{selfhealing2025,paser2025}.
10	No prior work has studied whether the \emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning---or whether this interaction differs from SFT-based recovery.
11	This gap is consequential because RLVR and SFT impose fundamentally different functional demands on the retained architecture: \citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation.
12	The optimal set of structures to retain should therefore depend on the recovery paradigm.
13	
14	We hypothesize that \emph{functional overlap}---the degree to which a structure's computation is redundant with its within-layer peers---positively predicts RLVR recoverability.
15	If a pruned structure has high overlap with retained structures, RLVR can absorb its function through global policy optimization over the remaining architecture.
16	Conversely, structures with unique, non-redundant computations are difficult to recover once removed.
17	This yields what we term the \textbf{Redundancy Paradox}: counterintuitively, the structures most valuable to retain for post-RLVR recovery are not the most important ones, but the most \emph{functionally unique} ones.
18	Recovery-aware pruning therefore \emph{preferentially removes} important-but-redundant structures---whose high overlap means RLVR can redistribute their function across retained peers---while protecting functionally unique structures that, once removed, leave an irrecoverable gap.
19	Standard importance-only pruning, by contrast, protects high-importance structures regardless of redundancy, inadvertently removing unique structures whose function cannot be recovered.
20	
21	We propose \textbf{Recovery-Aware Structured Pruning (\rasp{})}, a three-stage framework that incorporates recoverability into the pruning decision.
22	In Stage~1, \rasp{} computes for each structure both a gradient-based importance score and a functional overlap score via intra-layer Centered Kernel Alignment (CKA;~\citealp{kornblith2019cka}).
23	In Stage~2, these are combined into a recovery-aware score $S(h) = I(h) \times (1 - F(h))^\alpha$ that protects structures which are both important \emph{and} functionally unique, while allowing removal of important-but-redundant structures whose function RLVR can redistribute.
24	In Stage~3, the pruned model undergoes a brief SFT warmup to restore generation competence, followed by GRPO-based RLVR recovery~\citep{shao2024grpo} to restore reasoning ability.
25	Unlike prior CKA-based pruning that uses inter-layer similarity for depth pruning~\citep{mpruner2024,lachance2024cka}, \rasp{} uses \emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability---a finer granularity optimizing for a fundamentally different objective.
26	
27	We evaluate \rasp{} on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} at 20\% structured sparsity.
28	At matched sparsity, \rasp{}-pruned models retain 29\% GSM8K~\citep{cobbe2021gsm8k} accuracy immediately after pruning, compared to 1\% for importance-only pruning ($N{=}100$, $p{<}0.0001$)---a 28-percentage-point advantage attributable to the recovery-aware scoring criterion.
29	After SFT warmup, both pruning strategies recover substantially (57--64\%), with detailed comparison deferred to \S\ref{sec:experiments}.
30	[TBD: GRPO results]
31	
32	Our contributions are:
33	\begin{enumerate}[nosep,leftmargin=*]
34	    \item We identify the \emph{Redundancy Paradox}---that functional redundancy enables RLVR to recover the function of removed structures, making important-but-redundant structures safely removable while functionally unique structures become critical to retain---and formalize it through intra-layer CKA-based functional overlap scoring.
35	    \item We propose \rasp{}, a recovery-aware pruning framework that integrates functional overlap into structural pruning decisions, achieving 29\% post-prune GSM8K accuracy versus 1\% for importance-only pruning at matched 20\% sparsity on DeepSeek-R1-Distill-Qwen-7B.
36	    \item [TBD: GRPO recovery results---contribution demonstrating that \rasp{}'s post-prune advantage translates to superior post-RLVR reasoning performance.]
37	    \item We present preliminary evidence that the optimal pruning strategy may be conditioned on the recovery paradigm~\citep{frankle2019lth}, supporting the notion of \emph{paradigm-conditioned prunability} [TBD: pending GRPO confirmation and statistical validation].
38	\end{enumerate}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d738926-2f6f-4aa5-ae30-dcd345293604",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "5971fdfb-8962-404c-8d06-d386d2655b2d",
  "sourceToolAssistantUUID": "6d738926-2f6f-4aa5-ae30-dcd345293604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T14:52:44.962Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CS2xQ3wvSw8yj8xEE5GnXT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5971fdfb-8962-404c-8d06-d386d2655b2d",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YX5y6eGLFRhUQJccge",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ab91a9f-b66a-44cd-ae4d-beb6a6551e2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mk5yGDh8RSYrKchUgheUTi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1170,
      "cache_read_input_tokens": 39510,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1170
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 39510,
          "cache_creation_input_tokens": 1170,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1170,
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

_source line 30 · 2026-05-15T14:52:44.966Z_

<details><summary>↩ Tool result · `toolu_01CS2xQ3wvSw8yj8xEE5GnXT`</summary>

```text
1	\section{Method: Recovery-Aware Structured Pruning}
2	\label{sec:method}
3	
4	We propose \textbf{Recovery-Aware Structured Pruning (\rasp{})}, a three-stage framework that optimizes structural pruning decisions for post-RLVR recoverability rather than immediate accuracy preservation.
5	The core insight is that structures with high functional overlap---those whose computations are redundant with other retained structures---are more recoverable under RLVR, because reinforcement learning can redistribute their function through global exploration~\citep{rlsqueezes2026}.
6	
7	\subsection{Preliminaries and Notation}
8	\label{sec:prelim}
9	
10	\paragraph{Structured pruning.}
11	Given a pretrained transformer $\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units---attention heads or MLP channels---to reduce model size while maintaining hardware-friendly dense computation.
12	We denote the set of prunable structures as $\mathcal{H} = \{h_1, h_2, \ldots, h_N\}$.
13	
14	\paragraph{Grouped Query Attention (GQA).}
15	In GQA architectures~\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads, with each KV head serving a group of $G = n_Q / n_{KV}$ query heads.
16	For DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$), $G = 7$, yielding 4 GQA groups per layer.
17	We treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit, since removing a KV head necessitates removing all associated Q heads.
18	
19	\paragraph{RLVR and GRPO.}
20	Reinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.
21	We use Group Relative Policy Optimization (GRPO;~\citealp{shao2024grpo}) as the recovery algorithm, following~\citet{selfhealing2025}.
22	
23	\subsection{Stage 1: Reasoning-Trace Structural Analysis}
24	\label{sec:stage1}
25	
26	\rasp{} computes two complementary scores per structure: \emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \emph{functional overlap} $F(h)$ measuring the degree to which its function is recoverable from other structures.
27	
28	\paragraph{Calibration data.}
29	We compute importance and overlap scores on chain-of-thought reasoning data from GSM8K~\citep{cobbe2021gsm8k} training examples, using question--answer pairs as calibration traces.
30	Given a calibration set $\mathcal{D}_\text{cal} = \{(x_j, y_j)\}_{j=1}^{M}$, we compute activations and gradients on the concatenated sequences $(x_j, y_j)$.
31	This ensures importance scores reflect the model's behavior on representative reasoning tasks.
32	
33	\paragraph{Structural importance.}
34	For each structure $h$, we compute importance $I(h)$ via first-order Taylor expansion on the reasoning trace loss:
35	\begin{equation}
36	    I(h) = \left| \sum_{(x,y) \in \mathcal{D}_\text{cal}} \mathbf{a}_h(x, y)^\top \frac{\partial \mathcal{L}(x, y)}{\partial \mathbf{a}_h} \right|,
37	    \label{eq:importance}
38	\end{equation}
39	where $\mathbf{a}_h$ denotes the activation of structure $h$ and $\mathcal{L}$ is the language modeling loss over the reasoning trace.
40	For a GQA group $g$ containing Q heads $\{q_1, \ldots, q_G\}$ and KV head $k$, we aggregate: $I(g) = \sum_{i=1}^{G} I(q_i) + I(k)$.
41	
42	\paragraph{Functional overlap via CKA.}
43	We measure functional overlap using linear Centered Kernel Alignment (CKA;~\citealp{kornblith2019cka}), which quantifies similarity between two sets of representations invariant to invertible linear transformations.
44	Given activation matrices $\mathbf{X}, \mathbf{Y} \in \mathbb{R}^{n \times d}$ collected over $n$ calibration examples, linear CKA is:
45	\begin{equation}
46	    \text{CKA}(\mathbf{X}, \mathbf{Y}) = \frac{\text{HSIC}(\mathbf{X}, \mathbf{Y})}{\sqrt{\text{HSIC}(\mathbf{X}, \mathbf{X}) \cdot \text{HSIC}(\mathbf{Y}, \mathbf{Y})}},
47	    \label{eq:cka}
48	\end{equation}
49	where $\text{HSIC}(\mathbf{X}, \mathbf{Y}) = \frac{1}{(n-1)^2} \operatorname{tr}(\mathbf{K} \mathbf{H} \mathbf{L} \mathbf{H})$, with $\mathbf{K} = \mathbf{X}\mathbf{X}^\top$, $\mathbf{L} = \mathbf{Y}\mathbf{Y}^\top$, and $\mathbf{H} = \mathbf{I}_n - \frac{1}{n}\mathbf{1}\mathbf{1}^\top$.
50	
51	For a GQA group $g_i$ in layer $\ell$, we form its representation by concatenating its constituent Q head activations: $\mathbf{X}_{g_i} = [\mathbf{a}_{q_1}; \ldots; \mathbf{a}_{q_G}] \in \mathbb{R}^{n \times Gd_h}$.
52	The functional overlap of $g_i$ is the mean pairwise CKA with other groups in the same layer:
53	\begin{equation}
54	    F(g_i) = \frac{1}{|\mathcal{G}_\ell| - 1} \sum_{\substack{g_j \in \mathcal{G}_\ell \\ j \neq i}} \text{CKA}(\mathbf{X}_{g_i}, \mathbf{X}_{g_j}),
55	    \label{eq:overlap}
56	\end{equation}
57	where $\mathcal{G}_\ell$ is the set of GQA groups in layer $\ell$.
58	Unlike prior work that uses inter-layer CKA to identify globally redundant layers for depth pruning~\citep{mpruner2024,lachance2024cka}, \rasp{} uses \emph{intra-layer} CKA between individual GQA groups to predict per-structure recoverability---a fundamentally different granularity and objective.
59	
60	\paragraph{MLP channel group overlap.}
61	We apply the same intra-layer CKA overlap to MLP channel groups.
62	Each MLP intermediate dimension is partitioned into equal-sized groups; for group $m_i$ in layer $\ell$, we compute $F(m_i) = \frac{1}{|\mathcal{M}_\ell| - 1} \sum_{m_j \in \mathcal{M}_\ell, j \neq i} \text{CKA}(\mathbf{X}_{m_i}, \mathbf{X}_{m_j})$, where $\mathcal{M}_\ell$ is the set of MLP groups in layer $\ell$.
63	Attention GQA groups and MLP channel groups are then scored and ranked jointly in Stage~2.
64	
65	\subsection{Stage 2: Recovery-Aware Scoring}
66	\label{sec:stage2}
67	
68	The recovery-aware score combines importance and functional overlap:
69	\begin{equation}
70	    S(h) = I(h) \times \big(1 - F(h)\big)^\alpha,
71	    \label{eq:score}
72	\end{equation}
73	where $\alpha \ge 0$ controls the strength of the recoverability penalty ($\alpha{=}0$ reduces to standard importance-only pruning).
74	Structures with the lowest $S(h)$ are pruned up to the target sparsity ratio.
75	
76	The scoring captures three regimes:
77	\begin{itemize}[nosep,leftmargin=*]
78	    \item \textbf{High $I$, low $F$} (irreplaceable scaffolding): No other structure can assume its function. High $S$ $\rightarrow$ \emph{protected}.
79	    \item \textbf{High $I$, high $F$} (redundant but important): RLVR can redistribute its function via global exploration. Low $S$ $\rightarrow$ \emph{pruned preferentially}.
80	    \item \textbf{Low $I$} (unimportant): Pruned regardless of overlap.
81	\end{itemize}
82	
83	The key distinction from standard pruning---which ranks solely by $I(h)$---is that \rasp{} additionally down-weights protection of structures whose function overlaps with retained structures.
84	This is motivated by the finding that RLVR recovers through global exploration and path compression~\citep{rlsqueezes2026}, making high-overlap structures more amenable to functional redistribution than unique structures of equivalent importance.
85	
86	\paragraph{Per-layer capacity floor.}
87	Global ranking by $S(h)$ can concentrate pruning in layers where many structures have high overlap, collapsing that layer's representational capacity.
88	To prevent this, we enforce a per-layer capacity floor: each layer must retain at least 40\% of its MLP channel groups after pruning.
89	For DeepSeek-R1-Distill-Qwen-7B, this requires ${\ge}12$ of 28 MLP groups per layer.
90	During structure selection, if removing a candidate would violate this constraint, it is skipped in favor of the next lowest-scoring structure.
91	This constraint adds negligible overhead to the scoring procedure but prevents representational collapse in individual layers---a failure mode we observed when unconstrained global ranking was applied at 20\% sparsity.
92	
93	Attention GQA groups and MLP channel groups are scored jointly and ranked in a unified list, enabling cross-component pruning decisions subject to the per-layer floor.
94	Algorithm~\ref{alg:rasp} summarizes the complete pipeline.
95	
96	\subsection{Stage 3: Two-Stage Recovery}
97	\label{sec:stage3}
98	
99	After pruning, we recover reasoning ability through two stages: supervised finetuning (SFT) warmup followed by GRPO-based RLVR.
100	
101	\paragraph{Motivation for two-stage recovery.}
102	Directly applying GRPO to a pruned model fails.
103	Structured pruning disrupts the model's ability to generate end-of-sequence (EOS) tokens: in sampling mode, pruned models produce repetitive digit loops without termination, yielding sequences that are truncated at the maximum length.
104	Since GRPO computes rewards only from completed generations, this EOS collapse means no valid completions are produced, the clipped ratio reaches 1.0, and gradient norms drop to zero---making direct RLVR recovery impossible.
105	
106	\paragraph{Stage 3a: SFT warmup.}
107	We first apply a short SFT phase on reasoning demonstrations to restore two capabilities destroyed by pruning: (1) EOS token generation, ensuring the model can terminate sequences, and (2) basic format compliance, so that outputs follow the expected answer extraction pattern.
108	SFT warmup uses teacher-forced training on chain-of-thought traces, which does not require the model to produce complete generations and thus bypasses the EOS collapse problem.
109	This stage is intentionally brief---its purpose is to restore the minimal generation competence needed for GRPO, not to recover full reasoning ability.
110	
111	\paragraph{Stage 3b: GRPO recovery.}
112	With generation competence restored, we apply GRPO-based RLVR on mathematical reasoning data to recover the pruned model's reasoning ability.
113	The reward is binary: $r = 1$ if the model's final answer matches the ground truth, $r = 0$ otherwise.
114	RLVR is preferred over extended SFT for reasoning recovery because of their fundamentally different training dynamics: \citet{rlsqueezes2026} show that RLVR \emph{compresses} incorrect reasoning trajectories while SFT \emph{expands} correct ones.
115	For a pruned model, RLVR can globally explore and redistribute functionality across remaining structures, while SFT is limited to imitating fixed trajectories through a reduced architecture.
116	Structures with high functional overlap $F(h)$ are precisely those whose function can be absorbed by similar retained structures through RLVR's global optimization---the theoretical basis for \rasp{}'s scoring criterion.
117	
118	\begin{algorithm}[t]
119	\caption{Recovery-Aware Structured Pruning (\rasp{})}
120	\label{alg:rasp}
121	\begin{algorithmic}[1]
122	\Require Model $\mathcal{M}$, calibration problems $\mathcal{D}_\text{cal}$, target sparsity $s$, overlap weight $\alpha$, SFT data $\mathcal{D}_\text{sft}$, RLVR data $\mathcal{D}_\text{rlvr}$, layer floor $\tau$
123	\Ensure Pruned and recovered model $\mathcal{M}'$
124	\Statex \textit{\% Stage 1: Reasoning-Trace Structural Analysis}
125	\State Load calibration pairs $\{(x_j, y_j)\}$ from $\mathcal{D}_\text{cal}$
126	\For{each structure $h \in \mathcal{H}$}
127	    \State Compute $I(h)$ via Eq.~\eqref{eq:importance}
128	    \State Collect activations $\mathbf{X}_h$
129	\EndFor
130	\For{each layer $\ell = 1, \ldots, L$}
131	    \For{each group $g_i \in \mathcal{G}_\ell$}
132	        \State $F(g_i) \gets \frac{1}{|\mathcal{G}_\ell|-1} \sum_{j \neq i} \text{CKA}(\mathbf{X}_{g_i}, \mathbf{X}_{g_j})$
133	    \EndFor
134	\EndFor
135	\Statex \textit{\% Stage 2: Recovery-Aware Scoring}
136	\For{each structure $h \in \mathcal{H}$}
137	    \State $S(h) \gets I(h) \times (1 - F(h))^\alpha$
138	\EndFor
139	\State Sort $\mathcal{H}$ by $S(h)$ ascending
140	\State $\mathcal{P} \gets \emptyset$
141	\For{each $h$ in sorted $\mathcal{H}$}
142	    \If{layer($h$) retains $< \tau$ fraction after adding $h$ to $\mathcal{P}$}
143	        \State \textbf{continue}
144	    \EndIf
145	    \State $\mathcal{P} \gets \mathcal{P} \cup \{h\}$
146	    \If{$\sum_{h' \in \mathcal{P}} \text{params}(h') \ge s \cdot |\theta|$}
147	        \State \textbf{break}
148	    \EndIf
149	\EndFor
150	\State $\mathcal{M}_\text{pruned} \gets \text{Remove}(\mathcal{M}, \mathcal{P})$
151	\Statex \textit{\% Stage 3: Two-Stage Recovery}
152	\State $\mathcal{M}_\text{warm} \gets \text{SFT}(\mathcal{M}_\text{pruned}, \mathcal{D}_\text{sft})$ \hfill $\triangleright$ restore EOS \& format
153	\State $\mathcal{M}' \gets \text{GRPO}(\mathcal{M}_\text{warm}, \mathcal{D}_\text{rlvr})$ \hfill $\triangleright$ restore reasoning
154	\State \Return $\mathcal{M}'$
155	\end{algorithmic}
156	\end{algorithm}
157	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ab91a9f-b66a-44cd-ae4d-beb6a6551e2b",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "6b65b2cf-2b2d-4b33-9da5-27be5b30321b",
  "sourceToolAssistantUUID": "9ab91a9f-b66a-44cd-ae4d-beb6a6551e2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T14:52:49.477Z_

<details open><summary>🔧 Tool call — Read · `toolu_019eLEGNK5eWjiYnSFw4vuax`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b65b2cf-2b2d-4b33-9da5-27be5b30321b",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YXMzkpgqnLxX8vEkRM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0f72ada-3a65-4a39-b804-02f646cb5cbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zyh4XjNLdscsJi2fQFJvX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6756,
      "cache_read_input_tokens": 40680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6756,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 32 · 2026-05-15T14:52:49.489Z_

<details><summary>↩ Tool result · `toolu_019eLEGNK5eWjiYnSFw4vuax`</summary>

```text
1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	\subsection{Experimental Setup}
6	\label{sec:exp_setup}
7	
8	\paragraph{Base model.}
9	We evaluate \rasp{} on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\citep{qwen2.5} with 28 transformer layers.
10	The model uses Grouped Query Attention (GQA;~\citealp{ainslie2023gqa}) with 28 query heads and 4 key-value heads per layer (group size $G{=}7$), and an MLP intermediate dimension of 18{,}944.
11	As a reasoning-distilled model whose chain-of-thought capabilities originate from reinforcement learning, it provides a direct testbed for studying how structural pruning interacts with RLVR-based recovery.
12	
13	\paragraph{Evaluation.}
14	We evaluate on GSM8K~\citep{cobbe2021gsm8k}, a benchmark of 1{,}319 grade-school math problems requiring multi-step arithmetic reasoning.
15	We report exact-match accuracy: the final numerical answer is extracted from the model's generation and compared against the ground truth.
16	For rapid iteration during development, we use a fixed 100-problem subset ($N{=}100$); final results use the full test set ($N{=}1{,}319$).
17	We define recovery $\Delta$ as the accuracy gain from post-prune to post-recovery, capturing how much reasoning ability the recovery pipeline restores independent of initial pruning damage.
18	
19	\paragraph{Hardware.}
20	All experiments run on a single node with 2$\times$ NVIDIA RTX PRO 6000 GPUs (94\,GB VRAM each).
21	The two pruning variants (Standard and \rasp{}) are trained in parallel on separate GPUs to ensure identical wall-clock conditions.
22	
23	\subsection{Pruning Configuration}
24	\label{sec:pruning_config}
25	
26	\paragraph{Sparsity and granularity.}
27	We apply 20\% structured sparsity by scoring and ranking both attention GQA groups (each comprising 1 KV head and 7 query heads) and MLP channel groups in a unified importance list; at 20\% sparsity, the global ranking preferentially removes MLP channel groups (200 of 784), with attention groups receiving higher importance scores and remaining intact.
28	The MLP intermediate dimension (18{,}944) is partitioned into 28 equal-sized groups of 676 channels each.
29	Structures are scored and ranked in a unified list across both component types, enabling cross-component pruning decisions.
30	At 20\% sparsity, 200 MLP channel groups are removed across 28 layers, totaling approximately 1.45 billion parameters (each group contributes $676 \times 3{,}584 \times 3 = 7{,}268{,}352$ parameters across gate, up, and down projections).
31	Both configurations remove 200 MLP channel groups at matched parameter budgets (${\sim}$1.45B parameters each), but differ in \emph{which} groups are selected---the central comparison of this work.
32	
33	\paragraph{Importance scoring.}
34	For each structure $h$, we compute Taylor-expansion importance $I(h)$ (Eq.~\ref{eq:importance}) using activations and gradients collected on 512 randomly sampled chain-of-thought examples from the GSM8K training set.
35	For GQA groups, we aggregate importance across the constituent query heads and KV head (Section~\ref{sec:stage1}).
36	
37	\paragraph{CKA-based functional overlap.}
38	We compute intra-layer linear CKA (Eq.~\ref{eq:cka}) between all pairs of GQA groups and between all pairs of MLP channel groups within each layer, using the same 512 calibration examples.
39	The functional overlap $F(h)$ for each structure is the mean pairwise CKA with its within-layer peers (Eq.~\ref{eq:overlap}).
40	
41	\paragraph{Recovery-aware scoring.}
42	The final pruning score $S(h) = I(h) \times (1 - F(h))^\alpha$ (Eq.~\ref{eq:score}) combines importance and functional overlap with $\alpha{=}1.0$.
43	Structures with the lowest $S(h)$ are pruned first, subject to the per-layer capacity floor.
44	
45	\paragraph{Per-layer capacity floor.}
46	To prevent representational collapse in individual layers, we enforce that each layer retains at least 40\% of its MLP channel groups (${\ge}12$ of 28 groups per layer).
47	During structure selection, candidates whose removal would violate this constraint are skipped in favor of the next lowest-scoring structure.
48	This constraint is necessary because unconstrained global ranking at 20\% sparsity concentrates pruning in layers with uniformly high functional overlap, collapsing those layers' capacity.
49	
50	\paragraph{Baseline: Standard importance-only pruning.}
51	As the primary baseline, we apply the same Taylor-expansion importance scoring and global ranking but without the CKA overlap penalty ($\alpha{=}0$ in Eq.~\ref{eq:score}), following LLM-Pruner~\citep{llmpruner2023}.
52	The same per-layer capacity floor and sparsity target are applied, ensuring that the only difference between Standard and \rasp{} is the head selection criterion.
53	
54	\subsection{Recovery Pipeline}
55	\label{sec:recovery_pipeline}
56	
57	After pruning, we apply a two-stage recovery pipeline (Section~\ref{sec:stage3}) consisting of SFT warmup followed by GRPO-based RLVR.
58	
59	\paragraph{Stage 3a: SFT warmup.}
60	Structured pruning destroys the model's ability to generate EOS tokens, causing unterminated repetitive outputs that prevent GRPO from computing rewards.
61	We restore generation competence with a brief SFT phase on 7{,}473 chain-of-thought examples (the full GSM8K training set), trained for 2 epochs (1{,}870 gradient steps) with teacher forcing.
62	This stage is minimal in duration (2 epochs, 37 minutes): its sole purpose is to restore EOS generation and basic format compliance, not to recover reasoning ability.
63	
64	\paragraph{Stage 3b: GRPO recovery.}
65	With generation competence restored, we apply GRPO~\citep{shao2024grpo} on GSM8K training problems to recover reasoning ability.
66	The reward is binary: $r{=}1$ if the extracted final answer matches the ground truth, $r{=}0$ otherwise.
67	We use the following configuration: learning rate $1{\times}10^{-6}$, maximum completion length 1{,}024 tokens, 1{,}000 training samples, 1 epoch, KL penalty coefficient $\beta{=}0$, sampling temperature 0.7, and DAPO-style clipped loss.
68	Setting $\beta{=}0$ removes the KL divergence penalty against the reference policy, allowing the pruned model to freely explore new reasoning paths unconstrained by its pre-pruning behavior---a deliberate choice for post-pruning recovery where the reference policy's reasoning trajectories may no longer be achievable through the reduced architecture.
69	
70	\subsection{Results}
71	\label{sec:results}
72	
73	\input{tables/table1_postprune}
74	\input{tables/table2_recovery}
75	
76	\paragraph{Post-prune accuracy.}
77	Table~\ref{tab:postprune} reports accuracy immediately after pruning, before any recovery.
78	At 20\% sparsity, \rasp{} ($\alpha{=}1.0$) retains 29\% GSM8K accuracy compared to 1\% for Standard importance-only pruning ($N{=}100$, $p{<}0.0001$, Fisher's exact test).
79	Both configurations remove 200 MLP channel groups (of 784 total) at matched parameter budgets (${\sim}$1.45B parameters), with all attention GQA groups intact; the difference lies entirely in \emph{which} groups are selected.
80	Standard pruning removes the 200 lowest-importance groups, inadvertently discarding functionally unique structures whose computations cannot be compensated by retained peers.
81	\rasp{} instead removes important-but-redundant groups---those with high functional overlap ($F(h)$)---whose function can be absorbed by similar retained structures, while protecting functionally unique groups that would leave irrecoverable gaps.
82	The 28-percentage-point advantage demonstrates that recovery-aware selection preserves substantially more reasoning capacity at identical sparsity.
83	
84	\paragraph{Recovery pipeline.}
85	Table~\ref{tab:recovery} tracks accuracy through the two-stage recovery pipeline.
86	After SFT warmup (Stage~3a), Standard-pruned models reach 64\% accuracy while \rasp{}-pruned models reach 57\% ($N{=}100$; the difference is not statistically significant at this sample size, $p \approx 0.32$, Fisher's exact test).
87	This reversal is consistent with SFT's recovery mechanism: teacher-forced trajectory imitation favors architectures where the most important individual structures are retained, regardless of functional uniqueness.
88	Standard pruning optimizes precisely for this criterion by protecting high-importance structures, making it better suited to SFT-based recovery.
89	The SFT stage restores EOS generation (99\% termination rate for both configurations, up from 0\%) and basic format compliance in 37 minutes, fulfilling its intended role as a minimal warmup rather than a reasoning recovery method.
90	
91	[TBD: GRPO results. After GRPO recovery (Stage~3b), we expect the comparison to shift: \rasp{}'s preservation of functionally unique structures should provide a better substrate for RLVR's global exploration, potentially reversing the SFT-stage ordering.]
92	
93	\paragraph{Recovery $\Delta$.}
94	[TBD: Recovery $\Delta$ analysis. Post-prune $\to$ post-GRPO gains for both configurations. The key question is whether \rasp{}'s 28-point post-prune advantage translates to a net advantage after the full pipeline, or whether Standard's SFT-stage lead persists through GRPO.]
95	
96	\paragraph{Statistical significance.}
97	[TBD: Full evaluation on $N{=}1{,}319$ (complete GSM8K test set) with Fisher's exact test for pairwise comparisons at each pipeline stage. Preliminary results on $N{=}100$ are reported above; final significance testing awaits GRPO completion.]
98	
99	\subsection{Ablation Studies}
100	\label{sec:ablation}
101	
102	\input{tables/table3_alpha}
103	
104	\paragraph{Effect of CKA balancing coefficient $\alpha$.}
105	The coefficient $\alpha$ in the recovery-aware score $S(h) = I(h) \times (1 - F(h))^\alpha$ controls how strongly functional overlap influences pruning decisions.
106	At $\alpha{=}0$, the overlap term vanishes and \rasp{} reduces to standard importance-only pruning; as $\alpha$ increases, structures with high functional overlap $F(h)$ receive progressively lower scores and are pruned preferentially.
107	Table~\ref{tab:alpha} reports post-prune accuracy across $\alpha \in \{0.0, 0.5, 1.0, 2.0, 4.0\}$ at fixed 20\% sparsity.
108	At $\alpha{=}1.0$ (our default), the model retains 29\% post-prune accuracy.
109	[TBD: Results for $\alpha \in \{0.0, 0.5, 2.0, 4.0\}$ and post-GRPO accuracy across all $\alpha$ values. We expect a non-monotonic relationship: moderate $\alpha$ improves post-GRPO recovery by protecting unique structures, while excessively large $\alpha$ over-weights overlap and ignores importance, degrading both post-prune and post-recovery accuracy.]
110	
111	\paragraph{Per-layer capacity floor.}
112	[TBD: Ablation over the capacity floor threshold $\tau$, currently set to 40\% (each layer retains ${\ge}12$ of 28 MLP groups). Without this floor, unconstrained global ranking concentrates pruning in layers with uniformly high functional overlap, collapsing those layers' representational capacity. We plan to evaluate $\tau \in \{0\%, 20\%, 40\%, 60\%\}$ to quantify the floor's contribution.]
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0f72ada-3a65-4a39-b804-02f646cb5cbd",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "a6d8f201-1466-40fc-b44f-6fe293184584",
  "sourceToolAssistantUUID": "d0f72ada-3a65-4a39-b804-02f646cb5cbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T14:52:49.843Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LXCn6vqR3NFRXGqWZDzsT8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6d8f201-1466-40fc-b44f-6fe293184584",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YXMzkpgqnLxX8vEkRM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51198442-0862-4c9c-a4f7-07a7754c0dba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zyh4XjNLdscsJi2fQFJvX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6756,
      "cache_read_input_tokens": 40680,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6756
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 40680,
          "cache_creation_input_tokens": 6756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6756,
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

_source line 34 · 2026-05-15T14:52:49.847Z_

<details><summary>↩ Tool result · `toolu_01LXCn6vqR3NFRXGqWZDzsT8`</summary>

```text
1	% Abstract — to be written after experiments complete (Phase 2)
2	[TBD: Abstract placeholder. Awaiting GRPO Stage 2 results for headline numbers.]
3	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51198442-0862-4c9c-a4f7-07a7754c0dba",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "9d937a56-826f-4d79-b005-783134b136d7",
  "sourceToolAssistantUUID": "51198442-0862-4c9c-a4f7-07a7754c0dba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T14:52:52.870Z_

<details open><summary>🔧 Tool call — Read · `toolu_016d6zCrke7xcAT8y3tPKU7k`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d937a56-826f-4d79-b005-783134b136d7",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YXirNt3gRuSUMzihzP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac4ec91f-a6ee-4881-9756-5e0102725604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014jNAg1feXFfx4pFX9ADjCo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3522,
      "cache_read_input_tokens": 47436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3522,
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

_source line 36 · 2026-05-15T14:52:52.880Z_

<details><summary>↩ Tool result · `toolu_016d6zCrke7xcAT8y3tPKU7k`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Structured Pruning of Large Language Models}
5	\label{sec:rw_pruning}
6	
7	Structured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.
8	LLM-Pruner~\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.
9	Bonsai~\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating the need for gradient computation.
10	GRASPrune~\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.
11	ShortGPT~\citep{shortgpt2024} and SliceGPT~\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.
12	
13	For reasoning models specifically, RESP~\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\% on GSM8K at 40\% structured sparsity without any recovery training.
14	SSGR~\citep{ssgr2025} shows that selective self-generated calibration with challenging, moderately-lengthy reasoning examples further improves pruning quality for reasoning LLMs.
15	\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.
16	RAC~\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.
17	\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \emph{which} structures are removed critically shapes recovery potential.
18	
19	A parallel line of work recognizes that \emph{functional structure} within networks should guide pruning decisions.
20	FANG~\citep{fang_2025} groups FFN neurons by functional roles via activation clustering and retains shared neurons to prevent cross-task accuracy loss, outperforming FLAP/OBC by 1.5--8.5\% at 30--40\% sparsity.
21	FuncNet~\citep{funcnet_2025} applies Independent Component Analysis (borrowed from neuroimaging) to decompose LLMs into functional networks and preserves key neurons within each.
22	Both share RASP's motivation of identifying functionally critical structures, but neither incorporates a recovery component: they optimize for immediate post-pruning accuracy rather than recoverability under a downstream training paradigm.
23	RASP differs from all the above in that it optimizes the pruning decision for post-RLVR recoverability: structures are scored not only by their importance but by whether their function can be redistributed across retained structures during reinforcement learning recovery.
24	
25	\subsection{Pruning-Aware Recovery and Re-training}
26	\label{sec:rw_recovery}
27	
28	Post-pruning recovery is essential at moderate to high compression ratios.
29	\citet{selfhealing2025} demonstrate that RLVR recovery restores pruned reasoning models to 95\%+ accuracy at 25\% compression, significantly outperforming SFT recovery (${\sim}$80\%).
30	This establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \emph{choice} of what to prune affects how well RLVR can recover.
31	
32	P\textsuperscript{2} Law~\citep{p2law2025} establishes scaling laws for post-training loss after pruning ($L \propto (1/\rho)^\gamma$), predicting recovery data requirements at a given compression ratio, but studies only continual pre-training rather than RLVR or SFT.
33	PASER~\citep{paser2025} optimizes which recovery \emph{data} to use through manifold learning and capability-aware budget allocation---complementary to RASP, which optimizes which \emph{structures} to prune for recoverability.
34	PAT~\citep{pat2025} shows that jointly considering pruning and fine-tuning objectives outperforms the sequential prune-then-finetune pipeline.
35	RestoreLCC~\citep{restorelcc_2025} proposes a plug-and-play recovery method that contrastively probes critical attention heads and injects lost activation components back into the pruned model, achieving consistent gains across pruning methods (NeurIPS 2025 Spotlight).
36	\citet{boiling_frog_2026} adopt an iterative prune-tune loop that gradually compresses reasoning models, avoiding abrupt performance collapse through incremental SFT recovery.
37	Both represent alternative recovery strategies; RASP is complementary in that it optimizes \emph{what} to prune for RLVR recoverability, whereas RestoreLCC optimizes \emph{how} to compensate after pruning and Boiling Frog optimizes the \emph{schedule} of pruning-recovery iterations.
38	
39	The Lottery Ticket Hypothesis~\citep{frankle2019lth} asks which subnetworks can train effectively from random initialization.
40	RASP extends this notion to what we term \emph{paradigm-conditioned trainability}: the optimal subnetwork to retain depends not only on the task but on the recovery paradigm (RLVR vs.\ SFT), as each paradigm imposes fundamentally different functional requirements on the retained architecture.
41	
42	\subsection{RLVR Training Dynamics}
43	\label{sec:rw_rlvr}
44	
45	Understanding how RLVR reshapes model representations is central to predicting which pruned structures are recoverable.
46	\citet{rlsqueezes2026} show that RLVR and SFT shape reasoning capabilities through fundamentally different mechanisms: RLVR \emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \emph{expands} correct trajectories via local imitation.
47	This asymmetry provides the theoretical foundation for RASP---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization, whereas SFT's trajectory-imitation objective cannot achieve such redistribution.
48	OPSD~\citep{opsd2026} proposes a post-RL compaction stage that further compresses reasoning traces after RLVR training, reinforcing the view that RLVR-trained models exhibit compressible internal structure.
49	
50	\paragraph{CKA-based pruning.}
51	CKA~\citep{kornblith2019cka} has been previously applied to pruning, but at a fundamentally different granularity and with a different objective.
52	Among representation similarity measures (CCA, SVCCA, PWCCA, CKA), \citet{klabunde_similarity_survey_2025} show that CKA achieves 99.3\% layer identification accuracy versus 45.4\% for SVCCA, owing to its invariance to invertible linear transforms and isotropic scaling---properties critical for comparing heterogeneous structures (GQA groups vs.\ MLP channels) within the same layer.
53	MPruner~\citep{mpruner2024} uses \emph{inter-layer} CKA to cluster globally redundant layers for depth pruning in CNNs and general transformers, achieving up to 50\% parameter reduction by removing entire layers whose representations are similar to adjacent layers.
54	\citet{lachance2024cka} similarly apply CKA-based layer similarity for depth pruning of VGGNet.
55	Both operate at the \emph{layer} level, using CKA to identify which layers are redundant and can be removed with minimal accuracy loss.
56	In contrast, RASP uses \emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\ depth pruning) optimizing for a different objective (post-recovery reasoning performance vs.\ immediate accuracy preservation).
57	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac4ec91f-a6ee-4881-9756-5e0102725604",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "5d37eaab-2a61-4a98-87b1-e8c8fa9da952",
  "sourceToolAssistantUUID": "ac4ec91f-a6ee-4881-9756-5e0102725604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T14:52:53.403Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WDQvKeRHNEb58qY1w9dV92`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d37eaab-2a61-4a98-87b1-e8c8fa9da952",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YXirNt3gRuSUMzihzP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce97d8ae-1908-490d-94ed-984865aef308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014jNAg1feXFfx4pFX9ADjCo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3522,
      "cache_read_input_tokens": 47436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3522,
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

_source line 38 · 2026-05-15T14:52:53.407Z_

<details><summary>↩ Tool result · `toolu_01WDQvKeRHNEb58qY1w9dV92`</summary>

```text
1	\section{Conclusion}
2	% To be written after experiments complete (Phase 2)
3	[TBD: Conclusion placeholder.]
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce97d8ae-1908-490d-94ed-984865aef308",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "4533f67a-6fca-4379-88e0-f60b9ea9090f",
  "sourceToolAssistantUUID": "ce97d8ae-1908-490d-94ed-984865aef308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T14:52:53.633Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B5wfwiUc9e2PcczJytHECv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4533f67a-6fca-4379-88e0-f60b9ea9090f",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YXirNt3gRuSUMzihzP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc4bef2a-795e-4378-a775-601e674d60da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014jNAg1feXFfx4pFX9ADjCo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3522,
      "cache_read_input_tokens": 47436,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3522
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 47436,
          "cache_creation_input_tokens": 3522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3522,
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

_source line 40 · 2026-05-15T14:52:53.638Z_

<details><summary>↩ Tool result · `toolu_01B5wfwiUc9e2PcczJytHECv`</summary>

```text
1	% Limitations — required by ACL/EMNLP
2	
3	\paragraph{Single model and architecture.}
4	We evaluate \rasp{} exclusively on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, a 7B-parameter reasoning model with GQA ($G{=}7$).
5	Whether the Redundancy Paradox and \rasp{}'s advantages generalize to other model families (e.g., LLaMA, Mistral), scales (1B--70B), or attention configurations (MHA, MQA) remains an open question.
6	The intra-layer CKA overlap dynamics may differ substantially in architectures with more KV heads or different MLP structures.
7	Extending to multiple architectures and scales is a priority for future work, constrained here by the computational cost of the full prune--recover--evaluate pipeline.
8	
9	\paragraph{Single benchmark and sparsity ratio.}
10	Our evaluation uses GSM8K~\citep{cobbe2021gsm8k} as the sole reasoning benchmark and a fixed 20\% structured sparsity.
11	GSM8K tests multi-step arithmetic reasoning but does not cover other reasoning modalities such as logical, commonsense, or code reasoning~\citep{hendrycks2021mmlu,chen2021humaneval}.
12	Similarly, the interaction between functional overlap and recoverability may behave differently at higher sparsity ratios where more structures must be removed and functional redistribution becomes harder.
13	
14	\paragraph{No inference speedup measurement.}
15	Although structured pruning removes entire attention heads and MLP channels---which in principle enables wall-clock speedup without sparse-computation support---we do not report actual inference latency or throughput measurements.
16	The realized speedup depends on hardware, batch size, and framework-level kernel support for non-standard hidden dimensions, and validating these factors is beyond the scope of the current study.
17	
18	\paragraph{Limited seed diversity.}
19	Our experiments use a single random seed for both pruning calibration and recovery training.
20	While we report statistical significance for post-prune accuracy differences via Fisher's exact test ($N{=}100$), the variance introduced by seed-dependent calibration data sampling and GRPO training dynamics is not captured.
21	Multi-seed replication across 3--5 seeds would strengthen confidence in the reported effect sizes.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc4bef2a-795e-4378-a775-601e674d60da",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "5ee61145-7296-46e3-99b4-712178e0a48b",
  "sourceToolAssistantUUID": "fc4bef2a-795e-4378-a775-601e674d60da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-15T14:52:56.891Z_

Now let me read the dream report to see the simulated best/median/worst reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ee61145-7296-46e3-99b4-712178e0a48b",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YY16gM2kd4m8KUHwUN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d34c20fa-39ff-4c7c-ae8b-a42c1102a372",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJkNtskDyk3we3wLSJUCBm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3097,
      "cache_read_input_tokens": 50958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3097,
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

_source line 42 · 2026-05-15T14:52:58.338Z_

<details open><summary>🔧 Tool call — Read · `toolu_017LZ49uauK9JiDNdp63gJGP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/dream_reports/dream_20260515T140651/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d34c20fa-39ff-4c7c-ae8b-a42c1102a372",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YY16gM2kd4m8KUHwUN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b602b3a-1802-4ef7-bd7d-04922fdd0107",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJkNtskDyk3we3wLSJUCBm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3097,
      "cache_read_input_tokens": 50958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3097,
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

_source line 43 · 2026-05-15T14:52:58.352Z_

<details><summary>↩ Tool result · `toolu_017LZ49uauK9JiDNdp63gJGP`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}
13	\usepackage{natbib}
14	\renewcommand{\bibsection}{\section*{References}}
15	
16	\newcommand{\method}{RASP}
17	\newcommand{\score}{S(h)}
18	\newcommand{\importance}{I(h)}
19	\newcommand{\overlap}{F(h)}
20	
21	\title{Recovery-Aware Structured Pruning: Optimizing What to Remove\\for How You Recover}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\begin{abstract}
29	Structured pruning of reasoning-capable LLMs typically selects structures for removal based on importance metrics alone, treating subsequent recovery training as independent. We show this decoupling is suboptimal: the \emph{choice} of which structures to prune determines whether reinforcement learning from verifiable rewards (RLVR) can recover reasoning ability at all. We introduce Recovery-Aware Structured Pruning (\method{}), which scores each structure by $\score{} = \importance{} \times (1 - \overlap{})^\alpha$, where $\overlap{}$ measures functional overlap via linear CKA. \method{} preferentially removes functionally redundant structures whose computation can be redistributed by RLVR, while protecting functionally unique reasoning scaffolding. On DeepSeek-R1-Distill-Qwen-7B at 20\% structured sparsity, \method{} achieves 70\% GSM8K accuracy after SFT+GRPO recovery (84.1\% of the dense baseline), compared to 53\% for standard importance-based pruning (63.7\% recovery). A 25-percentage-point pruning$\times$recovery interaction effect ($p < 0.001$) reveals that optimal pruning order depends on the recovery paradigm: standard pruning outperforms \method{} under SFT-only recovery (66\% vs.\ 58\%) but dramatically underperforms under RLVR (53\% vs.\ 70\%). Per-structure CKA overlap is the strongest predictor of recoverability in a mixed-effects regression on MLP groups ($\beta = 0.38$, partial $R^2 = 0.22$, $p < 0.001$), after controlling for weight norm, gradient importance, and activation magnitude. These results establish that pruning and recovery are coupled optimization problems, and that functional redundancy---traditionally a signal of expendability---is the key resource RLVR exploits during recovery.
30	\end{abstract}
31	
32	%====================================================================
33	\section{Introduction}
34	\label{sec:intro}
35	%====================================================================
36	
37	Reasoning-capable LLMs such as DeepSeek-R1 \cite{deepseek2025r1} and QwQ \cite{qwq2024} achieve strong mathematical and logical reasoning through chain-of-thought distillation and reinforcement learning. Their deployment, however, is constrained by model size. Structured pruning---removing entire attention heads or MLP channel groups---offers hardware-friendly compression with real inference speedup, but at moderate sparsity (20--35\%) it can catastrophically collapse reasoning ability.
38	
39	Recent work addresses this from two directions. Self-Healing \cite{selfhealing2025} demonstrates that RLVR can recover pruned reasoning models to near-original accuracy but uses standard importance-based pruning without questioning \emph{what} to prune. GRASPrune \cite{graspprune2026} provides state-of-the-art budgeted structural pruning via learned gates but does not study recovery. RESP \cite{resp2025} introduces reasoning-trace calibration but omits recovery entirely. No prior work studies how the structural composition of a pruned model interacts with the recovery method.
40	
41	We argue that pruning and recovery are coupled: the structures removed during pruning determine the recovery landscape. This coupling creates a \textbf{Redundancy Paradox}. Traditional pruning treats functional overlap as a sign of expendability---redundant structures are safe to remove because their function is replicated elsewhere. But from the perspective of RLVR recovery, this reasoning is backwards. Structures with high functional overlap are precisely those whose function RLVR can redistribute to remaining structures. Structures with low overlap encode functionally unique computation that, once removed, cannot be recreated by any recovery method.
42	
43	We introduce \textbf{Recovery-Aware Structured Pruning (\method{})}, which scores each structure $h$ by:
44	\begin{equation}
45	\score{} = \importance{} \times (1 - \overlap{})^\alpha
46	\label{eq:rasp}
47	\end{equation}
48	where $\importance{}$ is gradient-based importance and $\overlap{}$ is functional overlap measured by linear CKA against same-layer neighbors. High-overlap structures receive low scores and are pruned first; low-overlap structures are protected. The hyperparameter $\alpha$ controls the CKA emphasis.
49	
50	Our contributions:
51	\begin{enumerate}
52	\item We show that CKA-aware pruning produces models with qualitatively different recovery trajectories: at 20\% sparsity, \method{} achieves 84.1\% recovery rate via SFT+GRPO versus 63.7\% for standard pruning, a 17-percentage-point gap ($p < 0.001$).
53	\item We demonstrate that per-structure CKA overlap is the strongest predictor of recoverability ($\beta = 0.38$, partial $R^2 = 0.22$) in a mixed-effects regression on 784 MLP groups, controlling for standard metrics.
54	\item We reveal a pruning$\times$recovery interaction: standard pruning \emph{outperforms} \method{} under SFT recovery (66\% vs.\ 58\%) but dramatically \emph{underperforms} under RLVR (53\% vs.\ 70\%), with a 25pp interaction effect ($p = 0.0008$).
55	\end{enumerate}
56	
57	%====================================================================
58	\section{Related Work}
59	\label{sec:related}
60	%====================================================================
61	
62	\paragraph{Structured Pruning for LLMs.}
63	LLM-Pruner \cite{llmpruner2023} and SliceGPT \cite{slicegpt2024} remove structures using gradient or projection-based importance. GRASPrune \cite{graspprune2026} learns differentiable gates for budgeted pruning. Bonsai \cite{bonsai2025} uses gradient-free activation-based importance. These methods optimize for immediate post-pruning quality without considering recovery.
64	
65	\paragraph{Recovery of Pruned Reasoning Models.}
66	Self-Healing \cite{selfhealing2025} shows GRPO recovers pruned DeepSeek-R1-Distill models at 25\% unstructured sparsity. PASER \cite{paser2025} optimizes recovery \emph{data} selection. Neither questions whether the pruning decision itself should account for recovery.
67	
68	\paragraph{CKA in Model Analysis.}
69	Centered Kernel Alignment \cite{kornblith2019cka} measures representational similarity between network layers or models. MPruner \cite{mpruner2024} uses inter-layer CKA for depth pruning in CNNs. We apply \emph{intra-layer} CKA between individual structures for width pruning in reasoning LLMs, optimizing for post-recovery rather than immediate performance.
70	
71	\paragraph{RL Squeezes, SFT Expands.}
72	Concurrent work \cite{rlsqueezes2026} shows RLVR compresses incorrect reasoning paths while SFT expands correct ones. Our pruning$\times$recovery interaction provides structural evidence for this mechanism: RLVR succeeds with diverse functional anchors (\method{}), while SFT succeeds with overlapping template structures (standard pruning).
73	
74	%====================================================================
75	\section{Method}
76	\label{sec:method}
77	%====================================================================
78	
79	\subsection{Problem Setting}
80	
81	Given a reasoning-capable LLM and a target structured sparsity ratio $s$, we seek a pruning mask that maximizes post-recovery accuracy under a fixed recovery budget. The recovery pipeline is SFT warmup followed by GRPO.
82	
83	We consider two types of structures: MLP channel groups and attention GQA groups. At 20--25\% sparsity on DeepSeek-R1-Distill-Qwen-7B, all pruned structures are MLP groups (0/112 attention groups are pruned under any method), as attention groups consistently rank higher in the global importance list.
84	
85	\subsection{Scoring Function}
86	
87	For each structure $h$, \method{} computes:
88	
89	\paragraph{Importance $\importance{}$.} First-order Taylor importance using reasoning-trace calibration data (512 GSM8K chain-of-thought traces):
90	\begin{equation}
91	\importance{} = \left| \frac{\partial \mathcal{L}}{\partial \mathbf{z}_h} \cdot \mathbf{z}_h \right|
92	\end{equation}
93	where $\mathbf{z}_h$ is the output activation of structure $h$ and $\mathcal{L}$ is the language modeling loss on reasoning traces.
94	
95	\paragraph{Functional Overlap $\overlap{}$.} For each MLP group $h$ in layer $l$, we compute the mean pairwise linear CKA between $h$ and all other MLP groups in the same layer:
96	\begin{equation}
97	\overlap{} = \frac{1}{|G_l| - 1} \sum_{h' \in G_l \setminus \{h\}} \text{CKA}(\mathbf{X}_h, \mathbf{X}_{h'})
98	\end{equation}
99	where $\mathbf{X}_h \in \mathbb{R}^{n \times d_h}$ contains mean-pooled activations of $h$ across $n=512$ calibration examples, and $G_l$ is the set of MLP groups in layer $l$. Linear CKA is used for computational efficiency and stability.
100	
101	\paragraph{Combined Score.} Structures are ranked by $\score{} = \importance{} \times (1 - \overlap{})^\alpha$, and the bottom $s$ fraction is pruned. The $(1 - \overlap{})^\alpha$ term penalizes high-overlap structures: if a structure's function is highly replicated, it receives a low score regardless of its importance. The hyperparameter $\alpha \geq 0$ controls the strength of this penalty ($\alpha = 0$ reduces to importance-only; $\alpha = 1$ is the default).
102	
103	\subsection{Recovery Pipeline}
104	
105	We adopt a two-stage recovery protocol:
106	\begin{enumerate}
107	\item \textbf{SFT Warmup} (Stage 1): Supervised fine-tuning on GSM8K training solutions to restore basic formatting and EOS behavior.
108	\item \textbf{GRPO} (Stage 2): Group Relative Policy Optimization \cite{grpo2024} with verifiable math rewards, using the SFT-warmed model as initialization.
109	\end{enumerate}
110	Both stages use identical hyperparameters and compute budgets across all pruning methods.
111	
112	%====================================================================
113	\section{Experimental Setup}
114	\label{sec:setup}
115	%====================================================================
116	
117	\paragraph{Model.} DeepSeek-R1-Distill-Qwen-7B, the most widely deployed open reasoning model.
118	
119	\paragraph{Evaluation.} GSM8K (N=1319, full test set) with 95\% bootstrap confidence intervals (10,000 iterations). Out-of-distribution evaluation on MATH-500 and HumanEval.
120	
121	\paragraph{Baselines.}
122	\begin{itemize}
123	\item \textbf{Standard}: Taylor importance-only pruning ($\alpha = 0$ in \method{}'s framework)
124	\item \textbf{GRASPrune} \cite{graspprune2026}: Learned-gate budgeted pruning (ACL 2026 SOTA)
125	\item \textbf{Bonsai} \cite{bonsai2025}: Gradient-free activation-based pruning (ICML 2025)
126	\item \textbf{Unstructured 20\%}: Magnitude-based weight pruning
127	\item \textbf{Random}: Uniform random structure removal
128	\end{itemize}
129	
130	\paragraph{Sparsity levels.} Primary: 20\%. Extended: 25\%, 30\%.
131	
132	%====================================================================
133	\section{Results}
134	\label{sec:results}
135	%====================================================================
136	
137	\subsection{Main Results: Recovery Amplification}
138	\label{sec:main_results}
139	
140	Table~\ref{tab:main} presents the full pruning-recovery pipeline at 20\% structured sparsity. The post-prune gap between \method{} and Standard is modest (4pp, 31\% vs.\ 27\%), but the SFT+GRPO pipeline amplifies this into a 17pp recovery gap (70\% vs.\ 53\%).
141	
142	\begin{table}[t]
143	\centering
144	\small
145	\caption{Main results at 20\% structured sparsity on GSM8K (N=1319). Recovery (\%) = Post-GRPO / Baseline $\times$ 100.}
146	\label{tab:main}
147	\begin{tabular}{lcccc}
148	\toprule
149	\textbf{Method} & \textbf{Post-Prune} & \textbf{+SFT} & \textbf{+GRPO} & \textbf{Recovery} \\
150	\midrule
151	Baseline & 83.2 & --- & --- & --- \\
152	\method{} & 31.0 & 57 & \textbf{70.0} & \textbf{84.1\%} \\
153	Standard & 27.0 & 64 & 53.0 & 63.7\% \\
154	Bonsai & 24.0 & 50 & 47.0 & 56.5\% \\
155	GRASPrune & 10.0 & 35 & 38.0 & 45.7\% \\
156	\bottomrule
157	\end{tabular}
158	\end{table}
159	
160	The recovery trajectories diverge strikingly at the GRPO stage. \method{} gains +13pp from GRPO (57\%$\to$70\%), while Standard \emph{loses} 11pp (64\%$\to$53\%). Bonsai similarly degrades ($-$3pp), and GRASPrune shows only marginal GRPO benefit (+3pp). The pattern is clear: only CKA-aware pruning produces structures that GRPO can effectively exploit.
161	
162	The amplification factor is $17/4 = 4.25\times$: a 4pp post-prune difference becomes a 17pp post-recovery difference. This non-linearity reflects GRPO's differential response to structural composition---it requires functionally diverse anchors for effective exploration, which \method{} preserves and standard pruning does not.
163	
164	\paragraph{Statistical robustness.} Bootstrap 95\% CIs for recovered models: \method{} [67.4, 72.4], Standard [50.3, 55.7]---non-overlapping. Cohen's $h = 0.35$ (medium-to-large effect).
165	
166	\subsection{Post-Prune Robustness Across Seeds}
167	\label{sec:seeds}
168	
169	Table~\ref{tab:seeds} reports 5-seed evaluation (N=1319 per seed). The post-prune gap of 4.5$\pm$0.8pp is consistent across all seeds (paired $t$-test $p = 0.0002$), with pruned-set overlap of 87--93\% confirming that the CKA-based ranking is stable.
170	
171	\begin{table}[t]
172	\centering
173	\small
174	\caption{5-seed post-prune evaluation at 20\% sparsity (GSM8K, N=1319).}
175	\label{tab:seeds}
176	\begin{tabular}{ccccc}
177	\toprule
178	\textbf{Seed} & \textbf{\method{} (\%)} & \textbf{Standard (\%)} & \textbf{Gap (pp)} & \textbf{Overlap (\%)} \\
179	\midrule
180	42 & 31.0 & 27.0 & 4.0 & --- \\
181	123 & 30.2 & 25.8 & 4.4 & 93 \\
182	7 & 32.1 & 27.5 & 4.6 & 89 \\
183	256 & 29.8 & 26.1 & 3.7 & 91 \\
184	1337 & 32.4 & 26.6 & 5.8 & 87 \\
185	\midrule
186	Mean$\pm$Std & 31.1$\pm$1.1 & 26.6$\pm$0.7 & 4.5$\pm$0.8 & --- \\
187	\bottomrule
188	\end{tabular}
189	\end{table}
190	
191	\subsection{GRPO Recovery Dynamics}
192	\label{sec:grpo}
193	
194	Table~\ref{tab:grpo} details the SFT$\to$GRPO transition. A critical observation: Standard achieves \emph{higher} post-SFT accuracy than \method{} (64\% vs.\ 57\%), yet GRPO reverses this ranking entirely. This ranking reversal is the empirical signature of the Redundancy Paradox.
195	
196	\begin{table}[t]
197	\centering
198	\small
199	\caption{SFT$\to$GRPO recovery dynamics. GRPO $\Delta$ = Post-GRPO $-$ Post-SFT.}
200	\label{tab:grpo}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b602b3a-1802-4ef7-bd7d-04922fdd0107",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "ceeb5c0a-a1b8-479a-b769-a62126cdefe6",
  "sourceToolAssistantUUID": "0b602b3a-1802-4ef7-bd7d-04922fdd0107",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T14:52:58.798Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SCaMQQiHEcQxNqbY676cx6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ceeb5c0a-a1b8-479a-b769-a62126cdefe6",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YY16gM2kd4m8KUHwUN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ac0bcf1-55bd-47ae-88fb-913aa67661fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJkNtskDyk3we3wLSJUCBm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3097,
      "cache_read_input_tokens": 50958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3097,
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

_source line 45 · 2026-05-15T14:52:58.803Z_

<details><summary>↩ Tool result · `toolu_01SCaMQQiHEcQxNqbY676cx6`</summary>

```text
1	% Appendix — optional supplementary material
2	% [TBD: hyperparameter tables, additional results]
3	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ac0bcf1-55bd-47ae-88fb-913aa67661fa",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "0989ae9a-8b83-4513-9dc9-95a05c15dee8",
  "sourceToolAssistantUUID": "5ac0bcf1-55bd-47ae-88fb-913aa67661fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T14:52:59.470Z_

<details open><summary>🔧 Tool call — Read · `toolu_019Kw9S47whBTVvfvL7UGycT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/tables/table1_postprune.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0989ae9a-8b83-4513-9dc9-95a05c15dee8",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YY16gM2kd4m8KUHwUN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ecce1e0-180a-4807-8ffe-7dd36060f517",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJkNtskDyk3we3wLSJUCBm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3097,
      "cache_read_input_tokens": 50958,
      "output_tokens": 290,
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
          "output_tokens": 290,
          "cache_read_input_tokens": 50958,
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

_source line 47 · 2026-05-15T14:52:59.475Z_

<details><summary>↩ Tool result · `toolu_019Kw9S47whBTVvfvL7UGycT`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\caption{Post-prune accuracy on GSM8K (N=100). Baseline: Qwen2.5-7B. Standard and \rasp{} remove identical parameter counts at matched sparsity; the difference is purely in structure selection strategy.}
4	\label{tab:postprune}
5	\sisetup{round-mode=places, round-precision=0, table-format=2.0}
6	\begin{tabular}{l S[table-format=2.0] S[table-format=2.0] l}
7	\toprule
8	{Method} & {Sparsity (\%)} & {GSM8K Acc (\%)} & {Params Removed} \\
9	\midrule
10	Baseline (no prune) & 0  & 94 & {---} \\
11	Standard            & 20 & 1  & {${\sim}$1.45B} \\
12	RASP ($\alpha{=}1.0$) & 20 & 29 & {${\sim}$1.45B} \\
13	GRASPrune           & 20 & \textcolor{gray}{TBD} & \textcolor{gray}{TBD} \\
14	\midrule
15	Standard            & 25 & \textcolor{gray}{TBD} & \textcolor{gray}{TBD} \\
16	RASP                & 25 & \textcolor{gray}{TBD} & \textcolor{gray}{TBD} \\
17	\bottomrule
18	\end{tabular}
19	\end{table}
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ecce1e0-180a-4807-8ffe-7dd36060f517",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "d84efb91-0fde-419a-bf1b-0741631a596c",
  "sourceToolAssistantUUID": "7ecce1e0-180a-4807-8ffe-7dd36060f517",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-15T14:53:02.350Z_

Let me read the rest of the dream best-case paper to see the full simulated results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d84efb91-0fde-419a-bf1b-0741631a596c",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YYS18ego8ctwaiYNrD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6476654-f063-4419-834f-4a9520ca9bee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQxjN5HYbPVb4uf3BfQWae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5838,
      "cache_read_input_tokens": 54055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5838,
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

_source line 49 · 2026-05-15T14:53:04.433Z_

<details open><summary>🔧 Tool call — Read · `toolu_019qL6Tnuo7YDX63q6jsDzY7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/dream_reports/dream_20260515T140651/best/paper.tex",
  "offset": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6476654-f063-4419-834f-4a9520ca9bee",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YYS18ego8ctwaiYNrD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2dfb1ae2-f68f-49f3-8a35-f058e6331f61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQxjN5HYbPVb4uf3BfQWae",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5838,
      "cache_read_input_tokens": 54055,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5838
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 54055,
          "cache_creation_input_tokens": 5838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5838,
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

_source line 50 · 2026-05-15T14:53:04.439Z_

<details><summary>↩ Tool result · `toolu_019qL6Tnuo7YDX63q6jsDzY7`</summary>

```text
200	\label{tab:grpo}
201	\begin{tabular}{lccccc}
202	\toprule
203	\textbf{Method} & \textbf{Post-Prune} & \textbf{Post-SFT} & \textbf{Post-GRPO} & \textbf{GRPO $\Delta$} & \textbf{KL} \\
204	\midrule
205	\method{} & 31 & 57 & 70 & +13 & 4.1 \\
206	Standard & 27 & 64 & 53 & $-$11 & 1.8 \\
207	\bottomrule
208	\end{tabular}
209	\end{table}
210	
211	\method{}'s higher KL divergence (4.1 vs.\ 1.8) indicates greater policy movement during GRPO---the model actively discovers new compressed reasoning paths. Standard's lower KL suggests GRPO exploration fails to find rewarding trajectories, and the KL penalty gradually erodes SFT-learned patterns.
212	
213	\subsection{Pruning $\times$ Recovery Interaction}
214	\label{sec:interaction}
215	
216	Table~\ref{tab:interaction} presents the 2$\times$2 factorial analysis (pruning method $\times$ recovery method), which is the core evidence for Claim~3.
217	
218	\begin{table}[t]
219	\centering
220	\small
221	\caption{Pruning $\times$ Recovery interaction. Main effects are non-significant; the 25pp interaction is highly significant ($p = 0.0008$).}
222	\label{tab:interaction}
223	\begin{tabular}{lccc}
224	\toprule
225	\textbf{Pruning} & \textbf{SFT-Only (\%)} & \textbf{SFT+GRPO (\%)} & \textbf{GRPO Marginal (pp)} \\
226	\midrule
227	\method{} & 58 & 70 & +12 \\
228	Standard & 66 & 53 & $-$13 \\
229	\midrule
230	\method{} Advantage & $-$8 & +17 & --- \\
231	\bottomrule
232	\end{tabular}
233	\end{table}
234	
235	Neither the pruning main effect (4.5pp, $p = 0.11$) nor the recovery main effect ($-$0.5pp, $p = 0.85$) is significant. The interaction, however, is 25pp ($p = 0.0008$): the optimal pruning strategy depends entirely on the recovery paradigm. Under SFT, Standard's high-overlap structures provide rich imitation templates. Under RLVR, \method{}'s functionally unique anchors enable effective exploration and redistribution.
236	
237	\subsection{CKA--Recoverability Correlation}
238	\label{sec:correlation}
239	
240	Table~\ref{tab:regression} presents the mixed-effects regression on N=784 MLP channel groups (28 layers as random effects), with per-structure recovery accuracy as the dependent variable.
241	
242	\begin{table}[t]
243	\centering
244	\small
245	\caption{Mixed-effects regression predicting per-structure recoverability. CKA overlap dominates all other predictors (partial $R^2 = 0.22$). VIF$_{\max} = 2.6$.}
246	\label{tab:regression}
247	\begin{tabular}{lcccc}
248	\toprule
249	\textbf{Predictor} & $\boldsymbol{\beta}$ \textbf{(std)} & \textbf{SE} & $\boldsymbol{p}$ & \textbf{Partial} $\boldsymbol{R^2}$ \\
250	\midrule
251	$\overlap{}$ CKA overlap & 0.38 & 0.055 & $<$0.001 & 0.22 \\
252	$\importance{}$ gradient & 0.12 & 0.052 & 0.019 & 0.04 \\
253	Weight norm & 0.07 & 0.050 & 0.15 & 0.01 \\
254	Activation magnitude & 0.04 & 0.050 & 0.42 & $<$0.01 \\
255	\midrule
256	Marginal $R^2$ & \multicolumn{4}{c}{0.31} \\
257	Conditional $R^2$ & \multicolumn{4}{c}{0.49} \\
258	ICC (layer) & \multicolumn{4}{c}{0.18} \\
259	\bottomrule
260	\end{tabular}
261	\end{table}
262	
263	CKA overlap ($\beta = 0.38$, $p < 0.001$) is 3.2$\times$ larger than the next-best predictor (gradient importance, $\beta = 0.12$), independently explaining 22\% of variance in recovery outcomes. Weight norm and activation magnitude are non-significant after controlling for CKA and gradient. The ICC of 0.18 indicates moderate layer-level clustering, with middle layers (8--18) showing the strongest CKA--recoverability coupling.
264	
265	\subsection{Scoring Ablation}
266	\label{sec:ablation}
267	
268	Table~\ref{tab:ablation} isolates the contribution of each component in the \method{} scoring function.
269	
270	\begin{table}[t]
271	\centering
272	\small
273	\caption{Scoring ablation at 20\% sparsity (post-prune GSM8K). Gradient-only corresponds to Standard pruning.}
274	\label{tab:ablation}
275	\begin{tabular}{llcc}
276	\toprule
277	\textbf{Scoring} & \textbf{Formula} & \textbf{GSM8K (\%)} & \textbf{95\% CI} \\
278	\midrule
279	\method{} (full) & $\importance{} \times (1{-}\overlap{})^\alpha$ & 31.0 & [28.6, 33.5] \\
280	CKA-only & $(1{-}\overlap{})^\alpha$ & 29.0 & [26.6, 31.5] \\
281	Gradient-only & $\importance{}$ & 27.0 & [24.6, 29.5] \\
282	Magnitude-only & $\|\mathbf{w}_h\|_2$ & 25.0 & [22.6, 27.5] \\
283	Random & Uniform & 18.0 & [15.9, 20.3] \\
284	\bottomrule
285	\end{tabular}
286	\end{table}
287	
288	The full \method{} score outperforms all ablated variants. CKA-only outperforms gradient-only by 2pp at the post-prune level; this modest gap is consistent with the Recovery Amplification thesis---the true value of CKA-awareness manifests during GRPO recovery (Section~\ref{sec:main_results}), not at the post-prune checkpoint.
289	
290	\subsection{$\alpha$ Sensitivity}
291	\label{sec:alpha}
292	
293	Table~\ref{tab:alpha} presents the sensitivity of the CKA weight $\alpha$.
294	
295	\begin{table}[t]
296	\centering
297	\small
298	\caption{$\alpha$ ablation at 20\% sparsity (post-prune GSM8K). $\alpha = 0$ reduces to importance-only.}
299	\label{tab:alpha}
300	\begin{tabular}{lccc}
301	\toprule
302	$\boldsymbol{\alpha}$ & \textbf{Emphasis} & \textbf{GSM8K (\%)} & \textbf{$\Delta$ vs $\alpha{=}0$ (pp)} \\
303	\midrule
304	0.0 & Importance-only & 25 & 0 \\
305	0.25 & Weak CKA & 27 & +2 \\
306	0.5 & Moderate CKA & 29 & +4 \\
307	1.0 & Balanced (default) & 31 & +6 \\
308	2.0 & Strong CKA & 35 & +10 \\
309	\bottomrule
310	\end{tabular}
311	\end{table}
312	
313	The curve is monotonically increasing with diminishing returns, spanning a 10pp range from $\alpha=0$ to $\alpha=2$. This 10pp gap quantifies the value of CKA as a pruning signal. The absence of a peak below $\alpha=2$ suggests the optimal $\alpha$ may be higher; we use $\alpha=1$ as a conservative default.
314	
315	\subsection{GRASPrune Baseline: Breaking the Linear Assumption}
316	\label{sec:graspprune}
317	
318	A potential confound: does \method{}'s recovery advantage simply reflect its higher post-prune accuracy? Table~\ref{tab:graspprune} addresses this using GRASPrune, which has much lower post-prune accuracy than Standard yet shows different recovery behavior.
319	
320	\begin{table}[t]
321	\centering
322	\small
323	\caption{GRASPrune breaks the ``recovery $\propto$ post-prune accuracy'' assumption.}
324	\label{tab:graspprune}
325	\begin{tabular}{lcccc}
326	\toprule
327	\textbf{Method} & \textbf{Post-Prune (\%)} & \textbf{Post-SFT (\%)} & \textbf{Post-GRPO (\%)} & \textbf{GRPO $\Delta$ (pp)} \\
328	\midrule
329	\method{} & 31 & 57 & 70 & +13 \\
330	Standard & 27 & 64 & 53 & $-$11 \\
331	GRASPrune & 10 & 35 & 38 & +3 \\
332	\bottomrule
333	\end{tabular}
334	\end{table}
335	
336	GRASPrune starts at only 10\% post-prune (far below Standard's 27\%) yet achieves a positive GRPO gain (+3pp), while Standard \emph{declines} ($-$11pp). If recovery were a simple function of post-prune accuracy, GRASPrune should recover less than Standard. The reversal suggests GRASPrune's learned gates implicitly preserve some functional diversity, providing GRPO with limited redistribution capacity despite poor immediate accuracy.
337	
338	\subsection{Multi-Sparsity Analysis}
339	\label{sec:sparsity}
340	
341	Table~\ref{tab:sparsity} extends results to 25\% and 30\% sparsity.
342	
343	\begin{table}[t]
344	\centering
345	\small
346	\caption{Multi-sparsity comparison. \method{}'s advantage grows with sparsity (17pp$\to$23pp). At 30\%, both methods approach collapse.}
347	\label{tab:sparsity}
348	\begin{tabular}{clcccc}
349	\toprule
350	\textbf{Sparsity} & \textbf{Method} & \textbf{Post-Prune (\%)} & \textbf{Post-GRPO (\%)} & \textbf{Recovery (\%)} & \textbf{Gap (pp)} \\
351	\midrule
352	\multirow{2}{*}{20\%} & \method{} & 31 & 70 & 84.1 & \multirow{2}{*}{17} \\
353	 & Standard & 27 & 53 & 63.7 & \\
354	\midrule
355	\multirow{2}{*}{25\%} & \method{} & 20 & 55 & 66.1 & \multirow{2}{*}{23} \\
356	 & Standard & 12 & 32 & 38.5 & \\
357	\midrule
358	\multirow{2}{*}{30\%} & \method{} & 8 & --- & Near-collapse & \multirow{2}{*}{---} \\
359	 & Standard & 3 & --- & Collapsed & \\
360	\bottomrule
361	\end{tabular}
362	\end{table}
363	
364	At 25\%, the recovery gap widens from 17pp to 23pp (55\% vs.\ 32\%). The post-prune gap also increases (8pp vs.\ 4pp at 20\%), because additional pruning disproportionately harms Standard---importance-only methods are forced to remove functionally unique groups at higher sparsity, while \method{} continues to protect them. At 30\%, both methods approach the collapse threshold (8\% and 3\% post-prune), indicating a practical operating envelope of $\leq$25\% for this model class.
365	
366	\subsection{Out-of-Distribution Evaluation}
367	\label{sec:ood}
368	
369	Table~\ref{tab:ood} evaluates recovered models on MATH-500 and HumanEval.
370	
371	\begin{table}[t]
372	\centering
373	\small
374	\caption{OOD evaluation of recovered models (20\% sparsity, SFT+GRPO recovery). \method{}'s advantage generalizes across benchmarks.}
375	\label{tab:ood}
376	\begin{tabular}{lcccc}
377	\toprule
378	\textbf{Benchmark} & \textbf{Baseline (\%)} & \textbf{\method{} (\%)} & \textbf{Standard (\%)} & \textbf{\method{} Adv.\ (pp)} \\
379	\midrule
380	GSM8K & 83.2 & 70 & 53 & 17 \\
381	MATH-500 & 70 & 55 & 42 & 13 \\
382	HumanEval & 50 & 40 & 33 & 7 \\
383	\bottomrule
384	\end{tabular}
385	\end{table}
386	
387	\method{}'s advantage is consistent across benchmarks: +17pp on GSM8K, +13pp on MATH-500, and +7pp on HumanEval. The larger gap on MATH-500 (which requires deeper multi-step reasoning) is consistent with \method{} preserving general reasoning scaffolding rather than GSM8K-specific patterns. Mean OOD retention is 79.3\% for \method{} vs.\ 63.0\% for Standard.
388	
389	\paragraph{SFT recovery is shallow.} Under SFT-only recovery, Standard achieves 66\% on GSM8K but drops to 35\% on MATH-500 (retention 53.8\%). \method{}'s SFT-only model achieves 58\% on GSM8K but retains 42\% on MATH-500 (retention 72.4\%). Standard's SFT advantage is partially GSM8K-specific surface pattern learning; \method{}'s GRPO advantage reflects deeper, generalizable reasoning recovery.
390	
391	\subsection{Structured vs.\ Unstructured Pruning}
392	\label{sec:unstructured}
393	
394	Table~\ref{tab:unstructured} compares structured and unstructured pruning at 20\% sparsity.
395	
396	\begin{table}[t]
397	\centering
398	\small
399	\caption{Structured vs.\ unstructured pruning at 20\% sparsity. \method{} structured pruning dominates on both accuracy and inference speed.}
400	\label{tab:unstructured}
401	\begin{tabular}{lcccc}
402	\toprule
403	\textbf{Method} & \textbf{Post-Prune (\%)} & \textbf{Post-GRPO (\%)} & \textbf{Speedup} & \textbf{Throughput (tok/s)} \\
404	\midrule
405	Dense baseline & 83.2 & --- & 1.00$\times$ & 80.6 \\
406	\method{} (structured) & 31 & 70 & 1.28$\times$ & 103.1 \\
407	Standard (structured) & 27 & 53 & 1.29$\times$ & --- \\
408	Unstructured 20\% & 45 & 60 & 1.02$\times$ & 82.0 \\
409	\bottomrule
410	\end{tabular}
411	\end{table}
412	
413	Despite starting 14pp lower post-prune (31\% vs.\ 45\%), \method{} structured pruning recovers to 10pp \emph{above} unstructured pruning (70\% vs.\ 60\%) while providing 1.28$\times$ actual inference speedup versus the negligible 1.02$\times$ of unstructured pruning. Structured pruning with \method{} provides a clear Pareto improvement: better accuracy \emph{and} faster inference.
414	
415	\subsection{CKA Reliability}
416	\label{sec:reliability}
417	
418	Split-half CKA scores achieve Spearman $\rho = 0.93$ ($p < 0.0001$), confirming measurement stability. Calibration size sensitivity is minimal: 256 samples yield 29\% GSM8K, 512 yield 31\%, and 1024 yield 32\% (3pp total range), with pruned-set overlap of 86--95\%. We use 512 as a near-optimal calibration size throughout.
419	
420	%====================================================================
421	\section{Discussion}
422	\label{sec:discussion}
423	%====================================================================
424	
425	\paragraph{The Redundancy Paradox.} Our central finding is that functional redundancy, traditionally a marker of safe removal, is the key resource RLVR exploits during recovery. \method{} operationalizes this insight: by preferentially removing redundant structures (high CKA overlap) and protecting unique ones, it creates a pruned model whose remaining structures can serve as redistribution targets for GRPO. Standard pruning, which removes structures purely by importance, accidentally destroys these unique anchors while preserving redundant ones that GRPO cannot effectively leverage.
426	
427	\paragraph{Why does Standard degrade under GRPO?} Standard's 64\%$\to$53\% GRPO decline is the most striking result. Standard pruning preserves high-overlap structures that provide rich SFT templates (hence 64\% post-SFT) but lack the functional diversity GRPO needs for exploration. GRPO's KL penalty then erodes SFT-learned surface patterns when exploration fails to discover rewarding alternatives. This aligns with the ``RL Squeezes, SFT Expands'' framework: SFT expands along existing solution paths (benefiting from template redundancy), while RLVR compresses by discovering new paths (requiring structural diversity).
428	
429	\paragraph{Connection to Lottery Ticket Hypothesis.} The Lottery Ticket Hypothesis asks ``which subnetwork trains well from scratch?'' (binary mask). \method{} asks a more nuanced question: ``which structures should be removed so the remainder recovers well under a \emph{specific} training paradigm?'' This is paradigm-conditioned trainability---the answer depends on whether recovery uses SFT or RLVR.
430	
431	\paragraph{Limitations.} (1)~Single base model (DeepSeek-R1-Distill-Qwen-7B); validation on larger models is needed. (2)~At 20--25\% sparsity, only MLP groups are pruned; cross-component (attention + MLP) validation requires higher sparsity ($\sim$40\%+) where current models collapse. (3)~CKA computation adds $\sim$15\% overhead to the pruning step (negligible relative to recovery training). (4)~The optimal $\alpha$ may exceed our tested range; automatic tuning is a natural extension.
432	
433	%====================================================================
434	\section{Conclusion}
435	\label{sec:conclusion}
436	%====================================================================
437	
438	We introduced Recovery-Aware Structured Pruning (\method{}), which integrates functional overlap (CKA) into the pruning decision to optimize for RLVR recovery rather than immediate post-pruning accuracy. At 20\% structured sparsity on DeepSeek-R1-Distill-Qwen-7B, \method{} achieves 70\% GSM8K accuracy after SFT+GRPO recovery (84.1\% of baseline), versus 53\% for standard pruning (63.7\% recovery), with a 1.28$\times$ inference speedup. The 25pp pruning$\times$recovery interaction ($p < 0.001$) demonstrates that pruning and recovery are fundamentally coupled: optimal compression requires knowing how you will recover.
439	
440	These results suggest a broader principle for model compression: the structures removed should be chosen not based on their current contribution, but based on whether the recovery method can redistribute their function. When recovery uses RLVR, functional redundancy is a resource, not a liability.
441	
442	%====================================================================
443	% References
444	%====================================================================
445	
446	\begin{thebibliography}{20}
447	
448	\bibitem[{DeepSeek-AI(2025)}]{deepseek2025r1}
449	DeepSeek-AI.
450	\newblock DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning.
451	\newblock {\em arXiv preprint arXiv:2501.12948}, 2025.
452	
453	\bibitem[{QwQ Team(2024)}]{qwq2024}
454	QwQ Team.
455	\newblock QwQ: Reflect deeply on the boundaries of the unknown.
456	\newblock Technical Report, 2024.
457	
458	\bibitem[{Chen et~al.(2025)}]{selfhealing2025}
459	X.~Chen et~al.
460	\newblock Self-Healing: RLVR recovery of pruned reasoning models.
461	\newblock {\em arXiv preprint}, 2025.
462	
463	\bibitem[{Wang et~al.(2026)}]{graspprune2026}
464	Y.~Wang et~al.
465	\newblock GRASPrune: Gradient-aware structured pruning with learned gates.
466	\newblock In {\em Proceedings of ACL}, 2026.
467	
468	\bibitem[{Zhang et~al.(2025)}]{bonsai2025}
469	L.~Zhang et~al.
470	\newblock Bonsai: Gradient-free structured pruning for large language models.
471	\newblock In {\em Proceedings of ICML}, 2025.
472	
473	\bibitem[{Li et~al.(2025)}]{resp2025}
474	H.~Li et~al.
475	\newblock RESP: Reasoning-trace calibration for structured pruning.
476	\newblock {\em arXiv preprint}, 2025.
477	
478	\bibitem[{Liu et~al.(2025)}]{paser2025}
479	Z.~Liu et~al.
480	\newblock PASER: Recovery-optimal data selection for pruned model fine-tuning.
481	\newblock {\em arXiv preprint}, 2025.
482	
483	\bibitem[{Kornblith et~al.(2019)}]{kornblith2019cka}
484	S.~Kornblith, M.~Norouzi, H.~Lee, and G.~Hinton.
485	\newblock Similarity of neural network representations revisited.
486	\newblock In {\em Proceedings of ICML}, 2019.
487	
488	\bibitem[{Ma et~al.(2023)}]{llmpruner2023}
489	X.~Ma et~al.
490	\newblock LLM-Pruner: On the structural pruning of large language models.
491	\newblock In {\em NeurIPS}, 2023.
492	
493	\bibitem[{Ashkboos et~al.(2024)}]{slicegpt2024}
494	S.~Ashkboos et~al.
495	\newblock SliceGPT: Compress large language models by deleting rows and columns.
496	\newblock In {\em ICLR}, 2024.
497	
498	\bibitem[{Liu et~al.(2024)}]{mpruner2024}
499	J.~Liu et~al.
500	\newblock MPruner: Optimizing neural network size with CKA-based structured pruning.
501	\newblock {\em arXiv preprint}, 2024.
502	
503	\bibitem[{Shao et~al.(2024)}]{grpo2024}
504	Z.~Shao et~al.
505	\newblock DeepSeekMath: Pushing the limits of mathematical reasoning in open language models.
506	\newblock {\em arXiv preprint arXiv:2402.03300}, 2024.
507	
508	\bibitem[{Huang et~al.(2026)}]{rlsqueezes2026}
509	W.~Huang et~al.
510	\newblock RL Squeezes, SFT Expands: Understanding the mechanisms of post-training.
511	\newblock In {\em ICLR}, 2026.
512	
513	\end{thebibliography}
514	
515	%====================================================================
516	\appendix
517	\section{Extended Baselines}
518	\label{app:baselines}
519	
520	Table~\ref{tab:extended} consolidates all baselines at 20\% sparsity, showing the GRPO benefit pattern: \method{} (+13) $\gg$ GRASPrune (+3) $>$ Bonsai ($-$3) $>$ Standard ($-$11). CKA-awareness is the distinguishing factor.
521	
522	\begin{table}[h]
523	\centering
524	\small
525	\caption{Extended baselines at 20\% sparsity.}
526	\label{tab:extended}
527	\begin{tabular}{lcccc}
528	\toprule
529	\textbf{Method} & \textbf{Post-Prune (\%)} & \textbf{Post-SFT (\%)} & \textbf{Post-GRPO (\%)} & \textbf{GRPO $\Delta$ (pp)} \\
530	\midrule
531	\method{} & 31 & 57 & 70 & +13 \\
532	Standard & 27 & 64 & 53 & $-$11 \\
533	Bonsai & 24 & 50 & 47 & $-$3 \\
534	GRASPrune & 10 & 35 & 38 & +3 \\
535	Random & 18 & --- & --- & --- \\
536	Unstructured & 45 & 55 & 60 & +5 \\
537	\bottomrule
538	\end{tabular}
539	\end{table}
540	
541	\section{Sparsity Collapse Map}
542	\label{app:collapse}
543	
544	Table~\ref{tab:collapse} maps the operating envelope for DeepSeek-R1-Distill-Qwen-7B structured pruning.
545	
546	\begin{table}[h]
547	\centering
548	\small
549	\caption{Sparsity collapse map. Recoverable sparsity $\leq$25\% for this model class.}
550	\label{tab:collapse}
551	\begin{tabular}{clcc}
552	\toprule
553	\textbf{Sparsity} & \textbf{Method} & \textbf{Post-Prune (\%)} & \textbf{Status} \\
554	\midrule
555	20\% & \method{} & 31 & Recoverable \\
556	20\% & Standard & 27 & Partial \\
557	25\% & \method{} & 20 & Recoverable \\
558	25\% & Standard & 12 & Weak \\
559	30\% & \method{} & 8 & Near-collapse \\
560	30\% & Standard & 3 & Collapsed \\
561	35\% & Both & 0 & Collapsed \\
562	\bottomrule
563	\end{tabular}
564	\end{table}
565	
566	\section{Inference Benchmark}
567	\label{app:inference}
568	
569	At 20\% structured sparsity, \method{} achieves 9.7~ms/token latency (vs.\ 12.4~ms dense), a 1.28$\times$ speedup with 18.5\% memory reduction. Unstructured pruning at the same sparsity achieves only 1.02$\times$ due to the absence of hardware-native sparse acceleration. \method{} and Standard achieve identical speedup ($\sim$1.28$\times$) since both remove the same number of structures; the difference is purely in which structures are removed.
570	
571	\end{document}
572	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2dfb1ae2-f68f-49f3-8a35-f058e6331f61",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "94819432-cfa1-4ca8-8fce-9531be0ba851",
  "sourceToolAssistantUUID": "2dfb1ae2-f68f-49f3-8a35-f058e6331f61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-15T14:53:07.871Z_

Now let me also check the actual experiment code to understand what has truly been run vs. what is projected/simulated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94819432-cfa1-4ca8-8fce-9531be0ba851",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YYoEaBfuEbvGjidFon",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "acf931c2-9958-4f34-a3a9-458a2e2fc1e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LgGzQtDejcLW2rdevZbeMG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7873,
      "cache_read_input_tokens": 59893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7873,
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

_source line 52 · 2026-05-15T14:53:09.367Z_

<details open><summary>🔧 Tool call — Read · `toolu_011Eb9LkPkSwsbGfiNurfqSc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acf931c2-9958-4f34-a3a9-458a2e2fc1e2",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YYoEaBfuEbvGjidFon",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e458591-c5ff-406e-b68f-c6d5eff7cfe6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LgGzQtDejcLW2rdevZbeMG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7873,
      "cache_read_input_tokens": 59893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7873,
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

_source line 53 · 2026-05-15T14:53:09.373Z_

<details><summary>↩ Tool result · `toolu_011Eb9LkPkSwsbGfiNurfqSc`</summary>

```text
1	"""
2	CKA Overlap Computation for RASP.
3	
4	Computes intra-layer functional overlap F(h) for each attention head and MLP channel group
5	using linear CKA (Centered Kernel Alignment via HSIC).
6	
7	Input:  model + calibration data (GSM8K train subset)
8	Output: per-structure F(h) scores saved as dict in .pt file
9	        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_heads]]),
10	              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])
11	"""
12	
13	import argparse
14	import logging
15	import math
16	import os
17	import random
18	
19	import numpy as np
20	import torch
21	from datasets import load_dataset
22	from transformers import AutoModelForCausalLM, AutoTokenizer
23	
24	logging.basicConfig(
25	    level=logging.INFO,
26	    format="%(asctime)s [%(levelname)s] %(message)s",
27	)
28	logger = logging.getLogger(__name__)
29	
30	
31	def set_seed(seed: int):
32	    random.seed(seed)
33	    np.random.seed(seed)
34	    torch.manual_seed(seed)
35	    torch.cuda.manual_seed_all(seed)
36	
37	
38	def linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:
39	    """Linear CKA between two activation matrices.
40	    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].
41	    """
42	    X = X - X.mean(0)
43	    Y = Y - Y.mean(0)
44	    hsic_xy = torch.norm(X.T @ Y, "fro") ** 2
45	    hsic_xx = torch.norm(X.T @ X, "fro") ** 2
46	    hsic_yy = torch.norm(Y.T @ Y, "fro") ** 2
47	    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()
48	
49	
50	def load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):
51	    """Load GSM8K train questions as calibration prompts."""
52	    ds = load_dataset("openai/gsm8k", "main", split="train")
53	    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
54	
55	    encodings = []
56	    for example in ds:
57	        prompt = f"Question: {example['question']}\nAnswer: Let me think step by step.\n"
58	        ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
59	        encodings.append(ids)
60	    return encodings
61	
62	
63	def collect_head_activations(model, tokenizer, calibration_data, device):
64	    """Run calibration data through model and collect per-head activations for each layer.
65	
66	    Returns dict[layer_idx] -> tensor[n_samples, n_heads, pooled_dim]
67	    where pooled_dim collapses (seq_len, head_dim) via mean-pool over seq_len.
68	    """
69	    config = model.config
70	    n_layers = config.num_hidden_layers
71	    n_heads = config.num_attention_heads
72	    head_dim = config.hidden_size // n_heads
73	
74	    layer_activations = {i: [] for i in range(n_layers)}
75	    hooks = []
76	
77	    def make_hook(layer_idx):
78	        def hook_fn(module, input, output):
79	            # output of attention: (hidden_states, attn_weights, past_kv)
80	            # We hook into q_proj to get query states, then reshape per-head
81	            pass
82	        return hook_fn
83	
84	    # Hook into each attention layer's output (the hidden_states after o_proj)
85	    # We instead hook the q_proj to capture per-head representations
86	    q_proj_outputs = {i: [] for i in range(n_layers)}
87	
88	    def make_q_hook(layer_idx):
89	        def hook_fn(module, input, output):
90	            # output shape: [batch, seq_len, n_heads * head_dim]
91	            q_proj_outputs[layer_idx].append(output.detach())
92	        return hook_fn
93	
94	    for i in range(n_layers):
95	        layer = model.model.layers[i]
96	        h = layer.self_attn.q_proj.register_forward_hook(make_q_hook(i))
97	        hooks.append(h)
98	
99	    model.eval()
100	    with torch.no_grad():
101	        for batch_idx, enc in enumerate(calibration_data):
102	            input_ids = enc["input_ids"].to(device)
103	            attention_mask = enc["attention_mask"].to(device)
104	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
105	            if (batch_idx + 1) % 50 == 0:
106	                logger.info(f"  Processed {batch_idx + 1}/{len(calibration_data)} samples")
107	
108	    for h in hooks:
109	        h.remove()
110	
111	    # Reshape and mean-pool: [batch, seq, n_heads*head_dim] -> per-head [batch, head_dim]
112	    for layer_idx in range(n_layers):
113	        tensors = q_proj_outputs[layer_idx]  # list of [1, seq, n_heads*head_dim]
114	        per_head_list = []
115	        for t in tensors:
116	            t = t.squeeze(0)  # [seq, n_heads*head_dim]
117	            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]
118	            t = t.mean(dim=0)  # [n_heads, head_dim] — mean pool over seq
119	            per_head_list.append(t)
120	        layer_activations[layer_idx] = torch.stack(per_head_list, dim=0)  # [n_samples, n_heads, head_dim]
121	        q_proj_outputs[layer_idx] = None  # free memory
122	
123	    return layer_activations
124	
125	
126	def collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups: int = 28):
127	    """Collect MLP intermediate activations grouped into channel groups.
128	
129	    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim]
130	    """
131	    config = model.config
132	    n_layers = config.num_hidden_layers
133	    intermediate_size = config.intermediate_size
134	    group_size = intermediate_size // n_groups
135	
136	    gate_outputs = {i: [] for i in range(n_layers)}
137	    hooks = []
138	
139	    def make_gate_hook(layer_idx):
140	        def hook_fn(module, input, output):
141	            gate_outputs[layer_idx].append(output.detach())
142	        return hook_fn
143	
144	    for i in range(n_layers):
145	        layer = model.model.layers[i]
146	        h = layer.mlp.gate_proj.register_forward_hook(make_gate_hook(i))
147	        hooks.append(h)
148	
149	    model.eval()
150	    with torch.no_grad():
151	        for enc in calibration_data:
152	            input_ids = enc["input_ids"].to(device)
153	            attention_mask = enc["attention_mask"].to(device)
154	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
155	
156	    for h in hooks:
157	        h.remove()
158	
159	    layer_activations = {}
160	    for layer_idx in range(n_layers):
161	        tensors = gate_outputs[layer_idx]
162	        per_group_list = []
163	        for t in tensors:
164	            t = t.squeeze(0)  # [seq, intermediate_size]
165	            t = t.mean(dim=0)  # [intermediate_size] — mean pool over seq
166	            # Truncate to exact multiple of group_size
167	            usable = n_groups * group_size
168	            t = t[:usable].view(n_groups, group_size)  # [n_groups, group_size]
169	            per_group_list.append(t)
170	        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)  # [n_samples, n_groups, group_size]
171	        gate_outputs[layer_idx] = None
172	
173	    return layer_activations
174	
175	
176	def compute_overlap(activations_dict: dict, structure_name: str) -> tuple:
177	    """Compute F(h) = mean CKA similarity and pairwise CKA matrix per layer.
178	
179	    activations_dict: dict[layer_idx] -> tensor[n_samples, n_structures, dim]
180	    Returns: (overlap_scores, cka_matrices)
181	        overlap_scores: dict[layer_idx] -> tensor[n_structures] of overlap F(h) in [0, 1]
182	        cka_matrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA
183	    """
184	    overlap_scores = {}
185	    cka_matrices = {}
186	    for layer_idx, acts in activations_dict.items():
187	        n_samples, n_structs, dim = acts.shape
188	        matrix = torch.zeros(n_structs, n_structs)
189	        for i in range(n_structs):
190	            matrix[i, i] = 1.0
191	            for j in range(i + 1, n_structs):
192	                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())
193	                matrix[i, j] = val
194	                matrix[j, i] = val
195	        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)
196	        overlap_scores[layer_idx] = scores
197	        cka_matrices[layer_idx] = matrix
198	        logger.info(
199	            f"  Layer {layer_idx} {structure_name}: F(h) range [{scores.min():.4f}, {scores.max():.4f}], "
200	            f"mean={scores.mean():.4f}"
201	        )
202	    return overlap_scores, cka_matrices
203	
204	
205	def main():
206	    parser = argparse.ArgumentParser(description="Compute CKA-based functional overlap scores for RASP")
207	    parser.add_argument("--model_path", type=str, required=True, help="Path to pretrained model")
208	    parser.add_argument("--output_path", type=str, required=True, help="Output .pt file for overlap scores")
209	    parser.add_argument("--n_samples", type=int, default=512, help="Number of calibration samples")
210	    parser.add_argument("--max_length", type=int, default=512, help="Max token length for calibration inputs")
211	    parser.add_argument("--mlp_groups", type=int, default=28, help="Number of MLP channel groups per layer")
212	    parser.add_argument("--seed", type=int, default=42, help="Random seed")
213	    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float16", "bfloat16", "float32"])
214	    args = parser.parse_args()
215	
216	    set_seed(args.seed)
217	    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
218	    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
219	    torch_dtype = dtype_map[args.dtype]
220	
221	    logger.info(f"Loading model from {args.model_path}")
222	    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
223	    model = AutoModelForCausalLM.from_pretrained(
224	        args.model_path,
225	        torch_dtype=torch_dtype,
226	        device_map=device,
227	        trust_remote_code=True,
228	    )
229	
230	    logger.info(f"Loading {args.n_samples} calibration samples from GSM8K train")
231	    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)
232	
233	    logger.info("Collecting attention head activations...")
234	    head_acts = collect_head_activations(model, tokenizer, calibration_data, device)
235	
236	    logger.info("Computing attention head overlap F(h)...")
237	    attn_overlap, attn_cka_matrix = compute_overlap(head_acts, "attn_heads")
238	    del head_acts
239	    torch.cuda.empty_cache()
240	
241	    logger.info("Collecting MLP activations...")
242	    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups=args.mlp_groups)
243	
244	    logger.info("Computing MLP group overlap F(h)...")
245	    mlp_overlap, mlp_cka_matrix = compute_overlap(mlp_acts, "mlp_groups")
246	    del mlp_acts
247	    torch.cuda.empty_cache()
248	
249	    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
250	    result = {
251	        "attn_overlap": attn_overlap,
252	        "mlp_overlap": mlp_overlap,
253	        "attn_cka_matrix": attn_cka_matrix,
254	        "mlp_cka_matrix": mlp_cka_matrix,
255	    }
256	    torch.save(result, args.output_path)
257	    logger.info(f"Saved CKA overlap scores to {args.output_path}")
258	
259	
260	if __name__ == "__main__":
261	    main()
262	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e458591-c5ff-406e-b68f-c6d5eff7cfe6",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "f170b042-122d-44fd-a2e3-0ee14c13fa01",
  "sourceToolAssistantUUID": "4e458591-c5ff-406e-b68f-c6d5eff7cfe6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-15T14:53:09.829Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GoRiDw9i36jXRnsrq74CmV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/rasp_scoring.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f170b042-122d-44fd-a2e3-0ee14c13fa01",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YYoEaBfuEbvGjidFon",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87846f9f-58e2-4750-adf0-eae60c0cbd0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LgGzQtDejcLW2rdevZbeMG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7873,
      "cache_read_input_tokens": 59893,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7873
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 59893,
          "cache_creation_input_tokens": 7873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7873,
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

_source line 55 · 2026-05-15T14:53:09.834Z_

<details><summary>↩ Tool result · `toolu_01GoRiDw9i36jXRnsrq74CmV`</summary>

```text
1	"""
2	RASP Scoring: combine importance I(h) and functional overlap F(h).
3	
4	S(h) = I(h) * (1 - F(h))^alpha
5	
6	Structures with lower S(h) are pruned first.
7	Standard baseline uses only I(h) for ranking.
8	"""
9	
10	import argparse
11	import logging
12	import os
13	
14	import torch
15	
16	logging.basicConfig(
17	    level=logging.INFO,
18	    format="%(asctime)s [%(levelname)s] %(message)s",
19	)
20	logger = logging.getLogger(__name__)
21	
22	
23	def compute_rasp_scores(importance: dict, overlap: dict, alpha: float = 1.0) -> dict:
24	    """Compute S(h) = I(h) * (1 - F(h))^alpha for each structure.
25	
26	    Args:
27	        importance: dict[layer_idx -> tensor of I(h)]
28	        overlap: dict[layer_idx -> tensor of F(h)]
29	        alpha: recoverability penalty exponent
30	
31	    Returns:
32	        dict[layer_idx -> tensor of S(h)]
33	    """
34	    scores = {}
35	    for layer_idx in importance:
36	        ih = importance[layer_idx].float()
37	        fh = overlap[layer_idx].float()
38	        sh = ih * (1.0 - fh).pow(alpha)
39	        scores[layer_idx] = sh
40	    return scores
41	
42	
43	def rank_structures(scores: dict) -> list:
44	    """Flatten and rank all structures globally by score (ascending = prune first).
45	
46	    Returns list of (score, layer_idx, struct_idx) sorted ascending.
47	    """
48	    entries = []
49	    for layer_idx, layer_scores in scores.items():
50	        for struct_idx in range(layer_scores.shape[0]):
51	            entries.append((layer_scores[struct_idx].item(), layer_idx, struct_idx))
52	    entries.sort(key=lambda x: x[0])
53	    return entries
54	
55	
56	def main():
57	    parser = argparse.ArgumentParser(description="Compute RASP pruning scores")
58	    parser.add_argument("--importance_path", type=str, required=True, help="Path to importance scores .pt")
59	    parser.add_argument("--cka_path", type=str, default=None, help="Path to CKA overlap scores .pt (None for standard mode)")
60	    parser.add_argument("--mode", type=str, choices=["standard", "rasp"], default="rasp")
61	    parser.add_argument("--alpha", type=float, default=1.0, help="Recoverability penalty exponent")
62	    parser.add_argument("--output_path", type=str, required=True, help="Output .pt file for pruning scores")
63	    args = parser.parse_args()
64	
65	    importance_data = torch.load(args.importance_path, map_location="cpu", weights_only=True)
66	    attn_importance = importance_data["attn_importance"]
67	    mlp_importance = importance_data["mlp_importance"]
68	
69	    if args.mode == "rasp":
70	        if args.cka_path is None:
71	            raise ValueError("--cka_path required for rasp mode")
72	        cka_data = torch.load(args.cka_path, map_location="cpu", weights_only=True)
73	        attn_overlap = cka_data["attn_overlap"]
74	        mlp_overlap = cka_data["mlp_overlap"]
75	
76	        attn_scores = compute_rasp_scores(attn_importance, attn_overlap, args.alpha)
77	        mlp_scores = compute_rasp_scores(mlp_importance, mlp_overlap, args.alpha)
78	        logger.info(f"Computed RASP scores with alpha={args.alpha}")
79	    else:
80	        # Standard: score = importance only
81	        attn_scores = {k: v.float() for k, v in attn_importance.items()}
82	        mlp_scores = {k: v.float() for k, v in mlp_importance.items()}
83	        logger.info("Computed standard importance-only scores")
84	
85	    attn_ranking = rank_structures(attn_scores)
86	    mlp_ranking = rank_structures(mlp_scores)
87	
88	    logger.info(f"Attention heads total: {len(attn_ranking)}, lowest 5 scores: "
89	                f"{[f'L{e[1]}H{e[2]}={e[0]:.6f}' for e in attn_ranking[:5]]}")
90	    logger.info(f"MLP groups total: {len(mlp_ranking)}, lowest 5 scores: "
91	                f"{[f'L{e[1]}G{e[2]}={e[0]:.6f}' for e in mlp_ranking[:5]]}")
92	
93	    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
94	    result = {
95	        "attn_scores": attn_scores,
96	        "mlp_scores": mlp_scores,
97	        "attn_ranking": attn_ranking,
98	        "mlp_ranking": mlp_ranking,
99	        "mode": args.mode,
100	        "alpha": args.alpha,
101	    }
102	    torch.save(result, args.output_path)
103	    logger.info(f"Saved pruning scores to {args.output_path}")
104	
105	
106	if __name__ == "__main__":
107	    main()
108	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87846f9f-58e2-4750-adf0-eae60c0cbd0f",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "e50f12db-69a2-43b5-aaa0-5083a71e859f",
  "sourceToolAssistantUUID": "87846f9f-58e2-4750-adf0-eae60c0cbd0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-15T14:53:13.026Z_

Now let me check the dream review report for reviewer guidance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e50f12db-69a2-43b5-aaa0-5083a71e859f",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YZCFBFaotr3SovCyy2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74c9229d-fcca-4957-9af6-e39b95f525b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011UwobxqijkAs6zLu8WBGxY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5748,
      "cache_read_input_tokens": 67766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5748,
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

_source line 57 · 2026-05-15T14:53:14.803Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018hQgw2LLdXT1ftSgpnkDHR`</summary>

```json
{
  "pattern": "**/dream_20260515T140651/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74c9229d-fcca-4957-9af6-e39b95f525b5",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YZCFBFaotr3SovCyy2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20c73ccd-ab8d-454b-9c24-96568aa06086",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011UwobxqijkAs6zLu8WBGxY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5748,
      "cache_read_input_tokens": 67766,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5748
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 127,
          "cache_read_input_tokens": 67766,
          "cache_creation_input_tokens": 5748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5748,
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

_source line 58 · 2026-05-15T14:53:14.822Z_

<details><summary>↩ Tool result · `toolu_018hQgw2LLdXT1ftSgpnkDHR`</summary>

```text
artifacts/dream_reports/dream_20260515T140651/logs/orchestrator.log
artifacts/dream_reports/dream_20260515T140651/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260515T140651/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260515T140651/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260515T140651/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260515T140651/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T140651/best/experiment_data.json
artifacts/dream_reports/dream_20260515T140651/best/paper_framing.md
artifacts/dream_reports/dream_20260515T140651/best/paper.tex
artifacts/dream_reports/dream_20260515T140651/best/paper.aux
artifacts/dream_reports/dream_20260515T140651/best/paper.out
artifacts/dream_reports/dream_20260515T140651/best/paper.pdf
artifacts/dream_reports/dream_20260515T140651/best/paper.log
artifacts/dream_reports/dream_20260515T140651/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260515T140651/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T140651/median/experiment_data.json
artifacts/dream_reports/dream_20260515T140651/median/paper_framing.md
artifacts/dream_reports/dream_20260515T140651/median/paper.tex
artifacts/dream_reports/dream_20260515T140651/median/paper.aux
artifacts/dream_reports/dream_20260515T140651/median/paper.out
artifacts/dream_reports/dream_20260515T140651/median/paper.pdf
artifacts/dream_reports/dream_20260515T140651/median/paper.log
artifacts/dream_reports/dream_20260515T140651/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260515T140651/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T140651/worst/experiment_data.json
artifacts/dream_reports/dream_20260515T140651/worst/paper_framing.md
artifacts/dream_reports/dream_20260515T140651/worst/paper.tex
artifacts/dream_reports/dream_20260515T140651/worst/paper.aux
artifacts/dream_reports/dream_20260515T140651/worst/paper.out
artifacts/dream_reports/dream_20260515T140651/worst/paper.pdf
artifacts/dream_reports/dream_20260515T140651/worst/paper.log
artifacts/dream_reports/dream_20260515T140651/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260515T140651/best/review_context.yaml
artifacts/dream_reports/dream_20260515T140651/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20c73ccd-ab8d-454b-9c24-96568aa06086",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "0cdb7110-561c-4731-9441-26026505db20",
  "sourceToolAssistantUUID": "20c73ccd-ab8d-454b-9c24-96568aa06086",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T14:53:18.442Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fda7w4cZjFenaiKQv7zSs9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/dream_reports/dream_20260515T140651/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cdb7110-561c-4731-9441-26026505db20",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YZZZ5kMyHGqpYZAKia",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1ede9af-0032-474f-9b33-f3b3269c70f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5pZx3mWDdgDE6xmjhkpBk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 915,
      "cache_read_input_tokens": 73514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 915,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 60 · 2026-05-15T14:53:18.584Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PLh9qW1J4uNFBLoXAtKQjT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/dream_reports/dream_20260515T140651/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1ede9af-0032-474f-9b33-f3b3269c70f8",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YZZZ5kMyHGqpYZAKia",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1f25a50-de7d-43f5-91c6-61e3da310197",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5pZx3mWDdgDE6xmjhkpBk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 915,
      "cache_read_input_tokens": 73514,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 915
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 73514,
          "cache_creation_input_tokens": 915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 915,
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

_source line 61 · 2026-05-15T14:53:18.759Z_

<details><summary>↩ Tool result · `toolu_01Fda7w4cZjFenaiKQv7zSs9`</summary>

```text
1	narrative_guidance: 'Recovery Amplification版本：post-prune差异仅4-8pp（31% vs 27%），但GRPO将其
2	  放大为17pp recovery gap（70% vs 53%）。更关键的是ranking reversal：SFT下 Standard>RASP（66%>58%），GRPO后RASP>>Standard（70%>>53%）。Redundancy
3	  Paradox 的表现形式不是post-prune的绝对优势，而是GRPO对不同结构组成的差异化响应—— GRPO对RASP +12pp，对Standard -13pp。三个claims全部成立：Claim
4	  1修正为 "recovery amplification"而非"29x advantage"；Claim 2的CKA correlation在MLP groups上显著（partial
5	  R²=0.22）；Claim 3的排序反转完整成立。GRASPrune打破 "recovery只反映post-prune accuracy"的线性假设。α ablation给出10pp的CKA贡献
6	  量化。OOD eval确认泛化。竞争力：EMNLP Main强投稿，Efficient Methods track。
7	
8	  '
9	imagined_experiments:
10	- name: Full GSM8K Evaluation (N=1319)
11	  plan_id: plan_001
12	  description: N=1319全集评估baseline + RASP_20 + Standard_20，替换N=100快速评估，产出publication-quality
13	    CI。
14	  expected_results:
15	    baseline_gsm8k_1319: 0.832
16	    baseline_ci95:
17	    - 0.811
18	    - 0.852
19	    rasp_20_gsm8k_1319: 0.31
20	    rasp_20_ci95:
21	    - 0.286
22	    - 0.335
23	    standard_20_gsm8k_1319: 0.27
24	    standard_20_ci95:
25	    - 0.246
26	    - 0.295
27	    rasp_vs_standard_gap_pp: 4
28	    mcnemar_p: 0.0038
29	    rasp_retention_rate: 0.373
30	    standard_retention_rate: 0.324
31	  result_rationale: 'Full N=1319确认reeval_postprune_definitive：RASP 31%、Standard 27%，gap仅4pp。
32	    CI从±9pp（N=100）收窄到±2.5pp，McNemar在N=1319下显著（p=0.004）。Baseline 83.2%符合DeepSeek-R1-Distill-Qwen-7B的已知GSM8K
33	    population accuracy。4pp的 post-prune差异表明两种方法保留了相似总量的推理能力，但结构组成不同：RASP保留 功能独特的MLP
34	    groups（低F(h)锚点），Standard保留高importance的MLP groups（往 往高F(h)、高重叠）。这种组成差异在post-prune层面效果有限（4pp），但在GRPO
35	    recovery阶段被非线性放大——因为GRPO的redistribution机制对结构多样性的依赖 远强于SFT的imitation learning。
36	
37	    '
38	  tables:
39	  - name: Post-Prune GSM8K (N=1319)
40	    columns:
41	    - Method
42	    - Sparsity
43	    - Acc (%)
44	    - 95% CI
45	    - Retention (%)
46	    rows:
47	    - - Baseline
48	      - 0%
49	      - 83.2
50	      - '[81.1, 85.2]'
51	      - —
52	    - - RASP
53	      - 20%
54	      - 31.0
55	      - '[28.6, 33.5]'
56	      - 37.3
57	    - - Standard
58	      - 20%
59	      - 27.0
60	      - '[24.6, 29.5]'
61	      - 32.4
62	  figures_description:
63	  - 柱状图+95% CI，三个条件。Y轴GSM8K accuracy。4pp gap的CI边缘不重叠。
64	  analysis: 'N=1319确认post-prune gap为4pp且显著。这是Recovery Amplification叙事的起点： 小的post-prune差异经过GRPO放大后变成不可逆的recovery
65	    gap。
66	
67	    '
68	- name: SFT Warmup Recovery
69	  plan_id: plan_002
70	  description: RASP_20和Standard_20的SFT warmup恢复。[DONE — 使用实际结果]
71	  expected_results:
72	    rasp_20_post_sft: 0.57
73	    standard_20_post_sft: 0.64
74	    rasp_sft_gain_pp: 26
75	    standard_sft_gain_pp: 37
76	    rasp_eos_rate: 0.99
77	    standard_eos_rate: 0.99
78	    rasp_train_loss_final: 0.64
79	    standard_train_loss_final: 0.64
80	  result_rationale: '[实际结果] Standard SFT(64%) > RASP SFT(57%)，差7pp。SFT通过模仿学习 "扩展"正确路径（"SFT
81	    Expands"），偏好高重叠结构——这正是Standard保留的结构 类型。Standard的高重叠MLP groups参与多条推理路径，提供了丰富的solution
82	    templates供SFT模仿利用。RASP保留的功能独特结构虽然对GRPO redistribution更 有利，但在SFT的imitation paradigm下利用效率较低。两者train
83	    loss均收敛到0.64、 EOS rate 99%，说明SFT学习充分、差异来自结构组成而非训练不充分。Standard SFT 优势在N=100下CI重叠（ER-001），不作为Claim
84	    3独立证据，但与GRPO联合构成交互效应。
85	
86	    '
87	  tables:
88	  - name: Post-SFT Warmup
89	    columns:
90	    - Method
91	    - Post-Prune (%)
92	    - Post-SFT (%)
93	    - SFT Gain (pp)
94	    - EOS Rate
95	    rows:
96	    - - RASP_20
97	      - 31
98	      - 57
99	      - 26
100	      - 0.99
101	    - - Standard_20
102	      - 27
103	      - 64
104	      - 37
105	      - 0.99
106	  figures_description:
107	  - SFT loss曲线对比。两曲线近乎重合（均收敛到0.64），差异来自结构组成非训练动态。
108	  analysis: 'SFT结果锚定了ranking reversal的"before"状态：SFT下Standard优于RASP。 GRPO（plan_003）需要将此反转。
109	
110	    '
111	- name: GRPO Recovery on SFT-Warmed Models
112	  plan_id: plan_003
113	  description: GRPO Stage 2恢复。RASP和Standard均从SFT-warmed模型开始，相同超参数和计算预算。核心MVP实验。
114	  expected_results:
115	    rasp_post_grpo_gsm8k: 0.7
116	    rasp_post_grpo_ci95:
117	    - 0.675
118	    - 0.724
119	    standard_post_grpo_gsm8k: 0.53
120	    standard_post_grpo_ci95:
121	    - 0.503
122	    - 0.557
123	    grpo_recovery_gap_pp: 17
124	    rasp_grpo_gain_over_sft_pp: 13
125	    standard_grpo_gain_over_sft_pp: -11
126	    rasp_recovery_rate: 0.841
127	    standard_recovery_rate: 0.637
128	    rasp_reward_mean_final: 0.62
129	    standard_reward_mean_final: 0.45
130	    rasp_kl_final: 4.1
131	    standard_kl_final: 1.8
132	    amplification_factor: 4.25
133	  result_rationale: 'GRPO是Recovery Amplification的核心。RASP 57%→70%（+13pp）：RASP保留的功能
134	    独特MLP groups充当GRPO exploration的锚点，编码不可替代的推理子步骤。GRPO通过 "RL Squeezes"将被剪掉的高重叠groups的功能重新分配到这些锚点。reward从~0.3
135	    稳步上升到0.62，KL=4.1表示显著policy移动——模型在积极探索并找到压缩后的推理路径。 Standard 64%→53%（-11pp）：GRPO反而伤害了Standard。Standard的高重叠结构为
136	    SFT提供了丰富模仿模板（故SFT达64%），但缺乏功能多样性——GRPO exploration在 同质化结构空间中找不到有奖励的新路径。KL penalty逐步侵蚀SFT学到的脆弱表面
137	    模式，exploration无法补偿损失。reward在0.45震荡（能部分答对但无法持续提升）。 核心数字：4pp post-prune gap → 17pp
138	    post-GRPO gap，amplification 4.25x。 这证明GRPO是非线性过程，对结构组成的依赖远强于SFT。
139	
140	    '
141	  tables:
142	  - name: SFT→GRPO Recovery Pipeline
143	    columns:
144	    - Method
145	    - Post-Prune (%)
146	    - Post-SFT (%)
147	    - Post-GRPO (%)
148	    - GRPO Δ (pp)
149	    - Recovery (%)
150	    rows:
151	    - - RASP_20
152	      - 31
153	      - 57
154	      - 70
155	      - 13
156	      - 84.1
157	    - - Standard_20
158	      - 27
159	      - 64
160	      - 53
161	      - -11
162	      - 63.7
163	    - - Baseline
164	      - 83.2
165	      - —
166	      - —
167	      - —
168	      - —
169	  figures_description:
170	  - GRPO reward曲线：RASP稳步上升到0.62，Standard在0.45震荡。
171	  - Waterfall：post-prune→post-SFT→post-GRPO，RASP持续恢复vs Standard的GRPO退化。
172	  analysis: 'Headline result。Ranking reversal完成：SFT下Standard>RASP (64>57)，GRPO后 RASP>>Standard
173	    (70>>53)。Standard的-11pp GRPO drop是最引人注目的发现—— GRPO不仅未帮助Standard，反而主动伤害它。Recovery
174	    Amplification confirmed。
175	
176	    '
177	- name: Full GSM8K Eval on Recovered Models (N=1319)
178	  plan_id: plan_004
179	  description: N=1319 bootstrap CI评估所有recovered模型，产出Table 1最终数据。
180	  expected_results:
181	    rasp_recovered_1319: 0.7
182	    rasp_ci95_bootstrap:
183	    - 0.674
184	    - 0.724
185	    standard_recovered_1319: 0.53
186	    standard_ci95_bootstrap:
187	    - 0.503
188	    - 0.557
189	    gap_pp: 17
190	    cohens_h: 0.35
191	    bootstrap_iterations: 10000
192	  result_rationale: 'Bootstrap CI确认17pp gap统计稳健，CI不重叠。Cohen''s h=0.35为中等偏大效应量—— 不是原始framing的"巨大"效应，但17pp在compressed
193	    model上是实质性差异（从 Standard的勉强可用到RASP的接近baseline性能）。这些数据填入Table 1 "+SFT+GRPO"列。
194	
195	    '
196	  tables:
197	  - name: 'Table 1: Main Results at 20% Structured Sparsity'
198	    columns:
199	    - Method
200	    - Post-Prune (%)
201	    - Post-SFT (%)
202	    - Post-SFT+GRPO (%)
203	    - Recovery (%)
204	    - 95% CI
205	    rows:
206	    - - Baseline
207	      - 83.2
208	      - —
209	      - —
210	      - —
211	      - '[81.1, 85.2]'
212	    - - RASP
213	      - 31
214	      - 57
215	      - 70
216	      - 84.1
217	      - '[67.4, 72.4]'
218	    - - Standard
219	      - 27
220	      - 64
221	      - 53
222	      - 63.7
223	      - '[50.3, 55.7]'
224	    - - GRASPrune†
225	      - 10
226	      - 35
227	      - 38
228	      - 45.7
229	      - —
230	  figures_description:
231	  - Grouped bar chart：pipeline各阶段accuracy。Paper Figure 1。
232	  analysis: 'Table 1锚定全文。同sparsity、同recovery budget，唯一区别是pruning criterion—— RASP的CKA-awareness将recovery
233	    rate从64%提升到84%（+20pp）。
234	
235	    '
236	- name: GRASPrune Baseline at 20% Sparsity
237	  plan_id: plan_005
238	  description: GRASPrune（ACL 2026 SOTA budgeted pruning）完整pipeline。排除recovery-只-反映-post-prune-accuracy的混淆。
239	  expected_results:
240	    grasp_post_prune_gsm8k: 0.1
241	    grasp_post_prune_ci95:
242	    - 0.084
243	    - 0.118
244	    grasp_post_sft_gsm8k: 0.35
245	    grasp_post_grpo_gsm8k: 0.38
246	    grasp_post_grpo_ci95:
247	    - 0.354
248	    - 0.407
249	    grasp_recovery_rate: 0.457
250	    grasp_grpo_gain_pp: 3
251	    grasp_vs_rasp_recovered_gap_pp: -32
252	  result_rationale: 'GRASPrune post-prune仅10%（与预实验8%/50样本一致），远低于Standard 27%。这出 人意料：GRASPrune的learned
253	    gates理论上应优于static Taylor。原因：gates通过 reconstruction loss训练，优化"对语言建模最重要的结构"而非"对推理链最重要的
254	    结构"——perplexity-optimal和reasoning-optimal存在系统偏差。 关键发现在recovery pattern：GRASPrune
255	    10%→38%（+28pp GRPO gain），Standard 27%→53%（+26pp）。GRASPrune起点远低于Standard（-17pp），但GRPO增量略高
256	    （+28>+26）。这打破了"recovery只是post-prune accuracy函数"的线性假设：如果 recovery仅反映post-prune
257	    accuracy，GRASPrune应该恢复更少。GRASPrune gates 通过梯度流隐式保留了部分功能冗余结构，给GRPO一定redistribution空间，尽管
258	    immediate accuracy很差。RASP（+39pp gain，31→70%）远超两者——显式CKA优化 比隐式捕获有效得多。
259	
260	    '
261	  tables:
262	  - name: GRASPrune Pipeline
263	    columns:
264	    - Method
265	    - Post-Prune (%)
266	    - Post-SFT (%)
267	    - Post-GRPO (%)
268	    - GRPO Gain (pp)
269	    rows:
270	    - - RASP
271	      - 31
272	      - 57
273	      - 70
274	      - 13
275	    - - Standard
276	      - 27
277	      - 64
278	      - 53
279	      - -11
280	    - - GRASPrune
281	      - 10
282	      - 35
283	      - 38
284	      - 3
285	  figures_description:
286	  - 三方法pipeline柱状图。
287	  - 'Scatter: post-prune accuracy (x) vs GRPO gain (y)，三个点打破线性。'
288	  analysis: 'GRASPrune排除两个混淆：(1) RASP优势≠更好的importance estimation（GRASPrune has learned
289	    gates yet worse）；(2) recovery≠post-prune accuracy的简单函数。 CKA是recovery-optimal pruning的missing
290	    ingredient。
291	
292	    '
293	- name: Multi-Seed Post-Prune Evaluation (5 Seeds)
294	  plan_id: plan_006
295	  description: 5种子（42,123,7,256,1337）RASP和Standard 20%剪枝+N=1319评估。Post-prune gap的统计稳健性验证。
296	  expected_results:
297	    rasp_seeds:
298	      42: 0.31
299	      123: 0.302
300	      7: 0.321
301	      256: 0.298
302	      1337: 0.324
303	    rasp_mean: 0.311
304	    rasp_std: 0.011
305	    standard_seeds:
306	      42: 0.27
307	      123: 0.258
308	      7: 0.275
309	      256: 0.261
310	      1337: 0.266
311	    standard_mean: 0.266
312	    standard_std: 0.007
313	    paired_diffs:
314	    - 0.04
315	    - 0.044
316	    - 0.046
317	    - 0.037
318	    - 0.058
319	    mean_gap_pp: 4.5
320	    gap_std_pp: 0.8
321	    paired_t_p: 0.0002
322	    pruned_set_overlap_range:
323	    - 0.87
324	    - 0.93
325	  result_rationale: '5-seed paired t-test p=0.0002确认4.5pp gap是系统性差异。RASP σ=1.1pp，
326	    Standard σ=0.7pp——CKA和Taylor importance在512 calibration样本上已充分收敛。 所有5个seed的差异均为正（3.7-5.8pp），无reversal。Pruned
327	    set overlap 87-93% 表明~180/200 MLP groups跨seed一致，仅14-26个边界groups随calibration变化。
328	    稳定性来源：linear CKA是kernel-based statistic，512个mean-pooled activations 提供>400有效数据点，远超stable
329	    estimation threshold。这排除了"lucky seed"和 "calibration artifact"。
330	
331	    '
332	  tables:
333	  - name: 5-Seed Robustness
334	    columns:
335	    - Seed
336	    - RASP (%)
337	    - Standard (%)
338	    - Gap (pp)
339	    - Pruned Set Overlap (%)
340	    rows:
341	    - - 42
342	      - 31.0
343	      - 27.0
344	      - 4.0
345	      - —
346	    - - 123
347	      - 30.2
348	      - 25.8
349	      - 4.4
350	      - 93
351	    - - 7
352	      - 32.1
353	      - 27.5
354	      - 4.6
355	      - 89
356	    - - 256
357	      - 29.8
358	      - 26.1
359	      - 3.7
360	      - 91
361	    - - 1337
362	      - 32.4
363	      - 26.6
364	      - 5.8
365	      - 87
366	    - - Mean±Std
367	      - 31.1±1.1
368	      - 26.6±0.7
369	      - 4.5±0.8
370	      - —
371	  figures_description:
372	  - Paired strip plot，5 seeds连线。所有连线斜率为正。
373	  analysis: 'Post-prune gap虽小（4.5pp），但5-seed p=0.0002稳健。Claim 1的post-prune component有充分统计支持。
374	
375	    '
376	- name: Scoring Ablation at 20% Sparsity
377	  plan_id: plan_007
378	  description: RASP评分函数控制消融：magnitude-only, gradient-only, random, CKA-only。隔离各组件贡献。
379	  expected_results:
380	    rasp_full_gsm8k: 0.31
381	    cka_only_gsm8k: 0.29
382	    gradient_only_gsm8k: 0.27
383	    magnitude_only_gsm8k: 0.25
384	    random_gsm8k: 0.18
385	  result_rationale: 'Post-prune差异较小但系统性：RASP(31%)>CKA-only(29%)>gradient(27%,=Standard)>
386	    magnitude(25%)>random(18%)。CKA-only vs gradient仅差2pp，CI部分重叠——在 post-prune层面CKA的边际贡献有限。但这恰恰是Recovery
387	    Amplification要点： post-prune差异小，GRPO放大差异。Importance贡献（gradient 27% vs random 18%=
388	    9pp）在post-prune层面实际上大于CKA边际贡献（CKA-only 29% vs gradient 27%=2pp）。 但这个关系在recovery后反转：CKA-aware结构的GRPO
389	    recoverability远高于 importance-only结构。Random at 18%确认structured scoring确实优于随机。
390	
391	    '
392	  tables:
393	  - name: Scoring Ablation (Post-Prune)
394	    columns:
395	    - Scoring
396	    - Formula
397	    - GSM8K (%)
398	    - 95% CI
399	    rows:
400	    - - RASP (full)
401	      - I(h)×(1-F(h))^α
402	      - 31.0
403	      - '[28.6, 33.5]'
404	    - - CKA-only
405	      - (1-F(h))^α
406	      - 29.0
407	      - '[26.6, 31.5]'
408	    - - Gradient-only (=Std)
409	      - I(h)
410	      - 27.0
411	      - '[24.6, 29.5]'
412	    - - Magnitude-only
413	      - '||w_h||₂'
414	      - 25.0
415	      - '[22.6, 27.5]'
416	    - - Random
417	      - Uniform
418	      - 18.0
419	      - '[15.9, 20.3]'
420	  figures_description:
421	  - 水平柱状图按accuracy排序。标注Standard baseline reference line (27%)。
422	  analysis: 'Post-prune ablation提供组件归因。差异较小但结构清晰。需与recovery数据联合 解读——真正的区分在GRPO阶段。
423	
424	    '
425	- name: Per-Structure CKA-Recoverability Correlation
426	  plan_id: plan_008
427	  description: MLP channel group级mixed-effects回归。N=784 MLP groups，layer random effect。控制weight
428	    norm/gradient/activation。
429	  expected_results:
430	    n_mlp_groups: 784
431	    n_pruned: 200
432	    n_layers: 28
433	    cka_beta: 0.38
434	    cka_se: 0.055
435	    cka_t: 6.91
436	    cka_p: 0.00034
437	    cka_partial_r2: 0.22
438	    gradient_beta: 0.12
439	    gradient_p: 0.019
440	    weight_norm_beta: 0.07
441	    weight_norm_p: 0.15
442	    activation_beta: 0.04
443	    activation_p: 0.42
444	    marginal_r2: 0.31
445	    conditional_r2: 0.49
446	    icc_layer: 0.18
447	    vif_max: 2.6
448	  result_rationale: 'CKA β=0.38 (p=0.0003)在控制weight norm(n.s.)、gradient(marginal p=0.019)、
449	    activation(n.s.)后仍显著dominant，partial R²=0.22独立解释22%方差。这是因为 CKA overlap直接度量functional
450	    redundancy——"这个MLP group的计算被同层其他 groups复制的程度"——本质上就是"GRPO能否将被剪group的功能重新分配给剩余groups"
451	    的代理指标。Weight/gradient/activation度量"当前有多重要"，不度量"功能能否 被接管"。ICC=0.18表明层间存在中等聚类：middle
452	    layers(8-18)的CKA-recoverability 耦合最强（推理redistribution集中于此），与"RL Squeezes"机制一致。
453	    注意：分析仅在MLP groups(N=784)上进行，20%稀疏度下0/112 attention GQA groups 被剪——CKA信号的实际效果是在MLP
454	    groups间做reranking。
455	
456	    '
457	  tables:
458	  - name: Mixed-Effects Regression
459	    columns:
460	    - Predictor
461	    - β (std)
462	    - SE
463	    - p
464	    - Partial R²
465	    rows:
466	    - - F(h) CKA overlap
467	      - 0.38
468	      - 0.055
469	      - <0.001
470	      - 0.22
471	    - - I(h) gradient
472	      - 0.12
473	      - 0.052
474	      - 0.019
475	      - 0.04
476	    - - Weight norm
477	      - 0.07
478	      - 0.05
479	      - 0.15
480	      - 0.01
481	    - - Activation mag.
482	      - 0.04
483	      - 0.05
484	      - 0.42
485	      - <0.01
486	    - - Marginal R²
487	      - 0.31
488	      - ''
489	      - ''
490	      - ''
491	    - - Conditional R²
492	      - 0.49
493	      - ''
494	      - ''
495	      - ''
496	    - - ICC (layer)
497	      - 0.18
498	      - ''
499	      - ''
500	      - ''
501	  figures_description:
502	  - 'Scatter: per-group F(h) vs recoverability，按layer depth着色，回归线+prediction band。'
503	  - 'Coefficient plot: 4 predictors的95% CI，CKA明确与零分离。'
504	  - 'Caterpillar plot: 28层random effects，middle layers intercept最高。'
505	  analysis: 'Claim 2核心证据。CKA(β=0.38)是next-best predictor(gradient β=0.12)的3.2倍， 独立解释22%方差。验证了RASP设计理论基础。
506	
507	    '
508	- name: SFT-Only Recovery Comparison
509	  plan_id: plan_009
510	  description: 相同pruned模型、相同总计算预算，仅SFT恢复。与plan_003联合构成2×2交互分析，验证Claim 3。
511	  expected_results:
512	    sft_only_rasp: 0.58
513	    sft_only_standard: 0.66
514	    sft_grpo_rasp: 0.7
515	    sft_grpo_standard: 0.53
516	    grpo_marginal_rasp_pp: 12
517	    grpo_marginal_standard_pp: -13
518	    interaction_pp: 25
519	    interaction_p: 0.0008
520	    rasp_adv_under_sft_pp: -8
521	    rasp_adv_under_grpo_pp: 17
522	  result_rationale: 'Extended SFT（全预算）RASP=58%、Standard=66%，与warmup SFT接近（SFT饱和快）。
523	    核心交互： SFT-only: Standard(66%) > RASP(58%) → Standard wins by 8pp SFT+GRPO: RASP(70%)
524	    > Standard(53%) → RASP wins by 17pp → 完整ranking reversal。交互效应=12-(-13)=25pp, p=0.0008。
525	    机制："SFT Expands"偏好高重叠结构（Standard保留的），模仿学习在多条重叠路径 上同时强化。"RL Squeezes"需要功能独特锚点（RASP保留的），exploration要求
526	    结构多样性来发现新推理路径。Standard缺乏这些锚点，GRPO的KL penalty在无 rewarding exploration下侵蚀SFT patterns。
527	    最引人入胜的发现：pruning主效应不显著（p≈0.11）——RASP和Standard"平均"差不多。 Method主效应也不显著（p≈0.85）——SFT和GRPO"平均"差不多。但交互25pp,
528	    p<0.001 ——pruning选择和recovery方法间存在质变性交互。
529	
530	    '
531	  tables:
532	  - name: Pruning × Recovery Interaction (2×2)
533	    columns:
534	    - Pruning
535	    - SFT-Only (%)
536	    - SFT+GRPO (%)
537	    - GRPO Marginal (pp)
538	    rows:
539	    - - RASP
540	      - 58
541	      - 70
542	      - 12
543	    - - Standard
544	      - 66
545	      - 53
546	      - -13
547	    - - RASP Advantage
548	      - -8
549	      - 17
550	      - —
551	  - name: Interaction ANOVA
552	    columns:
553	    - Effect
554	    - Estimate (pp)
555	    - SE
556	    - p
557	    rows:
558	    - - Pruning (RASP-Std)
559	      - 4.5
560	      - 2.8
561	      - '0.11'
562	    - - Method (GRPO-SFT)
563	      - -0.5
564	      - 2.7
565	      - '0.85'
566	    - - Pruning × Method
567	      - 25
568	      - 3.8
569	      - '0.0008'
570	  figures_description:
571	  - 2×2交互图：x=recovery method, y=accuracy, 两条非平行线交叉。Paper Figure 3。
572	  analysis: '交互p=0.0008直接支持Claim 3。Main effects不显著而interaction显著——optimal pruning取决于recovery
573	    method。这是novel finding。
574	
575	    '
576	- name: 25% Sparsity RASP + Standard
577	  plan_id: plan_010
578	  description: 25%稀疏度完整pipeline，测试RASP优势在更高压缩下的表现和sparsity scaling。
579	  expected_results:
580	    rasp_25_post_prune: 0.2
581	    standard_25_post_prune: 0.12
582	    rasp_25_gap_pp: 8
583	    rasp_25_post_sft: 0.42
584	    standard_25_post_sft: 0.36
585	    rasp_25_post_grpo: 0.55
586	    standard_25_post_grpo: 0.32
587	    rasp_25_recovery_gap_pp: 23
588	    rasp_25_recovery_rate: 0.661
589	    standard_25_recovery_rate: 0.385
590	  result_rationale: '25%稀疏度放大了post-prune gap（8pp vs 20%的4pp）：额外5%移除不成比例影响 Standard——importance-based策略在高稀疏度下被迫移除更多functionally
591	    unique groups（它们的importance低），而RASP仍优先保护这些groups。 Recovery gap也扩大：23pp(55% vs
592	    32%)，vs 20%的17pp。但amplification factor 下降（23/8=2.88x vs 20%的4.25x），因为RASP在25%也开始受损——更多unique
593	    groups被迫移除，GRPO redistribution空间缩小。 RASP graceful degradation（84→66% recovery
594	    rate）vs Standard accelerating collapse（64→39%）支持RASP在多稀疏度下的实用价值。
595	
596	    '
597	  tables:
598	  - name: Multi-Sparsity Comparison
599	    columns:
600	    - Sparsity
601	    - Method
602	    - Post-Prune (%)
603	    - Post-GRPO (%)
604	    - Recovery (%)
605	    - Gap (pp)
606	    rows:
607	    - - 20%
608	      - RASP
609	      - 31
610	      - 70
611	      - 84.1
612	      - ''
613	    - - 20%
614	      - Standard
615	      - 27
616	      - 53
617	      - 63.7
618	      - 17
619	    - - 25%
620	      - RASP
621	      - 20
622	      - 55
623	      - 66.1
624	      - ''
625	    - - 25%
626	      - Standard
627	      - 12
628	      - 32
629	      - 38.5
630	      - 23
631	  figures_description:
632	  - 折线图：sparsity vs recovered accuracy，RASP graceful vs Standard急降。
633	  analysis: '25%确认RASP优势不是单一操作点artifact。Recovery gap从17→23pp说明CKA-awareness 在更高压缩下价值更大。
634	
635	    '
636	- name: 30% Sparsity Probe
637	  plan_id: plan_011
638	  description: 30%稀疏度prune+eval only，映射collapse threshold和RASP的操作包络。
639	  expected_results:
640	    rasp_30_post_prune: 0.08
641	    rasp_30_ci95:
642	    - 0.065
643	    - 0.098
644	    standard_30_post_prune: 0.03
645	    standard_30_ci95:
646	    - 0.02
647	    - 0.044
648	  result_rationale: '30% RASP降至8%，Standard降至3%。RASP仍非零但已入collapse zone，与D005 35% 完全collapse一致。DeepSeek-R1-Distill模型的"可恢复稀疏度"上界：~25%有效
649	    操作范围，30%边界，35%+崩溃。不进行recovery：8% post-prune的reward signal 极稀疏，GRPO难以收敛。Distilled模型的冗余预算天然小于natively-trained模型，
650	    因为distillation已经压缩了表示。
651	
652	    '
653	  tables:
654	  - name: Sparsity Collapse Map
655	    columns:
656	    - Sparsity
657	    - Method
658	    - Post-Prune (%)
659	    - Status
660	    rows:
661	    - - 20%
662	      - RASP
663	      - 31
664	      - Recoverable
665	    - - 20%
666	      - Standard
667	      - 27
668	      - Partial
669	    - - 25%
670	      - RASP
671	      - 20
672	      - Recoverable
673	    - - 25%
674	      - Standard
675	      - 12
676	      - Weak
677	    - - 30%
678	      - RASP
679	      - 8
680	      - Near-collapse
681	    - - 30%
682	      - Standard
683	      - 3
684	      - Collapsed
685	    - - 35%
686	      - Both
687	      - 0
688	      - Collapsed (D005)
689	  figures_description:
690	  - Sparsity曲线20-35%，标注recoverable zone。
691	  analysis: '完成RASP操作包络映射。Appendix/Discussion材料，回应"为什么选20%"。
692	
693	    '
694	- name: OOD Evaluation (MATH-500, HumanEval)
695	  plan_id: plan_012
696	  description: Recovered models在GSM8K之外benchmark评估，验证RASP优势的OOD泛化。
697	  expected_results:
698	    baseline_math500: 0.7
699	    rasp_recovered_math500: 0.55
700	    standard_recovered_math500: 0.42
701	    rasp_math500_advantage_pp: 13
702	    baseline_humaneval: 0.5
703	    rasp_recovered_humaneval: 0.4
704	    standard_recovered_humaneval: 0.33
705	    rasp_humaneval_advantage_pp: 7
706	    rasp_mean_ood_retention: 0.793
707	    standard_mean_ood_retention: 0.63
708	  result_rationale: 'MATH-500上RASP优势13pp（55% vs 42%），HumanEval上7pp（40% vs 33%）。 MATH-500优势更大因为MATH需要更深推理链（多步数学推导），RASP保留的functionally
709	    unique结构在深层推理中价值更高。HumanEval更依赖pattern matching/syntax knowledge，pruning影响相对较小。RASP
710	    retention: GSM8K 84%, MATH-500 79%, HumanEval 80%——一致~80%+ retention说明RASP保留的是通用推理scaffold而非
711	    GSM8K-specific patterns。Standard retention: GSM8K 64%, MATH-500 60%, HumanEval
712	    66%——也一致但低~20pp。
713	
714	    '
715	  tables:
716	  - name: Cross-Benchmark OOD Evaluation
717	    columns:
718	    - Benchmark
719	    - Baseline (%)
720	    - RASP (%)
721	    - Standard (%)
722	    - RASP Adv. (pp)
723	    rows:
724	    - - GSM8K
725	      - 83.2
726	      - 70
727	      - 53
728	      - 17
729	    - - MATH-500
730	      - 70
731	      - 55
732	      - 42
733	      - 13
734	    - - HumanEval
735	      - 50
736	      - 40
737	      - 33
738	      - 7
739	  figures_description:
740	  - 'Radar chart: baseline vs RASP vs Standard，3 benchmarks。'
741	  analysis: 'OOD泛化将paper从GSM8K-specific提升为general reasoning compression method。 7-17pp一致优势回应reviewer的generalization
742	    concern。
743	
744	    '
745	- name: Bonsai Baseline at 20% Sparsity
746	  plan_id: plan_013
747	  description: Bonsai（ICML 2025）gradient-free结构化剪枝。补充external baseline。
748	  expected_results:
749	    bonsai_post_prune: 0.24
750	    bonsai_post_sft: 0.5
751	    bonsai_post_grpo: 0.47
752	    bonsai_grpo_gain_pp: -3
753	    bonsai_recovery_rate: 0.565
754	  result_rationale: 'Bonsai activation-based importance，post-prune 24%略低于Standard
755	    27%（Taylor importance在此模型上稍优，gradient signal捕获了更多推理相关信息）。GRPO对 Bonsai也产生负效应（-3pp），与Standard
756	    pattern一致：importance-without-CKA 方法保留高重叠结构，缺乏GRPO所需的功能独特锚点。4种non-CKA方法中仅GRASPrune
757	    从GRPO微弱获益（+3pp，因其gates隐式捕获了部分冗余信息），Standard(-11pp)和 Bonsai(-3pp)均受损。GRPO benefit不是普遍现象，而需要CKA-aware结构组成。
758	
759	    '
760	  tables:
761	  - name: Extended Baselines
762	    columns:
763	    - Method
764	    - Post-Prune (%)
765	    - Post-GRPO (%)
766	    - GRPO Δ (pp)
767	    rows:
768	    - - RASP
769	      - 31
770	      - 70
771	      - 13
772	    - - Standard
773	      - 27
774	      - 53
775	      - -11
776	    - - Bonsai
777	      - 24
778	      - 47
779	      - -3
780	    - - GRASPrune
781	      - 10
782	      - 38
783	      - 3
784	  figures_description: []
785	  analysis: 'Bonsai补全baseline方阵。GRPO benefit pattern: RASP(+13) >> GRASPrune(+3) >
786	    Bonsai(-3) > Standard(-11)。CKA-awareness是关键区分因素。
787	
788	    '
789	- name: CKA Reliability Analysis
790	  plan_id: plan_014
791	  description: Split-half consistency和calibration size sensitivity，CKA scoring可靠性验证。
792	  expected_results:
793	    split_half_rho: 0.93
794	    split_half_p: <0.0001
795	    cal_256_gsm8k: 0.29
796	    cal_512_gsm8k: 0.31
797	    cal_1024_gsm8k: 0.32
798	    cal_256_vs_512_rank_corr: 0.9
799	    cal_512_vs_1024_rank_corr: 0.97
800	    pruned_overlap_256_512: 0.86
801	    pruned_overlap_512_1024: 0.95
802	  result_rationale: 'Split-half ρ=0.93，linear CKA在512样本上已收敛。Calibration size影响微小：
803	    256→512提升2pp(29→31%)，512→1024仅1pp(31→32%)，总range 3pp小于inter-seed variance。512是near-optimal
804	    calibration size。核心剪枝决策（pruned set overlap 86-95%）对calibration不敏感。Housekeeping
805	    but essential for credibility。
806	
807	    '
808	  tables:
809	  - name: CKA Reliability
810	    columns:
811	    - Analysis
812	    - Metric
813	    - Value
814	    rows:
815	    - - Split-half
816	      - Spearman ρ
817	      - 0.93
818	    - - Cal 256
819	      - GSM8K (%)
820	      - 29
821	    - - Cal 512
822	      - GSM8K (%)
823	      - 31
824	    - - Cal 1024
825	      - GSM8K (%)
826	      - 32
827	  figures_description:
828	  - 左：split-half scatter。右：calibration sensitivity曲线，plateau at 512。
829	  analysis: 'Appendix材料，main text一行引用。
830	
831	    '
832	- name: α Sensitivity Ablation
833	  plan_id: plan_015
834	  description: α ∈ {0, 0.25, 0.5, 1.0, 2.0}，RASP唯一自由参数的系统性分析。
835	  expected_results:
836	    alpha_0_0: 0.25
837	    alpha_0_25: 0.27
838	    alpha_0_5: 0.29
839	    alpha_1_0: 0.31
840	    alpha_2_0: 0.35
841	    optimal_alpha: 2.0
842	    optimal_vs_alpha0_gap_pp: 10
843	    curve_shape: monotonically increasing, diminishing returns
844	  result_rationale: 'α=0（importance-only within RASP framework）给出25%，低于Standard 27%。原因：
845	    RASP使用reasoning-trace calibration（CoT traces）计算importance，CoT traces 较长噪声较高，产生比standard
846	    perplexity-calibration稍差的importance estimates。 CKA组件补偿并超过差距：α=0.5已达29%（超Standard
847	    27%），α=2.0达35%。 曲线单调递增+diminishing returns：0→0.5增4pp，0.5→1.0增2pp，1.0→2.0增4pp （高α端acceleration提示optimal可能>2.0，与预实验α=4.0=40%一致）。
848	    最优vs α=0 gap=10pp量化了CKA作为pruning signal的价值。α是唯一free parameter， 此ablation为practitioners提供调参指导：α=1合理default，α∈[1,2]推荐范围。
849	
850	    '
851	  tables:
852	  - name: α Ablation
853	    columns:
854	    - α
855	    - Emphasis
856	    - GSM8K (%)
857	    - Δ vs α=0 (pp)
858	    rows:
859	    - - 0.0
860	      - Importance-only
861	      - 25
862	      - 0
863	    - - 0.25
864	      - Weak CKA
865	      - 27
866	      - 2
867	    - - 0.5
868	      - Moderate CKA
869	      - 29
870	      - 4
871	    - - 1.0
872	      - Balanced (default)
873	      - 31
874	      - 6
875	    - - 2.0
876	      - Strong CKA
877	      - 35
878	      - 10
879	  figures_description:
880	  - α vs accuracy曲线，标注Standard(27%)reference line。α>0.3后RASP超Standard。
881	  analysis: 'Dream reviewers全档位Critical实验。10pp gap量化CKA贡献。曲线未见peak说明 optimal α可能>2.0，motivates
882	    future auto-tuning。
883	
884	    '
885	- name: Inference Speedup Benchmark
886	  plan_id: plan_016
887	  description: Wall-clock latency + throughput比较。结构化剪枝的practical motivation。
888	  expected_results:
889	    dense_latency_ms: 12.4
890	    rasp_20_latency_ms: 9.7
891	    standard_20_latency_ms: 9.6
892	    rasp_20_speedup: 1.28
893	    dense_throughput_tok_s: 80.6
894	    rasp_20_throughput_tok_s: 103.1
895	    memory_reduction_pct: 18.5
896	    unstructured_20_speedup: 1.02
897	  result_rationale: '20%结构化稀疏度提供1.28x实际加速（12.4→9.7 ms/tok），因为移除200个MLP channel groups直接减少矩阵维度，不需sparse
898	    hardware。RASP和Standard speedup 几乎相同（均~1.28x），因为两者移除相同数量structures。Memory减少18.5%。
899	    对比unstructured 20%（仅1.02x，需sparse tensor cores），structured pruning 的practical
900	    value明确。RASP在accuracy(70%) + speed(1.28x)两个维度均优于 unstructured(60%, 1.02x)。
901	
902	    '
903	  tables:
904	  - name: Inference Benchmark
905	    columns:
906	    - Model
907	    - Latency (ms/tok)
908	    - Speedup
909	    - Throughput (tok/s)
910	    rows:
911	    - - Dense
912	      - 12.4
913	      - 1.00x
914	      - 80.6
915	    - - RASP 20%
916	      - 9.7
917	      - 1.28x
918	      - 103.1
919	    - - Unstructured 20%
920	      - 12.2
921	      - 1.02x
922	      - 82.0
923	  figures_description:
924	  - 双轴图：latency bars + throughput line。标注structured vs unstructured差异。
925	  analysis: '1.28x加速 + 70% accuracy提供明确practical motivation。Structured RASP在 accuracy和speed两个维度均胜unstructured。
926	
927	    '
928	- name: Unstructured Pruning Baseline at 20%
929	  plan_id: plan_017
930	  description: Magnitude-based unstructured 20%。标定structured vs unstructured gap，对标Self-Healing。
931	  expected_results:
932	    unstructured_post_prune: 0.45
933	    unstructured_post_sft: 0.55
934	    unstructured_post_grpo: 0.6
935	    unstructured_grpo_gain_pp: 5
936	    unstructured_recovery_rate: 0.721
937	    unstructured_speedup: 1.02
938	  result_rationale: 'Unstructured 20% post-prune 45%远高于structured RASP 31%——保留了所有architectural
939	    structures，仅均匀削弱每个structure的capacity。但post-GRPO仅60%，低于RASP 70%。 看似反直觉：起点更高却恢复更低。原因：unstructured均匀削弱所有structures，
940	    GRPO的redistribution机制在此设置下效率低——没有完整结构可以"接管"被削弱结构 的功能。RASP的结构化移除创造了明确的donor(移除的高重叠groups)和receiver
941	    (保留的独特groups)，GRPO可清晰地将donor功能重分配给receiver。 关键比较：RASP structured(70%, 1.28x) vs
942	    unstructured(60%, 1.02x)——accuracy 和speed双维度RASP占优。对标Self-Healing(2025)的unstructured设置。
943	
944	    '
945	  tables:
946	  - name: Structured vs Unstructured
947	    columns:
948	    - Method
949	    - Post-Prune (%)
950	    - Post-GRPO (%)
951	    - Speedup
952	    rows:
953	    - - RASP (structured)
954	      - 31
955	      - 70
956	      - 1.28x
957	    - - Standard (structured)
958	      - 27
959	      - 53
960	      - 1.29x
961	    - - Unstructured 20%
962	      - 45
963	      - 60
964	      - 1.02x
965	  figures_description:
966	  - 'Scatter: accuracy vs speedup。RASP右上(高accuracy+高speed)，unstructured左下。'
967	  analysis: 'RASP structured在accuracy(70>60)和speed(1.28>1.02)双维度优于unstructured。 完成"为什么structured
968	    pruning"论证。
969	
970	    '
971	- name: SFT OOD Eval Contingency
972	  plan_id: plan_018
973	  description: SFT-recovered模型的OOD评估。检验Standard SFT 64%的GSM8K-specificity。
974	  expected_results:
975	    standard_sft_math500: 0.35
976	    standard_sft_humaneval: 0.25
977	    rasp_sft_math500: 0.42
978	    rasp_sft_humaneval: 0.32
979	    standard_gsm8k_to_math500_retention: 0.538
980	    rasp_gsm8k_to_math500_retention: 0.724
981	  result_rationale: 'Best tier下GRPO advantage=17pp远超5pp阈值（contingency不strictly needed），
982	    但仍提供有价值分析。Standard SFT从GSM8K 66%降至MATH-500 35%（retention 53%）， RASP SFT从58%降至42%（retention
983	    72%）。Standard的OOD drop更剧烈：其SFT recovery包含显著GSM8K-specific pattern learning——SFT在高重叠结构上学到了
984	    GSM8K特定的数字操作模板，不泛化到MATH。RASP的SFT recovery虽GSM8K绝对数低， 但泛化性好，因为functionally unique结构支持更通用推理。
985	    补充Claim 3：SFT下Standard的优势是shallow(GSM8K-specific)，GRPO下RASP的 优势是deep(OOD-generalizable)。
986	
987	    '
988	  tables:
989	  - name: SFT OOD Transfer
990	    columns:
991	    - Method
992	    - GSM8K (%)
993	    - MATH-500 (%)
994	    - HumanEval (%)
995	    - MATH Ret. (%)
996	    rows:
997	    - - RASP SFT-only
998	      - 58
999	      - 42
1000	      - 32
1001	      - 72.4
1002	    - - Standard SFT-only
1003	      - 66
1004	      - 35
1005	      - 25
1006	      - 53.8
1007	  figures_description:
1008	  - 'Bar chart: GSM8K vs MATH-500 vs HumanEval。Standard GSM8K领先但OOD落后。'
1009	  analysis: Standard SFT优势是shallow，RASP GRPO优势是deep。Discussion增加"surface vs genuine
1010	    reasoning recovery"分析维度。
1011	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1ede9af-0032-474f-9b33-f3b3269c70f8",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "ef5a21a6-1b50-44ad-be3a-54602b8ffa06",
  "sourceToolAssistantUUID": "b1ede9af-0032-474f-9b33-f3b3269c70f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T14:53:18.857Z_

<details><summary>↩ Tool result · `toolu_01PLh9qW1J4uNFBLoXAtKQjT`</summary>

```text
1	tier: best
2	narrative_guidance: 'Recovery Amplification版本：post-prune差异仅4-8pp（31% vs 27%），但GRPO将其
3	  放大为17pp recovery gap（70% vs 53%）。更关键的是ranking reversal：SFT下 Standard>RASP（66%>58%），GRPO后RASP>>Standard（70%>>53%）。Redundancy
4	  Paradox 的表现形式不是post-prune的绝对优势，而是GRPO对不同结构组成的差异化响应—— GRPO对RASP +12pp，对Standard -13pp。三个claims全部成立：Claim
5	  1修正为 "recovery amplification"而非"29x advantage"；Claim 2的CKA correlation在MLP groups上显著（partial
6	  R²=0.22）；Claim 3的排序反转完整成立。GRASPrune打破 "recovery只反映post-prune accuracy"的线性假设。α ablation给出10pp的CKA贡献
7	  量化。OOD eval确认泛化。竞争力：EMNLP Main强投稿，Efficient Methods track。
8	
9	  '
10	imagined_experiments:
11	- name: Full GSM8K Evaluation (N=1319)
12	  plan_id: plan_001
13	  description: N=1319全集评估baseline + RASP_20 + Standard_20，替换N=100快速评估，产出publication-quality
14	    CI。
15	  expected_results:
16	    baseline_gsm8k_1319: 0.832
17	    baseline_ci95:
18	    - 0.811
19	    - 0.852
20	    rasp_20_gsm8k_1319: 0.31
21	    rasp_20_ci95:
22	    - 0.286
23	    - 0.335
24	    standard_20_gsm8k_1319: 0.27
25	    standard_20_ci95:
26	    - 0.246
27	    - 0.295
28	    rasp_vs_standard_gap_pp: 4
29	    mcnemar_p: 0.0038
30	    rasp_retention_rate: 0.373
31	    standard_retention_rate: 0.324
32	  result_rationale: 'Full N=1319确认reeval_postprune_definitive：RASP 31%、Standard 27%，gap仅4pp。
33	    CI从±9pp（N=100）收窄到±2.5pp，McNemar在N=1319下显著（p=0.004）。Baseline 83.2%符合DeepSeek-R1-Distill-Qwen-7B的已知GSM8K
34	    population accuracy。4pp的 post-prune差异表明两种方法保留了相似总量的推理能力，但结构组成不同：RASP保留 功能独特的MLP
35	    groups（低F(h)锚点），Standard保留高importance的MLP groups（往 往高F(h)、高重叠）。这种组成差异在post-prune层面效果有限（4pp），但在GRPO
36	    recovery阶段被非线性放大——因为GRPO的redistribution机制对结构多样性的依赖 远强于SFT的imitation learning。
37	
38	    '
39	  tables:
40	  - name: Post-Prune GSM8K (N=1319)
41	    columns:
42	    - Method
43	    - Sparsity
44	    - Acc (%)
45	    - 95% CI
46	    - Retention (%)
47	    rows:
48	    - - Baseline
49	      - 0%
50	      - 83.2
51	      - '[81.1, 85.2]'
52	      - —
53	    - - RASP
54	      - 20%
55	      - 31.0
56	      - '[28.6, 33.5]'
57	      - 37.3
58	    - - Standard
59	      - 20%
60	      - 27.0
61	      - '[24.6, 29.5]'
62	      - 32.4
63	  figures_description:
64	  - 柱状图+95% CI，三个条件。Y轴GSM8K accuracy。4pp gap的CI边缘不重叠。
65	  analysis: 'N=1319确认post-prune gap为4pp且显著。这是Recovery Amplification叙事的起点： 小的post-prune差异经过GRPO放大后变成不可逆的recovery
66	    gap。
67	
68	    '
69	- name: SFT Warmup Recovery
70	  plan_id: plan_002
71	  description: RASP_20和Standard_20的SFT warmup恢复。[DONE — 使用实际结果]
72	  expected_results:
73	    rasp_20_post_sft: 0.57
74	    standard_20_post_sft: 0.64
75	    rasp_sft_gain_pp: 26
76	    standard_sft_gain_pp: 37
77	    rasp_eos_rate: 0.99
78	    standard_eos_rate: 0.99
79	    rasp_train_loss_final: 0.64
80	    standard_train_loss_final: 0.64
81	  result_rationale: '[实际结果] Standard SFT(64%) > RASP SFT(57%)，差7pp。SFT通过模仿学习 "扩展"正确路径（"SFT
82	    Expands"），偏好高重叠结构——这正是Standard保留的结构 类型。Standard的高重叠MLP groups参与多条推理路径，提供了丰富的solution
83	    templates供SFT模仿利用。RASP保留的功能独特结构虽然对GRPO redistribution更 有利，但在SFT的imitation paradigm下利用效率较低。两者train
84	    loss均收敛到0.64、 EOS rate 99%，说明SFT学习充分、差异来自结构组成而非训练不充分。Standard SFT 优势在N=100下CI重叠（ER-001），不作为Claim
85	    3独立证据，但与GRPO联合构成交互效应。
86	
87	    '
88	  tables:
89	  - name: Post-SFT Warmup
90	    columns:
91	    - Method
92	    - Post-Prune (%)
93	    - Post-SFT (%)
94	    - SFT Gain (pp)
95	    - EOS Rate
96	    rows:
97	    - - RASP_20
98	      - 31
99	      - 57
100	      - 26
101	      - 0.99
102	    - - Standard_20
103	      - 27
104	      - 64
105	      - 37
106	      - 0.99
107	  figures_description:
108	  - SFT loss曲线对比。两曲线近乎重合（均收敛到0.64），差异来自结构组成非训练动态。
109	  analysis: 'SFT结果锚定了ranking reversal的"before"状态：SFT下Standard优于RASP。 GRPO（plan_003）需要将此反转。
110	
111	    '
112	- name: GRPO Recovery on SFT-Warmed Models
113	  plan_id: plan_003
114	  description: GRPO Stage 2恢复。RASP和Standard均从SFT-warmed模型开始，相同超参数和计算预算。核心MVP实验。
115	  expected_results:
116	    rasp_post_grpo_gsm8k: 0.7
117	    rasp_post_grpo_ci95:
118	    - 0.675
119	    - 0.724
120	    standard_post_grpo_gsm8k: 0.53
121	    standard_post_grpo_ci95:
122	    - 0.503
123	    - 0.557
124	    grpo_recovery_gap_pp: 17
125	    rasp_grpo_gain_over_sft_pp: 13
126	    standard_grpo_gain_over_sft_pp: -11
127	    rasp_recovery_rate: 0.841
128	    standard_recovery_rate: 0.637
129	    rasp_reward_mean_final: 0.62
130	    standard_reward_mean_final: 0.45
131	    rasp_kl_final: 4.1
132	    standard_kl_final: 1.8
133	    amplification_factor: 4.25
134	  result_rationale: 'GRPO是Recovery Amplification的核心。RASP 57%→70%（+13pp）：RASP保留的功能
135	    独特MLP groups充当GRPO exploration的锚点，编码不可替代的推理子步骤。GRPO通过 "RL Squeezes"将被剪掉的高重叠groups的功能重新分配到这些锚点。reward从~0.3
136	    稳步上升到0.62，KL=4.1表示显著policy移动——模型在积极探索并找到压缩后的推理路径。 Standard 64%→53%（-11pp）：GRPO反而伤害了Standard。Standard的高重叠结构为
137	    SFT提供了丰富模仿模板（故SFT达64%），但缺乏功能多样性——GRPO exploration在 同质化结构空间中找不到有奖励的新路径。KL penalty逐步侵蚀SFT学到的脆弱表面
138	    模式，exploration无法补偿损失。reward在0.45震荡（能部分答对但无法持续提升）。 核心数字：4pp post-prune gap → 17pp
139	    post-GRPO gap，amplification 4.25x。 这证明GRPO是非线性过程，对结构组成的依赖远强于SFT。
140	
141	    '
142	  tables:
143	  - name: SFT→GRPO Recovery Pipeline
144	    columns:
145	    - Method
146	    - Post-Prune (%)
147	    - Post-SFT (%)
148	    - Post-GRPO (%)
149	    - GRPO Δ (pp)
150	    - Recovery (%)
151	    rows:
152	    - - RASP_20
153	      - 31
154	      - 57
155	      - 70
156	      - 13
157	      - 84.1
158	    - - Standard_20
159	      - 27
160	      - 64
161	      - 53
162	      - -11
163	      - 63.7
164	    - - Baseline
165	      - 83.2
166	      - —
167	      - —
168	      - —
169	      - —
170	  figures_description:
171	  - GRPO reward曲线：RASP稳步上升到0.62，Standard在0.45震荡。
172	  - Waterfall：post-prune→post-SFT→post-GRPO，RASP持续恢复vs Standard的GRPO退化。
173	  analysis: 'Headline result。Ranking reversal完成：SFT下Standard>RASP (64>57)，GRPO后 RASP>>Standard
174	    (70>>53)。Standard的-11pp GRPO drop是最引人注目的发现—— GRPO不仅未帮助Standard，反而主动伤害它。Recovery
175	    Amplification confirmed。
176	
177	    '
178	- name: Full GSM8K Eval on Recovered Models (N=1319)
179	  plan_id: plan_004
180	  description: N=1319 bootstrap CI评估所有recovered模型，产出Table 1最终数据。
181	  expected_results:
182	    rasp_recovered_1319: 0.7
183	    rasp_ci95_bootstrap:
184	    - 0.674
185	    - 0.724
186	    standard_recovered_1319: 0.53
187	    standard_ci95_bootstrap:
188	    - 0.503
189	    - 0.557
190	    gap_pp: 17
191	    cohens_h: 0.35
192	    bootstrap_iterations: 10000
193	  result_rationale: 'Bootstrap CI确认17pp gap统计稳健，CI不重叠。Cohen''s h=0.35为中等偏大效应量—— 不是原始framing的"巨大"效应，但17pp在compressed
194	    model上是实质性差异（从 Standard的勉强可用到RASP的接近baseline性能）。这些数据填入Table 1 "+SFT+GRPO"列。
195	
196	    '
197	  tables:
198	  - name: 'Table 1: Main Results at 20% Structured Sparsity'
199	    columns:
200	    - Method
201	    - Post-Prune (%)
202	    - Post-SFT (%)
203	    - Post-SFT+GRPO (%)
204	    - Recovery (%)
205	    - 95% CI
206	    rows:
207	    - - Baseline
208	      - 83.2
209	      - —
210	      - —
211	      - —
212	      - '[81.1, 85.2]'
213	    - - RASP
214	      - 31
215	      - 57
216	      - 70
217	      - 84.1
218	      - '[67.4, 72.4]'
219	    - - Standard
220	      - 27
221	      - 64
222	      - 53
223	      - 63.7
224	      - '[50.3, 55.7]'
225	    - - GRASPrune†
226	      - 10
227	      - 35
228	      - 38
229	      - 45.7
230	      - —
231	  figures_description:
232	  - Grouped bar chart：pipeline各阶段accuracy。Paper Figure 1。
233	  analysis: 'Table 1锚定全文。同sparsity、同recovery budget，唯一区别是pruning criterion—— RASP的CKA-awareness将recovery
234	    rate从64%提升到84%（+20pp）。
235	
236	    '
237	- name: GRASPrune Baseline at 20% Sparsity
238	  plan_id: plan_005
239	  description: GRASPrune（ACL 2026 SOTA budgeted pruning）完整pipeline。排除recovery-只-反映-post-prune-accuracy的混淆。
240	  expected_results:
241	    grasp_post_prune_gsm8k: 0.1
242	    grasp_post_prune_ci95:
243	    - 0.084
244	    - 0.118
245	    grasp_post_sft_gsm8k: 0.35
246	    grasp_post_grpo_gsm8k: 0.38
247	    grasp_post_grpo_ci95:
248	    - 0.354
249	    - 0.407
250	    grasp_recovery_rate: 0.457
251	    grasp_grpo_gain_pp: 3
252	    grasp_vs_rasp_recovered_gap_pp: -32
253	  result_rationale: 'GRASPrune post-prune仅10%（与预实验8%/50样本一致），远低于Standard 27%。这出 人意料：GRASPrune的learned
254	    gates理论上应优于static Taylor。原因：gates通过 reconstruction loss训练，优化"对语言建模最重要的结构"而非"对推理链最重要的
255	    结构"——perplexity-optimal和reasoning-optimal存在系统偏差。 关键发现在recovery pattern：GRASPrune
256	    10%→38%（+28pp GRPO gain），Standard 27%→53%（+26pp）。GRASPrune起点远低于Standard（-17pp），但GRPO增量略高
257	    （+28>+26）。这打破了"recovery只是post-prune accuracy函数"的线性假设：如果 recovery仅反映post-prune
258	    accuracy，GRASPrune应该恢复更少。GRASPrune gates 通过梯度流隐式保留了部分功能冗余结构，给GRPO一定redistribution空间，尽管
259	    immediate accuracy很差。RASP（+39pp gain，31→70%）远超两者——显式CKA优化 比隐式捕获有效得多。
260	
261	    '
262	  tables:
263	  - name: GRASPrune Pipeline
264	    columns:
265	    - Method
266	    - Post-Prune (%)
267	    - Post-SFT (%)
268	    - Post-GRPO (%)
269	    - GRPO Gain (pp)
270	    rows:
271	    - - RASP
272	      - 31
273	      - 57
274	      - 70
275	      - 13
276	    - - Standard
277	      - 27
278	      - 64
279	      - 53
280	      - -11
281	    - - GRASPrune
282	      - 10
283	      - 35
284	      - 38
285	      - 3
286	  figures_description:
287	  - 三方法pipeline柱状图。
288	  - 'Scatter: post-prune accuracy (x) vs GRPO gain (y)，三个点打破线性。'
289	  analysis: 'GRASPrune排除两个混淆：(1) RASP优势≠更好的importance estimation（GRASPrune has learned
290	    gates yet worse）；(2) recovery≠post-prune accuracy的简单函数。 CKA是recovery-optimal pruning的missing
291	    ingredient。
292	
293	    '
294	- name: Multi-Seed Post-Prune Evaluation (5 Seeds)
295	  plan_id: plan_006
296	  description: 5种子（42,123,7,256,1337）RASP和Standard 20%剪枝+N=1319评估。Post-prune gap的统计稳健性验证。
297	  expected_results:
298	    rasp_seeds:
299	      42: 0.31
300	      123: 0.302
301	      7: 0.321
302	      256: 0.298
303	      1337: 0.324
304	    rasp_mean: 0.311
305	    rasp_std: 0.011
306	    standard_seeds:
307	      42: 0.27
308	      123: 0.258
309	      7: 0.275
310	      256: 0.261
311	      1337: 0.266
312	    standard_mean: 0.266
313	    standard_std: 0.007
314	    paired_diffs:
315	    - 0.04
316	    - 0.044
317	    - 0.046
318	    - 0.037
319	    - 0.058
320	    mean_gap_pp: 4.5
321	    gap_std_pp: 0.8
322	    paired_t_p: 0.0002
323	    pruned_set_overlap_range:
324	    - 0.87
325	    - 0.93
326	  result_rationale: '5-seed paired t-test p=0.0002确认4.5pp gap是系统性差异。RASP σ=1.1pp，
327	    Standard σ=0.7pp——CKA和Taylor importance在512 calibration样本上已充分收敛。 所有5个seed的差异均为正（3.7-5.8pp），无reversal。Pruned
328	    set overlap 87-93% 表明~180/200 MLP groups跨seed一致，仅14-26个边界groups随calibration变化。
329	    稳定性来源：linear CKA是kernel-based statistic，512个mean-pooled activations 提供>400有效数据点，远超stable
330	    estimation threshold。这排除了"lucky seed"和 "calibration artifact"。
331	
332	    '
333	  tables:
334	  - name: 5-Seed Robustness
335	    columns:
336	    - Seed
337	    - RASP (%)
338	    - Standard (%)
339	    - Gap (pp)
340	    - Pruned Set Overlap (%)
341	    rows:
342	    - - 42
343	      - 31.0
344	      - 27.0
345	      - 4.0
346	      - —
347	    - - 123
348	      - 30.2
349	      - 25.8
350	      - 4.4
351	      - 93
352	    - - 7
353	      - 32.1
354	      - 27.5
355	      - 4.6
356	      - 89
357	    - - 256
358	      - 29.8
359	      - 26.1
360	      - 3.7
361	      - 91
362	    - - 1337
363	      - 32.4
364	      - 26.6
365	      - 5.8
366	      - 87
367	    - - Mean±Std
368	      - 31.1±1.1
369	      - 26.6±0.7
370	      - 4.5±0.8
371	      - —
372	  figures_description:
373	  - Paired strip plot，5 seeds连线。所有连线斜率为正。
374	  analysis: 'Post-prune gap虽小（4.5pp），但5-seed p=0.0002稳健。Claim 1的post-prune component有充分统计支持。
375	
376	    '
377	- name: Scoring Ablation at 20% Sparsity
378	  plan_id: plan_007
379	  description: RASP评分函数控制消融：magnitude-only, gradient-only, random, CKA-only。隔离各组件贡献。
380	  expected_results:
381	    rasp_full_gsm8k: 0.31
382	    cka_only_gsm8k: 0.29
383	    gradient_only_gsm8k: 0.27
384	    magnitude_only_gsm8k: 0.25
385	    random_gsm8k: 0.18
386	  result_rationale: 'Post-prune差异较小但系统性：RASP(31%)>CKA-only(29%)>gradient(27%,=Standard)>
387	    magnitude(25%)>random(18%)。CKA-only vs gradient仅差2pp，CI部分重叠——在 post-prune层面CKA的边际贡献有限。但这恰恰是Recovery
388	    Amplification要点： post-prune差异小，GRPO放大差异。Importance贡献（gradient 27% vs random 18%=
389	    9pp）在post-prune层面实际上大于CKA边际贡献（CKA-only 29% vs gradient 27%=2pp）。 但这个关系在recovery后反转：CKA-aware结构的GRPO
390	    recoverability远高于 importance-only结构。Random at 18%确认structured scoring确实优于随机。
391	
392	    '
393	  tables:
394	  - name: Scoring Ablation (Post-Prune)
395	    columns:
396	    - Scoring
397	    - Formula
398	    - GSM8K (%)
399	    - 95% CI
400	    rows:
401	    - - RASP (full)
402	      - I(h)×(1-F(h))^α
403	      - 31.0
404	      - '[28.6, 33.5]'
405	    - - CKA-only
406	      - (1-F(h))^α
407	      - 29.0
408	      - '[26.6, 31.5]'
409	    - - Gradient-only (=Std)
410	      - I(h)
411	      - 27.0
412	      - '[24.6, 29.5]'
413	    - - Magnitude-only
414	      - '||w_h||₂'
415	      - 25.0
416	      - '[22.6, 27.5]'
417	    - - Random
418	      - Uniform
419	      - 18.0
420	      - '[15.9, 20.3]'
421	  figures_description:
422	  - 水平柱状图按accuracy排序。标注Standard baseline reference line (27%)。
423	  analysis: 'Post-prune ablation提供组件归因。差异较小但结构清晰。需与recovery数据联合 解读——真正的区分在GRPO阶段。
424	
425	    '
426	- name: Per-Structure CKA-Recoverability Correlation
427	  plan_id: plan_008
428	  description: MLP channel group级mixed-effects回归。N=784 MLP groups，layer random effect。控制weight
429	    norm/gradient/activation。
430	  expected_results:
431	    n_mlp_groups: 784
432	    n_pruned: 200
433	    n_layers: 28
434	    cka_beta: 0.38
435	    cka_se: 0.055
436	    cka_t: 6.91
437	    cka_p: 0.00034
438	    cka_partial_r2: 0.22
439	    gradient_beta: 0.12
440	    gradient_p: 0.019
441	    weight_norm_beta: 0.07
442	    weight_norm_p: 0.15
443	    activation_beta: 0.04
444	    activation_p: 0.42
445	    marginal_r2: 0.31
446	    conditional_r2: 0.49
447	    icc_layer: 0.18
448	    vif_max: 2.6
449	  result_rationale: 'CKA β=0.38 (p=0.0003)在控制weight norm(n.s.)、gradient(marginal p=0.019)、
450	    activation(n.s.)后仍显著dominant，partial R²=0.22独立解释22%方差。这是因为 CKA overlap直接度量functional
451	    redundancy——"这个MLP group的计算被同层其他 groups复制的程度"——本质上就是"GRPO能否将被剪group的功能重新分配给剩余groups"
452	    的代理指标。Weight/gradient/activation度量"当前有多重要"，不度量"功能能否 被接管"。ICC=0.18表明层间存在中等聚类：middle
453	    layers(8-18)的CKA-recoverability 耦合最强（推理redistribution集中于此），与"RL Squeezes"机制一致。
454	    注意：分析仅在MLP groups(N=784)上进行，20%稀疏度下0/112 attention GQA groups 被剪——CKA信号的实际效果是在MLP
455	    groups间做reranking。
456	
457	    '
458	  tables:
459	  - name: Mixed-Effects Regression
460	    columns:
461	    - Predictor
462	    - β (std)
463	    - SE
464	    - p
465	    - Partial R²
466	    rows:
467	    - - F(h) CKA overlap
468	      - 0.38
469	      - 0.055
470	      - <0.001
471	      - 0.22
472	    - - I(h) gradient
473	      - 0.12
474	      - 0.052
475	      - 0.019
476	      - 0.04
477	    - - Weight norm
478	      - 0.07
479	      - 0.05
480	      - 0.15
481	      - 0.01
482	    - - Activation mag.
483	      - 0.04
484	      - 0.05
485	      - 0.42
486	      - <0.01
487	    - - Marginal R²
488	      - 0.31
489	      - ''
490	      - ''
491	      - ''
492	    - - Conditional R²
493	      - 0.49
494	      - ''
495	      - ''
496	      - ''
497	    - - ICC (layer)
498	      - 0.18
499	      - ''
500	      - ''
501	      - ''
502	  figures_description:
503	  - 'Scatter: per-group F(h) vs recoverability，按layer depth着色，回归线+prediction band。'
504	  - 'Coefficient plot: 4 predictors的95% CI，CKA明确与零分离。'
505	  - 'Caterpillar plot: 28层random effects，middle layers intercept最高。'
506	  analysis: 'Claim 2核心证据。CKA(β=0.38)是next-best predictor(gradient β=0.12)的3.2倍， 独立解释22%方差。验证了RASP设计理论基础。
507	
508	    '
509	- name: SFT-Only Recovery Comparison
510	  plan_id: plan_009
511	  description: 相同pruned模型、相同总计算预算，仅SFT恢复。与plan_003联合构成2×2交互分析，验证Claim 3。
512	  expected_results:
513	    sft_only_rasp: 0.58
514	    sft_only_standard: 0.66
515	    sft_grpo_rasp: 0.7
516	    sft_grpo_standard: 0.53
517	    grpo_marginal_rasp_pp: 12
518	    grpo_marginal_standard_pp: -13
519	    interaction_pp: 25
520	    interaction_p: 0.0008
521	    rasp_adv_under_sft_pp: -8
522	    rasp_adv_under_grpo_pp: 17
523	  result_rationale: 'Extended SFT（全预算）RASP=58%、Standard=66%，与warmup SFT接近（SFT饱和快）。
524	    核心交互： SFT-only: Standard(66%) > RASP(58%) → Standard wins by 8pp SFT+GRPO: RASP(70%)
525	    > Standard(53%) → RASP wins by 17pp → 完整ranking reversal。交互效应=12-(-13)=25pp, p=0.0008。
526	    机制："SFT Expands"偏好高重叠结构（Standard保留的），模仿学习在多条重叠路径 上同时强化。"RL Squeezes"需要功能独特锚点（RASP保留的），exploration要求
527	    结构多样性来发现新推理路径。Standard缺乏这些锚点，GRPO的KL penalty在无 rewarding exploration下侵蚀SFT patterns。
528	    最引人入胜的发现：pruning主效应不显著（p≈0.11）——RASP和Standard"平均"差不多。 Method主效应也不显著（p≈0.85）——SFT和GRPO"平均"差不多。但交互25pp,
529	    p<0.001 ——pruning选择和recovery方法间存在质变性交互。
530	
531	    '
532	  tables:
533	  - name: Pruning × Recovery Interaction (2×2)
534	    columns:
535	    - Pruning
536	    - SFT-Only (%)
537	    - SFT+GRPO (%)
538	    - GRPO Marginal (pp)
539	    rows:
540	    - - RASP
541	      - 58
542	      - 70
543	      - 12
544	    - - Standard
545	      - 66
546	      - 53
547	      - -13
548	    - - RASP Advantage
549	      - -8
550	      - 17
551	      - —
552	  - name: Interaction ANOVA
553	    columns:
554	    - Effect
555	    - Estimate (pp)
556	    - SE
557	    - p
558	    rows:
559	    - - Pruning (RASP-Std)
560	      - 4.5
561	      - 2.8
562	      - '0.11'
563	    - - Method (GRPO-SFT)
564	      - -0.5
565	      - 2.7
566	      - '0.85'
567	    - - Pruning × Method
568	      - 25
569	      - 3.8
570	      - '0.0008'
571	  figures_description:
572	  - 2×2交互图：x=recovery method, y=accuracy, 两条非平行线交叉。Paper Figure 3。
573	  analysis: '交互p=0.0008直接支持Claim 3。Main effects不显著而interaction显著——optimal pruning取决于recovery
574	    method。这是novel finding。
575	
576	    '
577	- name: 25% Sparsity RASP + Standard
578	  plan_id: plan_010
579	  description: 25%稀疏度完整pipeline，测试RASP优势在更高压缩下的表现和sparsity scaling。
580	  expected_results:
581	    rasp_25_post_prune: 0.2
582	    standard_25_post_prune: 0.12
583	    rasp_25_gap_pp: 8
584	    rasp_25_post_sft: 0.42
585	    standard_25_post_sft: 0.36
586	    rasp_25_post_grpo: 0.55
587	    standard_25_post_grpo: 0.32
588	    rasp_25_recovery_gap_pp: 23
589	    rasp_25_recovery_rate: 0.661
590	    standard_25_recovery_rate: 0.385
591	  result_rationale: '25%稀疏度放大了post-prune gap（8pp vs 20%的4pp）：额外5%移除不成比例影响 Standard——importance-based策略在高稀疏度下被迫移除更多functionally
592	    unique groups（它们的importance低），而RASP仍优先保护这些groups。 Recovery gap也扩大：23pp(55% vs
593	    32%)，vs 20%的17pp。但amplification factor 下降（23/8=2.88x vs 20%的4.25x），因为RASP在25%也开始受损——更多unique
594	    groups被迫移除，GRPO redistribution空间缩小。 RASP graceful degradation（84→66% recovery
595	    rate）vs Standard accelerating collapse（64→39%）支持RASP在多稀疏度下的实用价值。
596	
597	    '
598	  tables:
599	  - name: Multi-Sparsity Comparison
600	    columns:
601	    - Sparsity
602	    - Method
603	    - Post-Prune (%)
604	    - Post-GRPO (%)
605	    - Recovery (%)
606	    - Gap (pp)
607	    rows:
608	    - - 20%
609	      - RASP
610	      - 31
611	      - 70
612	      - 84.1
613	      - ''
614	    - - 20%
615	      - Standard
616	      - 27
617	      - 53
618	      - 63.7
619	      - 17
620	    - - 25%
621	      - RASP
622	      - 20
623	      - 55
624	      - 66.1
625	      - ''
626	    - - 25%
627	      - Standard
628	      - 12
629	      - 32
630	      - 38.5
631	      - 23
632	  figures_description:
633	  - 折线图：sparsity vs recovered accuracy，RASP graceful vs Standard急降。
634	  analysis: '25%确认RASP优势不是单一操作点artifact。Recovery gap从17→23pp说明CKA-awareness 在更高压缩下价值更大。
635	
636	    '
637	- name: 30% Sparsity Probe
638	  plan_id: plan_011
639	  description: 30%稀疏度prune+eval only，映射collapse threshold和RASP的操作包络。
640	  expected_results:
641	    rasp_30_post_prune: 0.08
642	    rasp_30_ci95:
643	    - 0.065
644	    - 0.098
645	    standard_30_post_prune: 0.03
646	    standard_30_ci95:
647	    - 0.02
648	    - 0.044
649	  result_rationale: '30% RASP降至8%，Standard降至3%。RASP仍非零但已入collapse zone，与D005 35% 完全collapse一致。DeepSeek-R1-Distill模型的"可恢复稀疏度"上界：~25%有效
650	    操作范围，30%边界，35%+崩溃。不进行recovery：8% post-prune的reward signal 极稀疏，GRPO难以收敛。Distilled模型的冗余预算天然小于natively-trained模型，
651	    因为distillation已经压缩了表示。
652	
653	    '
654	  tables:
655	  - name: Sparsity Collapse Map
656	    columns:
657	    - Sparsity
658	    - Method
659	    - Post-Prune (%)
660	    - Status
661	    rows:
662	    - - 20%
663	      - RASP
664	      - 31
665	      - Recoverable
666	    - - 20%
667	      - Standard
668	      - 27
669	      - Partial
670	    - - 25%
671	      - RASP
672	      - 20
673	      - Recoverable
674	    - - 25%
675	      - Standard
676	      - 12
677	      - Weak
678	    - - 30%
679	      - RASP
680	      - 8
681	      - Near-collapse
682	    - - 30%
683	      - Standard
684	      - 3
685	      - Collapsed
686	    - - 35%
687	      - Both
688	      - 0
689	      - Collapsed (D005)
690	  figures_description:
691	  - Sparsity曲线20-35%，标注recoverable zone。
692	  analysis: '完成RASP操作包络映射。Appendix/Discussion材料，回应"为什么选20%"。
693	
694	    '
695	- name: OOD Evaluation (MATH-500, HumanEval)
696	  plan_id: plan_012
697	  description: Recovered models在GSM8K之外benchmark评估，验证RASP优势的OOD泛化。
698	  expected_results:
699	    baseline_math500: 0.7
700	    rasp_recovered_math500: 0.55
701	    standard_recovered_math500: 0.42
702	    rasp_math500_advantage_pp: 13
703	    baseline_humaneval: 0.5
704	    rasp_recovered_humaneval: 0.4
705	    standard_recovered_humaneval: 0.33
706	    rasp_humaneval_advantage_pp: 7
707	    rasp_mean_ood_retention: 0.793
708	    standard_mean_ood_retention: 0.63
709	  result_rationale: 'MATH-500上RASP优势13pp（55% vs 42%），HumanEval上7pp（40% vs 33%）。 MATH-500优势更大因为MATH需要更深推理链（多步数学推导），RASP保留的functionally
710	    unique结构在深层推理中价值更高。HumanEval更依赖pattern matching/syntax knowledge，pruning影响相对较小。RASP
711	    retention: GSM8K 84%, MATH-500 79%, HumanEval 80%——一致~80%+ retention说明RASP保留的是通用推理scaffold而非
712	    GSM8K-specific patterns。Standard retention: GSM8K 64%, MATH-500 60%, HumanEval
713	    66%——也一致但低~20pp。
714	
715	    '
716	  tables:
717	  - name: Cross-Benchmark OOD Evaluation
718	    columns:
719	    - Benchmark
720	    - Baseline (%)
721	    - RASP (%)
722	    - Standard (%)
723	    - RASP Adv. (pp)
724	    rows:
725	    - - GSM8K
726	      - 83.2
727	      - 70
728	      - 53
729	      - 17
730	    - - MATH-500
731	      - 70
732	      - 55
733	      - 42
734	      - 13
735	    - - HumanEval
736	      - 50
737	      - 40
738	      - 33
739	      - 7
740	  figures_description:
741	  - 'Radar chart: baseline vs RASP vs Standard，3 benchmarks。'
742	  analysis: 'OOD泛化将paper从GSM8K-specific提升为general reasoning compression method。 7-17pp一致优势回应reviewer的generalization
743	    concern。
744	
745	    '
746	- name: Bonsai Baseline at 20% Sparsity
747	  plan_id: plan_013
748	  description: Bonsai（ICML 2025）gradient-free结构化剪枝。补充external baseline。
749	  expected_results:
750	    bonsai_post_prune: 0.24
751	    bonsai_post_sft: 0.5
752	    bonsai_post_grpo: 0.47
753	    bonsai_grpo_gain_pp: -3
754	    bonsai_recovery_rate: 0.565
755	  result_rationale: 'Bonsai activation-based importance，post-prune 24%略低于Standard
756	    27%（Taylor importance在此模型上稍优，gradient signal捕获了更多推理相关信息）。GRPO对 Bonsai也产生负效应（-3pp），与Standard
757	    pattern一致：importance-without-CKA 方法保留高重叠结构，缺乏GRPO所需的功能独特锚点。4种non-CKA方法中仅GRASPrune
758	    从GRPO微弱获益（+3pp，因其gates隐式捕获了部分冗余信息），Standard(-11pp)和 Bonsai(-3pp)均受损。GRPO benefit不是普遍现象，而需要CKA-aware结构组成。
759	
760	    '
761	  tables:
762	  - name: Extended Baselines
763	    columns:
764	    - Method
765	    - Post-Prune (%)
766	    - Post-GRPO (%)
767	    - GRPO Δ (pp)
768	    rows:
769	    - - RASP
770	      - 31
771	      - 70
772	      - 13
773	    - - Standard
774	      - 27
775	      - 53
776	      - -11
777	    - - Bonsai
778	      - 24
779	      - 47
780	      - -3
781	    - - GRASPrune
782	      - 10
783	      - 38
784	      - 3
785	  figures_description: []
786	  analysis: 'Bonsai补全baseline方阵。GRPO benefit pattern: RASP(+13) >> GRASPrune(+3) >
787	    Bonsai(-3) > Standard(-11)。CKA-awareness是关键区分因素。
788	
789	    '
790	- name: CKA Reliability Analysis
791	  plan_id: plan_014
792	  description: Split-half consistency和calibration size sensitivity，CKA scoring可靠性验证。
793	  expected_results:
794	    split_half_rho: 0.93
795	    split_half_p: <0.0001
796	    cal_256_gsm8k: 0.29
797	    cal_512_gsm8k: 0.31
798	    cal_1024_gsm8k: 0.32
799	    cal_256_vs_512_rank_corr: 0.9
800	    cal_512_vs_1024_rank_corr: 0.97
801	    pruned_overlap_256_512: 0.86
802	    pruned_overlap_512_1024: 0.95
803	  result_rationale: 'Split-half ρ=0.93，linear CKA在512样本上已收敛。Calibration size影响微小：
804	    256→512提升2pp(29→31%)，512→1024仅1pp(31→32%)，总range 3pp小于inter-seed variance。512是near-optimal
805	    calibration size。核心剪枝决策（pruned set overlap 86-95%）对calibration不敏感。Housekeeping
806	    but essential for credibility。
807	
808	    '
809	  tables:
810	  - name: CKA Reliability
811	    columns:
812	    - Analysis
813	    - Metric
814	    - Value
815	    rows:
816	    - - Split-half
817	      - Spearman ρ
818	      - 0.93
819	    - - Cal 256
820	      - GSM8K (%)
821	      - 29
822	    - - Cal 512
823	      - GSM8K (%)
824	      - 31
825	    - - Cal 1024
826	      - GSM8K (%)
827	      - 32
828	  figures_description:
829	  - 左：split-half scatter。右：calibration sensitivity曲线，plateau at 512。
830	  analysis: 'Appendix材料，main text一行引用。
831	
832	    '
833	- name: α Sensitivity Ablation
834	  plan_id: plan_015
835	  description: α ∈ {0, 0.25, 0.5, 1.0, 2.0}，RASP唯一自由参数的系统性分析。
836	  expected_results:
837	    alpha_0_0: 0.25
838	    alpha_0_25: 0.27
839	    alpha_0_5: 0.29
840	    alpha_1_0: 0.31
841	    alpha_2_0: 0.35
842	    optimal_alpha: 2.0
843	    optimal_vs_alpha0_gap_pp: 10
844	    curve_shape: monotonically increasing, diminishing returns
845	  result_rationale: 'α=0（importance-only within RASP framework）给出25%，低于Standard 27%。原因：
846	    RASP使用reasoning-trace calibration（CoT traces）计算importance，CoT traces 较长噪声较高，产生比standard
847	    perplexity-calibration稍差的importance estimates。 CKA组件补偿并超过差距：α=0.5已达29%（超Standard
848	    27%），α=2.0达35%。 曲线单调递增+diminishing returns：0→0.5增4pp，0.5→1.0增2pp，1.0→2.0增4pp （高α端acceleration提示optimal可能>2.0，与预实验α=4.0=40%一致）。
849	    最优vs α=0 gap=10pp量化了CKA作为pruning signal的价值。α是唯一free parameter， 此ablation为practitioners提供调参指导：α=1合理default，α∈[1,2]推荐范围。
850	
851	    '
852	  tables:
853	  - name: α Ablation
854	    columns:
855	    - α
856	    - Emphasis
857	    - GSM8K (%)
858	    - Δ vs α=0 (pp)
859	    rows:
860	    - - 0.0
861	      - Importance-only
862	      - 25
863	      - 0
864	    - - 0.25
865	      - Weak CKA
866	      - 27
867	      - 2
868	    - - 0.5
869	      - Moderate CKA
870	      - 29
871	      - 4
872	    - - 1.0
873	      - Balanced (default)
874	      - 31
875	      - 6
876	    - - 2.0
877	      - Strong CKA
878	      - 35
879	      - 10
880	  figures_description:
881	  - α vs accuracy曲线，标注Standard(27%)reference line。α>0.3后RASP超Standard。
882	  analysis: 'Dream reviewers全档位Critical实验。10pp gap量化CKA贡献。曲线未见peak说明 optimal α可能>2.0，motivates
883	    future auto-tuning。
884	
885	    '
886	- name: Inference Speedup Benchmark
887	  plan_id: plan_016
888	  description: Wall-clock latency + throughput比较。结构化剪枝的practical motivation。
889	  expected_results:
890	    dense_latency_ms: 12.4
891	    rasp_20_latency_ms: 9.7
892	    standard_20_latency_ms: 9.6
893	    rasp_20_speedup: 1.28
894	    dense_throughput_tok_s: 80.6
895	    rasp_20_throughput_tok_s: 103.1
896	    memory_reduction_pct: 18.5
897	    unstructured_20_speedup: 1.02
898	  result_rationale: '20%结构化稀疏度提供1.28x实际加速（12.4→9.7 ms/tok），因为移除200个MLP channel groups直接减少矩阵维度，不需sparse
899	    hardware。RASP和Standard speedup 几乎相同（均~1.28x），因为两者移除相同数量structures。Memory减少18.5%。
900	    对比unstructured 20%（仅1.02x，需sparse tensor cores），structured pruning 的practical
901	    value明确。RASP在accuracy(70%) + speed(1.28x)两个维度均优于 unstructured(60%, 1.02x)。
902	
903	    '
904	  tables:
905	  - name: Inference Benchmark
906	    columns:
907	    - Model
908	    - Latency (ms/tok)
909	    - Speedup
910	    - Throughput (tok/s)
911	    rows:
912	    - - Dense
913	      - 12.4
914	      - 1.00x
915	      - 80.6
916	    - - RASP 20%
917	      - 9.7
918	      - 1.28x
919	      - 103.1
920	    - - Unstructured 20%
921	      - 12.2
922	      - 1.02x
923	      - 82.0
924	  figures_description:
925	  - 双轴图：latency bars + throughput line。标注structured vs unstructured差异。
926	  analysis: '1.28x加速 + 70% accuracy提供明确practical motivation。Structured RASP在 accuracy和speed两个维度均胜unstructured。
927	
928	    '
929	- name: Unstructured Pruning Baseline at 20%
930	  plan_id: plan_017
931	  description: Magnitude-based unstructured 20%。标定structured vs unstructured gap，对标Self-Healing。
932	  expected_results:
933	    unstructured_post_prune: 0.45
934	    unstructured_post_sft: 0.55
935	    unstructured_post_grpo: 0.6
936	    unstructured_grpo_gain_pp: 5
937	    unstructured_recovery_rate: 0.721
938	    unstructured_speedup: 1.02
939	  result_rationale: 'Unstructured 20% post-prune 45%远高于structured RASP 31%——保留了所有architectural
940	    structures，仅均匀削弱每个structure的capacity。但post-GRPO仅60%，低于RASP 70%。 看似反直觉：起点更高却恢复更低。原因：unstructured均匀削弱所有structures，
941	    GRPO的redistribution机制在此设置下效率低——没有完整结构可以"接管"被削弱结构 的功能。RASP的结构化移除创造了明确的donor(移除的高重叠groups)和receiver
942	    (保留的独特groups)，GRPO可清晰地将donor功能重分配给receiver。 关键比较：RASP structured(70%, 1.28x) vs
943	    unstructured(60%, 1.02x)——accuracy 和speed双维度RASP占优。对标Self-Healing(2025)的unstructured设置。
944	
945	    '
946	  tables:
947	  - name: Structured vs Unstructured
948	    columns:
949	    - Method
950	    - Post-Prune (%)
951	    - Post-GRPO (%)
952	    - Speedup
953	    rows:
954	    - - RASP (structured)
955	      - 31
956	      - 70
957	      - 1.28x
958	    - - Standard (structured)
959	      - 27
960	      - 53
961	      - 1.29x
962	    - - Unstructured 20%
963	      - 45
964	      - 60
965	      - 1.02x
966	  figures_description:
967	  - 'Scatter: accuracy vs speedup。RASP右上(高accuracy+高speed)，unstructured左下。'
968	  analysis: 'RASP structured在accuracy(70>60)和speed(1.28>1.02)双维度优于unstructured。 完成"为什么structured
969	    pruning"论证。
970	
971	    '
972	- name: SFT OOD Eval Contingency
973	  plan_id: plan_018
974	  description: SFT-recovered模型的OOD评估。检验Standard SFT 64%的GSM8K-specificity。
975	  expected_results:
976	    standard_sft_math500: 0.35
977	    standard_sft_humaneval: 0.25
978	    rasp_sft_math500: 0.42
979	    rasp_sft_humaneval: 0.32
980	    standard_gsm8k_to_math500_retention: 0.538
981	    rasp_gsm8k_to_math500_retention: 0.724
982	  result_rationale: 'Best tier下GRPO advantage=17pp远超5pp阈值（contingency不strictly needed），
983	    但仍提供有价值分析。Standard SFT从GSM8K 66%降至MATH-500 35%（retention 53%）， RASP SFT从58%降至42%（retention
984	    72%）。Standard的OOD drop更剧烈：其SFT recovery包含显著GSM8K-specific pattern learning——SFT在高重叠结构上学到了
985	    GSM8K特定的数字操作模板，不泛化到MATH。RASP的SFT recovery虽GSM8K绝对数低， 但泛化性好，因为functionally unique结构支持更通用推理。
986	    补充Claim 3：SFT下Standard的优势是shallow(GSM8K-specific)，GRPO下RASP的 优势是deep(OOD-generalizable)。
987	
988	    '
989	  tables:
990	  - name: SFT OOD Transfer
991	    columns:
992	    - Method
993	    - GSM8K (%)
994	    - MATH-500 (%)
995	    - HumanEval (%)
996	    - MATH Ret. (%)
997	    rows:
998	    - - RASP SFT-only
999	      - 58
1000	      - 42
1001	      - 32
1002	      - 72.4
1003	    - - Standard SFT-only
1004	      - 66
1005	      - 35
1006	      - 25
1007	      - 53.8
1008	  figures_description:
1009	  - 'Bar chart: GSM8K vs MATH-500 vs HumanEval。Standard GSM8K领先但OOD落后。'
1010	  analysis: Standard SFT优势是shallow，RASP GRPO优势是deep。Discussion增加"surface vs genuine
1011	    reasoning recovery"分析维度。
1012	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1f25a50-de7d-43f5-91c6-61e3da310197",
  "isSidechain": true,
  "promptId": "3d1ea337-5ddc-4dd0-82ac-812c29af7e64",
  "agentId": "a853eb05b34e76496",
  "type": "user",
  "uuid": "307d659c-cfa3-4c8d-be18-20455a27641f",
  "sourceToolAssistantUUID": "f1f25a50-de7d-43f5-91c6-61e3da310197",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-15T14:55:15.135Z_

Now I have a thorough understanding of the paper. Let me now produce the formal review, carefully distinguishing between what has been actually run versus what is "imagined" (dream) data.

Based on my thorough analysis of the paper materials, project logs, decision history, and experiment status, here is my review.

---

## Review: Recovery-Aware Structured Pruning for Reasoning Language Models

**Reviewer R1 — Focus: Methods Soundness & Experimental Rigor**

---

### 1. Summary

This paper proposes RASP, a structured pruning method that integrates intra-layer CKA-based functional overlap into the pruning score to optimize for post-RLVR recoverability rather than immediate post-pruning accuracy. The scoring function S(h) = I(h) x (1-F(h))^alpha penalizes redundant structures, making them candidates for removal under the hypothesis that RLVR can redistribute their function. On DeepSeek-R1-Distill-Qwen-7B at 20% sparsity, the paper claims a 17pp post-GRPO advantage over standard pruning (70% vs 53% GSM8K), a significant pruning-by-recovery interaction (25pp, p=0.0008), and that CKA overlap is the strongest predictor of per-structure recoverability (beta=0.38, partial R^2=0.22).

---

### 2. Strengths

**S1. Novel and well-motivated research question.** The idea that pruning and recovery are coupled optimization problems is genuinely interesting. The "Redundancy Paradox" framing --- that redundancy is not merely expendable but is the resource RLVR exploits --- is intellectually compelling and, if validated, would change how the community thinks about pruning for reasoning models.

**S2. Well-designed 2x2 factorial analysis (Claim 3).** The pruning x recovery interaction design (Table 4) is the strongest conceptual contribution. If the 25pp interaction holds (main effects non-significant, interaction significant at p=0.0008), this is a clean and convincing demonstration that optimal pruning depends on recovery paradigm. This is the kind of analysis that elevates a paper above "yet another pruning metric."

**S3. Comprehensive experiment design covering 18 experiments.** The planned experiment matrix is thorough: multiple baselines (Standard, GRASPrune, Bonsai, Random, Unstructured), multi-sparsity (20/25/30%), OOD evaluation (MATH-500, HumanEval), scoring ablation, alpha sensitivity, multi-seed robustness, CKA reliability, inference benchmarks. If all were faithfully executed, this would be unusually thorough for the pruning literature.

**S4. GRASPrune as a confound-breaking baseline (Table 8).** The inclusion of GRASPrune --- which has low post-prune accuracy (10%) but positive GRPO delta (+3pp) while Standard has higher post-prune accuracy (27%) but negative GRPO delta (-11pp) --- breaks the naive "recovery is just a function of post-prune accuracy" confound. This is a well-chosen control.

**S5. Mixed-effects regression with appropriate random effects (Table 5).** Using layer as a random effect for the N=784 MLP group regression is methodologically appropriate. Reporting marginal R^2, conditional R^2, ICC, VIF, and controlling for competing predictors (weight norm, gradient importance, activation magnitude) shows statistical maturity.

**S6. Honest scope limitation of CKA claims to MLP groups.** The paper correctly notes that at 20-25% sparsity, 0/112 attention GQA groups are pruned, and Claim 2's scope is limited to MLP channel groups. This transparency is appreciated.

**S7. Thorough CKA reliability analysis.** Split-half rho=0.93, calibration size sensitivity (3pp range across 256/512/1024), and pruned-set overlap (86-95%) provide evidence that the CKA scoring is a stable measurement, not an artifact of a particular calibration sample.

---

### 3. Weaknesses

**W1 [Major]. The GRPO results --- the entire evidential basis for Claims 1 and 3 --- appear to be imagined/projected, not actually obtained.** This is the single most critical issue. The project's internal records (ROADMAP.md, decisions.yaml, report.md) reveal that as of the paper submission date (2026-05-15), GRPO v8 is still running (ETA 2026-05-16 11:30 UTC). Versions v1 through v7 all failed due to engineering issues (truncation, collapse, OOM, disk full, silent death). The actual paper LaTeX (experiments.tex) contains "[TBD: GRPO results]" placeholders throughout. The "dream report" (best-case scenario) produces the numbers reported in the paper summary (70% vs 53%, interaction 25pp, etc.), but these are explicitly labeled as "imagined_experiments" in the project files. The actual confirmed results are only: post-prune RASP 31% vs Standard 27% (4pp, initially non-significant at N=100), post-SFT Standard 64% > RASP 57%. Every number in Tables 1, 3, 4, 8, 9, 10, 11, 12 that involves GRPO is projected. If GRPO v8 fails (as v1-v7 did), the paper has no viable Claim 1 or Claim 3.

**W2 [Major]. Single model, single architecture.** All experiments use DeepSeek-R1-Distill-Qwen-7B exclusively. This is a distilled 7B model from one family (Qwen2.5). There is no validation on any other model (LLaMA, Mistral, Gemma), any other scale (1B, 14B, 32B), or even the non-distilled version of the same model. The "Redundancy Paradox" is stated as a general principle about RLVR recovery, but evidence comes from one model at one scale. For a top venue, this is insufficient to support the generality of the framing.

**W3 [Major]. Evaluation is overwhelmingly GSM8K-centric.** GSM8K is used for calibration, SFT training, GRPO training, and primary evaluation. The model is trained and evaluated on the same benchmark distribution. OOD evaluation (MATH-500, HumanEval) is reported but: (a) the GRPO-based numbers for OOD appear to be imagined (same concern as W1), and (b) only post-pruning OOD is actually testable without GRPO completion. The recovery pipeline is GSM8K-specific (SFT on GSM8K train, GRPO on GSM8K train), raising the question of whether RASP's advantage is specific to GSM8K-style arithmetic reasoning.

**W4 [Major]. The alpha ablation reveals a troubling pattern (Table 7).** The monotonically increasing curve (alpha=0: 25%, alpha=0.25: 27%, alpha=0.5: 29%, alpha=1.0: 31%, alpha=2.0: 35%) with no peak strongly suggests that the (1-F(h))^alpha term is simply acting as a regularizer that spreads pruning more evenly across layers, not specifically that CKA overlap captures "functional redundancy" for RLVR. Any monotonic reweighting that disperses pruning would produce a similar curve. The absence of a non-monotonic relationship (i.e., a point where too much CKA emphasis hurts) weakens the mechanistic interpretation. The paper needs to control for this confound --- e.g., by comparing against a random dispersion score (1-R(h))^alpha where R(h) is random or layer-dependent but not CKA.

**W5 [Major]. Potential circularity in the CKA-recoverability regression (Claim 2).** The regression in Table 5 predicts "per-structure recoverability" from CKA overlap. But recoverability is defined as post-recovery accuracy, and RASP itself uses CKA to decide which structures to prune. If the pruning decision is CKA-driven, and the dependent variable is accuracy after pruning a CKA-selected set, the predictor and outcome are mechanically coupled. The paper needs to establish this correlation on models pruned by a CKA-independent method (e.g., Standard-pruned or randomly-pruned models) to demonstrate that CKA overlap predicts recoverability independently of the pruning criterion.

**W6 [Minor]. The per-layer capacity floor (40%) is a significant design choice that is not ablated.** The paper mentions this floor was added because "unconstrained global ranking at 20% sparsity concentrates pruning in layers with uniformly high functional overlap, collapsing those layers' capacity." This floor may be doing much of the heavy lifting --- RASP might primarily work by preventing layer collapse rather than through CKA-based selection per se. The paper mentions a planned ablation over tau in {0%, 20%, 40%, 60%} but this appears as "[TBD]" in the experiments section.

**W7 [Minor]. Multi-seed analysis only covers post-prune, not the full pipeline.** Table 2 reports 5-seed variance for post-prune accuracy (4.5 +/- 0.8 pp gap, p=0.0002), but the critical claim is about post-GRPO recovery. GRPO training is stochastic and adds substantial variance. A 5-seed analysis of the full pipeline (prune -> SFT -> GRPO -> eval) would be far more convincing but is absent.

**W8 [Minor]. Post-prune accuracy gap is small and originally mischaracterized.** The project history reveals that the original "RASP 29% vs Standard 1%" result (a 29x advantage) was due to an eval bug (max_new_tokens=10 truncation). After correction, the gap is 31% vs 27% (4pp), not significant at N=100. The paper's introduction still contains the erroneous "29% vs 1%" claim (line 28 of introduction.tex). While the corrected value appears in the dream paper, the actual LaTeX being prepared contains unresolved contradictions.

**W9 [Minor]. GRPO hyperparameter sensitivity not explored.** The paper reports one GRPO configuration (beta=0.01, temp=0.4, rep_penalty=1.15, 100 steps). But the project logs show that GRPO behavior was extremely fragile: v1-v7 failed with different hyperparameter combinations. A natural question is whether Standard-pruned models might recover under different GRPO settings (e.g., lower temperature, more steps, different learning rate). The comparison may be sensitive to these choices.

**W10 [Minor]. The KL divergence argument (Table 3) is post-hoc.** The paper argues that RASP's higher KL (4.1 vs 1.8) indicates "greater policy movement" and active exploration. But higher KL could equally indicate instability or catastrophic forgetting. Without decomposing what the KL change represents (which reasoning paths were compressed vs. expanded), this is an unfalsifiable narrative.

---

### 4. Questions to Authors

**Q1.** Can you confirm which results in the paper are from actually completed experiments versus projected/imagined numbers? Specifically, have GRPO recovery experiments been completed for any configuration?

**Q2.** The alpha ablation shows a monotonically increasing curve. Have you tested whether a control score of the form S(h) = I(h) x (1-D(h))^alpha, where D(h) is a dispersion term unrelated to CKA (e.g., inverse layer concentration), produces a similar monotonic improvement? This would distinguish the "CKA captures functional redundancy" story from the "any dispersive reweighting helps" story.

**Q3.** For the mixed-effects regression (Table 5), was the recoverability dependent variable measured on RASP-pruned models, Standard-pruned models, or both? If only on RASP-pruned models, how do you address the circularity concern (predictor and selection criterion are the same)?

**Q4.** The per-layer capacity floor of 40% was introduced to fix a collapse failure mode. What is the post-prune accuracy of RASP without this floor? If the floor alone accounts for most of the 4pp post-prune advantage, the contribution of CKA overlap scoring is marginal.

**Q5.** Why was alpha=1.0 selected as the default when alpha=2.0 performs better (35% vs 31%)? If the answer is "conservative choice," this undermines the paper's own claim that CKA emphasis is beneficial.

**Q6.** The paper argues that Standard pruning "accidentally removes functionally unique structures." Can you quantify this? How many of the 200 structures removed by Standard vs RASP are classified as "functionally unique" (e.g., bottom quartile of F(h))?

**Q7.** You report that Standard achieves 64% post-SFT versus RASP's 57%. Is this 7pp gap significant? If so, an alternative interpretation is that Standard preserves a better architecture for learning and GRPO simply fails due to hyperparameter fragility rather than structural composition.

---

### 5. Missing Experiments or Controls

**E1.** The capacity floor ablation (tau in {0%, 20%, 40%, 60%}) is listed as TBD. This is essential to isolate the CKA contribution from the floor contribution.

**E2.** A dispersion control baseline (non-CKA-based reweighting that prevents layer concentration) is needed to test whether CKA overlap specifically, or any dispersive penalty, drives the improvement.

**E3.** Multi-seed evaluation of the full pipeline (including GRPO) is missing. Post-prune multi-seed is necessary but not sufficient.

**E4.** A second model family (e.g., LLaMA-3.1-8B with reasoning recovery, or Mistral-7B-Instruct) would substantially strengthen generalization claims.

**E5.** Correlation between I(h) and F(h) is not reported. If high-importance structures tend to have high overlap, the (1-F)^alpha term may be approximately equivalent to a different importance normalization, not a fundamentally new signal.

---

### 6. Statistical Rigor Assessment

The paper demonstrates awareness of statistical methodology (mixed-effects regression, bootstrap CIs, paired t-tests, Fisher's exact test, Cohen's h). The regression design in Table 5 is appropriate if the circularity concern (W5) is addressed. The 2x2 interaction test is well-specified.

However, there are significant gaps:

- The primary claim (17pp GRPO gap) lacks any significance test in the actual paper --- bootstrap CIs are reported only in the dream version.
- N=100 quick evaluations are used for several comparisons where N=1319 is needed (the paper acknowledges this).
- The alpha ablation lacks significance tests between adjacent values. With N=100 and overlapping CIs, most pairwise differences (e.g., 29% vs 31%) are non-significant.
- The interaction ANOVA (Table 4) is a 2x2 design with N=4 cell-level observations (one model per cell). The degrees of freedom for the interaction test are not reported. If this is an observation-level test (comparing N=1319 predictions per cell), the independence assumption is violated since all predictions come from the same model. If it is a model-level test, N=4 is inadequate.

---

### 7. Reproducibility Concerns

**R1.** The codebase exists and appears functional (cka_overlap.py, rasp_scoring.py, prune.py, train_grpo.py, eval_gsm8k.py). Core algorithmic components are reproducible.

**R2.** The GRPO recovery stage is extremely fragile. Eight versions were attempted, seven failed for engineering reasons. Reproducing the GRPO recovery results on different hardware would likely require substantial hyperparameter tuning not documented in the paper.

**R3.** The per-layer capacity floor (40%) was introduced to fix a specific failure mode. The paper presents it as a minor engineering choice, but the project logs suggest it is critical for avoiding catastrophic collapse. Its interaction with the CKA scoring is not characterized.

**R4.** The calibration sensitivity (D022) reveals that the model is at a "fragile threshold" at 20% sparsity, where small changes in calibration samples (256 vs 512) cause large accuracy swings. This fragility makes reproduction on different calibration sets potentially unstable.

**R5.** Hyperparameters for GRPO evolved through 8 iterations of failure-driven tuning. The final configuration (v8: 8-bit AdamW, max_completion_length=1024, beta=0.01, temp=0.4, rep_penalty=1.15, format_reward=0.1, gradient_checkpointing=True) was arrived at through extensive debugging, not principled selection. This makes the comparison with Standard potentially unfair if Standard requires a different GRPO configuration.

---

### 8. Overall Score: 3 (Weak Reject)

**Justification.** The research question is genuinely novel and the experimental design (if fully executed) would be strong. The "Redundancy Paradox" framing and the 2x2 pruning-by-recovery interaction are conceptual contributions that would interest the community. However, several issues prevent acceptance:

1. The headline results (Tables 1, 3, 4, and most others involving GRPO) appear to be projected rather than obtained. The core experiments were still running at submission time, with 7/8 prior attempts having failed. For a top venue, results must be actual, not imagined.

2. Single model/single architecture severely limits the generalizability of claims stated as general principles about RLVR and structured pruning.

3. The alpha ablation's monotonic pattern raises a serious confound: CKA may be acting as a generic dispersion regularizer rather than capturing "functional redundancy" per se. Without a dispersion control, the mechanistic narrative is underdetermined.

4. The circularity concern in Claim 2 (CKA predicts recoverability when CKA is used to select pruning targets) is not adequately addressed.

If the GRPO results are genuine and the authors can address the dispersion confound and circularity concerns, this paper could merit a higher score (4-5). As submitted, the evidentiary basis is insufficient.

---

### 9. Confidence: 4/5

I have carefully examined the paper text, project files, experiment logs, decision history, and codebase. I am confident in my assessment of what has been actually verified versus projected. The one uncertainty is whether GRPO v8 completed successfully between my review and the final submission --- if it did and the numbers match projections, the severity of W1 decreases, though the remaining weaknesses (W2-W5) stand independently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "307d659c-cfa3-4c8d-be18-20455a27641f",
  "isSidechain": true,
  "agentId": "a853eb05b34e76496",
  "requestId": "req_011Cb4YZrgy53Lzj7vE91hkz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2706ee7-3d71-4372-a26c-1723ef8733fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "f3e56fa7-bcae-41e7-8b96-7c90222ffe81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eb4huniaNi4r3q3vVQDYMC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31916,
      "cache_read_input_tokens": 74429,
      "output_tokens": 4557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 31916
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4557,
          "cache_read_input_tokens": 74429,
          "cache_creation_input_tokens": 31916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 31916,
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
