# Research conversation: You are Reviewer 1 (R1) in an academic paper review. Your focus is **methods and experiments**. The paper is: "Does Prob

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a8feaccbaabb0c33d.jsonl`
- **Structured JSON:** [`f85e0d4c3ecda3a66f5b.json`](../../sessions/f8/f85e0d4c3ecda3a66f5b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

46 recorded events

### User

_source line 1 · 2026-05-20T19:52:11.670Z_

You are Reviewer 1 (R1) in an academic paper review. Your focus is **methods and experiments**. 

The paper is: "Does Probe-Based Calibration Work Beyond English? A Systematic Study Across 3 Architectures and 52 Languages"

## Paper Summary
The paper studies whether English-trained correctness probes (linear probes on internal LLM representations predicting answer correctness) transfer cross-lingually. It evaluates 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20-52 languages, 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR), on GlobalMMLU, Belebele, MMLU-ProX.

## Key Results
1. Zero-shot transfer fails for 12/19 languages on Qwen3 (AUROC<0.65), 15/19 on Llama4
2. Pareto frontier (depth vs transferability) is architecture-dependent: ρ=0.41 Qwen3, 0.22 Llama4, 0.48 Gemma4
3. CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) — consistency loss is inert (sweeping β over 3 OOM changes AUROC <0.3pp; removing it improves by 0.2pp)
4. Difficulty-capability decomposition: projecting out difficulty hurts transfer by 1.3-1.4pp
5. Orthogonality (correctness vs confidence) persists across 20 languages (mean cosine 0.072)
6. Probe complexity: MLP +1pp English, -0.2 to -0.4pp transfer (Cohen's d=0.18)
7. Cross-benchmark: Belebele confirms, MMLU-ProX noisier; CaCLR never beats linear proj
8. Extended 52 languages: pass rate drops to 23.5%, very-low-resource 0%
9. INT8 validation: 0.3pp AUROC difference, cosine 0.994

## Experiment Design (from context YAML)
- Plan 001: Qwen3 full Pareto — 24 probed layers, 20 languages, all 5 transfer methods
- Plan 002: Llama4 full Pareto — 12 probed layers, same setup
- Plan 003: CaCLR — joint objective with BCE+SB-ECE+consistency, sweep α and β
- Plan 004: Difficulty decomposition — IRT difficulty probes, project out, retrain, 10 langs × 8 layers
- Plan 005: Orthogonality — confidence direction vs correctness direction, 20 langs × 2 models
- Plan 006: Probe complexity — LogReg vs 2-layer MLP
- Plan 007: Belebele + MMLU-ProX validation
- Plan 008: Gemma 4 31B (camera-ready extension)
- Plan 009: Extended 52 languages
- Plan 010: INT8 vs FP16 validation

## Tables in Paper
- Table 1: English probe performance by depth (6 depth bins × 2 models)
- Table 2: Zero-shot transfer AUROC by language (19 langs × 2 models)
- Table 3: Transfer method comparison (6 methods × 2 models, 19-lang mean)
- Table 4: CaCLR ablation (5 variants on Qwen3)
- Table 5: Pareto frontier coherence (3 architectures)
- Table 6: Decomposition ablation (4 conditions × 2 models, 9-lang mean)
- Table 7: Orthogonality by resource tier (3 tiers × 2 models)
- Table 8: Probe complexity (2 probes × 2 models)
- Table 9: Cross-benchmark generalization (3 benchmarks × 2 models)
- Table 10: Extended 52-language results by tier
- Table 11 (appendix): INT8 validation (5 layers)

## Your Task
Provide a detailed review focusing on:
1. **Experimental soundness**: Are the experiments well-designed? Are controls adequate? Are there confounds?
2. **Statistical rigor**: Are claims supported? Are significance tests missing? Are effect sizes meaningful?
3. **Methodological completeness**: Are there obvious methods/baselines missing? Is the CaCLR formulation well-specified?
4. **Reproducibility**: Is there enough detail to reproduce?
5. **Specific issues** with individual experiments

Score on 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept. Target venue: top ML venue (~25% acceptance rate).

Be thorough and critical. Output your review in structured format with Strengths, Weaknesses, Questions, Minor Issues, and Score with justification. Keep under 800 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "17a2eccd-909c-4db4-9a1e-aac1cae6c2a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T19:52:11.676Z_

```json
{
  "parentUuid": "17a2eccd-909c-4db4-9a1e-aac1cae6c2a5",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
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
  "uuid": "edae7880-bc30-4957-89e0-9ff0aac75270",
  "timestamp": "2026-05-20T19:52:11.676Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-20T19:52:15.565Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018v6WAB5SgzgzYLmLXTJnDz`</summary>

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
  "parentUuid": "edae7880-bc30-4957-89e0-9ff0aac75270",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQQLgnJoMzxHAoHC1x4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba48ff0e-84a2-4e6e-ac02-7fba63be6a0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAAmckYAfF2pjREx9Fw3t4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15564,
      "cache_read_input_tokens": 0,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15564
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 88,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15564,
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

_source line 4 · 2026-05-20T19:52:15.569Z_

<details><summary>↩ Tool result · `toolu_018v6WAB5SgzgzYLmLXTJnDz`</summary>

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
  "parentUuid": "ba48ff0e-84a2-4e6e-ac02-7fba63be6a0b",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "2a754ab6-6fa2-4bec-8c36-0cc2a5903165",
  "sourceToolAssistantUUID": "ba48ff0e-84a2-4e6e-ac02-7fba63be6a0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T19:52:19.601Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WuHwVbSouSzqXgufV7WdNN`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a754ab6-6fa2-4bec-8c36-0cc2a5903165",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQQdXZ6fiyjuKyYAatw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0fc732c-cc83-4ee7-8268-868befb2ee3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TABfTHGnyFCXgKTjya6Epi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 15564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1270,
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

_source line 6 · 2026-05-20T19:52:19.618Z_

<details><summary>↩ Tool result · `toolu_01WuHwVbSouSzqXgufV7WdNN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| mvp_003 | Cross-lingual correctness direction is model-agnostic: an English-trained linear probe on Llama-3.1-8B-Instruct internal representations will transfer to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the pattern observed in Qwen2.5-7B-Instruct (mvp_001). | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_002** (failed): Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与 mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际 28 层，index 0-27） ← 基于 mvp_001\\n- **mvp_001** (success): 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性 probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在 layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp for ≥3/5 语言）。\\n\\n## 趋势\\n成功 1 / 负向 0 / 失败 1 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-13176: 无 GPU 信息\\n\\n## 告警\\n- mvp_002: 训练失败 — unknown\\n\", \"total_chars\": 1092, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0fc732c-cc83-4ee7-8268-868befb2ee3b",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "306a2be9-da5f-4986-a0e0-ce7cc3efbb6a",
  "sourceToolAssistantUUID": "f0fc732c-cc83-4ee7-8268-868befb2ee3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T19:52:20.000Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0117275d7mEGstY6deLVi8GP`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "306a2be9-da5f-4986-a0e0-ce7cc3efbb6a",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQQdXZ6fiyjuKyYAatw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15ece6bf-43b0-4637-bf9a-538f8f133f34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TABfTHGnyFCXgKTjya6Epi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 15564,
      "output_tokens": 203,
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
          "output_tokens": 203,
          "cache_read_input_tokens": 15564,
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

_source line 8 · 2026-05-20T19:52:20.010Z_

<details><summary>↩ Tool result · `toolu_0117275d7mEGstY6deLVi8GP`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_provenance.yaml found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15ece6bf-43b0-4637-bf9a-538f8f133f34",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "e96664a9-81c6-4618-9942-3d0138c5c72f",
  "sourceToolAssistantUUID": "15ece6bf-43b0-4637-bf9a-538f8f133f34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T19:52:23.547Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01L61kDbNRuMuBhkp4FfVoeW`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e96664a9-81c6-4618-9942-3d0138c5c72f",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQQxiUJBejYaLQ9bX1h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2751bc43-2bf3-4aa5-85a1-3fa30496b951",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XhUiQEwd5nAFVMb9bKEcv1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 16834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1097,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 10 · 2026-05-20T19:52:23.556Z_

<details><summary>↩ Tool result · `toolu_01L61kDbNRuMuBhkp4FfVoeW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/decisions.yaml\", \"content\": \"_next_id: 5\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 13:49 UTC\\n  summary: MVP 用 7-8B 模型验证核心假设，不直接上 235B\\n  rationale: 核心假设（correctness probe 跨语言迁移 + layer-depth 效应）在 7-8B 模型上有充分先验（Miao &\\n    Ungar、Civelli 等均用 7-8B）。若 7B 无效应则整个方向不成立。7B 仅需 1 GPU × 2-4h，快速验证后再决定是否投入 235B\\n    的大资源。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 13:53 UTC\\n  summary: MVP 模型固定为 Qwen2.5-7B-Instruct\\n  rationale: 与正式实验 Qwen3-235B 同属 Qwen 家族，架构连续性最好。Civelli et al. 报告 Qwen3-8B 最优迁移深度为\\n    24%，可为正式实验提供直接参考。Reviewer 建议明确选一个并记录理由。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-20 18:25 UTC\\n  summary: P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/5 语言\\n  rationale: Mean-shift 是常数偏移，不改变 AUROC（rank-invariant）。Mean-shift 的设计目的是改善 calibration（概率准确性），应用\\n    ECE/Brier 衡量。同时 P1 ECE 阈值维持 0.15 但允许 temperature scaling 后重测。\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: trigger\\n    result: P4 ΔAUROC=0 暴露标准设计缺陷\\n  depends_on: []\\n- id: D004\\n  date: 2026-05-20 18:52 UTC\\n  summary: 'MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段'\\n  rationale: P1(AUROC=0.754+ECE=0.074 temp-scaled) / P2(4/5语言迁移) / P3(14.3pp depth\\n    effect) 全部 PASS。P4(mean-shift) FAIL 但属于 alignment baseline 方法失败，不否定核心假设。Mean-shift\\n    失败是有价值的 negative result：(1) 区分于 Xiao et al. 在 knowledge boundary 上 mean-shift\\n    成功；(2) motivate CaCLR 方法。额外发现：L27 英语最强但迁移退化 vs L24——直接观测到 Pareto tradeoff，是论文核心贡献的前兆。\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: primary\\n    result: P1✅P2✅P3✅P4❌, core hypothesis supported\\n  depends_on: []\\n\", \"total_chars\": 1523, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2751bc43-2bf3-4aa5-85a1-3fa30496b951",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "80e2b7b5-38c3-4f06-88fa-70035df75690",
  "sourceToolAssistantUUID": "2751bc43-2bf3-4aa5-85a1-3fa30496b951",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T19:52:24.457Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RffV7haAqG5gL1TKdoX3sb`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80e2b7b5-38c3-4f06-88fa-70035df75690",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQQxiUJBejYaLQ9bX1h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33c0f615-b3ef-4387-8eec-0471d8688c9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XhUiQEwd5nAFVMb9bKEcv1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 16834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1097,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 12 · 2026-05-20T19:52:24.465Z_

<details><summary>↩ Tool result · `toolu_01RffV7haAqG5gL1TKdoX3sb`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33c0f615-b3ef-4387-8eec-0471d8688c9f",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "1f33f8a2-f6b2-4cd9-b33e-529c47e99e2c",
  "sourceToolAssistantUUID": "33c0f615-b3ef-4387-8eec-0471d8688c9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T19:52:24.876Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WM3zoxrCTvU7RWTh3RHHd2`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f33f8a2-f6b2-4cd9-b33e-529c47e99e2c",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQQxiUJBejYaLQ9bX1h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f9ca5bb-37d1-4b00-bc58-6f9343ed326e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XhUiQEwd5nAFVMb9bKEcv1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 16834,
      "output_tokens": 291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1097
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 291,
          "cache_read_input_tokens": 16834,
          "cache_creation_input_tokens": 1097,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1097,
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

_source line 14 · 2026-05-20T19:52:24.885Z_

<details><summary>↩ Tool result · `toolu_01WM3zoxrCTvU7RWTh3RHHd2`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f9ca5bb-37d1-4b00-bc58-6f9343ed326e",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "638431eb-9442-46de-a9dc-89a596fbe8bb",
  "sourceToolAssistantUUID": "0f9ca5bb-37d1-4b00-bc58-6f9343ed326e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T19:52:28.182Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MtKXaw3oRs6sd4SqLJBx8K`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "638431eb-9442-46de-a9dc-89a596fbe8bb",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQRKQfoY9LY92KZ8pV4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b459f1d-7ed0-47de-9fd1-7537d58b8148",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W7jF7wyS3Zy8hws2QUZxWf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1525,
      "cache_read_input_tokens": 17931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1525,
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

_source line 16 · 2026-05-20T19:52:28.191Z_

<details><summary>↩ Tool result · `toolu_01MtKXaw3oRs6sd4SqLJBx8K`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/ROADMAP.md\", \"content\": \"# xling_calib_direction — Research Dashboard\\n\\n> 最后更新: 2026-05-20 19:00 UTC | 更新原因: Reviewer 修正 mean-shift 叙事 + 标注覆盖度风险 + temp scaling 待确认\\n\\n## 核心方向\\n通过中间层 correctness direction 将英语校准迁移到非英语语言。发现 depth-transferability Pareto frontier，提出 CaCLR 方法联合优化 correctness + 跨语言一致性。详见 paper_framing.md。\\n\\n## 当前进展\\n- 阶段：**Research**（MVP 已通过，D004）\\n- 服务器：westd-13176（4× RTX 6000 PRO 96GB）\\n- MVP 结论：核心假设获强支持（EN AUROC=0.754, 4/5 语言迁移成功, layer-depth 14.3pp, Pareto tradeoff 直接观测）\\n- Mean-shift 不可靠/不一致（部分语言微改善、部分恶化，无系统性）→ motivate CaCLR\\n- paper_framing.md ✅ | experiment_plan.yaml ✅ | Dream 模拟进行中（dream_20260520T185641）\\n- ⚠️ P1 ECE pass 依赖 post-hoc temp scaling (T=6.21)，需确认是否在 held-out set 上调\\n\\n## 实验计划（详见 experiment_plan.yaml）\\n- **P0**：plan_001(Qwen3-235B) + plan_002(Llama4 Scout) + plan_003(CaCLR) + plan_004(difficulty ablation)\\n- **P1**：plan_005(orthogonality) + plan_006(probe complexity) + plan_007(Belebele/MMLU-ProX) + plan_010(INT8 ablation)\\n- **P2**：plan_008(Gemma4) + plan_009(50+ languages)\\n- **MVP**：mvp_001 ✅ | mvp_002 bug 修复中 | mvp_003 RUNNING (Llama-3.1-8B, cuda:2)\\n- **覆盖风险**：Claims 2/3/4 各仅 1 个实验，需 Dream 反馈后评估是否加备份\\n\\n## 近期任务\\n- [ ] 等待 Dream 回调，按结果调整 framing/plan\\n- [ ] Agent 修复 --layers 默认值 bug（M004）+ mvp_002 重跑\\n- [ ] Agent 确认 temp scaling 是否在 held-out set 上调\\n- [ ] 确认 IRT difficulty scores 数据可获取性（plan_004 硬依赖）\\n- [ ] mvp_003 结果（cross-architecture 验证）\\n- [ ] Dream 通过后批准 P0 实验\\n\\n## GPU 预算\\n**已分配**：westd-13176 4× RTX 6000 PRO 96GB\\n**当前使用**：cuda:0 空闲 | cuda:1 空闲(mvp_002完成) | cuda:2 mvp_003 | cuda:3 空闲\\n**Critical path**：plan_001(Qwen3-235B INT8 ~235GB) 需 3-4 卡，是全计划瓶颈\\n**Fallback**：CaCLR 效果不显著 → paper 退化为 systematic characterization，仍可投但 significance 降级\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D004 | 2026-05-20 | MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段 | mvp_001 |\\n| D003 | 2026-05-20 | P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/ | mvp_001 |\\n| D002 | 2026-05-20 | MVP 模型固定为 Qwen2.5-7B-Instruct | — |\\n| D001 | 2026-05-20 | MVP 用 7-8B 模型验证核心假设，不直接上 235B | — |\\n\\n\\n\\n\", \"total_chars\": 1996, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b459f1d-7ed0-47de-9fd1-7537d58b8148",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "39f2f02d-66c4-4ee2-b1c7-e805a79324f6",
  "sourceToolAssistantUUID": "5b459f1d-7ed0-47de-9fd1-7537d58b8148",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T19:52:28.756Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014k8P9rRJzo1cpksLVrCh4j`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39f2f02d-66c4-4ee2-b1c7-e805a79324f6",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQRKQfoY9LY92KZ8pV4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74e6b2bc-cb8f-4e8b-aee8-65d6c20caa8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W7jF7wyS3Zy8hws2QUZxWf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1525,
      "cache_read_input_tokens": 17931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1525,
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

_source line 18 · 2026-05-20T19:52:28.769Z_

<details><summary>↩ Tool result · `toolu_014k8P9rRJzo1cpksLVrCh4j`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/memory.md\", \"content\": \"# Memory — xling_calib_direction\\n\\n## 环境配置\\n- **服务器**: westd-13176, 4× RTX 6000 PRO 96GB\\n- **环境**: conda base (`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`)\\n- **模型路径**: `/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct`（symlink `/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct`）\\n- **代码路径**: `/root/xling_calib_direction/`\\n- **Qwen2.5-7B-Instruct**: 28 layers (index 0-27), hidden_dim=3584\\n- **网络**: 不要用 `source /etc/network_turbo`（会破坏 HF SSL），用 `HF_ENDPOINT=https://hf-mirror.com`\\n- **模型下载**: 用 ModelScope（AutoDL 上 HF 代理太慢）\\n\\n## 数据集字段差异\\n- cais/mmlu: `choices` (list), `answer` (int 0-3)\\n- CohereForAI/Global-MMLU: `option_a/b/c/d` (str), `answer` (letter \\\"A\\\"-\\\"D\\\")\\n- `normalize_row()` 已处理两种格式\\n\\n## 激活提取速度\\n- Qwen2.5-7B-Instruct, BF16, RTX 6000 PRO 96GB: ~1 sample/s (MMLU 5-shot)\\n- 14K samples × 7 layers × 6 语言 ≈ 2h per GPU\\n\\n## MVP 实验关键发现 (2026-05-20)\\n\\n### Mean-shift alignment 完全无效（方法论发现）\\nMean-shift 对所有样本加同一常数向量 `(mean_en - mean_tgt)`。\\n- **不能改变 AUROC**: 经线性 probe 后等价于 logit 加常数，AUROC（rank-based）不变。\\n- **不能改善 calibration**: ΔECE 测试结果 0/5 语言达标。zh/ar 仅 marginal（<0.4pp），hi/sw 反而大幅恶化（+2.2pp/+6.4pp）。\\n- **结论**: 简单常数平移不足以 align 跨语言 representation。需要非常数方法（CDA/CORAL/Procrustes）。这是论文贡献空间。\\n\\n### Temperature scaling 有效修复 ECE\\n- Layer 24: T=5.36, ECE 0.1982→0.0888\\n- Layer 27: T=6.21, ECE 0.1951→0.0744\\n- T>1 说明 LogisticRegression 过于自信（overconfident），需要 softening\\n\\n### Layer 27 vs Layer 24: 最后一层更 language-specific\\n- EN AUROC: L27=0.7541 > L24=0.7486（最后一层英语 probe 最强）\\n- 但跨语言迁移: L24 全面优于 L27（zh 0.686 vs 0.661, ar 0.651 vs 0.635, hi 0.652 vs 0.626, ko 0.648 vs 0.607）\\n- **解读**: 最后一层 representation 更 language-specific，对 zero-shot transfer 不利。Optimal transfer layer ≠ optimal source-language layer。这是论文可讨论的有趣发现。\\n\\n### Swahili 始终最差\\n- Best zero-shot AUROC: sw=0.560 (L27) / 0.544 (L20)，均 < 0.58 阈值\\n- 与 low-resource 假设一致，论文中作为 expected limitation\\n\\n### 最终 Gate Check (2026-05-20)\\n- P1 ✅ PASS (AUROC=0.7541, ECE=0.0744 with temp scaling)\\n- P2 ✅ PASS (4/5 langs)\\n- P3 ✅ PASS (14.28pp)\\n- P4 ❌ FAIL (mean-shift 无效，0/5)\\n- 无 hard fail\\n- Overall: PARTIAL 3/4, 核心假设获强支持\\n\", \"total_chars\": 2071, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74e6b2bc-cb8f-4e8b-aee8-65d6c20caa8a",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "f0ab0b55-a467-4088-9a53-26234c97169c",
  "sourceToolAssistantUUID": "74e6b2bc-cb8f-4e8b-aee8-65d6c20caa8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T19:52:32.790Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DpTLCeUAP8gxN1bJfULoaD`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0ab0b55-a467-4088-9a53-26234c97169c",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQRcmhDYLeU7or2KYss",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aaebf434-c997-4100-a197-5add3c8fe078",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdSHcJi2b66neA1fkiYaSc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2949,
      "cache_read_input_tokens": 19456,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2949
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 19456,
          "cache_creation_input_tokens": 2949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2949,
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

_source line 20 · 2026-05-20T19:52:32.809Z_

<details><summary>↩ Tool result · `toolu_01DpTLCeUAP8gxN1bJfULoaD`</summary>

```text
literature_map.yaml
distill_tmp/karandikar2021sbece.yaml
distill_tmp/miao2026closing.yaml
distill_tmp/civelli2026shared.yaml
distill_tmp/confidence_manifold2026.yaml
distill_tmp/xiao2025knowledge.yaml
distill_tmp/joshi2025calibration.yaml
distill_tmp/khanmohammadi2025ccps.yaml
distill_tmp/liu2025middle.yaml
distill_tmp/ji2025calibrating.yaml
distill_tmp/ravisankar2026dali.yaml
distill_tmp/zhou2025lace.yaml
distill_tmp/miao2026coral.yaml
decisions.yaml
experiment_plan.yaml
mistakes.yaml
artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml
registry.yaml
artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml
artifacts/dream_reports/dream_20260520T185641/worst/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aaebf434-c997-4100-a197-5add3c8fe078",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "fee5c56b-2a0b-490e-ad0e-bd29f882da2b",
  "sourceToolAssistantUUID": "aaebf434-c997-4100-a197-5add3c8fe078",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T19:52:36.160Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01H626hiaph1Naj2U2r8NoRq`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "experiment_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fee5c56b-2a0b-490e-ad0e-bd29f882da2b",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQRu4UfqubK8QQzCgjt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffc3497e-2718-476e-acb8-708f87cf557c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5E8ZJXFVYAudY6hVUpwPC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 449,
      "cache_read_input_tokens": 22405,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 22 · 2026-05-20T19:52:36.175Z_

<details><summary>↩ Tool result · `toolu_01H626hiaph1Naj2U2r8NoRq`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffc3497e-2718-476e-acb8-708f87cf557c",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "b0194ff5-c993-4a7f-9d4d-1adb0263c67f",
  "sourceToolAssistantUUID": "ffc3497e-2718-476e-acb8-708f87cf557c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T19:52:36.726Z_

<details open><summary>🔧 Tool call — Read · `toolu_01944NU9qMkq8iVHeN52kUqY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0194ff5-c993-4a7f-9d4d-1adb0263c67f",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQRu4UfqubK8QQzCgjt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0487ab20-0a77-43d4-86db-0b802fb05e05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5E8ZJXFVYAudY6hVUpwPC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 449,
      "cache_read_input_tokens": 22405,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 449
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 22405,
          "cache_creation_input_tokens": 449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 449,
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

_source line 24 · 2026-05-20T19:52:36.977Z_

<details><summary>↩ Tool result · `toolu_01944NU9qMkq8iVHeN52kUqY`</summary>

```text
1	tier: best
2	narrative_guidance: 'Original framing stands: "CaCLR shifts the cross-lingual calibration
3	  Pareto frontier." All 4 claims form an unbroken causal chain — discovery → analysis
4	  → method → mechanism. Headline: CaCLR reduces non-EN ECE by 30-50% over temp scaling
5	  with zero target-language labels. Pareto frontier is the organizing principle, CaCLR
6	  is the actionable contribution, decomposition explains why it works, orthogonality
7	  explains why output-based methods can''t.
8	
9	  '
10	imagined_experiments:
11	- name: Full Pareto Frontier — Qwen3-235B-A22B
12	  plan_id: plan_001
13	  description: 'Extract activations at every 4th layer (24 probed layers out of 94),
14	    20 languages, train English correctness probes (logistic regression + 2-layer
15	    MLP), evaluate 5 transfer conditions (zero-shot, mean-shift, linear projection,
16	    few-shot 25/100, CaCLR).
17	
18	    '
19	  expected_results:
20	    en_auroc_best_layer: 0.843
21	    en_best_layer_idx: 72
22	    en_auroc_range:
23	    - 0.621
24	    - 0.843
25	    en_ece_raw_best: 0.162
26	    en_ece_tempcal_best: 0.054
27	    temp_scaling_T: 4.87
28	    zs_transfer_auroc_mean_19lang_best_transfer_layer: 0.762
29	    zs_best_transfer_layer_idx: 56
30	    zs_transfer_drop_from_en_mean_pp: 8.1
31	    zs_auroc_by_tier:
32	      high_resource_mean: 0.791
33	      mid_resource_mean: 0.754
34	      low_resource_mean: 0.683
35	    zs_auroc_by_lang:
36	      en: 0.843
37	      zh: 0.802
38	      de: 0.796
39	      fr: 0.793
40	      es: 0.789
41	      ja: 0.785
42	      ru: 0.782
43	      pt: 0.788
44	      it: 0.786
45	      ar: 0.768
46	      hi: 0.761
47	      ko: 0.755
48	      vi: 0.749
49	      th: 0.743
50	      bn: 0.738
51	      tr: 0.756
52	      nl: 0.79
53	      sw: 0.695
54	      yo: 0.672
55	      ig: 0.681
56	    mean_shift_improvement_count: 2
57	    mean_shift_delta_ece_mean: 1.41
58	    linproj_auroc_mean_19lang: 0.724
59	    fewshot_25_auroc_mean_19lang: 0.748
60	    fewshot_100_auroc_mean_19lang: 0.771
61	    pareto_depth_transfer_rank_corr: 0.88
62	    pareto_frontier_layers:
63	    - 40
64	    - 44
65	    - 48
66	    - 52
67	    - 56
68	    - 60
69	    layers_above_0p5_auroc_count: 22
70	  result_rationale: 'Qwen3-235B-A22B is a 94-layer MoE with massive representation
71	    capacity. The jump from MVP''s 7B (en AUROC 0.754) to 235B is expected to yield
72	    ~9pp AUROC gain, consistent with prior probing literature showing log-linear scaling
73	    of linear probe accuracy with model parameters (Burns et al., Marks et al.). The
74	    MoE architecture concentrates expert representations, producing cleaner correctness
75	    signals in intermediate layers. The Pareto frontier emerges because deeper layers
76	    (L72+) specialize for English-dominant pretraining data distribution — the model''s
77	    language-specific processing intensifies past ~75% depth, degrading cross-lingual
78	    invariance. The best transfer layer (L56, ~60% depth) sits in the "universal reasoning"
79	    zone before language-specific heads activate. Low-resource languages (sw, yo,
80	    ig) still transfer above 0.65 AUROC because GlobalMMLU questions share structural
81	    patterns that even underrepresented languages partially align with in middle layers.
82	    Mean-shift continues to mostly fail because correctness directions are not simply
83	    mean-offset between languages — they require rotation, not translation, which
84	    linear projection and CaCLR address.
85	
86	    '
87	  tables:
88	  - name: 'Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by
89	      Layer'
90	    columns:
91	    - layer_idx
92	    - layer_depth_pct
93	    - en_auroc
94	    - zs_mean_auroc_19
95	    - zs_drop_pp
96	    - on_pareto
97	    rows:
98	    - - 4
99	      - 4
100	      - 0.621
101	      - 0.608
102	      - 1.3
103	      - false
104	    - - 8
105	      - 9
106	      - 0.648
107	      - 0.637
108	      - 1.1
109	      - false
110	    - - 12
111	      - 13
112	      - 0.689
113	      - 0.671
114	      - 1.8
115	      - false
116	    - - 16
117	      - 17
118	      - 0.712
119	      - 0.698
120	      - 1.4
121	      - false
122	    - - 20
123	      - 21
124	      - 0.738
125	      - 0.724
126	      - 1.4
127	      - false
128	    - - 24
129	      - 26
130	      - 0.756
131	      - 0.742
132	      - 1.4
133	      - false
134	    - - 28
135	      - 30
136	      - 0.771
137	      - 0.755
138	      - 1.6
139	      - false
140	    - - 32
141	      - 34
142	      - 0.784
143	      - 0.764
144	      - 2.0
145	      - false
146	    - - 36
147	      - 38
148	      - 0.795
149	      - 0.771
150	      - 2.4
151	      - false
152	    - - 40
153	      - 43
154	      - 0.803
155	      - 0.776
156	      - 2.7
157	      - true
158	    - - 44
159	      - 47
160	      - 0.81
161	      - 0.774
162	      - 3.6
163	      - true
164	    - - 48
165	      - 51
166	      - 0.816
167	      - 0.77
168	      - 4.6
169	      - true
170	    - - 52
171	      - 55
172	      - 0.822
173	      - 0.765
174	      - 5.7
175	      - true
176	    - - 56
177	      - 60
178	      - 0.827
179	      - 0.762
180	      - 6.5
181	      - true
182	    - - 60
183	      - 64
184	      - 0.831
185	      - 0.753
186	      - 7.8
187	      - true
188	    - - 64
189	      - 68
190	      - 0.835
191	      - 0.741
192	      - 9.4
193	      - false
194	    - - 68
195	      - 72
196	      - 0.839
197	      - 0.728
198	      - 11.1
199	      - false
200	    - - 72
201	      - 77
202	      - 0.843
203	      - 0.712
204	      - 13.1
205	      - false
206	    - - 76
207	      - 81
208	      - 0.841
209	      - 0.694
210	      - 14.7
211	      - false
212	    - - 80
213	      - 85
214	      - 0.838
215	      - 0.671
216	      - 16.7
217	      - false
218	    - - 84
219	      - 89
220	      - 0.832
221	      - 0.643
222	      - 18.9
223	      - false
224	    - - 88
225	      - 94
226	      - 0.819
227	      - 0.611
228	      - 20.8
229	      - false
230	    - - 92
231	      - 98
232	      - 0.791
233	      - 0.574
234	      - 21.7
235	      - false
236	    - - 94
237	      - 100
238	      - 0.762
239	      - 0.541
240	      - 22.1
241	      - false
242	  - name: 'Table 2: Transfer Condition Comparison (at best-transfer layer L56)'
243	    columns:
244	    - condition
245	    - auroc_mean_19
246	    - ece_mean_19
247	    - ece_reduction_vs_tempcal_pct
248	    rows:
249	    - - zero-shot
250	      - 0.762
251	      - 0.098
252	      - 0
253	    - - mean-shift
254	      - 0.758
255	      - 0.101
256	      - -3.1
257	    - - linear_projection
258	      - 0.781
259	      - 0.082
260	      - 16.3
261	    - - few-shot-25
262	      - 0.748
263	      - 0.089
264	      - 9.2
265	    - - few-shot-100
266	      - 0.771
267	      - 0.079
268	      - 19.4
269	    - - CaCLR
270	      - 0.814
271	      - 0.058
272	      - 40.8
273	  figures_description:
274	  - 'Figure 1a: Pareto frontier scatter plot (EN AUROC x-axis vs ZS mean AUROC y-axis),
275	    each point a layer, Pareto-optimal layers highlighted in red. Clear convex frontier
276	    shape from L40-L60.'
277	  - 'Figure 1b: Heatmap of ZS AUROC by language (y-axis, ordered by resource tier)
278	    × layer depth (x-axis). Shows warm band in mid-layers, cooling at extremes, with
279	    low-resource langs cooling earlier.'
280	  analysis: 'The Pareto frontier is crisp and monotonic: 6 layers form the efficient
281	    frontier between L40-L60. The rank correlation (Spearman) between layer depth
282	    and transfer degradation is ρ=0.88 (p<0.001). The frontier''s shape confirms that
283	    the depth- transferability tradeoff is not an artifact of small models — it amplifies
284	    at scale. The 16pp gap between best-EN layer (L72) and best-transfer layer (L56)
285	    is larger than MVP''s ~3-layer gap, consistent with deeper models having more
286	    room for language-specific specialization. All high-resource languages pass AUROC
287	    > 0.75 at the best-transfer layer; all low-resource languages exceed 0.65.
288	
289	    '
290	- name: Full Pareto Frontier — Llama 4 Scout
291	  plan_id: plan_002
292	  description: 'Extract activations at every 4th layer (12 probed layers out of 48),
293	    20 languages, 5 transfer conditions. INT8 weight quantization.
294	
295	    '
296	  expected_results:
297	    en_auroc_best_layer: 0.821
298	    en_best_layer_idx: 36
299	    en_auroc_range:
300	    - 0.634
301	    - 0.821
302	    en_ece_raw_best: 0.174
303	    en_ece_tempcal_best: 0.061
304	    temp_scaling_T: 5.34
305	    zs_transfer_auroc_mean_19lang_best_transfer_layer: 0.741
306	    zs_best_transfer_layer_idx: 28
307	    zs_transfer_drop_from_en_mean_pp: 8.0
308	    zs_auroc_by_tier:
309	      high_resource_mean: 0.771
310	      mid_resource_mean: 0.733
311	      low_resource_mean: 0.661
312	    zs_auroc_by_lang:
313	      en: 0.821
314	      zh: 0.784
315	      de: 0.778
316	      fr: 0.775
317	      es: 0.771
318	      ja: 0.766
319	      ru: 0.762
320	      pt: 0.77
321	      it: 0.768
322	      ar: 0.748
323	      hi: 0.741
324	      ko: 0.735
325	      vi: 0.729
326	      th: 0.722
327	      bn: 0.718
328	      tr: 0.737
329	      nl: 0.772
330	      sw: 0.674
331	      yo: 0.641
332	      ig: 0.667
333	    mean_shift_improvement_count: 1
334	    linproj_auroc_mean_19lang: 0.706
335	    fewshot_25_auroc_mean_19lang: 0.728
336	    fewshot_100_auroc_mean_19lang: 0.752
337	    pareto_depth_transfer_rank_corr: 0.82
338	    pareto_frontier_layers:
339	    - 20
340	    - 24
341	    - 28
342	    - 32
343	  result_rationale: 'Llama 4 Scout has 48 layers (fewer than Qwen3''s 94) and a different
344	    MoE routing strategy (16 experts, top-2). With roughly 109B total / ~17B active
345	    params, its active compute is smaller than Qwen3-235B''s ~22B active. This yields
346	    ~2pp lower EN AUROC and ~2pp lower transfer AUROC. The Pareto frontier has fewer
347	    points (4 vs 6) due to coarser layer sampling (every 4th of 48 = 12 points), but
348	    the monotonic depth-transfer tradeoff still holds clearly. Llama 4 Scout''s best
349	    transfer layer sits at ~58% depth (L28), remarkably close to Qwen3''s 60%, suggesting
350	    a universal "mid-depth transfer zone" across architectures. The rank correlation
351	    is slightly lower (0.82 vs 0.88) due to fewer data points but still highly significant.
352	    Low-resource languages are slightly weaker because Meta''s multilingual pretraining
353	    mix underrepresents African languages compared to Qwen3.
354	
355	    '
356	  tables:
357	  - name: 'Table 3: Llama 4 Scout Pareto Frontier'
358	    columns:
359	    - layer_idx
360	    - layer_depth_pct
361	    - en_auroc
362	    - zs_mean_auroc_19
363	    - zs_drop_pp
364	    - on_pareto
365	    rows:
366	    - - 4
367	      - 8
368	      - 0.634
369	      - 0.624
370	      - 1.0
371	      - false
372	    - - 8
373	      - 17
374	      - 0.672
375	      - 0.659
376	      - 1.3
377	      - false
378	    - - 12
379	      - 25
380	      - 0.714
381	      - 0.699
382	      - 1.5
383	      - false
384	    - - 16
385	      - 33
386	      - 0.745
387	      - 0.729
388	      - 1.6
389	      - false
390	    - - 20
391	      - 42
392	      - 0.768
393	      - 0.748
394	      - 2.0
395	      - true
396	    - - 24
397	      - 50
398	      - 0.786
399	      - 0.745
400	      - 4.1
401	      - true
402	    - - 28
403	      - 58
404	      - 0.798
405	      - 0.741
406	      - 5.7
407	      - true
408	    - - 32
409	      - 67
410	      - 0.81
411	      - 0.732
412	      - 7.8
413	      - true
414	    - - 36
415	      - 75
416	      - 0.821
417	      - 0.714
418	      - 10.7
419	      - false
420	    - - 40
421	      - 83
422	      - 0.818
423	      - 0.689
424	      - 12.9
425	      - false
426	    - - 44
427	      - 92
428	      - 0.804
429	      - 0.651
430	      - 15.3
431	      - false
432	    - - 48
433	      - 100
434	      - 0.771
435	      - 0.608
436	      - 16.3
437	      - false
438	  - name: 'Table 4: Cross-Architecture Pareto Frontier Agreement'
439	    columns:
440	    - metric
441	    - qwen3_235b
442	    - llama4_scout
443	    - agreement
444	    rows:
445	    - - best_en_layer_depth_pct
446	      - 77
447	      - 75
448	      - within 2pp
449	    - - best_transfer_layer_depth_pct
450	      - 60
451	      - 58
452	      - within 2pp
453	    - - pareto_zone_depth_range_pct
454	      - 43-64
455	      - 42-67
456	      - overlapping
457	    - - depth_transfer_rank_corr
458	      - 0.88
459	      - 0.82
460	      - both >0.75
461	    - - frontier_shape
462	      - convex monotonic
463	      - convex monotonic
464	      - consistent
465	  figures_description:
466	  - 'Figure 2: Overlaid Pareto frontiers for both architectures (normalized depth
467	    %). Shows near-identical frontier shapes with Qwen3 shifted up-right (better overall)
468	    but same curvature.'
469	  analysis: 'Cross-architecture agreement is high: both models show best transfer
470	    at ~59% depth, the Pareto frontier occupies the 42-67% depth band, and the rank
471	    correlation between depth and transfer degradation exceeds 0.75 in both. The frontier
472	    shape is architecture-invariant — it''s the depth-normalized position, not absolute
473	    layer count, that determines the tradeoff. This validates Claim 1 at scale.
474	
475	    '
476	- name: CaCLR Implementation and Comparative Evaluation
477	  plan_id: plan_003
478	  description: 'CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) implementation. Train
479	    on English labels + unlabeled parallel activations. Compare vs all 5 conditions
480	    across full Pareto frontier, both models × 20 languages. Hyperparameter tuning
481	    (α, β).
482	
483	    '
484	  expected_results:
485	    best_alpha: 0.15
486	    best_beta: 0.08
487	    qwen3_caclr_auroc_mean_19lang: 0.814
488	    qwen3_caclr_ece_mean_19lang: 0.058
489	    qwen3_caclr_vs_linproj_auroc_delta_pp: 3.3
490	    qwen3_caclr_vs_zeroshot_auroc_delta_pp: 5.2
491	    qwen3_caclr_ece_reduction_vs_tempcal_pct: 40.8
492	    qwen3_caclr_best_operating_layer: 64
493	    llama4_caclr_auroc_mean_19lang: 0.793
494	    llama4_caclr_ece_mean_19lang: 0.064
495	    llama4_caclr_vs_linproj_auroc_delta_pp: 3.1
496	    llama4_caclr_vs_zeroshot_auroc_delta_pp: 5.2
497	    llama4_caclr_ece_reduction_vs_tempcal_pct: 38.5
498	    llama4_caclr_best_operating_layer: 32
499	    caclr_vs_linproj_auroc_delta_pp_mean: 3.2
500	    caclr_ece_reduction_vs_tempcal_pct_mean: 39.7
501	    caclr_improvement_pass_rate: 0.92
502	    caclr_pareto_shift_layers: 2
503	    low_resource_caclr_auroc:
504	      sw_qwen3: 0.731
505	      yo_qwen3: 0.709
506	      ig_qwen3: 0.718
507	      sw_llama4: 0.712
508	      yo_llama4: 0.681
509	      ig_llama4: 0.698
510	    low_resource_zs_pass_rate: 1.0
511	  result_rationale: 'CaCLR''s consistency loss (β·L_consistency) directly penalizes
512	    divergence between EN and non-EN probe outputs on parallel/comparable activations,
513	    forcing the probe to learn language-invariant features. This is strictly more
514	    informative than linear projection (which only aligns means and covariances post-hoc)
515	    because it shapes the learned representation during training. The 3.2pp AUROC
516	    gain over linear projection reflects the value of end-to-end optimization: linear
517	    projection corrects first-order distributional mismatch but not the nonlinear
518	    feature interactions that L_consistency captures. The SB-ECE term (α·L_SB-ECE)
519	    provides calibration-aware training that temperature scaling cannot — it directly
520	    optimizes the calibration objective rather than post-hoc rescaling. The 40% ECE
521	    reduction over temperature scaling arises because CaCLR addresses the root cause
522	    (representation misalignment) rather than the symptom (miscalibrated probabilities).
523	    The Pareto frontier shift is the key result: CaCLR allows operating 2 layers deeper
524	    than the ZS-optimal point while maintaining equivalent or better transfer — it
525	    literally pushes the Pareto frontier outward. Low-resource languages benefit most
526	    from L_consistency because their activation distributions are most misaligned
527	    from EN; the consistency term provides the strongest gradient signal precisely
528	    where the gap is largest.
529	
530	    '
531	  tables:
532	  - name: 'Table 5: CaCLR vs Baselines — Full Comparison (averaged across both architectures)'
533	    columns:
534	    - method
535	    - auroc_mean_19
536	    - ece_mean_19
537	    - requires_target_labels
538	    - params_overhead
539	    rows:
540	    - - zero-shot
541	      - 0.752
542	      - 0.098
543	      - 'no'
544	      - '0'
545	    - - mean-shift
546	      - 0.747
547	      - 0.102
548	      - 'no'
549	      - '0'
550	    - - linear_projection
551	      - 0.77
552	      - 0.082
553	      - 'no'
554	      - d×d matrix
555	    - - few-shot-25
556	      - 0.738
557	      - 0.089
558	      - yes (25)
559	      - '0'
560	    - - few-shot-100
561	      - 0.762
562	      - 0.079
563	      - yes (100)
564	      - '0'
565	    - - CaCLR
566	      - 0.804
567	      - 0.061
568	      - 'no'
569	      - ~1% probe params
570	  - name: 'Table 6: CaCLR Ablation — Loss Component Contributions'
571	    columns:
572	    - configuration
573	    - auroc_mean_19
574	    - ece_mean_19
575	    - delta_vs_full_auroc_pp
576	    rows:
577	    - - L_BCE_only (= zero-shot probe)
578	      - 0.752
579	      - 0.098
580	      - -5.2
581	    - - L_BCE + L_SB-ECE
582	      - 0.768
583	      - 0.072
584	      - -3.6
585	    - - L_BCE + L_consistency
586	      - 0.793
587	      - 0.078
588	      - -1.1
589	    - - L_BCE + L_SB-ECE + L_consistency (full CaCLR)
590	      - 0.804
591	      - 0.061
592	      - 0.0
593	  - name: 'Table 7: CaCLR Pareto Frontier Shift (Qwen3-235B)'
594	    columns:
595	    - layer_idx
596	    - zs_auroc_19
597	    - caclr_auroc_19
598	    - shift_pp
599	    - on_shifted_pareto
600	    rows:
601	    - - 40
602	      - 0.776
603	      - 0.798
604	      - 2.2
605	      - false
606	    - - 44
607	      - 0.774
608	      - 0.8
609	      - 2.6
610	      - false
611	    - - 48
612	      - 0.77
613	      - 0.803
614	      - 3.3
615	      - true
616	    - - 52
617	      - 0.765
618	      - 0.806
619	      - 4.1
620	      - true
621	    - - 56
622	      - 0.762
623	      - 0.81
624	      - 4.8
625	      - true
626	    - - 60
627	      - 0.753
628	      - 0.814
629	      - 6.1
630	      - true
631	    - - 64
632	      - 0.741
633	      - 0.814
634	      - 7.3
635	      - true
636	    - - 68
637	      - 0.728
638	      - 0.808
639	      - 8.0
640	      - true
641	    - - 72
642	      - 0.712
643	      - 0.796
644	      - 8.4
645	      - false
646	  figures_description:
647	  - 'Figure 3: Pareto frontier before/after CaCLR. ZS frontier (blue) vs CaCLR frontier
648	    (red), showing outward shift. CaCLR''s optimal operating point is 2 layers deeper
649	    with +5pp transfer AUROC.'
650	  - 'Figure 4: Per-language AUROC improvement from CaCLR over linear projection, grouped
651	    by resource tier. Low-resource languages show largest gains (4-6pp), high-resource
652	    2-3pp.'
653	  - 'Figure 5: Loss component ablation bar chart — stacked contributions of L_SB-ECE
654	    and L_consistency to final AUROC and ECE improvements.'
655	  analysis: 'CaCLR decisively outperforms all baselines. The ablation shows both loss
656	    terms contribute: L_consistency provides the bulk of AUROC improvement (+4.1pp
657	    alone), while L_SB-ECE provides calibration refinement (ECE drops from 0.078 to
658	    0.061 when added). The interaction is synergistic — joint optimization yields
659	    better results than either term alone. The Pareto shift is the headline result:
660	    at the same EN calibration quality (L64, AUROC 0.835), CaCLR achieves 0.814 transfer
661	    vs 0.741 zero-shot — a 7.3pp improvement. This shifts the practical recommendation
662	    from "use shallower layers for transfer" to "use CaCLR and operate at deeper,
663	    better-calibrated layers." The improvement pass rate of 92% (35/38 model-lang
664	    pairs) demonstrates consistency. The 3 non-improving pairs are high-resource languages
665	    (fr, nl, de on Llama 4 Scout) where zero-shot transfer is already excellent and
666	    the consistency loss has minimal signal to exploit.
667	
668	    '
669	- name: Difficulty-Controlled Ablation
670	  plan_id: plan_004
671	  description: 'IRT difficulty probes (Ridge regression), project out difficulty direction,
672	    retrain correctness probes on residuals, evaluate transfer. 10 languages × 8 layers
673	    per model.
674	
675	    '
676	  expected_results:
677	    difficulty_probe_r2_mean: 0.72
678	    difficulty_var_explained_pct_mean: 68.4
679	    difficulty_var_explained_pct_range:
680	    - 58.2
681	    - 79.1
682	    residual_en_auroc_drop_pp: 4.2
683	    residual_zs_transfer_drop_pp: 1.1
684	    capability_specific_var_pct: 31.6
685	    capability_specific_transfer_degradation_pct: 87
686	    difficulty_component_transfer_degradation_pct: 13
687	    decomp_prescriptive_accuracy: 0.81
688	    difficulty_var_by_depth:
689	      shallow_20pct: 0.74
690	      mid_50pct: 0.69
691	      deep_80pct: 0.62
692	    capability_transfer_drop_by_depth:
693	      shallow_20pct: 0.8
694	      mid_50pct: 3.4
695	      deep_80pct: 9.7
696	  result_rationale: 'IRT difficulty is a strong, language-agnostic property — harder
697	    questions are harder everywhere. Ridge regression captures this cleanly (R²=0.72)
698	    because difficulty is linearly encoded in intermediate representations (Civelli
699	    et al. confirmed this). The difficulty component accounts for 68% of explained
700	    variance because GlobalMMLU correctness is heavily driven by item difficulty:
701	    a model gets easy questions right in all languages and hard questions wrong in
702	    all languages. After projecting out difficulty, the residual correctness signal
703	    is "capability-specific" — it captures language-dependent competence differences.
704	    This residual transfers poorly at deep layers (9.7pp drop at 80% depth vs 0.8pp
705	    at 20% depth) because deep layers encode language-specific processing that makes
706	    capability assessments non-transferable. The difficulty component transfers well
707	    at all depths (only 13% of total transfer degradation) because it''s language-invariant
708	    by construction. This decomposition is prescriptive: when difficulty explains
709	    most of a language''s correctness variance, simple zero-shot transfer suffices;
710	    when the capability residual is large, CaCLR is needed. The 81% prescriptive accuracy
711	    validates the decomposition as more than descriptive.
712	
713	    '
714	  tables:
715	  - name: 'Table 8: Decomposition Results — Difficulty vs Capability Components'
716	    columns:
717	    - component
718	    - var_explained_pct
719	    - transfer_auroc_mean
720	    - transfer_drop_from_en_pp
721	    - share_of_total_transfer_drop_pct
722	    rows:
723	    - - full_correctness
724	      - 100
725	      - 0.752
726	      - 8.1
727	      - 100
728	    - - difficulty_shared
729	      - 68.4
730	      - 0.738
731	      - 1.1
732	      - 13
733	    - - capability_specific
734	      - 31.6
735	      - 0.614
736	      - 14.2
737	      - 87
738	  - name: 'Table 9: Capability-Specific Transfer Drop by Depth'
739	    columns:
740	    - depth_band
741	    - difficulty_transfer_drop_pp
742	    - capability_transfer_drop_pp
743	    - ratio
744	    rows:
745	    - - 0-30%
746	      - 0.3
747	      - 0.8
748	      - 2.7×
749	    - - 30-60%
750	      - 0.8
751	      - 3.4
752	      - 4.3×
753	    - - 60-90%
754	      - 1.6
755	      - 9.7
756	      - 6.1×
757	  figures_description:
758	  - 'Figure 6: Stacked area chart showing difficulty vs capability variance across
759	    depth. Difficulty dominates at all depths but capability grows at deeper layers.'
760	  - 'Figure 7: Transfer degradation decomposed into difficulty (flat, near-zero) and
761	    capability (exponentially increasing with depth) components.'
762	  analysis: 'The decomposition cleanly separates: difficulty-shared signal is the
763	    majority (68%) of correctness variance and transfers near-perfectly across languages
764	    and depths. The capability-specific residual (32%) drives nearly all transfer
765	    degradation (87%), and this degradation accelerates exponentially with depth.
766	    This explains the Pareto frontier mechanistically: deeper layers have stronger
767	    capability-specific signals that improve EN calibration but impede transfer. CaCLR
768	    works because its consistency loss specifically targets the capability-specific
769	    component — forcing alignment of the non-difficulty residual across languages.
770	    The prescriptive value (81% accuracy in predicting when CaCLR is needed) confirms
771	    this is a load-bearing decomposition, not a post-hoc narrative.
772	
773	    '
774	- name: Cross-Lingual Orthogonality Analysis
775	  plan_id: plan_005
776	  description: 'Extract verbalized confidence direction via prompted confidence scores,
777	    compute cosine similarity with correctness direction across 20 languages × 2 architectures.
778	    Analyze by resource tier and language family.
779	
780	    '
781	  expected_results:
782	    orthogonality_cosine_mean_overall: 0.052
783	    orthogonality_cosine_range:
784	    - 0.018
785	    - 0.094
786	    orthogonality_cosine_en: 0.034
787	    qwen3_cosine_mean: 0.048
788	    llama4_cosine_mean: 0.057
789	    high_resource_cosine_mean: 0.041
790	    mid_resource_cosine_mean: 0.054
791	    low_resource_cosine_mean: 0.074
792	    cosine_by_lang:
793	      en: 0.034
794	      zh: 0.038
795	      de: 0.036
796	      fr: 0.039
797	      es: 0.041
798	      ja: 0.044
799	      ru: 0.043
800	      pt: 0.04
801	      it: 0.042
802	      ar: 0.051
803	      hi: 0.055
804	      ko: 0.049
805	      vi: 0.058
806	      th: 0.061
807	      bn: 0.056
808	      tr: 0.052
809	      nl: 0.037
810	      sw: 0.078
811	      yo: 0.094
812	      ig: 0.082
813	    all_langs_below_0p1: true
814	    cosine_resource_tier_correlation: -0.68
815	  result_rationale: 'Miao & Ungar (2026) established correctness-confidence orthogonality
816	    (cosine < 0.04) for English on 7-8B models. We extend to 20 languages on larger
817	    models. The orthogonality persists universally (all < 0.1) because it reflects
818	    a fundamental architectural property: verbalized confidence is generated by the
819	    language modeling head from surface-level token probabilities, while correctness
820	    is encoded in intermediate representation geometry. These are structurally decoupled
821	    in transformer architectures. The slight increase in cosine for low-resource languages
822	    (0.074 mean vs 0.041 for high-resource) occurs because low-resource languages
823	    have noisier confidence elicitation — the model''s verbalized confidence in Yoruba
824	    is less well-calibrated and leaks some correctness signal, producing weak correlation.
825	    The resource-tier gradient (ρ=-0.68) suggests that better multilingual training
826	    data produces cleaner separation between correctness and confidence representations.
827	    The cross-architecture consistency (Qwen3: 0.048, Llama4: 0.057) confirms this
828	    is not architecture-specific. Llama 4''s slightly higher cosines may reflect its
829	    less aggressive multilingual pretraining compared to Qwen3.
830	
831	    '
832	  tables:
833	  - name: 'Table 10: Correctness-Confidence Cosine Similarity by Language and Architecture'
834	    columns:
835	    - language
836	    - resource_tier
837	    - qwen3_cosine
838	    - llama4_cosine
839	    - mean_cosine
840	    rows:
841	    - - en
842	      - high
843	      - 0.031
844	      - 0.037
845	      - 0.034
846	    - - zh
847	      - high
848	      - 0.035
849	      - 0.041
850	      - 0.038
851	    - - de
852	      - high
853	      - 0.033
854	      - 0.039
855	      - 0.036
856	    - - fr
857	      - high
858	      - 0.036
859	      - 0.042
860	      - 0.039
861	    - - es
862	      - high
863	      - 0.038
864	      - 0.044
865	      - 0.041
866	    - - ja
867	      - high
868	      - 0.041
869	      - 0.047
870	      - 0.044
871	    - - ru
872	      - high
873	      - 0.04
874	      - 0.046
875	      - 0.043
876	    - - pt
877	      - high
878	      - 0.037
879	      - 0.043
880	      - 0.04
881	    - - it
882	      - high
883	      - 0.039
884	      - 0.045
885	      - 0.042
886	    - - nl
887	      - high
888	      - 0.034
889	      - 0.04
890	      - 0.037
891	    - - ar
892	      - mid
893	      - 0.047
894	      - 0.055
895	      - 0.051
896	    - - hi
897	      - mid
898	      - 0.051
899	      - 0.059
900	      - 0.055
901	    - - ko
902	      - mid
903	      - 0.045
904	      - 0.053
905	      - 0.049
906	    - - vi
907	      - mid
908	      - 0.054
909	      - 0.062
910	      - 0.058
911	    - - th
912	      - mid
913	      - 0.057
914	      - 0.065
915	      - 0.061
916	    - - bn
917	      - mid
918	      - 0.052
919	      - 0.06
920	      - 0.056
921	    - - tr
922	      - mid
923	      - 0.048
924	      - 0.056
925	      - 0.052
926	    - - sw
927	      - low
928	      - 0.073
929	      - 0.083
930	      - 0.078
931	    - - yo
932	      - low
933	      - 0.089
934	      - 0.099
935	      - 0.094
936	    - - ig
937	      - low
938	      - 0.077
939	      - 0.087
940	      - 0.082
941	  - name: 'Table 11: Orthogonality Summary Statistics'
942	    columns:
943	    - statistic
944	    - qwen3_235b
945	    - llama4_scout
946	    - both_models
947	    rows:
948	    - - cosine_mean
949	      - 0.048
950	      - 0.057
951	      - 0.052
952	    - - cosine_std
953	      - 0.015
954	      - 0.017
955	      - 0.016
956	    - - cosine_max
957	      - 0.089
958	      - 0.099
959	      - 0.094
960	    - - cosine_min
961	      - 0.031
962	      - 0.037
963	      - 0.018
964	    - - all_below_0.1
965	      - yes (20/20)
966	      - yes (19/20)
967	      - 39/40
968	    - - resource_tier_corr
969	      - -0.71
970	      - -0.65
971	      - -0.68
972	  figures_description:
973	  - 'Figure 8: Cosine similarity violin plots by resource tier, showing clear gradient
974	    from high (tight around 0.04) to low (spread around 0.08). All below 0.1 threshold.'
975	  - 'Figure 9: Scatter plot of cosine similarity vs language resource level (log wiki
976	    size), colored by architecture. Strong negative trend.'
977	  analysis: 'Orthogonality generalizes comprehensively. The mean cosine of 0.052 across
978	    all 40 language-architecture pairs is well within the "near-orthogonal" regime
979	    (< 0.1). The resource-tier gradient is the novel finding: it suggests that output-based
980	    calibration methods are not just structurally limited but are *more* limited for
981	    well-resourced languages where the orthogonality is strongest. This strengthens
982	    the motivation for probe-based approaches universally and for CaCLR specifically
983	    in multilingual settings. Yoruba''s 0.094 is the only value approaching the 0.1
984	    threshold (on Llama4 it hits 0.099), which is worth noting but does not break
985	    the claim.
986	
987	    '
988	- name: Probe Complexity Comparison
989	  plan_id: plan_006
990	  description: 'Logistic regression vs 2-layer MLP at each probed layer, both models.
991	    Compare English accuracy, cross-lingual transfer degradation, calibration quality.
992	
993	    '
994	  expected_results:
995	    logreg_en_auroc_best: 0.843
996	    mlp_en_auroc_best: 0.856
997	    mlp_en_auroc_gain_pp: 1.3
998	    logreg_zs_transfer_drop_mean_pp: 8.1
999	    mlp_zs_transfer_drop_mean_pp: 12.4
1000	    transfer_degradation_ratio: 1.53
1001	    logreg_ece_mean: 0.054
1002	    mlp_ece_mean: 0.068
1003	    logreg_transfer_advantage_shallow_pp: 2.1
1004	    logreg_transfer_advantage_deep_pp: 6.8
1005	  result_rationale: 'Linear probes transfer better because they learn a single hyperplane
1006	    in activation space — the hyperplane generalizes across languages when the underlying
1007	    geometry is approximately shared (as it is in mid-depth layers). MLPs learn nonlinear
1008	    decision boundaries that fit English-specific feature interactions, gaining ~1.3pp
1009	    EN AUROC but losing ~4.3pp in transfer. The transfer gap widens at deeper layers
1010	    (6.8pp advantage for logreg) because deep layers have more language-specific nonlinear
1011	    structure that MLPs exploit but logreg ignores. This justifies our choice of linear
1012	    probes for the main results and supports the geometric interpretation of the Pareto
1013	    frontier: it''s about linear subspace alignment, not complex feature interactions.
1014	
1015	    '
1016	  tables:
1017	  - name: 'Table 12: Probe Complexity Comparison'
1018	    columns:
1019	    - probe_type
1020	    - en_auroc_best
1021	    - zs_auroc_mean_19
1022	    - zs_drop_pp
1023	    - ece_mean_19
1024	    rows:
1025	    - - logistic_regression
1026	      - 0.843
1027	      - 0.762
1028	      - 8.1
1029	      - 0.054
1030	    - - mlp_2layer
1031	      - 0.856
1032	      - 0.733
1033	      - 12.4
1034	      - 0.068
1035	  figures_description:
1036	  - 'Figure S1 (supplementary): Transfer drop (pp) vs layer depth for both probe types.
1037	    MLP line diverges sharply from logreg at deep layers.'
1038	  analysis: 'Linear probes are the correct choice for cross-lingual transfer: they
1039	    sacrifice 1.3pp EN AUROC but gain 4.3pp average transfer. The depth interaction
1040	    effect is notable — the logreg advantage grows from 2.1pp at shallow layers to
1041	    6.8pp at deep layers, confirming that deep-layer transfer degradation is driven
1042	    by nonlinear, language- specific features. CaCLR + logreg is thus the optimal
1043	    configuration.
1044	
1045	    '
1046	- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)
1047	  plan_id: plan_007
1048	  description: 'Evaluate best probes + CaCLR on Belebele (20 languages) and MMLU-ProX
1049	    (20 languages).
1050	
1051	    '
1052	  expected_results:
1053	    belebele_zs_auroc_mean_19: 0.738
1054	    belebele_caclr_auroc_mean_19: 0.789
1055	    belebele_caclr_vs_zs_pp: 5.1
1056	    belebele_ece_reduction_vs_tempcal_pct: 36.2
1057	    mmlupx_zs_auroc_mean_19: 0.722
1058	    mmlupx_caclr_auroc_mean_19: 0.774
1059	    mmlupx_caclr_vs_zs_pp: 5.2
1060	    mmlupx_ece_reduction_vs_tempcal_pct: 33.8
1061	    caclr_benefit_cross_benchmark_cv: 0.08
1062	  result_rationale: 'Belebele tests reading comprehension (vs GlobalMMLU''s factual
1063	    knowledge), providing domain generalization evidence. Transfer AUROC is slightly
1064	    lower (0.738 vs 0.762) because Belebele''s passage-dependent questions have weaker
1065	    difficulty-shared signal — comprehension difficulty is more language-dependent
1066	    than factual difficulty. CaCLR still provides ~5pp improvement, confirming the
1067	    consistency loss generalizes beyond factual MCQA. MMLU-ProX has harder questions
1068	    that compress the AUROC distribution (lower base rate of correctness), yielding
1069	    slightly lower absolute numbers but comparable CaCLR benefit. The cross-benchmark
1070	    CV of 0.08 for CaCLR improvement confirms the method is robust to evaluation domain.
1071	
1072	    '
1073	  tables:
1074	  - name: 'Table 13: Cross-Benchmark Generalization'
1075	    columns:
1076	    - benchmark
1077	    - zs_auroc_mean_19
1078	    - caclr_auroc_mean_19
1079	    - caclr_gain_pp
1080	    - ece_reduction_pct
1081	    rows:
1082	    - - GlobalMMLU
1083	      - 0.752
1084	      - 0.804
1085	      - 5.2
1086	      - 39.7
1087	    - - Belebele
1088	      - 0.738
1089	      - 0.789
1090	      - 5.1
1091	      - 36.2
1092	    - - MMLU-ProX
1093	      - 0.722
1094	      - 0.774
1095	      - 5.2
1096	      - 33.8
1097	  figures_description:
1098	  - 'Figure S2: CaCLR improvement (pp) by benchmark × language, showing consistent
1099	    gains across domains.'
1100	  analysis: 'CaCLR generalizes cleanly across benchmarks. The improvement magnitude
1101	    is remarkably stable (5.1-5.2pp AUROC, 33-40% ECE reduction), suggesting the method
1102	    addresses a fundamental representation alignment issue rather than overfitting
1103	    to GlobalMMLU- specific patterns. This is critical for reviewer confidence.
1104	
1105	    '
1106	- name: INT8 Validation Ablation
1107	  plan_id: plan_010
1108	  description: 'Compare INT8 vs FP16 probing results at 5 representative layers for
1109	    Llama 4 Scout on 5% random subset.
1110	
1111	    '
1112	  expected_results:
1113	    int8_fp16_auroc_diff_mean_pp: 0.3
1114	    int8_fp16_auroc_diff_max_pp: 0.7
1115	    int8_fp16_ece_diff_mean_pp: 0.2
1116	    int8_fp16_transfer_drop_diff_pp: 0.4
1117	    int8_fp16_rank_correlation: 0.997
1118	    conclusion: INT8 quantization introduces negligible distortion
1119	  result_rationale: 'INT8 weight-only quantization preserves the 8 most significant
1120	    bits of each weight, introducing per-channel quantization noise of ~0.4% relative
1121	    magnitude. Correctness probing relies on the geometry of activation space (direction
1122	    of correctness signal), not absolute magnitudes. The quantization noise is approximately
1123	    isotropic and thus preserves angular relationships between directions. The 0.3pp
1124	    mean AUROC difference is within random seed variance, and the rank correlation
1125	    of 0.997 between INT8 and FP16 layer rankings confirms that the Pareto frontier
1126	    shape is unaffected. This result is expected given prior work showing that probing
1127	    results are robust to quantization down to INT4 (Gao et al., 2024).
1128	
1129	    '
1130	  tables:
1131	  - name: 'Table S1: INT8 vs FP16 Comparison (Llama 4 Scout, 5% subset)'
1132	    columns:
1133	    - layer_idx
1134	    - fp16_auroc
1135	    - int8_auroc
1136	    - diff_pp
1137	    - fp16_zs_auroc_5lang
1138	    - int8_zs_auroc_5lang
1139	    - transfer_diff_pp
1140	    rows:
1141	    - - 8
1142	      - 0.674
1143	      - 0.672
1144	      - 0.2
1145	      - 0.661
1146	      - 0.658
1147	      - 0.3
1148	    - - 16
1149	      - 0.747
1150	      - 0.745
1151	      - 0.2
1152	      - 0.731
1153	      - 0.728
1154	      - 0.3
1155	    - - 24
1156	      - 0.788
1157	      - 0.786
1158	      - 0.2
1159	      - 0.747
1160	      - 0.744
1161	      - 0.3
1162	    - - 32
1163	      - 0.812
1164	      - 0.81
1165	      - 0.2
1166	      - 0.734
1167	      - 0.731
1168	      - 0.3
1169	    - - 40
1170	      - 0.82
1171	      - 0.817
1172	      - 0.3
1173	      - 0.691
1174	      - 0.687
1175	      - 0.4
1176	  figures_description:
1177	  - 'Figure S3: INT8 vs FP16 AUROC scatter plot at all tested layer-language combinations.
1178	    Points fall tightly along y=x diagonal.'
1179	  analysis: 'INT8 quantization is validated as safe for our experimental setup. The
1180	    maximum observed difference (0.7pp at a single layer-language combination) is
1181	    well within the noise floor of probing experiments. The Pareto frontier ordering
1182	    is perfectly preserved (rank correlation 0.997). This ablation preempts reviewer
1183	    concern #5.
1184	
1185	    '
1186	- name: Gemma 4 31B Dense — Third Architecture (Camera-Ready)
1187	  plan_id: plan_008
1188	  description: 'Full Pareto frontier on Gemma 4 31B Dense (60 layers), 20+ languages.
1189	    Provides dense vs MoE architectural contrast.
1190	
1191	    '
1192	  expected_results:
1193	    en_auroc_best_layer: 0.812
1194	    en_best_layer_idx: 45
1195	    zs_transfer_auroc_mean_19lang: 0.734
1196	    zs_best_transfer_layer_idx: 36
1197	    zs_transfer_drop_mean_pp: 7.8
1198	    pareto_depth_transfer_rank_corr: 0.86
1199	    caclr_auroc_mean_19lang: 0.786
1200	    caclr_vs_linproj_auroc_delta_pp: 2.9
1201	    dense_vs_moe_transfer_comparison: comparable within 2pp
1202	    pareto_shape: convex monotonic, consistent with MoE models
1203	  result_rationale: 'Gemma 4 31B Dense has fewer total parameters than the MoE models
1204	    but all are active, yielding comparable per-token compute. As a dense model, its
1205	    representations are more uniformly distributed across layers (no expert routing),
1206	    producing slightly smoother Pareto frontiers. The best-transfer depth (~60%) matches
1207	    both MoE models, confirming this is a universal property of transformer depth,
1208	    not MoE-specific. EN AUROC is slightly lower (0.812 vs 0.843/0.821) because 31B
1209	    active params < 22B active with MoE routing benefits. CaCLR improvement is slightly
1210	    lower (2.9pp) on the dense model because the absence of expert routing means less
1211	    language-specific feature fragmentation to correct. This is the ideal third data
1212	    point: different architecture family, consistent findings.
1213	
1214	    '
1215	  tables:
1216	  - name: 'Table 14: Three-Architecture Summary'
1217	    columns:
1218	    - model
1219	    - type
1220	    - layers
1221	    - en_auroc_best
1222	    - zs_auroc_mean_19
1223	    - best_transfer_depth_pct
1224	    - pareto_rank_corr
1225	    - caclr_gain_pp
1226	    rows:
1227	    - - Qwen3-235B-A22B
1228	      - MoE
1229	      - 94
1230	      - 0.843
1231	      - 0.762
1232	      - 60
1233	      - 0.88
1234	      - 3.3
1235	    - - Llama 4 Scout
1236	      - MoE
1237	      - 48
1238	      - 0.821
1239	      - 0.741
1240	      - 58
1241	      - 0.82
1242	      - 3.1
1243	    - - Gemma 4 31B Dense
1244	      - Dense
1245	      - 60
1246	      - 0.812
1247	      - 0.734
1248	      - 60
1249	      - 0.86
1250	      - 2.9
1251	  figures_description:
1252	  - 'Figure 10: Three-architecture Pareto frontiers overlaid (normalized depth). Remarkably
1253	    similar shapes despite architectural differences.'
1254	  analysis: 'The three-architecture comparison is the strongest evidence for the universality
1255	    of the depth-transferability tradeoff. The best-transfer depth converges to 58-60%
1256	    across dense and MoE architectures with 48-94 layers, CaCLR provides consistent
1257	    2.9-3.3pp improvement, and the Pareto rank correlation is 0.82-0.88 in all cases.
1258	    Dense vs MoE makes minimal difference — the phenomenon is a property of transformer
1259	    depth, not routing architecture.
1260	
1261	    '
1262	- name: Extended Language Coverage (Camera-Ready)
1263	  plan_id: plan_009
1264	  description: 'Expand from 20 to 50+ languages for camera-ready, leveraging GlobalMMLU/Belebele
1265	    full language sets.
1266	
1267	    '
1268	  expected_results:
1269	    total_languages: 52
1270	    new_languages_added: 32
1271	    zs_auroc_above_0p60_count: 48
1272	    zs_auroc_below_0p55_count: 2
1273	    caclr_improvement_positive_count: 49
1274	    mean_zs_auroc_51lang: 0.72
1275	    mean_caclr_auroc_51lang: 0.77
1276	    pareto_frontier_holds_all_langs: true
1277	    new_language_families_covered:
1278	    - Austronesian
1279	    - Dravidian
1280	    - Niger-Congo B
1281	    - Uralic
1282	    - Kartvelian
1283	  result_rationale: 'Expanding to 50+ languages primarily adds mid-resource languages
1284	    (Indonesian, Malay, Finnish, Georgian, Tamil, Telugu, etc.) where the model has
1285	    moderate pretraining exposure. Most new languages fall in the 0.65-0.78 AUROC
1286	    range, consistent with the mid-resource tier from the 20-language set. A handful
1287	    of extremely low-resource languages (e.g., Amharic script languages with minimal
1288	    pretraining data) may fall below 0.55, but these represent edge cases rather than
1289	    systematic failures. CaCLR continues to improve 96% of languages because the consistency
1290	    loss mechanism is language-agnostic — it aligns activation distributions without
1291	    requiring any language-specific knowledge. The Pareto frontier structure is preserved
1292	    across all 52 languages, confirming it''s a depth property, not a language-set
1293	    artifact.
1294	
1295	    '
1296	  tables:
1297	  - name: 'Table 15: Extended Language Coverage Summary by Resource Tier'
1298	    columns:
1299	    - tier
1300	    - n_langs
1301	    - zs_auroc_mean
1302	    - caclr_auroc_mean
1303	    - caclr_gain_pp
1304	    - pct_above_0p60
1305	    rows:
1306	    - - high
1307	      - 12
1308	      - 0.782
1309	      - 0.812
1310	      - 3.0
1311	      - 100
1312	    - - mid
1313	      - 25
1314	      - 0.738
1315	      - 0.784
1316	      - 4.6
1317	      - 100
1318	    - - low
1319	      - 10
1320	      - 0.661
1321	      - 0.712
1322	      - 5.1
1323	      - 90
1324	    - - very_low
1325	      - 4
1326	      - 0.582
1327	      - 0.638
1328	      - 5.6
1329	      - 50
1330	  figures_description:
1331	  - 'Figure 11: World map with per-language CaCLR AUROC, colored by performance tier.
1332	    Demonstrates broad geographic and typological coverage.'
1333	  analysis: 'The extension to 52 languages confirms all findings at broader scale.
1334	    The resource-tier gradient is smooth and predictable — no language family shows
1335	    anomalous behavior. CaCLR''s benefit is inversely correlated with resource level
1336	    (3.0pp for high-resource to 5.6pp for very-low-resource), confirming that the
1337	    consistency loss provides most value where representation misalignment is worst.
1338	    The 48/51 pass rate (>0.60 AUROC) for zero-shot CaCLR transfer with no target-language
1339	    labels is the practical headline for camera-ready: usable cross-lingual calibration
1340	    for the vast majority of languages.'
1341	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0487ab20-0a77-43d4-86db-0b802fb05e05",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "080aba64-7619-4b34-8c1f-b1568b96cfd8",
  "sourceToolAssistantUUID": "0487ab20-0a77-43d4-86db-0b802fb05e05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T19:52:42.565Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Jnirz2yPQJuftAEKYMk2At`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "080aba64-7619-4b34-8c1f-b1568b96cfd8",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQSCtHPfawLRfLGHS9n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ceb5329d-0172-468d-a95f-645a979618a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vwot3Y4T1qCBZJGJ4sRvm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17505,
      "cache_read_input_tokens": 22854,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17505,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 26 · 2026-05-20T19:52:42.573Z_

<details><summary>↩ Tool result · `toolu_01Jnirz2yPQJuftAEKYMk2At`</summary>

```text
1	tier: median
2	narrative_guidance: 'Rebalance toward discovery + analysis. Claim 1 (Pareto frontier)
3	  becomes the headline contribution — first systematic characterization of depth-transferability
4	  tradeoff across architectures and 20 languages. Claim 2 reframes decomposition as
5	  ''partial but prescriptive'': difficulty component is clearly transferable, capability
6	  residual is noisy but the decomposition still predicts when simple baselines suffice
7	  vs when CaCLR helps. Claim 3 softens: CaCLR is presented as ''matching or exceeding
8	  the best simple baseline (linear projection) while requiring no target-language
9	  data at all'' — emphasize the zero-label setting rather than raw metric superiority.
10	  Add ablation showing where CaCLR''s consistency term specifically helps (mid-resource
11	  languages). Claim 4 presented with resource-tier analysis showing orthogonality
12	  is robust for well-represented languages but noisier for low-resource. Headline:
13	  ''Cross-lingual calibration probes reveal architecture-dependent Pareto frontier;
14	  CaCLR matches supervised transfer without target labels.''
15	
16	  '
17	imagined_experiments:
18	- name: Full Pareto Frontier — Qwen3-235B-A22B
19	  plan_id: plan_001
20	  description: '94-layer MoE model, INT8 quantization. 24 probed layers (every 4th:
21	    L0–L92). 20 languages (7 high / 8 mid / 5 low resource). English logistic-regression
22	    correctness probes trained per layer, evaluated on 5 transfer conditions (zero-shot,
23	    mean-shift, linear projection, few-shot 25/100, CaCLR placeholder). Core Pareto
24	    frontier data for Claim 1.
25	
26	    '
27	  expected_results:
28	    en_auroc_best: 0.812
29	    en_best_layer: L76
30	    en_auroc_range:
31	    - 0.531
32	    - 0.812
33	    en_ece_raw_at_best: 0.168
34	    en_ece_tempcal_at_best: 0.057
35	    temp_scaling_T: 5.83
36	    zs_transfer_auroc_mean_19lang_at_best_en: 0.644
37	    zs_transfer_drop_at_best_en_pp: 16.8
38	    best_transfer_layer: L40
39	    zs_transfer_auroc_mean_at_best_transfer: 0.696
40	    en_auroc_at_best_transfer: 0.776
41	    pareto_depth_transfer_rank_corr: 0.71
42	    low_resource_zs_pass_rate: 0.6
43	    mean_shift_improvement_rate: 0.05
44	    linproj_auroc_mean_at_best_transfer: 0.724
45	    fewshot25_auroc_mean_at_best_transfer: 0.711
46	    fewshot100_auroc_mean_at_best_transfer: 0.743
47	  result_rationale: 'Qwen3-235B-A22B 的 94 层深度提供了充分的层级分辨率来观测 Pareto tradeoff。 深层（L76）英语
48	    AUROC 达 0.812，因为更深层积累了更多 task-specific correctness 信号； 但这些深层 representation 也更
49	    language-specific（MoE routing 在深层更分化）， 导致 zero-shot 迁移退化至 0.644（drop 16.8pp）。最佳迁移层
50	    L40 处于模型 ~42% 深度，此处 representation 仍保留足够的 language-agnostic 结构。跨语言层序一致性 Spearman
51	    ρ=0.71 表明各语言对最优迁移深度的偏好高度一致，Pareto 结构是 robust 的。 Mean-shift 继承 MVP 的失败模式（correctness
52	    ≠ knowledge-boundary），仅 1/19 语言微弱改善。Linear projection 利用无标注目标语激活做线性对齐，在 L40 处比
53	    zero-shot 高 2.8pp，确立为 CaCLR 需要超越的 strong baseline。 低资源语言（sw/te/my 通过，am/yo 失败）符合预期：GlobalMMLU
54	    低资源子集样本量小且 翻译质量不稳定，但 3/5 通过证明 correctness direction 跨语言性在大模型上比 7B 更强。
55	
56	    '
57	  tables:
58	  - title: English AUROC by Layer (Logistic Regression)
59	    columns:
60	    - layer
61	    - depth_pct
62	    - en_auroc
63	    - en_ece_raw
64	    data:
65	    - layer: L0
66	      depth_pct: 0
67	      en_auroc: 0.531
68	      en_ece_raw: 0.341
69	    - layer: L4
70	      depth_pct: 4
71	      en_auroc: 0.557
72	      en_ece_raw: 0.328
73	    - layer: L8
74	      depth_pct: 9
75	      en_auroc: 0.589
76	      en_ece_raw: 0.312
77	    - layer: L12
78	      depth_pct: 13
79	      en_auroc: 0.621
80	      en_ece_raw: 0.293
81	    - layer: L16
82	      depth_pct: 17
83	      en_auroc: 0.653
84	      en_ece_raw: 0.274
85	    - layer: L20
86	      depth_pct: 21
87	      en_auroc: 0.684
88	      en_ece_raw: 0.255
89	    - layer: L24
90	      depth_pct: 26
91	      en_auroc: 0.711
92	      en_ece_raw: 0.237
93	    - layer: L28
94	      depth_pct: 30
95	      en_auroc: 0.735
96	      en_ece_raw: 0.221
97	    - layer: L32
98	      depth_pct: 34
99	      en_auroc: 0.752
100	      en_ece_raw: 0.21
101	    - layer: L36
102	      depth_pct: 38
103	      en_auroc: 0.766
104	      en_ece_raw: 0.199
105	    - layer: L40
106	      depth_pct: 43
107	      en_auroc: 0.776
108	      en_ece_raw: 0.192
109	    - layer: L44
110	      depth_pct: 47
111	      en_auroc: 0.784
112	      en_ece_raw: 0.186
113	    - layer: L48
114	      depth_pct: 51
115	      en_auroc: 0.79
116	      en_ece_raw: 0.182
117	    - layer: L52
118	      depth_pct: 55
119	      en_auroc: 0.796
120	      en_ece_raw: 0.178
121	    - layer: L56
122	      depth_pct: 60
123	      en_auroc: 0.8
124	      en_ece_raw: 0.175
125	    - layer: L60
126	      depth_pct: 64
127	      en_auroc: 0.804
128	      en_ece_raw: 0.173
129	    - layer: L64
130	      depth_pct: 68
131	      en_auroc: 0.807
132	      en_ece_raw: 0.171
133	    - layer: L68
134	      depth_pct: 72
135	      en_auroc: 0.81
136	      en_ece_raw: 0.17
137	    - layer: L72
138	      depth_pct: 77
139	      en_auroc: 0.811
140	      en_ece_raw: 0.169
141	    - layer: L76
142	      depth_pct: 81
143	      en_auroc: 0.812
144	      en_ece_raw: 0.168
145	    - layer: L80
146	      depth_pct: 85
147	      en_auroc: 0.809
148	      en_ece_raw: 0.17
149	    - layer: L84
150	      depth_pct: 89
151	      en_auroc: 0.804
152	      en_ece_raw: 0.174
153	    - layer: L88
154	      depth_pct: 94
155	      en_auroc: 0.796
156	      en_ece_raw: 0.179
157	    - layer: L92
158	      depth_pct: 98
159	      en_auroc: 0.782
160	      en_ece_raw: 0.188
161	  - title: Zero-Shot Transfer AUROC by Resource Tier (key layers)
162	    note: 19 non-English languages; tier means ± std
163	    columns:
164	    - layer
165	    - high_6_mean
166	    - high_6_std
167	    - mid_8_mean
168	    - mid_8_std
169	    - low_5_mean
170	    - low_5_std
171	    - all_19_mean
172	    data:
173	    - layer: L24
174	      high_6_mean: 0.731
175	      high_6_std: 0.011
176	      mid_8_mean: 0.692
177	      mid_8_std: 0.014
178	      low_5_mean: 0.59
179	      low_5_std: 0.031
180	      all_19_mean: 0.679
181	    - layer: L32
182	      high_6_mean: 0.747
183	      high_6_std: 0.01
184	      mid_8_mean: 0.706
185	      mid_8_std: 0.013
186	      low_5_mean: 0.601
187	      low_5_std: 0.029
188	      all_19_mean: 0.691
189	    - layer: L40
190	      high_6_mean: 0.753
191	      high_6_std: 0.01
192	      mid_8_mean: 0.711
193	      mid_8_std: 0.013
194	      low_5_mean: 0.607
195	      low_5_std: 0.032
196	      all_19_mean: 0.696
197	    - layer: L52
198	      high_6_mean: 0.741
199	      high_6_std: 0.011
200	      mid_8_mean: 0.697
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceb5329d-0172-468d-a95f-645a979618a5",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "bcbd1455-1b50-46ad-8bdd-f65c76902f6d",
  "sourceToolAssistantUUID": "ceb5329d-0172-468d-a95f-645a979618a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T19:52:43.210Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LEGhC2yCG2kKwXDFM799W7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcbd1455-1b50-46ad-8bdd-f65c76902f6d",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQSCtHPfawLRfLGHS9n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7cc17ac-0379-4908-90a9-149a430b8078",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vwot3Y4T1qCBZJGJ4sRvm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17505,
      "cache_read_input_tokens": 22854,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17505
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 22854,
          "cache_creation_input_tokens": 17505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17505,
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

_source line 28 · 2026-05-20T19:52:43.216Z_

<details><summary>↩ Tool result · `toolu_01LEGhC2yCG2kKwXDFM799W7`</summary>

```text
1	tier: worst
2	narrative_guidance: 'Full reframe to field-level diagnostic paper: ''Does probe-based
3	  calibration work beyond English? A systematic study across 2 architectures and 20
4	  languages.'' Value proposition shifts from method contribution to first large-scale
5	  answer on whether this research line generalizes. CaCLR is reported as a rigorous
6	  negative result — consistency-based objectives do not help when the cross-lingual
7	  correctness signal is this noisy. Decomposition is reported as evidence that difficulty
8	  and capability are entangled in multilingual representations, contradicting the
9	  clean separation assumed by English-only prior work. Pareto frontier is real on
10	  Qwen3 but fails to replicate cleanly on Llama 4 Scout — reported as architecture-dependence
11	  finding rather than universal law. Orthogonality (Claim 4) survives as the one mechanistic
12	  takeaway: output-based calibration is structurally limited everywhere, not just
13	  English. Target EACL with framing that negative/diagnostic results at this scale
14	  (2 models × 20 languages × all layers) are community-valuable when the field is
15	  actively expanding probe-based methods without multilingual validation.
16	
17	  '
18	imagined_experiments:
19	- name: Full Pareto Frontier — Qwen3-235B-A22B (94 layers, MoE, INT8)
20	  plan_id: plan_001
21	  description: 'Extract activations at 24 probed layers (every 4th of 94), 20 languages
22	    on GlobalMMLU. Train English logistic regression + 2-layer MLP correctness probes.
23	    Evaluate 5 transfer conditions: zero-shot, mean-shift, linear projection, few-shot
24	    (25/100), CaCLR.
25	
26	    '
27	  expected_results:
28	    en_auroc_best_layer: 0.776
29	    en_best_layer_idx: 72
30	    en_auroc_range:
31	    - 0.612
32	    - 0.776
33	    en_ece_raw_best: 0.172
34	    en_ece_tempcal_best: 0.068
35	    temp_scaling_T: 5.83
36	    zs_transfer_auroc_mean_19lang: 0.621
37	    zs_transfer_auroc_median_19lang: 0.633
38	    zs_transfer_auroc_std_19lang: 0.054
39	    zs_transfer_drop_mean_pp: 15.5
40	    zs_pass_rate_19lang: 0.368
41	    zs_pass_langs:
42	    - zh
43	    - fr
44	    - de
45	    - es
46	    - ja
47	    - ru
48	    - ko
49	    zs_fail_langs:
50	    - ar
51	    - hi
52	    - sw
53	    - yo
54	    - te
55	    - bn
56	    - ta
57	    - th
58	    - vi
59	    - uk
60	    - id
61	    - pl
62	    mean_shift_improves_count: 0
63	    mean_shift_mean_delta_ece_pp: 3.14
64	    linproj_auroc_mean_19lang: 0.648
65	    linproj_improves_over_zs_count: 13
66	    linproj_mean_delta_auroc_vs_zs_pp: 2.7
67	    fewshot25_auroc_mean_19lang: 0.654
68	    fewshot25_improves_over_zs_count: 14
69	    fewshot100_auroc_mean_19lang: 0.671
70	    fewshot100_improves_over_zs_count: 16
71	    pareto_depth_transfer_rank_corr: 0.41
72	    pareto_frontier_monotonic: false
73	    pareto_n_dominated_layers: 6
74	    transfer_by_family:
75	      indo_european_germanic:
76	        mean: 0.672
77	        langs:
78	        - de
79	        - en
80	      indo_european_romance:
81	        mean: 0.661
82	        langs:
83	        - fr
84	        - es
85	      indo_european_slavic:
86	        mean: 0.629
87	        langs:
88	        - ru
89	        - uk
90	        - pl
91	      indo_european_indic:
92	        mean: 0.598
93	        langs:
94	        - hi
95	        - bn
96	        - te
97	        - ta
98	      sino_tibetan:
99	        mean: 0.668
100	        langs:
101	        - zh
102	      japonic:
103	        mean: 0.651
104	        langs:
105	        - ja
106	      koreanic:
107	        mean: 0.648
108	        langs:
109	        - ko
110	      afroasiatic:
111	        mean: 0.612
112	        langs:
113	        - ar
114	      niger_congo:
115	        mean: 0.543
116	        langs:
117	        - sw
118	        - yo
119	      tai_kadai:
120	        mean: 0.591
121	        langs:
122	        - th
123	      austronesian:
124	        mean: 0.618
125	        langs:
126	        - id
127	      austroasiatic:
128	        mean: 0.607
129	        langs:
130	        - vi
131	  result_rationale: 'Qwen3-235B is a much larger MoE model than the MVP''s Qwen2.5-7B.
132	    English AUROC at 0.776 improves modestly over MVP''s 0.754 because the model is
133	    more capable and the correctness signal is more linearly accessible in larger
134	    models, but gains are sublinear — the larger model also has more complex, distributed
135	    representations that resist simple linear probing. Zero-shot transfer mean of
136	    0.621 reflects the worst-tier prediction that transfer is unreliable: high-resource
137	    Indo-European languages (fr, de, es) and CJK (zh, ja, ko) transfer adequately
138	    because their representations share more subspace structure with English at intermediate
139	    layers, but low-resource languages (sw, yo, te, bn) and languages with very different
140	    morphology (th, ta) fail because the MoE routing creates language-specific expert
141	    patterns that are opaque to an English-trained linear probe. Mean-shift fails
142	    entirely (0/19) because the mean activation difference between languages conflates
143	    content, style, and script differences — subtracting it removes useful signal.
144	    The Pareto frontier rank correlation of 0.41 is real but moderate: the general
145	    trend (deeper = better English, worse transfer) holds, but MoE routing introduces
146	    non-monotonic noise at mid-depth layers where expert activation patterns shift.
147	    The 7/19 pass rate reflects that only typologically close or high-resource languages
148	    have enough representational overlap with English for zero-shot transfer to work.
149	
150	    '
151	  tables:
152	  - name: 'Table 1: Qwen3-235B English Probe Performance by Layer (Selected Layers)'
153	    columns:
154	    - layer
155	    - depth_pct
156	    - logreg_auroc
157	    - mlp_auroc
158	    - ece_raw
159	    - ece_tempcal
160	    rows:
161	    - - 4
162	      - 4
163	      - 0.612
164	      - 0.618
165	      - 0.298
166	      - 0.192
167	    - - 16
168	      - 17
169	      - 0.653
170	      - 0.661
171	      - 0.251
172	      - 0.148
173	    - - 28
174	      - 30
175	      - 0.694
176	      - 0.708
177	      - 0.224
178	      - 0.121
179	    - - 40
180	      - 43
181	      - 0.721
182	      - 0.737
183	      - 0.203
184	      - 0.098
185	    - - 52
186	      - 55
187	      - 0.742
188	      - 0.755
189	      - 0.191
190	      - 0.082
191	    - - 60
192	      - 64
193	      - 0.758
194	      - 0.769
195	      - 0.183
196	      - 0.075
197	    - - 72
198	      - 77
199	      - 0.776
200	      - 0.783
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7cc17ac-0379-4908-90a9-149a430b8078",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "66d45ef9-6bd7-40ac-90be-4e4caefcdd3e",
  "sourceToolAssistantUUID": "f7cc17ac-0379-4908-90a9-149a430b8078",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T19:52:50.633Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QJYLfb3WZ87Cvr1wMShi7P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66d45ef9-6bd7-40ac-90be-4e4caefcdd3e",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQSftFGJ9zKapq9B3bJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00bd5e8a-ed3a-4c50-96d0-d551f6e22b55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131jDHiPw3eby5ZskNHR3cN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5690,
      "cache_read_input_tokens": 40359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5690,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 30 · 2026-05-20T19:52:50.645Z_

<details><summary>↩ Tool result · `toolu_01QJYLfb3WZ87Cvr1wMShi7P`</summary>

```text
200	      - 0.783
201	      - 0.172
202	      - 0.068
203	    - - 80
204	      - 85
205	      - 0.771
206	      - 0.779
207	      - 0.176
208	      - 0.071
209	    - - 88
210	      - 94
211	      - 0.753
212	      - 0.762
213	      - 0.185
214	      - 0.079
215	    - - 92
216	      - 98
217	      - 0.728
218	      - 0.739
219	      - 0.198
220	      - 0.091
221	  - name: 'Table 2: Qwen3-235B Zero-Shot Transfer AUROC by Language (Best Transfer
222	      Layer)'
223	    columns:
224	    - language
225	    - family
226	    - resource_tier
227	    - best_zs_layer
228	    - best_zs_auroc
229	    - en_auroc_at_same_layer
230	    - drop_pp
231	    rows:
232	    - - zh
233	      - sino_tibetan
234	      - high
235	      - 52
236	      - 0.668
237	      - 0.742
238	      - 7.4
239	    - - fr
240	      - romance
241	      - high
242	      - 52
243	      - 0.672
244	      - 0.742
245	      - 7.0
246	    - - de
247	      - germanic
248	      - high
249	      - 52
250	      - 0.671
251	      - 0.742
252	      - 7.1
253	    - - es
254	      - romance
255	      - high
256	      - 52
257	      - 0.661
258	      - 0.742
259	      - 8.1
260	    - - ja
261	      - japonic
262	      - high
263	      - 48
264	      - 0.651
265	      - 0.735
266	      - 8.4
267	    - - ru
268	      - slavic
269	      - high
270	      - 48
271	      - 0.644
272	      - 0.735
273	      - 9.1
274	    - - ko
275	      - koreanic
276	      - high
277	      - 48
278	      - 0.648
279	      - 0.735
280	      - 8.7
281	    - - ar
282	      - afroasiatic
283	      - mid
284	      - 40
285	      - 0.612
286	      - 0.721
287	      - 10.9
288	    - - hi
289	      - indic
290	      - mid
291	      - 40
292	      - 0.618
293	      - 0.721
294	      - 10.3
295	    - - vi
296	      - austroasiatic
297	      - mid
298	      - 40
299	      - 0.607
300	      - 0.721
301	      - 11.4
302	    - - id
303	      - austronesian
304	      - mid
305	      - 40
306	      - 0.618
307	      - 0.721
308	      - 10.3
309	    - - th
310	      - tai_kadai
311	      - mid
312	      - 40
313	      - 0.591
314	      - 0.721
315	      - 13.0
316	    - - pl
317	      - slavic
318	      - mid
319	      - 40
320	      - 0.621
321	      - 0.721
322	      - 10.0
323	    - - uk
324	      - slavic
325	      - mid
326	      - 40
327	      - 0.614
328	      - 0.721
329	      - 10.7
330	    - - bn
331	      - indic
332	      - low
333	      - 28
334	      - 0.583
335	      - 0.694
336	      - 11.1
337	    - - te
338	      - indic
339	      - low
340	      - 28
341	      - 0.571
342	      - 0.694
343	      - 12.3
344	    - - ta
345	      - indic
346	      - low
347	      - 28
348	      - 0.568
349	      - 0.694
350	      - 12.6
351	    - - sw
352	      - niger_congo
353	      - low
354	      - 28
355	      - 0.557
356	      - 0.694
357	      - 13.7
358	    - - yo
359	      - niger_congo
360	      - low
361	      - 28
362	      - 0.529
363	      - 0.694
364	      - 16.5
365	  - name: 'Table 3: Qwen3-235B Transfer Method Comparison (AUROC, 19-Language Mean)'
366	    columns:
367	    - method
368	    - auroc_mean
369	    - auroc_std
370	    - pass_rate
371	    - ece_mean
372	    - delta_vs_zs_pp
373	    rows:
374	    - - zero_shot
375	      - 0.621
376	      - 0.054
377	      - 0.368
378	      - 0.194
379	      - 0.0
380	    - - mean_shift
381	      - 0.604
382	      - 0.067
383	      - 0.263
384	      - 0.225
385	      - -1.7
386	    - - linear_projection
387	      - 0.648
388	      - 0.048
389	      - 0.526
390	      - 0.171
391	      - 2.7
392	    - - few_shot_25
393	      - 0.654
394	      - 0.045
395	      - 0.526
396	      - 0.166
397	      - 3.3
398	    - - few_shot_100
399	      - 0.671
400	      - 0.041
401	      - 0.632
402	      - 0.152
403	      - 5.0
404	  figures_description:
405	  - 'Figure 1a: Heatmap of zero-shot transfer AUROC (y-axis: 24 probed layers sorted
406	    by depth, x-axis: 20 languages sorted by resource tier). Shows a gradient where
407	    upper-left (deep layers × high-resource langs) has moderate AUROC (~0.65-0.67)
408	    and lower-right (shallow layers × low-resource langs) is near chance (~0.52-0.57).
409	    But the pattern is noisy — no crisp diagonal boundary. Several mid-depth layers
410	    show unexpected dips (layers 48-56) breaking monotonicity.'
411	  - 'Figure 1b: Pareto frontier scatter plot (x-axis: mean 19-lang zero-shot AUROC,
412	    y-axis: English AUROC at same layer). Each point is a layer. The Pareto front
413	    connects 6 non-dominated layers but the remaining 18 points scatter widely around
414	    it. Convex hull is thin — the tradeoff is real but the frontier offers limited
415	    choice. Error bars (bootstrap 95% CI) overlap substantially between adjacent Pareto-optimal
416	    points.'
417	  - 'Figure 1c: Line plot of zero-shot transfer drop (EN AUROC minus target-lang AUROC)
418	    vs layer depth, one line per language, colored by resource tier. High-resource
419	    languages (blue) show a gentle upward slope (deeper = worse transfer). Low-resource
420	    languages (red) show a steep upward slope. The spread between lines increases
421	    with depth, illustrating that the Pareto tradeoff is more severe for low-resource
422	    languages.'
423	  analysis: 'The Pareto frontier is real on Qwen3-235B but weak: rank correlation
424	    of 0.41 means the depth-transfer tradeoff explains only ~17% of variance. MoE
425	    routing creates non-monotonic perturbations at mid-depth. The practical implication
426	    is limited — the frontier provides modest guidance for layer selection but is
427	    not a reliable engineering tool. Zero-shot transfer fails for 12/19 languages
428	    (AUROC < 0.65), with a clear resource-tier gradient. The field should not assume
429	    English-trained correctness probes transfer to low-resource languages. Mean-shift
430	    is confirmed dead at scale. Linear projection and few-shot are the only viable
431	    transfer methods, with few-shot-100 achieving the best results — but requiring
432	    100 labeled examples per language partially negates the zero-label promise.
433	
434	    '
435	- name: Full Pareto Frontier — Llama 4 Scout (48 layers, MoE, INT8)
436	  plan_id: plan_002
437	  description: 'Extract activations at 12 probed layers (every 4th of 48), 20 languages
438	    on GlobalMMLU. Train English correctness probes, evaluate 5 transfer conditions.
439	
440	    '
441	  expected_results:
442	    en_auroc_best_layer: 0.749
443	    en_best_layer_idx: 36
444	    en_auroc_range:
445	    - 0.598
446	    - 0.749
447	    en_ece_raw_best: 0.188
448	    en_ece_tempcal_best: 0.074
449	    temp_scaling_T: 5.47
450	    zs_transfer_auroc_mean_19lang: 0.594
451	    zs_transfer_auroc_median_19lang: 0.601
452	    zs_transfer_auroc_std_19lang: 0.061
453	    zs_transfer_drop_mean_pp: 18.2
454	    zs_pass_rate_19lang: 0.211
455	    zs_pass_langs:
456	    - zh
457	    - fr
458	    - de
459	    - es
460	    zs_fail_langs:
461	    - ja
462	    - ru
463	    - ko
464	    - ar
465	    - hi
466	    - sw
467	    - yo
468	    - te
469	    - bn
470	    - ta
471	    - th
472	    - vi
473	    - uk
474	    - id
475	    - pl
476	    mean_shift_improves_count: 0
477	    mean_shift_mean_delta_ece_pp: 4.21
478	    linproj_auroc_mean_19lang: 0.623
479	    linproj_improves_over_zs_count: 11
480	    fewshot25_auroc_mean_19lang: 0.631
481	    fewshot100_auroc_mean_19lang: 0.652
482	    pareto_depth_transfer_rank_corr: 0.22
483	    pareto_frontier_monotonic: false
484	    pareto_n_dominated_layers: 3
485	    pareto_frontier_agreement_with_qwen3: 0.33
486	    nonmonotonic_layers:
487	    - 20
488	    - 24
489	    - 28
490	  result_rationale: 'Llama 4 Scout is the worst-tier''s key failure point. Its Pareto
491	    frontier is flat/non-monotonic (rank correlation 0.22) because Llama 4 Scout''s
492	    MoE architecture uses a different routing strategy than Qwen3-235B: its experts
493	    are more language-specialized at intermediate layers, meaning the English correctness
494	    direction at layers 20-28 is entangled with English-specific expert activations
495	    in ways that neither degrade nor improve monotonically with depth. English AUROC
496	    peaks at 0.749 (lower than Qwen3''s 0.776) because Llama 4 Scout''s 48 layers
497	    compress the representational hierarchy — the same functional stages are packed
498	    into fewer layers, leaving less room for a clean correctness signal to emerge.
499	    Zero-shot transfer is worse overall (mean 0.594 vs Qwen3''s 0.621) because Llama
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00bd5e8a-ed3a-4c50-96d0-d551f6e22b55",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "2a08ad14-d7aa-473d-bb27-d357b46561be",
  "sourceToolAssistantUUID": "00bd5e8a-ed3a-4c50-96d0-d551f6e22b55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T19:52:50.963Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L8aAvuiQTyeiZjmV1XdoAL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a08ad14-d7aa-473d-bb27-d357b46561be",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQSftFGJ9zKapq9B3bJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7b66ed8-2029-4e57-958f-36d0e0ce1c5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131jDHiPw3eby5ZskNHR3cN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5690,
      "cache_read_input_tokens": 40359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5690,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 32 · 2026-05-20T19:52:50.969Z_

<details><summary>↩ Tool result · `toolu_01L8aAvuiQTyeiZjmV1XdoAL`</summary>

```text
1	experiments:
2	  # === P0: Core submission (must complete for EACL 2027 ARR Aug 3) ===
3	
4	  - id: plan_001
5	    claim: 1
6	    description: >
7	      Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8):
8	      extract activations at every 4th layer (24 probed layers),
9	      20 typologically diverse languages, train English correctness probes
10	      (logistic regression + 2-layer MLP), evaluate 5 transfer conditions
11	      (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).
12	    priority: P0
13	    gpu_budget_hours: 80
14	    deps: []
15	    notes: "Needs 3-4× RTX 6000 PRO 96GB at INT8. May need GPU upgrade request."
16	
17	  - id: plan_002
18	    claim: 1
19	    description: >
20	      Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8):
21	      extract activations at every 4th layer (12 probed layers),
22	      20 languages, 5 transfer conditions. INT8 weight quantization.
23	    priority: P0
24	    gpu_budget_hours: 40
25	    deps: []
26	    notes: "Needs 2× RTX 6000 PRO 96GB at INT8."
27	
28	  - id: plan_003
29	    claim: 3
30	    description: >
31	      CaCLR implementation and comparative evaluation:
32	      L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency.
33	      Train CaCLR probes using English labels + unlabeled parallel activations.
34	      Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100)
35	      across full Pareto frontier for both models × 20 languages.
36	      Hyperparameter tuning (α, β) on held-out English + 5-language validation.
37	    priority: P0
38	    gpu_budget_hours: 20
39	    deps: [plan_001, plan_002]
40	    notes: "CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS 2021."
41	
42	  - id: plan_004
43	    claim: 2
44	    description: >
45	      Difficulty-controlled ablation: train IRT difficulty probes (Ridge regression
46	      on human difficulty scores per Civelli et al.), project out difficulty direction
47	      from activations, retrain correctness probes on residuals, evaluate transfer.
48	      10 representative languages × 8 representative layers per model (20-90% depth).
49	    priority: P0
50	    gpu_budget_hours: 15
51	    deps: [plan_001, plan_002]
52	    notes: "Need IRT difficulty scores from GlobalMMLU or external source."
53	
54	  # === P1: Important for strong submission ===
55	
56	  - id: plan_005
57	    claim: 4
58	    description: >
59	      Cross-lingual orthogonality analysis: extract verbalized confidence direction
60	      (prompt model for confidence score, fit probe), compute cosine similarity
61	      with correctness direction across 20 languages × 2 architectures.
62	      Analyze by resource tier (high/mid/low) and language family.
63	    priority: P1
64	    gpu_budget_hours: 10
65	    deps: [plan_001, plan_002]
66	
67	  - id: plan_006
68	    claim: 1
69	    description: >
70	      Probe complexity comparison: logistic regression vs 2-layer MLP
71	      at each probed layer for both models. Compare English accuracy,
72	      cross-lingual transfer degradation, and calibration quality.
73	      Test hypothesis: linear probes transfer better cross-lingually.
74	    priority: P1
75	    gpu_budget_hours: 5
76	    deps: [plan_001, plan_002]
77	    notes: "CPU-bound, uses cached activations."
78	
79	  - id: plan_007
80	    claim: 1
81	    description: >
82	      Additional benchmark evaluation: evaluate best probes + CaCLR
83	      on Belebele (20 languages) and MMLU-ProX (20 languages).
84	      Validates generalization beyond MMLU/GlobalMMLU.
85	    priority: P1
86	    gpu_budget_hours: 30
87	    deps: [plan_001, plan_002, plan_003]
88	
89	  - id: plan_010
90	    claim: 1
91	    description: >
92	      INT8 validation ablation: compare INT8 vs FP16 probing results
93	      at 5 representative layers for Llama 4 Scout on 5% random subset.
94	      Validates that INT8 quantization doesn't distort correctness signals.
95	    priority: P1
96	    gpu_budget_hours: 5
97	    deps: [plan_002]
98	
99	  # === P2: Camera-ready extension ===
100	
101	  - id: plan_008
102	    claim: 1
103	    description: >
104	      Gemma 4 31B Dense (60 layers, dense, FP16): third architecture
105	      for camera-ready. Full Pareto frontier, 20+ languages.
106	      Provides dense vs MoE architectural contrast.
107	    priority: P2
108	    gpu_budget_hours: 30
109	    deps: []
110	
111	  - id: plan_009
112	    claim: 1
113	    description: >
114	      Extended language coverage: expand from 20 to 50+ languages
115	      for camera-ready. Leverages GlobalMMLU/Belebele full language sets.
116	    priority: P2
117	    gpu_budget_hours: 50
118	    deps: [plan_001, plan_002]
119	
120	  # === MVP experiments (completed/running) ===
121	
122	  - id: mvp_validation
123	    claim: 1
124	    description: "MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift"
125	    priority: P0
126	    registry_id: mvp_001
127	    gpu_budget_hours: 2
128	    deps: []
129	
130	  - id: mvp_complementary
131	    claim: 1
132	    description: "MVP robustness: complementary layer set (2,6,10,14,18,22,26)"
133	    priority: P1
134	    registry_id: mvp_002
135	    gpu_budget_hours: 2
136	    deps: [mvp_validation]
137	
138	  - id: mvp_llama_control
139	    claim: 1
140	    description: "MVP cross-architecture: Llama-3.1-8B control experiment"
141	    priority: P1
142	    registry_id: mvp_003
143	    gpu_budget_hours: 3
144	    deps: [mvp_validation]
145	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7b66ed8-2029-4e57-958f-36d0e0ce1c5a",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "60e53dc7-0ace-4abd-a42c-43cba92a8af3",
  "sourceToolAssistantUUID": "d7b66ed8-2029-4e57-958f-36d0e0ce1c5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T19:53:04.075Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BZZwzewEHFNNKu2UGiu8tb`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60e53dc7-0ace-4abd-a42c-43cba92a8af3",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQTFHBTidwnZpr3aYoc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1d819ef-2da3-461d-88fb-ac45e812a86c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WypyZcRkDv5CCq9oEVce5C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5500,
      "cache_read_input_tokens": 46049,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5500
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 111,
          "cache_read_input_tokens": 46049,
          "cache_creation_input_tokens": 5500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5500,
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

_source line 34 · 2026-05-20T19:53:04.084Z_

<details><summary>↩ Tool result · `toolu_01BZZwzewEHFNNKu2UGiu8tb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md\", \"content\": \"# Paper Framing — xling_calib_direction\\n\\n## Target Venue\\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\\n- Core submission: 2 models × 20 languages × all contributions\\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\\n\\n## Core Insight\\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\\n\\n## Core Claims (4, causal chain)\\n\\n### Claim 1 — Pareto Frontier (Discovery)\\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\\n\\n### Claim 2 — Decomposition (Analysis)\\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\\n\\n### Claim 3 — CaCLR (Method)\\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) shifts the Pareto frontier by jointly optimizing calibration and cross-lingual invariance, enabling effective probe transfer at deeper, better-calibrated layers without target-language correctness labels.\\n- MVP evidence: Mean-shift fails entirely (0/5 languages improved) — motivates principled approach.\\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier.\\n\\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\\n\\n## Story Spine\\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, and propose CaCLR to shift the frontier. This is both a field-level viability test and a practical method contribution.\\n- **Headline template**: \\\"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\\\"\\n\\n## Field-Level Significance\\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\\n\\n## Anticipated Reviewer Concerns & Responses\\n1. **\\\"Xiao et al. already did this\\\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier.\\n2. **\\\"Temperature scaling baseline\\\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\\n3. **\\\"Mean-shift too weak\\\"** → 5 transfer conditions tested. Mean-shift failure (MVP-confirmed) motivates CaCLR. Mean-shift works for Xiao et al.'s knowledge boundary but fails for correctness — important finding.\\n4. **\\\"Difficulty confound\\\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\\n5. **\\\"INT8 artifacts\\\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\\n6. **\\\"Only MCQA\\\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\\n\\n## Differentiation from Closest Prior Work\\n| Paper | Their Focus | Our Difference |\\n|-------|-------------|----------------|\\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier |\\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\\n\", \"total_chars\": 6025, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1d819ef-2da3-461d-88fb-ac45e812a86c",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "a0db7f73-c1e2-4c28-b215-5b887751d426",
  "sourceToolAssistantUUID": "f1d819ef-2da3-461d-88fb-ac45e812a86c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-20T19:53:08.779Z_

Now I have a comprehensive understanding of the paper's design, claims, experiments, and the range of possible outcomes (best/median/worst). Let me also check the actual results reported in the paper summary versus what was imagined.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0db7f73-c1e2-4c28-b215-5b887751d426",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQUDHQRFp8xiB21dUQY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a1486f1-028c-4476-8717-f4b632be8b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRnbSDjyaA67AQ4VKajUW2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1858,
      "cache_read_input_tokens": 51549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1858,
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

_source line 36 · 2026-05-20T19:53:09.770Z_

<details open><summary>🔧 Tool call — Read · `toolu_019x7XhCkf31yanb73P2RyCu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a1486f1-028c-4476-8717-f4b632be8b5e",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQUDHQRFp8xiB21dUQY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aaf7c16a-978a-493a-9edc-a644267be547",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRnbSDjyaA67AQ4VKajUW2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1858,
      "cache_read_input_tokens": 51549,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 51549,
          "cache_creation_input_tokens": 1858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1858,
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

_source line 37 · 2026-05-20T19:53:10.261Z_

<details><summary>↩ Tool result · `toolu_019x7XhCkf31yanb73P2RyCu`</summary>

```text
1	narrative_guidance: 'Original framing stands: "CaCLR shifts the cross-lingual calibration
2	  Pareto frontier." All 4 claims form an unbroken causal chain — discovery → analysis
3	  → method → mechanism. Headline: CaCLR reduces non-EN ECE by 30-50% over temp scaling
4	  with zero target-language labels. Pareto frontier is the organizing principle, CaCLR
5	  is the actionable contribution, decomposition explains why it works, orthogonality
6	  explains why output-based methods can''t.
7	
8	  '
9	imagined_experiments:
10	- name: Full Pareto Frontier — Qwen3-235B-A22B
11	  plan_id: plan_001
12	  description: 'Extract activations at every 4th layer (24 probed layers out of 94),
13	    20 languages, train English correctness probes (logistic regression + 2-layer
14	    MLP), evaluate 5 transfer conditions (zero-shot, mean-shift, linear projection,
15	    few-shot 25/100, CaCLR).
16	
17	    '
18	  expected_results:
19	    en_auroc_best_layer: 0.843
20	    en_best_layer_idx: 72
21	    en_auroc_range:
22	    - 0.621
23	    - 0.843
24	    en_ece_raw_best: 0.162
25	    en_ece_tempcal_best: 0.054
26	    temp_scaling_T: 4.87
27	    zs_transfer_auroc_mean_19lang_best_transfer_layer: 0.762
28	    zs_best_transfer_layer_idx: 56
29	    zs_transfer_drop_from_en_mean_pp: 8.1
30	    zs_auroc_by_tier:
31	      high_resource_mean: 0.791
32	      mid_resource_mean: 0.754
33	      low_resource_mean: 0.683
34	    zs_auroc_by_lang:
35	      en: 0.843
36	      zh: 0.802
37	      de: 0.796
38	      fr: 0.793
39	      es: 0.789
40	      ja: 0.785
41	      ru: 0.782
42	      pt: 0.788
43	      it: 0.786
44	      ar: 0.768
45	      hi: 0.761
46	      ko: 0.755
47	      vi: 0.749
48	      th: 0.743
49	      bn: 0.738
50	      tr: 0.756
51	      nl: 0.79
52	      sw: 0.695
53	      yo: 0.672
54	      ig: 0.681
55	    mean_shift_improvement_count: 2
56	    mean_shift_delta_ece_mean: 1.41
57	    linproj_auroc_mean_19lang: 0.724
58	    fewshot_25_auroc_mean_19lang: 0.748
59	    fewshot_100_auroc_mean_19lang: 0.771
60	    pareto_depth_transfer_rank_corr: 0.88
61	    pareto_frontier_layers:
62	    - 40
63	    - 44
64	    - 48
65	    - 52
66	    - 56
67	    - 60
68	    layers_above_0p5_auroc_count: 22
69	  result_rationale: 'Qwen3-235B-A22B is a 94-layer MoE with massive representation
70	    capacity. The jump from MVP''s 7B (en AUROC 0.754) to 235B is expected to yield
71	    ~9pp AUROC gain, consistent with prior probing literature showing log-linear scaling
72	    of linear probe accuracy with model parameters (Burns et al., Marks et al.). The
73	    MoE architecture concentrates expert representations, producing cleaner correctness
74	    signals in intermediate layers. The Pareto frontier emerges because deeper layers
75	    (L72+) specialize for English-dominant pretraining data distribution — the model''s
76	    language-specific processing intensifies past ~75% depth, degrading cross-lingual
77	    invariance. The best transfer layer (L56, ~60% depth) sits in the "universal reasoning"
78	    zone before language-specific heads activate. Low-resource languages (sw, yo,
79	    ig) still transfer above 0.65 AUROC because GlobalMMLU questions share structural
80	    patterns that even underrepresented languages partially align with in middle layers.
81	    Mean-shift continues to mostly fail because correctness directions are not simply
82	    mean-offset between languages — they require rotation, not translation, which
83	    linear projection and CaCLR address.
84	
85	    '
86	  tables:
87	  - name: 'Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by
88	      Layer'
89	    columns:
90	    - layer_idx
91	    - layer_depth_pct
92	    - en_auroc
93	    - zs_mean_auroc_19
94	    - zs_drop_pp
95	    - on_pareto
96	    rows:
97	    - - 4
98	      - 4
99	      - 0.621
100	      - 0.608
101	      - 1.3
102	      - false
103	    - - 8
104	      - 9
105	      - 0.648
106	      - 0.637
107	      - 1.1
108	      - false
109	    - - 12
110	      - 13
111	      - 0.689
112	      - 0.671
113	      - 1.8
114	      - false
115	    - - 16
116	      - 17
117	      - 0.712
118	      - 0.698
119	      - 1.4
120	      - false
121	    - - 20
122	      - 21
123	      - 0.738
124	      - 0.724
125	      - 1.4
126	      - false
127	    - - 24
128	      - 26
129	      - 0.756
130	      - 0.742
131	      - 1.4
132	      - false
133	    - - 28
134	      - 30
135	      - 0.771
136	      - 0.755
137	      - 1.6
138	      - false
139	    - - 32
140	      - 34
141	      - 0.784
142	      - 0.764
143	      - 2.0
144	      - false
145	    - - 36
146	      - 38
147	      - 0.795
148	      - 0.771
149	      - 2.4
150	      - false
151	    - - 40
152	      - 43
153	      - 0.803
154	      - 0.776
155	      - 2.7
156	      - true
157	    - - 44
158	      - 47
159	      - 0.81
160	      - 0.774
161	      - 3.6
162	      - true
163	    - - 48
164	      - 51
165	      - 0.816
166	      - 0.77
167	      - 4.6
168	      - true
169	    - - 52
170	      - 55
171	      - 0.822
172	      - 0.765
173	      - 5.7
174	      - true
175	    - - 56
176	      - 60
177	      - 0.827
178	      - 0.762
179	      - 6.5
180	      - true
181	    - - 60
182	      - 64
183	      - 0.831
184	      - 0.753
185	      - 7.8
186	      - true
187	    - - 64
188	      - 68
189	      - 0.835
190	      - 0.741
191	      - 9.4
192	      - false
193	    - - 68
194	      - 72
195	      - 0.839
196	      - 0.728
197	      - 11.1
198	      - false
199	    - - 72
200	      - 77
201	      - 0.843
202	      - 0.712
203	      - 13.1
204	      - false
205	    - - 76
206	      - 81
207	      - 0.841
208	      - 0.694
209	      - 14.7
210	      - false
211	    - - 80
212	      - 85
213	      - 0.838
214	      - 0.671
215	      - 16.7
216	      - false
217	    - - 84
218	      - 89
219	      - 0.832
220	      - 0.643
221	      - 18.9
222	      - false
223	    - - 88
224	      - 94
225	      - 0.819
226	      - 0.611
227	      - 20.8
228	      - false
229	    - - 92
230	      - 98
231	      - 0.791
232	      - 0.574
233	      - 21.7
234	      - false
235	    - - 94
236	      - 100
237	      - 0.762
238	      - 0.541
239	      - 22.1
240	      - false
241	  - name: 'Table 2: Transfer Condition Comparison (at best-transfer layer L56)'
242	    columns:
243	    - condition
244	    - auroc_mean_19
245	    - ece_mean_19
246	    - ece_reduction_vs_tempcal_pct
247	    rows:
248	    - - zero-shot
249	      - 0.762
250	      - 0.098
251	      - 0
252	    - - mean-shift
253	      - 0.758
254	      - 0.101
255	      - -3.1
256	    - - linear_projection
257	      - 0.781
258	      - 0.082
259	      - 16.3
260	    - - few-shot-25
261	      - 0.748
262	      - 0.089
263	      - 9.2
264	    - - few-shot-100
265	      - 0.771
266	      - 0.079
267	      - 19.4
268	    - - CaCLR
269	      - 0.814
270	      - 0.058
271	      - 40.8
272	  figures_description:
273	  - 'Figure 1a: Pareto frontier scatter plot (EN AUROC x-axis vs ZS mean AUROC y-axis),
274	    each point a layer, Pareto-optimal layers highlighted in red. Clear convex frontier
275	    shape from L40-L60.'
276	  - 'Figure 1b: Heatmap of ZS AUROC by language (y-axis, ordered by resource tier)
277	    × layer depth (x-axis). Shows warm band in mid-layers, cooling at extremes, with
278	    low-resource langs cooling earlier.'
279	  analysis: 'The Pareto frontier is crisp and monotonic: 6 layers form the efficient
280	    frontier between L40-L60. The rank correlation (Spearman) between layer depth
281	    and transfer degradation is ρ=0.88 (p<0.001). The frontier''s shape confirms that
282	    the depth- transferability tradeoff is not an artifact of small models — it amplifies
283	    at scale. The 16pp gap between best-EN layer (L72) and best-transfer layer (L56)
284	    is larger than MVP''s ~3-layer gap, consistent with deeper models having more
285	    room for language-specific specialization. All high-resource languages pass AUROC
286	    > 0.75 at the best-transfer layer; all low-resource languages exceed 0.65.
287	
288	    '
289	- name: Full Pareto Frontier — Llama 4 Scout
290	  plan_id: plan_002
291	  description: 'Extract activations at every 4th layer (12 probed layers out of 48),
292	    20 languages, 5 transfer conditions. INT8 weight quantization.
293	
294	    '
295	  expected_results:
296	    en_auroc_best_layer: 0.821
297	    en_best_layer_idx: 36
298	    en_auroc_range:
299	    - 0.634
300	    - 0.821
301	    en_ece_raw_best: 0.174
302	    en_ece_tempcal_best: 0.061
303	    temp_scaling_T: 5.34
304	    zs_transfer_auroc_mean_19lang_best_transfer_layer: 0.741
305	    zs_best_transfer_layer_idx: 28
306	    zs_transfer_drop_from_en_mean_pp: 8.0
307	    zs_auroc_by_tier:
308	      high_resource_mean: 0.771
309	      mid_resource_mean: 0.733
310	      low_resource_mean: 0.661
311	    zs_auroc_by_lang:
312	      en: 0.821
313	      zh: 0.784
314	      de: 0.778
315	      fr: 0.775
316	      es: 0.771
317	      ja: 0.766
318	      ru: 0.762
319	      pt: 0.77
320	      it: 0.768
321	      ar: 0.748
322	      hi: 0.741
323	      ko: 0.735
324	      vi: 0.729
325	      th: 0.722
326	      bn: 0.718
327	      tr: 0.737
328	      nl: 0.772
329	      sw: 0.674
330	      yo: 0.641
331	      ig: 0.667
332	    mean_shift_improvement_count: 1
333	    linproj_auroc_mean_19lang: 0.706
334	    fewshot_25_auroc_mean_19lang: 0.728
335	    fewshot_100_auroc_mean_19lang: 0.752
336	    pareto_depth_transfer_rank_corr: 0.82
337	    pareto_frontier_layers:
338	    - 20
339	    - 24
340	    - 28
341	    - 32
342	  result_rationale: 'Llama 4 Scout has 48 layers (fewer than Qwen3''s 94) and a different
343	    MoE routing strategy (16 experts, top-2). With roughly 109B total / ~17B active
344	    params, its active compute is smaller than Qwen3-235B''s ~22B active. This yields
345	    ~2pp lower EN AUROC and ~2pp lower transfer AUROC. The Pareto frontier has fewer
346	    points (4 vs 6) due to coarser layer sampling (every 4th of 48 = 12 points), but
347	    the monotonic depth-transfer tradeoff still holds clearly. Llama 4 Scout''s best
348	    transfer layer sits at ~58% depth (L28), remarkably close to Qwen3''s 60%, suggesting
349	    a universal "mid-depth transfer zone" across architectures. The rank correlation
350	    is slightly lower (0.82 vs 0.88) due to fewer data points but still highly significant.
351	    Low-resource languages are slightly weaker because Meta''s multilingual pretraining
352	    mix underrepresents African languages compared to Qwen3.
353	
354	    '
355	  tables:
356	  - name: 'Table 3: Llama 4 Scout Pareto Frontier'
357	    columns:
358	    - layer_idx
359	    - layer_depth_pct
360	    - en_auroc
361	    - zs_mean_auroc_19
362	    - zs_drop_pp
363	    - on_pareto
364	    rows:
365	    - - 4
366	      - 8
367	      - 0.634
368	      - 0.624
369	      - 1.0
370	      - false
371	    - - 8
372	      - 17
373	      - 0.672
374	      - 0.659
375	      - 1.3
376	      - false
377	    - - 12
378	      - 25
379	      - 0.714
380	      - 0.699
381	      - 1.5
382	      - false
383	    - - 16
384	      - 33
385	      - 0.745
386	      - 0.729
387	      - 1.6
388	      - false
389	    - - 20
390	      - 42
391	      - 0.768
392	      - 0.748
393	      - 2.0
394	      - true
395	    - - 24
396	      - 50
397	      - 0.786
398	      - 0.745
399	      - 4.1
400	      - true
401	    - - 28
402	      - 58
403	      - 0.798
404	      - 0.741
405	      - 5.7
406	      - true
407	    - - 32
408	      - 67
409	      - 0.81
410	      - 0.732
411	      - 7.8
412	      - true
413	    - - 36
414	      - 75
415	      - 0.821
416	      - 0.714
417	      - 10.7
418	      - false
419	    - - 40
420	      - 83
421	      - 0.818
422	      - 0.689
423	      - 12.9
424	      - false
425	    - - 44
426	      - 92
427	      - 0.804
428	      - 0.651
429	      - 15.3
430	      - false
431	    - - 48
432	      - 100
433	      - 0.771
434	      - 0.608
435	      - 16.3
436	      - false
437	  - name: 'Table 4: Cross-Architecture Pareto Frontier Agreement'
438	    columns:
439	    - metric
440	    - qwen3_235b
441	    - llama4_scout
442	    - agreement
443	    rows:
444	    - - best_en_layer_depth_pct
445	      - 77
446	      - 75
447	      - within 2pp
448	    - - best_transfer_layer_depth_pct
449	      - 60
450	      - 58
451	      - within 2pp
452	    - - pareto_zone_depth_range_pct
453	      - 43-64
454	      - 42-67
455	      - overlapping
456	    - - depth_transfer_rank_corr
457	      - 0.88
458	      - 0.82
459	      - both >0.75
460	    - - frontier_shape
461	      - convex monotonic
462	      - convex monotonic
463	      - consistent
464	  figures_description:
465	  - 'Figure 2: Overlaid Pareto frontiers for both architectures (normalized depth
466	    %). Shows near-identical frontier shapes with Qwen3 shifted up-right (better overall)
467	    but same curvature.'
468	  analysis: 'Cross-architecture agreement is high: both models show best transfer
469	    at ~59% depth, the Pareto frontier occupies the 42-67% depth band, and the rank
470	    correlation between depth and transfer degradation exceeds 0.75 in both. The frontier
471	    shape is architecture-invariant — it''s the depth-normalized position, not absolute
472	    layer count, that determines the tradeoff. This validates Claim 1 at scale.
473	
474	    '
475	- name: CaCLR Implementation and Comparative Evaluation
476	  plan_id: plan_003
477	  description: 'CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) implementation. Train
478	    on English labels + unlabeled parallel activations. Compare vs all 5 conditions
479	    across full Pareto frontier, both models × 20 languages. Hyperparameter tuning
480	    (α, β).
481	
482	    '
483	  expected_results:
484	    best_alpha: 0.15
485	    best_beta: 0.08
486	    qwen3_caclr_auroc_mean_19lang: 0.814
487	    qwen3_caclr_ece_mean_19lang: 0.058
488	    qwen3_caclr_vs_linproj_auroc_delta_pp: 3.3
489	    qwen3_caclr_vs_zeroshot_auroc_delta_pp: 5.2
490	    qwen3_caclr_ece_reduction_vs_tempcal_pct: 40.8
491	    qwen3_caclr_best_operating_layer: 64
492	    llama4_caclr_auroc_mean_19lang: 0.793
493	    llama4_caclr_ece_mean_19lang: 0.064
494	    llama4_caclr_vs_linproj_auroc_delta_pp: 3.1
495	    llama4_caclr_vs_zeroshot_auroc_delta_pp: 5.2
496	    llama4_caclr_ece_reduction_vs_tempcal_pct: 38.5
497	    llama4_caclr_best_operating_layer: 32
498	    caclr_vs_linproj_auroc_delta_pp_mean: 3.2
499	    caclr_ece_reduction_vs_tempcal_pct_mean: 39.7
500	    caclr_improvement_pass_rate: 0.92
501	    caclr_pareto_shift_layers: 2
502	    low_resource_caclr_auroc:
503	      sw_qwen3: 0.731
504	      yo_qwen3: 0.709
505	      ig_qwen3: 0.718
506	      sw_llama4: 0.712
507	      yo_llama4: 0.681
508	      ig_llama4: 0.698
509	    low_resource_zs_pass_rate: 1.0
510	  result_rationale: 'CaCLR''s consistency loss (β·L_consistency) directly penalizes
511	    divergence between EN and non-EN probe outputs on parallel/comparable activations,
512	    forcing the probe to learn language-invariant features. This is strictly more
513	    informative than linear projection (which only aligns means and covariances post-hoc)
514	    because it shapes the learned representation during training. The 3.2pp AUROC
515	    gain over linear projection reflects the value of end-to-end optimization: linear
516	    projection corrects first-order distributional mismatch but not the nonlinear
517	    feature interactions that L_consistency captures. The SB-ECE term (α·L_SB-ECE)
518	    provides calibration-aware training that temperature scaling cannot — it directly
519	    optimizes the calibration objective rather than post-hoc rescaling. The 40% ECE
520	    reduction over temperature scaling arises because CaCLR addresses the root cause
521	    (representation misalignment) rather than the symptom (miscalibrated probabilities).
522	    The Pareto frontier shift is the key result: CaCLR allows operating 2 layers deeper
523	    than the ZS-optimal point while maintaining equivalent or better transfer — it
524	    literally pushes the Pareto frontier outward. Low-resource languages benefit most
525	    from L_consistency because their activation distributions are most misaligned
526	    from EN; the consistency term provides the strongest gradient signal precisely
527	    where the gap is largest.
528	
529	    '
530	  tables:
531	  - name: 'Table 5: CaCLR vs Baselines — Full Comparison (averaged across both architectures)'
532	    columns:
533	    - method
534	    - auroc_mean_19
535	    - ece_mean_19
536	    - requires_target_labels
537	    - params_overhead
538	    rows:
539	    - - zero-shot
540	      - 0.752
541	      - 0.098
542	      - 'no'
543	      - '0'
544	    - - mean-shift
545	      - 0.747
546	      - 0.102
547	      - 'no'
548	      - '0'
549	    - - linear_projection
550	      - 0.77
551	      - 0.082
552	      - 'no'
553	      - d×d matrix
554	    - - few-shot-25
555	      - 0.738
556	      - 0.089
557	      - yes (25)
558	      - '0'
559	    - - few-shot-100
560	      - 0.762
561	      - 0.079
562	      - yes (100)
563	      - '0'
564	    - - CaCLR
565	      - 0.804
566	      - 0.061
567	      - 'no'
568	      - ~1% probe params
569	  - name: 'Table 6: CaCLR Ablation — Loss Component Contributions'
570	    columns:
571	    - configuration
572	    - auroc_mean_19
573	    - ece_mean_19
574	    - delta_vs_full_auroc_pp
575	    rows:
576	    - - L_BCE_only (= zero-shot probe)
577	      - 0.752
578	      - 0.098
579	      - -5.2
580	    - - L_BCE + L_SB-ECE
581	      - 0.768
582	      - 0.072
583	      - -3.6
584	    - - L_BCE + L_consistency
585	      - 0.793
586	      - 0.078
587	      - -1.1
588	    - - L_BCE + L_SB-ECE + L_consistency (full CaCLR)
589	      - 0.804
590	      - 0.061
591	      - 0.0
592	  - name: 'Table 7: CaCLR Pareto Frontier Shift (Qwen3-235B)'
593	    columns:
594	    - layer_idx
595	    - zs_auroc_19
596	    - caclr_auroc_19
597	    - shift_pp
598	    - on_shifted_pareto
599	    rows:
600	    - - 40
601	      - 0.776
602	      - 0.798
603	      - 2.2
604	      - false
605	    - - 44
606	      - 0.774
607	      - 0.8
608	      - 2.6
609	      - false
610	    - - 48
611	      - 0.77
612	      - 0.803
613	      - 3.3
614	      - true
615	    - - 52
616	      - 0.765
617	      - 0.806
618	      - 4.1
619	      - true
620	    - - 56
621	      - 0.762
622	      - 0.81
623	      - 4.8
624	      - true
625	    - - 60
626	      - 0.753
627	      - 0.814
628	      - 6.1
629	      - true
630	    - - 64
631	      - 0.741
632	      - 0.814
633	      - 7.3
634	      - true
635	    - - 68
636	      - 0.728
637	      - 0.808
638	      - 8.0
639	      - true
640	    - - 72
641	      - 0.712
642	      - 0.796
643	      - 8.4
644	      - false
645	  figures_description:
646	  - 'Figure 3: Pareto frontier before/after CaCLR. ZS frontier (blue) vs CaCLR frontier
647	    (red), showing outward shift. CaCLR''s optimal operating point is 2 layers deeper
648	    with +5pp transfer AUROC.'
649	  - 'Figure 4: Per-language AUROC improvement from CaCLR over linear projection, grouped
650	    by resource tier. Low-resource languages show largest gains (4-6pp), high-resource
651	    2-3pp.'
652	  - 'Figure 5: Loss component ablation bar chart — stacked contributions of L_SB-ECE
653	    and L_consistency to final AUROC and ECE improvements.'
654	  analysis: 'CaCLR decisively outperforms all baselines. The ablation shows both loss
655	    terms contribute: L_consistency provides the bulk of AUROC improvement (+4.1pp
656	    alone), while L_SB-ECE provides calibration refinement (ECE drops from 0.078 to
657	    0.061 when added). The interaction is synergistic — joint optimization yields
658	    better results than either term alone. The Pareto shift is the headline result:
659	    at the same EN calibration quality (L64, AUROC 0.835), CaCLR achieves 0.814 transfer
660	    vs 0.741 zero-shot — a 7.3pp improvement. This shifts the practical recommendation
661	    from "use shallower layers for transfer" to "use CaCLR and operate at deeper,
662	    better-calibrated layers." The improvement pass rate of 92% (35/38 model-lang
663	    pairs) demonstrates consistency. The 3 non-improving pairs are high-resource languages
664	    (fr, nl, de on Llama 4 Scout) where zero-shot transfer is already excellent and
665	    the consistency loss has minimal signal to exploit.
666	
667	    '
668	- name: Difficulty-Controlled Ablation
669	  plan_id: plan_004
670	  description: 'IRT difficulty probes (Ridge regression), project out difficulty direction,
671	    retrain correctness probes on residuals, evaluate transfer. 10 languages × 8 layers
672	    per model.
673	
674	    '
675	  expected_results:
676	    difficulty_probe_r2_mean: 0.72
677	    difficulty_var_explained_pct_mean: 68.4
678	    difficulty_var_explained_pct_range:
679	    - 58.2
680	    - 79.1
681	    residual_en_auroc_drop_pp: 4.2
682	    residual_zs_transfer_drop_pp: 1.1
683	    capability_specific_var_pct: 31.6
684	    capability_specific_transfer_degradation_pct: 87
685	    difficulty_component_transfer_degradation_pct: 13
686	    decomp_prescriptive_accuracy: 0.81
687	    difficulty_var_by_depth:
688	      shallow_20pct: 0.74
689	      mid_50pct: 0.69
690	      deep_80pct: 0.62
691	    capability_transfer_drop_by_depth:
692	      shallow_20pct: 0.8
693	      mid_50pct: 3.4
694	      deep_80pct: 9.7
695	  result_rationale: 'IRT difficulty is a strong, language-agnostic property — harder
696	    questions are harder everywhere. Ridge regression captures this cleanly (R²=0.72)
697	    because difficulty is linearly encoded in intermediate representations (Civelli
698	    et al. confirmed this). The difficulty component accounts for 68% of explained
699	    variance because GlobalMMLU correctness is heavily driven by item difficulty:
700	    a model gets easy questions right in all languages and hard questions wrong in
701	    all languages. After projecting out difficulty, the residual correctness signal
702	    is "capability-specific" — it captures language-dependent competence differences.
703	    This residual transfers poorly at deep layers (9.7pp drop at 80% depth vs 0.8pp
704	    at 20% depth) because deep layers encode language-specific processing that makes
705	    capability assessments non-transferable. The difficulty component transfers well
706	    at all depths (only 13% of total transfer degradation) because it''s language-invariant
707	    by construction. This decomposition is prescriptive: when difficulty explains
708	    most of a language''s correctness variance, simple zero-shot transfer suffices;
709	    when the capability residual is large, CaCLR is needed. The 81% prescriptive accuracy
710	    validates the decomposition as more than descriptive.
711	
712	    '
713	  tables:
714	  - name: 'Table 8: Decomposition Results — Difficulty vs Capability Components'
715	    columns:
716	    - component
717	    - var_explained_pct
718	    - transfer_auroc_mean
719	    - transfer_drop_from_en_pp
720	    - share_of_total_transfer_drop_pct
721	    rows:
722	    - - full_correctness
723	      - 100
724	      - 0.752
725	      - 8.1
726	      - 100
727	    - - difficulty_shared
728	      - 68.4
729	      - 0.738
730	      - 1.1
731	      - 13
732	    - - capability_specific
733	      - 31.6
734	      - 0.614
735	      - 14.2
736	      - 87
737	  - name: 'Table 9: Capability-Specific Transfer Drop by Depth'
738	    columns:
739	    - depth_band
740	    - difficulty_transfer_drop_pp
741	    - capability_transfer_drop_pp
742	    - ratio
743	    rows:
744	    - - 0-30%
745	      - 0.3
746	      - 0.8
747	      - 2.7×
748	    - - 30-60%
749	      - 0.8
750	      - 3.4
751	      - 4.3×
752	    - - 60-90%
753	      - 1.6
754	      - 9.7
755	      - 6.1×
756	  figures_description:
757	  - 'Figure 6: Stacked area chart showing difficulty vs capability variance across
758	    depth. Difficulty dominates at all depths but capability grows at deeper layers.'
759	  - 'Figure 7: Transfer degradation decomposed into difficulty (flat, near-zero) and
760	    capability (exponentially increasing with depth) components.'
761	  analysis: 'The decomposition cleanly separates: difficulty-shared signal is the
762	    majority (68%) of correctness variance and transfers near-perfectly across languages
763	    and depths. The capability-specific residual (32%) drives nearly all transfer
764	    degradation (87%), and this degradation accelerates exponentially with depth.
765	    This explains the Pareto frontier mechanistically: deeper layers have stronger
766	    capability-specific signals that improve EN calibration but impede transfer. CaCLR
767	    works because its consistency loss specifically targets the capability-specific
768	    component — forcing alignment of the non-difficulty residual across languages.
769	    The prescriptive value (81% accuracy in predicting when CaCLR is needed) confirms
770	    this is a load-bearing decomposition, not a post-hoc narrative.
771	
772	    '
773	- name: Cross-Lingual Orthogonality Analysis
774	  plan_id: plan_005
775	  description: 'Extract verbalized confidence direction via prompted confidence scores,
776	    compute cosine similarity with correctness direction across 20 languages × 2 architectures.
777	    Analyze by resource tier and language family.
778	
779	    '
780	  expected_results:
781	    orthogonality_cosine_mean_overall: 0.052
782	    orthogonality_cosine_range:
783	    - 0.018
784	    - 0.094
785	    orthogonality_cosine_en: 0.034
786	    qwen3_cosine_mean: 0.048
787	    llama4_cosine_mean: 0.057
788	    high_resource_cosine_mean: 0.041
789	    mid_resource_cosine_mean: 0.054
790	    low_resource_cosine_mean: 0.074
791	    cosine_by_lang:
792	      en: 0.034
793	      zh: 0.038
794	      de: 0.036
795	      fr: 0.039
796	      es: 0.041
797	      ja: 0.044
798	      ru: 0.043
799	      pt: 0.04
800	      it: 0.042
801	      ar: 0.051
802	      hi: 0.055
803	      ko: 0.049
804	      vi: 0.058
805	      th: 0.061
806	      bn: 0.056
807	      tr: 0.052
808	      nl: 0.037
809	      sw: 0.078
810	      yo: 0.094
811	      ig: 0.082
812	    all_langs_below_0p1: true
813	    cosine_resource_tier_correlation: -0.68
814	  result_rationale: 'Miao & Ungar (2026) established correctness-confidence orthogonality
815	    (cosine < 0.04) for English on 7-8B models. We extend to 20 languages on larger
816	    models. The orthogonality persists universally (all < 0.1) because it reflects
817	    a fundamental architectural property: verbalized confidence is generated by the
818	    language modeling head from surface-level token probabilities, while correctness
819	    is encoded in intermediate representation geometry. These are structurally decoupled
820	    in transformer architectures. The slight increase in cosine for low-resource languages
821	    (0.074 mean vs 0.041 for high-resource) occurs because low-resource languages
822	    have noisier confidence elicitation — the model''s verbalized confidence in Yoruba
823	    is less well-calibrated and leaks some correctness signal, producing weak correlation.
824	    The resource-tier gradient (ρ=-0.68) suggests that better multilingual training
825	    data produces cleaner separation between correctness and confidence representations.
826	    The cross-architecture consistency (Qwen3: 0.048, Llama4: 0.057) confirms this
827	    is not architecture-specific. Llama 4''s slightly higher cosines may reflect its
828	    less aggressive multilingual pretraining compared to Qwen3.
829	
830	    '
831	  tables:
832	  - name: 'Table 10: Correctness-Confidence Cosine Similarity by Language and Architecture'
833	    columns:
834	    - language
835	    - resource_tier
836	    - qwen3_cosine
837	    - llama4_cosine
838	    - mean_cosine
839	    rows:
840	    - - en
841	      - high
842	      - 0.031
843	      - 0.037
844	      - 0.034
845	    - - zh
846	      - high
847	      - 0.035
848	      - 0.041
849	      - 0.038
850	    - - de
851	      - high
852	      - 0.033
853	      - 0.039
854	      - 0.036
855	    - - fr
856	      - high
857	      - 0.036
858	      - 0.042
859	      - 0.039
860	    - - es
861	      - high
862	      - 0.038
863	      - 0.044
864	      - 0.041
865	    - - ja
866	      - high
867	      - 0.041
868	      - 0.047
869	      - 0.044
870	    - - ru
871	      - high
872	      - 0.04
873	      - 0.046
874	      - 0.043
875	    - - pt
876	      - high
877	      - 0.037
878	      - 0.043
879	      - 0.04
880	    - - it
881	      - high
882	      - 0.039
883	      - 0.045
884	      - 0.042
885	    - - nl
886	      - high
887	      - 0.034
888	      - 0.04
889	      - 0.037
890	    - - ar
891	      - mid
892	      - 0.047
893	      - 0.055
894	      - 0.051
895	    - - hi
896	      - mid
897	      - 0.051
898	      - 0.059
899	      - 0.055
900	    - - ko
901	      - mid
902	      - 0.045
903	      - 0.053
904	      - 0.049
905	    - - vi
906	      - mid
907	      - 0.054
908	      - 0.062
909	      - 0.058
910	    - - th
911	      - mid
912	      - 0.057
913	      - 0.065
914	      - 0.061
915	    - - bn
916	      - mid
917	      - 0.052
918	      - 0.06
919	      - 0.056
920	    - - tr
921	      - mid
922	      - 0.048
923	      - 0.056
924	      - 0.052
925	    - - sw
926	      - low
927	      - 0.073
928	      - 0.083
929	      - 0.078
930	    - - yo
931	      - low
932	      - 0.089
933	      - 0.099
934	      - 0.094
935	    - - ig
936	      - low
937	      - 0.077
938	      - 0.087
939	      - 0.082
940	  - name: 'Table 11: Orthogonality Summary Statistics'
941	    columns:
942	    - statistic
943	    - qwen3_235b
944	    - llama4_scout
945	    - both_models
946	    rows:
947	    - - cosine_mean
948	      - 0.048
949	      - 0.057
950	      - 0.052
951	    - - cosine_std
952	      - 0.015
953	      - 0.017
954	      - 0.016
955	    - - cosine_max
956	      - 0.089
957	      - 0.099
958	      - 0.094
959	    - - cosine_min
960	      - 0.031
961	      - 0.037
962	      - 0.018
963	    - - all_below_0.1
964	      - yes (20/20)
965	      - yes (19/20)
966	      - 39/40
967	    - - resource_tier_corr
968	      - -0.71
969	      - -0.65
970	      - -0.68
971	  figures_description:
972	  - 'Figure 8: Cosine similarity violin plots by resource tier, showing clear gradient
973	    from high (tight around 0.04) to low (spread around 0.08). All below 0.1 threshold.'
974	  - 'Figure 9: Scatter plot of cosine similarity vs language resource level (log wiki
975	    size), colored by architecture. Strong negative trend.'
976	  analysis: 'Orthogonality generalizes comprehensively. The mean cosine of 0.052 across
977	    all 40 language-architecture pairs is well within the "near-orthogonal" regime
978	    (< 0.1). The resource-tier gradient is the novel finding: it suggests that output-based
979	    calibration methods are not just structurally limited but are *more* limited for
980	    well-resourced languages where the orthogonality is strongest. This strengthens
981	    the motivation for probe-based approaches universally and for CaCLR specifically
982	    in multilingual settings. Yoruba''s 0.094 is the only value approaching the 0.1
983	    threshold (on Llama4 it hits 0.099), which is worth noting but does not break
984	    the claim.
985	
986	    '
987	- name: Probe Complexity Comparison
988	  plan_id: plan_006
989	  description: 'Logistic regression vs 2-layer MLP at each probed layer, both models.
990	    Compare English accuracy, cross-lingual transfer degradation, calibration quality.
991	
992	    '
993	  expected_results:
994	    logreg_en_auroc_best: 0.843
995	    mlp_en_auroc_best: 0.856
996	    mlp_en_auroc_gain_pp: 1.3
997	    logreg_zs_transfer_drop_mean_pp: 8.1
998	    mlp_zs_transfer_drop_mean_pp: 12.4
999	    transfer_degradation_ratio: 1.53
1000	    logreg_ece_mean: 0.054
1001	    mlp_ece_mean: 0.068
1002	    logreg_transfer_advantage_shallow_pp: 2.1
1003	    logreg_transfer_advantage_deep_pp: 6.8
1004	  result_rationale: 'Linear probes transfer better because they learn a single hyperplane
1005	    in activation space — the hyperplane generalizes across languages when the underlying
1006	    geometry is approximately shared (as it is in mid-depth layers). MLPs learn nonlinear
1007	    decision boundaries that fit English-specific feature interactions, gaining ~1.3pp
1008	    EN AUROC but losing ~4.3pp in transfer. The transfer gap widens at deeper layers
1009	    (6.8pp advantage for logreg) because deep layers have more language-specific nonlinear
1010	    structure that MLPs exploit but logreg ignores. This justifies our choice of linear
1011	    probes for the main results and supports the geometric interpretation of the Pareto
1012	    frontier: it''s about linear subspace alignment, not complex feature interactions.
1013	
1014	    '
1015	  tables:
1016	  - name: 'Table 12: Probe Complexity Comparison'
1017	    columns:
1018	    - probe_type
1019	    - en_auroc_best
1020	    - zs_auroc_mean_19
1021	    - zs_drop_pp
1022	    - ece_mean_19
1023	    rows:
1024	    - - logistic_regression
1025	      - 0.843
1026	      - 0.762
1027	      - 8.1
1028	      - 0.054
1029	    - - mlp_2layer
1030	      - 0.856
1031	      - 0.733
1032	      - 12.4
1033	      - 0.068
1034	  figures_description:
1035	  - 'Figure S1 (supplementary): Transfer drop (pp) vs layer depth for both probe types.
1036	    MLP line diverges sharply from logreg at deep layers.'
1037	  analysis: 'Linear probes are the correct choice for cross-lingual transfer: they
1038	    sacrifice 1.3pp EN AUROC but gain 4.3pp average transfer. The depth interaction
1039	    effect is notable — the logreg advantage grows from 2.1pp at shallow layers to
1040	    6.8pp at deep layers, confirming that deep-layer transfer degradation is driven
1041	    by nonlinear, language- specific features. CaCLR + logreg is thus the optimal
1042	    configuration.
1043	
1044	    '
1045	- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)
1046	  plan_id: plan_007
1047	  description: 'Evaluate best probes + CaCLR on Belebele (20 languages) and MMLU-ProX
1048	    (20 languages).
1049	
1050	    '
1051	  expected_results:
1052	    belebele_zs_auroc_mean_19: 0.738
1053	    belebele_caclr_auroc_mean_19: 0.789
1054	    belebele_caclr_vs_zs_pp: 5.1
1055	    belebele_ece_reduction_vs_tempcal_pct: 36.2
1056	    mmlupx_zs_auroc_mean_19: 0.722
1057	    mmlupx_caclr_auroc_mean_19: 0.774
1058	    mmlupx_caclr_vs_zs_pp: 5.2
1059	    mmlupx_ece_reduction_vs_tempcal_pct: 33.8
1060	    caclr_benefit_cross_benchmark_cv: 0.08
1061	  result_rationale: 'Belebele tests reading comprehension (vs GlobalMMLU''s factual
1062	    knowledge), providing domain generalization evidence. Transfer AUROC is slightly
1063	    lower (0.738 vs 0.762) because Belebele''s passage-dependent questions have weaker
1064	    difficulty-shared signal — comprehension difficulty is more language-dependent
1065	    than factual difficulty. CaCLR still provides ~5pp improvement, confirming the
1066	    consistency loss generalizes beyond factual MCQA. MMLU-ProX has harder questions
1067	    that compress the AUROC distribution (lower base rate of correctness), yielding
1068	    slightly lower absolute numbers but comparable CaCLR benefit. The cross-benchmark
1069	    CV of 0.08 for CaCLR improvement confirms the method is robust to evaluation domain.
1070	
1071	    '
1072	  tables:
1073	  - name: 'Table 13: Cross-Benchmark Generalization'
1074	    columns:
1075	    - benchmark
1076	    - zs_auroc_mean_19
1077	    - caclr_auroc_mean_19
1078	    - caclr_gain_pp
1079	    - ece_reduction_pct
1080	    rows:
1081	    - - GlobalMMLU
1082	      - 0.752
1083	      - 0.804
1084	      - 5.2
1085	      - 39.7
1086	    - - Belebele
1087	      - 0.738
1088	      - 0.789
1089	      - 5.1
1090	      - 36.2
1091	    - - MMLU-ProX
1092	      - 0.722
1093	      - 0.774
1094	      - 5.2
1095	      - 33.8
1096	  figures_description:
1097	  - 'Figure S2: CaCLR improvement (pp) by benchmark × language, showing consistent
1098	    gains across domains.'
1099	  analysis: 'CaCLR generalizes cleanly across benchmarks. The improvement magnitude
1100	    is remarkably stable (5.1-5.2pp AUROC, 33-40% ECE reduction), suggesting the method
1101	    addresses a fundamental representation alignment issue rather than overfitting
1102	    to GlobalMMLU- specific patterns. This is critical for reviewer confidence.
1103	
1104	    '
1105	- name: INT8 Validation Ablation
1106	  plan_id: plan_010
1107	  description: 'Compare INT8 vs FP16 probing results at 5 representative layers for
1108	    Llama 4 Scout on 5% random subset.
1109	
1110	    '
1111	  expected_results:
1112	    int8_fp16_auroc_diff_mean_pp: 0.3
1113	    int8_fp16_auroc_diff_max_pp: 0.7
1114	    int8_fp16_ece_diff_mean_pp: 0.2
1115	    int8_fp16_transfer_drop_diff_pp: 0.4
1116	    int8_fp16_rank_correlation: 0.997
1117	    conclusion: INT8 quantization introduces negligible distortion
1118	  result_rationale: 'INT8 weight-only quantization preserves the 8 most significant
1119	    bits of each weight, introducing per-channel quantization noise of ~0.4% relative
1120	    magnitude. Correctness probing relies on the geometry of activation space (direction
1121	    of correctness signal), not absolute magnitudes. The quantization noise is approximately
1122	    isotropic and thus preserves angular relationships between directions. The 0.3pp
1123	    mean AUROC difference is within random seed variance, and the rank correlation
1124	    of 0.997 between INT8 and FP16 layer rankings confirms that the Pareto frontier
1125	    shape is unaffected. This result is expected given prior work showing that probing
1126	    results are robust to quantization down to INT4 (Gao et al., 2024).
1127	
1128	    '
1129	  tables:
1130	  - name: 'Table S1: INT8 vs FP16 Comparison (Llama 4 Scout, 5% subset)'
1131	    columns:
1132	    - layer_idx
1133	    - fp16_auroc
1134	    - int8_auroc
1135	    - diff_pp
1136	    - fp16_zs_auroc_5lang
1137	    - int8_zs_auroc_5lang
1138	    - transfer_diff_pp
1139	    rows:
1140	    - - 8
1141	      - 0.674
1142	      - 0.672
1143	      - 0.2
1144	      - 0.661
1145	      - 0.658
1146	      - 0.3
1147	    - - 16
1148	      - 0.747
1149	      - 0.745
1150	      - 0.2
1151	      - 0.731
1152	      - 0.728
1153	      - 0.3
1154	    - - 24
1155	      - 0.788
1156	      - 0.786
1157	      - 0.2
1158	      - 0.747
1159	      - 0.744
1160	      - 0.3
1161	    - - 32
1162	      - 0.812
1163	      - 0.81
1164	      - 0.2
1165	      - 0.734
1166	      - 0.731
1167	      - 0.3
1168	    - - 40
1169	      - 0.82
1170	      - 0.817
1171	      - 0.3
1172	      - 0.691
1173	      - 0.687
1174	      - 0.4
1175	  figures_description:
1176	  - 'Figure S3: INT8 vs FP16 AUROC scatter plot at all tested layer-language combinations.
1177	    Points fall tightly along y=x diagonal.'
1178	  analysis: 'INT8 quantization is validated as safe for our experimental setup. The
1179	    maximum observed difference (0.7pp at a single layer-language combination) is
1180	    well within the noise floor of probing experiments. The Pareto frontier ordering
1181	    is perfectly preserved (rank correlation 0.997). This ablation preempts reviewer
1182	    concern #5.
1183	
1184	    '
1185	- name: Gemma 4 31B Dense — Third Architecture (Camera-Ready)
1186	  plan_id: plan_008
1187	  description: 'Full Pareto frontier on Gemma 4 31B Dense (60 layers), 20+ languages.
1188	    Provides dense vs MoE architectural contrast.
1189	
1190	    '
1191	  expected_results:
1192	    en_auroc_best_layer: 0.812
1193	    en_best_layer_idx: 45
1194	    zs_transfer_auroc_mean_19lang: 0.734
1195	    zs_best_transfer_layer_idx: 36
1196	    zs_transfer_drop_mean_pp: 7.8
1197	    pareto_depth_transfer_rank_corr: 0.86
1198	    caclr_auroc_mean_19lang: 0.786
1199	    caclr_vs_linproj_auroc_delta_pp: 2.9
1200	    dense_vs_moe_transfer_comparison: comparable within 2pp
1201	    pareto_shape: convex monotonic, consistent with MoE models
1202	  result_rationale: 'Gemma 4 31B Dense has fewer total parameters than the MoE models
1203	    but all are active, yielding comparable per-token compute. As a dense model, its
1204	    representations are more uniformly distributed across layers (no expert routing),
1205	    producing slightly smoother Pareto frontiers. The best-transfer depth (~60%) matches
1206	    both MoE models, confirming this is a universal property of transformer depth,
1207	    not MoE-specific. EN AUROC is slightly lower (0.812 vs 0.843/0.821) because 31B
1208	    active params < 22B active with MoE routing benefits. CaCLR improvement is slightly
1209	    lower (2.9pp) on the dense model because the absence of expert routing means less
1210	    language-specific feature fragmentation to correct. This is the ideal third data
1211	    point: different architecture family, consistent findings.
1212	
1213	    '
1214	  tables:
1215	  - name: 'Table 14: Three-Architecture Summary'
1216	    columns:
1217	    - model
1218	    - type
1219	    - layers
1220	    - en_auroc_best
1221	    - zs_auroc_mean_19
1222	    - best_transfer_depth_pct
1223	    - pareto_rank_corr
1224	    - caclr_gain_pp
1225	    rows:
1226	    - - Qwen3-235B-A22B
1227	      - MoE
1228	      - 94
1229	      - 0.843
1230	      - 0.762
1231	      - 60
1232	      - 0.88
1233	      - 3.3
1234	    - - Llama 4 Scout
1235	      - MoE
1236	      - 48
1237	      - 0.821
1238	      - 0.741
1239	      - 58
1240	      - 0.82
1241	      - 3.1
1242	    - - Gemma 4 31B Dense
1243	      - Dense
1244	      - 60
1245	      - 0.812
1246	      - 0.734
1247	      - 60
1248	      - 0.86
1249	      - 2.9
1250	  figures_description:
1251	  - 'Figure 10: Three-architecture Pareto frontiers overlaid (normalized depth). Remarkably
1252	    similar shapes despite architectural differences.'
1253	  analysis: 'The three-architecture comparison is the strongest evidence for the universality
1254	    of the depth-transferability tradeoff. The best-transfer depth converges to 58-60%
1255	    across dense and MoE architectures with 48-94 layers, CaCLR provides consistent
1256	    2.9-3.3pp improvement, and the Pareto rank correlation is 0.82-0.88 in all cases.
1257	    Dense vs MoE makes minimal difference — the phenomenon is a property of transformer
1258	    depth, not routing architecture.
1259	
1260	    '
1261	- name: Extended Language Coverage (Camera-Ready)
1262	  plan_id: plan_009
1263	  description: 'Expand from 20 to 50+ languages for camera-ready, leveraging GlobalMMLU/Belebele
1264	    full language sets.
1265	
1266	    '
1267	  expected_results:
1268	    total_languages: 52
1269	    new_languages_added: 32
1270	    zs_auroc_above_0p60_count: 48
1271	    zs_auroc_below_0p55_count: 2
1272	    caclr_improvement_positive_count: 49
1273	    mean_zs_auroc_51lang: 0.72
1274	    mean_caclr_auroc_51lang: 0.77
1275	    pareto_frontier_holds_all_langs: true
1276	    new_language_families_covered:
1277	    - Austronesian
1278	    - Dravidian
1279	    - Niger-Congo B
1280	    - Uralic
1281	    - Kartvelian
1282	  result_rationale: 'Expanding to 50+ languages primarily adds mid-resource languages
1283	    (Indonesian, Malay, Finnish, Georgian, Tamil, Telugu, etc.) where the model has
1284	    moderate pretraining exposure. Most new languages fall in the 0.65-0.78 AUROC
1285	    range, consistent with the mid-resource tier from the 20-language set. A handful
1286	    of extremely low-resource languages (e.g., Amharic script languages with minimal
1287	    pretraining data) may fall below 0.55, but these represent edge cases rather than
1288	    systematic failures. CaCLR continues to improve 96% of languages because the consistency
1289	    loss mechanism is language-agnostic — it aligns activation distributions without
1290	    requiring any language-specific knowledge. The Pareto frontier structure is preserved
1291	    across all 52 languages, confirming it''s a depth property, not a language-set
1292	    artifact.
1293	
1294	    '
1295	  tables:
1296	  - name: 'Table 15: Extended Language Coverage Summary by Resource Tier'
1297	    columns:
1298	    - tier
1299	    - n_langs
1300	    - zs_auroc_mean
1301	    - caclr_auroc_mean
1302	    - caclr_gain_pp
1303	    - pct_above_0p60
1304	    rows:
1305	    - - high
1306	      - 12
1307	      - 0.782
1308	      - 0.812
1309	      - 3.0
1310	      - 100
1311	    - - mid
1312	      - 25
1313	      - 0.738
1314	      - 0.784
1315	      - 4.6
1316	      - 100
1317	    - - low
1318	      - 10
1319	      - 0.661
1320	      - 0.712
1321	      - 5.1
1322	      - 90
1323	    - - very_low
1324	      - 4
1325	      - 0.582
1326	      - 0.638
1327	      - 5.6
1328	      - 50
1329	  figures_description:
1330	  - 'Figure 11: World map with per-language CaCLR AUROC, colored by performance tier.
1331	    Demonstrates broad geographic and typological coverage.'
1332	  analysis: 'The extension to 52 languages confirms all findings at broader scale.
1333	    The resource-tier gradient is smooth and predictable — no language family shows
1334	    anomalous behavior. CaCLR''s benefit is inversely correlated with resource level
1335	    (3.0pp for high-resource to 5.6pp for very-low-resource), confirming that the
1336	    consistency loss provides most value where representation misalignment is worst.
1337	    The 48/51 pass rate (>0.60 AUROC) for zero-shot CaCLR transfer with no target-language
1338	    labels is the practical headline for camera-ready: usable cross-lingual calibration
1339	    for the vast majority of languages.'
1340	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aaf7c16a-978a-493a-9edc-a644267be547",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "cd800c13-461c-42a6-abb9-2e7381918ab0",
  "sourceToolAssistantUUID": "aaf7c16a-978a-493a-9edc-a644267be547",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-20T19:53:15.717Z_

Now let me check the literature map for missing baselines and the worst-case CaCLR results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd800c13-461c-42a6-abb9-2e7381918ab0",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQUfCspeniBUiTw3Ln1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec0f6fe0-7b38-4769-ac85-910470138a03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xY4rv1gZqpWjJUMq3p1mV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17237,
      "cache_read_input_tokens": 53407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17237,
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

_source line 39 · 2026-05-20T19:53:16.737Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XrTL1sAqD9nmRFtkrk1YDU`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec0f6fe0-7b38-4769-ac85-910470138a03",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQUfCspeniBUiTw3Ln1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0583002b-2a20-4a0f-916f-65e06777fa04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016xY4rv1gZqpWjJUMq3p1mV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17237,
      "cache_read_input_tokens": 53407,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17237
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 133,
          "cache_read_input_tokens": 53407,
          "cache_creation_input_tokens": 17237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17237,
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

_source line 40 · 2026-05-20T19:53:16.748Z_

<details><summary>↩ Tool result · `toolu_01XrTL1sAqD9nmRFtkrk1YDU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/literature_map.yaml\", \"content\": \"papers:\\n  miao2026closing:\\n    title: \\\"Closing the Confidence-Faithfulness Gap in Large Language Models\\\"\\n    authors: [\\\"Ruoxi Miao\\\", \\\"Lyle Ungar\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.25052\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Showed correctness direction and verbalized confidence direction are orthogonal (cosine < 0.04) in 7-8B models. Motivates probing internal representations. English-only — our cross-lingual extension is the natural next step.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  xiao2025knowledge:\\n    title: \\\"Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations\\\"\\n    authors: [\\\"Zheng Xiao\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2504.13816\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest prior work. Cross-lingual transfer of knowledge-boundary probes (answerable vs unanswerable). Key differences: they probe knowledge boundaries (input-level), we probe correctness (output-dependent); they measure probing accuracy, not ECE/Brier; they test 8 languages, we target 20+.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  civelli2026shared:\\n    title: \\\"A Shared Geometry of Difficulty in Multilingual Language Models\\\"\\n    authors: [\\\"Andrea Civelli\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2601.12731\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Cross-lingual difficulty probe transfer at intermediate layers. Architecture-dependent optimal depth (24-49%). Probes IRT difficulty (question property), not correctness (model property). Critical control for our difficulty ablation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  zhou2025lace:\\n    title: \\\"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in LLMs\\\"\\n    authors: [\\\"Zhou\\\"]\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2510.03136\\\"\\n    category: \\\"multilingual_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"LACE: adaptive layer ensemble for multilingual calibration. Confirmed 5x ECE gap across 100+ languages. Requires per-language validation data. Our CaCLR needs no non-English correctness labels.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ravisankar2026dali:\\n    title: \\\"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs\\\"\\n    authors: [\\\"Ravisankar\\\"]\\n    year: 2026\\n    venue: \\\"EACL 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2504.09378\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"DALI: causal evidence via activation patching that English middle-layer representations fix non-English errors across 24 languages. Strongest causal support for our hypothesis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  miao2026coral:\\n    title: \\\"Correctness-Optimized Residual Activation Lens (CORAL)\\\"\\n    authors: [\\\"Ruoxi Miao\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.06022\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Transferable correctness probes via regularized MLP on residual activations, ~50% ECE improvement at 53-66% depth. English-only, cross-task. CaCLR positioned as solution to their identified distribution-shift transfer degradation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  joshi2025calibration:\\n    title: \\\"Calibration Across Layers: Understanding Calibration Evolution in LLMs\\\"\\n    authors: [\\\"Joshi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Identified low-dimensional calibration direction in residual stream evolving across layers.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  confidence_manifold2026:\\n    title: \\\"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.08159\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Correctness signals occupy 3-8 dimensions, linearly separable. 25 labeled examples achieve 89% of full-data accuracy. All English-only.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  karandikar2021sbece:\\n    title: \\\"Soft Calibration Objectives for Neural Networks\\\"\\n    authors: [\\\"Karandikar\\\"]\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"\\\"\\n    category: \\\"calibration_methods\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"SB-ECE: differentiable soft-binned ECE enabling gradient-based calibration optimization. Core component of our CaCLR objective.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  khanmohammadi2025ccps:\\n    title: \\\"Calibrating LLM Confidence by Probing Perturbed Representation Stability (CCPS)\\\"\\n    authors: [\\\"Khanmohammadi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2505.21772\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Calibration via probing perturbed representation stability at final layer. ~55% ECE reduction. English-only, single layer. No cross-lingual or multi-layer analysis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  liu2025middle:\\n    title: \\\"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs\\\"\\n    authors: [\\\"Liu\\\", \\\"Niehues\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Middle layers form strongest language-agnostic shared space. Supports our hypothesis about intermediate-layer transfer.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ji2025calibrating:\\n    title: \\\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\\\"\\n    authors: [\\\"Ji\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Verbal uncertainty governed by single linear direction in representation space.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\ncategories:\\n  mechanistic_calibration: \\\"Probing/steering calibration signals in LLM internal representations\\\"\\n  cross_lingual_probing: \\\"Cross-lingual transfer of probes/directions in multilingual models\\\"\\n  cross_lingual_alignment: \\\"Language alignment and shared representations in multilingual LLMs\\\"\\n  multilingual_calibration: \\\"Calibration methods for multilingual LLMs\\\"\\n  calibration_methods: \\\"General calibration objectives and techniques\\\"\\n\\nmeta:\\n  created_at: \\\"2026-05-20\\\"\\n  last_updated: \\\"2026-05-20\\\"\\n  total_papers: 12\\n\", \"total_chars\": 6989, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0583002b-2a20-4a0f-916f-65e06777fa04",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "ce0a3bb0-b5ca-433d-84cd-561b67079610",
  "sourceToolAssistantUUID": "0583002b-2a20-4a0f-916f-65e06777fa04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-20T19:53:23.032Z_

Now I have comprehensive information about the paper's experimental design, methodology, results (across best/median/worst scenarios), and related work. Let me also look at the actual reported results more carefully. The paper summary states the actual results align closer to the "worst" tier for many findings (e.g., rho=0.41 for Qwen3, 0.22 for Llama4, consistency loss being inert). Let me now write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce0a3bb0-b5ca-433d-84cd-561b67079610",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQV99PkXJ6RzkTMVByU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b8da982-42dc-4ccd-bdc4-39b8eea5522a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NrGTG2rnvzuJFi8Ccef9Uc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2990,
      "cache_read_input_tokens": 70644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2990,
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

_source line 42 · 2026-05-20T19:53:23.938Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01J8JwwGmE4VsCqSkFRffDVW`</summary>

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
  "parentUuid": "7b8da982-42dc-4ccd-bdc4-39b8eea5522a",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQV99PkXJ6RzkTMVByU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73ddd57b-caa1-46b9-8592-c400fbc8fc41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NrGTG2rnvzuJFi8Ccef9Uc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2990,
      "cache_read_input_tokens": 70644,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2990
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 70644,
          "cache_creation_input_tokens": 2990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2990,
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

_source line 43 · 2026-05-20T19:53:23.944Z_

<details><summary>↩ Tool result · `toolu_01J8JwwGmE4VsCqSkFRffDVW`</summary>

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
  "parentUuid": "73ddd57b-caa1-46b9-8592-c400fbc8fc41",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "baee2c74-20a3-463b-a6fc-4d0e756ca1ca",
  "sourceToolAssistantUUID": "73ddd57b-caa1-46b9-8592-c400fbc8fc41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T19:54:18.610Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01W6bEjMCMd8f1MuANXqDtM3`</summary>

```json
{
  "project": "xling_calib_direction",
  "tier": "best",
  "dream_id": "dream_20260520T185641",
  "overall_score": "Weak Accept (4/6)",
  "report": "## Reviewer 1 (R1): Methods and Experiments\n\n### Summary\nThis paper systematically evaluates whether English-trained correctness probes on internal LLM representations transfer cross-lingually, across 3 architectures (Qwen3-235B, Llama 4 Scout, Gemma 4 31B), 20-52 languages, and 5 transfer conditions. It discovers a depth-transferability Pareto frontier, proposes CaCLR (a joint calibration-consistency objective), performs difficulty-capability decomposition, and extends the correctness-confidence orthogonality finding to multilingual settings.\n\n### Strengths\n\n**S1. Ambitious and well-structured experimental scope.** 10 experiment plans covering 3 architectures, up to 52 languages, multiple benchmarks, and systematic ablations. The causal chain (discovery → analysis → method → mechanism) is logically coherent. The coverage of MoE vs Dense architectures strengthens generalizability claims.\n\n**S2. Principled negative results honestly reported.** The consistency loss being inert (sweeping beta over 3 OOM changes AUROC <0.3pp), mean-shift failing entirely, and CaCLR never beating linear projection on cross-benchmark evaluation are all valuable findings for the community. The paper does not oversell.\n\n**S3. Comprehensive baseline coverage.** Five transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR) provide a fair comparison landscape. The INT8 validation ablation (cosine 0.994, 0.3pp AUROC difference) proactively addresses quantization concerns.\n\n**S4. The difficulty-capability decomposition (Plan 004) is methodologically interesting.** Projecting out IRT difficulty and showing this *hurts* transfer by 1.3-1.4pp is a counterintuitive and informative result that challenges the assumption of clean separability.\n\n### Weaknesses\n\n**W1. The Pareto frontier claim is architecture-dependent to the point of undermining universality.** The paper reports rho=0.41 (Qwen3), 0.22 (Llama4), 0.48 (Gemma4). A rank correlation of 0.22 explains <5% of variance and is barely meaningful. Claiming a \"Pareto frontier\" when the relationship is this noisy on one of three architectures weakens Claim 1 substantially. The paper should acknowledge this is a *tendency* in some architectures rather than a universal structural property.\n\n**W2. CaCLR's consistency loss is inert — this fundamentally undermines Claim 3.** The paper's proposed method contribution is CaCLR (L_BCE + alpha*L_SB-ECE + beta*L_consistency). If sweeping beta over 3 orders of magnitude changes AUROC by <0.3pp, and *removing* it improves by 0.2pp, then CaCLR reduces to L_BCE + L_SB-ECE, which is simply calibration-aware probe training — not a novel cross-lingual alignment method. The \"consistency\" component that was supposed to be the differentiator from linear projection is doing nothing. Furthermore, \"CaCLR never beats linear projection\" on cross-benchmark (Result 7) means the method contribution is essentially negative.\n\n**W3. No confidence intervals or significance tests on the key comparisons.** Effect sizes like Cohen's d=0.18 for probe complexity and the 1.3-1.4pp decomposition degradation are small. Without bootstrap CIs or paired tests across the 19/52 languages, it is impossible to assess whether these effects are reliably non-zero. The MLP transfer penalty of -0.2 to -0.4pp is tiny and may be noise.\n\n**W4. The \"parallel activations\" requirement for CaCLR is underspecified.** The consistency loss requires comparable EN and non-EN activations. How are these obtained? Translated GlobalMMLU items? If so, how is translation quality controlled? Does it require parallel corpora at inference time? This has major practical implications for the \"zero target-language labels\" claim — you still need parallel *inputs*, which may be harder to obtain than 25-100 labeled examples.\n\n**W5. Extended 52-language evaluation (Plan 009) shows 23.5% pass rate and 0% for very-low-resource.** This result significantly undermines the practical value proposition. If the method works only for languages that already have reasonable LLM coverage, the incremental value over simply collecting a few dozen labeled examples per language is questionable.\n\n### Questions for Authors\n\nQ1. What exactly are \"parallel activations\" for L_consistency? Are these from the same MCQA items machine-translated into each language (as in GlobalMMLU)? If so, does CaCLR require access to the evaluation benchmark's translations at training time — creating a form of test-set leakage?\n\nQ2. For the Pareto frontier on Llama 4 Scout (rho=0.22, non-monotonic at layers 20-28), can you provide bootstrap confidence intervals on the rank correlation? With only 12 data points, the sampling uncertainty may be substantial.\n\nQ3. The paper claims \"projecting out difficulty hurts transfer by 1.3-1.4pp\" — but over how many language-layer combinations? Is this statistically significant by a paired test? What is the variance across the 10 languages x 8 layers = 80 conditions?\n\nQ4. Temperature scaling T values (5-6) are extremely high, implying massive overconfidence in the raw probes. Was T optimized on held-out data or the test set? If the latter, ECE numbers are unreliable.\n\nQ5. How sensitive is CaCLR to the choice of alpha? You report beta is inert, but what about alpha (the SB-ECE weight)?\n\n### Minor Issues\n\nM1. Table 5 reports \"Pareto frontier coherence\" across 3 architectures but rho values of 0.41, 0.22, 0.48 do not constitute \"coherence\" in any standard sense. Revise the table title.\n\nM2. The 52-language extension uses only Qwen3 (from context). Cross-architecture validation at this scale would strengthen the claim.\n\nM3. \"Orthogonality persists across 20 languages (mean cosine 0.072)\" — this is interesting but somewhat expected given the finding is architectural, not language-specific. The novelty here is incremental over Miao & Ungar.\n\nM4. The probe complexity finding (MLP +1pp EN, -0.2 to -0.4pp transfer) with Cohen's d=0.18 is a very small effect. Consider whether this table adds value or could move to supplementary.\n\nM5. The paper uses GlobalMMLU, Belebele, and MMLU-ProX — all MCQA. Generalization beyond MCQA remains entirely open.\n\n### Score: 4 (Weak Accept)\n\n**Justification:** The paper addresses a timely and important question (does probe-based calibration generalize multilingually?) with thorough experimentation across architectures and languages. The systematic characterization is valuable regardless of whether CaCLR succeeds as a method. However, the method contribution (CaCLR) is effectively negative — the consistency loss is inert and the method never beats linear projection cross-benchmark. The Pareto frontier is weak on 1/3 architectures (rho=0.22). These issues reduce the paper from a strong method+discovery paper to primarily a diagnostic/characterization paper with negative results. For a top venue, the paper needs either (a) a working method that actually shifts the frontier, or (b) explicit reframing as a diagnostic study with the CaCLR negative result as a contribution. Currently it sits uncomfortably between these framings. The breadth of experiments, honest reporting of negative results, and field-level significance of answering \"does this work multilingually?\" push it toward acceptance at a venue like EACL, but the weak method contribution keeps it below the bar for a top ML venue.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "baee2c74-20a3-463b-a6fc-4d0e756ca1ca",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQVfsLaz9YsSf2ThLnP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9043fc4-58b9-4935-ad8a-70b190714862",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEdchHv2ZxWW1CQtrXtTQE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 814,
      "cache_read_input_tokens": 73634,
      "output_tokens": 2035,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 814
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2035,
          "cache_read_input_tokens": 73634,
          "cache_creation_input_tokens": 814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 814,
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

_source line 45 · 2026-05-20T19:54:19.262Z_

<details><summary>↩ Tool result · `toolu_01W6bEjMCMd8f1MuANXqDtM3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_report.md\", \"dream_id\": \"dream_20260520T185641\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9043fc4-58b9-4935-ad8a-70b190714862",
  "isSidechain": true,
  "promptId": "74e75014-d2e0-4201-9f07-250c10a007ed",
  "agentId": "a8feaccbaabb0c33d",
  "type": "user",
  "uuid": "087ffadd-77d9-4eba-8e4c-1553a8b79cf4",
  "sourceToolAssistantUUID": "f9043fc4-58b9-4935-ad8a-70b190714862",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-20T19:54:27.187Z_

Review submitted. Here is the summary:

**Score: 4/6 (Weak Accept)**

Key findings from the review:

1. **CaCLR's method contribution is effectively undermined** by the consistency loss being inert (beta sweep over 3 OOM changes AUROC <0.3pp) and CaCLR never beating linear projection on cross-benchmark evaluation. The proposed method reduces to calibration-aware probe training rather than a novel cross-lingual alignment approach.

2. **The Pareto frontier claim lacks universality** — rho=0.22 on Llama 4 Scout (explaining <5% variance) is too weak to support a "frontier" narrative across architectures.

3. **Statistical rigor is insufficient** — no confidence intervals or significance tests on key small-effect comparisons (Cohen's d=0.18, 1.3-1.4pp decomposition effects).

4. **The "parallel activations" requirement for CaCLR is underspecified** — potentially requiring translated benchmarks at training time, which undermines the "zero target-language labels" framing.

5. **Practical value is limited** — 23.5% pass rate at 52 languages, 0% for very-low-resource languages.

The paper's strengths lie in its ambitious scope, honest negative results, comprehensive baselines, and field-level significance as a diagnostic study. It would benefit from explicit reframing as a systematic characterization paper rather than a method paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "087ffadd-77d9-4eba-8e4c-1553a8b79cf4",
  "isSidechain": true,
  "agentId": "a8feaccbaabb0c33d",
  "requestId": "req_011CbEQZkDtSG5A2E7qdAhqB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99783bba-b258-46a2-b931-09d9b7071625",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "8b4c3866-7c97-4fea-98c8-a02346ba8153",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMKo4MauF81T7qotRJrir2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2165,
      "cache_read_input_tokens": 74448,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2165
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 338,
          "cache_read_input_tokens": 74448,
          "cache_creation_input_tokens": 2165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2165,
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
