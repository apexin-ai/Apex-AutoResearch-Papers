# Research conversation: You are Reviewer 1 (R1) for a blind peer review. Your focus is **Methods and Experiments**. ## Venue & Scoring Rubric (E

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a10e5aef12332efbc.jsonl`
- **Structured JSON:** [`c531762a4de3f8883ec6.json`](../../sessions/c5/c531762a4de3f8883ec6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

58 recorded events

### User

_source line 1 · 2026-05-13T09:55:52.043Z_

You are Reviewer 1 (R1) for a blind peer review. Your focus is **Methods and Experiments**. 

## Venue & Scoring Rubric (EMNLP 2026 via ARR)

Use these scales (0.5 increments):
- **Soundness** (1-5): 5=Exceptional, 4=Strong (sufficient support for all claims), 3=Acceptable (sufficient for main claims), 2=Poor (main claims not sufficiently supported), 1=Major issues
- **Excitement** (1-5): 5=Highly exciting, 4=Exciting, 3=Interesting, 2=Potentially interesting, 1=Not exciting
- **Overall** (1-5): 5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle
- **Reproducibility** (1-5): 5=Easily reproducible, 4=Mostly reproducible, 3=Some difficulty, 2=Difficult, 1=Cannot reproduce
- **Confidence** (1-5): 5=Positive my evaluation is correct, 4=Quite sure, 3=Pretty sure, 2=Willing to defend but may have missed details, 1=Not my area

## Paper Summary

**Title:** "When Does Circuit Consensus Fail? A Systematic Analysis of Cross-Method Agreement in Mechanistic Interpretability"

The paper formalizes a "Circuit Selection Score" (CSS) — the fraction of K=3 circuit discovery methods (EAP-IG, EP, ACDC) selecting each edge — and tests whether high-consensus edges (CSS=1.0) outperform individual methods. Evaluated across 4 tasks (IOI, Arithmetic, SVA, Factual Recall) × 2 models (GPT-2 Small, Qwen-0.5B) = 6 configurations. Central finding: consensus succeeds in only 1/6 cases (IOI on GPT-2, ΔCPR=+0.085, p=0.002).

Three failure modes identified:
1. Task-induced method correlation (high Jaccard > 0.5 → methods converge on same obvious bottleneck edges)
2. Component-level scoring degeneration on Qwen-0.5B (IFR → layer-level due to GQA; ACDC → node-level due to 179K search space)
3. Jaccard diagnostic: max pairwise Jaccard > 0.5 predicts failure with 5/6 accuracy (Spearman ρ=−0.90, p=0.037 excl. outlier)

Key experimental results:
- **Table 1**: 6 configurations, only IOI GPT-2 PASS. IOI: max_J=0.307, CSS=1.0 has 7 edges, CPR=0.109 vs best single 0.029 (ACDC), Δ=+0.085. Factual Recall: max_J=0.620, CSS=1.0 CPR=0.905 < EAP-IG 0.975, Δ=−0.070. SVA: max_J=0.653, Δ=+0.013ns. Arithmetic: max_J=0.695, Δ=−0.063. Qwen IFR: max_J=0.540, 0 CSS=1.0 edges. Qwen ACDC: max_J=0.043, 0 CSS=1.0 edges.
- **Table 2**: Factual Recall detailed — EAP-IG 50 edges CPR=0.975, CSS=1.0 10 edges CPR=0.905.
- **Table 3**: Factual Recall Jaccard matrix: EAP-IG×EP=0.62, ACDC×EAP-IG=0.38, ACDC×EP=0.33.
- **Table 4**: Size-controlled IOI — CSS=1.0 (7 edges, CPR=0.109) vs Top-7 EAP-IG (0.048), Top-7 ACDC (0.042), Top-7 EP (0.035), Random-7 (0.003±0.012). 76.3% advantage retained.
- **Table 5**: Bootstrap CIs (B=10K, BCa) — IOI Δ=+0.085 CI [0.035,0.138] p=0.002; Arithmetic Δ=−0.063 CI [−0.112,−0.018] p=0.008; Factual Recall Δ=−0.068 CI [−0.118,−0.022] p=0.005; SVA Δ=+0.013 CI [−0.025,0.052] p=0.482.
- **Table 6**: Qwen scoring granularity — IFR=Layer (J=0.0 with gradient methods), ACDC=Node (J=0.022/0.021).
- **Table 7**: Scale-dependent behavior GPT-2 vs Qwen.
- **Table 8**: Jaccard diagnostic — 5/6 correct. Only miss: Qwen ACDC (low J but FAIL due to Claim 3 not Claim 4).
- **Table 9**: IOI zero vs mean ablation — Zero Δ=+0.080, Mean Δ=+0.065, 81.3% retained.

## Experiment Design Reference (from review_context.yaml)

The imagined experiment plan includes 5 experiments:
1. GPT-2 Factual Recall K=3 CSS (v2) — covered in paper
2. IOI Size-Controlled Baseline — covered in paper (Table 4)
3. Bootstrap Confidence Intervals — covered in paper (Table 5)
4. Ablation Method Comparison (Zero vs Mean) on IOI — covered in paper (Table 9)
5. IFR vs ACDC vs Gradient Method Divergence Analysis — covered in paper (Table 6, §5.2)
6. Jaccard-CSS Diagnostic Scatter Plot + Correlation — covered in paper (Table 8, §5.3)

All 5 planned experiments appear to be reflected in the paper.

## Your Review Focus (Methods + Experiments)

Evaluate:
1. **Methodological soundness**: Is CSS well-defined? Is the binarization (top-n) approach justified? Are evaluation metrics (CPR, CMD) appropriate?
2. **Experimental design**: Is the setup sufficient to support claims? Are controls adequate? Any missing baselines?
3. **Statistical rigor**: Are bootstrap CIs appropriate? Sample sizes adequate? Multiple testing issues?
4. **Reproducibility**: Is there enough detail to reproduce? Are hyperparameters specified?
5. **Edge count confound**: The paper acknowledges CSS=1.0 has far fewer edges than individual methods (7 vs 50-100). Is the size-controlled analysis sufficient?
6. **Evaluation metrics**: CPR is the primary metric. Is CMD sufficiently discussed? Are there other metrics that should be considered?
7. **Binarization sensitivity**: Does the choice of top-n affect conclusions? Is this explored?

## Output Format

Provide your review in this structure:
```
## R1 Review: Methods & Experiments

### Summary (2-3 sentences)

### Strengths
- S1: ...
- S2: ...
- S3: ...

### Weaknesses
- W1: ...
- W2: ...
- W3: ...

### Questions for Authors
- Q1: ...
- Q2: ...

### Minor Issues
- ...

### Scores
- Soundness: X/5
- Excitement: X/5
- Overall: X/5
- Reproducibility: X/5
- Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "cfd58459-a1fd-4461-8dc4-336541702ab0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T09:55:52.050Z_

```json
{
  "parentUuid": "cfd58459-a1fd-4461-8dc4-336541702ab0",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
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
  "uuid": "689315bb-a436-4c35-81a3-df6a73b6eece",
  "timestamp": "2026-05-13T09:55:52.050Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T09:55:54.891Z_



I'll start by reading the paper and all relevant project files to conduct a thorough methods and experiments review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "689315bb-a436-4c35-81a3-df6a73b6eece",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNGThCm6SZ6EE87wssQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c65ba49d-8d55-4969-8789-c0d08c8e4bcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014894hZadkR2XejkkETMpE8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15998,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15998,
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

_source line 4 · 2026-05-13T09:55:56.389Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012PoHAVTXRiwkgJTbhJ8oYe`</summary>

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
  "parentUuid": "c65ba49d-8d55-4969-8789-c0d08c8e4bcf",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNGThCm6SZ6EE87wssQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96c42e2e-39a2-4cfd-96ea-63fddb3f141f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014894hZadkR2XejkkETMpE8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15998,
      "cache_read_input_tokens": 0,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15998
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 128,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15998,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15998,
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

_source line 5 · 2026-05-13T09:55:56.393Z_

<details><summary>↩ Tool result · `toolu_012PoHAVTXRiwkgJTbhJ8oYe`</summary>

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
  "parentUuid": "96c42e2e-39a2-4cfd-96ea-63fddb3f141f",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "098b8bfc-622f-481b-9d80-56defa7f71d8",
  "sourceToolAssistantUUID": "96c42e2e-39a2-4cfd-96ea-63fddb3f141f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T09:55:59.103Z_



Let me read the paper and all relevant project files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "098b8bfc-622f-481b-9d80-56defa7f71d8",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNGnck4a3eTfxku21Hq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46616a64-4d19-4df8-85eb-d8271639c208",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmE1C4WRox6pFxgnUxreFq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
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

_source line 7 · 2026-05-13T09:55:59.580Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_0156d5ZrRQSxQ2pRZ4B5Goxr`</summary>

```json
{
  "project": "structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46616a64-4d19-4df8-85eb-d8271639c208",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNGnck4a3eTfxku21Hq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6bd3cb8-cb1f-4536-afde-faca858376ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmE1C4WRox6pFxgnUxreFq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
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

_source line 8 · 2026-05-13T09:55:59.639Z_

<details><summary>↩ Tool result · `toolu_0156d5ZrRQSxQ2pRZ4B5Goxr`</summary>

```text
{"result":"# 项目 structfuse-context 概况\n\n## 实验状态 (10 个)\n\n- **gpt2_factual_recall_k3_v2**: RUNNING — \n- **gpt2_factual_recall_k3**: DONE (failed) — \n- **mvp_sva_gpt2_k3_topk**: DONE (negative) — \n- **phase2_qwen05b_ioi_acdc_k3**: DONE (negative) — \n- **mvp_sva_gpt2_k3**: DONE (negative) — \n- **phase2_qwen05b_ioi_k3**: DONE (negative) — \n- **mvp_arithmetic_gpt2_k3**: DONE (negative) — \n- **mvp_pilot_gpt2_ioi_v3**: DONE (success) — \n- **mvp_pilot_gpt2_ioi_v2**: DONE (failed) — \n- **mvp_pilot_gpt2_ioi**: DEPLOYED (killed) — \n\n## 最新报告\n# Handover — 2026-05-13\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| gpt2_factual_recall_k3_v2 | — | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **gpt2_factual_recall_k3** (failed): Factual Recall (国家首都) 上 CSS=1.0 faithfulness > single-method，GPT-2 第四任务验证（D025 条件④, plan_005）\n- **mvp_sva_gpt2_k3_topk** (negative): SVA 上 CSS=1.0 faithfulness > single-method（ACDC top-100 修正版，westd-pro6000 cuda:1）\n  [sva_css067_fix_results](/api/workspace-files/projects/structfuse-context/artifacts/mvp_sva_gpt2_k3_topk/data/sva_css067_fix_results.txt)\n- **phase2_qwen05b_ioi_acdc_k3** (negative): —\n\n## 趋势\n成功 1 / 负向 5 / 失败 2 / 共 8\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-39279: 无 GPU 信息\nwestd-pro6000: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_pilot_gpt2_ioi_v2: 训练失败 — unknown\n- gpt2_factual_recall_k3: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6bd3cb8-cb1f-4536-afde-faca858376ab",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "2645d762-0c29-4b27-ba54-22ba87c49406",
  "sourceToolAssistantUUID": "f6bd3cb8-cb1f-4536-afde-faca858376ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T09:56:01.128Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PfWNaENciKzRpN2GnxPmu7`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2645d762-0c29-4b27-ba54-22ba87c49406",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNGnck4a3eTfxku21Hq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d97ae851-f537-4da2-ac7a-64400891effc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmE1C4WRox6pFxgnUxreFq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
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

_source line 10 · 2026-05-13T09:56:01.141Z_

<details><summary>↩ Tool result · `toolu_01PfWNaENciKzRpN2GnxPmu7`</summary>

```text
artifacts/dream_reports/dream_20260513T054654/best/paper.tex
artifacts/dream_reports/dream_20260513T054654/median/paper.tex
artifacts/dream_reports/dream_20260513T054654/worst/paper.tex
artifacts/dream_reports/dream_20260513T081242/best/paper.tex
artifacts/dream_reports/dream_20260513T081242/worst/paper.tex
artifacts/dream_reports/dream_20260513T092135/best/paper.tex
artifacts/dream_reports/dream_20260513T092135/median/paper.tex
artifacts/dream_reports/dream_20260513T092135/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d97ae851-f537-4da2-ac7a-64400891effc",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "c5f23df2-b4be-4b4f-872c-99b7ad6b9d7b",
  "sourceToolAssistantUUID": "d97ae851-f537-4da2-ac7a-64400891effc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T09:56:01.589Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Fm6GV29WbqHfX2HP3bsar7`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5f23df2-b4be-4b4f-872c-99b7ad6b9d7b",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNGnck4a3eTfxku21Hq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fef893cd-4fcb-4ff9-8fbd-0adcb5f51ae7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmE1C4WRox6pFxgnUxreFq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15998,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1450
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 243,
          "cache_read_input_tokens": 15998,
          "cache_creation_input_tokens": 1450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1450,
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

_source line 12 · 2026-05-13T09:56:01.602Z_

<details><summary>↩ Tool result · `toolu_01Fm6GV29WbqHfX2HP3bsar7`</summary>

```text
artifacts/dream_reports/dream_20260513T054654/best/paper.pdf
artifacts/dream_reports/dream_20260513T054654/median/paper.pdf
artifacts/dream_reports/dream_20260513T054654/worst/paper.pdf
artifacts/dream_reports/dream_20260513T081242/best/paper.pdf
artifacts/dream_reports/dream_20260513T081242/worst/paper.pdf
artifacts/dream_reports/dream_20260513T092135/best/paper.pdf
artifacts/dream_reports/dream_20260513T092135/median/paper.pdf
artifacts/dream_reports/dream_20260513T092135/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fef893cd-4fcb-4ff9-8fbd-0adcb5f51ae7",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "ecfa5630-b119-4d53-819e-1b776a563987",
  "sourceToolAssistantUUID": "fef893cd-4fcb-4ff9-8fbd-0adcb5f51ae7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-13T09:56:04.316Z_

Let me read the latest "best" paper, which should be the strongest version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecfa5630-b119-4d53-819e-1b776a563987",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNHAaLgzwW6shDDpc9M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19fbf3c7-a858-47c0-8ba6-0810f6c34700",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcaSZxxvpxS91DAidmF4xz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1492,
      "cache_read_input_tokens": 17448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1492,
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

_source line 14 · 2026-05-13T09:56:05.771Z_

<details open><summary>🔧 Tool call — Read · `toolu_013bazfTz2bgnGiEeScU8ggu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T092135/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19fbf3c7-a858-47c0-8ba6-0810f6c34700",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNHAaLgzwW6shDDpc9M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3abf3be6-3e7c-45d8-8b64-f1cd4417d14a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcaSZxxvpxS91DAidmF4xz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1492,
      "cache_read_input_tokens": 17448,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1492
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 17448,
          "cache_creation_input_tokens": 1492,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1492,
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

_source line 15 · 2026-05-13T09:56:06.015Z_

<details><summary>↩ Tool result · `toolu_013bazfTz2bgnGiEeScU8ggu`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=2.5cm]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{microtype}
12	\usepackage[hidelinks]{hyperref}
13	\usepackage{url}
14	\usepackage{cite}
15	
16	\newcommand{\css}{\textsc{CSS}}
17	\newcommand{\cpr}{\textsc{CPR}}
18	\newcommand{\cmd}{\textsc{CMD}}
19	\newcommand{\eapig}{\textsc{EAP-IG}}
20	\newcommand{\acdc}{\textsc{ACDC}}
21	\newcommand{\ep}{\textsc{EP}}
22	\newcommand{\ifr}{\textsc{IFR}}
23	
24	\title{When Does Circuit Consensus Fail? \\ A Systematic Analysis of Cross-Method Agreement in Mechanistic Interpretability}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\begin{abstract}
32	Circuit discovery in mechanistic interpretability aims to identify minimal subgraphs that explain model behavior. An intuitive strategy is to trust edges endorsed by multiple discovery methods---a \emph{consensus} approach. We formalize this intuition as the \emph{Circuit Selection Score} (\css{}), a binary consensus metric computed over $K{=}3$ methods (\eapig{}, \ep{}, \acdc{}), and evaluate it across 4~tasks and 2~model architectures (GPT-2 Small, Qwen-0.5B), yielding 6~configurations. Consensus succeeds in only 1 of 6 configurations (IOI on GPT-2, $\Delta\cpr{}=+0.085$, $p{=}0.002$), while failing in the remaining 5 through three distinct mechanisms: (1)~task structure forces method correlation, collapsing consensus to obvious-edge selection (Arithmetic, Factual Recall, SVA); (2)~component-level scoring granularity on larger models causes near-zero inter-method overlap (Qwen-0.5B); and (3)~high pairwise Jaccard ($>0.5$) reliably predicts consensus failure (5/6 diagnostic accuracy, Spearman $\rho{=}{-}0.90$, $p{=}0.037$). A size-controlled baseline confirms that the sole success case reflects genuine selection quality, with 76\% of the advantage retained after controlling for edge count. These findings yield actionable guidelines: practitioners should compute pairwise Jaccard \emph{before} investing in multi-method validation, and verify that each method operates at true edge-level scoring granularity.
33	\end{abstract}
34	
35	%--------------------------------------------------
36	\section{Introduction}
37	\label{sec:intro}
38	%--------------------------------------------------
39	
40	Mechanistic interpretability seeks to reverse-engineer neural network computations by identifying \emph{circuits}---sparse subgraphs of the computational graph that are both necessary and sufficient for a given behavior \cite{elhage2021mathematical, conmy2023towards, wang2023interpretability}. Multiple circuit discovery methods now exist, each using different scoring mechanisms: gradient-based approaches (\eapig{}, \ep{}), activation patching (\acdc{}), and representation similarity (\ifr{}). An appealing idea is that edges endorsed by multiple independent methods constitute a more reliable circuit than any single method's output.
41	
42	We call this the \emph{consensus hypothesis}: cross-method agreement should identify a functionally faithful circuit core. Despite its intuitive appeal, this hypothesis has not been systematically tested. In this paper, we formalize consensus as the \emph{Circuit Selection Score} (\css{})---the fraction of methods selecting each edge---and evaluate whether high-consensus edges ($\css{}=1.0$, selected by all $K{=}3$ methods) outperform individual methods on circuit faithfulness metrics.
43	
44	Our experiments span 4~tasks (Indirect Object Identification, Arithmetic, Subject--Verb Agreement, Factual Recall) and 2~models (GPT-2 Small with 32K edges, Qwen-0.5B with 179K edges), yielding 6~model$\times$task configurations. The central finding is negative: \textbf{consensus fails in 5 of 6 configurations}, with only IOI on GPT-2 showing a statistically significant advantage ($\Delta\cpr{}=+0.085$, bootstrap $p{=}0.002$).
45	
46	We identify three mechanistic failure modes:
47	\begin{enumerate}
48	    \item \textbf{Task-induced method correlation} (\S\ref{sec:failure-correlation}): When task computation concentrates on bottleneck layers (e.g., MLP storage in Factual Recall), methods converge on the same obvious edges, and consensus degenerates to a strict subset of any single method.
49	    \item \textbf{Component-level scoring degeneration} (\S\ref{sec:failure-scaling}): On Qwen-0.5B (179K edges), both \ifr{} and \acdc{} degenerate from edge-level to node- or layer-level scoring, producing near-zero inter-method overlap and making edge-level consensus impossible.
50	    \item \textbf{Jaccard-predictable failure} (\S\ref{sec:diagnostic}): Maximum pairwise Jaccard $>0.5$ predicts consensus failure with 5/6 accuracy (Spearman $\rho=-0.90$, $p=0.037$ excluding scaling outlier), providing an actionable pre-check.
51	\end{enumerate}
52	
53	These results contribute: (a) the first systematic negative evaluation of cross-method consensus in circuit discovery; (b) a taxonomy of three distinct failure modes with mechanistic explanations; and (c) practical diagnostic guidelines that can save practitioners the computational cost of multi-method validation when consensus is unlikely to help.
54	
55	%--------------------------------------------------
56	\section{Background and Related Work}
57	\label{sec:related}
58	%--------------------------------------------------
59	
60	\paragraph{Circuit discovery methods.}
61	\eapig{} \cite{syed2023attribution} scores edges by the integrated gradient of the attribution-patching objective. \ep{} \cite{kramarcost} uses gradient-weighted edge pruning. \acdc{} \cite{conmy2023towards} iteratively removes edges via activation patching. \ifr{} \cite{zhang2024best} scores edges by intermediate representation similarity. These methods use fundamentally different scoring mechanisms (gradient products, pruning sensitivity, clean--corrupt substitution, cosine similarity), motivating the hypothesis that their agreement should be informative.
62	
63	\paragraph{Ensemble approaches.}
64	\cite{nogueira2016measuring} formalize feature selection stability via consensus indices in machine learning. \cite{kuncheva2003measures} characterize ensemble diversity and its relationship to accuracy. In circuit discovery, CIRCUS \cite{parekh2026circus} explores within-method threshold diversity, while \cite{mondorf2025comparing} average continuous scores across methods. PIE \cite{pie2026} uses iterative pruning ensembles within a single paradigm. Our work differs in testing \emph{binary} cross-method consensus---the simplest aggregation strategy---and characterizing its failure modes.
65	
66	\paragraph{Evaluation metrics.}
67	We adopt the Circuit Performance Recovery (\cpr{}) and Circuit Metric Degradation (\cmd{}) framework of \cite{conmy2023towards}. \cpr{} measures the fraction of the original model's task-specific metric recovered by the circuit; \cmd{} measures the degradation when the circuit is ablated.
68	
69	%--------------------------------------------------
70	\section{Method}
71	\label{sec:method}
72	%--------------------------------------------------
73	
74	\subsection{Circuit Selection Score}
75	
76	Given $K$ circuit discovery methods and a computational graph $G=(V,E)$, each method $k$ produces a binary edge mask $m_k: E \to \{0,1\}$ after binarization. The \emph{Circuit Selection Score} of edge $e$ is:
77	\begin{equation}
78	    \css{}(e) = \frac{1}{K}\sum_{k=1}^{K} m_k(e)
79	\end{equation}
80	We use $K{=}3$ methods (\eapig{}, \ep{}, \acdc{}) with top-$n$ binarization to equalize edge counts across methods. The consensus circuit $C_\theta = \{e : \css{}(e) \geq \theta\}$ selects edges meeting a consensus threshold $\theta$. We focus on $\css{}=1.0$ (full consensus: all three methods agree).
81	
82	\subsection{Binarization}
83	All methods are binarized to the same edge count (top-$n$) to ensure commensurability. For GPT-2 Small experiments, $n \in \{50, 100\}$; edge counts are matched per experiment. We note that \acdc{} natively uses an \texttt{isinf} threshold that can produce highly sparse outputs, and we analyze this pathology in \S\ref{sec:failure-correlation}.
84	
85	\subsection{Evaluation Protocol}
86	Circuits are evaluated under two ablation regimes:
87	\begin{itemize}
88	    \item \textbf{Zero ablation}: Complement edges set to zero. More destructive; standard in the literature.
89	    \item \textbf{Mean ablation}: Complement edges set to training-set activation means. More conservative; used for robustness checks.
90	\end{itemize}
91	For each configuration, we compute \cpr{} over 100 evaluation examples and report paired bootstrap confidence intervals ($B{=}10{,}000$, BCa correction).
92	
93	\subsection{Jaccard Diagnostic}
94	To characterize method agreement, we compute pairwise Jaccard similarity between all $\binom{K}{2}$ pairs of binary edge masks:
95	\begin{equation}
96	    J(m_i, m_j) = \frac{|m_i \cap m_j|}{|m_i \cup m_j|}
97	\end{equation}
98	The maximum pairwise Jaccard serves as a summary statistic for method correlation. We test whether this predicts \css{} outcome.
99	
100	%--------------------------------------------------
101	\section{Experiments}
102	\label{sec:experiments}
103	%--------------------------------------------------
104	
105	We evaluate \css{} on 6 model$\times$task configurations spanning two architectures and four behavioral tasks.
106	
107	\subsection{Experimental Setup}
108	
109	\paragraph{Models.} GPT-2 Small \cite{radford2019language} (12 layers, 12 heads, $\sim$32K edges) and Qwen-0.5B \cite{bai2023qwen} (24 layers, 14 heads with GQA, $\sim$179K edges).
110	
111	\paragraph{Tasks.} (1)~\textbf{Indirect Object Identification (IOI)}: Predicting the indirect object in sentences like ``Mary and John went to the store. John gave the bag to \underline{\hspace{1cm}}'' \cite{wang2023interpretability}. (2)~\textbf{Arithmetic}: Two-digit addition carry detection. (3)~\textbf{Subject--Verb Agreement (SVA)}: Number agreement across attractors. (4)~\textbf{Factual Recall}: Country$\to$capital knowledge retrieval (``The capital of France is \underline{\hspace{1cm}}'').
112	
113	\paragraph{Methods.} \eapig{}, \ep{}, and \acdc{} on GPT-2; \eapig{}, \ep{}, and \ifr{}/\acdc{} on Qwen-0.5B (two configurations due to method availability).
114	
115	%--------------------------------------------------
116	\subsection{Main Results: CSS Success Rate}
117	\label{sec:main-results}
118	%--------------------------------------------------
119	
120	Table~\ref{tab:main-results} summarizes all 6 configurations. \css{}$=1.0$ produces a \cpr{} advantage over the best single method in only 1 of 6 cases.
121	
122	\begin{table*}[t]
123	\centering
124	\small
125	\begin{tabular}{llcccccc}
126	\toprule
127	\textbf{Task} & \textbf{Model} & \textbf{Max Jaccard} & \textbf{CSS=1.0 Edges} & \textbf{CSS \cpr{}} & \textbf{Best Single \cpr{}} & $\boldsymbol{\Delta}$ & \textbf{Verdict} \\
128	\midrule
129	IOI        & GPT-2   & 0.307 & 7   & 0.109 & 0.029 (ACDC) & +0.085$^{**}$ & PASS \\
130	Factual Recall & GPT-2 & 0.620 & 10 & 0.905 & 0.975 (EAP-IG) & $-$0.070$^{**}$ & FAIL \\
131	SVA        & GPT-2   & 0.653 & --- & ---   & ---          & +0.013\textsuperscript{ns} & FAIL \\
132	Arithmetic & GPT-2   & 0.695 & --- & ---   & ---          & $-$0.063$^{**}$ & FAIL \\
133	IOI (IFR)  & Qwen    & 0.540 & 0   & ---   & ---          & 0.000 & FAIL \\
134	IOI (ACDC) & Qwen    & 0.043 & 0   & ---   & ---          & $-$0.055 & FAIL \\
135	\bottomrule
136	\end{tabular}
137	\caption{Summary of \css{} performance across all configurations. \cpr{} values are under zero ablation. $\Delta$ = CSS=1.0 \cpr{} minus best single-method \cpr{} (positive = consensus helps). $^{**}$: $p<0.01$ by paired bootstrap; \textsuperscript{ns}: not significant ($p=0.482$). IOI on GPT-2 is the sole PASS case ($\Delta=+0.085$, $p=0.002$).}
138	\label{tab:main-results}
139	\end{table*}
140	
141	\paragraph{IOI (GPT-2): The sole success.} The 7 edges at \css{}$=1.0$ correspond to name-mover heads (9.9, 9.6, 10.0) and S-inhibition heads (7.3, 8.6)---the well-characterized functional core of the IOI circuit \cite{wang2023interpretability}. With max pairwise Jaccard $= 0.307$, the three methods provide genuinely diverse rankings, and their intersection isolates high-quality edges.
142	
143	\paragraph{Factual Recall (GPT-2): MLP bottleneck forces convergence.} All three methods converge on MLP storage layers 5--9 \cite{meng2022locating}. EAP-IG$\times$EP Jaccard $= 0.62$; the 10 consensus edges are dominated by bottleneck MLP edges. These are the most ``obvious'' edges---their \cpr{} of 0.905 is lower than EAP-IG's 50-edge circuit (0.975) because consensus discards method-specific but functionally relevant routing edges.
144	
145	\paragraph{Arithmetic and SVA (GPT-2): High Jaccard, no advantage.} Both configurations show max Jaccard $>0.65$, indicating that methods largely agree. Consensus cannot improve over individual methods when the methods already select similar edges. For SVA, the bootstrap CI crosses zero ($[-0.025, 0.052]$, $p=0.482$), confirming statistical non-significance.
146	
147	\paragraph{Qwen-0.5B: Scaling failure.} Neither \ifr{} nor \acdc{} produces any \css{}$=1.0$ edges. Both methods degenerate to component-level scoring (see \S\ref{sec:failure-scaling}).
148	
149	%--------------------------------------------------
150	\subsection{Factual Recall: A New Failure Case}
151	\label{sec:factual-recall}
152	%--------------------------------------------------
153	
154	\begin{table}[t]
155	\centering
156	\small
157	\begin{tabular}{lrcc}
158	\toprule
159	\textbf{Method} & \textbf{Edges} & \textbf{Mean \cpr{}} & \textbf{Mean \cmd{}} \\
160	\midrule
161	\eapig{}    & 50 & 0.975 & 0.112 \\
162	\ep{}       & 50 & 0.952 & 0.214 \\
163	\acdc{}     & 50 & 0.938 & 0.278 \\
164	CSS$\geq$2/3 & 40 & 0.932 & 0.385 \\
165	CSS$=$1.0  & 10 & 0.905 & 0.418 \\
166	\bottomrule
167	\end{tabular}
168	\caption{Factual Recall circuit evaluation (mean ablation). CSS$=$1.0 selects 10 edges at \cpr{}$=$0.905, underperforming \eapig{}'s 50 edges at 0.975 ($\Delta=-0.070$, $p=0.005$).}
169	\label{tab:factual-recall}
170	\end{table}
171	
172	\begin{table}[t]
173	\centering
174	\small
175	\begin{tabular}{lccc}
176	\toprule
177	 & \textbf{EAP-IG} & \textbf{EP} & \textbf{ACDC} \\
178	\midrule
179	\textbf{EAP-IG} & --- & 0.62 & 0.38 \\
180	\textbf{EP}     & 0.62 & --- & 0.33 \\
181	\textbf{ACDC}   & 0.38 & 0.33 & --- \\
182	\bottomrule
183	\end{tabular}
184	\caption{Pairwise Jaccard matrix for Factual Recall (top-50). High EAP-IG$\times$EP agreement (0.62) reflects shared sensitivity to MLP bottleneck edges.}
185	\label{tab:factual-recall-jaccard}
186	\end{table}
187	
188	Factual recall relies on MLP layers 5--9 for key--value knowledge storage \cite{meng2022locating}. Table~\ref{tab:factual-recall} shows that consensus monotonically degrades performance as the threshold increases: CSS$\geq$2/3 (40 edges, \cpr{}=0.932) already underperforms individual methods, and CSS$=$1.0 (10 edges, \cpr{}=0.905) removes method-specific routing edges that are functionally important despite lacking cross-method agreement. Table~\ref{tab:factual-recall-jaccard} confirms high method correlation (max Jaccard = 0.62), consistent with the MLP bottleneck forcing convergence.
189	
190	This result parallels Arithmetic ($\Delta=-0.063$): both are MLP-bottleneck tasks where the critical computation is concentrated in a small number of layers, forcing all methods to select overlapping edges regardless of their scoring mechanism.
191	
192	%--------------------------------------------------
193	\subsection{Size-Controlled Baseline (IOI)}
194	\label{sec:size-controlled}
195	%--------------------------------------------------
196	
197	\begin{table}[t]
198	\centering
199	\small
200	\begin{tabular}{lrcc}
201	\toprule
202	\textbf{Subcircuit} & \textbf{Edges} & \textbf{Zero \cpr{}} & \textbf{vs CSS $\Delta$}\\
203	\midrule
204	CSS$=$1.0         & 7 & 0.109 & --- \\
205	Top-7 \eapig{}    & 7 & 0.048 & $-$0.061 \\
206	Top-7 \acdc{}     & 7 & 0.042 & $-$0.067 \\
207	Top-7 \ep{}       & 7 & 0.035 & $-$0.074 \\
208	Random-7 ($\mu \pm \sigma$)  & 7 & $0.003 \pm 0.012$ & $-$0.106 \\
209	\bottomrule
210	\end{tabular}
211	\caption{Size-controlled comparison on IOI (all subcircuits contain exactly 7 edges). CSS$=$1.0 outperforms all single-method top-7 selections. Random-7 baseline: mean over 50 samples. Original $\Delta=0.080$; size-controlled $\Delta=0.061$; advantage retained = 76.3\%.}
212	\label{tab:size-controlled}
213	\end{table}
214	
215	A natural concern is that the IOI consensus advantage is a size artifact: CSS$=$1.0 selects only 7 edges vs.\ the 100 edges in single-method circuits, and fewer edges mean less collateral damage under zero ablation. Table~\ref{tab:size-controlled} controls for this by comparing CSS$=$1.0 against the top-7 edges from each individual method under identical conditions.
216	
217	CSS$=$1.0 (\cpr{}$=$0.109) significantly outperforms all top-7 baselines (best: \eapig{} at 0.048; random: $0.003 \pm 0.012$, $p < 0.001$). The size-controlled advantage ($\Delta = 0.061$) retains 76.3\% of the original advantage ($\Delta = 0.080$), confirming that the consensus benefit is predominantly a \emph{selection quality} effect, not a size artifact. The remaining 23.7\% likely reflects residual collateral damage differences.
218	
219	Edge identity analysis reveals that CSS$=$1.0 edges are not ``unique'' discoveries---5 of 7 overlap with EAP-IG's top-7, and 4 of 7 with ACDC's. The advantage comes from \emph{filtering out} method-specific false positives (e.g., early-layer position embedding edges with high gradient signal but low functional contribution), not from discovering edges invisible to individual methods.
220	
221	%--------------------------------------------------
222	\subsection{Bootstrap Confidence Intervals}
223	\label{sec:bootstrap}
224	%--------------------------------------------------
225	
226	\begin{table}[t]
227	\centering
228	\small
229	\begin{tabular}{lcccl}
230	\toprule
231	\textbf{Config} & $\boldsymbol{\Delta}$ & \textbf{95\% CI} & $\boldsymbol{p}$ & \textbf{Verdict} \\
232	\midrule
233	IOI (GPT-2) & +0.085 & [0.035, 0.138] & 0.002 & Sig.\ PASS \\
234	Arithmetic  & $-$0.063 & [$-$0.112, $-$0.018] & 0.008 & Sig.\ FAIL \\
235	Factual Rec.& $-$0.068 & [$-$0.118, $-$0.022] & 0.005 & Sig.\ FAIL \\
236	SVA         & +0.013 & [$-$0.025, 0.052] & 0.482 & Non-sig. \\
237	Qwen IFR    & \multicolumn{4}{c}{N/A (0 CSS$=$1.0 edges)} \\
238	Qwen ACDC   & \multicolumn{4}{c}{N/A (0 CSS$=$1.0 edges)} \\
239	\bottomrule
240	\end{tabular}
241	\caption{Paired bootstrap CIs ($B{=}10{,}000$, BCa) for $\Delta$\cpr{} (CSS$=$1.0 vs.\ best single method). IOI is the sole configuration with a CI entirely above zero.}
242	\label{tab:bootstrap}
243	\end{table}
244	
245	Table~\ref{tab:bootstrap} reports paired bootstrap confidence intervals for all configurations where CSS$=$1.0 edges exist. IOI is the sole significant positive result ($p=0.002$, CI entirely above zero). Arithmetic and Factual Recall are significantly \emph{worse} than the best single method ($p=0.008$ and $p=0.005$, respectively). SVA's CI spans zero ($[-0.025, 0.052]$, $p=0.482$), confirming its classification as FAIL: the consensus advantage is not statistically distinguishable from noise.
246	
247	The two Qwen configurations produce zero CSS$=$1.0 edges, precluding bootstrap analysis---this is itself evidence of failure mode 2 (component-level scoring degeneration, \S\ref{sec:failure-scaling}).
248	
249	%--------------------------------------------------
250	\section{Failure Mode Analysis}
251	\label{sec:failure-modes}
252	%--------------------------------------------------
253	
254	\subsection{Failure Mode 1: Task-Induced Method Correlation}
255	\label{sec:failure-correlation}
256	
257	When a task's critical computation concentrates on a small set of bottleneck components (e.g., MLP knowledge-storage layers in Factual Recall, carry-propagation heads in Arithmetic), all discovery methods---regardless of scoring mechanism---converge on these components. The resulting high Jaccard ($>0.5$) means that consensus adds no information beyond what any single method already provides, while the strict intersection \emph{removes} method-specific edges that may be functionally important.
258	
259	Factual Recall illustrates this clearly: EAP-IG$\times$EP Jaccard $= 0.62$, with both methods selecting MLP layers 5--9 as their top-ranked edges. CSS$=$1.0 edges are almost exclusively these bottleneck edges---the ``triple-verified'' core that is also the most obvious. Meanwhile, EAP-IG's gradient signal captures attention routing edges that are method-specific but contribute to the 0.975 \cpr{} that consensus cannot match.
260	
261	\subsection{Failure Mode 2: Component-Level Scoring Degeneration}
262	\label{sec:failure-scaling}
263	
264	\begin{table}[t]
265	\centering
266	\small
267	\begin{tabular}{lcccc}
268	\toprule
269	\textbf{Method} & \textbf{Scoring} & \textbf{Granularity} & \textbf{$J$ vs \eapig{}} & \textbf{$J$ vs \ep{}} \\
270	\midrule
271	\eapig{}  & Gradient$\times$act & Edge  & --- & 0.15 \\
272	\ep{}     & Gradient prune & Edge  & 0.15 & --- \\
273	\ifr{}    & Cosine sim.    & Layer & 0.00 & 0.00 \\
274	\acdc{}   & Act.\ patching & Node  & 0.022 & 0.021 \\
275	\bottomrule
276	\end{tabular}
277	\caption{Scoring granularity on Qwen-0.5B IOI (179K edges). \ifr{} degenerates to layer-level (GQA absorbs edge perturbations); \acdc{} degenerates to node-level (greedy pruning over 179K edges). Both produce near-zero Jaccard with gradient methods.}
278	\label{tab:scaling}
279	\end{table}
280	
281	On Qwen-0.5B, the computational graph contains $\sim$179K edges---5.6$\times$ more than GPT-2 Small. Table~\ref{tab:scaling} shows that two non-gradient methods degenerate:
282	
283	\paragraph{IFR degeneration.} Qwen uses Grouped Query Attention (GQA), where heads within a group share K/V projections. Removing a single attention edge is absorbed by co-group heads, driving \ifr{}'s cosine similarity scores to near-zero for individual edges. \ifr{} consequently selects only early-layer MLP edges (layers 0--5)---a bias detector, not an IOI circuit finder. Overlap with gradient methods: $J = 0.0$.
284	
285	\paragraph{ACDC degeneration.} \acdc{}'s greedy pruning evaluates edges sequentially. At 179K edges, per-edge evaluation becomes prohibitively expensive, causing \acdc{} to operate at node level (evaluating entire attention heads). The result is block-structured edge selection (all edges of a head selected or excluded together). Max Jaccard with gradient methods: 0.043.
286	
287	The CSS framework requires each method to provide independent edge-level scores. When methods degenerate to coarser granularities, the mathematical basis for edge-level consensus breaks down: the ``edges'' selected by different methods correspond to different levels of abstraction (individual edges vs.\ head blocks vs.\ layer ranges), making intersection semantically meaningless.
288	
289	\begin{table}[t]
290	\centering
291	\small
292	\begin{tabular}{lccccc}
293	\toprule
294	& \textbf{Edges} & \textbf{ACDC} & \textbf{IFR} & \textbf{Max $J$} & \textbf{CSS$=$1.0}\\
295	\midrule
296	GPT-2 & 32K & Edge & --- & 0.307 & 7 \\
297	Qwen  & 179K & Node & Layer & 0.043 & 0 \\
298	\bottomrule
299	\end{tabular}
300	\caption{Scale-dependent method behavior. On GPT-2, \acdc{} operates at edge level; on Qwen, both \acdc{} and \ifr{} degenerate to coarser granularity.}
301	\label{tab:gpt2-vs-qwen}
302	\end{table}
303	
304	%--------------------------------------------------
305	\subsection{Failure Mode 3: Jaccard Diagnostic}
306	\label{sec:diagnostic}
307	%--------------------------------------------------
308	
309	\begin{table*}[t]
310	\centering
311	\small
312	\begin{tabular}{llccccccc}
313	\toprule
314	\textbf{Task} & \textbf{Model} & \textbf{Methods} & \textbf{Max $J$} & \textbf{CSS \cpr{}} & \textbf{Best Single \cpr{}} & $\boldsymbol{\Delta}$ & \textbf{Prediction} & \textbf{Correct?} \\
315	\midrule
316	IOI          & GPT-2 & EAP/EP/ACDC & 0.307 & 0.109 & 0.029 & +0.085 & PASS ($<$0.35) & \checkmark \\
317	IOI (ACDC)   & Qwen  & EAP/EP/ACDC & 0.043 & ---   & ---   & $-$0.055 & PASS ($<$0.35) & $\times$\textsuperscript{$\dagger$} \\
318	IOI (IFR)    & Qwen  & EAP/EP/IFR  & 0.540 & ---   & ---   & 0.000 & FAIL ($>$0.50) & \checkmark \\
319	Factual Rec. & GPT-2 & EAP/EP/ACDC & 0.620 & 0.905 & 0.975 & $-$0.070 & FAIL ($>$0.50) & \checkmark \\
320	SVA          & GPT-2 & EAP/EP/ACDC & 0.653 & ---   & ---   & +0.013 & FAIL ($>$0.50) & \checkmark \\
321	Arithmetic   & GPT-2 & EAP/EP/ACDC & 0.695 & ---   & ---   & $-$0.063 & FAIL ($>$0.50) & \checkmark \\
322	\bottomrule
323	\end{tabular}
324	\caption{Jaccard diagnostic accuracy across all 6 configurations (sorted by max pairwise Jaccard). The diagnostic correctly predicts 5/6 outcomes. $^\dagger$The sole miss (Qwen ACDC) fails due to component-level scoring degeneration (Failure Mode 2), not method correlation---an orthogonal failure that Jaccard cannot detect. Spearman $\rho = -0.90$ ($p = 0.037$) excluding the scaling outlier; $\rho = -0.714$ ($p = 0.111$) on all 6. GPT-2 subset (4 tasks): $\rho = -1.0$ ($p = 0.042$).}
325	\label{tab:diagnostic}
326	\end{table*}
327	
328	Table~\ref{tab:diagnostic} aggregates all configurations into a diagnostic summary. The maximum pairwise Jaccard serves as a strong predictor of CSS outcome:
329	
330	\begin{itemize}
331	    \item \textbf{Max Jaccard $< 0.35$}: CSS beneficial (1/1 correct---IOI on GPT-2).
332	    \item \textbf{Max Jaccard $> 0.50$}: CSS ineffective (4/4 correct---Factual Recall, SVA, Arithmetic, Qwen IFR).
333	    \item \textbf{Gap zone (0.35--0.50)}: No data points; proceed with caution.
334	\end{itemize}
335	
336	The sole diagnostic miss is Qwen ACDC (max $J = 0.043$, predicted PASS, actual FAIL). This outlier reflects Failure Mode 2: low Jaccard coexists with failure because the methods have degenerated to different scoring granularities, not because they provide diverse edge-level perspectives. The Jaccard diagnostic correctly captures method-correlation failures (Failure Mode 1) but cannot detect method-degeneration failures (Failure Mode 2).
337	
338	Within the GPT-2 subset (4 tasks where all methods operate at edge level), the rank correlation is perfect: $\rho = -1.0$ ($p = 0.042$). This supports the Jaccard diagnostic as a reliable heuristic when methods are known to function at edge-level granularity.
339	
340	We acknowledge that $n=6$ is underpowered for strong statistical claims. We frame the diagnostic as an \emph{empirically supported heuristic}, not a proven law, and recommend that future work validate it on additional tasks and models.
341	
342	%--------------------------------------------------
343	\subsection{Ablation Method Robustness (IOI)}
344	\label{sec:ablation-robustness}
345	%--------------------------------------------------
346	
347	\begin{table}[t]
348	\centering
349	\small
350	\begin{tabular}{lccccc}
351	\toprule
352	\textbf{Ablation} & \textbf{CSS \cpr{}} & \textbf{ACDC} & \textbf{EAP-IG} & \textbf{EP} & $\boldsymbol{\Delta}$ \\
353	\midrule
354	Zero & 0.109 & 0.029 & --- & --- & +0.080 \\
355	Mean & 0.182 & 0.117 & 0.078 & 0.052 & +0.065 \\
356	\bottomrule
357	\end{tabular}
358	\caption{IOI CSS advantage under zero vs.\ mean ablation. $\Delta$ = CSS$=$1.0 minus best single method. Advantage retained under mean ablation: 81.3\%.}
359	\label{tab:ablation-robustness}
360	\end{table}
361	
362	Table~\ref{tab:ablation-robustness} verifies that the IOI consensus advantage is not an artifact of the zero-ablation evaluation protocol. Under mean ablation, all \cpr{} values increase (complement edges retain mean-level signal), but the relative advantage persists: $\Delta = 0.065$ (mean) vs.\ $\Delta = 0.080$ (zero), retaining 81.3\% of the advantage. This rules out the hypothesis that consensus edges benefit disproportionately from the destructive nature of zero ablation.
363	
364	%--------------------------------------------------
365	\section{Discussion}
366	\label{sec:discussion}
367	%--------------------------------------------------
368	
369	\paragraph{Why does IOI succeed?}
370	IOI on GPT-2 is the sole configuration where consensus helps. The distinguishing feature is low method correlation (max Jaccard $= 0.307$): the three methods provide genuinely independent rankings, and their intersection filters out method-specific noise. The IOI circuit's well-characterized modular structure \cite{wang2023interpretability}---with distinct functional roles (name movers, S-inhibition heads, duplicate token detectors)---may enable methods to ``agree for the right reasons'' on the functional core while diverging on peripheral edges.
371	
372	\paragraph{Practitioner guidelines.}
373	Our results suggest a two-step protocol before investing in multi-method circuit validation:
374	\begin{enumerate}
375	    \item \textbf{Verify scoring granularity}: Ensure each method operates at true edge-level resolution. Check for block-structured edge selection (\acdc{} on large models) or layer-concentrated selection (\ifr{} with GQA). If any method has degenerated, exclude it before computing consensus.
376	    \item \textbf{Compute pairwise Jaccard}: If max pairwise Jaccard $> 0.50$, consensus is unlikely to help---use the best single method instead. If $< 0.35$, consensus may provide genuine selection-quality improvement.
377	\end{enumerate}
378	
379	\paragraph{Limitations.}
380	Our evaluation covers 2 models and 4 tasks. While the failure modes we identify are mechanistically grounded and likely general, the Jaccard thresholds (0.35, 0.50) are empirical and may require adjustment on different architectures. The $n=6$ sample size is insufficient for robust threshold estimation; we recommend these as starting points for further validation, not as established thresholds.
381	
382	%--------------------------------------------------
383	\section{Conclusion}
384	\label{sec:conclusion}
385	%--------------------------------------------------
386	
387	We present the first systematic evaluation of cross-method binary consensus in circuit discovery. Across 6 model$\times$task configurations, consensus succeeds in only one case (IOI on GPT-2, $\Delta=+0.085$, $p=0.002$), with a size-controlled baseline confirming that 76\% of this advantage reflects genuine selection quality. The remaining 5 configurations fail through three distinct, mechanistically explained failure modes: task-induced method correlation, component-level scoring degeneration at scale, and high pairwise Jaccard as a diagnostic predictor of failure. These findings provide actionable guidelines for practitioners: compute pairwise Jaccard and verify method granularity before committing to multi-method validation. The consensus hypothesis---that cross-method agreement identifies better circuits---is not wrong in principle, but its applicability is far narrower than commonly assumed.
388	
389	%--------------------------------------------------
390	% References
391	%--------------------------------------------------
392	\begin{thebibliography}{20}
393	
394	\bibitem{bai2023qwen}
395	J.~Bai et al.
396	Qwen technical report.
397	{\em arXiv:2309.16609}, 2023.
398	
399	\bibitem{conmy2023towards}
400	A.~Conmy, A.~Mavor-Parker, A.~Lynch, S.~Heimersheim, and A.~Garriga-Alonso.
401	Towards automated circuit discovery for mechanistic interpretability.
402	In {\em NeurIPS}, 2023.
403	
404	\bibitem{elhage2021mathematical}
405	N.~Elhage, N.~Nanda, C.~Olsson, et al.
406	A mathematical framework for transformer circuits.
407	{\em Transformer Circuits Thread}, 2021.
408	
409	\bibitem{kramarcost}
410	J.~Kram{\'a}r, T.~Lieberum, R.~Shah, and N.~Nanda.
411	AtP*: An efficient and scalable method for localizing LLM behaviour to components.
412	{\em arXiv:2403.00745}, 2024.
413	
414	\bibitem{kuncheva2003measures}
415	L.~I.~Kuncheva and C.~J.~Whitaker.
416	Measures of diversity in classifier ensembles and their relationship with the ensemble accuracy.
417	{\em Machine Learning}, 51(2):181--207, 2003.
418	
419	\bibitem{meng2022locating}
420	K.~Meng, D.~Bau, A.~Andonian, and Y.~Belinkov.
421	Locating and editing factual associations in GPT.
422	In {\em NeurIPS}, 2022.
423	
424	\bibitem{mondorf2025comparing}
425	P.~Mondorf, L.~Strobl, and B.~Plank.
426	Comparing circuit discovery methods for mechanistic interpretability.
427	{\em arXiv:2510.06811}, 2025.
428	
429	\bibitem{nogueira2016measuring}
430	S.~Nogueira and G.~Brown.
431	Measuring the stability of feature selection.
432	In {\em ECML-PKDD}, 2016.
433	
434	\bibitem{parekh2026circus}
435	P.~Parekh et al.
436	CIRCUS: Within-method threshold diversity for circuit discovery.
437	{\em arXiv preprint}, 2026.
438	
439	\bibitem{pie2026}
440	Anonymous.
441	PIE: Pruning iterative ensembles for circuit discovery.
442	{\em arXiv:2604.16889}, 2026.
443	
444	\bibitem{radford2019language}
445	A.~Radford, J.~Wu, R.~Child, D.~Luan, D.~Amodei, and I.~Sutskever.
446	Language models are unsupervised multitask learners.
447	{\em OpenAI Blog}, 2019.
448	
449	\bibitem{syed2023attribution}
450	A.~Syed, C.~Rager, and A.~Conmy.
451	Attribution patching outperforms automated circuit discovery.
452	{\em arXiv:2310.10348}, 2023.
453	
454	\bibitem{wang2023interpretability}
455	K.~Wang, A.~Variengien, A.~Conmy, B.~Shlegeris, and J.~Steinhardt.
456	Interpretability in the wild: A circuit for indirect object identification in GPT-2 small.
457	In {\em ICLR}, 2023.
458	
459	\bibitem{zhang2024best}
460	F.~Zhang and N.~Nanda.
461	Best practices for circuit discovery with automated interpretability.
462	{\em arXiv preprint}, 2024.
463	
464	\end{thebibliography}
465	
466	\end{document}
467	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3abf3be6-3e7c-45d8-8b64-f1cd4417d14a",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "e41423fc-6b4d-49bf-a52b-f19e5ce7a5ba",
  "sourceToolAssistantUUID": "3abf3be6-3e7c-45d8-8b64-f1cd4417d14a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-13T09:56:10.493Z_

Now let me read the project's experimental data, review context, and other relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e41423fc-6b4d-49bf-a52b-f19e5ce7a5ba",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNHVRQwkg3awjHz77my",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c38b1c6d-fd1d-435b-b785-febd566028cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZbyGewRwtzPaX5TXhb3qZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11577,
      "cache_read_input_tokens": 18940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11577,
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

_source line 17 · 2026-05-13T09:56:11.505Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0189miULT27VLoMTBNksXRcA`</summary>

```json
{
  "project": "structfuse-context",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c38b1c6d-fd1d-435b-b785-febd566028cb",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNHVRQwkg3awjHz77my",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2514feae-21b9-412e-8cd1-72139adbe0f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZbyGewRwtzPaX5TXhb3qZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11577,
      "cache_read_input_tokens": 18940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11577,
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

_source line 18 · 2026-05-13T09:56:11.521Z_

<details><summary>↩ Tool result · `toolu_0189miULT27VLoMTBNksXRcA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ROADMAP.md\", \"content\": \"# structfuse-context — Research Dashboard\\n\\n> 最后更新: 2026-05-13 UTC | 更新原因: 更新当前进展与近期任务（IOI PASS_MAIN, Arithmetic 运行中）\\n\\n## 核心方向\\n跨方法二值共识（CSS）用于鲁棒电路编辑：证明 binary stability scoring + family-agreement constraint 在分布偏移下优于 score averaging 和单方法电路。\\n\\n## 当前进展\\n- **阶段**: MVP 验证 — IOI 已 PASS_MAIN（off-diagonal 13.3%），Arithmetic 确认实验运行中\\n- **核心假设**: CSS off-diagonal ≥5%（D021 CSS-only gate，D024 覆盖 D002）\\n- **基础设施**: cqa1-21977 (cuda:5, RTX 4090D) 已配置\\n- **大模型方案已定 (D006)**: IFR 作为第三方法，triangulation 框架定位\\n- **目标**: EMNLP 2026 Main（ARR deadline 2026-05-25，剩余 12 天）\\n\\n## 方法配置\\n| 模型 | K | 方法 | 算法族 |\\n|------|---|------|--------|\\n| GPT-2 Small | 3 | EAP-IG + Edge Pruning + ACDC | gradient / mask / greedy causal |\\n| Qwen-2.5 0.5B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |\\n| Gemma-2 2B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |\\n| Llama-3.1 8B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |\\n\\n论文需披露：GPT-2 Small CSS = 3 因果方法共识；大模型 CSS = 2 因果 + 1 相似度方法共识（triangulation）。\\n\\n## MVP Gate 规则（D001-D003）\\n| off-diagonal % | 决策 |\\n|---|---|\\n| ≥10% | → Main track |\\n| 5-10% | → Findings + 追加 Arithmetic 验证 |\\n| 2-5% | → Findings 确认 |\\n| <2% (两组) + ΔF 无差异 | → Kill |\\n\\n## 阶段规划\\n\\n### Phase 1: MVP pilot（当前）\\n- GPT-2 Small / IOI，K=3（3 因果族），~2h → off-diagonal 判定\\n\\n### Phase 2: K=3 checkpoint + 全量 CSS（MVP 后 ~3天）\\n- Qwen-2.5 0.5B / IOI K=3（含 IFR）快速检查\\n- 全 4 模型 × 4 任务 CSS 计算\\n- 确认 Edge Pruning 实现：princeton-nlp/edge-pruning（非 auto-circuit mask gradient）\\n\\n### Phase 3: OOD editing（~4天）\\n### Phase 4: 分析 + 写作（~3天，最迟 5月22日）\\n\\n## 近期任务\\n- [ ] 等待 mvp_arithmetic_gpt2_k3 完成 → gate 判定\\n- [ ] Gate PASS 后 complete_mvp → 进入 research\\n- [ ] 写 paper_framing.md + experiment_plan.yaml\\n- [ ] 部署 IFR + Phase 2 实验脚本到服务器\\n- [ ] 下载目标模型（Qwen-2.5 0.5B 优先）\\n\\n## GPU 预算\\n- 已分配: 1× RTX 4090D (cuda:5@cqa1-21977)\\n- MVP: ~2h | 全量: ~290h A100（需后续扩卡）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D035 | 2026-05-13 | D035: Reframe 为分析论文 Route A — \\\"When Does Cross-Met | mvp_pilot_gpt2_ioi_v3, phase2_qwen05b_ioi_acdc_k3, mvp_arithmetic_gpt2_k3 |\\n| D034 | 2026-05-13 | D034: Qwen ACDC 确认 CSS 跨模型 scaling 根本性失败——问题不在方法选择 | phase2_qwen05b_ioi_acdc_k3, phase2_qwen05b_ioi_k3, mvp_pilot_gpt2_ioi_v3 |\\n| D033 | 2026-05-13 | D033: SVA 判定降级为 inconclusive——单 seed Δ=0.013 不具鲁棒性 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |\\n| D032 | 2026-05-13 | D032: 条件④评估指标修正——必须用 css_1.00 而非 css_0.67 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |\\n| D031 | 2026-05-13 | 统一 D025 条件④标准：zero PASS 或 mean Δ≥0.01，SVA 两次均判 neg | mvp_sva_gpt2_k3, mvp_sva_gpt2_k3_topk |\\n| D030 | 2026-05-13 | SVA D025 gate FAIL（zero FAIL / mean 边际 Δ=0.008）；发现 | mvp_sva_gpt2_k3_topk |\\n| D029 | 2026-05-13 | Phase 2 第三方法：放弃 IFR，改用 ACDC top-k。IFR 跨族分歧作为 Discu | phase2_qwen05b_ioi_k3 |\\n| D028 | 2026-05-13 | Phase 2 IFR 零重叠问题：暂停 Qwen/Gemma 新实验，先修 IFR per-hea | phase2_qwen05b_ioi_k3 |\\n| D027 | 2026-05-13 | MVP 最终判定：CSS faithfulness 优势 task-dependent（IOI PA | mvp_arithmetic_gpt2_k3, mvp_pilot_gpt2_ioi_v3 |\\n| D026 | 2026-05-13 | Arithmetic D025 gate FAIL（条件④），暂不判 MVP 结果，先做 ACDC  | mvp_arithmetic_gpt2_k3 |\\n\\n\", \"total_chars\": 3059, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2514feae-21b9-412e-8cd1-72139adbe0f5",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "d275b01e-ab8f-42ac-9e68-8c8dd7808ec1",
  "sourceToolAssistantUUID": "2514feae-21b9-412e-8cd1-72139adbe0f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T09:56:12.010Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JmJNyovD9RZGEGpFDZiRUP`</summary>

```json
{
  "project": "structfuse-context",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d275b01e-ab8f-42ac-9e68-8c8dd7808ec1",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNHVRQwkg3awjHz77my",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "459a4b40-01dc-4ef7-b5b9-f2d88666aaf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZbyGewRwtzPaX5TXhb3qZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11577,
      "cache_read_input_tokens": 18940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11577,
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

_source line 20 · 2026-05-13T09:56:12.019Z_

<details><summary>↩ Tool result · `toolu_01JmJNyovD9RZGEGpFDZiRUP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| gpt2_factual_recall_k3_v2 | — | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **gpt2_factual_recall_k3** (failed): Factual Recall (国家首都) 上 CSS=1.0 faithfulness > single-method，GPT-2 第四任务验证（D025 条件④, plan_005）\\n- **mvp_sva_gpt2_k3_topk** (negative): SVA 上 CSS=1.0 faithfulness > single-method（ACDC top-100 修正版，westd-pro6000 cuda:1）\\n  [sva_css067_fix_results](/api/workspace-files/projects/structfuse-context/artifacts/mvp_sva_gpt2_k3_topk/data/sva_css067_fix_results.txt)\\n- **phase2_qwen05b_ioi_acdc_k3** (negative): —\\n\\n## 趋势\\n成功 1 / 负向 5 / 失败 2 / 共 8\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39279: 无 GPU 信息\\nwestd-pro6000: 空闲 cuda:0, cuda:1\\n\\n## 告警\\n- mvp_pilot_gpt2_ioi_v2: 训练失败 — unknown\\n- gpt2_factual_recall_k3: 训练失败 — unknown\\n\", \"total_chars\": 870, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "459a4b40-01dc-4ef7-b5b9-f2d88666aaf4",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "4f03cb14-f4d6-43f1-8698-d0f426a087b8",
  "sourceToolAssistantUUID": "459a4b40-01dc-4ef7-b5b9-f2d88666aaf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T09:56:12.614Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HuZhM5SpFVqRKAdjJZKkjm`</summary>

```json
{
  "project": "structfuse-context",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f03cb14-f4d6-43f1-8698-d0f426a087b8",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNHVRQwkg3awjHz77my",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecb8ec3e-c0f7-429f-a2b1-3ae8cb5515e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZbyGewRwtzPaX5TXhb3qZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11577,
      "cache_read_input_tokens": 18940,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11577
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 18940,
          "cache_creation_input_tokens": 11577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11577,
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

_source line 22 · 2026-05-13T09:56:12.625Z_

<details><summary>↩ Tool result · `toolu_01HuZhM5SpFVqRKAdjJZKkjm`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecb8ec3e-c0f7-429f-a2b1-3ae8cb5515e9",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "431f0ebe-18c1-4490-b3f3-2de658b044dd",
  "sourceToolAssistantUUID": "ecb8ec3e-c0f7-429f-a2b1-3ae8cb5515e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T09:56:15.662Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Ux5GssD4TEsnaytU7dizMD`</summary>

```json
{
  "project": "structfuse-context",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "431f0ebe-18c1-4490-b3f3-2de658b044dd",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNHytSJ9L9XEHsYnirY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f0341fd-7067-42f4-a223-010210838744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAJ6MKbrn3vqK7VqM7eros",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3124,
      "cache_read_input_tokens": 30517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3124,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 24 · 2026-05-13T09:56:15.674Z_

<details><summary>↩ Tool result · `toolu_01Ux5GssD4TEsnaytU7dizMD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/decisions.yaml\", \"content\": \"_next_id: 36\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: MVP 定义为 pre-registered pilot：GPT-2 Small/IOI 上 K=4 方法 CSS + CIRCUS cross-tabulation\\n  rationale: 'IDEA_BRIEF 已定义 pilot 为第一个计算里程碑（~2h），直接检验核心假设\\\"方法类 artifact 可被二值共识检测\\\"。Pass\\n    criterion: ≥10% CIRCUS-core 边落入 off-diagonal cell。该 pilot 同时也是论文 Section 3 的 motivating\\n    result，失败则需 reframe 为 Findings track。选择此 MVP 因为：(1) 成本极低（~2h 单卡）(2) 直接验证核心假设 (3)\\n    结果直接决定投稿策略。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 09:59 UTC\\n  summary: 定义 MVP gate 灰区规则：5-10% off-diagonal → Findings + 追加第二组 task 验证\\n  rationale: 'Reviewer warning: 5%-10% 灰区无决策规则。决定：5-10% 默认走 Findings track，但在 GPT-2\\n    Small / Arithmetic 上追加验证。若第二组 ≥10% → 升级回 Main；若第二组也 5-10% → 确认 Findings；若第二组 <5%\\n    → 评估是否 IOI 特有现象。同时要求 MVP 报告包含 CIRCUS-core 绝对边数 + binomial 95% CI，若 CIRCUS-core\\n    <30 条边则必须追加第二组 task。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-12 09:59 UTC\\n  summary: 定义项目级 kill criteria：off-diagonal <2% + ΔF 无统计差异 → kill\\n  rationale: 'Reviewer warning: 缺项目级 kill criteria。决定：off-diagonal <2% across GPT-2\\n    Small 两个 task (IOI + Arithmetic) AND 四种电路 ΔF 无统计显著差异 (bootstrap p>0.05) → kill\\n    project。单一 task <2% 不触发 kill，需两组确认。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D004\\n  date: 2026-05-12 09:59 UTC\\n  summary: MVP 通过后增加 K=3 checkpoint：Qwen-2.5 0.5B / IOI 快速验证\\n  rationale: 'Reviewer warning: 3/4 模型用 K=3 + family constraint，但 pilot 仅测 K=4。决定：MVP\\n    通过后、全量实验前，增加 Qwen-2.5 0.5B / IOI 的 K=3 快速检查（EAP-IG + AtP* + Edge Pruning，~数小时）。若\\n    K=3 family constraint 下 off-diagonal 完全消失（<2%），需重新评估大模型贡献——可能论文仅限 K=4 结果或需要调整\\n    family constraint 定义。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-12 10:08 UTC\\n  summary: AtP* 无 edge-level 实现：MVP 改为 K=3（EAP-IG+Edge Pruning+ACDC），大模型方案待评估\\n  rationale: 'Reviewer critical: AtP* 官方未开源，社区版仅 node-level。影响：(1) GPT-2 Small 原 K=4\\n    降为 K=3，但 EAP-IG+EP+ACDC 恰好覆盖 3 个算法族（gradient/mask/greedy causal），实际更干净；(2) 大模型原\\n    K=3 降为 K=2（仅 EAP-IG+EP），CSS 退化为平凡二值投票，严重削弱贡献。决策：MVP 用 K=3（3族）推进，同时评估大模型第三方法：(a)\\n    AtP* 自行实现可行性（≤1天）(b) PAHQ 加速 ACDC 到大模型的可行性 (c) MIB 其他 edge-level 方法的算法族分类。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D006\\n  date: 2026-05-12 10:28 UTC\\n  summary: 大模型 K=3 第三方法确定为 IFR，论文采用 triangulation 框架定位\\n  rationale: Agent 评估三条路径：(a) AtP* 自实现仍是 gradient 族，不解决 K=2 仅 2 族问题 (b) PAHQ 加速 ACDC\\n    不可行 (c) MIB 方法中 IFR 唯一满足\\\"非 gradient、非 mask optimization、edge-level、可扩展到 8B\\\"。Reviewer\\n    确认 IFR 为最佳选项，但指出 IFR 是非因果方法（度量激活空间 proximity 而非因果贡献）。采纳 Reviewer 建议：论文定位 IFR 为\\n    triangulation 中的\\\"independent signal\\\"而非\\\"causal validator\\\"——若一条边同时被因果方法 + 优化方法 +\\n    相似度方法识别，作为机制组件的证据更强。GPT-2 Small（3 因果方法）vs 大模型（2 因果 + 1 非因果）的 CSS 语义差异须在论文中诚实披露。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-12 12:11 UTC\\n  summary: GPU 越界事故：kill 越界进程 + 修复 CUDA_VISIBLE_DEVICES + 重跑 MVP\\n  rationale: 'Reviewer critical: 项目进程跑到 cuda:0/cuda:1（白名单仅 cuda:5），L1 红线违规。原因推测为 Agent\\n    重启进程时未设 CUDA_VISIBLE_DEVICES=5。处置：立即 kill + 修复启动脚本加入 GPU 硬检查 + cuda:5 上重跑。ACDC\\n    71.5% 进度丢失。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D008\\n  date: 2026-05-12 13:02 UTC\\n  summary: MVP 结果解读协议：mask_gradient proxy 下 ≥10% 可信（保守估计），<10% 需 L0 EP 重测\\n  rationale: 当前 MVP 实际为 2 族（EAP-IG + mask_gradient 同属 gradient，+ ACDC greedy causal），非\\n    3 族。同族方法更易同意 → off-diagonal 偏低。因此：≥10% 是保守估计（真实跨族分歧可能更大），gate pass 可信；<10% 不直接判\\n    fail，需部署 L0 EP 到服务器重测 IOI 后再做 gate 判定。Phase 2 全量实验无论如何必须换 L0 EP。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n  - D007\\n- id: D009\\n  date: 2026-05-12 17:01 UTC\\n  summary: 修复边名格式不匹配 critical bug：统一 EAP-IG 和 EP/ACDC 的边名归一化到同一 canonical form\\n  rationale: Reviewer 发现 _normalize_eap_edge 产出 dash 分隔符 + m0 格式，_normalize_ac_edge\\n    产出 arrow 分隔符 + mlp 0 格式，导致 css.py 字符串匹配完全失败，所有 CSS 值和 off_diagonal_pct 无效。修复方案：统一\\n    canonical form + 转换已有缓存，不重跑 discovery。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi\\n    role: affected\\n    result: CSS 结果因边名 bug 无效，需修复后重算\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-12 18:40 UTC\\n  summary: Phase 2 IFR binarization策略：用 percentile threshold 或 unique-score-rank 替代\\n    top-N，避免 layer-block voting 偏差\\n  rationale: Reviewer 审查发现 IFR run_ifr() 对同一 (src, dst_layer) 的所有 head×QKV 赋相同 proximity\\n    score（residual-stream proximity 固有局限），导致每对产生 36 条同分边。CSS binarize_scores 的 top-N\\n    模式下少数 (src,layer) 对即可 block-vote 占满配额，与 EAP-IG/EP 的 per-edge 粒度系统性不匹配，可能人为膨胀/压缩\\n    off-diagonal。不影响 MVP（MVP 不含 IFR），Phase 2 集成时需：(1) 改用 percentile threshold 或 unique-score-rank\\n    binarization (2) 论文披露 IFR layer-block 粒度 vs 其他方法 edge 粒度差异。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D011\\n  date: 2026-05-12 19:13 UTC\\n  summary: EP HF 后端需重构：从 layer pre-hook 改为 submodule-level hooks（q_proj/k_proj/v_proj/mlp\\n    各自 hook），修复 MLP mask 未应用 + Q/K/V 聚合两个问题\\n  rationale: Reviewer 发现 EP HF 实现有两个 warning：(1) MLP edge mask 参数参与 backward 但 forward\\n    无 hook 应用，MLP score 不可信；(2) 同一 (src, layer) 的所有 Q/K/V edge mask 被 mean 聚合为单标量，丢失\\n    per-edge 粒度。两个问题使 EP 退化为 layer-level masking。修复方案：将 hook 从 layer pre-hook 下沉到\\n    q_proj/k_proj/v_proj/mlp submodule level，每个 submodule 独立 hook 并应用对应 edge mask。这在\\n    HF hook 框架内可行，不需要重写 forward pass。若不修复，Phase 2 K=3 中 EP+IFR 都是 approximate，CSS\\n    edge-level 共识叙事被削弱。\\n  related_experiments: []\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-12 22:19 UTC\\n  summary: Reviewer 洞察：cross-tabulation（CIRCUS×CSS → 2×2 矩阵）应作为论文核心 novelty claim，而非仅\\n    CSS 填补 gap\\n  rationale: Reviewer 审查 related_work_notes.md 指出：CIRCUS（intra-method stability）×\\n    CSS（cross-method consensus）的系统组合产生 stable_core / method_specific 分类，这个 cross-tabulation\\n    在现有文献中无人做过。比单独宣称 CSS 新颖性更强。同时记录：(1) GPT-2 Small K=3 中 EAP-IG+EP 同为 gradient-adjacent\\n    需在论文中论证 optimization 差异；(2) 2025-2026 引用需 reference-audit 验证；(3) Phase D faithfulness\\n    评估必须证明 stable_core 优于 single-method circuit。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n  - D008\\n- id: D013\\n  date: 2026-05-12 22:24 UTC\\n  summary: CIRCUS 实现 bug：1D percentile sweep 产生嵌套电路，退化为 top-k。MVP v3 不中断（结果仍有信息量），Phase\\n    2 必须修复为 2D non-nested grid\\n  rationale: Reviewer 发现 circus.py 用 np.linspace percentiles 产生严格嵌套 C(t_low)⊇C(t_high)，违反\\n    CIRCUS 原文 non-nesting 约束。退化后 stability=1.0 core = top-9.1% 边（B=10），失去 config-bagging\\n    统计意义。MVP v3 cross-tabulation 仍测试 CSS vs score-ranking 一致性，gate 判定可用，故不中断。Phase\\n    2 须改为 2D grid（node threshold × edge threshold）或 random-subset 采样实现 non-nesting。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: affected\\n    result: running, results still informative despite CIRCUS degradation\\n  depends_on:\\n  - D012\\n- id: D014\\n  date: 2026-05-12 23:04 UTC\\n  summary: 论文 framing 校准：4-cell taxonomy 为核心 novelty，contribution statement 弱化避免全称量词，Phase\\n    D 增加 method_specific/cross_unstable 独立评估\\n  rationale: Reviewer 深度评估确认：(1) CIRCUS×CSS cross-tabulation 在文献中无先例，novelty 成立；(2)\\n    当前 statement 过强——\\\"any\\\" 全称量词和 \\\"distribution shift\\\" claim 缺实验支撑，需弱化；(3) 4-cell taxonomy\\n    是最强贡献点，但必须实证 4 个 cell 有不同 faithfulness 特性；(4) Phase D 需增加 method_specific 和 cross_unstable\\n    独立 CPR/CMD 评估；(5) OOD 评估（ioi_variant）应提至 priority 2；(6) D013 CIRCUS 修复已完成，Phase\\n    2 用修复版本。faithfulness 必须满足：CPR(stable_core) ≥ 0.8×CPR(best_single_method) 且 |stable_core|\\n    < |best_single_method| 且优于纯 CSS 和纯 CIRCUS。\\n  related_experiments: []\\n  depends_on:\\n  - D012\\n  - D013\\n- id: D015\\n  date: 2026-05-12 23:04 UTC\\n  summary: Framing 调整：claim 降级删除全称量词和 OOD claim；Phase D 必须增加 method_specific + cross_unstable\\n    独立 faithfulness 评估；MVP 后首检 4-cell cardinality\\n  rationale: Reviewer 两轮一致评估：(1) \\\"any single-method\\\" 全称量词超出 1 模型×1 任务实验覆盖；(2) \\\"distribution\\n    shift\\\" 无 OOD 数据支撑；(3) 4-cell taxonomy 是文献空白（novelty 成立），但需实证 4 个 cell 各有不同特性——当前\\n    Phase D 只评 stable_core，缺 method_specific/cross_unstable 独立评估；(4) D008 风险：gradient-adjacent\\n    方法可能压缩 method_specific cell。暂定 claim：\\\"competitive or superior faithfulness with\\n    fewer edges\\\"。OOD claim 推 Phase 2。\\n  related_experiments: []\\n  depends_on:\\n  - D012\\n  - D013\\n  - D008\\n- id: D016\\n  date: 2026-05-12 23:09 UTC\\n  summary: 更正：D013 CIRCUS config_bag nonnesting 修复未实际完成。Agent 产出为 Phase 2 前置代码（L0\\n    EP + IFR），远程 circus.py 零改动。另发现 L0 EP per-layer 粒度问题，Phase 2 前必须修复\\n  rationale: Reviewer 审查 worker 产出发现：(1) 远程 circus.py 仍为 1D percentile nesting，config_bag()\\n    未改动，Agent 报告的\\\"17 测试通过\\\"与实际不符；(2) 新增 edge_pruning_l0.py 的 mask 粒度为 (src, dst_layer)，所有\\n    head×QKV 共享同一值，与 EAP-IG per-edge 粒度不一致。Phase 2 三方法中两个（L0 EP + IFR）退化为 layer-level，CSS\\n    edge-level 共识叙事不成立。两项均为 Phase 2 启动前必修。\\n  related_experiments: []\\n  depends_on:\\n  - D013\\n  - D011\\n  - D010\\n- id: D017\\n  date: 2026-05-12 23:14 UTC\\n  summary: CRITICAL：CIRCUS-CSS 作用域不匹配导致 off-diagonal 结构性膨胀 ~98%，v3 cross-tabulation\\n    无效。需统一 edge universe 后重算\\n  rationale: Reviewer 发现 CIRCUS 在全量 32491 边上操作（core≈2953 条），CSS 在三方法二值化电路并集（~150 条）上操作，20\\n    倍作用域差距。CIRCUS-core 中不在二值化电路的边自动 CSS=0 → method_specific≈2893 条 → off-diagonal≈98%，为测量\\n    artifact。同时 EP binarization 用 score>0.5 对 mask_gradient 输出无意义（梯度分数非 [0,1]），导致\\n    EP 选边极少（~20-50 条）。修复方向：(1) 统一 edge universe 为三方法二值化电路并集，CIRCUS 只在此并集内操作；(2) EP\\n    改为 top-N 或 percentile binarization；(3) gate KILL 改为 KILL_CANDIDATE（D003 要求两 task）。v3\\n    原始 scores 可复用，无需重跑。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: invalidated_analysis\\n    result: raw data valid, cross-tabulation invalid due to scope mismatch\\n  depends_on:\\n  - D013\\n  - D016\\n  - D008\\n- id: D018\\n  date: 2026-05-13 01:26 UTC\\n  summary: MVP gate 条件性 PASS_MAIN：off-diagonal 13.3% ≥ 10%，但 CIRCUS-core=15 < 30 触发\\n    D002，需 Arithmetic task 确认\\n  rationale: K=3 corrected 分析（修复 ACDC binarization 后）：off-diagonal 2/15=13.3%，点估计过\\n    ≥10% 线 → PASS_MAIN。但 95% CI [1.7%, 40.5%] 横跨所有 gate 区间，统计功效不足。D002 明确规定 core <\\n    30 时必须追加第二 task 验证。同时 CSS ≥ 2/3 对已知 IOI 12-edge 电路 recall=1.0 是强正面信号，说明 cross-method\\n    consensus 确实能捕捉真实电路结构。Pairwise Jaccard（EAP-IG×ACDC=0.096, EP×ACDC=0.086）在文献典型范围内，证实方法间存在真实分歧。EAP-IG×EP=0.307\\n    偏高（gradient-adjacent），Phase 2 切 L0 EP 后预期改善。决策：暂定 PASS_MAIN，待 Arithmetic task\\n    确认后正式通过 MVP gate。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: primary\\n    result: off-diagonal 13.3%, CSS recall=1.0, conditional PASS\\n  depends_on:\\n  - D001\\n  - D002\\n  - D008\\n- id: D019\\n  date: 2026-05-13 01:32 UTC\\n  summary: 补充 gate criterion：Arithmetic 不仅看 off-diagonal %，还需验证 CSS faithfulness >\\n    single-method faithfulness 排序\\n  rationale: Reviewer 指出 CIRCUS-core 自身 CPR 为负（-0.108），说明 CIRCUS stability 与功能重要性不相关，off-diagonal\\n    % 作为唯一 gate 指标解释力不足。但 faithfulness 排序 CSS=3/3 (0.110) > CSS≥2/3 (0.063) > ACDC\\n    (0.029) > single-method (负值) 清晰支撑核心论点\\\"跨方法共识 → 更高质量电路\\\"。决定：Arithmetic gate 判定同时要求\\n    (1) off-diagonal 存在（>0%，证明方法特异性 artifact 存在）(2) CSS faithfulness > best single-method\\n    faithfulness（证明 consensus 的功能价值）。两条都满足 → PASS_MAIN；只满足一条 → 评估是否 task-specific；都不满足\\n    → 重新评估方向。同时要求 Arithmetic Phase D 使用 mean ablation 作为 zero ablation 的对比，排除 ablation\\n    方式的影响。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: evidence\\n    result: faithfulness ranking supports CSS > single-method\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: planned\\n    result: pending - must verify both off-diagonal + faithfulness ordering\\n  depends_on:\\n  - D018\\n  - D002\\n- id: D020\\n  date: 2026-05-13 01:34 UTC\\n  summary: 'CRITICAL: stable_core faithfulness 三重 FAIL，暂停 MVP pass 判定。根因是 D013 CIRCUS\\n    退化未修复——stable_core CPR=-0.187 远差于 CSS≥0.67 (CPR=+0.063)。必须先修复 CIRCUS (2D non-nested\\n    grid) 再重评。'\\n  rationale: Reviewer 深度验证发现：(1) stable_core IOI recall 仅 0.17 (2/12)，因为 CIRCUS-core\\n    系统性选中 Negative Name Mover 通路而非核心 IOI 正向信号边；(2) 这是 D013 CIRCUS 1D percentile →\\n    top-k EAP-IG 退化的直接后果；(3) CSS≥0.67 单独就达到 12/12 IOI recall + 正向 CPR，说明 cross-tabulation\\n    的\\\"附加价值\\\"目前为负；(4) D018 条件性 pass (off-diagonal 13.3%) 在 faithfulness 硬伤未修复前无效。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: evidence\\n    result: stable_core CPR=-0.187, IOI recall=0.17; CSS≥0.67 CPR=+0.063, recall=1.00\\n  depends_on:\\n  - D018\\n  - D013\\n  - D014\\n- id: D021\\n  date: 2026-05-13 02:07 UTC\\n  summary: 放弃 CIRCUS 作为独立 claim，转 CSS-only 叙事。CIRCUS 三次修复均失败，降级为 negative ablation\\n  rationale: CIRCUS 经历三轮修复全部失败：(1) D013 发现 1D percentile 嵌套退化为 top-k；(2) D020 stable_core\\n    faithfulness 三重 FAIL；(3) random-subset fix 后 stable_core CPR=-0.023, IOI recall=0/12，比旧版更差。根本问题是\\n    faithfulness-based stability scoring 在当前 circuit 粒度下无法产出有意义的 stable core。ARR DDL\\n    剩 12 天，不能再投入时间调试。CSS off-diagonal 13.3% 已过 gate，CSS-only 叙事足够支撑论文。CIRCUS 失败作为\\n    negative ablation 保留（\\\"structural consensus > faithfulness scoring\\\"），反而强化 CSS 的\\n    claim。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: evidence\\n    result: CSS off-diagonal 13.3% pass, but CIRCUS stable_core triple fail\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: ongoing\\n    result: Arithmetic validation running, independent of CIRCUS\\n  depends_on:\\n  - D020\\n  - D018\\n  - D013\\n- id: D022\\n  date: 2026-05-13 02:11 UTC\\n  summary: 紧急处理第三次 GPU 越界事件：杀 PID 897752 + 根因排查 + 强制 CUDA_VISIBLE_DEVICES=5\\n  rationale: Manager 报告进程 PID 897752 (17GB, 100% util) 越界占用 cuda:0（属于 rl-active-probe-fl\\n    项目），已导致对方代码和数据丢失。这是 cqa1-21977 上第三次越界事件，Manager 警告再犯将回收 GPU。根因待 Agent 排查（CUDA_VISIBLE_DEVICES\\n    未正确设置或被覆盖）。要求所有后续实验脚本开头强制 export CUDA_VISIBLE_DEVICES=5。\\n  related_experiments:\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: suspected_source\\n    result: 疑似越界进程来源，待确认\\n  depends_on: []\\n- id: D023\\n  date: 2026-05-13 02:18 UTC\\n  summary: 澄清 D021 与 D002 灰区关系：Arithmetic 实验 gate 统一为 CSS off-diagonal ≥5%，D002 的\\n    5-10% 灰区规则不再适用\\n  rationale: D002 原定义基于 CIRCUS-core edges：≥10% PASS_MAIN，5-10% 灰区走 Findings track。D021\\n    已从 CIRCUS 转向 CSS-only，指标体系变化，原灰区阈值不再有意义。Arithmetic 实验 gate 统一为 CSS off-diagonal\\n    ≥5% = PASS（确认跨任务泛化性），<5% = FAIL。D002 的 5-10% 灰区规则被 D021 显式 deprecate。\\n  related_experiments:\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: gate_experiment\\n    result: running\\n  depends_on:\\n  - D002\\n  - D021\\n- id: D024\\n  date: 2026-05-13 02:18 UTC\\n  summary: D021 覆盖 D002 灰区定义：arithmetic CSS off-diagonal ≥5% 即为 PASS，不再区分灰区\\n  rationale: D002 原定 5-10% 为灰区（走 Findings track），≥10% 为 PASS_MAIN。D021 pivot 为 CSS-only\\n    后将 arithmetic gate 改为 ≥5%。Reviewer 指出两者语义冲突。决定：D021 显式覆盖 D002 的灰区规则。理由：CSS-only\\n    pivot 后 off-diagonal 的意义更明确（纯 consensus 信号），5% 阈值已足够表明 cross-method structural\\n    agreement 非 task-specific。D002 的 5-10% 灰区基于 CIRCUS+CSS 混合框架下的不确定性，该前提已不存在。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n  - D021\\n- id: D025\\n  date: 2026-05-13 03:14 UTC\\n  summary: 更新 Arithmetic gate 为 CSS-only 四条件标准（替代 D024 的单一 5% 阈值）\\n  rationale: Reviewer 审查发现：(1) run_arithmetic.py 代码仍跑 CIRCUS cross-tabulation + D002\\n    旧阈值，D024 未落地到代码；(2) CIRCUS 已知 broken（D013 nesting + D017 scope mismatch），基于 CIRCUS\\n    的 off-diagonal % 无意义。采纳 Reviewer 建议的 CSS-only 四条件 gate：① Pairwise Jaccard 任意方法对\\n    < 0.70 ② CSS ≥2/3 edge count ≥ 10 ③ CSS = 1.0 edge count ≥ 3 ④ CSS faithfulness\\n    > single-method（D019）。四条全满足 = PASS。实验不中断（ACDC 75%+），结果出来后忽略代码 gate_verdict，人工按新标准判定。\\n  related_experiments:\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: target\\n    result: RUNNING\\n  depends_on:\\n  - D024\\n  - D021\\n  - D019\\n- id: D026\\n  date: 2026-05-13 03:39 UTC\\n  summary: Arithmetic D025 gate FAIL（条件④），暂不判 MVP 结果，先做 ACDC 阈值 ablation + mean ablation\\n    诊断\\n  rationale: Arithmetic CSS=1.0 CPR=-0.197 < EAP-IG CPR=-0.142，条件④失败。但 Reviewer 同时发现两个方法论问题：(1)\\n    ACDC isinf 仅保留 17 边，与 EAP-IG/EP 各 100 边形成 6:1 不对称，CSS=1.0 退化为纯 ACDC 输出；(2) 所有小电路\\n    CPR 均为负，zero ablation 可能对 Greaterthan 过于苛刻。这两个问题在 IOI 上同样存在但被正结果掩盖。在排除 binarization\\n    artifact 和 ablation method artifact 之前，不应判定 CSS 方法论失败。诊断方案：(a) ACDC top-k 阈值 sweep（k=50/100/150，CPU\\n    分析，不需新 GPU 实验）；(b) mean ablation 替代 zero ablation 重算 Phase D。两者均可在已有 raw scores\\n    上快速完成。\\n  related_experiments:\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: primary\\n    result: D025 gate FAIL (condition ④)\\n  depends_on:\\n  - D025\\n  - D019\\n- id: D027\\n  date: 2026-05-13 04:37 UTC\\n  summary: MVP 最终判定：CSS faithfulness 优势 task-dependent（IOI PASS / Arithmetic FAIL），不\\n    kill，reframe claim scope\\n  rationale: Arithmetic D025 条件④在 2 ablation × 4 k = 8 个配置下全部 FAIL，排除了 isinf 退化和 zero\\n    ablation artifact。IOI 在 zero ablation 下一致 PASS（k=isinf/50/100 均通过）。CSS 不是普遍优于单方法，而是在\\n    localized-circuit 任务（IOI 有明确的 Name Mover 等组件）上有效，在 distributed-computation 任务（Greaterthan）上无效。D003\\n    kill criteria 未触发（两任务 off-diagonal 均 >2%）。方向决策：(1) 不 kill 项目 (2) Reframe：从\\\"CSS\\n    always better\\\"转为\\\"CSS identifies faithful consensus when circuits are localized;\\n    reveals task structure when they're not\\\" (3) 补 1-2 个任务建立 localized vs distributed\\n    模式 (4) 这个发现本身比 universal claim 更有学术价值——审稿人更 appreciate nuanced finding。\\n  related_experiments:\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: primary\\n    result: FAIL (condition ④ across all 8 configs)\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: reference\\n    result: PASS (consistent across k and ablation)\\n  depends_on:\\n  - D026\\n  - D025\\n  - D021\\n- id: D028\\n  date: 2026-05-13 07:31 UTC\\n  summary: Phase 2 IFR 零重叠问题：暂停 Qwen/Gemma 新实验，先修 IFR per-head 分解 + 调 binarization\\n    比例\\n  rationale: Qwen-0.5B IOI K=3 实验显示 IFR×EAP-IG Jaccard=0.000, IFR×EP Jaccard=0.000，CSS=1.0=0\\n    条边。根因是 D010 已标记的 IFR layer-block voting：同层所有 head×QKV 共享 score，top-100 选出的边与 per-head\\n    方法完全正交。附加问题：179K 边取 top-100=0.06%，远低于 GPT-2 的 0.3%。两个修复方向并行验证：(1) ifr_scoring.py\\n    的 _decompose_per_head() 分解每头输出；(2) 改用 proportional binarization top-0.3%（~538\\n    边）。修复验证前暂停 Qwen/Gemma 新实验。SVA（GPT-2 + ACDC）不受影响，继续跑。\\n  related_experiments:\\n  - exp_id: phase2_qwen05b_ioi_k3\\n    role: primary\\n    result: CSS=1.0=0 edges, IFR zero overlap\\n  depends_on:\\n  - D027\\n- id: D029\\n  date: 2026-05-13 07:59 UTC\\n  summary: Phase 2 第三方法：放弃 IFR，改用 ACDC top-k。IFR 跨族分歧作为 Discussion finding。\\n  rationale: D028 两项诊断均失败：(1) per-head 分解已在使用，IFR 根本性偏向 MLP/early layers 而 gradient\\n    方法偏向 attention/late layers；(2) proportional binarization 到 3.5%（~6000 edges）才出现\\n    1 条 CSS=1.0 边。IFR×gradient Jaccard 结构性为零，不是调参能解决。ACDC top-k 是唯一已验证的跨族方法（GPT-2\\n    上与 gradient 有合理重叠）。计算成本高（30min-2h vs 1s）但 96GB 卡可承受。不选 AtP 因为与 EAP-IG/EP 同为 gradient\\n    族（K≈2 问题不解决）。IFR×gradient 分歧本身是有价值的 finding，放入论文 Discussion。\\n  related_experiments:\\n  - exp_id: phase2_qwen05b_ioi_k3\\n    role: evidence\\n    result: IFR zero overlap confirmed\\n  depends_on:\\n  - D028\\n- id: D030\\n  date: 2026-05-13 08:01 UTC\\n  summary: SVA D025 gate FAIL（zero FAIL / mean 边际 Δ=0.008）；发现 css_0.67 评估 bug 影响所有历史实验\\n  rationale: SVA GPT-2 K=3 (ACDC top-100) 结果：zero ablation CSS=1.0 CPR=-0.703 < EAP-IG=-0.348（FAIL）；mean\\n    ablation CSS=1.0 CPR=1.180 vs ACDC=1.172（Δ=0.008，噪声范围，无统计意义）。跨任务 pattern 确认：CSS=1.0\\n    faithfulness 优势仅在 IOI+GPT-2 + zero ablation 下成立（1/3 任务）。另发现 css_0.67 评估 bug：css_0.67\\n    实际在评估 css_1.0 的边集（阈值过滤逻辑错误），影响所有历史实验的 css≥0.67 数据。需立即修复后重评。\\n  related_experiments:\\n  - exp_id: mvp_sva_gpt2_k3_topk\\n    role: primary\\n    result: condition④ FAIL (zero) / marginal PASS (mean Δ=0.008)\\n  depends_on:\\n  - D027\\n  - D025\\n- id: D031\\n  date: 2026-05-13 08:04 UTC\\n  summary: 统一 D025 条件④标准：zero PASS 或 mean Δ≥0.01，SVA 两次均判 negative；修正 cqa1 registry\\n  rationale: Reviewer 发现 cqa1 SVA (conclusion=success) 与 westd SVA (conclusion=negative)\\n    对同一 pattern（zero FAIL + mean Δ=0.006）给出矛盾判定。统一标准：条件④要求 (a) zero ablation CSS >\\n    best single-method，或 (b) mean ablation CSS > best single-method 且 Δ ≥ 0.01。Δ=0.006/0.008\\n    在单 seed 单次运行下无统计意义（ACDC 跨硬件差异本身就有这个量级）。两次 SVA 均判 negative。cqa1 registry 需修正 conclusion=negative。\\n  related_experiments:\\n  - exp_id: mvp_sva_gpt2_k3\\n    role: primary\\n    result: corrected to negative\\n  - exp_id: mvp_sva_gpt2_k3_topk\\n    role: reference\\n    result: negative confirmed\\n  depends_on:\\n  - D030\\n  - D025\\n- id: D032\\n  date: 2026-05-13 08:12 UTC\\n  summary: 'D032: 条件④评估指标修正——必须用 css_1.00 而非 css_0.67'\\n  rationale: Reviewer 发现 D025 条件④定义为 \\\"CSS=1.0 > best single-method\\\"，但实际评估代码检查了 css_0.67\\n    的 CPR。这是一个与 css_0.67 filtering bug 相关但独立的问题：即使 css_0.67 的边集计算正确，条件④也应该用 css_1.00\\n    的 CPR。westd SVA 数据：css_1.00 mean CPR=1.1873 vs ACDC=1.1746, Δ=0.0127≥0.01（D031\\n    门槛），可能从 negative 翻转为 marginal PASS。需要 Agent 在 css_0.67 bug 修复后，用 css_1.00 重新跑条件④判定。\\n  related_experiments:\\n  - exp_id: mvp_sva_gpt2_k3_topk\\n    role: re-evaluate\\n    result: westd css_1.00 Δ=0.0127, pending re-evaluation\\n  - exp_id: mvp_sva_gpt2_k3\\n    role: invalidate\\n    result: cqa1 isinf + css_0.67 bug, conclusion unreliable → negative\\n  depends_on:\\n  - D031\\n  - D030\\n  - D025\\n- id: D033\\n  date: 2026-05-13 08:30 UTC\\n  summary: 'D033: SVA 判定降级为 inconclusive——单 seed Δ=0.013 不具鲁棒性'\\n  rationale: D032 将 westd SVA 从 negative 改为 success（css_1.00 Δ=0.0127≥0.01）。但 Reviewer\\n    指出：(1) cqa1 同任务/模型/seed Δ=0.006<0.01 仍为 negative，(2) 两台服务器结论分裂是 ACDC 硬件不确定性导致，(3)\\n    论文不能 cherry-pick 一台的结果。跨服务器平均 Δ=(0.013+0.006)/2=0.0095<0.01。因此 SVA 整体判定为 inconclusive/marginal，不计入\\n    clear success。论文中需如实报告两台结果并注明 marginal。当前真实成绩：IOI clear PASS, SVA inconclusive,\\n    Arithmetic FAIL。\\n  related_experiments:\\n  - exp_id: mvp_sva_gpt2_k3_topk\\n    role: downgrade\\n    result: success → inconclusive (Δ=0.013 not robust)\\n  - exp_id: mvp_sva_gpt2_k3\\n    role: context\\n    result: negative (Δ=0.006, same task different server)\\n  depends_on:\\n  - D032\\n  - D031\\n- id: D034\\n  date: 2026-05-13 08:37 UTC\\n  summary: 'D034: Qwen ACDC 确认 CSS 跨模型 scaling 根本性失败——问题不在方法选择而在模型规模'\\n  rationale: D029 将 IFR 替换为 ACDC top-0.3%，结果与 IFR 版本相同：CSS=1.0=0 边，所有 pairwise Jaccard≈0。关键发现：(1)\\n    ACDC 在 Qwen 上退化为 node-level scoring（与 IFR block-voting 同一问题），(2) 相同 binarization\\n    比例（0.3%），GPT-2(32k边) Jaccard=0.09-0.69 vs Qwen(179k边) Jaccard=0.00-0.04，差一个数量级，(3)\\n    单方法 faithfulness 也极低（EP CPR=0.055）。结论：CSS 跨模型 scaling 失败是结构性的，不可通过换方法修复。当前真实成绩：IOI\\n    GPT-2 明确 PASS，其余全部 FAIL 或 inconclusive。原 paper framing（CSS 作为正向方法贡献）不再可行。\\n  related_experiments:\\n  - exp_id: phase2_qwen05b_ioi_acdc_k3\\n    role: primary\\n    result: CSS=1.0=0 edges, all Jaccard≈0, FAIL\\n  - exp_id: phase2_qwen05b_ioi_k3\\n    role: context\\n    result: IFR version also 0 CSS=1.0 edges\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: contrast\\n    result: GPT-2 IOI PASS, same methods work at 32k scale\\n  depends_on:\\n  - D029\\n  - D025\\n- id: D035\\n  date: 2026-05-13 09:21 UTC\\n  summary: 'D035: Reframe 为分析论文 Route A — \\\"When Does Cross-Method Consensus Fail in\\n    Circuit Discovery?\\\" 目标 EMNLP Findings'\\n  rationale: Dream 三档结果（best 2/6 Reject, median/worst 3/6 Weak Reject）+ 实际实验结果（1/5\\n    PASS，Qwen scaling 根本性失败）共同表明：(1) 正向方法贡献论文不可行——即使 best case 也被 reject，(2) CSS =\\n    feature selection stability index，原框架有致命新颖性问题。Route A 将叙事从\\\"提出 CSS 方法\\\"转为\\\"系统性分析\\n    cross-method consensus 的失败模式\\\"：ACDC binarization pathology（三档一致最强贡献）、component-level\\n    scoring scaling failure、method correlation diagnostics。目标降为 EMNLP Findings。paper_framing.md\\n    和 experiment_plan.yaml 已更新。\\n  related_experiments:\\n  - exp_id: mvp_pilot_gpt2_ioi_v3\\n    role: lone positive\\n    result: CSS PASS, but size confound pending\\n  - exp_id: phase2_qwen05b_ioi_acdc_k3\\n    role: scaling failure\\n    result: zero CSS=1.0 edges, node-level degeneration\\n  - exp_id: mvp_arithmetic_gpt2_k3\\n    role: task-dependent failure\\n    result: high Jaccard → CSS degenerates\\n  depends_on:\\n  - D034\\n  - D033\\n  - D029\\n\", \"total_chars\": 22880, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f0341fd-7067-42f4-a223-010210838744",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "91a5d4a6-3bec-4b86-aca1-6d93624e59c0",
  "sourceToolAssistantUUID": "1f0341fd-7067-42f4-a223-010210838744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T09:56:16.608Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013YBmRuxE1KzetGgmBeDTWz`</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91a5d4a6-3bec-4b86-aca1-6d93624e59c0",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNHytSJ9L9XEHsYnirY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15fc5419-7258-4149-85d4-34e31f2f770f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAJ6MKbrn3vqK7VqM7eros",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3124,
      "cache_read_input_tokens": 30517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3124,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 26 · 2026-05-13T09:56:16.630Z_

<details><summary>↩ Tool result · `toolu_013YBmRuxE1KzetGgmBeDTWz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — structfuse-context\\n\\n> 最后更新: 2026-05-13 | 更新原因: D034 后 reframe 为分析论文（Route A）\\n\\n## Target Venue\\nEMNLP 2026 Findings (ARR deadline 2026-05-25)\\n\\n## Core Insight\\nCross-method binary consensus in circuit discovery fails more often than it succeeds. Through systematic experiments on 4 tasks × 2 models, we identify three distinct failure modes: (1) task structure forces method correlation (high Jaccard → consensus degenerates to single-method), (2) ACDC's isinf binarization creates artificial sparsity that collapses consensus to a single method's output, and (3) component-level scoring granularity on larger models (>100K edges) causes near-zero inter-method overlap regardless of binarization strategy. These findings provide actionable diagnostic guidelines: check pairwise Jaccard before investing in multi-method validation, normalize binarization thresholds across methods, and verify scoring granularity compatibility.\\n\\n## Narrative Arc\\n1. Circuit discovery methods find different circuits — intuition says \\\"consensus = truth,\\\" but is this justified?\\n2. We test this intuition systematically with CSS (binary consensus) across K=3 methods on multiple tasks and models\\n3. CSS succeeds in only 1 of 5+ configurations (IOI on GPT-2) — consensus mostly fails\\n4. We identify three mechanistic failure modes with distinct signatures\\n5. Negative results + failure mode taxonomy = actionable practitioner guidelines\\n\\n## Core Claims\\n\\n### Claim 1: ACDC isinf binarization pathology (METHODOLOGICAL — strongest)\\n- **Evidence**: CSS=1.0 ≡ ACDC under isinf; top-k normalization breaks degeneracy; Jaccard shifts +0.16 to +0.25 across tasks\\n- **Status**: Fully demonstrated on IOI + Arithmetic + SVA (3 tasks)\\n- **Strength**: ★★★★★ — concrete, reproducible, actionable\\n\\n### Claim 2: CSS fails on majority of task×model configurations (EMPIRICAL)\\n- **Evidence**: 1/5+ configurations show CSS=1.0 CPR advantage; failures include task-dependent (Arithmetic, SVA) and model-scaling (Qwen×2)\\n- **Status**: IOI PASS, Arithmetic FAIL, SVA inconclusive (D033), Qwen IFR FAIL, Qwen ACDC FAIL, Factual Recall pending\\n- **Strength**: ★★★★ — honest negative finding with systematic coverage\\n\\n### Claim 3: Component-level scoring causes scaling failure (MECHANISTIC)\\n- **Evidence**: On Qwen-0.5B (179K edges), both IFR and ACDC degenerate to node-level scoring; top-0.3% binarization selects block-structured edge sets; all pairwise Jaccard ≈ 0; zero CSS=1.0 edges\\n- **Status**: Demonstrated with two independent methods (IFR D028, ACDC D034)\\n- **Strength**: ★★★★ — root cause identified, not fixable by method substitution\\n\\n### Claim 4: Jaccard as necessary-condition diagnostic (PRACTICAL)\\n- **Evidence**: max Jaccard > 0.5 → CSS never helps (3/3 cases); max Jaccard < 0.35 → CSS helps (1/1 case, IOI); gap zone 0.35-0.50 inconclusive\\n- **Status**: Directionally supported but n too small for statistical significance. Framed as \\\"motivated conjecture + practical heuristic,\\\" NOT as proven correlation\\n- **Strength**: ★★★ — honest about limitations, still useful as guideline\\n\\n### Claim 5: CIRCUS (within-method threshold diversity) fails completely (COMPARATIVE)\\n- **Evidence**: CIRCUS produces negative CPR on all tested tasks; cross-method consensus is necessary but not sufficient\\n- **Status**: D021 documented 3× failure\\n- **Strength**: ★★★ — negative ablation, depends on implementation correctness caveat\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1: \\\"This is just a negative result, what's the contribution?\\\"\\n- **Response**: Three concrete contributions: (a) binarization pathology + fix, (b) scaling failure root cause (component-level scoring), (c) diagnostic guidelines. Negative results that illuminate *why* something fails are more useful than positive results that don't generalize.\\n\\n### R2: \\\"CSS is just the feature selection stability index (Nogueira & Brown 2016)\\\"\\n- **Response**: Acknowledged explicitly in Related Work. Our contribution is not the mathematical framework but the systematic empirical characterization of when it fails in circuit discovery, plus the domain-specific failure modes (binarization pathology, scoring granularity).\\n\\n### R3: \\\"IOI positive result could be size effect\\\"\\n- **Response**: Size-controlled baseline analysis (pending) directly addresses this. If confirmed as artifact, strengthens the negative finding narrative.\\n\\n### R4: \\\"Only GPT-2 Small + Qwen 0.5B, limited model coverage\\\"\\n- **Response**: Two models at different scales (32K vs 179K edges) already reveal the scaling failure. The root cause (component-level scoring) is architectural, not model-specific.\\n\\n### R5: \\\"EAP-IG and EP are gradient-adjacent, K=3 is effectively K≈2\\\"\\n- **Response**: This is part of our finding, not a limitation — even theoretically diverse methods (IFR, ACDC) fail to provide independent evidence at scale. Method correlation is structural, not accidental.\\n\\n### R6: \\\"No confidence intervals on CPR differences\\\"\\n- **Response**: Must add bootstrap CIs. IOI advantage of +0.08 needs statistical validation.\\n\\n## Competitors\\n- **CIRCUS** (Parekh 2026): Within-method threshold diversity; our negative ablation\\n- **Mondorf et al.** (2510.06811): Cross-method score averaging; must acknowledge continuous averaging may outperform binary consensus\\n- **PIE** (2604.16889): Iterative pruning ensemble; single paradigm\\n- **Nogueira & Brown** (JMLR 2016): Feature selection stability; CSS is domain application, must cite\\n- **Kuncheva & Whitaker** (2003): Ensemble diversity theory; theoretical foundation for our failure mode analysis\\n\", \"total_chars\": 5555, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15fc5419-7258-4149-85d4-34e31f2f770f",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "c4c60e7d-31ba-45de-b348-1121fa66dd0f",
  "sourceToolAssistantUUID": "15fc5419-7258-4149-85d4-34e31f2f770f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T09:56:16.837Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RYNDVpBNf3pR3PAqCnmgGC`</summary>

```json
{
  "project": "structfuse-context",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4c60e7d-31ba-45de-b348-1121fa66dd0f",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNHytSJ9L9XEHsYnirY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd9299a9-30aa-475d-b700-3a9a68b4b209",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAJ6MKbrn3vqK7VqM7eros",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3124,
      "cache_read_input_tokens": 30517,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3124
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 30517,
          "cache_creation_input_tokens": 3124,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3124,
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

_source line 28 · 2026-05-13T09:56:16.856Z_

<details><summary>↩ Tool result · `toolu_01RYNDVpBNf3pR3PAqCnmgGC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/memory.md\", \"content\": \"# Memory — structfuse-context\\n\\n## GPU 越界教训 (2026-05-13)\\n\\n第三次 GPU 越界事件：PID 897752 占用 cuda:0（属于 rl-active-probe-fl），导致对方数据丢失。根因：旧进程或直接运行库模块时未设 CUDA_VISIBLE_DEVICES，torch 默认使用 cuda:0。\\n\\n**硬规则**：\\n- 项目只有 cuda:5@cqa1-21977，所有 .py 文件（含库模块）必须在 import torch 前用 `os.environ.setdefault(\\\"CUDA_VISIBLE_DEVICES\\\", \\\"5\\\")` 防护\\n- 入口脚本用 `os.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"5\\\"`（强制覆盖），库模块用 `setdefault`（不覆盖入口已设的值）\\n- Worker 提交实验必须用 submit_training_job（自动管理 CUDA_VISIBLE_DEVICES），禁止 nohup\\n\\n## ACDC isinf 退化——核心方法论问题 (2026-05-13)\\n\\nACDC binarization 用 `isinf` 只选出极少边（IOI 14, Arithmetic 17），但 ACDC 实际有 0.03-0.09 四级中间分数。isinf 导致 CSS=1.0 与 ACDC 完全重合，跨方法共识退化。top-k binarization（k=50-75）解决此问题：Arithmetic CSS 3/3 从 17→44-54。\\n\\n**但 top-k 未翻转条件④**：CSS=1.0 mean CPR=0.919 < EAP-IG=0.985。\\n\\n## D021: CSS-only 叙事 (2026-05-13)\\n\\n放弃 CIRCUS 作为独立 claim。转 CSS-only 叙事。\\n\\n## 竞争定位：CSS vs CIRCUS (2026-05-13)\\n\\n- **CIRCUS (Parekh, 2026)** 最大竞争对手。CSS 差异化 = method diversity > threshold diversity\\n- **Mondorf et al.** direct competitor：仅 gradient 族、score averaging（非 binary consensus）\\n- 关键支撑：Miller et al. (COLM 2024) faithfulness 对消融敏感；Méloux et al. EAP/EAP-IG 高方差\\n\\n## D026: MVP Gate 最终结论 (2026-05-13)\\n\\n**Arithmetic 条件④ FAIL（CSS=1.0 < EAP-IG），IOI PASS。**\\n\\n关键教训：\\n1. **Zero ablation 是 artifact 源**——所有小电路 zero CPR 为负，mean ablation 翻正到 0.9+\\n2. **节点级 ablation 的局限**——CSS=1.0 CPR 在 k=50→75 不变（节点集相同，边数变化无法区分）\\n3. **EAP-IG×EP 在 arithmetic 上 Jaccard=0.695**——两方法高度一致，CSS 缺少第三方视角的信息增益\\n4. **IOI 上 CSS 边效率极高**——14 edges CPR≈50 edges 单方法，每条边贡献远超单方法\\n5. **IOI CPR 不一致是误报**——mean_ablation_results.json 中标注为 IOI 的数据实际是 Arithmetic\\n\\n**等待 Director 决策：edge-efficiency claim / 原 claim + 更多任务 / pivot。**\\n\\n## IFR 作为第三方法——已证伪 (2026-05-13)\\n\\n**phase2_qwen05b_ioi_k3 (negative)**: Qwen-2.5 0.5B 上 IFR 与 EAP-IG/EP 的 Jaccard = 0.00。\\n\\n**D028 诊断结论**:\\n1. **Per-head 分解无效**: IFR 已经在用 per-head 分解，不是修复方向\\n2. **根本原因**: IFR (proximity) 度量 activation magnitude → 偏向高幅度 MLP 输出 (m2, m20, m22)；gradient 方法度量 causal influence → 偏向任务关键 attention heads (a20.h9)。两者解构的是不同维度\\n3. **Jaccard sweep**: 首次非零在 N=500 (J=0.045)，unique_score_rank 展开到 2191 边也仅 J=0.065\\n4. **Destination-side 退化 100%**: 同层头共享 residual stream，所有头得到相同 destination score\\n\\n**结论**: IFR 不能作为 CSS 第三方法用于大模型。gradient 族内部仍有共识（EAP-IG×EP Jaccard=0.54）。Phase 2 需要替代第三方法（ACDC top-k 或另一个 gradient 方法）。\\n\", \"total_chars\": 2263, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd9299a9-30aa-475d-b700-3a9a68b4b209",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "bb43bfea-6824-45d9-bd8b-c121ca213fa5",
  "sourceToolAssistantUUID": "cd9299a9-30aa-475d-b700-3a9a68b4b209",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-13T09:56:19.882Z_

Now let me look at the experimental artifacts and any review context files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb43bfea-6824-45d9-bd8b-c121ca213fa5",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNJHuQCdD96K27VdcEe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f578daf-126b-4a1a-9fc4-6febf6aa2d4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwaHWt32ePM26Gc9A7cSR3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16747,
      "cache_read_input_tokens": 33641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16747,
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

_source line 30 · 2026-05-13T09:56:21.850Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01N94FwzNmKTxy8y74uTiyFi`</summary>

```json
{
  "pattern": "**/review_context.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f578daf-126b-4a1a-9fc4-6febf6aa2d4d",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNJHuQCdD96K27VdcEe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d36b92a1-d9ad-4ebc-a625-88500f3efcb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwaHWt32ePM26Gc9A7cSR3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16747,
      "cache_read_input_tokens": 33641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16747,
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

_source line 31 · 2026-05-13T09:56:21.868Z_

<details><summary>↩ Tool result · `toolu_01N94FwzNmKTxy8y74uTiyFi`</summary>

```text
artifacts/dream_reports/dream_20260513T054654/best/review_context.yaml
artifacts/dream_reports/dream_20260513T054654/median/review_context.yaml
artifacts/dream_reports/dream_20260513T054654/worst/review_context.yaml
artifacts/dream_reports/dream_20260513T081242/best/review_context.yaml
artifacts/dream_reports/dream_20260513T081242/worst/review_context.yaml
artifacts/dream_reports/dream_20260513T092135/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d36b92a1-d9ad-4ebc-a625-88500f3efcb6",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "88129870-441a-4a51-b8a0-0a3eedd5cad4",
  "sourceToolAssistantUUID": "d36b92a1-d9ad-4ebc-a625-88500f3efcb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-13T09:56:23.301Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014y1TH2ni1kqRDJDxqZvoBV`</summary>

```json
{
  "pattern": "**/experiment_plan*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88129870-441a-4a51-b8a0-0a3eedd5cad4",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNJHuQCdD96K27VdcEe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90525713-0a80-4e41-bf0e-9fb69e8478ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwaHWt32ePM26Gc9A7cSR3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16747,
      "cache_read_input_tokens": 33641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16747,
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

_source line 33 · 2026-05-13T09:56:23.316Z_

<details><summary>↩ Tool result · `toolu_014y1TH2ni1kqRDJDxqZvoBV`</summary>

```text
experiment_plan.lock
experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90525713-0a80-4e41-bf0e-9fb69e8478ee",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "824195a6-04fa-41f3-9a04-0193a164d4ff",
  "sourceToolAssistantUUID": "90525713-0a80-4e41-bf0e-9fb69e8478ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-13T09:56:23.929Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DTEZThiTC7dLTWxPqv5uJm`</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "824195a6-04fa-41f3-9a04-0193a164d4ff",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNJHuQCdD96K27VdcEe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0d1faa8-c0de-4b06-820f-b59109195078",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AwaHWt32ePM26Gc9A7cSR3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16747,
      "cache_read_input_tokens": 33641,
      "output_tokens": 291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16747
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 291,
          "cache_read_input_tokens": 33641,
          "cache_creation_input_tokens": 16747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16747,
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

_source line 35 · 2026-05-13T09:56:23.942Z_

<details><summary>↩ Tool result · `toolu_01DTEZThiTC7dLTWxPqv5uJm`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0d1faa8-c0de-4b06-820f-b59109195078",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "f56c5bd7-4a07-4958-9b83-3388224edc79",
  "sourceToolAssistantUUID": "a0d1faa8-c0de-4b06-820f-b59109195078",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-13T09:56:27.338Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A1fCJzhkNMbXLmdh2nsY9j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T092135/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f56c5bd7-4a07-4958-9b83-3388224edc79",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNJpGX6uy2ftE1aNGGo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33f1249d-5ad0-440e-8185-a21f7b21a667",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012hVCJzwRdsFDREdAw6zuY3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 50388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 582,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 37 · 2026-05-13T09:56:27.345Z_

<details><summary>↩ Tool result · `toolu_01A1fCJzhkNMbXLmdh2nsY9j`</summary>

```text
1	narrative_guidance: 'Route A framing 完全成立。Factual Recall v2 产出清晰 FAIL（CSS-1.0 mean
2	  CPR=0.905 < EAP-IG=0.975，Δ=-0.070）， 提供第5个 FAIL 数据点，使总配置达 1 PASS / 5 FAIL（6 configs）。Size-controlled
3	  baseline 证实 IOI CSS 优势 76%归因于 selection quality 而非 edge count（top-7 EAP-IG CPR=0.048
4	  vs CSS=1.0 CPR=0.109）。Bootstrap CIs 确认 IOI Δ=0.085 显著（95% CI [0.035, 0.138]，p=0.002），SVA
5	  CI 跨零（[-0.025, 0.052]）验证其 FAIL 归类。 Ablation comparison 排除 zero-ablation artifact（IOI
6	  mean ablation Δ=0.065 仍为正）。Jaccard diagnostic 在全部 6 configs 上 5/6 正确（唯一失误是 Qwen
7	  ACDC 的 component-level scoring failure，属 Claim 3 而非 Claim 4 范畴）。 Claims 1-4 全部保留原始强度，Claim
8	  4 从 ''motivated conjecture'' 升级为 ''empirically supported heuristic''。 论文标题不变，投 Findings
9	  绰绰有余。
10	
11	  '
12	imagined_experiments:
13	- name: GPT-2 Factual Recall K=3 CSS (v2)
14	  plan_id: plan_004
15	  description: 'GPT-2 Small 上运行 country→capital factual recall（如 "The capital of France
16	    is" → "Paris"）。 K=3 方法（EAP-IG + EP + ACDC），top-50 binarization。MLP-based knowledge
17	    retrieval circuit 导致方法在 MLP bottleneck edges 上高度收敛，预期 max Jaccard > 0.5，CSS FAIL。
18	
19	    '
20	  expected_results:
21	    binarization: top-50
22	    edge_counts:
23	      eap_ig: 50
24	      ep: 50
25	      acdc: 50
26	    pairwise_jaccard:
27	      eapig_x_ep: 0.62
28	      acdc_x_eapig: 0.38
29	      acdc_x_ep: 0.33
30	    max_pairwise_jaccard: 0.62
31	    three_way_jaccard: 0.205
32	    css_distribution:
33	      '0.33': 74
34	      '0.67': 30
35	      '1.00': 10
36	    evaluation_mean:
37	      css_1.00:
38	        edges: 10
39	        CPR: 0.905
40	        CMD: 0.418
41	      css_0.67:
42	        edges: 40
43	        CPR: 0.932
44	        CMD: 0.385
45	      eap_ig:
46	        edges: 50
47	        CPR: 0.975
48	        CMD: 0.112
49	      ep:
50	        edges: 50
51	        CPR: 0.952
52	        CMD: 0.214
53	      acdc:
54	        edges: 50
55	        CPR: 0.938
56	        CMD: 0.278
57	    evaluation_zero:
58	      css_1.00:
59	        edges: 10
60	        CPR: -0.032
61	        CMD: 1.045
62	      eap_ig:
63	        edges: 50
64	        CPR: -0.085
65	        CMD: 1.198
66	      acdc:
67	        edges: 50
68	        CPR: -0.112
69	        CMD: 1.247
70	    d025_conditions:
71	      cond1_jaccard_lt070: PASS (0.62)
72	      cond2_css_ge23_ge10: PASS (30)
73	      cond3_css_10_ge3: PASS (10)
74	      cond4_cpr_dominance: 'FAIL (mean: css_1.00=0.905 < EAP-IG=0.975, Δ=-0.070)'
75	    factual_recall_css_vs_best_single_delta: -0.07
76	    jaccard_diagnostic_prediction: '>0.5 → FAIL'
77	    jaccard_diagnostic_correct: true
78	  result_rationale: 'Factual recall 依赖 MLP layer 5-9 的 key-value 知识存储机制（Meng et al.
79	    2022）和多层 attention head 的 subject→last-token routing。三种方法在 MLP 存储层的边上被迫高度共识——这些边是知识检索的
80	    不可替代瓶颈，无论用梯度、剪枝还是 activation patching 评估都会被选中。EAP-IG×EP Jaccard=0.62： 两种 gradient-adjacent
81	    方法在 MLP bottleneck edges 上几乎完全一致，分歧仅在 attention routing 边的 排序上。ACDC×gradient Jaccard
82	    较低（0.38/0.33）因为 ACDC 的 clean→corrupt substitution 在 routing edges 上给出不同排序，但仍然收敛于相同的
83	    MLP 核心。css_1.00 的 10 条边几乎全部是 MLP 存储层的 bottleneck edges——它们是三种算法视角的交集，但恰恰是最 obvious
84	    的边。这些边的 mean CPR=0.905 低于 EAP-IG 的 0.975， 因为 EAP-IG 的 50 条边额外捕获了 attention routing
85	    edges 中的 high-gradient 子集，这些 routing edges 虽然方法间不一致，但 EAP-IG 选中的那部分确实是 functionally
86	    important 的。CSS consensus 过滤掉了 这些 method-specific 但 functionally relevant 的 routing
87	    edges，导致 faithfulness 下降。 这与 Arithmetic 的失败模式一致：当任务的关键计算集中在少数 bottleneck 层时，方法收敛使
88	    consensus 退化为 obvious-edge selection，不优于最佳单方法。
89	
90	    '
91	  tables:
92	  - name: 'Table: Factual Recall Circuit Discovery Summary'
93	    description: '行: EAP-IG, EP, ACDC, CSS≥2/3, CSS=1.0 列: Edges, Mean CPR, Mean CMD,
94	      Δ(vs best single) CSS=1.0 的 10 edges mean CPR=0.905 < EAP-IG 50 edges CPR=0.975，Δ=-0.070
95	
96	      '
97	  - name: 'Table: Factual Recall Pairwise Jaccard Matrix'
98	    description: '3×3 对称矩阵：EAP-IG×EP=0.62, ACDC×EAP-IG=0.38, ACDC×EP=0.33。 与 Arithmetic
99	      (max_J=0.695) 并列，展示 MLP-heavy tasks 的方法收敛模式
100	
101	      '
102	  figures_description:
103	  - '加入 cross-task CPR bar chart 作为第四个 subplot。CSS=1.0 bar (0.905) 明显低于 EAP-IG bar
104	    (0.975)， 与 Arithmetic 类似的 FAIL pattern。视觉化 MLP-bottleneck task 上 consensus 失败。
105	
106	    '
107	  analysis: 'Factual Recall FAIL 使 pass/fail ratio 从 1/4 变为 1/5，进一步巩固 "consensus fails
108	    more often than it succeeds" 的核心叙事。max_J=0.62 落在 Arithmetic(0.695) 和 SVA(0.653)
109	    之间， Δ=-0.070 与 Arithmetic 的 Δ=-0.066 量级一致——两个 MLP-bottleneck 任务的平行失败 构成 failure
110	    mode 1（task structure forces method correlation）的强化证据。 对 Claim 4 的贡献：第6个数据点落在
111	    Jaccard > 0.5 区域且 FAIL， 使 >0.5 区域 FAIL rate 从 3/4 变为 4/5（排除 SVA 的 marginal case
112	    则为 3/3→4/4）， diagnostic accuracy 继续成立。
113	
114	    '
115	- name: IOI Size-Controlled Baseline
116	  plan_id: plan_008
117	  description: 'IOI 上控制 edge count：将 CSS=1.0（7 edges）与 top-7 of EAP-IG、top-7 of EP、top-7
118	    of ACDC、 random-7 edges 在相同 edge 数量下比较 zero ablation CPR。排除 "CSS 优势仅因 fewer edges"
119	    的 size confound。
120	
121	    '
122	  expected_results:
123	    css_1.00:
124	      edges: 7
125	      CPR_zero: 0.109
126	    top7_eapig:
127	      edges: 7
128	      CPR_zero: 0.048
129	    top7_acdc:
130	      edges: 7
131	      CPR_zero: 0.042
132	    top7_ep:
133	      edges: 7
134	      CPR_zero: 0.035
135	    random7:
136	      edges: 7
137	      CPR_zero: 0.003
138	      CPR_zero_std: 0.012
139	      n_random_samples: 50
140	    original_best_single_cpr: 0.029
141	    original_delta: 0.08
142	    size_controlled_delta: 0.061
143	    size_controlled_advantage_retained_pct: 76.3
144	    css_beats_all_top7: true
145	    css_beats_random_p_value: <0.001
146	  result_rationale: 'CSS=1.0 的 7 条边是 EAP-IG、EP、ACDC 三种独立算法视角的交集——它们对应 IOI circuit
147	    中 name mover heads（9.9, 9.6, 10.0）和 S-inhibition heads（7.3, 8.6）的关键 attention
148	    edges， 加上 1-2 条必要的 MLP routing edges。这些边被三种完全不同的评分机制（gradient×activation product、
149	    pruning sensitivity、clean→corrupt activation difference）共同认定为最重要， 构成了 IOI circuit
150	    的 "triple-verified functional core"。 相比之下，top-7 of EAP-IG（CPR=0.048）包含一些 gradient
151	    signal 强但功能贡献弱的边 （如 early-layer position embedding edges，gradient 高但 ablation
152	    后可被其他路径补偿）。 Top-7 of EP（CPR=0.035）包含 pruning-sensitive 但非 functionally-critical
153	    的边 （如 LayerNorm→attention edges，移除后 attention pattern 改变但不影响 name-moving 功能）。
154	    Top-7 of ACDC（CPR=0.042）质量略好于 EP（ACDC 的 activation patching 更直接衡量功能贡献）， 但仍包含 2-3
155	    条 ACDC-specific 的 false positives（其他方法未选中的边）。 Random-7 CPR≈0.003（50 次采样均值），确认
156	    7 条随机边几乎无功能意义。 Size-controlled advantage retained = (0.109-0.048)/0.080 = 76.3%：
157	    原始 CSS 优势的四分之三归因于 selection quality（consensus 过滤 method-specific noise）， 仅四分之一可能与
158	    size effect 相关。这直接回应 R3 的 size artifact 质疑。
159	
160	    '
161	  tables:
162	  - name: 'Table: Size-Controlled Baseline Comparison (IOI)'
163	    description: '行: CSS=1.0, Top-7 EAP-IG, Top-7 ACDC, Top-7 EP, Random-7 (mean±std,
164	      n=50) 列: Edges, Zero CPR, CMD, vs CSS Δ 底部: Advantage retained = 76.3%
165	
166	      '
167	  - name: 'Table: Edge Identity Analysis'
168	    description: 'CSS=1.0 的 7 条边与各 top-7 的 overlap 分析。 CSS∩EAP-IG_top7: 5/7, CSS∩ACDC_top7:
169	      4/7, CSS∩EP_top7: 4/7。 CSS-unique edges（仅 consensus 选中）: 0-1 条。证明 CSS 的优势不在于发现
170	      unique edges， 而在于从多个 top-ranked lists 的交集中过滤出 most reliable edges。
171	
172	      '
173	  figures_description:
174	  - 'Bar chart: x=method (CSS=1.0, EAP-IG top-7, ACDC top-7, EP top-7, Random-7),
175	    y=zero CPR。所有 bar 相同 edge count (N=7)。CSS=1.0 bar 显著高于其他。 Error bar on Random-7
176	    (±std from 50 samples)。灰色虚线 y=0。 右侧标注 "76% of advantage from selection quality"。
177	
178	    '
179	  analysis: 'Size-controlled baseline 排除了最直接的 confound。76.3% retained advantage 意味着：
180	    即使控制 edge count，consensus 选出的 7 条边仍显著优于任何单方法选出的 7 条边。 剩余 23.7% 的 "size effect"
181	    可能来自 original comparison 中 single methods 使用 100 edges 而 CSS 仅 7 edges——更多边意味着更多
182	    collateral damage under zero ablation。 这为 Claim 2 提供了 decisive control experiment：IOI
183	    的 CSS 成功是真正的 selection quality 效应，不是 size artifact。
184	
185	    '
186	- name: Bootstrap Confidence Intervals on CPR
187	  plan_id: plan_009
188	  description: '对所有完成实验的 CPR Δ（CSS=1.0 vs best single method）进行 paired bootstrap（B=10000），
189	    报告 95% BCa CIs。重点验证 IOI Δ 显著性（CI 不跨零）和 SVA 非显著性（CI 跨零 → 确认 FAIL 归类）。
190	
191	    '
192	  expected_results:
193	    ioi_gpt2:
194	      delta_point: 0.085
195	      delta_ci_95:
196	      - 0.035
197	      - 0.138
198	      p_value: 0.002
199	      n_eval_examples: 100
200	      bootstrap_samples: 10000
201	      significant: true
202	      note: paired bootstrap on per-example CPR differences; BCa correction for skewness
203	    arithmetic_gpt2:
204	      delta_point: -0.063
205	      delta_ci_95:
206	      - -0.112
207	      - -0.018
208	      p_value: 0.008
209	      significant: true
210	      direction: CSS significantly WORSE than EAP-IG
211	    sva_gpt2:
212	      delta_point: 0.013
213	      delta_ci_95:
214	      - -0.025
215	      - 0.052
216	      p_value: 0.482
217	      significant: false
218	      note: CI crosses zero, confirms SVA as FAIL (advantage not statistically significant)
219	    factual_recall_gpt2:
220	      delta_point: -0.068
221	      delta_ci_95:
222	      - -0.118
223	      - -0.022
224	      p_value: 0.005
225	      significant: true
226	      direction: CSS significantly WORSE than EAP-IG
227	    qwen_ifr:
228	      note: N/A — zero CSS=1.0 edges, bootstrap not applicable
229	    qwen_acdc:
230	      note: N/A — zero CSS=1.0 edges, bootstrap not applicable
231	    summary:
232	      significant_pass: 1
233	      significant_fail: 2
234	      non_significant: 1
235	      not_applicable: 2
236	  result_rationale: 'Paired bootstrap 是这些小样本 CPR 比较的最合适统计方法：每个评估示例同时计算 CSS 和 single-method
237	    CPR， 差值的 bootstrap 分布直接反映 CSS 优势的不确定性。BCa（bias-corrected and accelerated）修正 处理
238	    CPR 分布的偏斜（zero ablation CPR 常右偏）。 IOI Δ=0.085 (CI [0.035, 0.138])：100 个 IOI 评估示例中，CSS=1.0
239	    在大多数示例上优于 ACDC， per-example Δ 的标准差约 0.025，除以 sqrt(100)≈10 给出 SE≈0.025，95% CI 宽度约
240	    0.10。 CI 下界 0.035 > 0，p=0.002，IOI PASS 的统计显著性确认。 Arithmetic Δ=-0.063 (CI [-0.112,
241	    -0.018])：CI 完全在负区域，CSS 显著不如 EAP-IG， 确认 FAIL 结论。per-example 差异的方差较大（Arithmetic
242	    各示例的 difficulty 差异更大），CI 略宽。 SVA Δ=0.013 (CI [-0.025, 0.052])：CI 跨零，p=0.482，advantage
243	    统计不显著。 这是 best tier 的关键结果——SVA 从 "inconclusive" 正式归类为 FAIL（优势不显著 = 不支持 CSS 有效）。
244	    Factual Recall Δ=-0.068 (CI [-0.118, -0.022])：与 Arithmetic 模式一致的显著 FAIL。 两个 Qwen
245	    实验因 CSS=1.0=0 edges 无法计算 bootstrap（不是缺陷，而是反映 Claim 3 的 method degeneration）。
246	
247	    '
248	  tables:
249	  - name: 'Table: Bootstrap CI Summary (All Configurations)'
250	    description: '行: IOI, Arithmetic, SVA, Factual Recall, Qwen IFR (N/A), Qwen ACDC
251	      (N/A) 列: Δ Point, 95% CI Lower, 95% CI Upper, p-value, Verdict IOI 行高亮（唯一 CI
252	      完全正的配置）
253	
254	      '
255	  - name: 'Table: IOI Per-Example CPR Distribution'
256	    description: 'Histogram data: CSS=1.0 per-example CPR vs ACDC per-example CPR。
257	      展示 paired difference 分布的形状（轻微右偏，中位数 > 0）
258	
259	      '
260	  figures_description:
261	  - 'Forest plot: 每个 configuration 一行，点估计 + 95% CI 横线。 垂直虚线 x=0。IOI 的 CI 完全在正区域（蓝色），Arithmetic
262	    和 Factual Recall 完全在负区域（红色）， SVA 跨零（灰色）。Qwen 两行标注 "N/A"。 右侧标注 p-value。视觉化一目了然：IOI
263	    是唯一统计显著的 PASS。
264	
265	    '
266	  analysis: 'Bootstrap CIs 将整个实验体系的统计严谨性提升到 Findings 要求。 核心发现：IOI 是唯一 CI 不跨零的正向结果（p=0.002），
267	    SVA 的 CI 跨零（p=0.482）彻底消除了 D033 cross-server 分析的歧义—— SVA 不是 "inconclusive"，而是 "statistically
268	    confirmed FAIL"。 这使 pass/fail classification 完全由统计检验驱动，不依赖 ad hoc thresholds。
269	    直接回应 R6（"No confidence intervals on CPR differences"）。
270	
271	    '
272	- name: Ablation Method Comparison (Zero vs Mean) on IOI
273	  plan_id: plan_011
274	  description: '在 IOI 上比较 zero ablation 和 mean ablation 下 CSS=1.0 的 CPR advantage。
275	    排除 "IOI CSS 优势仅在 zero ablation 下成立" 的 evaluation artifact 质疑。
276	
277	    '
278	  expected_results:
279	    ioi_zero:
280	      css_1.00_CPR: 0.109
281	      best_single_CPR: 0.029
282	      delta: 0.08
283	      best_single_method: ACDC (14 edges)
284	    ioi_mean:
285	      css_1.00_CPR: 0.182
286	      best_single_CPR: 0.117
287	      delta: 0.065
288	      best_single_method: ACDC (14 edges)
289	      eapig_CPR: 0.078
290	      ep_CPR: 0.052
291	    advantage_ratio_mean_vs_zero: 0.813
292	    advantage_positive_both: true
293	    conclusion: CSS advantage robust across ablation methods
294	  result_rationale: 'Zero ablation 将 complement edges 的 activation 设为零，mean ablation
295	    替换为 training-set 均值。 Mean ablation 更 "温和"——保留了残余信号的均值统计特征，因此所有 CPR 值上升（CSS=1.0
296	    从 0.109→0.182， ACDC 从 0.029→0.117）。关键是 relative advantage 是否保持。 CSS=1.0 的 7 条边在
297	    mean ablation 下 CPR=0.182：这些边对应 IOI 的 functional core （name mover + S-inhibition
298	    heads），即使 complement 用均值替代（而非零化）， 这些核心边仍然承载着 IOI task 的主要 logit difference。ACDC
299	    的 14 条边在 mean ablation 下 CPR=0.117：ACDC isinf edges 质量不错但包含 7 条 non-consensus
300	    edges， 其中 2-3 条在 mean ablation 下被证明是 "zero-ablation-sensitive but functionally
301	    replaceable" ——它们在 zero ablation 下似乎重要（移除导致大破坏），但 mean ablation 表明 其功能可被残余均值信号部分补偿。
302	    Δ 从 0.080（zero）降至 0.065（mean），retained ratio = 81.3%。 CSS advantage 在两种 ablation
303	    下均为正，确认 IOI CSS PASS 不是 evaluation artifact。 这直接回应 Dream worst-tier 的核心 concern（zero
304	    ablation bias as IOI confound）。
305	
306	    '
307	  tables:
308	  - name: 'Table: IOI Ablation Method Robustness'
309	    description: '行: Zero Ablation, Mean Ablation 列: CSS=1.0 CPR, ACDC CPR, EAP-IG
310	      CPR, EP CPR, Δ(CSS vs best single) 底部: Advantage retained under mean = 81.3%
311	
312	      '
313	  figures_description:
314	  - 'Grouped bar chart: 两组 (Zero, Mean)，每组 4 bars (CSS=1.0, ACDC, EAP-IG, EP)。 CSS=1.0
315	    bar 在两组中均最高。标注 Δ 值。视觉化 CSS advantage 的 ablation-robustness。
316	
317	    '
318	  analysis: '此实验为 Appendix 提供关键 robustness check。Zero vs mean 给出 Δ=0.080 vs 0.065，
319	    CSS advantage 在两种 evaluation 下一致为正。这排除了 "CSS 仅在 destructive zero ablation 下 人为获胜"
320	    的假说，也为 future work 推荐 mean ablation 作为更温和的默认评估方式。 与 SVA 形成对比：SVA 的 CSS advantage
321	    在 zero ablation 下为负（已知）， mean ablation 下仅 Δ=0.013（non-significant by bootstrap）——
322	    进一步证实 IOI 和 SVA 的 CSS outcome 差异是 task-driven 而非 evaluation-driven。
323	
324	    '
325	- name: IFR vs ACDC vs Gradient Method Divergence Analysis
326	  plan_id: plan_012
327	  description: '系统文档化 Qwen-0.5B 上 IFR 和 ACDC 的退化机制，作为 Claim 3（component-level scoring
328	    scaling failure） 的 case study。纯分析，使用 plan_006/plan_007 已有数据，0 GPU hours。
329	
330	    '
331	  expected_results:
332	    ifr_failure_analysis:
333	      scoring_mechanism: intermediate representation cosine similarity
334	      failure_mode: GQA 的 KV sharing 使 deep-layer attention edge 的 representation
335	        变化被同组 heads 吸收
336	      selected_layer_range: layers 0-5 (early MLP→Attn routing)
337	      gradient_layer_range: layers 18-23 (deep attention heads)
338	      overlap_with_gradient: 0.0
339	      diagnosis: IFR 退化为 early-layer MLP bias detector
340	    acdc_failure_analysis:
341	      scoring_mechanism: activation patching (clean→corrupt substitution)
342	      failure_mode: 179K edges 上 node-level scoring，top-0.3% 选出 block-structured edge
343	        sets
344	      max_jaccard_with_gradient: 0.043
345	      css_3of3: 0
346	      diagnosis: ACDC 也退化为 component-level scoring，与 gradient 方法零重叠
347	    comparative:
348	      ifr_jaccard_eapig: 0.0
349	      ifr_jaccard_ep: 0.0
350	      acdc_jaccard_eapig: 0.022
351	      acdc_jaccard_ep: 0.021
352	      conclusion: 两种非 gradient 方法均因不同机制退化到 component-level，使 CSS consensus 不可能成立
353	    root_cause: 'Component-level scoring 是 architectural 问题而非 method-specific 缺陷：
354	      (1) IFR 因 GQA KV sharing 丢失 edge-level sensitivity (2) ACDC 因 179K 边的搜索空间过大退化为
355	      node-level pruning (3) Gradient 方法（EAP-IG/EP）保持 edge-level scoring 但计算成本高 三种
356	      failure 机制独立，不可通过 method substitution 修复
357	
358	      '
359	  result_rationale: '此分析整合 plan_006 (IFR, D028) 和 plan_007 (ACDC, D034) 的已有数据。 IFR
360	    的失败有明确的 architectural root cause：Qwen-2.5 使用 Grouped Query Attention (GQA)， 同组
361	    heads 共享 K/V projection。当移除一条 attention edge 时，同组其他 heads 的 KV buffer 吸收了 representation
362	    变化，IFR 的 cosine similarity 评分趋近于零。IFR 因此只选中 early-layer MLP edges（representation
363	    影响大但位于 IOI circuit 之外）。 ACDC 在 GPT-2 (32K edges) 上正常工作（isinf 给出 14 条 edge-level
364	    edges）， 但在 Qwen (179K edges) 上搜索空间过大，ACDC 的 greedy pruning 退化为 node-level 操作——
365	    每步评估整个 attention head 而非单条边，因为逐边评估 179K 边的时间成本不可接受。 结果：ACDC 选出的 edges 呈 block
366	    structure（同一 head 的所有边同时被选中或同时排除）， 与 gradient 方法的 fine-grained edge selection
367	    零重叠。 两种非 gradient 方法因完全不同的机制退化到 component-level， 使三方法 consensus 在 Qwen 上不可能成立——这是
368	    Claim 3 的 definitive evidence。
369	
370	    '
371	  tables:
372	  - name: 'Table: Method Scoring Granularity Comparison (Qwen-0.5B IOI)'
373	    description: '行: IFR, ACDC, EAP-IG, EP 列: Scoring Mechanism, Effective Granularity
374	      (edge/node/layer), Selected Layer Range, Jaccard with EAP-IG, Jaccard with EP,
375	      CPR
376	
377	      '
378	  - name: 'Table: GPT-2 vs Qwen Method Behavior'
379	    description: '行: GPT-2 Small (32K edges), Qwen-0.5B (179K edges) 列: ACDC Granularity,
380	      ACDC Edges (isinf), IFR Available, Max Pairwise Jaccard, CSS=1.0 Edges 展示 scale-dependent
381	      method degeneration
382	
383	      '
384	  figures_description:
385	  - 'Layer distribution histogram（三面板）: x=layer (0-23), y=selected edge count。 Panel
386	    1: IFR (红, 集中在 layer 0-5)。 Panel 2: Gradient methods (蓝, layer 18-23)。 Panel 3:
387	    ACDC (绿, block-structured, 集中在 3-4 个 attention heads 的全部边)。 视觉化三种方法在 Qwen 上的退化模式差异。
388	
389	    '
390	  analysis: '此 case study 为 Discussion 提供 Claim 3 的 mechanistic 证据。 核心 insight：CSS
391	    的前提是"每种方法独立地在 edge-level 提供有效评分"。 当方法退化到 component-level（IFR→layer, ACDC→node），
392	    edge-level consensus 的数学基础不成立（三种方法选出的 "edges" 实际上是不同层级的 components， 无法在边级别求交集）。
393	    这为 practitioner guidelines 增加第三条：使用 CSS 前， 验证每种方法的 scoring granularity 是否为 true
394	    edge-level。 如果 ACDC 的选边呈 block structure 或 IFR 的选边集中在窄层范围， 说明该方法已退化，应排除后再计算 consensus。
395	
396	    '
397	- name: Jaccard-CSS Diagnostic Scatter Plot + Correlation
398	  plan_id: plan_013
399	  description: '汇总全部 6 个 model×task 配置的 (max pairwise Jaccard, CSS CPR advantage)，
400	    计算 Spearman rank correlation，验证 Jaccard diagnostic（<0.35→PASS, >0.5→FAIL）的准确率。
401	    明确报告为 n=6 underpowered 但 directionally consistent。
402	
403	    '
404	  expected_results:
405	    data_points:
406	    - label: IOI (GPT-2)
407	      model: GPT-2 Small
408	      max_jaccard: 0.307
409	      css_cpr_advantage: 0.085
410	      css_pass: true
411	      diagnostic_prediction: PASS (< 0.35)
412	      diagnostic_correct: true
413	    - label: Qwen IOI (IFR)
414	      model: Qwen-0.5B
415	      max_jaccard: 0.54
416	      css_cpr_advantage: 0.0
417	      css_pass: false
418	      diagnostic_prediction: FAIL (> 0.5)
419	      diagnostic_correct: true
420	      note: IFR degeneration → all CPR≈0, CSS=1.0=0 edges
421	    - label: Factual Recall (GPT-2)
422	      model: GPT-2 Small
423	      max_jaccard: 0.62
424	      css_cpr_advantage: -0.07
425	      css_pass: false
426	      diagnostic_prediction: FAIL (> 0.5)
427	      diagnostic_correct: true
428	    - label: SVA (GPT-2)
429	      model: GPT-2 Small
430	      max_jaccard: 0.653
431	      css_cpr_advantage: 0.013
432	      css_pass: false
433	      diagnostic_prediction: FAIL (> 0.5)
434	      diagnostic_correct: true
435	      note: Bootstrap CI crosses zero → reclassified as FAIL
436	    - label: Arithmetic (GPT-2)
437	      model: GPT-2 Small
438	      max_jaccard: 0.695
439	      css_cpr_advantage: -0.063
440	      css_pass: false
441	      diagnostic_prediction: FAIL (> 0.5)
442	      diagnostic_correct: true
443	    - label: Qwen IOI (ACDC)
444	      model: Qwen-0.5B
445	      max_jaccard: 0.043
446	      css_cpr_advantage: -0.055
447	      css_pass: false
448	      diagnostic_prediction: PASS (< 0.35)
449	      diagnostic_correct: false
450	      note: Outlier — fails due to component-level scoring (Claim 3), not method correlation
451	        (Claim 4)
452	    n_data_points: 6
453	    diagnostic_accuracy: 5/6 (83.3%)
454	    diagnostic_miss_explanation: 'Qwen ACDC (max_J=0.043, FAIL) is the sole exception:
455	      low Jaccard coexists with FAIL because the failure mode is component-level scoring
456	      degeneration (Claim 3), not method correlation (Claim 4). The diagnostic correctly
457	      predicts when methods function at edge-level; it cannot predict method-degeneration
458	      failures.
459	
460	      '
461	    spearman_rho_all_6: -0.714
462	    spearman_p_all_6: 0.111
463	    spearman_rho_excluding_outlier: -0.9
464	    spearman_p_excluding_outlier: 0.037
465	    gpt2_only_4_points:
466	      spearman_rho: -1.0
467	      spearman_p: 0.042
468	      note: Perfect negative rank correlation on 4 GPT-2 tasks
469	    fitted_threshold_jaccard: 0.5
470	    threshold_interpretation: 'max pairwise Jaccard < 0.35 → CSS likely beneficial
471	      (1/1 correct). max pairwise Jaccard > 0.50 → CSS likely ineffective (4/4 correct,
472	      excluding scaling failures). Gap zone 0.35-0.50: no data points in this range,
473	      recommendation is to proceed with caution.
474	
475	      '
476	  result_rationale: '6 个配置横跨 2 个模型架构（GPT-2, Qwen）、4 个任务（IOI, Arithmetic, SVA, Factual
477	    Recall）。 在排除 Qwen ACDC outlier 后，5 个数据点的 Spearman ρ=-0.900 (p=0.037) 表明 max pairwise
478	    Jaccard 与 CSS advantage 之间存在统计显著的负相关—— method diversity 越高（Jaccard 越低），CSS consensus
479	    的 CPR advantage 越大。 包含 outlier 时 ρ=-0.714 (p=0.111)，不显著—— 因为 Qwen ACDC 的低 Jaccard
480	    + FAIL 组合严重违反了线性趋势。 但这不是 diagnostic 的缺陷，而是反映了两种独立的 failure mode： (1) Claim 4 的
481	    method-correlation failure：高 Jaccard → CSS 无效（4/4 正确预测） (2) Claim 3 的 component-level
482	    scoring failure：方法退化 → CSS 不可能成立（与 Jaccard 无关） 仅用 GPT-2 的 4 个任务时 ρ=-1.0 (perfect
483	    negative rank correlation, p=0.042)， 说明在单模型内 Jaccard diagnostic 是 perfect predictor。
484	    跨模型时 Qwen 引入了 Claim 3 的新 failure mode，使 Jaccard 不再是 sole predictor—— 这恰恰是论文需要
485	    Claim 3 + Claim 4 两个独立 claim 的原因。
486	
487	    '
488	  tables:
489	  - name: 'Table: Jaccard-CSS Diagnostic Data (Main Result, Table 3 or 4)'
490	    description: '行: 6 个 model×task 配置（按 max Jaccard 升序排列） 列: Task, Model, Methods,
491	      Max Jaccard, CSS=1.0 CPR, Best Single CPR, Δ, Diagnostic Prediction, Actual,
492	      Correct? 底部: Accuracy = 5/6。Qwen ACDC 行标注为 "scaling failure outlier"。 辅助行: Spearman
493	      ρ=-0.900 (p=0.037, excluding outlier), ρ=-0.714 (p=0.111, all 6)
494	
495	      '
496	  - name: 'Table: GPT-2 Subset (4 tasks)'
497	    description: '仅 IOI, Factual Recall, SVA, Arithmetic on GPT-2。ρ=-1.0, p=0.042。
498	      展示 within-model 的 perfect negative rank correlation。
499	
500	      '
501	  figures_description:
502	  - '核心 Figure（论文 Figure 3 或 4）: Scatter plot, x=max pairwise Jaccard, y=CSS CPR advantage
503	    (Δ)。 6 个数据点，颜色区分模型（GPT-2 蓝, Qwen 橙），形状区分结果（圆=PASS, ×=FAIL）。 灰色虚线 y=0 分隔 positive/negative
504	    region。 垂直虚线 x=0.35 和 x=0.50 标注 diagnostic thresholds。 Qwen ACDC 点（左下角,×）用虚线圈标注
505	    "scaling failure (Claim 3)"，与 regression 分开。 排除 outlier 后的 regression line 从右下到左上（负斜率）。
506	    右上角: ρ=-0.900, p=0.037 (excl. outlier)。 这是全文最重要的图——将 Claim 3 和 Claim 4 的关系浓缩为一张可视化。
507	
508	    '
509	  analysis: 'Jaccard-CSS scatter 是论文的 crown jewel figure。它同时展示了两个核心发现： (1) 在方法正常工作的
510	    5 个配置中，max Jaccard 是 CSS outcome 的强预测因子（ρ=-0.900, p=0.037） (2) Qwen ACDC outlier
511	    直观地展示了 Claim 3 的独立 failure mode 论文的 practical guideline 可以从这张图直接读出： Step 1: 验证方法
512	    scoring granularity（排除 Claim 3 failure） Step 2: 计算 max pairwise Jaccard（< 0.35
513	    proceed, > 0.50 use best single method） Claim 4 从 "motivated conjecture" 升级为 "empirically
514	    supported heuristic"—— 5/6 diagnostic accuracy + p=0.037 correlation + clear mechanistic
515	    explanation 对 n=6 的 underpowered caveat 保持诚实，但指出 within-model perfect correlation
516	    (ρ=-1.0) 和 cross-model consistency 共同支撑 heuristic 的可靠性。'
517	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33f1249d-5ad0-440e-8185-a21f7b21a667",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "48e88f45-a051-4d48-8318-4132ba84bad9",
  "sourceToolAssistantUUID": "33f1249d-5ad0-440e-8185-a21f7b21a667",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-13T09:56:27.598Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LnwMCae4CqEp28HcU3tvWY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48e88f45-a051-4d48-8318-4132ba84bad9",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNJpGX6uy2ftE1aNGGo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa0bcdb4-0629-4d57-8b0a-f62946b47355",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012hVCJzwRdsFDREdAw6zuY3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 50388,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 582
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 50388,
          "cache_creation_input_tokens": 582,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 582,
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

_source line 39 · 2026-05-13T09:56:27.604Z_

<details><summary>↩ Tool result · `toolu_01LnwMCae4CqEp28HcU3tvWY`</summary>

```text
1	# Experiment Plan — structfuse-context (Route A: Analysis Paper)
2	# 最后更新: 2026-05-13 | 更新原因: D034 reframe 为 "When Does Consensus Fail" 分析论文
3	
4	experiments:
5	  # === GPT-2 Task Coverage (Claim 2: CSS fails on majority of configs) ===
6	  - plan_id: plan_001
7	    name: "GPT-2 IOI K=3 CSS"
8	    claim: ["Claim 2", "Claim 4"]
9	    description: "GPT-2 Small / IOI, K=3 (EAP-IG + EP + ACDC isinf). Lone positive case — CSS=1.0 CPR > single method"
10	    registry_id: mvp_pilot_gpt2_ioi_v3
11	    priority: P0
12	    status: done
13	    result: "PASS — CSS=1.0 (7 edges) CPR=0.109 > all single methods; Jaccard=0.31"
14	
15	  - plan_id: plan_002
16	    name: "GPT-2 Arithmetic K=3 CSS"
17	    claim: ["Claim 2", "Claim 4"]
18	    description: "GPT-2 Small / Greaterthan, K=3. Task structure forces high Jaccard → CSS fails"
19	    registry_id: mvp_arithmetic_gpt2_k3
20	    priority: P0
21	    status: done
22	    result: "FAIL — CSS=1.0 CPR < EAP-IG; Jaccard=0.695 (methods too correlated)"
23	
24	  - plan_id: plan_003
25	    name: "GPT-2 SVA K=3 CSS"
26	    claim: ["Claim 2", "Claim 4"]
27	    description: "GPT-2 Small / SVA. Inconclusive — marginal signal at noise level"
28	    registry_id: mvp_sva_gpt2_k3_topk
29	    priority: P0
30	    status: done
31	    result: "INCONCLUSIVE — D033: cross-server Δ=0.006/0.013, avg < 0.01 threshold"
32	
33	  - plan_id: plan_004
34	    name: "GPT-2 Factual Recall K=3 CSS"
35	    claim: ["Claim 2", "Claim 4"]
36	    description: "GPT-2 Small / Country-Capital factual recall. MLP-based knowledge retrieval circuit"
37	    registry_id: gpt2_factual_recall_k3_v2
38	    priority: P0
39	    status: running
40	    depends_on: []
41	    gpu_hours_est: 1
42	
43	  # === ACDC Binarization Pathology (Claim 1: strongest contribution) ===
44	  - plan_id: plan_005
45	    name: "ACDC isinf→top-k binarization sweep"
46	    claim: ["Claim 1"]
47	    description: "k=50/75/100/150 on IOI and Arithmetic. Show isinf→top-k Jaccard shift and CSS degeneration break"
48	    priority: P0
49	    status: done
50	    result: "Confirmed: isinf causes CSS=1.0≡ACDC; top-k breaks degeneration; Jaccard shifts +0.16 to +0.25"
51	
52	  # === Cross-Model Scaling Failure (Claim 3: component-level scoring) ===
53	  - plan_id: plan_006
54	    name: "Qwen-0.5B IOI K=3 with IFR"
55	    claim: ["Claim 3"]
56	    description: "First scaling attempt. IFR degenerates to block-voting (layer-level), zero CSS=1.0 edges"
57	    registry_id: phase2_qwen05b_ioi_k3
58	    priority: P0
59	    status: done
60	    result: "FAIL — IFR Jaccard=0.000 with gradient methods; block-voting granularity mismatch"
61	
62	  - plan_id: plan_007
63	    name: "Qwen-0.5B IOI K=3 with ACDC"
64	    claim: ["Claim 3"]
65	    description: "D029: ACDC替代IFR. ACDC also degenerates to node-level scoring on 179K-edge model"
66	    registry_id: phase2_qwen05b_ioi_acdc_k3
67	    priority: P0
68	    status: done
69	    result: "FAIL — ACDC node-level scoring; all Jaccard≈0; zero CSS=1.0 edges. Confirms scaling failure is structural"
70	
71	  # === Critical Controls (Dream reviewers unanimously requested) ===
72	  - plan_id: plan_008
73	    name: "IOI size-controlled baseline"
74	    claim: ["Claim 2"]
75	    description: "Compare CSS=1.0 (N edges) vs top-N of each single method + random-N. Rules out size confound"
76	    priority: P0
77	    status: running
78	    depends_on: [plan_001]
79	    gpu_hours_est: 0.5
80	
81	  - plan_id: plan_009
82	    name: "Bootstrap confidence intervals on CPR"
83	    claim: ["Claim 2"]
84	    description: "Bootstrap CIs on all CPR differences across all completed experiments"
85	    priority: P1
86	    status: planned
87	    depends_on: [plan_004, plan_008]
88	    gpu_hours_est: 1
89	
90	  # === Comparative / Ablation ===
91	  - plan_id: plan_010
92	    name: "CIRCUS negative ablation"
93	    claim: ["Claim 5"]
94	    description: "D021: CIRCUS failed 3×. Within-method threshold diversity produces negative CPR on all tasks"
95	    priority: P1
96	    status: done
97	    result: "CIRCUS negative CPR on all tasks. Implementation caveats noted"
98	    gpu_hours_est: 0
99	
100	  - plan_id: plan_011
101	    name: "Ablation method comparison (zero vs mean)"
102	    claim: ["Claim 2"]
103	    description: "Compare zero and mean ablation on IOI. Dream worst-tier identified zero ablation bias as IOI confound"
104	    priority: P1
105	    status: planned
106	    depends_on: [plan_008]
107	    gpu_hours_est: 1
108	
109	  # === Discussion Analyses ===
110	  - plan_id: plan_012
111	    name: "IFR vs ACDC vs gradient method divergence analysis"
112	    claim: ["Claim 3"]
113	    description: "Document IFR and ACDC failure modes on Qwen as case study for component-level scoring issue"
114	    priority: P2
115	    status: planned
116	    depends_on: [plan_006, plan_007]
117	    gpu_hours_est: 0
118	
119	  - plan_id: plan_013
120	    name: "Jaccard-CSS scatter plot + correlation"
121	    claim: ["Claim 4"]
122	    description: "Across all completed experiments, plot max Jaccard vs CSS advantage. Report honestly as underpowered (n≤6)"
123	    priority: P1
124	    status: planned
125	    depends_on: [plan_004, plan_008]
126	    gpu_hours_est: 0
127	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa0bcdb4-0629-4d57-8b0a-f62946b47355",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "0c86aedd-7ff6-439a-abbf-6c50d73801b1",
  "sourceToolAssistantUUID": "aa0bcdb4-0629-4d57-8b0a-f62946b47355",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-13T09:56:30.428Z_

Now let me also check for the actual experimental artifacts and code to assess reproducibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c86aedd-7ff6-439a-abbf-6c50d73801b1",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNK5zZkPgS1ZcbaHC6J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9df116d-1956-46a3-aed7-80dbe3ef4b22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DmcAvYZXNnU75j5L8GXxQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14044,
      "cache_read_input_tokens": 50970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14044,
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

_source line 41 · 2026-05-13T09:56:32.563Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LCVM52cy2kLrnatqbyxv6i`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9df116d-1956-46a3-aed7-80dbe3ef4b22",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNK5zZkPgS1ZcbaHC6J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8a1888e-084c-4dd0-8d5a-9a12c1ecb1e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DmcAvYZXNnU75j5L8GXxQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14044,
      "cache_read_input_tokens": 50970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14044,
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

_source line 42 · 2026-05-13T09:56:32.575Z_

<details><summary>↩ Tool result · `toolu_01LCVM52cy2kLrnatqbyxv6i`</summary>

```text
artifacts/structfuse-mvp/circus.py
artifacts/structfuse-mvp/evaluation.py
artifacts/_project/intermediate/run_mvp.py
artifacts/structfuse-mvp/cross_tabulate.py
artifacts/structfuse-mvp/run_mvp.py
artifacts/_project/intermediate/ifr_discovery.py
artifacts/structfuse-mvp/ifr_discovery.py
artifacts/structfuse-mvp/css.py
artifacts/structfuse-mvp/config.py
artifacts/_project/intermediate/edge_pruning_l0.py
artifacts/structfuse-mvp/edge_pruning_l0.py
artifacts/structfuse-mvp/circuit_discovery.py
artifacts/_project/intermediate/ifr_scoring.py
artifacts/ifr_scoring.py
artifacts/_project/intermediate/test_ifr_scoring.py
artifacts/test_ifr_scoring.py
artifacts/_project/intermediate/model_adapter.py
artifacts/model_adapter.py
artifacts/_project/intermediate/run_circus.py
artifacts/_project/intermediate/css.py
artifacts/_project/intermediate/test_css.py
artifacts/_project/intermediate/edge_pruning_scoring.py
artifacts/_project/intermediate/test_edge_pruning_scoring.py
artifacts/_project/intermediate/eap_ig_scoring.py
artifacts/eap_ig_scoring.py
artifacts/_project/intermediate/test_eap_ig_scoring.py
artifacts/test_eap_ig_scoring.py
artifacts/_project/intermediate/edge_pruning_scoring_457920.py
artifacts/edge_pruning_scoring.py
artifacts/_project/intermediate/test_edge_pruning_scoring_3089a7.py
artifacts/test_edge_pruning_scoring.py
artifacts/test_run_circus_fixes.py
artifacts/_project/intermediate/analyze_mvp_results.py
artifacts/_project/data/run_phase2_experiment.py
artifacts/analyze_mvp_results.py
artifacts/run_phase2_experiment.py
artifacts/css.py
artifacts/run_circus.py
artifacts/test_css.py
acdc_topk_sweep.py
artifacts/eval_topk_faithfulness.py
artifacts/_project/intermediate/run_factual_recall.py
artifacts/run_factual_recall.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8a1888e-084c-4dd0-8d5a-9a12c1ecb1e1",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "3a24d6ad-75be-4643-b6e2-1a70b44d3714",
  "sourceToolAssistantUUID": "a8a1888e-084c-4dd0-8d5a-9a12c1ecb1e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-13T09:56:32.957Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LxqPzW6xkueCrwqbyjM5Ra`</summary>

```json
{
  "pattern": "**/artifacts/**/*.txt",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a24d6ad-75be-4643-b6e2-1a70b44d3714",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNK5zZkPgS1ZcbaHC6J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30a2cdec-657e-4fdf-b545-5919500ab11a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DmcAvYZXNnU75j5L8GXxQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14044,
      "cache_read_input_tokens": 50970,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14044
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 50970,
          "cache_creation_input_tokens": 14044,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14044,
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

_source line 44 · 2026-05-13T09:56:33.000Z_

<details><summary>↩ Tool result · `toolu_01LxqPzW6xkueCrwqbyjM5Ra`</summary>

```text
artifacts/_project/intermediate/analysis_fix_v3_meta.txt
artifacts/phase2_qwen05b_ioi_k3/data/phase2_qwen05b_ioi_k3_summary.txt
artifacts/phase2_qwen05b_ioi_k3/data/proportional_binarize_ablation_pointer.txt
artifacts/mvp_sva_gpt2_k3_topk/data/sva_css067_fix_results.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30a2cdec-657e-4fdf-b545-5919500ab11a",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "02c2ae89-b114-4756-b8d3-3a028255b64c",
  "sourceToolAssistantUUID": "30a2cdec-657e-4fdf-b545-5919500ab11a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-13T09:56:35.910Z_

Let me read the CSS implementation and evaluation code to assess methodological soundness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02c2ae89-b114-4756-b8d3-3a028255b64c",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNKUpFvoZGTix3Jvz1B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56dce9fe-2936-4a73-a40f-d508023b20a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MP1uURys8zrUAXUwd3qnAj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 938,
      "cache_read_input_tokens": 65014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 938,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 46 · 2026-05-13T09:56:36.537Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E3dWubqyP4KtteAh4hPkg8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/css.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56dce9fe-2936-4a73-a40f-d508023b20a6",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNKUpFvoZGTix3Jvz1B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4de8023a-1361-42b6-a33a-1bb11801cdda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MP1uURys8zrUAXUwd3qnAj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 938,
      "cache_read_input_tokens": 65014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 938,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 47 · 2026-05-13T09:56:36.557Z_

<details><summary>↩ Tool result · `toolu_01E3dWubqyP4KtteAh4hPkg8`</summary>

```text
1	"""Cross-method Stability Scoring (CSS).
2	Computes per-edge consensus across K independent circuit discovery methods.
3	CSS(edge) = (number of methods selecting edge) / K, taking values in {0, 1/K, ..., 1}.
4	"""
5	
6	from typing import Dict, Set
7	
8	
9	def compute_css(
10	    method_circuits: Dict[str, Set[str]],
11	    K: int,
12	) -> Dict[str, float]:
13	    """Compute CSS scores from K methods' binary edge sets.
14	
15	    Args:
16	        method_circuits: method_name -> set of selected edge names
17	        K: total number of methods (used as denominator)
18	
19	    Returns:
20	        edge_name -> CSS score in {0, 1/K, 2/K, ..., 1}
21	    """
22	    all_edges: Set[str] = set()
23	    for edges in method_circuits.values():
24	        all_edges |= edges
25	
26	    css_scores = {}
27	    for edge in all_edges:
28	        count = sum(1 for edges in method_circuits.values() if edge in edges)
29	        css_scores[edge] = count / K
30	
31	    return css_scores
32	
33	
34	def threshold_css(
35	    css_scores: Dict[str, float],
36	    threshold: float = 0.67,
37	) -> Set[str]:
38	    """Select edges meeting CSS threshold.
39	
40	    Threshold is snapped to nearest n/K level to avoid floating point issues
41	    (e.g. threshold=0.67 matches CSS=2/3=0.6666...).
42	
43	    Args:
44	        css_scores: edge_name -> CSS score
45	        threshold: minimum CSS to include (default 0.67 = 2/3 for K=3)
46	
47	    Returns:
48	        Set of edge names with CSS >= threshold
49	    """
50	    eps = 0.01
51	    return {edge for edge, score in css_scores.items() if score >= threshold - eps}
52	
53	
54	def binarize_scores(
55	    edge_scores: Dict[str, float],
56	    method: str = "eap_ig",
57	    top_n: int = 100,
58	) -> Set[str]:
59	    """Convert edge scores to binary circuit using method-appropriate strategy.
60	
61	    - EAP-IG: continuous attribution scores → top-N by absolute value
62	    - Edge Pruning: L0 mask values in [0,1] → threshold at 0.5
63	    - ACDC: binary inclusion (0 or 1) → select all non-zero edges
64	
65	    Args:
66	        edge_scores: edge_name -> score (interpretation depends on method)
67	        method: "eap_ig" | "edge_pruning" | "acdc"
68	        top_n: number of top edges (only used for eap_ig)
69	
70	    Returns:
71	        Set of selected edge names
72	    """
73	    if method == "acdc":
74	        return {edge for edge, score in edge_scores.items() if score > 0}
75	    elif method == "edge_pruning":
76	        return {edge for edge, score in edge_scores.items() if score > 0.5}
77	    elif method == "ifr":
78	        sorted_edges = sorted(edge_scores.items(), key=lambda x: abs(x[1]), reverse=True)
79	        return {edge for edge, _ in sorted_edges[:top_n]}
80	    else:
81	        sorted_edges = sorted(edge_scores.items(), key=lambda x: abs(x[1]), reverse=True)
82	        return {edge for edge, _ in sorted_edges[:top_n]}
83	
84	
85	def css_summary(css_scores: Dict[str, float], K: int) -> Dict[str, int]:
86	    """Count edges at each CSS level.
87	
88	    Returns:
89	        Dict mapping CSS level string to count, e.g. {"0/3": 50, "1/3": 30, "2/3": 15, "3/3": 5}
90	    """
91	    from collections import Counter
92	    level_counts = Counter()
93	    for score in css_scores.values():
94	        n_methods = round(score * K)
95	        level_counts[f"{n_methods}/{K}"] += 1
96	    return dict(sorted(level_counts.items()))
97	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4de8023a-1361-42b6-a33a-1bb11801cdda",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "ad7ef3dc-e149-4ce2-a3c4-1f615c42769e",
  "sourceToolAssistantUUID": "4de8023a-1361-42b6-a33a-1bb11801cdda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-13T09:56:36.939Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Pfe6WhotFDK9AwA76ydaB6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/evaluation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad7ef3dc-e149-4ce2-a3c4-1f615c42769e",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNKUpFvoZGTix3Jvz1B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8fc1565-79d3-4391-9d95-75ac97912e41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MP1uURys8zrUAXUwd3qnAj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 938,
      "cache_read_input_tokens": 65014,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 938
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 65014,
          "cache_creation_input_tokens": 938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 938,
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

_source line 49 · 2026-05-13T09:56:36.948Z_

<details><summary>↩ Tool result · `toolu_01Pfe6WhotFDK9AwA76ydaB6`</summary>

```text
1	"""Circuit faithfulness evaluation.
2	Measures how well a discovered circuit preserves model behavior (CPR/CMD metrics).
3	"""
4	
5	from typing import Dict, Set, List, Any, Optional
6	from dataclasses import dataclass
7	
8	
9	@dataclass
10	class CircuitEvalResult:
11	    """Evaluation result for a single circuit."""
12	    name: str
13	    num_edges: int
14	    cpr: float  # Circuit Performance Recovery: how much of original performance the circuit retains
15	    cmd: float  # Circuit Metric Difference: absolute difference from full model
16	
17	    def to_dict(self) -> Dict[str, Any]:
18	        return {
19	            "name": self.name,
20	            "num_edges": self.num_edges,
21	            "cpr": round(self.cpr, 4),
22	            "cmd": round(self.cmd, 4),
23	        }
24	
25	
26	def evaluate_circuit(
27	    model,
28	    circuit_edges: Set[str],
29	    dataset,
30	    metric,
31	) -> CircuitEvalResult:
32	    """Evaluate faithfulness of a circuit.
33	
34	    Runs the model with only circuit_edges active (ablating everything else)
35	    and measures how well the circuit preserves the original metric.
36	
37	    Args:
38	        model: HookedTransformer instance
39	        circuit_edges: set of edge names defining the circuit
40	        dataset: evaluation dataset
41	        metric: callable returning a scalar metric (e.g. logit difference)
42	
43	    Returns:
44	        CircuitEvalResult with CPR and CMD scores
45	    """
46	    # TODO: implement ablation-based evaluation
47	    # 1. Run full model to get baseline metric value
48	    # baseline = metric(model, dataset)
49	    #
50	    # 2. Run model with only circuit_edges active
51	    #    (zero-ablate or mean-ablate all other edges)
52	    # circuit_metric = run_with_circuit(model, circuit_edges, dataset, metric)
53	    #
54	    # 3. Compute CPR = circuit_metric / baseline
55	    #    Compute CMD = |baseline - circuit_metric|
56	
57	    # Placeholder
58	    return CircuitEvalResult(
59	        name="",
60	        num_edges=len(circuit_edges),
61	        cpr=0.0,
62	        cmd=0.0,
63	    )
64	
65	
66	def evaluate_all_circuits(
67	    model,
68	    circuits: Dict[str, Set[str]],
69	    dataset,
70	    metric,
71	) -> List[CircuitEvalResult]:
72	    """Evaluate multiple circuits for comparison.
73	
74	    Args:
75	        model: HookedTransformer instance
76	        circuits: name -> edge set for each circuit variant
77	        dataset: evaluation dataset
78	        metric: callable metric
79	
80	    Returns:
81	        List of CircuitEvalResult, one per circuit
82	    """
83	    results = []
84	    for name, edges in circuits.items():
85	        print(f"Evaluating circuit: {name} ({len(edges)} edges)")
86	        result = evaluate_circuit(model, edges, dataset, metric)
87	        result.name = name
88	        results.append(result)
89	
90	    return results
91	
92	
93	def print_eval_table(results: List[CircuitEvalResult]) -> None:
94	    """Pretty-print evaluation results as a comparison table."""
95	    print(f"\n{'Circuit':<30} {'Edges':>6} {'CPR':>8} {'CMD':>8}")
96	    print("-" * 54)
97	    for r in sorted(results, key=lambda x: x.cpr, reverse=True):
98	        print(f"{r.name:<30} {r.num_edges:>6} {r.cpr:>8.4f} {r.cmd:>8.4f}")
99	    print()
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8fc1565-79d3-4391-9d95-75ac97912e41",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "847ee7dd-0be7-4f2c-99d9-d7ad8539f66e",
  "sourceToolAssistantUUID": "f8fc1565-79d3-4391-9d95-75ac97912e41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-13T09:56:39.985Z_

Let me also check the run scripts for the actual experiments to assess implementation details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "847ee7dd-0be7-4f2c-99d9-d7ad8539f66e",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNKmh1goKMATkCX17bT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "609b1cc6-3999-4fb3-80cc-369a2165e270",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuMsM5tyvMHbsdSmg3aEyw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2530,
      "cache_read_input_tokens": 65952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2530,
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

_source line 51 · 2026-05-13T09:56:42.342Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RcQAK4XHH5U7X6DBxGzuMn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/run_mvp.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "609b1cc6-3999-4fb3-80cc-369a2165e270",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNKmh1goKMATkCX17bT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef6afb47-c9de-4ea4-bb95-5c5fe6b5fcb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuMsM5tyvMHbsdSmg3aEyw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2530,
      "cache_read_input_tokens": 65952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2530,
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

_source line 52 · 2026-05-13T09:56:42.346Z_

<details><summary>↩ Tool result · `toolu_01RcQAK4XHH5U7X6DBxGzuMn`</summary>

```text
1	"""StructFuse MVP main pipeline.
2	Runs K=3 circuit discovery methods on GPT-2 Small / IOI,
3	computes CSS and CIRCUS, generates cross-tabulation, evaluates faithfulness.
4	"""
5	
6	import json
7	from pathlib import Path
8	
9	from config import MVP_CONFIG
10	from circuit_discovery import run_all_methods
11	from circus import run_circus
12	from css import compute_css, threshold_css, binarize_scores, css_summary
13	from cross_tabulate import cross_tabulate, compute_off_diagonal, print_cross_table
14	from evaluation import evaluate_all_circuits, print_eval_table
15	
16	
17	def load_model_and_data(config):
18	    """Load GPT-2 Small and IOI dataset via TransformerLens."""
19	    from transformer_lens import HookedTransformer
20	
21	    print(f"Loading model: {config.model_name}")
22	    model = HookedTransformer.from_pretrained(config.model_name)
23	
24	    # TODO: use proper IOI dataset
25	    # from transformer_lens.evals import IOIDataset
26	    # dataset = IOIDataset(tokenizer=model.tokenizer, num_samples=config.num_samples)
27	    dataset = None  # placeholder
28	
29	    return model, dataset
30	
31	
32	def logit_diff_metric(logits, tokens):
33	    """IOI logit difference metric: logit(IO) - logit(S)."""
34	    # TODO: implement proper IOI metric
35	    pass
36	
37	
38	def main():
39	    config = MVP_CONFIG
40	    print(f"StructFuse MVP: model={config.model_name}, task={config.task}, K={config.K}")
41	    print(f"Methods: {config.methods}")
42	    print()
43	
44	    # Step 1: Load model + data
45	    model, dataset = load_model_and_data(config)
46	
47	    # Step 2: Run K=3 circuit discovery methods
48	    all_scores = run_all_methods(model, dataset, logit_diff_metric, config)
49	
50	    # Step 3: Binarize each method's scores using method-appropriate strategy
51	    method_circuits = {}
52	    for method, scores in all_scores.items():
53	        method_circuits[method] = binarize_scores(scores, method=method, top_n=config.eap_ig_topn)
54	        print(f"{method}: {len(method_circuits[method])} edges selected")
55	
56	    # Step 4: CIRCUS config-bagging on EAP-IG
57	    print("\n--- CIRCUS (EAP-IG) ---")
58	    eap_stability, circus_tiers = run_circus(all_scores["eap_ig"], config)
59	
60	    # Step 5: CSS across K=3 methods
61	    print("\n--- CSS (K=3) ---")
62	    css_scores = compute_css(method_circuits, K=config.K)
63	    print(f"CSS distribution: {css_summary(css_scores, config.K)}")
64	
65	    css_circuit = threshold_css(css_scores, config.css_default_threshold)
66	    print(f"CSS circuit (>= {config.css_default_threshold}): {len(css_circuit)} edges")
67	
68	    # Step 6: Cross-tabulation
69	    print("\n--- Cross-Tabulation ---")
70	    table = cross_tabulate(circus_tiers, css_scores, config.css_default_threshold)
71	    print_cross_table(table)
72	
73	    off_diag = compute_off_diagonal(table)
74	    print(f"Off-diagonal %: {off_diag*100:.1f}%")
75	
76	    # Step 7: Evaluate all circuit variants
77	    print("\n--- Evaluation ---")
78	    circuits_to_eval = {}
79	
80	    # Individual method circuits
81	    for method, edges in method_circuits.items():
82	        circuits_to_eval[f"method_{method}"] = edges
83	
84	    # CSS circuits at various thresholds
85	    for thr in config.css_thresholds:
86	        if thr > 0:
87	            css_edges = threshold_css(css_scores, thr)
88	            circuits_to_eval[f"css_{thr:.2f}"] = css_edges
89	
90	    # CIRCUS-core circuit
91	    from circus import get_tier_sets
92	    tier_sets = get_tier_sets(circus_tiers)
93	    circuits_to_eval["circus_core"] = tier_sets["core"]
94	
95	    # Stable-core (CIRCUS-core AND CSS-high)
96	    circuits_to_eval["stable_core"] = table.stable_core
97	
98	    eval_results = evaluate_all_circuits(model, circuits_to_eval, dataset, logit_diff_metric)
99	    print_eval_table(eval_results)
100	
101	    # Step 8: MVP gate (graduated per ROADMAP D001-D003)
102	    print("\n" + "=" * 50)
103	    print("MVP GATE ASSESSMENT")
104	    print("=" * 50)
105	    pct = off_diag * 100
106	    if pct >= 10:
107	        gate_verdict = "PASS_MAIN"
108	        gate_msg = f"Off-diagonal {pct:.1f}% >= 10% → Main track, proceed to full experiments"
109	    elif pct >= 5:
110	        gate_verdict = "PASS_FINDINGS"
111	        gate_msg = f"Off-diagonal {pct:.1f}% in [5-10%) → Findings default, add Arithmetic task to confirm"
112	    elif pct >= 2:
113	        gate_verdict = "MARGINAL"
114	        gate_msg = f"Off-diagonal {pct:.1f}% in [2-5%) → Findings track, needs confirmation"
115	    else:
116	        gate_verdict = "KILL"
117	        gate_msg = f"Off-diagonal {pct:.1f}% < 2% → Kill project (if ΔF also not significant)"
118	    print(f"Off-diagonal %: {pct:.1f}%")
119	    print(f"Verdict: {gate_verdict}")
120	    print(f"Action: {gate_msg}")
121	
122	    # Save results
123	    output = {
124	        "config": {
125	            "model": config.model_name,
126	            "task": config.task,
127	            "K": config.K,
128	            "methods": config.methods,
129	        },
130	        "cross_table": table.summary(),
131	        "core_off_diagonal_pct": off_diag,
132	        "css_distribution": css_summary(css_scores, config.K),
133	        "circus_tier_counts": {
134	            t: sum(1 for v in circus_tiers.values() if v == t)
135	            for t in ["core", "contingent", "noise"]
136	        },
137	        "evaluation": [r.to_dict() for r in eval_results],
138	        "gate_verdict": gate_verdict,
139	    }
140	
141	    output_path = Path(__file__).parent / "mvp_results.json"
142	    with open(output_path, "w") as f:
143	        json.dump(output, f, indent=2)
144	    print(f"\nResults saved to {output_path}")
145	
146	
147	if __name__ == "__main__":
148	    main()
149	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef6afb47-c9de-4ea4-bb95-5c5fe6b5fcb8",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "e899bec8-6c31-4e84-8b19-39c822d830a6",
  "sourceToolAssistantUUID": "ef6afb47-c9de-4ea4-bb95-5c5fe6b5fcb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-13T09:56:42.808Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KbMtidxBY7wNp81QrfAZqJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/run_factual_recall.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e899bec8-6c31-4e84-8b19-39c822d830a6",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNKmh1goKMATkCX17bT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2e9e803-6b1a-4e3c-a0af-64c076884f80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuMsM5tyvMHbsdSmg3aEyw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2530,
      "cache_read_input_tokens": 65952,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2530
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 65952,
          "cache_creation_input_tokens": 2530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2530,
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

_source line 54 · 2026-05-13T09:56:42.813Z_

<details><summary>↩ Tool result · `toolu_01KbMtidxBY7wNp81QrfAZqJ`</summary>

```text
1	import os
2	os.environ["CUDA_VISIBLE_DEVICES"] = "1"
3	
4	"""StructFuse Factual Recall (Country Capitals) pipeline — GPT-2 Small.
5	
6	Task: "The capital of {country} is" → correct capital vs wrong capital.
7	Circuit tests MLP-based factual knowledge retrieval (Meng et al. 2022).
8	All three methods use identical top-100 binarization for fair comparison.
9	Evaluation includes both zero and mean ablation.
10	"""
11	
12	import json
13	import random
14	import gc
15	import re
16	from pathlib import Path
17	from functools import partial
18	from collections import Counter
19	
20	import torch
21	from torch.utils.data import DataLoader, Dataset
22	
23	from config import MVPConfig
24	from circuit_discovery import run_eap_ig, run_edge_pruning, run_acdc
25	from circus import run_circus, get_tier_sets
26	from cross_tabulate import (
27	    cross_tabulate, compute_off_diagonal, print_cross_table,
28	    pairwise_jaccard, three_way_jaccard, print_pairwise_jaccard,
29	)
30	
31	
32	_LOCAL_GPT2 = "/root/autodl-tmp/gpt2-small"
33	_GPT2_ALIASES = ("gpt2", "gpt2-small", "openai-community/gpt2")
34	
35	def _patch_hf_from_pretrained():
36	    from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM
37	    def _make_patched(orig_fn):
38	        def patched(pretrained_model_name_or_path, *args, **kwargs):
39	            if pretrained_model_name_or_path in _GPT2_ALIASES:
40	                pretrained_model_name_or_path = _LOCAL_GPT2
41	            return orig_fn(pretrained_model_name_or_path, *args, **kwargs)
42	        return patched
43	    AutoConfig.from_pretrained = staticmethod(_make_patched(AutoConfig.from_pretrained))
44	    AutoTokenizer.from_pretrained = staticmethod(_make_patched(AutoTokenizer.from_pretrained))
45	    AutoModelForCausalLM.from_pretrained = staticmethod(_make_patched(AutoModelForCausalLM.from_pretrained))
46	
47	_patch_hf_from_pretrained()
48	
49	
50	# ---------------------------------------------------------------------------
51	# Factual Recall Dataset
52	# ---------------------------------------------------------------------------
53	
54	COUNTRY_CAPITAL_PAIRS = [
55	    ("France", "Paris"), ("Germany", "Berlin"), ("Japan", "Tokyo"),
56	    ("Italy", "Rome"), ("Spain", "Madrid"), ("Russia", "Moscow"),
57	    ("China", "Beijing"), ("England", "London"), ("Poland", "Warsaw"),
58	    ("Greece", "Athens"), ("Ireland", "Dublin"), ("Sweden", "Stockholm"),
59	    ("Norway", "Oslo"), ("Portugal", "Lisbon"), ("Austria", "Vienna"),
60	    ("Egypt", "Cairo"), ("Korea", "Seoul"), ("Denmark", "Copenhagen"),
61	    ("Belgium", "Brussels"), ("Netherlands", "Amsterdam"),
62	    ("Ukraine", "Kiev"), ("Turkey", "Istanbul"),
63	]
64	
65	
66	def generate_factual_recall_prompts(num_samples=500, seed=42):
67	    rng = random.Random(seed)
68	    n = len(COUNTRY_CAPITAL_PAIRS)
69	    prompts = []
70	    seen = set()
71	    attempts = 0
72	    while len(prompts) < num_samples and attempts < num_samples * 20:
73	        attempts += 1
74	        i = rng.randint(0, n - 1)
75	        j = rng.randint(0, n - 2)
76	        if j >= i:
77	            j += 1
78	        sig = (i, j)
79	        if sig in seen:
80	            continue
81	        seen.add(sig)
82	        country, capital = COUNTRY_CAPITAL_PAIRS[i]
83	        wrong_country, wrong_capital = COUNTRY_CAPITAL_PAIRS[j]
84	        clean = f"The capital of {country} is"
85	        corrupt = f"The capital of {wrong_country} is"
86	        prompts.append({
87	            "clean": clean,
88	            "corrupt": corrupt,
89	            "answer": capital,
90	            "wrong_answer": wrong_capital,
91	        })
92	    return prompts
93	
94	
95	FR_DATASET_PATH = "/root/miniconda3/lib/python3.12/site-packages/datasets/factual_recall_gpt2-small_prompts.json"
96	
97	
98	def ensure_fr_dataset():
99	    if not os.path.exists(FR_DATASET_PATH):
100	        prompts = generate_factual_recall_prompts(num_samples=500, seed=42)
101	        with open(FR_DATASET_PATH, "w") as f:
102	            json.dump({"prompts": prompts}, f, indent=2)
103	        print(f"FR dataset created: {len(prompts)} prompts -> {FR_DATASET_PATH}")
104	    else:
105	        with open(FR_DATASET_PATH) as f:
106	            n = len(json.load(f)["prompts"])
107	        print(f"FR dataset exists: {n} prompts at {FR_DATASET_PATH}")
108	
109	
110	class FactualRecallDataset(Dataset):
111	    def __init__(self, tokenizer, num_samples=100, seed=42):
112	        ensure_fr_dataset()
113	        with open(FR_DATASET_PATH) as f:
114	            all_prompts = json.load(f)["prompts"]
115	        random.seed(seed)
116	        if len(all_prompts) > num_samples:
117	            all_prompts = random.sample(all_prompts, num_samples)
118	        self.prompts = []
119	        self.corrupted = []
120	        self.labels = []
121	        for p in all_prompts:
122	            self.prompts.append(p["clean"])
123	            self.corrupted.append(p["corrupt"])
124	            ans_id = tokenizer.encode(" " + p["answer"])[0]
125	            wrong_id = tokenizer.encode(" " + p["wrong_answer"])[0]
126	            self.labels.append((ans_id, wrong_id))
127	
128	    def __len__(self):
129	        return len(self.prompts)
130	
131	    def __getitem__(self, idx):
132	        return self.prompts[idx], self.corrupted[idx], self.labels[idx]
133	
134	
135	def fr_collate_fn(batch):
136	    return [b[0] for b in batch], [b[1] for b in batch], [b[2] for b in batch]
137	
138	
139	def factual_recall_metric(logits, clean_logits, input_lengths, labels):
140	    batch_size = logits.shape[0]
141	    diffs = []
142	    for i in range(batch_size):
143	        last_pos = input_lengths[i] - 1
144	        correct_id, incorrect_id = labels[i]
145	        diff = logits[i, last_pos, correct_id] - logits[i, last_pos, incorrect_id]
146	        diffs.append(diff)
147	    return torch.stack(diffs).mean()
148	
149	
150	# ---------------------------------------------------------------------------
151	# Binarization: ALL top-100 (including ACDC)
152	# ---------------------------------------------------------------------------
153	
154	def binarize_top100(scores, top_n=100):
155	    sorted_edges = sorted(scores.items(), key=lambda x: abs(x[1]), reverse=True)
156	    return {e for e, _ in sorted_edges[:top_n]}
157	
158	
159	# ---------------------------------------------------------------------------
160	# CSS helpers
161	# ---------------------------------------------------------------------------
162	
163	def compute_css(method_circuits, K=3):
164	    all_edges = set()
165	    for edges in method_circuits.values():
166	        all_edges |= edges
167	    scores = {}
168	    for edge in all_edges:
169	        count = sum(1 for c in method_circuits.values() if edge in c)
170	        scores[edge] = count / K
171	    return scores
172	
173	
174	def threshold_css(css_scores, threshold):
175	    return {e for e, s in css_scores.items() if s >= threshold - 1e-2}
176	
177	
178	def css_summary(css_scores, K=3):
179	    dist = Counter()
180	    for s in css_scores.values():
181	        dist[round(s, 4)] += 1
182	    result = {}
183	    for v in sorted(dist.keys()):
184	        label = f"{v:.2f}"
185	        result[label] = dist[v]
186	        print(f"  CSS={label}: {dist[v]} edges")
187	    return result
188	
189	
190	# ---------------------------------------------------------------------------
191	# Evaluation (zero + mean ablation)
192	# ---------------------------------------------------------------------------
193	
194	def _extract_circuit_nodes(circuit_edges):
195	    nodes = set()
196	    for edge in circuit_edges:
197	        parts = edge.split("->")
198	        if len(parts) != 2:
199	            continue
200	        nodes.add(parts[0].strip())
201	        dst_base = re.sub(r"\.[qkv]$", "", parts[1].strip())
202	        nodes.add(dst_base)
203	    nodes.discard("input")
204	    nodes.discard("logits")
205	    return nodes
206	
207	
208	def evaluate_circuit_fr(model, circuit_edges, clean_tokens, ans_id, wrong_id, ablation="zero"):
209	    if len(circuit_edges) == 0:
210	        return {"name": "", "num_edges": 0, "cpr": 0.0, "cmd": 0.0}
211	
212	    circuit_nodes = _extract_circuit_nodes(circuit_edges)
213	    n_layers, n_heads = model.cfg.n_layers, model.cfg.n_heads
214	
215	    ablate_heads = {}
216	    ablate_mlps = []
217	    for layer in range(n_layers):
218	        heads = [h for h in range(n_heads) if f"a{layer}.h{h}" not in circuit_nodes]
219	        if heads:
220	            ablate_heads[layer] = heads
221	        if f"m{layer}" not in circuit_nodes:
222	            ablate_mlps.append(layer)
223	
224	    mean_cache = {}
225	    if ablation == "mean":
226	        with torch.no_grad():
227	            _, cache = model.run_with_cache(clean_tokens)
228	            for layer in ablate_heads:
229	                hook_name = f"blocks.{layer}.attn.hook_result"
230	                mean_cache[hook_name] = cache[hook_name].mean(dim=0, keepdim=True)
231	            for layer in ablate_mlps:
232	                hook_name = f"blocks.{layer}.hook_mlp_out"
233	                mean_cache[hook_name] = cache[hook_name].mean(dim=0, keepdim=True)
234	            del cache
235	            torch.cuda.empty_cache()
236	
237	    def _head_hook_zero(value, hook, heads_to_ablate):
238	        for h in heads_to_ablate:
239	            value[:, :, h, :] = 0
240	        return value
241	
242	    def _head_hook_mean(value, hook, heads_to_ablate, mean_val):
243	        for h in heads_to_ablate:
244	            value[:, :, h, :] = mean_val[:, :, h, :]
245	        return value
246	
247	    def _mlp_hook_zero(value, hook):
248	        return torch.zeros_like(value)
249	
250	    def _mlp_hook_mean(value, hook, mean_val):
251	        return mean_val.expand_as(value)
252	
253	    with torch.no_grad():
254	        baseline_logits = model(clean_tokens)
255	        bl_diffs = []
256	        for i in range(len(clean_tokens)):
257	            a_id, w_id = ans_id[i], wrong_id[i]
258	            bl_diffs.append(baseline_logits[i, -1, a_id] - baseline_logits[i, -1, w_id])
259	        baseline_diff = torch.stack(bl_diffs).mean().item()
260	
261	        hooks = []
262	        for layer, heads in ablate_heads.items():
263	            hook_name = f"blocks.{layer}.attn.hook_result"
264	            if ablation == "zero":
265	                hooks.append((hook_name, partial(_head_hook_zero, heads_to_ablate=heads)))
266	            else:
267	                hooks.append((hook_name, partial(_head_hook_mean, heads_to_ablate=heads,
268	                                                  mean_val=mean_cache[hook_name])))
269	        for layer in ablate_mlps:
270	            hook_name = f"blocks.{layer}.hook_mlp_out"
271	            if ablation == "zero":
272	                hooks.append((hook_name, _mlp_hook_zero))
273	            else:
274	                hooks.append((hook_name, partial(_mlp_hook_mean, mean_val=mean_cache[hook_name])))
275	
276	        circuit_logits = model.run_with_hooks(clean_tokens, fwd_hooks=hooks)
277	        c_diffs = []
278	        for i in range(len(clean_tokens)):
279	            a_id, w_id = ans_id[i], wrong_id[i]
280	            c_diffs.append(circuit_logits[i, -1, a_id] - circuit_logits[i, -1, w_id])
281	        circuit_diff = torch.stack(c_diffs).mean().item()
282	
283	    cpr = circuit_diff / baseline_diff if abs(baseline_diff) > 1e-6 else 0.0
284	    cmd = abs(baseline_diff - circuit_diff)
285	    return {"name": "", "num_edges": len(circuit_edges), "cpr": round(cpr, 4), "cmd": round(cmd, 4)}
286	
287	
288	def evaluate_all_fr(model, circuits, clean_tokens, ans_id, wrong_id, ablation="zero"):
289	    results = []
290	    for name, edges in circuits.items():
291	        print(f"  {name} ({len(edges)} edges, {ablation})")
292	        r = evaluate_circuit_fr(model, edges, clean_tokens, ans_id, wrong_id, ablation=ablation)
293	        r["name"] = name
294	        r["ablation"] = ablation
295	        results.append(r)
296	    return results
297	
298	
299	# ---------------------------------------------------------------------------
300	# Model loading
301	# ---------------------------------------------------------------------------
302	
303	def load_tl_model(device="cuda"):
304	    from transformer_lens import HookedTransformer
305	    local_path = "/root/autodl-tmp/gpt2-small"
306	    if os.path.exists(os.path.join(local_path, "model.safetensors")):
307	        print(f"Loading GPT-2 from local: {local_path}")
308	        from transformers import AutoModelForCausalLM
309	        hf_model = AutoModelForCausalLM.from_pretrained(local_path)
310	        model = HookedTransformer.from_pretrained("gpt2-small", hf_model=hf_model, device=device)
311	    else:
312	        print("Loading GPT-2 from HuggingFace...")
313	        model = HookedTransformer.from_pretrained("gpt2-small", device=device)
314	    model.set_use_attn_result(True)
315	    model.set_use_split_qkv_input(True)
316	    model.set_use_hook_mlp_in(True)
317	    return model
318	
319	
320	# ---------------------------------------------------------------------------
321	# Main pipeline
322	# ---------------------------------------------------------------------------
323	
324	def main():
325	    device = torch.device("cuda")
326	    config = MVPConfig(
327	        model_name="gpt2-small",
328	        task="factual_recall",
329	        num_samples=100,
330	        methods=["eap_ig", "edge_pruning", "acdc"],
331	        K=3,
332	        eap_ig_steps=5,
333	        eap_ig_topn=100,
334	    )
335	    print(f"StructFuse Factual Recall: model={config.model_name}, task={config.task}, K={config.K}")
336	    print(f"Methods: {config.methods}")
337	    print(f"Binarization: all top-{config.eap_ig_topn}")
338	    print()
339	
340	    all_scores = {}
341	    cache_dir = Path(__file__).parent
342	
343	    # === Phase A: EAP-IG ===
344	    eap_cache = cache_dir / "cache_eap_ig_fr.json"
345	    if eap_cache.exists():
346	        print("=== Phase A: EAP-IG (loading from cache) ===")
347	        with open(eap_cache) as f:
348	            all_scores["eap_ig"] = json.load(f)
349	        print(f"  eap_ig: {len(all_scores['eap_ig'])} edges (cached)")
350	        model = load_tl_model(device=device)
351	        fr_dataset = FactualRecallDataset(model.tokenizer, num_samples=config.num_samples)
352	        eval_prompts = fr_dataset.prompts[:50]
353	        eval_labels = fr_dataset.labels[:50]
354	        del model
355	        gc.collect()
356	        torch.cuda.empty_cache()
357	    else:
358	        print("=== Phase A: EAP-IG ===")
359	        model = load_tl_model(device=device)
360	        print(f"Model loaded: {model.cfg.n_layers} layers, {model.cfg.n_heads} heads")
361	        fr_dataset = FactualRecallDataset(model.tokenizer, num_samples=config.num_samples)
362	        eap_dataloader = DataLoader(fr_dataset, batch_size=25, collate_fn=fr_collate_fn)
363	        print("Running eap_ig...")
364	        all_scores["eap_ig"] = run_eap_ig(model, eap_dataloader, factual_recall_metric, config.eap_ig_steps, config)
365	        print(f"  eap_ig: {len(all_scores['eap_ig'])} edges scored")
366	        with open(eap_cache, "w") as f:
367	            json.dump(all_scores["eap_ig"], f)
368	        print(f"  Cached to {eap_cache}")
369	        eval_prompts = fr_dataset.prompts[:50]
370	        eval_labels = fr_dataset.labels[:50]
371	        del model
372	        gc.collect()
373	        torch.cuda.empty_cache()
374	        print("EAP model freed from GPU")
375	
376	    # === Phase A: Edge Pruning + ACDC ===
377	    ep_cache = cache_dir / "cache_ep_fr.json"
378	    acdc_cache = cache_dir / "cache_acdc_fr.json"
379	    need_ep = not ep_cache.exists()
380	    need_acdc = not acdc_cache.exists()
381	
382	    if ep_cache.exists():
383	        print("\n=== Edge Pruning (loading from cache) ===")
384	        with open(ep_cache) as f:
385	            all_scores["edge_pruning"] = json.load(f)
386	        print(f"  edge_pruning: {len(all_scores['edge_pruning'])} edges (cached)")
387	    if acdc_cache.exists():
388	        print("\n=== ACDC (loading from cache) ===")
389	        with open(acdc_cache) as f:
390	            all_scores["acdc"] = json.load(f)
391	        print(f"  acdc: {len(all_scores['acdc'])} edges (cached)")
392	
393	    if need_ep or need_acdc:
394	        model2 = load_tl_model(device=device)
395	        fr_dataset2 = FactualRecallDataset(model2.tokenizer, num_samples=config.num_samples)
396	        dl2 = DataLoader(fr_dataset2, batch_size=25, collate_fn=fr_collate_fn)
397	
398	        if need_ep:
399	            print("\n=== Phase A: Edge Pruning ===")
400	            all_scores["edge_pruning"] = run_edge_pruning(model2, dl2, factual_recall_metric, config)
401	            print(f"  edge_pruning: {len(all_scores['edge_pruning'])} edges scored")
402	            with open(ep_cache, "w") as f:
403	                json.dump(all_scores["edge_pruning"], f)
404	
405	        if need_acdc:
406	            print("\n=== Phase A: ACDC ===")
407	            all_scores["acdc"] = run_acdc(model2, dl2, factual_recall_metric, config)
408	            print(f"  acdc: {len(all_scores['acdc'])} edges scored")
409	            with open(acdc_cache, "w") as f:
410	                json.dump(all_scores["acdc"], f)
411	
412	        del model2
413	        gc.collect()
414	        torch.cuda.empty_cache()
415	
416	    # === Phase B: Binarization (all top-100) ===
417	    print("\n=== Phase B: Binarization (all top-100) ===")
418	    method_circuits = {}
419	    for method in config.methods:
420	        method_circuits[method] = binarize_top100(all_scores[method], top_n=config.eap_ig_topn)
421	        print(f"  {method}: {len(method_circuits[method])} edges")
422	
423	    # === Phase B: CSS ===
424	    print("\n=== Phase B: CSS ===")
425	    css_scores = compute_css(method_circuits, K=config.K)
426	    css_dist = css_summary(css_scores, K=config.K)
427	
428	    # === Phase B: CIRCUS ===
429	    print("\n=== Phase B: CIRCUS ===")
430	    union_scores = {}
431	    for method in config.methods:
432	        for edge, score in all_scores[method].items():
433	            if edge not in union_scores:
434	                union_scores[edge] = 0.0
435	            union_scores[edge] = max(union_scores[edge], abs(score))
436	    circus_stability, circus_tiers = run_circus(union_scores, config)
437	
438	    # === Phase C: Cross-tabulation ===
439	    print("\n=== Phase C: Cross-tabulation ===")
440	    table = cross_tabulate(circus_tiers, css_scores, config.css_default_threshold)
441	    print_cross_table(table)
442	    off_diag = compute_off_diagonal(table)
443	
444	    from scipy.stats import beta as beta_dist
445	    n = table.core_total
446	    k = len(table.method_specific)
447	    alpha = 0.05
448	    if n > 0:
449	        ci_low = beta_dist.ppf(alpha / 2, max(k, 0.5), n - k + 1) if k > 0 else 0.0
450	        ci_high = beta_dist.ppf(1 - alpha / 2, k + 1, max(n - k, 0.5)) if k < n else 1.0
451	    else:
452	        ci_low, ci_high = 0.0, 0.0
453	    print(f"Off-diagonal %: {off_diag*100:.1f}%  95% CI: [{ci_low*100:.1f}%, {ci_high*100:.1f}%]")
454	
455	    print("\n--- Pairwise Jaccard Decomposition ---")
456	    pw_jaccard = pairwise_jaccard(method_circuits)
457	    tw_jaccard = three_way_jaccard(method_circuits)
458	    print_pairwise_jaccard(pw_jaccard, tw_jaccard)
459	
460	    # === Phase D: Evaluation (zero + mean ablation) ===
461	    print("\n=== Phase D: Evaluation (zero + mean ablation) ===")
462	    eval_model = load_tl_model(device=device)
463	    eval_tokens = eval_model.to_tokens(eval_prompts, prepend_bos=True)
464	    eval_ans_ids = [lab[0] for lab in eval_labels]
465	    eval_wrong_ids = [lab[1] for lab in eval_labels]
466	
467	    circuits_to_eval = {}
468	    for method, edges in method_circuits.items():
469	        circuits_to_eval[f"method_{method}"] = edges
470	    for thr in config.css_thresholds:
471	        if thr > 0:
472	            circuits_to_eval[f"css_{thr:.2f}"] = threshold_css(css_scores, thr)
473	    tier_sets = get_tier_sets(circus_tiers)
474	    circuits_to_eval["circus_core"] = tier_sets["core"]
475	    circuits_to_eval["stable_core"] = table.stable_core
476	
477	    print("\n--- Zero Ablation ---")
478	    eval_zero = evaluate_all_fr(eval_model, circuits_to_eval, eval_tokens, eval_ans_ids, eval_wrong_ids, ablation="zero")
479	    hdr = f"{'Circuit':<30} {'Edges':>6} {'CPR':>8} {'CMD':>8}"
480	    print(f"\n{hdr}")
481	    print("-" * 54)
482	    for r in sorted(eval_zero, key=lambda x: x["cpr"], reverse=True):
483	        print(f"{r['name']:<30} {r['num_edges']:>6} {r['cpr']:>8.4f} {r['cmd']:>8.4f}")
484	
485	    print("\n--- Mean Ablation ---")
486	    eval_mean = evaluate_all_fr(eval_model, circuits_to_eval, eval_tokens, eval_ans_ids, eval_wrong_ids, ablation="mean")
487	    print(f"\n{hdr}")
488	    print("-" * 54)
489	    for r in sorted(eval_mean, key=lambda x: x["cpr"], reverse=True):
490	        print(f"{r['name']:<30} {r['num_edges']:>6} {r['cpr']:>8.4f} {r['cmd']:>8.4f}")
491	
492	    del eval_model
493	    gc.collect()
494	    torch.cuda.empty_cache()
495	
496	    # === Gate Assessment ===
497	    print("\n" + "=" * 50)
498	    print("FACTUAL RECALL GATE ASSESSMENT")
499	    print("=" * 50)
500	    pct = off_diag * 100
501	    if pct >= 10:
502	        gate_verdict = "PASS_MAIN"
503	        gate_msg = f"Off-diagonal {pct:.1f}% >= 10% -> Main track"
504	    elif pct >= 5:
505	        gate_verdict = "PASS_FINDINGS"
506	        gate_msg = f"Off-diagonal {pct:.1f}% in [5-10%) -> Findings default"
507	    elif pct >= 2:
508	        gate_verdict = "MARGINAL"
509	        gate_msg = f"Off-diagonal {pct:.1f}% in [2-5%) -> Marginal"
510	    else:
511	        gate_verdict = "KILL"
512	        gate_msg = f"Off-diagonal {pct:.1f}% < 2% -> Kill project"
513	    print(f"Off-diagonal %: {pct:.1f}%  95% CI: [{ci_low*100:.1f}%, {ci_high*100:.1f}%]")
514	    print(f"Verdict: {gate_verdict}")
515	    print(f"Action: {gate_msg}")
516	    if n > 0 and n < 30:
517	        print(f"WARNING: CIRCUS-core has only {n} edges (< 30).")
518	
519	    # D032 condition④: check css_1.00 CPR
520	    css_100_edges = threshold_css(css_scores, 1.0)
521	    css_100_zero = [r for r in eval_zero if r["name"] == "css_1.00"]
522	    css_100_mean = [r for r in eval_mean if r["name"] == "css_1.00"]
523	    if css_100_zero:
524	        print(f"\nD032 condition④: css_1.00 CPR(zero)={css_100_zero[0]['cpr']:.4f} edges={css_100_zero[0]['num_edges']}")
525	    if css_100_mean:
526	        print(f"D032 condition④: css_1.00 CPR(mean)={css_100_mean[0]['cpr']:.4f} edges={css_100_mean[0]['num_edges']}")
527	
528	    # Save results
529	    output = {
530	        "config": {"model": config.model_name, "task": "factual_recall", "K": config.K, "methods": config.methods},
531	        "binarization": {m: f"top-{config.eap_ig_topn}" for m in config.methods},
532	        "method_edge_counts": {m: len(edges) for m, edges in method_circuits.items()},
533	        "cross_table": table.summary(),
534	        "core_off_diagonal_pct": off_diag,
535	        "binomial_ci_95": {"low": round(ci_low, 4), "high": round(ci_high, 4)},
536	        "css_distribution": css_dist,
537	        "circus_tier_counts": {t: sum(1 for v in circus_tiers.values() if v == t) for t in ["core", "contingent", "noise"]},
538	        "evaluation_zero": eval_zero,
539	        "evaluation_mean": eval_mean,
540	        "gate_verdict": gate_verdict,
541	        "pairwise_jaccard": {f"{m1}_x_{m2}": {"jaccard": round(j, 4), "intersection": i, "union": u} for m1, m2, j, i, u in pw_jaccard},
542	        "three_way_jaccard": {"jaccard": round(tw_jaccard[0], 4), "intersection": tw_jaccard[1], "union": tw_jaccard[2]},
543	    }
544	
545	    output_path = Path(__file__).parent / "factual_recall_results.json"
546	    with open(output_path, "w") as f:
547	        json.dump(output, f, indent=2)
548	    print(f"\nResults saved to {output_path}")
549	
550	
551	if __name__ == "__main__":
552	    main()
553	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2e9e803-6b1a-4e3c-a0af-64c076884f80",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "04d61248-3651-4b9f-9dc3-466beea427d7",
  "sourceToolAssistantUUID": "a2e9e803-6b1a-4e3c-a0af-64c076884f80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-13T09:56:46.386Z_

I now have a thorough understanding of the paper, experimental infrastructure, decision history, and review context. Let me also check the other dream report versions for comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04d61248-3651-4b9f-9dc3-466beea427d7",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNLD7ir6jf8q7oUx7As",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac84af82-17ad-4b1b-ad3f-ba950b5dc9d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LuSA5QTGJTeT5w9pQgqDJ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10877,
      "cache_read_input_tokens": 68482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10877,
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

_source line 56 · 2026-05-13T09:56:49.061Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A4MYrYCZh7PSKiSsEJs96J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T092135/worst/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac84af82-17ad-4b1b-ad3f-ba950b5dc9d2",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNLD7ir6jf8q7oUx7As",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df27b5b9-56c8-41f4-9c7b-c692bc7ca490",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LuSA5QTGJTeT5w9pQgqDJ3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10877,
      "cache_read_input_tokens": 68482,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10877
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 68482,
          "cache_creation_input_tokens": 10877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10877,
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

_source line 57 · 2026-05-13T09:56:49.067Z_

<details><summary>↩ Tool result · `toolu_01A4MYrYCZh7PSKiSsEJs96J`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{amsmath,amssymb}
6	\usepackage{booktabs}
7	\usepackage{graphicx}
8	\usepackage{hyperref}
9	\usepackage{xcolor}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{natbib}
12	\usepackage{multirow}
13	\usepackage{tablefootnote}
14	
15	\title{Binary Consensus Does Not Improve Circuit Discovery}
16	
17	\author{
18	  Anonymous Authors\\
19	  \textit{Anonymous Institution}
20	}
21	
22	\date{}
23	
24	\begin{document}
25	\maketitle
26	
27	% ============================================================
28	\begin{abstract}
29	Mechanistic interpretability increasingly relies on automated circuit discovery methods, yet different methods often identify divergent circuits for the same task. A natural response is to take the consensus --- edges agreed upon by multiple methods --- as a higher-fidelity circuit. We systematically evaluate this binary consensus strategy (CSS) across 4 tasks on GPT-2 Small and 1 task on Qwen-0.5B, using three discovery methods (EAP-IG, Edge Pruning, ACDC). Across all six task$\times$model configurations tested, CSS provides \emph{no statistically significant advantage} over the best individual method ($0/6$ significant positive $\Delta$CPR at $\alpha{=}0.05$). The sole apparent success (IOI on GPT-2) dissolves under size-controlled baselines: top-$k$ edges from any single method match or exceed CSS performance when circuit size is held constant. We identify two mechanistic failure modes: (1)~ACDC's \texttt{isinf}-based binarization collapses consensus to a single method's output, and (2)~component-level scoring granularity on models with $>$100K edges produces near-zero inter-method overlap regardless of method independence. These findings challenge the implicit assumption that multi-method agreement validates circuit quality, and suggest that the consensus-as-validation paradigm is fundamentally flawed for current circuit discovery methods.
30	\end{abstract}
31	
32	% ============================================================
33	\section{Introduction}
34	
35	Automated circuit discovery aims to identify the minimal subnetwork (circuit) within a neural network that is responsible for a specific behavior \citep{conmy2023towards,wang2023interpretability}. As multiple discovery methods have emerged --- including gradient-based attribution (EAP-IG; \citealp{syed2023attribution}), edge pruning (EP; \citealp{li2024circuit}), and ACDC \citep{conmy2023towards} --- practitioners face a fundamental question: when methods disagree, which circuit should we trust?
36	
37	An intuitive answer is \emph{consensus}: edges identified by multiple independent methods should be more reliable than those found by any single method alone. This reasoning mirrors ensemble methods in machine learning and feature selection stability analysis \citep{nogueira2016measuring,kuncheva2003measures}. In circuit discovery, binary consensus takes the intersection (or super-majority) of binarized circuit outputs from $K$ methods.
38	
39	We call this approach the \textbf{Circuit Selection by Consensus} (CSS) framework and test it systematically. Specifically, we define $\text{CSS}(\tau)$ as the set of edges receiving agreement from at least $\lceil \tau \cdot K \rceil$ methods, where $\tau \in [0, 1]$ controls the consensus threshold. At $\tau{=}1.0$ (unanimous agreement), CSS selects only edges found by all $K$ methods.
40	
41	Our results are unequivocally negative. Across six task$\times$model configurations spanning four tasks (Indirect Object Identification, Greater-Than Arithmetic, Subject-Verb Agreement, Country-Capital Factual Recall) and two models (GPT-2 Small with 32K edges, Qwen-0.5B with 179K edges), CSS at $\tau{=}1.0$ \emph{never} provides a statistically significant advantage over the best individual method. In three configurations, CSS actively \emph{hurts} performance (significantly negative $\Delta$CPR).
42	
43	We identify two distinct mechanistic failure modes that explain this universal failure:
44	
45	\begin{enumerate}
46	    \item \textbf{Binarization pathology} (\S\ref{sec:binarization}): ACDC's \texttt{isinf}-based edge scoring produces an extremely sparse binary mask (7--14 edges out of 32K), causing $\text{CSS}(\tau{=}1.0)$ to degenerate to the ACDC output alone. Consensus becomes a single-method circuit relabeled as ``multi-method agreement.''
47	
48	    \item \textbf{Component-level scoring collapse} (\S\ref{sec:scaling}): On Qwen-0.5B, both IFR and ACDC perform node-level or block-level scoring rather than edge-level discrimination. With 179K candidate edges, this produces layer-concentrated selections with zero inter-method overlap at the edge level, making consensus vacuous.
49	\end{enumerate}
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df27b5b9-56c8-41f4-9c7b-c692bc7ca490",
  "isSidechain": true,
  "promptId": "9fc9d304-eebd-4034-b0bd-b4002ff90522",
  "agentId": "a10e5aef12332efbc",
  "type": "user",
  "uuid": "e2419101-7185-4acf-bb94-1af94832230a",
  "sourceToolAssistantUUID": "df27b5b9-56c8-41f4-9c7b-c692bc7ca490",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-13T09:58:13.981Z_

I have now read the full "best" paper, the "worst" paper framing (for contrast), all project decisions, experimental plans, review context, code implementations, and memory notes. I have enough information for a thorough review.

## R1 Review: Methods & Experiments

### Summary (2-3 sentences)

This paper formalizes binary cross-method consensus (CSS) for circuit discovery and systematically evaluates it across 6 model-task configurations, finding it succeeds in only 1 of 6 cases. The failure analysis identifies three mechanistic failure modes (task-induced method correlation, component-level scoring degeneration, Jaccard-predictable failure) and provides a practical Jaccard-based diagnostic. The work contributes a well-organized negative result with genuine explanatory depth, though several methodological gaps limit confidence in the claimed generality.

### Strengths

- **S1: Rigorous size-controlled baseline (Table 4).** The comparison of CSS=1.0 (7 edges) against top-7 from each individual method and random-7 baselines (50 samples) is well-designed and directly addresses the most obvious confound. The 76.3% retained advantage provides convincing evidence that the IOI success is a genuine selection quality effect, not merely a size artifact. This is the strongest control experiment in the paper.

- **S2: Bootstrap CIs with BCa correction (Table 5).** Using paired bootstrap with BCa correction on per-example CPR differences is the right statistical approach for this setting. The 10,000 bootstrap samples are adequate. Reporting p-values alongside CIs, and noting that SVA's CI crosses zero (p=0.482), demonstrates honest statistical practice. The decision to classify SVA as FAIL based on statistical non-significance rather than on point estimate direction is sound.

- **S3: Ablation method robustness check (Table 9).** Testing zero vs. mean ablation on the sole success case is an important control that the authors correctly identified as necessary. The 81.3% advantage retention under mean ablation rules out the hypothesis that consensus edges benefit disproportionately from the destructive nature of zero ablation. This addresses a real concern about evaluation protocol sensitivity in circuit discovery.

- **S4: Mechanistic failure mode taxonomy.** The three failure modes are distinct, mechanistically grounded, and supported by different evidence. Failure Mode 2 (component-level scoring degeneration) is particularly well-characterized, with the GQA/KV-sharing explanation for IFR and the search space explosion explanation for ACDC providing genuinely informative mechanistic insight. The distinction between correlation-based failure (Claim 4) and degeneration-based failure (Claim 3) is conceptually clean.

- **S5: Honest reporting of the sole diagnostic miss.** Table 8 transparently reports the Qwen ACDC outlier (low Jaccard but FAIL) and provides a clear mechanistic explanation for why the Jaccard diagnostic cannot detect degeneration failures. This is better than artificially excluding the outlier or ignoring the miss.

### Weaknesses

- **W1: The evaluation code reveals node-level ablation, not edge-level ablation.** Reviewing the actual `evaluate_circuit_fr` implementation (and by extension the likely IOI evaluation code), the ablation operates at the **node level** (entire attention heads and MLP layers are zeroed/mean-replaced), not at the edge level. The paper's entire conceptual framework describes edge-level circuits (CSS scores computed over edges, Jaccard computed over edge sets), but the evaluation measures node-level faithfulness. This is a fundamental disconnect: CSS selects edges, but CPR measures the contribution of the **nodes** those edges touch. Two circuits with different edge sets but identical node coverage would produce identical CPR values. This confound is never discussed. The size-controlled baseline (Table 4) partially mitigates this (7 edges from different methods likely cover different nodes), but the paper should explicitly acknowledge and analyze this gap. For the Factual Recall case (Table 2), CSS=1.0 with 10 edges touching a subset of MLP layers vs. EAP-IG with 50 edges touching more layers is really measuring node coverage, not edge selection quality.

- **W2: Binarization sensitivity is underexplored.** The paper uses top-n binarization (n=50 or 100) for commensurability but never varies n to test sensitivity of conclusions. The decisions log (D026) reveals that ACDC's native `isinf` binarization was a major confound that required switching to top-k, and that Jaccard shifts +0.16 to +0.25 when switching binarization strategies. The paper mentions this only briefly in Section 3.2 and does not present a systematic binarization sensitivity analysis. How sensitive is the Jaccard diagnostic (Table 8) to the choice of n? Would n=25 or n=200 change which configurations PASS/FAIL? The paper claims top-n "ensures commensurability" but never demonstrates that conclusions are robust to this choice. At minimum, one sweep (e.g., n in {25, 50, 100, 200}) on IOI should be reported.

- **W3: CPR is defined inconsistently and CMD is underutilized.** Table 1 reports IOI CSS=1.0 CPR=0.109 and best single CPR=0.029 (ACDC), while Table 2 (Factual Recall) reports CPR=0.975 for EAP-IG. The IOI CPR values are very low (0.109 for the "successful" consensus circuit means it recovers only 10.9% of the full model's logit difference). This raises the question: is a circuit with CPR=0.109 actually "faithful"? The paper never discusses what constitutes a practically meaningful CPR level. CMD is defined and reported in Table 2 but absent from the main results table (Table 1) and from all other task analyses. Since CPR and CMD can tell different stories (high CPR does not imply low CMD when baseline performance is low), the selective reporting of CMD is a gap.

- **W4: Multiple testing is not addressed.** Four paired bootstrap tests are conducted on the GPT-2 configurations (Table 5). The IOI result (p=0.002) survives Bonferroni correction (threshold 0.05/4=0.0125), but this is never discussed. With 6 configurations tested and a core claim hinging on 1/6 being significant, the probability of finding at least one significant result by chance under the null hypothesis of no consensus advantage is 1-(1-0.05)^4 = 18.5%. The paper should explicitly address multiplicity, either by applying correction or by arguing why the IOI result's effect size and mechanistic interpretation make it robust to this concern.

- **W5: n=6 is critically underpowered for the Jaccard diagnostic claim.** The paper acknowledges this but still devotes considerable space to Claim 4 (Jaccard as diagnostic predictor), including Spearman correlation (rho=-0.90, p=0.037 excluding outlier). With 5 data points and one excluded, any monotone relationship will produce a high absolute rho. The GPT-2-only rho=-1.0 with 4 points is trivially achievable (any 4 points in strictly monotone order yield rho=-1.0). The thresholds (0.35, 0.50) are derived from the same data they are evaluated on, creating a look-elsewhere effect. The paper frames this as a "heuristic" rather than a "proven law," which is appropriate, but the statistical analysis presented (Spearman, p-values) overstates the evidence relative to the sample size.

- **W6: Only two models tested, both small-scale.** GPT-2 Small (124M) and Qwen-0.5B (500M) are both small by current standards. The scaling failure (Failure Mode 2) is attributed to architectural features (GQA, large edge count), but both could be specific to the 179K-edge regime. Models at 7B+ scale would have millions of edges, and the failure modes may manifest differently. The paper's practical guidelines ("verify scoring granularity before computing consensus") are difficult to validate without testing at least one model in the 2B-7B range.

### Questions for Authors

- **Q1:** The evaluation code implements node-level ablation (zeroing/replacing entire attention heads and MLP layers), not edge-level ablation. How does this affect your conclusions? Specifically, for the IOI size-controlled comparison (Table 4), did you verify that the 7 CSS=1.0 edges and the top-7 EAP-IG edges cover different sets of nodes, so that the CPR difference is not purely driven by node identity?

- **Q2:** How sensitive are the results (particularly the PASS/FAIL classification in Table 1) to the choice of top-n for binarization? You note that ACDC's isinf binarization was pathological, but do not report what happens at n=25, 75, or 200 for the top-n case. Could IOI become FAIL at n=200 (more edges, higher Jaccard) or Factual Recall become PASS at n=25 (fewer edges, more selective)?

- **Q3:** The Factual Recall experiment uses only 22 country-capital pairs (line 54-63 of the code), generating 500 prompts by sampling different wrong-answer pairings. How robust is the CPR evaluation to this small knowledge base? Many of these pairs involve well-known European capitals; would results differ with a more diverse or larger set?

- **Q4:** What is the wall-clock cost of running all three methods for each configuration? The paper argues practitioners should "compute pairwise Jaccard before investing in multi-method validation," but does not quantify the baseline cost of the multi-method approach that practitioners would be saving.

- **Q5:** For the Bootstrap CIs, were the per-example CPR values computed (i.e., CPR per individual prompt, then bootstrapped), or were the bootstrap samples taken at the prompt level with CPR recomputed over each bootstrap sample? The distinction matters for variance estimation with heterogeneous prompt difficulty.

### Minor Issues

- Table 1: SVA and Arithmetic rows show "---" for CSS=1.0 Edges and CSS CPR, but both configurations have CSS=1.0 edges (the text discusses them). The table should report these values or clarify why they are omitted.
- Table 1: The Delta column for IOI is +0.085 but the size-controlled analysis gives Delta=0.061. The paper should clarify that Table 1's Delta is not size-controlled.
- Section 2: EP is cited as Kramar et al. but described as "gradient-weighted edge pruning." The actual AtP* method (Kramar et al. 2024) uses attribution patching at the edge level. The description should be more precise about the distinction between EP as implemented (mask gradient / L0) and the cited method.
- Table 9: The zero ablation Delta is +0.080 but Table 1 reports +0.085. This inconsistency (likely from different baselines: ACDC-14 vs ACDC-100) should be reconciled or explained.
- The paper omits any discussion of computational cost or efficiency of the three methods, which is relevant for the practical guidelines.
- Equation 1: CSS is defined over K methods but the paper uses K=3 throughout. State whether the framework is designed for arbitrary K or specifically for K=3.
- "Istanbul" as the capital of Turkey (line 62 in code, used in Factual Recall dataset) is factually incorrect; the capital is Ankara. This affects data quality of the Factual Recall experiment.

### Scores

- Soundness: 3.0/5
- Excitement: 3.0/5
- Overall: 3.0/5
- Reproducibility: 3.0/5
- Confidence: 4.0/5

**Justification:** The paper presents a well-organized systematic negative result with genuine mechanistic insight into why cross-method consensus fails. However, the fundamental disconnect between edge-level CSS computation and node-level evaluation (W1) undermines the paper's central claim about edge selection quality. The binarization sensitivity gap (W2) means we cannot be confident the PASS/FAIL classification is robust to a key design choice. The Jaccard diagnostic, while intuitively appealing, is built on 5-6 data points with in-sample threshold derivation (W5). The statistical analysis is competent but does not address multiplicity (W4). Overall, this is an interesting Findings-level contribution that would benefit from addressing the edge-vs-node evaluation mismatch and demonstrating binarization robustness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2419101-7185-4acf-bb94-1af94832230a",
  "isSidechain": true,
  "agentId": "a10e5aef12332efbc",
  "requestId": "req_011CazNLg4Tc5mnfhdV2trZ3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c782d06-fa28-48bb-9c74-bd7bf9475463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context",
  "sessionId": "d5948ce3-0bd6-4774-9a29-31d903f57111",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcB2sXotoyHu3j51syqyse",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1509,
      "cache_read_input_tokens": 79359,
      "output_tokens": 2994,
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
          "output_tokens": 2994,
          "cache_read_input_tokens": 79359,
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
