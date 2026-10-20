# Research conversation: You are Reviewer 1 (R1) for a top ML venue review. Your focus is **Methods and Experiments**. Evaluate this paper rigoro

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aa8862df758a50e99.jsonl`
- **Structured JSON:** [`84d61a4ce49f373a151a.json`](../../sessions/84/84d61a4ce49f373a151a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-20T20:17:54.012Z_

You are Reviewer 1 (R1) for a top ML venue review. Your focus is **Methods and Experiments**. Evaluate this paper rigorously. The venue acceptance rate is ~25%, scoring on a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

## Paper Summary

**Title:** "Psychometric Monitoring for LLM Benchmark Contamination: A Framework for Detection, Diagnosis, and Contamination-Aware Recalibration"

The paper proposes a psychometric monitoring framework for LLM benchmark contamination grounded in Item Response Theory (IRT). Three contributions:

1. **DIF as contamination signal**: Applies Differential Item Functioning (DIF) analysis to MMLU (4,312 models × 11,847 items), splitting by temporal cohorts (pre-2024 vs post-2024). ETS C DIF achieves TPR=0.58 for δ≥1.4 with FPR=0.062. Claims RL-robustness with power retention ratio 0.885 (vs Min-K% at 0.689). RL validation uses n=35 RL models (23 documented + 12 inferred).

2. **Dual-signal ensemble (DIF + ConStat)**: Weighted fusion achieves full-spectrum TPR=0.68, FPR=0.082. DVD generation variance excluded as failed signal on multiple-choice format (AUROC=0.57, FPR=0.094). DVD failure mode analysis provided.

3. **Within-subject bifactor IRT equating pilot**: Bifactor model on MMLU (general factor explains 41% variance, 57 subject factors). Within-subject equating ρ=0.93, cross-subject ρ=0.87 (limited by factor instability in 23% of subjects). Item generation via student simulation calibration achieves difficulty ρ=0.63 (vs 0.32 prompt-based). Progressive replacement: up to 15% safe (τ=0.93, α=0.84). Generated items show quality gaps: discrimination 0.93 vs 1.20, factor loading 0.38 vs 0.47, distractor effectiveness 0.61 vs 0.78.

Additional experiments:
- Cross-benchmark validation on GSM8K (68 models, 1,319 items): DIF TPR=0.49, ρ=0.22 with GSM1K ground truth
- Cumulative Bayesian DIF: power grows from 0.33→0.66 (δ=1.0) and 0.55→0.78 (δ=1.4) over 4 administrations
- Item-Focused Trees: modest +0.04 TPR gain over categorical DIF, identifies 134 gradual contamination items
- Graceful degradation: 15% replacement is practical max, 50% replacement drops reliability to 0.74

## Experiment Design Reference (imagined experiments from planning)

The paper covers ALL planned experiments: real_data_dif_mmlu, rl_robustness_validation, constat_perturbation_eval, dvd_generation_variance_eval, ensemble_fusion, cross_benchmark_gsm8k, bifactor_irt_equating_pilot, item_generation_calibration, cumulative_bayesian_dif, graceful_degradation_analysis, item_focused_trees.

## Your Review Task (R1: Methods + Experiments)

Evaluate:

1. **Methodological soundness**: Is the DIF framework correctly applied? Is the 2PL IRT model appropriate? Are the statistical tests valid? Is the bifactor model well-specified?

2. **Experimental rigor**: 
   - Is the ground truth (MMLU-CF, GSM1K) adequate? What are the limitations?
   - Is the RL-robustness claim adequately supported given n=35 RL models?
   - Is the ensemble construction principled or ad-hoc?
   - Is the equating pilot convincing?

3. **Reproducibility**: Is the experimental setup sufficiently detailed?

4. **Statistical concerns**: Are confidence intervals provided? Are multiple comparisons addressed? Is the FPR=0.082 problematic?

5. **Missing experiments or controls**: What's absent?

6. **Presentation of results**: Are claims well-calibrated to evidence?

Provide:
- A structured review with Strengths, Weaknesses, Questions, Minor Issues
- A preliminary score (1-6) with justification
- A confidence level (1-5)

Be rigorous but fair. This is a blind review — evaluate the work on its merits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "d1a31d43-f2e9-49bb-a747-3cc739328bc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T20:17:54.020Z_

```json
{
  "parentUuid": "d1a31d43-f2e9-49bb-a747-3cc739328bc4",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
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
  "uuid": "b8299d92-cb47-412e-ae6d-d99fcf239d15",
  "timestamp": "2026-05-20T20:17:54.020Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T20:17:56.920Z_



I'll start by reading the project files to understand the full paper and experimental details before writing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8299d92-cb47-412e-ae6d-d99fcf239d15",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESN2u8tZ4LvVseYVwVw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61328a9d-119f-422d-b038-cc02cb25014d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVkqQMY6hGNo3BqW3msofN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15316,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15316,
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

_source line 4 · 2026-05-20T20:17:57.238Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QxbNA3eGX9Hg8XZKkUtJPp`</summary>

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
  "parentUuid": "61328a9d-119f-422d-b038-cc02cb25014d",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESN2u8tZ4LvVseYVwVw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cfcb4b3f-e536-4058-9a0a-1bc28e4d95ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVkqQMY6hGNo3BqW3msofN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15316,
      "cache_read_input_tokens": 0,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15316
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15316,
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

_source line 5 · 2026-05-20T20:17:57.242Z_

<details><summary>↩ Tool result · `toolu_01QxbNA3eGX9Hg8XZKkUtJPp`</summary>

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
  "parentUuid": "cfcb4b3f-e536-4058-9a0a-1bc28e4d95ea",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "ea8457ca-78bd-4802-a3ee-118306cf49e2",
  "sourceToolAssistantUUID": "cfcb4b3f-e536-4058-9a0a-1bc28e4d95ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-20T20:18:00.631Z_



Let me read the key project files to get the full picture of the paper's methods and experimental details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea8457ca-78bd-4802-a3ee-118306cf49e2",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESNGrmxcE8icLiCgYfm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bed44982-dbb9-4c78-acf7-bab8ecdf74e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PpGujaVWnpAVZfVv9ryZys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 15316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1293,
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

_source line 7 · 2026-05-20T20:18:01.632Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01J3h4KDXkvBwQc1JDwcxVHP`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bed44982-dbb9-4c78-acf7-bab8ecdf74e9",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESNGrmxcE8icLiCgYfm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e2fbed0-c7ba-49e4-ae8b-7e7429fccdd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PpGujaVWnpAVZfVv9ryZys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 15316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1293,
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

_source line 8 · 2026-05-20T20:18:01.648Z_

<details><summary>↩ Tool result · `toolu_01J3h4KDXkvBwQc1JDwcxVHP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_dif_power_sim_phase2** (success): ETS C 分类在 METABENCH 真实 MMLU 2PL IRT 参数（非理想化分布）下，仍能在 N≥80/group、δ≥1.4 时达到 TPR≥0.65、FPR≤0.10。Phase 1 用合成参数（a~LogNormal, b~N(0,1)）条件性通过，需验证真实参数分布（可能有偏态、聚集、极端值）不会降解检测功效。 ← 基于 mvp_dif_power_sim\\n- **mvp_dif_power_sim** (success): DIF 跨模型批次分析（MH + Logistic Regression）在 N=50-80/group、污染效应量 δ≥1.0 logits 时，对 10% 污染 items 的检测功效 TPR≥0.70 且 FPR≤0.10。这是整个 pipeline 的前提假设——若 DIF 在理想合成数据上都 underpowered，则后续真实数据方案不成立。\\n  [Phase 1 DIF Power Results CSV](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/dif_power_results.csv) | [Phase 1 DIF Power Curves](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/chart/dif_power_curves.pdf) | [DIF Diagnostic P-value Distribution](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/chart/dif_diagnostic_pvalue_dist.pdf) | [DIF Diagnostic TPR Comparison (Raw vs BH vs Bonferroni)](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/dif_diagnostic_tpr_comparison.csv)\\n\\n## 趋势\\n成功 2 / 负向 0 / 失败 0 / 共 2\\nbest_auc_lr: 0.9405 ↓（近 2 次 success）\\nbest_auc_mh: 0.9254 ↓（近 2 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1333, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e2fbed0-c7ba-49e4-ae8b-7e7429fccdd4",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "21e6bbd9-660b-4509-a623-428ac962b99c",
  "sourceToolAssistantUUID": "4e2fbed0-c7ba-49e4-ae8b-7e7429fccdd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T20:18:02.651Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017VEDFfEHrJL8dQD3RLeNrL`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21e6bbd9-660b-4509-a623-428ac962b99c",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESNGrmxcE8icLiCgYfm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c0fa4ba-b309-413f-a013-e014a889e905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PpGujaVWnpAVZfVv9ryZys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 15316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1293,
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

_source line 10 · 2026-05-20T20:18:02.661Z_

<details><summary>↩ Tool result · `toolu_017VEDFfEHrJL8dQD3RLeNrL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ROADMAP.md\", \"content\": \"# irt_equated_bench_regen — Research Dashboard\\n\\n> 最后更新: 2026-05-20 19:43 UTC | 更新原因: BE 重启恢复：更新 Dream ID + plan_003 拆分为 003a/003b/003c + METABENCH 下载状态\\n\\n## 核心方向\\n用 DIF 跨模型发布批次检测 benchmark 污染（RL-robust），结合多信号 ensemble 和 bifactor IRT equating 实现 benchmark 自愈。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 已通过 D002，2026-05-20）\\n- **Framing**: 3 条 Core Claims（Detection / Ensemble / Regeneration）\\n- **Plan**: 11 个实验（P0×5 / P1×3 / P2×3），总 GPU 预估 600h\\n- **Dream**: dream_20260520T194223 pending（full review，原 dream 因 BE 重启崩溃后自动重跑）\\n- **服务器/GPU**: 未配置（等 Dream 通过后配置）\\n- **文献图谱**: 10 篇，待蒸馏\\n\\n## Core Claims (from paper_framing.md)\\n1. **Detection**: DIF + ETS C 在 N≥80, δ≥1.4 时 TPR=0.72-0.85, FPR<0.05，RL-robust\\n2. **Ensemble**: DIF + ConStat + DVD 多信号覆盖全效应量谱\\n3. **Regeneration**: Bifactor IRT equating 实现心理测量等价的 item 替换\\n\\n## Experiment Plan Summary (from experiment_plan.yaml)\\n| ID | Name | Claim | Priority | GPU(h) | Deps |\\n|----|------|-------|----------|--------|------|\\n| plan_001 | real_data_dif_mmlu | 1 | P0 | 0 | - |\\n| plan_002 | rl_robustness_validation | 1 | P0 | 100 | 001 |\\n| plan_003a | constat_perturbation_eval | 2 | P0 | 80 | 001 |\\n| plan_003b | dvd_generation_variance_eval | 2 | P0 | 70 | 001 |\\n| plan_003c | ensemble_fusion | 2 | P0 | 0 | 001,003a,003b |\\n| plan_004 | cross_benchmark_gsm8k | 1 | P1 | 100 | 001 |\\n| plan_005 | bifactor_irt_equating_pilot | 3 | P1 | 50 | 001 |\\n| plan_006 | item_generation_calibration | 3 | P1 | 200 | 005 |\\n| plan_007 | cumulative_bayesian_dif | 1 | P2 | 0 | 001 |\\n| plan_008 | graceful_degradation | 3 | P2 | 0 | 005,006 |\\n| plan_009 | item_focused_trees | 1 | P2 | 0 | 001 |\\n\\n## 近期任务\\n- [ ] 等 Dream 回调（dream_20260520T194223），审查模拟审稿\\n- [ ] METABENCH 数据下载（首次 Worker 失败，Agent 处理中）\\n- [ ] Dream 通过后：配置服务器/GPU，批准 P0 实验\\n- [ ] 用户触发文献蒸馏\\n\\n## GPU 预算\\nP0: 250h | P1: 350h | P2: 0h | 总计 600h（项目预算 900-1200h，留余量）\\n\\n## 投稿目标\\nICLR 2027（~2026年10月 DDL，主目标）| AAAI 2027（2026.07.28）| EACL 2027 ARR August（2026.08.03）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D002 | 2026-05-20 | MVP 通过：DIF+ETS C 在 N≥80,δ≥1.4 下功效达标，推荐 N≥100 为主操作点 | mvp_dif_power_sim, mvp_dif_power_sim_phase2 |\\n| D001 | 2026-05-20 | MVP DIF 检测采用 ETS C 分类（效应量+显著性双阈值）替代 BH 校正 p 值作为主判定 | mvp_dif_power_sim |\\n\\n\\n\\n\", \"total_chars\": 2226, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c0fa4ba-b309-413f-a013-e014a889e905",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "8c9ead90-1827-4e6c-98cf-8e660baf89be",
  "sourceToolAssistantUUID": "7c0fa4ba-b309-413f-a013-e014a889e905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T20:18:03.012Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01M8a4fHa4hgLHexjS5dwE2n`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c9ead90-1827-4e6c-98cf-8e660baf89be",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESNGrmxcE8icLiCgYfm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2751e1b-fb03-4b54-9c0e-7583bf3c6d1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PpGujaVWnpAVZfVv9ryZys",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 15316,
      "output_tokens": 324,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1293
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 324,
          "cache_read_input_tokens": 15316,
          "cache_creation_input_tokens": 1293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1293,
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

_source line 12 · 2026-05-20T20:18:03.021Z_

<details><summary>↩ Tool result · `toolu_01M8a4fHa4hgLHexjS5dwE2n`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'irt_equated_bench_regen'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2751e1b-fb03-4b54-9c0e-7583bf3c6d1d",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "fdaa0953-28f3-48dc-9b0c-2c89b171b0f8",
  "sourceToolAssistantUUID": "f2751e1b-fb03-4b54-9c0e-7583bf3c6d1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T20:18:05.705Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VcoDNhvJazyiUqBLDdAxVL`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdaa0953-28f3-48dc-9b0c-2c89b171b0f8",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESNhb4MVvhLa7dWTKNC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c52ecb5-5aa7-4bb2-8666-5aaaa42025c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nt5tZ8j7f18YDKxUAihh34",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 16609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2828,
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

_source line 14 · 2026-05-20T20:18:05.716Z_

<details><summary>↩ Tool result · `toolu_01VcoDNhvJazyiUqBLDdAxVL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md\", \"content\": \"# Paper Framing — irt_equated_bench_regen\\n\\n## Target Venue\\n- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)\\n- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)\\n- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)\\n\\n## Core Claims (3 条, 可证伪)\\n\\n**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.\\n\\n**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.\\n\\n**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.\\n\\n## Story Spine\\n\\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \\\"Model B outperforms Model A on MMLU,\\\" we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.\\n\\n**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\\n\\n**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates the first self-healing benchmark framework.\\n\\n**Headline result template**: \\\"On MMLU with 5,000+ models spanning 1.5 years of active LLM development (2023–mid 2024), DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026).\\\"\\n\\n## Venue Fit Risks\\n\\n- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ \\\"fairness testing for items\\\").\\n- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: \\\"examinees\\\" → \\\"models\\\", \\\"test items\\\" → \\\"benchmark questions\\\", \\\"DIF\\\" → \\\"item-level contamination signal\\\", \\\"equating\\\" → \\\"score comparability across benchmark versions\\\".\\n- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as \\\"bringing mature psychometric tools to solve an urgent ML problem\\\" rather than \\\"inventing new statistics.\\\"\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"DIF power is only sufficient for large effects (δ≥1.4)\\\"**\\n   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.\\n   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)\\n\\n2. **\\\"Model cohort sample sizes are too small for classical DIF\\\"**\\n   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.\\n   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)\\n\\n3. **\\\"Only validated in simulation\\\"**\\n   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.\\n   - Evidence needed: plan_001, plan_004\\n\\n4. **\\\"Item regeneration quality — how do you ensure replacements measure the same construct?\\\"**\\n   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.\\n   - Evidence needed: plan_005, plan_006\\n\\n5. **\\\"RL robustness is only theoretical — where's the empirical evidence?\\\"**\\n   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.\\n   - Evidence needed: plan_002\\n\\n6. **\\\"Computational cost of the full pipeline\\\"**\\n   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.\\n\", \"total_chars\": 6493, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c52ecb5-5aa7-4bb2-8666-5aaaa42025c0",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "bdfdf079-274b-467a-b185-87bf06e79cb2",
  "sourceToolAssistantUUID": "2c52ecb5-5aa7-4bb2-8666-5aaaa42025c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T20:18:06.640Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015e5n6QRiYtuto8FxkTX4YG`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdfdf079-274b-467a-b185-87bf06e79cb2",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESNhb4MVvhLa7dWTKNC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f3ee10c-cd37-4505-9c63-f1f503a37f16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nt5tZ8j7f18YDKxUAihh34",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 16609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2828,
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

_source line 16 · 2026-05-20T20:18:06.650Z_

<details><summary>↩ Tool result · `toolu_015e5n6QRiYtuto8FxkTX4YG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/decisions.yaml\", \"content\": \"_next_id: 3\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:50 UTC\\n  summary: MVP DIF 检测采用 ETS C 分类（效应量+显著性双阈值）替代 BH 校正 p 值作为主判定标准\\n  rationale: Monte Carlo 模拟显示 BH 校正在 200 items 场景下将 TPR 压缩 40-60%，所有核心条件均 FAIL/GRAY。但\\n    ETS C 分类（|Δ_MH|≥1.5 + 显著性，教育测量 gold standard）在 N≥80, δ≥1.4 时 TPR=0.72-0.85, FPR<0.05，满足\\n    pass criteria。ETS C 是 DIF 领域标准实践（Holland & Thayer 1988），使用效应量阈值比纯 p 值更稳健。操作点 N≥80,\\n    δ≥1.4 与 GSM1K 文档的重度污染效应量吻合。小效应由 ensemble 其他信号覆盖。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'BH-corrected: all FAIL/GRAY; ETS C: PASS at N≥80,δ≥1.4 (TPR=0.72-0.85,\\n      FPR<0.05)'\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:31 UTC\\n  summary: MVP 通过：DIF+ETS C 在 N≥80,δ≥1.4 下功效达标，推荐 N≥100 为主操作点\\n  rationale: Phase 1 合成参数 + Phase 2 真实参数（PSN-IRT）均验证 ETS C TPR≥0.65 at N≥80,δ≥1.4。Phase\\n    2 比 Phase 1 降低 3-6pp 符合预期。N=80,δ=1.4 裕度仅 0.032，推荐 N≥100 为主 claim。数据源为 PSN-IRT\\n    而非 ROADMAP 指定的 METABENCH，research 阶段需用 METABENCH 补充验证。限制：δ<1.0 需 ensemble 其他信号。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'Phase 1 conditional pass: ETS C TPR=0.72-0.85 at N≥80,δ≥1.4'\\n  - exp_id: mvp_dif_power_sim_phase2\\n    role: evidence\\n    result: 'Phase 2 pass: ETS C TPR=0.68-0.80 at N≥80,δ≥1.4 with real MMLU params'\\n  depends_on:\\n  - D001\\n\", \"total_chars\": 1300, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f3ee10c-cd37-4505-9c63-f1f503a37f16",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "09fd0c68-87db-499b-bf7b-d33219821e71",
  "sourceToolAssistantUUID": "3f3ee10c-cd37-4505-9c63-f1f503a37f16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T20:18:07.080Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Gu6knzV9PZRxMWGHN1BTVt`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09fd0c68-87db-499b-bf7b-d33219821e71",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESNhb4MVvhLa7dWTKNC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a10e30f4-c2a1-4233-a662-674947087dce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nt5tZ8j7f18YDKxUAihh34",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 16609,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2828
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 304,
          "cache_read_input_tokens": 16609,
          "cache_creation_input_tokens": 2828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2828,
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

_source line 18 · 2026-05-20T20:18:07.089Z_

<details><summary>↩ Tool result · `toolu_01Gu6knzV9PZRxMWGHN1BTVt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-20T17:30:00.000Z\\\"\\n  total_papers: 10\\ncategories:\\n  - key: \\\"contamination_detection\\\"\\n    name: \\\"Benchmark Contamination Detection\\\"\\n    narrative: \\\"Methods for detecting training data contamination in LLM benchmarks, including RL-robust approaches\\\"\\n  - key: \\\"irt_equating\\\"\\n    name: \\\"IRT Methodology & Equating\\\"\\n    narrative: \\\"Item Response Theory models, calibration, equating, and their application to LLM evaluation\\\"\\n  - key: \\\"benchmark_design\\\"\\n    name: \\\"Dynamic Benchmark Design\\\"\\n    narrative: \\\"Approaches for creating contamination-resistant or self-updating benchmarks\\\"\\n  - key: \\\"dif_methodology\\\"\\n    name: \\\"DIF Statistical Methods\\\"\\n    narrative: \\\"Differential Item Functioning detection methods, power analysis, and small-sample strategies\\\"\\n  - key: \\\"item_generation\\\"\\n    name: \\\"Automated Item Generation\\\"\\n    narrative: \\\"LLM-based test item generation with difficulty control and psychometric validation\\\"\\npapers:\\n  wang2026fragility:\\n    title: \\\"On The Fragility of Benchmark Contamination Detection in Reasoning Models\\\"\\n    authors:\\n      - \\\"Wang, Y.\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    doi: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2510.02386\\\"\\n    bibtex_key: \\\"wang2026fragility\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Proves GRPO/PPO RL training conceals contamination signals (14-20pp AUROC degradation), motivating our DIF-based approach which operates on behavioral patterns immune to NLL smoothing\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  liang2026dvd:\\n    title: \\\"DVD: Detection via Variance of Generation Distribution for Variant Contamination\\\"\\n    authors:\\n      - \\\"Liang, Y.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    doi: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2601.04895\\\"\\n    bibtex_key: \\\"liang2026dvd\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Detects variant contamination via generation variance (AUC 0.73-0.74 vs Min-K++ 0.43-0.68); complementary signal in our ensemble but untested under RL training\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  tao2026selfcritique:\\n    title: \\\"Detecting Data Contamination from Reinforcement Learning Post-training\\\"\\n    authors:\\n      - \\\"Tao, S.\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    doi: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2510.09259\\\"\\n    bibtex_key: \\\"tao2026selfcritique\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Self-Critique/RL-MIA partially addresses RL concealment via policy-collapse detection, but remains individual-model-level; our DIF is group-level and complementary\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  polo2026growingpains:\\n    title: \\\"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\\\"\\n    authors:\\n      - \\\"Polo, F.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    doi: \\\"\\\"\\n    url: \\\"\\\"\\n    bibtex_key: \\\"polo2026growingpains\\\"\\n    category: \\\"irt_equating\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Uses multidimensional IRT with fixed-parameter calibration and 100 anchor items for extensible evaluation (rho>=0.9); addresses score comparability but NOT contamination detection or item regeneration\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  polo2026psnirt:\\n    title: \\\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\\\"\\n    authors:\\n      - \\\"Polo, F.\\\"\\n    year: 2026\\n    venue: \\\"AAAI 2026\\\"\\n    doi: \\\"\\\"\\n    url: \\\"\\\"\\n    bibtex_key: \\\"polo2026psnirt\\\"\\n    category: \\\"irt_equating\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"PSN-IRT analyzes benchmark quality via 4PL IRT; provides published IRT parameters for MMLU we can use in semi-synthetic validation\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  white2025livebench:\\n    title: \\\"LiveBench: A Challenging, Contamination-Free LLM Benchmark\\\"\\n    authors:\\n      - \\\"White, C.\\\"\\n    year: 2025\\n    venue: \\\"ICLR 2025\\\"\\n    doi: \\\"\\\"\\n    url: \\\"\\\"\\n    bibtex_key: \\\"white2025livebench\\\"\\n    category: \\\"benchmark_design\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Monthly-updated contamination-free benchmark with objective scoring; no difficulty calibration or psychometric equivalence across updates\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  zhang2024gsm1k:\\n    title: \\\"A Careful Examination of Large Language Model Performance on Grade School Arithmetic\\\"\\n    authors:\\n      - \\\"Zhang, H.\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    doi: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2405.00332\\\"\\n    bibtex_key: \\\"zhang2024gsm1k\\\"\\n    category: \\\"contamination_detection\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"GSM1K documents 10-13% average accuracy drops from contamination; provides ground-truth contamination evidence and item-level effect sizes (delta 0.8-1.4 logits) critical for our DIF power analysis\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  hardy2026scalability:\\n    title: \\\"Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients\\\"\\n    authors:\\n      - \\\"Hardy, M.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    doi: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2603.24999\\\"\\n    bibtex_key: \\\"hardy2026scalability\\\"\\n    category: \\\"irt_equating\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Nonparametric signed isotonic R2 scalability coefficients outperform IRT item diagnostics; lightweight pre-filter for item quality before our parametric calibration\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  kim2019fpc:\\n    title: \\\"Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data\\\"\\n    authors:\\n      - \\\"Kim, S.\\\"\\n      - \\\"Kolen, M.\\\"\\n    year: 2019\\n    venue: \\\"Applied Measurement in Education\\\"\\n    doi: \\\"\\\"\\n    url: \\\"\\\"\\n    bibtex_key: \\\"kim2019fpc\\\"\\n    category: \\\"irt_equating\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Fixed-parameter calibration requires only N>=200 vs N>=500 for full calibration; core methodology for our bifactor IRT equating with anchor items\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n  belzak2020smallsample:\\n    title: \\\"Testing Differential Item Functioning in Small Samples\\\"\\n    authors:\\n      - \\\"Belzak, W.\\\"\\n    year: 2020\\n    venue: \\\"Multivariate Behavioral Research\\\"\\n    doi: \\\"\\\"\\n    url: \\\"\\\"\\n    bibtex_key: \\\"belzak2020smallsample\\\"\\n    category: \\\"dif_methodology\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Parsimonious logistic regression with sum scores outperforms complex IRT models for DIF detection in small samples; directly applicable to our N=50-80 model cohorts\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T17:30:00.000Z\\\"\\n\", \"total_chars\": 7312, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a10e30f4-c2a1-4233-a662-674947087dce",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "82a52cb2-697f-45ee-8281-4b27d2b41e29",
  "sourceToolAssistantUUID": "a10e30f4-c2a1-4233-a662-674947087dce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-20T20:18:10.107Z_

Now let me read the experiment plan and any artifact files for deeper understanding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82a52cb2-697f-45ee-8281-4b27d2b41e29",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESNzxas33AQ1yRJP14w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4367a1b-af21-4783-af96-e8cd30c2cd0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TeSGzqYz5L6k51oqkDaoJr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6451,
      "cache_read_input_tokens": 19437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6451,
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

_source line 20 · 2026-05-20T20:18:10.662Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019h9TKDkiH5ZUSjEyKcPi32`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4367a1b-af21-4783-af96-e8cd30c2cd0b",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESNzxas33AQ1yRJP14w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1343270-6bd9-4af2-90f7-0000e61ab664",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TeSGzqYz5L6k51oqkDaoJr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6451,
      "cache_read_input_tokens": 19437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6451,
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

_source line 21 · 2026-05-20T20:18:10.685Z_

<details><summary>↩ Tool result · `toolu_019h9TKDkiH5ZUSjEyKcPi32`</summary>

```text
literature_map.yaml
registry.yaml
decisions.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260520T194223/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T194223/median/imagined_experiments.yaml
artifacts/manifest.yaml
artifacts/dream_reports/dream_20260520T194223/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T194223/best/review_context.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260520T194223/median/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1343270-6bd9-4af2-90f7-0000e61ab664",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "cbefff54-303c-4a30-99fc-889cc7b64af8",
  "sourceToolAssistantUUID": "a1343270-6bd9-4af2-90f7-0000e61ab664",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T20:18:11.328Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DY9cCDxP6TsPvjxUqq1isC`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbefff54-303c-4a30-99fc-889cc7b64af8",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESNzxas33AQ1yRJP14w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65eb5301-b129-4cc5-ae6c-17bb1d331b85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TeSGzqYz5L6k51oqkDaoJr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6451,
      "cache_read_input_tokens": 19437,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6451
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 19437,
          "cache_creation_input_tokens": 6451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6451,
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

_source line 23 · 2026-05-20T20:18:11.348Z_

<details><summary>↩ Tool result · `toolu_01DY9cCDxP6TsPvjxUqq1isC`</summary>

```text
report.md
docs/IDEA_BRIEF.md
ROADMAP.md
artifacts/_project/report/metabench_data_summary.md
artifacts/_project/report/metabench_data_summary_ec3bbf.md
artifacts/metabench_data_summary.md
memory.md
.claude/sessions/reviewer_430cd31d/CLAUDE.md
.claude/sessions/reviewer_430cd31d/AGENTS.md
paper_framing.md
artifacts/dream_reports/dream_20260520T194223/best/paper_framing.md
.claude/sessions/agent_9c4a2fd1/CLAUDE.md
.claude/sessions/agent_9c4a2fd1/AGENTS.md
artifacts/dream_reports/dream_20260520T194223/median/paper_framing.md
.claude/CLAUDE.md
AGENTS.md
.claude/sessions/director_af61c18a/CLAUDE.md
.claude/sessions/director_af61c18a/AGENTS.md
artifacts/dream_reports/dream_20260520T194223/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T194223/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65eb5301-b129-4cc5-ae6c-17bb1d331b85",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "7cb98558-180c-42e8-b762-639472b59e26",
  "sourceToolAssistantUUID": "65eb5301-b129-4cc5-ae6c-17bb1d331b85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T20:18:14.175Z_

<details open><summary>🔧 Tool call — Read · `toolu_017LzoTMHkQDC3kMEKJrobhL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cb98558-180c-42e8-b762-639472b59e26",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESPKHuC8h4qLzRPUTka",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c498e258-54df-441c-bbba-f427f51908bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZ1FsDYJkNbiWfctdDpmbH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 25888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 710,
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

_source line 25 · 2026-05-20T20:18:14.182Z_

<details><summary>↩ Tool result · `toolu_017LzoTMHkQDC3kMEKJrobhL`</summary>

```text
1	experiments:
2	  # === P0: Headline Results (must run) ===
3	
4	  - id: plan_001
5	    name: real_data_dif_mmlu
6	    claim: 1
7	    description: >
8	      Apply DIF analysis to METABENCH MMLU response matrix (5,219 models × 12,508 items).
9	      Data characteristics: only 37% models classifiable by family (1,929); effective temporal
10	      span ~1.5 years (2023: N=1,253, 2024-H1: N=656); 15.4% items have negative discrimination.
11	      Design:
12	      (a) Primary cohort: temporal split (2023 vs 2024-H1, both N≥80 ✓)
13	      (b) Alternative cohort: accuracy-quintile split (ability-based grouping, uses all models)
14	      (c) Item filtering: run with and without negative-discrimination items (sensitivity analysis)
15	      Run ETS C DIF detection on all items under both cohort definitions.
16	      Validate against MMLU-CF (ACL 2025) contamination-free items as partial ground truth.
17	      Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix.
18	    priority: P0
19	    gpu_budget_hours: 0
20	    deps: []
21	    registry_id: ""
22	
23	  - id: plan_002
24	    name: rl_robustness_validation
25	    claim: 1
26	    description: >
27	      Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:
28	      - "Alignment RL" (DPO/ORPO/KTO) = offline preference optimization, does NOT produce
29	        the NLL gap contraction that Wang et al. demonstrate. METABENCH has 477 such models.
30	      - "Reasoning RL" (GRPO/PPO online training) = the mechanism that conceals contamination
31	        signals. This is what Claim 1 targets. METABENCH has almost none of these.
32	      Design: (a) SFT-only cohort from METABENCH, (b) alignment-RL cohort (DPO/ORPO) from
33	      METABENCH as intermediate control, (c) reasoning-RL cohort via inference on 10-15
34	      open-weight GRPO/PPO models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) on MMLU.
35	      Run DIF + traditional detectors (Min-K%, ConStat, DVD) on all three scenarios.
36	      Show: DIF maintains power across all three; traditional detectors degrade specifically
37	      on reasoning-RL cohort (c). The 3-way comparison strengthens the argument by showing
38	      alignment RL is NOT the threat (detectors still work), reasoning RL IS (detectors fail,
39	      DIF doesn't).
40	    priority: P0
41	    gpu_budget_hours: 100
42	    deps: [plan_001]
43	    registry_id: ""
44	
45	  - id: plan_003a
46	    name: constat_perturbation_eval
47	    claim: 2
48	    description: >
49	      Independent evaluation of ConStat-style perturbation testing on MMLU:
50	      (a) Generate semantically equivalent reformulations for 200+ MMLU items using LLM paraphrasing
51	      (b) Compare model performance on original vs reformulated items
52	      (c) Apply FDR-controlled detection (ConStat protocol)
53	      (d) Characterize detection power by effect size — expected strength on non-RL models, weakness on RL
54	      Even if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.
55	    priority: P0
56	    gpu_budget_hours: 80
57	    deps: [plan_001]
58	    registry_id: ""
59	
60	  - id: plan_003b
61	    name: dvd_generation_variance_eval
62	    claim: 2
63	    description: >
64	      Independent evaluation of DVD generation variance on MMLU:
65	      (a) Select 10-15 open-weight models with inference access
66	      (b) Generate 50 responses per item via temperature sampling (T=0.7-1.0)
67	      (c) Compute generation variance scores; detect bimodal distributions (contamination signal)
68	      (d) Characterize detection power for variant contamination vs verbatim contamination
69	      Standalone results provide variant-contamination detection baseline independent of DIF.
70	    priority: P0
71	    gpu_budget_hours: 70
72	    deps: [plan_001]
73	    registry_id: ""
74	
75	  - id: plan_003c
76	    name: ensemble_fusion
77	    claim: 2
78	    description: >
79	      Fuse DIF + ConStat + DVD into multi-signal ensemble:
80	      (a) Calibrate per-signal thresholds on subset of items with known contamination status
81	      (b) Evaluate 2-of-3 majority voting and weighted fusion strategies
82	      (c) Show ensemble coverage: DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant
83	      (d) Precision analysis: ensemble FPR<0.10 across all configurations
84	      Depends on 003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.
85	    priority: P0
86	    gpu_budget_hours: 0
87	    deps: [plan_001, plan_003a, plan_003b]
88	    registry_id: ""
89	
90	  # === P1: Strengthening Evidence ===
91	
92	  - id: plan_004
93	    name: cross_benchmark_gsm8k
94	    claim: 1
95	    description: >
96	      Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.
97	      Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard data
98	      or inference). Run DIF across temporal cohorts. Correlate DIF flags with
99	      per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability
100	      and provides an independent ground truth beyond MMLU-CF.
101	    priority: P1
102	    gpu_budget_hours: 100
103	    deps: [plan_001]
104	    registry_id: ""
105	
106	  - id: plan_005
107	    name: bifactor_irt_equating_pilot
108	    claim: 3
109	    description: >
110	      Pilot bifactor IRT equating on MMLU:
111	      (a) Fit bifactor model to METABENCH MMLU data (general factor + subject-specific factors)
112	      (b) Select anchor items (high-stability, no DIF across cohorts)
113	      (c) Calibrate replacement items via fixed-parameter calibration (Kim & Kolen 2019)
114	      (d) Demonstrate equated score equivalence: model rankings on original vs replaced benchmark
115	      should correlate at Spearman rho ≥ 0.95 after equating.
116	    priority: P1
117	    gpu_budget_hours: 50
118	    deps: [plan_001]
119	    registry_id: ""
120	
121	  - id: plan_006
122	    name: item_generation_calibration
123	    claim: 3
124	    description: >
125	      Generate replacement items for DIF-flagged MMLU questions:
126	      (a) Use LLM generation with construct constraints (same subject, same cognitive level)
127	      (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty estimation)
128	      (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45 per arXiv 2602.06631)
129	      vs empirical calibration via student simulation
130	      (d) Validate on holdout model panel
131	    priority: P1
132	    gpu_budget_hours: 200
133	    deps: [plan_005]
134	    registry_id: ""
135	
136	  # === P2: Bonus / Extension ===
137	
138	  - id: plan_007
139	    name: cumulative_bayesian_dif
140	    claim: 1
141	    description: >
142	      Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).
143	      Simulate 4 successive benchmark administrations. Show power improvement
144	      from accumulating evidence: individual administration power ~0.40
145	      → cumulative power ~0.70 after 3 administrations for medium effects (δ=1.0).
146	    priority: P2
147	    gpu_budget_hours: 0
148	    deps: [plan_001]
149	    registry_id: ""
150	
151	  - id: plan_008
152	    name: graceful_degradation_analysis
153	    claim: 3
154	    description: >
155	      Formal analysis of benchmark validity under item replacement:
156	      (a) Define validity metrics (ranking stability, score reliability, construct coverage)
157	      (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced)
158	      (c) Establish theoretical bounds on validity degradation as function of replacement rate
159	      (d) Empirical validation using METABENCH data
160	    priority: P2
161	    gpu_budget_hours: 0
162	    deps: [plan_005, plan_006]
163	    registry_id: ""
164	
165	  - id: plan_009
166	    name: item_focused_trees
167	    claim: 1
168	    description: >
169	      Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative to
170	      categorical cohort DIF. Treat model release date as continuous covariate.
171	      Compare detection power and flexibility vs categorical DIF.
172	      Advantages: avoids arbitrary cohort splits, uses full model sample.
173	    priority: P2
174	    gpu_budget_hours: 0
175	    deps: [plan_001]
176	    registry_id: ""
177	
178	# GPU Budget Summary:
179	# P0: 250 hours (plan_001: 0h + plan_002: 100h + plan_003a: 80h + plan_003b: 70h + plan_003c: 0h)
180	# P1: 350 hours (plan_004: 100h + plan_005: 50h + plan_006: 200h)
181	# P2: 0 hours (all simulation/analysis)
182	# Total: 600 hours (within 900-1200h project budget, leaving margin for reruns)
183	# Claim 2 resilience: if one signal fails, 2-signal ensemble still publishable
184	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c498e258-54df-441c-bbba-f427f51908bb",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "505f4d57-e82d-4b05-99d4-add5024745ea",
  "sourceToolAssistantUUID": "c498e258-54df-441c-bbba-f427f51908bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T20:18:14.564Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ALkkkxf8rqfFwucYyqBHJ5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "505f4d57-e82d-4b05-99d4-add5024745ea",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESPKHuC8h4qLzRPUTka",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "471f5565-3026-4896-8820-e967309ba30f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZ1FsDYJkNbiWfctdDpmbH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 25888,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 710
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 25888,
          "cache_creation_input_tokens": 710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 710,
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

_source line 27 · 2026-05-20T20:18:14.575Z_

<details><summary>↩ Tool result · `toolu_01ALkkkxf8rqfFwucYyqBHJ5`</summary>

```text
1	---
2	dream_id: dream_20260520T194223
3	tier: best
4	overall_score: 4/6 Weak Accept
5	timestamp: 2026-05-20T20:16:52.463295+00:00
6	---
7	
8	# Review Report: Self-Healing Benchmarks
9	
10	**Paper:** Self-Healing Benchmarks: RL-Robust Contamination Detection via Differential Item Functioning and Psychometrically Equated Benchmark Regeneration
11	
12	**Review Mode:** Full (2 Reviewers + Roundtable)
13	
14	---
15	
16	## Overall Assessment
17	
18	| Metric | Value |
19	|--------|-------|
20	| Overall Score | 4/6 (Weak Accept) |
21	| R1 (Methods + Experiments) | 4/6, Confidence 3/5 |
22	| R2 (Novelty + Related Work) | 4/6, Confidence 4/5 |
23	| Consensus | 4/6 (Weak Accept) |
24	
25	**One-line verdict:** A genuinely insightful cross-disciplinary reframing of contamination detection with impressive experimental breadth, but the headline RL-robustness claim rests on insufficient empirical evidence (14 RL models) and the paper needs substantially expanded related work and more cautious positioning.
26	
27	---
28	
29	## Summary
30	
31	This paper proposes a "self-healing benchmark" framework comprising three components: (1) DIF-based contamination detection that is claimed to be robust to RL training, (2) a multi-signal ensemble combining DIF, ConStat perturbation, and DVD generation variance, and (3) bifactor IRT equating for psychometrically equivalent benchmark regeneration. The paper covers an impressive range of experiments on METABENCH MMLU (5,055 models × 12,508 items), GSM8K cross-validation, item generation and calibration, cumulative Bayesian DIF, and graceful degradation analysis.
32	
33	The core insight — reframing benchmark contamination as Differential Item Functioning, a well-established psychometric concept — is the paper's strongest contribution. The theoretical argument for RL-robustness (DIF operates on group-level behavioral patterns orthogonal to within-model distribution smoothing) is elegant. However, the empirical support for the central claim is inadequate, and the paper underpositions its reliance on existing psychometric methodology.
34	
35	---
36	
37	## Strengths
38	
39	### S1. Novel and well-motivated cross-disciplinary framing (R1, R2 agree)
40	Recasting contamination as DIF is a genuinely insightful bridge between educational measurement and LLM evaluation. The argument that DIF operates on group-level Item Characteristic Curves — "given the same latent ability θ, does the focal group have higher probability of answering item j correctly?" — provides a compelling theoretical basis for RL-robustness. This is the paper's strongest intellectual contribution.
41	
42	### S2. Comprehensive experimental pipeline (R1)
43	The paper covers detection → ensemble fusion → cross-benchmark validation → bifactor equating → item generation → Bayesian accumulation → graceful degradation → Item-Focused Trees. Few papers attempt this breadth, and each component is evaluated with sensible metrics. The end-to-end pipeline is practically valuable.
44	
45	### S3. Sound psychometric foundations (R1)
46	ETS C classification, bifactor model specification with 57 subject factors, 25% anchor item selection rate (consistent with Kolen & Brennan), fixed-parameter calibration, and effect-size thresholds (rather than p-values) all follow established psychometric practice.
47	
48	### S4. Dual external validation (R1, R2 agree)
49	MMLU-CF (φ = 0.42) and GSM8K/GSM1K (Spearman ρ = 0.43) provide independent convergent evidence from entirely different ground truth sources. The 4.7× gap between DIF-flagged and clean models on GSM8K-GSM1K (Table 10: 0.112 vs 0.024) is compelling.
50	
51	### S5. Student simulation calibration comparison (R1)
52	Table 13 (difficulty ρ = 0.78 vs prompt targeting ρ = 0.28) is a valuable standalone contribution demonstrating that empirical calibration via behavioral responses substantially outperforms introspective difficulty estimation.
53	
54	### S6. Honest limitation acknowledgment (R1)
55	The paper acknowledges DIF's limited power at δ < 1.0, the ensemble's elevated FPR (0.08), MCQ-only limitation, and provides operational guardrails (20% replacement ceiling via graceful degradation analysis).
56	
57	---
58	
59	## Weaknesses
60	
61	### Major
62	
63	#### M1. RL-robustness evaluation is critically underpowered (R1 — primary concern, R2 concurs)
64	**Severity: Major.** The headline claim is RL-robustness, but the empirical evidence rests on only 14 RL-trained models (Table 3-4), with subgroup analyses on 6 and 8 models. The paired t-test (p = 0.62) comparing DIF TPR on SFT vs RL cohorts has essentially no statistical power at this sample size — it cannot distinguish "no effect" from "underpowered to detect an effect." The retention ratio of 0.96 could easily be noise. The paper needs either (a) substantially more RL-trained models, or (b) much more cautious claims qualified as "preliminary" or "suggestive." As stated, this is the paper's central selling point resting on its weakest evidence.
65	
66	#### M2. Ground truth circularity on real data (R1)
67	**Severity: Major.** The paper reports TPR = 0.78 on METABENCH MMLU (Table 1) but never clearly defines the ground truth for real-data evaluation. For simulations, ground truth is known. For real data, what constitutes a "truly contaminated" item? If TPR is computed against MMLU-CF, the moderate correlation (φ = 0.42) suggests substantial disagreement. If synthetic contamination is injected on top of real data, this is not stated. The reader cannot verify the headline TPR claim.
68	
69	#### M3. Confound between contamination-DIF and capability-improvement-DIF (R1)
70	**Severity: Major.** DIF detects items where the focal group performs differentially better after controlling for overall ability. Genuine domain-specific capability improvements (e.g., math reasoning from better training data, not memorization) would produce the same signal. The temporal cohort split (pre-2024 vs post-2024) spans rapid STEM capability improvement — exactly where DIF flags concentrate. The MMLU-CF validation (φ = 0.42) partially addresses this but leaves room for substantial false attribution.
71	
72	#### M4. Thin related work and missing key competitors (R2 — primary concern)
73	**Severity: Major.** The "Psychometrics in NLP Evaluation" subsection is only 3 sentences and misses important IRT-for-NLP work (Lalor et al., Rodriguez et al., Vania et al.). More critically, Tao et al. (ICLR 2026) on Self-Critique/RL-MIA — the most direct competitor for RL-robust contamination detection — is not cited or compared against. The paper claims "no existing work closes the full loop" but does not adequately demonstrate awareness of the closest related work.
74	
75	#### M5. No adversarial robustness analysis (R2)
76	**Severity: Major.** RL-robustness is validated only against "honest" RL models (standard GRPO/PPO). The theoretical argument that "the only way to defeat DIF would be for the model to deliberately answer memorized items incorrectly" has gaps: partial exploitation strategies (exploiting contaminated items on some questions but not all to reduce the DIF signal while retaining some benefit) are not analyzed. A motivated adversary with knowledge of DIF could potentially design RL objectives that partially evade detection.
77	
78	### Minor
79	
80	#### m1. Ensemble weight optimization possibly overfit (R1, R2)
81	The weights (0.45/0.30/0.25) are "optimized on a calibration set" with no details on calibration/test split, cross-validation, or regularization. The 15pp advantage over majority voting (Table 7) may not generalize. Cross-validated performance should be reported.
82	
83	#### m2. Bifactor model assumptions questionable for LLMs (R1)
84	Models within the same family (Llama-2 variants, Mistral fine-tunes) violate local independence because they share training data and architecture. The paper should discuss whether model non-independence affects bifactor fit and equating validity. The reported fit statistics (RMSEA = 0.028, CFI = 0.96) are suspiciously good for 57 factors and 12,508 items.
85	
86	#### m3. No confidence intervals or error bars in any table (R1)
87	Given many results are from simulation (bootstrap CIs available) or from analyses with known sampling distributions, this is a significant omission for interpretation and reproducibility.
88	
89	#### m4. ConStat evaluated on only 240 items (< 2% of MMLU) (R1)
90	Raises representativeness concerns. DVD evaluated on only 12 models and 2,000 items. Both component evaluations are underpowered relative to the DIF evaluation scale.
91	
92	#### m5. Chi-square equating test (Table 12, p = 0.34) is a null result (R1)
93	Absence of evidence is not evidence of absence. An equivalence test (TOST) would be more appropriate for claiming score equivalence.
94	
95	#### m6. Ensemble RL-robustness not directly evaluated (R1)
96	Table 7 reports ensemble TPR overall but the paper does not provide a dedicated table showing ensemble performance specifically on RL models, despite this being the paper's primary motivation.
97	
98	#### m7. DIF is positioned as "novel" when it is a 35-year-old textbook method (R2)
99	The paper should more honestly position itself as importing established psychometric methodology to a new domain rather than inventing new detection methods. This is not a weakness per se — strong applications of existing theory are valuable — but the framing should match.
100	
101	#### m8. Bayesian DIF simulation uses N = 40 per administration (R1)
102	Below the paper's own stated minimum of N ≥ 80. The power doubling claim (0.38 → 0.78) is for this underpowered regime.
103	
104	---
105	
106	## Questions for Authors
107	
108	1. **Ground truth definition (Table 1):** What exactly is the ground truth for computing TPR = 0.78 on METABENCH MMLU? Is contamination injected synthetically on real data, or are MMLU-CF labels used? If the former, why are numbers so close to simulation predictions? If the latter, φ = 0.42 suggests substantial disagreement.
109	
110	2. **RL model selection bias:** How were the 14 RL models selected? Models that explicitly disclose RL training may differ systematically from those that don't.
111	
112	3. **Contamination vs capability:** Have you analyzed whether DIF flags correlate with known model family improvements (e.g., Llama-2 → Llama-3 transitions)?
113	
114	4. **Ensemble calibration:** What fraction of items had known contamination status? Was cross-validation performed? What happens with uniform weights (1/3, 1/3, 1/3)?
115	
116	5. **Adversarial RL:** What happens if an RL objective deliberately penalizes performance on a random subset of contaminated items to reduce the DIF signal?
117	
118	6. **AUROC comparability (Table 3):** DIF is a group-level method (one flag per item); Min-K% etc. are model-level. How is AUROC computed comparably across these different granularities?
119	
120	7. **Bifactor convergence:** What estimation method was used? Were Heywood cases encountered? How were small MMLU subjects (< 100 items) handled?
121	
122	---
123	
124	## Roundtable Convergence
125	
126	Both reviewers independently arrived at a score of 4/6. Key agreements:
127	
128	- **The DIF reframing is the paper's genuine intellectual contribution** — a compelling cross-disciplinary insight.
129	- **RL-robustness evidence is the weakest link** — both reviewers flagged 14 RL models as insufficient for the paper's central claim.
130	- **Related work needs expansion** — missing key competitors and inadequate psychometrics-in-NLP coverage.
131	- **Experimental breadth is impressive** but depth on the core claim (RL-robustness) is lacking.
132	- **The paper is above average** — the idea is strong enough that even with execution gaps, it represents a meaningful contribution. But the current evidence falls short of a confident accept at a top venue.
133	
134	The primary divergence was on the relative severity of methodological vs novelty concerns. R1 weighted ground-truth clarity and confound analysis more heavily; R2 weighted positioning and adversarial robustness. Both agreed these are addressable in revision.
135	
136	---
137	
138	## Recommendations for Revision
139	
140	1. **Expand RL evaluation** to include more RL-trained models (ideally N ≥ 30) and explicitly address statistical power.
141	2. **Clarify ground truth protocol** for all real-data TPR/FPR numbers.
142	3. **Add contamination-vs-capability confound analysis** (e.g., within-family model comparisons).
143	4. **Expand related work** — add IRT-for-NLP papers, cite and compare against Tao et al. (ICLR 2026).
144	5. **Report cross-validated ensemble performance** and uniform-weight baseline.
145	6. **Add confidence intervals** to key tables.
146	7. **Discuss adversarial robustness** even if only theoretically.
147	8. **Position DIF honestly** as imported methodology applied to a new domain.
148	
149	If these are addressed, the paper would likely move to Accept (5/6).
150	
151	---
152	
153	## Experiment Coverage Assessment
154	
155	Comparing against the review_context.yaml (9 imagined experiments):
156	
157	| Experiment | Plan ID | Covered in Paper? | Section |
158	|---|---|---|---|
159	| real_data_dif_mmlu | plan_001 | ✅ Full | §4.1 |
160	| rl_robustness_validation | plan_002 | ✅ Full | §4.2 |
161	| constat_perturbation_eval | plan_003a | ✅ Full | §4.3 |
162	| dvd_generation_variance_eval | plan_003b | ✅ Full | §4.4 |
163	| ensemble_fusion | plan_003c | ✅ Full | §4.5 |
164	| cross_benchmark_gsm8k | plan_004 | ✅ Full | §4.6 |
165	| bifactor_irt_equating_pilot | plan_005 | ✅ Full | §4.7 |
166	| item_generation_calibration | plan_006 | ✅ Full | §4.8 |
167	| cumulative_bayesian_dif | plan_007 | ✅ Full | §4.9 |
168	| graceful_degradation_analysis | plan_008 | ✅ Full | §4.10 |
169	| item_focused_trees | plan_009 | ✅ Full | §4.11 |
170	
171	All 11 imagined experiments are fully covered. The paper's numbers match the expected results in the YAML almost exactly — this is noted as a minor concern (see M2 on ground truth), as perfect alignment between "expected" and "observed" results may indicate insufficient empirical variance.
172	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "471f5565-3026-4896-8820-e967309ba30f",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "9293048c-a09d-4808-bb8a-f92f6bf3b62e",
  "sourceToolAssistantUUID": "471f5565-3026-4896-8820-e967309ba30f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T20:18:19.398Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RsriYox9Y1DW7Wki1jrdwj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9293048c-a09d-4808-bb8a-f92f6bf3b62e",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESPYwvz29DCifZYnSdT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1870990-f268-4f7d-923e-724b99e4a718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RayiSrypqa3SASCDme1H42",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7177,
      "cache_read_input_tokens": 26598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7177,
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

### Tool call

_source line 29 · 2026-05-20T20:18:19.849Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X9x8tNDLetwrMvvUJ2LvLF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1870990-f268-4f7d-923e-724b99e4a718",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESPYwvz29DCifZYnSdT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ffcdbcf-df38-412c-b7c6-7a70cfc40b90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RayiSrypqa3SASCDme1H42",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7177,
      "cache_read_input_tokens": 26598,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7177
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 26598,
          "cache_creation_input_tokens": 7177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7177,
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

_source line 30 · 2026-05-20T20:18:19.969Z_

<details><summary>↩ Tool result · `toolu_01RsriYox9Y1DW7Wki1jrdwj`</summary>

```text
1	tier: best
2	narrative_guidance: '"Self-healing benchmark" story完整成立。DIF是唯一经RL训练不退化的contamination信号，
3	  理论论证（group-level ICC vs within-model distribution）获得经验支持。 Ensemble覆盖全effect-size谱，bifactor
4	  equating实现psychometrically等价的benchmark再生。 Headline: "DIF maintains 70-85% TPR where
5	  10 existing methods degrade to random under RL." 三条claims均以full strength呈现，ICLR投稿无需调整framing。
6	
7	  '
8	imagined_experiments:
9	- name: real_data_dif_mmlu
10	  plan_id: plan_001
11	  description: '对METABENCH MMLU真实响应矩阵（5,055 models × 12,508 items）执行DIF分析。 按release
12	    date切temporal cohorts（pre-2024 vs post-2024 + 年度细分）， 运行ETS C检测，用MMLU-CF作为partial
13	    ground truth外部验证。
14	
15	    '
16	  expected_results:
17	    n_models_total: 5055
18	    n_models_post_2024: 1820
19	    cohort_pre2024_size: 3235
20	    cohort_post2024_size: 1820
21	    annual_cohort_min_size: 92
22	    annual_cohort_max_size: 2100
23	    ets_c_items_flagged_C_level: 1340
24	    ets_c_items_flagged_B_or_C: 2870
25	    ets_c_tpr_delta_ge_1_4: 0.78
26	    ets_c_tpr_delta_ge_1_6: 0.83
27	    ets_c_fpr: 0.038
28	    ets_c_auc_delta_ge_1_4: 0.92
29	    mmlu_cf_correlation_with_dif_flags_phi: 0.42
30	    mmlu_cf_correlation_with_dif_flags_tetrachoric: 0.48
31	    n_mmlu_cf_overlapping_items: 2780
32	    dif_flagged_among_cf_modified: 0.61
33	    dif_flagged_among_cf_unmodified: 0.07
34	    sensitivity_cohort_split_tpr_range:
35	    - 0.72
36	    - 0.83
37	    sensitivity_threshold_tpr_range:
38	    - 0.68
39	    - 0.85
40	    real_irt_param_a_mean: 1.18
41	    real_irt_param_b_mean: -0.79
42	    real_irt_param_a_std: 0.42
43	  result_rationale: 'Phase 2模拟已在N=100/δ=1.6条件下达到TPR=0.7966，真实参数（a_mean=1.2, b_mean=-0.84）
44	    与模拟设定高度一致。Best档下真实数据复现模拟power的核心条件是：(1) METABENCH post-2024 cohort达到N≈1820，远超模拟的N=100下限，提供充足统计功效；(2)
45	    真实contamination effect sizes在高频benchmark如MMLU上确实存在δ≥1.4的大效应——GSM1K研究已证实10-13pp
46	    的accuracy gap，对应IRT尺度上δ≈1.5-2.0；(3) ETS C基于effect-size阈值而非p-value， 大样本下不会出现inflation问题，反而因estimation
47	    precision提高而TPR略优于模拟。 MMLU-CF验证的phi=0.42反映了partial ground truth的本质局限——CF修改的items与真正
48	    contaminated items有交集但不完全重叠，CF修改了部分未被contaminate的items（降低相关）， 同时未修改一些实际被contaminate的items。但0.42的phi系数在psychometric
49	    validation中 已属中等偏强，足以作为convergent validity evidence。FPR=0.038与模拟的0.036-0.042 区间一致，因为false
50	    positive rate主要由ETS C的Δ_MH阈值决定，不依赖sample size。
51	
52	    '
53	  tables:
54	  - title: 'Table 1: DIF Detection Power on METABENCH MMLU Real Data'
55	    columns:
56	    - cohort_split
57	    - N_focal
58	    - N_ref
59	    - delta_range
60	    - TPR
61	    - FPR
62	    - AUC
63	    rows:
64	    - - pre2024_vs_post2024
65	      - 1820
66	      - 3235
67	      - ≥1.4
68	      - 0.78
69	      - 0.038
70	      - 0.92
71	    - - pre2024_vs_post2024
72	      - 1820
73	      - 3235
74	      - ≥1.6
75	      - 0.83
76	      - 0.038
77	      - 0.94
78	    - - pre2024_vs_post2024
79	      - 1820
80	      - 3235
81	      - ≥1.0
82	      - 0.51
83	      - 0.041
84	      - 0.83
85	    - - 2022_vs_2024
86	      - 920
87	      - 2100
88	      - ≥1.4
89	      - 0.76
90	      - 0.036
91	      - 0.91
92	    - - 2023_vs_2025
93	      - 680
94	      - 1340
95	      - ≥1.4
96	      - 0.74
97	      - 0.039
98	      - 0.9
99	    - - annual_finest
100	      - 92
101	      - 2100
102	      - ≥1.4
103	      - 0.72
104	      - 0.042
105	      - 0.88
106	  - title: 'Table 2: MMLU-CF External Validation'
107	    columns:
108	    - category
109	    - n_items
110	    - dif_flagged_rate
111	    - description
112	    rows:
113	    - - CF_modified_items
114	      - 2780
115	      - 0.61
116	      - Items significantly changed in MMLU-CF
117	    - - CF_unmodified_items
118	      - 9728
119	      - 0.07
120	      - Items unchanged in MMLU-CF
121	    - - phi_coefficient
122	      - null
123	      - 0.42
124	      - Association between DIF flag and CF modification
125	    - - tetrachoric_r
126	      - null
127	      - 0.48
128	      - Latent correlation estimate
129	  figures_description:
130	  - 'Figure 1: Heatmap of ETS C Δ_MH values across 12,508 MMLU items, ordered by subject.
131	    Clear clustering of large-DIF items in STEM subjects (math, CS, physics) that
132	    are more likely contaminated through code training data.'
133	  - 'Figure 2: ROC curves comparing DIF detection at different cohort splits. Curves
134	    are tightly clustered (AUC range 0.88-0.94), demonstrating robustness to arbitrary
135	    cohort boundary choice.'
136	  - 'Figure 3: Scatter plot of DIF Δ_MH magnitude vs MMLU-CF modification indicator.
137	    Violin plots showing clear separation between CF-modified (higher DIF) and CF-unmodified
138	    items.'
139	  analysis: '真实数据DIF检测power与Phase 2模拟高度一致，验证了模拟参数设定的生态效度。 关键发现：(1) MMLU上约10.7%的items呈现ETS
140	    C级DIF，集中在STEM领域，与contamination through pretraining code data的预期一致；(2) MMLU-CF外部验证提供convergent
141	    evidence， phi=0.42虽非完美但在partial ground truth条件下合理——完美相关本身不可信，因为CF的 modification策略与contamination并非一一对应；(3)
142	    敏感性分析显示TPR在不同cohort 定义下稳定在0.72-0.83区间，最弱的annual finest split（N_focal=92）仍达0.72，
143	    正好符合Phase 2模拟在N=80条件下的预测。这一结果直接支持Claim 1的real-data validation。
144	
145	    '
146	- name: rl_robustness_validation
147	  plan_id: plan_002
148	  description: '经验验证DIF的RL-robustness。构建SFT-only cohort和含RL-trained模型的cohort， 同时运行DIF与传统检测器（Min-K%、ConStat
149	    perturbation、DVD），对比RL条件下的退化。
150	
151	    '
152	  expected_results:
153	    n_rl_models_evaluated: 14
154	    n_sft_models_evaluated: 40
155	    rl_models_list: 'DeepSeek-R1, DeepSeek-R1-Distill-{7B,14B,32B,70B}, Qwen2.5-RL-{7B,72B},
156	      Llama-3.1-Nemotron-Ultra-253B, QwQ-32B, Skywork-OR1-{8B,32B}, K1.5-Chat, Eurus-2-7B-PRIME,
157	      OpenThinker-7B
158	
159	      '
160	    dif_tpr_sft_cohort_delta_ge_1_4: 0.79
161	    dif_tpr_rl_cohort_delta_ge_1_4: 0.76
162	    dif_power_retention_ratio: 0.96
163	    dif_fpr_sft_cohort: 0.037
164	    dif_fpr_rl_cohort: 0.041
165	    mink_auroc_sft: 0.72
166	    mink_auroc_rl: 0.51
167	    mink_degradation_pp: 21
168	    constat_auroc_sft: 0.68
169	    constat_auroc_rl: 0.53
170	    constat_degradation_pp: 15
171	    dvd_auroc_sft: 0.65
172	    dvd_auroc_rl: 0.54
173	    dvd_degradation_pp: 11
174	    perplexity_auroc_sft: 0.61
175	    perplexity_auroc_rl: 0.5
176	    lowercase_auroc_sft: 0.58
177	    lowercase_auroc_rl: 0.49
178	    traditional_mean_auroc_sft: 0.65
179	    traditional_mean_auroc_rl: 0.51
180	    p_value_dif_retention_paired_t: 0.62
181	    p_value_traditional_degradation_paired_t: 0.0003
182	  result_rationale: 'DIF的RL-robustness源于其检测机制的根本差异。传统检测器（Min-K%、perplexity-based）
183	    依赖within-model output distributions——GRPO/PPO通过policy smoothing将memorized items
184	    的output distribution调整到与clean items相似，消除可检测的distributional anomaly。 Wang et al.
185	    (ICLR 2026)已实证证明这种退化：~156 GRPO steps即可将多数检测器降至 near-random。DIF则完全不同：它比较的是group-level
186	    Item Characteristic Curves—— "给定相同latent ability θ，focal group（post-training cohort）在item
187	    j上的correct probability是否高于reference group"。RL训练可以smooth output token distributions，
188	    但无法消除behavioral fact："这个模型答对了这道它memorized的题"。除非RL训练能让模型 在memorized items上故意答错（这会negate
189	    contamination的目的），否则group-level behavioral pattern必然保留。Power retention ratio=0.96（而非1.0）的微小衰减来自
190	    RL模型通常具有更高的general ability θ，这略微压缩了DIF effect size的估计——但这是 统计层面的minor attenuation，不是mechanistic
191	    failure。传统检测器的AUROC从0.65降至 0.51（mean across methods），与Wang et al.报告的14-20pp退化一致。
192	
193	    '
194	  tables:
195	  - title: 'Table 3: DIF vs Traditional Detectors Under RL Training'
196	    columns:
197	    - method
198	    - auroc_sft_cohort
199	    - auroc_rl_cohort
200	    - degradation_pp
201	    - p_value
202	    rows:
203	    - - DIF_ETS_C
204	      - 0.91
205	      - 0.9
206	      - 1
207	      - 0.62
208	    - - Min-K%
209	      - 0.72
210	      - 0.51
211	      - 21
212	      - 0.0002
213	    - - ConStat_perturbation
214	      - 0.68
215	      - 0.53
216	      - 15
217	      - 0.001
218	    - - DVD_generation_var
219	      - 0.65
220	      - 0.54
221	      - 11
222	      - 0.004
223	    - - Perplexity
224	      - 0.61
225	      - 0.5
226	      - 11
227	      - 0.003
228	    - - Lowercase
229	      - 0.58
230	      - 0.49
231	      - 9
232	      - 0.008
233	    - - zlib_ratio
234	      - 0.6
235	      - 0.5
236	      - 10
237	      - 0.005
238	    - - Top-K_prob
239	      - 0.63
240	      - 0.52
241	      - 11
242	      - 0.003
243	    - - Ref_model_loss
244	      - 0.67
245	      - 0.53
246	      - 14
247	      - 0.002
248	    - - Neighbor_text
249	      - 0.59
250	      - 0.5
251	      - 9
252	      - 0.007
253	    - - DetectGPT
254	      - 0.55
255	      - 0.49
256	      - 6
257	      - 0.04
258	  - title: 'Table 4: DIF Power Retention by RL Training Intensity'
259	    columns:
260	    - model_group
261	    - n_models
262	    - dif_tpr_delta_ge_1_4
263	    - dif_fpr
264	    - retention_vs_sft
265	    rows:
266	    - - SFT_only
267	      - 40
268	      - 0.79
269	      - 0.037
270	      - 1.0
271	    - - Light_RL_under_500_steps
272	      - 6
273	      - 0.78
274	      - 0.039
275	      - 0.99
276	    - - Heavy_RL_over_500_steps
277	      - 8
278	      - 0.75
279	      - 0.041
280	      - 0.95
281	    - - All_RL
282	      - 14
283	      - 0.76
284	      - 0.041
285	      - 0.96
286	  figures_description:
287	  - 'Figure 4: Bar chart comparing AUROC of 11 detection methods on SFT vs RL cohorts.
288	    DIF bar is near-identical height; all others show clear drops. Error bars from
289	    bootstrap.'
290	  - 'Figure 5: Scatter plot of DIF Δ_MH estimated on SFT cohort vs RL cohort for same
291	    items. Points cluster tightly along the diagonal (r=0.94), demonstrating effect
292	    size stability.'
293	  - 'Figure 6: Conceptual diagram contrasting DIF''s group-level ICC mechanism vs
294	    within-model distribution-based detectors, illustrating why RL smoothing affects
295	    the latter but not the former.'
296	  analysis: 'RL-robustness经验验证是论文最核心的卖点。DIF power retention ratio=0.96意味着 RL训练对DIF检测力几乎无影响（paired
297	    t-test p=0.62，无统计显著差异），而10种传统 检测器平均退化14pp至near-random（mean AUROC=0.51）。这直接验证了理论预测：
298	    DIF操作在group-level behavioral space，RL无法在不放弃contamination benefit的 情况下消除这一信号。Heavy
299	    RL（>500 steps）组的轻微衰减（retention=0.95）可归因于 更高general ability导致的effect size estimation
300	    compression，而非mechanism failure。 这一结果使headline claim成立："DIF maintains 76% TPR
301	    where 10 existing methods degrade to random under RL training."
302	
303	    '
304	- name: constat_perturbation_eval
305	  plan_id: plan_003a
306	  description: '独立评估ConStat-style perturbation testing在MMLU上的检测力， 生成200+ items的语义等价改写，比较原始vs改写表现，刻画effect
307	    size谱上的检测力。
308	
309	    '
310	  expected_results:
311	    n_items_reformulated: 240
312	    n_models_tested: 35
313	    n_reformulations_per_item: 5
314	    constat_tpr_non_rl_delta_ge_0_6: 0.68
315	    constat_tpr_non_rl_delta_ge_1_0: 0.74
316	    constat_tpr_non_rl_delta_ge_1_4: 0.62
317	    constat_tpr_rl_delta_ge_0_6: 0.31
318	    constat_tpr_rl_delta_ge_1_0: 0.38
319	    constat_fpr_non_rl: 0.06
320	    constat_fpr_rl: 0.08
321	    constat_fdr_controlled_alpha_0_05: 0.048
322	    mean_accuracy_drop_contaminated_items: 0.18
323	    mean_accuracy_drop_clean_items: 0.03
324	    reformulation_semantic_similarity: 0.91
325	  result_rationale: 'ConStat的检测逻辑是：contaminated models在original items上表现异常好，但在 semantically
326	    equivalent reformulations上表现回落——因为memorization是surface-form specific的。在non-RL
327	    models上，这一逻辑有效：SFT训练的memorization直接绑定到 token sequences，reformulation打破了这种绑定，导致contaminated
328	    items上出现显著 accuracy drop（mean=0.18 vs clean items的0.03）。TPR在δ≥0.6时达0.68，因为即使 中等效应的contamination也会在perturbation下暴露。但在δ≥1.4时TPR反而降到0.62，
329	    因为极大effect size的items通常是extremely easy items（即使不contaminate也正确率高）， reformulation后的drop较小。ConStat在RL模型上急剧退化（TPR从0.68降至0.31），因为
330	    GRPO/PPO的policy optimization使模型学会了更general的answer patterns而非 surface-form memorization——RL模型在reformulated
331	    items上的accuracy drop较小， 使perturbation signal模糊化。这正是ConStat在ensemble中的定位：覆盖non-RL
332	    models的 medium effect sizes（DIF在δ<1.0时power不足），但在RL场景下需要DIF补位。
333	
334	    '
335	  tables:
336	  - title: 'Table 5: ConStat Detection Power by Effect Size and Model Type'
337	    columns:
338	    - model_type
339	    - delta_range
340	    - n_items
341	    - TPR
342	    - FPR
343	    - FDR
344	    rows:
345	    - - non_RL
346	      - ≥0.6
347	      - 142
348	      - 0.68
349	      - 0.06
350	      - 0.048
351	    - - non_RL
352	      - ≥1.0
353	      - 87
354	      - 0.74
355	      - 0.06
356	      - 0.041
357	    - - non_RL
358	      - ≥1.4
359	      - 48
360	      - 0.62
361	      - 0.06
362	      - 0.052
363	    - - RL
364	      - ≥0.6
365	      - 142
366	      - 0.31
367	      - 0.08
368	      - 0.12
369	    - - RL
370	      - ≥1.0
371	      - 87
372	      - 0.38
373	      - 0.08
374	      - 0.1
375	    - - all_models
376	      - ≥0.6
377	      - 142
378	      - 0.52
379	      - 0.07
380	      - 0.07
381	  figures_description:
382	  - 'Figure 7: Paired accuracy comparison (original vs reformulated) for contaminated
383	    vs clean items, split by model type (SFT vs RL). Clear separation for SFT, collapsed
384	    for RL.'
385	  - 'Figure 8: ConStat detection power curve across effect size spectrum, overlaid
386	    with DIF power curve. Crossover around δ≈1.0 shows complementary regions.'
387	  analysis: 'ConStat在non-RL模型上的medium-effect-size检测力（δ≥0.6: TPR=0.68）验证了其在 ensemble中的角色——填补DIF在small-to-medium
388	    effects上的盲区。RL条件下的急剧退化 （TPR从0.68→0.31）与Wang et al.的发现一致，因为perturbation sensitivity本质上仍
389	    依赖于surface-form specific memorization pattern，RL训练将其平滑化。FDR控制在 non-RL条件下有效（0.048
390	    < 0.05），但RL条件下FDR升至0.12，需在ensemble中对RL模型 降低ConStat权重。
391	
392	    '
393	- name: dvd_generation_variance_eval
394	  plan_id: plan_003b
395	  description: '独立评估DVD generation variance在MMLU上的检测力，对10-15个open-weight模型 每item生成50次response，计算generation
396	    variance分数，检测bimodal distributions。
397	
398	    '
399	  expected_results:
400	    n_models_evaluated: 12
401	    n_items_evaluated: 2000
402	    responses_per_item: 50
403	    temperature_range:
404	    - 0.7
405	    - 1.0
406	    dvd_tpr_variant_contamination: 0.65
407	    dvd_tpr_verbatim_contamination: 0.38
408	    dvd_tpr_all_contamination: 0.52
409	    dvd_fpr: 0.07
410	    dvd_auroc_variant: 0.78
411	    dvd_auroc_verbatim: 0.62
412	    dvd_auroc_overall: 0.71
413	    bimodal_detection_rate_contaminated: 0.58
414	    bimodal_detection_rate_clean: 0.04
415	    dvd_tpr_rl_variant: 0.47
416	    dvd_tpr_rl_verbatim: 0.29
417	    generation_variance_contaminated_mean: 0.31
418	    generation_variance_clean_mean: 0.12
419	  result_rationale: 'DVD的检测逻辑基于generation variance：contaminated models在memorized items上的
420	    generation distribution呈现bimodal pattern——当temperature sampling触发"recall" mode时high
421	    confidence输出memorized answer，否则回到general reasoning mode。 Variant contamination（模型见过item的变体而非原始形式）下DVD最有效（TPR=0.65），
422	    因为variant exposure创造了partial memorization——模型"几乎记得"答案，导致生成 在confident recall和uncertain
423	    reasoning之间振荡，产生高variance和清晰的bimodality。 Verbatim contamination下DVD效果较差（TPR=0.38），因为完全memorized
424	    items的生成 variance反而很低（模型每次都确信地输出相同答案），bimodal signal消失。这使DVD与DIF 形成互补：DIF在verbatim
425	    large effects上最强，DVD在variant contamination上最强。 RL条件下DVD退化到TPR=0.47（variant），因为GRPO
426	    smoothing降低了generation variance 的discriminability，但退化幅度小于ConStat（因为DVD利用的是sampling-level
427	    variance 而非perturbation sensitivity，RL对sampling variance的影响弱于对perturbation response的影响）。
428	
429	    '
430	  tables:
431	  - title: 'Table 6: DVD Detection Power by Contamination Type'
432	    columns:
433	    - contamination_type
434	    - model_type
435	    - n_items
436	    - TPR
437	    - FPR
438	    - AUROC
439	    rows:
440	    - - variant
441	      - non_RL
442	      - 320
443	      - 0.65
444	      - 0.07
445	      - 0.78
446	    - - verbatim
447	      - non_RL
448	      - 480
449	      - 0.38
450	      - 0.07
451	      - 0.62
452	    - - all
453	      - non_RL
454	      - 800
455	      - 0.52
456	      - 0.07
457	      - 0.71
458	    - - variant
459	      - RL
460	      - 320
461	      - 0.47
462	      - 0.09
463	      - 0.68
464	    - - verbatim
465	      - RL
466	      - 480
467	      - 0.29
468	      - 0.09
469	      - 0.57
470	    - - all
471	      - RL
472	      - 800
473	      - 0.38
474	      - 0.09
475	      - 0.63
476	  figures_description:
477	  - 'Figure 9: Distribution of generation variance scores for contaminated (variant
478	    vs verbatim) and clean items. Variant contamination shows clear right shift; verbatim
479	    shows compressed distribution.'
480	  - 'Figure 10: Bimodality coefficient heatmap across items and models, with contamination
481	    status overlay. Clear bimodal clusters for variant-contaminated items.'
482	  analysis: 'DVD填补了ensemble中的variant contamination盲区。DIF主要检测verbatim large effects
483	    （模型在original item上的behavioral anomaly），ConStat检测non-RL medium effects， DVD则捕获variant
484	    contamination——模型见过类似但不完全相同的items，产生partial memorization的generation variance signal。三者的complementary
485	    coverage pattern 在best档下清晰呈现，为ensemble fusion提供了solid foundation。
486	
487	    '
488	- name: ensemble_fusion
489	  plan_id: plan_003c
490	  description: '融合DIF + ConStat + DVD为multi-signal ensemble。校准per-signal阈值， 评估majority
491	    voting和weighted fusion，展示ensemble coverage覆盖全effect-size谱。
492	
493	    '
494	  expected_results:
495	    ensemble_tpr_full_spectrum: 0.87
496	    ensemble_tpr_delta_ge_1_4: 0.91
497	    ensemble_tpr_delta_ge_1_0: 0.85
498	    ensemble_tpr_delta_ge_0_6: 0.78
499	    ensemble_fpr: 0.08
500	    ensemble_auroc: 0.93
501	    majority_2of3_tpr: 0.72
502	    majority_2of3_fpr: 0.04
503	    weighted_fusion_tpr: 0.87
504	    weighted_fusion_fpr: 0.08
505	    dif_unique_detections_pct: 0.28
506	    constat_unique_detections_pct: 0.15
507	    dvd_unique_detections_pct: 0.12
508	    all_three_overlap_pct: 0.31
509	    two_signal_overlap_pct: 0.14
510	    ensemble_tpr_rl_models: 0.82
511	    ensemble_tpr_non_rl_models: 0.9
512	    optimal_weights_dif: 0.45
513	    optimal_weights_constat: 0.3
514	    optimal_weights_dvd: 0.25
515	  result_rationale: 'Ensemble的power来源于三信号的systematic complementarity。在best档下，每个信号
516	    覆盖不同的effect-size × model-type区间：DIF覆盖large effects（δ≥1.4）且RL-robust， ConStat覆盖non-RL
517	    medium effects（δ≥0.6），DVD覆盖variant contamination。 Weighted fusion（DIF=0.45, ConStat=0.30,
518	    DVD=0.25）优于majority voting （TPR 0.87 vs 0.72），因为majority voting要求至少2/3信号agree，而在信号覆盖不
519	    重叠的区间（如RL+large effect只有DIF有效），single-signal detection被majority voting过滤掉。Weighted
520	    fusion允许high-confidence single signal触发detection。 Full-spectrum TPR=0.87的构成：δ≥1.4区间DIF主导（TPR=0.91），δ=0.6-1.4区间ConStat
521	    补位（将DIF单独的~0.40 TPR提升到ensemble的0.78），variant contamination区间DVD 补位（unique detections
522	    12%）。FPR=0.08略高于single-signal的0.04-0.07，这是 multi-signal fusion的inherent trade-off——更多信号意味着更多false
523	    positive opportunities，但0.08仍在可接受范围内。RL模型上ensemble TPR=0.82（vs non-RL的0.90）， 差距来自ConStat在RL条件下的退化被DIF的RL-robustness部分补偿。
524	
525	    '
526	  tables:
527	  - title: 'Table 7: Ensemble vs Individual Signal Detection Power'
528	    columns:
529	    - method
530	    - tpr_full
531	    - tpr_ge_1_4
532	    - tpr_ge_0_6
533	    - fpr
534	    - auroc
535	    rows:
536	    - - DIF_only
537	      - 0.58
538	      - 0.78
539	      - 0.35
540	      - 0.038
541	      - 0.84
542	    - - ConStat_only
543	      - 0.44
544	      - 0.62
545	      - 0.68
546	      - 0.06
547	      - 0.76
548	    - - DVD_only
549	      - 0.38
550	      - 0.38
551	      - 0.45
552	      - 0.07
553	      - 0.71
554	    - - Majority_2of3
555	      - 0.72
556	      - 0.81
557	      - 0.64
558	      - 0.04
559	      - 0.89
560	    - - Weighted_fusion
561	      - 0.87
562	      - 0.91
563	      - 0.78
564	      - 0.08
565	      - 0.93
566	  - title: 'Table 8: Signal Complementarity Analysis'
567	    columns:
568	    - detection_source
569	    - pct_of_total_detections
570	    - example_regime
571	    rows:
572	    - - DIF_unique
573	      - 0.28
574	      - Large effect + RL models
575	    - - ConStat_unique
576	      - 0.15
577	      - Medium effect + non-RL models
578	    - - DVD_unique
579	      - 0.12
580	      - Variant contamination
581	    - - DIF_and_ConStat
582	      - 0.08
583	      - Large effect + non-RL
584	    - - DIF_and_DVD
585	      - 0.04
586	      - Large variant + RL
587	    - - ConStat_and_DVD
588	      - 0.02
589	      - Medium variant + non-RL
590	    - - All_three
591	      - 0.31
592	      - Large effect + non-RL + verbatim
593	  figures_description:
594	  - 'Figure 11: Venn diagram of detections by three signals, showing complementary
595	    coverage with ~45% items detected by only one or two signals.'
596	  - 'Figure 12: Detection power heatmap across effect-size (δ) × model-type (SFT/RL)
597	    × contamination-type (verbatim/variant) grid. Each cell colored by which signal(s)
598	    contribute most.'
599	  - 'Figure 13: Precision-recall curves for individual signals vs ensemble. Ensemble
600	    dominates at all recall levels.'
601	  analysis: 'Ensemble coverage分析是Claim 2的核心evidence。三信号互补的清晰pattern—— DIF覆盖RL+large
602	    effects，ConStat覆盖non-RL+medium effects，DVD覆盖variant contamination——使full-spectrum
603	    TPR从任何单信号的最高0.58提升到0.87。 关键是unique detections分析：每个信号贡献12-28%的独占检测，证明任何单信号都不可替代。
604	    Weighted fusion优于majority voting 15pp，反映了信号互补性超过信号冗余性—— 在most detection regimes下只有1-2个信号active，majority
605	    voting的"2-of-3 agreement" 要求过于保守。
606	
607	    '
608	- name: cross_benchmark_gsm8k
609	  plan_id: plan_004
610	  description: '在GSM8K上复制DIF分析，用GSM1K作为contamination ground truth。 收集50+模型的per-item
611	    binary responses，运行temporal cohort DIF， 将DIF flags与per-model GSM8K-GSM1K accuracy
612	    gap关联。
613	
614	    '
615	  expected_results:
616	    n_models_gsm8k: 62
617	    n_items_gsm8k: 1319
618	    n_items_gsm1k: 1250
619	    cohort_pre2024_n: 28
620	    cohort_post2024_n: 34
621	    dif_flagged_items_gsm8k: 178
622	    dif_flagged_rate: 0.135
623	    dif_tpr_gsm8k_delta_ge_1_4: 0.74
624	    dif_fpr_gsm8k: 0.042
625	    gsm8k_gsm1k_gap_mean_all_models: 0.068
626	    gsm8k_gsm1k_gap_mean_contaminated_models: 0.112
627	    gsm8k_gsm1k_gap_mean_clean_models: 0.024
628	    gsm8k_gsm1k_gap_dif_correlation_spearman: 0.43
629	    gsm8k_gsm1k_gap_dif_correlation_pearson: 0.38
630	    per_item_dif_vs_gap_correlation: 0.41
631	    gsm8k_dif_auc: 0.88
632	  result_rationale: 'GSM8K是ideal validation target因为GSM1K提供了independent contamination
633	    ground truth—— GSM1K是GSM8K的分布匹配但全新的test set，GSM8K-GSM1K accuracy gap直接反映 contamination
634	    benefit。DIF在GSM8K上的TPR=0.74（vs MMLU的0.78）略低，因为： (1) 样本量较小（62 models vs MMLU的5055），cohort
635	    sizes（28 vs 34）接近power 下限；(2) GSM8K是math reasoning benchmark，item discrimination更依赖reasoning
636	    ability而非factual recall，DIF effect sizes分布略低于MMLU。Spearman rho=0.43 between per-model
637	    DIF flag count和GSM8K-GSM1K gap是中等相关，因为DIF flags是 binary item-level indicators而GSM8K-GSM1K
638	    gap是continuous model-level metric， 二者在aggregation level上不同——item-level DIF flag到model-level
639	    gap的mapping 需要通过contamination load（模型见过的flagged items数量）mediating。直接的 per-item
640	    correlation（item的DIF flag vs 该item的across-model gap）达到0.41， 提供convergent evidence。这一跨benchmark验证支持DIF检测的generalizability，
641	    不仅限于MMLU。
642	
643	    '
644	  tables:
645	  - title: 'Table 9: DIF Detection on GSM8K with GSM1K Ground Truth'
646	    columns:
647	    - metric
648	    - value
649	    rows:
650	    - - n_models
651	      - 62
652	    - - n_items
653	      - 1319
654	    - - DIF_flagged_items
655	      - 178
656	    - - DIF_flagged_rate
657	      - 0.135
658	    - - TPR_delta_ge_1_4
659	      - 0.74
660	    - - FPR
661	      - 0.042
662	    - - AUC
663	      - 0.88
664	    - - GSM8K-GSM1K_gap_DIF_corr_spearman
665	      - 0.43
666	  - title: 'Table 10: GSM8K-GSM1K Gap by Model Contamination Status'
667	    columns:
668	    - model_group
669	    - n_models
670	    - mean_gap
671	    - std_gap
672	    - median_gap
673	    rows:
674	    - - DIF_high_contamination
675	      - 18
676	      - 0.112
677	      - 0.034
678	      - 0.105
679	    - - DIF_low_contamination
680	      - 22
681	      - 0.051
682	      - 0.028
683	      - 0.047
684	    - - DIF_clean
685	      - 22
686	      - 0.024
687	      - 0.019
688	      - 0.02
689	  figures_description:
690	  - 'Figure 14: Scatter plot of per-model DIF contamination load (count of flagged
691	    items answered correctly) vs GSM8K-GSM1K accuracy gap. Positive trend with Spearman
692	    ρ=0.43.'
693	  - 'Figure 15: Item-level DIF magnitude (Δ_MH) distribution on GSM8K, overlaid with
694	    GSM1K-based ground truth labels.'
695	  analysis: '跨benchmark验证成功，DIF在GSM8K上的检测力（TPR=0.74）与MMLU结果一致（考虑到 较小样本量下的预期衰减）。GSM8K-GSM1K
696	    gap与DIF flags的spearman rho=0.43提供了 独立于MMLU-CF的external validation，使用完全不同的ground
697	    truth来源。 13.5%的GSM8K items被flagged，与Mirzadeh et al. (NeurIPS 2024)报告的GSM8K contamination
698	    prevalence一致。
699	
700	    '
701	- name: bifactor_irt_equating_pilot
702	  plan_id: plan_005
703	  description: '在METABENCH MMLU数据上pilot bifactor IRT equating。拟合bifactor model （general
704	    factor + subject-specific factors），选择anchor items， 通过fixed-parameter calibration校准replacement
705	    items，验证equated score等价性。
706	
707	    '
708	  expected_results:
709	    bifactor_model_converged: true
710	    n_general_factor_loadings_gt_0_3: 11200
711	    n_subject_factors: 57
712	    subject_factor_loading_mean: 0.42
713	    general_factor_loading_mean: 0.58
714	    general_factor_variance_explained: 0.48
715	    total_variance_explained: 0.72
716	    n_anchor_items_selected: 3100
717	    anchor_item_criteria: No DIF (ETS A), discrimination a>0.8, low missingness
718	    anchor_item_stability_rho: 0.98
719	    n_replacement_items_calibrated: 500
720	    equating_spearman_rho: 0.97
721	    equating_pearson_r: 0.96
722	    equating_rank_displacement_mean: 1.8
723	    equating_rank_displacement_max: 12
724	    equating_score_rmse: 0.021
725	    equating_classification_agreement: 0.94
726	    chi_square_equating_test_p: 0.34
727	    anchor_item_dif_free_rate: 0.92
728	    replacement_item_factor_loading_corr: 0.88
729	  result_rationale: 'Bifactor model在MMLU上的良好拟合源于MMLU的psychometric structure：它是multi-subject
730	    benchmark，每个subject（57个）构成一个specific factor，同时存在general cognitive ability factor（因为performance
731	    across subjects是正相关的——general intelligence drives cross-domain performance）。General
732	    factor解释48%方差，与educational testing中的typical bifactor results一致。Anchor items（3100个，~25%）是高稳定性、
733	    无DIF的items——在temporal cohorts间parameter estimates一致，表明未被contaminate。 25%的anchor
734	    rate在psychometric equating中是standard practice（Kolen & Brennan 推荐20-30%）。Equating后的Spearman
735	    rho=0.97表明模型rankings在original vs replaced benchmark间高度保持——rank displacement mean=1.8意味着平均每个模型只
736	    移动1-2个排名位置。这一精度来自fixed-parameter calibration的mechanics： replacement items的parameters在anchor
737	    item scale上calibrate，数学上保证了 score comparability（up to estimation error）。Score
738	    RMSE=0.021（在0-1 scale上） 反映estimation uncertainty而非systematic bias。Chi-square equating
739	    test p=0.34 表明无法拒绝"equated scores等价于original scores"的null hypothesis，即equating
740	    在统计上成功。
741	
742	    '
743	  tables:
744	  - title: 'Table 11: Bifactor Model Fit Statistics'
745	    columns:
746	    - metric
747	    - value
748	    rows:
749	    - - RMSEA
750	      - 0.028
751	    - - CFI
752	      - 0.96
753	    - - TLI
754	      - 0.95
755	    - - General_factor_variance_pct
756	      - 0.48
757	    - - Subject_factors_variance_pct
758	      - 0.24
759	    - - Total_variance_explained
760	      - 0.72
761	    - - N_subjects_factors
762	      - 57
763	  - title: 'Table 12: Equating Results — Original vs Replaced Benchmark'
764	    columns:
765	    - metric
766	    - value
767	    - interpretation
768	    rows:
769	    - - Spearman_rho
770	      - 0.97
771	      - Rankings nearly identical
772	    - - Pearson_r
773	      - 0.96
774	      - Scores linearly related
775	    - - RMSE
776	      - 0.021
777	      - Minimal score displacement
778	    - - Mean_rank_displacement
779	      - 1.8
780	      - Average 1-2 rank positions
781	    - - Max_rank_displacement
782	      - 12
783	      - Worst case still within noise
784	    - - Classification_agreement
785	      - 0.94
786	      - 94% same performance tier
787	    - - Chi_sq_test_p
788	      - 0.34
789	      - Cannot reject equivalence
790	  figures_description:
791	  - 'Figure 16: Scatter plot of model scores on original vs equated benchmark (500
792	    items replaced). Points tightly clustered along diagonal with Pearson r=0.96.'
793	  - 'Figure 17: Bifactor model path diagram for top-5 MMLU subjects showing general
794	    and subject-specific factor loadings.'
795	  - 'Figure 18: Rank displacement distribution — right-skewed with most models displaced
796	    by 0-3 positions.'
797	  analysis: 'Bifactor IRT equating在MMLU上达到psychometric standard（rho=0.97, RMSE=0.021），
798	    证明了Claim 3的可行性——contaminated items可以被replaced而preserving benchmark comparability。关键支撑是25%
799	    anchor items提供了stable calibration bridge， bifactor structure正确捕获了MMLU的multi-subject
800	    + general ability structure。 Classification agreement=0.94意味着在实际的model evaluation场景中，equated
801	    benchmark与original benchmark在94%的模型对比决策上给出相同结论。
802	
803	    '
804	- name: item_generation_calibration
805	  plan_id: plan_006
806	  description: '生成replacement items并通过student simulation校准。对比prompt-based difficulty
807	    targeting与empirical calibration的精度。在holdout model panel上验证。
808	
809	    '
810	  expected_results:
811	    n_items_generated: 500
812	    n_items_passing_quality_filter: 420
813	    quality_filter_pass_rate: 0.84
814	    n_student_sim_models: 8
815	    student_sim_responses_per_item: 200
816	    difficulty_rho_student_sim: 0.78
817	    difficulty_rho_prompt_targeting: 0.28
818	    difficulty_rmse_student_sim: 0.14
819	    difficulty_rmse_prompt_targeting: 0.38
820	    discrimination_rho_student_sim: 0.62
821	    discrimination_rho_prompt_targeting: 0.15
822	    holdout_panel_equating_rho: 0.95
823	    construct_validity_factor_loading_corr: 0.85
824	    subject_match_accuracy: 0.92
825	    cognitive_level_match_accuracy: 0.78
826	    item_format_compliance: 0.97
827	  result_rationale: 'Student simulation校准（基于arXiv 2601.09953方法）的核心优势是empirical—— 它通过让diverse
828	    student models实际回答generated items来estimate difficulty， 而非依赖LLM的self-report。rho=0.78与原论文报告的r=0.75-0.82一致，因为MMLU
829	    的MCQ format与student simulation的optimal use case对齐（forced-choice items 比open-ended
830	    items更适合binary response modeling）。Prompt-based targeting 的rho=0.28与arXiv 2602.06631报告的rho=0.10-0.45一致——LLMs在内省difficulty
831	    时系统性地低估hard items、高估easy items，因为difficulty perception与generation capability不同。Student
832	    simulation的优势在于它bypasses这种miscalibration， 直接从behavioral responses estimate difficulty。Discrimination的rho=0.62较低
833	    于difficulty的0.78，因为discrimination是IRT的second-order parameter（item sensitivity
834	    to ability differences），inherently harder to control through generation——它依赖item的specific
835	    cognitive demands，而这些难以通过prompt engineering精确控制。Construct validity factor loading
836	    correlation=0.85表明 generated items load on相同的subject-specific factors，preserving
837	    MMLU的 bifactor structure。
838	
839	    '
840	  tables:
841	  - title: 'Table 13: Calibration Method Comparison'
842	    columns:
843	    - method
844	    - difficulty_rho
845	    - difficulty_rmse
846	    - discrimination_rho
847	    - n_items
848	    rows:
849	    - - Student_simulation
850	      - 0.78
851	      - 0.14
852	      - 0.62
853	      - 420
854	    - - Prompt_targeting
855	      - 0.28
856	      - 0.38
857	      - 0.15
858	      - 420
859	    - - Random_baseline
860	      - 0.05
861	      - 0.52
862	      - 0.03
863	      - 420
864	  - title: 'Table 14: Generated Item Quality Metrics'
865	    columns:
866	    - metric
867	    - value
868	    rows:
869	    - - Quality_filter_pass_rate
870	      - 0.84
871	    - - Subject_match_accuracy
872	      - 0.92
873	    - - Cognitive_level_match
874	      - 0.78
875	    - - Format_compliance
876	      - 0.97
877	    - - Factor_loading_corr
878	      - 0.85
879	    - - Holdout_equating_rho
880	      - 0.95
881	  figures_description:
882	  - 'Figure 19: Scatter plot of estimated vs true difficulty for student simulation
883	    (rho=0.78) and prompt targeting (rho=0.28). Student simulation points cluster
884	    near diagonal; prompt targeting shows systematic bias.'
885	  - 'Figure 20: Factor loading comparison between original and generated items on
886	    same MMLU subjects. High correspondence (r=0.85) confirms construct preservation.'
887	  analysis: 'Student simulation校准是item regeneration pipeline的关键enabler，将difficulty
888	    estimation精度从prompt-based的rho=0.28提升到0.78——接近3x improvement。 这一结果支持Claim 3的"empirically
889	    calibrated alternatives"承诺。Holdout panel equating rho=0.95达到psychometric standard，证明end-to-end
890	    pipeline（generation → simulation calibration → equating）可以produce functionally
891	    equivalent benchmark items。
892	
893	    '
894	- name: cumulative_bayesian_dif
895	  plan_id: plan_007
896	  description: '实现Bayesian累积DIF先验。模拟4次连续benchmark administration， 展示evidence accumulation带来的power提升。
897	
898	    '
899	  expected_results:
900	    n_administrations_simulated: 4
901	    n_models_per_administration: 40
902	    admin_1_power_medium_delta_1_0: 0.38
903	    admin_2_cumulative_power: 0.55
904	    admin_3_cumulative_power: 0.7
905	    admin_4_cumulative_power: 0.78
906	    power_gain_per_administration:
907	    - 0.38
908	    - 0.17
909	    - 0.15
910	    - 0.08
911	    bayesian_bf_threshold: 3.0
912	    false_discovery_rate: 0.04
913	    convergence_rate: 0.98
914	    prior_posterior_shrinkage: 0.42
915	    credible_interval_width_admin1: 0.68
916	    credible_interval_width_admin4: 0.31
917	  result_rationale: 'Bayesian累积先验的power gain来自evidence accumulation的数学性质——每次新的 administration提供independent
918	    observations，posterior distribution随data收窄。 从single administration的0.38到4次累积的0.78，power
919	    nearly doubles。Gain是 diminishing的（0.17→0.15→0.08），因为posterior precision的improvement是
920	    sub-linear in sample size（~√n scaling）。对medium effects（δ=1.0）这尤其重要， 因为classical
921	    DIF在single administration with N=40 per cohort时power不足 （Phase 2模拟显示N=50/δ=1.0时TPR仅0.04-0.07）。Bayesian
922	    approach通过 accumulating evidence across time解决了这个sample-size limitation——每次 administration贡献40个models，4次累积相当于effective
923	    sample of ~160， 但通过informative priors获得比simple pooling更高的statistical efficiency。
924	    BF threshold=3.0（moderate evidence）对应psychometric practice中的standard decision
925	    criterion。FDR=0.04 < 0.05表明error control有效。
926	
927	    '
928	  tables:
929	  - title: 'Table 15: Cumulative Bayesian DIF Power Over Administrations'
930	    columns:
931	    - administration
932	    - cumulative_n
933	    - power_delta_1_0
934	    - power_delta_1_4
935	    - CI_width
936	    rows:
937	    - - 1
938	      - 40
939	      - 0.38
940	      - 0.62
941	      - 0.68
942	    - - 2
943	      - 80
944	      - 0.55
945	      - 0.76
946	      - 0.48
947	    - - 3
948	      - 120
949	      - 0.7
950	      - 0.84
951	      - 0.37
952	    - - 4
953	      - 160
954	      - 0.78
955	      - 0.88
956	      - 0.31
957	  figures_description:
958	  - 'Figure 21: Power accumulation curves across 4 administrations for δ=0.6, 1.0,
959	    1.4. All show diminishing returns but substantial gains.'
960	  - 'Figure 22: Posterior distribution evolution for a representative DIF-flagged
961	    item across 4 administrations, showing progressive shrinkage toward true effect.'
962	  analysis: 'Bayesian累积DIF直接回应reviewer concern #2（sample sizes too small）。 4次累积后medium-effect
963	    power从0.38→0.78，使DIF对medium effects也实用化。 这一结果支持论文的"living benchmark"叙事——不需要一次性获得大样本，
964	    可以通过temporal accumulation逐步建立detection confidence。
965	
966	    '
967	- name: graceful_degradation_analysis
968	  plan_id: plan_008
969	  description: '分析benchmark在progressive item replacement下的validity degradation。 定义validity
970	    metrics，模拟5%-50% replacement，建立理论bounds。
971	
972	    '
973	  expected_results:
974	    replacement_rates:
975	    - 0.05
976	    - 0.1
977	    - 0.2
978	    - 0.5
979	    ranking_stability_rho_5pct: 0.99
980	    ranking_stability_rho_10pct: 0.97
981	    ranking_stability_rho_20pct: 0.95
982	    ranking_stability_rho_50pct: 0.89
983	    score_reliability_alpha_original: 0.94
984	    score_reliability_alpha_5pct: 0.93
985	    score_reliability_alpha_10pct: 0.93
986	    score_reliability_alpha_20pct: 0.91
987	    score_reliability_alpha_50pct: 0.87
988	    construct_coverage_jaccard_5pct: 0.98
989	    construct_coverage_jaccard_10pct: 0.96
990	    construct_coverage_jaccard_20pct: 0.92
991	    construct_coverage_jaccard_50pct: 0.83
992	    theoretical_rho_lower_bound_formula: rho >= 1 - k*replacement_rate*(1-r_replacement)
993	    theoretical_rho_lower_bound_20pct: 0.93
994	    empirical_rho_20pct: 0.95
995	    validity_threshold_replacement_rate: 0.35
996	  result_rationale: 'Graceful degradation的数学基础是：如果replacement items与original items测量相同
997	    construct（通过bifactor equating保证），且parameter estimation是unbiased的， 那么benchmark
998	    score的perturbation仅来自estimation error。Ranking stability (Spearman rho)随replacement
999	    rate的下降是approximately linear的：5%→0.99, 10%→0.97, 20%→0.95, 50%→0.89。0.95 threshold（psychometric
1000	    standard for "essentially equivalent"）在~20% replacement rate时hit——这意味着可以替换 最多20%的items（~2500
1001	    items on MMLU）while maintaining psychometrically equivalent rankings。50% replacement导致rho=0.89，仍然usable但not
1002	    equivalent。 Score reliability (Cronbach''s alpha)从0.94降至0.91 at 20%，因为replacement
1003	    items的discrimination estimates有更大variance（calibration uncertainty）， but alpha>0.90在psychometric
1004	    standards中仍属excellent。Construct coverage (Jaccard similarity of subject factor
1005	    coverage)在20%时为0.92，因为replacement item generation已constrained to same subject，但minor
1006	    gaps in specific cognitive sub-skills可能出现。Theoretical lower bound formula provides
1007	    conservative estimate，empirical results consistently exceed it（0.95 > 0.93 at
1008	    20%），validating the bound''s correctness。
1009	
1010	    '
1011	  tables:
1012	  - title: 'Table 16: Validity Metrics Under Progressive Replacement'
1013	    columns:
1014	    - replacement_rate
1015	    - ranking_rho
1016	    - reliability_alpha
1017	    - construct_jaccard
1018	    - score_rmse
1019	    rows:
1020	    - - 0.0
1021	      - 1.0
1022	      - 0.94
1023	      - 1.0
1024	      - 0.0
1025	    - - 0.05
1026	      - 0.99
1027	      - 0.93
1028	      - 0.98
1029	      - 0.008
1030	    - - 0.1
1031	      - 0.97
1032	      - 0.93
1033	      - 0.96
1034	      - 0.015
1035	    - - 0.2
1036	      - 0.95
1037	      - 0.91
1038	      - 0.92
1039	      - 0.025
1040	    - - 0.35
1041	      - 0.92
1042	      - 0.89
1043	      - 0.87
1044	      - 0.038
1045	    - - 0.5
1046	      - 0.89
1047	      - 0.87
1048	      - 0.83
1049	      - 0.052
1050	  - title: 'Table 17: Theoretical vs Empirical Bounds'
1051	    columns:
1052	    - replacement_rate
1053	    - theoretical_rho_lb
1054	    - empirical_rho
1055	    - bound_tight
1056	    rows:
1057	    - - 0.05
1058	      - 0.97
1059	      - 0.99
1060	      - false
1061	    - - 0.1
1062	      - 0.95
1063	      - 0.97
1064	      - false
1065	    - - 0.2
1066	      - 0.93
1067	      - 0.95
1068	      - false
1069	    - - 0.5
1070	      - 0.84
1071	      - 0.89
1072	      - false
1073	  figures_description:
1074	  - 'Figure 23: Validity degradation curves (rho, alpha, Jaccard) vs replacement rate,
1075	    with 0.95 threshold line marking ''psychometrically equivalent'' zone.'
1076	  - 'Figure 24: Theoretical lower bound vs empirical results, showing bound is conservative
1077	    but informative.'
1078	  analysis: 'Graceful degradation分析为benchmark regeneration建立了formal safety guarantees。
1079	    20% replacement threshold（rho≥0.95）为实际操作提供了clear guideline—— given MMLU上约10.7%
1080	    items被DIF flagged（plan_001），单轮replacement在安全范围内。 理论bound的conservativeness（empirical
1081	    consistently exceeds theoretical by 2-5pp） 提供额外safety margin。这一结果完成了Claim 3从detection
1082	    → generation → equating → validity guarantee的完整pipeline。
1083	
1084	    '
1085	- name: item_focused_trees
1086	  plan_id: plan_009
1087	  description: '实现Item-Focused Trees作为categorical cohort DIF的替代方案。 将model release
1088	    date作为continuous covariate，比较检测力和灵活性。
1089	
1090	    '
1091	  expected_results:
1092	    ift_tpr_delta_ge_1_4: 0.81
1093	    ift_tpr_delta_ge_1_0: 0.58
1094	    ift_fpr: 0.044
1095	    ift_auc: 0.9
1096	    ift_vs_ets_c_tpr_improvement: 0.03
1097	    ift_vs_ets_c_auc_improvement: -0.02
1098	    ift_detected_gradual_contamination: true
1099	    n_items_with_changepoint: 890
1100	    median_changepoint_date: 2023-06
1101	    changepoint_clustering_by_subject: true
1102	    ift_computation_time_seconds: 340
1103	    ets_c_computation_time_seconds: 28
1104	  result_rationale: 'Item-Focused Trees的优势在于不需要arbitrary cohort splits——它自动发现每个item
1105	    的contamination onset point（changepoint）作为tree split。TPR=0.81略优于 ETS C的0.78（+3pp），因为IFT可以为每个item找到optimal
1106	    focal/reference split 而非使用统一的pre/post cutoff。但AUC=0.90略低于ETS C的0.92，因为IFT在small
1107	    effects区间的precision较低（tree splitting在low-signal regime容易overfit）。 Changepoint
1108	    clustering by subject是重要的secondary finding——STEM subjects的 median changepoint早于humanities（2023-03
1109	    vs 2023-09），反映code-heavy training data对STEM contamination的earlier onset。890个items有detectable
1110	    changepoints， 与plan_001的1340 flagged items部分重叠（IFT的threshold更conservative因为tree
1111	    pruning）。计算成本是ETS C的12x，因为recursive partitioning需要对每个item 搜索所有可能splits，但仍在minutes级别（CPU
1112	    only），实际可用。IFT的主要paper value 是methodological：它证明contamination timing是item-specific而非cohort-uniform，
1113	    支持"contamination as gradual process"的narrative。
1114	
1115	    '
1116	  tables:
1117	  - title: 'Table 18: Item-Focused Trees vs ETS C Comparison'
1118	    columns:
1119	    - method
1120	    - tpr_ge_1_4
1121	    - tpr_ge_1_0
1122	    - fpr
1123	    - auc
1124	    - time_sec
1125	    rows:
1126	    - - ETS_C
1127	      - 0.78
1128	      - 0.45
1129	      - 0.038
1130	      - 0.92
1131	      - 28
1132	    - - Item_Focused_Trees
1133	      - 0.81
1134	      - 0.58
1135	      - 0.044
1136	      - 0.9
1137	      - 340
1138	    - - Combined
1139	      - 0.84
1140	      - 0.6
1141	      - 0.048
1142	      - 0.93
1143	      - 368
1144	  - title: 'Table 19: Contamination Changepoint Analysis'
1145	    columns:
1146	    - subject_group
1147	    - n_items_with_changepoint
1148	    - median_changepoint
1149	    - range
1150	    rows:
1151	    - - STEM
1152	      - 520
1153	      - 2023-03
1154	      - 2022-06 to 2024-01
1155	    - - Humanities
1156	      - 210
1157	      - 2023-09
1158	      - 2023-01 to 2024-06
1159	    - - Social_Sciences
1160	      - 160
1161	      - 2023-06
1162	      - 2022-09 to 2024-03
1163	  figures_description:
1164	  - 'Figure 25: Item-level changepoint distribution across calendar time, colored
1165	    by subject. STEM items show earlier contamination onset.'
1166	  - 'Figure 26: Example Item-Focused Tree for a specific MMLU item, showing splits
1167	    on release date and model family.'
1168	  analysis: IFT作为P2实验提供了methodological depth——contamination timing的item-specific 和subject-specific
1169	    patterns是novel finding，支持论文的temporal dynamics narrative。 Detection power的marginal
1170	    improvement（+3pp TPR）不足以替代ETS C作为primary method，但combined approach（union of flags）将TPR推到0.84。更重要的是IFT的
1171	    changepoint analysis为understanding contamination dynamics提供了unique evidence， 可作为analysis
1172	    section的secondary contribution。
1173	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1870990-f268-4f7d-923e-724b99e4a718",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "a40fe0cf-4000-4c7f-aebd-fc51c3ee0e69",
  "sourceToolAssistantUUID": "a1870990-f268-4f7d-923e-724b99e4a718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T20:18:20.266Z_

<details><summary>↩ Tool result · `toolu_01X9x8tNDLetwrMvvUJ2LvLF`</summary>

```text
1	narrative_guidance: '"Self-healing benchmark" story完整成立。DIF是唯一经RL训练不退化的contamination信号，
2	  理论论证（group-level ICC vs within-model distribution）获得经验支持。 Ensemble覆盖全effect-size谱，bifactor
3	  equating实现psychometrically等价的benchmark再生。 Headline: "DIF maintains 70-85% TPR where
4	  10 existing methods degrade to random under RL." 三条claims均以full strength呈现，ICLR投稿无需调整framing。
5	
6	  '
7	imagined_experiments:
8	- name: real_data_dif_mmlu
9	  plan_id: plan_001
10	  description: '对METABENCH MMLU真实响应矩阵（5,055 models × 12,508 items）执行DIF分析。 按release
11	    date切temporal cohorts（pre-2024 vs post-2024 + 年度细分）， 运行ETS C检测，用MMLU-CF作为partial
12	    ground truth外部验证。
13	
14	    '
15	  expected_results:
16	    n_models_total: 5055
17	    n_models_post_2024: 1820
18	    cohort_pre2024_size: 3235
19	    cohort_post2024_size: 1820
20	    annual_cohort_min_size: 92
21	    annual_cohort_max_size: 2100
22	    ets_c_items_flagged_C_level: 1340
23	    ets_c_items_flagged_B_or_C: 2870
24	    ets_c_tpr_delta_ge_1_4: 0.78
25	    ets_c_tpr_delta_ge_1_6: 0.83
26	    ets_c_fpr: 0.038
27	    ets_c_auc_delta_ge_1_4: 0.92
28	    mmlu_cf_correlation_with_dif_flags_phi: 0.42
29	    mmlu_cf_correlation_with_dif_flags_tetrachoric: 0.48
30	    n_mmlu_cf_overlapping_items: 2780
31	    dif_flagged_among_cf_modified: 0.61
32	    dif_flagged_among_cf_unmodified: 0.07
33	    sensitivity_cohort_split_tpr_range:
34	    - 0.72
35	    - 0.83
36	    sensitivity_threshold_tpr_range:
37	    - 0.68
38	    - 0.85
39	    real_irt_param_a_mean: 1.18
40	    real_irt_param_b_mean: -0.79
41	    real_irt_param_a_std: 0.42
42	  result_rationale: 'Phase 2模拟已在N=100/δ=1.6条件下达到TPR=0.7966，真实参数（a_mean=1.2, b_mean=-0.84）
43	    与模拟设定高度一致。Best档下真实数据复现模拟power的核心条件是：(1) METABENCH post-2024 cohort达到N≈1820，远超模拟的N=100下限，提供充足统计功效；(2)
44	    真实contamination effect sizes在高频benchmark如MMLU上确实存在δ≥1.4的大效应——GSM1K研究已证实10-13pp
45	    的accuracy gap，对应IRT尺度上δ≈1.5-2.0；(3) ETS C基于effect-size阈值而非p-value， 大样本下不会出现inflation问题，反而因estimation
46	    precision提高而TPR略优于模拟。 MMLU-CF验证的phi=0.42反映了partial ground truth的本质局限——CF修改的items与真正
47	    contaminated items有交集但不完全重叠，CF修改了部分未被contaminate的items（降低相关）， 同时未修改一些实际被contaminate的items。但0.42的phi系数在psychometric
48	    validation中 已属中等偏强，足以作为convergent validity evidence。FPR=0.038与模拟的0.036-0.042 区间一致，因为false
49	    positive rate主要由ETS C的Δ_MH阈值决定，不依赖sample size。
50	
51	    '
52	  tables:
53	  - title: 'Table 1: DIF Detection Power on METABENCH MMLU Real Data'
54	    columns:
55	    - cohort_split
56	    - N_focal
57	    - N_ref
58	    - delta_range
59	    - TPR
60	    - FPR
61	    - AUC
62	    rows:
63	    - - pre2024_vs_post2024
64	      - 1820
65	      - 3235
66	      - ≥1.4
67	      - 0.78
68	      - 0.038
69	      - 0.92
70	    - - pre2024_vs_post2024
71	      - 1820
72	      - 3235
73	      - ≥1.6
74	      - 0.83
75	      - 0.038
76	      - 0.94
77	    - - pre2024_vs_post2024
78	      - 1820
79	      - 3235
80	      - ≥1.0
81	      - 0.51
82	      - 0.041
83	      - 0.83
84	    - - 2022_vs_2024
85	      - 920
86	      - 2100
87	      - ≥1.4
88	      - 0.76
89	      - 0.036
90	      - 0.91
91	    - - 2023_vs_2025
92	      - 680
93	      - 1340
94	      - ≥1.4
95	      - 0.74
96	      - 0.039
97	      - 0.9
98	    - - annual_finest
99	      - 92
100	      - 2100
101	      - ≥1.4
102	      - 0.72
103	      - 0.042
104	      - 0.88
105	  - title: 'Table 2: MMLU-CF External Validation'
106	    columns:
107	    - category
108	    - n_items
109	    - dif_flagged_rate
110	    - description
111	    rows:
112	    - - CF_modified_items
113	      - 2780
114	      - 0.61
115	      - Items significantly changed in MMLU-CF
116	    - - CF_unmodified_items
117	      - 9728
118	      - 0.07
119	      - Items unchanged in MMLU-CF
120	    - - phi_coefficient
121	      - null
122	      - 0.42
123	      - Association between DIF flag and CF modification
124	    - - tetrachoric_r
125	      - null
126	      - 0.48
127	      - Latent correlation estimate
128	  figures_description:
129	  - 'Figure 1: Heatmap of ETS C Δ_MH values across 12,508 MMLU items, ordered by subject.
130	    Clear clustering of large-DIF items in STEM subjects (math, CS, physics) that
131	    are more likely contaminated through code training data.'
132	  - 'Figure 2: ROC curves comparing DIF detection at different cohort splits. Curves
133	    are tightly clustered (AUC range 0.88-0.94), demonstrating robustness to arbitrary
134	    cohort boundary choice.'
135	  - 'Figure 3: Scatter plot of DIF Δ_MH magnitude vs MMLU-CF modification indicator.
136	    Violin plots showing clear separation between CF-modified (higher DIF) and CF-unmodified
137	    items.'
138	  analysis: '真实数据DIF检测power与Phase 2模拟高度一致，验证了模拟参数设定的生态效度。 关键发现：(1) MMLU上约10.7%的items呈现ETS
139	    C级DIF，集中在STEM领域，与contamination through pretraining code data的预期一致；(2) MMLU-CF外部验证提供convergent
140	    evidence， phi=0.42虽非完美但在partial ground truth条件下合理——完美相关本身不可信，因为CF的 modification策略与contamination并非一一对应；(3)
141	    敏感性分析显示TPR在不同cohort 定义下稳定在0.72-0.83区间，最弱的annual finest split（N_focal=92）仍达0.72，
142	    正好符合Phase 2模拟在N=80条件下的预测。这一结果直接支持Claim 1的real-data validation。
143	
144	    '
145	- name: rl_robustness_validation
146	  plan_id: plan_002
147	  description: '经验验证DIF的RL-robustness。构建SFT-only cohort和含RL-trained模型的cohort， 同时运行DIF与传统检测器（Min-K%、ConStat
148	    perturbation、DVD），对比RL条件下的退化。
149	
150	    '
151	  expected_results:
152	    n_rl_models_evaluated: 14
153	    n_sft_models_evaluated: 40
154	    rl_models_list: 'DeepSeek-R1, DeepSeek-R1-Distill-{7B,14B,32B,70B}, Qwen2.5-RL-{7B,72B},
155	      Llama-3.1-Nemotron-Ultra-253B, QwQ-32B, Skywork-OR1-{8B,32B}, K1.5-Chat, Eurus-2-7B-PRIME,
156	      OpenThinker-7B
157	
158	      '
159	    dif_tpr_sft_cohort_delta_ge_1_4: 0.79
160	    dif_tpr_rl_cohort_delta_ge_1_4: 0.76
161	    dif_power_retention_ratio: 0.96
162	    dif_fpr_sft_cohort: 0.037
163	    dif_fpr_rl_cohort: 0.041
164	    mink_auroc_sft: 0.72
165	    mink_auroc_rl: 0.51
166	    mink_degradation_pp: 21
167	    constat_auroc_sft: 0.68
168	    constat_auroc_rl: 0.53
169	    constat_degradation_pp: 15
170	    dvd_auroc_sft: 0.65
171	    dvd_auroc_rl: 0.54
172	    dvd_degradation_pp: 11
173	    perplexity_auroc_sft: 0.61
174	    perplexity_auroc_rl: 0.5
175	    lowercase_auroc_sft: 0.58
176	    lowercase_auroc_rl: 0.49
177	    traditional_mean_auroc_sft: 0.65
178	    traditional_mean_auroc_rl: 0.51
179	    p_value_dif_retention_paired_t: 0.62
180	    p_value_traditional_degradation_paired_t: 0.0003
181	  result_rationale: 'DIF的RL-robustness源于其检测机制的根本差异。传统检测器（Min-K%、perplexity-based）
182	    依赖within-model output distributions——GRPO/PPO通过policy smoothing将memorized items
183	    的output distribution调整到与clean items相似，消除可检测的distributional anomaly。 Wang et al.
184	    (ICLR 2026)已实证证明这种退化：~156 GRPO steps即可将多数检测器降至 near-random。DIF则完全不同：它比较的是group-level
185	    Item Characteristic Curves—— "给定相同latent ability θ，focal group（post-training cohort）在item
186	    j上的correct probability是否高于reference group"。RL训练可以smooth output token distributions，
187	    但无法消除behavioral fact："这个模型答对了这道它memorized的题"。除非RL训练能让模型 在memorized items上故意答错（这会negate
188	    contamination的目的），否则group-level behavioral pattern必然保留。Power retention ratio=0.96（而非1.0）的微小衰减来自
189	    RL模型通常具有更高的general ability θ，这略微压缩了DIF effect size的估计——但这是 统计层面的minor attenuation，不是mechanistic
190	    failure。传统检测器的AUROC从0.65降至 0.51（mean across methods），与Wang et al.报告的14-20pp退化一致。
191	
192	    '
193	  tables:
194	  - title: 'Table 3: DIF vs Traditional Detectors Under RL Training'
195	    columns:
196	    - method
197	    - auroc_sft_cohort
198	    - auroc_rl_cohort
199	    - degradation_pp
200	    - p_value
201	    rows:
202	    - - DIF_ETS_C
203	      - 0.91
204	      - 0.9
205	      - 1
206	      - 0.62
207	    - - Min-K%
208	      - 0.72
209	      - 0.51
210	      - 21
211	      - 0.0002
212	    - - ConStat_perturbation
213	      - 0.68
214	      - 0.53
215	      - 15
216	      - 0.001
217	    - - DVD_generation_var
218	      - 0.65
219	      - 0.54
220	      - 11
221	      - 0.004
222	    - - Perplexity
223	      - 0.61
224	      - 0.5
225	      - 11
226	      - 0.003
227	    - - Lowercase
228	      - 0.58
229	      - 0.49
230	      - 9
231	      - 0.008
232	    - - zlib_ratio
233	      - 0.6
234	      - 0.5
235	      - 10
236	      - 0.005
237	    - - Top-K_prob
238	      - 0.63
239	      - 0.52
240	      - 11
241	      - 0.003
242	    - - Ref_model_loss
243	      - 0.67
244	      - 0.53
245	      - 14
246	      - 0.002
247	    - - Neighbor_text
248	      - 0.59
249	      - 0.5
250	      - 9
251	      - 0.007
252	    - - DetectGPT
253	      - 0.55
254	      - 0.49
255	      - 6
256	      - 0.04
257	  - title: 'Table 4: DIF Power Retention by RL Training Intensity'
258	    columns:
259	    - model_group
260	    - n_models
261	    - dif_tpr_delta_ge_1_4
262	    - dif_fpr
263	    - retention_vs_sft
264	    rows:
265	    - - SFT_only
266	      - 40
267	      - 0.79
268	      - 0.037
269	      - 1.0
270	    - - Light_RL_under_500_steps
271	      - 6
272	      - 0.78
273	      - 0.039
274	      - 0.99
275	    - - Heavy_RL_over_500_steps
276	      - 8
277	      - 0.75
278	      - 0.041
279	      - 0.95
280	    - - All_RL
281	      - 14
282	      - 0.76
283	      - 0.041
284	      - 0.96
285	  figures_description:
286	  - 'Figure 4: Bar chart comparing AUROC of 11 detection methods on SFT vs RL cohorts.
287	    DIF bar is near-identical height; all others show clear drops. Error bars from
288	    bootstrap.'
289	  - 'Figure 5: Scatter plot of DIF Δ_MH estimated on SFT cohort vs RL cohort for same
290	    items. Points cluster tightly along the diagonal (r=0.94), demonstrating effect
291	    size stability.'
292	  - 'Figure 6: Conceptual diagram contrasting DIF''s group-level ICC mechanism vs
293	    within-model distribution-based detectors, illustrating why RL smoothing affects
294	    the latter but not the former.'
295	  analysis: 'RL-robustness经验验证是论文最核心的卖点。DIF power retention ratio=0.96意味着 RL训练对DIF检测力几乎无影响（paired
296	    t-test p=0.62，无统计显著差异），而10种传统 检测器平均退化14pp至near-random（mean AUROC=0.51）。这直接验证了理论预测：
297	    DIF操作在group-level behavioral space，RL无法在不放弃contamination benefit的 情况下消除这一信号。Heavy
298	    RL（>500 steps）组的轻微衰减（retention=0.95）可归因于 更高general ability导致的effect size estimation
299	    compression，而非mechanism failure。 这一结果使headline claim成立："DIF maintains 76% TPR
300	    where 10 existing methods degrade to random under RL training."
301	
302	    '
303	- name: constat_perturbation_eval
304	  plan_id: plan_003a
305	  description: '独立评估ConStat-style perturbation testing在MMLU上的检测力， 生成200+ items的语义等价改写，比较原始vs改写表现，刻画effect
306	    size谱上的检测力。
307	
308	    '
309	  expected_results:
310	    n_items_reformulated: 240
311	    n_models_tested: 35
312	    n_reformulations_per_item: 5
313	    constat_tpr_non_rl_delta_ge_0_6: 0.68
314	    constat_tpr_non_rl_delta_ge_1_0: 0.74
315	    constat_tpr_non_rl_delta_ge_1_4: 0.62
316	    constat_tpr_rl_delta_ge_0_6: 0.31
317	    constat_tpr_rl_delta_ge_1_0: 0.38
318	    constat_fpr_non_rl: 0.06
319	    constat_fpr_rl: 0.08
320	    constat_fdr_controlled_alpha_0_05: 0.048
321	    mean_accuracy_drop_contaminated_items: 0.18
322	    mean_accuracy_drop_clean_items: 0.03
323	    reformulation_semantic_similarity: 0.91
324	  result_rationale: 'ConStat的检测逻辑是：contaminated models在original items上表现异常好，但在 semantically
325	    equivalent reformulations上表现回落——因为memorization是surface-form specific的。在non-RL
326	    models上，这一逻辑有效：SFT训练的memorization直接绑定到 token sequences，reformulation打破了这种绑定，导致contaminated
327	    items上出现显著 accuracy drop（mean=0.18 vs clean items的0.03）。TPR在δ≥0.6时达0.68，因为即使 中等效应的contamination也会在perturbation下暴露。但在δ≥1.4时TPR反而降到0.62，
328	    因为极大effect size的items通常是extremely easy items（即使不contaminate也正确率高）， reformulation后的drop较小。ConStat在RL模型上急剧退化（TPR从0.68降至0.31），因为
329	    GRPO/PPO的policy optimization使模型学会了更general的answer patterns而非 surface-form memorization——RL模型在reformulated
330	    items上的accuracy drop较小， 使perturbation signal模糊化。这正是ConStat在ensemble中的定位：覆盖non-RL
331	    models的 medium effect sizes（DIF在δ<1.0时power不足），但在RL场景下需要DIF补位。
332	
333	    '
334	  tables:
335	  - title: 'Table 5: ConStat Detection Power by Effect Size and Model Type'
336	    columns:
337	    - model_type
338	    - delta_range
339	    - n_items
340	    - TPR
341	    - FPR
342	    - FDR
343	    rows:
344	    - - non_RL
345	      - ≥0.6
346	      - 142
347	      - 0.68
348	      - 0.06
349	      - 0.048
350	    - - non_RL
351	      - ≥1.0
352	      - 87
353	      - 0.74
354	      - 0.06
355	      - 0.041
356	    - - non_RL
357	      - ≥1.4
358	      - 48
359	      - 0.62
360	      - 0.06
361	      - 0.052
362	    - - RL
363	      - ≥0.6
364	      - 142
365	      - 0.31
366	      - 0.08
367	      - 0.12
368	    - - RL
369	      - ≥1.0
370	      - 87
371	      - 0.38
372	      - 0.08
373	      - 0.1
374	    - - all_models
375	      - ≥0.6
376	      - 142
377	      - 0.52
378	      - 0.07
379	      - 0.07
380	  figures_description:
381	  - 'Figure 7: Paired accuracy comparison (original vs reformulated) for contaminated
382	    vs clean items, split by model type (SFT vs RL). Clear separation for SFT, collapsed
383	    for RL.'
384	  - 'Figure 8: ConStat detection power curve across effect size spectrum, overlaid
385	    with DIF power curve. Crossover around δ≈1.0 shows complementary regions.'
386	  analysis: 'ConStat在non-RL模型上的medium-effect-size检测力（δ≥0.6: TPR=0.68）验证了其在 ensemble中的角色——填补DIF在small-to-medium
387	    effects上的盲区。RL条件下的急剧退化 （TPR从0.68→0.31）与Wang et al.的发现一致，因为perturbation sensitivity本质上仍
388	    依赖于surface-form specific memorization pattern，RL训练将其平滑化。FDR控制在 non-RL条件下有效（0.048
389	    < 0.05），但RL条件下FDR升至0.12，需在ensemble中对RL模型 降低ConStat权重。
390	
391	    '
392	- name: dvd_generation_variance_eval
393	  plan_id: plan_003b
394	  description: '独立评估DVD generation variance在MMLU上的检测力，对10-15个open-weight模型 每item生成50次response，计算generation
395	    variance分数，检测bimodal distributions。
396	
397	    '
398	  expected_results:
399	    n_models_evaluated: 12
400	    n_items_evaluated: 2000
401	    responses_per_item: 50
402	    temperature_range:
403	    - 0.7
404	    - 1.0
405	    dvd_tpr_variant_contamination: 0.65
406	    dvd_tpr_verbatim_contamination: 0.38
407	    dvd_tpr_all_contamination: 0.52
408	    dvd_fpr: 0.07
409	    dvd_auroc_variant: 0.78
410	    dvd_auroc_verbatim: 0.62
411	    dvd_auroc_overall: 0.71
412	    bimodal_detection_rate_contaminated: 0.58
413	    bimodal_detection_rate_clean: 0.04
414	    dvd_tpr_rl_variant: 0.47
415	    dvd_tpr_rl_verbatim: 0.29
416	    generation_variance_contaminated_mean: 0.31
417	    generation_variance_clean_mean: 0.12
418	  result_rationale: 'DVD的检测逻辑基于generation variance：contaminated models在memorized items上的
419	    generation distribution呈现bimodal pattern——当temperature sampling触发"recall" mode时high
420	    confidence输出memorized answer，否则回到general reasoning mode。 Variant contamination（模型见过item的变体而非原始形式）下DVD最有效（TPR=0.65），
421	    因为variant exposure创造了partial memorization——模型"几乎记得"答案，导致生成 在confident recall和uncertain
422	    reasoning之间振荡，产生高variance和清晰的bimodality。 Verbatim contamination下DVD效果较差（TPR=0.38），因为完全memorized
423	    items的生成 variance反而很低（模型每次都确信地输出相同答案），bimodal signal消失。这使DVD与DIF 形成互补：DIF在verbatim
424	    large effects上最强，DVD在variant contamination上最强。 RL条件下DVD退化到TPR=0.47（variant），因为GRPO
425	    smoothing降低了generation variance 的discriminability，但退化幅度小于ConStat（因为DVD利用的是sampling-level
426	    variance 而非perturbation sensitivity，RL对sampling variance的影响弱于对perturbation response的影响）。
427	
428	    '
429	  tables:
430	  - title: 'Table 6: DVD Detection Power by Contamination Type'
431	    columns:
432	    - contamination_type
433	    - model_type
434	    - n_items
435	    - TPR
436	    - FPR
437	    - AUROC
438	    rows:
439	    - - variant
440	      - non_RL
441	      - 320
442	      - 0.65
443	      - 0.07
444	      - 0.78
445	    - - verbatim
446	      - non_RL
447	      - 480
448	      - 0.38
449	      - 0.07
450	      - 0.62
451	    - - all
452	      - non_RL
453	      - 800
454	      - 0.52
455	      - 0.07
456	      - 0.71
457	    - - variant
458	      - RL
459	      - 320
460	      - 0.47
461	      - 0.09
462	      - 0.68
463	    - - verbatim
464	      - RL
465	      - 480
466	      - 0.29
467	      - 0.09
468	      - 0.57
469	    - - all
470	      - RL
471	      - 800
472	      - 0.38
473	      - 0.09
474	      - 0.63
475	  figures_description:
476	  - 'Figure 9: Distribution of generation variance scores for contaminated (variant
477	    vs verbatim) and clean items. Variant contamination shows clear right shift; verbatim
478	    shows compressed distribution.'
479	  - 'Figure 10: Bimodality coefficient heatmap across items and models, with contamination
480	    status overlay. Clear bimodal clusters for variant-contaminated items.'
481	  analysis: 'DVD填补了ensemble中的variant contamination盲区。DIF主要检测verbatim large effects
482	    （模型在original item上的behavioral anomaly），ConStat检测non-RL medium effects， DVD则捕获variant
483	    contamination——模型见过类似但不完全相同的items，产生partial memorization的generation variance signal。三者的complementary
484	    coverage pattern 在best档下清晰呈现，为ensemble fusion提供了solid foundation。
485	
486	    '
487	- name: ensemble_fusion
488	  plan_id: plan_003c
489	  description: '融合DIF + ConStat + DVD为multi-signal ensemble。校准per-signal阈值， 评估majority
490	    voting和weighted fusion，展示ensemble coverage覆盖全effect-size谱。
491	
492	    '
493	  expected_results:
494	    ensemble_tpr_full_spectrum: 0.87
495	    ensemble_tpr_delta_ge_1_4: 0.91
496	    ensemble_tpr_delta_ge_1_0: 0.85
497	    ensemble_tpr_delta_ge_0_6: 0.78
498	    ensemble_fpr: 0.08
499	    ensemble_auroc: 0.93
500	    majority_2of3_tpr: 0.72
501	    majority_2of3_fpr: 0.04
502	    weighted_fusion_tpr: 0.87
503	    weighted_fusion_fpr: 0.08
504	    dif_unique_detections_pct: 0.28
505	    constat_unique_detections_pct: 0.15
506	    dvd_unique_detections_pct: 0.12
507	    all_three_overlap_pct: 0.31
508	    two_signal_overlap_pct: 0.14
509	    ensemble_tpr_rl_models: 0.82
510	    ensemble_tpr_non_rl_models: 0.9
511	    optimal_weights_dif: 0.45
512	    optimal_weights_constat: 0.3
513	    optimal_weights_dvd: 0.25
514	  result_rationale: 'Ensemble的power来源于三信号的systematic complementarity。在best档下，每个信号
515	    覆盖不同的effect-size × model-type区间：DIF覆盖large effects（δ≥1.4）且RL-robust， ConStat覆盖non-RL
516	    medium effects（δ≥0.6），DVD覆盖variant contamination。 Weighted fusion（DIF=0.45, ConStat=0.30,
517	    DVD=0.25）优于majority voting （TPR 0.87 vs 0.72），因为majority voting要求至少2/3信号agree，而在信号覆盖不
518	    重叠的区间（如RL+large effect只有DIF有效），single-signal detection被majority voting过滤掉。Weighted
519	    fusion允许high-confidence single signal触发detection。 Full-spectrum TPR=0.87的构成：δ≥1.4区间DIF主导（TPR=0.91），δ=0.6-1.4区间ConStat
520	    补位（将DIF单独的~0.40 TPR提升到ensemble的0.78），variant contamination区间DVD 补位（unique detections
521	    12%）。FPR=0.08略高于single-signal的0.04-0.07，这是 multi-signal fusion的inherent trade-off——更多信号意味着更多false
522	    positive opportunities，但0.08仍在可接受范围内。RL模型上ensemble TPR=0.82（vs non-RL的0.90）， 差距来自ConStat在RL条件下的退化被DIF的RL-robustness部分补偿。
523	
524	    '
525	  tables:
526	  - title: 'Table 7: Ensemble vs Individual Signal Detection Power'
527	    columns:
528	    - method
529	    - tpr_full
530	    - tpr_ge_1_4
531	    - tpr_ge_0_6
532	    - fpr
533	    - auroc
534	    rows:
535	    - - DIF_only
536	      - 0.58
537	      - 0.78
538	      - 0.35
539	      - 0.038
540	      - 0.84
541	    - - ConStat_only
542	      - 0.44
543	      - 0.62
544	      - 0.68
545	      - 0.06
546	      - 0.76
547	    - - DVD_only
548	      - 0.38
549	      - 0.38
550	      - 0.45
551	      - 0.07
552	      - 0.71
553	    - - Majority_2of3
554	      - 0.72
555	      - 0.81
556	      - 0.64
557	      - 0.04
558	      - 0.89
559	    - - Weighted_fusion
560	      - 0.87
561	      - 0.91
562	      - 0.78
563	      - 0.08
564	      - 0.93
565	  - title: 'Table 8: Signal Complementarity Analysis'
566	    columns:
567	    - detection_source
568	    - pct_of_total_detections
569	    - example_regime
570	    rows:
571	    - - DIF_unique
572	      - 0.28
573	      - Large effect + RL models
574	    - - ConStat_unique
575	      - 0.15
576	      - Medium effect + non-RL models
577	    - - DVD_unique
578	      - 0.12
579	      - Variant contamination
580	    - - DIF_and_ConStat
581	      - 0.08
582	      - Large effect + non-RL
583	    - - DIF_and_DVD
584	      - 0.04
585	      - Large variant + RL
586	    - - ConStat_and_DVD
587	      - 0.02
588	      - Medium variant + non-RL
589	    - - All_three
590	      - 0.31
591	      - Large effect + non-RL + verbatim
592	  figures_description:
593	  - 'Figure 11: Venn diagram of detections by three signals, showing complementary
594	    coverage with ~45% items detected by only one or two signals.'
595	  - 'Figure 12: Detection power heatmap across effect-size (δ) × model-type (SFT/RL)
596	    × contamination-type (verbatim/variant) grid. Each cell colored by which signal(s)
597	    contribute most.'
598	  - 'Figure 13: Precision-recall curves for individual signals vs ensemble. Ensemble
599	    dominates at all recall levels.'
600	  analysis: 'Ensemble coverage分析是Claim 2的核心evidence。三信号互补的清晰pattern—— DIF覆盖RL+large
601	    effects，ConStat覆盖non-RL+medium effects，DVD覆盖variant contamination——使full-spectrum
602	    TPR从任何单信号的最高0.58提升到0.87。 关键是unique detections分析：每个信号贡献12-28%的独占检测，证明任何单信号都不可替代。
603	    Weighted fusion优于majority voting 15pp，反映了信号互补性超过信号冗余性—— 在most detection regimes下只有1-2个信号active，majority
604	    voting的"2-of-3 agreement" 要求过于保守。
605	
606	    '
607	- name: cross_benchmark_gsm8k
608	  plan_id: plan_004
609	  description: '在GSM8K上复制DIF分析，用GSM1K作为contamination ground truth。 收集50+模型的per-item
610	    binary responses，运行temporal cohort DIF， 将DIF flags与per-model GSM8K-GSM1K accuracy
611	    gap关联。
612	
613	    '
614	  expected_results:
615	    n_models_gsm8k: 62
616	    n_items_gsm8k: 1319
617	    n_items_gsm1k: 1250
618	    cohort_pre2024_n: 28
619	    cohort_post2024_n: 34
620	    dif_flagged_items_gsm8k: 178
621	    dif_flagged_rate: 0.135
622	    dif_tpr_gsm8k_delta_ge_1_4: 0.74
623	    dif_fpr_gsm8k: 0.042
624	    gsm8k_gsm1k_gap_mean_all_models: 0.068
625	    gsm8k_gsm1k_gap_mean_contaminated_models: 0.112
626	    gsm8k_gsm1k_gap_mean_clean_models: 0.024
627	    gsm8k_gsm1k_gap_dif_correlation_spearman: 0.43
628	    gsm8k_gsm1k_gap_dif_correlation_pearson: 0.38
629	    per_item_dif_vs_gap_correlation: 0.41
630	    gsm8k_dif_auc: 0.88
631	  result_rationale: 'GSM8K是ideal validation target因为GSM1K提供了independent contamination
632	    ground truth—— GSM1K是GSM8K的分布匹配但全新的test set，GSM8K-GSM1K accuracy gap直接反映 contamination
633	    benefit。DIF在GSM8K上的TPR=0.74（vs MMLU的0.78）略低，因为： (1) 样本量较小（62 models vs MMLU的5055），cohort
634	    sizes（28 vs 34）接近power 下限；(2) GSM8K是math reasoning benchmark，item discrimination更依赖reasoning
635	    ability而非factual recall，DIF effect sizes分布略低于MMLU。Spearman rho=0.43 between per-model
636	    DIF flag count和GSM8K-GSM1K gap是中等相关，因为DIF flags是 binary item-level indicators而GSM8K-GSM1K
637	    gap是continuous model-level metric， 二者在aggregation level上不同——item-level DIF flag到model-level
638	    gap的mapping 需要通过contamination load（模型见过的flagged items数量）mediating。直接的 per-item
639	    correlation（item的DIF flag vs 该item的across-model gap）达到0.41， 提供convergent evidence。这一跨benchmark验证支持DIF检测的generalizability，
640	    不仅限于MMLU。
641	
642	    '
643	  tables:
644	  - title: 'Table 9: DIF Detection on GSM8K with GSM1K Ground Truth'
645	    columns:
646	    - metric
647	    - value
648	    rows:
649	    - - n_models
650	      - 62
651	    - - n_items
652	      - 1319
653	    - - DIF_flagged_items
654	      - 178
655	    - - DIF_flagged_rate
656	      - 0.135
657	    - - TPR_delta_ge_1_4
658	      - 0.74
659	    - - FPR
660	      - 0.042
661	    - - AUC
662	      - 0.88
663	    - - GSM8K-GSM1K_gap_DIF_corr_spearman
664	      - 0.43
665	  - title: 'Table 10: GSM8K-GSM1K Gap by Model Contamination Status'
666	    columns:
667	    - model_group
668	    - n_models
669	    - mean_gap
670	    - std_gap
671	    - median_gap
672	    rows:
673	    - - DIF_high_contamination
674	      - 18
675	      - 0.112
676	      - 0.034
677	      - 0.105
678	    - - DIF_low_contamination
679	      - 22
680	      - 0.051
681	      - 0.028
682	      - 0.047
683	    - - DIF_clean
684	      - 22
685	      - 0.024
686	      - 0.019
687	      - 0.02
688	  figures_description:
689	  - 'Figure 14: Scatter plot of per-model DIF contamination load (count of flagged
690	    items answered correctly) vs GSM8K-GSM1K accuracy gap. Positive trend with Spearman
691	    ρ=0.43.'
692	  - 'Figure 15: Item-level DIF magnitude (Δ_MH) distribution on GSM8K, overlaid with
693	    GSM1K-based ground truth labels.'
694	  analysis: '跨benchmark验证成功，DIF在GSM8K上的检测力（TPR=0.74）与MMLU结果一致（考虑到 较小样本量下的预期衰减）。GSM8K-GSM1K
695	    gap与DIF flags的spearman rho=0.43提供了 独立于MMLU-CF的external validation，使用完全不同的ground
696	    truth来源。 13.5%的GSM8K items被flagged，与Mirzadeh et al. (NeurIPS 2024)报告的GSM8K contamination
697	    prevalence一致。
698	
699	    '
700	- name: bifactor_irt_equating_pilot
701	  plan_id: plan_005
702	  description: '在METABENCH MMLU数据上pilot bifactor IRT equating。拟合bifactor model （general
703	    factor + subject-specific factors），选择anchor items， 通过fixed-parameter calibration校准replacement
704	    items，验证equated score等价性。
705	
706	    '
707	  expected_results:
708	    bifactor_model_converged: true
709	    n_general_factor_loadings_gt_0_3: 11200
710	    n_subject_factors: 57
711	    subject_factor_loading_mean: 0.42
712	    general_factor_loading_mean: 0.58
713	    general_factor_variance_explained: 0.48
714	    total_variance_explained: 0.72
715	    n_anchor_items_selected: 3100
716	    anchor_item_criteria: No DIF (ETS A), discrimination a>0.8, low missingness
717	    anchor_item_stability_rho: 0.98
718	    n_replacement_items_calibrated: 500
719	    equating_spearman_rho: 0.97
720	    equating_pearson_r: 0.96
721	    equating_rank_displacement_mean: 1.8
722	    equating_rank_displacement_max: 12
723	    equating_score_rmse: 0.021
724	    equating_classification_agreement: 0.94
725	    chi_square_equating_test_p: 0.34
726	    anchor_item_dif_free_rate: 0.92
727	    replacement_item_factor_loading_corr: 0.88
728	  result_rationale: 'Bifactor model在MMLU上的良好拟合源于MMLU的psychometric structure：它是multi-subject
729	    benchmark，每个subject（57个）构成一个specific factor，同时存在general cognitive ability factor（因为performance
730	    across subjects是正相关的——general intelligence drives cross-domain performance）。General
731	    factor解释48%方差，与educational testing中的typical bifactor results一致。Anchor items（3100个，~25%）是高稳定性、
732	    无DIF的items——在temporal cohorts间parameter estimates一致，表明未被contaminate。 25%的anchor
733	    rate在psychometric equating中是standard practice（Kolen & Brennan 推荐20-30%）。Equating后的Spearman
734	    rho=0.97表明模型rankings在original vs replaced benchmark间高度保持——rank displacement mean=1.8意味着平均每个模型只
735	    移动1-2个排名位置。这一精度来自fixed-parameter calibration的mechanics： replacement items的parameters在anchor
736	    item scale上calibrate，数学上保证了 score comparability（up to estimation error）。Score
737	    RMSE=0.021（在0-1 scale上） 反映estimation uncertainty而非systematic bias。Chi-square equating
738	    test p=0.34 表明无法拒绝"equated scores等价于original scores"的null hypothesis，即equating
739	    在统计上成功。
740	
741	    '
742	  tables:
743	  - title: 'Table 11: Bifactor Model Fit Statistics'
744	    columns:
745	    - metric
746	    - value
747	    rows:
748	    - - RMSEA
749	      - 0.028
750	    - - CFI
751	      - 0.96
752	    - - TLI
753	      - 0.95
754	    - - General_factor_variance_pct
755	      - 0.48
756	    - - Subject_factors_variance_pct
757	      - 0.24
758	    - - Total_variance_explained
759	      - 0.72
760	    - - N_subjects_factors
761	      - 57
762	  - title: 'Table 12: Equating Results — Original vs Replaced Benchmark'
763	    columns:
764	    - metric
765	    - value
766	    - interpretation
767	    rows:
768	    - - Spearman_rho
769	      - 0.97
770	      - Rankings nearly identical
771	    - - Pearson_r
772	      - 0.96
773	      - Scores linearly related
774	    - - RMSE
775	      - 0.021
776	      - Minimal score displacement
777	    - - Mean_rank_displacement
778	      - 1.8
779	      - Average 1-2 rank positions
780	    - - Max_rank_displacement
781	      - 12
782	      - Worst case still within noise
783	    - - Classification_agreement
784	      - 0.94
785	      - 94% same performance tier
786	    - - Chi_sq_test_p
787	      - 0.34
788	      - Cannot reject equivalence
789	  figures_description:
790	  - 'Figure 16: Scatter plot of model scores on original vs equated benchmark (500
791	    items replaced). Points tightly clustered along diagonal with Pearson r=0.96.'
792	  - 'Figure 17: Bifactor model path diagram for top-5 MMLU subjects showing general
793	    and subject-specific factor loadings.'
794	  - 'Figure 18: Rank displacement distribution — right-skewed with most models displaced
795	    by 0-3 positions.'
796	  analysis: 'Bifactor IRT equating在MMLU上达到psychometric standard（rho=0.97, RMSE=0.021），
797	    证明了Claim 3的可行性——contaminated items可以被replaced而preserving benchmark comparability。关键支撑是25%
798	    anchor items提供了stable calibration bridge， bifactor structure正确捕获了MMLU的multi-subject
799	    + general ability structure。 Classification agreement=0.94意味着在实际的model evaluation场景中，equated
800	    benchmark与original benchmark在94%的模型对比决策上给出相同结论。
801	
802	    '
803	- name: item_generation_calibration
804	  plan_id: plan_006
805	  description: '生成replacement items并通过student simulation校准。对比prompt-based difficulty
806	    targeting与empirical calibration的精度。在holdout model panel上验证。
807	
808	    '
809	  expected_results:
810	    n_items_generated: 500
811	    n_items_passing_quality_filter: 420
812	    quality_filter_pass_rate: 0.84
813	    n_student_sim_models: 8
814	    student_sim_responses_per_item: 200
815	    difficulty_rho_student_sim: 0.78
816	    difficulty_rho_prompt_targeting: 0.28
817	    difficulty_rmse_student_sim: 0.14
818	    difficulty_rmse_prompt_targeting: 0.38
819	    discrimination_rho_student_sim: 0.62
820	    discrimination_rho_prompt_targeting: 0.15
821	    holdout_panel_equating_rho: 0.95
822	    construct_validity_factor_loading_corr: 0.85
823	    subject_match_accuracy: 0.92
824	    cognitive_level_match_accuracy: 0.78
825	    item_format_compliance: 0.97
826	  result_rationale: 'Student simulation校准（基于arXiv 2601.09953方法）的核心优势是empirical—— 它通过让diverse
827	    student models实际回答generated items来estimate difficulty， 而非依赖LLM的self-report。rho=0.78与原论文报告的r=0.75-0.82一致，因为MMLU
828	    的MCQ format与student simulation的optimal use case对齐（forced-choice items 比open-ended
829	    items更适合binary response modeling）。Prompt-based targeting 的rho=0.28与arXiv 2602.06631报告的rho=0.10-0.45一致——LLMs在内省difficulty
830	    时系统性地低估hard items、高估easy items，因为difficulty perception与generation capability不同。Student
831	    simulation的优势在于它bypasses这种miscalibration， 直接从behavioral responses estimate difficulty。Discrimination的rho=0.62较低
832	    于difficulty的0.78，因为discrimination是IRT的second-order parameter（item sensitivity
833	    to ability differences），inherently harder to control through generation——它依赖item的specific
834	    cognitive demands，而这些难以通过prompt engineering精确控制。Construct validity factor loading
835	    correlation=0.85表明 generated items load on相同的subject-specific factors，preserving
836	    MMLU的 bifactor structure。
837	
838	    '
839	  tables:
840	  - title: 'Table 13: Calibration Method Comparison'
841	    columns:
842	    - method
843	    - difficulty_rho
844	    - difficulty_rmse
845	    - discrimination_rho
846	    - n_items
847	    rows:
848	    - - Student_simulation
849	      - 0.78
850	      - 0.14
851	      - 0.62
852	      - 420
853	    - - Prompt_targeting
854	      - 0.28
855	      - 0.38
856	      - 0.15
857	      - 420
858	    - - Random_baseline
859	      - 0.05
860	      - 0.52
861	      - 0.03
862	      - 420
863	  - title: 'Table 14: Generated Item Quality Metrics'
864	    columns:
865	    - metric
866	    - value
867	    rows:
868	    - - Quality_filter_pass_rate
869	      - 0.84
870	    - - Subject_match_accuracy
871	      - 0.92
872	    - - Cognitive_level_match
873	      - 0.78
874	    - - Format_compliance
875	      - 0.97
876	    - - Factor_loading_corr
877	      - 0.85
878	    - - Holdout_equating_rho
879	      - 0.95
880	  figures_description:
881	  - 'Figure 19: Scatter plot of estimated vs true difficulty for student simulation
882	    (rho=0.78) and prompt targeting (rho=0.28). Student simulation points cluster
883	    near diagonal; prompt targeting shows systematic bias.'
884	  - 'Figure 20: Factor loading comparison between original and generated items on
885	    same MMLU subjects. High correspondence (r=0.85) confirms construct preservation.'
886	  analysis: 'Student simulation校准是item regeneration pipeline的关键enabler，将difficulty
887	    estimation精度从prompt-based的rho=0.28提升到0.78——接近3x improvement。 这一结果支持Claim 3的"empirically
888	    calibrated alternatives"承诺。Holdout panel equating rho=0.95达到psychometric standard，证明end-to-end
889	    pipeline（generation → simulation calibration → equating）可以produce functionally
890	    equivalent benchmark items。
891	
892	    '
893	- name: cumulative_bayesian_dif
894	  plan_id: plan_007
895	  description: '实现Bayesian累积DIF先验。模拟4次连续benchmark administration， 展示evidence accumulation带来的power提升。
896	
897	    '
898	  expected_results:
899	    n_administrations_simulated: 4
900	    n_models_per_administration: 40
901	    admin_1_power_medium_delta_1_0: 0.38
902	    admin_2_cumulative_power: 0.55
903	    admin_3_cumulative_power: 0.7
904	    admin_4_cumulative_power: 0.78
905	    power_gain_per_administration:
906	    - 0.38
907	    - 0.17
908	    - 0.15
909	    - 0.08
910	    bayesian_bf_threshold: 3.0
911	    false_discovery_rate: 0.04
912	    convergence_rate: 0.98
913	    prior_posterior_shrinkage: 0.42
914	    credible_interval_width_admin1: 0.68
915	    credible_interval_width_admin4: 0.31
916	  result_rationale: 'Bayesian累积先验的power gain来自evidence accumulation的数学性质——每次新的 administration提供independent
917	    observations，posterior distribution随data收窄。 从single administration的0.38到4次累积的0.78，power
918	    nearly doubles。Gain是 diminishing的（0.17→0.15→0.08），因为posterior precision的improvement是
919	    sub-linear in sample size（~√n scaling）。对medium effects（δ=1.0）这尤其重要， 因为classical
920	    DIF在single administration with N=40 per cohort时power不足 （Phase 2模拟显示N=50/δ=1.0时TPR仅0.04-0.07）。Bayesian
921	    approach通过 accumulating evidence across time解决了这个sample-size limitation——每次 administration贡献40个models，4次累积相当于effective
922	    sample of ~160， 但通过informative priors获得比simple pooling更高的statistical efficiency。
923	    BF threshold=3.0（moderate evidence）对应psychometric practice中的standard decision
924	    criterion。FDR=0.04 < 0.05表明error control有效。
925	
926	    '
927	  tables:
928	  - title: 'Table 15: Cumulative Bayesian DIF Power Over Administrations'
929	    columns:
930	    - administration
931	    - cumulative_n
932	    - power_delta_1_0
933	    - power_delta_1_4
934	    - CI_width
935	    rows:
936	    - - 1
937	      - 40
938	      - 0.38
939	      - 0.62
940	      - 0.68
941	    - - 2
942	      - 80
943	      - 0.55
944	      - 0.76
945	      - 0.48
946	    - - 3
947	      - 120
948	      - 0.7
949	      - 0.84
950	      - 0.37
951	    - - 4
952	      - 160
953	      - 0.78
954	      - 0.88
955	      - 0.31
956	  figures_description:
957	  - 'Figure 21: Power accumulation curves across 4 administrations for δ=0.6, 1.0,
958	    1.4. All show diminishing returns but substantial gains.'
959	  - 'Figure 22: Posterior distribution evolution for a representative DIF-flagged
960	    item across 4 administrations, showing progressive shrinkage toward true effect.'
961	  analysis: 'Bayesian累积DIF直接回应reviewer concern #2（sample sizes too small）。 4次累积后medium-effect
962	    power从0.38→0.78，使DIF对medium effects也实用化。 这一结果支持论文的"living benchmark"叙事——不需要一次性获得大样本，
963	    可以通过temporal accumulation逐步建立detection confidence。
964	
965	    '
966	- name: graceful_degradation_analysis
967	  plan_id: plan_008
968	  description: '分析benchmark在progressive item replacement下的validity degradation。 定义validity
969	    metrics，模拟5%-50% replacement，建立理论bounds。
970	
971	    '
972	  expected_results:
973	    replacement_rates:
974	    - 0.05
975	    - 0.1
976	    - 0.2
977	    - 0.5
978	    ranking_stability_rho_5pct: 0.99
979	    ranking_stability_rho_10pct: 0.97
980	    ranking_stability_rho_20pct: 0.95
981	    ranking_stability_rho_50pct: 0.89
982	    score_reliability_alpha_original: 0.94
983	    score_reliability_alpha_5pct: 0.93
984	    score_reliability_alpha_10pct: 0.93
985	    score_reliability_alpha_20pct: 0.91
986	    score_reliability_alpha_50pct: 0.87
987	    construct_coverage_jaccard_5pct: 0.98
988	    construct_coverage_jaccard_10pct: 0.96
989	    construct_coverage_jaccard_20pct: 0.92
990	    construct_coverage_jaccard_50pct: 0.83
991	    theoretical_rho_lower_bound_formula: rho >= 1 - k*replacement_rate*(1-r_replacement)
992	    theoretical_rho_lower_bound_20pct: 0.93
993	    empirical_rho_20pct: 0.95
994	    validity_threshold_replacement_rate: 0.35
995	  result_rationale: 'Graceful degradation的数学基础是：如果replacement items与original items测量相同
996	    construct（通过bifactor equating保证），且parameter estimation是unbiased的， 那么benchmark
997	    score的perturbation仅来自estimation error。Ranking stability (Spearman rho)随replacement
998	    rate的下降是approximately linear的：5%→0.99, 10%→0.97, 20%→0.95, 50%→0.89。0.95 threshold（psychometric
999	    standard for "essentially equivalent"）在~20% replacement rate时hit——这意味着可以替换 最多20%的items（~2500
1000	    items on MMLU）while maintaining psychometrically equivalent rankings。50% replacement导致rho=0.89，仍然usable但not
1001	    equivalent。 Score reliability (Cronbach''s alpha)从0.94降至0.91 at 20%，因为replacement
1002	    items的discrimination estimates有更大variance（calibration uncertainty）， but alpha>0.90在psychometric
1003	    standards中仍属excellent。Construct coverage (Jaccard similarity of subject factor
1004	    coverage)在20%时为0.92，因为replacement item generation已constrained to same subject，但minor
1005	    gaps in specific cognitive sub-skills可能出现。Theoretical lower bound formula provides
1006	    conservative estimate，empirical results consistently exceed it（0.95 > 0.93 at
1007	    20%），validating the bound''s correctness。
1008	
1009	    '
1010	  tables:
1011	  - title: 'Table 16: Validity Metrics Under Progressive Replacement'
1012	    columns:
1013	    - replacement_rate
1014	    - ranking_rho
1015	    - reliability_alpha
1016	    - construct_jaccard
1017	    - score_rmse
1018	    rows:
1019	    - - 0.0
1020	      - 1.0
1021	      - 0.94
1022	      - 1.0
1023	      - 0.0
1024	    - - 0.05
1025	      - 0.99
1026	      - 0.93
1027	      - 0.98
1028	      - 0.008
1029	    - - 0.1
1030	      - 0.97
1031	      - 0.93
1032	      - 0.96
1033	      - 0.015
1034	    - - 0.2
1035	      - 0.95
1036	      - 0.91
1037	      - 0.92
1038	      - 0.025
1039	    - - 0.35
1040	      - 0.92
1041	      - 0.89
1042	      - 0.87
1043	      - 0.038
1044	    - - 0.5
1045	      - 0.89
1046	      - 0.87
1047	      - 0.83
1048	      - 0.052
1049	  - title: 'Table 17: Theoretical vs Empirical Bounds'
1050	    columns:
1051	    - replacement_rate
1052	    - theoretical_rho_lb
1053	    - empirical_rho
1054	    - bound_tight
1055	    rows:
1056	    - - 0.05
1057	      - 0.97
1058	      - 0.99
1059	      - false
1060	    - - 0.1
1061	      - 0.95
1062	      - 0.97
1063	      - false
1064	    - - 0.2
1065	      - 0.93
1066	      - 0.95
1067	      - false
1068	    - - 0.5
1069	      - 0.84
1070	      - 0.89
1071	      - false
1072	  figures_description:
1073	  - 'Figure 23: Validity degradation curves (rho, alpha, Jaccard) vs replacement rate,
1074	    with 0.95 threshold line marking ''psychometrically equivalent'' zone.'
1075	  - 'Figure 24: Theoretical lower bound vs empirical results, showing bound is conservative
1076	    but informative.'
1077	  analysis: 'Graceful degradation分析为benchmark regeneration建立了formal safety guarantees。
1078	    20% replacement threshold（rho≥0.95）为实际操作提供了clear guideline—— given MMLU上约10.7%
1079	    items被DIF flagged（plan_001），单轮replacement在安全范围内。 理论bound的conservativeness（empirical
1080	    consistently exceeds theoretical by 2-5pp） 提供额外safety margin。这一结果完成了Claim 3从detection
1081	    → generation → equating → validity guarantee的完整pipeline。
1082	
1083	    '
1084	- name: item_focused_trees
1085	  plan_id: plan_009
1086	  description: '实现Item-Focused Trees作为categorical cohort DIF的替代方案。 将model release
1087	    date作为continuous covariate，比较检测力和灵活性。
1088	
1089	    '
1090	  expected_results:
1091	    ift_tpr_delta_ge_1_4: 0.81
1092	    ift_tpr_delta_ge_1_0: 0.58
1093	    ift_fpr: 0.044
1094	    ift_auc: 0.9
1095	    ift_vs_ets_c_tpr_improvement: 0.03
1096	    ift_vs_ets_c_auc_improvement: -0.02
1097	    ift_detected_gradual_contamination: true
1098	    n_items_with_changepoint: 890
1099	    median_changepoint_date: 2023-06
1100	    changepoint_clustering_by_subject: true
1101	    ift_computation_time_seconds: 340
1102	    ets_c_computation_time_seconds: 28
1103	  result_rationale: 'Item-Focused Trees的优势在于不需要arbitrary cohort splits——它自动发现每个item
1104	    的contamination onset point（changepoint）作为tree split。TPR=0.81略优于 ETS C的0.78（+3pp），因为IFT可以为每个item找到optimal
1105	    focal/reference split 而非使用统一的pre/post cutoff。但AUC=0.90略低于ETS C的0.92，因为IFT在small
1106	    effects区间的precision较低（tree splitting在low-signal regime容易overfit）。 Changepoint
1107	    clustering by subject是重要的secondary finding——STEM subjects的 median changepoint早于humanities（2023-03
1108	    vs 2023-09），反映code-heavy training data对STEM contamination的earlier onset。890个items有detectable
1109	    changepoints， 与plan_001的1340 flagged items部分重叠（IFT的threshold更conservative因为tree
1110	    pruning）。计算成本是ETS C的12x，因为recursive partitioning需要对每个item 搜索所有可能splits，但仍在minutes级别（CPU
1111	    only），实际可用。IFT的主要paper value 是methodological：它证明contamination timing是item-specific而非cohort-uniform，
1112	    支持"contamination as gradual process"的narrative。
1113	
1114	    '
1115	  tables:
1116	  - title: 'Table 18: Item-Focused Trees vs ETS C Comparison'
1117	    columns:
1118	    - method
1119	    - tpr_ge_1_4
1120	    - tpr_ge_1_0
1121	    - fpr
1122	    - auc
1123	    - time_sec
1124	    rows:
1125	    - - ETS_C
1126	      - 0.78
1127	      - 0.45
1128	      - 0.038
1129	      - 0.92
1130	      - 28
1131	    - - Item_Focused_Trees
1132	      - 0.81
1133	      - 0.58
1134	      - 0.044
1135	      - 0.9
1136	      - 340
1137	    - - Combined
1138	      - 0.84
1139	      - 0.6
1140	      - 0.048
1141	      - 0.93
1142	      - 368
1143	  - title: 'Table 19: Contamination Changepoint Analysis'
1144	    columns:
1145	    - subject_group
1146	    - n_items_with_changepoint
1147	    - median_changepoint
1148	    - range
1149	    rows:
1150	    - - STEM
1151	      - 520
1152	      - 2023-03
1153	      - 2022-06 to 2024-01
1154	    - - Humanities
1155	      - 210
1156	      - 2023-09
1157	      - 2023-01 to 2024-06
1158	    - - Social_Sciences
1159	      - 160
1160	      - 2023-06
1161	      - 2022-09 to 2024-03
1162	  figures_description:
1163	  - 'Figure 25: Item-level changepoint distribution across calendar time, colored
1164	    by subject. STEM items show earlier contamination onset.'
1165	  - 'Figure 26: Example Item-Focused Tree for a specific MMLU item, showing splits
1166	    on release date and model family.'
1167	  analysis: IFT作为P2实验提供了methodological depth——contamination timing的item-specific 和subject-specific
1168	    patterns是novel finding，支持论文的temporal dynamics narrative。 Detection power的marginal
1169	    improvement（+3pp TPR）不足以替代ETS C作为primary method，但combined approach（union of flags）将TPR推到0.84。更重要的是IFT的
1170	    changepoint analysis为understanding contamination dynamics提供了unique evidence， 可作为analysis
1171	    section的secondary contribution。
1172	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ffcdbcf-df38-412c-b7c6-7a70cfc40b90",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "e46a2add-69da-48ea-8410-6d6a87a7d37b",
  "sourceToolAssistantUUID": "2ffcdbcf-df38-412c-b7c6-7a70cfc40b90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-20T20:18:24.450Z_

Now let me also check the paper summary numbers against the "median" and "worst" tiers to understand the variance, and read the memory file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e46a2add-69da-48ea-8410-6d6a87a7d37b",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESPyAxhKxZEf2y2KwTp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4961625f-cf7d-4eba-8046-5289c7d613ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ns5wjYRoP3CtV8uXwc68WB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37932,
      "cache_read_input_tokens": 33775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37932,
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

_source line 33 · 2026-05-20T20:18:25.463Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AeYoooRXKBmrfhUv1RTkMz`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4961625f-cf7d-4eba-8046-5289c7d613ce",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESPyAxhKxZEf2y2KwTp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cce7943e-7cce-4231-903b-1fea1056130a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ns5wjYRoP3CtV8uXwc68WB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37932,
      "cache_read_input_tokens": 33775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37932,
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

_source line 34 · 2026-05-20T20:18:25.476Z_

<details><summary>↩ Tool result · `toolu_01AeYoooRXKBmrfhUv1RTkMz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/memory.md\", \"content\": \"## MVP 验证关键经验 (2026-05-20)\\n\\n### D001 决策：ETS C 分类 > p-value 检验\\n- **p-value based DIF 检测在 200-item benchmark 上严重 underpowered**：BH 校正后 TPR 仅 0.04-0.07（N=50, δ=1.0）。即使 raw（不校正）TPR 也只有 0.36-0.39，远低于 0.70 目标\\n- **ETS C 分类（|Δ_MH|≥1.5 + 显著性）是可行的替代**：TPR=0.68-0.85 at N≥80, δ≥1.4。本质是 magnitude-based detection，绕过了多重检验问题\\n- **AUC 一直很好（0.91-0.96）**：说明 DIF 统计量的区分能力没问题，问题在假设检验的 threshold，不在信号本身\\n- **原因**：200 个 items 做 BH 校正，需要极小的 p-value 才能过。N=50-100 per group 对 MH/LR 的 per-item 统计功效不够产生 p<0.001 级别的 evidence\\n\\n### Phase 2 验证：真实参数稳健\\n- **PSN-IRT 真实 MMLU 参数** vs 合成参数差异显著：b_mean=-0.84（真实）vs 0.0（合成），即真实 MMLU items 偏容易\\n- 尽管参数分布差异大，ETS C TPR 在真实参数下反而更高（N=100, δ=1.6: 0.80 vs Phase 1 的 0.85）——差异不大，结论稳健\\n- **Phase 2 用了 PSN-IRT 而非 METABENCH**：PSN-IRT 的 item_parameters.csv 可直接使用（14042 items），无需下载 620MB 大包\\n\\n### 关键操作参数\\n- N≥80/group 是最低要求，N≥100 显著改善功效\\n- δ≥1.4 logits 是可靠检测区间，δ=1.0 在边界\\n- MH 5 层 quantile-based 分层 + ETS C 阈值是当前最佳组合\\n- LR 方法与 MH 表现相当，无显著优势\\n\\n## Phase 2 数据源调研 (2026-05-20)\\n\\n### PSN-IRT (AAAI 2026)\\n\\n- **论文全名**: \\\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\\\"\\n- **作者**: Joe-Hall-Lee et al.\\n- **发表**: AAAI 2026 Oral\\n- **GitHub**: https://github.com/Joe-Hall-Lee/PSN-IRT\\n- **IRT 参数公开**: ✅ 是\\n  - `results/item_parameters.csv`: 全部 41,871 items 的 4PL 参数 (a=discrimination, b=difficulty, c=guessing, d=feasibility)\\n  - `results/student_abilities.csv`: 12 个模型的 latent abilities (θ)\\n  - `data/combine.csv`: 12 LLMs × 11 benchmarks 的 binary response matrix\\n- **MMLU 覆盖**: 14,042 items（MMLU 全集）\\n- **模型数**: 仅 12 个\\n- **局限**: 12 个模型太少，IRT 参数估计的可靠性存疑（经典 IRT 通常需要 ≥200 考生）\\n\\n### METABENCH (Kipnis et al., ICLR 2025) ⭐ 推荐\\n\\n- **论文全名**: \\\"metabench — A Sparse Benchmark of Reasoning and Knowledge in Large Language Models\\\"\\n- **GitHub**: https://github.com/adkipnis/metabench\\n- **Zenodo 数据**: https://zenodo.org/records/12819251 (`data.tgz`, 620MB)\\n- **MMLU 覆盖**: 12,508 items\\n- **模型数**: 5,219 个模型（RDS 预处理后）\\n- **优势**: 模型数量充足（5000+），IRT 估计可靠\\n\\n### 数据规模对比\\n\\n| 数据源 | 模型数 | MMLU items | IRT 参数 | 获取难度 |\\n|--------|--------|------------|----------|----------|\\n| **METABENCH** | 5,219 | 12,508 | 2PL (预拟合) | ⭐ 低 |\\n| **PSN-IRT** | 12 | 14,042 | 4PL (PSN) | ⭐ 低 |\\n| **Open LLM LB v1** | ~数千 | ~14,042 | 无 | 中 |\\n\\n## METABENCH 数据探索关键发现 (2026-05-20)\\n\\n### RDS 预拟合 IRT 参数\\n- `mmlu-preproc.rds` 包含 **12,508 items 的 2PL IRT 参数** (difficulty, discrimination)\\n- Difficulty range: [0.008, 0.689], mean=0.444; Discrimination range: [-0.551, 0.291], mean=0.076\\n- 1,926 items (15.4%) 有负区分度\\n- 258 floor items (p<0.05), 0 ceiling items (p>0.95)\\n- **可直接使用，无需自行拟合 IRT**\\n\\n### 响应矩阵 & Train/Test Split\\n- 完整 5219×12508 响应矩阵在 RDS 中\\n- 预建 train/test split: 4,755 train / 464 test models\\n\\n### Cohort 可行性\\n- 通过模型名正则分类：仅 1,929/5,219 (37%) 可归类到已知 family\\n- **2 个年度 cohort 满足 N≥80**: 2023 (N=1,253), 2024 (N=658)\\n- 63% 模型无法从名称分类（社区微调/合并模型）\\n- **结论**: 粗粒度 2-cohort (2023 vs 2024) 可行；细粒度年度 cohort 需外部元数据\\n\\n### RL-trained 模型\\n- **477 个模型**名称含 RL/alignment 信号: DPO(346), ORPO(52), PPO(11), KTO(6)\\n- 大量隐式 RLHF 模型（Llama-3, Qwen-2 等）名称不含标记\\n- **结论**: RL 模型充足，可用于污染检测 validation\\n\\n### 模型准确率分布\\n- Mean=0.592, Std=0.160, Range=[0.218, 0.911]\\n- 366 (7%) 模型低于随机水平 (0.25)\\n- Top families: mistral-0.1 (400), llama-3 (308), llama-2 (161)\\n\\n### CSV vs RDS 差异\\n- CSV: 5,227 模型; RDS: 5,219 模型（8 个被预处理过滤）\\n- 每个 subject 的模型数在 5,225-5,227 之间（近完整覆盖）\\n\", \"total_chars\": 3288, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cce7943e-7cce-4231-903b-1fea1056130a",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "0a80b4ed-cbfe-4450-b610-64cee63a4fd3",
  "sourceToolAssistantUUID": "cce7943e-7cce-4231-903b-1fea1056130a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T20:18:27.819Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NysTUmVT6GSk5EFKsxAzui`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/imagined_experiments.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a80b4ed-cbfe-4450-b610-64cee63a4fd3",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESPyAxhKxZEf2y2KwTp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a125a1a1-d64f-46af-9bcb-b306c1415be3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ns5wjYRoP3CtV8uXwc68WB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37932,
      "cache_read_input_tokens": 33775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37932,
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

_source line 36 · 2026-05-20T20:18:27.826Z_

<details><summary>↩ Tool result · `toolu_01NysTUmVT6GSk5EFKsxAzui`</summary>

```text
1	tier: median
2	narrative_guidance: 'Claim 1 调整为 "DIF provides a complementary contamination signal
3	  with unique RL-robustness properties"， 强调程度差异而非 binary 生存。Claim 2 从三信号降级为双信号 + DVD
4	  failure mode analysis。 Claim 3 限定为 within-subject equating pilot，讨论 acceptable degradation
5	  bounds。 核心叙事从 "self-healing benchmark" 转向 "psychometric monitoring framework with
6	  contamination-aware recalibration"。 需补充 2-3 个 ablation 实验填补 reviewer 攻击面。仍投 ICLR，但
7	  related work 和 limitation 需加厚。
8	
9	  '
10	imagined_experiments:
11	- name: real_data_dif_mmlu
12	  plan_id: plan_001
13	  description: '在 METABENCH MMLU 响应矩阵（5,055 models × 12,508 items）上执行 DIF 分析。 按 release
14	    date 划分 temporal cohorts（pre-2024 vs post-2024，以及更细的年度分割）。 对所有 items 运行 ETS C
15	    DIF 检测，以 MMLU-CF 为部分 ground truth 做交叉验证。
16	
17	    '
18	  expected_results:
19	    n_models_after_quality_filter: 4312
20	    n_items_analyzable: 11847
21	    cohort_pre2024_size: 2876
22	    cohort_post2024_size: 1436
23	    n_items_flagged_ets_c: 743
24	    pct_items_flagged: 0.0627
25	    dif_tpr_delta_ge_1.4_vs_mmlu_cf: 0.58
26	    dif_tpr_delta_ge_1.0: 0.41
27	    dif_fpr_clean_items: 0.062
28	    mmlu_cf_correlation_spearman: 0.21
29	    mmlu_cf_correlation_p_value: 0.003
30	    n_items_delta_ge_1.4_estimated: 187
31	    n_items_delta_1.0_to_1.4_estimated: 412
32	    n_items_delta_lt_1.0_estimated: 144
33	    ets_c_auc_vs_mmlu_cf_binary: 0.71
34	    sensitivity_cohort_split_annual_tpr_range: 0.52-0.63
35	    sensitivity_threshold_sweep_tpr_range: 0.44-0.67
36	  result_rationale: 'Simulation 在 N=100, δ=1.4 下得到 TPR=0.758，但真实数据有三个系统性降级因素： (1)
37	    真实 contamination effect sizes 不是均匀的 δ=1.4，多数 flagged items 落在 δ=1.0-1.4 的中间地带，
38	    拉低了 aggregate TPR；(2) METABENCH 数据的 model heterogeneity（不同架构、不同 training recipe）
39	    引入 DIF 分析假设之外的 noise，使得 IRT ability estimation 精度下降； (3) contamination 不是 binary
40	    uniform 的——部分 models 只接触了 partial benchmark subsets， 创造了 fuzzy group boundaries
41	    而非 simulation 中的 clean reference/focal split。 MMLU-CF correlation 为正但弱（ρ=0.21），因为
42	    MMLU-CF 的 modification 并非针对 DIF 设计—— 它改变了 item 内容以消除记忆优势，但有些 modification 也改变了
43	    difficulty， 引入了 false negatives（item 有 DIF 但 CF 版本 too different to count as same
44	    construct）。 FPR 从 simulation 的 0.036-0.042 升至 0.062，因为 real data 中存在 non-contamination
45	    来源的 DIF（如 certain model families 对特定 domain 有 architecture-driven advantages）。
46	    δ≥1.4 的 items 仅占 flagged items 的约 25%，大部分 contamination signal 在 medium effect
47	    区间。
48	
49	    '
50	  tables:
51	  - name: 'Table 1: DIF Detection Performance on MMLU by Effect Size Band'
52	    columns:
53	    - effect_size_band
54	    - n_items_estimated
55	    - ets_c_tpr
56	    - ets_c_fpr
57	    - mh_tpr
58	    - lr_tpr
59	    rows:
60	    - - δ ≥ 1.6
61	      - 68
62	      - 0.69
63	      - 0.058
64	      - 0.54
65	      - 0.61
66	    - - δ ∈ [1.4, 1.6)
67	      - 119
68	      - 0.52
69	      - 0.065
70	      - 0.38
71	      - 0.44
72	    - - δ ∈ [1.0, 1.4)
73	      - 412
74	      - 0.41
75	      - 0.063
76	      - 0.27
77	      - 0.33
78	    - - δ ∈ [0.6, 1.0)
79	      - 144
80	      - 0.18
81	      - 0.061
82	      - 0.11
83	      - 0.14
84	    - - Clean (no contamination evidence)
85	      - ~10400
86	      - —
87	      - 0.062
88	      - —
89	      - —
90	  - name: 'Table 2: Sensitivity to Cohort Definition'
91	    columns:
92	    - cohort_split
93	    - focal_n
94	    - reference_n
95	    - tpr_delta_ge_1.4
96	    - fpr
97	    - n_flagged
98	    rows:
99	    - - pre-2024 vs post-2024
100	      - 1436
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a125a1a1-d64f-46af-9bcb-b306c1415be3",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "83679f5a-0abd-405c-9c0a-b03630475dfb",
  "sourceToolAssistantUUID": "a125a1a1-d64f-46af-9bcb-b306c1415be3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T20:18:28.298Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JBAWmFi4ZkvXV6WQLbGPAm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/worst/imagined_experiments.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83679f5a-0abd-405c-9c0a-b03630475dfb",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESPyAxhKxZEf2y2KwTp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d13f7d4f-2e69-4267-b3c2-597c1b04e6a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ns5wjYRoP3CtV8uXwc68WB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37932,
      "cache_read_input_tokens": 33775,
      "output_tokens": 359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 37932
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 359,
          "cache_read_input_tokens": 33775,
          "cache_creation_input_tokens": 37932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 37932,
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

_source line 38 · 2026-05-20T20:18:28.305Z_

<details><summary>↩ Tool result · `toolu_01JBAWmFi4ZkvXV6WQLbGPAm`</summary>

```text
1	tier: worst
2	narrative_guidance: '核心"DIF是RL-robust contamination signal"假设不成立。5000+异构模型的response
3	  matrix严重违反IRT unidimensionality假设，architecture差异（encoder-only vs decoder-only vs
4	  MoE）制造了大量 spurious DIF，FPR膨胀至实用边界之外。真实contamination以partial memorization为主， ICC
5	  shift不足以在高噪声背景下被检出。RL-robustness优势不显著——传统方法在RL下虽然退化， 但DIF也退化，差距不足以支撑"orthogonal
6	  signal"叙事。需要pivot到negative-result framing 或剥离Claim 3做独立贡献。
7	
8	  '
9	imagined_experiments:
10	- name: real_data_dif_mmlu
11	  plan_id: plan_001
12	  description: '对METABENCH MMLU response matrix (5,055 models × 12,508 items)执行temporal
13	    cohort DIF分析， 以MMLU-CF为partial ground truth验证。
14	
15	    '
16	  expected_results:
17	    dif_tpr_delta_ge_1.4: 0.38
18	    dif_tpr_delta_ge_1.0: 0.18
19	    dif_fpr: 0.12
20	    mmlu_cf_correlation_with_dif_flags_phi: 0.09
21	    mmlu_cf_correlation_with_dif_flags_spearman: 0.07
22	    irt_model_fit_rmsea: 0.11
23	    irt_model_fit_cfi: 0.78
24	    n_items_flagged_ets_c: 1840
25	    n_items_flagged_ets_c_after_fpr_correction: 620
26	    cohort_size_pre2024: 1850
27	    cohort_size_post2024: 3205
28	    unidimensionality_test_p: 0.001
29	    item_discrimination_variance: 2.8
30	  result_rationale: '5055个模型跨越encoder-only (BERT-family)、decoder-only (GPT/LLaMA family)、MoE等根本不同
31	    的architecture，对MMLU items的response pattern受architecture驱动而非ability驱动。例如 decoder-only模型在long-context
32	    reasoning items上系统性优于encoder-only模型，这与contamination 无关但产生大量DIF。RMSEA=0.11远超可接受阈值(0.06)，CFI=0.78低于0.90标准，表明unidimensional
33	    IRT model严重misfit。在此背景下ETS C的effect-size threshold无法区分architecture-driven DIF
34	    和contamination-driven DIF，导致FPR膨胀至0.12。1840个items被flagged（15%的item pool）， 其中大部分是false
35	    positives。与MMLU-CF的correlation仅phi=0.09，接近random——因为MMLU-CF 本身的contamination annotation也有噪声（它只标注了"显著修改"的items，但并未验证原始items
36	    确实被contaminated），加上DIF flags被spurious signal淹没，两个noisy signal之间几乎无相关。
37	
38	    '
39	  tables:
40	  - title: 'Table 1: DIF Detection Performance on METABENCH MMLU (Worst Tier)'
41	    columns:
42	    - metric
43	    - pre2024_vs_post2024
44	    - annual_cohorts
45	    - sliding_window_6mo
46	    rows:
47	    - - TPR_delta_ge_1.4
48	      - 0.38
49	      - 0.31
50	      - 0.28
51	    - - TPR_delta_ge_1.0
52	      - 0.18
53	      - 0.14
54	      - 0.12
55	    - - FPR
56	      - 0.12
57	      - 0.14
58	      - 0.15
59	    - - F1_delta_ge_1.4
60	      - 0.33
61	      - 0.28
62	      - 0.25
63	    - - N_flagged_items
64	      - 1840
65	      - 2100
66	      - 2350
67	    - - MMLU-CF_phi_correlation
68	      - 0.09
69	      - 0.07
70	      - 0.06
71	  - title: 'Table 2: IRT Model Fit Diagnostics'
72	    columns:
73	    - fit_index
74	    - value
75	    - acceptable_threshold
76	    - verdict
77	    rows:
78	    - - RMSEA
79	      - 0.11
80	      - ≤0.06
81	      - FAIL
82	    - - CFI
83	      - 0.78
84	      - ≥0.90
85	      - FAIL
86	    - - TLI
87	      - 0.74
88	      - ≥0.90
89	      - FAIL
90	    - - SRMR
91	      - 0.09
92	      - ≤0.08
93	      - FAIL
94	    - - M2_p_value
95	      - <0.001
96	      - '>0.05'
97	      - FAIL
98	  figures_description:
99	  - 'Fig 1: ICC overlay of 20 highest-DIF items — curves show chaotic crossing patterns
100	    rather than clean uniform/non-uniform DIF, suggesting architecture heterogeneity
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d13f7d4f-2e69-4267-b3c2-597c1b04e6a1",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "72644a5e-0fd9-4669-9c15-7c0b696be38f",
  "sourceToolAssistantUUID": "d13f7d4f-2e69-4267-b3c2-597c1b04e6a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T20:18:32.149Z_

Now let me read the median-tier experiments more fully and the paper framing from median.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72644a5e-0fd9-4669-9c15-7c0b696be38f",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESQZpJG9EWjEw6nCfk7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b79178d7-94c7-4a30-a209-abbc35227a5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013H9Yji95VxTUQ4ZafiW8Jo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6041,
      "cache_read_input_tokens": 71707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6041,
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

_source line 40 · 2026-05-20T20:18:34.666Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LokTwuK1VEcHm8HUuYe1K6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b79178d7-94c7-4a30-a209-abbc35227a5a",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESQZpJG9EWjEw6nCfk7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "524b2918-6da8-4cf3-b36c-c90b09470124",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013H9Yji95VxTUQ4ZafiW8Jo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6041,
      "cache_read_input_tokens": 71707,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6041
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 71707,
          "cache_creation_input_tokens": 6041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6041,
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

_source line 41 · 2026-05-20T20:18:34.930Z_

<details><summary>↩ Tool result · `toolu_01LokTwuK1VEcHm8HUuYe1K6`</summary>

```text
1	tier: median
2	narrative_guidance: 'Claim 1 调整为 "DIF provides a complementary contamination signal
3	  with unique RL-robustness properties"， 强调程度差异而非 binary 生存。Claim 2 从三信号降级为双信号 + DVD
4	  failure mode analysis。 Claim 3 限定为 within-subject equating pilot，讨论 acceptable degradation
5	  bounds。 核心叙事从 "self-healing benchmark" 转向 "psychometric monitoring framework with
6	  contamination-aware recalibration"。 需补充 2-3 个 ablation 实验填补 reviewer 攻击面。仍投 ICLR，但
7	  related work 和 limitation 需加厚。
8	
9	  '
10	imagined_experiments:
11	- name: real_data_dif_mmlu
12	  plan_id: plan_001
13	  description: '在 METABENCH MMLU 响应矩阵（5,055 models × 12,508 items）上执行 DIF 分析。 按 release
14	    date 划分 temporal cohorts（pre-2024 vs post-2024，以及更细的年度分割）。 对所有 items 运行 ETS C
15	    DIF 检测，以 MMLU-CF 为部分 ground truth 做交叉验证。
16	
17	    '
18	  expected_results:
19	    n_models_after_quality_filter: 4312
20	    n_items_analyzable: 11847
21	    cohort_pre2024_size: 2876
22	    cohort_post2024_size: 1436
23	    n_items_flagged_ets_c: 743
24	    pct_items_flagged: 0.0627
25	    dif_tpr_delta_ge_1.4_vs_mmlu_cf: 0.58
26	    dif_tpr_delta_ge_1.0: 0.41
27	    dif_fpr_clean_items: 0.062
28	    mmlu_cf_correlation_spearman: 0.21
29	    mmlu_cf_correlation_p_value: 0.003
30	    n_items_delta_ge_1.4_estimated: 187
31	    n_items_delta_1.0_to_1.4_estimated: 412
32	    n_items_delta_lt_1.0_estimated: 144
33	    ets_c_auc_vs_mmlu_cf_binary: 0.71
34	    sensitivity_cohort_split_annual_tpr_range: 0.52-0.63
35	    sensitivity_threshold_sweep_tpr_range: 0.44-0.67
36	  result_rationale: 'Simulation 在 N=100, δ=1.4 下得到 TPR=0.758，但真实数据有三个系统性降级因素： (1)
37	    真实 contamination effect sizes 不是均匀的 δ=1.4，多数 flagged items 落在 δ=1.0-1.4 的中间地带，
38	    拉低了 aggregate TPR；(2) METABENCH 数据的 model heterogeneity（不同架构、不同 training recipe）
39	    引入 DIF 分析假设之外的 noise，使得 IRT ability estimation 精度下降； (3) contamination 不是 binary
40	    uniform 的——部分 models 只接触了 partial benchmark subsets， 创造了 fuzzy group boundaries
41	    而非 simulation 中的 clean reference/focal split。 MMLU-CF correlation 为正但弱（ρ=0.21），因为
42	    MMLU-CF 的 modification 并非针对 DIF 设计—— 它改变了 item 内容以消除记忆优势，但有些 modification 也改变了
43	    difficulty， 引入了 false negatives（item 有 DIF 但 CF 版本 too different to count as same
44	    construct）。 FPR 从 simulation 的 0.036-0.042 升至 0.062，因为 real data 中存在 non-contamination
45	    来源的 DIF（如 certain model families 对特定 domain 有 architecture-driven advantages）。
46	    δ≥1.4 的 items 仅占 flagged items 的约 25%，大部分 contamination signal 在 medium effect
47	    区间。
48	
49	    '
50	  tables:
51	  - name: 'Table 1: DIF Detection Performance on MMLU by Effect Size Band'
52	    columns:
53	    - effect_size_band
54	    - n_items_estimated
55	    - ets_c_tpr
56	    - ets_c_fpr
57	    - mh_tpr
58	    - lr_tpr
59	    rows:
60	    - - δ ≥ 1.6
61	      - 68
62	      - 0.69
63	      - 0.058
64	      - 0.54
65	      - 0.61
66	    - - δ ∈ [1.4, 1.6)
67	      - 119
68	      - 0.52
69	      - 0.065
70	      - 0.38
71	      - 0.44
72	    - - δ ∈ [1.0, 1.4)
73	      - 412
74	      - 0.41
75	      - 0.063
76	      - 0.27
77	      - 0.33
78	    - - δ ∈ [0.6, 1.0)
79	      - 144
80	      - 0.18
81	      - 0.061
82	      - 0.11
83	      - 0.14
84	    - - Clean (no contamination evidence)
85	      - ~10400
86	      - —
87	      - 0.062
88	      - —
89	      - —
90	  - name: 'Table 2: Sensitivity to Cohort Definition'
91	    columns:
92	    - cohort_split
93	    - focal_n
94	    - reference_n
95	    - tpr_delta_ge_1.4
96	    - fpr
97	    - n_flagged
98	    rows:
99	    - - pre-2024 vs post-2024
100	      - 1436
101	      - 2876
102	      - 0.58
103	      - 0.062
104	      - 743
105	    - - pre-2023 vs post-2023
106	      - 1891
107	      - 2421
108	      - 0.54
109	      - 0.071
110	      - 812
111	    - - Annual (2022 vs 2024+)
112	      - 987
113	      - 1436
114	      - 0.63
115	      - 0.057
116	      - 691
117	    - - Quarterly (Q1-Q2 2023 vs Q3-Q4 2024)
118	      - 623
119	      - 718
120	      - 0.52
121	      - 0.084
122	      - 658
123	  - name: 'Table 3: MMLU-CF Cross-Validation'
124	    columns:
125	    - metric
126	    - value
127	    - 95% CI
128	    rows:
129	    - - Spearman ρ (DIF effect size vs CF accuracy gap)
130	      - 0.21
131	      - '[0.09, 0.33]'
132	    - - Items flagged by both DIF and CF
133	      - 47
134	      - —
135	    - - Items flagged by DIF only
136	      - 696
137	      - —
138	    - - Items flagged by CF only
139	      - 83
140	      - —
141	    - - Cohen's κ (binary agreement)
142	      - 0.14
143	      - '[0.06, 0.22]'
144	  figures_description:
145	  - 'Figure 1: Scatter plot — DIF effect size (Δ_MH) vs MMLU-CF accuracy gap per item.
146	    Weak positive trend (ρ=0.21) with substantial scatter. Color-coded by MMLU subject.
147	    STEM items cluster slightly tighter; humanities items show more dispersion. Annotation:
148	    items with high DIF but low CF gap likely reflect contamination patterns CF modification
149	    did not capture (e.g., partial memorization of distractor patterns).'
150	  - 'Figure 2: Histogram of estimated DIF effect sizes across all 12,508 items. Distribution
151	    is right-skewed with long tail. Vertical lines at δ=0.6, 1.0, 1.4 thresholds.
152	    Bulk of items (89%) below δ=0.6. Of flagged items, majority in δ=1.0-1.4 band,
153	    not the δ≥1.4 band where DIF has strongest power.'
154	  - 'Figure 3: ROC curves for DIF detection using MMLU-CF as noisy ground truth. ETS
155	    C achieves AUC=0.71, MH AUC=0.64, LR AUC=0.68. Note: AUC is suppressed by ground
156	    truth noise (CF ≠ perfect contamination label).'
157	  analysis: '核心发现：DIF 在真实数据上有统计显著的 contamination 信号，但 power 比 simulation 低约 12-18pp。
158	    主要瓶颈是 real contamination effect sizes 分布——δ≥1.4 的 items 仅占约 25%， 而 DIF 在 δ<1.0
159	    区间的 power 不足以独立检测。 MMLU-CF 交叉验证提供了 directional support（p=0.003）但 agreement 较低（κ=0.14），
160	    这既反映 DIF 的 imperfect power，也反映 CF 本身作为 ground truth 的局限性。 Cohort split sensitivity
161	    分析显示：focal group 越小，FPR 升高（quarterly split 达 0.084）， 建议使用年度或更粗的 cohort 划分。 对 Claim
162	    1 的影响：TPR=0.58 低于 paper framing 中承诺的 0.72-0.85 range， 需要将 claim 调整为 "practical
163	    detection of large effects" 并明确 medium effect 的 coverage gap。 这个 gap 恰好为 ensemble（Claim
164	    2）提供了动机。
165	
166	    '
167	- name: rl_robustness_validation
168	  plan_id: plan_002
169	  description: '实证验证 DIF 的 RL-robustness。构建 SFT-only 和 SFT+RL 两种 cohort， 在两种场景下运行
170	    DIF 和传统 detectors，量化 RL 对各方法的影响。
171	
172	    '
173	  expected_results:
174	    n_rl_models_identified_in_metabench: 23
175	    n_rl_models_added_via_inference: 12
176	    total_rl_models: 35
177	    total_sft_only_models: 187
178	    dif_tpr_sft_cohort_delta_ge_1.4: 0.61
179	    dif_tpr_rl_cohort_delta_ge_1.4: 0.54
180	    dif_power_retention_ratio: 0.885
181	    mink_auroc_sft: 0.74
182	    mink_auroc_rl: 0.51
183	    mink_power_retention: 0.689
184	    constat_auroc_sft: 0.69
185	    constat_auroc_rl: 0.58
186	    constat_power_retention: 0.841
187	    dvd_auroc_sft: 0.62
188	    dvd_auroc_rl: 0.56
189	    dvd_power_retention: 0.903
190	    dif_vs_best_traditional_gap_under_rl: 0.08
191	    gpu_hours_used: 87
192	  result_rationale: 'DIF 的 power retention ratio (0.885) 高于传统方法平均值，但 gap 不如理论预期那么
193	    dramatic。 原因：(1) RL 训练确实平滑了 output distribution（Min-K% AUROC 从 0.74 降至 0.51， 与
194	    Wang et al. 的 14-20pp degradation 一致），但 DIF 也受到了轻微影响—— RL 不仅平滑 output，还改变了 response
195	    的 confidence calibration， 这通过 ability estimation 间接影响 DIF（IRT θ estimates 在 RL
196	    models 上 less stable）。 (2) 传统方法在 RL 下并未完全退化到 random：ConStat AUROC=0.58（不是 0.50），
197	    因为 perturbation sensitivity 虽然降低但未完全消失——RL 训练通常在 original format 上做 PPO， paraphrased
198	    items 仍能 trip up 部分 RL models。 DVD 在 RL 下 AUROC=0.56，看似 retention 高（0.903），但 baseline
199	    本身就低（0.62）， 说明 DVD 对这个 scenario 本身就不敏感而非 RL-robust。 最终 DIF vs best traditional
200	    的 gap（在 RL 下 DIF TPR=0.54 vs ConStat AUROC=0.58） 不是 "DIF 独活" 的故事，而是 "DIF 保持了 reasonable
201	    power 且是 RL-robustness 最好的之一"。 这要求将 narrative 从 "only survivor" 调整为 "most robust
202	    complement"。
203	
204	    '
205	  tables:
206	  - name: 'Table 4: Detection Power Under SFT vs RL Training'
207	    columns:
208	    - method
209	    - auroc_sft
210	    - auroc_rl
211	    - retention_ratio
212	    - Δ_auroc
213	    rows:
214	    - - DIF (ETS C)
215	      - 0.73
216	      - 0.68
217	      - 0.885
218	      - -0.05
219	    - - Min-K%
220	      - 0.74
221	      - 0.51
222	      - 0.689
223	      - -0.23
224	    - - Min-K%++
225	      - 0.71
226	      - 0.53
227	      - 0.746
228	      - -0.18
229	    - - ConStat (perturbation)
230	      - 0.69
231	      - 0.58
232	      - 0.841
233	      - -0.11
234	    - - DVD (generation variance)
235	      - 0.62
236	      - 0.56
237	      - 0.903
238	      - -0.06
239	    - - Perplexity ratio
240	      - 0.67
241	      - 0.49
242	      - 0.731
243	      - -0.18
244	    - - Zlib ratio
245	      - 0.59
246	      - 0.52
247	      - 0.881
248	      - -0.07
249	  - name: 'Table 5: DIF TPR Breakdown by RL Intensity'
250	    columns:
251	    - rl_category
252	    - n_models
253	    - dif_tpr_delta_ge_1.4
254	    - mink_auroc
255	    rows:
256	    - - SFT only
257	      - 187
258	      - 0.61
259	      - 0.74
260	    - - Light RL (< 200 steps)
261	      - 14
262	      - 0.57
263	      - 0.59
264	    - - Heavy RL (≥ 200 steps)
265	      - 21
266	      - 0.51
267	      - 0.47
268	  figures_description:
269	  - 'Figure 4: Grouped bar chart — AUROC by detection method, SFT vs RL cohorts. DIF
270	    shows smallest absolute drop. Min-K% shows largest. Error bars from bootstrap.
271	    Key visual: DIF bar heights nearly equal across groups; Min-K% and perplexity
272	    bars drop sharply in RL group.'
273	  - 'Figure 5: Power retention ratio plot — methods ranked by (AUROC_RL / AUROC_SFT).
274	    DIF ranks 2nd (0.885) after DVD (0.903), but DVD''s baseline is too low to be
275	    useful. Annotation: ''high retention on low baseline ≠ useful detection''.'
276	  - 'Figure 6: Scatter — DIF effect size vs Min-K% score per item, colored by model
277	    training type. SFT models show positive correlation; RL models show DIF signal
278	    persisting while Min-K% collapses toward uniform.'
279	  analysis: 'RL-robustness 存在但不 dramatic。DIF 的 retention ratio (0.885) 在所有方法中排名靠前，
280	    但 ConStat (0.841) 也保持了 reasonable power，DVD retention 高但 baseline 低。 Median tier
281	    下的故事不是 "DIF 是唯一幸存者"， 而是 "DIF 提供了 RL-robust 且 complementary 的信号"。 传统方法中 Min-K%
282	    退化最严重（AUROC 0.51，接近 random）， 这与 Wang et al. 一致——output-distribution-based 方法对
283	    RL 最脆弱。 但 performance-based 方法（ConStat）退化幅度小于预期。 Reviewer 可能攻击：(1) RL models 样本量小（n=35），统计
284	    power 有限； (2) "RL intensity" 是 proxy 而非精确度量。 需在 paper 中 acknowledge 这些 limitations
285	    并建议 future work 用 controlled RL fine-tuning 验证。
286	
287	    '
288	- name: constat_perturbation_eval
289	  plan_id: plan_003a
290	  description: '独立评估 ConStat-style perturbation testing 在 MMLU 上的 contamination 检测能力。
291	
292	    '
293	  expected_results:
294	    n_items_reformulated: 248
295	    n_models_tested: 42
296	    reformulation_semantic_similarity_mean: 0.91
297	    constat_tpr_non_rl_delta_ge_0.6: 0.47
298	    constat_tpr_non_rl_delta_ge_1.0: 0.58
299	    constat_tpr_non_rl_delta_ge_1.4: 0.64
300	    constat_tpr_rl_models_delta_ge_0.6: 0.23
301	    constat_tpr_rl_models_delta_ge_1.0: 0.31
302	    constat_fdr_controlled_alpha_0.05: 0.048
303	    constat_fdr_controlled_alpha_0.10: 0.087
304	    n_items_detected_fdr_0.10: 89
305	    overlap_with_dif_flags: 0.34
306	    gpu_hours_used: 72
307	  result_rationale: 'ConStat 在 non-RL models 上表现 reasonable（TPR=0.47 at δ≥0.6）， 因为
308	    perturbation sensitivity 是 memorization 的 direct signal—— memorized items 的 reformulated
309	    版本会导致 accuracy drop， 而 genuinely understood items 不会。这在 SFT models 上工作良好。 但 TPR
310	    未达到 ConStat 原论文 claimed 的水平，原因是： (1) MMLU 是 multiple-choice，perturbation space
311	    受限—— 改变 stem wording 可能改变 difficulty 而非仅测 memorization； (2) LLM reformulation
312	    质量不均匀，部分 paraphrases 引入了 subtle meaning shifts， 增加了 noise。在 RL models 上 TPR 下降到
313	    0.23（δ≥0.6）， 因为 RL 训练增强了 models 对 input perturbation 的 robustness（PPO reward hacking
314	    的副效应）， 使得 perturbation sensitivity 信号被 masked。 与 DIF flags 的 overlap 为 0.34——两种方法检测不同的
315	    contamination facets， DIF 捕捉 group-level behavioral shift，ConStat 捕捉 item-level
316	    perturbation sensitivity， 这正好支持 ensemble 的 complementarity 论点。
317	
318	    '
319	  tables:
320	  - name: 'Table 6: ConStat Detection Power by Effect Size and Model Type'
321	    columns:
322	    - effect_size_band
323	    - tpr_non_rl
324	    - tpr_rl
325	    - tpr_all_models
326	    rows:
327	    - - δ ≥ 1.4
328	      - 0.64
329	      - 0.31
330	      - 0.53
331	    - - δ ∈ [1.0, 1.4)
332	      - 0.58
333	      - 0.28
334	      - 0.48
335	    - - δ ∈ [0.6, 1.0)
336	      - 0.47
337	      - 0.23
338	      - 0.39
339	    - - δ < 0.6
340	      - 0.12
341	      - 0.08
342	      - 0.1
343	  - name: 'Table 7: ConStat vs DIF Signal Overlap Analysis'
344	    columns:
345	    - category
346	    - n_items
347	    - pct_of_flagged
348	    rows:
349	    - - Flagged by both DIF and ConStat
350	      - 31
351	      - 34%
352	    - - Flagged by DIF only
353	      - 58
354	      - 64%
355	    - - Flagged by ConStat only
356	      - 52
357	      - 57%
358	    - - Union (either method)
359	      - 141
360	      - —
361	  figures_description:
362	  - 'Figure 7: Venn diagram of DIF vs ConStat flagged items. Modest overlap (34%)
363	    demonstrates complementarity rather than redundancy. Annotated with examples:
364	    DIF-only items tend to be large-effect, RL-model-driven; ConStat-only items tend
365	    to be medium-effect, SFT-model-driven.'
366	  - 'Figure 8: ConStat detection power curve (TPR vs FDR threshold) for non-RL vs
367	    RL model subsets. Non-RL curve substantially above RL curve, visualizing the RL
368	    degradation. DIF power (horizontal reference line) shown for comparison.'
369	  analysis: 'ConStat 是 ensemble 中可用的第二个信号。它在 non-RL 场景下提供了 DIF 的 complementary coverage，
370	    尤其在 medium effect sizes（δ=0.6-1.4）——这恰好是 DIF 的 weak spot。 但 ConStat 在 RL 下 degradation
371	    明显（TPR 从 0.47 降至 0.23）， 形成了与 DIF 的互补关系：DIF RL-robust 但需大 effect sizes，ConStat
372	    覆盖 medium effects 但 RL-fragile。 两者 overlap 仅 34%，支持 ensemble 而非 redundancy。
373	
374	    '
375	- name: dvd_generation_variance_eval
376	  plan_id: plan_003b
377	  description: '独立评估 DVD generation variance 在 MMLU contamination detection 上的表现。
378	
379	    '
380	  expected_results:
381	    n_models_with_inference_access: 14
382	    n_items_tested: 248
383	    responses_per_item: 50
384	    dvd_tpr_variant_contamination: 0.38
385	    dvd_tpr_verbatim_contamination: 0.16
386	    dvd_tpr_non_variant_all: 0.19
387	    dvd_fpr: 0.094
388	    dvd_auroc_overall: 0.57
389	    bimodal_distribution_pct_items: 0.078
390	    generation_variance_mean_clean: 0.42
391	    generation_variance_mean_contaminated: 0.31
392	    generation_variance_separation_cohens_d: 0.38
393	    gpu_hours_used: 64
394	  result_rationale: 'DVD 在 median tier 下是表现最弱的信号，降级 ensemble 从 3-signal 到 2-signal
395	    的主要原因。 核心问题：MMLU 是 multiple-choice format，generation variance 的 signal 天然被压缩——
396	    即使 model 记忆了答案，其 generation 仍然只是 output 一个 letter (A/B/C/D)， variance 空间极为有限。DVD
397	    原设计针对 open-ended generation tasks， 在那里 memorized 内容会导致 deterministic long-form
398	    output（低 variance）， 但 MMLU 的 forced-choice format 使得这个信号几乎消失。 Variant contamination（model
399	    见过 rephrased version）确实产生了 slightly higher detection（TPR=0.38）， 因为 model 在 seen
400	    variants 上的 confidence distribution 有异常—— 但这个 TPR 仍然不足以作为 reliable signal。 Verbatim
401	    contamination 的 TPR 仅 0.16，因为 correct 答案的 generation variance 在 clean 和 contaminated
402	    items 之间差异太小（Cohen''s d=0.38）。 FPR=0.094 偏高，接近 actionable threshold。 这些结果表明 DVD
403	    在 MMLU-like benchmarks 上不适用， 但需在 paper 中分析 failure mode 并讨论其在 open-ended benchmarks
404	    上的 potential。
405	
406	    '
407	  tables:
408	  - name: 'Table 8: DVD Detection Performance on MMLU'
409	    columns:
410	    - contamination_type
411	    - n_items
412	    - tpr
413	    - auroc
414	    - cohen_d
415	    rows:
416	    - - Variant contamination
417	      - 34
418	      - 0.38
419	      - 0.62
420	      - 0.51
421	    - - Verbatim contamination
422	      - 89
423	      - 0.16
424	      - 0.54
425	      - 0.29
426	    - - Mixed/unknown
427	      - 125
428	      - 0.19
429	      - 0.57
430	      - 0.38
431	    - - Clean items
432	      - ~11600
433	      - —(FPR=0.094)
434	      - —
435	      - —
436	  - name: 'Table 9: Generation Variance Statistics'
437	    columns:
438	    - item_category
439	    - mean_variance
440	    - std
441	    - median
442	    rows:
443	    - - Clean items
444	      - 0.42
445	      - 0.18
446	      - 0.39
447	    - - Contaminated (verbatim)
448	      - 0.31
449	      - 0.21
450	      - 0.28
451	    - - Contaminated (variant)
452	      - 0.27
453	      - 0.19
454	      - 0.24
455	  figures_description:
456	  - 'Figure 9: Distribution of generation variance scores for clean vs contaminated
457	    items. Substantial overlap between distributions. Cohen''s d=0.38 indicates weak
458	    separation. Contrast with DIF effect size distribution (Figure 2) to motivate
459	    why DVD fails on multiple-choice format.'
460	  - 'Figure 10: Per-model variance heatmap (14 models × 248 items). No clear bimodal
461	    structure visible for most contaminated items. Bimodal pattern appears in only
462	    7.8% of items — insufficient for reliable detection.'
463	  analysis: 'DVD 是 ensemble 中 failed signal。Multiple-choice format 从根本上限制了 generation
464	    variance 的信息量。 这不是 DVD method 本身的缺陷，而是 application domain mismatch。 Paper 中需要：(1)
465	    清楚报告 DVD 的 failure 及 root cause analysis； (2) 讨论 DVD 可能在 open-ended benchmarks（如
466	    HumanEval、MATH with free-form answers）上有效； (3) 作为 ablation study 之一，分析 format
467	    dependence 对 detection signal 的影响。 这个 negative result 反而增强 paper 的 intellectual
468	    honesty，reviewer 会 appreciate  对 failure mode 的 transparent analysis 而非 cherry-picking。
469	
470	    '
471	- name: ensemble_fusion
472	  plan_id: plan_003c
473	  description: '将 DIF + ConStat 融合为双信号 ensemble（DVD 降级为 ablation analysis）。
474	
475	    '
476	  expected_results:
477	    ensemble_type: 2-signal (DIF + ConStat)
478	    ensemble_tpr_delta_ge_1.4_all: 0.73
479	    ensemble_tpr_delta_ge_1.0_all: 0.61
480	    ensemble_tpr_delta_ge_0.6_all: 0.48
481	    ensemble_tpr_full_spectrum: 0.68
482	    ensemble_fpr: 0.082
483	    ensemble_tpr_rl_only_delta_ge_1.4: 0.59
484	    ensemble_tpr_non_rl_delta_ge_0.6: 0.55
485	    majority_voting_2of2_tpr: 0.34
486	    majority_voting_1of2_tpr: 0.79
487	    majority_voting_1of2_fpr: 0.11
488	    weighted_fusion_optimal_tpr: 0.73
489	    weighted_fusion_optimal_fpr: 0.082
490	    dif_weight_in_fusion: 0.58
491	    constat_weight_in_fusion: 0.42
492	    ablation_dif_only_tpr: 0.58
493	    ablation_constat_only_tpr: 0.47
494	    ablation_add_dvd_tpr_gain: 0.02
495	    coverage_analysis_dif_unique: 0.21
496	    coverage_analysis_constat_unique: 0.18
497	    coverage_analysis_overlap: 0.29
498	  result_rationale: '2-signal ensemble 通过 complementarity 实现了比任一单信号更好的 coverage： DIF
499	    覆盖 large effects + RL-robust，ConStat 覆盖 medium effects + non-RL， union coverage
500	    高于单独使用任一方法。 Weighted fusion（DIF 0.58, ConStat 0.42）优于 simple voting， 因为 DIF 的
501	    RL-robustness 使其在 mixed model population 中更 reliable。 2-of-2 voting 过于保守（TPR=0.34），因为两种方法检测的
502	    contamination facet 不同—— 要求两者同时 flag 等于取 intersection 而非 union。 1-of-2 voting
503	    FPR 偏高（0.11），因为 ConStat 的 FPR contribution。 Weighted fusion 在 TPR=0.73 / FPR=0.082
504	    处取得最佳平衡。 加入 DVD 仅带来 +0.02 TPR gain，不值得增加 pipeline 复杂度， 证实了 2-signal 降级的合理性。 Ensemble
505	    TPR=0.68（full spectrum）落在 median tier 指标范围 [0.6, 0.8] 内。
506	
507	    '
508	  tables:
509	  - name: 'Table 10: Ensemble Fusion Strategy Comparison'
510	    columns:
511	    - strategy
512	    - tpr_δ≥1.4
513	    - tpr_δ≥0.6
514	    - fpr
515	    - f1
516	    rows:
517	    - - DIF only
518	      - 0.58
519	      - 0.38
520	      - 0.062
521	      - 0.47
522	    - - ConStat only
523	      - 0.64
524	      - 0.47
525	      - 0.087
526	      - 0.51
527	    - - 1-of-2 (union)
528	      - 0.79
529	      - 0.61
530	      - 0.11
531	      - 0.54
532	    - - 2-of-2 (intersection)
533	      - 0.34
534	      - 0.24
535	      - 0.031
536	      - 0.37
537	    - - Weighted fusion (optimal)
538	      - 0.73
539	      - 0.48
540	      - 0.082
541	      - 0.56
542	  - name: 'Table 11: Coverage Analysis — What Each Signal Uniquely Detects'
543	    columns:
544	    - scenario
545	    - dif_alone_detects
546	    - constat_alone_detects
547	    - both_detect
548	    - neither_detects
549	    rows:
550	    - - Large effect + RL model
551	      - ✓
552	      - ✗
553	      - —
554	      - —
555	    - - Medium effect + SFT model
556	      - ✗
557	      - ✓
558	      - —
559	      - —
560	    - - Large effect + SFT model
561	      - —
562	      - —
563	      - ✓
564	      - —
565	    - - Small effect (δ<0.6)
566	      - —
567	      - —
568	      - —
569	      - ✓
570	  - name: 'Table 12: Ablation — Value of Each Signal in Ensemble'
571	    columns:
572	    - configuration
573	    - tpr_full_spectrum
574	    - Δ_vs_full_ensemble
575	    rows:
576	    - - DIF + ConStat (full)
577	      - 0.68
578	      - baseline
579	    - - DIF only
580	      - 0.58
581	      - -0.1
582	    - - ConStat only
583	      - 0.47
584	      - -0.21
585	    - - DIF + ConStat + DVD
586	      - 0.7
587	      - 0.02
588	  figures_description:
589	  - 'Figure 11: Coverage heatmap — rows are (effect size band × model type) cells,
590	    columns are detection methods. Color intensity = TPR in that cell. Shows DIF strong
591	    in upper-right (large effect, RL), ConStat strong in middle-left (medium effect,
592	    SFT), both weak in lower region (small effects). Ensemble union covers more cells
593	    than either alone.'
594	  - 'Figure 12: Precision-Recall curves for single-signal vs ensemble approaches.
595	    Ensemble curve dominates both individual curves, especially in the 0.4-0.7 recall
596	    range where complementarity adds most value.'
597	  - 'Figure 13: Ablation bar chart — TPR contribution of adding each signal. DIF→DIF+ConStat:
598	    +0.10. DIF+ConStat→+DVD: +0.02. Diminishing returns visualized; motivates 2-signal
599	    design choice.'
600	  analysis: '2-signal ensemble 在 median tier 下是 pragmatic best result： full spectrum
601	    TPR=0.68 说明 coverage 有显著 gaps（尤其 small effects + RL）， 但比任一单信号提升 10-21pp。 Paper
602	    narrative 需强调 complementarity mechanism 而非 absolute performance， 并 honestly 报告
603	    coverage holes。 DVD ablation 提供了 principled argument for 2-signal design， 同时 DVD
604	    failure analysis 作为 Section 5.3 的 content。 Reviewer concern：FPR=0.082 接近 0.10
605	    boundary，需讨论 false alarm cost 和 threshold tuning。
606	
607	    '
608	- name: cross_benchmark_gsm8k
609	  plan_id: plan_004
610	  description: '在 GSM8K 上复制 DIF 分析，使用 GSM1K 作为 contamination ground truth。
611	
612	    '
613	  expected_results:
614	    n_models_gsm8k: 68
615	    n_items_gsm8k: 1319
616	    n_items_gsm1k: 1250
617	    cohort_split: pre-2024 vs post-2024
618	    focal_n: 31
619	    reference_n: 37
620	    n_items_dif_flagged_gsm8k: 127
621	    pct_items_flagged_gsm8k: 0.096
622	    gsm8k_gsm1k_gap_mean_all_models: 0.073
623	    gsm8k_gsm1k_gap_mean_flagged_models: 0.118
624	    gsm8k_gsm1k_gap_dif_correlation: 0.22
625	    gsm8k_gsm1k_gap_correlation_p_value: 0.014
626	    dif_tpr_vs_gsm1k_proxy: 0.49
627	    dif_fpr_vs_gsm1k_proxy: 0.071
628	    per_model_dif_flag_count_vs_gap_r: 0.31
629	    gpu_hours_used: 83
630	  result_rationale: 'GSM8K 上的 DIF 分析面临更大挑战：(1) model sample size 更小（N=68 vs MMLU 的
631	    4312）， 直接降低 statistical power；(2) GSM8K 是 math reasoning 而非 factual recall， contamination
632	    pattern 不同——models 可能记忆了 solution patterns 而非 specific items， DIF 对 pattern-level
633	    contamination 不如 item-level 敏感。 GSM8K-GSM1K gap correlation (ρ=0.22, p=0.014)
634	    提供了独立验证 DIF 有 contamination 信号的证据， 但 correlation 弱于 MMLU-CF（ρ=0.21 对 ρ=0.22 看似接近，但
635	    GSM1K 是更 clean 的 ground truth）， 反映了 math reasoning benchmark 上 contamination 形态的不同。
636	    Per-model analysis（每个 model 被 flag 的 item count vs 其 GSM8K-GSM1K gap，r=0.31） 比
637	    item-level correlation 更强，说明 DIF 在 model-level 上更有 discriminative power。 TPR=0.49
638	    低于 MMLU 的 0.58，主要因为 sample size 和 effect size distribution 差异。
639	
640	    '
641	  tables:
642	  - name: 'Table 13: GSM8K DIF Results Summary'
643	    columns:
644	    - metric
645	    - value
646	    - 95% CI
647	    rows:
648	    - - Items flagged by DIF
649	      - 127
650	      - —
651	    - - Mean GSM8K-GSM1K gap (all models)
652	      - 7.3%
653	      - '[5.1%, 9.5%]'
654	    - - Mean gap (high DIF-flag-count models)
655	      - 11.8%
656	      - '[8.2%, 15.4%]'
657	    - - Item-level DIF-gap correlation (ρ)
658	      - 0.22
659	      - '[0.06, 0.37]'
660	    - - Model-level flag-count-gap correlation (r)
661	      - 0.31
662	      - '[0.14, 0.47]'
663	  - name: 'Table 14: Cross-Benchmark Comparison'
664	    columns:
665	    - benchmark
666	    - n_models
667	    - n_items
668	    - dif_tpr
669	    - ground_truth_correlation
670	    - fpr
671	    rows:
672	    - - MMLU
673	      - 4312
674	      - 11847
675	      - 0.58
676	      - ρ=0.21 (MMLU-CF)
677	      - 0.062
678	    - - GSM8K
679	      - 68
680	      - 1319
681	      - 0.49
682	      - ρ=0.22 (GSM1K)
683	      - 0.071
684	  figures_description:
685	  - 'Figure 14: Scatter — per-model DIF flag count vs GSM8K-GSM1K accuracy gap. Positive
686	    trend (r=0.31) with high variance. Models with >15 flagged items tend to have
687	    larger gaps. Outliers annotated: some models with large gaps but few DIF flags
688	    (pattern-level contamination DIF misses).'
689	  - 'Figure 15: Side-by-side DIF effect size distributions for MMLU and GSM8K. GSM8K
690	    distribution shifted left (smaller effects on average), consistent with math reasoning
691	    contamination being subtler than factual knowledge contamination.'
692	  analysis: 'GSM8K 结果提供了 complementary 但非 decisive 的验证。 ρ=0.22 是 statistically significant
693	    但 practically weak 的 correlation。 主要价值是证明 DIF 在不同 benchmark domain（factual vs
694	    reasoning）上都有 signal， 但 power 更低。Paper 中需讨论 math reasoning benchmarks 上 contamination
695	    形态不同 （pattern memorization vs item memorization）作为 DIF power 下降的 explanation。
696	    这个实验作为 supporting evidence 而非 standalone result。
697	
698	    '
699	- name: bifactor_irt_equating_pilot
700	  plan_id: plan_005
701	  description: '在 MMLU 上 pilot bifactor IRT equating：拟合 bifactor model，选择 anchor items，
702	    通过 fixed-parameter calibration 校准 replacement items。
703	
704	    '
705	  expected_results:
706	    bifactor_model_converged: true
707	    n_general_factor_loadings_gt_0.3: 9847
708	    n_subject_factors: 57
709	    subject_factor_variance_explained_range: 0.04-0.18
710	    general_factor_variance_explained: 0.41
711	    n_anchor_items_selected: 2340
712	    anchor_item_dif_stability: 0.96
713	    within_subject_equating_spearman_rho_mean: 0.93
714	    within_subject_equating_rho_range: 0.89-0.97
715	    cross_subject_equating_spearman_rho: 0.87
716	    cross_subject_factor_instability_pct: 0.23
717	    score_reliability_original: 0.89
718	    score_reliability_equated_5pct_replaced: 0.87
719	    score_reliability_equated_20pct_replaced: 0.82
720	    equating_bias_mean: 0.003
721	    equating_rmse: 0.047
722	  result_rationale: 'Bifactor model 在 MMLU 上 converges 但 reveals structural heterogeneity：
723	    general factor 仅解释 41% variance（低于典型 educational test 的 50-60%）， 因为 MMLU 覆盖 57
724	    个 diverse subjects，跨 subject variance 大。 Within-subject equating 表现良好（mean ρ=0.93），因为
725	    same-subject items 共享 factor structure， anchor items 稳定性高（stability=0.96）。 但 cross-subject
726	    equating（ρ=0.87）低于 within-subject，因为 23% 的 subjects 的 factor structure 在不同 model
727	    cohorts 间不稳定—— 即 model evolution 不仅改变了 ability level，也改变了 ability structure （某些
728	    model families 在 STEM 上进步远快于 humanities）， violating bifactor model 的 factorial
729	    invariance 假设。 ρ=0.93 在 within-subject 内可行但 ρ=0.87 cross-subject 不足以支持 "全 benchmark
730	    等值" 的 claim。 这迫使 Claim 3 限定 scope 为 within-subject equating pilot。 Progressive
731	    replacement 分析显示 5% 替换下 reliability 可接受（0.87）， 但 20% 替换时 reliability 降至 0.82，接近
732	    practical minimum。
733	
734	    '
735	  tables:
736	  - name: 'Table 15: Bifactor Model Fit Statistics'
737	    columns:
738	    - metric
739	    - value
740	    rows:
741	    - - General factor variance explained
742	      - 0.41
743	    - - Mean subject-factor variance
744	      - 0.09
745	    - - RMSEA
746	      - 0.038
747	    - - CFI
748	      - 0.94
749	    - - TLI
750	      - 0.92
751	    - - Subjects with stable factor structure
752	      - 44/57 (77%)
753	  - name: 'Table 16: Equating Performance by Scope'
754	    columns:
755	    - scope
756	    - spearman_rho
757	    - equating_bias
758	    - rmse
759	    - n_items_replaced
760	    rows:
761	    - - Within-subject (STEM avg)
762	      - 0.95
763	      - 0.002
764	      - 0.038
765	      - 47
766	    - - Within-subject (Humanities avg)
767	      - 0.91
768	      - 0.004
769	      - 0.052
770	      - 39
771	    - - Within-subject (overall)
772	      - 0.93
773	      - 0.003
774	      - 0.047
775	      - 86
776	    - - Cross-subject (full MMLU)
777	      - 0.87
778	      - 0.011
779	      - 0.073
780	      - 86
781	  - name: 'Table 17: Score Reliability Under Progressive Replacement'
782	    columns:
783	    - pct_items_replaced
784	    - reliability_α
785	    - ranking_τ
786	    - rho
787	    rows:
788	    - - 0% (baseline)
789	      - 0.89
790	      - 1.0
791	      - 1.0
792	    - - 5%
793	      - 0.87
794	      - 0.98
795	      - 0.97
796	    - - 10%
797	      - 0.85
798	      - 0.96
799	      - 0.95
800	    - - 20%
801	      - 0.82
802	      - 0.93
803	      - 0.91
804	    - - 50%
805	      - 0.74
806	      - 0.84
807	      - 0.82
808	  figures_description:
809	  - 'Figure 16: Within-subject equating scatter plots for 4 representative subjects.
810	    Original vs equated model rankings. STEM subjects (physics, CS) show tighter fit;
811	    humanities subjects (philosophy, history) show more scatter.'
812	  - 'Figure 17: Reliability degradation curve — score reliability (Cronbach''s α equivalent)
813	    vs percentage of items replaced. Horizontal dashed line at α=0.80 (acceptable
814	    threshold). Crosses threshold between 20-30% replacement, suggesting practical
815	    upper bound.'
816	  - 'Figure 18: Subject-level factor stability analysis. Heatmap of factor loading
817	    correlations across cohorts per subject. 23% of subjects show loading correlation
818	    < 0.85, indicating structural instability.'
819	  analysis: 'Within-subject equating 是 viable（ρ=0.93），但 cross-subject 不稳定（ρ=0.87）
820	    限制了 full-benchmark equating 的 claim。 Paper 中需要：(1) 明确 scope 限制——Claim 3 rewrite
821	    为 "within-subject equating pilot"； (2) 讨论 factor instability 的 root cause（model
822	    capability evolution 非 uniform across domains）； (3) 提出 subject-specific equating
823	    作为 practical deployment strategy。 Progressive replacement 结果提供了 practical guideline：5-10%
824	    替换安全，20% 是 borderline， 50% 不可接受。这是有用的 contribution 即使 full equating 不完美。
825	
826	    '
827	- name: item_generation_calibration
828	  plan_id: plan_006
829	  description: '为 DIF-flagged 的 MMLU items 生成替换 items，通过 student simulation 校准 difficulty。
830	
831	    '
832	  expected_results:
833	    n_items_generated: 150
834	    n_items_passing_quality_filter: 118
835	    quality_filter_pass_rate: 0.787
836	    difficulty_rho_prompt_based: 0.32
837	    difficulty_rho_student_sim: 0.63
838	    difficulty_rho_student_sim_within_subject: 0.68
839	    discrimination_correlation: 0.41
840	    construct_validity_factor_loading_mean: 0.38
841	    construct_validity_factor_loading_original_mean: 0.47
842	    difficulty_mae_prompt_based: 0.34
843	    difficulty_mae_student_sim: 0.19
844	    n_items_within_0.5_logit_of_target: 74
845	    pct_items_within_0.5_logit: 0.627
846	    gpu_hours_used: 178
847	  result_rationale: 'Student simulation calibration（ρ=0.63）显著优于 prompt-based targeting（ρ=0.32），
848	    因为 student simulation 通过实际 "model population" 响应来 estimate difficulty， 绕过了 LLM
849	    self-assessment 的 calibration 问题。 但 ρ=0.63 低于 arXiv 2601.09953 reported 的 r=0.75-0.82，原因有二：
850	    (1) 那篇论文的 evaluation 是 within-domain（同类型题目）， 而这里的 generated items 跨越了 57 subjects，domain
851	    diversity 降低了 aggregate correlation； (2) MMLU items 的 difficulty 部分来自 distractor
852	    quality， LLM generation 的 distractors 往往不如 human-crafted 的 effective， 导致 generated
853	    items systematically easier（difficulty MAE=0.19 with slight easy-bias）。 Within-subject
854	    ρ=0.68 高于 overall 的 0.63，说明 domain-specific generation 更 reliable。 Construct validity
855	    是 soft spot：generated items 的 factor loadings（mean=0.38） 低于 original items（0.47），表明
856	    generated items 与 underlying construct 的 alignment 较弱。 这 limits claim 强度——replacement
857	    items 在 difficulty 上校准 acceptable， 但 construct validity 有 degradation。
858	
859	    '
860	  tables:
861	  - name: 'Table 18: Difficulty Calibration Comparison'
862	    columns:
863	    - method
864	    - ρ_overall
865	    - ρ_within_subject
866	    - mae
867	    - n_within_0.5_logit
868	    rows:
869	    - - Prompt-based targeting
870	      - 0.32
871	      - 0.39
872	      - 0.34
873	      - 41/118 (35%)
874	    - - Student simulation
875	      - 0.63
876	      - 0.68
877	      - 0.19
878	      - 74/118 (63%)
879	    - - Student sim + iterative refinement
880	      - 0.66
881	      - 0.71
882	      - 0.17
883	      - 79/118 (67%)
884	  - name: 'Table 19: Generated Item Quality Metrics'
885	    columns:
886	    - metric
887	    - generated_items
888	    - original_items
889	    - gap
890	    rows:
891	    - - Mean difficulty (IRT b)
892	      - -0.62
893	      - -0.84
894	      - +0.22 (easier)
895	    - - Mean discrimination (IRT a)
896	      - 0.93
897	      - 1.2
898	      - '-0.27'
899	    - - Factor loading (general)
900	      - 0.38
901	      - 0.47
902	      - '-0.09'
903	    - - Distractor effectiveness
904	      - 0.61
905	      - 0.78
906	      - '-0.17'
907	  figures_description:
908	  - 'Figure 19: Scatter — target difficulty (from DIF-flagged original item) vs achieved
909	    difficulty (student simulation estimate). Prompt-based (left panel, ρ=0.32) vs
910	    student sim (right panel, ρ=0.63). Student sim shows tighter fit with systematic
911	    easy-bias visible as regression line below identity.'
912	  - 'Figure 20: Histogram of difficulty calibration errors (|b_target - b_achieved|).
913	    Student sim distribution shifted left relative to prompt-based. 63% of student
914	    sim items within 0.5 logit of target (vs 35% for prompt-based).'
915	  analysis: 'Student simulation calibration 是 viable 但 imperfect 的 difficulty estimation
916	    method。 ρ=0.63 的 practical implication：about 2/3 of items 在 acceptable difficulty
917	    range 内， 足够 support "empirical calibration dramatically outperforms prompt-based"
918	    的 claim， 但不足以 claim "precise psychometric replacement"。 Construct validity gap（factor
919	    loading 0.38 vs 0.47）是 paper 需要 honestly address 的 limitation—— generated items
920	    测量了 approximately same construct 但不 identical。 Combined with equating results
921	    (plan_005)，Claim 3 的叙事应为 "pilot demonstration of calibrated regeneration with
922	    known quality bounds"。
923	
924	    '
925	- name: cumulative_bayesian_dif
926	  plan_id: plan_007
927	  description: '实现 cumulative Bayesian DIF priors，模拟 4 次连续 benchmark administrations，
928	    展示 evidence accumulation 带来的 power improvement。
929	
930	    '
931	  expected_results:
932	    n_administrations_simulated: 4
933	    n_models_per_administration: 80
934	    power_admin_1_medium_delta_1.0: 0.33
935	    power_admin_2_cumulative: 0.48
936	    power_admin_3_cumulative: 0.59
937	    power_admin_4_cumulative: 0.66
938	    power_admin_1_large_delta_1.4: 0.55
939	    power_admin_4_large_delta_1.4_cumulative: 0.78
940	    false_positive_rate_cumulative: 0.053
941	    bayes_factor_threshold: 3.0
942	    pct_items_reaching_bf_threshold_by_admin_4: 0.71
943	  result_rationale: 'Bayesian accumulation 从 real-data 的 lower baseline 开始（而非 simulation
944	    的 higher baseline）， 所以 single administration power 为 0.33（medium effect），低于 simulation
945	    的 ~0.40。 但 accumulation dynamic 仍然 works：每次 administration 增加约 0.10-0.15 power，
946	    到第 4 次达到 0.66——接近但未达到 simulation 预期的 0.70。 Gap 来自 real data 的 prior mis-specification：Bayesian
947	    prior 假设 DIF effects  follow specific distribution，但真实 contamination 的 temporal
948	    dynamics 不 stationary （某些 items 的 contamination 随时间变化，violating prior assumptions）。
949	    FPR 保持在 0.053，说明 Bayesian framework 的 false alarm control 合理。 For large effects（δ=1.4），cumulative
950	    power 达到 0.78（4 administrations）， 这是 paper 中值得 highlight 的 positive result——说明
951	    "patience pays off"。
952	
953	    '
954	  tables:
955	  - name: 'Table 20: Cumulative Bayesian DIF Power Over Successive Administrations'
956	    columns:
957	    - administration
958	    - n_models_cumulative
959	    - power_δ=1.0
960	    - power_δ=1.4
961	    - fpr
962	    rows:
963	    - - '1'
964	      - 80
965	      - 0.33
966	      - 0.55
967	      - 0.048
968	    - - '2'
969	      - 160
970	      - 0.48
971	      - 0.67
972	      - 0.051
973	    - - '3'
974	      - 240
975	      - 0.59
976	      - 0.74
977	      - 0.052
978	    - - '4'
979	      - 320
980	      - 0.66
981	      - 0.78
982	      - 0.053
983	  figures_description:
984	  - 'Figure 21: Power accumulation curves — TPR vs number of administrations for δ=1.0
985	    and δ=1.4. Both curves show diminishing-returns concave shape. δ=1.4 curve crosses
986	    0.70 threshold by administration 3; δ=1.0 curve approaches but doesn''t reach
987	    0.70 by administration 4. Extrapolation (dashed) suggests ~6 administrations needed
988	    for δ=1.0 to reach 0.70.'
989	  analysis: 'Bayesian accumulation 是 DIF power 不足问题的 temporal solution。 核心 message：单次检测
990	    power 有限（0.33-0.55），但 monitoring framework  通过时间积累达到 useful power（0.66-0.78 at
991	    4 administrations）。 这 directly supports "psychometric monitoring framework" 的
992	    narrative reframing—— 不是 one-shot detection 而是 continuous monitoring。 但需要注意 practical
993	    caveat：4 administrations 可能需要 1-2 年， 在此期间 contamination 已经对 benchmark validity
994	    造成了 damage。
995	
996	    '
997	- name: graceful_degradation_analysis
998	  plan_id: plan_008
999	  description: '分析 benchmark validity 在 progressive item replacement 下的 graceful degradation。
1000	
1001	    '
1002	  expected_results:
1003	    replacement_rates_tested:
1004	    - 0.05
1005	    - 0.1
1006	    - 0.15
1007	    - 0.2
1008	    - 0.3
1009	    - 0.5
1010	    ranking_stability_kendall_tau_5pct: 0.97
1011	    ranking_stability_kendall_tau_10pct: 0.95
1012	    ranking_stability_kendall_tau_20pct: 0.91
1013	    ranking_stability_kendall_tau_50pct: 0.81
1014	    score_reliability_cronbach_5pct: 0.87
1015	    score_reliability_cronbach_10pct: 0.85
1016	    score_reliability_cronbach_20pct: 0.82
1017	    score_reliability_cronbach_50pct: 0.74
1018	    construct_coverage_jaccard_5pct: 0.97
1019	    construct_coverage_jaccard_20pct: 0.89
1020	    construct_coverage_jaccard_50pct: 0.76
1021	    theoretical_upper_bound_replacement_rate: 0.25
1022	    practical_recommended_max: 0.15
1023	    equating_error_propagation_rmse_10pct: 0.041
1024	    equating_error_propagation_rmse_20pct: 0.068
1025	  result_rationale: 'Graceful degradation 分析显示 benchmark validity 在 low replacement
1026	    rates 下 well-preserved， 但在 >20% 时快速衰退。这符合 psychometric theory：test reliability
1027	    近似为 Spearman-Brown 函数， each replaced item 引入 calibration error（plan_006 显示 difficulty
1028	    ρ=0.63）， error 随 replacement rate 线性累积但 validity impact 呈 nonlinear degradation。
1029	    15% replacement 是 practical sweet spot：ranking stability (τ=0.93) 和 reliability
1030	    (α=0.84)  都在 acceptable range，且涵盖了 plan_001 中约 80% 的 δ≥1.0 flagged items。 50%
1031	    replacement 的 reliability 降至 0.74，低于 psychometric 标准的 0.80 threshold—— 这是 "benchmark
1032	    不再可比" 的 hard boundary。 Theoretical analysis 给出 upper bound 25%（在 perfect calibration
1033	    假设下）， 但 plan_006 的 imperfect calibration 将实际 limit 压到 15%。
1034	
1035	    '
1036	  tables:
1037	  - name: 'Table 21: Validity Metrics Under Progressive Replacement'
1038	    columns:
1039	    - replacement_rate
1040	    - kendall_τ
1041	    - cronbach_α
1042	    - construct_jaccard
1043	    - equating_rmse
1044	    rows:
1045	    - - 0% (baseline)
1046	      - 1.0
1047	      - 0.89
1048	      - 1.0
1049	      - 0.0
1050	    - - 5%
1051	      - 0.97
1052	      - 0.87
1053	      - 0.97
1054	      - 0.029
1055	    - - 10%
1056	      - 0.95
1057	      - 0.85
1058	      - 0.94
1059	      - 0.041
1060	    - - 15%
1061	      - 0.93
1062	      - 0.84
1063	      - 0.91
1064	      - 0.054
1065	    - - 20%
1066	      - 0.91
1067	      - 0.82
1068	      - 0.89
1069	      - 0.068
1070	    - - 30%
1071	      - 0.87
1072	      - 0.78
1073	      - 0.83
1074	      - 0.091
1075	    - - 50%
1076	      - 0.81
1077	      - 0.74
1078	      - 0.76
1079	      - 0.132
1080	  figures_description:
1081	  - 'Figure 22: Multi-panel degradation curves — kendall τ, cronbach α, construct
1082	    coverage vs replacement rate. All three metrics show concave degradation pattern.
1083	    Shaded regions indicate ''safe'' (<15%), ''caution'' (15-25%), and ''unacceptable''
1084	    (>25%) zones. Vertical dashed lines at 15% (practical) and 25% (theoretical) bounds.'
1085	  - 'Figure 23: Equating error propagation — RMSE of equated scores vs replacement
1086	    rate. Near-linear growth up to 20%, then acceleration. Error bars from bootstrap
1087	    (100 resamples).'
1088	  analysis: 'This experiment 提供了 Claim 3 最重要的 practical guideline： up to 15% item
1089	    replacement 维持 acceptable validity，这足以处理大部分 contamination。 Paper 应将此 frame 为 "known
1090	    operating envelope" 而非 limitation—— psychometric maturity 在于知道方法的 validity bounds，而非声称无限
1091	    scalability。 Theoretical vs practical bound gap（25% vs 15%）由 item generation quality
1092	    驱动， 指向 future work：improve generation quality → expand operating envelope。
1093	
1094	    '
1095	- name: item_focused_trees
1096	  plan_id: plan_009
1097	  description: '实现 Item-Focused Trees 作为 categorical cohort DIF 的替代方案， 将 model release
1098	    date 作为连续 covariate。
1099	
1100	    '
1101	  expected_results:
1102	    n_items_analyzed: 11847
1103	    n_items_significant_ift: 891
1104	    ift_tpr_delta_ge_1.4: 0.62
1105	    ift_tpr_delta_ge_1.0: 0.46
1106	    ift_fpr: 0.058
1107	    ift_vs_ets_c_tpr_gain: 0.04
1108	    ift_vs_ets_c_fpr_reduction: 0.004
1109	    ift_detected_gradual_contamination_items: 134
1110	    ift_split_point_mode_month: 2023-09
1111	    ift_computational_time_minutes: 47
1112	  result_rationale: 'Item-Focused Trees 提供了 modest improvement over categorical DIF（TPR
1113	    +0.04, FPR -0.004）， 因为它避免了 arbitrary cohort splits 导致的 information loss—— 连续 covariate
1114	    保留了 release date 的 full ordering information。 但 improvement 幅度有限，因为 contamination
1115	    在时间上确实是 roughly step-function-like （一旦 benchmark 被 widely available，contamination
1116	    快速 saturates）， 使得 continuous treatment 的 marginal benefit 小。 IFT 的独特贡献是发现了 134
1117	    个 "gradual contamination" items—— 这些 items 的 DIF effect size 随时间平滑增长而非 suddenly
1118	    appear， 对应 incremental leakage pattern。这在 categorical DIF 中不可见。 Split point mode
1119	    在 2023-09，大致对应 MMLU 进入 mainstream LLM training data 的时间点。
1120	
1121	    '
1122	  tables:
1123	  - name: 'Table 22: IFT vs Categorical DIF Comparison'
1124	    columns:
1125	    - method
1126	    - tpr_δ≥1.4
1127	    - tpr_δ≥1.0
1128	    - fpr
1129	    - unique_detections
1130	    rows:
1131	    - - ETS C (categorical)
1132	      - 0.58
1133	      - 0.41
1134	      - 0.062
1135	      - 47
1136	    - - IFT (continuous)
1137	      - 0.62
1138	      - 0.46
1139	      - 0.058
1140	      - 134
1141	    - - Overlap (both detect)
1142	      - —
1143	      - —
1144	      - —
1145	      - 612
1146	  figures_description:
1147	  - 'Figure 24: Item-level contamination onset timeline. X-axis: model release date.
1148	    Y-axis: IFT-estimated DIF effect size. Each line represents one item. Most items
1149	    show step-function pattern (sudden onset); 134 items show gradual ramp (linear
1150	    increase). Vertical dashed line at 2023-09.'
1151	  analysis: IFT 是 useful methodological extension 但非 game-changer。 Paper 中作为 robustness
1152	    check 和 methodological contribution（Section 4.x）。 Gradual contamination finding
1153	    是 interesting insight， 可作为 discussion point 关于 contamination dynamics。 Reviewer
1154	    可能认为 +0.04 TPR 不值得 additional complexity； response 是 IFT 的价值在 qualitative insight（gradual
1155	    contamination）而非 quantitative gain。
1156	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "524b2918-6da8-4cf3-b36c-c90b09470124",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "e8b5c3ea-9c5e-4917-8652-bcb7ada810a9",
  "sourceToolAssistantUUID": "524b2918-6da8-4cf3-b36c-c90b09470124",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-20T20:18:38.987Z_

Now I have a thorough understanding of the paper across all three tiers (best/median/worst). The paper summary provided in the prompt uses numbers that closely match the **median** tier imagined experiments. Let me now write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8b5c3ea-9c5e-4917-8652-bcb7ada810a9",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESR3nZ7SWc2KTs4CXwW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43ad07cb-5dd6-42ee-b668-047b398bb265",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yqLzn6PzV9vaBcAKd56CH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19613,
      "cache_read_input_tokens": 77748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19613,
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

_source line 43 · 2026-05-20T20:18:39.831Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012J2sa43KN4CmptJeqyXN2k`</summary>

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
  "parentUuid": "43ad07cb-5dd6-42ee-b668-047b398bb265",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESR3nZ7SWc2KTs4CXwW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e33e9120-c8d3-49b5-bc91-b0ce9de29b65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yqLzn6PzV9vaBcAKd56CH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19613,
      "cache_read_input_tokens": 77748,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19613
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 77748,
          "cache_creation_input_tokens": 19613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19613,
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

_source line 44 · 2026-05-20T20:18:39.834Z_

<details><summary>↩ Tool result · `toolu_012J2sa43KN4CmptJeqyXN2k`</summary>

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
  "parentUuid": "e33e9120-c8d3-49b5-bc91-b0ce9de29b65",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "0f5fb94f-92a0-4922-9350-90dbf4ef65e8",
  "sourceToolAssistantUUID": "e33e9120-c8d3-49b5-bc91-b0ce9de29b65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-20T20:18:43.465Z_



Now I have all the information needed to write a thorough R1 review. The paper summary numbers align with the **median** tier imagined experiments, which is the most realistic scenario. Let me construct the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f5fb94f-92a0-4922-9350-90dbf4ef65e8",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESRQxmSzaHRmS9QiA6S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84305b4e-7918-4eba-8466-07dffecaff94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lg6j1oCu3pG8pwg282ohUu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 97361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 764,
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

_source line 46 · 2026-05-20T20:21:03.713Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01B4yPyGBY5MUirzztkrJ75a`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "tier": "median",
  "dream_id": "dream_20260520T194223",
  "overall_score": "3/6 Weak Reject",
  "report": "# Review Report — R1: Methods and Experiments\n\n**Paper:** \"Psychometric Monitoring for LLM Benchmark Contamination: A Framework for Detection, Diagnosis, and Contamination-Aware Recalibration\"\n\n**Reviewer Role:** R1 (Methods + Experiments)\n**Score:** 3/6 (Weak Reject)\n**Confidence:** 4/5\n\n---\n\n## Summary\n\nThe paper proposes a psychometric monitoring framework for LLM benchmark contamination grounded in Item Response Theory (IRT). It makes three claims: (1) DIF analysis detects contamination robustly to RL training, (2) a dual-signal ensemble (DIF + ConStat) covers the full effect-size spectrum, and (3) bifactor IRT equating enables psychometrically calibrated benchmark regeneration. Experiments span MMLU (4,312 models x 11,847 items), GSM8K cross-validation, item generation calibration, cumulative Bayesian DIF, graceful degradation, and Item-Focused Trees.\n\nThe core intellectual contribution -- reframing benchmark contamination as Differential Item Functioning -- is genuinely insightful and represents a valuable cross-disciplinary bridge. However, as detailed below, the paper has multiple methodological weaknesses that collectively undermine the headline claims: the RL-robustness evidence is critically underpowered, real-data ground truth is inadequately defined, a fundamental contamination-vs-capability confound is not addressed, the ensemble construction lacks rigor, and the equating pilot reveals structural limitations that the claims do not sufficiently acknowledge.\n\n---\n\n## Strengths\n\n### S1. Principled cross-disciplinary reframing\nRecasting contamination detection as DIF is the paper's strongest intellectual contribution. The argument that DIF operates on group-level Item Characteristic Curves -- detecting whether the focal group has higher P(correct | theta) than the reference group for specific items -- provides a well-grounded theoretical basis for why this signal should survive RL training. The psychometric vocabulary is correctly applied: ETS C classification (|Delta_MH| >= 1.5 + statistical significance), Mantel-Haenszel stratification, and effect-size-based detection rather than p-value thresholding are all methodologically sound choices that reflect genuine understanding of the DIF literature.\n\n### S2. Appropriate IRT model selection for the primary analysis\nThe 2PL IRT model is a defensible choice for MMLU binary response data at this scale. The decision to use ETS C classification over BH-corrected p-values (documented in D001) is well-motivated: with ~12K items, multiple testing correction destroys power while ETS C's magnitude-based thresholds maintain practical detection rates. This reflects mature psychometric reasoning.\n\n### S3. DVD failure mode analysis as honest negative result\nThe paper's transparent reporting of DVD's failure on multiple-choice format (AUROC=0.57, FPR=0.094) and the principled downgrade from 3-signal to 2-signal ensemble is commendable. The root cause analysis -- that forced-choice response format compresses generation variance, eliminating DVD's discriminative signal -- is convincing and adds methodological value. This kind of honest negative result reporting is rare and appreciated.\n\n### S4. Student simulation calibration comparison\nThe difficulty calibration comparison (student simulation rho=0.63 vs prompt-based rho=0.32) is a valuable standalone contribution. The systematic easy-bias in generated items (mean discrimination 0.93 vs 1.20 for originals; factor loading 0.38 vs 0.47) is honestly reported and provides actionable guidance for the item generation community.\n\n### S5. Graceful degradation framework with practical bounds\nThe progressive replacement analysis (5%-50%) with three validity metrics (ranking tau, reliability alpha, construct Jaccard) provides a useful operational framework. The finding that 15% replacement is the practical maximum (tau=0.93, alpha=0.84) given imperfect calibration quality is a responsible, data-driven recommendation.\n\n### S6. Breadth of experimental coverage\nCovering 11 experiments across detection, ensemble fusion, cross-benchmark validation, equating, generation, Bayesian accumulation, degradation analysis, and Item-Focused Trees is ambitious. Each experiment addresses a logical gap in the overall framework.\n\n---\n\n## Weaknesses\n\n### Major\n\n#### M1. RL-robustness claim is critically underpowered and the headline framing is unjustified\n**Severity: Major (potential reject-level).**\n\nThe paper's central selling point is RL-robustness, yet it rests on n=35 RL models (23 identified in METABENCH + 12 via inference), with subgroup analyses splitting into groups of n=14 and n=21. Several specific problems:\n\n(a) **Statistical power is insufficient for the claimed conclusion.** The power retention ratio of 0.885 (DIF AUROC 0.68 under RL vs 0.73 under SFT) yields a Delta of 0.05 AUROC points. With n=35, a paired comparison has essentially no power to distinguish \"no meaningful degradation\" from \"meaningful degradation that we failed to detect.\" The paper does not report a power analysis for this comparison, nor does it compute confidence intervals on the retention ratio. A bootstrap 95% CI on 0.885 with n=35 would likely span from ~0.75 to ~1.0, encompassing scenarios where DIF loses 25% of its power under RL -- far from \"robust.\"\n\n(b) **The comparison between DIF and traditional methods is on different granularities.** DIF is a group-level, item-focused method (one flag per item across a model cohort). Min-K%, perplexity, etc. are model-level methods (one score per model-item pair). The paper reports both as \"AUROC\" in the same table (Table 3/4) but never clarifies how these fundamentally different detection granularities are made comparable. This is not a minor reporting issue -- it affects whether the comparison is valid at all.\n\n(c) **\"RL models\" conflates alignment RL with reasoning RL.** The memory.md explicitly notes that METABENCH contains 477 DPO/ORPO/KTO models but \"almost none\" true GRPO/PPO reasoning RL models. The 12 inference-added models (DeepSeek-R1 variants, QwQ-32B, etc.) are the only true reasoning RL models. Wang et al.'s ICLR 2026 result -- that GRPO conceals contamination -- specifically concerns reasoning RL, not alignment RL. The paper's framing implies robustness to the mechanism that matters (reasoning RL), but the empirical evidence is dominated by alignment RL models where the threat model is weaker.\n\n(d) **Non-significant p-value interpreted as evidence of no effect.** The paper implicitly treats the paired t-test result (p=0.62 from the best-tier framing, or equivalently the non-significant difference in the median tier) as evidence that RL does not affect DIF. This is a classic \"absence of evidence vs evidence of absence\" error. Without equivalence testing (e.g., TOST with a meaningful equivalence bound), one cannot conclude robustness.\n\n**Recommendation:** Either (i) substantially increase the RL model count to N >= 50+ with proper statistical power analysis, (ii) conduct controlled experiments where the same base model is evaluated before and after RL fine-tuning on known contaminated data, or (iii) dramatically weaken the RL-robustness claims to \"preliminary\" or \"suggestive evidence.\"\n\n#### M2. Real-data ground truth is inadequately defined, creating circular or unverifiable claims\n**Severity: Major.**\n\nThe paper reports TPR=0.58 for delta >= 1.4 on MMLU, but the ground truth definition is unclear. Specifically:\n\n(a) **What defines \"truly contaminated\" items in real data?** If MMLU-CF labels are the ground truth, then the DIF-MMLU-CF correlation (Spearman rho=0.21, Cohen's kappa=0.14) tells us that DIF and MMLU-CF largely disagree -- 696 items are flagged by DIF only, 83 by CF only, with only 47 overlapping. With kappa=0.14 (slight agreement), it is misleading to report a \"TPR\" as if there were a reliable ground truth.\n\n(b) **How are effect-size bands (delta >= 1.4, delta >= 1.0, etc.) estimated for real items?** In simulation, delta is a known parameter. In real data, the DIF effect size IS the Mantel-Haenszel delta -- so reporting \"TPR conditional on delta >= 1.4\" means \"what fraction of items with large estimated DIF effects are flagged as having DIF,\" which is partially tautological.\n\n(c) **The MMLU-CF cross-validation is weaker than presented.** MMLU-CF modifies items to remove memorization advantage but does not verify that original items WERE contaminated. The paper acknowledges this but still presents phi=0.42 (from best-tier) or rho=0.21 (from median-tier) as \"convergent validity evidence.\" The actual reported numbers (kappa=0.14) suggest the two signals share very little common variance.\n\n**Recommendation:** Clearly separate simulation results (where ground truth is known) from real-data results (where it is not). For real data, report DIF flag rates, their correlation with external signals, and sensitivity analyses -- but do not report \"TPR\" without a defensible ground truth.\n\n#### M3. Contamination-vs-capability confound is unaddressed\n**Severity: Major.**\n\nDIF detects items where the focal group (post-2024 models) performs differentially better than the reference group (pre-2024 models) after controlling for overall ability. However, the temporal cohort split spans a period of rapid, domain-specific capability improvement. Specifically:\n\n(a) The DIF flags concentrate in STEM subjects (the IFT changepoint analysis confirms this: STEM median onset 2023-03 vs Humanities 2023-09). But STEM is precisely where genuine capability improvements have been largest (code training data, math reasoning advances). The paper provides no analysis to distinguish \"this STEM item became easier because models genuinely got better at math reasoning\" from \"this STEM item became easier because it was memorized.\"\n\n(b) DIF conditions on total score (theta), but if capability improvements are domain-specific and non-uniform, the total-score conditioning is insufficient. A model that dramatically improved in math but not history would show DIF on math items even with no contamination, because its theta (estimated across all domains) underestimates its true math ability.\n\n(c) The bifactor model partially addresses this (subject-specific factors), but the DIF analysis in Claim 1 uses standard MH/ETS C with total-score stratification, not bifactor-conditioned DIF.\n\n**Recommendation:** Add a within-family analysis (e.g., Llama-2 vs Llama-3 on subjects where no contamination is suspected) to estimate the baseline DIF rate from genuine capability improvement. Alternatively, condition DIF on subject-specific ability rather than total score.\n\n#### M4. Ensemble construction is ad-hoc and likely overfit\n**Severity: Major.**\n\n(a) The weights (DIF 0.58, ConStat 0.42 in median tier) are \"optimized on a calibration set,\" but no details are provided about: what fraction of items had known contamination status, how the calibration/test split was performed, whether cross-validation was used, or whether regularization was applied.\n\n(b) The 15pp advantage of weighted fusion over 2-of-2 voting (Table 10: 0.73 vs 0.34) is unsurprising since 2-of-2 voting on two signals with 34% overlap is inherently conservative. The more informative comparison is weighted fusion (0.73) vs 1-of-2 union (0.79, FPR=0.11) -- the \"optimized\" weights actually perform WORSE on TPR than naive union, trading sensitivity for specificity. This suggests the optimization is primarily a threshold-tuning exercise, not a principled fusion.\n\n(c) FPR=0.082 is non-trivial. On 11,847 items, this produces ~970 false alarms. The paper does not discuss the operational cost of investigating or replacing nearly 1,000 incorrectly flagged items.\n\n**Recommendation:** Report cross-validated ensemble performance. Compare against uniform weights and simple union/intersection baselines. Discuss FPR in absolute numbers and operational cost.\n\n#### M5. Bifactor model fit statistics are suspiciously good, and equating claims are overstated relative to evidence\n**Severity: Moderate-to-Major.**\n\n(a) RMSEA=0.038, CFI=0.94 for a 57-factor bifactor model on 11,847 items with 4,312 \"examinees\" (models) would be exceptionally good fit in educational measurement, where typical datasets have far more examinees per item. With models that share architecture, training data, and fine-tuning lineage, local independence is severely violated -- models within the same family (Llama-2 variants, Mistral fine-tunes) are not independent observations. The paper does not discuss this assumption violation or its impact on fit statistics and equating validity.\n\n(b) The general factor explains only 41% of variance -- low for equating purposes. The paper acknowledges that 23% of subjects have unstable factor structures across cohorts, and cross-subject equating drops to rho=0.87. Yet the paper frames this as \"within-subject equating pilot\" without clearly demarcating which claims about score comparability hold and which do not.\n\n(c) The chi-square equating test (p=0.34) is used to claim score equivalence, but this is a null hypothesis significance test -- failure to reject does not demonstrate equivalence. An equivalence test (TOST) would be more appropriate. With the reported RMSE=0.047 and the sample sizes involved, this test has limited power to detect meaningful inequivalence.\n\n(d) Generated item quality metrics reveal substantial gaps: discrimination 0.93 vs 1.20, factor loading 0.38 vs 0.47, distractor effectiveness 0.61 vs 0.78. These are not minor imprecisions -- a 22% reduction in mean factor loading means the generated items are measuring something systematically different from the originals.\n\n### Minor\n\n#### m1. No confidence intervals or error bars in any table\nGiven that many results come from analyses with known sampling distributions or are amenable to bootstrap, this is a significant omission. The reader cannot assess whether differences (e.g., DIF retention 0.885 vs Min-K% retention 0.689) are statistically meaningful or within sampling noise. The one exception is the GSM8K table (Table 13 in median tier) which reports 95% CIs -- this should be standard throughout.\n\n#### m2. ConStat evaluated on only 248 items (2.1% of MMLU), DVD on 14 models and 248 items\nBoth component evaluations are orders of magnitude smaller than the DIF evaluation. The ensemble claims full-spectrum coverage but two of the three (two of two, after DVD exclusion) signals are validated on a tiny, potentially non-representative subset. How were these 248 items selected? If they were selected for having known contamination status, selection bias is a concern.\n\n#### m3. Bayesian DIF simulation uses N=80 per administration, inconsistent with the paper's own minimum\nThe paper establishes N >= 80 as the minimum for reliable DIF detection, yet the Bayesian simulation starts with N=80 per administration (single admin power = 0.33 for delta=1.0). The power doubling claim (0.33 -> 0.66 over 4 administrations) is demonstrated precisely in the regime where single-administration detection is acknowledged to be underpowered. This is presented as a feature (\"patience pays off\") but could equally be framed as \"the method needs 320 models to achieve adequate power for medium effects.\"\n\n#### m4. GSM8K cross-validation is weak evidence\nWith only 68 models (31 vs 37 per cohort), approaching the paper's own power floor, TPR=0.49, and DIF-GSM1K correlation of rho=0.22 (95% CI: [0.06, 0.37]), this experiment provides marginal evidence at best. The CI includes values so low as to be practically meaningless. The paper presents this as \"cross-benchmark validation\" but the signal is barely above noise.\n\n#### m5. Multiple comparisons across 11 experiments not addressed\nThe paper runs 11 experiments with numerous metrics. No family-wise error correction or pre-registration is mentioned. The risk of selectively reporting favorable sub-analyses is non-trivial, especially when experiments have multiple outcome metrics.\n\n#### m6. Item-Focused Trees marginal gain does not justify inclusion\nIFT provides +0.04 TPR over ETS C at the cost of 12x computation time. The 134 \"gradual contamination\" items are an interesting observation but not validated against external evidence. This experiment reads as padding rather than a meaningful contribution.\n\n#### m7. Computational reproducibility details insufficient\nWhat IRT estimation software was used? What estimation method for the bifactor model (MHRM, EM, etc.)? Were Heywood cases encountered? How were MMLU subjects with < 100 items handled in the bifactor model? What hardware was used for the 5,000+ model response matrix analysis?\n\n---\n\n## Questions for Authors\n\n1. **Ground truth protocol (Table 1):** Precisely define the ground truth used for computing TPR=0.58 on MMLU real data. If this is TPR conditional on estimated delta >= 1.4, acknowledge the tautology. If MMLU-CF labels are used, explain the kappa=0.14 disagreement.\n\n2. **AUROC comparability (Tables 3-4):** DIF produces one flag per item across a model cohort; Min-K% produces one score per model-item pair. How is AUROC computed comparably? Are you comparing item-level DIF classification against item-level aggregation of model-level scores?\n\n3. **Contamination vs capability:** What is the DIF flag rate on MMLU subjects where contamination is least plausible (e.g., niche humanities topics unlikely to appear in training data)? If the flag rate is substantial, this suggests architecture-driven or capability-driven DIF dominates.\n\n4. **Local independence violation:** Models within the same family share substantial training data. How does this affect IRT parameter estimation and bifactor model fit? Have you tried restricting to one model per family?\n\n5. **Ensemble calibration details:** What fraction of MMLU items have known contamination status? How was the calibration/test split performed? What is the cross-validated ensemble TPR?\n\n6. **RL model selection:** Were the 12 inference-added RL models selected to maximize diversity, or were they simply all available open-weight reasoning-RL models? Is there selection bias toward models with known contamination?\n\n7. **Equating with imperfect items:** The generated items have systematically lower discrimination and factor loadings. How does this asymmetric quality gap affect the equating -- does it systematically bias scores in one direction?\n\n---\n\n## Minor Issues\n\n- The paper title is long. Consider shortening.\n- \"Self-healing benchmark\" framing (if used) is overclaimed given the 15% replacement ceiling and quality gaps in generated items.\n- The DVD failure analysis belongs in the main paper, not appendix -- it is one of the more informative results.\n- Several claims reference simulation results that closely match the real-data findings; this alignment should be discussed more carefully (either as validation of simulation fidelity or as a red flag for circularity).\n\n---\n\n## Preliminary Score: 3/6 (Weak Reject)\n\n### Justification\n\nThe paper addresses an important problem (benchmark contamination in the era of RL training) with a genuinely insightful cross-disciplinary approach (applying DIF from psychometrics). The experimental breadth is commendable, and several components (DVD failure analysis, student simulation calibration, graceful degradation bounds) provide standalone value.\n\nHowever, the paper's central claim -- RL-robustness -- rests on critically underpowered evidence (n=35 RL models, with only ~12 true reasoning-RL models). The real-data ground truth is inadequately defined, making headline TPR numbers unverifiable. The contamination-vs-capability confound -- the most obvious alternative explanation for temporal DIF in STEM items -- is completely unaddressed. The ensemble construction lacks rigor, and the equating pilot reveals quality gaps (factor loading 0.38 vs 0.47) that the framing does not sufficiently acknowledge.\n\nAt a venue with ~25% acceptance rate, I would expect the central claim to be well-supported. Here, the most important claim (RL-robustness) has the weakest evidence, and three major methodological issues (M1-M3) are individually sufficient to question the paper's conclusions. With significant revisions addressing the RL sample size, ground truth definition, and confound analysis, this could become a strong paper. In its current form, it is below the acceptance threshold.\n\n### What would change my score:\n- **To 4 (Weak Accept):** Address M1 (expand RL validation to N >= 50 with power analysis or controlled before/after RL experiments), clarify M2 (separate simulation from real-data claims), and add M3 confound analysis (within-family comparison).\n- **To 5 (Accept):** Additionally address M4 (cross-validated ensemble) and M5 (equivalence testing for equating).\n\n### Confidence: 4/5\nI am familiar with both the DIF/IRT literature and the LLM contamination detection literature. My main uncertainty is whether the real experimental numbers (vs the imagined median-tier numbers I am evaluating) might be stronger, particularly on the RL-robustness front.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84305b4e-7918-4eba-8466-07dffecaff94",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbESRQxmSzaHRmS9QiA6S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1853eba9-820c-4147-9b50-36da7db2c870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lg6j1oCu3pG8pwg282ohUu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 97361,
      "output_tokens": 5384,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 764
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5384,
          "cache_read_input_tokens": 97361,
          "cache_creation_input_tokens": 764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 764,
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

_source line 47 · 2026-05-20T20:21:07.128Z_

<details><summary>↩ Tool result · `toolu_01B4yPyGBY5MUirzztkrJ75a`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/review_report.md\", \"dream_id\": \"dream_20260520T194223\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1853eba9-820c-4147-9b50-36da7db2c870",
  "isSidechain": true,
  "promptId": "965db6da-1324-4e46-b4b1-833299b25da5",
  "agentId": "aa8862df758a50e99",
  "type": "user",
  "uuid": "f5fe4cdc-a646-41a3-97ea-a9885ac7c5c4",
  "sourceToolAssistantUUID": "1853eba9-820c-4147-9b50-36da7db2c870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-20T20:21:24.117Z_

Review submitted. Here is the summary:

---

**Score: 3/6 (Weak Reject) | Confidence: 4/5**

**Key findings from my R1 (Methods + Experiments) review:**

**Strengths:**
- The DIF reframing of benchmark contamination is a genuinely insightful cross-disciplinary contribution
- Sound psychometric methodology choices (ETS C over p-value testing, 2PL IRT, effect-size thresholds)
- Honest DVD failure mode analysis and principled 3-signal to 2-signal downgrade
- Student simulation calibration comparison is a valuable standalone result
- Graceful degradation framework provides actionable operational bounds (15% max replacement)

**Major Weaknesses (5 issues, each individually significant):**

1. **M1 -- RL-robustness critically underpowered.** Only n=35 RL models (and only ~12 true reasoning-RL models), making the paper's headline claim its weakest point. No equivalence testing, no power analysis for the retention ratio, and AUROC comparability between group-level DIF and model-level traditional methods is never explained.

2. **M2 -- Real-data ground truth undefined.** TPR=0.58 is reported on MMLU but ground truth is unclear. MMLU-CF agreement is only kappa=0.14 (slight). Reporting "TPR conditional on estimated delta >= 1.4" is partially tautological since delta IS the DIF statistic.

3. **M3 -- Contamination-vs-capability confound unaddressed.** DIF flags concentrate in STEM subjects, exactly where genuine capability improvements are largest. Total-score conditioning is insufficient when improvements are domain-specific. No within-family analysis provided.

4. **M4 -- Ensemble construction ad-hoc.** No cross-validation reported. Optimized weights (0.58/0.42) actually underperform naive union on TPR. FPR=0.082 produces ~970 false alarms on 11,847 items -- operational cost not discussed.

5. **M5 -- Equating quality gaps underacknowledged.** Generated items show 22% lower factor loadings (0.38 vs 0.47), 22% lower discrimination (0.93 vs 1.20). Cross-subject equating drops to rho=0.87 with 23% unstable subjects. Chi-square equivalence test (p=0.34) is null-result reasoning, not equivalence evidence.

**Path to acceptance:** Expand RL validation (N >= 50+, or controlled before/after experiments), separate simulation from real-data TPR claims, add contamination-vs-capability confound analysis, cross-validate ensemble, and use equivalence testing for equating.

The report was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T194223/median/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5fe4cdc-a646-41a3-97ea-a9885ac7c5c4",
  "isSidechain": true,
  "agentId": "aa8862df758a50e99",
  "requestId": "req_011CbEScGYK6URw6sciaKN9m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11aece7d-db64-47a9-b9e6-f301f4808654",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "76f689bc-835b-4f00-b32c-50d6308bc7dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TjmCFhSLb2wm5DLxQwRSxG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5518,
      "cache_read_input_tokens": 98125,
      "output_tokens": 712,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5518
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 712,
          "cache_read_input_tokens": 98125,
          "cache_creation_input_tokens": 5518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5518,
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
