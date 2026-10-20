# Research conversation: You are Reviewer 1 (R1) for a blind peer review of an academic paper submitted to AAAI 2027. Your focus areas are **Meth

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-adeeb26d08149eca7.jsonl`
- **Structured JSON:** [`b229ae8414e3ea0912e7.json`](../../sessions/b2/b229ae8414e3ea0912e7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

50 recorded events

### User

_source line 1 · 2026-05-14T18:43:17.433Z_

You are Reviewer 1 (R1) for a blind peer review of an academic paper submitted to AAAI 2027. Your focus areas are **Methods and Experiments**.

## AAAI Review Criteria
AAAI uses a 1-10 overall assessment scale. Acceptance rate ~23%. Dimensions: soundness, significance, novelty, clarity, relevance. The review form asks for a paper summary, strengths, weaknesses, questions for authors, and an overall score.

Scale:
- 10: Top 5%, seminal
- 9: Strong accept
- 8: Clear accept
- 7: Accept, good paper with minor weaknesses
- 6: Weak accept / borderline
- 5: Borderline / weak reject
- 4: Reject, below threshold
- 3: Clear reject
- 2: Strong reject
- 1: Trivial or wrong

## Paper Summary

**Title**: "Distributional Fingerprints of Generation Depth: Detecting Recursive LLM Contamination Beyond Binary Classification"

The paper introduces "distributional fingerprinting" for estimating the generation depth of text (gen-0/gen-1/gen-2+) by measuring distributional divergence from human text under a small reference LM. It tests two hypotheses about non-paraphrastic generation chains: convergence (H1) vs monotonic divergence (H2), confirming H2. A 7-feature classifier (5 reference-model entropy features + 2 surface features) with XGBoost achieves macro-F1=0.87 (3-class) and generalizes across 5 generators (leave-one-out F1=0.78). Depth-aware data filtering retains 42% data at near-human perplexity, outperforming binary baselines by 5.2%.

## Key Results (from paper)
- Table 1: Feature ablation — ref-only F1=0.79, surface-only F1=0.63, full F1=0.87, delta=+0.16
- Table 2: Permutation importance — entropy_mean=0.28 (top), hapax_ratio drops from 0.30 XGB gain to 0.14 permutation
- Table 3: Leave-one-generator-out — mean F1=0.78±0.03 across 5 generators
- Table 4: Per-generator in-distribution — pooled F1=0.86
- Table 5: Cross-reference models — Pythia-410M F1=0.86, OLMo-2-1B F1=0.76, Qwen3.5-0.8B F1=0.74, ensemble F1=0.88
- Table 6: Paraphrastic vs continuation — continuation F1=0.85, paraphrastic F1=0.58, KS D=0.41 p<1e-4
- Table 7-8: Downstream utility — depth-filtered PPL=29.0, binary baselines PPL=31.8-32.1, human PPL=28.3
- Table 9: Prompt types — continuation F1=0.85, elaboration F1=0.80, inspired_rewriting F1=0.72, drift rate correlation ρ=0.91
- Table 10: Cross-model chains — F1=0.75, 10-point drop from single-model
- Table 11: Multi-domain — Wikipedia F1=0.86, News F1=0.83, Scientific F1=0.81, Creative F1=0.78, leave-one-out F1=0.77
- Table 12: 5-class ordinal — macro-F1=0.62, Spearman ρ=0.83, MAE=0.58
- Table 13: Robustness — 5% edit F1=0.83, 10% F1=0.78, 20% F1=0.67
- Table 14: LD-Score integration — marginal +0.01
- Table 15: Neural baseline — XGBoost F1=0.86/0.78 (in/cross), QLoRA F1=0.83/0.71, XGBoost 3min vs 12 GPU·h

## Experiment Design Reference (what was planned)
The full experiment plan includes 12 experiments:
1. feature_ablation (plan_001) — covered in paper
2. cross_generator_evaluation (plan_002) — covered
3. cross_family_reference_model (plan_003) — covered
4. downstream_utility (plan_004) — covered
5. prompt_type_comparison (plan_005) — covered
6. paraphrastic_comparison (plan_006) — covered
7. cross_model_chains (plan_007) — covered
8. multi_domain_seeds (plan_008) — covered
9. finer_grained_ordinal (plan_009) — covered
10. human_edit_robustness (plan_010) — covered
11. ld_score_feature (plan_011) — covered
12. end_to_end_classifier (plan_012) — covered

All 12 planned experiments appear in the paper.

## Your Task (R1: Methods + Experiments)

Provide a detailed review focusing on:

1. **Methodological Soundness**: Are the methods technically correct? Are the experimental designs valid? Are there confounds or methodological issues?
2. **Experimental Rigor**: Are the experiments comprehensive? Are baselines appropriate? Are statistical tests used correctly? Is there proper cross-validation?
3. **Reproducibility**: Is there enough detail to reproduce the results?
4. **Specific Technical Concerns**: Any issues with feature design, classifier choice, evaluation metrics, etc.
5. **Missing Experiments or Baselines**: What's not covered that should be?

Format your review as:

### Paper Summary (2-3 sentences)
### Strengths (bulleted)
### Weaknesses (bulleted)
### Questions for Authors (bulleted)
### Missing Experiments/Concerns
### Scores
- Soundness: X/10
- Experimental Rigor: X/10
- Reproducibility: X/10
- Overall (Methods+Experiments focus): X/10
- Confidence: X/5


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "291b2db2-0ea1-4faa-8602-53757c603b28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T18:43:17.437Z_

```json
{
  "parentUuid": "291b2db2-0ea1-4faa-8602-53757c603b28",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
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
  "uuid": "dff2f9bb-f048-45c5-b2ea-1ea0436cb9ca",
  "timestamp": "2026-05-14T18:43:17.437Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T18:43:20.612Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dff2f9bb-f048-45c5-b2ea-1ea0436cb9ca",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xJ6THkEV9C8rZwuabk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "429338da-e0a9-47f7-ac4f-6c6e9a3a1fc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfyXjVgrkFEyGK5bjdi7cD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15560,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15560,
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

_source line 4 · 2026-05-14T18:43:20.940Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018wNPz6cFSLPUCUYTtw1YGS`</summary>

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
  "parentUuid": "429338da-e0a9-47f7-ac4f-6c6e9a3a1fc1",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xJ6THkEV9C8rZwuabk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "444f9d03-6744-4f1a-88ff-492050f76b50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfyXjVgrkFEyGK5bjdi7cD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15560,
      "cache_read_input_tokens": 0,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15560
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 124,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15560,
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

_source line 5 · 2026-05-14T18:43:20.944Z_

<details><summary>↩ Tool result · `toolu_018wNPz6cFSLPUCUYTtw1YGS`</summary>

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
  "parentUuid": "444f9d03-6744-4f1a-88ff-492050f76b50",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "3a562832-237e-4c0c-b701-cd9b906399e9",
  "sourceToolAssistantUUID": "444f9d03-6744-4f1a-88ff-492050f76b50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T18:43:23.664Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01D6MnrjPL24GhFf2rbvGVX2`</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a562832-237e-4c0c-b701-cd9b906399e9",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xJMccFLV69D8pxZc7e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81db90bb-21f9-43d5-a665-1caebdca73be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MK3VDa6aofFTa5EAc3smz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 7 · 2026-05-14T18:43:23.695Z_

<details><summary>↩ Tool result · `toolu_01D6MnrjPL24GhFf2rbvGVX2`</summary>

```text
{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (6 个)\n\n- **plan-001**: ALLOCATED — \n- **mvp-001**: DONE (success) — \n- **mvp-001-gen-s0**: PREPARING — \n- **mvp-001-gen-s3**: PREPARING (failed) — \n- **mvp-001-gen-s2**: PREPARING (failed) — \n- **mvp-001-gen-s1**: PREPARING (failed) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan-001: Feature ablation: 模型级特征（entropy系列+tail_decay）独立于表面特征仍能区分生成深度；H1/H2趋势分析确认特征随depth的变化模式；perplexity随depth显著变化（已分配 ? GPU:?，等待提交）\n- mvp-001-gen-s0（准备中）\n- mvp-001-gen-s3（准备中）\n- mvp-001-gen-s2（准备中）\n- mvp-001-gen-s1（准备中）\n\n## 近期结论\n- **mvp-001** (success): Pythia-410M 参考模型的分布特征（entropy stats, tail-decay, TTR, hapax）能区分 Pythia-2.8B continuation 链的 gen-0/gen-1/gen-2+，3-class macro-F1 ≥ 0.45\n  [MVP Results](/api/workspace-files/projects/gen-depth-fingerprint/artifacts/mvp-001/data/mvp_results_pointer.txt) | [MVP-001 Results](autodl-5090:/root/gen-depth-fingerprint/results/mvp_results.json)\n\n## 趋势\n成功 1 / 负向 0 / 失败 0 / 共 1\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81db90bb-21f9-43d5-a665-1caebdca73be",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "34ff6ec9-57a9-423f-aa29-1935951395fd",
  "sourceToolAssistantUUID": "81db90bb-21f9-43d5-a665-1caebdca73be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T18:43:24.220Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014WQPbwXBoq6dxrTm7GkmqZ`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34ff6ec9-57a9-423f-aa29-1935951395fd",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xJMccFLV69D8pxZc7e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b163e1c-7c4c-411e-8ca0-f5e75dcdaadf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MK3VDa6aofFTa5EAc3smz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15560,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1446
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 162,
          "cache_read_input_tokens": 15560,
          "cache_creation_input_tokens": 1446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1446,
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

_source line 9 · 2026-05-14T18:43:24.228Z_

<details><summary>↩ Tool result · `toolu_014WQPbwXBoq6dxrTm7GkmqZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- plan-001: Feature ablation: 模型级特征（entropy系列+tail_decay）独立于表面特征仍能区分生成深度；H1/H2趋势分析确认特征随depth的变化模式；perplexity随depth显著变化（已分配 ? GPU:?，等待提交）\\n- mvp-001-gen-s0（准备中）\\n- mvp-001-gen-s3（准备中）\\n- mvp-001-gen-s2（准备中）\\n- mvp-001-gen-s1（准备中）\\n\\n## 近期结论\\n- **mvp-001** (success): Pythia-410M 参考模型的分布特征（entropy stats, tail-decay, TTR, hapax）能区分 Pythia-2.8B continuation 链的 gen-0/gen-1/gen-2+，3-class macro-F1 ≥ 0.45\\n  [MVP Results](/api/workspace-files/projects/gen-depth-fingerprint/artifacts/mvp-001/data/mvp_results_pointer.txt) | [MVP-001 Results](autodl-5090:/root/gen-depth-fingerprint/results/mvp_results.json)\\n\\n## 趋势\\n成功 1 / 负向 0 / 失败 0 / 共 1\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 810, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b163e1c-7c4c-411e-8ca0-f5e75dcdaadf",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "01a8afef-beee-4a46-aa6f-9e725d279c81",
  "sourceToolAssistantUUID": "8b163e1c-7c4c-411e-8ca0-f5e75dcdaadf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T18:43:27.358Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017R1TQpjpYfdddTBzoiaj5h`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01a8afef-beee-4a46-aa6f-9e725d279c81",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xJbeTcB1Dvgekqpp7C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9db6f1fd-5684-46aa-a523-414ee4bef4ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qp4ScKvqmdgbSjowgna1G6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1515,
      "cache_read_input_tokens": 17006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1515,
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

_source line 11 · 2026-05-14T18:43:27.364Z_

<details><summary>↩ Tool result · `toolu_017R1TQpjpYfdddTBzoiaj5h`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9db6f1fd-5684-46aa-a523-414ee4bef4ae",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "1cb3f247-4ccf-458a-96fa-7db9e8354c05",
  "sourceToolAssistantUUID": "9db6f1fd-5684-46aa-a523-414ee4bef4ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T18:43:28.379Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012G3KrPuNbug3yChGEHuMW4`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cb3f247-4ccf-458a-96fa-7db9e8354c05",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xJbeTcB1Dvgekqpp7C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5e7d3e1-b380-4ebc-8c75-cf58fb569294",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qp4ScKvqmdgbSjowgna1G6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1515,
      "cache_read_input_tokens": 17006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1515,
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

_source line 13 · 2026-05-14T18:43:28.386Z_

<details><summary>↩ Tool result · `toolu_012G3KrPuNbug3yChGEHuMW4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ROADMAP.md\", \"content\": \"# gen-depth-fingerprint — Research Dashboard\\n\\n> 最后更新: 2026-05-14 18:12 UTC | 更新原因: Post-MVP: research 阶段启动，引用 paper_framing.md + experiment_plan.yaml\\n\\n## 核心方向\\n估计文本的\\\"生成深度\\\"（gen-0 / gen-1 / gen-2+），实现风险分层数据治理。非释义生成链打破 attractor 收敛约束，分布漂移随深度累积，留下可检测的\\\"分布指纹\\\"。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-14 通过，macro-F1=0.84，binary-F1=0.87）\\n- **服务器**: autodl-5090 (4× RTX 5090 32GB)\\n- **Venue**: AAAI 2027 (DDL Aug 2) primary / EMNLP 2026 ARR (May 25) stretch\\n- **Dream**: dream_20260514T181213 pending（full review mode）\\n- **覆盖率**: MVP 验证了 Claim 1 单生成器场景；Claim 2/3 待验证\\n\\n## Core Claims (from paper_framing.md)\\n1. **Depth Discriminability** — 分布特征能跨生成器区分 gen-0/gen-1/gen-2+\\n2. **Distributional Fingerprint Independence** — 参考模型特征独立于表面词汇统计\\n3. **Downstream Utility** — 深度感知过滤优于二分类过滤\\n\\n## 实验计划 (from experiment_plan.yaml)\\n| ID | Name | Claim | Pri | GPU·h | Status |\\n|----|------|-------|-----|-------|--------|\\n| mvp-001 | mvp_validation | 1 | — | 3 | ✅ DONE |\\n| plan_001 | feature_ablation | 2 | P0 | 1 | pending |\\n| plan_002 | cross_generator_evaluation | 1 | P0 | 20 | pending |\\n| plan_003 | cross_family_reference_model | 1 | P0 | 8 | pending |\\n| plan_004 | downstream_utility | 3 | P0 | 15 | pending |\\n| plan_005 | prompt_type_comparison | 1 | P1 | 10 | pending |\\n| plan_006 | paraphrastic_comparison | 1 | P1 | 8 | pending |\\n| plan_007 | cross_model_chains | 1 | P1 | 12 | pending |\\n| plan_008 | multi_domain_seeds | 1 | P1 | 10 | pending |\\n| plan_009-012 | P2 experiments | 1,2 | P2 | 23 | pending |\\n\\n**GPU 预算**: P0 ~44h / P1 ~40h / P2 ~23h / Total ~107h (≤200h budget)\\n\\n## 近期任务\\n- [ ] 等待 Dream 回调 → 分析审稿反馈 → 决定是否调整 framing/plan\\n- [ ] Dream 通过后：批准 plan_001 (feature_ablation) — 用现有 MVP 数据，无需新 generation\\n- [ ] plan_001 结果确认 Claim 2 后：批准 plan_002 (cross_generator，需下载 4 个新模型)\\n\\n## GPU 预算\\n本项目分配: autodl-5090 4× RTX 5090 (32GB)\\n已用: ~3 GPU·h (MVP generation + feature extraction)\\n剩余: ~197 GPU·h\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D004 | 2026-05-14 | Claim 2 framing 调整：从 \\\"Fingerprint Independence\\\" 转为 | plan_001 |\\n| D003 | 2026-05-14 | Claim 2 准备 Plan B framing：若 ablation 显示表面特征足够，叙事从  | — |\\n| D002 | 2026-05-14 | MVP PASS → 进入研究阶段。首要任务：特征 ablation + depth signal  | mvp-001 |\\n| D001 | 2026-05-14 | MVP 方案：Pythia-2.8B continuation 链 + Pythia-410M 参考 | — |\\n\\n\", \"total_chars\": 2298, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5e7d3e1-b380-4ebc-8c75-cf58fb569294",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "56d227f0-3220-429b-a79b-fe641d5080ec",
  "sourceToolAssistantUUID": "e5e7d3e1-b380-4ebc-8c75-cf58fb569294",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T18:43:28.822Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HtcfJzo7VHDnRb3tqBvmgZ`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56d227f0-3220-429b-a79b-fe641d5080ec",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xJbeTcB1Dvgekqpp7C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68161f2d-4c1f-47f6-b79f-e02124f1af1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qp4ScKvqmdgbSjowgna1G6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1515,
      "cache_read_input_tokens": 17006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1515,
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

_source line 15 · 2026-05-14T18:43:28.828Z_

<details><summary>↩ Tool result · `toolu_01HtcfJzo7VHDnRb3tqBvmgZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/memory.md\", \"content\": \"# gen-depth-fingerprint — Memory\\n\\n## 关键发现\\n\\n### MVP-001 结果（2026-05-14）\\n- **PASS**: macro-F1=0.8408 (阈值 0.45), binary F1=0.8653 (阈值 0.65)\\n- 词汇多样性特征（hapax_ratio, ttr）区分力最强，feature importance 分别 0.30 和 0.17\\n- entropy_mean 是最强的模型级特征（importance 0.22）\\n- tail_decay 区分力最弱（importance 0.057），但仍统计显著\\n- gen-0 几乎完美分离（F1=0.95），gen-1 vs gen-2+ 有一定混淆（45 个 gen-2+ 误判为 gen-1）\\n- 深度衰减 17.4%：部分 continuation 产生空文本导致链条中断（995→822 from depth 0→4）\\n- **洞察**：表面特征（hapax/ttr）可能过于强势，掩盖了模型级特征的真实区分力。后续实验应考虑：(a) 只用模型级特征的 ablation (b) 跨模型泛化测试\\n\\n## 经验教训\\n\\n### submit_training_job + CUDA_VISIBLE_DEVICES 映射（2026-05-14）\\n`submit_training_job` 自动注入 `CUDA_VISIBLE_DEVICES=N`（物理卡号）。注入后进程只看到 1 张卡，脚本内必须用 `--device cuda:0`（逻辑设备 0），不能用 `cuda:N`。否则 shard 1/2/3 会报 \\\"CUDA device ordinal out of range\\\"。\\n\\n### AutoDL 网络 + 数据源（2026-05-14）\\nWikipedia 数据集在 AutoDL 上流式加载失败。解决方案：预下载到本地 JSONL（`wiki_seed_1000.jsonl`），脚本用 `--input` 参数读本地文件。ModelScope 下载 HF 模型时路径名会转换（如 `pythia-2.8b` → `pythia-2___8b`）。\\n\\n### nohup vs submit_training_job（2026-05-14）\\nWorker 用 nohup 提交后台任务会导致 orphan 进程（无监控、无回调）。必须用 `submit_training_job`（tmux + cron 自动监控）。\\n\\n### 生成参数敏感性（2026-05-14）\\ntemperature=0.7/top_p=0.9（IDEA_BRIEF 规定）。不能用 temp=1.0——高温度使生成文本更随机、分类更容易，MVP 通过不能证明假设。\\n\\n## 决策记录\\n\\n### MVP 生成参数（2026-05-14，Director 指定）\\n- temperature=0.7, top_p=0.9, max_new_tokens=256, do_sample=True, seed=42\\n- 种子数据：wiki_seed_1000.jsonl（1000 条 Wikipedia，本地预下载）\\n- 判定标准：二值 PASS/FAIL（无 MARGINAL），macro-F1 ≥ 0.45 AND binary F1 ≥ 0.65\\n\", \"total_chars\": 1434, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68161f2d-4c1f-47f6-b79f-e02124f1af1b",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "c64a430e-afb1-4dd8-af4e-74ea21f195c7",
  "sourceToolAssistantUUID": "68161f2d-4c1f-47f6-b79f-e02124f1af1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T18:43:29.348Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DMnPS9H6pTte9BzX7hZGRa`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c64a430e-afb1-4dd8-af4e-74ea21f195c7",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xJbeTcB1Dvgekqpp7C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "354633c3-7503-47ba-932c-d361a38d9b0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qp4ScKvqmdgbSjowgna1G6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1515,
      "cache_read_input_tokens": 17006,
      "output_tokens": 382,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1515
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 382,
          "cache_read_input_tokens": 17006,
          "cache_creation_input_tokens": 1515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1515,
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

_source line 17 · 2026-05-14T18:43:29.355Z_

<details><summary>↩ Tool result · `toolu_01DMnPS9H6pTte9BzX7hZGRa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-fingerprint\\n\\n## Target Venue\\n- Primary: AAAI 2027 (deadline: August 2, 2026)\\n- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4\\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\\n\\n## Core Insight\\nNon-paraphrastic LLM generation chains exhibit **feature-dependent depth dynamics**: vocabulary/surface features (TTR, hapax ratio) and aggregate entropy drift monotonically with depth (H₂), while distributional shape features (tail decay, entropy variance) remain near-stationary (H₁). This dual pattern — surface impoverishment + stable distributional shape — creates a rich, complementary feature space for depth estimation. The combination of surface and reference-model features significantly outperforms either alone (macro-F1 0.82 vs 0.76/0.72), enabling risk-stratified data curation beyond binary real/synthetic filtering.\\n\\n## Core Claims (3 条，均可证伪)\\n\\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).\\n\\n**Claim 2 — Feature Complementarity & Dual Dynamics**: Surface features (vocabulary impoverishment) and reference-model features (distributional shape) capture **different aspects** of depth-dependent signal. Neither alone matches the full feature set (ablation: full 0.82 > surface 0.76 > reference 0.72, p<0.001 for full vs surface). Moreover, these two feature families exhibit distinct depth dynamics: surface features drift monotonically (H₂), while distributional shape features remain stationary (H₁) — revealing that recursive generation simultaneously impoverishes vocabulary and preserves distributional structure.\\n\\n**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.\\n\\n## Story Spine\\n\\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\\n\\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.\\n\\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing a **dual dynamics** pattern: vocabulary features drift monotonically with depth (supporting H₂) while distributional shape features remain stationary (supporting H₁). This is not H₁-vs-H₂ — both coexist in different feature families, suggesting distinct mechanisms: vocabulary impoverishment accumulates via mode collapse in the lexical space, while the reference model's token-level probability structure is robust to recursive generation. This dual pattern is practically useful: combining both feature types yields significantly better depth estimation than either alone, enabling risk-stratified data curation.\\n\\n**Headline result template**: \\\"On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines.\\\"\\n\\n## Anticipated Reviewer Concerns\\n\\n**RC1 — \\\"Is this just vocabulary impoverishment?\\\"**: Surface features alone achieve 0.76 macro-F1, but full features achieve 0.82 (p<0.001). We don't claim reference features are \\\"better\\\" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting vocabulary). The dual dynamics finding is itself a scientific contribution.\\n\\n**RC2 — \\\"Does this generalize beyond Pythia?\\\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\\n\\n**RC3 — \\\"Is 3-class sufficient? Why not finer-grained?\\\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\\n\\n**RC4 — \\\"How realistic are single-model chains?\\\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\\n\\n**RC5 — \\\"What about human editing / post-processing?\\\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\\n\\n**RC6 — \\\"Ecological validity — continuation vs real web content\\\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\\n\\n## Venue Fit\\n- AAAI 2027: Strong fit — data governance + ML methodology. The dual dynamics (H₁+H₂ coexistence) finding positions it as empirical science with theoretical insight, not just a classifier paper.\\n- EMNLP 2026: Excellent fit — directly addresses special theme \\\"New Missions for NLP Research\\\" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work.\\n\", \"total_chars\": 5969, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "354633c3-7503-47ba-932c-d361a38d9b0c",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "e2561570-7c6a-4f9b-8587-fd7e0b516205",
  "sourceToolAssistantUUID": "354633c3-7503-47ba-932c-d361a38d9b0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-14T18:43:33.575Z_

Now let me read the actual paper and experiment plan files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2561570-7c6a-4f9b-8587-fd7e0b516205",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xK13syLi2QWf8k6nHs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c546b36-d640-4159-b0e8-1b4fcbdd7191",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwDibqGmsXUgSUBQMxSaeh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4712,
      "cache_read_input_tokens": 18521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4712,
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

_source line 19 · 2026-05-14T18:43:34.046Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PW8wKFLLP4GDWWYTywns9a`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c546b36-d640-4159-b0e8-1b4fcbdd7191",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xK13syLi2QWf8k6nHs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94699955-51a8-442d-a49b-2d6a184a7b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwDibqGmsXUgSUBQMxSaeh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4712,
      "cache_read_input_tokens": 18521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4712,
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

_source line 20 · 2026-05-14T18:43:34.062Z_

<details><summary>↩ Tool result · `toolu_01PW8wKFLLP4GDWWYTywns9a`</summary>

```text
artifacts/dream_reports/dream_20260514T181213/best/paper.tex
artifacts/dream_reports/dream_20260514T181213/median/paper.tex
artifacts/dream_reports/dream_20260514T181213/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94699955-51a8-442d-a49b-2d6a184a7b9e",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "9d077410-d0d6-4c85-ae66-e22090c9f6ca",
  "sourceToolAssistantUUID": "94699955-51a8-442d-a49b-2d6a184a7b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T18:43:34.498Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01AdMz79nLw3SQS2EBu8Stfj`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d077410-d0d6-4c85-ae66-e22090c9f6ca",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xK13syLi2QWf8k6nHs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7f02012-b09d-4303-a1e6-ce4f4e912170",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwDibqGmsXUgSUBQMxSaeh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4712,
      "cache_read_input_tokens": 18521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4712,
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

_source line 22 · 2026-05-14T18:43:34.506Z_

<details><summary>↩ Tool result · `toolu_01AdMz79nLw3SQS2EBu8Stfj`</summary>

```text
artifacts/manifest.yaml
experiment_plan.yaml
registry.yaml
artifacts/dream_reports/dream_20260514T181213/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T181213/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T181213/worst/imagined_experiments.yaml
decisions.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260514T181213/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7f02012-b09d-4303-a1e6-ce4f4e912170",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "49f803f7-8734-409c-88ac-6f5157d62370",
  "sourceToolAssistantUUID": "f7f02012-b09d-4303-a1e6-ce4f4e912170",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T18:43:35.026Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014uRFZRki7Hr9meGvEbPmTW`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49f803f7-8734-409c-88ac-6f5157d62370",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xK13syLi2QWf8k6nHs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d78457df-0028-49ca-aea0-a5bbaad8c707",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwDibqGmsXUgSUBQMxSaeh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4712,
      "cache_read_input_tokens": 18521,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4712
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 18521,
          "cache_creation_input_tokens": 4712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4712,
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

_source line 24 · 2026-05-14T18:43:35.038Z_

<details><summary>↩ Tool result · `toolu_014uRFZRki7Hr9meGvEbPmTW`</summary>

```text
artifacts/_project/data/generate_chain.py
artifacts/generate_chain.py
artifacts/ablation_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d78457df-0028-49ca-aea0-a5bbaad8c707",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "d24facb1-66ac-4579-84eb-3153ba77f6be",
  "sourceToolAssistantUUID": "d78457df-0028-49ca-aea0-a5bbaad8c707",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T18:43:37.707Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CvmY5nmZm49owx8ktKCru6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d24facb1-66ac-4579-84eb-3153ba77f6be",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xKPrL9Nuz2o4hh8zjS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e873af61-26e3-40a0-a75f-24085d3f358d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JJo6CHvT4YXySNnYBNqJWc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 671,
      "cache_read_input_tokens": 23233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 671,
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

_source line 26 · 2026-05-14T18:43:37.962Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RmPiHEGSxo7waj6WwJUZKP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e873af61-26e3-40a0-a75f-24085d3f358d",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xKPrL9Nuz2o4hh8zjS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24b2fc51-ce56-4e9f-baff-dfe753289eee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JJo6CHvT4YXySNnYBNqJWc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 671,
      "cache_read_input_tokens": 23233,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 671
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 23233,
          "cache_creation_input_tokens": 671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 671,
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

_source line 27 · 2026-05-14T18:43:37.966Z_

<details><summary>↩ Tool result · `toolu_01RmPiHEGSxo7waj6WwJUZKP`</summary>

```text
1	experiments:
2	  # === P0: Must-run experiments (headline results) ===
3	
4	  - id: plan_001
5	    claim: 2
6	    name: feature_ablation_and_trend
7	    description: >
8	      Three-part analysis on existing MVP data (zero new generation):
9	      (A) Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)
10	      vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold CV for each.
11	      (B) H1/H2 trend analysis: plot each feature's mean ± std across depth 0-4. Monotonic trend → H2 (divergence);
12	      plateau → H1 (convergence). Fit linear regression per feature, report slope + R².
13	      (C) Perplexity pre-validation for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets
14	      (no fine-tuning, just forward pass). If perplexity varies significantly with depth → Claim 3 signal exists.
15	    priority: P0
16	    gpu_budget_hours: 1
17	    deps: [mvp-001]
18	    notes: >
19	      Uses existing MVP data + features.csv. Critical for Claim 2.
20	      Plan B if surface-only ≈ full: reframe Claim 2 as "complementary signal" instead of "independent signal",
21	      narrative shifts to "vocabulary impoverishment as primary depth signal".
22	
23	  - id: plan_002
24	    claim: 1
25	    name: cross_generator_evaluation
26	    description: >
27	      Expand to 5 generators (Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, Pythia-1B).
28	      Leave-one-generator-out CV to test cross-generator generalization.
29	      1000 seeds × 5 generators × 5 depths = 25K chains.
30	    priority: P0
31	    gpu_budget_hours: 20
32	    deps: [plan_001]
33	    notes: >
34	      Only proceed if plan_001 confirms reference features have independent or complementary value.
35	      Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out evaluation in analysis.
36	      Discuss limitation in paper if Pythia holdout performance inflated by Pythia-1B in training set.
37	
38	  - id: plan_003
39	    claim: 1
40	    name: cross_family_reference_model
41	    description: >
42	      Test non-Pythia reference models (OLMo-2-1B, Qwen3.5-0.8B) for feature extraction.
43	      Addresses RC2 — verifies signal isn't architecture-specific artifact.
44	    priority: P0
45	    gpu_budget_hours: 8
46	    deps: [plan_002]
47	
48	  - id: plan_004
49	    claim: 3
50	    name: downstream_utility
51	    description: >
52	      RQ4: Fine-tune a small LM (Pythia-410M or OLMo-1B) on depth-stratified data subsets.
53	      Measure perplexity degradation on held-out test set as function of training data depth.
54	      Compare depth-aware filtering vs binary baselines (FastDetectGPT, LD-Score threshold).
55	    priority: P0
56	    gpu_budget_hours: 15
57	    deps: [plan_002]
58	
59	  # === P1: Important for story completeness ===
60	
61	  - id: plan_005
62	    claim: 1
63	    name: prompt_type_comparison
64	    description: >
65	      RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting chains.
66	      Tests whether semantic divergence from source correlates with depth signal preservation.
67	      Same 1000 seeds, Pythia-2.8B, 3 prompt types.
68	    priority: P1
69	    gpu_budget_hours: 10
70	    deps: [plan_001]
71	
72	  - id: plan_006
73	    claim: 1
74	    name: paraphrastic_comparison
75	    description: >
76	      RQ2 full: Construct parallel paraphrasing chains for direct comparison with continuation chains.
77	      Tests attractor convergence theory — do non-paraphrastic chains preserve more depth signal?
78	    priority: P1
79	    gpu_budget_hours: 8
80	    deps: [plan_005]
81	
82	  - id: plan_007
83	    claim: 1
84	    name: cross_model_chains
85	    description: >
86	      RQ3: Cross-model chains (different generator per depth step) vs single-model chains.
87	      More realistic scenario — web contamination involves diverse generators.
88	    priority: P1
89	    gpu_budget_hours: 12
90	    deps: [plan_002]
91	
92	  - id: plan_008
93	    claim: 1
94	    name: multi_domain_seeds
95	    description: >
96	      Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC abstracts),
97	      creative writing (WritingPrompts). 500 seeds per domain × 5 depths.
98	    priority: P1
99	    gpu_budget_hours: 10
100	    deps: [plan_002]
101	
102	  # === P2: Nice-to-have / strengthen claims ===
103	
104	  - id: plan_009
105	    claim: 1
106	    name: finer_grained_ordinal
107	    description: >
108	      Secondary analysis: 5-class ordinal classification (gen-0 through gen-4)
109	      on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.
110	    priority: P2
111	    gpu_budget_hours: 1
112	    deps: [plan_002]
113	
114	  - id: plan_010
115	    claim: 1
116	    name: human_edit_robustness
117	    description: >
118	      RC5: Robustness to simulated human edits.
119	      (A) Random word replacement (5%, 10%, 20%) as lower-bound.
120	      (B) LLM-simulated editing (light rephrasing of random sentences).
121	    priority: P2
122	    gpu_budget_hours: 5
123	    deps: [plan_002]
124	
125	  - id: plan_011
126	    claim: 2
127	    name: ld_score_feature
128	    description: >
129	      Add LD-Score (character-distribution signature from arXiv:2605.01647) as additional feature.
130	      Tests whether character-level features provide complementary depth signal.
131	    priority: P2
132	    gpu_budget_hours: 2
133	    deps: [plan_001]
134	
135	  - id: plan_012
136	    claim: 1
137	    name: end_to_end_classifier
138	    description: >
139	      QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.
140	      Compares learned representations vs handcrafted distributional features.
141	    priority: P2
142	    gpu_budget_hours: 15
143	    deps: [plan_002]
144	
145	# GPU Budget Summary:
146	# P0: ~44 GPU·hours
147	# P1: ~40 GPU·hours
148	# P2: ~23 GPU·hours
149	# Total: ~107 GPU·hours (well within 200 H100-hour budget; RTX 5090 ≈ H100 throughput for small models)
150	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24b2fc51-ce56-4e9f-baff-dfe753289eee",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "82091385-388f-44cb-8b5b-5088f3b1bc2f",
  "sourceToolAssistantUUID": "24b2fc51-ce56-4e9f-baff-dfe753289eee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T18:43:38.025Z_

<details><summary>↩ Tool result · `toolu_01CvmY5nmZm49owx8ktKCru6`</summary>

```text
1	\documentclass[letterpaper, 10pt]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{helvet}
5	\usepackage{courier}
6	\usepackage[hyphens]{url}
7	\usepackage{graphicx}
8	\usepackage{amsmath,amssymb}
9	\usepackage{booktabs}
10	\usepackage{multirow}
11	\usepackage{xcolor}
12	\usepackage{hyperref}
13	\usepackage{enumitem}
14	
15	\title{Distributional Fingerprints of Generation Depth:\\Detecting Recursive LLM Contamination Beyond Binary Classification}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\begin{abstract}
23	Web-scraped training corpora increasingly contain LLM-generated text of unknown provenance depth---text generated by models that were themselves trained on synthetic data.
24	Current detection methods provide only binary real-vs-synthetic classification, forcing all-or-nothing filtering that either discards useful first-generation content or admits deeply contaminated text with compounding distributional drift.
25	We introduce \emph{distributional fingerprinting}, a method that estimates the generation depth of text by measuring its distributional divergence from human text under a small reference language model.
26	We formalize and test two competing hypotheses for non-paraphrastic generation chains: convergence to a distributional fixed point (H$_1$) versus monotonic divergence (H$_2$).
27	Our experiments across 5 generators, 4 text domains, and 3 prompt types confirm H$_2$: non-paraphrastic chains exhibit monotonic distributional drift detectable via reference-model entropy features.
28	On multi-generator continuation chains, our 7-feature classifier achieves macro-F1 of 0.87 for 3-class depth estimation (gen-0/gen-1/gen-2+) and generalizes to unseen generators with leave-one-out F1 of 0.78.
29	Feature ablation shows reference-model entropy features carry independent signal beyond surface vocabulary impoverishment ($\Delta$F1 = +0.16, McNemar $p < 10^{-4}$).
30	Depth-aware data filtering retains 42\% of training data while achieving perplexity within 0.7 points of human-only baselines---outperforming binary detection baselines by 5.2\% while retaining 50\% more data.
31	\end{abstract}
32	
33	\section{Introduction}
34	
35	The recursive contamination of training data by LLM outputs is an accelerating concern.
36	As language models are deployed at scale, their outputs enter the web, are scraped into training corpora, and are used to train the next generation of models~\cite{shumailov2024model}.
37	This creates generation chains: text at \emph{depth~0} is human-written, depth~1 is generated from human text, depth~2 is generated from depth-1 text, and so forth.
38	The distributional consequences of this recursive process are poorly understood.
39	
40	Existing detection methods---FastDetectGPT, SynthID-Text, LD-Score~\cite{bao2024fastdetectgpt, dathathri2024synthid, dugan2024ldscore}---operate in a binary paradigm: text is classified as real or synthetic.
41	This forces a lossy tradeoff.
42	Aggressive filtering discards all flagged text, including first-generation content that is distributionally close to human text and useful for training.
43	Permissive filtering admits deeply generated text with compounding distributional artifacts.
44	Neither approach is adequate for risk-stratified data governance.
45	
46	Attractor cycle theory~\cite{briesch2025attractor} has established that \emph{paraphrastic} generation chains converge to 2-period distributional cycles, bounding depth discriminability to roughly 3 classes.
47	However, this result depends on the semantic-preservation constraint inherent to paraphrasing.
48	Non-paraphrastic chains---continuations, elaborations, and other open-ended generation tasks---operate in an unbounded semantic state space.
49	Whether distributional drift in such chains converges (H$_1$) or diverges monotonically (H$_2$) remains an open empirical question.
50	
51	We address this question by introducing \emph{distributional fingerprinting}: computing token-level statistics under a small reference language model to characterize the distributional displacement of text from the human-text manifold.
52	Our method extracts 7 features---5 reference-model entropy statistics and 2 surface vocabulary statistics---and uses an XGBoost classifier for ordinal depth estimation.
53	
54	Our contributions are:
55	\begin{enumerate}
56	    \item \textbf{Empirical confirmation of H$_2$}: Non-paraphrastic generation chains exhibit monotonic distributional divergence, in contrast to the convergence observed in paraphrastic chains. This is demonstrated by direct comparison of continuation vs.\ paraphrasing chains (KS statistic $D = 0.41$, $p < 10^{-4}$).
57	    \item \textbf{Cross-generator depth classification}: Our distributional fingerprint achieves macro-F1 = 0.87 (3-class) and generalizes across 5 generator families with leave-one-generator-out F1 = 0.78 $\pm$ 0.03.
58	    \item \textbf{Risk-stratified data curation}: Depth-aware filtering outperforms binary baselines by 5.2\% in downstream perplexity while retaining 50\% more training data.
59	\end{enumerate}
60	
61	\section{Related Work}
62	
63	\paragraph{Synthetic text detection.}
64	Binary detection methods assign a real/synthetic label to text.
65	FastDetectGPT~\cite{bao2024fastdetectgpt} uses conditional probability curvature, SynthID-Text~\cite{dathathri2024synthid} embeds statistical watermarks, and LD-Score~\cite{dugan2024ldscore} uses character-level distributional signatures.
66	All are binary classifiers that cannot distinguish generation depth.
67	
68	\paragraph{Model collapse and iterative retraining.}
69	Shumailov et al.~\cite{shumailov2024model} demonstrate that iterative retraining on model outputs leads to distributional collapse, with progressive loss of low-frequency modes.
70	Their analysis focuses on full-model retraining dynamics rather than individual text-level depth estimation.
71	
72	\paragraph{Attractor cycles in paraphrasing chains.}
73	Briesch et al.~\cite{briesch2025attractor} prove that iterative paraphrasing converges to 2-period distributional cycles, where semantic content oscillates between two attractors.
74	This convergence limits depth discriminability for paraphrastic chains.
75	Our work complements theirs by studying non-paraphrastic chains, where the absence of semantic preservation constraints leads to qualitatively different dynamics.
76	
77	\section{Method}
78	
79	\subsection{Problem Formulation}
80	
81	Let $\mathcal{G}$ be a text generator and $x^{(0)}$ be a human-authored seed text.
82	A \emph{generation chain} of depth $d$ produces a sequence $x^{(0)}, x^{(1)}, \ldots, x^{(d)}$ where $x^{(k)} = \mathcal{G}(x^{(k-1)})$.
83	Given a text sample $x$ drawn from an unknown depth, the depth estimation task is to predict $\hat{d} \in \{0, 1, 2, \ldots\}$.
84	We operationalize this as classification into depth classes: gen-0 (human), gen-1 (first-generation synthetic), and gen-2+ (depth $\geq 2$).
85	
86	\subsection{Distributional Fingerprint Features}
87	
88	We extract features by scoring text under a \emph{reference model} $p_{\text{ref}}$---a small pretrained language model (Pythia-410M by default) that was never fine-tuned on synthetic data.
89	For each token $t_i$ in a text of length $n$, we compute the reference-model negative log-likelihood $\ell_i = -\log p_{\text{ref}}(t_i | t_{&lt;i})$.
90	
91	\paragraph{Reference-model features (5).}
92	We compute: (1) $\texttt{entropy\_mean} = \frac{1}{n}\sum_i \ell_i$, the average surprise under the reference model; (2) $\texttt{entropy\_std}$, the standard deviation of per-token surprises; (3--4) $\texttt{entropy\_min}$, $\texttt{entropy\_max}$, capturing the range; and (5) $\texttt{tail\_decay}$, the fraction of tokens in the top-10\% surprise quantile, measuring how much text mass falls in the distributional tail.
93	
94	The intuition is that deeper-generation text progressively occupies lower-probability regions of the reference model's distribution.
95	As drift accumulates, $\texttt{entropy\_mean}$ increases because the reference model is increasingly ``surprised'' by text that has drifted from the human-text manifold.
96	The variance ($\texttt{entropy\_std}$) increases because deeper text alternates between familiar patterns and novel drift artifacts.
97	
98	\paragraph{Surface features (2).}
99	We include type-token ratio ($\texttt{ttr}$) and hapax legomenon ratio ($\texttt{hapax\_ratio}$) as vocabulary diversity measures.
100	These capture the well-known vocabulary impoverishment effect of language model generation but, as we show, provide weaker and less fine-grained depth signal than reference-model features.
101	
102	\subsection{Classifier}
103	
104	We train an XGBoost classifier on the 7-dimensional feature vector with 5-fold stratified cross-validation.
105	We chose XGBoost over neural alternatives for interpretability and computational efficiency (training in $\sim$3 minutes vs.\ 12 GPU-hours for a fine-tuned LLM baseline; see Section~\ref{sec:e2e}).
106	
107	\subsection{Hypotheses}
108	
109	We formalize two competing hypotheses about distributional dynamics in recursive generation:
110	
111	\noindent\textbf{H$_1$ (Convergence):} Non-paraphrastic chains converge to a distributional fixed point, analogous to paraphrastic attractor cycles.
112	Under H$_1$, depth signal saturates after a few generations.
113	
114	\noindent\textbf{H$_2$ (Divergence):} Non-paraphrastic chains accumulate monotonic distributional drift from the human-text manifold.
115	Under H$_2$, depth signal grows with generation depth, enabling ordinal depth estimation.
116	
117	\section{Experimental Setup}
118	
119	\paragraph{Data generation.}
120	We construct generation chains from 2{,}000 seed texts spanning 4 domains (Wikipedia, CNN/DailyMail news, S2ORC scientific abstracts, WritingPrompts creative fiction), 500 seeds per domain.
121	Each seed is extended to depth 5 using 5 generators: Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, and Pythia-1B.
122	Three prompt types are used: continuation, elaboration, and inspired rewriting.
123	The resulting dataset contains $\sim$24{,}200 chains after $\sim$3.2\% attrition from generation failures.
124	
125	\paragraph{Feature extraction.}
126	All features are extracted using Pythia-410M as the default reference model.
127	Cross-reference experiments additionally use OLMo-2-1B and Qwen3.5-0.8B.
128	
129	\paragraph{Evaluation protocol.}
130	Unless otherwise stated, we report macro-F1 over 5-fold stratified cross-validation for the 3-class task (gen-0/gen-1/gen-2+).
131	For generalization experiments, we use leave-one-generator-out and leave-one-domain-out protocols.
132	
133	\section{Experiments}
134	
135	\subsection{Feature Ablation (Claim 2)}
136	\label{sec:ablation}
137	
138	We ablate the 7-feature set into three conditions: (A) reference-only features (5 entropy statistics), (B) surface-only features (TTR, hapax ratio), and (C) the full 7-feature set.
139	All use the same XGBoost classifier with 5-fold stratified CV on the MVP dataset (4{,}609 records, Pythia-2.8B generator, Wikipedia seeds).
140	
141	\begin{table}[t]
142	\centering
143	\caption{Feature ablation results (3-class depth classification). Reference-model features alone substantially outperform surface-only features, and the full set achieves the best performance.}
144	\label{tab:ablation}
145	\small
146	\begin{tabular}{@{}lcccc@{}}
147	\toprule
148	Feature Set & Macro-F1 & gen-0 & gen-1 & gen-2+ \\
149	\midrule
150	Reference-only (5) & 0.79 {\scriptsize$\pm$0.018} & 0.91 & 0.71 & 0.74 \\
151	Surface-only (2) & 0.63 {\scriptsize$\pm$0.022} & 0.82 & 0.52 & 0.55 \\
152	Full (7) & \textbf{0.87} {\scriptsize$\pm$0.012} & \textbf{0.96} & \textbf{0.81} & \textbf{0.83} \\
153	\midrule
154	$\Delta$ (ref $-$ surface) & +0.16 & +0.09 & +0.19 & +0.19 \\
155	\bottomrule
156	\end{tabular}
157	\end{table}
158	
159	Table~\ref{tab:ablation} shows that reference-only features achieve macro-F1 = 0.79, substantially outperforming surface-only features at 0.63 ($\Delta$ = +0.16, McNemar $p = 3 \times 10^{-5}$).
160	The advantage is largest for gen-1 and gen-2+ ($\Delta$ = +0.19 each), precisely the classes where surface features struggle.
161	This is because vocabulary impoverishment (captured by TTR, hapax ratio) saturates between gen-0 and gen-1, while reference-model entropy features capture cumulative distributional drift that continues to grow at deeper depths.
162	
163	Permutation importance analysis (Table~\ref{tab:importance}) confirms this pattern: under permutation (which avoids XGBoost's split-gain bias toward high-cardinality features), $\texttt{entropy\_mean}$ emerges as the dominant feature (importance = 0.28), while $\texttt{hapax\_ratio}$ drops from its inflated XGBoost gain rank.
164	
165	\begin{table}[t]
166	\centering
167	\caption{Permutation importance vs.\ XGBoost gain.}
168	\label{tab:importance}
169	\small
170	\begin{tabular}{@{}lcc@{}}
171	\toprule
172	Feature & Perm.\ Importance & XGB Gain \\
173	\midrule
174	entropy\_mean & \textbf{0.28} & 0.22 \\
175	entropy\_std & 0.19 & 0.13 \\
176	hapax\_ratio & 0.14 & 0.30 \\
177	tail\_decay & 0.13 & 0.06 \\
178	ttr & 0.09 & 0.17 \\
179	entropy\_max & 0.09 & 0.07 \\
180	entropy\_min & 0.08 & 0.06 \\
181	\bottomrule
182	\end{tabular}
183	\end{table}
184	
185	\subsection{Cross-Generator Generalization (Claim 1)}
186	\label{sec:crossgen}
187	
188	To test whether distributional fingerprints generalize beyond any single generator family, we evaluate using leave-one-generator-out cross-validation across 5 generators.
189	
190	\begin{table}[t]
191	\centering
192	\caption{Leave-one-generator-out cross-validation. The classifier trained on 4 generators generalizes to the held-out generator.}
193	\label{tab:crossgen}
194	\small
195	\begin{tabular}{@{}lcccc@{}}
196	\toprule
197	Held-out Generator & Macro-F1 & gen-0 & gen-1 & gen-2+ \\
198	\midrule
199	Pythia-2.8B & 0.81 & 0.91 & 0.75 & 0.77 \\
200	OLMo-2-1B & 0.77 & 0.87 & 0.72 & 0.73 \\
201	Qwen3.5-2B & 0.76 & 0.86 & 0.71 & 0.72 \\
202	Qwen3.5-0.8B & 0.74 & 0.84 & 0.68 & 0.70 \\
203	Pythia-1B & 0.82 & 0.92 & 0.76 & 0.78 \\
204	\midrule
205	Mean $\pm$ std & 0.78 $\pm$ 0.03 & 0.88 & 0.73 & 0.75 \\
206	\bottomrule
207	\end{tabular}
208	\end{table}
209	
210	Table~\ref{tab:crossgen} demonstrates consistent generalization: mean leave-one-out F1 = 0.78 $\pm$ 0.03 across all 5 generators, with gen-0 separation remaining strong ($\geq$0.84) in all cases.
211	Cross-family transfer (e.g., Pythia-trained classifier tested on Qwen) maintains F1 $\geq$ 0.74, confirming that the distributional fingerprint is a property of the generation process rather than a generator-specific artifact.
212	In-distribution pooled performance reaches 0.86, suggesting that multi-generator training improves robustness (Table~\ref{tab:indist}).
213	
214	\begin{table}[t]
215	\centering
216	\caption{Per-generator in-distribution 5-fold CV.}
217	\label{tab:indist}
218	\small
219	\begin{tabular}{@{}lcc@{}}
220	\toprule
221	Generator & Macro-F1 & CV std \\
222	\midrule
223	Pythia-2.8B & 0.85 & 0.014 \\
224	OLMo-2-1B & 0.84 & 0.016 \\
225	Qwen3.5-2B & 0.86 & 0.013 \\
226	Qwen3.5-0.8B & 0.83 & 0.019 \\
227	Pythia-1B & 0.84 & 0.015 \\
228	\midrule
229	Pooled (all 5) & 0.86 & 0.011 \\
230	\bottomrule
231	\end{tabular}
232	\end{table}
233	
234	\subsection{Cross-Family Reference Models}
235	
236	A natural concern is whether the fingerprint depends on the choice of reference model.
237	We re-extract features using OLMo-2-1B and Qwen3.5-0.8B as alternative reference models, and compare classification performance.
238	
239	\begin{table}[t]
240	\centering
241	\caption{Reference model comparison on pooled 5-generator data.}
242	\label{tab:crossref}
243	\small
244	\begin{tabular}{@{}llcccc@{}}
245	\toprule
246	Reference Model & Params & F1 & gen-0 & gen-1 & gen-2+ \\
247	\midrule
248	Pythia-410M & 410M & 0.86 & 0.95 & 0.80 & 0.82 \\
249	OLMo-2-1B & 1B & 0.76 & 0.88 & 0.69 & 0.72 \\
250	Qwen3.5-0.8B & 0.8B & 0.74 & 0.86 & 0.66 & 0.70 \\
251	Ensemble (3 refs) & --- & \textbf{0.88} & \textbf{0.96} & \textbf{0.83} & \textbf{0.85} \\
252	\bottomrule
253	\end{tabular}
254	\end{table}
255	
256	All three reference models detect depth signal (F1 $\geq$ 0.74; Table~\ref{tab:crossref}), confirming that the fingerprint is not a Pythia-specific artifact.
257	High cross-reference correlations in entropy features (Spearman $\rho$ = 0.78--0.82 for $\texttt{entropy\_mean}$) indicate that different reference models measure the same underlying drift phenomenon through slightly different lenses.
258	The 3-reference ensemble achieves F1 = 0.88, suggesting that diverse reference models capture complementary drift aspects.
259	
260	\subsection{Paraphrastic vs.\ Non-Paraphrastic Chains (H$_1$ vs.\ H$_2$)}
261	\label{sec:h1h2}
262	
263	We directly test H$_1$ vs.\ H$_2$ by constructing parallel paraphrasing and continuation chains from the same 1{,}000 seeds.
264	
265	\begin{table}[t]
266	\centering
267	\caption{Paraphrastic vs.\ continuation chain comparison. Continuation chains show monotonic divergence (H$_2$); paraphrastic chains converge (H$_1$).}
268	\label{tab:h1h2}
269	\small
270	\begin{tabular}{@{}lccc@{}}
271	\toprule
272	Chain Type & Macro-F1 & Entropy Drift @d3 & Cycle \% \\
273	\midrule
274	Continuation & 0.85 & 0.52 nats & $<5\%$ \\
275	Paraphrasing & 0.58 & 0.06 nats & 68\% \\
276	\midrule
277	$\Delta$ & +0.27 & +0.46 nats & --- \\
278	\bottomrule
279	\end{tabular}
280	\end{table}
281	
282	Table~\ref{tab:h1h2} provides definitive evidence.
283	Continuation chains accumulate substantial entropy drift (0.52 nats by depth 3) with strong depth classification (F1 = 0.85), while paraphrastic chains show near-zero drift (0.06 nats) and weak classification (F1 = 0.58).
284	The 68\% cycle detection rate in paraphrastic chains---where text at depth $d$ is more similar to depth $d{-}2$ than $d{-}1$---directly corroborates the attractor cycle prediction of~\cite{briesch2025attractor}.
285	A two-sample Kolmogorov-Smirnov test on the depth-3 entropy distributions yields $D = 0.41$, $p < 10^{-4}$, confirming that the two chain types occupy distinct distributional regimes.
286	H$_2$ holds for non-paraphrastic chains; H$_1$ holds for paraphrastic chains.
287	
288	\subsection{Downstream Utility (Claim 3)}
289	\label{sec:downstream}
290	
291	We validate the practical value of depth estimation by fine-tuning Pythia-410M on depth-stratified data subsets and measuring perplexity on a held-out human test set.
292	
293	\begin{table}[t]
294	\centering
295	\caption{Fine-tuning perplexity by training data depth. Perplexity increases monotonically with depth ($\rho = 0.72$).}
296	\label{tab:ppl}
297	\small
298	\begin{tabular}{@{}llcc@{}}
299	\toprule
300	Training Data & Depth & PPL ($\downarrow$) & Samples \\
301	\midrule
302	Human-only & gen-0 & 28.3 & $\sim$4{,}800 \\
303	gen-1 only & gen-1 & 30.1 & $\sim$4{,}750 \\
304	gen-2 only & gen-2 & 34.7 & $\sim$4{,}500 \\
305	gen-3 only & gen-3 & 38.9 & $\sim$4{,}200 \\
306	gen-4 only & gen-4 & 43.2 & $\sim$3{,}900 \\
307	Uniform mix & gen-0--4 & 35.8 & $\sim$22{,}000 \\
308	\midrule
309	Depth-filtered (ours) & gen-0+1 & \textbf{29.0} & $\sim$9{,}500 \\
310	FastDetectGPT filter & binary & 31.8 & $\sim$6{,}300 \\
311	LD-Score filter & binary & 32.1 & $\sim$6{,}100 \\
312	\midrule
313	Human test baseline & --- & 27.5 & --- \\
314	\bottomrule
315	\end{tabular}
316	\end{table}
317	
318	Table~\ref{tab:ppl} demonstrates a monotonic relationship between training data depth and downstream perplexity (Spearman $\rho = 0.72$), providing an intuitive translation of distributional drift into a metric practitioners care about.
319	Depth-aware filtering (keep gen-0 + gen-1) achieves perplexity 29.0---within 0.7 points of the human-only baseline---while binary baselines achieve 31.8--32.1.
320	
321	\begin{table}[t]
322	\centering
323	\caption{Depth-aware vs.\ binary filtering. Depth-aware filtering retains more data at lower perplexity.}
324	\label{tab:filter}
325	\small
326	\begin{tabular}{@{}lccc@{}}
327	\toprule
328	Method & PPL & Retained & $\Delta$ Human \\
329	\midrule
330	Depth-filtered (gen-0+1) & \textbf{29.0} & 42\% & +0.7 \\
331	FastDetectGPT binary & 31.8 & 28\% & +3.5 \\
332	LD-Score binary & 32.1 & 26\% & +3.8 \\
333	No filtering & 35.8 & 100\% & +7.5 \\
334	\bottomrule
335	\end{tabular}
336	\end{table}
337	
338	The key practical insight (Table~\ref{tab:filter}): gen-1 text is ``good enough'' for training (PPL = 30.1 vs.\ human 28.3), but gen-2+ is not (PPL $\geq$ 34.7).
339	Binary detectors cannot make this distinction.
340	Depth-aware filtering retains 42\% of data (vs.\ 28\% for binary filtering), resolving the precision--recall tradeoff that plagues binary detection.
341	
342	\subsection{Prompt Type Analysis}
343	\label{sec:prompt}
344	
345	We compare depth signal across three prompt types: continuation, elaboration, and inspired rewriting.
346	
347	\begin{table}[t]
348	\centering
349	\caption{Depth classification by prompt type. More constrained generation produces stronger depth signal.}
350	\label{tab:prompt}
351	\small
352	\begin{tabular}{@{}lccccc@{}}
353	\toprule
354	Prompt Type & F1 & gen-0 & gen-1 & gen-2+ & Drift Rate \\
355	\midrule
356	Continuation & 0.85 & 0.95 & 0.79 & 0.81 & 0.18 \\
357	Elaboration & 0.80 & 0.92 & 0.73 & 0.75 & 0.14 \\
358	Inspired rewriting & 0.72 & 0.86 & 0.64 & 0.67 & 0.10 \\
359	\bottomrule
360	\end{tabular}
361	\end{table}
362	
363	Table~\ref{tab:prompt} reveals a graded relationship: the more a generation task constrains the output to build on previous text, the faster drift accumulates.
364	Continuation (maximum constraint) yields the strongest signal; inspired rewriting (maximum freedom) yields the weakest.
365	The strong correlation between per-depth entropy drift rate and classification F1 (Spearman $\rho = 0.91$) confirms the theoretical prediction that drift accumulation rate determines depth discriminability.
366	Cross-prompt-type transfer achieves F1 = 0.74, indicating partially shared but rate-differentiated drift signatures.
367	
368	\subsection{Cross-Model Chains}
369	
370	Real-world contamination involves diverse generators at different depths.
371	We construct cross-model chains where each depth step uses a randomly sampled generator.
372	
373	\begin{table}[t]
374	\centering
375	\caption{Single-model vs.\ cross-model chain comparison.}
376	\label{tab:crossmodel}
377	\small
378	\begin{tabular}{@{}lcccc@{}}
379	\toprule
380	Chain Type & F1 & gen-0 & gen-1 & gen-2+ \\
381	\midrule
382	Single-model (mean) & 0.85 & 0.95 & 0.79 & 0.81 \\
383	Cross-model & 0.75 & 0.90 & 0.68 & 0.67 \\
384	\midrule
385	$\Delta$ & $-$0.10 & $-$0.05 & $-$0.11 & $-$0.14 \\
386	\bottomrule
387	\end{tabular}
388	\end{table}
389	
390	Cross-model chains incur a 10-point F1 drop (Table~\ref{tab:crossmodel})---the honest cost of ecological validity.
391	Generator switching introduces distributional discontinuities that partially mask the monotonic drift signal.
392	However, F1 = 0.75 remains well above chance (0.33), and gen-0 separation is robust (F1 = 0.90), preserving the method's primary utility for separating human from synthetic text.
393	
394	\subsection{Multi-Domain Evaluation}
395	
396	\begin{table}[t]
397	\centering
398	\caption{Multi-domain depth classification. Depth signal is domain-general, strongest for factual text.}
399	\label{tab:domain}
400	\small
401	\begin{tabular}{@{}lccccc@{}}
402	\toprule
403	Domain & Seeds & F1 & gen-0 & gen-1 & gen-2+ \\
404	\midrule
405	Wikipedia & 500 & 0.86 & 0.95 & 0.80 & 0.82 \\
406	News & 500 & 0.83 & 0.93 & 0.77 & 0.79 \\
407	Scientific & 500 & 0.81 & 0.91 & 0.74 & 0.77 \\
408	Creative & 500 & 0.78 & 0.88 & 0.71 & 0.74 \\
409	\midrule
410	Pooled & 2{,}000 & 0.84 & 0.93 & 0.78 & 0.80 \\
411	Leave-one-out & --- & 0.77 & 0.88 & 0.70 & 0.73 \\
412	\bottomrule
413	\end{tabular}
414	\end{table}
415	
416	Table~\ref{tab:domain} confirms domain generalization across 4 text types.
417	The ordering (factual $>$ creative) is interpretable: generators produce more fluent creative text with smaller human--synthetic distributional gaps, reducing overall drift magnitude.
418	Leave-one-domain-out F1 = 0.77 with low cross-domain variance ($\sigma^2$ = 0.0009) demonstrates that depth signal is a robust, domain-general phenomenon.
419	
420	\subsection{Finer-Grained Ordinal Classification}
421	\label{sec:ordinal}
422	
423	We test whether non-paraphrastic chains support depth resolution beyond 3 classes.
424	
425	\begin{table}[t]
426	\centering
427	\caption{5-class ordinal depth classification.}
428	\label{tab:ordinal}
429	\small
430	\begin{tabular}{@{}lccc@{}}
431	\toprule
432	Class & Precision & Recall & F1 \\
433	\midrule
434	gen-0 & 0.93 & 0.91 & 0.92 \\
435	gen-1 & 0.66 & 0.70 & 0.68 \\
436	gen-2 & 0.50 & 0.54 & 0.52 \\
437	gen-3 & 0.47 & 0.49 & 0.48 \\
438	gen-4 & 0.53 & 0.50 & 0.51 \\
439	\midrule
440	Macro & --- & --- & 0.62 \\
441	\bottomrule
442	\end{tabular}
443	\end{table}
444	
445	5-class macro-F1 is 0.62 (Table~\ref{tab:ordinal}), lower than the 3-class result due to overlapping feature distributions at deep classes.
446	However, the ordinal structure is preserved: Spearman $\rho = 0.83$ between predicted and true depth, with MAE = 0.58 and 72\% of errors being off-by-one.
447	This confirms that drift is monotonic (supporting H$_2$) while establishing a practical resolution ceiling: 3-class coarse bucketing is more reliable than exact depth prediction for data curation purposes.
448	
449	\subsection{Robustness to Post-Generation Editing}
450	
451	\begin{table}[t]
452	\centering
453	\caption{Robustness to simulated post-generation edits.}
454	\label{tab:robust}
455	\small
456	\begin{tabular}{@{}llcc@{}}
457	\toprule
458	Edit Type & Rate & Macro-F1 & $\Delta$ \\
459	\midrule
460	None (baseline) & 0\% & 0.86 & --- \\
461	Random word replacement & 5\% & 0.83 & $-$0.03 \\
462	Random word replacement & 10\% & 0.78 & $-$0.08 \\
463	Random word replacement & 20\% & 0.67 & $-$0.19 \\
464	LLM light editing & $\sim$8--12\% & 0.76 & $-$0.10 \\
465	\bottomrule
466	\end{tabular}
467	\end{table}
468	
469	Table~\ref{tab:robust} characterizes degradation under post-generation editing.
470	Light editing (5\%) typical of human post-processing preserves most depth signal ($\Delta$ = $-$0.03).
471	Degradation is approximately linear ($-$0.095 F1 per 10\% edit rate), providing a simple model for practitioners to assess reliability.
472	Even at 20\% editing, performance (F1 = 0.67) remains well above chance.
473	
474	\subsection{LD-Score Feature Integration}
475	
476	\begin{table}[t]
477	\centering
478	\caption{LD-Score feature integration.}
479	\label{tab:ld}
480	\small
481	\begin{tabular}{@{}lcc@{}}
482	\toprule
483	Feature Set & Macro-F1 & $\Delta$ from Full \\
484	\midrule
485	Full (7 features) & 0.87 & --- \\
486	Full + LD-Score & 0.88 & +0.01 \\
487	LD-Score only & 0.59 & $-$0.28 \\
488	\bottomrule
489	\end{tabular}
490	\end{table}
491	
492	Adding LD-Score~\cite{dugan2024ldscore} as an 8th feature provides marginal improvement ($\Delta$ = +0.01; Table~\ref{tab:ld}).
493	LD-Score alone achieves only F1 = 0.59 with low permutation importance (0.06), confirming that character-level distributional signatures are largely redundant with existing surface features---both measure vocabulary impoverishment at different granularities.
494	This reinforces that reference-model entropy features, not surface-level statistics, are the novel signal source.
495	
496	\subsection{End-to-End Neural Baseline}
497	\label{sec:e2e}
498	
499	\begin{table}[t]
500	\centering
501	\caption{Feature-based vs.\ end-to-end neural comparison.}
502	\label{tab:e2e}
503	\small
504	\begin{tabular}{@{}lccc@{}}
505	\toprule
506	Method & In-Dist F1 & Cross-Gen F1 & Cost \\
507	\midrule
508	XGBoost + features & \textbf{0.86} & \textbf{0.78} & 3 min \\
509	QLoRA Qwen3.5-0.8B & 0.83 & 0.71 & 12 GPU$\cdot$h \\
510	\midrule
511	$\Delta$ & +0.03 & +0.07 & --- \\
512	\bottomrule
513	\end{tabular}
514	\end{table}
515	
516	We compare against a QLoRA-fine-tuned Qwen3.5-0.8B as an end-to-end neural baseline (Table~\ref{tab:e2e}).
517	The handcrafted feature approach outperforms on both in-distribution (+0.03) and cross-generator (+0.07) F1, while being $\sim$240$\times$ cheaper to train.
518	The larger cross-generator gap reveals that the fine-tuned model memorizes generator-specific artifacts, while handcrafted features are designed to capture generator-invariant distributional drift.
519	
520	\section{Discussion}
521	
522	\paragraph{Theoretical implications.}
523	Our results establish a clean dichotomy in recursive generation dynamics: paraphrastic chains converge (H$_1$), non-paraphrastic chains diverge (H$_2$).
524	This distinction arises from the presence or absence of a semantic-preservation constraint: paraphrasing re-anchors to a fixed semantic target at each step, while continuation explores an unbounded state space where distributional drift accumulates.
525	The prompt type analysis (Section~\ref{sec:prompt}) reveals this is a spectrum, not a binary---elaboration lies between continuation and paraphrasing in drift rate.
526	
527	\paragraph{Practical implications for data curation.}
528	Distributional fingerprints enable \emph{risk-stratified} data governance: rather than binary accept/reject decisions, practitioners can assign depth-derived risk scores and set thresholds appropriate to their quality requirements.
529	Our downstream experiments show that gen-1 text is nearly as valuable as human text for training (perplexity gap of 1.8 points), while gen-2+ text introduces meaningful quality degradation.
530	Depth-aware filtering achieves the best quality--quantity tradeoff: 42\% data retention at near-human quality, vs.\ 28\% retention with worse quality under binary filtering.
531	
532	\paragraph{Limitations.}
533	The method's primary limitation is sensitivity to post-generation editing ($-$0.095 F1 per 10\% edit rate).
534	Cross-model chains reduce accuracy by 10 points compared to single-model chains.
535	Finer-grained depth estimation (5-class) has limited precision for depths $\geq$2, though ordinal structure is preserved.
536	All experiments use models $\leq$2.8B parameters; scaling to larger generators requires further investigation.
537	
538	\section{Conclusion}
539	
540	We introduced distributional fingerprinting for generation depth estimation, demonstrating that non-paraphrastic LLM generation chains exhibit monotonic distributional divergence detectable via reference-model entropy features.
541	Our 7-feature classifier achieves macro-F1 = 0.87 for 3-class depth estimation, generalizes across 5 generator families (leave-one-out F1 = 0.78), and enables depth-aware data curation that outperforms binary detection baselines by 5.2\% in downstream quality while retaining 50\% more training data.
542	The clean separation between convergent paraphrastic chains and divergent non-paraphrastic chains provides a unified framework connecting attractor cycle theory to the distributional dynamics of recursive text generation.
543	
544	\bibliographystyle{plain}
545	
546	\begin{thebibliography}{10}
547	
548	\bibitem{shumailov2024model}
549	I.~Shumailov, Z.~Shumaylov, Y.~Zhao, N.~Papernot, R.~Anderson, and Y.~Gal.
550	\newblock AI models collapse when trained on recursively generated data.
551	\newblock {\em Nature}, 631:755--759, 2024.
552	
553	\bibitem{bao2024fastdetectgpt}
554	G.~Bao, Y.~Zhao, Z.~Teng, L.~Yang, and J.~Zhang.
555	\newblock Fast-{D}etect{GPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.
556	\newblock In {\em Proc.\ ICLR}, 2024.
557	
558	\bibitem{dathathri2024synthid}
559	S.~Dathathri, A.~See, S.~Ghaisas, P.-S.~Huang, R.~McAdam, J.~Welbl, V.~Bachani, A.~Kaskasoli, R.~Stanforth, T.~Matejovicova, et~al.
560	\newblock Scalable watermarking for identifying large language model outputs.
561	\newblock {\em Nature}, 634:818--823, 2024.
562	
563	\bibitem{dugan2024ldscore}
564	L.~Dugan, H.~Hwang, F.~Trhl{\'\i}k, A.~Ladhak, A.~Ippolito, and C.~Callison-Burch.
565	\newblock {LD}-Score: A character-level metric for distinguishing human from machine-generated text.
566	\newblock {\em arXiv preprint arXiv:2605.01647}, 2025.
567	
568	\bibitem{briesch2025attractor}
569	M.~Briesch, D.~Sobania, and F.~Rothlauf.
570	\newblock Large language models are attractor cycles of iterative paraphrasing.
571	\newblock In {\em Proc.\ ACL}, 2025.
572	
573	\end{thebibliography}
574	
575	\end{document}
576	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e873af61-26e3-40a0-a75f-24085d3f358d",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "c8bab345-ac7f-4029-9a26-fe70ec677c3f",
  "sourceToolAssistantUUID": "e873af61-26e3-40a0-a75f-24085d3f358d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-14T18:43:40.688Z_

Now let me read the other dream report variants and the imagined experiments to get a complete picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8bab345-ac7f-4029-9a26-fe70ec677c3f",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xKcR8DhvM8bHxqSPSv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10dbe99a-e95c-4724-a6cd-c5a0d82944ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ugotz5JdPhxADhPayxUgiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2111,
      "cache_creation_input_tokens": 11858,
      "cache_read_input_tokens": 23904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11858,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 30 · 2026-05-14T18:43:42.562Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UV5gRBfgz8xxaP8rXrTeiL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10dbe99a-e95c-4724-a6cd-c5a0d82944ca",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xKcR8DhvM8bHxqSPSv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d254ba59-cedf-4b78-8f3f-7f8a2453a154",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ugotz5JdPhxADhPayxUgiU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2111,
      "cache_creation_input_tokens": 11858,
      "cache_read_input_tokens": 23904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11858,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 31 · 2026-05-14T18:43:42.842Z_

<details><summary>↩ Tool result · `toolu_01UV5gRBfgz8xxaP8rXrTeiL`</summary>

```text
1	tier: best
2	narrative_guidance: 'Original framing fully intact. Story: non-paraphrastic chains
3	  exhibit monotonic distributional divergence (H₂ confirmed), detectable via reference-model
4	  entropy features that capture drift beyond surface vocabulary impoverishment. Headline:
5	  "distributional fingerprints enable risk-stratified data curation," with clean ablation
6	  separating signal from shortcut. All three claims stated at full strength. AAAI
7	  submission with no scope reduction.
8	
9	  '
10	imagined_experiments:
11	- name: feature_ablation
12	  plan_id: plan_001
13	  description: 'Ablation on existing MVP data (4609 records, Pythia-2.8B generator,
14	    Pythia-410M reference, Wikipedia seeds). Three conditions: (A) reference-only
15	    features (entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay), (B)
16	    surface-only features (ttr, hapax_ratio), (C) full 7-feature set. Same XGBoost
17	    classifier, 5-fold stratified CV, 3-class (gen-0/gen-1/gen-2+).
18	
19	    '
20	  expected_results:
21	    ref_only_macro_f1: 0.79
22	    ref_only_cv_std: 0.018
23	    ref_only_gen0_f1: 0.91
24	    ref_only_gen1_f1: 0.71
25	    ref_only_gen2plus_f1: 0.74
26	    surface_only_macro_f1: 0.63
27	    surface_only_cv_std: 0.022
28	    surface_only_gen0_f1: 0.82
29	    surface_only_gen1_f1: 0.52
30	    surface_only_gen2plus_f1: 0.55
31	    full_macro_f1: 0.87
32	    full_cv_std: 0.012
33	    full_gen0_f1: 0.96
34	    full_gen1_f1: 0.81
35	    full_gen2plus_f1: 0.83
36	    ref_minus_surface_delta: 0.16
37	    mcnemar_p_ref_vs_surface: 3.0e-05
38	    permutation_importance_entropy_mean: 0.28
39	    permutation_importance_entropy_std: 0.19
40	    permutation_importance_hapax_ratio: 0.14
41	    permutation_importance_ttr: 0.09
42	  result_rationale: 'MVP feature importance (hapax_ratio=0.30) was inflated by XGBoost''s
43	    split-gain metric, which overweights high-cardinality continuous features with
44	    many useful split points. When surface features are ablated, the 5 reference-model
45	    features retain macro-F1=0.79 because they directly measure the generator''s deviation
46	    from the reference model''s next-token distribution — a signal that accumulates
47	    monotonically with depth as the generator''s output drifts further from human
48	    text. Entropy_mean captures the average surprise under the reference model (increases
49	    with depth as generated text occupies lower-probability regions), while entropy_std
50	    captures the increasing variance of surprise (deeper text alternates between familiar
51	    patterns and novel drift). Surface features alone (F1=0.63) capture only vocabulary
52	    impoverishment — TTR and hapax_ratio decline with depth as generators recycle
53	    high-frequency tokens — but this is a weaker, noisier proxy. The 0.16 delta and
54	    significant McNemar test confirm reference features carry independent, dominant
55	    signal. The full set achieves F1=0.87 (up from MVP''s 0.84) because retuned hyperparameters
56	    on the same data with proper ablation awareness extract slightly more complementary
57	    value. Permutation importance (which avoids split-gain bias) reranks entropy_mean
58	    as the top feature.
59	
60	    '
61	  tables:
62	  - name: 'Table 1: Feature Ablation Results (3-class depth classification)'
63	    columns:
64	    - Feature Set
65	    - Features
66	    - Macro-F1
67	    - gen-0 F1
68	    - gen-1 F1
69	    - gen-2+ F1
70	    - CV std
71	    rows:
72	    - - Reference-only
73	      - entropy_{mean,std,min,max}, tail_decay
74	      - 0.79
75	      - 0.91
76	      - 0.71
77	      - 0.74
78	      - 0.018
79	    - - Surface-only
80	      - ttr, hapax_ratio
81	      - 0.63
82	      - 0.82
83	      - 0.52
84	      - 0.55
85	      - 0.022
86	    - - Full
87	      - All 7 features
88	      - 0.87
89	      - 0.96
90	      - 0.81
91	      - 0.83
92	      - 0.012
93	    - - Δ (ref − surface)
94	      - —
95	      - '+0.16'
96	      - '+0.09'
97	      - '+0.19'
98	      - '+0.19'
99	      - —
100	  - name: 'Table 2: Permutation Importance (Full model, 5-fold mean)'
101	    columns:
102	    - Feature
103	    - Permutation Importance
104	    - XGBoost Gain (MVP)
105	    rows:
106	    - - entropy_mean
107	      - 0.28
108	      - 0.22
109	    - - entropy_std
110	      - 0.19
111	      - 0.13
112	    - - hapax_ratio
113	      - 0.14
114	      - 0.3
115	    - - tail_decay
116	      - 0.13
117	      - 0.06
118	    - - ttr
119	      - 0.09
120	      - 0.17
121	    - - entropy_max
122	      - 0.09
123	      - 0.07
124	    - - entropy_min
125	      - 0.08
126	      - 0.06
127	  figures_description:
128	  - 'Fig 1a: Grouped bar chart — Macro-F1 for ref-only / surface-only / full, with
129	    95% CI error bars from CV. Clear visual gap between ref-only and surface-only.'
130	  - 'Fig 1b: Per-class F1 heatmap (3 feature sets × 3 classes). Shows that the surface→ref
131	    gap is largest for gen-1 and gen-2+ (the harder classes), confirming reference
132	    features add discriminability precisely where surface shortcuts fail.'
133	  - 'Fig 1c: Permutation importance bar chart (full model) vs XGBoost gain bar chart
134	    (MVP). Side-by-side comparison reveals hapax_ratio''s gain was inflated; entropy_mean
135	    is the true top feature under permutation.'
136	  analysis: 'The ablation cleanly validates Claim 2. The ref-only advantage is strongest
137	    on gen-1 (Δ=+0.19) and gen-2+ (Δ=+0.19), the classes where surface features struggle
138	    most — TTR/hapax can separate human text from any synthetic text but cannot distinguish
139	    depth levels within synthetic text, because vocabulary impoverishment saturates
140	    quickly (mostly between gen-0→gen-1). Reference-model entropy features, by contrast,
141	    capture cumulative distributional drift that continues to grow between gen-1 and
142	    gen-2+. The reranking of feature importance under permutation (entropy_mean rises
143	    to 0.28, hapax_ratio drops to 0.14) directly addresses RC1 ("Is this just vocabulary
144	    impoverishment?") — it is not. The full model''s improvement to 0.87 suggests
145	    the two feature families capture partially orthogonal information: surface features
146	    provide a cheap gen-0 vs rest shortcut, while reference features provide the finer
147	    gen-1 vs gen-2+ signal.
148	
149	    '
150	- name: cross_generator_evaluation
151	  plan_id: plan_002
152	  description: 'Generate 25K chains: 1000 Wikipedia seeds × 5 generators (Pythia-2.8B,
153	    OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, Pythia-1B) × 5 depths. Feature extraction
154	    with Pythia-410M reference model. Leave-one-generator-out CV (train on 4 generators,
155	    test on held-out generator). Also report per-generator in-distribution results
156	    and per-class breakdowns.
157	
158	    '
159	  expected_results:
160	    leave_one_out_macro_f1_mean: 0.78
161	    leave_one_out_macro_f1_std: 0.03
162	    leave_one_out_gen1_f1_mean: 0.73
163	    leave_one_out_gen2plus_f1_mean: 0.75
164	    leave_one_out_gen0_f1_mean: 0.88
165	    in_distribution_5fold_macro_f1: 0.86
166	    per_generator_held_out:
167	      pythia_2_8b: 0.81
168	      olmo_2_1b: 0.77
169	      qwen3_5_2b: 0.76
170	      qwen3_5_0_8b: 0.74
171	      pythia_1b: 0.82
172	    total_chains_generated: 24200
173	    attrition_rate_pct: 3.2
174	    generation_gpu_hours: 18.5
175	  result_rationale: 'Cross-generator generalization holds (mean leave-one-out F1=0.78)
176	    because distributional drift is measured from the reference model''s perspective,
177	    not the generator''s. All generators produce text that progressively deviates
178	    from human text distribution as measured by Pythia-410M; the drift trajectory
179	    differs in magnitude but shares the same directional pattern (entropy increases,
180	    tail probability mass shifts). Pythia-family generators (2.8B, 1B) transfer best
181	    to each other (F1=0.81–0.82) due to shared pretraining distribution. Qwen3.5-0.8B
182	    is the hardest held-out case (F1=0.74) because its smaller capacity produces qualitatively
183	    different text that drifts faster at early depths — the classifier trained on
184	    larger models underestimates Qwen-0.8B''s depth. The gen-1 vs gen-2+ boundary
185	    remains the bottleneck (gen-1 F1=0.73) because gen-1 text from some generators
186	    overlaps with gen-2+ text from others in feature space. In-distribution pooled
187	    performance (0.86) is close to MVP (0.84) despite mixing generators, confirming
188	    that generator diversity adds training signal rather than noise. Attrition (~3.2%)
189	    is lower than MVP (3.7%) due to improved generation pipeline with retry logic.
190	
191	    '
192	  tables:
193	  - name: 'Table 3: Leave-One-Generator-Out Cross-Validation'
194	    columns:
195	    - Held-out Generator
196	    - Macro-F1
197	    - gen-0 F1
198	    - gen-1 F1
199	    - gen-2+ F1
200	    rows:
201	    - - Pythia-2.8B
202	      - 0.81
203	      - 0.91
204	      - 0.75
205	      - 0.77
206	    - - OLMo-2-1B
207	      - 0.77
208	      - 0.87
209	      - 0.72
210	      - 0.73
211	    - - Qwen3.5-2B
212	      - 0.76
213	      - 0.86
214	      - 0.71
215	      - 0.72
216	    - - Qwen3.5-0.8B
217	      - 0.74
218	      - 0.84
219	      - 0.68
220	      - 0.7
221	    - - Pythia-1B
222	      - 0.82
223	      - 0.92
224	      - 0.76
225	      - 0.78
226	    - - Mean ± std
227	      - 0.78 ± 0.03
228	      - 0.88 ± 0.03
229	      - 0.73 ± 0.03
230	      - 0.75 ± 0.03
231	  - name: 'Table 4: Per-Generator In-Distribution 5-Fold CV'
232	    columns:
233	    - Generator
234	    - Macro-F1
235	    - CV std
236	    rows:
237	    - - Pythia-2.8B
238	      - 0.85
239	      - 0.014
240	    - - OLMo-2-1B
241	      - 0.84
242	      - 0.016
243	    - - Qwen3.5-2B
244	      - 0.86
245	      - 0.013
246	    - - Qwen3.5-0.8B
247	      - 0.83
248	      - 0.019
249	    - - Pythia-1B
250	      - 0.84
251	      - 0.015
252	    - - Pooled (all 5)
253	      - 0.86
254	      - 0.011
255	  figures_description:
256	  - 'Fig 2a: Leave-one-out macro-F1 bar chart with error bars, generators ordered
257	    by held-out performance. Horizontal dashed line at 0.78 (mean). Shows Pythia-family
258	    clusters above mean, Qwen-0.8B below.'
259	  - 'Fig 2b: Confusion matrix heatmaps (5 panels, one per held-out generator). Highlights
260	    that gen-1↔gen-2+ confusion is the primary failure mode across all generators.'
261	  - 'Fig 2c: t-SNE of reference-model features colored by depth, faceted by generator.
262	    Shows that depth clusters are geometrically similar across generators despite
263	    generator-specific offsets in feature space.'
264	  analysis: 'The 0.78 mean leave-one-out F1 with narrow std (0.03) strongly supports
265	    Claim 1''s cross-generator generalization. The pattern is consistent: gen-0 is
266	    always well-separated (F1≥0.84), while gen-1 and gen-2+ form a harder boundary.
267	    Pythia-family transfer is strongest, suggesting some same-family distributional
268	    similarity, but even cross-family transfer (Pythia→Qwen) maintains F1≥0.74. This
269	    confirms the distributional fingerprint is a property of the generation process,
270	    not a generator-specific artifact. The pooled in-distribution result (0.86) exceeding
271	    any single-generator result suggests that multi-generator training improves robustness.
272	    For the paper, this table is the centerpiece of Claim 1 and directly addresses
273	    RC2.
274	
275	    '
276	- name: cross_family_reference_model
277	  plan_id: plan_003
278	  description: 'Re-extract features using non-Pythia reference models (OLMo-2-1B,
279	    Qwen3.5-0.8B) on the plan_002 dataset (25K chains). Compare classification performance
280	    across 3 reference model families. Tests whether the fingerprint is reference-model-agnostic.
281	
282	    '
283	  expected_results:
284	    pythia_410m_ref_macro_f1: 0.86
285	    olmo_2_1b_ref_macro_f1: 0.76
286	    qwen3_5_0_8b_ref_macro_f1: 0.74
287	    ensemble_3refs_macro_f1: 0.88
288	    cross_ref_leave_one_out_macro_f1: 0.75
289	    feature_correlation_pythia_olmo_entropy_mean: 0.82
290	    feature_correlation_pythia_qwen_entropy_mean: 0.78
291	  result_rationale: 'All three reference models detect depth signal (F1≥0.74) because
292	    any well-trained LM assigns progressively lower probability to deeper-generation
293	    text — the drift is a property of the text, not the measuring instrument. Pythia-410M
294	    performs best (0.86) because it was the reference model used during pipeline development
295	    and its capacity is calibrated for sensitivity to distributional shifts (small
296	    enough to be "surprised" by drift, large enough to model human text well). OLMo-2-1B
297	    (0.76) and Qwen3.5-0.8B (0.74) are slightly weaker because their different pretraining
298	    distributions create different baselines for "expected" text, adding noise to
299	    depth features. High cross-reference entropy_mean correlations (0.78–0.82) confirm
300	    that all three models agree on the direction of drift even if magnitudes differ.
301	    The 3-reference ensemble (0.88) exceeds any single reference, indicating that
302	    diverse reference models capture complementary aspects of distributional drift.
303	    This decisively addresses RC2 — the signal is not a Pythia-specific artifact.
304	
305	    '
306	  tables:
307	  - name: 'Table 5: Reference Model Comparison (pooled 5-generator data)'
308	    columns:
309	    - Reference Model
310	    - Family
311	    - Params
312	    - Macro-F1
313	    - gen-0 F1
314	    - gen-1 F1
315	    - gen-2+ F1
316	    rows:
317	    - - Pythia-410M
318	      - Pythia
319	      - 410M
320	      - 0.86
321	      - 0.95
322	      - 0.8
323	      - 0.82
324	    - - OLMo-2-1B
325	      - OLMo
326	      - 1B
327	      - 0.76
328	      - 0.88
329	      - 0.69
330	      - 0.72
331	    - - Qwen3.5-0.8B
332	      - Qwen
333	      - 0.8B
334	      - 0.74
335	      - 0.86
336	      - 0.66
337	      - 0.7
338	    - - Ensemble (3 refs)
339	      - Mixed
340	      - —
341	      - 0.88
342	      - 0.96
343	      - 0.83
344	      - 0.85
345	  - name: 'Table 6: Pairwise Feature Correlation (Spearman ρ) Across Reference Models'
346	    columns:
347	    - Feature
348	    - Pythia↔OLMo
349	    - Pythia↔Qwen
350	    - OLMo↔Qwen
351	    rows:
352	    - - entropy_mean
353	      - 0.82
354	      - 0.78
355	      - 0.8
356	    - - entropy_std
357	      - 0.79
358	      - 0.74
359	      - 0.76
360	    - - tail_decay
361	      - 0.71
362	      - 0.66
363	      - 0.69
364	  figures_description:
365	  - 'Fig 3a: Parallel coordinates plot showing entropy_mean distributions by depth,
366	    one panel per reference model. Monotonic increase with depth visible in all three,
367	    confirming H₂ across reference architectures.'
368	  - 'Fig 3b: Scatter matrix of entropy_mean values across reference model pairs, colored
369	    by depth. Strong positive correlation with depth-dependent clustering confirms
370	    cross-reference consistency.'
371	  analysis: 'The cross-family validation eliminates the concern that Pythia-410M has
372	    some idiosyncratic sensitivity to synthetic text. All three reference architectures
373	    detect monotonic distributional drift. The ensemble''s improvement to 0.88 provides
374	    an optional "best-effort" configuration for practitioners, though the single-reference
375	    Pythia-410M result (0.86) is sufficient for the paper''s claims. The correlation
376	    analysis (Table 6) is particularly informative: high but imperfect correlations
377	    indicate that reference models measure the same underlying phenomenon through
378	    slightly different lenses, explaining why ensembling helps. For the paper, this
379	    experiment transforms a potential weakness (Pythia-only evaluation) into a strength
380	    (reference-model-agnostic signal).
381	
382	    '
383	- name: downstream_utility
384	  plan_id: plan_004
385	  description: 'Fine-tune Pythia-410M on depth-stratified subsets of the plan_002
386	    data. Measure perplexity on held-out human test set as function of training data
387	    depth composition. Compare depth-aware filtering (keep gen-0 + gen-1, discard
388	    gen-2+) vs binary baselines (FastDetectGPT threshold, LD-Score threshold) for
389	    preserving downstream model quality.
390	
391	    '
392	  expected_results:
393	    depth_quality_spearman_rho: 0.72
394	    ppl_gen0_only: 28.3
395	    ppl_gen1_only: 30.1
396	    ppl_gen2_only: 34.7
397	    ppl_gen3_only: 38.9
398	    ppl_gen4_only: 43.2
399	    ppl_mixed_uniform: 35.8
400	    ppl_depth_filtered_gen01: 29.0
401	    ppl_binary_fastdetectgpt: 31.8
402	    ppl_binary_ldscore: 32.1
403	    ppl_human_baseline: 27.5
404	    depth_filter_vs_binary_gap_pct: 5.2
405	    training_samples_kept_depth_filter: 0.42
406	    training_samples_kept_binary: 0.28
407	  result_rationale: 'Perplexity increases monotonically with training data depth (28.3→43.2
408	    from gen-0→gen-4) because deeper-generation text has compounded distributional
409	    drift from human text — fine-tuning on it shifts the model''s learned distribution
410	    away from the human test set. The Spearman ρ=0.72 between depth and perplexity
411	    is strong but not perfect because individual samples vary in drift magnitude (some
412	    gen-3 texts are less drifted than some gen-2 texts). Depth-aware filtering (keep
413	    gen-0+gen-1, perplexity=29.0) outperforms binary baselines (~31.8–32.1) by 5.2%
414	    because binary detectors discard all synthetic text including useful gen-1 content
415	    that is distributionally close to human text. Binary filtering retains only 28%
416	    of data (mostly gen-0) while depth filtering retains 42% (gen-0 + gen-1), providing
417	    more training data of acceptable quality. The gap between gen-0-only (28.3) and
418	    depth-filtered (29.0) is small, confirming that gen-1 text is nearly as good as
419	    human text for training — the key practical insight for data curation.
420	
421	    '
422	  tables:
423	  - name: 'Table 7: Fine-tuning Perplexity by Training Data Depth'
424	    columns:
425	    - Training Data
426	    - Depth Composition
427	    - PPL (↓)
428	    - Samples Used
429	    rows:
430	    - - Human-only
431	      - gen-0
432	      - 28.3
433	      - ~4800
434	    - - gen-1 only
435	      - gen-1
436	      - 30.1
437	      - ~4750
438	    - - gen-2 only
439	      - gen-2
440	      - 34.7
441	      - ~4500
442	    - - gen-3 only
443	      - gen-3
444	      - 38.9
445	      - ~4200
446	    - - gen-4 only
447	      - gen-4
448	      - 43.2
449	      - ~3900
450	    - - Uniform mix
451	      - gen-0–4 equal
452	      - 35.8
453	      - ~22000
454	    - - Depth-filtered (ours)
455	      - gen-0 + gen-1
456	      - 29.0
457	      - ~9500
458	    - - FastDetectGPT filter
459	      - binary threshold
460	      - 31.8
461	      - ~6300
462	    - - LD-Score filter
463	      - binary threshold
464	      - 32.1
465	      - ~6100
466	    - - Human test baseline
467	      - —
468	      - 27.5
469	      - —
470	  - name: 'Table 8: Depth-Aware vs Binary Filtering Comparison'
471	    columns:
472	    - Method
473	    - PPL
474	    - Data Retained (%)
475	    - PPL Gap to Human-Only
476	    rows:
477	    - - Depth-filtered (gen-0+1)
478	      - 29.0
479	      - 42%
480	      - '+0.7'
481	    - - FastDetectGPT binary
482	      - 31.8
483	      - 28%
484	      - '+3.5'
485	    - - LD-Score binary
486	      - 32.1
487	      - 26%
488	      - '+3.8'
489	    - - No filtering (all data)
490	      - 35.8
491	      - 100%
492	      - '+7.5'
493	  figures_description:
494	  - 'Fig 4a: Line plot — perplexity vs generation depth (gen-0 through gen-4). Monotonic
495	    increase with 95% CI bands from 3 random seeds. Confirms H₂''s downstream consequence.'
496	  - 'Fig 4b: Bar chart comparing filtering strategies (depth-aware, FastDetectGPT,
497	    LD-Score, no filter) on perplexity and data retention. Dual y-axis: bars for perplexity,
498	    overlaid line for % data retained.'
499	  - 'Fig 4c: Scatter plot — predicted depth score vs actual fine-tuning perplexity
500	    contribution per sample, with Spearman ρ annotation. Shows the sample-level correlation
501	    between depth estimate and quality impact.'
502	  analysis: 'This experiment validates Claim 3 and provides the practical punchline
503	    of the paper. The monotonic perplexity curve (Fig 4a) is the most intuitive visualization
504	    of H₂ — it translates distributional drift into a metric practitioners care about.
505	    The 5.2% gap between depth-aware and binary filtering is meaningful because it
506	    comes with MORE data retained (42% vs 28%), resolving the precision-recall tradeoff
507	    that plagues binary detection. The key insight is that gen-1 text is "good enough"
508	    for training (PPL=30.1 vs human 28.3), but gen-2+ is not (PPL≥34.7). Binary detectors
509	    cannot make this distinction. For AAAI reviewers, this experiment connects the
510	    theoretical contribution (distributional drift characterization) to a practical
511	    application (data curation), which is important for venue fit.
512	
513	    '
514	- name: prompt_type_comparison
515	  plan_id: plan_005
516	  description: 'Generate chains with 3 prompt types (continuation, elaboration, inspired_rewriting)
517	    using Pythia-2.8B on 1000 Wikipedia seeds × 5 depths. Compare depth signal preservation
518	    across prompt types. Tests whether semantic divergence from source correlates
519	    with depth signal.
520	
521	    '
522	  expected_results:
523	    continuation_macro_f1: 0.85
524	    elaboration_macro_f1: 0.8
525	    inspired_rewriting_macro_f1: 0.72
526	    continuation_entropy_drift_per_depth: 0.18
527	    elaboration_entropy_drift_per_depth: 0.14
528	    inspired_rewriting_entropy_drift_per_depth: 0.1
529	    cross_prompt_train_test_macro_f1: 0.74
530	    prompt_type_drift_rate_spearman: 0.91
531	  result_rationale: 'Continuation preserves the strongest depth signal (F1=0.85) because
532	    each generation step continues directly from the previous output, maximizing the
533	    accumulation of distributional drift. Elaboration (F1=0.80) injects some new semantic
534	    direction via the prompt instruction, which partially resets the drift trajectory
535	    at each step — drift still accumulates but at a slower rate. Inspired rewriting
536	    (F1=0.72) has the most semantic freedom: the model is instructed to produce text
537	    "inspired by" the input, allowing it to diverge from the drift trajectory and
538	    partially re-anchor to its pretraining distribution. The strong correlation between
539	    per-depth entropy drift rate and classification F1 (Spearman ρ=0.91) confirms
540	    the theoretical prediction: more constrained generation → faster drift accumulation
541	    → stronger depth signal. Cross-prompt-type transfer (F1=0.74) is moderate, indicating
542	    that the drift signature is partially shared across prompt types but the rate
543	    differences create distribution shift in feature space.
544	
545	    '
546	  tables:
547	  - name: 'Table 9: Depth Classification by Prompt Type'
548	    columns:
549	    - Prompt Type
550	    - Macro-F1
551	    - gen-0 F1
552	    - gen-1 F1
553	    - gen-2+ F1
554	    - Entropy Drift Rate
555	    rows:
556	    - - Continuation
557	      - 0.85
558	      - 0.95
559	      - 0.79
560	      - 0.81
561	      - 0.18 nats/depth
562	    - - Elaboration
563	      - 0.8
564	      - 0.92
565	      - 0.73
566	      - 0.75
567	      - 0.14 nats/depth
568	    - - Inspired rewriting
569	      - 0.72
570	      - 0.86
571	      - 0.64
572	      - 0.67
573	      - 0.10 nats/depth
574	  figures_description:
575	  - 'Fig 5a: Line plots — entropy_mean vs depth for each prompt type, showing different
576	    drift rates. Continuation has steepest slope.'
577	  - 'Fig 5b: Scatter plot — prompt type drift rate vs macro-F1, confirming linear
578	    relationship. Three points with regression line and ρ annotation.'
579	  analysis: 'This experiment decomposes the depth signal by generation modality. The
580	    ordering (continuation > elaboration > inspired rewriting) aligns with the theoretical
581	    framework: the more the generation task constrains the output to build on previous
582	    text, the more drift accumulates. Inspired rewriting''s lower F1 is not a failure
583	    — it confirms the mechanism. For the paper, this comparison strengthens the theoretical
584	    story by showing that depth signal is graded, not binary, and correlates with
585	    the degree of semantic coupling between successive generation steps.
586	
587	    '
588	- name: paraphrastic_comparison
589	  plan_id: plan_006
590	  description: 'Construct parallel paraphrasing chains (same 1000 seeds, Pythia-2.8B,
591	    5 depths) alongside continuation chains. Measure whether paraphrastic chains converge
592	    (per attractor theory) while continuation chains diverge (our H₂). Direct empirical
593	    test of H₁ vs H₂.
594	
595	    '
596	  expected_results:
597	    paraphrase_macro_f1_3class: 0.58
598	    paraphrase_gen0_f1: 0.81
599	    paraphrase_gen1_f1: 0.46
600	    paraphrase_gen2plus_f1: 0.47
601	    continuation_macro_f1_3class: 0.85
602	    paraphrase_entropy_drift_depth3: 0.06
603	    continuation_entropy_drift_depth3: 0.52
604	    paraphrase_cycle_detection_pct: 68.0
605	    divergence_test_ks_statistic: 0.41
606	    divergence_test_p_value: 1.0e-05
607	  result_rationale: 'Paraphrastic chains show weak depth signal (F1=0.58) because
608	    the semantic preservation constraint of paraphrasing creates attractor dynamics
609	    — the text oscillates around a fixed semantic point, and distributional features
610	    converge after ~2 steps (confirming ACL 2025 attractor cycle theory). By depth
611	    3, paraphrastic entropy drift has nearly plateaued (0.06 nats) while continuation
612	    drift continues growing (0.52 nats). The 68% cycle detection rate in paraphrastic
613	    chains (text at depth d is more similar to depth d-2 than d-1) directly corroborates
614	    the 2-period attractor cycle prediction. Continuation chains show no such periodicity
615	    — drift is monotonic. The KS test between depth-3 entropy distributions of paraphrastic
616	    vs continuation chains (D=0.41, p<0.001) provides the statistical test of H₁ vs
617	    H₂. This is the most theoretically clean result in the paper: H₂ (divergence)
618	    holds for non-paraphrastic chains, H₁ (convergence) holds for paraphrastic chains,
619	    exactly as predicted by the semantic constraint difference.
620	
621	    '
622	  tables:
623	  - name: 'Table 10: Paraphrastic vs Continuation Chain Comparison'
624	    columns:
625	    - Chain Type
626	    - Macro-F1
627	    - Entropy Drift @depth3
628	    - Cycle Detection %
629	    rows:
630	    - - Continuation
631	      - 0.85
632	      - 0.52 nats
633	      - < 5%
634	    - - Paraphrasing
635	      - 0.58
636	      - 0.06 nats
637	      - 68%
638	    - - Δ
639	      - '+0.27'
640	      - +0.46 nats
641	      - —
642	  figures_description:
643	  - 'Fig 6a: Dual-panel line plot — entropy_mean vs depth for continuation (diverging)
644	    and paraphrasing (converging). The visual contrast is the paper''s most compelling
645	    figure.'
646	  - 'Fig 6b: Autocorrelation plot of entropy_mean sequence across depths for paraphrastic
647	    chains, showing the period-2 oscillation pattern predicted by attractor theory.'
648	  analysis: 'This is the experiment that elevates the paper from "a depth classifier"
649	    to "an empirical test of distributional dynamics in recursive generation." The
650	    clean separation between convergent (paraphrastic) and divergent (non-paraphrastic)
651	    chains validates the core theoretical insight and connects our work to the ACL
652	    2025 attractor cycle literature. H₂ is confirmed for non-paraphrastic chains:
653	    drift accumulates monotonically, enabling depth estimation. H₁ is confirmed for
654	    paraphrastic chains: convergence limits depth signal to ~2 classes. This dual
655	    result explains WHY our approach works and WHY prior work on paraphrasing chains
656	    found limited depth discriminability.
657	
658	    '
659	- name: cross_model_chains
660	  plan_id: plan_007
661	  description: 'Generate cross-model chains where each depth step uses a different
662	    generator (randomly sampled from the 5 generators). 1000 seeds × 5 depths. Compares
663	    cross-model chain depth classification to single-model chains. More realistic
664	    scenario — real web contamination involves diverse generators.
665	
666	    '
667	  expected_results:
668	    cross_model_chain_macro_f1: 0.75
669	    single_model_chain_macro_f1_mean: 0.85
670	    cross_model_gen0_f1: 0.9
671	    cross_model_gen1_f1: 0.68
672	    cross_model_gen2plus_f1: 0.67
673	    cross_model_entropy_drift_per_depth: 0.13
674	    cross_vs_single_model_delta: -0.1
675	  result_rationale: 'Cross-model chains are harder to classify (F1=0.75 vs single-model
676	    0.85) because generator switching introduces distributional discontinuities —
677	    each new generator has its own distributional signature that partially masks the
678	    monotonic drift signal. However, F1=0.75 is still well above chance (0.33) and
679	    practically useful, because the underlying drift phenomenon persists: even when
680	    generators change, the cumulative deviation from human text distribution still
681	    increases with depth. The gen-1 and gen-2+ classes are most affected (F1=0.68,
682	    0.67) because generator-switching noise is most confusing for the middle classes.
683	    Gen-0 remains well-separated (F1=0.90) because human text is fundamentally different
684	    from any generator''s output. The 10-point drop from single-model is a known cost
685	    that should be reported transparently — it bounds the method''s real-world applicability
686	    but does not invalidate the approach. Entropy drift rate (0.13 nats/depth) is
687	    lower than single-model continuation (0.18) because generator transitions partially
688	    reset drift.
689	
690	    '
691	  tables:
692	  - name: 'Table 11: Single-Model vs Cross-Model Chain Comparison'
693	    columns:
694	    - Chain Type
695	    - Macro-F1
696	    - gen-0 F1
697	    - gen-1 F1
698	    - gen-2+ F1
699	    rows:
700	    - - Single-model (mean of 5)
701	      - 0.85
702	      - 0.95
703	      - 0.79
704	      - 0.81
705	    - - Cross-model (random switch)
706	      - 0.75
707	      - 0.9
708	      - 0.68
709	      - 0.67
710	    - - Δ
711	      - '-0.10'
712	      - '-0.05'
713	      - '-0.11'
714	      - '-0.14'
715	  figures_description:
716	  - 'Fig 7: Box plot of entropy_mean by depth for cross-model chains. Wider boxes
717	    than single-model chains reflect generator-switching variance, but median still
718	    increases monotonically.'
719	  analysis: 'The 10-point F1 drop is the honest cost of ecological validity. Reviewers
720	    (RC4) will ask about this — reporting it transparently strengthens the paper.
721	    The key takeaway is that depth signal survives cross-model chains despite generator-switching
722	    noise, maintaining F1=0.75. For practical data curation, this means depth-aware
723	    filtering still provides value even when contamination sources are diverse. The
724	    fact that gen-0 F1 remains at 0.90 means the method''s primary utility (separating
725	    human from any-depth synthetic) is robust; the finer-grained depth estimation
726	    within synthetic text is where accuracy degrades.
727	
728	    '
729	- name: multi_domain_seeds
730	  plan_id: plan_008
731	  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific
732	    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5
733	    generators × 5 depths. Tests domain generalization of depth signal.
734	
735	    '
736	  expected_results:
737	    wikipedia_macro_f1: 0.86
738	    news_macro_f1: 0.83
739	    scientific_macro_f1: 0.81
740	    creative_macro_f1: 0.78
741	    cross_domain_leave_one_out_f1: 0.77
742	    pooled_all_domains_f1: 0.84
743	    domain_variance_of_f1: 0.0009
744	  result_rationale: 'Wikipedia performs best (0.86) because it matches the MVP setting
745	    and has the most structured, information-dense text that generators struggle to
746	    faithfully continue. News is close (0.83) due to similar factual density. Scientific
747	    text (0.81) has domain-specific vocabulary that somewhat masks depth drift in
748	    surface features, but reference-model features still capture the signal. Creative
749	    writing is hardest (0.78) because generators produce more fluent, human-like creative
750	    text — the distributional gap between human and generated creative writing is
751	    smaller than for factual domains, reducing the overall drift magnitude. Cross-domain
752	    leave-one-out (0.77) confirms that the depth signal generalizes across domains,
753	    though some domain-specific calibration is lost. The low variance (0.0009) across
754	    domains indicates that depth signal is a robust, domain-general phenomenon. Pooled
755	    performance (0.84) suggests that multi-domain training is beneficial — diverse
756	    training data helps the classifier learn domain-invariant depth features.
757	
758	    '
759	  tables:
760	  - name: 'Table 12: Multi-Domain Depth Classification'
761	    columns:
762	    - Domain
763	    - Seeds
764	    - Macro-F1
765	    - gen-0 F1
766	    - gen-1 F1
767	    - gen-2+ F1
768	    rows:
769	    - - Wikipedia
770	      - 500
771	      - 0.86
772	      - 0.95
773	      - 0.8
774	      - 0.82
775	    - - News
776	      - 500
777	      - 0.83
778	      - 0.93
779	      - 0.77
780	      - 0.79
781	    - - Scientific
782	      - 500
783	      - 0.81
784	      - 0.91
785	      - 0.74
786	      - 0.77
787	    - - Creative
788	      - 500
789	      - 0.78
790	      - 0.88
791	      - 0.71
792	      - 0.74
793	    - - Pooled (all)
794	      - 2000
795	      - 0.84
796	      - 0.93
797	      - 0.78
798	      - 0.8
799	    - - Leave-one-domain-out
800	      - —
801	      - 0.77
802	      - 0.88
803	      - 0.7
804	      - 0.73
805	  figures_description:
806	  - 'Fig 8: Faceted violin plot of entropy_mean by depth, one panel per domain. All
807	    domains show monotonic drift but with different baseline offsets and drift rates.'
808	  analysis: 'Domain generalization confirms that distributional drift is not an artifact
809	    of Wikipedia-style text. The ordering (factual > creative) is interpretable and
810	    provides nuance for practitioners: depth estimation is most reliable for factual
811	    domains where generators have clear distributional signatures. The cross-domain
812	    leave-one-out result (0.77) is strong enough to claim domain generalization in
813	    the paper. For AAAI, including 4 domains in the evaluation addresses RC6 and demonstrates
814	    ecological validity.
815	
816	    '
817	- name: finer_grained_ordinal
818	  plan_id: plan_009
819	  description: '5-class ordinal classification (gen-0 through gen-4) on the plan_002
820	    data. Tests whether non-paraphrastic chains support finer-grained depth estimation
821	    beyond the 3-class setup.
822	
823	    '
824	  expected_results:
825	    ordinal_5class_macro_f1: 0.62
826	    ordinal_5class_gen0_f1: 0.92
827	    ordinal_5class_gen1_f1: 0.68
828	    ordinal_5class_gen2_f1: 0.52
829	    ordinal_5class_gen3_f1: 0.48
830	    ordinal_5class_gen4_f1: 0.51
831	    ordinal_mae: 0.58
832	    ordinal_spearman_rho: 0.83
833	    adjacent_class_confusion_pct: 72.0
834	  result_rationale: '5-class F1 (0.62) is lower than 3-class (0.86) because deeper
835	    classes (gen-2/gen-3/gen-4) have progressively overlapping feature distributions
836	    — drift accumulates but with diminishing marginal signal per step. Gen-0 remains
837	    easy (F1=0.92), gen-1 is moderate (F1=0.68), and gen-2/3/4 are difficult (F1≈0.48–0.52)
838	    because the distributional differences between adjacent deep classes are small.
839	    However, the high Spearman ρ (0.83) and low MAE (0.58) indicate that the classifier''s
840	    errors are ordinal — when it misclassifies, it predicts an adjacent class (72%
841	    of errors are off-by-one), not a distant one. This supports ordinal regression
842	    as a natural formulation and suggests that while exact depth prediction is noisy
843	    for deep classes, the relative ordering is preserved. For the paper, this result
844	    supports the claim that drift is monotonic (H₂) while honestly reporting the practical
845	    ceiling on depth resolution.
846	
847	    '
848	  tables:
849	  - name: 'Table 13: 5-Class Ordinal Depth Classification'
850	    columns:
851	    - Class
852	    - Precision
853	    - Recall
854	    - F1
855	    rows:
856	    - - gen-0
857	      - 0.93
858	      - 0.91
859	      - 0.92
860	    - - gen-1
861	      - 0.66
862	      - 0.7
863	      - 0.68
864	    - - gen-2
865	      - 0.5
866	      - 0.54
867	      - 0.52
868	    - - gen-3
869	      - 0.47
870	      - 0.49
871	      - 0.48
872	    - - gen-4
873	      - 0.53
874	      - 0.5
875	      - 0.51
876	    - - Macro
877	      - —
878	      - —
879	      - 0.62
880	  - name: 'Table 13b: Ordinal Error Analysis'
881	    columns:
882	    - Metric
883	    - Value
884	    rows:
885	    - - MAE
886	      - 0.58
887	    - - Spearman ρ (pred vs true depth)
888	      - 0.83
889	    - - Adjacent-class confusion (%)
890	      - 72%
891	  figures_description:
892	  - 'Fig 9a: 5×5 confusion matrix heatmap. Diagonal + adjacent-diagonal cells are
893	    dark, confirming ordinal error structure.'
894	  - 'Fig 9b: Predicted depth (box plot) vs true depth. Boxes overlap for gen-2/3/4
895	    but medians increase monotonically.'
896	  analysis: 'The 5-class result characterizes the resolution ceiling of distributional
897	    fingerprints. While exact depth-4 vs depth-3 discrimination is weak, the ordinal
898	    structure is strong (ρ=0.83). This has practical implications: for data curation,
899	    coarse depth buckets (gen-0 / gen-1 / gen-2+) are more useful than exact depth
900	    anyway — the key decision boundary is "how much drift is tolerable." The result
901	    also differentiates our work from attractor theory: paraphrastic chains converge
902	    to ~2 distinguishable classes, while our non-paraphrastic chains support at least
903	    3 clean classes and 5 ordinal classes. This directly addresses RC3.
904	
905	    '
906	- name: human_edit_robustness
907	  plan_id: plan_010
908	  description: 'Robustness test on plan_002 data with simulated edits: (A) random
909	    word replacement at 5%, 10%, 20% rates, (B) LLM-simulated light editing (rephrase
910	    random sentences). Tests depth signal persistence under post-generation editing.
911	
912	    '
913	  expected_results:
914	    no_edit_macro_f1: 0.86
915	    random_5pct_macro_f1: 0.83
916	    random_10pct_macro_f1: 0.78
917	    random_20pct_macro_f1: 0.67
918	    llm_light_edit_macro_f1: 0.76
919	    degradation_slope_per_10pct: -0.095
920	  result_rationale: 'Random word replacement at 5% has minimal impact (F1=0.83, Δ=-0.03)
921	    because replacing 5% of tokens introduces noise uniformly across all depth classes,
922	    preserving the relative distributional differences. At 10% (F1=0.78), the noise
923	    begins to mask depth-specific features — entropy statistics become noisier as
924	    random words inject unpredictable surprise values. At 20% (F1=0.67), substantial
925	    text corruption disrupts the distributional fingerprint significantly but performance
926	    remains above chance (0.33). LLM-simulated editing (F1=0.76) is comparable to
927	    10% random replacement because light rephrasing changes surface statistics but
928	    largely preserves the underlying distributional structure — the edited text still
929	    occupies the same region of reference-model feature space. The degradation is
930	    approximately linear (-0.095 F1 per 10% edit rate), providing a simple model for
931	    practitioners to assess signal reliability given estimated editing rates. These
932	    results address RC5 while honestly reporting the method''s sensitivity to post-generation
933	    modification.
934	
935	    '
936	  tables:
937	  - name: 'Table 14: Robustness to Simulated Edits'
938	    columns:
939	    - Edit Type
940	    - Edit Rate
941	    - Macro-F1
942	    - Δ from No-Edit
943	    rows:
944	    - - None (baseline)
945	      - 0%
946	      - 0.86
947	      - —
948	    - - Random word replacement
949	      - 5%
950	      - 0.83
951	      - '-0.03'
952	    - - Random word replacement
953	      - 10%
954	      - 0.78
955	      - '-0.08'
956	    - - Random word replacement
957	      - 20%
958	      - 0.67
959	      - '-0.19'
960	    - - LLM light editing
961	      - ~8–12%
962	      - 0.76
963	      - '-0.10'
964	  figures_description:
965	  - 'Fig 10: Line plot — macro-F1 vs edit rate. Linear degradation with 95% CI band.
966	    Horizontal dashed line at chance level (0.33). Annotation at 10% edit rate: ''typical
967	    human editing range.'''
968	  analysis: 'The robustness profile is realistic for practical deployment. Light editing
969	    (5–10%) typical of human post-processing preserves most of the depth signal. Heavy
970	    editing (20%) degrades performance significantly but remains above chance, suggesting
971	    that even heavily edited text retains some distributional fingerprint. For the
972	    paper, this experiment provides the necessary caveat about real-world applicability
973	    while showing that the method is viable for the most common use case (lightly
974	    edited or unedited synthetic text in web-scraped data).
975	
976	    '
977	- name: ld_score_feature
978	  plan_id: plan_011
979	  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)
980	    as an additional feature to the plan_001 ablation framework. Tests whether character-level
981	    features provide complementary depth signal beyond token-level distributional
982	    features.
983	
984	    '
985	  expected_results:
986	    full_plus_ld_macro_f1: 0.88
987	    ld_score_only_macro_f1: 0.59
988	    ld_score_permutation_importance: 0.06
989	    full_plus_ld_vs_full_delta: 0.01
990	  result_rationale: 'LD-Score alone achieves modest depth discrimination (F1=0.59)
991	    because character-level distributional signatures capture some depth-dependent
992	    patterns — deeper generation text has slightly more uniform character distributions
993	    as vocabulary impoverishment affects character-level statistics. However, adding
994	    LD-Score to the full feature set provides only marginal improvement (Δ=+0.01)
995	    because LD-Score''s signal is largely redundant with existing surface features
996	    (TTR, hapax_ratio) — both measure vocabulary impoverishment, just at different
997	    granularities (character vs word level). The low permutation importance (0.06)
998	    confirms that LD-Score is not providing new information. This is a useful negative-ish
999	    result: it shows that character-level features do not add a fundamentally new
1000	    signal modality, reinforcing that the key complementary feature families are surface
1001	    vocabulary statistics and reference-model distributional features.
1002	
1003	    '
1004	  tables:
1005	  - name: 'Table 15: LD-Score Feature Integration'
1006	    columns:
1007	    - Feature Set
1008	    - Macro-F1
1009	    - Δ from Full
1010	    rows:
1011	    - - Full (7 features)
1012	      - 0.87
1013	      - —
1014	    - - Full + LD-Score (8 features)
1015	      - 0.88
1016	      - '+0.01'
1017	    - - LD-Score only
1018	      - 0.59
1019	      - '-0.28'
1020	  figures_description:
1021	  - 'Fig S1 (supplementary): Feature importance bar chart with LD-Score included.
1022	    LD-Score ranks below all reference-model features.'
1023	  analysis: 'A clean but unexciting result that belongs in the supplementary material.
1024	    It confirms the two-modality structure of depth signal (reference-model entropy
1025	    + surface vocabulary) and shows that adding more surface-level features (even
1026	    at a different granularity) does not expand the signal envelope. For the paper,
1027	    this addresses potential questions about "what about other feature types" and
1028	    justifies the focus on reference-model features as the novel contribution.
1029	
1030	    '
1031	- name: end_to_end_classifier
1032	  plan_id: plan_012
1033	  description: 'QLoRA fine-tune Qwen3.5-0.8B for end-to-end depth classification (directly
1034	    from text, no handcrafted features). Compares learned representations vs handcrafted
1035	    distributional features on the plan_002 dataset.
1036	
1037	    '
1038	  expected_results:
1039	    qwen_qlora_macro_f1: 0.83
1040	    qwen_qlora_gen0_f1: 0.94
1041	    qwen_qlora_gen1_f1: 0.77
1042	    qwen_qlora_gen2plus_f1: 0.79
1043	    handcrafted_features_macro_f1: 0.86
1044	    qwen_qlora_cross_gen_leave_one_out_f1: 0.71
1045	    handcrafted_cross_gen_leave_one_out_f1: 0.78
1046	    qwen_qlora_training_gpu_hours: 12.0
1047	    handcrafted_training_time_minutes: 3.0
1048	  result_rationale: 'The QLoRA fine-tuned model achieves competitive in-distribution
1049	    performance (F1=0.83 vs handcrafted 0.86) because the transformer can implicitly
1050	    learn distributional features from raw text. However, it underperforms the handcrafted
1051	    approach for two reasons: (1) the handcrafted features distill the reference model''s
1052	    perspective into compact statistics that directly measure what matters (distributional
1053	    drift from human text), while the fine-tuned model must learn this implicitly
1054	    from text patterns; (2) the XGBoost classifier on 7 features is harder to overfit
1055	    than a 0.8B parameter model on ~25K training examples. The larger gap in cross-generator
1056	    leave-one-out (0.71 vs 0.78) reveals that the fine-tuned model memorizes generator-specific
1057	    artifacts more than the handcrafted features, which are designed to be generator-invariant.
1058	    The 4000× training time difference (12 GPU-hours vs 3 minutes) makes the handcrafted
1059	    approach clearly preferable for practical deployment. This result validates the
1060	    feature engineering approach over brute-force fine-tuning and justifies the paper''s
1061	    focus on interpretable distributional features.
1062	
1063	    '
1064	  tables:
1065	  - name: 'Table 16: End-to-End vs Feature-Based Comparison'
1066	    columns:
1067	    - Method
1068	    - In-Dist F1
1069	    - Cross-Gen F1
1070	    - Training Cost
1071	    rows:
1072	    - - XGBoost + handcrafted features
1073	      - 0.86
1074	      - 0.78
1075	      - 3 min
1076	    - - QLoRA Qwen3.5-0.8B
1077	      - 0.83
1078	      - 0.71
1079	      - 12 GPU·h
1080	    - - Δ (handcrafted − QLoRA)
1081	      - '+0.03'
1082	      - '+0.07'
1083	      - —
1084	  figures_description:
1085	  - 'Fig S2 (supplementary): Paired bar chart — in-distribution vs cross-generator
1086	    F1 for both methods. Handcrafted features show smaller generalization gap.'
1087	  analysis: 'This is a strategically important result. Reviewers might ask "why not
1088	    just fine-tune a model?" — this experiment shows that handcrafted features outperform,
1089	    generalize better, are 4000× cheaper to train, and are interpretable (you can
1090	    point to specific features and explain why they work). The fine-tuned model''s
1091	    worse cross-generator generalization is the most telling result: it confirms that
1092	    the handcrafted features capture the right abstraction (distributional drift as
1093	    measured by a reference model) while the fine-tuned model takes shortcuts via
1094	    generator-specific patterns. This result belongs in the supplementary material
1095	    and reinforces the paper''s methodological choice.'
1096	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d254ba59-cedf-4b78-8f3f-7f8a2453a154",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "cee190f0-ddd9-4d51-890a-f1c15e99c0e2",
  "sourceToolAssistantUUID": "d254ba59-cedf-4b78-8f3f-7f8a2453a154",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T18:43:43.174Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BSTJiRV7wLtwy5zKi5riA3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cee190f0-ddd9-4d51-890a-f1c15e99c0e2",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xKcR8DhvM8bHxqSPSv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9cbb898-6475-4834-a0a1-392799b0b22c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ugotz5JdPhxADhPayxUgiU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2111,
      "cache_creation_input_tokens": 11858,
      "cache_read_input_tokens": 23904,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2111,
          "output_tokens": 211,
          "cache_read_input_tokens": 23904,
          "cache_creation_input_tokens": 11858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11858,
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

_source line 33 · 2026-05-14T18:43:43.447Z_

<details><summary>↩ Tool result · `toolu_01BSTJiRV7wLtwy5zKi5riA3`</summary>

```text
1	narrative_guidance: 'Original framing fully intact. Story: non-paraphrastic chains
2	  exhibit monotonic distributional divergence (H₂ confirmed), detectable via reference-model
3	  entropy features that capture drift beyond surface vocabulary impoverishment. Headline:
4	  "distributional fingerprints enable risk-stratified data curation," with clean ablation
5	  separating signal from shortcut. All three claims stated at full strength. AAAI
6	  submission with no scope reduction.
7	
8	  '
9	imagined_experiments:
10	- name: feature_ablation
11	  plan_id: plan_001
12	  description: 'Ablation on existing MVP data (4609 records, Pythia-2.8B generator,
13	    Pythia-410M reference, Wikipedia seeds). Three conditions: (A) reference-only
14	    features (entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay), (B)
15	    surface-only features (ttr, hapax_ratio), (C) full 7-feature set. Same XGBoost
16	    classifier, 5-fold stratified CV, 3-class (gen-0/gen-1/gen-2+).
17	
18	    '
19	  expected_results:
20	    ref_only_macro_f1: 0.79
21	    ref_only_cv_std: 0.018
22	    ref_only_gen0_f1: 0.91
23	    ref_only_gen1_f1: 0.71
24	    ref_only_gen2plus_f1: 0.74
25	    surface_only_macro_f1: 0.63
26	    surface_only_cv_std: 0.022
27	    surface_only_gen0_f1: 0.82
28	    surface_only_gen1_f1: 0.52
29	    surface_only_gen2plus_f1: 0.55
30	    full_macro_f1: 0.87
31	    full_cv_std: 0.012
32	    full_gen0_f1: 0.96
33	    full_gen1_f1: 0.81
34	    full_gen2plus_f1: 0.83
35	    ref_minus_surface_delta: 0.16
36	    mcnemar_p_ref_vs_surface: 3.0e-05
37	    permutation_importance_entropy_mean: 0.28
38	    permutation_importance_entropy_std: 0.19
39	    permutation_importance_hapax_ratio: 0.14
40	    permutation_importance_ttr: 0.09
41	  result_rationale: 'MVP feature importance (hapax_ratio=0.30) was inflated by XGBoost''s
42	    split-gain metric, which overweights high-cardinality continuous features with
43	    many useful split points. When surface features are ablated, the 5 reference-model
44	    features retain macro-F1=0.79 because they directly measure the generator''s deviation
45	    from the reference model''s next-token distribution — a signal that accumulates
46	    monotonically with depth as the generator''s output drifts further from human
47	    text. Entropy_mean captures the average surprise under the reference model (increases
48	    with depth as generated text occupies lower-probability regions), while entropy_std
49	    captures the increasing variance of surprise (deeper text alternates between familiar
50	    patterns and novel drift). Surface features alone (F1=0.63) capture only vocabulary
51	    impoverishment — TTR and hapax_ratio decline with depth as generators recycle
52	    high-frequency tokens — but this is a weaker, noisier proxy. The 0.16 delta and
53	    significant McNemar test confirm reference features carry independent, dominant
54	    signal. The full set achieves F1=0.87 (up from MVP''s 0.84) because retuned hyperparameters
55	    on the same data with proper ablation awareness extract slightly more complementary
56	    value. Permutation importance (which avoids split-gain bias) reranks entropy_mean
57	    as the top feature.
58	
59	    '
60	  tables:
61	  - name: 'Table 1: Feature Ablation Results (3-class depth classification)'
62	    columns:
63	    - Feature Set
64	    - Features
65	    - Macro-F1
66	    - gen-0 F1
67	    - gen-1 F1
68	    - gen-2+ F1
69	    - CV std
70	    rows:
71	    - - Reference-only
72	      - entropy_{mean,std,min,max}, tail_decay
73	      - 0.79
74	      - 0.91
75	      - 0.71
76	      - 0.74
77	      - 0.018
78	    - - Surface-only
79	      - ttr, hapax_ratio
80	      - 0.63
81	      - 0.82
82	      - 0.52
83	      - 0.55
84	      - 0.022
85	    - - Full
86	      - All 7 features
87	      - 0.87
88	      - 0.96
89	      - 0.81
90	      - 0.83
91	      - 0.012
92	    - - Δ (ref − surface)
93	      - —
94	      - '+0.16'
95	      - '+0.09'
96	      - '+0.19'
97	      - '+0.19'
98	      - —
99	  - name: 'Table 2: Permutation Importance (Full model, 5-fold mean)'
100	    columns:
101	    - Feature
102	    - Permutation Importance
103	    - XGBoost Gain (MVP)
104	    rows:
105	    - - entropy_mean
106	      - 0.28
107	      - 0.22
108	    - - entropy_std
109	      - 0.19
110	      - 0.13
111	    - - hapax_ratio
112	      - 0.14
113	      - 0.3
114	    - - tail_decay
115	      - 0.13
116	      - 0.06
117	    - - ttr
118	      - 0.09
119	      - 0.17
120	    - - entropy_max
121	      - 0.09
122	      - 0.07
123	    - - entropy_min
124	      - 0.08
125	      - 0.06
126	  figures_description:
127	  - 'Fig 1a: Grouped bar chart — Macro-F1 for ref-only / surface-only / full, with
128	    95% CI error bars from CV. Clear visual gap between ref-only and surface-only.'
129	  - 'Fig 1b: Per-class F1 heatmap (3 feature sets × 3 classes). Shows that the surface→ref
130	    gap is largest for gen-1 and gen-2+ (the harder classes), confirming reference
131	    features add discriminability precisely where surface shortcuts fail.'
132	  - 'Fig 1c: Permutation importance bar chart (full model) vs XGBoost gain bar chart
133	    (MVP). Side-by-side comparison reveals hapax_ratio''s gain was inflated; entropy_mean
134	    is the true top feature under permutation.'
135	  analysis: 'The ablation cleanly validates Claim 2. The ref-only advantage is strongest
136	    on gen-1 (Δ=+0.19) and gen-2+ (Δ=+0.19), the classes where surface features struggle
137	    most — TTR/hapax can separate human text from any synthetic text but cannot distinguish
138	    depth levels within synthetic text, because vocabulary impoverishment saturates
139	    quickly (mostly between gen-0→gen-1). Reference-model entropy features, by contrast,
140	    capture cumulative distributional drift that continues to grow between gen-1 and
141	    gen-2+. The reranking of feature importance under permutation (entropy_mean rises
142	    to 0.28, hapax_ratio drops to 0.14) directly addresses RC1 ("Is this just vocabulary
143	    impoverishment?") — it is not. The full model''s improvement to 0.87 suggests
144	    the two feature families capture partially orthogonal information: surface features
145	    provide a cheap gen-0 vs rest shortcut, while reference features provide the finer
146	    gen-1 vs gen-2+ signal.
147	
148	    '
149	- name: cross_generator_evaluation
150	  plan_id: plan_002
151	  description: 'Generate 25K chains: 1000 Wikipedia seeds × 5 generators (Pythia-2.8B,
152	    OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, Pythia-1B) × 5 depths. Feature extraction
153	    with Pythia-410M reference model. Leave-one-generator-out CV (train on 4 generators,
154	    test on held-out generator). Also report per-generator in-distribution results
155	    and per-class breakdowns.
156	
157	    '
158	  expected_results:
159	    leave_one_out_macro_f1_mean: 0.78
160	    leave_one_out_macro_f1_std: 0.03
161	    leave_one_out_gen1_f1_mean: 0.73
162	    leave_one_out_gen2plus_f1_mean: 0.75
163	    leave_one_out_gen0_f1_mean: 0.88
164	    in_distribution_5fold_macro_f1: 0.86
165	    per_generator_held_out:
166	      pythia_2_8b: 0.81
167	      olmo_2_1b: 0.77
168	      qwen3_5_2b: 0.76
169	      qwen3_5_0_8b: 0.74
170	      pythia_1b: 0.82
171	    total_chains_generated: 24200
172	    attrition_rate_pct: 3.2
173	    generation_gpu_hours: 18.5
174	  result_rationale: 'Cross-generator generalization holds (mean leave-one-out F1=0.78)
175	    because distributional drift is measured from the reference model''s perspective,
176	    not the generator''s. All generators produce text that progressively deviates
177	    from human text distribution as measured by Pythia-410M; the drift trajectory
178	    differs in magnitude but shares the same directional pattern (entropy increases,
179	    tail probability mass shifts). Pythia-family generators (2.8B, 1B) transfer best
180	    to each other (F1=0.81–0.82) due to shared pretraining distribution. Qwen3.5-0.8B
181	    is the hardest held-out case (F1=0.74) because its smaller capacity produces qualitatively
182	    different text that drifts faster at early depths — the classifier trained on
183	    larger models underestimates Qwen-0.8B''s depth. The gen-1 vs gen-2+ boundary
184	    remains the bottleneck (gen-1 F1=0.73) because gen-1 text from some generators
185	    overlaps with gen-2+ text from others in feature space. In-distribution pooled
186	    performance (0.86) is close to MVP (0.84) despite mixing generators, confirming
187	    that generator diversity adds training signal rather than noise. Attrition (~3.2%)
188	    is lower than MVP (3.7%) due to improved generation pipeline with retry logic.
189	
190	    '
191	  tables:
192	  - name: 'Table 3: Leave-One-Generator-Out Cross-Validation'
193	    columns:
194	    - Held-out Generator
195	    - Macro-F1
196	    - gen-0 F1
197	    - gen-1 F1
198	    - gen-2+ F1
199	    rows:
200	    - - Pythia-2.8B
201	      - 0.81
202	      - 0.91
203	      - 0.75
204	      - 0.77
205	    - - OLMo-2-1B
206	      - 0.77
207	      - 0.87
208	      - 0.72
209	      - 0.73
210	    - - Qwen3.5-2B
211	      - 0.76
212	      - 0.86
213	      - 0.71
214	      - 0.72
215	    - - Qwen3.5-0.8B
216	      - 0.74
217	      - 0.84
218	      - 0.68
219	      - 0.7
220	    - - Pythia-1B
221	      - 0.82
222	      - 0.92
223	      - 0.76
224	      - 0.78
225	    - - Mean ± std
226	      - 0.78 ± 0.03
227	      - 0.88 ± 0.03
228	      - 0.73 ± 0.03
229	      - 0.75 ± 0.03
230	  - name: 'Table 4: Per-Generator In-Distribution 5-Fold CV'
231	    columns:
232	    - Generator
233	    - Macro-F1
234	    - CV std
235	    rows:
236	    - - Pythia-2.8B
237	      - 0.85
238	      - 0.014
239	    - - OLMo-2-1B
240	      - 0.84
241	      - 0.016
242	    - - Qwen3.5-2B
243	      - 0.86
244	      - 0.013
245	    - - Qwen3.5-0.8B
246	      - 0.83
247	      - 0.019
248	    - - Pythia-1B
249	      - 0.84
250	      - 0.015
251	    - - Pooled (all 5)
252	      - 0.86
253	      - 0.011
254	  figures_description:
255	  - 'Fig 2a: Leave-one-out macro-F1 bar chart with error bars, generators ordered
256	    by held-out performance. Horizontal dashed line at 0.78 (mean). Shows Pythia-family
257	    clusters above mean, Qwen-0.8B below.'
258	  - 'Fig 2b: Confusion matrix heatmaps (5 panels, one per held-out generator). Highlights
259	    that gen-1↔gen-2+ confusion is the primary failure mode across all generators.'
260	  - 'Fig 2c: t-SNE of reference-model features colored by depth, faceted by generator.
261	    Shows that depth clusters are geometrically similar across generators despite
262	    generator-specific offsets in feature space.'
263	  analysis: 'The 0.78 mean leave-one-out F1 with narrow std (0.03) strongly supports
264	    Claim 1''s cross-generator generalization. The pattern is consistent: gen-0 is
265	    always well-separated (F1≥0.84), while gen-1 and gen-2+ form a harder boundary.
266	    Pythia-family transfer is strongest, suggesting some same-family distributional
267	    similarity, but even cross-family transfer (Pythia→Qwen) maintains F1≥0.74. This
268	    confirms the distributional fingerprint is a property of the generation process,
269	    not a generator-specific artifact. The pooled in-distribution result (0.86) exceeding
270	    any single-generator result suggests that multi-generator training improves robustness.
271	    For the paper, this table is the centerpiece of Claim 1 and directly addresses
272	    RC2.
273	
274	    '
275	- name: cross_family_reference_model
276	  plan_id: plan_003
277	  description: 'Re-extract features using non-Pythia reference models (OLMo-2-1B,
278	    Qwen3.5-0.8B) on the plan_002 dataset (25K chains). Compare classification performance
279	    across 3 reference model families. Tests whether the fingerprint is reference-model-agnostic.
280	
281	    '
282	  expected_results:
283	    pythia_410m_ref_macro_f1: 0.86
284	    olmo_2_1b_ref_macro_f1: 0.76
285	    qwen3_5_0_8b_ref_macro_f1: 0.74
286	    ensemble_3refs_macro_f1: 0.88
287	    cross_ref_leave_one_out_macro_f1: 0.75
288	    feature_correlation_pythia_olmo_entropy_mean: 0.82
289	    feature_correlation_pythia_qwen_entropy_mean: 0.78
290	  result_rationale: 'All three reference models detect depth signal (F1≥0.74) because
291	    any well-trained LM assigns progressively lower probability to deeper-generation
292	    text — the drift is a property of the text, not the measuring instrument. Pythia-410M
293	    performs best (0.86) because it was the reference model used during pipeline development
294	    and its capacity is calibrated for sensitivity to distributional shifts (small
295	    enough to be "surprised" by drift, large enough to model human text well). OLMo-2-1B
296	    (0.76) and Qwen3.5-0.8B (0.74) are slightly weaker because their different pretraining
297	    distributions create different baselines for "expected" text, adding noise to
298	    depth features. High cross-reference entropy_mean correlations (0.78–0.82) confirm
299	    that all three models agree on the direction of drift even if magnitudes differ.
300	    The 3-reference ensemble (0.88) exceeds any single reference, indicating that
301	    diverse reference models capture complementary aspects of distributional drift.
302	    This decisively addresses RC2 — the signal is not a Pythia-specific artifact.
303	
304	    '
305	  tables:
306	  - name: 'Table 5: Reference Model Comparison (pooled 5-generator data)'
307	    columns:
308	    - Reference Model
309	    - Family
310	    - Params
311	    - Macro-F1
312	    - gen-0 F1
313	    - gen-1 F1
314	    - gen-2+ F1
315	    rows:
316	    - - Pythia-410M
317	      - Pythia
318	      - 410M
319	      - 0.86
320	      - 0.95
321	      - 0.8
322	      - 0.82
323	    - - OLMo-2-1B
324	      - OLMo
325	      - 1B
326	      - 0.76
327	      - 0.88
328	      - 0.69
329	      - 0.72
330	    - - Qwen3.5-0.8B
331	      - Qwen
332	      - 0.8B
333	      - 0.74
334	      - 0.86
335	      - 0.66
336	      - 0.7
337	    - - Ensemble (3 refs)
338	      - Mixed
339	      - —
340	      - 0.88
341	      - 0.96
342	      - 0.83
343	      - 0.85
344	  - name: 'Table 6: Pairwise Feature Correlation (Spearman ρ) Across Reference Models'
345	    columns:
346	    - Feature
347	    - Pythia↔OLMo
348	    - Pythia↔Qwen
349	    - OLMo↔Qwen
350	    rows:
351	    - - entropy_mean
352	      - 0.82
353	      - 0.78
354	      - 0.8
355	    - - entropy_std
356	      - 0.79
357	      - 0.74
358	      - 0.76
359	    - - tail_decay
360	      - 0.71
361	      - 0.66
362	      - 0.69
363	  figures_description:
364	  - 'Fig 3a: Parallel coordinates plot showing entropy_mean distributions by depth,
365	    one panel per reference model. Monotonic increase with depth visible in all three,
366	    confirming H₂ across reference architectures.'
367	  - 'Fig 3b: Scatter matrix of entropy_mean values across reference model pairs, colored
368	    by depth. Strong positive correlation with depth-dependent clustering confirms
369	    cross-reference consistency.'
370	  analysis: 'The cross-family validation eliminates the concern that Pythia-410M has
371	    some idiosyncratic sensitivity to synthetic text. All three reference architectures
372	    detect monotonic distributional drift. The ensemble''s improvement to 0.88 provides
373	    an optional "best-effort" configuration for practitioners, though the single-reference
374	    Pythia-410M result (0.86) is sufficient for the paper''s claims. The correlation
375	    analysis (Table 6) is particularly informative: high but imperfect correlations
376	    indicate that reference models measure the same underlying phenomenon through
377	    slightly different lenses, explaining why ensembling helps. For the paper, this
378	    experiment transforms a potential weakness (Pythia-only evaluation) into a strength
379	    (reference-model-agnostic signal).
380	
381	    '
382	- name: downstream_utility
383	  plan_id: plan_004
384	  description: 'Fine-tune Pythia-410M on depth-stratified subsets of the plan_002
385	    data. Measure perplexity on held-out human test set as function of training data
386	    depth composition. Compare depth-aware filtering (keep gen-0 + gen-1, discard
387	    gen-2+) vs binary baselines (FastDetectGPT threshold, LD-Score threshold) for
388	    preserving downstream model quality.
389	
390	    '
391	  expected_results:
392	    depth_quality_spearman_rho: 0.72
393	    ppl_gen0_only: 28.3
394	    ppl_gen1_only: 30.1
395	    ppl_gen2_only: 34.7
396	    ppl_gen3_only: 38.9
397	    ppl_gen4_only: 43.2
398	    ppl_mixed_uniform: 35.8
399	    ppl_depth_filtered_gen01: 29.0
400	    ppl_binary_fastdetectgpt: 31.8
401	    ppl_binary_ldscore: 32.1
402	    ppl_human_baseline: 27.5
403	    depth_filter_vs_binary_gap_pct: 5.2
404	    training_samples_kept_depth_filter: 0.42
405	    training_samples_kept_binary: 0.28
406	  result_rationale: 'Perplexity increases monotonically with training data depth (28.3→43.2
407	    from gen-0→gen-4) because deeper-generation text has compounded distributional
408	    drift from human text — fine-tuning on it shifts the model''s learned distribution
409	    away from the human test set. The Spearman ρ=0.72 between depth and perplexity
410	    is strong but not perfect because individual samples vary in drift magnitude (some
411	    gen-3 texts are less drifted than some gen-2 texts). Depth-aware filtering (keep
412	    gen-0+gen-1, perplexity=29.0) outperforms binary baselines (~31.8–32.1) by 5.2%
413	    because binary detectors discard all synthetic text including useful gen-1 content
414	    that is distributionally close to human text. Binary filtering retains only 28%
415	    of data (mostly gen-0) while depth filtering retains 42% (gen-0 + gen-1), providing
416	    more training data of acceptable quality. The gap between gen-0-only (28.3) and
417	    depth-filtered (29.0) is small, confirming that gen-1 text is nearly as good as
418	    human text for training — the key practical insight for data curation.
419	
420	    '
421	  tables:
422	  - name: 'Table 7: Fine-tuning Perplexity by Training Data Depth'
423	    columns:
424	    - Training Data
425	    - Depth Composition
426	    - PPL (↓)
427	    - Samples Used
428	    rows:
429	    - - Human-only
430	      - gen-0
431	      - 28.3
432	      - ~4800
433	    - - gen-1 only
434	      - gen-1
435	      - 30.1
436	      - ~4750
437	    - - gen-2 only
438	      - gen-2
439	      - 34.7
440	      - ~4500
441	    - - gen-3 only
442	      - gen-3
443	      - 38.9
444	      - ~4200
445	    - - gen-4 only
446	      - gen-4
447	      - 43.2
448	      - ~3900
449	    - - Uniform mix
450	      - gen-0–4 equal
451	      - 35.8
452	      - ~22000
453	    - - Depth-filtered (ours)
454	      - gen-0 + gen-1
455	      - 29.0
456	      - ~9500
457	    - - FastDetectGPT filter
458	      - binary threshold
459	      - 31.8
460	      - ~6300
461	    - - LD-Score filter
462	      - binary threshold
463	      - 32.1
464	      - ~6100
465	    - - Human test baseline
466	      - —
467	      - 27.5
468	      - —
469	  - name: 'Table 8: Depth-Aware vs Binary Filtering Comparison'
470	    columns:
471	    - Method
472	    - PPL
473	    - Data Retained (%)
474	    - PPL Gap to Human-Only
475	    rows:
476	    - - Depth-filtered (gen-0+1)
477	      - 29.0
478	      - 42%
479	      - '+0.7'
480	    - - FastDetectGPT binary
481	      - 31.8
482	      - 28%
483	      - '+3.5'
484	    - - LD-Score binary
485	      - 32.1
486	      - 26%
487	      - '+3.8'
488	    - - No filtering (all data)
489	      - 35.8
490	      - 100%
491	      - '+7.5'
492	  figures_description:
493	  - 'Fig 4a: Line plot — perplexity vs generation depth (gen-0 through gen-4). Monotonic
494	    increase with 95% CI bands from 3 random seeds. Confirms H₂''s downstream consequence.'
495	  - 'Fig 4b: Bar chart comparing filtering strategies (depth-aware, FastDetectGPT,
496	    LD-Score, no filter) on perplexity and data retention. Dual y-axis: bars for perplexity,
497	    overlaid line for % data retained.'
498	  - 'Fig 4c: Scatter plot — predicted depth score vs actual fine-tuning perplexity
499	    contribution per sample, with Spearman ρ annotation. Shows the sample-level correlation
500	    between depth estimate and quality impact.'
501	  analysis: 'This experiment validates Claim 3 and provides the practical punchline
502	    of the paper. The monotonic perplexity curve (Fig 4a) is the most intuitive visualization
503	    of H₂ — it translates distributional drift into a metric practitioners care about.
504	    The 5.2% gap between depth-aware and binary filtering is meaningful because it
505	    comes with MORE data retained (42% vs 28%), resolving the precision-recall tradeoff
506	    that plagues binary detection. The key insight is that gen-1 text is "good enough"
507	    for training (PPL=30.1 vs human 28.3), but gen-2+ is not (PPL≥34.7). Binary detectors
508	    cannot make this distinction. For AAAI reviewers, this experiment connects the
509	    theoretical contribution (distributional drift characterization) to a practical
510	    application (data curation), which is important for venue fit.
511	
512	    '
513	- name: prompt_type_comparison
514	  plan_id: plan_005
515	  description: 'Generate chains with 3 prompt types (continuation, elaboration, inspired_rewriting)
516	    using Pythia-2.8B on 1000 Wikipedia seeds × 5 depths. Compare depth signal preservation
517	    across prompt types. Tests whether semantic divergence from source correlates
518	    with depth signal.
519	
520	    '
521	  expected_results:
522	    continuation_macro_f1: 0.85
523	    elaboration_macro_f1: 0.8
524	    inspired_rewriting_macro_f1: 0.72
525	    continuation_entropy_drift_per_depth: 0.18
526	    elaboration_entropy_drift_per_depth: 0.14
527	    inspired_rewriting_entropy_drift_per_depth: 0.1
528	    cross_prompt_train_test_macro_f1: 0.74
529	    prompt_type_drift_rate_spearman: 0.91
530	  result_rationale: 'Continuation preserves the strongest depth signal (F1=0.85) because
531	    each generation step continues directly from the previous output, maximizing the
532	    accumulation of distributional drift. Elaboration (F1=0.80) injects some new semantic
533	    direction via the prompt instruction, which partially resets the drift trajectory
534	    at each step — drift still accumulates but at a slower rate. Inspired rewriting
535	    (F1=0.72) has the most semantic freedom: the model is instructed to produce text
536	    "inspired by" the input, allowing it to diverge from the drift trajectory and
537	    partially re-anchor to its pretraining distribution. The strong correlation between
538	    per-depth entropy drift rate and classification F1 (Spearman ρ=0.91) confirms
539	    the theoretical prediction: more constrained generation → faster drift accumulation
540	    → stronger depth signal. Cross-prompt-type transfer (F1=0.74) is moderate, indicating
541	    that the drift signature is partially shared across prompt types but the rate
542	    differences create distribution shift in feature space.
543	
544	    '
545	  tables:
546	  - name: 'Table 9: Depth Classification by Prompt Type'
547	    columns:
548	    - Prompt Type
549	    - Macro-F1
550	    - gen-0 F1
551	    - gen-1 F1
552	    - gen-2+ F1
553	    - Entropy Drift Rate
554	    rows:
555	    - - Continuation
556	      - 0.85
557	      - 0.95
558	      - 0.79
559	      - 0.81
560	      - 0.18 nats/depth
561	    - - Elaboration
562	      - 0.8
563	      - 0.92
564	      - 0.73
565	      - 0.75
566	      - 0.14 nats/depth
567	    - - Inspired rewriting
568	      - 0.72
569	      - 0.86
570	      - 0.64
571	      - 0.67
572	      - 0.10 nats/depth
573	  figures_description:
574	  - 'Fig 5a: Line plots — entropy_mean vs depth for each prompt type, showing different
575	    drift rates. Continuation has steepest slope.'
576	  - 'Fig 5b: Scatter plot — prompt type drift rate vs macro-F1, confirming linear
577	    relationship. Three points with regression line and ρ annotation.'
578	  analysis: 'This experiment decomposes the depth signal by generation modality. The
579	    ordering (continuation > elaboration > inspired rewriting) aligns with the theoretical
580	    framework: the more the generation task constrains the output to build on previous
581	    text, the more drift accumulates. Inspired rewriting''s lower F1 is not a failure
582	    — it confirms the mechanism. For the paper, this comparison strengthens the theoretical
583	    story by showing that depth signal is graded, not binary, and correlates with
584	    the degree of semantic coupling between successive generation steps.
585	
586	    '
587	- name: paraphrastic_comparison
588	  plan_id: plan_006
589	  description: 'Construct parallel paraphrasing chains (same 1000 seeds, Pythia-2.8B,
590	    5 depths) alongside continuation chains. Measure whether paraphrastic chains converge
591	    (per attractor theory) while continuation chains diverge (our H₂). Direct empirical
592	    test of H₁ vs H₂.
593	
594	    '
595	  expected_results:
596	    paraphrase_macro_f1_3class: 0.58
597	    paraphrase_gen0_f1: 0.81
598	    paraphrase_gen1_f1: 0.46
599	    paraphrase_gen2plus_f1: 0.47
600	    continuation_macro_f1_3class: 0.85
601	    paraphrase_entropy_drift_depth3: 0.06
602	    continuation_entropy_drift_depth3: 0.52
603	    paraphrase_cycle_detection_pct: 68.0
604	    divergence_test_ks_statistic: 0.41
605	    divergence_test_p_value: 1.0e-05
606	  result_rationale: 'Paraphrastic chains show weak depth signal (F1=0.58) because
607	    the semantic preservation constraint of paraphrasing creates attractor dynamics
608	    — the text oscillates around a fixed semantic point, and distributional features
609	    converge after ~2 steps (confirming ACL 2025 attractor cycle theory). By depth
610	    3, paraphrastic entropy drift has nearly plateaued (0.06 nats) while continuation
611	    drift continues growing (0.52 nats). The 68% cycle detection rate in paraphrastic
612	    chains (text at depth d is more similar to depth d-2 than d-1) directly corroborates
613	    the 2-period attractor cycle prediction. Continuation chains show no such periodicity
614	    — drift is monotonic. The KS test between depth-3 entropy distributions of paraphrastic
615	    vs continuation chains (D=0.41, p<0.001) provides the statistical test of H₁ vs
616	    H₂. This is the most theoretically clean result in the paper: H₂ (divergence)
617	    holds for non-paraphrastic chains, H₁ (convergence) holds for paraphrastic chains,
618	    exactly as predicted by the semantic constraint difference.
619	
620	    '
621	  tables:
622	  - name: 'Table 10: Paraphrastic vs Continuation Chain Comparison'
623	    columns:
624	    - Chain Type
625	    - Macro-F1
626	    - Entropy Drift @depth3
627	    - Cycle Detection %
628	    rows:
629	    - - Continuation
630	      - 0.85
631	      - 0.52 nats
632	      - < 5%
633	    - - Paraphrasing
634	      - 0.58
635	      - 0.06 nats
636	      - 68%
637	    - - Δ
638	      - '+0.27'
639	      - +0.46 nats
640	      - —
641	  figures_description:
642	  - 'Fig 6a: Dual-panel line plot — entropy_mean vs depth for continuation (diverging)
643	    and paraphrasing (converging). The visual contrast is the paper''s most compelling
644	    figure.'
645	  - 'Fig 6b: Autocorrelation plot of entropy_mean sequence across depths for paraphrastic
646	    chains, showing the period-2 oscillation pattern predicted by attractor theory.'
647	  analysis: 'This is the experiment that elevates the paper from "a depth classifier"
648	    to "an empirical test of distributional dynamics in recursive generation." The
649	    clean separation between convergent (paraphrastic) and divergent (non-paraphrastic)
650	    chains validates the core theoretical insight and connects our work to the ACL
651	    2025 attractor cycle literature. H₂ is confirmed for non-paraphrastic chains:
652	    drift accumulates monotonically, enabling depth estimation. H₁ is confirmed for
653	    paraphrastic chains: convergence limits depth signal to ~2 classes. This dual
654	    result explains WHY our approach works and WHY prior work on paraphrasing chains
655	    found limited depth discriminability.
656	
657	    '
658	- name: cross_model_chains
659	  plan_id: plan_007
660	  description: 'Generate cross-model chains where each depth step uses a different
661	    generator (randomly sampled from the 5 generators). 1000 seeds × 5 depths. Compares
662	    cross-model chain depth classification to single-model chains. More realistic
663	    scenario — real web contamination involves diverse generators.
664	
665	    '
666	  expected_results:
667	    cross_model_chain_macro_f1: 0.75
668	    single_model_chain_macro_f1_mean: 0.85
669	    cross_model_gen0_f1: 0.9
670	    cross_model_gen1_f1: 0.68
671	    cross_model_gen2plus_f1: 0.67
672	    cross_model_entropy_drift_per_depth: 0.13
673	    cross_vs_single_model_delta: -0.1
674	  result_rationale: 'Cross-model chains are harder to classify (F1=0.75 vs single-model
675	    0.85) because generator switching introduces distributional discontinuities —
676	    each new generator has its own distributional signature that partially masks the
677	    monotonic drift signal. However, F1=0.75 is still well above chance (0.33) and
678	    practically useful, because the underlying drift phenomenon persists: even when
679	    generators change, the cumulative deviation from human text distribution still
680	    increases with depth. The gen-1 and gen-2+ classes are most affected (F1=0.68,
681	    0.67) because generator-switching noise is most confusing for the middle classes.
682	    Gen-0 remains well-separated (F1=0.90) because human text is fundamentally different
683	    from any generator''s output. The 10-point drop from single-model is a known cost
684	    that should be reported transparently — it bounds the method''s real-world applicability
685	    but does not invalidate the approach. Entropy drift rate (0.13 nats/depth) is
686	    lower than single-model continuation (0.18) because generator transitions partially
687	    reset drift.
688	
689	    '
690	  tables:
691	  - name: 'Table 11: Single-Model vs Cross-Model Chain Comparison'
692	    columns:
693	    - Chain Type
694	    - Macro-F1
695	    - gen-0 F1
696	    - gen-1 F1
697	    - gen-2+ F1
698	    rows:
699	    - - Single-model (mean of 5)
700	      - 0.85
701	      - 0.95
702	      - 0.79
703	      - 0.81
704	    - - Cross-model (random switch)
705	      - 0.75
706	      - 0.9
707	      - 0.68
708	      - 0.67
709	    - - Δ
710	      - '-0.10'
711	      - '-0.05'
712	      - '-0.11'
713	      - '-0.14'
714	  figures_description:
715	  - 'Fig 7: Box plot of entropy_mean by depth for cross-model chains. Wider boxes
716	    than single-model chains reflect generator-switching variance, but median still
717	    increases monotonically.'
718	  analysis: 'The 10-point F1 drop is the honest cost of ecological validity. Reviewers
719	    (RC4) will ask about this — reporting it transparently strengthens the paper.
720	    The key takeaway is that depth signal survives cross-model chains despite generator-switching
721	    noise, maintaining F1=0.75. For practical data curation, this means depth-aware
722	    filtering still provides value even when contamination sources are diverse. The
723	    fact that gen-0 F1 remains at 0.90 means the method''s primary utility (separating
724	    human from any-depth synthetic) is robust; the finer-grained depth estimation
725	    within synthetic text is where accuracy degrades.
726	
727	    '
728	- name: multi_domain_seeds
729	  plan_id: plan_008
730	  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific
731	    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5
732	    generators × 5 depths. Tests domain generalization of depth signal.
733	
734	    '
735	  expected_results:
736	    wikipedia_macro_f1: 0.86
737	    news_macro_f1: 0.83
738	    scientific_macro_f1: 0.81
739	    creative_macro_f1: 0.78
740	    cross_domain_leave_one_out_f1: 0.77
741	    pooled_all_domains_f1: 0.84
742	    domain_variance_of_f1: 0.0009
743	  result_rationale: 'Wikipedia performs best (0.86) because it matches the MVP setting
744	    and has the most structured, information-dense text that generators struggle to
745	    faithfully continue. News is close (0.83) due to similar factual density. Scientific
746	    text (0.81) has domain-specific vocabulary that somewhat masks depth drift in
747	    surface features, but reference-model features still capture the signal. Creative
748	    writing is hardest (0.78) because generators produce more fluent, human-like creative
749	    text — the distributional gap between human and generated creative writing is
750	    smaller than for factual domains, reducing the overall drift magnitude. Cross-domain
751	    leave-one-out (0.77) confirms that the depth signal generalizes across domains,
752	    though some domain-specific calibration is lost. The low variance (0.0009) across
753	    domains indicates that depth signal is a robust, domain-general phenomenon. Pooled
754	    performance (0.84) suggests that multi-domain training is beneficial — diverse
755	    training data helps the classifier learn domain-invariant depth features.
756	
757	    '
758	  tables:
759	  - name: 'Table 12: Multi-Domain Depth Classification'
760	    columns:
761	    - Domain
762	    - Seeds
763	    - Macro-F1
764	    - gen-0 F1
765	    - gen-1 F1
766	    - gen-2+ F1
767	    rows:
768	    - - Wikipedia
769	      - 500
770	      - 0.86
771	      - 0.95
772	      - 0.8
773	      - 0.82
774	    - - News
775	      - 500
776	      - 0.83
777	      - 0.93
778	      - 0.77
779	      - 0.79
780	    - - Scientific
781	      - 500
782	      - 0.81
783	      - 0.91
784	      - 0.74
785	      - 0.77
786	    - - Creative
787	      - 500
788	      - 0.78
789	      - 0.88
790	      - 0.71
791	      - 0.74
792	    - - Pooled (all)
793	      - 2000
794	      - 0.84
795	      - 0.93
796	      - 0.78
797	      - 0.8
798	    - - Leave-one-domain-out
799	      - —
800	      - 0.77
801	      - 0.88
802	      - 0.7
803	      - 0.73
804	  figures_description:
805	  - 'Fig 8: Faceted violin plot of entropy_mean by depth, one panel per domain. All
806	    domains show monotonic drift but with different baseline offsets and drift rates.'
807	  analysis: 'Domain generalization confirms that distributional drift is not an artifact
808	    of Wikipedia-style text. The ordering (factual > creative) is interpretable and
809	    provides nuance for practitioners: depth estimation is most reliable for factual
810	    domains where generators have clear distributional signatures. The cross-domain
811	    leave-one-out result (0.77) is strong enough to claim domain generalization in
812	    the paper. For AAAI, including 4 domains in the evaluation addresses RC6 and demonstrates
813	    ecological validity.
814	
815	    '
816	- name: finer_grained_ordinal
817	  plan_id: plan_009
818	  description: '5-class ordinal classification (gen-0 through gen-4) on the plan_002
819	    data. Tests whether non-paraphrastic chains support finer-grained depth estimation
820	    beyond the 3-class setup.
821	
822	    '
823	  expected_results:
824	    ordinal_5class_macro_f1: 0.62
825	    ordinal_5class_gen0_f1: 0.92
826	    ordinal_5class_gen1_f1: 0.68
827	    ordinal_5class_gen2_f1: 0.52
828	    ordinal_5class_gen3_f1: 0.48
829	    ordinal_5class_gen4_f1: 0.51
830	    ordinal_mae: 0.58
831	    ordinal_spearman_rho: 0.83
832	    adjacent_class_confusion_pct: 72.0
833	  result_rationale: '5-class F1 (0.62) is lower than 3-class (0.86) because deeper
834	    classes (gen-2/gen-3/gen-4) have progressively overlapping feature distributions
835	    — drift accumulates but with diminishing marginal signal per step. Gen-0 remains
836	    easy (F1=0.92), gen-1 is moderate (F1=0.68), and gen-2/3/4 are difficult (F1≈0.48–0.52)
837	    because the distributional differences between adjacent deep classes are small.
838	    However, the high Spearman ρ (0.83) and low MAE (0.58) indicate that the classifier''s
839	    errors are ordinal — when it misclassifies, it predicts an adjacent class (72%
840	    of errors are off-by-one), not a distant one. This supports ordinal regression
841	    as a natural formulation and suggests that while exact depth prediction is noisy
842	    for deep classes, the relative ordering is preserved. For the paper, this result
843	    supports the claim that drift is monotonic (H₂) while honestly reporting the practical
844	    ceiling on depth resolution.
845	
846	    '
847	  tables:
848	  - name: 'Table 13: 5-Class Ordinal Depth Classification'
849	    columns:
850	    - Class
851	    - Precision
852	    - Recall
853	    - F1
854	    rows:
855	    - - gen-0
856	      - 0.93
857	      - 0.91
858	      - 0.92
859	    - - gen-1
860	      - 0.66
861	      - 0.7
862	      - 0.68
863	    - - gen-2
864	      - 0.5
865	      - 0.54
866	      - 0.52
867	    - - gen-3
868	      - 0.47
869	      - 0.49
870	      - 0.48
871	    - - gen-4
872	      - 0.53
873	      - 0.5
874	      - 0.51
875	    - - Macro
876	      - —
877	      - —
878	      - 0.62
879	  - name: 'Table 13b: Ordinal Error Analysis'
880	    columns:
881	    - Metric
882	    - Value
883	    rows:
884	    - - MAE
885	      - 0.58
886	    - - Spearman ρ (pred vs true depth)
887	      - 0.83
888	    - - Adjacent-class confusion (%)
889	      - 72%
890	  figures_description:
891	  - 'Fig 9a: 5×5 confusion matrix heatmap. Diagonal + adjacent-diagonal cells are
892	    dark, confirming ordinal error structure.'
893	  - 'Fig 9b: Predicted depth (box plot) vs true depth. Boxes overlap for gen-2/3/4
894	    but medians increase monotonically.'
895	  analysis: 'The 5-class result characterizes the resolution ceiling of distributional
896	    fingerprints. While exact depth-4 vs depth-3 discrimination is weak, the ordinal
897	    structure is strong (ρ=0.83). This has practical implications: for data curation,
898	    coarse depth buckets (gen-0 / gen-1 / gen-2+) are more useful than exact depth
899	    anyway — the key decision boundary is "how much drift is tolerable." The result
900	    also differentiates our work from attractor theory: paraphrastic chains converge
901	    to ~2 distinguishable classes, while our non-paraphrastic chains support at least
902	    3 clean classes and 5 ordinal classes. This directly addresses RC3.
903	
904	    '
905	- name: human_edit_robustness
906	  plan_id: plan_010
907	  description: 'Robustness test on plan_002 data with simulated edits: (A) random
908	    word replacement at 5%, 10%, 20% rates, (B) LLM-simulated light editing (rephrase
909	    random sentences). Tests depth signal persistence under post-generation editing.
910	
911	    '
912	  expected_results:
913	    no_edit_macro_f1: 0.86
914	    random_5pct_macro_f1: 0.83
915	    random_10pct_macro_f1: 0.78
916	    random_20pct_macro_f1: 0.67
917	    llm_light_edit_macro_f1: 0.76
918	    degradation_slope_per_10pct: -0.095
919	  result_rationale: 'Random word replacement at 5% has minimal impact (F1=0.83, Δ=-0.03)
920	    because replacing 5% of tokens introduces noise uniformly across all depth classes,
921	    preserving the relative distributional differences. At 10% (F1=0.78), the noise
922	    begins to mask depth-specific features — entropy statistics become noisier as
923	    random words inject unpredictable surprise values. At 20% (F1=0.67), substantial
924	    text corruption disrupts the distributional fingerprint significantly but performance
925	    remains above chance (0.33). LLM-simulated editing (F1=0.76) is comparable to
926	    10% random replacement because light rephrasing changes surface statistics but
927	    largely preserves the underlying distributional structure — the edited text still
928	    occupies the same region of reference-model feature space. The degradation is
929	    approximately linear (-0.095 F1 per 10% edit rate), providing a simple model for
930	    practitioners to assess signal reliability given estimated editing rates. These
931	    results address RC5 while honestly reporting the method''s sensitivity to post-generation
932	    modification.
933	
934	    '
935	  tables:
936	  - name: 'Table 14: Robustness to Simulated Edits'
937	    columns:
938	    - Edit Type
939	    - Edit Rate
940	    - Macro-F1
941	    - Δ from No-Edit
942	    rows:
943	    - - None (baseline)
944	      - 0%
945	      - 0.86
946	      - —
947	    - - Random word replacement
948	      - 5%
949	      - 0.83
950	      - '-0.03'
951	    - - Random word replacement
952	      - 10%
953	      - 0.78
954	      - '-0.08'
955	    - - Random word replacement
956	      - 20%
957	      - 0.67
958	      - '-0.19'
959	    - - LLM light editing
960	      - ~8–12%
961	      - 0.76
962	      - '-0.10'
963	  figures_description:
964	  - 'Fig 10: Line plot — macro-F1 vs edit rate. Linear degradation with 95% CI band.
965	    Horizontal dashed line at chance level (0.33). Annotation at 10% edit rate: ''typical
966	    human editing range.'''
967	  analysis: 'The robustness profile is realistic for practical deployment. Light editing
968	    (5–10%) typical of human post-processing preserves most of the depth signal. Heavy
969	    editing (20%) degrades performance significantly but remains above chance, suggesting
970	    that even heavily edited text retains some distributional fingerprint. For the
971	    paper, this experiment provides the necessary caveat about real-world applicability
972	    while showing that the method is viable for the most common use case (lightly
973	    edited or unedited synthetic text in web-scraped data).
974	
975	    '
976	- name: ld_score_feature
977	  plan_id: plan_011
978	  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)
979	    as an additional feature to the plan_001 ablation framework. Tests whether character-level
980	    features provide complementary depth signal beyond token-level distributional
981	    features.
982	
983	    '
984	  expected_results:
985	    full_plus_ld_macro_f1: 0.88
986	    ld_score_only_macro_f1: 0.59
987	    ld_score_permutation_importance: 0.06
988	    full_plus_ld_vs_full_delta: 0.01
989	  result_rationale: 'LD-Score alone achieves modest depth discrimination (F1=0.59)
990	    because character-level distributional signatures capture some depth-dependent
991	    patterns — deeper generation text has slightly more uniform character distributions
992	    as vocabulary impoverishment affects character-level statistics. However, adding
993	    LD-Score to the full feature set provides only marginal improvement (Δ=+0.01)
994	    because LD-Score''s signal is largely redundant with existing surface features
995	    (TTR, hapax_ratio) — both measure vocabulary impoverishment, just at different
996	    granularities (character vs word level). The low permutation importance (0.06)
997	    confirms that LD-Score is not providing new information. This is a useful negative-ish
998	    result: it shows that character-level features do not add a fundamentally new
999	    signal modality, reinforcing that the key complementary feature families are surface
1000	    vocabulary statistics and reference-model distributional features.
1001	
1002	    '
1003	  tables:
1004	  - name: 'Table 15: LD-Score Feature Integration'
1005	    columns:
1006	    - Feature Set
1007	    - Macro-F1
1008	    - Δ from Full
1009	    rows:
1010	    - - Full (7 features)
1011	      - 0.87
1012	      - —
1013	    - - Full + LD-Score (8 features)
1014	      - 0.88
1015	      - '+0.01'
1016	    - - LD-Score only
1017	      - 0.59
1018	      - '-0.28'
1019	  figures_description:
1020	  - 'Fig S1 (supplementary): Feature importance bar chart with LD-Score included.
1021	    LD-Score ranks below all reference-model features.'
1022	  analysis: 'A clean but unexciting result that belongs in the supplementary material.
1023	    It confirms the two-modality structure of depth signal (reference-model entropy
1024	    + surface vocabulary) and shows that adding more surface-level features (even
1025	    at a different granularity) does not expand the signal envelope. For the paper,
1026	    this addresses potential questions about "what about other feature types" and
1027	    justifies the focus on reference-model features as the novel contribution.
1028	
1029	    '
1030	- name: end_to_end_classifier
1031	  plan_id: plan_012
1032	  description: 'QLoRA fine-tune Qwen3.5-0.8B for end-to-end depth classification (directly
1033	    from text, no handcrafted features). Compares learned representations vs handcrafted
1034	    distributional features on the plan_002 dataset.
1035	
1036	    '
1037	  expected_results:
1038	    qwen_qlora_macro_f1: 0.83
1039	    qwen_qlora_gen0_f1: 0.94
1040	    qwen_qlora_gen1_f1: 0.77
1041	    qwen_qlora_gen2plus_f1: 0.79
1042	    handcrafted_features_macro_f1: 0.86
1043	    qwen_qlora_cross_gen_leave_one_out_f1: 0.71
1044	    handcrafted_cross_gen_leave_one_out_f1: 0.78
1045	    qwen_qlora_training_gpu_hours: 12.0
1046	    handcrafted_training_time_minutes: 3.0
1047	  result_rationale: 'The QLoRA fine-tuned model achieves competitive in-distribution
1048	    performance (F1=0.83 vs handcrafted 0.86) because the transformer can implicitly
1049	    learn distributional features from raw text. However, it underperforms the handcrafted
1050	    approach for two reasons: (1) the handcrafted features distill the reference model''s
1051	    perspective into compact statistics that directly measure what matters (distributional
1052	    drift from human text), while the fine-tuned model must learn this implicitly
1053	    from text patterns; (2) the XGBoost classifier on 7 features is harder to overfit
1054	    than a 0.8B parameter model on ~25K training examples. The larger gap in cross-generator
1055	    leave-one-out (0.71 vs 0.78) reveals that the fine-tuned model memorizes generator-specific
1056	    artifacts more than the handcrafted features, which are designed to be generator-invariant.
1057	    The 4000× training time difference (12 GPU-hours vs 3 minutes) makes the handcrafted
1058	    approach clearly preferable for practical deployment. This result validates the
1059	    feature engineering approach over brute-force fine-tuning and justifies the paper''s
1060	    focus on interpretable distributional features.
1061	
1062	    '
1063	  tables:
1064	  - name: 'Table 16: End-to-End vs Feature-Based Comparison'
1065	    columns:
1066	    - Method
1067	    - In-Dist F1
1068	    - Cross-Gen F1
1069	    - Training Cost
1070	    rows:
1071	    - - XGBoost + handcrafted features
1072	      - 0.86
1073	      - 0.78
1074	      - 3 min
1075	    - - QLoRA Qwen3.5-0.8B
1076	      - 0.83
1077	      - 0.71
1078	      - 12 GPU·h
1079	    - - Δ (handcrafted − QLoRA)
1080	      - '+0.03'
1081	      - '+0.07'
1082	      - —
1083	  figures_description:
1084	  - 'Fig S2 (supplementary): Paired bar chart — in-distribution vs cross-generator
1085	    F1 for both methods. Handcrafted features show smaller generalization gap.'
1086	  analysis: 'This is a strategically important result. Reviewers might ask "why not
1087	    just fine-tune a model?" — this experiment shows that handcrafted features outperform,
1088	    generalize better, are 4000× cheaper to train, and are interpretable (you can
1089	    point to specific features and explain why they work). The fine-tuned model''s
1090	    worse cross-generator generalization is the most telling result: it confirms that
1091	    the handcrafted features capture the right abstraction (distributional drift as
1092	    measured by a reference model) while the fine-tuned model takes shortcuts via
1093	    generator-specific patterns. This result belongs in the supplementary material
1094	    and reinforces the paper''s methodological choice.'
1095	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9cbb898-6475-4834-a0a1-392799b0b22c",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "d3fc6e14-60a0-4e4c-8b72-a24829975580",
  "sourceToolAssistantUUID": "b9cbb898-6475-4834-a0a1-392799b0b22c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-14T18:43:46.851Z_

Now let me also check the generation code and any actual experimental results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3fc6e14-60a0-4e4c-8b72-a24829975580",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xL1eNbt5uvYLa8yxC9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b79d658b-6ec9-430a-a04b-abb8fed679cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wPg5pNWhjTPzj24mVPra5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34893,
      "cache_read_input_tokens": 35762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34893,
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

_source line 35 · 2026-05-14T18:43:48.399Z_

<details open><summary>🔧 Tool call — Read · `toolu_014aRp9bNXXPjNuDngiodent`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/generate_chain.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b79d658b-6ec9-430a-a04b-abb8fed679cc",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xL1eNbt5uvYLa8yxC9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddc815d8-fc17-44ca-b982-a04b17b1b202",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wPg5pNWhjTPzj24mVPra5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34893,
      "cache_read_input_tokens": 35762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34893,
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

_source line 36 · 2026-05-14T18:43:48.403Z_

<details><summary>↩ Tool result · `toolu_014aRp9bNXXPjNuDngiodent`</summary>

```text
1	"""
2	generate_chain.py — Continuation depth chain data generation pipeline.
3	
4	Input:  Wikipedia text (via HuggingFace datasets, streaming)
5	Output: /root/gen-depth-fingerprint/data/generations.jsonl
6	        Each line: {"id": int, "depth": int, "text": str, "seed_id": int, "token_count": int}
7	        1000 seeds × 5 depths (gen-0 to gen-4) = 5000 records.
8	
9	Dependencies: transformers, datasets, torch, tqdm
10	Model: EleutherAI/pythia-2.8b (local cache)
11	"""
12	
13	import argparse
14	import json
15	import os
16	import time
17	
18	import torch
19	from datasets import load_dataset
20	from tqdm import tqdm
21	from transformers import AutoModelForCausalLM, AutoTokenizer
22	
23	
24	def load_seeds(tokenizer, num_seeds=1000, max_tokens=256):
25	    """Load Wikipedia texts and truncate each to max_tokens tokens as gen-0 seeds."""
26	    seeds = []
27	    try:
28	        ds = load_dataset(
29	            "wikipedia", "20220301.en",
30	            split="train", streaming=True,
31	            trust_remote_code=True,
32	            cache_dir="/root/autodl-tmp/.hf_cache",
33	        )
34	    except Exception:
35	        print("[WARN] wikipedia dataset failed, falling back to wikitext-103")
36	        ds = load_dataset(
37	            "wikitext", "wikitext-103-raw-v1",
38	            split="train", streaming=True,
39	            cache_dir="/root/autodl-tmp/.hf_cache",
40	        )
41	
42	    for item in ds:
43	        text = item.get("text", "")
44	        if len(text.strip()) < 100:
45	            continue
46	        token_ids = tokenizer.encode(text, add_special_tokens=False)[:max_tokens]
47	        if len(token_ids) < 64:
48	            continue
49	        seeds.append(tokenizer.decode(token_ids))
50	        if len(seeds) >= num_seeds:
51	            break
52	
53	    print(f"Loaded {len(seeds)} seeds")
54	    return seeds
55	
56	
57	def generate_continuation(model, tokenizer, text, device, max_new_tokens=256, prompt_tokens=128):
58	    """Take the last prompt_tokens tokens of text, generate max_new_tokens continuation."""
59	    input_ids = tokenizer.encode(text, add_special_tokens=False)
60	    # use last prompt_tokens as the prompt
61	    input_ids = input_ids[-prompt_tokens:]
62	    input_tensor = torch.tensor([input_ids], device=device)
63	
64	    with torch.no_grad():
65	        output = model.generate(
66	            input_tensor,
67	            max_new_tokens=max_new_tokens,
68	            temperature=1.0,
69	            top_p=0.95,
70	            do_sample=True,
71	            pad_token_id=tokenizer.eos_token_id,
72	        )
73	
74	    # only decode newly generated tokens
75	    new_tokens = output[0][len(input_ids):]
76	    return tokenizer.decode(new_tokens, skip_special_tokens=True)
77	
78	
79	def main():
80	    parser = argparse.ArgumentParser()
81	    parser.add_argument("--dry-run", action="store_true", help="Only process 2 seeds for validation")
82	    parser.add_argument("--num-seeds", type=int, default=1000)
83	    parser.add_argument("--output", type=str, default="/root/gen-depth-fingerprint/data/generations.jsonl")
84	    parser.add_argument("--device", type=str, default="cuda:0", help="Device to use")
85	    parser.add_argument("--max-depth", type=int, default=4)
86	    args = parser.parse_args()
87	
88	    num_seeds = 2 if args.dry_run else args.num_seeds
89	    device = torch.device(args.device)
90	
91	    # reproducibility
92	    torch.manual_seed(42)
93	    torch.cuda.manual_seed(42)
94	
95	    print("Loading tokenizer and model...")
96	    model_name = "EleutherAI/pythia-2.8b"
97	    cache_dir = "/root/autodl-tmp/models/pythia-2.8b"
98	
99	    tokenizer = AutoTokenizer.from_pretrained(
100	        model_name, cache_dir=cache_dir, local_files_only=True
101	    )
102	    model = AutoModelForCausalLM.from_pretrained(
103	        model_name, cache_dir=cache_dir, local_files_only=True,
104	        dtype=torch.float16,
105	    ).to(device)
106	    model.eval()
107	    print(f"Model loaded on {device}, dtype={model.dtype}")
108	
109	    print(f"Loading {num_seeds} seed texts...")
110	    seeds = load_seeds(tokenizer, num_seeds=num_seeds)
111	
112	    output_path = args.output
113	    os.makedirs(os.path.dirname(output_path), exist_ok=True)
114	
115	    record_id = 0
116	    t0 = time.time()
117	
118	    with open(output_path, "w") as f:
119	        for seed_idx, seed_text in enumerate(tqdm(seeds, desc="Seeds")):
120	            # gen-0: original Wikipedia text
121	            gen0_tokens = tokenizer.encode(seed_text, add_special_tokens=False)
122	            record = {
123	                "id": record_id,
124	                "depth": 0,
125	                "text": seed_text,
126	                "seed_id": seed_idx,
127	                "token_count": len(gen0_tokens),
128	            }
129	            f.write(json.dumps(record, ensure_ascii=False) + "\n")
130	            record_id += 1
131	
132	            # gen-1 through gen-4
133	            prev_text = seed_text
134	            for depth in range(1, args.max_depth + 1):
135	                continuation = generate_continuation(model, tokenizer, prev_text, device)
136	                cont_tokens = tokenizer.encode(continuation, add_special_tokens=False)
137	                record = {
138	                    "id": record_id,
139	                    "depth": depth,
140	                    "text": continuation,
141	                    "seed_id": seed_idx,
142	                    "token_count": len(cont_tokens),
143	                }
144	                f.write(json.dumps(record, ensure_ascii=False) + "\n")
145	                record_id += 1
146	                prev_text = continuation
147	
148	            if (seed_idx + 1) % 100 == 0:
149	                elapsed = time.time() - t0
150	                rate = (seed_idx + 1) / elapsed
151	                print(f"[{seed_idx+1}/{len(seeds)}] {elapsed:.0f}s elapsed, {rate:.2f} seeds/s")
152	
153	    elapsed = time.time() - t0
154	    print(f"Done. {record_id} records written to {output_path} in {elapsed:.1f}s")
155	
156	
157	if __name__ == "__main__":
158	    main()
159	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddc815d8-fc17-44ca-b982-a04b17b1b202",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "9ecf6e92-d690-4663-bab7-7ae5b36fa5b4",
  "sourceToolAssistantUUID": "ddc815d8-fc17-44ca-b982-a04b17b1b202",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T18:43:49.037Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A4YLWmctmZ67vUtANYxRRJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/ablation_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ecf6e92-d690-4663-bab7-7ae5b36fa5b4",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xL1eNbt5uvYLa8yxC9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3266d27d-3a95-4482-ac75-407622cbbca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wPg5pNWhjTPzj24mVPra5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34893,
      "cache_read_input_tokens": 35762,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 34893
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 35762,
          "cache_creation_input_tokens": 34893,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 34893,
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

_source line 38 · 2026-05-14T18:43:49.043Z_

<details><summary>↩ Tool result · `toolu_01A4YLWmctmZ67vUtANYxRRJ`</summary>

```text
1	# ablation_analysis.py — Feature ablation, trend analysis, perplexity pre-validation
2	# Input:  data/features.csv (4609 rows), data/generations.jsonl (4609 rows)
3	# Output: results/ablation_results.json, results/trend_analysis.json,
4	#         results/depth_trends.png, results/perplexity_by_depth.json
5	# Deps:   xgboost, scikit-learn, scipy, matplotlib, numpy, pandas, torch, transformers
6	
7	import matplotlib
8	matplotlib.use('Agg')
9	
10	import argparse
11	import json
12	import os
13	import numpy as np
14	import pandas as pd
15	import matplotlib.pyplot as plt
16	from scipy import stats as sp_stats
17	from pathlib import Path
18	
19	
20	FEATURES_REF = ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max', 'tail_decay']
21	FEATURES_SURF = ['ttr', 'hapax_ratio']
22	FEATURES_ALL = FEATURES_REF + FEATURES_SURF
23	
24	MODEL_PATHS = [
25	    '/root/autodl-tmp/.hf_cache/EleutherAI/pythia-410m',
26	    '/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f',
27	]
28	
29	
30	def _stratified_sample(df, n_per_depth, seed=42):
31	    parts = []
32	    for d in sorted(df['depth'].unique()):
33	        sub = df[df['depth'] == d]
34	        parts.append(sub.sample(min(n_per_depth, len(sub)), random_state=seed))
35	    return pd.concat(parts).reset_index(drop=True)
36	
37	
38	def part_a(input_path, output_dir, dry_run=False):
39	    from sklearn.model_selection import StratifiedKFold
40	    from sklearn.metrics import f1_score
41	    from xgboost import XGBClassifier
42	
43	    df = pd.read_csv(input_path)
44	
45	    if dry_run:
46	        df = _stratified_sample(df, 20)
47	
48	    df['label'] = df['depth'].apply(lambda d: 0 if d == 0 else (1 if d == 1 else 2))
49	
50	    if not dry_run:
51	        gen0 = df[df['label'] == 0]
52	        gen1 = df[df['label'] == 1]
53	        gen2p = df[df['label'] == 2]
54	        gen2p_sampled = pd.concat([
55	            gen2p[gen2p['depth'] == d].sample(333, random_state=42) for d in [2, 3, 4]
56	        ])
57	        target_n = min(len(gen0), len(gen1), len(gen2p_sampled))
58	        df = pd.concat([
59	            gen0.sample(target_n, random_state=42),
60	            gen1.sample(target_n, random_state=42),
61	            gen2p_sampled.sample(target_n, random_state=42),
62	        ]).reset_index(drop=True)
63	
64	    y = df['label'].values
65	    min_class_n = int(np.bincount(y).min())
66	    n_folds = min(5, min_class_n)
67	    n_folds = max(2, n_folds)
68	
69	    feature_sets = {
70	        'reference_only': FEATURES_REF,
71	        'surface_only': FEATURES_SURF,
72	        'full': FEATURES_ALL,
73	    }
74	
75	    results = {}
76	    fold_scores = {}
77	
78	    for name, feats in feature_sets.items():
79	        X = df[feats].values
80	        skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=42)
81	        macro_f1s, per_class_f1s = [], []
82	
83	        for train_idx, test_idx in skf.split(X, y):
84	            clf = XGBClassifier(
85	                n_estimators=100, max_depth=6, learning_rate=0.1,
86	                random_state=42, verbosity=0, eval_metric='mlogloss',
87	            )
88	            clf.fit(X[train_idx], y[train_idx])
89	            pred = clf.predict(X[test_idx])
90	            macro_f1s.append(f1_score(y[test_idx], pred, average='macro', zero_division=0))
91	            per_class_f1s.append(f1_score(y[test_idx], pred, average=None, labels=[0, 1, 2], zero_division=0))
92	
93	        macro_f1s = np.array(macro_f1s)
94	        per_class_f1s = np.array(per_class_f1s)
95	        fold_scores[name] = macro_f1s
96	
97	        results[name] = {
98	            'macro_f1_mean': float(macro_f1s.mean()),
99	            'macro_f1_std': float(macro_f1s.std()),
100	            'per_class_f1': {
101	                'gen-0': float(per_class_f1s[:, 0].mean()),
102	                'gen-1': float(per_class_f1s[:, 1].mean()),
103	                'gen-2+': float(per_class_f1s[:, 2].mean()),
104	            },
105	        }
106	
107	    pairs = [('full', 'reference_only'), ('full', 'surface_only'), ('reference_only', 'surface_only')]
108	    t_tests = {}
109	    for a, b in pairs:
110	        t_stat, p_val = sp_stats.ttest_rel(fold_scores[a], fold_scores[b])
111	        t_tests[f'{a}_vs_{b}'] = {'t_stat': float(t_stat), 'p_value': float(p_val)}
112	
113	    results['paired_t_tests'] = t_tests
114	    results['n_samples'] = len(df)
115	    results['n_folds'] = n_folds
116	
117	    print("\n=== Part A: Feature Ablation ===")
118	    print(f"Samples: {len(df)} (balanced 1:1:1), Folds: {n_folds}")
119	    print(f"{'Feature Set':<20} {'Macro-F1':>14} {'gen-0':>8} {'gen-1':>8} {'gen-2+':>8}")
120	    print("-" * 62)
121	    for name in ['reference_only', 'surface_only', 'full']:
122	        r = results[name]
123	        print(f"{name:<20} {r['macro_f1_mean']:.4f}±{r['macro_f1_std']:.4f}"
124	              f"   {r['per_class_f1']['gen-0']:.4f}   {r['per_class_f1']['gen-1']:.4f}   {r['per_class_f1']['gen-2+']:.4f}")
125	    print("\nPaired t-tests:")
126	    for key, val in t_tests.items():
127	        sig = "***" if val['p_value'] < 0.001 else "**" if val['p_value'] < 0.01 else "*" if val['p_value'] < 0.05 else "ns"
128	        print(f"  {key}: t={val['t_stat']:.4f}, p={val['p_value']:.4f} {sig}")
129	
130	    out_path = os.path.join(output_dir, 'ablation_results.json')
131	    with open(out_path, 'w') as f:
132	        json.dump(results, f, indent=2)
133	    print(f"\nSaved: {out_path}")
134	    return results
135	
136	
137	def part_b(input_path, output_dir, dry_run=False):
138	    df = pd.read_csv(input_path)
139	
140	    if dry_run:
141	        df = _stratified_sample(df, 20)
142	
143	    depths = sorted(df['depth'].unique())
144	
145	    depth_stats = {}
146	    for d in depths:
147	        sub = df[df['depth'] == d]
148	        depth_stats[int(d)] = {
149	            feat: {'mean': float(sub[feat].mean()), 'std': float(sub[feat].std())}
150	            for feat in FEATURES_ALL
151	        }
152	
153	    trend_results = {}
154	    for feat in FEATURES_ALL:
155	        x = df['depth'].values.astype(float)
156	        y = df[feat].values.astype(float)
157	        slope, intercept, r_value, p_value, std_err = sp_stats.linregress(x, y)
158	        r_sq = r_value ** 2
159	
160	        if r_sq > 0.8 and p_value < 0.05:
161	            interpretation = f"divergence (H2, {'increasing' if slope > 0 else 'decreasing'})"
162	        elif r_sq < 0.3 or p_value >= 0.05:
163	            interpretation = 'attractor (H1)'
164	        else:
165	            interpretation = 'moderate trend'
166	
167	        trend_results[feat] = {
168	            'slope': float(slope),
169	            'intercept': float(intercept),
170	            'r_squared': float(r_sq),
171	            'p_value': float(p_value),
172	            'std_err': float(std_err),
173	            'interpretation': interpretation,
174	        }
175	
176	    print("\n=== Part B: H1/H2 Trend Analysis ===")
177	    print(f"Samples: {len(df)}")
178	    print(f"\n{'Feature':<15} {'Slope':>10} {'R²':>8} {'p-value':>10} {'Interpretation'}")
179	    print("-" * 72)
180	    for feat in FEATURES_ALL:
181	        r = trend_results[feat]
182	        print(f"{feat:<15} {r['slope']:>10.6f} {r['r_squared']:>8.4f} {r['p_value']:>10.2e} {r['interpretation']}")
183	
184	    print(f"\nPer-depth means:")
185	    header = f"{'Feature':<15}" + "".join(f" {'d=' + str(d):>12}" for d in depths)
186	    print(header)
187	    for feat in FEATURES_ALL:
188	        row = f"{feat:<15}" + "".join(f" {depth_stats[d][feat]['mean']:>12.4f}" for d in depths)
189	        print(row)
190	
191	    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
192	    axes = axes.flatten()
193	    for i, feat in enumerate(FEATURES_ALL):
194	        ax = axes[i]
195	        means = [depth_stats[d][feat]['mean'] for d in depths]
196	        stds = [depth_stats[d][feat]['std'] for d in depths]
197	
198	        ax.errorbar(depths, means, yerr=stds, fmt='o-', capsize=5, capthick=1.5,
199	                     linewidth=1.5, markersize=6, color='#1f77b4')
200	
201	        r = trend_results[feat]
202	        x_line = np.linspace(min(depths), max(depths), 100)
203	        y_line = r['slope'] * x_line + r['intercept']
204	        ax.plot(x_line, y_line, '--', color='red', alpha=0.7, linewidth=1.5)
205	
206	        ax.set_xlabel('Depth', fontsize=11)
207	        ax.set_ylabel(feat, fontsize=11)
208	        ax.set_title(f"{feat}\nslope={r['slope']:.4f}, R²={r['r_squared']:.4f}", fontsize=10)
209	        ax.set_xticks(depths)
210	
211	    for j in range(len(FEATURES_ALL), len(axes)):
212	        axes[j].set_visible(False)
213	
214	    plt.tight_layout()
215	    png_path = os.path.join(output_dir, 'depth_trends.png')
216	    plt.savefig(png_path, dpi=300, bbox_inches='tight')
217	    plt.close()
218	    print(f"\nSaved: {png_path}")
219	
220	    output = {'depth_stats': depth_stats, 'trend_results': trend_results, 'n_samples': len(df)}
221	    json_path = os.path.join(output_dir, 'trend_analysis.json')
222	    with open(json_path, 'w') as f:
223	        json.dump(output, f, indent=2)
224	    print(f"Saved: {json_path}")
225	    return output
226	
227	
228	def part_c(generations_path, output_dir, device='cuda:0', dry_run=False):
229	    import torch
230	    from transformers import AutoModelForCausalLM, AutoTokenizer
231	
232	    records = []
233	    with open(generations_path) as f:
234	        for line in f:
235	            records.append(json.loads(line))
236	
237	    if dry_run:
238	        by_depth = {}
239	        for r in records:
240	            by_depth.setdefault(r['depth'], []).append(r)
241	        sampled = []
242	        for d in sorted(by_depth.keys()):
243	            sampled.extend(by_depth[d][:4])
244	        records = sampled
245	
246	    print(f"\n=== Part C: Perplexity Pre-validation ===")
247	    print(f"Records: {len(records)}")
248	
249	    model_path = None
250	    for p in MODEL_PATHS:
251	        if os.path.isdir(p):
252	            model_path = p
253	            break
254	    if model_path is None:
255	        raise FileNotFoundError(f"Pythia-410M not found at any of: {MODEL_PATHS}")
256	
257	    print(f"Loading model from {model_path} ...")
258	    tokenizer = AutoTokenizer.from_pretrained(model_path)
259	    model = AutoModelForCausalLM.from_pretrained(model_path, dtype=torch.float16).to(device)
260	    model.eval()
261	
262	    if tokenizer.pad_token is None:
263	        tokenizer.pad_token = tokenizer.eos_token
264	
265	    perplexities = []
266	    with torch.no_grad():
267	        for i, rec in enumerate(records):
268	            inputs = tokenizer(rec['text'], return_tensors='pt', truncation=True, max_length=512)
269	            input_ids = inputs['input_ids'].to(device)
270	
271	            if input_ids.shape[1] < 2:
272	                perplexities.append({'id': rec['id'], 'depth': rec['depth'], 'perplexity': float('nan')})
273	                continue
274	
275	            outputs = model(input_ids, labels=input_ids)
276	            ppl = float(np.exp(outputs.loss.item()))
277	            perplexities.append({'id': rec['id'], 'depth': rec['depth'], 'perplexity': ppl})
278	
279	            if (i + 1) % 200 == 0 or (i + 1) == len(records):
280	                print(f"  Processed {i+1}/{len(records)}")
281	
282	    depth_ppls = {}
283	    for p in perplexities:
284	        if not np.isnan(p['perplexity']):
285	            depth_ppls.setdefault(p['depth'], []).append(p['perplexity'])
286	
287	    depth_summary = {}
288	    for d in sorted(depth_ppls.keys()):
289	        vals = depth_ppls[d]
290	        depth_summary[int(d)] = {
291	            'mean': float(np.mean(vals)),
292	            'std': float(np.std(vals)),
293	            'count': len(vals),
294	        }
295	
296	    groups = [depth_ppls[d] for d in sorted(depth_ppls.keys())]
297	    if len(groups) >= 2 and all(len(g) >= 1 for g in groups):
298	        kw_stat, kw_p = sp_stats.kruskal(*groups)
299	    else:
300	        kw_stat, kw_p = float('nan'), float('nan')
301	
302	    print(f"\n{'Depth':>6} {'Mean PPL':>12} {'Std':>10} {'Count':>6}")
303	    print("-" * 38)
304	    for d in sorted(depth_summary.keys()):
305	        s = depth_summary[d]
306	        print(f"{d:>6} {s['mean']:>12.2f} {s['std']:>10.2f} {s['count']:>6}")
307	    print(f"\nKruskal-Wallis: H={kw_stat:.4f}, p={kw_p:.4e}")
308	
309	    output = {
310	        'depth_summary': depth_summary,
311	        'kruskal_wallis': {'H_stat': float(kw_stat), 'p_value': float(kw_p)},
312	        'n_records': len(records),
313	    }
314	    out_path = os.path.join(output_dir, 'perplexity_by_depth.json')
315	    with open(out_path, 'w') as f:
316	        json.dump(output, f, indent=2)
317	    print(f"Saved: {out_path}")
318	    return output
319	
320	
321	def main():
322	    parser = argparse.ArgumentParser(description='Ablation analysis for gen-depth-fingerprint')
323	    parser.add_argument('--parts', nargs='+', default=['A', 'B', 'C'], choices=['A', 'B', 'C'])
324	    parser.add_argument('--input', default='data/features.csv')
325	    parser.add_argument('--generations', default='data/generations.jsonl')
326	    parser.add_argument('--output-dir', default='results/')
327	    parser.add_argument('--device', default='cuda:0')
328	    parser.add_argument('--dry-run', action='store_true')
329	    args = parser.parse_args()
330	
331	    os.makedirs(args.output_dir, exist_ok=True)
332	
333	    if args.dry_run:
334	        print("[DRY-RUN MODE]")
335	
336	    if 'A' in args.parts:
337	        part_a(args.input, args.output_dir, dry_run=args.dry_run)
338	    if 'B' in args.parts:
339	        part_b(args.input, args.output_dir, dry_run=args.dry_run)
340	    if 'C' in args.parts:
341	        part_c(args.generations, args.output_dir, device=args.device, dry_run=args.dry_run)
342	
343	    print("\nDone.")
344	
345	
346	if __name__ == '__main__':
347	    main()
348	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3266d27d-3a95-4482-ac75-407622cbbca9",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "33c10021-0294-4d8e-b76a-dc3ebcf4703c",
  "sourceToolAssistantUUID": "3266d27d-3a95-4482-ac75-407622cbbca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-14T18:43:51.846Z_

Now let me check the decisions.yaml for additional context on the project's decision history.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33c10021-0294-4d8e-b76a-dc3ebcf4703c",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xLRaY2a8L6LH7AoNpz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93d6ffca-bc72-417f-a00b-339d64bbb22c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzXQCFNSpNoByQmtAtkFWt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7720,
      "cache_read_input_tokens": 70655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7720,
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

_source line 40 · 2026-05-14T18:43:53.327Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TqzXkge89guTCtQoNyVZT2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93d6ffca-bc72-417f-a00b-339d64bbb22c",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xLRaY2a8L6LH7AoNpz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56767f50-82a6-4be8-b5cb-017afe04da50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzXQCFNSpNoByQmtAtkFWt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7720,
      "cache_read_input_tokens": 70655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7720,
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

_source line 41 · 2026-05-14T18:43:53.332Z_

<details><summary>↩ Tool result · `toolu_01TqzXkge89guTCtQoNyVZT2`</summary>

```text
1	_next_id: 5
2	decisions:
3	- id: D001
4	  date: 2026-05-14 16:15 UTC
5	  summary: MVP 方案：Pythia-2.8B continuation 链 + Pythia-410M 参考模型 + XGBoost 3-class
6	    分类
7	  rationale: '选择 continuation（最低语义偏离）作为最可能保留 depth 信号的生成类型；单生成器简化变量；Pythia-410M 作为参考模型避免与生成器的规模/架构循环；XGBoost
8	    快速验证无需 GPU 训练。Pass: macro-F1≥0.45 且 gen-0 vs gen-2+ F1≥0.65。'
9	  related_experiments: []
10	  depends_on: []
11	- id: D002
12	  date: 2026-05-14 18:10 UTC
13	  summary: MVP PASS → 进入研究阶段。首要任务：特征 ablation + depth signal 增量验证
14	  rationale: macro-F1=0.84 远超 0.45 阈值，binary F1=0.87 远超 0.65，7/7 特征显著。核心假设成立。但 Reviewer
15	    指出 hapax_ratio（表面特征）贡献最大，需 ablation 验证分布指纹的独立价值；gen-1 vs gen-2+ 混淆率高，需量化 depth
16	    信号超越 binary 分类的增量。
17	  related_experiments:
18	  - exp_id: mvp-001
19	    role: primary
20	    result: 'PASS: macro-F1=0.8408, binary-F1=0.8653'
21	  depends_on:
22	  - D001
23	- id: D003
24	  date: 2026-05-14 18:15 UTC
25	  summary: Claim 2 准备 Plan B framing：若 ablation 显示表面特征足够，叙事从 "independent signal"
26	    调整为 "complementary signal"
27	  rationale: Reviewer 指出 Claim 2 是整个叙事的 single point of failure。MVP 中 hapax_ratio
28	    importance=0.30，表面特征贡献 47%。Plan B 不 kill 项目，只调 framing 强度——从"分布指纹独立于表面统计"降为"分布指纹提供互补信号"，核心叙事转为
29	    vocabulary impoverishment as primary depth signal。
30	  related_experiments: []
31	  depends_on:
32	  - D002
33	- id: D004
34	  date: 2026-05-14 18:38 UTC
35	  summary: Claim 2 framing 调整：从 "Fingerprint Independence" 转为 "Feature Complementarity
36	    & Dual Dynamics"；H1/H2 从二选一转为共存
37	  rationale: plan_001 ablation 结果：surface_only (0.76) > reference_only (0.72)，但 full
38	    (0.82) 显著优于 surface_only (p=0.0008)。原 Claim 2 "independent signal" 被否定，触发 Plan
39	    B (D003)。新发现更强：表面特征呈 H2 drift、分布形状特征呈 H1 stationary，dual dynamics 是比原 framing
40	    更丰富的科学贡献。
41	  related_experiments:
42	  - exp_id: plan_001
43	    role: primary
44	    result: surface_only 0.76 > reference_only 0.72; full 0.82 显著优于两者; H1/H2 按特征类型共存
45	  depends_on:
46	  - D002
47	  - D003
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56767f50-82a6-4be8-b5cb-017afe04da50",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "089f8c36-b68d-4f02-a3db-a0d7d53701f6",
  "sourceToolAssistantUUID": "56767f50-82a6-4be8-b5cb-017afe04da50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T18:43:54.184Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HYXVXVQUUVt4fXkR48pqVJ`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "089f8c36-b68d-4f02-a3db-a0d7d53701f6",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xLRaY2a8L6LH7AoNpz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e64c5e6b-6147-4480-b7a4-c06116a288b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzXQCFNSpNoByQmtAtkFWt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7720,
      "cache_read_input_tokens": 70655,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7720
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 70655,
          "cache_creation_input_tokens": 7720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7720,
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

_source line 43 · 2026-05-14T18:43:54.202Z_

<details><summary>↩ Tool result · `toolu_01HYXVXVQUUVt4fXkR48pqVJ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e64c5e6b-6147-4480-b7a4-c06116a288b0",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "e46dcadd-64bd-4d1a-b31d-40e7c7ed0fc0",
  "sourceToolAssistantUUID": "e64c5e6b-6147-4480-b7a4-c06116a288b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-14T18:43:57.405Z_

Now I have a thorough understanding of the paper, the experiment plans, the actual code, and the project's full context. Let me now submit my review via the appropriate tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e46dcadd-64bd-4d1a-b31d-40e7c7ed0fc0",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xLopFZaGEgUetw6A15",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c41533ff-af6b-4280-8618-39de63a961ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PnUaRxRU1qqSFJ576rcER",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1507,
      "cache_read_input_tokens": 78375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1507,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 45 · 2026-05-14T18:43:57.813Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01C9fUHatWXbJ5CRSqjCwDmh`</summary>

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
  "parentUuid": "c41533ff-af6b-4280-8618-39de63a961ed",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xLopFZaGEgUetw6A15",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2d2b3ac-4318-49ed-9c9e-4b8c103828ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PnUaRxRU1qqSFJ576rcER",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1507,
      "cache_read_input_tokens": 78375,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1507
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 127,
          "cache_read_input_tokens": 78375,
          "cache_creation_input_tokens": 1507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1507,
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

_source line 46 · 2026-05-14T18:43:57.815Z_

<details><summary>↩ Tool result · `toolu_01C9fUHatWXbJ5CRSqjCwDmh`</summary>

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
  "parentUuid": "c2d2b3ac-4318-49ed-9c9e-4b8c103828ff",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "8f76b189-c151-4bba-99fd-2c8500225bb9",
  "sourceToolAssistantUUID": "c2d2b3ac-4318-49ed-9c9e-4b8c103828ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-14T18:44:01.208Z_



Now I have all the information needed to write a thorough review. Let me synthesize my findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f76b189-c151-4bba-99fd-2c8500225bb9",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xM5HvZg917VU1gG89b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01377e8d-61b2-4312-a496-119e07beea30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pgdqETrH1dtaJmyuipCAQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 705,
      "cache_read_input_tokens": 79882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 705,
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

_source line 48 · 2026-05-14T18:45:23.814Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_011KoSNohAhjPEKLFFzHdYew`</summary>

```json
{
  "report": "\n# R1 Review: Methods and Experiments\n\n## Paper Summary (2-3 sentences)\n\nThis paper introduces \"distributional fingerprinting\" for estimating the generation depth of text (gen-0/gen-1/gen-2+) by computing token-level entropy statistics under a small reference language model. It tests whether non-paraphrastic generation chains converge (H1) or diverge monotonically (H2), confirming H2, and builds a 7-feature XGBoost classifier achieving macro-F1=0.87 (3-class) with cross-generator generalization at F1=0.78. Depth-aware data filtering is shown to outperform binary detection baselines by 5.2% in downstream perplexity while retaining more training data.\n\n## Strengths\n\n- **Comprehensive experimental coverage.** All 12 planned experiments are reported, spanning feature ablation, cross-generator generalization, cross-reference models, downstream utility, prompt types, paraphrastic comparison, cross-model chains, multi-domain evaluation, finer-grained ordinal classification, robustness, LD-Score integration, and a neural baseline. This is unusually thorough for a single paper and addresses most foreseeable reviewer objections proactively.\n\n- **Clean hypothesis testing framework.** The H1 vs H2 formalization, combined with the direct paraphrastic vs non-paraphrastic comparison (Table 6, KS D=0.41, p<1e-4), provides a satisfying theoretical backbone. The finding that H1 holds for paraphrastic chains and H2 for non-paraphrastic chains is genuinely informative and connects well to the Briesch et al. (2025) attractor cycle literature.\n\n- **Feature ablation is well-designed.** The three-condition ablation (ref-only, surface-only, full) with McNemar test and permutation importance analysis directly addresses the \"is this just vocabulary impoverishment?\" concern. The ref-only F1=0.79 vs surface-only F1=0.63 gap (+0.16) is substantial and statistically significant.\n\n- **Honest reporting of limitations.** The paper transparently reports the 10-point F1 drop for cross-model chains, the degradation under editing, and the resolution ceiling at 5 classes. This builds credibility.\n\n- **Strong practical contribution.** The downstream utility experiment (Table 7-8) translates distributional drift into perplexity, a metric practitioners care about. The 42% data retention vs 28% for binary baselines, at better quality, is a compelling practical result.\n\n- **Appropriate classifier choice with justification.** The XGBoost vs QLoRA comparison (Table 15) demonstrates that handcrafted features outperform, generalize better (+0.07 cross-gen), and are 240x cheaper. This justifies the methodology.\n\n## Weaknesses\n\n- **CRITICAL: Discrepancy between actual MVP results and paper claims.** The project's own decision log (D004) records that the actual plan_001 ablation found surface_only (0.76) > reference_only (0.72), with full at 0.82. The paper_framing.md also states these numbers. However, the paper reports reference_only (0.79) > surface_only (0.63), a complete reversal. The paper's Table 1 claims reference-only features substantially outperform surface features, but the project's own experimental record shows the opposite. This is the most serious issue in the paper. Either the results were updated after additional experiments (in which case the methodology section must explain what changed), or the numbers in the paper are imagined/projected rather than measured. The abstract's claim that \"reference-model entropy features carry independent signal beyond surface vocabulary impoverishment (delta-F1 = +0.16)\" appears to contradict the actual experimental record.\n\n- **CRITICAL: All results beyond MVP appear to be \"imagined\" rather than executed.** The project overview shows only mvp-001 as DONE (with macro-F1=0.84). All other experiments (plan_001 through plan_012) are listed as \"pending.\" The `imagined_experiments.yaml` file contains the exact numbers that appear in the paper's tables — down to the decimal place. The paper appears to be a \"dream\" report (best-case scenario projection) rather than a report of actual experimental results. This must be disclosed. If the paper is submitted with these numbers, they need to be validated by actually running the experiments.\n\n- **Generation parameters mismatch.** The actual generation code (`generate_chain.py`) uses temperature=1.0 and top_p=0.95, while the project memory explicitly states the Director specified temperature=0.7 and top_p=0.9, noting \"不能用 temp=1.0——高温度使生成文本更随机、分类更容易.\" If the MVP was run with temp=1.0 instead of 0.7, the macro-F1=0.84 result may be inflated by the higher temperature making generated text easier to distinguish from human text. The paper does not report generation parameters at all, which is a reproducibility gap.\n\n- **Text length confound not controlled.** The generation pipeline truncates seeds to 256 tokens and generates max_new_tokens=256 continuations. Deeper generations may systematically differ in length (the memory notes \"depth attrition 17.4%: some continuations produce empty text\"). Neither the features nor the evaluation account for text length as a confound. Entropy statistics computed over different-length texts are not directly comparable. The paper should include a length-controlled analysis or demonstrate that length is not a confounding feature.\n\n- **Generator scale range is narrow.** All 5 generators are between 0.8B and 2.8B parameters. The paper claims to study \"recursive LLM contamination\" broadly, but modern contamination involves 7B-70B+ models. The limitation section mentions this (\"all experiments use models <=2.8B\") but understates its significance — it is unclear whether the distributional drift phenomenon and feature design transfer to larger, more capable generators that produce more human-like text.\n\n- **Downstream utility experiment has confounds.** In Table 7, the depth-filtered condition (gen-0+gen-1) uses ~9,500 samples while binary baselines use ~6,100-6,300 samples. The perplexity advantage could partially be a data quantity effect rather than a data quality effect. A controlled comparison at equal sample sizes is needed. Additionally, Pythia-410M is used as both the reference model for feature extraction AND the downstream fine-tuning target — this creates a circularity where the reference model's own preferences are used to both measure drift and evaluate downstream quality.\n\n- **5-fold CV on non-independent data.** Generation chains from the same seed are not independent (gen-1 through gen-4 all derive from the same gen-0). If stratified CV splits by sample rather than by seed, train and test sets may contain related samples from the same chain, inflating performance. The paper does not specify whether CV stratification is seed-aware.\n\n- **Paraphrastic comparison uses Pythia-2.8B for paraphrasing.** A 2.8B parameter model is a weak paraphraser. The low F1=0.58 for paraphrastic chains might reflect poor paraphrase quality rather than genuine attractor convergence. Using a stronger paraphraser (or a dedicated paraphrase model) would strengthen this comparison.\n\n- **No confidence intervals on most headline numbers.** The main result (F1=0.87) reports CV std=0.012, but most other tables lack uncertainty estimates. Leave-one-generator-out reports std=0.03 across 5 generators, but this is cross-generator variance, not sampling uncertainty.\n\n- **Statistical testing is inconsistent.** McNemar test is used for the ablation but not for other comparisons. The KS test is used for H1/H2 but no effect size is reported beyond the test statistic. The Spearman rho=0.91 for prompt type drift rate vs F1 is computed on only 3 data points, making it statistically meaningless.\n\n## Questions for Authors\n\n- Can you clarify the discrepancy between the decision log (D004: surface_only=0.76 > reference_only=0.72) and the paper's Table 1 (reference_only=0.79 >> surface_only=0.63)? Were additional experiments run that changed these numbers, or do they reflect different datasets/configurations?\n\n- Which experiments have actually been executed vs projected? The project tracker shows only mvp-001 as completed.\n\n- What generation parameters (temperature, top_p) were used for the results reported in the paper? The codebase shows temp=1.0/top_p=0.95, but the project specification calls for temp=0.7/top_p=0.9.\n\n- Is the 5-fold CV seed-aware? That is, are all depths from a single seed guaranteed to be in the same fold?\n\n- For the downstream utility experiment (Table 7-8), have you controlled for training data size? What happens if you downsample the depth-filtered set to match binary baseline sizes?\n\n- Why was Pythia-410M used as both the reference model and the downstream fine-tuning target? Have you verified results with a different downstream model?\n\n- The Spearman rho=0.91 for drift rate vs F1 across prompt types is computed on n=3 points. Do the authors consider this statistically meaningful?\n\n## Missing Experiments/Concerns\n\n1. **Length-controlled evaluation.** Add text length as a feature or control variable to verify that depth classification is not primarily driven by length differences across depths.\n\n2. **Seed-aware cross-validation.** Ensure that all samples from the same generation chain are in the same CV fold. Report both seed-aware and sample-level CV to quantify any inflation.\n\n3. **Equal-size downstream comparison.** Control for data quantity in the downstream utility experiment by downsampling the depth-filtered set.\n\n4. **Larger generators.** Even one experiment with a 7B+ generator would substantially strengthen the generalization claim.\n\n5. **Adversarial evasion.** What happens when a generator is specifically prompted to \"write like a human\" or when decoding parameters are tuned to minimize detectability? The robustness experiments only consider post-generation editing, not adversarial generation.\n\n6. **Real-world wild data.** All chains are lab-constructed. Even a small pilot on naturally occurring web text with suspected multi-generation provenance would improve ecological validity.\n\n7. **Feature correlation analysis.** The 5 entropy features (mean, std, min, max, tail_decay) likely have high multicollinearity. A correlation matrix or VIF analysis would clarify whether all 5 carry independent information or whether a smaller subset suffices.\n\n8. **Calibration analysis.** Are the classifier's probability outputs well-calibrated? For risk-stratified data curation, calibrated confidence scores matter more than raw F1.\n\n## Scores\n\n- **Soundness: 4/10** — The core idea is sensible, but the paper appears to report projected/imagined results rather than actual experimental outcomes. The discrepancy between the project's recorded ablation results and the paper's claims is a fundamental integrity concern that must be resolved before publication. If all numbers are confirmed by actual experiments, this score would rise substantially (likely 7/10).\n\n- **Experimental Rigor: 5/10** — The experimental design is impressively comprehensive in scope (12 experiments covering most foreseeable concerns). However, several confounds are uncontrolled (text length, data size in downstream comparison, seed-awareness in CV, reference model circularity). The narrow generator scale range (0.8-2.8B) limits external validity. If these are addressed, rigor would be strong (7-8/10).\n\n- **Reproducibility: 3/10** — Generation parameters are not reported in the paper. The actual code uses different parameters than specified. No code/data release is mentioned. Feature extraction details (tokenization, context window, handling of special tokens) are underspecified. The reference model selection rationale (\"never fine-tuned on synthetic data\") is claimed but not verified.\n\n- **Overall (Methods+Experiments focus): 4/10** — The paper presents a well-motivated research question with a creative methodological approach and impressively broad experimental coverage. However, the apparent gap between imagined and actual results, the ablation number discrepancy, and several uncontrolled confounds prevent a positive recommendation in the current form. If the experiments are actually run and the confounds addressed, this could be a solid 7/10 paper. The theoretical contribution (H1 vs H2 dichotomy) and practical contribution (depth-aware filtering) are both meaningful.\n\n- **Confidence: 4/5** — I have high confidence in these assessments. I examined the full paper, experiment plan, actual code, project decision log, and imagined experiment specifications. The discrepancy between recorded experimental results and paper claims is clearly documented in the project's own files.\n",
  "project": "gen-depth-fingerprint",
  "tier": "best",
  "dream_id": "dream_20260514T181213",
  "overall_score": "4/10 — Reject pending actual experimental validation; promising if confirmed"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01377e8d-61b2-4312-a496-119e07beea30",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xM5HvZg917VU1gG89b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9702afc-ee0d-4ccd-96b9-9e57149a4c9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pgdqETrH1dtaJmyuipCAQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 705,
      "cache_read_input_tokens": 79882,
      "output_tokens": 3202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 705
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3202,
          "cache_read_input_tokens": 79882,
          "cache_creation_input_tokens": 705,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 705,
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

_source line 49 · 2026-05-14T18:45:26.667Z_

<details><summary>↩ Tool result · `toolu_011KoSNohAhjPEKLFFzHdYew`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/review_report.md\", \"dream_id\": \"dream_20260514T181213\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9702afc-ee0d-4ccd-96b9-9e57149a4c9d",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "adeeb26d08149eca7",
  "type": "user",
  "uuid": "1149d336-0689-44dc-8b4f-32c5c4834fd9",
  "sourceToolAssistantUUID": "d9702afc-ee0d-4ccd-96b9-9e57149a4c9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-14T18:45:38.347Z_

Review submitted. Here is a summary of the key findings:

**Overall Assessment: 4/10 (Reject pending experimental validation)**

The paper presents an interesting and well-motivated research direction -- distributional fingerprinting for generation depth estimation -- with impressively comprehensive experimental design (12 experiments). However, I identified several critical issues:

**Most serious findings:**

1. **Results appear to be projections, not actuals.** The project tracker shows only `mvp-001` as completed. All 12 paper experiments match the `imagined_experiments.yaml` file to the decimal place, suggesting the paper reports best-case projections rather than executed experiments.

2. **Ablation numbers contradict the project's own records.** Decision D004 records that the actual ablation found surface_only (0.76) > reference_only (0.72), but the paper claims reference_only (0.79) >> surface_only (0.63) -- a complete reversal that undermines the core claim about reference-model features.

3. **Generation parameter mismatch.** The code uses temperature=1.0/top_p=0.95, while the Director specified 0.7/0.9, noting that temp=1.0 inflates classification results.

**Additional methodological concerns:** text length confound, non-seed-aware CV, data size confound in downstream experiments, reference model circularity (Pythia-410M used for both feature extraction and downstream evaluation), narrow generator scale (0.8-2.8B only), and a Spearman correlation computed on n=3 points.

**If the experiments are actually run and confounds addressed**, the paper could reach 7/10 -- the theoretical framework (H1/H2 dichotomy), experimental breadth, and practical application (depth-aware filtering) are all well-conceived.

Review saved to: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/review_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1149d336-0689-44dc-8b4f-32c5c4834fd9",
  "isSidechain": true,
  "agentId": "adeeb26d08149eca7",
  "requestId": "req_011Cb2xTczKyzgMZUgi7MTrq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12a102a6-b44c-4196-81b5-e3e5d56a6ee5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoNCMc8SHBjEjNKC5gqEVd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3332,
      "cache_read_input_tokens": 80587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3332,
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
