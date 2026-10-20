# Research conversation: You are Reviewer 1 (R1) for an ACL ARR peer review. Your focus is **methods and experiments**. You must be thorough, cri

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-acf51195619fdbc79.jsonl`
- **Structured JSON:** [`0c327d5aed6de304cf09.json`](../../sessions/0c/0c327d5aed6de304cf09.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

58 recorded events

### User

_source line 1 · 2026-05-21T06:00:20.143Z_

You are Reviewer 1 (R1) for an ACL ARR peer review. Your focus is **methods and experiments**. You must be thorough, critical, and fair.

## Paper Summary

**Title**: "When Does Cross-Lingual Calibration Transfer Work? Geometric Analysis and Practical Solutions"

**Core idea**: First large-scale study of cross-lingual correctness probe transfer. Trains English logistic regression probes on hidden-state activations, then evaluates zero-shot transfer to 20 languages across 3 resource tiers (HIGH/MID/LOW) on 2 MoE architectures (Qwen3-235B-A22B, Llama 4 Scout 17B-16E). Evaluates 5 transfer methods: zero-shot, mean-shift, CaCLR (MMD consistency loss), linear projection (Procrustes), few-shot fine-tuning.

**Key findings**:
1. Depth-transferability Pareto frontier is architecture-dependent: Qwen3 shows strong tradeoff (16/20 langs negative depth-transfer ρ, median −0.42), Llama 4 weaker (13/20, median −0.28). Linked to CKA cliff steepness.
2. CaCLR (systematic negative result): MMD consistency loss across full β sweep (0.001–1.0) yields ΔAUROC=+0.002 (p=0.42). Geometric explanation: MMD matches marginal probe-logit distributions but cannot align low-dimensional correctness subspace rotation. Subspace angles unchanged after CaCLR.
3. Linear projection with ~70 parallel pairs reaches 95% of max improvement. Procrustes effect reversal at ZS AUROC ~0.55: helps misaligned languages, hurts well-aligned ones.
4. ~30% LOW-resource and ~28% MID-resource language-layer combinations are capacity artifacts (selectivity < 0.05).
5. Simpson's Paradox in CKA-transfer: raw ρ negative, partial (controlling depth) positive. Significant on Llama 4 (ρ=0.29, p=0.018), trending on Qwen3 (ρ=0.16, p=0.072).

**Supporting analyses**: Cross-lingual orthogonality (cosine ~0.038, confirming Miao & Ungar), LR vs MLP comparison (LR better for transfer), cross-benchmark generalization (Belebele, MMLU-ProX), quantization validation (max |ΔAUROC| < 0.012), camera-ready extensions (Gemma 4 31B dense 3rd architecture, 52 languages).

**Models**: Qwen3-235B-A22B (94 layers, MoE, INT4, 24 probed layers every 4th) and Llama 4 Scout (48 layers, MoE, W4A16, 12 probed layers every 4th).

**Benchmarks**: Primary: GlobalMMLU. Generalization: Belebele, MMLU-ProX.

**Metrics**: AUROC, ECE. Bootstrap 95% CIs (1000 resamples), paired permutation tests, Cohen's d.

## Detailed Experimental Results

### Table 1 (Per-language ZS AUROC at EN-optimal layer L80, Qwen3):
HIGH: zh 0.732, es 0.741, fr 0.738, de 0.720, pt 0.730, ja 0.710
MID: ar 0.690, ru 0.700, ko 0.685, hi 0.665, vi 0.678, tr 0.655
LOW: sw 0.592, bn 0.608, th 0.620, te 0.568, yo 0.542, am 0.530

### Table 2 (Architecture comparison):
Qwen3: EN best 0.78, Mean ZS 0.660, Pareto sig 15/20, median ρ −0.42, CKA cliff ~68%, slope −0.025/L
Llama4: EN best 0.76, Mean ZS 0.643, Pareto sig 11/20, median ρ −0.28, CKA cliff ~55%, slope −0.015/L

### Table 5 (Simpson's Paradox):
Qwen3: n=480, raw ρ=−0.22 p<.001, partial ρ=+0.16 p=.072
Llama4: n=240, raw ρ=−0.28 p<.001, partial ρ=+0.29 p=.018

### Table 7 (CaCLR β sweep, Qwen3 L80):
β=0: 0.660 (baseline)
β=0.001: 0.661, Δ=+0.001, CI [−.004,+.006], d=0.03
β=0.01: 0.663, Δ=+0.003, CI [−.003,+.009], d=0.07
β=0.1: 0.658, Δ=−0.002, CI [−.008,+.004], d=0.05
β=1.0: 0.652, Δ=−0.008, CI [−.015,−.001], d=0.19

### Table 8 (CaCLR ablation):
BCE only: AUROC 0.660, ECE 0.192
BCE+SB-ECE: 0.658, 0.178
BCE+MMD: 0.662, 0.190
BCE+SB-ECE+MMD: 0.661, 0.176

### Table 9 (CKA subspace — why MMD fails):
HIGH: angle pre 12°, MMD 0.02→0.01, angle post 11°
MID: angle pre 24°, MMD 0.05→0.02, angle post 23°
LOW: angle pre 42°, MMD 0.12→0.05, angle post 40°

### Table 10 (Transfer method comparison, mean 20 langs):
Zero-shot: Q3 .660, L4 .643, Mean .652
Mean-shift: .660, .643, .652
CaCLR(best): .662, .645, .654
Lin proj(50): .678, .660, .669
Lin proj(200): .692, .673, .683
Few-shot 25: .678, .662, .670
Few-shot 100: .712, .693, .703

### Table 11 (Linear projection saturation):
10 pairs: HIGH +0.002, MID +0.010, LOW +0.028, Overall +0.013
50 pairs: +0.007, +0.026, +0.054, +0.027
100 pairs: +0.008, +0.029, +0.060, +0.030
200 pairs: +0.008, +0.030, +0.063, +0.032

### Table 12 (Procrustes reversal):
ZS < 0.50: n=4, mean Δ=+0.058, 100% positive
0.60–0.65: n=4, Δ=+0.003, 50% positive
> 0.70: n=4, Δ=−0.018, 0% positive
Reversal threshold ~0.55, CI [0.46, 0.63]

### Table 13 (Difficulty decomposition, Qwen3, 10 langs):
Mean ΔAUROC from difficulty projection: +0.012 (7/10 positive)
Random-direction control: +0.005
Difficulty-specific effect: ~2.4× random
Difficulty probe R²=0.35
Prescriptive accuracy: 58% (barely above chance 50%)

### Table 14 (Artifact rates):
LOW 0–25% depth: 83% artifacts; LOW overall: 30%
MID 0–25% depth: 58% artifacts; MID overall: 28%
HIGH overall: 6%

### Table 15 (Selectivity at L80):
yo: real .542, ctrl .510, selectivity .032 → ARTIFACT
am: real .530, ctrl .512, selectivity .018 → ARTIFACT

### Tables 17-21 (Supporting):
LR vs MLP: MLP +2pp EN but −5pp transfer gap
Cross-benchmark: patterns hold on Belebele/MMLU-ProX
Quantization: max |ΔAUROC| < 0.012
Gemma4 31B: Pareto sig 13/20, partial ρ(CKA)=0.22* (p=0.045)
52-lang expansion: core findings stable (rank ρ=0.94 with 20-lang)

## Experiment Design Reference (from context file)

The full experiment plan includes these experiments:
1. plan_001: Full Pareto Frontier — Qwen3-235B (COVERED in paper)
2. plan_002: Full Pareto Frontier — Llama 4 Scout (COVERED)
3. plan_003: CaCLR Implementation and Negative Result (COVERED)
4. plan_004: Difficulty-Controlled Decomposition Ablation (COVERED)
5. plan_005: Cross-Lingual Orthogonality Analysis (COVERED in §4.9.1)
6. plan_006: Probe Complexity LR vs MLP (COVERED in §4.9.2)
7. plan_007: Additional Benchmark Evaluation (COVERED in §4.9.3)
8. plan_008: Gemma 4 31B Dense (COVERED in §4.10 as camera-ready)
9. plan_009: Extended Language Coverage 52 langs (COVERED in §4.10)
10. plan_010: Quantization Validation (COVERED in §4.9.4)
11. plan_011: Full CKA + Simpson's Paradox Analysis (COVERED in §4.3)
12. plan_012: Linear Projection Sensitivity + Procrustes Reversal (COVERED in §4.6)
13. plan_013: Probing Control Tasks (COVERED in §4.8)

## ACL ARR Scoring Criteria

**Soundness** (1-5):
- 5 = Excellent: one of the most thorough studies
- 4 = Strong: sufficient support for all claims, some extra experiments nice but not essential
- 3 = Acceptable: sufficient support for main claims, minor points may need extra support
- 2 = Poor: main claims not sufficiently supported, major methodological problems
- 1 = Major Issues: not sufficiently thorough

**Excitement** (1-5):
- 5 = Highly Exciting
- 4 = Exciting
- 3 = Interesting
- 2 = Potentially Interesting
- 1 = Not Exciting

**Overall** (1-5):
- 5 = Consider for Award
- 4 = Conference (*ACL main)
- 3 = Findings
- 2 = Resubmit next cycle
- 1 = Do not resubmit

## Your Task

Write a thorough review focusing on **methods and experiments**. Structure your review as:

1. **Summary** (2-3 sentences)
2. **Strengths** (numbered, focus on methodological rigor, experimental design, statistical practices)
3. **Weaknesses** (numbered, focus on methodological gaps, experimental limitations, missing controls, statistical concerns)
4. **Questions for Authors** (numbered)
5. **Minor Issues** (if any)
6. **Scores**: Soundness (1-5, with 0.5 increments), Excitement (1-5), Overall (1-5)
7. **Confidence** (1-5): 1=low, 5=expert

Be specific and cite table/section numbers. Do not be overly generous or harsh — calibrate to what you'd expect at a strong *ACL venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "5599c95b-6a8c-4135-accf-709ee64db8f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T06:00:20.149Z_

```json
{
  "parentUuid": "5599c95b-6a8c-4135-accf-709ee64db8f2",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
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
  "uuid": "90d00806-6217-4aee-8e76-37d16b880182",
  "timestamp": "2026-05-21T06:00:20.149Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T06:00:23.063Z_



I'll start by loading the project files to get full context on the paper, experimental setup, and any available drafts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90d00806-6217-4aee-8e76-37d16b880182",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCn4b8WAb6MKy51bpbx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d5b672d-2ad5-4077-af94-8b4f3178dcbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SmUtoR5WCi7wgcD1zHxkDo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17283,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17283,
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

_source line 4 · 2026-05-21T06:00:23.837Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JHgWeTdaVLm84EpjA4qoVy`</summary>

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
  "parentUuid": "5d5b672d-2ad5-4077-af94-8b4f3178dcbd",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCn4b8WAb6MKy51bpbx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7848935e-6ed7-41a7-b41d-33ad23fcb517",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SmUtoR5WCi7wgcD1zHxkDo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17283,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17283,
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

_source line 5 · 2026-05-21T06:00:23.840Z_

<details><summary>↩ Tool result · `toolu_01JHgWeTdaVLm84EpjA4qoVy`</summary>

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
  "parentUuid": "7848935e-6ed7-41a7-b41d-33ad23fcb517",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "4f2a5da2-cdbf-4dcf-852c-aa43b50897fd",
  "sourceToolAssistantUUID": "7848935e-6ed7-41a7-b41d-33ad23fcb517",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T06:00:26.871Z_



Let me gather the full paper context and experimental details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f2a5da2-cdbf-4dcf-852c-aa43b50897fd",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCnM3LNg7p8oecbU1wh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "858632d7-c8bf-4dc2-ac00-04ccf35b4564",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTeMjB3sQPg4j1XzoaRT3W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1454,
      "cache_read_input_tokens": 17283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1454,
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

_source line 7 · 2026-05-21T06:00:27.311Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01V4XFF5586mtpjsy1c8yvTV`</summary>

```json
{
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "858632d7-c8bf-4dc2-ac00-04ccf35b4564",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCnM3LNg7p8oecbU1wh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15eeeb8d-a896-40d3-94b8-eff427ce5e48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTeMjB3sQPg4j1XzoaRT3W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1454,
      "cache_read_input_tokens": 17283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1454,
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

_source line 8 · 2026-05-21T06:00:27.358Z_

<details><summary>↩ Tool result · `toolu_01V4XFF5586mtpjsy1c8yvTV`</summary>

```text
{"result":"# 项目 xling_calib_direction 概况\n\n## 实验状态 (5 个)\n\n- **plan_013_probing_controls_v2**: PREPARING (failed) — \n- **plan_013**: DONE (success) — \n- **mvp_003**: DONE (success) — \n- **mvp_001**: DONE (success) — \n- **mvp_002**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan_013** (success): English correctness probes capture genuine linguistic signal: 5-fold CV with PCA(100) dimensionality reduction shows real AUROC significantly above permuted-label baseline (0.746 vs 0.484 at best layer), with selectivity (Hewitt & Liang 2019) concentrated in later layers (L20-L27), confirming the probe is not exploiting spurious high-dimensional correlations. ← 基于 mvp_001\n- **mvp_003** (success): Cross-lingual correctness direction is model-agnostic: an English-trained linear probe on Llama-3.1-8B-Instruct internal representations will transfer to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the pattern observed in Qwen2.5-7B-Instruct (mvp_001). ← 基于 mvp_001\n- **mvp_001** (success): 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性 probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在 layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp for ≥3/5 语言）。\n\n## 趋势\n成功 4 / 负向 0 / 失败 0 / 共 4\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-13176: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15eeeb8d-a896-40d3-94b8-eff427ce5e48",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "0691dbec-996a-4df4-9e58-8a272a8c1a24",
  "sourceToolAssistantUUID": "15eeeb8d-a896-40d3-94b8-eff427ce5e48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T06:00:28.348Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011ouf9i1exzKeZhvn2LnJzi`</summary>

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
  "parentUuid": "0691dbec-996a-4df4-9e58-8a272a8c1a24",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCnM3LNg7p8oecbU1wh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c3a843f-1f58-465a-8e7d-758b587cf6b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTeMjB3sQPg4j1XzoaRT3W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1454,
      "cache_read_input_tokens": 17283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1454,
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

_source line 10 · 2026-05-21T06:00:28.360Z_

<details><summary>↩ Tool result · `toolu_011ouf9i1exzKeZhvn2LnJzi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **plan_013** (success): English correctness probes capture genuine linguistic signal: 5-fold CV with PCA(100) dimensionality reduction shows real AUROC significantly above permuted-label baseline (0.746 vs 0.484 at best layer), with selectivity (Hewitt & Liang 2019) concentrated in later layers (L20-L27), confirming the probe is not exploiting spurious high-dimensional correlations. ← 基于 mvp_001\\n- **mvp_003** (success): Cross-lingual correctness direction is model-agnostic: an English-trained linear probe on Llama-3.1-8B-Instruct internal representations will transfer to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the pattern observed in Qwen2.5-7B-Instruct (mvp_001). ← 基于 mvp_001\\n- **mvp_001** (success): 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性 probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在 layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp for ≥3/5 语言）。\\n\\n## 趋势\\n成功 4 / 负向 0 / 失败 0 / 共 4\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-13176: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1201, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c3a843f-1f58-465a-8e7d-758b587cf6b3",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "3ca77dd1-d6fe-421c-b2a5-0eaff53ae746",
  "sourceToolAssistantUUID": "9c3a843f-1f58-465a-8e7d-758b587cf6b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T06:00:28.640Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Y6Wp9mrhZEwu9G3UWALbbJ`</summary>

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
  "parentUuid": "3ca77dd1-d6fe-421c-b2a5-0eaff53ae746",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCnM3LNg7p8oecbU1wh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "877ad4a4-8765-4583-ab1b-2cca6cf28001",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTeMjB3sQPg4j1XzoaRT3W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1454,
      "cache_read_input_tokens": 17283,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1454
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 268,
          "cache_read_input_tokens": 17283,
          "cache_creation_input_tokens": 1454,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1454,
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

_source line 12 · 2026-05-21T06:00:28.648Z_

<details><summary>↩ Tool result · `toolu_01Y6Wp9mrhZEwu9G3UWALbbJ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "877ad4a4-8765-4583-ab1b-2cca6cf28001",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "de5f3ca3-6256-4909-a714-3819aabb1292",
  "sourceToolAssistantUUID": "877ad4a4-8765-4583-ab1b-2cca6cf28001",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T06:00:31.687Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RUGUwKBudraoSMS2RD6sEf`</summary>

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
  "parentUuid": "de5f3ca3-6256-4909-a714-3819aabb1292",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCnh7Kzza8c66SDZQ2D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98941227-c844-44b7-ac4b-c63bf649bdf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMLPq8D5qVUPJs7WzHRo79",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1836,
      "cache_read_input_tokens": 18737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1836,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 14 · 2026-05-21T06:00:31.695Z_

<details><summary>↩ Tool result · `toolu_01RUGUwKBudraoSMS2RD6sEf`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98941227-c844-44b7-ac4b-c63bf649bdf8",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "73c25e06-a79a-496a-880f-5be40c3342d5",
  "sourceToolAssistantUUID": "98941227-c844-44b7-ac4b-c63bf649bdf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T06:00:32.666Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012JmDbFewUM6fyqZ2iJu23j`</summary>

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
  "parentUuid": "73c25e06-a79a-496a-880f-5be40c3342d5",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCnh7Kzza8c66SDZQ2D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bd5cc1a-81c8-47bc-8aa8-4f273be700b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMLPq8D5qVUPJs7WzHRo79",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1836,
      "cache_read_input_tokens": 18737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1836,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 16 · 2026-05-21T06:00:32.674Z_

<details><summary>↩ Tool result · `toolu_012JmDbFewUM6fyqZ2iJu23j`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/memory.md\", \"content\": \"# Memory\\n\\n## 2026-05-21: Simpson's Paradox in CKA-transfer relationship (D012 关键发现)\\n\\n- **发现**: CKA vs transfer AUROC 存在 Simpson's Paradox——pool 所有 layer 时弱负相关 (rho≈−0.16)，控制 depth 后符号反转为正 (Llama rho=+0.41 p=0.006, Qwen rho=+0.18 ns)\\n- **机制**: CKA 随 depth 下降，AUROC 随 depth 上升，两趋势相消产生虚假负相关。同一 depth 下，CKA 越高 → transfer 越好\\n- **意义**: 直接回应 Reviewer depth confound 质疑；符号反转本身是 publishable finding\\n- **局限**: Qwen partial rho underpowered (n=40)，per-layer n=5 只能看方向。Full-scale 20 langs 会大幅增加统计功效\\n- **决策影响**: 如 Director 确认，paper_framing 中 CKA 分析可从 \\\"suggestive correlation\\\" 升级\\n\\n## 2026-05-21: run_plan_001.sh 关键设计决策\\n\\n- **GPTQ 加载**: `--quantization none` 让 HF 自动检测 GPTQ（不用 bitsandbytes NF4）\\n- **Train/eval split**: `--split_ratio 0.7` 产出 `_train.pt`/`_eval.pt`，symlink 桥接下游脚本\\n- **Procrustes 平行配对**: for_eval/ 中 EN 必须指向 eval split（与 target 平行），已修复初始 bug\\n\\n## 2026-05-21: 模型下载路径\\n\\n- Llama4 正确路径: `/root/autodl-tmp/models/Llama4-Scout-W4A16`（不带连字符）\\n- Qwen3 路径: `/root/autodl-tmp/models/Qwen3-235B-GPTQ-Int4`\\n- 必须用 `HF_HUB_DISABLE_XET=1`（在 os.environ 中设置）+ `hf-mirror.com`\\n- `python3` 不在 PATH，用 `/root/miniconda3/bin/python3`\\n\", \"total_chars\": 1108, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bd5cc1a-81c8-47bc-8aa8-4f273be700b4",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "39f70f4a-e520-4728-9a04-0a31043f338c",
  "sourceToolAssistantUUID": "7bd5cc1a-81c8-47bc-8aa8-4f273be700b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T06:00:33.077Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Stt66nsyE4nbxn3TkNmMep`</summary>

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
  "parentUuid": "39f70f4a-e520-4728-9a04-0a31043f338c",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCnh7Kzza8c66SDZQ2D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63d92bca-1b4d-480e-9e7d-74da57bcb11a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMLPq8D5qVUPJs7WzHRo79",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1836,
      "cache_read_input_tokens": 18737,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1836
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 18737,
          "cache_creation_input_tokens": 1836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1836,
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

_source line 18 · 2026-05-21T06:00:33.091Z_

<details><summary>↩ Tool result · `toolu_01Stt66nsyE4nbxn3TkNmMep`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/ROADMAP.md\", \"content\": \"# xling_calib_direction — Research Dashboard\\n\\n> 最后更新: 2026-05-21 01:18 UTC | 更新原因: Correct model sizes (Llama4 66GB, Qwen3 122GB), revert to parallel download strategy, disk math confirms both fit\\n\\n## 核心方向\\nCross-lingual correctness probe transfer: 探索 LLM 内部 correctness direction 的跨语言可迁移性，测试 probe-based calibration 在非英语语言的可行性。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research phase — MVP 通过 (D004), Dream 审稿两轮完成 (D005→D009), P0 条件批准\\n- **MVP**: 3/3 完成 (mvp_001 ✓, mvp_002 ✓, mvp_003 ✓)\\n- **代码准备**: 全部就绪 ✅\\n  - transfer_eval.py: 5 种 transfer methods 已部署 (zero-shot, mean-shift, Procrustes, few-shot, CaCLR)\\n  - extract_activations_large.py: register_forward_hook + post-norm + 70/30 split ✅\\n  - train_caclr.py: M007 梯度修复已验证 ✅\\n- **模型下载** (并行，磁盘充足):\\n  - Llama4 Scout W4A16: ~44GB/66GB，ETA ~30-45min\\n  - Qwen3 GPTQ-Int4: ~38GB/122GB，ETA ~2-3h\\n  - 两模型合计 ~188GB，基础占用 ~88GB，总计 ~276GB/350GB = 79%\\n- **P1 先行**: plan_013 控制任务 ✅ (selectivity 0.262 at L27), plan_012 Procrustes sensitivity 运行中\\n- **关键发现**: Pareto tradeoff Qwen strong/Llama weak; mean-shift rank-invariance proof; few-shot +4.9pp AUROC over zero-shot\\n\\n## 近期任务\\n- [ ] Llama4 下载完成 (~30-45min) → 完整性验证 → dry-run → 正式审批 plan_002\\n- [ ] Qwen3 下载完成 (~2-3h) → 完整性验证 → dry-run → 正式审批 plan_001\\n- [ ] plan_002 执行: 提取激活 (12 layers × 20 langs) → 5 种 transfer eval\\n- [ ] plan_001 执行: 提取激活 (24 layers × 20 langs) → 5 种 transfer eval\\n- [ ] Procrustes sensitivity 结果收集 + CSV 完整性验证 (双进程写入风险)\\n- [ ] CPU-bound P1 (plan_011/012/013) 与 P0 并行推进\\n\\n## GPU 预算\\n- 服务器: westd-13176 (4× RTX 6000 PRO 96GB)\\n- 磁盘: /root/autodl-tmp/ 350GB total，下载完成后 ~276GB used (~74GB 余量)\\n- 激活存储策略: 先提取 Llama4 (~33GB) → 实验 → 可删模型释放 66GB → 再提取 Qwen3\\n- P0 总 GPU 预算: plan_001(80h) + plan_002(40h) + plan_003(20h) + plan_004(15h) = 155h → ~39h 墙钟\\n- 距 EACL ARR deadline (Aug 3): 74 天\\n\\n## Dream 审稿摘要 (Re-dream, D009)\\n| 档位 | 分数 | 核心反馈 |\\n|------|------|---------|\\n| Best | 4/6 WA | CaCLR underspec, CKA depth confound, arch confound, scope+controls 认可 |\\n| Median | 3/6 WR | Novelty insufficient (DA theory predicts), self-debunking less impactful |\\n| Worst | 3/6 WR | Contributions trivial/confirmatory, control task finding should be centered |\\n\\n### D009 确认行动项 (已全部执行 ✅)\\n1. CaCLR 完整实现规格 → plan_003 notes\\n2. CKA partial correlation controlling for depth → plan_011 (最关键分析)\\n3. Architecture-dependence 限定为 observational → paper_framing.md Claim 1\\n4. Control task finding 提升到 story spine → paper_framing.md\\n5. 补充引用: Zhao et al. 2019, DALI, Pires et al., Wu & Dredze → paper_framing.md\\n6. CKA: \\\"geometric/correlational analysis\\\" 非 \\\"mechanistic\\\" → paper_framing.md + plan_011\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D012 | 2026-05-21 | Novelty strategy: CKA partial correlation (plan_01 | plan_011, plan_013, plan_012 |\\n| D011 | 2026-05-21 | Revert to parallel download: Llama4 (66GB) + Qwen3 | plan_001, plan_002 |\\n| D010 | 2026-05-20 | GlobalMMLU data decisions: test 70/30 split for Ca | — |\\n| D009 | 2026-05-20 | Re-dream processed (4/3/3), P0 approved with condi | — |\\n| D008 | 2026-05-20 | Clarify P1 criterion: mvp_003 is 2/4 PASS (not 3/4 | mvp_003, mvp_001 |\\n| D007 | 2026-05-20 | mvp_003 (Llama-3.1-8B) cross-architecture validati | mvp_003, mvp_001 |\\n| D006 | 2026-05-20 | MVP gate re-evaluation after P1 leakage fix: 2/4 P | mvp_001, plan_003 |\\n| D005 | 2026-05-20 | Dream review (3/6 weak reject) processed: 13 confi | plan_003, plan_011, plan_012, plan_013 |\\n| D004 | 2026-05-20 | MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段 | mvp_001 |\\n| D003 | 2026-05-20 | P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/ | mvp_001 |\\n\\n\", \"total_chars\": 3556, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63d92bca-1b4d-480e-9e7d-74da57bcb11a",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "37c37c7a-1da1-4e83-ab59-5821568c4f39",
  "sourceToolAssistantUUID": "63d92bca-1b4d-480e-9e7d-74da57bcb11a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T06:00:35.952Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01EJREKkCM9CVqmbpPgS6myp`</summary>

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
  "parentUuid": "37c37c7a-1da1-4e83-ab59-5821568c4f39",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCo2F1yZX5s6xgu5Zye",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72e20767-c078-4c3e-86d2-0249140862e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149NXitJ5VPAUVDhhHLs9vZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3226,
      "cache_read_input_tokens": 20573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3226,
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

_source line 20 · 2026-05-21T06:00:35.961Z_

<details><summary>↩ Tool result · `toolu_01EJREKkCM9CVqmbpPgS6myp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md\", \"content\": \"# Paper Framing — xling_calib_direction\\n\\n## Target Venue\\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\\n- Core submission: 2 models × 20 languages × all contributions\\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\\n\\n## Core Insight\\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. This geometric insight, combined with the architecture-dependent depth-transferability tradeoff (strong on Qwen, weak on Llama), provides a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\\n\\n## Core Claims (4, causal chain)\\n\\n### Claim 1 — Pareto Frontier (Discovery)\\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\\n\\n### Claim 2 — Decomposition (Analysis)\\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\\n\\n### Claim 3 — CaCLR (Method / Diagnostic)\\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\\n\\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\\\"method replication to more languages\\\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\\n\\n### Key Empirical Contributions (elevated from appendix to main body, D012)\\n- **Control task methodological warning**: Hewitt & Liang selectivity analysis reveals ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold). First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\\n\\n## Story Spine\\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) ~28% of low-resource probing results are capacity artifacts (control task warning for the field); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\\n- **Headline template (method success)**: \\\"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\\\"\\n- **Headline template (negative result)**: \\\"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\\\"\\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\\n\\n## Field-Level Significance\\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\\n\\n## Anticipated Reviewer Concerns & Responses\\n1. **\\\"Xiao et al. already did this\\\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\\n2. **\\\"Temperature scaling baseline\\\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\\n3. **\\\"Mean-shift too weak / why does it fail?\\\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\\n4. **\\\"Difficulty confound\\\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\\n5. **\\\"INT8 artifacts\\\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\\n6. **\\\"Only MCQA\\\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\\n7. **\\\"Predictable from domain adaptation theory\\\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\\n8. **\\\"No statistical tests\\\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\\n9. **\\\"Probing methodology concerns\\\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\\n10. **\\\"No mechanistic explanation\\\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \\\"geometric analysis\\\" not \\\"mechanistic explanation.\\\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\\n11. **\\\"Why not conformal prediction?\\\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\\n12. **\\\"CaCLR parallel activations = test leakage?\\\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\\n13. **\\\"CaCLR is your own method — self-debunking is less impactful\\\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\\n14. **\\\"CKA is correlational, not mechanistic\\\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\\n\\n## Additional Related Work Coverage (Dream-identified gaps)\\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \\\"On learning invariant representations for domain adaptation\\\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\\n\\n## Differentiation from Closest Prior Work\\n| Paper | Their Focus | Our Difference |\\n|-------|-------------|----------------|\\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\\n\", \"total_chars\": 17679, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72e20767-c078-4c3e-86d2-0249140862e0",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "eb01ef08-e92b-49c3-87d9-ee727f0cc2ac",
  "sourceToolAssistantUUID": "72e20767-c078-4c3e-86d2-0249140862e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T06:00:36.531Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01W9YycvgcZi1FLsNt44EaRC`</summary>

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
  "parentUuid": "eb01ef08-e92b-49c3-87d9-ee727f0cc2ac",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCo2F1yZX5s6xgu5Zye",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d81698e1-ea6d-40bb-8850-6ffbee35a381",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149NXitJ5VPAUVDhhHLs9vZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3226,
      "cache_read_input_tokens": 20573,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3226
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 20573,
          "cache_creation_input_tokens": 3226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3226,
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

_source line 22 · 2026-05-21T06:00:36.546Z_

<details><summary>↩ Tool result · `toolu_01W9YycvgcZi1FLsNt44EaRC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/decisions.yaml\", \"content\": \"_next_id: 13\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 13:49 UTC\\n  summary: MVP 用 7-8B 模型验证核心假设，不直接上 235B\\n  rationale: 核心假设（correctness probe 跨语言迁移 + layer-depth 效应）在 7-8B 模型上有充分先验（Miao &\\n    Ungar、Civelli 等均用 7-8B）。若 7B 无效应则整个方向不成立。7B 仅需 1 GPU × 2-4h，快速验证后再决定是否投入 235B\\n    的大资源。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 13:53 UTC\\n  summary: MVP 模型固定为 Qwen2.5-7B-Instruct\\n  rationale: 与正式实验 Qwen3-235B 同属 Qwen 家族，架构连续性最好。Civelli et al. 报告 Qwen3-8B 最优迁移深度为\\n    24%，可为正式实验提供直接参考。Reviewer 建议明确选一个并记录理由。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-20 18:25 UTC\\n  summary: P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/5 语言\\n  rationale: Mean-shift 是常数偏移，不改变 AUROC（rank-invariant）。Mean-shift 的设计目的是改善 calibration（概率准确性），应用\\n    ECE/Brier 衡量。同时 P1 ECE 阈值维持 0.15 但允许 temperature scaling 后重测。\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: trigger\\n    result: P4 ΔAUROC=0 暴露标准设计缺陷\\n  depends_on: []\\n- id: D004\\n  date: 2026-05-20 18:52 UTC\\n  summary: 'MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段'\\n  rationale: P1(AUROC=0.754+ECE=0.074 temp-scaled) / P2(4/5语言迁移) / P3(14.3pp depth\\n    effect) 全部 PASS。P4(mean-shift) FAIL 但属于 alignment baseline 方法失败，不否定核心假设。Mean-shift\\n    失败是有价值的 negative result：(1) 区分于 Xiao et al. 在 knowledge boundary 上 mean-shift\\n    成功；(2) motivate CaCLR 方法。额外发现：L27 英语最强但迁移退化 vs L24——直接观测到 Pareto tradeoff，是论文核心贡献的前兆。\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: primary\\n    result: P1✅P2✅P3✅P4❌, core hypothesis supported\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-20 20:14 UTC\\n  summary: 'Dream review (3/6 weak reject) processed: 13 confirmed actions, 5 observations,\\n    3 ignores. Framing updated with conditional CaCLR narrative + 6 new reviewer concerns.\\n    3 new P1 experiments added (CKA, linproj sensitivity, control tasks). Proceeding\\n    with re-dream after changes.'\\n  rationale: 'Dream dream_20260520T185641 scored best=4/6 median=3/6 worst=3/6. Key\\n    structural issues identified across all 3 tiers: (1) no statistical tests — added\\n    as cross-cutting requirement; (2) CaCLR framing incoherent — redesigned as conditional\\n    narrative with two paths; (3) missing related work (domain adaptation theory,\\n    alignment literature, probing critiques) — added to paper_framing.md. Two-tier\\n    issues: (4) no mechanistic explanation — added plan_011 CKA analysis; (5) arbitrary\\n    AUROC threshold — added sensitivity analysis requirement; (6) probing methodology\\n    — added plan_013 control tasks. CaCLR consistency loss value is the key data-dependent\\n    risk (O3). Core 4-claim structure preserved; framing strengthened not weakened.\\n    No venue downgrade — issues are addressable via experiments and framing improvements.'\\n  related_experiments:\\n  - exp_id: plan_003\\n    role: affected\\n    result: CaCLR conditional narrative added\\n  - exp_id: plan_011\\n    role: new\\n    result: CKA mechanistic analysis (P1, 5 GPU-hrs)\\n  - exp_id: plan_012\\n    role: new\\n    result: Linear projection sensitivity (P1, 2 GPU-hrs)\\n  - exp_id: plan_013\\n    role: new\\n    result: Probing control tasks (P1, 2 GPU-hrs)\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-20 20:23 UTC\\n  summary: 'MVP gate re-evaluation after P1 leakage fix: 2/4 PASS, still proceed to\\n    research phase'\\n  rationale: 'M005 reveals temp scaling data leakage — P1 ECE now FAIL (0.2216 > 0.15).\\n    Gate drops from 3/4 to 2/4 PASS. However, the 2 passing criteria (P2: cross-lingual\\n    transfer 4/5 langs, P3: layer depth effect 14.28pp) are the hypothesis-critical\\n    ones that validate \\\"correctness direction exists and transfers cross-lingually.\\\"\\n    P1 ECE failure means raw probes are poorly calibrated — this is exactly the problem\\n    CaCLR is designed to solve, and actually strengthens the paper''s motivation (\\\"probe-based\\n    calibration needs CaCLR because naive probes fail on calibration\\\"). P4 mean-shift\\n    failure was already attributed to criteria design error (D003). Research phase\\n    continues with strengthened CaCLR motivation. The 0.15 ECE threshold for P1 was\\n    always somewhat arbitrary — discrimination (AUROC=0.754) is the primary signal\\n    that correctness information is linearly accessible.'\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: gate_check\\n    result: 2/4 PASS (P2+P3), P1 ECE FAIL after leakage fix\\n  - exp_id: plan_003\\n    role: motivated_by\\n    result: CaCLR motivation strengthened by raw probe calibration failure\\n  depends_on:\\n  - D004\\n  - D005\\n- id: D007\\n  date: 2026-05-20 20:31 UTC\\n  summary: 'mvp_003 (Llama-3.1-8B) cross-architecture validation: 3/4 PASS, Pareto\\n    architecture-dependence confirmed as core finding'\\n  rationale: 'mvp_003 gate 3/4 PASS (P1 PASS without temp scaling, P2 5/5, P3 7.85pp,\\n    P4 FAIL). Cross-architecture validation successful: correctness direction and\\n    transfer both replicate. Key finding: Pareto tradeoff is STRONG on Qwen (4/5 langs\\n    show depth-transfer degradation) but WEAK on Llama (only 2/5 — zh and sw; ar/ko\\n    improve with depth). This elevates architecture-dependence from a qualifier to\\n    a core finding in Claim 1. CKA pilot shows same two-model contrast. Swahili is\\n    model-dependent (fails Qwen, passes Llama). zh@L31 mean-shift anomaly flagged\\n    for investigation.'\\n  related_experiments:\\n  - exp_id: mvp_003\\n    role: validation\\n    result: 3/4 PASS, weak Pareto on Llama\\n  - exp_id: mvp_001\\n    role: comparison\\n    result: 2/4 PASS (post-fix), strong Pareto on Qwen\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-20 20:40 UTC\\n  summary: 'Clarify P1 criterion: mvp_003 is 2/4 PASS (not 3/4), consistent with mvp_001.\\n    P1 evaluated at best-AUROC layer.'\\n  rationale: 'Reviewer pointed out D007 ambiguity: P1 passes at L0 (AUROC=0.650, ECE=0.148)\\n    but fails at best-AUROC layer L31 (AUROC=0.728, ECE=0.205). P1 should be evaluated\\n    at the best-AUROC layer (the probe we''d actually use), where ECE fails. Both\\n    models are now 2/4 PASS (P2+P3). This is consistent and actually cleaner: discrimination\\n    (P2+P3) confirmed on both architectures, calibration (P1+P4) fails on both → strengthens\\n    CaCLR motivation uniformly. No impact on research phase decision (D006).'\\n  related_experiments:\\n  - exp_id: mvp_003\\n    role: clarification\\n    result: 2/4 PASS (P2+P3), not 3/4\\n  - exp_id: mvp_001\\n    role: comparison\\n    result: 2/4 PASS (P2+P3), consistent\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-20 21:27 UTC\\n  summary: Re-dream processed (4/3/3), P0 approved with conditions — 6 confirmed action\\n    items integrated into framing+plan\\n  rationale: 'Re-dream scores: best=4/6 (Weak Accept) ✓, median=3/6 (Weak Reject =\\n    borderline), worst=3/6. All simulated quality. Scores unchanged from first dream\\n    despite acknowledged framing improvements — remaining issues are (1) implementation-level\\n    (CaCLR specs, CKA partial correlation) addressable in experiment execution, and\\n    (2) novelty concerns inherent to negative-result scenario that only resolve with\\n    real data. Blocking P0 further would waste time without improving situation. 6\\n    confirmed action items: A1-CaCLR complete implementation spec required, A2-CKA\\n    partial correlation controlling for depth mandatory, A3-architecture claim qualified\\n    as observational, A4-control task finding elevated in story, A5-missing references\\n    added (Zhao et al. 2019, DALI, Pires et al.), A6-CKA framed as geometric/correlational\\n    not mechanistic. 7 observation items tracked for real experiment validation. P0\\n    approved conditional on code blockers resolved (transfer_eval.py, extract_activations_large.py).'\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D010\\n  date: 2026-05-20 21:58 UTC\\n  summary: 'GlobalMMLU data decisions: test 70/30 split for CaCLR (no train split\\n    exists); th→te language swap'\\n  rationale: 'GlobalMMLU has only test (14042/lang) and dev (285/lang) splits, no\\n    train split. plan_003 assumed train split for CaCLR parallel activations. Fix:\\n    partition test 70/30 stratified into probe_train and eval. probe_train for BCE\\n    labels + MMD parallel activations; eval for all metrics. 4200 eval samples sufficient.\\n    dev too small (285) for MMD. Thai not in GlobalMMLU; replaced with Telugu (te)\\n    to add Dravidian family coverage (currently missing language family).'\\n  related_experiments: []\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-21 01:18 UTC\\n  summary: 'Revert to parallel download: Llama4 (66GB) + Qwen3 (122GB) both fit on\\n    disk (276GB/350GB)'\\n  rationale: 'Agent initially reported Qwen3=208GB and Llama4=103GB, triggering serial\\n    strategy. Reviewer verified actual sizes: Llama4 W4A16 = 14×4.7GB = 66GB, Qwen3\\n    GPTQ-Int4 = 32×3.8GB = 122GB. Total 188GB + 88GB baseline = 276GB/350GB (79%).\\n    Parallel download saves 2-3h. Activation storage handled sequentially: extract\\n    Llama4 first, delete model, then extract Qwen3.'\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: gated_by\\n  - exp_id: plan_002\\n    role: gated_by\\n  depends_on:\\n  - D009\\n- id: D012\\n  date: 2026-05-21 03:56 UTC\\n  summary: 'Novelty strategy: CKA partial correlation (plan_011) is the pivot point;\\n    Claim 4 downgrade to subsection; control task finding + projection efficiency\\n    elevated to main body'\\n  rationale: 'Reviewer independent assessment: CKA partial correlation controlling\\n    for depth is the single highest-impact novelty lever (+0.5 if significant). Control\\n    task finding (+0.3) and projection sample efficiency (+0.2) are certain improvements.\\n    Claim 4 (orthogonality) has weakest standalone novelty, should be subsection to\\n    free space. Pareto formalization doesn''t improve novelty score. Best case 2.5→3.5-4.0,\\n    conservative 2.5→3.0.'\\n  related_experiments:\\n  - exp_id: plan_011\\n    role: pivot_point\\n  - exp_id: plan_013\\n    role: elevate_finding\\n  - exp_id: plan_012\\n    role: elevate_finding\\n  depends_on:\\n  - D009\\n\", \"total_chars\": 9902, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d81698e1-ea6d-40bb-8850-6ffbee35a381",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "2f46cf60-8501-473c-b2fa-eaabd02f6faf",
  "sourceToolAssistantUUID": "d81698e1-ea6d-40bb-8850-6ffbee35a381",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-21T06:00:40.286Z_

Now let me look at the actual experiment artifacts and code to understand the methodology more deeply.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f46cf60-8501-473c-b2fa-eaabd02f6faf",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCoH6Uv9AGnaEZPeVE5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fdfccda4-c156-4343-aae6-b0f4bdd8b955",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NTW8VW5JNMtAKifjeB5vJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8696,
      "cache_read_input_tokens": 23799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8696,
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

_source line 24 · 2026-05-21T06:00:41.253Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01B2oaCvgPkX9hY8M73gyrnZ`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdfccda4-c156-4343-aae6-b0f4bdd8b955",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCoH6Uv9AGnaEZPeVE5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ad75c1e-fbfa-4a44-a90f-cdc8715a4008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NTW8VW5JNMtAKifjeB5vJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8696,
      "cache_read_input_tokens": 23799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8696,
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

_source line 25 · 2026-05-21T06:00:41.266Z_

<details><summary>↩ Tool result · `toolu_01B2oaCvgPkX9hY8M73gyrnZ`</summary>

```text
code/extract_activations.py
code/analyze_results.py
code/train_probe.py
code/train_caclr.py
code/extract_activations_large.py
code/transfer_eval.py
code/compute_cka.py
code/pareto_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ad75c1e-fbfa-4a44-a90f-cdc8715a4008",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "a7e6783d-d8b2-41d1-883a-639d7d1dbbbf",
  "sourceToolAssistantUUID": "6ad75c1e-fbfa-4a44-a90f-cdc8715a4008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T06:00:41.746Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Wn77ZutPYmrLPFmNGwtCEm`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7e6783d-d8b2-41d1-883a-639d7d1dbbbf",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCoH6Uv9AGnaEZPeVE5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59aeaa40-691f-432f-8059-683f983ce177",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NTW8VW5JNMtAKifjeB5vJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8696,
      "cache_read_input_tokens": 23799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8696,
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

_source line 27 · 2026-05-21T06:00:41.756Z_

<details><summary>↩ Tool result · `toolu_01Wn77ZutPYmrLPFmNGwtCEm`</summary>

```text
artifacts/dream_reports/dream_20260520T185641/best/paper_framing.md
artifacts/dream_reports/dream_20260520T185641/median/paper_framing.md
artifacts/dream_reports/dream_20260520T185641/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T185641/median/review_report.md
artifacts/dream_reports/dream_20260520T185641/best/review_report.md
artifacts/dream_reports/dream_20260520T185641/worst/review_report.md
artifacts/review_reports/round_0.md
artifacts/_project/report/cka_vs_degradation_report.md
artifacts/dream_reports/dream_20260520T201854/best/paper_framing.md
artifacts/dream_reports/dream_20260520T201854/median/paper_framing.md
artifacts/dream_reports/dream_20260520T201854/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T201854/median/review_report.md
artifacts/dream_reports/dream_20260520T201854/best/review_report.md
artifacts/dream_reports/dream_20260520T201854/worst/review_report.md
artifacts/kill_qwen3_status.md
artifacts/qwen3_size_check.md
artifacts/download_restart_pids.md
artifacts/download_fix_result.md
artifacts/compute_cka_verified.md
artifacts/download_progress_plan002.md
artifacts/dream_reports/dream_20260521T032808/best/paper_framing.md
artifacts/dream_reports/dream_20260521T032808/median/paper_framing.md
artifacts/dream_reports/dream_20260521T032808/worst/paper_framing.md
artifacts/cka_mvp_full_results.md
artifacts/partial_correlation_pilot.md
artifacts/pareto_analysis_verified.md
artifacts/dream_reports/dream_20260521T032808/best/review_report.md
artifacts/dream_reports/dream_20260521T032808/median/review_report.md
artifacts/dream_reports/dream_20260521T032808/worst/review_report.md
artifacts/dream_reports/dream_20260521T044911/best/paper_framing.md
artifacts/dream_reports/dream_20260521T044911/median/paper_framing.md
artifacts/dream_reports/dream_20260521T044911/worst/paper_framing.md
artifacts/dream_reports/dream_20260521T044911/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59aeaa40-691f-432f-8059-683f983ce177",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "34d743b1-c681-41f0-9c63-33880d8f079e",
  "sourceToolAssistantUUID": "59aeaa40-691f-432f-8059-683f983ce177",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T06:00:42.376Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Wxyy1xWjJJvFUmiZtG5zMc`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34d743b1-c681-41f0-9c63-33880d8f079e",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCoH6Uv9AGnaEZPeVE5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b34a3fa9-313d-468d-a765-cecab8f989a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NTW8VW5JNMtAKifjeB5vJ7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8696,
      "cache_read_input_tokens": 23799,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8696
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 23799,
          "cache_creation_input_tokens": 8696,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8696,
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

_source line 29 · 2026-05-21T06:00:42.388Z_

<details><summary>↩ Tool result · `toolu_01Wxyy1xWjJJvFUmiZtG5zMc`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b34a3fa9-313d-468d-a765-cecab8f989a3",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "b95312e2-eb79-4ac3-a25e-b15028410f88",
  "sourceToolAssistantUUID": "b34a3fa9-313d-468d-a765-cecab8f989a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T06:00:45.304Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R5GfT8kmcgkDDLsMiD712Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/transfer_eval.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b95312e2-eb79-4ac3-a25e-b15028410f88",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCoi1SD4pEtgmoGw1U6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86bb887b-992a-4ad3-ae15-e1f040429562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zDwd8VkMX4pUemfghNwE6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1161,
      "cache_read_input_tokens": 32495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1161,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 31 · 2026-05-21T06:00:45.309Z_

<details><summary>↩ Tool result · `toolu_01R5GfT8kmcgkDDLsMiD712Q`</summary>

```text
1	"""
2	Evaluate cross-lingual transfer of English correctness probes.
3	
4	Three transfer conditions:
5	  (a) Zero-shot: apply English probe directly to target-language activations
6	  (b) Mean-shift: shift target activations by (mean_en - mean_tgt) before probing
7	  (c) Linear projection (Procrustes): learn orthogonal W from parallel pairs,
8	      transform X_tgt' = (X_tgt - mu_tgt) @ W + mu_en, then probe
9	
10	Input:  English probes (.pkl) + per-language activations (.pt)
11	Output: transfer_results.csv with AUROC / ECE / Brier per (layer, language, method)
12	
13	Usage:
14	  python transfer_eval.py \
15	    --activations_dir ./activations \
16	    --probes_dir ./probes \
17	    --output_dir ./results \
18	    --layers 0,4,8,12,16,20,24,28,31 \
19	    --languages zh ar hi sw ko \
20	    --n_proj_pairs 100
21	"""
22	
23	import argparse
24	import os
25	import pickle
26	
27	import numpy as np
28	import torch
29	from scipy.linalg import orthogonal_procrustes
30	from sklearn.linear_model import LogisticRegression
31	from sklearn.metrics import roc_auc_score, brier_score_loss
32	from sklearn.preprocessing import StandardScaler
33	
34	
35	def parse_args():
36	    p = argparse.ArgumentParser()
37	    p.add_argument("--activations_dir", default="./activations")
38	    p.add_argument("--probes_dir", default="./probes")
39	    p.add_argument("--output_dir", default="./results")
40	    p.add_argument("--layers", default=None,
41	                   help="Comma-separated layer indices. Default: auto-detect from activations_dir")
42	    p.add_argument("--languages", nargs="+", default=["zh", "ar", "hi", "sw", "ko"])
43	    p.add_argument("--n_perm", type=int, default=1000,
44	                   help="Number of permutations for significance test")
45	    p.add_argument("--n_proj_pairs", type=int, default=0,
46	                   help="Number of parallel pairs for linear projection. 0 = skip projection.")
47	    p.add_argument("--proj_seed", type=int, default=42,
48	                   help="Random seed for sampling parallel pairs")
49	    p.add_argument("--n_few_shot", default=None,
50	                   help="Comma-separated few-shot counts, e.g. '25,100'. 0 or omit = skip.")
51	    return p.parse_args()
52	
53	
54	def compute_ece(probs, labels, n_bins=10):
55	    """Histogram-based ECE."""
56	    bin_edges = np.linspace(0, 1, n_bins + 1)
57	    ece = 0.0
58	    for lo, hi in zip(bin_edges[:-1], bin_edges[1:]):
59	        mask = (probs > lo) & (probs <= hi)
60	        if lo == 0.0:
61	            mask = (probs >= lo) & (probs <= hi)
62	        n_in_bin = mask.sum()
63	        if n_in_bin == 0:
64	            continue
65	        ece += (n_in_bin / len(probs)) * abs(labels[mask].mean() - probs[mask].mean())
66	    return ece
67	
68	
69	def permutation_test_auroc(y_true, y_score, n_perm=1000, seed=42):
70	    """One-sided permutation test: is AUROC significantly above chance?"""
71	    rng = np.random.RandomState(seed)
72	    real_auroc = roc_auc_score(y_true, y_score)
73	    count_ge = 0
74	    for _ in range(n_perm):
75	        perm_auroc = roc_auc_score(rng.permutation(y_true), y_score)
76	        if perm_auroc >= real_auroc:
77	            count_ge += 1
78	    return (count_ge + 1) / (n_perm + 1)
79	
80	
81	def evaluate_probe(probe, scaler, X, y, n_perm=1000):
82	    """Apply probe and compute metrics. Returns (auroc, ece, brier, p_value, probs)."""
83	    X_s = scaler.transform(X)
84	    probs = probe.predict_proba(X_s)[:, 1]
85	    logits = probe.decision_function(X_s)
86	
87	    if len(np.unique(y)) < 2:
88	        return None, None, None, None, probs
89	
90	    auroc = roc_auc_score(y, logits)
91	    ece = compute_ece(probs, y)
92	    brier = brier_score_loss(y, probs)
93	    p_value = permutation_test_auroc(y, logits, n_perm=n_perm)
94	    return auroc, ece, brier, p_value, probs
95	
96	
97	def procrustes_align(X_en_pairs, X_tgt_pairs, X_tgt_all):
98	    """Align target activations to English space via orthogonal Procrustes.
99	
100	    Learns orthogonal W from N parallel pairs such that X_tgt @ W ≈ X_en (after centering).
101	    Consistent with cross-lingual alignment literature (VecMap/MUSE).
102	
103	    Args:
104	        X_en_pairs: (N, D) English activations for parallel items
105	        X_tgt_pairs: (N, D) Target activations for the same items
106	        X_tgt_all: (M, D) All target activations to transform
107	
108	    Returns:
109	        X_aligned: (M, D) Transformed target activations in English space
110	    """
111	    mu_en = X_en_pairs.mean(axis=0)
112	    mu_tgt = X_tgt_pairs.mean(axis=0)
113	    X_en_c = X_en_pairs - mu_en
114	    X_tgt_c = X_tgt_pairs - mu_tgt
115	    W, _ = orthogonal_procrustes(X_tgt_c, X_en_c)
116	    return (X_tgt_all - mu_tgt) @ W + mu_en
117	
118	
119	def main():
120	    args = parse_args()
121	    if args.layers is None:
122	        import glob
123	        available = sorted(set(
124	            int(os.path.basename(f).split('_')[0].replace('layer', ''))
125	            for f in glob.glob(os.path.join(args.activations_dir, 'layer*_en.pt'))
126	        ))
127	        if not available:
128	            raise RuntimeError(f"No layer*_en.pt files found in {args.activations_dir}")
129	        print(f"Auto-detected layers: {available}")
130	        layer_indices = available
131	    else:
132	        layer_indices = sorted(int(x) for x in args.layers.split(","))
133	    os.makedirs(args.output_dir, exist_ok=True)
134	
135	    results = []
136	
137	    def _fmt(v):
138	        return f"{v:.4f}" if v is not None else "  N/A "
139	
140	    print(f"{'Layer':>5s} {'Lang':>4s} {'Method':>10s} {'AUROC':>7s} {'ECE':>7s} {'Brier':>7s} {'p':>7s} {'N':>6s}")
141	    print("-" * 60)
142	
143	    for li in layer_indices:
144	        probe_path = os.path.join(args.probes_dir, f"probe_layer{li}.pkl")
145	        if not os.path.exists(probe_path):
146	            print(f"  [SKIP] No probe for layer {li}")
147	            continue
148	
149	        with open(probe_path, "rb") as f:
150	            saved = pickle.load(f)
151	        probe = saved["model"]
152	        scaler = saved["scaler"]
153	
154	        en_pt = os.path.join(args.activations_dir, f"layer{li}_en.pt")
155	        if not os.path.exists(en_pt):
156	            print(f"  [SKIP] No English activations for layer {li}")
157	            continue
158	        en_data = torch.load(en_pt, weights_only=True)
159	        en_mean = en_data["activations"].numpy().mean(axis=0)
160	
161	        for lang in args.languages:
162	            tgt_pt = os.path.join(args.activations_dir, f"layer{li}_{lang}.pt")
163	            if not os.path.exists(tgt_pt):
164	                print(f"  [SKIP] No activations for layer {li}, lang {lang}")
165	                continue
166	
167	            tgt_data = torch.load(tgt_pt, weights_only=True)
168	            X_tgt = tgt_data["activations"].numpy()
169	            y_tgt = tgt_data["labels"].numpy()
170	            n_samples = len(y_tgt)
171	
172	            # (a) Zero-shot
173	            auroc, ece, brier, pval, _ = evaluate_probe(probe, scaler, X_tgt, y_tgt, n_perm=args.n_perm)
174	            row = {"layer": li, "language": lang, "method": "zero_shot",
175	                   "auroc": auroc, "ece": ece, "brier": brier, "p_value": pval, "n": n_samples}
176	            results.append(row)
177	            print(f"{li:>5d} {lang:>4s} {'zero_shot':>10s} {_fmt(auroc):>7s} {_fmt(ece):>7s} {_fmt(brier):>7s} {_fmt(pval):>7s} {n_samples:>6d}")
178	
179	            # (b) Mean-shift: X_shifted = X_tgt - (mean_tgt - mean_en)
180	            tgt_mean = X_tgt.mean(axis=0)
181	            X_shifted = X_tgt - (tgt_mean - en_mean)
182	            auroc, ece, brier, pval, _ = evaluate_probe(probe, scaler, X_shifted, y_tgt, n_perm=args.n_perm)
183	            row = {"layer": li, "language": lang, "method": "mean_shift",
184	                   "auroc": auroc, "ece": ece, "brier": brier, "p_value": pval, "n": n_samples}
185	            results.append(row)
186	            print(f"{li:>5d} {lang:>4s} {'mean_shift':>10s} {_fmt(auroc):>7s} {_fmt(ece):>7s} {_fmt(brier):>7s} {_fmt(pval):>7s} {n_samples:>6d}")
187	
188	            # (c) Linear projection (Procrustes): orthogonal alignment from parallel pairs
189	            if args.n_proj_pairs > 0:
190	                X_en_all = en_data["activations"].numpy()
191	                n_pairs = min(args.n_proj_pairs, len(X_en_all), len(X_tgt))
192	                rng = np.random.RandomState(args.proj_seed)
193	                pair_idx = rng.choice(min(len(X_en_all), len(X_tgt)), size=n_pairs, replace=False)
194	                X_aligned = procrustes_align(X_en_all[pair_idx], X_tgt[pair_idx], X_tgt)
195	                auroc, ece, brier, pval, _ = evaluate_probe(probe, scaler, X_aligned, y_tgt, n_perm=args.n_perm)
196	                row = {"layer": li, "language": lang, "method": f"procrustes_{n_pairs}",
197	                       "auroc": auroc, "ece": ece, "brier": brier, "p_value": pval, "n": n_samples}
198	                results.append(row)
199	                print(f"{li:>5d} {lang:>4s} {f'proc_{n_pairs}':>10s} {_fmt(auroc):>7s} {_fmt(ece):>7s} {_fmt(brier):>7s} {_fmt(pval):>7s} {n_samples:>6d}")
200	
201	            # (d) Few-shot: retrain probe with English + N target-language samples
202	            if args.n_few_shot:
203	                for n_fs in [int(x) for x in args.n_few_shot.split(",")]:
204	                    if n_fs >= len(y_tgt):
205	                        print(f"  [SKIP] n_few_shot={n_fs} >= target samples ({len(y_tgt)})")
206	                        continue
207	
208	                    rng_fs = np.random.RandomState(args.proj_seed)
209	                    fs_idx = rng_fs.choice(len(y_tgt), size=n_fs, replace=False)
210	                    eval_mask = np.ones(len(y_tgt), dtype=bool)
211	                    eval_mask[fs_idx] = False
212	
213	                    X_fs = X_tgt[fs_idx]
214	                    y_fs = y_tgt[fs_idx]
215	                    X_eval = X_tgt[eval_mask]
216	                    y_eval = y_tgt[eval_mask]
217	
218	                    X_en_all = en_data["activations"].numpy()
219	                    y_en_all = en_data["labels"].numpy()
220	
221	                    X_combined = np.concatenate([X_en_all, X_fs])
222	                    y_combined = np.concatenate([y_en_all, y_fs])
223	
224	                    scaler_fs = StandardScaler()
225	                    X_combined_s = scaler_fs.fit_transform(X_combined)
226	                    clf_fs = LogisticRegression(C=1.0, penalty="l2", solver="lbfgs",
227	                                                max_iter=2000, random_state=42)
228	                    clf_fs.fit(X_combined_s, y_combined)
229	
230	                    auroc, ece, brier, pval, _ = evaluate_probe(clf_fs, scaler_fs, X_eval, y_eval, n_perm=args.n_perm)
231	                    method_name = f"few_shot_{n_fs}"
232	                    n_eval = len(y_eval)
233	                    row = {"layer": li, "language": lang, "method": method_name,
234	                           "auroc": auroc, "ece": ece, "brier": brier, "p_value": pval, "n": n_eval}
235	                    results.append(row)
236	                    print(f"{li:>5d} {lang:>4s} {method_name:>10s} {_fmt(auroc):>7s} {_fmt(ece):>7s} {_fmt(brier):>7s} {_fmt(pval):>7s} {n_eval:>6d}")
237	
238	    csv_path = os.path.join(args.output_dir, "transfer_results.csv")
239	    with open(csv_path, "w") as f:
240	        f.write("layer,language,method,auroc,ece,brier,p_value,n\n")
241	        for r in results:
242	            vals = []
243	            for k in ["auroc", "ece", "brier", "p_value"]:
244	                vals.append(f"{r[k]:.6f}" if r[k] is not None else "")
245	            f.write(f"{r['layer']},{r['language']},{r['method']},{','.join(vals)},{r['n']}\n")
246	
247	    print(f"\nResults saved to {csv_path}")
248	
249	
250	if __name__ == "__main__":
251	    main()
252	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86bb887b-992a-4ad3-ae15-e1f040429562",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "4e22bb41-d4d0-494d-bfea-f7ff79354866",
  "sourceToolAssistantUUID": "86bb887b-992a-4ad3-ae15-e1f040429562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T06:00:45.743Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A2PUXqqPdDENCBrruF7GKS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/train_caclr.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e22bb41-d4d0-494d-bfea-f7ff79354866",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCoi1SD4pEtgmoGw1U6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ccc444a-fe1a-4a89-b4a0-4a5829afc671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zDwd8VkMX4pUemfghNwE6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1161,
      "cache_read_input_tokens": 32495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1161,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 33 · 2026-05-21T06:00:45.749Z_

<details><summary>↩ Tool result · `toolu_01A2PUXqqPdDENCBrruF7GKS`</summary>

```text
1	"""
2	CaCLR: Calibration-aware Cross-Lingual Regularization.
3	
4	Train a linear probe with two additional regularization terms beyond BCE:
5	  Loss = L_BCE + α · L_SB-ECE + β · L_consistency(MMD)
6	
7	  - L_SB-ECE: differentiable soft-binning ECE (calibration regularizer)
8	  - L_consistency: MMD with Gaussian RBF kernel (cross-lingual consistency)
9	
10	Input:  per-language activation .pt files from extract_activations.py
11	        (each file has {"activations": Tensor, "labels": Tensor})
12	Output: trained probe .pkl compatible with transfer_eval.py
13	        (pickle dict with {"model": CaCLRProbe, "scaler": StandardScaler, ...})
14	
15	Usage:
16	  # Single run
17	  python train_caclr.py \
18	    --activations_dir ./activations --output_dir ./probes_caclr \
19	    --layer 16 --languages zh ar hi sw ko --alpha 1.0 --beta 0.1
20	
21	  # Sweep over α × β
22	  python train_caclr.py \
23	    --activations_dir ./activations --output_dir ./probes_caclr \
24	    --layer 16 --languages zh ar hi sw ko \
25	    --alpha_sweep 0.01,0.1,0.5,1.0,2.0,5.0,10.0 \
26	    --beta_sweep 0.001,0.01,0.05,0.1,0.5,1.0
27	"""
28	
29	import argparse
30	import os
31	import pickle
32	from itertools import product
33	
34	import numpy as np
35	import torch
36	import torch.nn as nn
37	import torch.nn.functional as F
38	from sklearn.linear_model import LogisticRegression
39	from sklearn.model_selection import train_test_split
40	from sklearn.preprocessing import StandardScaler
41	from sklearn.metrics import roc_auc_score, brier_score_loss
42	
43	
44	# ---------------------------------------------------------------------------
45	# Loss components
46	# ---------------------------------------------------------------------------
47	
48	def bce_loss(logits, labels):
49	    """Standard binary cross-entropy on probe logits."""
50	    return F.binary_cross_entropy_with_logits(logits, labels)
51	
52	
53	def sb_ece_loss(probs, labels, n_bins=10, temperature=0.05):
54	    """Differentiable soft-binning ECE approximation.
55	
56	    Hard-histogram ECE is non-differentiable. We replace indicator-based bin
57	    assignment with Gaussian soft assignment:
58	      bin centers c_k = (k + 0.5) / n_bins,  k = 0, ..., n_bins-1
59	      weights  w_{ik} = softmax( -|p_i - c_k|^2 / temperature )
60	
61	    Per-bin calibration error:
62	      CE_k = | Σ_i w_{ik} * (label_i - p_i) | / (Σ_i w_{ik} + ε)
63	
64	    SB-ECE = Σ_k (Σ_i w_{ik} / N) * CE_k
65	    """
66	    centers = torch.linspace(0.5 / n_bins, 1.0 - 0.5 / n_bins, n_bins,
67	                             device=probs.device)                          # (K,)
68	    # Pairwise distances: (N, K)
69	    dists = (probs.unsqueeze(1) - centers.unsqueeze(0)) ** 2               # (N, K)
70	    weights = F.softmax(-dists / temperature, dim=1)                       # (N, K)
71	
72	    bin_counts = weights.sum(dim=0)                                        # (K,)
73	    # Weighted calibration gap per bin
74	    gap = labels.unsqueeze(1) - probs.unsqueeze(1)                         # (N, K) broadcast
75	    weighted_gap = (weights * gap).sum(dim=0)                              # (K,)
76	    per_bin_ce = weighted_gap.abs() / (bin_counts + 1e-8)
77	
78	    ece = (bin_counts / probs.shape[0] * per_bin_ce).sum()
79	    return ece
80	
81	
82	def gaussian_rbf_kernel(x, y, bandwidth=None):
83	    """Gaussian RBF kernel matrix.
84	
85	    k(x, y) = exp( -||x - y||^2 / (2 * bandwidth^2) )
86	
87	    If bandwidth is None, uses the median heuristic:
88	      bandwidth = sqrt( median(||x_i - y_j||^2) / 2 )
89	    """
90	    xx = torch.cdist(x, x) ** 2    # (N, N)
91	    yy = torch.cdist(y, y) ** 2    # (M, M)
92	    xy = torch.cdist(x, y) ** 2    # (N, M)
93	
94	    if bandwidth is None:
95	        # Median heuristic over cross-distances
96	        all_dists = xy.detach().reshape(-1)
97	        median_dist = all_dists.median()
98	        bandwidth = torch.sqrt(median_dist / 2.0).clamp(min=1e-5)
99	
100	    gamma = 1.0 / (2.0 * bandwidth ** 2)
101	    K_xx = torch.exp(-gamma * xx)
102	    K_yy = torch.exp(-gamma * yy)
103	    K_xy = torch.exp(-gamma * xy)
104	    return K_xx, K_yy, K_xy, bandwidth
105	
106	
107	def mmd_loss(x_en, x_tgt, bandwidth=None):
108	    """Unbiased estimate of MMD^2 between English and target representations.
109	
110	    MMD^2 = E[k(x,x')] + E[k(y,y')] - 2·E[k(x,y)]
111	
112	    where k is a Gaussian RBF kernel with median heuristic bandwidth.
113	    """
114	    K_xx, K_yy, K_xy, bw = gaussian_rbf_kernel(x_en, x_tgt, bandwidth)
115	    n = K_xx.shape[0]
116	    m = K_yy.shape[0]
117	
118	    # Unbiased: zero out diagonal for self-terms
119	    sum_xx = (K_xx.sum() - K_xx.diagonal().sum()) / (n * (n - 1)) if n > 1 else K_xx.mean()
120	    sum_yy = (K_yy.sum() - K_yy.diagonal().sum()) / (m * (m - 1)) if m > 1 else K_yy.mean()
121	    sum_xy = K_xy.mean()
122	
123	    return sum_xx + sum_yy - 2.0 * sum_xy
124	
125	
126	# ---------------------------------------------------------------------------
127	# CaCLR Probe model
128	# ---------------------------------------------------------------------------
129	
130	class CaCLRProbe(nn.Module):
131	    """Linear probe with CaCLR regularization.
132	
133	    Functionally equivalent to sklearn LogisticRegression (single Linear layer),
134	    but trained with gradient descent plus L_SB-ECE and L_MMD regularizers.
135	
136	    Exposes predict_proba() and decision_function() for compatibility with
137	    transfer_eval.py's evaluate_probe().
138	    """
139	
140	    def __init__(self, input_dim, l2_weight=1.0):
141	        super().__init__()
142	        self.linear = nn.Linear(input_dim, 1)
143	        self.l2_weight = l2_weight
144	
145	    def forward(self, x):
146	        """Return raw logits (N,)."""
147	        return self.linear(x).squeeze(-1)
148	
149	    def predict_proba(self, x):
150	        """Return (N, 2) numpy array of [P(class=0), P(class=1)].
151	
152	        Accepts numpy array or torch Tensor. Returns numpy for sklearn compat.
153	        """
154	        if isinstance(x, np.ndarray):
155	            x = torch.from_numpy(x).float().to(self.linear.weight.device)
156	        with torch.no_grad():
157	            p1 = torch.sigmoid(self.forward(x)).cpu().numpy()
158	        return np.column_stack([1 - p1, p1])
159	
160	    def decision_function(self, x):
161	        """Return logits as 1-D numpy array (sklearn compat)."""
162	        if isinstance(x, np.ndarray):
163	            x = torch.from_numpy(x).float().to(self.linear.weight.device)
164	        with torch.no_grad():
165	            return self.forward(x).cpu().numpy()
166	
167	    def l2_reg(self):
168	        """L2 penalty on weights (not bias), matching sklearn C = 1/l2_weight."""
169	        return self.l2_weight * (self.linear.weight ** 2).sum()
170	
171	    @classmethod
172	    def from_sklearn(cls, sklearn_probe, scaler, l2_weight=1.0):
173	        """Initialize from a trained sklearn LogisticRegression + StandardScaler.
174	
175	        Copies weight and bias so CaCLR starts from the converged LR solution.
176	        The scaler is applied externally (same as sklearn pipeline), so we only
177	        need the LR parameters here.
178	        """
179	        input_dim = sklearn_probe.coef_.shape[1]
180	        model = cls(input_dim, l2_weight=l2_weight)
181	        with torch.no_grad():
182	            model.linear.weight.copy_(torch.from_numpy(sklearn_probe.coef_).float())
183	            model.linear.bias.copy_(torch.from_numpy(sklearn_probe.intercept_).float())
184	        return model
185	
186	
187	# ---------------------------------------------------------------------------
188	# Training loop
189	# ---------------------------------------------------------------------------
190	
191	def train_caclr(
192	    X_en, y_en,
193	    X_tgt_dict,
194	    alpha=1.0,
195	    beta=0.1,
196	    lr=1e-3,
197	    epochs=100,
198	    l2_weight=1.0,
199	    init_from_sklearn=True,
200	    seed=42,
201	    verbose=True,
202	):
203	    """Train CaCLR probe.
204	
205	    Steps:
206	      1. Fit StandardScaler on English data.
207	      2. Train standard LogisticRegression on English (sklearn).
208	      3. Initialize CaCLRProbe from LR weights.
209	      4. Fine-tune with L_BCE + α·L_SB-ECE + β·L_MMD.
210	
211	    Args:
212	        X_en: (N_en, D) numpy array of English activations.
213	        y_en: (N_en,) numpy array of binary labels.
214	        X_tgt_dict: {lang: (X_tgt, y_tgt)} numpy arrays for target languages.
215	        alpha: weight on SB-ECE calibration loss.
216	        beta: weight on MMD consistency loss.
217	        lr: learning rate for Adam optimizer.
218	        epochs: number of training epochs.
219	        l2_weight: L2 regularization weight (sklearn C = 1/l2_weight).
220	        init_from_sklearn: if True, warm-start from sklearn LR solution.
221	        seed: random seed.
222	        verbose: print training progress.
223	
224	    Returns:
225	        probe: trained CaCLRProbe (on CPU).
226	        scaler: fitted StandardScaler.
227	        history: dict with keys "total", "bce", "sb_ece", "mmd" (lists of per-epoch losses).
228	    """
229	    torch.manual_seed(seed)
230	    np.random.seed(seed)
231	    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
232	
233	    # 1. Fit scaler on English data
234	    scaler = StandardScaler()
235	    X_en_s = scaler.fit_transform(X_en)
236	
237	    # 2. Train sklearn LR as initialization
238	    sklearn_C = 1.0 / l2_weight if l2_weight > 0 else 1e6
239	    sklearn_lr = LogisticRegression(
240	        C=sklearn_C, penalty="l2", solver="lbfgs", max_iter=2000, random_state=seed,
241	    )
242	    sklearn_lr.fit(X_en_s, y_en)
243	
244	    # 3. Initialize CaCLRProbe
245	    if init_from_sklearn:
246	        probe = CaCLRProbe.from_sklearn(sklearn_lr, scaler, l2_weight=l2_weight)
247	    else:
248	        probe = CaCLRProbe(X_en_s.shape[1], l2_weight=l2_weight)
249	    probe = probe.to(device)
250	
251	    # Convert data to tensors
252	    X_en_t = torch.from_numpy(X_en_s).float().to(device)
253	    y_en_t = torch.from_numpy(y_en.astype(np.float32)).to(device)
254	
255	    tgt_tensors = {}
256	    for lang, (X_tgt, y_tgt) in X_tgt_dict.items():
257	        X_tgt_s = scaler.transform(X_tgt)
258	        tgt_tensors[lang] = (
259	            torch.from_numpy(X_tgt_s).float().to(device),
260	            torch.from_numpy(y_tgt.astype(np.float32)).to(device),
261	        )
262	
263	    # 4. Fine-tune with CaCLR loss
264	    optimizer = torch.optim.Adam(probe.parameters(), lr=lr)
265	    history = {"total": [], "bce": [], "sb_ece": [], "mmd": [], "l2": []}
266	
267	    for epoch in range(epochs):
268	        probe.train()
269	        optimizer.zero_grad()
270	
271	        logits_en = probe(X_en_t)
272	        probs_en = torch.sigmoid(logits_en)
273	
274	        loss_bce = bce_loss(logits_en, y_en_t)
275	        loss_sb_ece = sb_ece_loss(probs_en, y_en_t)
276	        loss_l2 = probe.l2_reg()
277	
278	        # MMD: average over all target languages
279	        loss_mmd = torch.tensor(0.0, device=device)
280	        if beta > 0 and len(tgt_tensors) > 0:
281	            # Note: linear probe logits are 1-D, so MMD operates in a 1-dimensional space.
282	            # This limits MMD's ability to capture complex distributional differences.
283	            # This is a design trade-off, not a bug — observe in experiments and discuss in paper.
284	            mmd_terms = []
285	            for lang, (X_tgt_t, _) in tgt_tensors.items():
286	                n_sub = min(512, X_en_t.shape[0], X_tgt_t.shape[0])
287	                idx_en = torch.randperm(X_en_t.shape[0], device=device)[:n_sub]
288	                idx_tgt = torch.randperm(X_tgt_t.shape[0], device=device)[:n_sub]
289	                logits_en_sub = probe(X_en_t[idx_en])
290	                logits_tgt_sub = probe(X_tgt_t[idx_tgt])
291	                mmd_terms.append(mmd_loss(logits_en_sub.unsqueeze(1), logits_tgt_sub.unsqueeze(1)))
292	            loss_mmd = torch.stack(mmd_terms).mean()
293	
294	        total = loss_bce + alpha * loss_sb_ece + beta * loss_mmd + loss_l2
295	        total.backward()
296	        optimizer.step()
297	
298	        history["total"].append(total.item())
299	        history["bce"].append(loss_bce.item())
300	        history["sb_ece"].append(loss_sb_ece.item())
301	        history["mmd"].append(loss_mmd.item())
302	        history["l2"].append(loss_l2.item())
303	
304	        if verbose and (epoch + 1) % max(1, epochs // 10) == 0:
305	            print(f"  epoch {epoch+1:>4d}/{epochs}  "
306	                  f"total={total.item():.4f}  bce={loss_bce.item():.4f}  "
307	                  f"sb_ece={loss_sb_ece.item():.4f}  mmd={loss_mmd.item():.4f}")
308	
309	    probe = probe.cpu().eval()
310	    return probe, scaler, history
311	
312	
313	# ---------------------------------------------------------------------------
314	# Evaluation helper (quick validation during sweep)
315	# ---------------------------------------------------------------------------
316	
317	def compute_ece(probs, labels, n_bins=10):
318	    """Histogram-based ECE (numpy, matches train_probe.py)."""
319	    bin_edges = np.linspace(0, 1, n_bins + 1)
320	    ece = 0.0
321	    for lo, hi in zip(bin_edges[:-1], bin_edges[1:]):
322	        mask = (probs > lo) & (probs <= hi)
323	        if lo == 0.0:
324	            mask = (probs >= lo) & (probs <= hi)
325	        n_in_bin = mask.sum()
326	        if n_in_bin == 0:
327	            continue
328	        ece += (n_in_bin / len(probs)) * abs(labels[mask].mean() - probs[mask].mean())
329	    return ece
330	
331	
332	def quick_eval(probe, scaler, X, y):
333	    """AUROC + ECE + Brier on held-out data."""
334	    X_s = scaler.transform(X)
335	    probs = probe.predict_proba(X_s)[:, 1]
336	    logits = probe.decision_function(X_s)
337	    if len(np.unique(y)) < 2:
338	        return None, None, None
339	    return roc_auc_score(y, logits), compute_ece(probs, y), brier_score_loss(y, probs)
340	
341	
342	# ---------------------------------------------------------------------------
343	# CLI
344	# ---------------------------------------------------------------------------
345	
346	def parse_args():
347	    p = argparse.ArgumentParser(description="CaCLR probe training")
348	    p.add_argument("--activations_dir", default="./activations")
349	    p.add_argument("--output_dir", default="./probes_caclr")
350	    p.add_argument("--layer", type=int, required=True,
351	                   help="Layer index to train on")
352	    p.add_argument("--languages", nargs="+", default=["zh", "ar", "hi", "sw", "ko"],
353	                   help="Target languages for MMD consistency loss")
354	    p.add_argument("--alpha", type=float, default=1.0,
355	                   help="SB-ECE calibration loss weight")
356	    p.add_argument("--beta", type=float, default=0.1,
357	                   help="MMD consistency loss weight")
358	    p.add_argument("--alpha_sweep", type=str, default=None,
359	                   help="Comma-separated alpha values for grid search "
360	                        "(e.g., '0.01,0.1,1.0,10.0')")
361	    p.add_argument("--beta_sweep", type=str, default=None,
362	                   help="Comma-separated beta values for grid search")
363	    p.add_argument("--lr", type=float, default=1e-3)
364	    p.add_argument("--epochs", type=int, default=100)
365	    p.add_argument("--l2_weight", type=float, default=1.0)
366	    p.add_argument("--test_size", type=float, default=0.2,
367	                   help="English held-out fraction for sweep selection")
368	    p.add_argument("--ece_weight", type=float, default=0.1,
369	                   help="Weight for ECE penalty in sweep selection: score = auroc - ece_weight * ece")
370	    p.add_argument("--seed", type=int, default=42)
371	    return p.parse_args()
372	
373	
374	def main():
375	    args = parse_args()
376	    os.makedirs(args.output_dir, exist_ok=True)
377	
378	    # Load English activations
379	    en_path = os.path.join(args.activations_dir, f"layer{args.layer}_en.pt")
380	    en_data = torch.load(en_path, weights_only=True)
381	    X_en = en_data["activations"].numpy()
382	    y_en = en_data["labels"].numpy()
383	    print(f"English data: {X_en.shape[0]} samples, dim={X_en.shape[1]}")
384	
385	    # Load target language activations
386	    X_tgt_dict = {}
387	    for lang in args.languages:
388	        tgt_path = os.path.join(args.activations_dir, f"layer{args.layer}_{lang}.pt")
389	        if not os.path.exists(tgt_path):
390	            print(f"  [SKIP] {tgt_path} not found")
391	            continue
392	        tgt_data = torch.load(tgt_path, weights_only=True)
393	        X_tgt_dict[lang] = (tgt_data["activations"].numpy(), tgt_data["labels"].numpy())
394	        print(f"  {lang}: {X_tgt_dict[lang][0].shape[0]} samples")
395	
396	    # Determine if sweep mode
397	    sweep_mode = args.alpha_sweep is not None or args.beta_sweep is not None
398	    alphas = [float(v) for v in args.alpha_sweep.split(",")] if args.alpha_sweep else [args.alpha]
399	    betas = [float(v) for v in args.beta_sweep.split(",")] if args.beta_sweep else [args.beta]
400	
401	    if sweep_mode:
402	        # Hold out English validation set for selecting best (alpha, beta)
403	        X_train, X_val, y_train, y_val = train_test_split(
404	            X_en, y_en, test_size=args.test_size, random_state=args.seed, stratify=y_en,
405	        )
406	        print(f"\nSweep mode: {len(alphas)} alphas × {len(betas)} betas = {len(alphas)*len(betas)} runs")
407	        print(f"Train: {len(y_train)}, Val: {len(y_val)}")
408	        print(f"{'alpha':>8s} {'beta':>8s} {'AUROC':>7s} {'ECE':>7s} {'Brier':>7s}")
409	        print("-" * 42)
410	
411	        best_score = -float("inf")
412	        best_result = None
413	
414	        for a, b in product(alphas, betas):
415	            probe, scaler, history = train_caclr(
416	                X_train, y_train, X_tgt_dict,
417	                alpha=a, beta=b, lr=args.lr, epochs=args.epochs,
418	                l2_weight=args.l2_weight, seed=args.seed, verbose=False,
419	            )
420	            auroc, ece, brier = quick_eval(probe, scaler, X_val, y_val)
421	            score = (auroc or 0.0) - args.ece_weight * (ece or 1.0)
422	            print(f"{a:>8.3f} {b:>8.4f} {auroc or 0:>7.4f} {ece or 0:>7.4f} {brier or 0:>7.4f}"
423	                  f"{'  *' if score > best_score else ''}")
424	
425	            if score > best_score:
426	                best_score = score
427	                best_result = {
428	                    "probe": probe, "scaler": scaler, "alpha": a, "beta": b,
429	                    "history": history, "val_auroc": auroc, "val_ece": ece, "val_brier": brier,
430	                }
431	
432	        # Retrain best on full English data
433	        print(f"\nBest: alpha={best_result['alpha']}, beta={best_result['beta']} "
434	              f"(val AUROC={best_result['val_auroc']:.4f}, ECE={best_result['val_ece']:.4f})")
435	        print("Retraining on full English data...")
436	        probe, scaler, history = train_caclr(
437	            X_en, y_en, X_tgt_dict,
438	            alpha=best_result["alpha"], beta=best_result["beta"],
439	            lr=args.lr, epochs=args.epochs, l2_weight=args.l2_weight,
440	            seed=args.seed, verbose=True,
441	        )
442	        save_dict = {
443	            "model": probe, "scaler": scaler,
444	            "alpha": best_result["alpha"], "beta": best_result["beta"],
445	            "history": history,
446	            "sweep_best": {"val_auroc": best_result["val_auroc"],
447	                           "val_ece": best_result["val_ece"],
448	                           "val_brier": best_result["val_brier"]},
449	        }
450	    else:
451	        # Single run
452	        probe, scaler, history = train_caclr(
453	            X_en, y_en, X_tgt_dict,
454	            alpha=args.alpha, beta=args.beta, lr=args.lr, epochs=args.epochs,
455	            l2_weight=args.l2_weight, seed=args.seed, verbose=True,
456	        )
457	        save_dict = {
458	            "model": probe, "scaler": scaler,
459	            "alpha": args.alpha, "beta": args.beta,
460	            "history": history,
461	        }
462	
463	    # Save probe (compatible with transfer_eval.py)
464	    out_path = os.path.join(args.output_dir, f"probe_layer{args.layer}.pkl")
465	    with open(out_path, "wb") as f:
466	        pickle.dump(save_dict, f)
467	    print(f"\nProbe saved to {out_path}")
468	
469	
470	if __name__ == "__main__":
471	    main()
472	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ccc444a-fe1a-4a89-b4a0-4a5829afc671",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "3f5e225a-9279-4872-8f87-4df52a11d8e5",
  "sourceToolAssistantUUID": "0ccc444a-fe1a-4a89-b4a0-4a5829afc671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T06:00:46.131Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EH4DFxSz1S45sq24efJGxq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/extract_activations_large.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f5e225a-9279-4872-8f87-4df52a11d8e5",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCoi1SD4pEtgmoGw1U6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6da47c1-93ba-4145-bbc5-553e740c24d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zDwd8VkMX4pUemfghNwE6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1161,
      "cache_read_input_tokens": 32495,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1161
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 32495,
          "cache_creation_input_tokens": 1161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1161,
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

_source line 35 · 2026-05-21T06:00:46.137Z_

<details><summary>↩ Tool result · `toolu_01EH4DFxSz1S45sq24efJGxq`</summary>

```text
1	"""
2	Extract residual-stream activations from *large* LLMs (Qwen3-235B-A22B, Llama 4 Scout, etc.).
3	
4	Differences from extract_activations.py:
5	  - Uses register_forward_hook instead of output_hidden_states=True.
6	    Reason: output_hidden_states returns ALL layers' hidden states simultaneously,
7	    which is prohibitive for 94-layer models. Hooks capture only the target layers.
8	  - Supports INT4/INT8 quantization via bitsandbytes (--quantization int4/int8).
9	  - Incremental saving via --save_interval to survive OOM or interruption.
10	  - Architecture-adaptive layer access (model.model.layers / model.transformer.h).
11	
12	Output format is identical to extract_activations.py:
13	  layer{i}_{lang}.pt  ->  {"activations": Tensor(N, hidden_dim), "labels": Tensor(N,)}
14	
15	Dependencies: torch, transformers, datasets, bitsandbytes (for quantization), tqdm
16	
17	Usage:
18	  python extract_activations_large.py \
19	    --model Qwen/Qwen3-235B-A22B \
20	    --languages en zh ar hi sw ko \
21	    --layers 0,8,16,24,32,48,64,80,93 \
22	    --output_dir ./activations \
23	    --quantization int4 \
24	    --save_interval 200
25	"""
26	
27	import argparse
28	import os
29	
30	import torch
31	from datasets import load_dataset
32	from transformers import AutoModelForCausalLM, AutoTokenizer
33	from tqdm import tqdm
34	
35	
36	LETTERS = ["A", "B", "C", "D"]
37	
38	
39	def parse_args():
40	    p = argparse.ArgumentParser()
41	    p.add_argument("--model", required=True, help="HuggingFace model name or path")
42	    p.add_argument("--languages", nargs="+",
43	                   default=["en", "zh", "ar", "hi", "sw", "ko", "es", "fr", "de", "ru",
44	                            "tr", "bn", "ja", "pt", "vi", "te", "id", "pl", "nl", "uk"])
45	    p.add_argument("--layers", default="0,4,8,12,16,20,24,28,31",
46	                   help="Comma-separated transformer layer indices (0-indexed)")
47	    p.add_argument("--output_dir", default="./activations")
48	    p.add_argument("--n_shot", type=int, default=5)
49	    p.add_argument("--max_samples", type=int, default=0, help="0 = all test samples")
50	    p.add_argument("--dtype", default="bfloat16", choices=["float16", "bfloat16"])
51	    p.add_argument("--subjects", nargs="*", default=None,
52	                   help="Restrict to these MMLU subjects (default: all)")
53	    p.add_argument("--quantization", default="none", choices=["none", "int4", "int8"],
54	                   help="Quantization: none (full precision), int4 (NF4 4-bit), int8 (LLM.int8)")
55	    p.add_argument("--save_interval", type=int, default=500,
56	                   help="Incrementally save every N samples (0 = only save at end)")
57	    p.add_argument("--split_ratio", type=float, default=0.0,
58	                   help="If > 0, split test data into train/eval. E.g., 0.7 = 70%% train, 30%% eval")
59	    p.add_argument("--split_seed", type=int, default=42,
60	                   help="Random seed for train/eval split (ensures reproducibility across languages)")
61	    return p.parse_args()
62	
63	
64	# ---------------------------------------------------------------------------
65	# Data loading (identical to extract_activations.py)
66	# ---------------------------------------------------------------------------
67	
68	def load_mmlu(language, split="test"):
69	    """Load an MMLU split. English from cais/mmlu, others from Global-MMLU."""
70	    if language == "en":
71	        return load_dataset("cais/mmlu", "all", split=split)
72	    return load_dataset("CohereForAI/Global-MMLU", language, split=split)
73	
74	
75	def load_mmlu_dev(language):
76	    """Load few-shot exemplars (try 'dev' first, then 'validation')."""
77	    for split_name in ["dev", "validation"]:
78	        try:
79	            return load_mmlu(language, split_name)
80	        except (ValueError, KeyError):
81	            continue
82	    raise RuntimeError(f"No dev/validation split found for '{language}'")
83	
84	
85	def normalize_row(row):
86	    """Normalize a dataset row to {question, choices, answer(int), subject}."""
87	    question = row.get("question", row.get("input", ""))
88	
89	    if "choices" in row and isinstance(row["choices"], list):
90	        choices = list(row["choices"])
91	    else:
92	        choices = [row.get(f"option_{l.lower()}", "") for l in LETTERS]
93	
94	    answer = row.get("answer", row.get("target", 0))
95	    if isinstance(answer, str):
96	        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)
97	
98	    return {
99	        "question": question,
100	        "choices": choices,
101	        "answer": int(answer),
102	        "subject": row.get("subject", "unknown"),
103	    }
104	
105	
106	# ---------------------------------------------------------------------------
107	# Prompt formatting (identical to extract_activations.py)
108	# ---------------------------------------------------------------------------
109	
110	def _format_question(question, choices):
111	    parts = [f"{question}\n"]
112	    for i, c in enumerate(choices):
113	        parts.append(f"{LETTERS[i]}. {c}\n")
114	    return "".join(parts)
115	
116	
117	def build_prompt(row, few_shot_rows, n_shot):
118	    """Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars."""
119	    subject_pretty = row["subject"].replace("_", " ")
120	    lines = [
121	        f"The following are multiple choice questions (with answers) about {subject_pretty}.\n\n"
122	    ]
123	    for fs in few_shot_rows[:n_shot]:
124	        fs = normalize_row(fs) if "choices" not in fs or not isinstance(fs.get("answer"), int) else fs
125	        lines.append(_format_question(fs["question"], fs["choices"]))
126	        lines.append(f"Answer: {LETTERS[fs['answer']]}\n\n")
127	    lines.append(_format_question(row["question"], row["choices"]))
128	    lines.append("Answer:")
129	    return "".join(lines)
130	
131	
132	# ---------------------------------------------------------------------------
133	# Model loading with quantization support
134	# ---------------------------------------------------------------------------
135	
136	def load_model(model_name, dtype, quantization):
137	    """Load model with optional INT4/INT8 quantization via bitsandbytes."""
138	    kwargs = dict(device_map="auto", trust_remote_code=True)
139	
140	    if quantization == "int4":
141	        from transformers import BitsAndBytesConfig
142	        kwargs["quantization_config"] = BitsAndBytesConfig(
143	            load_in_4bit=True,
144	            bnb_4bit_compute_dtype=torch.bfloat16,
145	            bnb_4bit_quant_type="nf4",
146	            bnb_4bit_use_double_quant=True,
147	        )
148	    elif quantization == "int8":
149	        from transformers import BitsAndBytesConfig
150	        kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)
151	    else:
152	        kwargs["torch_dtype"] = dtype
153	
154	    model = AutoModelForCausalLM.from_pretrained(model_name, **kwargs)
155	    model.eval()
156	    return model
157	
158	
159	# ---------------------------------------------------------------------------
160	# Architecture-adaptive layer access
161	# ---------------------------------------------------------------------------
162	
163	def get_layer_modules(model):
164	    """Return the nn.ModuleList of transformer layers, adapting to model architecture.
165	
166	    Tries common attribute paths used by different model families:
167	      - model.model.layers      (Qwen, Llama, Mistral, Gemma, etc.)
168	      - model.transformer.h     (GPT-2, GPT-J, GPT-NeoX)
169	      - model.gpt_neox.layers   (GPT-NeoX variants)
170	    """
171	    candidates = [
172	        ("model.model.layers", lambda m: m.model.layers),
173	        ("model.transformer.h", lambda m: m.transformer.h),
174	        ("model.gpt_neox.layers", lambda m: m.gpt_neox.layers),
175	    ]
176	    for path_name, accessor in candidates:
177	        try:
178	            layers = accessor(model)
179	            if hasattr(layers, "__len__") and len(layers) > 0:
180	                print(f"  Layer access path: {path_name}  ({len(layers)} layers)")
181	                return layers
182	        except AttributeError:
183	            continue
184	    raise RuntimeError(
185	        "Cannot locate transformer layers. "
186	        "Supported paths: model.model.layers, model.transformer.h, model.gpt_neox.layers"
187	    )
188	
189	
190	# ---------------------------------------------------------------------------
191	# Forward hook machinery
192	# ---------------------------------------------------------------------------
193	
194	def get_final_norm(model):
195	    """Return the model's final normalization layer (RMSNorm/LayerNorm after last transformer block).
196	
197	    Used to apply post-norm on the last layer's hook output, matching the behavior of
198	    output_hidden_states=True which returns post-norm activations for the final layer.
199	    """
200	    candidates = [
201	        lambda m: m.model.norm,       # Qwen, Llama, Mistral, Gemma
202	        lambda m: m.transformer.ln_f,  # GPT-2, GPT-J
203	        lambda m: m.gpt_neox.final_layer_norm,  # GPT-NeoX
204	    ]
205	    for accessor in candidates:
206	        try:
207	            norm = accessor(model)
208	            if norm is not None:
209	                return norm
210	        except AttributeError:
211	            continue
212	    return None
213	
214	
215	def register_activation_hooks(model, layer_indices, captured):
216	    """Register forward hooks on target layers to capture last-token hidden states.
217	
218	    Why hooks instead of output_hidden_states=True:
219	      output_hidden_states materializes ALL layers' hidden states in memory at once.
220	      For a 94-layer model like Qwen3-235B, this means 94 * (batch * seq_len * hidden_dim)
221	      tensors kept alive — easily 50+ GB extra VRAM. Hooks only capture the specific
222	      layers we need and immediately detach/move to CPU, keeping peak VRAM minimal.
223	
224	    Post-norm on last layer:
225	      output_hidden_states returns post-norm activations for the final layer (i.e., after
226	      the model's final RMSNorm/LayerNorm). To match this behavior and ensure consistency
227	      with MVP experiments that used output_hidden_states, we apply the final norm to the
228	      last layer's hook output. All other layers return pre-norm (direct layer output).
229	    """
230	    layers = get_layer_modules(model)
231	    n_layers = len(layers)
232	    final_norm = get_final_norm(model)
233	    max_target_layer = max(layer_indices)
234	    handles = []
235	
236	    def make_hook(layer_idx):
237	        def hook_fn(module, input, output):
238	            h = output[0] if isinstance(output, tuple) else output
239	            h = h[0, -1]
240	            # Apply final norm on the last transformer layer to match output_hidden_states behavior
241	            if layer_idx == n_layers - 1 and final_norm is not None:
242	                with torch.no_grad():
243	                    h = final_norm(h.unsqueeze(0)).squeeze(0)
244	            captured[layer_idx] = h.detach().cpu().float()
245	        return hook_fn
246	
247	    for li in layer_indices:
248	        if li < 0 or li >= n_layers:
249	            raise ValueError(f"Layer index {li} out of range [0, {n_layers})")
250	        handles.append(layers[li].register_forward_hook(make_hook(li)))
251	
252	    return handles
253	
254	
255	def remove_hooks(handles):
256	    for h in handles:
257	        h.remove()
258	
259	
260	# ---------------------------------------------------------------------------
261	# Incremental save / load
262	# ---------------------------------------------------------------------------
263	
264	def save_layer_data(storage, layer_indices, lang, output_dir,
265	                    train_indices=None, eval_indices=None):
266	    """Save accumulated activations for all target layers.
267	
268	    If train_indices/eval_indices are provided, saves separate train/eval files
269	    instead of a single file.
270	    """
271	    for li in layer_indices:
272	        if not storage[li]["acts"]:
273	            continue
274	        acts = torch.stack(storage[li]["acts"])
275	        labels = torch.tensor(storage[li]["labels"], dtype=torch.long)
276	
277	        if train_indices is not None and eval_indices is not None:
278	            for suffix, indices in [("train", train_indices), ("eval", eval_indices)]:
279	                idx = [i for i in indices if i < len(acts)]
280	                if not idx:
281	                    continue
282	                idx_t = torch.tensor(idx, dtype=torch.long)
283	                path = os.path.join(output_dir, f"layer{li}_{lang}_{suffix}.pt")
284	                torch.save({"activations": acts[idx_t], "labels": labels[idx_t]}, path)
285	        else:
286	            path = os.path.join(output_dir, f"layer{li}_{lang}.pt")
287	            torch.save({"activations": acts, "labels": labels}, path)
288	
289	
290	def load_existing_progress(layer_indices, lang, output_dir):
291	    """Load previously saved data to support resumption after interruption."""
292	    storage = {li: {"acts": [], "labels": []} for li in layer_indices}
293	    n_existing = 0
294	    for li in layer_indices:
295	        path = os.path.join(output_dir, f"layer{li}_{lang}.pt")
296	        if os.path.exists(path):
297	            data = torch.load(path, weights_only=True)
298	            storage[li]["acts"] = list(data["activations"].unbind(0))
299	            storage[li]["labels"] = data["labels"].tolist()
300	            n_existing = max(n_existing, len(storage[li]["labels"]))
301	    return storage, n_existing
302	
303	
304	# ---------------------------------------------------------------------------
305	# Main extraction loop
306	# ---------------------------------------------------------------------------
307	
308	def main():
309	    args = parse_args()
310	    layer_indices = sorted(int(x) for x in args.layers.split(","))
311	    os.makedirs(args.output_dir, exist_ok=True)
312	
313	    dtype = torch.bfloat16 if args.dtype == "bfloat16" else torch.float16
314	    print(f"Loading model: {args.model}  dtype={args.dtype}  quantization={args.quantization}")
315	
316	    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
317	    if tokenizer.pad_token is None:
318	        tokenizer.pad_token = tokenizer.eos_token
319	
320	    model = load_model(args.model, dtype, args.quantization)
321	
322	    n_model_layers = model.config.num_hidden_layers
323	    print(f"Model has {n_model_layers} transformer layers; extracting: {layer_indices}")
324	    for li in layer_indices:
325	        if li < 0 or li >= n_model_layers:
326	            raise ValueError(f"Layer index {li} out of range [0, {n_model_layers})")
327	
328	    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]
329	    print(f"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }")
330	
331	    # Split indices: computed once on the first language, reused for all
332	    split_train_indices = None
333	    split_eval_indices = None
334	
335	    # Register hooks once — they persist across forward calls
336	    captured = {}
337	    handles = register_activation_hooks(model, layer_indices, captured)
338	
339	    try:
340	        for lang_idx, lang in enumerate(args.languages):
341	            print(f"\n{'='*50}")
342	            print(f"  Language: {lang}")
343	            print(f"{'='*50}")
344	
345	            test_ds = load_mmlu(lang, "test")
346	            dev_ds = load_mmlu_dev(lang)
347	
348	            if args.subjects:
349	                test_ds = test_ds.filter(lambda x: x.get("subject") in args.subjects)
350	                dev_ds = dev_ds.filter(lambda x: x.get("subject") in args.subjects)
351	
352	            n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))
353	
354	            # Compute split on first language, reuse for all subsequent languages
355	            if args.split_ratio > 0 and split_train_indices is None:
356	                from sklearn.model_selection import train_test_split
357	                subjects = [normalize_row(test_ds[i])["subject"] for i in range(n)]
358	                split_train_indices, split_eval_indices = train_test_split(
359	                    list(range(n)), train_size=args.split_ratio,
360	                    stratify=subjects, random_state=args.split_seed,
361	                )
362	                split_path = os.path.join(args.output_dir, "split_indices.pt")
363	                torch.save({
364	                    "train": split_train_indices, "eval": split_eval_indices,
365	                    "split_ratio": args.split_ratio, "seed": args.split_seed,
366	                    "n_total": n, "first_lang": lang,
367	                }, split_path)
368	                print(f"  Split: {len(split_train_indices)} train + {len(split_eval_indices)} eval  (saved to {split_path})")
369	
370	            dev_by_subject: dict[str, list] = {}
371	            for r in dev_ds:
372	                dev_by_subject.setdefault(r.get("subject", "unknown"), []).append(r)
373	            dev_fallback = list(dev_ds)[:args.n_shot]
374	
375	            # Try to resume from existing partial results
376	            storage, n_existing = load_existing_progress(layer_indices, lang, args.output_dir)
377	            if n_existing > 0:
378	                print(f"  Resuming from sample {n_existing} (found existing data)")
379	
380	            for i in tqdm(range(n_existing, n), desc=f"[{lang}]", initial=n_existing, total=n):
381	                row = normalize_row(test_ds[i])
382	                few_shots = dev_by_subject.get(row["subject"], dev_fallback)
383	                prompt = build_prompt(row, few_shots, args.n_shot)
384	
385	                inputs = tokenizer(prompt, return_tensors="pt", truncation=True,
386	                                   max_length=4096).to(model.device)
387	
388	                with torch.no_grad():
389	                    # No output_hidden_states — hooks capture what we need
390	                    out = model(**inputs)
391	
392	                logits_last = out.logits[0, -1]
393	                choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])
394	                pred = choice_logits.argmax().item()
395	                correct = int(pred == row["answer"])
396	
397	                for li in layer_indices:
398	                    storage[li]["acts"].append(captured[li])
399	                    storage[li]["labels"].append(correct)
400	
401	                captured.clear()
402	                del out, inputs
403	
404	                if (i + 1) % 100 == 0:
405	                    torch.cuda.empty_cache()
406	
407	                # Incremental save
408	                if args.save_interval > 0 and (i + 1) % args.save_interval == 0:
409	                    save_layer_data(storage, layer_indices, lang, args.output_dir,
410	                                    split_train_indices, split_eval_indices)
411	                    print(f"  [checkpoint] saved at sample {i + 1}")
412	
413	            # Final save for this language
414	            save_layer_data(storage, layer_indices, lang, args.output_dir,
415	                            split_train_indices, split_eval_indices)
416	            for li in layer_indices:
417	                n_samples = len(storage[li]["labels"])
418	                if n_samples > 0:
419	                    acc = sum(storage[li]["labels"]) / n_samples
420	                    if split_train_indices is not None:
421	                        print(f"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}_{{train,eval}}.pt")
422	                    else:
423	                        print(f"  Layer {li:>2d}: N={n_samples:>5d}  model_acc={acc:.3f}  -> layer{li}_{lang}.pt")
424	
425	    finally:
426	        # Always clean up hooks, even if an exception occurs
427	        remove_hooks(handles)
428	
429	    print("\nExtraction complete.")
430	
431	
432	if __name__ == "__main__":
433	    main()
434	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6da47c1-93ba-4145-bbc5-553e740c24d3",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "bdf3595e-d7a4-496c-8578-88938d2ab04a",
  "sourceToolAssistantUUID": "c6da47c1-93ba-4145-bbc5-553e740c24d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T06:00:50.687Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QStABx6z1ez9QjpLGCEUHh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/compute_cka.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdf3595e-d7a4-496c-8578-88938d2ab04a",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCoyw99DneRoqppuFmG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab9e8cf6-32ca-46f7-838a-22df26b8b6dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdSWYQ9DHPoNPH8hBTSQU6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18502,
      "cache_read_input_tokens": 33656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18502,
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

_source line 37 · 2026-05-21T06:00:50.692Z_

<details><summary>↩ Tool result · `toolu_01QStABx6z1ez9QjpLGCEUHh`</summary>

```text
1	"""
2	Compute Linear CKA (Centered Kernel Alignment) between cross-lingual activations.
3	
4	Measures representational similarity between English and target language activations
5	at each layer of an LLM, using parallel data (same samples in same order).
6	
7	Input:  activation files `layer{i}_{lang}.pt`, each containing
8	        {"activations": Tensor(N, hidden_dim), "labels": Tensor(N,)}
9	Output: CSV with columns (layer, language, cka_value) + summary statistics.
10	
11	Reference: Kornblith et al., "Similarity of Neural Network Representations Revisited",
12	           ICML 2019. https://arxiv.org/abs/1905.00414
13	
14	Requires: torch
15	"""
16	
17	import argparse
18	import os
19	import re
20	import sys
21	from pathlib import Path
22	
23	import torch
24	
25	
26	def linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:
27	    """Linear CKA between two activation matrices.
28	
29	    Args:
30	        X: (n, p) activations for language A
31	        Y: (n, q) activations for language B
32	        Both must share the same n (parallel samples in identical order).
33	    """
34	    X = X - X.mean(0)
35	    Y = Y - Y.mean(0)
36	
37	    hsic_xy = torch.norm(X.T @ Y, "fro") ** 2
38	    hsic_xx = torch.norm(X.T @ X, "fro") ** 2
39	    hsic_yy = torch.norm(Y.T @ Y, "fro") ** 2
40	
41	    return (hsic_xy / (hsic_xx.sqrt() * hsic_yy.sqrt())).item()
42	
43	
44	def detect_layers(activations_dir: str) -> list[int]:
45	    """Auto-detect available layer indices from filenames."""
46	    pattern = re.compile(r"^layer(\d+)_\w+\.pt$")
47	    layers = set()
48	    for f in os.listdir(activations_dir):
49	        m = pattern.match(f)
50	        if m:
51	            layers.add(int(m.group(1)))
52	    return sorted(layers)
53	
54	
55	def load_activations(activations_dir: str, layer: int, lang: str) -> torch.Tensor:
56	    path = os.path.join(activations_dir, f"layer{layer}_{lang}.pt")
57	    data = torch.load(path, map_location="cpu", weights_only=True)
58	    return data["activations"].float()
59	
60	
61	def main():
62	    parser = argparse.ArgumentParser(description="Compute Linear CKA across languages and layers")
63	    parser.add_argument("--activations_dir", default="./activations", help="Directory with activation .pt files")
64	    parser.add_argument("--output_dir", default="./results", help="Output directory")
65	    parser.add_argument("--layers", default=None, help="Comma-separated layer indices (default: auto-detect)")
66	    parser.add_argument("--languages", nargs="+", default=["zh", "ar", "hi", "sw", "ko"], help="Target languages")
67	    parser.add_argument("--reference_lang", default="en", help="Reference language")
68	    parser.add_argument("--output_file", default="cka_matrix.csv", help="Output CSV filename")
69	    args = parser.parse_args()
70	
71	    if not os.path.isdir(args.activations_dir):
72	        print(f"Error: activations_dir not found: {args.activations_dir}", file=sys.stderr)
73	        sys.exit(1)
74	
75	    layers = [int(x) for x in args.layers.split(",")] if args.layers else detect_layers(args.activations_dir)
76	    if not layers:
77	        print("Error: no layers detected", file=sys.stderr)
78	        sys.exit(1)
79	
80	    os.makedirs(args.output_dir, exist_ok=True)
81	    output_path = os.path.join(args.output_dir, args.output_file)
82	
83	    print(f"Layers: {layers}")
84	    print(f"Languages: {args.languages} (ref: {args.reference_lang})")
85	
86	    results = []
87	
88	    for layer in layers:
89	        ref_acts = load_activations(args.activations_dir, layer, args.reference_lang)
90	        for lang in args.languages:
91	            tgt_acts = load_activations(args.activations_dir, layer, lang)
92	            n = min(ref_acts.shape[0], tgt_acts.shape[0])
93	            cka_val = linear_cka(ref_acts[:n], tgt_acts[:n])
94	            results.append((layer, lang, cka_val))
95	            print(f"  layer {layer:2d} | {lang} | CKA = {cka_val:.6f} (n={n})")
96	
97	    # Write CSV
98	    with open(output_path, "w") as f:
99	        f.write("layer,language,cka_value\n")
100	        for layer, lang, cka_val in results:
101	            f.write(f"{layer},{lang},{cka_val:.6f}\n")
102	    print(f"\nResults saved to {output_path}")
103	
104	    # Summary
105	    print("\n=== Per-language mean CKA ===")
106	    for lang in args.languages:
107	        vals = [c for _, l, c in results if l == lang]
108	        print(f"  {lang}: {sum(vals)/len(vals):.6f}")
109	
110	    print("\n=== Per-layer mean CKA ===")
111	    for layer in layers:
112	        vals = [c for la, _, c in results if la == layer]
113	        print(f"  layer {layer:2d}: {sum(vals)/len(vals):.6f}")
114	
115	
116	if __name__ == "__main__":
117	    main()
118	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab9e8cf6-32ca-46f7-838a-22df26b8b6dc",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "5805175b-2a8d-44cd-ac36-01716750e1ca",
  "sourceToolAssistantUUID": "ab9e8cf6-32ca-46f7-838a-22df26b8b6dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T06:00:51.183Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SZyFi8RwGg7xFHxx3GH4VC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/pareto_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5805175b-2a8d-44cd-ac36-01716750e1ca",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCoyw99DneRoqppuFmG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "baf5d610-adbc-4667-a13e-fc9e0faa736b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdSWYQ9DHPoNPH8hBTSQU6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18502,
      "cache_read_input_tokens": 33656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18502,
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

_source line 39 · 2026-05-21T06:00:51.193Z_

<details><summary>↩ Tool result · `toolu_01SZyFi8RwGg7xFHxx3GH4VC`</summary>

```text
1	#!/usr/bin/env python3
2	"""Pareto dominance analysis for cross-lingual probe transfer tradeoff.
3	
4	Quantifies the depth-transferability tradeoff: deeper-layer EN probes achieve
5	higher in-language accuracy but may transfer worse cross-lingually. Identifies
6	Pareto-optimal layers, computes hypervolume indicators, and tests tradeoff
7	significance via Spearman correlation.
8	
9	Input modes:
10	  (A) Pre-merged CSV with --en_metric and --transfer_metric columns per row.
11	  (B) Separate files: --results_csv (transfer eval) + --probe_csv (EN quality).
12	      In mode B, --method selects which transfer method to analyze.
13	
14	Output (to --output_dir):
15	  pareto_detail.csv   per (layer, language) with Pareto flags and ranks
16	  pareto_summary.csv  per language: hypervolume, Spearman rho, p-value
17	  pareto_results.json combined results (with --json flag)
18	
19	Algorithms:
20	  Pareto dominance: pairwise comparison, O(n^2), n = number of layers (< 50).
21	  Hypervolume: 2D sweep-line (Zitzler & Thiele, IEEE TEC 1999).
22	"""
23	
24	import argparse
25	import csv
26	import json
27	import os
28	import sys
29	from collections import defaultdict
30	
31	import numpy as np
32	from scipy import stats
33	
34	
35	def find_pareto_optimal(points):
36	    """Identify non-dominated points (maximize both objectives). O(n^2)."""
37	    n = len(points)
38	    is_optimal = np.ones(n, dtype=bool)
39	    for i in range(n):
40	        if not is_optimal[i]:
41	            continue
42	        for j in range(n):
43	            if i == j or not is_optimal[j]:
44	                continue
45	            if (points[j, 0] >= points[i, 0] and points[j, 1] >= points[i, 1]
46	                    and (points[j, 0] > points[i, 0] or points[j, 1] > points[i, 1])):
47	                is_optimal[i] = False
48	                break
49	    return is_optimal
50	
51	
52	def compute_pareto_ranks(points):
53	    """Assign Pareto rank (1 = frontier) by iterative peeling."""
54	    n = len(points)
55	    ranks = np.zeros(n, dtype=int)
56	    remaining = np.ones(n, dtype=bool)
57	    rank = 1
58	    while remaining.any():
59	        idx = np.where(remaining)[0]
60	        is_opt = find_pareto_optimal(points[idx])
61	        for k, i in enumerate(idx):
62	            if is_opt[k]:
63	                ranks[i] = rank
64	                remaining[i] = False
65	        rank += 1
66	    return ranks
67	
68	
69	def compute_hypervolume_2d(pareto_points, ref_point):
70	    """2D hypervolume: area dominated by Pareto front above reference point.
71	
72	    Sweep-line: sort Pareto points by x ascending (y non-increasing on front).
73	    HV = sum_i (x_i - x_{i-1}) * (y_i - ref_y), with x_{-1} = ref_x.
74	    """
75	    if len(pareto_points) == 0:
76	        return 0.0
77	    mask = (pareto_points[:, 0] > ref_point[0]) & (pareto_points[:, 1] > ref_point[1])
78	    pts = pareto_points[mask]
79	    if len(pts) == 0:
80	        return 0.0
81	    pts = pts[np.argsort(pts[:, 0])]
82	    hv = 0.0
83	    prev_x = ref_point[0]
84	    for i in range(len(pts)):
85	        hv += (pts[i, 0] - prev_x) * (pts[i, 1] - ref_point[1])
86	        prev_x = pts[i, 0]
87	    return hv
88	
89	
90	def load_data(args):
91	    """Load and merge EN probe quality + transfer results into per-language data."""
92	    with open(args.results_csv) as f:
93	        reader = csv.DictReader(f)
94	        transfer_rows = list(reader)
95	
96	    if not transfer_rows:
97	        print("ERROR: results_csv is empty", file=sys.stderr)
98	        sys.exit(1)
99	
100	    has_merged = (args.en_metric in transfer_rows[0] and
101	                  args.transfer_metric in transfer_rows[0])
102	
103	    if has_merged:
104	        data = defaultdict(list)
105	        for row in transfer_rows:
106	            lang = row.get("language", "all")
107	            if args.languages and lang not in args.languages:
108	                continue
109	            data[lang].append((
110	                int(row["layer"]),
111	                float(row[args.en_metric]),
112	                float(row[args.transfer_metric]),
113	            ))
114	        return data
115	
116	    if args.probe_csv is None:
117	        print(f"ERROR: results_csv lacks '{args.en_metric}' column. "
118	              f"Provide --probe_csv for EN probe quality.", file=sys.stderr)
119	        sys.exit(1)
120	
121	    transfer_data = defaultdict(dict)
122	    for row in transfer_rows:
123	        if row["method"] != args.method:
124	            continue
125	        lang = row["language"]
126	        if args.languages and lang not in args.languages:
127	            continue
128	        transfer_data[lang][int(row["layer"])] = float(row["auroc"])
129	
130	    en_data = {}
131	    with open(args.probe_csv) as f:
132	        reader = csv.DictReader(f)
133	        for row in reader:
134	            en_data[int(row["layer"])] = float(row["real_auroc"])
135	
136	    data = defaultdict(list)
137	    for lang, layer_map in transfer_data.items():
138	        for layer in sorted(layer_map):
139	            if layer not in en_data:
140	                print(f"WARNING: layer {layer} in transfer results but not in probe_csv, skipping",
141	                      file=sys.stderr)
142	                continue
143	            data[lang].append((layer, en_data[layer], layer_map[layer]))
144	    return data
145	
146	
147	def analyze(data, ref_point):
148	    """Run Pareto analysis on per-language data. Returns (detail_rows, summary_rows, json_dict)."""
149	    detail_rows = []
150	    summary_rows = []
151	    json_results = {"ref_point": ref_point.tolist(), "languages": {}}
152	
153	    for lang in sorted(data):
154	        entries = sorted(data[lang], key=lambda x: x[0])
155	        layers = np.array([e[0] for e in entries])
156	        en_vals = np.array([e[1] for e in entries])
157	        zs_vals = np.array([e[2] for e in entries])
158	        points = np.column_stack([en_vals, zs_vals])
159	
160	        is_pareto = find_pareto_optimal(points)
161	        ranks = compute_pareto_ranks(points)
162	        hv = compute_hypervolume_2d(points[is_pareto], ref_point)
163	        rho, p_val = stats.spearmanr(en_vals, zs_vals)
164	
165	        for i in range(len(layers)):
166	            detail_rows.append({
167	                "layer": int(layers[i]),
168	                "language": lang,
169	                "en_auroc": f"{en_vals[i]:.6f}",
170	                "zs_auroc": f"{zs_vals[i]:.6f}",
171	                "is_pareto_optimal": bool(is_pareto[i]),
172	                "pareto_rank": int(ranks[i]),
173	            })
174	
175	        pareto_layers = sorted(layers[is_pareto].astype(int).tolist())
176	        summary_rows.append({
177	            "language": lang,
178	            "hypervolume": f"{hv:.6f}",
179	            "spearman_rho": f"{rho:.4f}",
180	            "spearman_p": f"{p_val:.6f}",
181	            "n_pareto_optimal": int(is_pareto.sum()),
182	            "pareto_layers": str(pareto_layers),
183	            "n_layers": len(layers),
184	            "tradeoff": "yes" if rho < 0 else "no",
185	        })
186	
187	        json_results["languages"][lang] = {
188	            "hypervolume": round(hv, 6),
189	            "spearman_rho": round(float(rho), 4),
190	            "spearman_p": round(float(p_val), 6),
191	            "n_pareto_optimal": int(is_pareto.sum()),
192	            "pareto_layers": pareto_layers,
193	            "tradeoff": bool(rho < 0),
194	            "points": [
195	                {"layer": int(layers[i]), "en_auroc": round(float(en_vals[i]), 6),
196	                 "zs_auroc": round(float(zs_vals[i]), 6),
197	                 "is_pareto": True if is_pareto[i] else False,
198	                 "rank": int(ranks[i])}
199	                for i in range(len(layers))
200	            ],
201	        }
202	
203	        print(f"[{lang}] HV={hv:.4f}  rho={rho:+.3f} (p={p_val:.4f})  "
204	              f"Pareto: {pareto_layers}  tradeoff={'YES' if rho < 0 else 'NO'}")
205	
206	    return detail_rows, summary_rows, json_results
207	
208	
209	def write_outputs(detail_rows, summary_rows, json_results, output_dir, write_json):
210	    detail_path = os.path.join(output_dir, "pareto_detail.csv")
211	    with open(detail_path, "w", newline="") as f:
212	        w = csv.DictWriter(f, fieldnames=[
213	            "layer", "language", "en_auroc", "zs_auroc",
214	            "is_pareto_optimal", "pareto_rank"])
215	        w.writeheader()
216	        w.writerows(detail_rows)
217	    print(f"\nWrote {detail_path}")
218	
219	    summary_path = os.path.join(output_dir, "pareto_summary.csv")
220	    with open(summary_path, "w", newline="") as f:
221	        w = csv.DictWriter(f, fieldnames=[
222	            "language", "hypervolume", "spearman_rho", "spearman_p",
223	            "n_pareto_optimal", "pareto_layers", "n_layers", "tradeoff"])
224	        w.writeheader()
225	        w.writerows(summary_rows)
226	    print(f"Wrote {summary_path}")
227	
228	    if write_json:
229	        json_path = os.path.join(output_dir, "pareto_results.json")
230	        with open(json_path, "w") as f:
231	            json.dump(json_results, f, indent=2)
232	        print(f"Wrote {json_path}")
233	
234	
235	def main():
236	    parser = argparse.ArgumentParser(
237	        description="Pareto dominance analysis for cross-lingual probe transfer")
238	    parser.add_argument("--results_csv", required=True,
239	                        help="Transfer results CSV (or pre-merged CSV with en/zs columns)")
240	    parser.add_argument("--probe_csv", default=None,
241	                        help="EN probe quality CSV (layer, real_auroc). "
242	                             "Required if results_csv lacks --en_metric column.")
243	    parser.add_argument("--output_dir", default="./results")
244	    parser.add_argument("--en_metric", default="en_auroc",
245	                        help="EN probe quality column name (default: en_auroc)")
246	    parser.add_argument("--transfer_metric", default="zs_auroc",
247	                        help="Transfer quality column name (default: zs_auroc)")
248	    parser.add_argument("--method", default="zero_shot",
249	                        help="Transfer method to analyze (default: zero_shot)")
250	    parser.add_argument("--languages", nargs="+", default=None,
251	                        help="Target languages (default: all in CSV)")
252	    parser.add_argument("--ref_point", nargs=2, type=float, default=[0.5, 0.5],
253	                        metavar=("X", "Y"),
254	                        help="Reference point for hypervolume (default: 0.5 0.5)")
255	    parser.add_argument("--json", action="store_true",
256	                        help="Also output JSON")
257	    args = parser.parse_args()
258	
259	    os.makedirs(args.output_dir, exist_ok=True)
260	
261	    data = load_data(args)
262	    if not data:
263	        print("ERROR: no data after filtering", file=sys.stderr)
264	        sys.exit(1)
265	
266	    ref = np.array(args.ref_point)
267	    detail, summary, js = analyze(data, ref)
268	    write_outputs(detail, summary, js, args.output_dir, args.json)
269	
270	
271	if __name__ == "__main__":
272	    main()
273	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "baf5d610-adbc-4667-a13e-fc9e0faa736b",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "aaf80e1d-6f39-4477-b410-62970c67671e",
  "sourceToolAssistantUUID": "baf5d610-adbc-4667-a13e-fc9e0faa736b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T06:00:51.638Z_

<details open><summary>🔧 Tool call — Read · `toolu_0152C5o63gTc7qzA3VSEf7wN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/code/train_probe.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aaf80e1d-6f39-4477-b410-62970c67671e",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCoyw99DneRoqppuFmG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7dada5d5-c69d-4957-85d6-d7861cb1dbb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdSWYQ9DHPoNPH8hBTSQU6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18502,
      "cache_read_input_tokens": 33656,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18502
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 33656,
          "cache_creation_input_tokens": 18502,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18502,
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

_source line 41 · 2026-05-21T06:00:51.647Z_

<details><summary>↩ Tool result · `toolu_0152C5o63gTc7qzA3VSEf7wN`</summary>

```text
1	"""
2	Train per-layer correctness probes (logistic regression) on English activations.
3	
4	For each layer, trains an L2-regularized LogisticRegression on 80% of the
5	English data and evaluates on the held-out 20%. Reports AUROC, ECE, Brier score.
6	
7	Input:  .pt files from extract_activations.py  (e.g. activations/layer8_en.pt)
8	Output: probe pickle files + train_metrics.csv
9	
10	Usage:
11	  python train_probe.py \
12	    --activations_dir ./activations \
13	    --output_dir ./probes \
14	    --layers 0,4,8,12,16,20,24,28,31
15	"""
16	
17	import argparse
18	import os
19	import pickle
20	
21	import numpy as np
22	import torch
23	from sklearn.linear_model import LogisticRegression
24	from sklearn.model_selection import train_test_split
25	from sklearn.preprocessing import StandardScaler
26	from sklearn.metrics import roc_auc_score, brier_score_loss
27	
28	
29	def parse_args():
30	    p = argparse.ArgumentParser()
31	    p.add_argument("--activations_dir", default="./activations")
32	    p.add_argument("--output_dir", default="./probes")
33	    p.add_argument("--layers", default=None,
34	                   help="Comma-separated layer indices. Default: auto-detect from activations_dir")
35	    p.add_argument("--test_size", type=float, default=0.2)
36	    p.add_argument("--seed", type=int, default=42)
37	    p.add_argument("--C", type=float, default=1.0, help="Inverse regularization strength")
38	    p.add_argument("--max_iter", type=int, default=2000)
39	    return p.parse_args()
40	
41	
42	def compute_ece(probs, labels, n_bins=10):
43	    """Histogram-based Expected Calibration Error (10 equal-width bins)."""
44	    bin_edges = np.linspace(0, 1, n_bins + 1)
45	    ece = 0.0
46	    for lo, hi in zip(bin_edges[:-1], bin_edges[1:]):
47	        mask = (probs > lo) & (probs <= hi)
48	        if lo == 0.0:
49	            mask = (probs >= lo) & (probs <= hi)
50	        n_in_bin = mask.sum()
51	        if n_in_bin == 0:
52	            continue
53	        avg_conf = probs[mask].mean()
54	        avg_acc = labels[mask].mean()
55	        ece += (n_in_bin / len(probs)) * abs(avg_acc - avg_conf)
56	    return ece
57	
58	
59	def main():
60	    args = parse_args()
61	    if args.layers is None:
62	        import glob
63	        available = sorted(set(
64	            int(os.path.basename(f).split('_')[0].replace('layer', ''))
65	            for f in glob.glob(os.path.join(args.activations_dir, 'layer*_en.pt'))
66	        ))
67	        if not available:
68	            raise RuntimeError(f"No layer*_en.pt files found in {args.activations_dir}")
69	        print(f"Auto-detected layers: {available}")
70	        layer_indices = available
71	    else:
72	        layer_indices = sorted(int(x) for x in args.layers.split(","))
73	    os.makedirs(args.output_dir, exist_ok=True)
74	
75	    results = []
76	    print(f"{'Layer':>5s} {'N_train':>7s} {'N_test':>6s} {'AUROC':>7s} {'ECE':>7s} {'Brier':>7s}")
77	    print("-" * 46)
78	
79	    for li in layer_indices:
80	        pt_path = os.path.join(args.activations_dir, f"layer{li}_en.pt")
81	        if not os.path.exists(pt_path):
82	            print(f"  [SKIP] {pt_path} not found")
83	            continue
84	
85	        data = torch.load(pt_path, weights_only=True)
86	        X = data["activations"].numpy()
87	        y = data["labels"].numpy()
88	
89	        if len(np.unique(y)) < 2:
90	            print(f"  [SKIP] Layer {li}: only one class present (all correct or all wrong)")
91	            continue
92	
93	        X_train, X_test, y_train, y_test = train_test_split(
94	            X, y, test_size=args.test_size, random_state=args.seed, stratify=y,
95	        )
96	
97	        scaler = StandardScaler()
98	        X_train_s = scaler.fit_transform(X_train)
99	        X_test_s = scaler.transform(X_test)
100	
101	        clf = LogisticRegression(
102	            C=args.C, penalty="l2", solver="lbfgs", max_iter=args.max_iter, random_state=args.seed,
103	        )
104	        clf.fit(X_train_s, y_train)
105	
106	        probs = clf.predict_proba(X_test_s)[:, 1]
107	        auroc = roc_auc_score(y_test, probs)
108	        ece = compute_ece(probs, y_test)
109	        brier = brier_score_loss(y_test, probs)
110	
111	        print(f"{li:>5d} {len(y_train):>7d} {len(y_test):>6d} {auroc:>7.4f} {ece:>7.4f} {brier:>7.4f}")
112	
113	        probe_path = os.path.join(args.output_dir, f"probe_layer{li}.pkl")
114	        with open(probe_path, "wb") as f:
115	            pickle.dump({"scaler": scaler, "model": clf}, f)
116	
117	        results.append({
118	            "layer": li,
119	            "n_train": len(y_train),
120	            "n_test": len(y_test),
121	            "auroc": auroc,
122	            "ece": ece,
123	            "brier": brier,
124	            "probe_path": probe_path,
125	        })
126	
127	    csv_path = os.path.join(args.output_dir, "train_metrics.csv")
128	    with open(csv_path, "w") as f:
129	        f.write("layer,n_train,n_test,auroc,ece,brier\n")
130	        for r in results:
131	            f.write(f"{r['layer']},{r['n_train']},{r['n_test']},{r['auroc']:.6f},{r['ece']:.6f},{r['brier']:.6f}\n")
132	    print(f"\nMetrics saved to {csv_path}")
133	    print(f"Probes saved to {args.output_dir}/")
134	
135	
136	if __name__ == "__main__":
137	    main()
138	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dada5d5-c69d-4957-85d6-d7861cb1dbb1",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "3847217f-8c89-462e-afaf-bfc173f547c9",
  "sourceToolAssistantUUID": "7dada5d5-c69d-4957-85d6-d7861cb1dbb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-21T06:00:54.893Z_

Now let me check the dream review reports for additional context on what reviewers have already flagged.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3847217f-8c89-462e-afaf-bfc173f547c9",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCpPT1DGLXDPJfNRrJQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d47d0e81-7e5b-480c-abaa-d83e2ef8d540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L89nsjyXsjPdFAMMsrg1uE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7874,
      "cache_read_input_tokens": 52158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7874,
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

_source line 43 · 2026-05-21T06:00:57.020Z_

<details open><summary>🔧 Tool call — Read · `toolu_018gghC6pctjJrzbro8hEh9u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T044911/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d47d0e81-7e5b-480c-abaa-d83e2ef8d540",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCpPT1DGLXDPJfNRrJQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "338cea61-1090-4a2f-8c39-3c014d17b101",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L89nsjyXsjPdFAMMsrg1uE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7874,
      "cache_read_input_tokens": 52158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7874,
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

_source line 44 · 2026-05-21T06:00:57.027Z_

<details><summary>↩ Tool result · `toolu_018gghC6pctjJrzbro8hEh9u`</summary>

```text
1	---
2	dream_id: dream_20260521T044911
3	tier: best
4	overall_score: 3.5/5 — Findings-worthy
5	timestamp: 2026-05-21T05:57:23.078791+00:00
6	---
7	
8	# Dream Review Report: "Geometric Analysis Reveals When and Why Cross-Lingual Calibration Transfer Succeeds"
9	
10	**Dream ID**: 20260521T044911  
11	**Review Mode**: full  
12	**Venue**: ACL ARR (no venue specified; defaulting to ACL Rolling Review 1–5 scale)  
13	**Reviewers**: R1 (Methods & Experiments), R2 (Novelty & Related Work)
14	
15	---
16	
17	## Consolidated Scores
18	
19	| Dimension | R1 | R2 | Final |
20	|-----------|----|----|-------|
21	| Soundness | 4/5 | — | **4/5** |
22	| Excitement | — | 3.5/5 | **3.5/5** |
23	| Overall Assessment | 3.5/5 | 3.5/5 | **3.5/5** |
24	
25	**Recommendation**: Findings-worthy at a top \*CL venue (ACL/EMNLP/NAACL Findings).
26	
27	---
28	
29	## Paper Summary
30	
31	The paper presents the first large-scale study of cross-lingual correctness probe transfer across three architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20–50 languages, and five transfer conditions. Four claims form a causal chain: (1) an architecture-dependent depth-transferability Pareto frontier (Qwen strong ρ=−0.91, Llama weak ρ=−0.78, knee at 55–58% depth); (2) a difficulty-capability decomposition showing capability drives 88% of transfer degradation despite only 35% of variance; (3) CaCLR, a consistency-regularized calibration method providing +3.5pp AUROC over zero-shot without target labels; (4) a Simpson's Paradox in the CKA–transfer relationship — raw correlation negative (depth confound), partial correlation positive (p < 0.01 on all three architectures). Additional findings include 27% low-resource probing artifacts, Procrustes reversal at ZS AUROC ~0.52, and ~42 parallel pairs for 95% Procrustes performance.
32	
33	---
34	
35	## Experiment Coverage Assessment
36	
37	All 13 experiments from the design plan are reflected in the paper:
38	
39	| Plan | Experiment | Status in Paper |
40	|------|-----------|----------------|
41	| plan_001 | Qwen3-235B Pareto | §5.1, Table 2 |
42	| plan_002 | Llama 4 Scout Pareto | §5.1, Tables 3–5 |
43	| plan_011 | CKA & Simpson's Paradox | §5.2, Tables 6–8 |
44	| plan_003 | CaCLR Implementation | §5.4, Tables 11–13 |
45	| plan_004 | Decomposition | §5.3, Tables 9–10 |
46	| plan_012 | Linear Projection Sensitivity | §5.5, Tables 14–15 |
47	| plan_013 | Control Tasks | §5.6, Tables 16–17 |
48	| plan_005 | Orthogonality | §5.7, Table 18 |
49	| plan_006 | Probe Complexity | §6.1, Table 19 |
50	| plan_007 | Cross-Benchmark | §6.2, Table 20 |
51	| plan_010 | Quantization Validation | §6.3, Table 21 |
52	| plan_008 | Gemma 4 31B | §6.4, Table 1 |
53	| plan_009 | Extended 50 Languages | §6.5, Table 22 |
54	
55	**Coverage: 13/13 (100%).** The paper faithfully reflects the full experiment plan.
56	
57	---
58	
59	## R1 Review: Methods and Experiments
60	
61	### Soundness Score: 4/5
62	
63	### Strengths
64	
65	1. **Comprehensive experimental design with strong controls.** 13 experiments systematically cover all four claims with appropriate P0 (core), P1 (robustness), and P2 (extension) prioritization. The progression from MVP (7–8B, 5 languages) to full-scale (235B, 20 languages) is methodologically sound.
66	
67	2. **Rigorous probing methodology.** Hewitt & Liang control tasks with selectivity analysis (§5.6) are essential and often omitted. The 27% low-resource artifact rate is a genuine methodological contribution that challenges prior cross-lingual probing studies.
68	
69	3. **Mean-shift invariance proof is clean.** The mathematical argument that StandardScaler + logistic regression makes mean-shift AUROC-invariant is correct and experimentally verified (ΔAUROC = 0.000). This clearly differentiates from Xiao et al.'s pipeline.
70	
71	4. **Simpson's Paradox analysis is well-designed.** Partial Spearman correlation controlling for normalized depth is the correct approach. Bootstrap CIs (95%) are reported for both architectures. Per-layer cross-language correlations (Table 7) provide independent non-parametric support.
72	
73	5. **CaCLR is well-specified and reproducible.** Loss function fully specified (Eq. 2–3), optimizer details given, β sweep across three orders of magnitude, component ablation (BCE-only → +SB-ECE → +consistency → full), initialization from sklearn LR solution.
74	
75	6. **Quantization validation addresses a key confound.** W4A16 (Llama) and GPTQ-Int4 (Qwen) vs FP16 baselines show ≤0.5pp mean AUROC difference and rank correlation ≥0.994 (Table 21), confirming Pareto frontier ordering is preserved.
76	
77	7. **Cross-benchmark generalization with low variance.** CaCLR improvement is consistent across GlobalMMLU (+3.5pp), Belebele (+3.3pp), MMLU-ProX (+3.5pp) with CV = 0.04, defending against overfitting concerns.
78	
79	### Weaknesses
80	
81	1. **Procrustes train/eval separation is unclear.** The linear projection evaluation should explicitly exclude training pairs from the evaluation set. If Procrustes alignment and evaluation share items, the +1.9pp claim for LinProj(200) is optimistically biased. The full-scale protocol (70/30 split) should be verified to enforce this separation at the Procrustes level, not just the CaCLR level.
82	
83	2. **CaCLR hyperparameter selection uses English-only metrics.** The β sweep (Table 11) selects the optimal β=0.05 based on combined AUROC and ECE on English data. If the consistency loss (β > 0) happens to hurt English performance, the sweep would select against it. A proper protocol would include at least a few validation languages in the selection criterion, or demonstrate that the English-optimal β is also cross-lingually optimal.
84	
85	3. **IRT difficulty source is not specified.** The decomposition (§5.3) requires item-level difficulty scores. GlobalMMLU does not include IRT parameters. If difficulty is estimated from model performance, circularity arises (model accuracy → difficulty estimate → projected out of representations → retrained probe evaluated on model accuracy). The paper should clarify whether external human annotations are used.
86	
87	4. **Single random seed for CaCLR and few-shot evaluations.** Given the effect sizes (+3.5pp CaCLR, +1.7pp few-shot-100 vs zero-shot), variance across initialization seeds should be quantified. With 25 labeled examples for few-shot, seed-dependent variance could be substantial.
88	
89	5. **The decomposition lacks a rigorous identification strategy.** Projecting out a single difficulty direction assumes difficulty is linearly encoded in one dimension. The residual still contains difficulty information encoded nonlinearly or in correlated directions. The random-direction control (−1.2pp) addresses dimensionality reduction artifacts but not this fundamental issue. A stronger test would vary projection rank or use held-out difficulty annotations.
90	
91	6. **ECE binning inconsistency.** The paper uses 10 equal-width bins for ECE computation but some design documents reference 15 bins. Equal-width binning is sensitive to bin count; reporting results at multiple bin counts (or using adaptive binning) would strengthen calibration claims.
92	
93	7. **No cross-validation for primary probes.** English probes use a single 80/20 split. Five-fold CV with variance estimates would strengthen the EN AUROC claims and provide confidence intervals for downstream transfer metrics.
94	
95	### Questions for Authors
96	
97	1. Can you confirm the Procrustes evaluation excludes training pairs?
98	2. How are IRT difficulty scores sourced? Is there a circularity risk?
99	3. What is the variance of CaCLR results across 3–5 random seeds?
100	4. Have you considered a mixed English + cross-lingual criterion for the CaCLR β sweep?
101	5. The subspace angle analysis (12.4° within-layer, 38.7° cross-layer) — how exactly is this computed? Is it the angle between logistic regression weight vectors w_l across languages, or a PCA-based subspace comparison?
102	6. CaCLR gains at deep layers are reported as +4.8pp (mean). What is the per-language variance? Does this hold for LOW-tier languages?
103	
104	### Detailed Claim Assessment
105	
106	**Claim 1 (Pareto)**: Well-supported. Per-language Spearman ρ is the right metric. Architecture comparison (Qwen 15/20 significant vs Llama 6/20) is convincing. The convergent best-transfer depth at 55–58% across architectures is a clean finding. Main limitation: n=3 architectures, confounded by scale/type/training data differences.
107	
108	**Claim 2 (Decomposition)**: Conceptually sound, methodologically weakest. The 65/35 variance split with 12/88 degradation asymmetry is striking, but the linear single-direction projection is a strong assumption. The random-direction control is necessary but not sufficient. The prescriptive accuracy (78%) adds practical value but needs confidence intervals.
109	
110	**Claim 3 (CaCLR)**: Method is well-implemented and honestly framed. The 1-D MMD limitation is acknowledged. The β sweep is thorough. Main concerns: English-only hyperparameter selection, modest improvement over linear projection (+1.5pp), parallel activation requirement is understated.
111	
112	**Claim 4 (CKA/Simpson)**: Strongest claim methodologically. Partial correlation is the correct approach, bootstrap CIs exclude zero, three-architecture replication with consistent p < 0.01. The CKA cliff threshold (0.35) connecting to Procrustes reversal (0.52) is elegant. Concern: potential tautology (both CKA and AUROC measure EN-target similarity).
113	
114	---
115	
116	## R2 Review: Novelty, Significance, and Related Work
117	
118	### Excitement Score: 3.5/5
119	
120	### Strengths
121	
122	1. **Simpson's Paradox finding is genuinely novel and non-trivial.** The sign reversal from negative raw correlation to positive partial correlation across all three architectures is not predicted by prior work. This is the paper's standout contribution — a real geometric insight with explanatory power.
123	
124	2. **First large-scale cross-lingual correctness probe study.** The entire probe-based calibration literature (CORAL, CCPS, Miao & Ungar) is English-only. This paper fills a genuine gap.
125	
126	3. **Control task artifact finding has field-level impact.** The 27% low-resource artifact rate is the first application of Hewitt & Liang controls to cross-lingual probing. This directly challenges the reliability of prior work (including Xiao et al.) and should influence methodological standards.
127	
128	4. **Difficulty-capability decomposition extends Civelli et al. meaningfully.** Going from "difficulty transfers cross-lingually" to "capability drives 88% of transfer *degradation*" is a non-trivial insight. The 78% prescriptive accuracy for strategy selection adds practical value.
129	
130	5. **Causal chain structure is well-argued.** The four claims genuinely build on each other: Pareto establishes phenomenon → decomposition reveals mechanism → CaCLR tests intervention → CKA provides geometric grounding. This is not four papers stapled together but a coherent narrative.
131	
132	6. **Practical guidelines are actionable.** (1) Select layers at 55–60% depth, (2) check ZS AUROC before applying Procrustes (threshold ~0.52), (3) ~42 parallel pairs suffice for 95% performance, (4) apply selectivity controls for low-resource languages.
133	
134	### Weaknesses
135	
136	1. **CaCLR's method novelty is limited.** BCE + SB-ECE + 1-D MMD is a standard combination. The +3.5pp gain is real but modest. The paper frames CaCLR as a "positive method contribution" in the causal chain, but it is more accurately a systematic evaluation showing that distributional matching helps within bounds. The "no target labels" framing understates the requirement for parallel activations (running inference on target-language inputs).
137	
138	2. **Architecture-dependent claims rest on n=3 architectures.** "Strong on Qwen, weak on Llama, intermediate on Gemma" is an observation, not a generalizable finding. The architectures differ simultaneously in type (MoE vs dense), scale, layer count, and training data. The paper cannot attribute tradeoff differences to specific architectural features. This is acknowledged in Limitations but the main text still presents architecture dependence as a core claim rather than an observation.
139	
140	3. **Potential tautology in CKA-transfer correlation.** CKA measures EN-target representation similarity. Transfer AUROC also reflects EN-target alignment quality. The positive partial correlation may partly reflect measurement overlap rather than genuine geometric prediction. The subspace angle analysis partially addresses this (correctness direction persists even as global CKA declines), but the tautology concern deserves more prominent discussion.
141	
142	4. **MCQA-only scope limits the "when and why" title claim.** The title suggests general insights, but all findings are specific to MCQA correctness probing. Whether the Pareto frontier, decomposition, CKA relationship, and CaCLR improvements extend to open-ended generation or other task formats is unknown and undiscussed.
143	
144	5. **Some numbers appear suspiciously consistent.** CaCLR gains of +3.5, +3.3, +3.5 across three benchmarks (CV=0.04) are remarkably uniform. Per-language variance and confidence intervals should be reported to demonstrate these are real measurements with natural variation.
145	
146	6. **Mean-shift invariance is overclaimed.** The mathematical fact that StandardScaler + LR makes mean-shift AUROC-invariant is straightforward. The paper devotes non-trivial space to this, but the insight is about preprocessing pipeline choices, not about correctness vs. answerability probing.
147	
148	### Novelty Assessment per Claim
149	
150	| Claim | Novelty | Rationale |
151	|-------|---------|-----------|
152	| 1. Pareto | Incremental | Intuitive from domain adaptation theory; Civelli et al. showed architecture-dependent optimal depth. Contribution is quantification and Pareto framing. |
153	| 2. Decomposition | Moderate-to-solid | Extends Civelli's difficulty finding to decompose *transfer degradation*. The 12%/88% asymmetry is non-trivial. |
154	| 3. CaCLR | Low (method), Moderate (evaluation) | Standard components; value is in systematic evaluation showing bounds of 1-D distributional matching. |
155	| 4. CKA/Simpson | **High** | Sign reversal across three architectures is non-trivial. Subspace angle analysis provides mechanism. Connection to Procrustes threshold is elegant. |
156	
157	### Related Work Gaps
158	
159	1. **Burns et al. (2023), "Discovering Latent Knowledge" (CCS)**: Unsupervised probe training via consistency constraints is conceptually similar to CaCLR's consistency loss. Should be discussed.
160	2. **Kadavath et al. (2022), "Language Models (Mostly) Know What They Know"**: Foundational work on self-knowledge motivating correctness probing. Currently uncited.
161	3. **Wendler et al. (2024), "Do Llamas Work in English?"**: Studies language-specific vs. shared processing in multilingual LLMs. Directly relevant.
162	4. **Zhao et al. (2024, ICLR), "LLMs Are Not Robust MC Selectors"**: MCQA-specific calibration issues (option bias) may interact with correctness signal.
163	5. **Ravisankar et al. (DALI, EACL 2026)**: Causal evidence via activation patching that English middle-layer representations fix non-English errors. Directly supports this paper's hypothesis.
164	
165	### Significance and Impact
166	
167	**Significance: moderate-to-high.** Fills a genuine gap (English-only calibration probing literature). Simpson's Paradox and control task findings will influence methodology. Practical guidelines are directly usable.
168	
169	**Impact trajectory:** More likely to influence *methodology* (how people do cross-lingual probing) than *deployed systems* (CaCLR gains modest, MCQA-only). The control task warning may have the broadest impact — it applies to all cross-lingual probing studies.
170	
171	**Appropriate venue:** Findings track at ACL/EMNLP. The paper is primarily analytical/empirical. CaCLR alone would not support a main conference method paper, but the causal chain and geometric analysis elevate it above typical Findings.
172	
173	### Writing and Presentation
174	
175	- **Organization**: Well-structured. Causal chain ordering provides clear narrative arc.
176	- **Clarity**: Generally clear. CaCLR, CKA analysis, and decomposition are accessible.
177	- **Table density**: Very high (23+ tables). Some could be consolidated. The paper would benefit from 2–3 key figures (Pareto frontier scatter, Simpson's Paradox panel, CaCLR depth profile) that visually convey core findings. The PDF references figures but figure quality and placement were not evaluable in this review format.
178	- **Xiao et al. differentiation**: The answerability vs. correctness distinction is stated clearly and reinforced. A concrete example of their divergence would strengthen it further.
179	- **Length**: Appropriate. Mean-shift discussion could be shortened to make room for scope/limitation discussion.
180	
181	---
182	
183	## Roundtable Synthesis
184	
185	### Areas of Agreement
186	
187	1. **Simpson's Paradox (Claim 4) is the paper's strongest and most novel contribution.** Both reviewers identify it as genuinely non-trivial, well-executed statistically, and replicated across three architectures.
188	
189	2. **The 27% control task artifact finding is a field-level methodological contribution.** First cross-lingual application of probing controls.
190	
191	3. **CaCLR's method novelty is limited**, but its systematic evaluation within the causal chain adds value. The honest acknowledgment of the 1-D constraint is a positive.
192	
193	4. **The decomposition is conceptually sound but methodologically the weakest claim.** IRT difficulty source and linear projection assumption need clarification.
194	
195	5. **n=3 architectures genuinely limits architecture-dependent claims.** The paper correctly frames this as observational but could be more conservative in the abstract and conclusion.
196	
197	6. **The paper is Findings-worthy** at a top \*CL venue. The causal chain structure, Simpson's Paradox, and control task finding elevate it above typical probing papers. CaCLR alone would not justify main conference acceptance.
198	
199	### Areas of Disagreement (resolved)
200	
201	- R1 rated the experimental design more highly (comprehensive plan, good controls), while R2 questioned whether reported numbers might be projections. **Resolution**: Both concerns are valid. The experimental *design* is strong (4/5 soundness), but the review cannot verify whether final numbers are from completed experiments. This should be noted as a caveat.
202	
203	- R2 rated the tautology concern in CKA-transfer more severely than R1. **Resolution**: The concern is legitimate but partially mitigated by the subspace angle analysis. The paper should add a paragraph explicitly addressing why the positive partial correlation is informative beyond measurement overlap.
204	
205	### Top-Level Recommendations
206	
207	1. **Strengthen the tautology discussion.** Add explicit argument for why CKA partial correlation is informative beyond both metrics measuring EN-target similarity.
208	2. **Clarify IRT difficulty source** and address circularity risk.
209	3. **Add multi-seed variance** for CaCLR and few-shot results.
210	4. **Verify Procrustes train/eval separation** in the evaluation code.
211	5. **Cite missing related work**: Burns et al. (CCS), Kadavath et al., Wendler et al., Ravisankar et al. (DALI).
212	6. **Soften architecture-dependent framing** to "observation across three architectures" rather than implying causal attribution.
213	7. **Add per-language confidence intervals** for CaCLR gains to address the suspiciously uniform cross-benchmark numbers.
214	8. **Reduce mean-shift discussion** and expand scope/limitations.
215	
216	---
217	
218	## Final Assessment
219	
220	| Dimension | Score | Justification |
221	|-----------|-------|---------------|
222	| Soundness | **4/5 (Strong)** | Experimental design is comprehensive with appropriate controls. Statistical methodology is correct. Minor concerns about train/eval separation, single seeds, IRT source. |
223	| Excitement | **3.5/5** | Simpson's Paradox is exciting and novel. Control task finding has field-level impact. Decomposition is solid. CaCLR is useful but not exciting as a method. MCQA-only scope limits broader excitement. |
224	| Overall | **3.5/5 (Findings-worthy)** | Strong analytical work filling a genuine gap. Four-claim causal chain is coherent and well-supported. Primarily empirical/analytical contribution with modest method novelty. Appropriate for Findings at ACL/EMNLP. |
225	
226	**Verdict**: The paper makes a solid contribution to cross-lingual calibration probing with one genuinely novel geometric insight (Simpson's Paradox), a useful methodological warning (control task artifacts), and a well-executed empirical analysis. CaCLR is honest about its limitations. The main weaknesses are the limited architecture count for causal claims, underspecified decomposition methodology, and scope limited to MCQA. With the recommended revisions (tautology discussion, IRT clarification, multi-seed variance, missing citations), this is a strong Findings paper.
227	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "338cea61-1090-4a2f-8c39-3c014d17b101",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "0c67940e-2759-4a2b-ad5d-feaa49c8088c",
  "sourceToolAssistantUUID": "338cea61-1090-4a2f-8c39-3c014d17b101",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T06:00:57.429Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hgf723VXfrfaBhgSc4Lru1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/partial_correlation_pilot.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c67940e-2759-4a2b-ad5d-feaa49c8088c",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCpPT1DGLXDPJfNRrJQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "098d0356-00c9-41d7-a83b-7798ea7a384f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L89nsjyXsjPdFAMMsrg1uE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7874,
      "cache_read_input_tokens": 52158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7874,
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

_source line 46 · 2026-05-21T06:00:57.433Z_

<details><summary>↩ Tool result · `toolu_01Hgf723VXfrfaBhgSc4Lru1`</summary>

```text
1	# Partial Correlation Pilot: CKA vs Transfer AUROC (Controlling for Depth)
2	
3	**Date**: 2026-05-21  
4	**Purpose**: Test whether CKA has independent explanatory power for transfer AUROC beyond depth confound.
5	
6	## Key Finding: Simpson's Paradox
7	
8	The raw pooled correlation is misleading. Controlling for depth **reverses the sign** from negative to positive — a textbook Simpson's paradox.
9	
10	## Results
11	
12	### Qwen2.5-7B (n=40, 8 layers x 5 languages)
13	
14	| Metric | rho | p-value | Sig |
15	|--------|-----|---------|-----|
16	| Raw Spearman(CKA, AUROC) | -0.1645 | 0.310 | ns |
17	| Partial Spearman (ctrl depth) | **+0.1796** | 0.274 | ns |
18	| CKA ~ depth | -0.4632 | 0.003 | ** |
19	| AUROC ~ depth | +0.6238 | <0.001 | *** |
20	
21	Per-layer cross-language Spearman(CKA, AUROC):
22	
23	| Layer | Depth | rho | p |
24	|-------|-------|-----|---|
25	| 0 | 0.00 | -0.10 | 0.873 |
26	| 4 | 0.15 | +0.50 | 0.391 |
27	| 8 | 0.30 | **+1.00** | <0.001 |
28	| 12 | 0.44 | **+0.90** | 0.037 |
29	| 16 | 0.59 | **+1.00** | <0.001 |
30	| 20 | 0.74 | +0.30 | 0.624 |
31	| 24 | 0.89 | +0.80 | 0.104 |
32	| 27 | 1.00 | +0.80 | 0.104 |
33	
34	**Median per-layer rho: +0.80**
35	
36	### Llama-3.1-8B (n=45, 9 layers x 5 languages)
37	
38	| Metric | rho | p-value | Sig |
39	|--------|-----|---------|-----|
40	| Raw Spearman(CKA, AUROC) | -0.1598 | 0.294 | ns |
41	| Partial Spearman (ctrl depth) | **+0.4093** | 0.006 | ** |
42	| CKA ~ depth | -0.5852 | <0.001 | *** |
43	| AUROC ~ depth | +0.6859 | <0.001 | *** |
44	
45	Per-layer cross-language Spearman(CKA, AUROC):
46	
47	| Layer | Depth | rho | p |
48	|-------|-------|-----|---|
49	| 0 | 0.00 | -0.20 | 0.747 |
50	| 4 | 0.13 | +0.40 | 0.505 |
51	| 8 | 0.26 | +0.10 | 0.873 |
52	| 12 | 0.39 | +0.80 | 0.104 |
53	| 16 | 0.52 | **+0.90** | 0.037 |
54	| 20 | 0.65 | +0.40 | 0.505 |
55	| 24 | 0.77 | +0.60 | 0.285 |
56	| 28 | 0.90 | +0.60 | 0.285 |
57	| 31 | 1.00 | +0.80 | 0.104 |
58	
59	**Median per-layer rho: +0.60**
60	
61	## Interpretation
62	
63	### The Simpson's Paradox mechanism
64	
65	1. **CKA decreases with depth** (rho ~ -0.5): deeper layers have more language-specific representations
66	2. **Transfer AUROC increases with depth** (rho ~ +0.65): deeper representations are more discriminative for calibration
67	3. **Pooling across depths**: the opposing depth trends create a spurious negative correlation
68	4. **Within each layer**: higher CKA (more similar representations) -> higher transfer AUROC — the relationship is **positive**
69	
70	### Statistical strength
71	
72	- **Llama**: Partial rho = +0.41, p = 0.006 — statistically significant, medium-large effect
73	- **Qwen**: Partial rho = +0.18, p = 0.27 — same positive direction, but underpowered (n=40, only 8 layers sampled)
74	- **Per-layer analysis**: 14/17 layer-level correlations are positive across both models; median rho ~ +0.70 combined
75	
76	### Note on methods
77	
78	AUROC is identical for zero_shot and mean_shift (AUROC measures ranking, not calibration), so the analysis applies to both methods.
79	
80	## Conclusion
81	
82	**YES — CKA has independent explanatory power beyond depth, and the story is stronger than a simple negative correlation.**
83	
84	The finding is a Simpson's paradox:
85	- **Naive claim** (wrong): "CKA and transfer AUROC are uncorrelated (rho ~ -0.16, ns)"
86	- **Correct claim**: "CKA positively predicts transfer AUROC within each depth level (partial rho up to +0.41**, per-layer median rho +0.70), but this is masked by opposing depth trends"
87	
88	### Novelty assessment
89	
90	This **strengthens** the paper's novelty:
91	1. The depth confound is real and must be controlled — addresses Reviewer's concern directly
92	2. The sign reversal (Simpson's paradox) is a publishable finding in itself
93	3. The mechanistic story is clean: at each depth, languages with more similar representations to English transfer calibration directions better
94	4. Limitation: n=5 languages per layer is small; the per-layer p-values should be treated as directional evidence, not confirmatory
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "098d0356-00c9-41d7-a83b-7798ea7a384f",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "a87ba083-cd7b-4f09-b944-d1f1fb2af078",
  "sourceToolAssistantUUID": "098d0356-00c9-41d7-a83b-7798ea7a384f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-21T06:01:01.694Z_

Now I have comprehensive context. Let me also check the writing plan and literature map for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a87ba083-cd7b-4f09-b944-d1f1fb2af078",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCppSR8v7Wf6seau55j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de74c5bf-591e-4e4b-92e7-ca8bb9e518c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Taq53rcJaMbPFsZ7yeiaeG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7875,
      "cache_read_input_tokens": 60032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7875,
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

_source line 48 · 2026-05-21T06:01:02.814Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HTtmTopPd4KvfU1eTaSXFj`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de74c5bf-591e-4e4b-92e7-ca8bb9e518c4",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCppSR8v7Wf6seau55j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "861acec4-ab09-47f9-84fb-250e47e6f721",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Taq53rcJaMbPFsZ7yeiaeG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7875,
      "cache_read_input_tokens": 60032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7875,
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

_source line 49 · 2026-05-21T06:01:02.828Z_

<details><summary>↩ Tool result · `toolu_01HTtmTopPd4KvfU1eTaSXFj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EACL 2027\\n  track: long\\n  template: docs/paper/  # ACL style files (acl.sty, acl_natbib.bst) from github.com/acl-org/acl-style-files\\n  template_note: \\\"Downloaded 2026-05-21 from official acl-org/acl-style-files repo.\\\"\\n  page_limit: 8\\n  deadline: 2026-08-03\\n  core_claim: >-\\n    Cross-lingual correctness probe transfer reveals an architecture-dependent\\n    depth-transferability tradeoff; the natural distributional-matching approach\\n    (CaCLR) fails, but linear projection with ~50 parallel pairs is the practical\\n    solution. A Simpson's Paradox in CKA-transfer provides geometric insight into\\n    when and why transfer succeeds.\\n  created_at: 2026-05-21T08:00:00Z\\n  terminology_fixes:\\n    - old: \\\"zero-label\\\"\\n      new: \\\"zero-correctness-label\\\"\\n    - old: \\\"First systematic study\\\"\\n      new: \\\"First large-scale study comparing correctness probe transfer across architectures\\\"\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 220\\n    core_bullets:\\n      - \\\"Problem: Non-English languages suffer 5x worse calibration; all probe-based calibration methods are English-only\\\"\\n      - \\\"Approach: First large-scale study — 2+ architectures × 20 languages × 5 transfer methods on GlobalMMLU\\\"\\n      - \\\"Finding 1: Architecture-dependent Pareto frontier (Qwen strong tradeoff, Llama language-specific)\\\"\\n      - \\\"Finding 2: Simpson's Paradox in CKA-transfer — raw negative, partial positive (geometric insight)\\\"\\n      - \\\"Finding 3: ~28% low-resource probing results are capacity artifacts (control task warning)\\\"\\n      - \\\"Finding 4: Linear projection ~50 pairs achieves 98% of full performance; Procrustes reversal at AUROC>0.60\\\"\\n      - \\\"Finding 5: CaCLR distributional matching fails — geometric analysis explains why\\\"\\n    dependencies: [experiments, method, introduction]\\n\\n  - section: introduction\\n    word_budget: 1000\\n    core_bullets:\\n      - \\\"Hook: Non-English LLM users face 5x worse calibration (ECE gap, cite LACE), yet all probe-based calibration methods operate English-only\\\"\\n      - \\\"Gap: Fixes require per-language labels (LACE) or 5x inference cost (MKA); nobody has tested correctness probe transfer multilingually. Xiao et al. probed knowledge boundaries (input-level answerability), not correctness (output-dependent accuracy)\\\"\\n      - \\\"Insight: Correctness direction occupies language-agnostic low-dimensional subspace, but transfer governed by architecture-specific depth dynamics and a Simpson's Paradox in geometric alignment\\\"\\n      - \\\"Approach: Systematic comparison of 5 transfer methods across architectures and 20 languages; CaCLR tests distributional matching; difficulty-capability decomposition explains failure modes\\\"\\n      - \\\"Contributions: (1) architecture-dependent Pareto discovery + CKA geometric analysis with Simpson's Paradox, (2) 28% control-task artifact warning for the field, (3) linear projection practical recipe (~50 pairs, resource-tier stratification), (4) CaCLR principled negative result + decomposition analysis\\\"\\n    dependencies: [experiments, method]\\n    figures: [fig1_pareto]\\n    citation_hints:\\n      - \\\"Zhou et al. LACE — 5x ECE gap across 100+ languages\\\"\\n      - \\\"Miao & Ungar 2026 — correctness-confidence orthogonality\\\"\\n      - \\\"Xiao et al. ACL 2025 — closest prior work, differentiate knowledge boundary vs correctness\\\"\\n      - \\\"CORAL, CCPS, Confidence Manifold — all English-only\\\"\\n\\n  - section: related_work\\n    word_budget: 1000\\n    core_bullets:\\n      - \\\"Cluster 1 — Mechanistic calibration: Miao & Ungar (orthogonality), CORAL (cross-task probes), CCPS (perturbation stability), Confidence Manifold (low-dim structure), Joshi (layer evolution), Ji (verbal uncertainty direction) → all English-only, single architecture; we extend to multilingual multi-architecture\\\"\\n      - \\\"Cluster 2 — Cross-lingual probing & alignment: Xiao (knowledge boundary ≠ correctness), Civelli (difficulty ≠ correctness), DALI (causal activation patching), Liu & Niehues (middle-layer alignment), Pires/Wu & Dredze (multilingual BERT transfer) → we add depth analysis, Pareto frontier, 5 transfer methods\\\"\\n      - \\\"Cluster 3 — Multilingual calibration: LACE (per-language ensemble), temperature scaling → require per-language labels; we require zero correctness labels\\\"\\n      - \\\"Cluster 4 — Theoretical: Ben-David (H-divergence), Zhao et al. 2019 (invariant representations + conditional shift) → we empirically test distributional matching prediction\\\"\\n      - \\\"Cluster 5 — Methodology: Hewitt & Liang (control tasks), Voita & Titov (MDL), CKA (Kornblith), MUSE/VecMap (projection baselines), conformal prediction (complementary) → we apply controls to cross-lingual setting; projection motivated by MUSE/VecMap\\\"\\n      - \\\"Table 1: side-by-side differentiation from 5 closest works (Xiao, LACE, CORAL, Miao & Ungar, Civelli)\\\"\\n    dependencies: [introduction]\\n    tables: [tab1_related_work]\\n\\n  - section: method\\n    word_budget: 1200\\n    core_bullets:\\n      - \\\"3.1 Problem formulation: correctness probing (definition: p(correct|h_l)), notation, contrast with knowledge boundary (Xiao) and difficulty (Civelli)\\\"\\n      - \\\"3.2 Experimental framework: models (Qwen3-8B/Llama4-Scout + MVP models), 20 languages by resource tier (HIGH/MED/LOW), GlobalMMLU test split 70/30 (probe_train/eval), activation extraction (register_forward_hook, post-norm, INT8/FP16)\\\"\\n      - \\\"3.3 Transfer methods: (a) zero-shot (direct application), (b) mean-shift + rank-invariance proof (1-2 para formal argument why ΔAUROC≡0), (c) Procrustes alignment (parallel pairs, effect reversal analysis), (d) few-shot (25/50/100 target labels), (e) CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency; MMD on 1-D probe logits from parallel GlobalMMLU items; implementation spec for reproducibility)\\\"\\n      - \\\"3.4 Difficulty-capability decomposition: IRT difficulty probes → project out shared component → retrain on residual → prescriptive predictions\\\"\\n      - \\\"3.5 Geometric analysis: CKA across layers controlling for depth (partial correlation), subspace angle measurement, Simpson's Paradox characterization\\\"\\n      - \\\"3.6 Probing controls: Hewitt & Liang selectivity, permuted-label baseline, PCA dimensionality reduction (plan_013 protocol)\\\"\\n    dependencies: []\\n    figures: [fig2_method_pipeline]\\n    registry_refs: [mvp_001, mvp_003, plan_013]\\n    notation_table:\\n      h_l: \\\"hidden representation at layer l\\\"\\n      w_l: \\\"learned probe weight vector (correctness direction) at layer l\\\"\\n      AUROC: \\\"Area Under ROC for correctness prediction\\\"\\n      ECE: \\\"Expected Calibration Error (15-bin)\\\"\\n      CKA: \\\"Centered Kernel Alignment\\\"\\n      SB-ECE: \\\"Soft-Binned ECE (differentiable, Karandikar 2021)\\\"\\n\\n  - section: experiments\\n    word_budget: 1800\\n    core_bullets:\\n      - \\\"4.1 Setup: 2+ architectures × 20 languages × 12-24 layers × 5 transfer methods; metrics (AUROC, ECE, Brier, selectivity); bootstrap CIs (1000 resamples) + paired permutation tests; Cohen's d effect sizes\\\"\\n      - \\\"4.2 Main transfer results (Table 2): zero-shot → mean-shift → Procrustes → few-shot → CaCLR, grouped by architecture and resource tier [TODO plan_001, plan_002, plan_003]\\\"\\n      - \\\"4.3 Pareto frontier (Figure 1): per-architecture depth-transferability scatter; per-language Spearman rho quantifying tradeoff strength; architecture comparison\\\"\\n      - \\\"4.4 CKA geometric analysis (Figure 3): Simpson's Paradox — raw rho=-0.40 (p<0.01, Llama pilot) vs partial rho=+0.41 (p=0.006); transparency: Qwen pilot non-significant (rho=+0.18, p=0.274); bootstrap CIs; subspace angles\\\"\\n      - \\\"4.5 Decomposition (Figure 4): difficulty-shared vs capability-specific transfer by resource tier and depth [TODO plan_004]\\\"\\n      - \\\"4.6 Empirical findings (Table 3): (a) control task: 28% low-resource artifacts (selectivity&lt;threshold at L20-L27), (b) projection: 50 pairs → 98%, HIGH saturate ~22, LOW ~48, (c) Procrustes reversal at zero-shot AUROC>0.60\\\"\\n      - \\\"4.7 CaCLR analysis: β sweep across 3 OOM, component ablation, comparison with linear projection, negative result + geometric explanation (MMD matches marginals but not low-dim directional structure) [TODO plan_003]\\\"\\n    dependencies: [method]\\n    tables: [tab2_main_results, tab3_empirical]\\n    figures: [fig1_pareto, fig3_cka_simpson, fig4_decomposition, fig5_layer_auroc]\\n    registry_refs: [mvp_001, mvp_002, mvp_003, plan_013]\\n\\n  - section: conclusion\\n    word_budget: 350\\n    core_bullets:\\n      - \\\"Summary: field-level viability test for multilingual probe calibration — architecture-dependent Pareto, CKA geometric insight, practical 50-pair recipe\\\"\\n      - \\\"Limitations: MCQA only (GlobalMMLU), 2-3 architectures (observational, no causal attribution to specific features), CaCLR 1-D MMD design limitation, INT8 quantization\\\"\\n      - \\\"Field warning: 28% capacity artifacts → all cross-lingual probing studies should include selectivity checks\\\"\\n      - \\\"Future: multilingual probe pooling on high-resource languages, adapter-based alignment, extension to open-ended generation\\\"\\n    dependencies: [experiments, method, introduction]\\n\\nvisualization_plan:\\n  - fig_id: fig1_pareto\\n    type: statistical\\n    tool: matplotlib\\n    description: \\\"Hero figure: Pareto scatter — English probe AUROC (x) vs mean cross-lingual transfer AUROC (y) across layers, separate trajectories per architecture\\\"\\n    narrative_intent: >-\\n      Deeper layers improve English probes but degrade cross-lingual transfer in\\n      Qwen (strong Pareto tradeoff); Llama shows language-specific patterns where\\n      some languages improve with depth — the tradeoff shape is architecture-dependent.\\n    design_notes:\\n      - \\\"Pattern A: background bands for layer depth zones (shallow L0-8, mid L12-20, deep L24+) — show where tradeoff kicks in\\\"\\n      - \\\"Connect layers with thin lines to show trajectory (path through Pareto space)\\\"\\n      - \\\"Different marker shapes per architecture (circle=Qwen, triangle=Llama)\\\"\\n      - \\\"Pattern F: per-label offset for key layer annotations (L0, L16, L24, L27/L31)\\\"\\n      - \\\"Dashed Pareto frontier line for Qwen to highlight envelope\\\"\\n      - \\\"Reference: calibration literature Pareto scatter (see CORAL Fig 3 style)\\\"\\n    data_source: \\\"registry: mvp_001, mvp_002, mvp_003 [TODO: plan_001, plan_002 for full-scale 20 langs]\\\"\\n    placement: introduction\\n    aspect_ratio: \\\"4:3\\\"\\n\\n  - fig_id: fig2_method_pipeline\\n    type: conceptual\\n    tool: paperbanana\\n    description: \\\"Method overview: LLM → layer activations → English probe → 5 transfer paths → multilingual evaluation\\\"\\n    narrative_intent: >-\\n      Our framework systematically tests 5 transfer strategies from English-trained\\n      correctness probes to target languages, ranging from zero-shot to CaCLR\\n      distributional matching, evaluated across the full layer depth.\\n    design_notes:\\n      - \\\"Left-to-right flow: multilingual LLM → extract h_l → train English probe → branch into 5 transfer methods\\\"\\n      - \\\"5 methods as parallel paths: zero-shot (direct), mean-shift, Procrustes, few-shot, CaCLR\\\"\\n      - \\\"CaCLR path highlighted: show BCE + SB-ECE + MMD(parallel) components\\\"\\n      - \\\"Bottom: evaluation across 20 languages × resource tiers\\\"\\n      - \\\"Keep minimal — max 3 vertical levels, no decorative elements\\\"\\n    data_source: \\\"conceptual\\\"\\n    placement: method\\n    aspect_ratio: \\\"16:9\\\"\\n\\n  - fig_id: fig3_cka_simpson\\n    type: statistical\\n    tool: matplotlib\\n    description: \\\"Simpson's Paradox dual panel: (left) raw CKA vs transfer with negative trend, (right) per-layer partial correlations showing positive trend\\\"\\n    narrative_intent: >-\\n      Raw CKA-transfer correlation is negative (depth confound — deeper layers have\\n      lower CKA AND lower transfer), but within each layer, higher cross-lingual CKA\\n      predicts better transfer — a Simpson's Paradox revealing genuine geometric structure.\\n    design_notes:\\n      - \\\"Pattern H: multi-panel asymmetric (1.4:1), left=aggregated, right=layer-stratified\\\"\\n      - \\\"Left: scatter colored by depth (viridis gradient), global regression line (negative slope), annotate rho_raw and p-value\\\"\\n      - \\\"Right: separate mini regression lines per layer (same depth colors), show positive slopes, annotate rho_partial\\\"\\n      - \\\"Pattern J: path-effect white stroke on annotations for readability\\\"\\n      - \\\"Panel titles as insights: left='Aggregate: depth confounds CKA-transfer', right='Per-layer: CKA predicts transfer'\\\"\\n      - \\\"Transparency: if Qwen non-significant, mark with hollow markers + note\\\"\\n    data_source: \\\"registry: mvp_003 CKA data [TODO: plan_001, plan_002 for full-scale + plan_011 partial correlation]\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"2:1\\\"\\n\\n  - fig_id: fig4_decomposition\\n    type: statistical\\n    tool: matplotlib\\n    description: \\\"Difficulty-capability decomposition: transfer AUROC curves for full probe vs difficulty-only vs capability-residual across layers\\\"\\n    narrative_intent: >-\\n      The difficulty-shared component transfers well at all depths (flat curve);\\n      the capability-specific component drives deep-layer degradation, explaining\\n      why transfer fails for some languages at later layers.\\n    design_notes:\\n      - \\\"Three lines per resource tier: full transfer (solid), difficulty-only (dashed), capability-residual (dotted)\\\"\\n      - \\\"Pattern B: fill_between for gap between full and difficulty-only (shows capability contribution)\\\"\\n      - \\\"Pattern A: vertical band marking 'degradation zone' where capability component diverges\\\"\\n      - \\\"Facet by resource tier (HIGH/MED/LOW) or overlay with alpha differentiation\\\"\\n      - \\\"X-axis: normalized layer depth (0-1); Y-axis: transfer AUROC\\\"\\n    data_source: \\\"[TODO: plan_004 decomposition experiments]\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n\\n  - fig_id: fig5_layer_auroc\\n    type: statistical\\n    tool: matplotlib\\n    description: \\\"Layer-wise AUROC: English vs cross-lingual transfer across all layers, side-by-side panels per architecture\\\"\\n    narrative_intent: >-\\n      English AUROC increases monotonically with depth in both architectures, but\\n      cross-lingual transfer peaks at intermediate layers — the divergence point and\\n      pattern differ by architecture (Qwen: sharp drop after L24; Llama: gradual, language-dependent).\\n    design_notes:\\n      - \\\"Pattern H: side-by-side panels (Qwen | Llama), shared y-axis\\\"\\n      - \\\"English line bold blue; target languages by resource tier color (HIGH=green, MED=orange, LOW=red)\\\"\\n      - \\\"Pattern C: horizontal dashed line at English best AUROC as reference\\\"\\n      - \\\"Pattern A: vertical band marking 'optimal transfer zone' per architecture\\\"\\n      - \\\"Thin lines per language, thick line for tier mean — show both individual variation and trend\\\"\\n      - \\\"Reference: layer analysis line plots universal in this subfield (distilled-writing)\\\"\\n    data_source: \\\"registry: mvp_001, mvp_002, mvp_003 [TODO: plan_001, plan_002 full-scale]\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"2:1\\\"\\n\\ntable_plan:\\n  - table_id: tab1_related_work\\n    caption: \\\"Comparison with closely related work on calibration probing and cross-lingual transfer\\\"\\n    placement: related_work\\n    type: comparison\\n    columns: [Paper, Target Signal, \\\"# Langs\\\", Metrics, \\\"Labels Req.\\\", Depth Analysis, Transfer Methods]\\n    data_source: \\\"manual\\\"\\n    notes: >-\\n      Rows: Xiao et al. (knowledge boundary), LACE (per-language ensemble), CORAL (cross-task English),\\n      Miao & Ungar (orthogonality), Civelli (difficulty), Ours. Checkmarks for binary features.\\n      Highlight our unique combination: correctness + 20 langs + 0 correctness labels + full depth + 5 methods.\\n\\n  - table_id: tab2_main_results\\n    caption: \\\"Cross-lingual correctness probe transfer results (AUROC) across 5 methods, grouped by resource tier\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Method, \\\"HIGH (5L avg)\\\", \\\"MED (5L avg)\\\", \\\"LOW (5L avg)\\\", Overall, \\\"Best Layer\\\"]\\n    data_source: \\\"registry: [TODO plan_001, plan_002, plan_003]\\\"\\n    notes: >-\\n      Rows: zero-shot, mean-shift, Procrustes, few-shot-25, few-shot-50, few-shot-100, CaCLR.\\n      Separate sub-tables per architecture. Bold best per column. Include ECE in parentheses.\\n      MVP data (mvp_001, mvp_003) available for preliminary version.\\n    baseline_row: \\\"zero-shot\\\"\\n\\n  - table_id: tab3_empirical\\n    caption: \\\"Key empirical findings with practical implications\\\"\\n    placement: experiments\\n    type: statistics\\n    columns: [Finding, Evidence, Threshold/Value, Implication]\\n    data_source: \\\"registry: plan_013, mvp_001, mvp_003 [TODO: plan_012]\\\"\\n    notes: >-\\n      Three rows: (1) Control task: 28% low-resource results below selectivity threshold → field warning,\\n      (2) Projection saturation: ~50 pairs (HIGH ~22, LOW ~48) → practical recipe,\\n      (3) Procrustes reversal: helps when AUROC<0.50, hurts when >0.60 → conditional strategy.\\n\\nliterature_strategy:\\n  citation_budget: 35\\n  macro_context:\\n    - \\\"LLM calibration and confidence estimation via internal representations\\\"\\n    - \\\"cross-lingual representation transfer and alignment in multilingual LLMs\\\"\\n    - \\\"probing methodology, controls, and representation similarity\\\"\\n  micro_clusters:\\n    - cluster_name: \\\"mechanistic_calibration\\\"\\n      search_queries:\\n        - \\\"correctness direction probing language models 2025 2026\\\"\\n        - \\\"calibration internal representations LLM residual stream\\\"\\n        - \\\"confidence manifold neural network representations\\\"\\n      must_cite:\\n        - \\\"Miao & Ungar 2026 (correctness-confidence orthogonality)\\\"\\n        - \\\"Miao 2026 CORAL (cross-task correctness probes)\\\"\\n        - \\\"Khanmohammadi 2025 CCPS (perturbation stability)\\\"\\n        - \\\"Confidence Manifold 2026 (low-dimensional structure)\\\"\\n        - \\\"Joshi 2025 (calibration across layers)\\\"\\n        - \\\"Ji 2025 (verbal uncertainty linear feature)\\\"\\n      target_count: 8\\n\\n    - cluster_name: \\\"cross_lingual_probing\\\"\\n      search_queries:\\n        - \\\"cross-lingual probe transfer multilingual LLM 2024 2025 2026\\\"\\n        - \\\"knowledge boundary probing across languages\\\"\\n        - \\\"cross-lingual difficulty probing shared geometry multilingual\\\"\\n      must_cite:\\n        - \\\"Xiao et al. ACL 2025 (knowledge boundary)\\\"\\n        - \\\"Civelli 2026 (shared geometry of difficulty)\\\"\\n      target_count: 5\\n\\n    - cluster_name: \\\"cross_lingual_alignment\\\"\\n      search_queries:\\n        - \\\"cross-lingual representation alignment multilingual LLM 2024 2025\\\"\\n        - \\\"activation patching cross-lingual transfer\\\"\\n        - \\\"MUSE VecMap cross-lingual embedding alignment\\\"\\n      must_cite:\\n        - \\\"Ravisankar 2026 DALI\\\"\\n        - \\\"Liu & Niehues 2025 (middle-layer alignment)\\\"\\n        - \\\"Conneau et al. 2018 MUSE\\\"\\n        - \\\"Artetxe et al. 2018 VecMap\\\"\\n        - \\\"Pires et al. 2019 (multilingual BERT)\\\"\\n        - \\\"Wu & Dredze 2019 (cross-lingual transfer)\\\"\\n      target_count: 7\\n\\n    - cluster_name: \\\"multilingual_calibration\\\"\\n      search_queries:\\n        - \\\"multilingual LLM calibration ECE cross-lingual 2024 2025\\\"\\n        - \\\"temperature scaling multilingual language models\\\"\\n      must_cite:\\n        - \\\"Zhou et al. LACE (adaptive layer ensemble)\\\"\\n      target_count: 4\\n\\n    - cluster_name: \\\"domain_adaptation_theory\\\"\\n      search_queries:\\n        - \\\"domain adaptation theory H-divergence representation learning\\\"\\n        - \\\"invariant representations domain adaptation conditional shift Zhao 2019\\\"\\n      must_cite:\\n        - \\\"Ben-David et al. 2010 (H-divergence)\\\"\\n        - \\\"Zhao et al. 2019 (invariant representations + conditional failure)\\\"\\n      target_count: 3\\n\\n    - cluster_name: \\\"probing_methodology\\\"\\n      search_queries:\\n        - \\\"probing classifier control task selectivity Hewitt Liang\\\"\\n        - \\\"MDL probes Voita Titov online coding\\\"\\n        - \\\"probing methodology neural network representations 2019 2020\\\"\\n      must_cite:\\n        - \\\"Hewitt & Liang 2019 (control tasks)\\\"\\n        - \\\"Voita & Titov 2020 (MDL probes)\\\"\\n      target_count: 3\\n\\n    - cluster_name: \\\"representation_similarity\\\"\\n      search_queries:\\n        - \\\"CKA centered kernel alignment representation similarity\\\"\\n        - \\\"SVCCA representation comparison neural networks\\\"\\n      must_cite:\\n        - \\\"Kornblith et al. 2019 (CKA)\\\"\\n      target_count: 2\\n\\n    - cluster_name: \\\"calibration_foundations\\\"\\n      search_queries:\\n        - \\\"neural network calibration temperature scaling Guo 2017\\\"\\n        - \\\"conformal prediction language models coverage guarantee\\\"\\n        - \\\"soft binned ECE differentiable calibration\\\"\\n      must_cite:\\n        - \\\"Guo et al. 2017 (modern calibration)\\\"\\n        - \\\"Angelopoulos & Bates 2023 (conformal prediction)\\\"\\n        - \\\"Karandikar 2021 (SB-ECE)\\\"\\n      target_count: 3\\n\\nwriting_order:\\n  - method          # Can start now — framework clear from paper_framing\\n  - related_work    # Can start now — literature-based, addresses reviewer concern\\n  - experiments     # Needs P0 data; setup section writable now, results after plan_001/002\\n  - introduction    # Needs method + experiments framing\\n  - abstract        # Last — distills all sections\\n  - conclusion      # Last — mirrors abstract + limitations\\n\\nappendix_plan:\\n  - \\\"A: Per-language detailed results (20 languages × all layers × 5 methods)\\\"\\n  - \\\"B: CaCLR hyperparameter sensitivity (α and β sweeps)\\\"\\n  - \\\"C: INT8 vs FP16 validation ablation\\\"\\n  - \\\"D: Full CKA matrices and subspace angle tables\\\"\\n  - \\\"E: Mean-shift rank-invariance formal proof\\\"\\n  - \\\"F: Additional Pareto plots (per-language individual trajectories)\\\"\\n  - \\\"G: Procrustes sensitivity analysis (pairs vs ΔAUROC curves)\\\"\\n\", \"total_chars\": 21359, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "861acec4-ab09-47f9-84fb-250e47e6f721",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "207edcf7-1382-43b8-a225-998f5aed38a3",
  "sourceToolAssistantUUID": "861acec4-ab09-47f9-84fb-250e47e6f721",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-21T06:01:03.084Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01255ANAnMLeWZi3pmeyZJHk`</summary>

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
  "parentUuid": "207edcf7-1382-43b8-a225-998f5aed38a3",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCppSR8v7Wf6seau55j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1ee4796-b099-4169-8fe7-5fedd0963745",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Taq53rcJaMbPFsZ7yeiaeG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7875,
      "cache_read_input_tokens": 60032,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7875
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 60032,
          "cache_creation_input_tokens": 7875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7875,
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

_source line 51 · 2026-05-21T06:01:03.115Z_

<details><summary>↩ Tool result · `toolu_01255ANAnMLeWZi3pmeyZJHk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/literature_map.yaml\", \"content\": \"papers:\\n  miao2026closing:\\n    title: \\\"Closing the Confidence-Faithfulness Gap in Large Language Models\\\"\\n    authors: [\\\"Ruoxi Miao\\\", \\\"Lyle Ungar\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.25052\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Showed correctness direction and verbalized confidence direction are orthogonal (cosine < 0.04) in 7-8B models. Motivates probing internal representations. English-only — our cross-lingual extension is the natural next step.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  xiao2025knowledge:\\n    title: \\\"Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations\\\"\\n    authors: [\\\"Zheng Xiao\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2504.13816\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest prior work. Cross-lingual transfer of knowledge-boundary probes (answerable vs unanswerable). Key differences: they probe knowledge boundaries (input-level), we probe correctness (output-dependent); they measure probing accuracy, not ECE/Brier; they test 8 languages, we target 20+.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  civelli2026shared:\\n    title: \\\"A Shared Geometry of Difficulty in Multilingual Language Models\\\"\\n    authors: [\\\"Andrea Civelli\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2601.12731\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Cross-lingual difficulty probe transfer at intermediate layers. Architecture-dependent optimal depth (24-49%). Probes IRT difficulty (question property), not correctness (model property). Critical control for our difficulty ablation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  zhou2025lace:\\n    title: \\\"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in LLMs\\\"\\n    authors: [\\\"Zhou\\\"]\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2510.03136\\\"\\n    category: \\\"multilingual_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"LACE: adaptive layer ensemble for multilingual calibration. Confirmed 5x ECE gap across 100+ languages. Requires per-language validation data. Our CaCLR needs no non-English correctness labels.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ravisankar2026dali:\\n    title: \\\"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs\\\"\\n    authors: [\\\"Ravisankar\\\"]\\n    year: 2026\\n    venue: \\\"EACL 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2504.09378\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"DALI: causal evidence via activation patching that English middle-layer representations fix non-English errors across 24 languages. Strongest causal support for our hypothesis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  miao2026coral:\\n    title: \\\"Correctness-Optimized Residual Activation Lens (CORAL)\\\"\\n    authors: [\\\"Ruoxi Miao\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.06022\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Transferable correctness probes via regularized MLP on residual activations, ~50% ECE improvement at 53-66% depth. English-only, cross-task. CaCLR positioned as solution to their identified distribution-shift transfer degradation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  joshi2025calibration:\\n    title: \\\"Calibration Across Layers: Understanding Calibration Evolution in LLMs\\\"\\n    authors: [\\\"Joshi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Identified low-dimensional calibration direction in residual stream evolving across layers.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  confidence_manifold2026:\\n    title: \\\"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.08159\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Correctness signals occupy 3-8 dimensions, linearly separable. 25 labeled examples achieve 89% of full-data accuracy. All English-only.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  karandikar2021sbece:\\n    title: \\\"Soft Calibration Objectives for Neural Networks\\\"\\n    authors: [\\\"Archit Karandikar\\\", \\\"Nicholas Cain\\\", \\\"Dustin Tran\\\", \\\"Balaji Lakshminarayanan\\\", \\\"Jonathon Shlens\\\", \\\"Michael C. Mozer\\\", \\\"Becca Roelofs\\\"]\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"https://proceedings.neurips.cc/paper/2021/hash/f8905bd3df64ace64a68e154ba72f24c-Abstract.html\\\"\\n    category: \\\"calibration_foundations\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"SB-ECE: differentiable soft-binned ECE enabling gradient-based calibration optimization. Core component of our CaCLR objective.\\\"\\n    verified: true\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  khanmohammadi2025ccps:\\n    title: \\\"Calibrating LLM Confidence by Probing Perturbed Representation Stability (CCPS)\\\"\\n    authors: [\\\"Khanmohammadi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2505.21772\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Calibration via probing perturbed representation stability at final layer. ~55% ECE reduction. English-only, single layer. No cross-lingual or multi-layer analysis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  liu2025middle:\\n    title: \\\"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs\\\"\\n    authors: [\\\"Liu\\\", \\\"Niehues\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Middle layers form strongest language-agnostic shared space. Supports our hypothesis about intermediate-layer transfer.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ji2025calibrating:\\n    title: \\\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\\\"\\n    authors: [\\\"Ji\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Verbal uncertainty governed by single linear direction in representation space.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  bendavid2010theory:\\n    title: \\\"A Theory of Learning from Different Domains\\\"\\n    authors: [\\\"Shai Ben-David\\\", \\\"John Blitzer\\\", \\\"Koby Crammer\\\", \\\"Alex Kulesza\\\", \\\"Fernando Pereira\\\", \\\"Jennifer Wortman Vaughan\\\"]\\n    year: 2010\\n    venue: \\\"Machine Learning, Vol. 79, pp. 151-175\\\"\\n    url: \\\"https://link.springer.com/article/10.1007/s10994-009-5152-4\\\"\\n    category: \\\"domain_adaptation_theory\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"H-divergence framework for domain adaptation. Theoretical basis for bounding target error via source error and domain divergence — underpins our cross-lingual transfer analysis.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  zhao2019invariant:\\n    title: \\\"On Learning Invariant Representations for Domain Adaptation\\\"\\n    authors: [\\\"Han Zhao\\\", \\\"Remi Tachet des Combes\\\", \\\"Kun Zhang\\\", \\\"Geoffrey J. Gordon\\\"]\\n    year: 2019\\n    venue: \\\"ICML 2019\\\"\\n    url: \\\"https://proceedings.mlr.press/v97/zhao19a.html\\\"\\n    category: \\\"domain_adaptation_theory\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Proves marginal distribution matching fails when conditional distributions differ. Motivates why naive cross-lingual probe transfer may degrade — our CaCLR addresses this gap.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  zhang2019bridging:\\n    title: \\\"Bridging Theory and Algorithm for Domain Adaptation\\\"\\n    authors: [\\\"Yuchen Zhang\\\", \\\"Tianle Liu\\\", \\\"Mingsheng Long\\\", \\\"Michael I. Jordan\\\"]\\n    year: 2019\\n    venue: \\\"ICML 2019\\\"\\n    url: \\\"https://proceedings.mlr.press/v97/zhang19i.html\\\"\\n    category: \\\"domain_adaptation_theory\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Margin Disparity Discrepancy — tighter generalization bound connecting domain adaptation theory to practical adversarial algorithms. Complements Ben-David and Zhao theoretical foundations.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  hewitt2019control:\\n    title: \\\"Designing and Interpreting Probes with Control Tasks\\\"\\n    authors: [\\\"John Hewitt\\\", \\\"Percy Liang\\\"]\\n    year: 2019\\n    venue: \\\"EMNLP 2019\\\"\\n    url: \\\"https://aclanthology.org/D19-1275/\\\"\\n    category: \\\"probing_methodology\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Defines selectivity metric for probes — ensures probe accuracy reflects encoded information, not classifier capacity. Methodological baseline for our probing evaluation.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  voita2020mdl:\\n    title: \\\"Information-Theoretic Probing with Minimum Description Length\\\"\\n    authors: [\\\"Elena Voita\\\", \\\"Ivan Titov\\\"]\\n    year: 2020\\n    venue: \\\"EMNLP 2020\\\"\\n    url: \\\"https://aclanthology.org/2020.emnlp-main.14/\\\"\\n    category: \\\"probing_methodology\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"MDL probing — information-theoretic alternative measuring compression quality rather than raw accuracy. More robust evaluation metric for cross-lingual probe transfer.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  belinkov2022probing:\\n    title: \\\"Probing Classifiers: Promises, Shortcomings, and Advances\\\"\\n    authors: [\\\"Yonatan Belinkov\\\"]\\n    year: 2022\\n    venue: \\\"Computational Linguistics, Vol. 48, No. 1, pp. 207-219\\\"\\n    url: \\\"https://aclanthology.org/2022.cl-1.7/\\\"\\n    category: \\\"probing_methodology\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Comprehensive survey of probing methodology — defines best practices, pitfalls, and evaluation standards we follow in our experimental design.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  kornblith2019cka:\\n    title: \\\"Similarity of Neural Network Representations Revisited\\\"\\n    authors: [\\\"Simon Kornblith\\\", \\\"Mohammad Norouzi\\\", \\\"Honglak Lee\\\", \\\"Geoffrey Hinton\\\"]\\n    year: 2019\\n    venue: \\\"ICML 2019\\\"\\n    url: \\\"https://proceedings.mlr.press/v97/kornblith19a.html\\\"\\n    category: \\\"representation_similarity\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Centered Kernel Alignment (CKA) — our primary metric for measuring cross-lingual representation similarity across layers.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  wu2020similarity:\\n    title: \\\"Similarity Analysis of Contextual Word Representation Models\\\"\\n    authors: [\\\"John Wu\\\", \\\"Yonatan Belinkov\\\", \\\"Hassan Sajjad\\\", \\\"Nadir Durrani\\\", \\\"Fahim Dalvi\\\", \\\"James Glass\\\"]\\n    year: 2020\\n    venue: \\\"ACL 2020\\\"\\n    url: \\\"https://aclanthology.org/2020.acl-main.422/\\\"\\n    category: \\\"representation_similarity\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Applies CKA and SVCCA to compare contextual word representations across architectures — direct precedent for our cross-lingual representation similarity analysis.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  guo2017calibration:\\n    title: \\\"On Calibration of Modern Neural Networks\\\"\\n    authors: [\\\"Chuan Guo\\\", \\\"Geoff Pleiss\\\", \\\"Yu Sun\\\", \\\"Kilian Q. Weinberger\\\"]\\n    year: 2017\\n    venue: \\\"ICML 2017\\\"\\n    url: \\\"https://proceedings.mlr.press/v70/guo17a.html\\\"\\n    category: \\\"calibration_foundations\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Temperature scaling baseline — canonical post-hoc calibration method we compare against. Established ECE as standard calibration metric.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\n  angelopoulos2023conformal:\\n    title: \\\"Conformal Prediction: A Gentle Introduction\\\"\\n    authors: [\\\"Anastasios N. Angelopoulos\\\", \\\"Stephen Bates\\\"]\\n    year: 2023\\n    venue: \\\"Foundations and Trends in Machine Learning, Vol. 16, No. 4, pp. 494-591\\\"\\n    url: \\\"https://www.nowpublishers.com/article/Details/MAL-101\\\"\\n    category: \\\"calibration_foundations\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Distribution-free uncertainty quantification framework — theoretical grounding for our conformal prediction extension of CaCLR.\\\"\\n    verified: true\\n    added_by: \\\"worker\\\"\\n    added_at: \\\"2026-05-21\\\"\\n\\ncategories:\\n  mechanistic_calibration: \\\"Probing/steering calibration signals in LLM internal representations\\\"\\n  cross_lingual_probing: \\\"Cross-lingual transfer of probes/directions in multilingual models\\\"\\n  cross_lingual_alignment: \\\"Language alignment and shared representations in multilingual LLMs\\\"\\n  multilingual_calibration: \\\"Calibration methods for multilingual LLMs\\\"\\n  calibration_methods: \\\"General calibration objectives and techniques\\\"\\n  domain_adaptation_theory: \\\"Theoretical foundations for domain adaptation and representation learning\\\"\\n  probing_methodology: \\\"Methodology for probing neural network representations\\\"\\n  representation_similarity: \\\"Metrics and methods for comparing neural network representations\\\"\\n  calibration_foundations: \\\"Foundational calibration and uncertainty quantification methods\\\"\\n\\nmeta:\\n  created_at: \\\"2026-05-20\\\"\\n  last_updated: \\\"2026-05-21\\\"\\n  total_papers: 22\\n\", \"total_chars\": 13373, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1ee4796-b099-4169-8fe7-5fedd0963745",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "5b849530-3312-4a84-bb8a-46cdb96bd62e",
  "sourceToolAssistantUUID": "f1ee4796-b099-4169-8fe7-5fedd0963745",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-21T06:01:19.236Z_

Now I have thorough context. Let me also check the distilled research skill for additional methodological context before writing the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b849530-3312-4a84-bb8a-46cdb96bd62e",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCqEr79BnnHFVABj3bN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebf6cbf9-5327-4fa3-a9d9-ee422abaea82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RfSWyV2GfZHqrp3wntSPYH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12967,
      "cache_read_input_tokens": 67907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12967,
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

_source line 53 · 2026-05-21T06:01:21.334Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HVwUFbGWQAW7W9vQ8ugQok`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-research.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebf6cbf9-5327-4fa3-a9d9-ee422abaea82",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCqEr79BnnHFVABj3bN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44790536-397b-48ae-b881-d8bba3c9b2d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RfSWyV2GfZHqrp3wntSPYH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12967,
      "cache_read_input_tokens": 67907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12967,
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

_source line 54 · 2026-05-21T06:01:21.345Z_

<details><summary>↩ Tool result · `toolu_01HVwUFbGWQAW7W9vQ8ugQok`</summary>

```text
1	---
2	name: xling-calib-direction-research
3	description: Research patterns from 12 papers on cross-lingual calibration and internal representations in LLMs
4	type: skill
5	---
6	
7	# Cross-Lingual Calibration — Research Patterns (12 papers)
8	
9	## Evaluation Protocol
10	
11	**Metrics**: ECE (8/12) + AUROC (5/12) + Brier (4/12). Always pair calibration with discrimination. Point estimates without CIs is field norm (6/8). High conf.
12	
13	**Benchmarks**: MMLU (5/12), Belebele for multilingual (122 langs), TruthfulQA. Transfer: ARC, HellaSwag, CSQA. High conf.
14	
15	**Models**: 3-6 models. Llama-3.1-8B + Qwen2.5-7B near-universal. Include multilingual-first model (Aya). High conf.
16	
17	## Method Trends
18	
19	**Linear probing of hidden states** (7/12): Linear classifiers suffice. AUC 0.80-0.97. Source: confidence_manifold2026. High conf.
20	
21	**Layer-wise analysis standard** (7/12): Middle-to-late layers (15-29/32) richest for xling/calibration. Final layer suboptimal for non-English. Source: zhou2025lace (24-29), civelli2026shared (xling ~15, monolingual ~30). High conf.
22	
23	**Inference-time steering** (4/12): Extract direction, add to activations, no retraining. Source: ji2025calibrating, miao2026coral, miao2026closing. Med conf.
24	
25	**Training-free methods rising** (3/12): LACE, mean shift, projection. Field moving from fine-tuning. Med conf.
26	
27	**Temperature scaling declining**: Only baseline now. High conf.
28	
29	## Cross-Paper Findings
30	
31	**Non-English ECE 5x English** (23% vs 4.6%). Structural, tied to pretraining data. Source: zhou2025lace. 3/12. High conf.
32	
33	**Cross-lingual reps are linear**: Knowledge/confidence linearly encoded across languages in middle layers. Mean shift/projection enables training-free transfer. Source: xiao2025knowledge. 4/12. High conf.
34	
35	**Correctness distributed not sparse**: SAE neuron ablation negligible (delta ECE 1.25e-4). 3-8D subspace. Source: miao2026coral, confidence_manifold2026. 2/12. Med conf.
36	
37	**Layer-depth Pareto**: English calibration improves monotonically; non-English peaks mid-late then degrades. Source: zhou2025lace, joshi2025calibration. 2/12. High conf.
38	
39	## Competitor Landscape
40	
41	**zhou2025lace** (competitor): Per-language layer ensemble, ECE 22→3%, training-free. No directional methods.
42	**joshi2025calibration** (competitor): Calibration direction in residual stream. Transfers across datasets but NOT across models. Monolingual only.
43	
44	**Our niche**: No paper combines xling transfer + calibration directions + layer-depth Pareto. joshi's direction fails cross-model. civelli shows xling/monolingual optimal layers diverge. Intersection is open.
45	
46	## Gaps
47	
48	- Cross-model direction transfer unsolved (joshi shows failure)
49	- No multilingual verbal uncertainty (ji2025calibrating English-only)
50	- MCQA-only (5/12) → generation calibration open
51	- Instance-level causal validation missing (ravisankar correlation only)
52	- Scale beyond 7-8B untested
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44790536-397b-48ae-b881-d8bba3c9b2d8",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "bd8c4f64-332b-4ec8-80ac-5f46e316c96c",
  "sourceToolAssistantUUID": "44790536-397b-48ae-b881-d8bba3c9b2d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-21T06:01:25.315Z_

I now have comprehensive understanding of the paper, its methodology, experimental design, code implementation, and context. Let me write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd8c4f64-332b-4ec8-80ac-5f46e316c96c",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCraybcbhtUYdse5e3G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9d8aab1-7bae-4eec-9c88-26d1505216cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmHGcd4wcAWUFX31YX5PDB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1140,
      "cache_read_input_tokens": 80874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1140,
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

_source line 56 · 2026-05-21T06:01:25.642Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0198RxNX7Lk2Ah7fCcDXULc9`</summary>

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
  "parentUuid": "b9d8aab1-7bae-4eec-9c88-26d1505216cd",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCraybcbhtUYdse5e3G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a26de245-eca0-4494-b266-173f0c98c5bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmHGcd4wcAWUFX31YX5PDB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1140,
      "cache_read_input_tokens": 80874,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1140
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 80874,
          "cache_creation_input_tokens": 1140,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1140,
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

_source line 57 · 2026-05-21T06:01:25.645Z_

<details><summary>↩ Tool result · `toolu_0198RxNX7Lk2Ah7fCcDXULc9`</summary>

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
  "parentUuid": "a26de245-eca0-4494-b266-173f0c98c5bc",
  "isSidechain": true,
  "promptId": "d159e131-5779-4f9c-878e-e70f68151974",
  "agentId": "acf51195619fdbc79",
  "type": "user",
  "uuid": "be402a21-1380-489f-99de-a964ee7174db",
  "sourceToolAssistantUUID": "a26de245-eca0-4494-b266-173f0c98c5bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-21T06:03:11.651Z_



Based on my thorough analysis of the paper's methodology, experimental design, code implementation, statistical practices, and supporting documentation, here is my review.

---

## R1 Review: Methods and Experiments

### 1. Summary

This paper presents a large-scale empirical study of cross-lingual correctness probe transfer, training English logistic regression probes on hidden-state activations from two MoE architectures (Qwen3-235B, Llama 4 Scout) and evaluating zero-shot transfer to 20 languages across three resource tiers using five transfer methods. The core contributions are an architecture-dependent depth-transferability Pareto frontier, a Simpson's Paradox in the CKA-transfer relationship, a systematic CaCLR negative result with geometric explanation, practical linear projection guidelines, and a control-task artifact warning for low-resource probing.

### 2. Strengths

**S1. Comprehensive and well-structured experimental plan.** The 13-experiment design covers core claims (plan_001/002), robustness checks (plan_010 quantization, plan_013 controls, plan_006 probe complexity), generalization (plan_007 cross-benchmark, plan_009 extended languages), and extensions (plan_008 Gemma 4). The progression from MVP validation on 7-8B models to full-scale 235B execution is methodologically sound and reduces resource waste.

**S2. Rigorous statistical methodology.** Bootstrap 95% CIs with 1000 resamples, paired permutation tests, and Cohen's d effect sizes are reported throughout. This exceeds the field norm, where 6/8 comparable papers report point estimates without CIs (per the distilled research skill). The permutation test implementation in `transfer_eval.py` (lines 69-78) is correct, using `(count_ge + 1) / (n_perm + 1)` to avoid zero p-values.

**S3. Simpson's Paradox analysis is the methodological highlight.** Partial Spearman correlation controlling for normalized depth is the correct approach to disentangle the CKA-depth confound. The pilot data (Table 5) shows the expected sign reversal on both architectures, with Llama 4 reaching significance (partial rho=+0.29, p=0.018). The per-layer cross-language correlations provide independent non-parametric support. This directly addresses the "CKA is just a depth proxy" concern.

**S4. Probing control tasks are essential and rarely included.** The Hewitt & Liang selectivity analysis (Table 14-15) revealing ~30% LOW-resource and ~28% MID-resource artifacts is a genuine methodological contribution. The implementation uses PCA(100) dimensionality reduction with 5-fold CV, and the selectivity threshold (0.05) is conservative. The finding that yo (selectivity=0.032) and am (selectivity=0.018) are capacity artifacts at L80 directly impacts interpretation of transfer results for these languages.

**S5. Mean-shift rank-invariance proof is clean and useful.** The mathematical argument that StandardScaler + logistic regression makes mean-shift AUROC-invariant is correct: mean-shift adds a constant to all pre-scaling activations, which after StandardScaler becomes a constant offset to logits, preserving ranking. This is verified empirically and clearly differentiates from Xiao et al.'s pipeline where mean-shift operates under different conditions.

**S6. CaCLR implementation is well-specified for reproducibility.** The code (`train_caclr.py`) fully specifies: Gaussian RBF kernel with median heuristic bandwidth (lines 82-104), unbiased MMD estimator with diagonal exclusion (lines 107-123), soft-binning ECE with temperature=0.05 (lines 53-79), initialization from sklearn LR solution (lines 172-184), Adam optimizer, and subsampling to 512 for MMD computation (line 286). The beta sweep across three orders of magnitude (0.001-1.0) with component ablation (Table 8) constitutes a fair trial of the distributional matching hypothesis.

**S7. Quantization validation addresses a key confound.** With max |ΔAUROC| < 0.012 between quantized and FP16 baselines, the paper demonstrates that INT4/W4A16 quantization does not distort the Pareto frontier ordering. This is important given both models use aggressive quantization.

### 3. Weaknesses

**W1. Procrustes train/eval contamination risk.** In `transfer_eval.py` (lines 189-199), the Procrustes alignment samples parallel pairs from the same data that is subsequently used for evaluation. Specifically, `pair_idx` is sampled from `min(len(X_en_all), len(X_tgt))` indices, and then the full `X_tgt` (including those same indices) is transformed and evaluated. With 200 pairs out of ~4200 eval samples (~5%), the bias may be small, but it is methodologically incorrect. The 70/30 train/eval split in `extract_activations_large.py` addresses CaCLR data separation but the code does not enforce that Procrustes pairs come exclusively from the train split. Table 11 (linear projection saturation) and Table 12 (Procrustes reversal) are both affected. The paper should either (a) restrict Procrustes pairs to train-split items and evaluate only on eval-split items, or (b) quantify the contamination bias via leave-pair-out analysis.

**W2. CaCLR hyperparameter selection criterion is English-only.** The sweep in `train_caclr.py` (lines 401-434) selects the best (alpha, beta) by `score = auroc - ece_weight * ece` computed on an English validation split. If the consistency loss (beta > 0) improves cross-lingual transfer at the expense of English performance, the English-only criterion would select against it. This creates a structural bias toward low beta values, potentially undermining the CaCLR negative result. The paper reports mean ΔAUROC=+0.002 (p=0.42) for CaCLR (Table 7), but with an English-optimized beta, the true cross-lingual potential may be underestimated. A mixed criterion incorporating at least one or two validation languages would strengthen the negative result claim.

**W3. CaCLR operates on 1-D probe logits, which severely limits MMD's expressiveness.** The code confirms (line 283, `train_caclr.py`) that MMD operates on `logits_en_sub.unsqueeze(1)` and `logits_tgt_sub.unsqueeze(1)` — scalar probe outputs. In 1-D, Gaussian RBF MMD is essentially matching the marginal distribution of a single scalar. The paper acknowledges this as a "design limitation" but then draws the strong conclusion that "distributional matching fails for correctness probe transfer" (Table 9 geometric explanation). This conclusion is specific to 1-D marginal matching, not distributional matching in general. MMD on the full hidden-state space, or on a low-rank projection of it, could yield different results. The negative result should be scoped more precisely: "1-D logit-level MMD matching fails" rather than implying distributional matching as a class is ineffective.

**W4. Single random seed throughout.** `train_caclr.py` uses `seed=42` (line 229), `transfer_eval.py` uses `proj_seed=42` (line 48), and `train_probe.py` uses `seed=42` (line 38). Given the modest effect sizes (CaCLR: +0.002; linear projection at 50 pairs: +0.027; few-shot 25: +0.018 over zero-shot), variance across seeds could be comparable to reported effects. The few-shot evaluation (lines 202-236) is particularly sensitive: with only 25 labeled examples, the specific sample drawn determines the result. Multi-seed variance estimates (3-5 seeds) are needed for all methods, especially few-shot and Procrustes with small pair counts.

**W5. Difficulty decomposition methodology is underspecified.** Table 13 reports ΔAUROC from "difficulty projection" (+0.012, 7/10 positive) vs. random-direction control (+0.005), yielding a 2.4x ratio. However: (a) the source of IRT difficulty scores is not specified — if estimated from model accuracy on the same data, circularity arises; (b) the prescriptive accuracy of 58% is barely above the 50% random baseline, undermining the practical value of the decomposition; (c) the difficulty probe R²=0.35 means 65% of difficulty variance is unexplained, so the "projection out" step leaves substantial difficulty signal in the residual. The random-direction control addresses dimensionality reduction artifacts but not the residual difficulty confound.

**W6. ECE computation has minor inconsistencies.** The writing plan (notation table) references "ECE (15-bin)" but the code consistently uses 10 bins (`n_bins=10` in `transfer_eval.py` line 54, `train_caclr.py` line 317, `train_probe.py` line 43). Equal-width binning with 10 bins is standard (Guo et al. 2017) but the paper should be internally consistent. Additionally, the ECE boundary condition handling differs subtly between the hard-histogram version (includes left boundary via `>=` only at lo=0.0) and the SB-ECE soft-binning version — while both are reasonable, the paper should state which ECE variant is used for final reporting.

**W7. Linear CKA may be insensitive to the relevant representational differences.** The paper uses linear CKA (confirmed in `compute_cka.py` lines 26-41), which captures linear relationships between representations. If correctness information is encoded in nonlinear substructures that differ across languages, linear CKA would miss this while still showing high similarity. The Simpson's Paradox finding — positive partial correlation between CKA and transfer — could partly reflect that both CKA and AUROC (via linear probes) are sensitive to the same linear structure, creating tautological agreement. Kernel CKA or projection-weighted CKA could test whether the finding holds for richer similarity measures.

**W8. Few-shot evaluation does not properly account for reduced test set.** In `transfer_eval.py` (lines 208-211), the few-shot samples are excluded from the evaluation set (`eval_mask[fs_idx] = False`), which is correct for avoiding data leakage. However, with few-shot 100 from ~4200 total samples, the evaluation set drops to ~4100 — comparable to zero-shot's ~4200 — making results comparable. But for few-shot 25, the specific 25 samples removed could shift the difficulty distribution of the remaining test set. A stratified sampling strategy (by subject) for few-shot selection would mitigate this.

### 4. Questions for Authors

1. **Procrustes contamination**: Can you confirm that Table 11 and Table 12 results use Procrustes pairs exclusively from the train split, with evaluation only on the eval split? The code suggests otherwise.

2. **IRT difficulty source**: Where do the item-level difficulty scores for the decomposition (Table 13) come from? If from model accuracy, how do you address circularity?

3. **CaCLR in higher dimensions**: Have you tried MMD on the hidden-state activations directly (before the probe), or on a PCA-reduced intermediate representation? The 1-D logit constraint seems artificially restrictive.

4. **Multi-seed variance**: What is the standard deviation of CaCLR AUROC across 3-5 random seeds? Is the +0.002 effect (Table 7) within noise?

5. **Procrustes reversal mechanism**: Table 12 shows that Procrustes hurts when ZS AUROC > 0.70. Is this because well-aligned languages have representations that are already in the correct subspace, and the Procrustes rotation introduces noise from fitting irrelevant dimensions?

6. **CKA tautology**: Both linear CKA and linear probe AUROC measure linear alignment between English and target representations. How do you establish that the positive partial correlation reflects genuine geometric structure rather than measurement overlap?

7. **Selectivity threshold**: The 0.05 selectivity threshold for declaring artifacts (Table 14-15) — is this from Hewitt & Liang's original recommendation, or was it chosen post-hoc? How sensitive are the artifact rates to this threshold (e.g., at 0.03 or 0.10)?

### 5. Minor Issues

- Table 7 (CaCLR beta sweep): The beta=1.0 row shows ΔAUROC=-0.008 with CI [-0.015, -0.001] excluding zero, yet d=0.19 is labeled as small effect. This is the one setting where CaCLR has a detectable (negative) effect, and it deserves discussion — at high beta, the consistency loss actively hurts.

- The paper reports 20 languages but Tables 1-2 show 18 (6 HIGH + 6 MID + 6 LOW). The remaining 2 languages should be accounted for, or the paper should state 18.

- The Pareto analysis code (`pareto_analysis.py`) uses Spearman correlation to test for tradeoff (line 164: `"tradeoff": "yes" if rho < 0 else "no"`), which is a one-sided test without significance threshold. Some of the 16/20 (Qwen) or 13/20 (Llama) languages with negative rho may not reach significance — the paper should report how many are significant at p < 0.05.

- The `extract_activations_large.py` uses the same split indices across all languages (line 355-368), which is correct for ensuring parallel data. However, the first language processed determines the stratification — the paper should confirm English is always processed first.

- Cohen's d values in Table 7 are very small (0.03-0.19). The paper should explicitly state these effect sizes when claiming CaCLR is "inert" — the quantitative framing strengthens the negative result.

### 6. Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | **3.5 / 5** | Experimental design is comprehensive and statistical methodology is generally strong. However, the Procrustes train/eval contamination (W1), English-only CaCLR selection criterion (W2), 1-D MMD limitation affecting the scope of the negative result claim (W3), and single-seed variance concerns (W4) collectively reduce confidence. The difficulty decomposition (W5) is the methodologically weakest component. None of these are fatal — all are addressable — but together they represent more than "minor points." |
| **Excitement** | **3 / 5** | The Simpson's Paradox finding is genuinely interesting. The control-task artifact warning has field-level utility. The practical linear projection recipe is useful. However, the CaCLR negative result, once properly scoped to 1-D MMD, is less informative than presented. The Pareto frontier, while well-quantified, is largely predicted by domain adaptation theory and prior work (Civelli et al.). The paper is more of a thorough empirical characterization than a source of surprising insights. |
| **Overall** | **3 / 5** | Findings-worthy at a strong *CL venue. The paper fills a genuine gap (English-only calibration probing literature), the experimental scale is impressive (2 large MoE models, 20 languages, 5 methods), and the statistical practices exceed field norms. The Simpson's Paradox and control-task findings are solid contributions. The main limitations — CaCLR negative result scope, difficulty decomposition weakness, Procrustes contamination, single seeds — are all addressable in revision. With the recommended fixes, this could reach 3.5. |

### 7. Confidence

**4 / 5** — I have read the code implementation in detail, verified the statistical methodology, cross-referenced the experimental results with the codebase, and have strong familiarity with the probing, calibration, and cross-lingual transfer literatures. My main uncertainty is whether the final reported numbers correspond to completed full-scale experiments or are partially projected from MVP pilots, as the project status indicates some experiments were still in preparation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be402a21-1380-489f-99de-a964ee7174db",
  "isSidechain": true,
  "agentId": "acf51195619fdbc79",
  "requestId": "req_011CbFCrtptvWczwcnYKpH6p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea5cea58-984c-40fe-be4e-39ff409194ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "91a2196c-7a23-4294-80ba-646c05703e7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2GA85zjjnUFhyrXXnTWAK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 741,
      "cache_read_input_tokens": 82014,
      "output_tokens": 3899,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 741
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3899,
          "cache_read_input_tokens": 82014,
          "cache_creation_input_tokens": 741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 741,
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
