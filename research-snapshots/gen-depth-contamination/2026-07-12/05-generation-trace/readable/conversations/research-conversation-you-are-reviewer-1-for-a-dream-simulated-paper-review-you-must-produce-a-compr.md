# Research conversation: You are Reviewer 1 for a Dream (simulated) paper review. You must produce a comprehensive review covering method+experim

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 68
- **Recorded user turns:** 1
- **Tool calls:** 28
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aea58d8549abcc920.jsonl`
- **Structured JSON:** [`5b29827dce91fcbce5eb.json`](../../sessions/5b/5b29827dce91fcbce5eb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

68 recorded events

### User

_source line 1 · 2026-05-18T12:09:24.060Z_

You are Reviewer 1 for a Dream (simulated) paper review. You must produce a comprehensive review covering method+experiments, novelty+related work, and overall judgment.

## Paper Summary

**Title:** "Bounded Depth Discrimination in Recursive Synthetic Text: Domain-Dependent Saturation at K* ≤ 3"

**Core idea:** Formalizes recursive text generation as an iterated lossy channel, introduces K* (generational discrimination boundary beyond which adjacent depths become statistically indistinguishable). Measures K* empirically across 8 model configs (5 architecture families, 1B-8B), 3 domains, 4 decoding strategies.

**Key findings:**
- K* ∈ {1,2,3} with domain hierarchy: Wikipedia(1) < C4(2) < arXiv(3)
- Domain structural complexity is the sole systematic determinant
- Cross-model transfer retains 80-92% accuracy; feature ordering scorer-invariant (ρ>0.90)
- K*-aware binary filtering outperforms graduated weighting and DSIR on downstream benchmarks

**Method:**
- 15D model-free feature vector (lexical diversity, syntactic complexity, info-theoretic, distributional)
- LightGBM classifiers with bootstrap 95% CI, 5-fold CV
- K* = max{k : AUC_CI-lower(k vs k+1) > θ=0.60}
- θ=0.60 corresponds to Cohen's h ≈ 0.20 (small effect size)

**Sections:**
1. Introduction - problem framing, contributions
2. Related Work - model collapse, MG text detection, data selection
3. Theoretical Framework - DPI proof of finite K*, operational definition, 15D features
4. Experimental Setup - generation pipeline, evaluation protocol
5. Results: K* Characterization
   - 5.1 C4: K*=2 dominant (7/8 configs), Table 1
   - 5.2 Domain hierarchy (Table 3): Wiki(1)<C4(2)<arXiv(3)
   - 5.3 Mistral dissociation: K*=1 on C4, K*=3 on arXiv
   - 5.4 Cross-model transfer (80-92%), cross-scorer (11/12 yield K*=2 on C4)
   - 5.5 Neural probe comparison (model-dependent K*)
   - 5.6 Generation mode analysis (rewrite vs continuation)
6. K*-Aware Data Curation
   - Binary filtering best on HellaSwag (p≤0.004), MMLU Δ=0.76pp (p=0.074 not significant)
7. Additional Analyses
   - 7.1 Common Crawl validation (no ground truth): AlignScore ρ=-0.274, within-synthetic ρ=-0.118
   - 7.2 Power analysis: Qwen-cont marginal (CI lower=0.6015, exceeds θ by 0.0015), 80% power needs n≈2200
   - 7.3 Prompt-chain vs retrain-chain: retrain yields K*≥4

**References:** Only 7 references total.

## Experiment Design Reference (from review_context.yaml)

The design includes two planned experiments:
1. **exp-014: Naturalistic Common Crawl Validation** — Apply classifier to CC 2025/2026, correlate predicted depth with AlignScore, TTR, hapax, Yule's K. No ground truth. Results: AlignScore ρ=-0.274 (all), ρ=-0.118 (within-synthetic). Binary detection F1=0.68. This IS in the paper (Section 7.1).
2. **exp-028: Subsampling Power Curve** — Bootstrap resampling at n∈{1000-5000} for Qwen-cont. Results: 80% power at n≈2200, 90% at n≈2800. This IS in the paper (Section 7.2).

Both planned experiments are present in the paper. The paper covers them adequately.

## Review Instructions

Cover these three dimensions:

**A. Method & Experiments**
- Are methods described completely? Are claims supported by experimental data?
- Does experimental design cover key baselines / ablations / cross-dataset comparisons?
- Can a reviewer reproduce conclusions from the data presentation (tables/figures)?

**B. Novelty & Related Work**
- Is differentiation from existing work clear? Is literature coverage sufficient?
- Is the narrative logically self-consistent?

**C. Overall Judgment**
- Judge independently based on paper content
- Explicitly flag any contradictions between claims and experimental results
- Use 6-point scale: 1=Strong Reject, 2=Reject, 3=Borderline Reject, 4=Borderline Accept/Weak Accept, 5=Accept, 6=Strong Accept
- Top ML venue standard (~25% acceptance rate)

**DO NOT judge:** formatting, typesetting, reference style, word count. This is a Dream (simulated) paper.

**Tag each weakness** as either **[idea-level]** or **[presentation-level]**.

**Scoring calibration:**
- 3+ Major issues → no higher than Borderline Reject
- 2 Major issues → no higher than Weak Accept
- 1 Major issue → no higher than Accept
- 0 Major issues → may give Strong Accept
- Each Major issue needs explicit justification for why it's Major not Minor.

**Output format:**

```
## Summary
[2-3 sentences]

## Strengths
[Bulleted list]

## Weaknesses
[Bulleted, each tagged [idea-level] or [presentation-level], each marked Major/Minor with justification]

## Questions for Authors
[Bulleted]

## Missing Experiments / Analyses
[What would strengthen the paper]

## Overall Assessment
Score: X/6
Confidence: {low, medium, high}
Recommendation: {Strong Reject / Reject / Borderline Reject / Weak Accept / Accept / Strong Accept}
[2-3 sentence justification]
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "4f363f5e-8e53-4d55-900f-c5c553d56acf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T12:09:24.073Z_

```json
{
  "parentUuid": "4f363f5e-8e53-4d55-900f-c5c553d56acf",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
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
  "uuid": "e558195d-efba-4871-ac9f-943dc181fbaf",
  "timestamp": "2026-05-18T12:09:24.073Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T12:09:32.129Z_



I'll start by reading the paper and all related project files to produce a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e558195d-efba-4871-ac9f-943dc181fbaf",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1Ve9i13Q2tQjYJSdxh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb4509f7-328e-4f69-933e-4a2ebcfb2bdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAMC8E2i3PzmeSLCUMUjM6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16809,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16809,
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

_source line 4 · 2026-05-18T12:09:32.592Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Qp8d3naeStuWYe4KKycRaq`</summary>

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
  "parentUuid": "eb4509f7-328e-4f69-933e-4a2ebcfb2bdb",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1Ve9i13Q2tQjYJSdxh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7caf1fb5-e054-41c0-9ab0-afdb8d87f693",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAMC8E2i3PzmeSLCUMUjM6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16809,
      "cache_read_input_tokens": 0,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16809
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 125,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16809,
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

_source line 5 · 2026-05-18T12:09:32.595Z_

<details><summary>↩ Tool result · `toolu_01Qp8d3naeStuWYe4KKycRaq`</summary>

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
  "parentUuid": "7caf1fb5-e054-41c0-9ab0-afdb8d87f693",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "12304ca8-72b9-41c5-991b-549dfdf7871d",
  "sourceToolAssistantUUID": "7caf1fb5-e054-41c0-9ab0-afdb8d87f693",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T12:09:36.188Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01PCL3eAbXxfFfPAWMX3kQ8r`</summary>

```json
{
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12304ca8-72b9-41c5-991b-549dfdf7871d",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1WGwHRB1RuXpbGwmTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0baae4ce-7987-4ae5-b0dc-03f25755b772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXCWSLH7v4B42anxi46uSw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 7 · 2026-05-18T12:09:36.508Z_

<details><summary>↩ Tool result · `toolu_01PCL3eAbXxfFfPAWMX3kQ8r`</summary>

```text
{"result":"# 项目 gen-depth-contamination 概况\n\n## 实验状态 (69 个)\n\n- **exp_016_base_vs_instruct**: DONE (success) — \n- **exp_003_decoding_ablation**: DONE (success) — \n- **exp_004_7b_crossscale**: DONE (success) — \n- **exp_E_paired_stats**: DONE (success) — \n- **exp_D_obd_n500**: DONE (success) — \n- **exp_B_14d_ablation**: DONE (success) — \n- **exp_A_alt_scorer**: DONE (success) — \n- **exp_015_neural_probe**: DONE (success) — \n- **exp_006_graduated_filtering**: DONE (success) — \n- **exp_007_bootstrap_ci**: DONE (success) — \n- **exp_011_llm_zeroshot**: DONE (success) — \n- **exp_013_cross_transfer**: DONE (success) — \n- **exp_010_ordinal_baseline**: DONE (success) — \n- **exp_001_pythia_depth**: DONE (success) — \n- **mvp_pilot_sat_v1**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_32b_c4 | Scale-dependent K* on C4: Qwen2.5-32B fp16 continuation on C4 web text 的 K* 是否仍 = 2？验证 K*=2 dominant mode 在 32B scale 是否稳定（已确认 1.5B/7B/8B/14B 均 K*=2），排除 scale ceiling effect。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B. | — | — | — |\n\n## 待处理\n- exp_008_retrain_chain: Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32) retrain-chain K* ≤ prompt-chain K*=2. 每代独立 LoRA fine-tune 1 epoch on 前代输出，再用 fine-tuned model 生成下一代。验证 prompt-chain 是 conservative upper bound。C4 5K docs, depth 0-4, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.（准备中）\n\n## 近期结论\n- **exp_026_arxiv_filtering** (negative): Graduated depth weighting (α=0.9^d) on arXiv depth chains will outperform both no-filter and binary-cut baselines on downstream benchmarks (MMLU, HellaSwag), because it preserves useful signal from deeper generations while down-weighting accumulated contamination, rather than discarding data entirely. ← 基于 exp_006_graduated_filtering\n- **exp_027_latex_ablation** (success): arXiv K*=3 不依赖 LaTeX 格式特征。去除 LaTeX markup 后重新提取 15D features 并跑 pairwise classification，K* 应仍=3，排除 LaTeX 语法作为 confound。 ← 基于 exp_024_arxiv_depth_chain\n  [exp027_latex_ablation_results](/api/workspace-files/projects/gen-depth-contamination/artifacts/exp_027_latex_ablation/report/exp027_comparison.md)\n- **exp_025_pythia_filtering** (negative): Filtering strategy ordering (binary > graduated > no-filter) 在 Pythia-1.4B 上与 Qwen 一致，验证 K*=2 对 curation 策略选择的跨模型预测价值。Pythia-1.4B LoRA rank=8 continued pretraining on C4 depth chain, 3 strategies × 3 seeds, eval MMLU+HellaSwag. ← 基于 exp_006_graduated_filtering\n\n## 趋势\n成功 49 / 负向 9 / 失败 9 / 共 67\nk_star: 3 →（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\ncqa1-22115: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\nwestd-42896: 无 GPU 信息\n\n## 告警\n- exp-008-retrain-chain: 训练失败 — unknown\n- exp_009_dose_10pct: 训练失败 — unknown\n- exp_009_dose_30pct: 训练失败 — unknown\n- exp_009_dose_50pct: 训练失败 — unknown\n- exp_009_dose_10pct_v2: 训练失败 — unknown\n- exp_009_dose_30pct_v2: 训练失败 — unknown\n- exp_009_dose_50pct_v2: 训练失败 — unknown\n- exp_wiki_pythia: 训练失败 — unknown\n- exp_wiki_olmo: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0baae4ce-7987-4ae5-b0dc-03f25755b772",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "a5eb7c07-b63f-4264-a059-b7d46fec95fb",
  "sourceToolAssistantUUID": "0baae4ce-7987-4ae5-b0dc-03f25755b772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T12:09:36.722Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FBqzQmiJExu7FYv7AbTYSH`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5eb7c07-b63f-4264-a059-b7d46fec95fb",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1WGwHRB1RuXpbGwmTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79ca6c9e-7403-468f-8e5e-7d5ede5657f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXCWSLH7v4B42anxi46uSw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16809,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 162,
          "cache_read_input_tokens": 16809,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1447,
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

_source line 9 · 2026-05-18T12:09:36.737Z_

<details><summary>↩ Tool result · `toolu_01FBqzQmiJExu7FYv7AbTYSH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/report.md\", \"content\": \"# Handover — 2026-05-18\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_32b_c4 | Scale-dependent K* on C4: Qwen2.5-32B fp16 continuation on C4 web text 的 K* 是否仍 = 2？验证 K*=2 dominant mode 在 32B scale 是否稳定（已确认 1.5B/7B/8B/14B 均 K*=2），排除 scale ceiling effect。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B. | — | — | — |\\n\\n## 待处理\\n- exp_008_retrain_chain: Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32) retrain-chain K* ≤ prompt-chain K*=2. 每代独立 LoRA fine-tune 1 epoch on 前代输出，再用 fine-tuned model 生成下一代。验证 prompt-chain 是 conservative upper bound。C4 5K docs, depth 0-4, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.（准备中）\\n\\n## 近期结论\\n- **exp_026_arxiv_filtering** (negative): Graduated depth weighting (α=0.9^d) on arXiv depth chains will outperform both no-filter and binary-cut baselines on downstream benchmarks (MMLU, HellaSwag), because it preserves useful signal from deeper generations while down-weighting accumulated contamination, rather than discarding data entirely. ← 基于 exp_006_graduated_filtering\\n- **exp_027_latex_ablation** (success): arXiv K*=3 不依赖 LaTeX 格式特征。去除 LaTeX markup 后重新提取 15D features 并跑 pairwise classification，K* 应仍=3，排除 LaTeX 语法作为 confound。 ← 基于 exp_024_arxiv_depth_chain\\n  [exp027_latex_ablation_results](/api/workspace-files/projects/gen-depth-contamination/artifacts/exp_027_latex_ablation/report/exp027_comparison.md)\\n- **exp_025_pythia_filtering** (negative): Filtering strategy ordering (binary > graduated > no-filter) 在 Pythia-1.4B 上与 Qwen 一致，验证 K*=2 对 curation 策略选择的跨模型预测价值。Pythia-1.4B LoRA rank=8 continued pretraining on C4 depth chain, 3 strategies × 3 seeds, eval MMLU+HellaSwag. ← 基于 exp_006_graduated_filtering\\n\\n## 趋势\\n成功 49 / 负向 9 / 失败 9 / 共 67\\nk_star: 3 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-22115: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\nwestd-42896: 无 GPU 信息\\n\\n## 告警\\n- exp-008-retrain-chain: 训练失败 — unknown\\n- exp_009_dose_10pct: 训练失败 — unknown\\n- exp_009_dose_30pct: 训练失败 — unknown\\n- exp_009_dose_50pct: 训练失败 — unknown\\n- exp_009_dose_10pct_v2: 训练失败 — unknown\\n- exp_009_dose_30pct_v2: 训练失败 — unknown\\n- exp_009_dose_50pct_v2: 训练失败 — unknown\\n- exp_wiki_pythia: 训练失败 — unknown\\n- exp_wiki_olmo: 训练失败 — unknown\\n\", \"total_chars\": 2279, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79ca6c9e-7403-468f-8e5e-7d5ede5657f3",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "c86b8ddc-1d99-4b48-b656-49baaa8f9193",
  "sourceToolAssistantUUID": "79ca6c9e-7403-468f-8e5e-7d5ede5657f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T12:09:41.079Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015wRq8BhWG3K1RLRzAcsCpm`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c86b8ddc-1d99-4b48-b656-49baaa8f9193",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1WaTjLKVn3x4FwE92t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4128eb6c-b254-4334-b0e7-b484d838f689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QqNvyeYG1v7ErxPLy5Bk4Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2981,
      "cache_read_input_tokens": 18256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2981,
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

_source line 11 · 2026-05-18T12:09:41.090Z_

<details><summary>↩ Tool result · `toolu_015wRq8BhWG3K1RLRzAcsCpm`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4128eb6c-b254-4334-b0e7-b484d838f689",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "a39658a9-e1fc-4cb4-abd7-e17b09ebbd14",
  "sourceToolAssistantUUID": "4128eb6c-b254-4334-b0e7-b484d838f689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T12:09:42.009Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Q2tbeEkvgYKsCMXhBXhG2P`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a39658a9-e1fc-4cb4-abd7-e17b09ebbd14",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1WaTjLKVn3x4FwE92t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f16211e-b46b-4ac0-b48d-9bc73bc5d984",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QqNvyeYG1v7ErxPLy5Bk4Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2981,
      "cache_read_input_tokens": 18256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2981,
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

_source line 13 · 2026-05-18T12:09:42.022Z_

<details><summary>↩ Tool result · `toolu_01Q2tbeEkvgYKsCMXhBXhG2P`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/literature_map.yaml\", \"content\": \"papers:\\n  # === Must-Cite ===\\n\\n  - id: drayson2025\\n    title: \\\"Machine-generated text detection prevents language model collapse\\\"\\n    authors: \\\"Drayson, Yilmaz, Lampos\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n    code: \\\"https://github.com/GeorgeDrayson/model_collapse\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Binary MGT detection + importance resampling for collapse prevention; our depth estimator generalizes their binary detector to ordinal depth\\\"\\n    cited: false\\n    methodology: >\\n      Binary MGT detector (encoder-only transformer + classification head; best: ModernBERT-150M, AUC .986 in-dist, .943 OOD).\\n      Fine-tuned 5 epochs with label smoothing α=0.1 + temperature scaling.\\n      Sampling Importance Resampling (SIR): w_j = (1-q(x_j))^b / Σ(1-q(x_l))^b, where q(x) = P(machine-generated), b≥1 bias term.\\n      Resample at k=1.5 (50% upsampling). Evaluated on GPT-2 and SmolLM2 (124M–1.7B).\\n    key_findings:\\n      - \\\"SIR filtering not only prevents collapse but improves over human-only training (perplexity -0.85% to -25.65%, diversity +3.44% to +14.62%, MAUVE +8.46% to +20.92%)\\\"\\n      - \\\"ModernBERT achieves best detection (AUC .986 in-dist); optimal threshold 0.8674 on imbalanced data (29% human)\\\"\\n      - \\\"Curated synthetic data has positive value — outperforms oracle (perfect filter) in equal-ratio settings\\\"\\n      - \\\"Only evaluates fine-tuning (not pretraining), models ≤2B, open-ended generation only\\\"\\n    positioning_notes: >\\n      Closest prior work. Their SIR is a special case of our graduated filtering when K*=1 (binary: human vs all synthetic).\\n      We generalize binary→ordinal: estimate depth d∈{0,1,...,K*} and apply depth-graduated weights.\\n      K* tells when ordinal signal adds value over binary. They never discuss ordinal depth or multi-class estimation.\\n      Our C3 claim directly extends their framework: \\\"even coarse 3-class signal yields better calibration at decision boundaries.\\\"\\n\\n  - id: schaeffer2025position\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: \\\"Schaeffer, Kazdan, Arulandu, Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2503.03150\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"framing-critical\\\"\\n    relevance: \\\"Identifies 8 definitions of model collapse across 3 families; forces us to position K* as discriminability saturation (distribution deformation), not test-loss collapse\\\"\\n    cited: false\\n    methodology: >\\n      Position paper. Surveys model collapse literature and identifies 8 distinct definitions organized in 3 families.\\n      Evaluates each definition against realistic deployment conditions. No experiments—purely analytical/argumentative.\\n    key_findings:\\n      - \\\"8 definitions in 3 families: (A) Population risk degrading [D1: catastrophic increase, D2: any increase, D3: asymptotic divergence]; (B) Distributions deforming [D4: collapsing variance, D5: scaling law change, D6: mode disappearance/entanglement, D7: tail data loss]; (C) Spurious generation [D8: hallucinated data]\\\"\\n      - \\\"Under realistic conditions (data accumulation, growing compute), catastrophic risk divergence (D1-D3) is avoidable\\\"\\n      - \\\"Real harms—tail data loss (D7) and mode entanglement (D6)—have received disproportionately less attention\\\"\\n      - \\\"Recommends researchers explicitly state which definition they study\\\"\\n    positioning_notes: >\\n      K* belongs to Family B (distributions deforming), specifically D4 (collapsing variance) + D6 (mode entanglement).\\n      K* measures when distribution deformation renders generations indistinguishable in feature space.\\n      K* is NOT about population risk (Family A). This distinction is critical for framing:\\n      we contribute a diagnostic for exactly the harms Schaeffer et al. identify as underexplored.\\n      Adopt their taxonomy explicitly in Related Work to anchor K* precisely.\\n\\n  - id: kazdan2025collapse\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: \\\"Kazdan, Schaeffer, Dey, Gerstgrasser, Rafailov, Donoho, Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2410.16713\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Accumulate vs replace regimes affect contamination dynamics; in accumulate regime K* may shift upward\\\"\\n    cited: false\\n    methodology: >\\n      Formal comparison of 3 data regimes: Replace (train on latest synthetic only; Σ→0 a.s.),\\n      Accumulate (train on all historical data; real fraction→0 but stability holds),\\n      Accumulate-subsample (fixed budget from accumulated pool; intermediate degradation).\\n      Theory: Gaussian setting with closed-form limits. Experiments: multivariate Gaussian, KDE, LLM SFT (Gemma2-2B on HelpSteer2/TinyStories).\\n    key_findings:\\n      - \\\"Replace: covariance collapses to 0 (a.s.), W2 diverges. Collapse inevitable within 5-10 iterations\\\"\\n      - \\\"Accumulate: covariance stabilizes at σ₀²·sin(π/√n)/(π/√n). No collapse even as real data fraction→0\\\"\\n      - \\\"Accumulate-subsample: degradation plateaus rather than diverges\\\"\\n      - \\\"Cardinality of real data matters more than proportion (R²=0.59 vs 0.34)\\\"\\n    positioning_notes: >\\n      Our prompt-chain = replace regime (harshest setting). K*=2 measured under replace conditions.\\n      This makes K*=2 a conservative lower bound: under accumulate regime (more realistic), K* would shift upward.\\n      Strengthens our result: if depth estimation adds value at K*=2 under replace, it adds more under accumulate.\\n      Cite to justify experimental design and contextualize K* as regime-dependent.\\n\\n  - id: shi2025generalization\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: \\\"Shi, Wu, Zhang, Zhang, Tao, Qu\\\"\\n    venue: \\\"NeurIPS 2025 Spotlight\\\"\\n    url: \\\"https://arxiv.org/abs/2509.16499\\\"\\n    code: \\\"https://shilianghe007.github.io/model-collapse/\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Generalization-to-memorization transition in iterative retraining parallels our feature-space convergence; entropy decrease over iterations aligns with our depth-discriminative features\\\"\\n    cited: false\\n    methodology: >\\n      Study iterative retraining of diffusion models (DDPM) on CIFAR-10 subsets (1K–32K images).\\n      Generalization Score (GS): avg distance between generated and nearest training image.\\n      Entropy: Kozachenko-Leonenko estimator. Strong correlation: Pearson r=0.91 between entropy and log(GS).\\n      Mitigation: entropy-based data selection (greedy max-NN-distance + threshold-decay filter).\\n    key_findings:\\n      - \\\"GS drops approximately exponentially across iterations; collapse within 5-10 iterations for large datasets\\\"\\n      - \\\"Training data entropy is a direct predictor of generalization capability (r=0.91)\\\"\\n      - \\\"Entropy-based data selection mitigates memorization transition\\\"\\n      - \\\"Diffusion models only; no LLM experiments. No theoretical analysis of WHY entropy collapses\\\"\\n      - \\\"Generated images form tight local clusters while overall variance remains relatively stable\\\"\\n    positioning_notes: >\\n      Parallel phenomenon across modalities: their entropy decline ↔ our JSD decrease (0.27→0.004).\\n      Their \\\"GS drops exponentially\\\" ↔ our feature-space divergence vanishes rapidly → K*=2.\\n      Key distinction: they measure output-distribution entropy; we measure discriminability in feature space.\\n      K* complements their entropy metric: operationalizes \\\"at what depth does entropy decline = indistinguishability?\\\"\\n      Their clustering-while-variance-stable parallels our depth features converging before global statistics.\\n      Cite for cross-modal validation of convergence phenomenon.\\n\\n  # === Should-Cite ===\\n\\n  - id: basani2026diveye\\n    title: \\\"DivEye: Diversity Boosts AI-Generated Text Detection\\\"\\n    authors: \\\"Basani, Chen\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2509.18880\\\"\\n    code: \\\"https://github.com/IBM/diveye\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Surprisal diversity features as potential baseline for depth estimation; zero-shot detector outperforms prior work by 33.2%\\\"\\n    cited: false\\n\\n  - id: amin2025escaping\\n    title: \\\"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\\\"\\n    authors: \\\"Amin et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2502.08924\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Boosting-inspired framework showing weak signal suffices for iterative training; motivates practical utility of imperfect depth estimators\\\"\\n    cited: false\\n\\n  - id: zawalski2026codec\\n    title: \\\"CoDeC: Detecting Data Contamination in LLMs via In-Context Learning\\\"\\n    authors: \\\"Zawalski et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2510.27055\\\"\\n    category: \\\"contamination\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Binary contamination detection via ICL confidence shifts; complementary to our finer-grained depth estimation approach\\\"\\n    cited: false\\n\\n  - id: gambetta2025surplexity\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse\\\"\\n    authors: \\\"Gambetta et al.\\\"\\n    venue: \\\"arXiv preprint 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2410.12341\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Surprise-based collapse metric; surplexity scores as potential feature for depth estimation pipeline and baseline comparison\\\"\\n    cited: false\\n\\n  - id: zhang2024minkpp\\n    title: \\\"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\\\"\\n    authors: \\\"Zhang, Zheng, Gao, Miao\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Binary detection baseline; does not distinguish generational depth\\\"\\n    cited: false\\n\\n  - id: shumailov2024collapse\\n    title: \\\"AI models collapse when trained on recursively generated data\\\"\\n    authors: \\\"Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal\\\"\\n    venue: \\\"Nature 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Seminal model collapse result; describes macro phenomenon but provides no detection tool for depth\\\"\\n    cited: false\\n\\n  - id: alemohammad2024selfconsuming\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Alemohammad, Casco-Rodriguez, Luber, Babaei, Letizia, Bastani, Baraniuk\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Theoretical and empirical analysis of iterative generative training; complements Shumailov with formal convergence analysis\\\"\\n    cited: false\\n\\n  - id: dohmatob2024model\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: \\\"Dohmatob, Feng, Yang, Charton, Kempe\\\"\\n    venue: \\\"ICML 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Scaling law perspective on collapse; tail distribution loss aligns with our observed feature convergence\\\"\\n    cited: false\\n\\n  - id: xie2023dsir\\n    title: \\\"Data Selection with Importance Resampling\\\"\\n    authors: \\\"Xie, Santurkar, Ma, Liang\\\"\\n    venue: \\\"ICML 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Distribution-matching data selection baseline; does not estimate recursive depth\\\"\\n    cited: false\\n\\n  - id: tirumala2024d4\\n    title: \\\"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\\\"\\n    authors: \\\"Tirumala, Markosyan, Zettlemoyer, Aghajanyan\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Deduplication + diversification baseline for data curation; orthogonal to depth-based filtering\\\"\\n    cited: false\\n\\n  - id: xie2024doremi\\n    title: \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\"\\n    authors: \\\"Xie, Pham, Dong, Du, Liu, Lu, Liang, Le, Ma, Yu\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Domain reweighting for pretraining; does not consider generational depth dimension\\\"\\n    cited: false\\n\\n  - id: kirchenbauer2023watermark\\n    title: \\\"A Watermark for Large Language Models\\\"\\n    authors: \\\"Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein\\\"\\n    venue: \\\"ICML 2023\\\"\\n    category: \\\"watermarking\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Provenance tracking via watermarking; complementary approach to depth estimation when watermarks are available\\\"\\n    cited: false\\n\\n  - id: zellers2019grover\\n    title: \\\"Defending Against Neural Fake News\\\"\\n    authors: \\\"Zellers, Holtzman, Rashkin, Bisk, Farhadi, Roesner, Choi\\\"\\n    venue: \\\"NeurIPS 2019\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Early neural text detection; binary classification paradigm that our ordinal approach generalizes\\\"\\n    cited: false\\n\\n  - id: ippolito2020detection\\n    title: \\\"Automatic Detection of Generated Text is Easiest when Humans are Fooled\\\"\\n    authors: \\\"Ippolito, Duckworth, Callison-Burch, Eck\\\"\\n    venue: \\\"ACL 2020\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Binary detection difficulty analysis; does not consider multi-generational depth\\\"\\n    cited: false\\n\\n  # === New additions (scan 2026-04-28 to 2026-05-14) ===\\n\\n  - id: falahati2026curated\\n    title: \\\"Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences\\\"\\n    authors: \\\"Falahati, Amiri, Larson, Golab\\\"\\n    venue: \\\"arXiv preprint 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2605.07724\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Proves pluralistic reward-based curation prevents collapse via Nash bargaining convergence; directly relevant to our graduated filtering—multi-reward curation is orthogonal to depth-based curation, potentially complementary\\\"\\n    cited: false\\n    date_found: \\\"2026-05-14\\\"\\n    positioning_notes: >\\n      Shows that curation strategy matters for collapse prevention: single-reward collapses, multi-reward stabilizes.\\n      Our depth estimator provides a different curation axis: instead of multiple rewards, we use generational depth.\\n      Potential synergy: combine their pluralistic rewards with our depth signal for even stronger filtering.\\n      Does NOT address generational depth or K*. No direct challenge to K*=2.\\n\\n  - id: mady2026feataugmented\\n    title: \\\"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\\\"\\n    authors: \\\"Mady, Reschke, Schuller\\\"\\n    venue: \\\"arXiv preprint 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2605.03969\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Attention-based linguistic feature fusion for cross-domain/cross-generator binary detection; DeBERTa-v3-base+FeatAttn achieves 85.9% balanced accuracy under distribution shift on M4. Feature augmentation architecture applicable to depth estimation pipeline\\\"\\n    cited: false\\n    date_found: \\\"2026-05-14\\\"\\n    positioning_notes: >\\n      Binary detector (human vs AI) with strong cross-generator generalization via feature augmentation.\\n      Their FeatAttn module could be adapted for our ordinal depth classifier—fuse linguistic features with encoder representations.\\n      Key limitation: binary only, no depth awareness. In-domain 99.5% but brittle under shift.\\n      Our K* result implies even perfect binary detection hits diminishing returns past depth 2.\\n\\n  - id: pu2026generator\\n    title: \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\"\\n    authors: \\\"Pu, Cheng, Yuan, Wu, Bi\\\"\\n    venue: \\\"arXiv preprint 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2604.13692\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Generator-agnostic detection via disentangled representations (dual-bottleneck + cross-view regularization); up to 24.2% accuracy gain on MAGE benchmark (20 LLMs). Disentanglement of semantic vs generator artifacts is architecturally relevant for our depth estimator\\\"\\n    cited: false\\n    date_found: \\\"2026-05-14\\\"\\n    positioning_notes: >\\n      Key insight: separate semantic content from generator-specific artifacts parallels our need to isolate depth signal from generator identity.\\n      Dual-bottleneck architecture enforces compact, minimal latent codes; could inspire our depth encoder design.\\n      Tests on 20 LLMs across 7 categories but only binary classification. No multi-generation or depth estimation.\\n      Our depth estimator needs similar generator invariance: depth signal should hold across model families.\\n\", \"total_chars\": 16560, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f16211e-b46b-4ac0-b48d-9bc73bc5d984",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "624955a7-1bdd-4043-89ea-bf7bae9105a2",
  "sourceToolAssistantUUID": "9f16211e-b46b-4ac0-b48d-9bc73bc5d984",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T12:09:42.993Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NqJBmLqCvXAH2pW1i9478f`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "624955a7-1bdd-4043-89ea-bf7bae9105a2",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1WaTjLKVn3x4FwE92t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e413940-42ed-433d-8e0e-8f575a18366c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QqNvyeYG1v7ErxPLy5Bk4Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2981,
      "cache_read_input_tokens": 18256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2981,
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

_source line 15 · 2026-05-18T12:09:43.005Z_

<details><summary>↩ Tool result · `toolu_01NqJBmLqCvXAH2pW1i9478f`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-contamination\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\\n- Fallback: EMNLP 2026 Findings\\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\\n\\n## Canonical Experimental Condition\\n\\n**Continuation mode 是 cross-model 结论的基础。**\\n\\n> \\\"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\\\"\\n\\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\\n|-----------|-------------|-------------|---------|\\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\\n\\n**原则**：\\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\\n- mvp-001 (Qwen-rewrite) 定位为 \\\"pilot study demonstrating feasibility\\\"，后续用 continuation mode rigorously validate\\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\\n\\n## Core Claims (2+1 结构, updated D049/D050)\\n\\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\\n\\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 8 model configurations（5 architecture families, 1B-8B）、3 source domains（C4, Wikipedia, arXiv）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\\n\\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现三级域阶梯：Wikipedia(1) < C4(2) < arXiv(3)\\n- **Web text K*=2 是 dominant mode**（7/8 configurations），展现跨模型架构、跨解码策略的一致性\\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\\n- **Domain 是 K* 的唯一主导因素**：scorer control 后，model scale/architecture/decoding strategy 均不改变域内 K* 一致性\\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\\n\\n**子组件：**\\n\\n**(a) K*=2 as dominant mode for web text (7/8 configurations)**\\n> **7/8 model configurations yield K*=2 on C4 web text：**\\n>\\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\\n> |-------|-----------|---------|--------|-----------------|\\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\\n>\\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\\n>\\n> *Decoding strategy invariance (exp-003):*\\n> | Decoding | AUC 1v2 | K* |\\n> |----------|---------|-----|\\n> | greedy | 0.6893 | 2 |\\n> | nucleus p=0.9 | 0.6866 | 2 |\\n> | temp=0.7 | 0.6887 | 2 |\\n> | temp=1.2 | 0.7039 | 2 |\\n>\\n> - 7/8 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\\n> - ⚠️ θ-sensitivity: θ=0.60 下 7/8 K*=2; θ=0.70 下多数降至 K*=1\\n> - Paper 措辞：\\\"K*=2 emerges as the dominant mode for general web text (7/8 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\\\"\\n\\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \\\"domain competence prerequisite\\\" 分析放 Appendix\\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\\n> - Sample size: n=2,200 per model\\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \\\"K*=3 with boundary pair AUC of 0.62\\\" 而非 \\\"robustly K*=3\\\"\\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\\n\\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\\n\\n**(d) Cross-model transfer (scorer invariance)**\\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\\n\\n**(e) Representation dependence of K* (Neural Probe)**\\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\\n> - 论文定位：validates choice of model-free 15D features for headline characterization\\n\\n**(f) Generation mode analysis (§4.x Analysis subsection)**\\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\\n> - 论文定位：Analysis subsection，不是独立 claim\\n\\n### Secondary: C3 (K*-Aware Data Curation Validation)\\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\\n\\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \\\"universally beneficial\\\"。维持 \\\"consistent advantage\\\" 措辞，以 HellaSwag 显著性为主要证据。\\n\\n### Supporting Analysis: Canonical Condition Selection\\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\\n\\n## Story Spine\\n\\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\\\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\\\"。通过 8 model configurations（5 architecture families, 1B-8B）、3 source domains、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的三级域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（7/8 configurations），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\\\"one-wash laundering\\\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\\n- **Headline result template**: \\\"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a three-level domain hierarchy: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text at K*=2 (7/8 model configurations, 5 architecture families, 1B-8B), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\\\"\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n1. **\\\"K*∈{1,2,3} 范围太小，结论是否 trivial？\\\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\\n2. **\\\"只基于小模型（≤8B），能推广到更大模型吗？\\\"** → 5 architecture families (1B-8B) 覆盖了当前开源生态的主要架构。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\\n3. **\\\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\\\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\\n4. **\\\"arXiv K*=3 样本量够吗？\\\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\\n5. **\\\"Mistral K*=1 是 outlier 还是 systematic？\\\"** → Cross-scorer validation 确认是 text-intrinsic（非 scorer artifact）。Mistral 可能因训练数据/alignment 差异导致生成文本在一代后即失去 depth-distinguishing structure。这强化了 domain/model dependence 的核心论点。\\n6. **\\\"Prompt-chain 不代表真实世界递归污染\\\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**exp-008 实证验证**：retrain-chain (Pythia-1.4B LoRA) K*≥4（1v2=0.9484, 2v3=0.8888, 3v4=0.7982），远高于 prompt-chain K*=2。原因：LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），使各代高度可区分。这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss），而非 retrain-chain 的 upper bound。\\n7. **\\\"同模型做生成和 surprisal 计算有 bias\\\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\\n8. **\\\"为什么不用 learned representations\\\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\\n9. **\\\"θ=0.60 选择是否 arbitrary？\\\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\\n10. **\\\"Graduated filtering 没和 data selection methods 比\\\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\\n\\n## Venue Fit\\n\\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} 的 bounded range + domain dependence 是 nuanced scientific finding，比 \\\"K*=2 everywhere\\\" 更可信且更 interesting（审稿人不必怀疑过度外推）\\n- One-wash laundering effect 是 memorable concept 便于传播\\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\\n\", \"total_chars\": 14041, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e413940-42ed-433d-8e0e-8f575a18366c",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "a8cc8bf0-c696-4456-9440-594dad6bab55",
  "sourceToolAssistantUUID": "0e413940-42ed-433d-8e0e-8f575a18366c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T12:09:43.460Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JmTmKNAs3NJbj4F3RXKe7J`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8cc8bf0-c696-4456-9440-594dad6bab55",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1WaTjLKVn3x4FwE92t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59c76686-d55a-4652-9b4e-f6d269463987",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QqNvyeYG1v7ErxPLy5Bk4Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2981,
      "cache_read_input_tokens": 18256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2981,
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

_source line 17 · 2026-05-18T12:09:43.471Z_

<details><summary>↩ Tool result · `toolu_01JmTmKNAs3NJbj4F3RXKe7J`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026 Main\\n  track: ARR May 2026\\n  template: null\\n  template_note: \\\"ARR uses ACL Rolling Review format (acl2023.sty). Will use standard ACL LaTeX class from EMNLP 2025 call.\\\"\\n  page_limit: 8\\n  deadline: 2026-05-25\\n  core_claim: >\\n    K*=2 is the generational discrimination boundary for 1.5B-scale models, invariant to decoding strategy (nucleus, greedy, temperature).\\n    Transfer retention of 80-92% suggests a large text-intrinsic component (Pythia↔OLMo 91% retention).\\n    Even coarse 3-class ordinal signal enables graduated filtering that outperforms binary approaches.\\n  created_at: 2026-05-13T12:00:00Z\\n  partial_draft: true\\n  partial_scope: [method, experiments_c1, related_work, introduction]\\n  deferred_sections: [abstract, experiments_c3, conclusion]\\n  deferred_reason: \\\"exp-006 (graduated filtering) and exp-003 (decoding ablation) not yet complete\\\"\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 250\\n    status: deferred\\n    core_bullets:\\n      - \\\"Problem: Web data contaminated by multi-generational recursive synthetic text; binary detectors ignore depth\\\"\\n      - \\\"Method: DPI motivates finite K* (theoretical motivation); 15D feature pipeline + OBD-LightGBM measures it empirically\\\"\\n      - \\\"C1': K*=2 across 4 model configs (bootstrap 95% CI), 80-92% transfer retention suggests large text-intrinsic component\\\"\\n      - \\\"C3: [TODO exp-006] Graduated filtering outperforms binary on MMLU/HellaSwag\\\"\\n    dependencies: [experiments_c1, experiments_c3, method]\\n\\n  - section: introduction\\n    word_budget: 1200\\n    status: writable\\n    core_bullets:\\n      - \\\"Hook: First-gen synthetic text retains ~85% information structure of source; fourth-gen is qualitatively different — yet binary detectors treat them identically\\\"\\n      - \\\"Gap: Binary detection doesn't estimate depth; model collapse literature describes macro phenomenon without detection tools; data selection methods ignore recursive depth\\\"\\n      - \\\"Insight: Recursive generation = iterated lossy channel; DPI guarantees finite K* (theoretical motivation, not contribution); we are first to systematically measure it\\\"\\n      - \\\"Mechanism: 15D statistical feature pipeline + ordinal classifier; K* operationalized via θ=0.60 AUC threshold with bootstrap CI\\\"\\n      - \\\"Contributions: C1' K* Characterization with sub-components: (a) K*=2 across all tested configs including decoding strategies — invariant to sampling method; (b) cross-model transfer 80-92% retention → large text-intrinsic component; (c) degradation ordering ρ≥0.85; (d) generation mode analysis. C3 Graduated Filtering (pending exp-006). Supporting: systematic characterization across decoding strategies, model architectures, and generation modes. DPI is theoretical motivation, NOT independent contribution\\\"\\n    dependencies: [experiments_c1]\\n    citation_hints:\\n      - \\\"shumailov2024collapse (model collapse seminal)\\\"\\n      - \\\"drayson2025 (closest prior work)\\\"\\n      - \\\"basani2026diveye, zhang2024minkpp (binary detection)\\\"\\n      - \\\"schaeffer2025position (collapse taxonomy)\\\"\\n    figures: [fig1_pipeline]\\n    registry_refs: [exp_007_bootstrap_ci]\\n\\n  - section: related_work\\n    word_budget: 800\\n    status: writable\\n    core_bullets:\\n      - \\\"Model Collapse & Recursive Generation: Shumailov 2024 (Nature, seminal), Alemohammad 2024 (self-consuming MAD), Dohmatob 2024 (scaling law perspective), Schaeffer 2025 (8 definitions taxonomy — K* = Family B D4+D6), Kazdan 2025 (accumulate vs replace), Shi 2025 (memorization transition) → macro phenomenon, no per-text detection tool\\\"\\n      - \\\"Binary Synthetic Text Detection: Zellers 2019 (Grover), Ippolito 2020, DivEye (Basani 2026), Min-K%++ (Zhang 2024), CoDeC (Zawalski 2026) → binary boundary only, AUC_{1v2} ≤ 0.53 for depth\\\"\\n      - \\\"Data Selection & Curation: DSIR (Xie 2023), D4 (Tirumala 2023), DoReMi (Xie 2023) → distribution matching without depth; Drayson 2025 = closest (binary MGT + SIR for collapse prevention, our ordinal generalization); Amin 2025 (weak signal suffices); Gambetta 2025 (surplexity)\\\"\\n      - \\\"Watermarking & Provenance: Kirchenbauer 2023 → complementary when watermarks available; our method works on unwatermarked text\\\"\\n    dependencies: [introduction]\\n    citation_hints:\\n      - \\\"Position Drayson 2025 as closest prior work: SIR is special case of graduated filtering when K*=1\\\"\\n      - \\\"Adopt Schaeffer 2025 taxonomy explicitly: K* = distributions deforming (Family B)\\\"\\n\\n  - section: method\\n    word_budget: 1500\\n    status: writable\\n    core_bullets:\\n      - \\\"§3.1 Problem Formulation: Recursive generation as iterated lossy channel X → Y₁ → Y₂ → ...; DPI as theoretical motivation: I(X;Y_k) monotonically decreasing → finite K*_theory must exist; motivated by this guarantee, we measure K*_empirical\\\"\\n      - \\\"§3.2 Feature Extraction: 15D statistical features in 4 groups (surprisal moments, surprisal derivatives, vocabulary diversity, frequency tail); computed via external scorer model on tokenized text\\\"\\n      - \\\"§3.3 Ordinal Binary Decomposition Classifier: OBD-LightGBM — K binary classifiers for K+1 depth levels; ordinal structure enforced by cumulative probability decomposition; advantage over multiclass (exp-010: lower MAE)\\\"\\n      - \\\"§3.4 K* Operationalization: K*_empirical = max k s.t. AUC(k,k+1) bootstrap 95% CI lower > θ; θ=0.60 as operational threshold (justified by permutation test null distribution); K*_empirical ≤ K*_theory (conservative lower bound)\\\"\\n      - \\\"§3.5 Experimental Setup: 3 model families (Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct) × 2 generation modes; C4 seed corpus (5K docs); nucleus sampling p=0.95 T=1.0; depth 0-5; 5-fold group CV (GroupKFold by seed document)\\\"\\n      - \\\"§3.6 Generation Mode Control: continuation (complete truncated prefix) vs rewrite (instruction-based rewrite); continuation as canonical condition for cross-model claims; rewrite as upper bound with mode-specific confound\\\"\\n    dependencies: []\\n    notation_table:\\n      X: \\\"original human-written text\\\"\\n      Y_k: \\\"k-th generation synthetic text\\\"\\n      G_delta: \\\"LLM generation function with decoding strategy δ\\\"\\n      K_star: \\\"generational discrimination boundary\\\"\\n      theta: \\\"operational AUC threshold (0.60)\\\"\\n      f: \\\"15D feature extraction function\\\"\\n    tables: [tab_features, tab_setup]\\n    figures: [fig1_pipeline]\\n    registry_refs: [exp_010_ordinal_baseline]\\n\\n  - section: experiments_c1\\n    word_budget: 1800\\n    status: writable\\n    core_bullets:\\n      - \\\"§4.1 K*=2 Across All Configurations: 4-model bootstrap CI table; all 1v2 CI_lower > 0.60; all 2v3 CI_upper < 0.60; permutation p < 0.002 for all 1v2; most marginal = Qwen-cont (CI_lower=0.6015); sharp AUC drop from 0v1 (~0.995) to 1v2 (~0.61-0.70) to 2v3 (~0.55-0.59)\\\"\\n      - \\\"§4.2 Cross-Model Transfer: 4×4 accuracy matrix + retention analysis; Pythia↔OLMo 91-92% retention → large text-intrinsic component; 0v1 AUC >0.96 universally; Qwen-rewrite catastrophic transfer (61-63%); Qwen-cont much better (80-85%); confirms continuation as canonical\\\"\\n      - \\\"§4.3 Feature Degradation Ordering: Spearman ρ ≥ 0.85 on single-feature AUC ranking (continuation, Pythia vs OLMo = 0.95); shared top features: surp_d1_std, surp_std, surp_d2_std; limitation: depth-pair level τ~0.37 at 1v2\\\"\\n      - \\\"§4.4 Generation Mode Effect: rewrite AUC 1v2=0.6957 vs continuation 0.6114 (Δ=+8.4pp); transfer asymmetry cont→rw 89% > rw→cont 82%; rewrite amplifies depth signal via instruction-following artifacts but reduces cross-model generalizability\\\"\\n    dependencies: []\\n    tables: [tab_kstar_ci, tab_transfer_matrix, tab_top_features]\\n    figures: [fig2_auc_decay, fig3_transfer_heatmap]\\n    registry_refs:\\n      - exp_001_pythia_depth\\n      - exp_002_olmo_depth\\n      - exp_017_qwen_continuation\\n      - mvp_pilot_sat_v1\\n      - exp_007_bootstrap_ci\\n      - exp_013_cross_transfer\\n      - exp_005_degradation\\n\\n  - section: experiments_c3\\n    word_budget: 1000\\n    status: deferred\\n    core_bullets:\\n      - \\\"[TODO exp-006] 6 filtering strategies × 5 seeds × α sweep\\\"\\n      - \\\"[TODO exp-006] Graduated vs binary on MMLU/HellaSwag\\\"\\n      - \\\"[TODO exp-006] α sensitivity + DSIR baseline comparison\\\"\\n    dependencies: [experiments_c1]\\n    tables: [tab_filtering]\\n\\n  - section: conclusion\\n    word_budget: 400\\n    status: deferred\\n    core_bullets:\\n      - \\\"Summary: K*=2 first systematic measurement + cross-model transferability + graduated filtering\\\"\\n      - \\\"Limitations: 1.5B-scale only; C4 English only; prompt-chain not retrain-chain; K* = operational lower bound\\\"\\n      - \\\"Future: retrain-chain validation; larger models; multilingual; temporal dynamics of web contamination\\\"\\n    dependencies: [experiments_c1, experiments_c3, method]\\n\\nvisualization_plan:\\n  - fig_id: fig1_pipeline\\n    type: conceptual\\n    tool: matplotlib\\n    description: \\\"System overview diagram: recursive generation chain (X → Y₁ → Y₂ → ... → Y_K) → 15D feature extraction → OBD-LightGBM depth classifier → K* determination via bootstrap CI. Clean academic style with arrows and labeled components.\\\"\\n    placement: method\\n    aspect_ratio: \\\"16:6\\\"\\n    data_source: \\\"manual (conceptual diagram)\\\"\\n\\n  - fig_id: fig2_auc_decay\\n    type: statistical\\n    tool: matplotlib\\n    description: \\\"Pairwise AUC decay curves across depth pairs (0v1, 1v2, 2v3, 3v4, 4v5) for 4 model configurations. Horizontal dashed line at θ=0.60. Error bars from bootstrap 95% CI. X-axis: depth pair, Y-axis: AUC. Shows K*=2 boundary clearly — all curves cross θ between 1v2 and 2v3.\\\"\\n    placement: experiments_c1\\n    aspect_ratio: \\\"4:3\\\"\\n    data_source: \\\"registry: exp_007_bootstrap_ci\\\"\\n\\n  - fig_id: fig3_transfer_heatmap\\n    type: statistical\\n    tool: matplotlib\\n    description: \\\"4×4 cross-model transfer accuracy heatmap. Rows = training source (Qwen-rw, Pythia, OLMo, Qwen-cont), columns = evaluation target. Annotated with accuracy values. Color scale from low (Qwen-rw cross-transfer ~0.26) to high (diagonal ~0.38-0.42). Highlight Pythia↔OLMo cluster.\\\"\\n    placement: experiments_c1\\n    aspect_ratio: \\\"1:1\\\"\\n    data_source: \\\"registry: exp_013_cross_transfer\\\"\\n\\n  - fig_id: fig4_filtering\\n    type: statistical\\n    tool: matplotlib\\n    status: deferred\\n    description: \\\"[DEFERRED] Graduated vs binary filtering comparison on MMLU/HellaSwag.\\\"\\n    placement: experiments_c3\\n    data_source: \\\"[TODO exp-006]\\\"\\n\\ntable_plan:\\n  - table_id: tab_kstar_ci\\n    caption: \\\"Pairwise depth discrimination AUC with bootstrap 95\\\\\\\\% CI across four model configurations. All 1v2 CI lower bounds exceed $\\\\\\\\theta=0.60$; all 2v3 CI upper bounds fall below $\\\\\\\\theta$, establishing $K^*=2$.\\\"\\n    placement: experiments_c1\\n    type: statistics\\n    columns: [Configuration, Generation Mode, \\\"AUC$_{0v1}$\\\", \\\"AUC$_{1v2}$\\\", \\\"95\\\\\\\\% CI$_{1v2}$\\\", \\\"$p_{1v2}$\\\", \\\"AUC$_{2v3}$\\\", \\\"95\\\\\\\\% CI$_{2v3}$\\\"]\\n    data_source: \\\"registry: exp_007_bootstrap_ci\\\"\\n    notes: \\\"Bold 1v2 values above threshold. Report permutation test p-values.\\\"\\n\\n  - table_id: tab_transfer_matrix\\n    caption: \\\"Cross-model transfer accuracy matrix (6-class ordinal depth classification). Diagonal entries show within-model performance; off-diagonal entries show cross-model transfer.\\\"\\n    placement: experiments_c1\\n    type: comparison\\n    columns: [\\\"Train $\\\\\\\\backslash$ Test\\\", Qwen-rw, Pythia, OLMo, Qwen-cont]\\n    data_source: \\\"registry: exp_013_cross_transfer\\\"\\n    notes: \\\"Report retention percentage (off-diagonal / diagonal). Highlight Pythia↔OLMo 91-92% and Qwen-rw 61-63%.\\\"\\n\\n  - table_id: tab_top_features\\n    caption: \\\"Top-3 discriminative features by single-feature AUC ranking across model configurations (continuation mode only). Spearman $\\\\\\\\rho$ between model pairs shown below.\\\"\\n    placement: experiments_c1\\n    type: statistics\\n    columns: [Rank, Pythia-1.4B, OLMo-1B, Qwen-1.5B-cont]\\n    data_source: \\\"registry: exp_005_degradation\\\"\\n    notes: \\\"surp_d1_std, surp_std, surp_d2_std shared across all architectures.\\\"\\n\\n  - table_id: tab_features\\n    caption: \\\"15-dimensional feature set for depth estimation, organized by feature group.\\\"\\n    placement: method\\n    type: configuration\\n    columns: [Group, Feature, Description]\\n    data_source: \\\"manual\\\"\\n\\n  - table_id: tab_setup\\n    caption: \\\"Experimental configurations for recursive depth chain generation.\\\"\\n    placement: method\\n    type: configuration\\n    columns: [ID, Model, Parameters, Generation Mode, N, Max Depth]\\n    data_source: \\\"manual + registry specs\\\"\\n\\n  - table_id: tab_filtering\\n    caption: \\\"[DEFERRED] Downstream evaluation: filtering strategy comparison.\\\"\\n    placement: experiments_c3\\n    type: comparison\\n    status: deferred\\n    columns: [Strategy, MMLU, HellaSwag, \\\"Δ vs no-filter\\\"]\\n    data_source: \\\"[TODO exp-006]\\\"\\n\\nliterature_strategy:\\n  citation_budget: 30\\n  macro_context:\\n    - \\\"recursive synthetic text contamination and generational depth\\\"\\n    - \\\"data curation and quality estimation for LLM pretraining\\\"\\n  micro_clusters:\\n    - cluster_name: \\\"model-collapse\\\"\\n      search_queries:\\n        - \\\"model collapse iterative training synthetic data 2024 2025\\\"\\n        - \\\"recursive generation quality degradation LLM\\\"\\n      must_cite:\\n        - shumailov2024collapse\\n        - alemohammad2024selfconsuming\\n        - dohmatob2024model\\n        - schaeffer2025position\\n        - kazdan2025collapse\\n        - shi2025generalization\\n      target_count: 6\\n\\n    - cluster_name: \\\"detection\\\"\\n      search_queries:\\n        - \\\"machine generated text detection statistical 2024 2025 2026\\\"\\n        - \\\"AI text detection zero-shot features\\\"\\n      must_cite:\\n        - basani2026diveye\\n        - zhang2024minkpp\\n        - zellers2019grover\\n        - ippolito2020detection\\n      target_count: 5\\n\\n    - cluster_name: \\\"verification-curation\\\"\\n      search_queries:\\n        - \\\"data selection pretraining LLM synthetic filtering 2024 2025\\\"\\n        - \\\"synthetic data curation importance resampling\\\"\\n      must_cite:\\n        - drayson2025\\n        - xie2023dsir\\n        - tirumala2024d4\\n        - xie2024doremi\\n        - amin2025escaping\\n        - gambetta2025surplexity\\n      target_count: 7\\n\\n    - cluster_name: \\\"watermarking\\\"\\n      search_queries:\\n        - \\\"LLM watermarking provenance tracking 2024 2025\\\"\\n      must_cite:\\n        - kirchenbauer2023watermark\\n      target_count: 2\\n\\nwriting_order:\\n  - method\\n  - experiments_c1\\n  - related_work\\n  - introduction\\n\", \"total_chars\": 14238, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59c76686-d55a-4652-9b4e-f6d269463987",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "e74e2d45-2e22-44b3-907b-c0b0ddb61451",
  "sourceToolAssistantUUID": "59c76686-d55a-4652-9b4e-f6d269463987",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T12:09:44.117Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VQQ8C6p4cqQvCpjhKepQRh`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e74e2d45-2e22-44b3-907b-c0b0ddb61451",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1WaTjLKVn3x4FwE92t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86804110-54ec-452f-8f76-ea1153fa011a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QqNvyeYG1v7ErxPLy5Bk4Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2981,
      "cache_read_input_tokens": 18256,
      "output_tokens": 474,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2981
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 474,
          "cache_read_input_tokens": 18256,
          "cache_creation_input_tokens": 2981,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2981,
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

_source line 19 · 2026-05-18T12:09:44.430Z_

<details><summary>↩ Tool result · `toolu_01VQQ8C6p4cqQvCpjhKepQRh`</summary>

```text
Error: result (53,235 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1/tool-results/mcp-agent-ml-research-read_project_file-1779106184426.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1/tool-results/mcp-agent-ml-research-read_project_file-1779106184426.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1/tool-results/mcp-agent-ml-research-read_project_file-1779106184426.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86804110-54ec-452f-8f76-ea1153fa011a",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "cb861dc9-29cc-4347-bed2-c5d886f95c96",
  "sourceToolAssistantUUID": "86804110-54ec-452f-8f76-ea1153fa011a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-18T12:09:49.511Z_

Let me read the decisions file and the paper artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb861dc9-29cc-4347-bed2-c5d886f95c96",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1X991JzuzSCXqTySG5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eadf4da2-afb6-4cfa-9513-25c91cdbd6b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNWKaLP68fVL9Ff27Sqmb8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19029,
      "cache_read_input_tokens": 21237,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19029,
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

_source line 21 · 2026-05-18T12:09:51.353Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KD7NghKEgiXWXm9fCmVgJy`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1/tool-results/mcp-agent-ml-research-read_project_file-1779106184426.txt | python3 -c \"import json,sys; d=json.load(sys.stdin); r=json.loads(d['result']); print(r['data']['content'][:8000])\"",
  "description": "Extract first 8000 chars of decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eadf4da2-afb6-4cfa-9513-25c91cdbd6b5",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1X991JzuzSCXqTySG5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc5da585-7966-4d48-814e-0c08a85e6815",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNWKaLP68fVL9Ff27Sqmb8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19029,
      "cache_read_input_tokens": 21237,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19029,
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

### Tool result

_source line 22 · 2026-05-18T12:09:51.550Z_

<details><summary>↩ Tool result · `toolu_01KD7NghKEgiXWXm9fCmVgJy`</summary>

```text
_next_id: 69
decisions:
- id: D001
  date: 2026-05-12 10:58 UTC
  summary: MVP 方案：Qwen2.5-1.8B + C4 5K docs 做 pilot saturation study，验证代际深度可分辨性
  rationale: Phase 0 pilot saturation study 是天然的 MVP gate——如果不同代际深度的文本在特征空间上不可区分，整个项目没有意义。选
    Qwen2.5-1.8B 因为体积小、开源、生成速度快。5K docs 足够统计显著性但不浪费 GPU。Pass 标准 K*≥3 对应至少 4 个有意义的类别（human/gen1/gen2/gen3+），AUC>0.70
    确保特征有实质区分力。
  related_experiments: []
  depends_on: []
- id: D002
  date: 2026-05-12 15:10 UTC
  summary: MVP 初步结果 K*=2（边界），修复 right-padding 后重跑确认再锁路线
  rationale: AUC(2v3)=0.5797 距阈值 0.60 仅差 0.02，right-padding bug 可能系统性压低 K*。修复成本（1行代码+3h
    GPU）远低于错选路线的代价。
  related_experiments:
  - exp_id: mvp_pilot_sat_v1
    role: primary
    result: K*=2 (borderline), AUC(0v1)=0.9952, AUC(1v2)=0.6712, AUC(2v3)=0.5797
  depends_on: []
- id: D003
  date: 2026-05-12 19:27 UTC
  summary: MVP Conditional Pass, K*=2, 锁定 Route B (Saturation Characterization), 进入
    research 阶段
  rationale: v3 definitive run 确认 K*=2：AUC(0v1)=0.9956, AUC(1v2)=0.6957, AUC(2v3)=0.5893(<0.60)。JSD
    严格单调递减支持 DPI 理论。Depth signal 存在但饱和在 depth 2-3。Route B 将 K* 本身定位为首次测量的基本科学量，比 Route
    A（depth classifier 可行性）更 robust——不依赖阈值选择。3-class 系统（human/gen-1/gen-2+）仍比 binary
    更有信息量。
  related_experiments:
  - exp_id: mvp_pilot_sat_v1
    role: primary
    result: K*=2, AUC(0v1)=0.9956, AUC(1v2)=0.6957, AUC(2v3)=0.5893, JSD monotonic
      decay
  depends_on:
  - D002
- id: D004
  date: 2026-05-12 20:08 UTC
  summary: Reviewer 审查后修正：C1 区分 K*_empirical vs K*_theory；exp-013 (cross-model transfer)
    从 P1 提升至 P0
  rationale: Reviewer 指出 C1 混淆了经验值和理论值——实测 K*=2 是特定特征+分类器下的 practical boundary，不等于信息论
    impossibility boundary。更好的特征/分类器可能推高 K*。修正为"K*_empirical 是 K*_theory 的保守下界"。exp-013
    (cross-model transfer, 仅 2h) 直接回答审稿人最危险的攻击面：depth signal 是文本固有属性还是 model self-familiarity？Transfer
    失败则 C1 需根本调整。性价比极高，必须 P0。
  related_experiments: []
  depends_on:
  - D003
- id: D005
  date: 2026-05-13 00:23 UTC
  summary: Dream 分析完成：proceed with P0, 整合 8 项确认行动到 framing/plan
  rationale: Dream 三档评分 Best=Weak Accept / Median=Borderline / Worst=Weak Reject。跨三档一致的结构性问题（通用建议）已整合：(1)
    IT/fundamental framing 已在 D004 校正，进一步软化 "universal" 措辞; (2) related work 扩展到 4
    方向; (3) exp-006 加 DSIR baseline + α ablation + 5 seeds; (4) exp-007 加 bootstrap
    CI + permutation-test; (5) exp-015 从 P2 升 P1; (6) 3-class accuracy 显式报告。6 项观察项待真实实验验证：Drayson
    et al. 存在性待查、cross-model transfer framing、domain sensitivity、method-code consistency、learned
    probe strength、cross-scale probe power。无需 re-dream——确认行动项均为增量调整，不改变 framing 结构。
  related_experiments:
  - exp_id: exp-006
    role: updated
    result: 加 DSIR baseline + α ablation + 5 seeds, GPU 48h→72h
  - exp_id: exp-007
    role: updated
    result: 加 bootstrap CI + permutation-test, GPU 1h→2h
  - exp_id: exp-015
    role: promoted
    result: P2→P1
  depends_on:
  - D004
- id: D006
  date: 2026-05-13 00:58 UTC
  summary: '回滚 Drayson et al. 引用清理——Reviewer 确认为真实论文 (EMNLP 2025 #1506)'
  rationale: D005 中基于 web search 无结果将 Drayson et al. (2025) 判定为 Dream 幻觉引用并指示 Agent
    清理。Reviewer 独立核实找到 arXiv:2502.15654 + UCL Discovery PDF + GitHub repo，确认为真实发表论文。这是我们最相关的
    prior work（binary filtering 防 collapse），我们的 ordinal depth estimation 是其自然推广。教训：单次
    web search 不足以判定引用为幻觉，应交叉验证（arXiv ID + 作者机构 + 会议 proceedings）。
  related_experiments: []
  depends_on:
  - D005
- id: D007
  date: 2026-05-13 02:06 UTC
  summary: Drayson novelty 评估完成：核心 novelty 安全，Story Spine 微调，exp-006 加公平 binary baseline
  rationale: Reviewer 独立评估确认：(1) Drayson 做 binary detection 防 collapse（宏观训练动态），我们做
    ordinal depth estimation + K* measurement（单样本深度估计）——问题定义层面的扩展，非渐进改进；(2) Drayson
    100 代是训练迭代不是文本递归深度，不构成 novelty 威胁；(3) Story Spine 加入 Drayson 作为 closest prior
    work 但保持 gap statement 完整；(4) exp-006 加 binary-ours baseline（同 15D 特征做 binary，唯一变量
    = binary/ordinal），确保 C3 对比公平。
  related_experiments:
  - exp_id: exp-006
    role: updated
    result: 加 binary-ours 公平对比 baseline
  depends_on:
  - D006
- id: D008
  date: 2026-05-13 02:45 UTC
  summary: C2 claim 暂停写入论文——等 exp-017 解耦 generation mode 因素后决定措辞
  rationale: exp-005 结果显示 Kendall τ 仅 Pythia-OLMo 达 0.8476（≥0.8），Pythia-Qwen 0.5238、OLMo-Qwen
    0.4857 均不达标。1/3 通过率不支持 C2 当前 "τ≥0.8 across all tested families" 的表述。关键混杂因素：Pythia/OLMo
    用 continuation 模式，Qwen 用 rewrite 模式。exp-017（Qwen continuation，~4h 后完成）将区分是 mode-dependent
    还是 model-dependent。若 Qwen continuation τ≥0.8 → C2 限定为 "consistent within continuation
    mode"；若仍低 → C2 大幅弱化为 "partially consistent" 或限定 base model 范围。
  related_experiments:
  - exp_id: exp-005
    role: evidence
    result: partial_consistency_1of3_pairs
  - exp_id: exp-017
    role: pending_resolution
    result: running
  depends_on: []
- id: D009
  date: 2026-05-13 03:35 UTC
  summary: C2 战略评估：C1 是承重墙，C3 是安全网，C2 是加分项；exp-016 列为场景 B 应急
  rationale: 'Reviewer 深度评估指出第三混杂因素：instruct-tuning。Qwen-Instruct vs Pythia/OLMo base
    的差异不仅是 generation mode。exp-017 无法完全解耦 mode 和 instruct-tuning 的联合效应。场景 A (τ≥0.8):
    C2 改为 mode-dependent insight (7/10)，可撑 EMNLP Main。场景 B (τ<0.7): C2 降级为 supplementary
    finding (3/10)，C1+C3 仍可投 Main/Findings，取决于 C3 效果大小。exp-006 (graduated filtering)
    优先级应提升作为 C2 弱化的安全网。exp-016 (Qwen base continuation) 作为场景 B 应急实验预备——可解耦 instruct-tuning
    vs architecture 效应，仅 6h GPU。'
  related_experiments:
  - exp_id: exp-005
    role: evidence
    result: partial_consistency
  - exp_id: exp-017
    role: pending_resolution
    result: running
  - exp_id: exp-006
    role: priority_elevated
    result: planned
  - exp_id: exp-016
    role: contingency_scenario_B
    result: planned
  depends_on:
  - D008
- id: D010
  date: 2026-05-13 06:20 UTC
  summary: C2 Plan A 否决 → 执行 Plan B：degradation ordering 限定为 "within architecture
    family"，降级为 supplementary finding
  rationale: exp-017 (Qwen continuation) 结果明确：控制 generation mode 后，Qwen top feature
    仍是 freq_entropy（vs Pythia/OLMo 的 surp_d1_mean）。分歧是 model-dependent 而非 mode-dependent。按
    D009 预案，C2 降级为 supplementary finding，措辞改为 "feature degradation ordering consistent
    within architecture family (base models τ=0.85), but diverges across architecture
    types"。同时发现 generation mode effect 很大（rewrite→continuation AUC 1v2 下降 0.084），论文需增加
    mode effect 讨论段。C1 不受影响（4/4 条件 K*=2）。C3 重要性提升为论文第二支柱。
  related_experiments:
  - exp_id: exp-017
    role: decisive_evidence
    result: plan_a_rejected
  - exp_id: exp-005
    role: initial_evidence
    result: partial_consistency
  depends_on:
  - D008
  - D009
- id: D011
  date: 2026-05-13 06:24 UTC
  summary: D010 修正：C2 从 "supplementary" 升级为 "qualified claim"——使用 single-feature AUC
    + Spearman ρ≥0.85 + mode-controlled 条件
  rationale: 'Reviewer 4-model 降解分析修正了此前结论。LightGBM split count 和 single-feature AUC
    给出矛盾排名：split count 显示 Qwen-cont freq_entropy #1（与 Pythia/OLMo 分歧），但 single-feature
    AUC 显示 Qwen-cont top-3 与 Pythia/OLMo 完全一致（surp_d1_std, surp_std, surp_d2_std）。Single-feature
    AUC 更直接衡量代际区分力，更适合 C2 语义。Spearman ρ: Pythia-OLMo=0.95, Pythia-Qwen_cont=0.9143,
    OLMo-Qwen_cont=0.85——全部≥0.85。C2 可行路径：(1) 用 single-feature AUC ranking 定义 ordering；(2)
    用 Spearman ρ≥0.85 作为一致性阈值；(3) 限定 mode-controlled 条件；(4) 透明报告 depth-pair level
    差异（1v2 对 τ 仅 0.35-0.39）和 τ vs ρ 选择理由。风险：depth-pair 1v2 一致性差（τ~0.37），审稿人可能做 depth-stratified
    分析。'
  related_experiments:
  - exp_id: exp-005
    role: 4model_reanalysis
    result: rho_ge_0.85_all_pairs
  - exp_id: exp-017
    role: mode_control
    result: convergence_confirmed
  depends_on:
  - D010
- id: D012
  date: 2026-05-13 07:29 UTC
  summary: 论文 claim 重构：4 claims → 2+1 结构（C1' K* characterization + C3 graduated filtering
    + supporting analysis）
  rationale: Reviewer 评估指出 4 claims (C1/C2/C3/C4) 对 EMNLP Main 太散，每个不够厚。重构为：Primary
    C1' = 首次系统测量 K*_empirical（含 DPI 理论 + 4-model 验证 + cross-model transfer + degradation
    ordering + generation mode analysis）；Secondary C3 = graduated filtering > binary；Supporting
    = generation mode effect + metric analysis 作为 §4.4 subsection。C4 从独立 claim 降级为方法论洞见（Canonical
    Condition
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc5da585-7966-4d48-814e-0c08a85e6815",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "b54588f6-f667-4255-9242-e2f45f0cad63",
  "sourceToolAssistantUUID": "bc5da585-7966-4d48-814e-0c08a85e6815",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T12:09:52.087Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KJebfcpsNJqoMHfYVMF69k`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b54588f6-f667-4255-9242-e2f45f0cad63",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1X991JzuzSCXqTySG5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2291f98-4762-43d5-83c7-7b098ad5481f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNWKaLP68fVL9Ff27Sqmb8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19029,
      "cache_read_input_tokens": 21237,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19029
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 315,
          "cache_read_input_tokens": 21237,
          "cache_creation_input_tokens": 19029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19029,
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

_source line 24 · 2026-05-18T12:09:52.115Z_

<details><summary>↩ Tool result · `toolu_01KJebfcpsNJqoMHfYVMF69k`</summary>

```text
artifacts/dream_reports/dream_20260512T200328/best/paper.tex
artifacts/dream_reports/dream_20260512T200328/median/paper.tex
artifacts/dream_reports/dream_20260512T200328/worst/paper.tex
artifacts/dream_reports/dream_20260513T080728/best/paper.tex
artifacts/dream_reports/dream_20260513T080728/median/paper.tex
artifacts/dream_reports/dream_20260513T080728/worst/paper.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_c1.tex
artifacts/exp_015_neural_probe/paper/neural_probe_analysis.tex
artifacts/drafts/neural_probe_analysis.tex
artifacts/c3_contingency_versions.tex
artifacts/exp-006/paper/c3_contingency_versions.tex
docs/paper/tables/tab_filtering_main.tex
docs/paper/tables/tab_alpha_sweep.tex
docs/paper/tables/tab_pairwise_significance.tex
docs/paper/tables/tab_crossscorer.tex
artifacts/dream_reports/dream_20260516T073047/best/paper.tex
artifacts/dream_reports/dream_20260516T073047/median/paper.tex
artifacts/dream_reports/dream_20260516T073047/worst/paper.tex
artifacts/_project/paper/theta_sensitivity_table.tex
artifacts/theta_sensitivity_table.tex
artifacts/_project/paper/tab_domain_model_kstar.tex
artifacts/_project/paper/tab_domain_model_kstar_full.tex
docs/paper/tables/tab_domain_model_kstar.tex
docs/paper/tables/tab_domain_model_kstar_full.tex
docs/paper/related_work.tex
docs/paper/experiments_c1.tex
docs/paper/method.tex
docs/paper/experiments_c3.tex
docs/paper/discussion.tex
docs/paper/introduction.tex
docs/paper/main.tex
docs/paper/conclusion.tex
docs/paper/appendix.tex
docs/paper/appendix_extended.tex
artifacts/dream_reports/dream_20260518T113009/best/paper.tex
artifacts/dream_reports/dream_20260518T113009/median/paper.tex
artifacts/dream_reports/dream_20260518T113009/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2291f98-4762-43d5-83c7-7b098ad5481f",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "0ddc985b-139e-4c9c-8fe7-a4269edbb519",
  "sourceToolAssistantUUID": "f2291f98-4762-43d5-83c7-7b098ad5481f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-18T12:09:58.178Z_

Now let me read the actual paper (the latest dream report and the main paper files).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ddc985b-139e-4c9c-8fe7-a4269edbb519",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1XiPFuUrWGFpZHwbLY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f19e5cf-1506-43a8-b13b-a5bef7b5ef7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGSRbhGDgjUyXg7FmbkTtt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5070,
      "cache_read_input_tokens": 40266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5070,
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

_source line 26 · 2026-05-18T12:09:59.715Z_

<details open><summary>🔧 Tool call — Read · `toolu_016pZ7E77king56pWPiLY9Pe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260518T113009/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f19e5cf-1506-43a8-b13b-a5bef7b5ef7b",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1XiPFuUrWGFpZHwbLY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43e96785-a734-45e8-81ff-854991b9578c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGSRbhGDgjUyXg7FmbkTtt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5070,
      "cache_read_input_tokens": 40266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5070,
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

_source line 27 · 2026-05-18T12:09:59.723Z_

<details><summary>↩ Tool result · `toolu_016pZ7E77king56pWPiLY9Pe`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage{times}
3	\usepackage{latexsym}
4	\usepackage{graphicx}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{xcolor}
10	\usepackage{subcaption}
11	\usepackage[T1]{fontenc}
12	\usepackage[utf8]{inputenc}
13	\usepackage[margin=1in]{geometry}
14	\usepackage{hyperref}
15	
16	\newcommand{\Kstar}{K^{*}}
17	
18	\title{Generational Depth Contamination Has a Bounded Discrimination Boundary:\\Measuring $K^{*}$ Across Domains, Models, and Decoding Strategies}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	Web-scale text corpora are increasingly contaminated by recursively generated synthetic text, where Large Language Model (LLM) outputs are fed back as inputs to produce multi-generational content. Current detection methods treat synthetic text as a binary category, ignoring the nonlinear quality degradation across generational depths. We formalize recursive generation as an iterated lossy channel and derive from the Data Processing Inequality (DPI) that a finite discrimination boundary $\Kstar$ must exist, beyond which successive generations become statistically indistinguishable. We then conduct the first systematic empirical measurement of $\Kstar$ across 8 model configurations (5 architecture families, 1B to 8B parameters), 3 source domains, and 4 decoding strategies. Our results reveal that $\Kstar \in \{1,2,3\}$ and is primarily determined by source domain complexity, forming a three-level hierarchy: Wikipedia saturates at $\Kstar=1$, web text at $\Kstar=2$ (7/8 configurations), and structured academic text at $\Kstar=3$ (5/5 domain-competent models). Cross-model transfer retains 80--92\% accuracy with scorer-invariant feature ordering ($\rho > 0.90$), confirming depth features are text-intrinsic. We validate that domain-appropriate $\Kstar$ predicts optimal data curation granularity: binary $\Kstar$-aware filtering outperforms graduated depth weighting and distribution matching baselines on downstream language modeling.
27	\end{abstract}
28	
29	\section{Introduction}
30	
31	Training corpora for large language models increasingly contain synthetic text produced by other LLMs. As these models are trained on web-scraped data and their outputs re-enter the web, a recursive feedback loop emerges: text generated at depth $d$ becomes training data that produces text at depth $d+1$. Public reports estimate that 20--35\% of recent web text is LLM-generated, and this proportion grows with each crawl cycle. The resulting multi-generational contamination degrades data quality in ways that binary human-vs-machine detection cannot capture.
32	
33	This problem matters for two reasons. First, the quality degradation across generational depths is nonlinear: a first-generation paraphrase may be nearly indistinguishable from human text, while a fourth-generation output exhibits measurable losses in vocabulary diversity and factual consistency. Second, current data curation pipelines lack tools to estimate generational depth, forcing practitioners into a coarse binary choice between keeping and discarding synthetic content. Distribution matching methods such as DSIR \cite{xie2023dsir} optimize for domain similarity without considering recursive contamination structure, while binary detectors \cite{mitchell2023detectgpt,bao2024diveye} provide no depth signal.
34	
35	Prior work on model collapse \cite{shumailov2024modelcollapse,alemohammad2024selfconsuming} demonstrates that iterative training on synthetic data causes progressive quality loss, and theoretical analyses \cite{dohmatob2024tale} characterize scaling behavior of this phenomenon. Binary machine-generated text detectors achieve high accuracy on the 0-vs-1 boundary but do not attempt to distinguish depth $d$ from depth $d+1$ for $d \geq 1$. Drayson et al.~\cite{drayson2025} apply binary detection scores as importance weights to mitigate model collapse during retraining. None of these approaches estimate how many recursive generation passes a text has undergone, nor do they characterize where depth discrimination becomes infeasible.
36	
37	We address this gap by formalizing recursive generation as an iterated lossy information channel. The Data Processing Inequality guarantees that mutual information between the source text and each successive generation is non-increasing, implying the existence of a finite boundary $\Kstar$ beyond which adjacent depths are statistically indistinguishable. We design a 15-dimensional model-free feature set based on surprisal statistics and train ordinal classifiers to measure pairwise discriminability between adjacent generational depths. We then conduct a controlled study across 8 model configurations (5 architecture families spanning 1B to 8B parameters), 3 source domains (C4 web text, Wikipedia, arXiv), and 4 decoding strategies to empirically characterize $\Kstar$.
38	
39	Our contributions are:
40	\begin{itemize}
41	\item We provide the first systematic empirical measurement of the generational discrimination boundary $\Kstar$, revealing it is bounded at $\Kstar \leq 3$ and primarily determined by source domain structural complexity, with a three-level hierarchy: Wikipedia ($\Kstar=1$), web text ($\Kstar=2$, 7/8 configurations), and structured academic text ($\Kstar=3$, 5/5 domain-competent models cross-validated across 4 architecture families).
42	\item We demonstrate that depth features are text-intrinsic through cross-model transfer (80--92\% accuracy retention), cross-scorer validation (11/12 generator$\times$scorer combinations yield consistent $\Kstar$), and scorer-invariant feature ordering ($\rho > 0.90$), confirming $\Kstar$ is governed by the generation process rather than the measurement apparatus.
43	\item We validate that domain-appropriate $\Kstar$ predicts optimal curation granularity: for web text ($\Kstar=2$), binary $\Kstar$-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892), surprisal-based selection (0.5894), and DSIR distribution matching ($\sim$0.5867).
44	\end{itemize}
45	
46	\section{Related Work}
47	
48	\paragraph{Model Collapse and Recursive Contamination.}
49	Shumailov et al.~\cite{shumailov2024modelcollapse} show that iteratively retraining language models on their own outputs leads to progressive distribution narrowing, a phenomenon termed model collapse. Alemohammad et al.~\cite{alemohammad2024selfconsuming} extend this analysis to self-consuming generative models, demonstrating quality degradation in images and text across generation loops. Dohmatob et al.~\cite{dohmatob2024tale} provide scaling-law analyses of collapse dynamics. These works characterize the macro-level phenomenon but do not provide detection tools for identifying the generational depth of individual documents. Our work complements this literature by measuring the empirical boundary at which depth discrimination saturates.
50	
51	\paragraph{Machine-Generated Text Detection.}
52	Binary detectors distinguish human from machine text using statistical divergence \cite{mitchell2023detectgpt}, vocabulary fingerprints \cite{bao2024diveye}, or minimum-$k$\% probability \cite{shi2024minkpp}. These methods achieve strong 0-vs-1 accuracy but do not differentiate among generational depths $d \geq 1$. Drayson et al.~\cite{drayson2025} use binary detection scores as importance weights during retraining to prevent model collapse. Our approach extends beyond binary classification to ordinal depth estimation, enabling finer-grained curation.
53	
54	\paragraph{Data Selection and Curation.}
55	DSIR \cite{xie2023dsir} selects pretraining data via distribution matching with a target corpus. D4 \cite{tirumala2024d4} and DoReMi \cite{xie2024doremi} optimize data mixing proportions for downstream performance. These methods operate on distributional properties without considering recursive generation depth. We show that $\Kstar$-aware filtering, informed by the measured discrimination boundary, provides a complementary and effective curation signal.
56	
57	\section{Method}
58	
59	\subsection{Problem Formulation}
60	
61	Let $X_0$ denote human-authored source text drawn from domain $\mathcal{D}$. We model recursive generation as an iterated channel: $X_d = G(X_{d-1})$ for $d = 1, 2, \ldots$, where $G$ is a generative model that takes text at depth $d{-}1$ as a prompt and produces a continuation or rewrite at depth $d$. By the Data Processing Inequality (DPI), the mutual information between the source and depth-$d$ text satisfies $I(X_0; X_d) \leq I(X_0; X_{d-1})$, so information about the original text is non-increasing with depth.
62	
63	We define the empirical discrimination boundary $\Kstar$ as the smallest depth $k$ such that a classifier cannot reliably distinguish depth-$k$ text from depth-$(k{+}1)$ text:
64	\begin{equation}
65	\Kstar = \min \{ k \geq 1 : \text{AUC}(k \text{ vs } k{+}1) < \theta \},
66	\end{equation}
67	where $\theta$ is a discrimination threshold. We set $\theta = 0.60$, corresponding to Cohen's $h \approx 0.20$ (small effect size). DPI guarantees that $\Kstar$ is finite for any lossy channel, but it does not constrain the magnitude. Measuring $\Kstar$ empirically is the central goal of this work.
68	
69	\subsection{Feature Design}
70	
71	We compute a 15-dimensional feature vector for each document using model-free surprisal statistics. For a given text $x$ and a reference language model $M$, we compute the per-token surprisal sequence $s_t = -\log p_M(x_t \mid x_{&lt;t})$. From this sequence we extract: (1) distributional moments (mean, variance, skewness, kurtosis); (2) tail statistics (fraction of tokens exceeding the 90th and 95th percentile of the reference model's training distribution); (3) rank-based features (mean and variance of token rank); (4) burstiness features (autocorrelation at lags 1--3 of the surprisal sequence); and (5) entropy rate estimates via sliding-window surprisal. These features are designed to capture the progressive narrowing of surprisal distributions predicted by DPI: as generation depth increases, the model ``washes out'' low-probability tokens, compressing the surprisal distribution toward its mode.
72	
73	The model-free design is motivated by the need for cross-model applicability. We validate this choice through cross-scorer experiments (\S\ref{sec:cross-model}) and comparison with neural probes (\S\ref{sec:neural-probe}).
74	
75	\subsection{Classifier and \texorpdfstring{$\Kstar$}{K*} Measurement Protocol}
76	
77	For each pair of adjacent depths $(d, d{+}1)$, we train an Ordered Bayesian Decision (OBD) classifier on LightGBM features to compute a pairwise AUC score. We use 5-fold stratified cross-validation with 10,000-resample bootstrap confidence intervals. The $\Kstar$ determination follows a sequential testing protocol: starting from depth pair (0,1), we test each successive pair until $\text{AUC}(k, k{+}1)$ falls below $\theta = 0.60$ with 95\% confidence (CI lower bound $< \theta$). The last pair with CI lower $> \theta$ determines $\Kstar$.
78	
79	\subsection{Data Generation Pipeline}
80	
81	We generate recursive text chains using a prompt-chain design: source documents from depth 0 are fed as prompts to produce depth-1 text, which in turn serves as prompts for depth-2 text, and so on up to depth 5. We use continuation mode as the canonical condition, where the model generates text that continues from the source. We also evaluate rewrite (instruction) mode as an ablation (\S\ref{sec:genmode}). For each configuration, we generate $n = 5{,}000$ documents per depth level.
82	
83	We evaluate 8 model configurations spanning 5 architecture families: Pythia-1.4B, OLMo-1B, Qwen-1.5B (base and instruct variants), Qwen-2.5-7B, LLaMA-3.1-8B, Mistral-7B, plus the Qwen-1.5B-Instruct rewrite pilot. Source domains are C4 (web text), Wikipedia, and arXiv. Decoding strategies include greedy, nucleus ($p=0.9$), and temperature sampling ($T \in \{0.7, 1.2\}$).
84	
85	\section{Experiments}
86	
87	\subsection{K* Characterization on Web Text (C4)}
88	\label{sec:webtext}
89	
90	Table~\ref{tab:kstar-c4} reports the 1-vs-2 pairwise AUC for all 8 model configurations on C4 web text in continuation mode. Seven of eight configurations yield $\Kstar = 2$: the 1-vs-2 AUC CI lower bound exceeds $\theta = 0.60$ in each case, while all 2-vs-3 comparisons fall below the threshold. The single exception is Mistral-7B, where 1-vs-2 AUC CI lower is 0.5835, yielding $\Kstar = 1$; we analyze this case in \S\ref{sec:mistral}.
91	
92	\begin{table}[t]
93	\centering
94	\small
95	\begin{tabular}{lcccc}
96	\toprule
97	\textbf{Model} & \textbf{AUC 1v2} & \textbf{95\% CI} & \textbf{CI low $> \theta$?} & $\Kstar$ \\
98	\midrule
99	Qwen-1.5B rw & 0.696 & [0.686, 0.704] & \checkmark (+8.6pp) & 2 \\
100	Pythia-1.4B & 0.654 & [0.645, 0.663] & \checkmark (+4.5pp) & 2 \\
101	Qwen-1.5B base & 0.626 & [0.617, 0.635] & \checkmark (+1.7pp) & 2 \\
102	Qwen-2.5-7B & 0.618 & [0.608, 0.626] & \checkmark (+0.8pp) & 2 \\
103	OLMo-1B & 0.615 & [0.605, 0.625] & \checkmark (+0.5pp) & 2 \\
104	LLaMA-3.1-8B & 0.612 & [0.603, 0.622] & \checkmark (+0.3pp) & 2 \\
105	Qwen-1.5B inst & 0.611 & [0.602, 0.621] & \checkmark (+0.2pp) & 2 \\
106	\midrule
107	Mistral-7B & 0.594 & [0.584, 0.603] & \texttimes & 1 \\
108	\bottomrule
109	\end{tabular}
110	\caption{1-vs-2 pairwise AUC on C4 web text (continuation mode). $\theta = 0.60$. All 2-vs-3 AUC CI upper bounds fall below 0.60, confirming $\Kstar = 2$ for the seven passing configurations. Qwen-1.5B rewrite (rw) is included for comparison but is not part of the canonical continuation-mode evaluation.}
111	\label{tab:kstar-c4}
112	\end{table}
113	
114	Decoding strategy does not alter $\Kstar$. Table~\ref{tab:decoding} shows that all four strategies yield $\Kstar = 2$ for Qwen-1.5B rewrite, with 1-vs-2 AUC in the narrow range [0.687, 0.704].
115	
116	\begin{table}[t]
117	\centering
118	\small
119	\begin{tabular}{lcc}
120	\toprule
121	\textbf{Decoding} & \textbf{AUC 1v2} & $\Kstar$ \\
122	\midrule
123	Greedy & 0.689 & 2 \\
124	Nucleus $p{=}0.9$ & 0.687 & 2 \\
125	Temperature 0.7 & 0.689 & 2 \\
126	Temperature 1.2 & 0.704 & 2 \\
127	\bottomrule
128	\end{tabular}
129	\caption{Decoding strategy invariance of $\Kstar$ (Qwen-1.5B rewrite on C4). All strategies produce $\Kstar = 2$.}
130	\label{tab:decoding}
131	\end{table}
132	
133	\subsection{Domain Dependence: A Three-Level Hierarchy}
134	\label{sec:domain}
135	
136	We evaluate $\Kstar$ across three source domains to test whether domain structural complexity modulates the discrimination boundary.
137	
138	\paragraph{arXiv ($\Kstar = 3$).} Five model configurations across four architecture families yield $\Kstar = 3$ on arXiv text (Table~\ref{tab:arxiv}). The 2-vs-3 pairwise AUC ranges from 0.622 to 0.654, with all CI lower bounds exceeding 0.60. The structured features of academic text (LaTeX formatting, citation patterns, mathematical notation) provide additional depth-distinguishing signal that extends the discrimination boundary by one generation beyond web text. OLMo-1B is excluded from this count due to a capacity failure: it generates fully out-of-domain text on arXiv prompts, which we analyze in the appendix.
139	
140	\begin{table}[t]
141	\centering
142	\small
143	\begin{tabular}{lccc}
144	\toprule
145	\textbf{Model} & \textbf{AUC 2v3} & \textbf{CI lower} & $\Kstar$ \\
146	\midrule
147	Pythia-1.4B & 0.654 & 0.640 & 3 \\
148	Qwen-1.5B & 0.643 & 0.628 & 3 \\
149	Mistral-7B & 0.628 & 0.614 & 3 \\
150	Qwen-2.5-7B & 0.626 & 0.612 & 3 \\
151	LLaMA-3.1-8B & 0.622 & 0.608 & 3 \\
152	\bottomrule
153	\end{tabular}
154	\caption{2-vs-3 pairwise AUC on arXiv (continuation mode). All five domain-competent models yield $\Kstar = 3$, cross-validated across four architecture families.}
155	\label{tab:arxiv}
156	\end{table}
157	
158	\paragraph{Wikipedia ($\Kstar = 1$).} All six evaluated models yield $\Kstar = 1$ on Wikipedia after controlling for scorer family bias. The 1-vs-2 AUC CI lower falls below 0.60 for all cross-family scorer evaluations. An initial finding of $\Kstar = 2$ for Qwen-generated Wikipedia text was traced to a same-family scorer artifact: when Qwen-family models score Qwen-generated text, shared vocabulary biases inflate the 1-vs-2 AUC by approximately 1 point. Using Pythia as a cross-family scorer eliminates this inflation, confirming $\Kstar = 1$.
159	
160	\paragraph{Domain hierarchy summary.} The resulting three-level hierarchy, Wikipedia ($\Kstar = 1$) $<$ C4 web text ($\Kstar = 2$) $<$ arXiv ($\Kstar = 3$), demonstrates that source domain structural complexity is the primary determinant of $\Kstar$. The strongest evidence for domain dependence comes from Mistral-7B, which yields $\Kstar = 1$ on C4 but $\Kstar = 3$ on arXiv, a within-model shift that rules out model identity as the driving factor.
161	
162	\subsection{Cross-Model Transfer and Scorer Invariance}
163	\label{sec:cross-model}
164	
165	To verify that $\Kstar$ reflects text-intrinsic properties rather than model-specific artifacts, we conduct two transfer experiments. First, cross-model accuracy transfer between Pythia and OLMo retains 90--92\% of within-model accuracy, and 0-vs-1 AUC exceeds 0.96 across all transfer pairs, indicating the binary contamination signal transfers perfectly. Second, a cross-scorer validation using 11 out of 12 generator$\times$scorer combinations yields $\Kstar = 2$ on C4. Feature importance rankings across scorers show Spearman $\rho > 0.90$. These results confirm that $\Kstar$ is governed by the generation process, not the scoring model.
166	
167	\subsection{Mistral One-Wash Effect}
168	\label{sec:mistral}
169	
170	Mistral-7B achieves $\Kstar = 1$ on C4 web text: a single generation pass renders its output statistically indistinguishable from deeper generations. Cross-scorer validation confirms this is text-intrinsic, not a scorer artifact. Yet the same model yields $\Kstar = 3$ on arXiv. This domain-specific one-wash effect is the clearest demonstration that $\Kstar$ is a joint property of the model and source domain, not of the model alone. For homogeneous web text, Mistral's generation process erases depth-distinguishing structure in a single pass; for structured academic text, the additional formatting and notation signals rescue depth discriminability for two additional generations.
171	
172	\subsection{Neural Probe Comparison}
173	\label{sec:neural-probe}
174	
175	We compare our 15-dimensional model-free features against neural probes that use frozen self-embeddings with an MLP classifier. Neural probe $\Kstar$ is model-dependent: Qwen yields $\Kstar_\text{neural} = 3$ (2-vs-3 AUC = 0.616, CI lower = 0.610), while Pythia and OLMo both yield $\Kstar_\text{neural} = 2$ (2-vs-3 AUC of 0.596 and 0.589, respectively, with CI lower below 0.60). In contrast, the model-free features produce consistent $\Kstar$ across all models. This discrepancy highlights an interpretability-deployability tradeoff: neural probes can extract model-specific depth signal beyond the model-free boundary, but this additional signal does not generalize across architectures. The model-free approach is preferable for cross-model characterization.
176	
177	\subsection{Generation Mode Analysis}
178	\label{sec:genmode}
179	
180	Signal strength differs substantially between generation modes. Rewrite mode achieves 1-vs-2 AUC of 0.696, compared to 0.611 for continuation mode on the same model (Qwen-1.5B-Instruct). This 8.4-percentage-point gap arises because instruction-following in rewrite mode introduces systematic style artifacts that amplify the depth signal. However, cross-model transferability is markedly lower for rewrite features: continuation mode retains 80--92\% accuracy in transfer, while rewrite retains only 61--63\%. The asymmetric transfer pattern (continuation$\to$rewrite: 89\%, rewrite$\to$continuation: 82\%) indicates that continuation features form a universal subset of rewrite features. We therefore adopt continuation mode as the canonical condition for cross-model claims, with rewrite mode reported as an upper-bound ablation.
181	
182	\subsection{Threshold Sensitivity}
183	
184	We evaluate $\Kstar$ across a threshold range $\theta \in [0.55, 0.70]$. At $\theta = 0.55$, all configurations yield $\Kstar \geq 2$. At $\theta = 0.70$, most configurations drop to $\Kstar = 1$, reflecting the stringent discrimination criterion. The AUC gap between the boundary pair and the next pair exhibits a sharp discontinuity: for C4, the 1-vs-2 to 2-vs-3 AUC drop ranges from 2 to 7 percentage points across models, making the $\Kstar$ determination robust to moderate threshold variation. Our choice of $\theta = 0.60$ aligns with Cohen's $h \approx 0.20$ (small effect size) and is further validated by permutation test calibration.
185	
186	\subsection{K*-Aware Data Curation}
187	\label{sec:curation}
188	
189	We test whether the measured $\Kstar$ provides actionable guidance for data curation. For C4 web text ($\Kstar = 2$), we compare four curation strategies applied to a pretraining corpus with controlled contamination at 10\%, 30\%, and 50\% synthetic content:
190	
191	\begin{itemize}
192	\item \textbf{Binary $\Kstar$-aware filtering}: remove documents classified as depth $\geq 1$.
193	\item \textbf{Graduated depth weighting}: assign weights inversely proportional to predicted depth, with sensitivity parameter $\alpha \in \{0.5, 0.7, 0.9, 1.0\}$.
194	\item \textbf{Surprisal-based selection}: select documents with surprisal statistics closest to the reference human distribution.
195	\item \textbf{DSIR distribution matching}: importance resampling to match target domain statistics.
196	\end{itemize}
197	
198	Each configuration is evaluated with 5 random seeds on downstream MMLU and HellaSwag benchmarks. Table~\ref{tab:curation} reports results at 30\% contamination (the moderate regime).
199	
200	\begin{table}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43e96785-a734-45e8-81ff-854991b9578c",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "1909017b-0519-44ea-9aab-d99b2957731b",
  "sourceToolAssistantUUID": "43e96785-a734-45e8-81ff-854991b9578c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-18T12:10:00.311Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YaTo1VVQGKe5STj4pAYAbf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1909017b-0519-44ea-9aab-d99b2957731b",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1XiPFuUrWGFpZHwbLY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b5b13de-750b-438f-a52b-e269d4579502",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGSRbhGDgjUyXg7FmbkTtt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5070,
      "cache_read_input_tokens": 40266,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5070
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 40266,
          "cache_creation_input_tokens": 5070,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5070,
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

_source line 29 · 2026-05-18T12:10:00.319Z_

<details><summary>↩ Tool result · `toolu_01YaTo1VVQGKe5STj4pAYAbf`</summary>

```text
1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage[section]{placeins}
18	
19	\newcommand{\Kstar}{{K^*}}
20	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
21	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
22	\newcommand{\auc}{\text{AUC}}
23	\newcommand{\jsd}{\text{JSD}}
24	
25	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	% === Abstract ===
33	\begin{abstract}
34	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
35	We measure the discrimination boundary $\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable) using 15 statistical features and an OBD-LightGBM classifier.
36	Across five architecture families (1B--14B), three source domains, and four decoding strategies at $\theta{=}0.60$, $\Kempirical{=}2$ for general web text (8/9 model configurations) and $\Kempirical{=}3$ for structured academic text (arXiv).
37	A single generation pass suffices to render general web text indistinguishable from deeper synthetic content, a \emph{one-wash laundering} effect.
38	Generator-independent statistical features, computed via a fixed reference scorer, enable 80--92\% accuracy retention among continuation-mode generators, and cross-scorer validation is consistent with $\Kempirical$ being governed by the generation process rather than the scoring model.
39	Downstream, domain-appropriate $\Kempirical$ correctly predicts optimal curation granularity: when contamination causes detectable quality loss, binary filtering minimizes degradation most effectively for web text.
40	\end{abstract}
41	
42	% === Section 1: Introduction ===
43	\input{introduction}
44	
45	% === Section 2: Related Work ===
46	\input{related_work}
47	
48	% === Section 3: Method ===
49	\input{method}
50	
51	% === Section 4: Experiments ===
52	\input{experiments_c1}
53	
54	% === Section 5: K*-Aware Data Filtering ===
55	\input{experiments_c3}
56	
57	% === Section 6: Discussion ===
58	\input{discussion}
59	
60	% === Section 7: Conclusion ===
61	\input{conclusion}
62	
63	% === Limitations (ACL required, unnumbered) ===
64	\clearpage
65	\section*{Limitations}
66	
67	Our findings are bounded by:
68	(1)~\emph{Scope}: model scale $\leq$14B (5 architecture families), English text (C4, Wikipedia, arXiv), four decoding strategies; arXiv $\Kempirical{=}3$ is confirmed with five models across four architecture families but with reduced sample size ($n{=}2{,}200$ per model).
69	(2)~\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\Kempirical{\geq}4$ (Pythia-1.4B LoRA; Appendix~\ref{sec:extended_limitations}), so prompt-chain $\Kempirical$ may underestimate discriminability in mixed settings.
70	(3)~\emph{Threshold}: $\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; 8/9 configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (Mistral-7B: $\Kempirical{=}1$).
71	(4)~\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.002; cross-scorer validation drops this to $\Kempirical{=}1$ (Section~\ref{sec:transfer}). LLaMA-3.1-8B represents the most marginal $\Kempirical{=}2$ assignment, with the 1v2 CI lower bound within 0.3 percentage points of $\theta$.
72	(5)~\emph{Feature set}: the 15D features yield a feature-set-specific lower bound ($\Ktheory$ may be strictly higher); neural probe $\Kempirical$ is model-dependent ($3$ for Qwen, $2$ for Pythia/OLMo).
73	(6)~\emph{Segment length}: $\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \theta$); 512 tokens yields point estimate $\Kempirical{=}2$ but CI lower marginally below $\theta$ ($0.5979$), indicating the boundary weakens at longer generation lengths.
74	(7)~\emph{Curation applicability}: the filtering evaluation is validated on two architectures (Qwen2.5-1.5B-Instruct and Pythia-1.4B) with consistent strategy ordering (Appendix~\ref{sec:pythia_filtering}), though absolute improvement remains small and effect sizes diminish at lower contamination ratios (10--50\%; Appendix~\ref{sec:dose_response}).
75	(8)~\emph{Family balance}: the Qwen2.5 family provides 5/9 configurations; though spanning three scales (1.5B, 7B, 14B) and two training variants (base, instruct), aggregate statistics weight this family more heavily than the four single-configuration families.
76	Additional limitations (cross-model scoring sensitivity, feature ranking variability at the 1v2 boundary, structural composition confound analysis) appear in Appendix~\ref{sec:extended_limitations}.
77	
78	% === Ethics Statement (ACL required, unnumbered) ===
79	\section*{Ethics Statement}
80	
81	Generational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.
82	Our experiments use publicly available corpora (C4, Wikipedia, arXiv abstracts) and do not involve personally identifiable information.
83	A potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\auc \geq 0.96$ at 0v1) remains robust.
84	Code and generated corpora will be released upon acceptance to enable reproducibility.
85	
86	\bibliography{references}
87	
88	\input{appendix}
89	\input{appendix_extended}
90	
91	\end{document}
92	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b5b13de-750b-438f-a52b-e269d4579502",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "49f81112-70af-44a8-b61c-f01ad8f036e7",
  "sourceToolAssistantUUID": "7b5b13de-750b-438f-a52b-e269d4579502",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-18T12:10:06.610Z_

<details open><summary>🔧 Tool call — Read · `toolu_013Yr2pPjNRYAYRZJTHEta3x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260518T113009/best/paper.tex",
  "offset": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49f81112-70af-44a8-b61c-f01ad8f036e7",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1YK5pq5NTKymfRHMUU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d7f7b6b-77eb-4589-afb8-da884260bb65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017PovqjMAqtCcJ958GX6ofV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9111,
      "cache_read_input_tokens": 45336,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9111
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 45336,
          "cache_creation_input_tokens": 9111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9111,
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

_source line 31 · 2026-05-18T12:10:06.624Z_

<details><summary>↩ Tool result · `toolu_013Yr2pPjNRYAYRZJTHEta3x`</summary>

```text
200	\begin{table}[t]
201	\centering
202	\small
203	\begin{tabular}{lcc}
204	\toprule
205	\textbf{Strategy} & \textbf{MMLU} & \textbf{HellaSwag} \\
206	\midrule
207	No filtering & 0.5865 & 0.5812 \\
208	DSIR matching & 0.5867 & 0.5830 \\
209	Surprisal selection & 0.5894 & 0.5856 \\
210	Graduated ($\alpha{=}0.9$) & 0.5892 & 0.5848 \\
211	Binary $\Kstar$-aware & \textbf{0.5941} & \textbf{0.5901} \\
212	\bottomrule
213	\end{tabular}
214	\caption{Downstream performance at 30\% contamination ratio (mean over 5 seeds). Binary $\Kstar$-aware filtering outperforms all baselines. HellaSwag differences are significant ($p \leq 0.004$) at all contamination ratios; MMLU at 30\% shows a directional advantage ($p = 0.074$).}
215	\label{tab:curation}
216	\end{table}
217	
218	Binary $\Kstar$-aware filtering achieves the best performance on both metrics. The key insight is that because $\Kstar = 2$ for web text, a binary depth cut at the $\Kstar$ boundary captures the primary discrimination signal. Graduated weighting, which assumes useful signal beyond the $\Kstar$ boundary, adds noise from unreliable depth estimates at higher depths and collapses to baseline performance. Dose-response analysis across 10\%, 30\%, and 50\% contamination ratios confirms that binary filtering maintains a consistent advantage, with HellaSwag improvements significant at all levels ($p \leq 0.004$).
219	
220	\subsection{Prompt-Chain vs. Retrain-Chain}
221	
222	A natural concern is whether prompt-chain generation captures the dynamics of real-world recursive contamination, where models are retrained on their own outputs. We compare against a retrain-chain experiment using Pythia-1.4B with LoRA fine-tuning at each generation. The retrain-chain yields $\Kstar \geq 4$, with 1-vs-2 AUC of 0.948, 2-vs-3 AUC of 0.889, and 3-vs-4 AUC of 0.798. The dramatically higher discriminability arises because each LoRA fine-tuning step introduces cumulative model-specific artifacts (vocabulary narrowing, repetition bias) that make each generation highly distinguishable. These artifacts are specific to the training setup and do not generalize to wild contamination scenarios. Prompt-chain $\Kstar = 2$ reflects text-intrinsic information loss only and provides the operationally relevant lower bound for data curation.
223	
224	\section{Discussion}
225	
226	The central finding of this work is that generational depth discrimination saturates rapidly: $\Kstar \leq 3$ across all tested conditions, with web text saturating at $\Kstar = 2$ in seven of eight model configurations. This ``one-wash laundering'' effect means that for general web text, a single generation pass is sufficient to make synthetic content indistinguishable from deeper recursive generations. The practical consequence is that depth-aware data curation beyond the binary boundary provides diminishing returns for web text, a finding validated by our curation experiments.
227	
228	The domain dependence of $\Kstar$ is perhaps the most nuanced finding. Structured text with distinctive formatting conventions (arXiv LaTeX, mathematical notation, citation patterns) provides additional depth-distinguishing signal that extends the discrimination boundary. This suggests that domain-specific curation strategies may be warranted: while binary filtering suffices for web text, academic text corpora may benefit from finer-grained depth estimation. The Mistral C4-to-arXiv $\Kstar$ shift (1 to 3) provides the most direct evidence that domain structure, not model identity, drives this effect.
229	
230	Several limitations merit discussion. Our evaluation covers models up to 8B parameters across five architecture families. DPI guarantees that a finite $\Kstar$ exists for any model scale, and cross-scorer invariance suggests the result generalizes, but direct measurement on 13B+ and 70B+ models remains important future work. The choice of $\theta = 0.60$ influences the absolute $\Kstar$ values; our sensitivity analysis shows the qualitative domain hierarchy is robust, but the specific numbers shift with the threshold. Finally, prompt-chain generation is a controlled approximation of real-world recursive contamination. Our retrain-chain comparison suggests that prompt-chain $\Kstar$ provides a conservative lower bound, since model retraining introduces additional distinguishable artifacts.
231	
232	\section{Conclusion}
233	
234	We introduced $\Kstar$, the generational discrimination boundary, as a measurable quantity for recursive synthetic text contamination. Through systematic experiments across 8 model configurations, 3 domains, and 4 decoding strategies, we established that $\Kstar$ is bounded at $\leq 3$ and determined primarily by source domain complexity. This finding has direct implications for data governance: binary $\Kstar$-aware filtering, informed by the domain-specific discrimination boundary, provides an effective and principled curation strategy. We release our feature extraction pipeline and evaluation framework to support further research on multi-generational contamination.
235	
236	\appendix
237	
238	\section{Naturalistic Common Crawl Validation}
239	\label{app:cc-validation}
240	
241	To assess whether our controlled findings extend to web-scale data, we apply the trained 15D feature + OBD-LightGBM pipeline to Common Crawl snapshots from 2025-03 and 2026-01 ($n = 10{,}000$ documents each, excluding documents shorter than 100 tokens).
242	
243	\paragraph{Depth distribution shift.} Table~\ref{tab:cc-depth} shows predicted depth distributions across both snapshots. The proportion of documents predicted as depth 0 (human-authored) decreases from 64.0\% to 51.0\% between snapshots, while all predicted synthetic depth bins increase. The mean predicted depth rises from 0.57 to 0.81 ($\Delta = +0.24$, Mann-Whitney $U$ $p < 0.001$, Cohen's $d = 0.31$). This shift is directionally consistent with the growing LLM penetration rate documented by commercial detection services.
244	
245	\begin{table}[t]
246	\centering
247	\small
248	\begin{tabular}{lccc}
249	\toprule
250	\textbf{Pred. Depth} & \textbf{CC 2025-03 (\%)} & \textbf{CC 2026-01 (\%)} & \textbf{$\Delta$ (pp)} \\
251	\midrule
252	0 (human) & 64.0 & 51.0 & $-$13.0 \\
253	1 & 22.0 & 28.0 & +6.0 \\
254	2 & 9.0 & 13.0 & +4.0 \\
255	3 & 3.0 & 5.0 & +2.0 \\
256	$\geq 4$ & 2.0 & 3.0 & +1.0 \\
257	\midrule
258	Mean depth & 0.57 & 0.81 & +0.24*** \\
259	\bottomrule
260	\end{tabular}
261	\caption{Predicted depth distributions on Common Crawl snapshots ($n = 10{,}000$ per snapshot). The year-over-year shift toward higher predicted depths is significant (Mann-Whitney $U$, $p < 0.001$, Cohen's $d = 0.31$).}
262	\label{tab:cc-depth}
263	\end{table}
264	
265	\paragraph{Correlation with quality metrics.} We compute Spearman rank correlations between predicted depth and three independent text quality indicators: AlignScore (self-reference factual consistency), type-token ratio (TTR), and unique trigram ratio. As shown in Table~\ref{tab:cc-corr}, all correlations are significant and in the expected direction: higher predicted depth is associated with lower factual consistency ($\rho = -0.32$), lower vocabulary diversity ($\rho = -0.27$ for TTR, $\rho = -0.24$ for unique trigram ratio), and higher lexical repetitiveness (Yule's K, $\rho = +0.21$).
266	
267	\begin{table}[t]
268	\centering
269	\small
270	\begin{tabular}{lcc}
271	\toprule
272	\textbf{Metric Pair} & \textbf{Spearman $\rho$} & $p$ \\
273	\midrule
274	Pred. depth $\times$ AlignScore & $-$0.32 & $<$0.001 \\
275	Pred. depth $\times$ TTR & $-$0.27 & $<$0.001 \\
276	Pred. depth $\times$ Uniq. trigram ratio & $-$0.24 & $<$0.001 \\
277	Pred. depth $\times$ Yule's K & +0.21 & $<$0.001 \\
278	AlignScore $\times$ TTR (reference) & +0.41 & $<$0.001 \\
279	\bottomrule
280	\end{tabular}
281	\caption{Spearman correlations between predicted depth and quality metrics ($n = 20{,}000$). All correlations significant at $p < 0.001$.}
282	\label{tab:cc-corr}
283	\end{table}
284	
285	\paragraph{Monotonic quality degradation.} Table~\ref{tab:cc-quality} reports mean quality metrics by predicted depth bin. All three quality indicators decrease monotonically with predicted depth (Jonckheere-Terpstra test, $p < 0.001$). The largest drop occurs between depth 0 and depth 1 (AlignScore: 0.782 to 0.741, a 4.1 percentage point decrease), with diminishing incremental degradation at higher depths. This pattern is consistent with the one-wash effect observed in controlled experiments and with the DPI prediction that information loss is greatest in the first generation pass.
286	
287	\begin{table}[t]
288	\centering
289	\small
290	\begin{tabular}{lcccc}
291	\toprule
292	\textbf{Pred. Depth} & $n$ & \textbf{AlignScore} & \textbf{TTR} & \textbf{Uniq. Tri. Ratio} \\
293	\midrule
294	0 & $\sim$11,500 & 0.782$\pm$0.08 & 0.423$\pm$0.05 & 0.612$\pm$0.06 \\
295	1 & $\sim$5,000 & 0.741$\pm$0.09 & 0.398$\pm$0.05 & 0.578$\pm$0.06 \\
296	2 & $\sim$2,200 & 0.718$\pm$0.10 & 0.381$\pm$0.06 & 0.553$\pm$0.07 \\
297	3 & $\sim$800 & 0.693$\pm$0.11 & 0.370$\pm$0.06 & 0.534$\pm$0.07 \\
298	$\geq 4$ & $\sim$500 & 0.679$\pm$0.12 & 0.362$\pm$0.07 & 0.521$\pm$0.08 \\
299	\bottomrule
300	\end{tabular}
301	\caption{Mean quality metrics by predicted depth bin ($n = 20{,}000$ combined). Monotonic decrease confirmed by Jonckheere-Terpstra test ($p < 0.001$ for all metrics).}
302	\label{tab:cc-quality}
303	\end{table}
304	
305	The absence of ground-truth depth labels for wild data is an inherent limitation; observed correlations reflect the joint contribution of classifier accuracy and the true depth-quality relationship. The directional consistency with our controlled findings provides ecological plausibility.
306	
307	\section{Subsampling Power Analysis}
308	\label{app:power}
309	
310	We assess whether our sample size of $n = 5{,}000$ per depth is sufficient for reliable $\Kstar$ determination by conducting a subsampling power analysis. From the full C4 dataset, we draw without-replacement subsamples at $n \in \{1{,}000,\; 2{,}000,\; 3{,}000,\; 4{,}000,\; 5{,}000\}$ (preserving depth proportions) with 10 independent resamples per $n$. For each subsample, we compute the 1-vs-2 AUC with 95\% bootstrap confidence intervals and record whether $\Kstar = 2$ is determined (CI lower $> 0.60$).
311	
312	\paragraph{Determination rate by sample size.} Table~\ref{tab:power-rate} reports the $\Kstar = 2$ determination rate across sample sizes and models. Pythia-1.4B, with the largest effect size (AUC margin of 5.4 percentage points above $\theta$), achieves 10/10 at all sample sizes, including $n = 1{,}000$. OLMo-1B and LLaMA-3.1-8B, with moderate margins (3--5pp), reach 80\% power at $n = 4{,}000$. Qwen-1.5B-Instruct (continuation), the configuration with the smallest margin (1.5pp above $\theta$), requires the full $n = 5{,}000$ for reliable determination.
313	
314	\begin{table}[t]
315	\centering
316	\small
317	\begin{tabular}{lccccc}
318	\toprule
319	$n$ & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} & \textbf{LLaMA} & \textbf{$\geq$3/4 pass} \\
320	\midrule
321	1,000 & 10/10 & 2/10 & 1/10 & 2/10 & No \\
322	2,000 & 10/10 & 4/10 & 2/10 & 3/10 & No \\
323	3,000 & 10/10 & 6/10 & 4/10 & 5/10 & No \\
324	4,000 & 10/10 & 9/10 & 5/10 & 8/10 & Yes (3/4) \\
325	5,000 & 10/10 & 10/10 & 10/10$^\dagger$ & 10/10 & Yes (4/4) \\
326	\bottomrule
327	\end{tabular}
328	\caption{$\Kstar = 2$ determination rate (out of 10 resamples) by sample size and model. $^\dagger n = 5{,}000$ is the full dataset; result is deterministic.}
329	\label{tab:power-rate}
330	\end{table}
331	
332	\paragraph{AUC stability and CI width.} Table~\ref{tab:power-auc} reports mean AUC estimates and CI widths. Point estimates are stable across all sample sizes (variation $< 0.001$ AUC), confirming that the subsample means are unbiased. CI width scales as expected with $1/\sqrt{n}$: approximately 0.04 at $n = 1{,}000$ and 0.02 at $n = 5{,}000$, with near-identical widths across models at each $n$ (cross-model variation $< 0.003$). This confirms that CI width is a purely sample-size-driven statistical property, and that the power differences across models arise entirely from the distance between the AUC point estimate and $\theta$.
333	
334	\begin{table}[t]
335	\centering
336	\small
337	\begin{tabular}{lcccc}
338	\toprule
339	$n$ & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} & \textbf{LLaMA} \\
340	\midrule
341	1k & .654 (.039) & .615 (.045) & .611 (.044) & .612 (.042) \\
342	2k & .654 (.028) & .614 (.032) & .611 (.031) & .612 (.030) \\
343	3k & .654 (.023) & .615 (.026) & .611 (.026) & .612 (.024) \\
344	4k & .654 (.020) & .615 (.023) & .611 (.022) & .612 (.021) \\
345	5k & .654 (.018) & .615 (.020) & .611 (.020) & .612 (.019) \\
346	\bottomrule
347	\end{tabular}
348	\caption{Mean 1-vs-2 AUC and CI width (in parentheses) by sample size. Format: AUC (CI width). Point estimates are stable across $n$; CI width differences across models are negligible.}
349	\label{tab:power-auc}
350	\end{table}
351	
352	\paragraph{Minimum sample size by effect size.} The relationship between required sample size and effect size follows the expected $n_\text{min} \propto 1/(\text{AUC} - \theta)^2$ scaling. Table~\ref{tab:power-min} summarizes the minimum $n$ for 80\% power by effect size category. For researchers replicating this work, models with Pythia-class effect sizes ($>$4pp above $\theta$) require only $n \geq 1{,}000$; moderate-effect models (OLMo, LLaMA) need $n \geq 4{,}000$; marginal-effect models (Qwen-cont class) need $n \geq 5{,}000$. The current experimental design with $n = 5{,}000$ per depth achieves full coverage across all tested models.
353	
354	\begin{table}[t]
355	\centering
356	\small
357	\begin{tabular}{llcc}
358	\toprule
359	\textbf{Effect Category} & \textbf{Model} & \textbf{AUC $-$ $\theta$ (pp)} & \textbf{Min $n$} \\
360	\midrule
361	Large ($>$4pp) & Pythia-1.4B & 5.4 & $\leq$1,000 \\
362	Medium (3--5pp) & OLMo / LLaMA & 1.5--4.5 & 4,000 \\
363	Small (1--2pp) & Qwen-cont & 1.1 & 5,000$^\dagger$ \\
364	\bottomrule
365	\end{tabular}
366	\caption{Minimum $n$ per depth for 80\% $\Kstar = 2$ determination power. $^\dagger$Qwen-cont passes deterministically at $n = 5{,}000$ (full data); probabilistic 80\% power extrapolates to $n \approx 6{,}000$--$7{,}000$.}
367	\label{tab:power-min}
368	\end{table}
369	
370	\begin{thebibliography}{10}
371	
372	\bibitem{alemohammad2024selfconsuming}
373	S.~Alemohammad, J.~Casco-Rodriguez, L.~Luzi, A.~I.~Humayun, H.~Babaei, D.~LeJeune, A.~Siahkoohi, and R.~G.~Baraniuk.
374	\newblock Self-consuming generative models go MAD.
375	\newblock In \emph{ICLR}, 2024.
376	
377	\bibitem{bao2024diveye}
378	G.~Bao, Y.~Zhao, Z.~Teng, L.~Yang, and Y.~Zhang.
379	\newblock DivEye: Divergence-based machine-generated text detection.
380	\newblock In \emph{Findings of ACL}, 2024.
381	
382	\bibitem{dohmatob2024tale}
383	E.~Dohmatob, Y.~Feng, and J.~Kempe.
384	\newblock A tale of tails: Model collapse as a change of scaling laws.
385	\newblock In \emph{ICML}, 2024.
386	
387	\bibitem{drayson2025}
388	T.~Drayson, L.~Griffin, and I.~Sheremetov.
389	\newblock Preventing model collapse with data filtering.
390	\newblock \emph{arXiv preprint}, 2025.
391	
392	\bibitem{mitchell2023detectgpt}
393	E.~Mitchell, Y.~Lee, A.~Khazatsky, C.~D.~Manning, and C.~Finn.
394	\newblock DetectGPT: Zero-shot machine-generated text detection using probability curvature.
395	\newblock In \emph{ICML}, 2023.
396	
397	\bibitem{shi2024minkpp}
398	Z.~Shi, Y.~Wang, and M.~Wang.
399	\newblock Min-K\%++: Improved baseline for detecting pre-training data from large language models.
400	\newblock In \emph{EMNLP}, 2024.
401	
402	\bibitem{shumailov2024modelcollapse}
403	I.~Shumailov, Z.~Shumaylov, Y.~Zhao, N.~Papernot, R.~Anderson, and Y.~Gal.
404	\newblock AI models collapse when trained on recursively generated data.
405	\newblock \emph{Nature}, 631:755--759, 2024.
406	
407	\bibitem{tirumala2024d4}
408	K.~Tirumala, D.~Simig, A.~Aghajanyan, and A.~Morcos.
409	\newblock D4: Improving LLM pretraining via document de-duplication and diversification.
410	\newblock In \emph{NeurIPS}, 2024.
411	
412	\bibitem{xie2023dsir}
413	S.~M.~Xie, S.~Santurkar, T.~Ma, and P.~Liang.
414	\newblock Data selection with importance resampling.
415	\newblock In \emph{ICML}, 2023.
416	
417	\bibitem{xie2024doremi}
418	S.~M.~Xie, H.~Pham, X.~Dong, N.~Du, H.~Liu, Y.~Lu, P.~Liang, Q.~V.~Le, T.~Ma, and A.~W.~Yu.
419	\newblock DoReMi: Optimizing data mixtures speeds up language model pretraining.
420	\newblock In \emph{NeurIPS}, 2024.
421	
422	\end{thebibliography}
423	
424	\end{document}
425	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d7f7b6b-77eb-4589-afb8-da884260bb65",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "757783cd-0b07-487b-8523-1cced110252d",
  "sourceToolAssistantUUID": "4d7f7b6b-77eb-4589-afb8-da884260bb65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-18T12:10:11.373Z_

Now let me read the actual paper sections from the docs/paper directory to understand the full paper structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "757783cd-0b07-487b-8523-1cced110252d",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1YnDiazzhxC56Pg9oK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dcd5c24e-f926-4f2f-82c9-745a7f2f87dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXBWzuPCjCzU7KYGt2fpHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6293,
      "cache_read_input_tokens": 54447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6293,
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

_source line 33 · 2026-05-18T12:10:14.431Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XaFeqMuZyFQ26w79LtJfhb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcd5c24e-f926-4f2f-82c9-745a7f2f87dc",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1YnDiazzhxC56Pg9oK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0316cf23-c795-4071-bbaf-5b2f7de10952",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXBWzuPCjCzU7KYGt2fpHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6293,
      "cache_read_input_tokens": 54447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6293,
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

_source line 34 · 2026-05-18T12:10:14.437Z_

<details><summary>↩ Tool result · `toolu_01XaFeqMuZyFQ26w79LtJfhb`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.
9	
10	This gap cuts across multiple communities: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}), membership inference~\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.
11	Data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} likewise ignore recursive depth.
12	No existing method estimates how many rounds of recursive generation a text has undergone.
13	
14	Knowing whether the discriminable depth is finite, and where it saturates, has direct practical consequences.
15	For data curation, the saturation point determines filtering granularity: if discrimination collapses at depth 2, graduated weighting beyond that boundary injects noise, and binary filtering becomes the principled choice.
16	Model collapse theory predicts monotonic quality degradation across generations, but existing analyses are population-level and provide no per-text measure of where degradation saturates.
17	$\Kempirical$ fills this gap by localizing the generation at which adjacent outputs become empirically indistinguishable.
18	
19	The Data Processing Inequality implies that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
20	We empirically measure $\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features computed via a fixed reference scorer (Section~\ref{sec:features}) and an Ordinal Binary Decomposition (OBD) LightGBM classifier.
21	We operationalize $\Kempirical$ as the deepest $k \geq 1$ where the pairwise $\auc_{k-1,k}$ exceeds $\theta = 0.60$ (Section~\ref{sec:formulation}).
22	
23	Our contributions:
24	\begin{enumerate}[label=(\alph*),nosep]
25	  \item \textbf{First empirical measurement of $\Kempirical$} across 9 model configurations (5 architecture families, 1B--14B), 3 source domains, and 4 decoding strategies at $\theta{=}0.60$ ($p \leq 0.002$; Section~\ref{sec:kstar_boundary}).
26	  Both supervised OBD and zero-shot frontier Large Language Models (LLMs) show no statistically significant difference beyond $\Kempirical$ (McNemar $p > 0.05$, $N{=}500$; Section~\ref{sec:why_kstar}).
27	  \item \textbf{Domain ordering invariance}: the hierarchy arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$) is preserved across six models spanning four architecture families, three scales (1B--14B), and four decoding strategies, with $\Kempirical$ consistently varying by source domain (Section~\ref{sec:cross_domain}).
28	  \item \textbf{Practical validation}: generator-independent features enable 80--92\% accuracy retention among continuation-mode generators ($\rho > 0.90$; Section~\ref{sec:transfer}), and $\Kempirical{=}2$ correctly predicts binary filtering as optimal granularity for web text (Section~\ref{sec:filtering}).
29	\end{enumerate}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0316cf23-c795-4071-bbaf-5b2f7de10952",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "2f5e14f9-cc0e-4fb0-b344-12acfc21ae56",
  "sourceToolAssistantUUID": "0316cf23-c795-4071-bbaf-5b2f7de10952",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T12:10:14.886Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XN4jbBRjbkgcxFY9MGdZb9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f5e14f9-cc0e-4fb0-b344-12acfc21ae56",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1YnDiazzhxC56Pg9oK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "294b1c1f-6f6a-4e67-8a56-7069e055e984",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXBWzuPCjCzU7KYGt2fpHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6293,
      "cache_read_input_tokens": 54447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6293,
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

_source line 36 · 2026-05-18T12:10:14.896Z_

<details><summary>↩ Tool result · `toolu_01XN4jbBRjbkgcxFY9MGdZb9`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model}.
6	In the context of diffusion models, \citet{shi2025collapse} trace a generalization-to-memorization transition under iterative synthetic training.
7	\citet{gambetta2024surplexity} propose surplexity, a single surprisal-based collapse indicator; our 15-dimensional feature set captures richer distributional structure and enables cross-model transfer.
8	\citet{amin2025escaping} show that weak-data curation can mitigate collapse, connecting to our filtering evaluation (Section~\ref{sec:filtering}).
9	Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}, making $\Kempirical = 2$ a conservative lower bound.
10	This literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.
11	
12	\paragraph{Beyond binary detection.}
13	Binary detectors~\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.
14	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
15	None estimates recursive generation depth.
16	
17	\paragraph{Data selection and curation.}
18	DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling, a special case when $\Kstar = 1$.
19	
20	\paragraph{Ordinal classification and probing.}
21	Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "294b1c1f-6f6a-4e67-8a56-7069e055e984",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "1902fc77-ef59-4588-bfd1-ef78a6ed652b",
  "sourceToolAssistantUUID": "294b1c1f-6f6a-4e67-8a56-7069e055e984",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T12:10:15.439Z_

<details open><summary>🔧 Tool call — Read · `toolu_01865PPcNGWheHZDi285tKSv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1902fc77-ef59-4588-bfd1-ef78a6ed652b",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1YnDiazzhxC56Pg9oK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "062b7057-b117-440b-b51b-0ff2103b4b5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXBWzuPCjCzU7KYGt2fpHt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6293,
      "cache_read_input_tokens": 54447,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6293
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 54447,
          "cache_creation_input_tokens": 6293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6293,
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

_source line 38 · 2026-05-18T12:10:15.444Z_

<details><summary>↩ Tool result · `toolu_01865PPcNGWheHZDi285tKSv`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: the original signal degrades monotonically.
17	Together with Markov chain convergence, this motivates a finite $\Ktheory$ beyond which adjacent generations become indistinguishable.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\{k \geq 1 : \auc_{k-1,k} > \theta\},
22	  \label{eq:kstar}
23	\end{equation}
24	where $\auc_{k-1,k}$ is the point-estimate pairwise AUC (Area Under the ROC Curve) and $\theta = 0.60$ is a data-driven operational threshold (motivated below).
25	Bootstrap 95\% confidence intervals (CIs; 1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
26	
27	\paragraph{Threshold choice.}
28	We set $\theta{=}0.60$ as a data-driven operational threshold, chosen at the empirical discontinuity in the AUC distribution (Figure~\ref{fig:kstar_theta}).
29	A 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\,0.55$ and $p < 0.002$ for all boundary comparisons, placing $\theta{=}0.60$ well above the empirical null.
30	$\Kempirical{=}2$ is stable across $\theta \in [0.55, 0.65]$ for all but two marginal configurations (Table~\ref{tab:kstar_ci_extended}): 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, creating a ${\sim}$5--11\,pp discontinuity.
31	Only at extremes does $\Kempirical$ shift: $\theta{=}0.55$ yields $\Kempirical{=}3$ for two Qwen configurations; $\theta{=}0.70$ yields $\Kempirical{=}1$ across all configurations.
32	The downstream filtering evaluation (Section~\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\theta$, avoiding circularity.
33	
34	\subsection{Features and Classifier}
35	\label{sec:features}
36	
37	Each document is characterized by a 15-dimensional feature vector spanning four groups: \emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).
38	All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
39	Self-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.
40	Removing self-BLEU reduces mean $\auc_{1v2}$ by $< 1$\,pp across all models (14D $\Kempirical = 2$ for all 4 configurations; bootstrap CIs in Table~\ref{tab:selfbleu_ablation}); in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss.
41	Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.
42	
43	We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
44	OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression).
45	
46	\subsection{Experimental Setup}
47	\label{sec:experimental_setup}
48	
49	We evaluate nine configurations spanning five architecture families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B, Qwen2.5-14B, Pythia-1.4B, OLMo-1B, LLaMA-3.1-8B, and Mistral-7B (all continuation except Qwen-rw).
50	Each uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
51	Default decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.
52	Continuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.
53	Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.
54	
55	\begin{table}[t]
56	\centering
57	\small
58	\caption{Experimental configurations for depth-chain generation. \textbf{Config}: shorthand identifier; \textbf{Model}: architecture and parameter count; \textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}
59	\label{tab:setup}
60	\resizebox{\columnwidth}{!}{%
61	\begin{tabular}{llcc}
62	\toprule
63	\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
64	\midrule
65	Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\
66	Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\
67	Qwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\
68	Pythia    & Pythia-1.4B            & Continuation & 5{,}000 \\
69	OLMo      & OLMo-1B               & Continuation & 5{,}000 \\
70	Qwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\
71	Qwen-14B  & Qwen2.5-14B           & Continuation & 5{,}000 \\
72	LLaMA-8B  & LLaMA-3.1-8B          & Continuation & 5{,}000 \\
73	Mistral   & Mistral-7B            & Continuation & 5{,}000 \\
74	\bottomrule
75	\end{tabular}}
76	\end{table}
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "062b7057-b117-440b-b51b-0ff2103b4b5a",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "6f5456bf-b05f-4b09-b8df-f47ee45045ce",
  "sourceToolAssistantUUID": "062b7057-b117-440b-b51b-0ff2103b4b5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T12:10:22.840Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RuLtSCmTp57wCPHZ3vdRms`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f5456bf-b05f-4b09-b8df-f47ee45045ce",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1ZS91Syu5YRnpz7Xa8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aac328b5-6a78-4eaa-a4d1-c9fadd85e77c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJw3GGRaWhfwESGBcL2bcd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4538,
      "cache_read_input_tokens": 60740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4538,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 40 · 2026-05-18T12:10:22.846Z_

<details><summary>↩ Tool result · `toolu_01RuLtSCmTp57wCPHZ3vdRms`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on nine model configurations spanning five architecture families:
5	Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, Qwen2.5-14B, LLaMA-3.1-8B, and Mistral-7B, all in continuation mode except where noted.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{\texorpdfstring{$\Kempirical \leq 2$}{K*<=2} Across Model Configurations (C4)}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\begin{tabular}{lcccccccccc}
20	\toprule
21	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
22	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
23	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
24	\midrule
25	0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] \\
26	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
27	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
28	3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\
29	4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\
30	\bottomrule
31	\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\
32	\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}
33	\end{tabular}
34	\end{table*}
35	
36	\begin{figure}[t]
37	\centering
38	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
39	\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\theta = 0.60$.}
40	\label{fig:auc_decay}
41	\end{figure}
42	
43	Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 9 model configurations: 8/9 yield $\Kempirical{=}2$ (1v2 $\auc$ range: 0.6112--0.6955; all CI lower bounds $> \theta$; permutation $p < 0.001$), while Mistral-7B is the sole exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, below $\theta$; Section~\ref{sec:boundary_cases}).
44	LLaMA-3.1-8B yields $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123$, 95\% CI $[0.603, 0.622]$; borderline: 1/5 folds falls below $\theta$; Table~\ref{tab:kstar_ci_extended}).
45	All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
46	The 1v2 spread due to generation mode ($\Delta = 8.4$\,pp within Qwen) exceeds the spread across models in continuation mode ($\Delta = 3.9$\,pp).
47	
48	\paragraph{Scale and instruction-tuning invariance.}
49	$\Kempirical{=}2$ persists from 1.5B through 14B: Qwen-14B (1v2 $\auc = 0.621$ $[0.612, 0.630]$), Qwen-7B ($0.6168$ $[0.608, 0.626]$), and LLaMA-3.1-8B ($0.6123$) all exceed $\theta$, despite progressively reduced 0v1 signal (0.960 at 14B, 0.964 at 7B, 0.923 at 8B vs.\ $> 0.99$ at $\leq$1.5B).
50	A base-vs.-instruct ablation at 1.5B likewise yields $\Kempirical = 2$ (1v2 $\auc = 0.626$), indicating the boundary is not an instruction-tuning artifact.
51	
52	\begin{figure}[t]
53	\centering
54	\includegraphics[width=\columnwidth]{figures/fig_kstar_theta.pdf}
55	\caption{$\Kempirical(\theta)$ sensitivity curve for six configurations. $\Kempirical$: maximum discriminable depth; $\theta$: AUC decision threshold. All configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (dashed line). At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
56	\label{fig:kstar_theta}
57	\end{figure}
58	
59	Figure~\ref{fig:kstar_theta} shows $\Kempirical$ as a function of $\theta$: web text $\Kempirical{=}2$ is stable across a 5\,pp window ($\theta \in [0.575, 0.625]$), with a gradual transition to $\Kempirical{=}3$ at $\theta{=}0.55$ (two Qwen configurations) and $\Kempirical{=}1$ at $\theta{=}0.70$.
60	The domain ordering (arXiv $>$ web $\geq$ cross-scorer) is preserved across the full $\theta$ range (Table~\ref{tab:theta_sensitivity}).
61	All four decoding strategies likewise yield $\Kempirical = 2$ at $\theta{=}0.60$ (1v2 $\auc \in [0.687, 0.704]$; Table~\ref{tab:s2_decoding}).
62	
63	%% ====================================================================
64	\subsection{Generator-Independent Transfer}
65	\label{sec:transfer}
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
70	\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\leftrightarrow$OLMo: 90--92\%; Qwen-rewrite$\to$continuation: 61--63\%.}
71	\label{fig:transfer_heatmap}
72	\end{figure}
73	
74	Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
75	Qwen-rewrite classifiers transfer poorly (61--63\%), consistent with reliance on mode-specific artifacts rather than generalizable depth features.
76	
77	\paragraph{Cross-scorer validation.}
78	Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\ref{tab:crossscorer}).
79	Qwen-rewrite $\Kempirical$ remains 2 under all scorers; Qwen-continuation drops to 1 (1v2 $\auc$: $0.6112 \to 0.5923/0.5858$), consistent with its marginality under self-scoring.
80	Both alternative scorers agree on $\Kempirical$ per generation mode, indicating that $\Kempirical$ is governed by the generation process rather than the scorer.
81	For arXiv, cross-scoring with Pythia-1.4B preserves $\Kempirical{=}3$ for three of four generators (Qwen-1.5B, LLaMA-8B, Mistral-7B; 2v3 $\auc$ range: 0.608--0.632).
82	Qwen-7B exhibits a borderline decrease to $\Kempirical{=}2$ (2v3 $\auc = 0.599$ vs.\ $0.626$ self-scored, $\Delta = -2.7$\,pp; 3/5 folds above $\theta$), consistent with the Qwen family's scorer sensitivity observed on C4 and Wikipedia.
83	Bootstrap CIs (10{,}000 resamples) confirm $\Kempirical{=}3$ for Qwen-1.5B (CI lower $= 0.617$) and LLaMA-8B (CI lower $= 0.605$); for Mistral-7B (CI: $[0.593, 0.622]$) and Qwen-7B (CI: $[0.584, 0.613]$), the CI straddles $\theta$, indicating that their $\Kempirical{=}3$ assignment is sensitive to resampling variance (Table~\ref{tab:arxiv_crossscorer_ci}).
84	A three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair; $N{=}300$; Table~\ref{tab:anova_crossscorer}) confirms that Depth-Pair dominates variance ($\eta^2_p = 0.998$); Scorer is statistically significant ($p < .001$) but practically minor ($\eta^2_p = 0.192$), consistent with a detectable but small scorer influence on absolute discriminability.
85	
86	%% ====================================================================
87	\subsection{Feature Ordering and Generation Mode}
88	\label{sec:feature_degradation}
89	\label{sec:generation_mode}
90	
91	Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
92	The top-3 features (\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability; however, no single feature subset of size ${<}8$ reliably sustains $\Kempirical{=}2$ (Appendix~\ref{sec:feature_subset}).
93	Qwen-rewrite diverges (\texttt{freq\_entropy} dominates), consistent with its poor cross-model transfer (61--63\%).
94	Within Qwen, rewrite yields 1v2 $\auc = 0.6955$ vs.\ continuation's $0.6112$ ($\Delta = +8.4$\,pp); continuation mode is therefore recommended as the canonical condition.
95	
96	%% ====================================================================
97	\subsection{Neural Probe}
98	\label{sec:neural_probe}
99	
100	Replacing the 15D features with frozen encoder hidden states (MLP probe; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia and OLMo remain at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3}$: 0.5963, 0.5892).
101	The Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\ref{sec:transfer}); the 15D features yield consistent $\Kempirical = 2$ across all families.
102	
103	\noindent\begin{minipage}{\columnwidth}
104	\centering
105	\footnotesize
106	\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $\Kempirical^{\text{neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}
107	\label{tab:neural_probe_crossmodel}
108	\resizebox{\columnwidth}{!}{%
109	\begin{tabular}{lccc}
110	\toprule
111	\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
112	\midrule
113	Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
114	Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
115	OLMo-1B    & 0.5892 & $[0.582,\,0.597]$ & 2 \\
116	\bottomrule
117	\end{tabular}}
118	\end{minipage}
119	
120	%% ====================================================================
121	\subsection{Cross-Domain Variation}
122	\label{sec:cross_domain}
123	
124	The preceding experiments use C4 (general web text).
125	To test whether $\Kempirical$ reflects domain structure or model identity, we evaluate on arXiv abstracts ($n{=}2{,}200$ per model) and Wikipedia ($n{=}5{,}000$ per model) across six model configurations spanning four architecture families (Table~\ref{tab:domain_kstar}).
126	
127	\paragraph{arXiv ($\Kempirical{=}3$): five-model cross-validation.}
128	All five domain-competent models yield $\Kempirical{=}3$ on arXiv, with boundary-pair $\auc$ (2v3) ranging from 0.6215 to 0.6545, all exceeding $\theta$.
129	The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4): formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation and supply persistent depth signal across four architecture families and 1.4B--8B parameters.
130	OLMo-1B constitutes a capacity failure rather than a counter-example; its arXiv generations are entirely out-of-domain (0v1 JSD $= 0.33$, near-total information loss at the first step), yielding $\Kempirical{=}1$.
131	Mistral-7B provides the strongest domain-dependence evidence: $\Kempirical{=}1$ on C4 (Section~\ref{sec:boundary_cases}) but $\Kempirical{=}3$ on arXiv, confirming that domain structure alone can shift $\Kempirical$ by two levels within the same model.
132	
133	\paragraph{Wikipedia ($\Kempirical{=}1$): single-generation saturation.}
134	With scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\Kempirical{=}1$ on Wikipedia: 1v2 $\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\theta$.
135	Wikipedia represents the simplest domain tested; its encyclopedic regularity provides minimal structural signal beyond the 0v1 boundary, and a single generation pass suffices for complete saturation.
136	A same-family scorer confound inflates the apparent $\Kempirical$ for Qwen generators: Qwen-1.5B scoring yields $\Kempirical{=}2$ (1v2 $\auc \approx 0.61$--$0.62$), but cross-family scoring reduces 1v2 by 2.4\,pp to below $\theta$ (Appendix~\ref{sec:wiki_domain}).
137	This +1 depth bias under same-family scoring is specific to Qwen generators on Wikipedia and does not affect C4 results (Section~\ref{sec:transfer}).
138	
139	\paragraph{Domain as the sole dominant factor.}
140	With the scorer confound controlled, the domain ordering is uniform across all tested models: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$).
141	Neither model scale (1B--14B), architecture family, nor decoding strategy alters this ordering, establishing source-domain structural complexity as the primary determinant of $\Kempirical$.
142	
143	\noindent\begin{minipage}{\columnwidth}
144	\centering
145	\footnotesize
146	\captionof{table}{Domain $\times$ Model $\Kempirical$ matrix (scorer-controlled). Wikipedia values use cross-family scorer (Pythia-1.4B). $^*$OLMo arXiv: capacity failure (out-of-domain generation). $^\dagger$Raw same-family scoring yields $\Kempirical{=}2$; controlled value shown (Appendix~\ref{sec:wiki_domain}).}
147	\label{tab:domain_kstar}
148	\resizebox{\columnwidth}{!}{%
149	\begin{tabular}{lccc}
150	\toprule
151	\textbf{Model} & \textbf{C4} & \textbf{arXiv} & \textbf{Wikipedia} \\
152	\midrule
153	Qwen-1.5B    & 2 & 3 & 1$^\dagger$ \\
154	Qwen-7B      & 2 & 3 & 1$^\dagger$ \\
155	Pythia-1.4B  & 2 & 3 & 1 \\
156	OLMo-1B      & 2 & 1$^*$ & 1 \\
157	LLaMA-3.1-8B & 2 & 3 & 1 \\
158	Mistral-7B   & 1 & 3 & 1 \\
159	\bottomrule
160	\end{tabular}}
161	\end{minipage}
162	
163	%% ====================================================================
164	\subsection{Binary Detector Confidence}
165	\label{sec:binary_confidence}
166	
167	Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
168	The observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.
169	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aac328b5-6a78-4eaa-a4d1-c9fadd85e77c",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "52b6aeb0-b884-4f4b-9f40-7ee0237ad8d9",
  "sourceToolAssistantUUID": "aac328b5-6a78-4eaa-a4d1-c9fadd85e77c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-18T12:10:23.129Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D5CnbpSDR5dp1nQoanVtKX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52b6aeb0-b884-4f4b-9f40-7ee0237ad8d9",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1ZS91Syu5YRnpz7Xa8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66db0150-4e12-4eae-abb6-102e598a336a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJw3GGRaWhfwESGBcL2bcd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4538,
      "cache_read_input_tokens": 60740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4538,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 42 · 2026-05-18T12:10:23.145Z_

<details><summary>↩ Tool result · `toolu_01D5CnbpSDR5dp1nQoanVtKX`</summary>

```text
1	\section{Downstream Filtering Validation}
2	\label{sec:filtering}
3	
4	We test whether $\Kempirical$ has predictive value for curation strategy selection, using a single-model setup (Qwen2.5-1.5B-Instruct) as proof of concept.
5	$\Kempirical = 2$ predicts that binary curation should suffice, and that graduated performance should converge toward binary as the decay steepness increases.
6	We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} ($w = 1 - P(\text{synthetic})$ from 15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \cdot \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal} (retain above median), and (vi)~\textbf{DSIR}~\citep{xie2023dsir}.
7	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU (a multitask language understanding benchmark) and HellaSwag (a commonsense reasoning benchmark) across 5 seeds (51 total runs: 5 base strategies $\times$ 5 seeds $+$ 5 graduated-$\alpha$ values $\times$ 5 seeds $+$ 1 base-model reference; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Appendix~\ref{sec:extended_limitations}.}
13	\label{tab:tab_filtering_main}
14	\resizebox{\columnwidth}{!}{\input{tables/tab_filtering_main}}
15	\end{table}
16	
17	Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp ($p_{\text{corr}} < 0.05$ vs.\ all alternatives).
18	The absolute improvement is modest (${\sim}$0.8\,pp), consistent with the constrained dynamic range of a 100\% synthetic upper-bound setting; real-world contamination ratios are typically lower and effect sizes scale accordingly.
19	The strategy ordering is interpretable through $\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.
20	Graduated filtering converges monotonically toward binary: at $\alpha{=}0.9$, it matches binary-ours on HellaSwag exactly ($\Delta = 0$, $p_{\text{corr}} = 1.00$) but remains significantly worse on MMLU ($p_{\text{corr}} = 0.011$).
21	DSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\ref{fig:filtering_strategies} in Appendix).
22	Binary filtering retains a consistent advantage across contamination levels (10--50\%), with effect sizes diminishing 3--6$\times$ relative to the 100\% setting; graduated weighting remains indistinguishable from no-filter at all tested ratios, confirming that depth assignments beyond $\Kempirical$ inject noise regardless of severity (Appendix~\ref{sec:dose_response}).
23	Cross-model replication on Pythia-1.4B confirms the binary $>$ graduated ordering (Appendix~\ref{sec:pythia_filtering}), consistent with $\Kempirical{=}2$ predicting binary filtering as optimal granularity.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66db0150-4e12-4eae-abb6-102e598a336a",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "d913ada1-aad5-420a-b727-993188c36c2b",
  "sourceToolAssistantUUID": "66db0150-4e12-4eae-abb6-102e598a336a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-18T12:10:23.598Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RrmaX2J7e3a9wBj6GyfFaF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d913ada1-aad5-420a-b727-993188c36c2b",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1ZS91Syu5YRnpz7Xa8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c24df86-a7fe-46a0-89f0-7b55a8457dd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJw3GGRaWhfwESGBcL2bcd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4538,
      "cache_read_input_tokens": 60740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4538,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 44 · 2026-05-18T12:10:23.604Z_

<details><summary>↩ Tool result · `toolu_01RrmaX2J7e3a9wBj6GyfFaF`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	\label{sec:why_kstar}
4	\label{sec:one_wash}
5	\label{sec:negative_graduated}
6	\label{sec:repr_dependence}
7	\label{sec:boundary_cases}
8	\label{sec:length_confound}
9	
10	\begin{figure}[t]
11	\centering
12	\includegraphics[width=\columnwidth]{figures/fig_jsd_decay.pdf}
13	\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\Kempirical{=}2$; dashed purple: Mistral-7B ($\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\Kempirical{=}3$); dotted red: retrain-chain ($\Kempirical{\geq}4$). C4 models exhibit a sharp cliff ($\lambda \approx 2.2$--$3.5$), while arXiv decays gradually ($\lambda \approx 1.0$) and retrain-chain shows no cliff ($\lambda = 0.285$).}
14	\label{fig:jsd_decay}
15	\end{figure}
16	
17	\paragraph{One-wash laundering (web text).}
18	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
19	A single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.
20	Converging evidence supports a data-intrinsic interpretation: OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 8--38\% (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).
21	
22	\paragraph{JSD decay and the discrimination boundary.}
23	Token-level Jensen-Shannon Divergence (JSD) between adjacent generations reveals two distinct decay regimes (Figure~\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\times$, median ${\sim}$15$\times$) followed by rapid convergence to a noise floor, while arXiv decays ${\sim}$3$\times$ slower ($\lambda \approx 1.0$ vs.\ $2.9$).
24	Cross-model consistency indicates that $G_\delta$ contraction rate is domain-governed; the retrain-chain profile ($\lambda = 0.285$, no sharp cliff) reflects model-adaptation artifacts rather than text-intrinsic loss (Appendix~\ref{sec:jsd_extended}).
25	
26	\paragraph{Graduated filtering failure.}
27	For web text, 2v3 $\auc < \theta$ across all model configurations, so depth assignments for $d \geq 2$ approximate random labels; graduated weighting injects noise, explaining convergence toward binary at high $\alpha$ (Appendix~\ref{sec:extended_limitations}).
28	The strategy ordering binary $>$ graduated aligns with the $\Kempirical{=}2$ prediction: graduated approaches cannot exploit depth information that does not exist beyond the discrimination boundary.
29	DSIR fails differently: bigram hashing captures domain shift but not depth-correlated signatures (pattern persists across 10--50\% contamination ratios; Appendix~\ref{sec:dose_response}).
30	
31	\paragraph{Representation and scorer dependence.}
32	$\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$, while Pythia and OLMo match the 15D boundary at $\Kempirical^{\text{neural}} = 2$ (Table~\ref{tab:neural_probe_crossmodel}); the 15D features trade one depth level for cross-model consistency (8/9 configurations $\Kempirical{\leq}2$).
33	$\Kempirical$ can also depend on scorer family: on Wikipedia, cross-family scoring reduces $\Kempirical$ from 2 to 1 ($\Delta = -2.4$\,pp; Appendix~\ref{sec:wiki_domain}), while on C4 it preserves feature rankings ($\rho > 0.90$) and $\Kempirical$ for 6/8 configurations (Section~\ref{sec:transfer}).
34	Scorer sensitivity is inversely related to domain lexical diversity; we recommend cross-family validation for new domains.
35	
36	\paragraph{Domain dependence of $\Kempirical$.}
37	C4 web text yields $\Kempirical{=}2$ (8/9 configurations, 1B--14B), while arXiv yields $\Kempirical{=}3$ across five models and four architecture families (Section~\ref{sec:cross_domain}).
38	With scorer confound controlled, all six models yield $\Kempirical{=}1$ on Wikipedia (Appendix~\ref{sec:wiki_domain}), producing a consistent ordering by source domain: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$), which correlates with domain-level lexical diversity.
39	The sole C4 exception (Mistral-7B, $\Kempirical{=}1$) has $\Kempirical{=}3$ on arXiv, reinforcing the domain-governed interpretation (Appendix~\ref{sec:boundary_extended}).
40	
41	\paragraph{Prompt-chain vs.\ retrain-chain $\Kempirical$.}
42	Retrain-chain experiments (Pythia-1.4B LoRA) yield $\Kempirical{\geq}4$ (Table~\ref{tab:retrain_ci}), far exceeding prompt-chain $\Kempirical{=}2$; the former reflects model-adaptation artifacts rather than text-level information loss (Appendix~\ref{sec:extended_limitations}).
43	
44	
45	
46	\paragraph{Why $\Kempirical$ matters.}
47	$\Kempirical{=}2$ for web text is not a negative result but a precise measurement: it rules out both $\Kempirical{=}1$ (no depth signal beyond 0v1) and $\Kempirical{\geq}3$ (graduated tracking feasible), while arXiv $\Kempirical{=}3$ confirms the framework captures real domain-level variation rather than a methodological ceiling.
48	$\Kempirical$ thus serves as an empirical diagnostic of domain properties and is directly prescriptive for curation granularity.
49	The method combines established components (LightGBM, hand-crafted features, ordinal decomposition); the contribution is the measurement framework and the empirical characterization it enables.
50	
51	
52	
53	\paragraph{Practical implications.}
54	For web text ($\Kempirical{=}2$), graduated depth weighting injects noise beyond the boundary, validating binary filtering as optimal (Section~\ref{sec:filtering}); for arXiv ($\Kempirical{=}3$), an additional depth level carries discriminative signal.
55	Mixed-domain corpora thus require domain-stratified filtering, and $\Kempirical{=}2$ provides post-hoc grounding for the binary approach of \citet{drayson2025} (segment-length sensitivity in Table~\ref{tab:s11_length_ablation}).
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c24df86-a7fe-46a0-89f0-7b55a8457dd5",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "7553eb6b-9944-4d74-8a15-890817f61a8e",
  "sourceToolAssistantUUID": "9c24df86-a7fe-46a0-89f0-7b55a8457dd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-18T12:10:23.928Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XbyyJgGiuAfn1jR8k2Rubn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7553eb6b-9944-4d74-8a15-890817f61a8e",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1ZS91Syu5YRnpz7Xa8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31655c47-d595-41c2-b979-6c1706f6ca0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJw3GGRaWhfwESGBcL2bcd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4538,
      "cache_read_input_tokens": 60740,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4538
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 307,
          "cache_read_input_tokens": 60740,
          "cache_creation_input_tokens": 4538,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4538,
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

_source line 46 · 2026-05-18T12:10:23.938Z_

<details><summary>↩ Tool result · `toolu_01XbyyJgGiuAfn1jR8k2Rubn`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We measure the generational depth discrimination boundary $\Kempirical$ for recursive synthetic text.
5	$\Kempirical \in \{1, 2, 3\}$ depends on source domain and model characteristics: general web text yields $\Kempirical{=}2$ across 8/9 configurations (5 families, 1B--14B; $p \leq 0.002$), with $\Kempirical{=}3$ for academic text, confirmed across five models and four architecture families.
6	Generator-independent features enable 80--92\% accuracy retention across generators ($\rho > 0.90$), making $\Kempirical$ measurement practical without generator-specific training.
7	As downstream validation, $\Kempirical{=}2$ supports binary filtering as the optimal granularity for web text: graduated depth weighting cannot exploit information that does not exist beyond the discrimination boundary.
8	$\Kempirical$ provides a representation-dependent lower bound on discriminable depth; the gap between $\Kempirical$ and the theoretical limit $\Ktheory$ remains open and may narrow with richer feature representations.
9	Future work includes scaling beyond 14B, additional structured domains, and retrain-chain $\Kstar$ characterization.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31655c47-d595-41c2-b979-6c1706f6ca0b",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "02d7d713-4f21-4fac-957d-594bf8fd85d9",
  "sourceToolAssistantUUID": "31655c47-d595-41c2-b979-6c1706f6ca0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-18T12:10:30.155Z_

Now let me also read the appendix and the reference list for the full paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02d7d713-4f21-4fac-957d-594bf8fd85d9",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1a4G9dqivYqwob1Den",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06db8131-64e7-4aa1-b611-c1d6c8ae94d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf5qgKtjXiX9dcwvk9Pt1g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9622,
      "cache_read_input_tokens": 65278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9622,
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

_source line 48 · 2026-05-18T12:10:32.165Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HwWDu8VknYJe1DHehYEMPC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06db8131-64e7-4aa1-b611-c1d6c8ae94d1",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1a4G9dqivYqwob1Den",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a9a621d-a3b1-4ec2-bb5f-cc92d75e3308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf5qgKtjXiX9dcwvk9Pt1g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9622,
      "cache_read_input_tokens": 65278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9622,
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

_source line 49 · 2026-05-18T12:10:32.427Z_

<details><summary>↩ Tool result · `toolu_01HwWDu8VknYJe1DHehYEMPC`</summary>

```text
1	\appendix
2	\section{Supplementary Figures}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
7	\caption{Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}
8	\label{fig:filtering_strategies}
9	\end{figure}
10	
11	\begin{figure}[t]
12	  \centering
13	  \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
14	  \caption{Pairwise $\auc$ decay curves for five model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
15	  \label{fig:s1_auc_decay_ci}
16	\end{figure}
17	
18	\section{Supplementary Tables}
19	
20	%%% Feature ranking table (moved from main text)
21	\begin{table}[t]
22	\centering
23	\small
24	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
25	\label{tab:top_features}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{cllll}
28	\toprule
29	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
30	\midrule
31	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
32	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_std}} \\
33	3 & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_d2\_std}} \\
34	\bottomrule
35	\end{tabular}}
36	\end{table}
37	
38	%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)
39	\begin{table*}[t]
40	  \centering
41	  \caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}
42	  \label{tab:s1_transfer}
43	  \begin{tabular}{lcccc}
44	    \toprule
45	    \multirow{2}{*}{\textbf{Train Model}} & \multicolumn{4}{c}{\textbf{Test Model}} \\
46	    \cmidrule(lr){2-5}
47	    & Qwen-rw & Pythia & OLMo & Qwen-cont \\
48	    \midrule
49	    Qwen-rw   & \textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\
50	    Pythia    & 0.2718 & \textbf{0.3856} & 0.3531 & 0.3287 \\
51	    OLMo      & 0.2768 & 0.3450 & \textbf{0.3822} & 0.3244 \\
52	    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \textbf{0.3875} \\
53	    \bottomrule
54	  \end{tabular}
55	  \vspace{4pt}
56	
57	  \footnotesize
58	  \textit{Transfer retention} between models $A$ and $B$ is defined as $\frac{1}{2}\bigl(\frac{\mathrm{acc}(A \to B)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}} + \frac{\mathrm{acc}(B \to A)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}}\bigr)$.
59	  Notable pairs: Pythia$\leftrightarrow$OLMo 91--92\%, Qwen-cont$\leftrightarrow$Pythia 83--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\%, Qwen-rw$\to$Pythia/OLMo 61--63\%.
60	\end{table*}
61	
62	%%% Table S2: Decoding Ablation AUC (exp-003)
63	\begin{table*}[t]
64	  \centering
65	  \caption{Pairwise AUC with bootstrap 95\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\,vs.\,2 and 2\,vs.\,3 marks the empirical detectability boundary $\Kempirical=2$. Bottom rows report cross-configuration Spearman $\rho$ on per-feature discriminative-power rankings.}
66	  \label{tab:s2_decoding}
67	  \footnotesize
68	  \begin{tabular}{lcccc}
69	    \toprule
70	    \textbf{Depth Pair} & \textbf{Greedy} & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
71	    \midrule
72	    0 vs.\ 1 & $.980\;[.977,\,.982]$ & $.995\;[.993,\,.996]$ & $.988\;[.986,\,.990]$ & $.998\;[.998,\,.999]$ \\
73	    1 vs.\ 2 & $.689\;[.680,\,.698]$ & $.687\;[.677,\,.695]$ & $.689\;[.680,\,.697]$ & $.704\;[.695,\,.713]$ \\
74	    \cmidrule(lr){1-5}
75	    2 vs.\ 3 & $.561\;[.552,\,.571]$ & $.592\;[.582,\,.601]$\rlap{$^\dagger$} & $.590\;[.581,\,.600]$ & $.582\;[.572,\,.592]$ \\
76	    3 vs.\ 4 & $.540\;[.531,\,.550]$ & $.547\;[.537,\,.557]$ & $.539\;[.529,\,.549]$ & $.529\;[.519,\,.540]$ \\
77	    4 vs.\ 5 & $.514\;[.503,\,.524]$ & $.507\;[.496,\,.517]^{\ddagger}$ & $.535\;[.524,\,.545]$ & $.524\;[.513,\,.535]$ \\
78	    \midrule
79	    \multicolumn{5}{l}{\textbf{Cross-config feature Spearman $\rho$}} \\
80	    \midrule
81	    \multicolumn{2}{l}{Greedy vs.\ Nuc $p{=}0.9$} & 0.600 &
82	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}0.7$} & 0.782 \\
83	    \multicolumn{2}{l}{Greedy vs.\ $T{=}0.7$} & 0.914 &
84	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}1.2$} & 0.893 \\
85	    \multicolumn{2}{l}{Greedy vs.\ $T{=}1.2$} & 0.532 &
86	    \multicolumn{1}{l}{$T{=}0.7$ vs.\ $T{=}1.2$} & 0.668 \\
87	    \bottomrule
88	    \multicolumn{5}{l}{${}^{\dagger}$\,CI upper bound (0.601) marginally exceeds $\theta{=}0.60$ by 0.001.} \\
89	    \multicolumn{5}{l}{${}^{\ddagger}$\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}
90	  \end{tabular}
91	\end{table*}
92	
93	%%% Table S2b: Extended K* CI (all models including new additions)
94	\begin{table*}[t]
95	  \centering
96	  \footnotesize
97	  \caption{Extended pairwise $\auc$ with bootstrap 95\% CIs for all 9 model configurations.
98	  This table extends Table~\ref{tab:kstar_ci} in the main text with Qwen-base, Qwen-14B, LLaMA-8B, and Mistral-7B.
99	  8/9 yield $\Kempirical = 2$; Mistral-7B yields $\Kempirical = 1$ (1v2 $\auc < \theta$).}
100	  \label{tab:kstar_ci_extended}
101	  \resizebox{\textwidth}{!}{%
102	  \begin{tabular}{lcccccccccccccccccc}
103	    \toprule
104	     & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} & \multicolumn{2}{c}{Qwen-14B\rlap{$^\ddagger$}} & \multicolumn{2}{c}{Qwen-base} & \multicolumn{2}{c}{LLaMA-8B} & \multicolumn{2}{c}{Mistral-7B} \\
105	    \cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}\cmidrule(lr){12-13}\cmidrule(lr){14-15}\cmidrule(lr){16-17}\cmidrule(lr){18-19}
106	     & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
107	    \midrule
108	    0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] & .960 & [.956,\,.963] & .987 & [.985,\,.989] & .9225 & [.918,\,.927] & .930 & [.925,\,.935] \\
109	    1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} & .621 & [.612,\,.630]\rlap{$^*$} & .626 & [.617,\,.635]\rlap{$^*$} & .6123 & [.603,\,.622]\rlap{$^*$} & .594 & [.584,\,.603] \\
110	    2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] & .549 & [.539,\,.559] & .550 & [.540,\,.560] & .5518 & [.542,\,.562] & .548 & [.538,\,.558] \\
111	    3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & & .524 & [.514,\,.535] & .529 & [.519,\,.540] & .5203 & [.510,\,.531] & .521 & \\
112	    4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & & .515 & [.505,\,.527] & .518 & [.508,\,.529] & .5089 & [.499,\,.519] & .510 & \\
113	    \bottomrule
114	    \multicolumn{19}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all boundary comparisons. Mistral-7B 1v2: $p = 0.001$ but $\auc < \theta$, hence $\Kempirical{=}1$.} \\
115	    \multicolumn{19}{l}{\footnotesize $^\ddagger$Qwen-7B: Qwen2.5-7B (fp16); Qwen-14B: Qwen2.5-14B; scorer: Qwen2.5-1.5B.}
116	  \end{tabular}}
117	
118	\end{table*}
119	
120	%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)
121	\begin{table*}[t]
122	  \centering
123	  \caption{LLM zero-shot depth classification: $5{\times}5$ confusion matrices
124	    (Exp-011). Both frontier LLMs achieve high binary detection accuracy
125	    (GPT-5.5: 0.8780; Claude Opus~4.6: 0.8818) but near-chance 5-class
126	    accuracy (${\sim}0.33$ vs.\ OBD-LightGBM baseline 0.386, evaluated on the full test set $N{=}5{,}000$). GPT-5.5
127	    strongly identifies depth-0 text (recall${=}0.7700$) but collapses on
128	    depth-4 (recall${=}0.0800$), misclassifying 50/100 depth-4 samples as
129	    depth-2. Claude Opus~4.6 shows more uniform errors across depths 1--4,
130	    with depth-4 recall (0.3700) substantially exceeding GPT-5.5.
131	    Per-depth recall comparison with OBD-LightGBM in Table~\ref{tab:s3c_perdepth}.}
132	  \label{tab:s3_llm_zeroshot}
133	
134	  \vspace{0.5em}
135	  \begin{subtable}{0.48\textwidth}
136	    \centering
137	    \caption{GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)}
138	    \label{tab:s3a_gpt55}
139	    \small
140	    \begin{tabular}{lcccccc}
141	      \toprule
142	      & \multicolumn{5}{c}{Predicted Depth} & \\
143	      \cmidrule(lr){2-6}
144	      True & 0 & 1 & 2 & 3 & 4 & Rec. \\
145	      \midrule
146	      0 & \textbf{77} & 18 &  4 &  0 &  1 & .770 \\
147	      1 &  9 & \textbf{19} & 36 & 24 & 12 & .190 \\
148	      2 &  8 & 10 & \textbf{38} & 35 &  9 & .380 \\
149	      3 & 10 & 16 & 35 & \textbf{24} & 15 & .240 \\
150	      4 & 11 & 13 & 50 & 18 &  \textbf{8} & .080 \\
151	      \bottomrule
152	    \end{tabular}
153	  \end{subtable}
154	  \hfill
155	  \begin{subtable}{0.48\textwidth}
156	    \centering
157	    \caption{Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)}
158	    \label{tab:s3b_claude}
159	    \small
160	    \begin{tabular}{lcccccc}
161	      \toprule
162	      & \multicolumn{5}{c}{Predicted Depth} & \\
163	      \cmidrule(lr){2-6}
164	      True & 0 & 1 & 2 & 3 & 4 & Rec. \\
165	      \midrule
166	      0 & \textbf{69} & 26 &  3 &  0 &  2 & .690 \\
167	      1 &  8 & \textbf{21} & 32 & 11 & 28 & .210 \\
168	      2 &  6 & 36 & \textbf{28} &  5 & 25 & .280 \\
169	      3 &  7 & 20 & 31 & \textbf{10} & 31 & .100 \\
170	      4 &  7 & 28 & 22 &  6 & \textbf{37} & .370 \\
171	      \bottomrule
172	    \end{tabular}
173	  \end{subtable}
174	\end{table*}
175	
176	\begin{table}[t]
177	  \centering
178	  \small
179	  \caption{Per-depth recall (\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\geq 2$, consistent with $\Kempirical = 2$.}
180	  \label{tab:s3c_perdepth}
181	  \resizebox{\columnwidth}{!}{%
182	  \begin{tabular}{lccccc}
183	    \toprule
184	    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\
185	    \midrule
186	    OBD-LightGBM & \textbf{96} & \textbf{39} & 14 & 19 & 22 \\
187	    GPT-5.5      & 77 & 19 & \textbf{38} & \textbf{24} &  8 \\
188	    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \textbf{37} \\
189	    \bottomrule
190	  \end{tabular}}
191	\end{table}
192	
193	\paragraph{Zero-shot prompt template.}
194	Both GPT-5.5 and Claude Opus~4.6 received the following system prompt (temperature 0, single-token output constraint):
195	
196	\begin{quote}
197	\small
198	\texttt{The following text passage was produced through recursive LLM generation starting from human-written text (depth~0). Each successive generation feeds the previous output back to the LLM: depth~0 = human, depth~1 = first LLM pass, depth~2 = second pass, etc.}
199	
200	\texttt{Estimate the generational depth (0, 1, 2, 3, or 4) of the passage below. Respond with only the depth number.}
201	
202	\texttt{Text: \{text\}}
203	\end{quote}
204	
205	%%% Table: Token Length and EOS Truncation Analysis
206	\begin{table*}[t]
207	  \centering
208	  \small
209	  \caption{Mean subword token count per depth and EOS truncation rate (\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend within any model; the 0v1 length asymmetry (human texts shorter) makes detection \emph{more conservative}, not inflated. See Section~\ref{sec:length_confound} for discussion.}
210	  \label{tab:token_length}
211	  \begin{tabular}{lcccccccc}
212	    \toprule
213	    & \multicolumn{6}{c}{\textbf{Mean Token Count}} & & \\
214	    \cmidrule(lr){2-7}
215	    \textbf{Model} & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 & Depth 5 & \textbf{EOS Trunc.\ (\%)} & \textbf{Severity} \\
216	    \midrule
217	    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\
218	    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\
219	    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negligible \\
220	    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Moderate \\
221	    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\
222	    \midrule
223	    \multicolumn{9}{l}{\textit{Decoding ablation (Qwen-rw 1.5B)}} \\
224	    \quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\
225	    \quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\
226	    \quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\
227	    \quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\
228	    \bottomrule
229	  \end{tabular}
230	
231	  \vspace{4pt}
232	  \footnotesize
233	  EOS truncation rate: percentage of depth~1+ samples where generation terminated via EOS before reaching the 256-token limit. Ranges span depths 1--5.
234	\end{table*}
235	
236	%%% Table S4: Dataset Statistics
237	\begin{table}[t]
238	  \centering
239	  \small
240	  \caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}
241	  \label{tab:s4_dataset_stats}
242	  \resizebox{\columnwidth}{!}{%
243	  \begin{tabular}{clrl}
244	    \toprule
245	    \textbf{Depth} & \textbf{$N$ samples} & \textbf{Mean tokens} & \textbf{Source} \\
246	    \midrule
247	    0 & 5{,}000 & 147.8 & C4 validation (human) \\
248	    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\
249	    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\
250	    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\
251	    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
252	    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
253	    \midrule
254	    \multicolumn{2}{l}{Total} & \multicolumn{2}{l}{30{,}000 samples} \\
255	    \bottomrule
256	  \end{tabular}}
257	\end{table}
258	
259	%%% Table S5: Complete 15-D Feature Descriptions
260	\begin{table*}[t]
261	  \centering
262	  \caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}
263	  \label{tab:s5_features}
264	  \begin{tabular}{llp{0.45\textwidth}l}
265	    \toprule
266	    \textbf{Group} & \textbf{Feature} & \textbf{Description} & \textbf{Range} \\
267	    \midrule
268	    \multirow{9}{*}{\rotatebox[origin=c]{90}{\textsc{Surprisal}}}
269	    & \texttt{surp\_mean}   & Mean token surprisal $\frac{1}{T}\sum_t -\log p(x_t \mid x_{&lt;t})$ & $\mathbb{R}^+$ \\
270	    & \texttt{surp\_std}    & Standard deviation of token surprisal & $\mathbb{R}^+$ \\
271	    & \texttt{surp\_skew}   & Skewness of the surprisal distribution & $\mathbb{R}$ \\
272	    & \texttt{surp\_kurt}   & Excess kurtosis of the surprisal distribution & $\mathbb{R}$ \\
273	    & \texttt{surp\_d1\_mean} & Mean of first-order surprisal differences $\Delta s_t = s_{t+1} - s_t$ & $\mathbb{R}$ \\
274	    & \texttt{surp\_d1\_std}  & Std of first-order surprisal differences & $\mathbb{R}^+$ \\
275	    & \texttt{surp\_d1\_skew} & Skewness of first-order surprisal differences & $\mathbb{R}$ \\
276	    & \texttt{surp\_d2\_mean} & Mean of second-order differences $\Delta^2 s_t$ & $\mathbb{R}$ \\
277	    & \texttt{surp\_d2\_std}  & Std of second-order surprisal differences & $\mathbb{R}^+$ \\
278	    \midrule
279	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Lex}}}
280	    & \texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\
281	    & \texttt{hapax\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\
282	    & \texttt{self\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\
283	    \midrule
284	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Freq}}}
285	    & \texttt{freq\_kurtosis}  & Excess kurtosis of word frequency distribution & $\mathbb{R}$ \\
286	    & \texttt{freq\_entropy}   & Shannon entropy of word frequencies: $-\sum p_w \log_2 p_w$ & $\mathbb{R}^+$ \\
287	    & \texttt{low\_freq\_ratio} & Proportion of vocabulary with count $\leq 2$ & $[0, 1]$ \\
288	    \bottomrule
289	  \end{tabular}
290	\end{table*}
291	
292	%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap
293	\begin{table*}[t]
294	\begin{minipage}[t]{0.45\textwidth}
295	  \centering
296	  \small
297	  \captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \texttt{doc\_id} to prevent data leakage from the same seed document appearing in both train and test.}
298	  \label{tab:s6_lgbm_params}
299	  \begin{tabular}{ll}
300	    \toprule
301	    \textbf{Parameter} & \textbf{Value} \\
302	    \midrule
303	    \texttt{n\_estimators}      & 200 \\
304	    \texttt{learning\_rate}     & 0.05 \\
305	    \texttt{max\_depth}         & 6 \\
306	    \texttt{num\_leaves}        & 31 \\
307	    \texttt{verbose}            & $-1$ \\
308	    \texttt{n\_jobs}            & $-1$ (all cores) \\
309	    Cross-validation            & 5-fold GroupKFold \\
310	    Grouping key                & \texttt{doc\_id} \\
311	    Objective                   & Binary (per depth pair) \\
312	    \bottomrule
313	  \end{tabular}
314	\end{minipage}\hfill
315	\begin{minipage}[t]{0.52\textwidth}
316	  \centering
317	  \small
318	  \captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}
319	  \label{tab:s7_neural_probe}
320	  \resizebox{\textwidth}{!}{%
321	  \begin{tabular}{ll}
322	    \toprule
323	    \textbf{Component} & \textbf{Details} \\
324	    \midrule
325	    \multicolumn{2}{l}{\textit{Embedding extraction}} \\
326	    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\
327	    Representation    & Last hidden state, attention-masked avg pool \\
328	    Embedding dim     & 1536 / 2048 / 2048 \\
329	    Max sequence len   & 512 tokens \\
330	    \midrule
331	    \multicolumn{2}{l}{\textit{MLP classifier}} \\
332	    Architecture      & $d_{\text{emb}} \to 512 \to 256 \to 6$ \\
333	    Activations       & ReLU \\
334	    Dropout           & 0.1 (after each hidden layer) \\
335	    Output            & 6-class softmax \\
336	    \midrule
337	    \multicolumn{2}{l}{\textit{Training}} \\
338	    Optimizer         & Adam ($\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\
339	    Loss              & Cross-entropy \\
340	    Batch size        & 256 \\
341	    Max epochs        & 20 \\
342	    Early stopping    & Patience = 5 (validation loss) \\
343	    Cross-validation  & 5-fold GroupKFold \\
344	    \bottomrule
345	  \end{tabular}%
346	  }
347	\end{minipage}
348	\end{table*}
349	
350	%%% Table S8: Per-Model Bootstrap CI Results (exp-007)
351	\begin{table*}[t]
352	  \centering
353	  \footnotesize
354	  \caption{Pairwise AUC with bootstrap 95\% confidence intervals for four model-mode configurations (Exp-007, 1{,}000 bootstrap resamples). The horizontal rule separates depth pairs above and below the detectability threshold $\theta = 0.60$. Permutation $p$-values test $H_0\colon \auc = 0.50$. All pairs are significant at $p < 0.01$ except OLMo 3\,vs.\,4 ($p = 0.064$) and 4\,vs.\,5 ($p = 0.232$), consistent with convergence to chance at deeper generations.}
355	  \label{tab:s8_cv_folds}
356	  \begin{tabular}{lcccc}
357	    \toprule
358	    \textbf{Depth Pair} & \textbf{Qwen-rewrite} & \textbf{Pythia-1.4B} & \textbf{OLMo-1B} & \textbf{Qwen-cont} \\
359	    \midrule
360	    0 vs.\ 1
361	      & $.996\;[.995,\,.997]$
362	      & $.993\;[.992,\,.994]$
363	      & $.997\;[.996,\,.998]$
364	      & $.997\;[.996,\,.998]$ \\
365	    1 vs.\ 2
366	      & $.696\;[.686,\,.704]$
367	      & $.654\;[.645,\,.663]$
368	      & $.615\;[.605,\,.625]$
369	      & $.611\;[.602,\,.621]$ \\
370	    \cmidrule(lr){1-5}
371	    2 vs.\ 3
372	      & $.589\;[.580,\,.599]$
373	      & $.551\;[.542,\,.563]$
374	      & $.550\;[.540,\,.560]$
375	      & $.561\;[.551,\,.571]$ \\
376	    3 vs.\ 4
377	      & $.544\;[.533,\,.555]$
378	      & $.515\;[.504,\,.526]$
379	      & $.509\;[.497,\,.520]^{\dagger}$
380	      & $.541\;[.531,\,.551]$ \\
381	    4 vs.\ 5
382	      & $.534\;[.524,\,.545]$
383	      & $.514\;[.502,\,.525]$
384	      & $.505\;[.493,\,.515]^{\ddagger}$
385	      & $.514\;[.504,\,.526]$ \\
386	    \bottomrule
387	  \end{tabular}
388	
389	  \vspace{4pt}
390	  \footnotesize
391	  Each cell: AUC $[95\%$ CI$]$. CI from 1{,}000 bootstrap resamples; $p$-values from 500-resample permutation test.
392	  ${}^{\dagger}$\,$p = 0.064$;\; ${}^{\ddagger}$\,$p = 0.232$;\; all other pairs $p < 0.01$.
393	\end{table*}
394	
395	%%% Table S9: Binary Detector Spearman ρ (exp-012)
396	\begin{table*}[t]
397	  \centering
398	  \small
399	  \caption{Spearman rank correlation ($\rho$) between binary detector confidence scores and true generational depth, and 6-class depth classification accuracy (Exp-012). Three metrics: log-PPL from the reference model (DivEye), log-PPL from the observer model, and PPL ratio (Binoculars; observer: Pythia-1.4B, performer: OLMo-1B). Random baseline for 6-class accuracy: 0.167. While statistically significant, correlations are driven by the 0v1 boundary; confidence scores do not monotonically track depth beyond generation~1. Qwen-rewrite exhibits reversed sign ($\rho > 0$), indicating that generation mode alters the direction of binary confidence's relationship with depth.}
400	  \label{tab:s9_binary_spearman}
401	  \begin{tabular}{lcccc}
402	    \toprule
403	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
404	    \midrule
405	    \multicolumn{5}{l}{\textit{Spearman $\rho$ with true depth}} \\
406	    \quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\
407	    \quad log-PPL (observer) & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\
408	    \quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\
409	    \midrule
410	    \multicolumn{5}{l}{\textit{Classification}} \\
411	    \quad 6-class accuracy    & 0.199    & 0.130    & 0.127    & 0.183 \\
412	    \midrule
413	    \multicolumn{5}{l}{Random baseline: 0.167 \quad $\Kempirical^{\text{binary}} = 1$ \quad $\Kempirical^{\text{OBD}} = 2$} \\
414	    \bottomrule
415	  \end{tabular}
416	\end{table*}
417	
418	%%% Table S10: Pythia Decoding Ablation (exp-020)
419	\begin{table*}[t]
420	  \centering
421	  \small
422	  \caption{Pairwise $\auc$ with bootstrap 95\% CIs across depth pairs for Pythia-1.4B under four decoding configurations (Exp-020; 10{,}000 bootstrap resamples). Complements Table~\ref{tab:s2_decoding} (Qwen-rewrite) with a second model family. $^\dagger$Greedy decoding triggers repetition collapse in Pythia-1.4B (4-gram repeat rate: $d_0{=}0.01 \to d_1{=}0.72$), inflating 0v1 and 1v2 AUC via lexical degeneracy rather than depth-discriminative features.}
423	  \label{tab:s10_pythia_decoding}
424	  \begin{tabular}{lcccc}
425	    \toprule
426	    \textbf{Depth Pair} & \textbf{Greedy}$^\dagger$ & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
427	    \midrule
428	    0 vs.\ 1 & .9992 & .9948 & .9965 & .9933 \\
429	    1 vs.\ 2 & .8838 & .6770 & .7265 & .6172 \\
430	    \cmidrule(lr){1-5}
431	    2 vs.\ 3 & .5342 & .5549 & .5941 & .5226 \\
432	    3 vs.\ 4 & .5228 & .5299 & .5698 & .5170 \\
433	    4 vs.\ 5 & .5162 & .5013 & .5284 & .5051 \\
434	    \midrule
435	    $\Kempirical$ & 2 & 2 & 2 & 2 \\
436	    \bottomrule
437	  \end{tabular}
438	\end{table*}
439	
440	%%% Table S11: Length Ablation (exp-021)
441	\begin{table*}[t]
442	  \centering
443	  \small
444	  \caption{Pairwise $\auc$ across depth pairs for three segment lengths (Exp-021; Qwen2.5-1.5B base, continuation mode). $\Kempirical{=}2$ is confirmed for 128 and 256 tokens; 512 tokens yields point estimate $\Kempirical{=}2$ but the 1v2 bootstrap CI lower bound falls marginally below $\theta$.}
445	  \label{tab:s11_length_ablation}
446	  \begin{tabular}{lccc}
447	    \toprule
448	    \textbf{Depth Pair} & \textbf{128 tokens} & \textbf{256 tokens} & \textbf{512 tokens} \\
449	    \midrule
450	    0 vs.\ 1 & .9948 & .9956 & .9961 \\
451	    1 vs.\ 2 & .6219 & .6282 & .6073$^\dagger$ \\
452	    \cmidrule(lr){1-4}
453	    2 vs.\ 3 & .5531 & .5609 & .5482 \\
454	    3 vs.\ 4 & .5218 & .5305 & .5196 \\
455	    4 vs.\ 5 & .5104 & .5142 & .5078 \\
456	    \midrule
457	    $\Kempirical$ & 2 & 2 & 2$^\dagger$ \\
458	    \bottomrule
459	    \multicolumn{4}{l}{\footnotesize $^\dagger$CI $[0.5979,\,0.6166]$; lower bound ${<}\theta{=}0.60$.}
460	  \end{tabular}
461	\end{table*}
462	
463	%%% Table S12: Domain Ablation
464	\begin{table*}[t]
465	  \centering
466	  \small
467	  \caption{Pairwise $\auc$ across depth pairs for three text domains (Qwen2.5-1.5B base, continuation mode). Tests generalization of $\Kempirical{=}2$ beyond C4 web text to structured and technical domains. Same-family scoring (Qwen-1.5B); cross-family controlled values in Table~\ref{tab:wiki_domain}.}
468	  \label{tab:s12_domain_ablation}
469	  \begin{tabular}{lccc}
470	    \toprule
471	    \textbf{Depth Pair} & \textbf{C4 (web)} & \textbf{Wikipedia} & \textbf{arXiv} \\
472	    \midrule
473	    0 vs.\ 1 & .9971 & .996 & .9984 \\
474	    1 vs.\ 2 & .6112 & .6193 & .8580 \\
475	    \cmidrule(lr){1-4}
476	    2 vs.\ 3 & .5609 & .556 & .6427 \\
477	    3 vs.\ 4 & .5409 & .528 & .5813 \\
478	    4 vs.\ 5 & .5141 & .509 & .5346 \\
479	    \midrule
480	    $\Kempirical$ & 2 & 2 & 3 \\
481	    \bottomrule
482	  \end{tabular}
483	\end{table*}
484	
485	%%% Table S13: Scorer Sensitivity Analysis
486	\begin{table*}[t]
487	  \centering
488	  \small
489	  \caption{Scorer sensitivity: $\Kempirical$ under self-scoring vs.\ cross-scoring. Self-scorer uses the generator's own model family for feature extraction; cross-scorer uses alternative models (Pythia-1.4B, OLMo-1B). $\Kempirical$ agreement across scorer conditions indicates the boundary is governed by the generation process. Cross-scoring reduces $\Kempirical$ only for the most marginal self-scorer condition (Qwen-continuation).}
490	  \label{tab:s13_scorer_sensitivity}
491	  \begin{tabular}{lccccc}
492	    \toprule
493	    & & \multicolumn{3}{c}{\textbf{Scorer}} & \\
494	    \cmidrule(lr){3-5}
495	    \textbf{Generator} & \textbf{Mode} & \textbf{Self} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Agreement} \\
496	    \midrule
497	    Qwen-1.5B-Instruct & Rewrite      & 2 (.696) & 2 & 2 & \checkmark \\
498	    Qwen-1.5B-Instruct & Continuation & 2 (.611) & 1 & 1 & $\times$ \\
499	    Qwen-1.5B (base)   & Continuation & 2 (.626) & 2 & 2 & \checkmark \\
500	    Pythia-1.4B         & Continuation & 2 (.654) & 2 & 2 & \checkmark \\
501	    OLMo-1B             & Continuation & 2 (.615) & 2 & 2 & \checkmark \\
502	    Qwen-7B             & Continuation & 2 (.618) & 2 & 2 & \checkmark \\
503	    Mistral-7B          & Continuation & 1 (.594) & 1 & 1 & \checkmark \\
504	    \bottomrule
505	  \end{tabular}
506	\end{table*}
507	
508	\clearpage
509	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a9a621d-a3b1-4ec2-bb5f-cc92d75e3308",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "7b5aa5f1-dcef-4844-97e3-b10a2cecf513",
  "sourceToolAssistantUUID": "6a9a621d-a3b1-4ec2-bb5f-cc92d75e3308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-18T12:10:32.434Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M15QZZ9ANdG7jr7FmHm9Bm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b5aa5f1-dcef-4844-97e3-b10a2cecf513",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1a4G9dqivYqwob1Den",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07d90fe9-21c5-4400-a847-f0607034e459",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf5qgKtjXiX9dcwvk9Pt1g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9622,
      "cache_read_input_tokens": 65278,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9622
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 65278,
          "cache_creation_input_tokens": 9622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9622,
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

_source line 51 · 2026-05-18T12:10:32.439Z_

<details><summary>↩ Tool result · `toolu_01M15QZZ9ANdG7jr7FmHm9Bm`</summary>

```text
1	\section{Extended Analysis and Limitations}
2	\label{sec:extended_discussion}
3	
4	This section provides supporting tables for cross-scorer validation (Tables~\ref{tab:crossscorer}--\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.
5	
6	\noindent\begin{minipage}{\columnwidth}
7	\centering
8	\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
9	\label{tab:crossscorer}
10	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
11	\end{minipage}
12	
13	\begin{table}[h]
14	\centering
15	\small
16	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\times$ 5 folds $\times$ 5 depth-pairs; 3 generators $\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\eta^2_p = 0.19$) relative to Depth-Pair ($\eta^2_p = 1.00$) and Generator ($\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination (Scorer $\eta^2_p$ is approximately 5$\times$ smaller than Generator and dwarfed by Depth-Pair). Per-fold AUC values within the same generator share seed documents across folds and are not fully independent; we therefore rely on effect-size ratios rather than $p$-values for interpretation.}
17	\label{tab:anova_crossscorer}
18	\begin{tabular}{lrrrr}
19	\toprule
20	\textbf{Source} & \textbf{df} & $F$ & $p$ & $\eta^2_p$ \\
21	\midrule
22	Generator     & 2  & 926.8  & ${<}.001$  & .885 \\
23	Scorer        & 3  & 19.02  & ${<}.001$  & .192 \\
24	Depth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\
25	Gen$\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\
26	Gen$\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\
27	Scorer$\times$Depth & 12 & 2.45 & .005 & .109 \\
28	Residual      & 240 & & & \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	\subsection{Extended Limitations}
34	\label{sec:extended_limitations}
35	
36	\emph{Prompt-chain versus retrain-chain.}
37	Retrain-chain validation (Pythia-1.4B LoRA, 5 generations) yields $\Kempirical{\geq}4$ (Table~\ref{tab:retrain_ci}), far exceeding prompt-chain $\Kempirical{=}2$.
38	All pairwise CIs have lower bounds well above $\theta{=}0.60$ ($p < 0.001$), statistically confirming $\Kempirical{\geq}4$.
39	The elevated signal arises from cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) rather than text-intrinsic degradation; prompt-chain $\Kempirical$ is the operationally relevant boundary for data curation.
40	
41	\begin{table}[h]
42	\centering
43	\small
44	\caption{Retrain-chain pairwise $\auc$ with bootstrap 95\% CIs (Pythia-1.4B LoRA, 5 generations). All CI lower bounds $\gg \theta{=}0.60$.}
45	\label{tab:retrain_ci}
46	\begin{tabular}{lccc}
47	\toprule
48	\textbf{Pair} & $\auc$ & \textbf{95\% CI} & $p$ \\
49	\midrule
50	0v1 & 0.9842 & $[0.9823,\,0.9860]$ & ${<}0.001$ \\
51	1v2 & 0.9471 & $[0.9432,\,0.9509]$ & ${<}0.001$ \\
52	2v3 & 0.8888 & $[0.8832,\,0.8943]$ & ${<}0.001$ \\
53	3v4 & 0.7994 & $[0.7920,\,0.8067]$ & ${<}0.001$ \\
54	\bottomrule
55	\end{tabular}
56	\end{table}
57	
58	\emph{Threshold sensitivity.}
59	Table~\ref{tab:theta_sensitivity} reports $\Kempirical$ across $\theta \in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.
60	Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
61	
62	\begin{table}[h]
63	\centering
64	\small
65	\caption{$\Kempirical$ as a function of $\theta$ across conditions. The \textbf{domain ordering} (arXiv $>$ web $\geq$ cross-scorer) and \textbf{bounded range} ($\Kempirical{\leq}4$) are preserved across $\theta \in [0.55, 0.70]$. The headline result (web $\Kempirical{=}2$, arXiv $\Kempirical{=}3$) holds for $\theta \in [0.575, 0.625]$.}
66	\label{tab:theta_sensitivity}
67	\resizebox{\columnwidth}{!}{%
68	\begin{tabular}{llcccc}
69	\toprule
70	\textbf{Condition} & \textbf{Config} & $\theta{=}0.55$ & $\theta{=}0.60$ & $\theta{=}0.625$ & $\theta{=}0.70$ \\
71	\midrule
72	C4 (web) & Qwen-rw      & 3 & 2 & 2 & 1 \\
73	C4 (web) & Pythia       & 2 & 2 & 2 & 1 \\
74	C4 (web) & OLMo         & 2 & 2 & 1 & 1 \\
75	C4 (web) & Qwen-cont    & 3 & 2 & 2 & 1 \\
76	C4 (web) & Qwen-7B      & 2 & 2 & 2 & 1 \\
77	C4 (web) & Mistral-7B   & 1 & 1 & 1 & 1 \\
78	\midrule
79	arXiv    & Qwen-1.5B-base (cont.) & 4 & 3 & 3 & 2 \\
80	arXiv    & Pythia-1.4B (cont.)    & 4 & 3 & 3 & 2 \\
81	\midrule
82	Cross-scorer & Qwen-cont/Pythia-scored & 2 & 1 & 1 & 1 \\
83	Cross-scorer & Qwen-cont/OLMo-scored   & 2 & 1 & 1 & 1 \\
84	\bottomrule
85	\end{tabular}}
86	\end{table}
87	
88	\emph{Structural confound: token length.}
89	In continuation mode the generation prompt is discarded, so all depths $\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\ machine-generated prompt), not structural composition.
90	Depth~0 texts average ${\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\ref{tab:token_length}).
91	This asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.
92	Within depths 1--5, mean token counts are stable (within-model range $\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\Kempirical{=}2$ are unaffected by length.
93	EOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\%, Pythia 34--36\%, OLMo $<$1\%, Qwen-continuation 17--20\%, Qwen-7B 45--47\%.
94	Models with the highest truncation (Pythia, Qwen-7B) still yield $\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.
95	
96	\emph{Graduated filtering.}
97	All $\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\alpha{=}0.1$: 0.5873; $\alpha{=}0.9$: 0.5892 vs.\ 0.5941); at $\alpha{=}0.9$, HellaSwag matches exactly (0.6701).
98	Binary-ours significantly outperforms all alternatives on MMLU ($p_{\text{corr}} \leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\text{corr}} = 0.011$).
99	\label{tab:pairwise_significance}
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07d90fe9-21c5-4400-a847-f0607034e459",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "faaf9194-b4db-4534-be34-d0cf19354ae1",
  "sourceToolAssistantUUID": "07d90fe9-21c5-4400-a847-f0607034e459",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-18T12:10:40.928Z_

Now let me check the reference list in the main paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faaf9194-b4db-4534-be34-d0cf19354ae1",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1agwGzetJCDY6bKHGp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f86c56b4-c701-45ab-84f2-a6e2c3b63af6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014eGcjN6CE6mzQkj3NzTQ3N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16285,
      "cache_read_input_tokens": 74900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16285,
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

_source line 53 · 2026-05-18T12:10:42.088Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01B2kNBgRdY7gfZkzWgSBCyV`</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f86c56b4-c701-45ab-84f2-a6e2c3b63af6",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1agwGzetJCDY6bKHGp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20633da7-d01e-4768-b2bc-ce991875b26d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014eGcjN6CE6mzQkj3NzTQ3N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16285,
      "cache_read_input_tokens": 74900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16285,
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

_source line 54 · 2026-05-18T12:10:42.122Z_

<details><summary>↩ Tool result · `toolu_01B2kNBgRdY7gfZkzWgSBCyV`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20633da7-d01e-4768-b2bc-ce991875b26d",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "8ea68288-6f3f-4f5f-a408-09910eef8578",
  "sourceToolAssistantUUID": "20633da7-d01e-4768-b2bc-ce991875b26d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-18T12:10:45.614Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TrdqiTK1ATZpV9XE6JpKFr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ea68288-6f3f-4f5f-a408-09910eef8578",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1bQNu9FeDiaduE5Dk3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "937e1f9d-69f4-4128-b475-fb78015ca777",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBEDYevNPQXiyzMhZRyeou",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 134,
      "cache_read_input_tokens": 91185,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 134
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 91185,
          "cache_creation_input_tokens": 134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 134,
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

_source line 56 · 2026-05-18T12:10:45.628Z_

<details><summary>↩ Tool result · `toolu_01TrdqiTK1ATZpV9XE6JpKFr`</summary>

```text
1	% === References for gen-depth-contamination ===
2	% Source: literature_map.yaml — verified 2026-05-15
3	
4	% === Must-Cite ===
5	
6	@inproceedings{drayson2025,
7	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
8	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
9	  booktitle={Proceedings of EMNLP},
10	  year={2025},
11	  url={https://arxiv.org/abs/2502.15654}
12	}
13	
14	@inproceedings{schaeffer2025position,
15	  title={Position: Model Collapse Does Not Mean What You Think},
16	  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},
17	  booktitle={Proceedings of ICML},
18	  year={2025},
19	  url={https://arxiv.org/abs/2503.03150}
20	}
21	
22	@inproceedings{kazdan2025collapse,
23	  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
24	  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},
25	  booktitle={Proceedings of ICML},
26	  year={2025},
27	  url={https://arxiv.org/abs/2410.16713}
28	}
29	
30	@inproceedings{mitchell2023detectgpt,
31	  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
32	  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
33	  booktitle={Proceedings of ICML},
34	  year={2023}
35	}
36	
37	% === Should-Cite ===
38	
39	@article{basani2026diveye,
40	  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},
41	  author={Basani, Advik Raj and Chen, Pin-Yu},
42	  journal={Transactions on Machine Learning Research},
43	  issn={2835-8856},
44	  year={2026},
45	  url={https://arxiv.org/abs/2509.18880}
46	}
47	
48	@inproceedings{zawalski2026codec,
49	  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},
50	  author={Zawalski, Micha{\l} and Boubdir, Meriem and Ba{\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},
51	  booktitle={Proceedings of ICLR},
52	  year={2026},
53	  url={https://arxiv.org/abs/2510.27055}
54	}
55	
56	@inproceedings{zhang2024minkpp,
57	  title={Min-{K}\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
58	  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},
59	  booktitle={Proceedings of EMNLP},
60	  year={2024}
61	}
62	
63	@article{shumailov2024collapse,
64	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
65	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
66	  journal={Nature},
67	  volume={631},
68	  pages={755--759},
69	  year={2024}
70	}
71	
72	@inproceedings{alemohammad2024selfconsuming,
73	  title={Self-Consuming Generative Models Go {MAD}},
74	  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
75	  booktitle={Proceedings of ICLR},
76	  year={2024}
77	}
78	
79	@inproceedings{dohmatob2024model,
80	  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},
81	  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},
82	  booktitle={Proceedings of ICML},
83	  year={2024}
84	}
85	
86	@inproceedings{xie2023dsir,
87	  title={Data Selection for Language Models via Importance Resampling},
88	  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
89	  booktitle={Advances in Neural Information Processing Systems},
90	  year={2023}
91	}
92	
93	@inproceedings{tirumala2023d4,
94	  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},
95	  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},
96	  booktitle={Advances in Neural Information Processing Systems},
97	  year={2023}
98	}
99	
100	@inproceedings{xie2023doremi,
101	  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},
102	  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},
103	  booktitle={Advances in Neural Information Processing Systems},
104	  year={2023}
105	}
106	
107	@inproceedings{hans2024binoculars,
108	  title={Spotting {LLMs} With Binoculars},
109	  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
110	  booktitle={Proceedings of ICML},
111	  year={2024}
112	}
113	
114	% === Probing Classifiers ===
115	
116	@inproceedings{alain2017understanding,
117	  title={Understanding Intermediate Layers Using Linear Classifier Probes},
118	  author={Alain, Guillaume and Bengio, Yoshua},
119	  booktitle={ICLR Workshop},
120	  year={2017}
121	}
122	
123	@article{belinkov2022probing,
124	  title={Probing Classifiers: Promises, Shortcomings, and Advances},
125	  author={Belinkov, Yonatan},
126	  journal={Computational Linguistics},
127	  volume={48},
128	  number={1},
129	  pages={207--219},
130	  year={2022}
131	}
132	
133	% === Model Collapse Avoidability ===
134	
135	@inproceedings{bao2024fast,
136	  title={{Fast-DetectGPT}: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature},
137	  author={Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
138	  booktitle={Proceedings of ICLR},
139	  year={2024},
140	  url={https://arxiv.org/abs/2310.05130}
141	}
142	
143	@inproceedings{frank2001ordinal,
144	  title={A Simple Approach to Ordinal Classification},
145	  author={Frank, Eibe and Hall, Mark},
146	  booktitle={Proceedings of ECML},
147	  pages={145--156},
148	  year={2001}
149	}
150	
151	% === Beyond-Binary Detection ===
152	
153	@inproceedings{cheng2025beyond,
154	  title={Beyond Binary: Towards Fine-Grained {LLM}-Generated Text Detection via Role Recognition and Involvement Measurement},
155	  author={Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
156	  booktitle={Proceedings of the ACM Web Conference (WWW)},
157	  year={2025},
158	  url={https://arxiv.org/abs/2410.14259}
159	}
160	
161	@article{mehta2025beyond,
162	  title={Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models},
163	  author={Mehta, Sushant},
164	  journal={arXiv preprint arXiv:2511.17602},
165	  year={2025},
166	  url={https://arxiv.org/abs/2511.17602}
167	}
168	
169	% === AI-Generated Content Prevalence ===
170	
171	@inproceedings{sun2025aigt,
172	  title={Are We in the {AI}-Generated Text World Already? Quantifying and Monitoring {AIGT} on Social Media},
173	  author={Sun, Zhen and Zhang, Zongmin and Shen, Xinyue and Zhang, Ziyi and Liu, Yule and Backes, Michael and Zhang, Yang and He, Xinlei},
174	  booktitle={Proceedings of ACL},
175	  year={2025},
176	  url={https://arxiv.org/abs/2412.18148}
177	}
178	
179	@article{spennemann2025quantifying,
180	  title={Delving into: the Quantification of {AI}-Generated Content on the Internet (Synthetic Data)},
181	  author={Spennemann, Dirk H. R.},
182	  journal={arXiv preprint arXiv:2504.08755},
183	  year={2025},
184	  url={https://arxiv.org/abs/2504.08755}
185	}
186	
187	% === New entries (added 2026-05-16, Round 4 reviewer) ===
188	
189	@inproceedings{dohmatob2025strong,
190	  title={Strong Model Collapse},
191	  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
192	  booktitle={Proceedings of ICLR},
193	  year={2025},
194	  url={https://arxiv.org/abs/2410.04840}
195	}
196	
197	@inproceedings{wang2024semeval,
198	  title={{SemEval}-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection},
199	  author={Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas},
200	  booktitle={Proceedings of SemEval},
201	  year={2024},
202	  url={https://arxiv.org/abs/2404.14183}
203	}
204	
205	@inproceedings{gerstgrasser2024model,
206	  title={Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},
207	  author={Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
208	  booktitle={Proceedings of COLM},
209	  year={2024},
210	  url={https://arxiv.org/abs/2404.01413}
211	}
212	
213	@inproceedings{guo2024curious,
214	  title={The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},
215	  author={Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chloe},
216	  booktitle={Findings of NAACL},
217	  year={2024},
218	  url={https://arxiv.org/abs/2311.09807}
219	}
220	
221	@article{briesch2023selfconsuming,
222	  title={Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop},
223	  author={Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},
224	  journal={arXiv preprint arXiv:2311.16822},
225	  year={2023},
226	  url={https://arxiv.org/abs/2311.16822}
227	}
228	
229	@inproceedings{padmakumar2024writing,
230	  title={Does Writing with Language Models Reduce Content Diversity?},
231	  author={Padmakumar, Vishakh and He, He},
232	  booktitle={Proceedings of ICLR},
233	  year={2024},
234	  url={https://arxiv.org/abs/2309.05196}
235	}
236	
237	% === New entries (added 2026-05-15, FR-10) ===
238	
239	@inproceedings{krishna2023paraphrasing,
240	  title={Paraphrasing Evades Detectors of {AI}-Generated Text, but Retrieval is an Effective Defense},
241	  author={Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
242	  booktitle={Advances in Neural Information Processing Systems},
243	  year={2023}
244	}
245	
246	@article{sadasivan2023detect,
247	  title={Can {AI}-Generated Text be Reliably Detected?},
248	  author={Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
249	  journal={arXiv preprint arXiv:2303.11156},
250	  year={2023},
251	  url={https://arxiv.org/abs/2303.11156}
252	}
253	
254	@inproceedings{hao2025rewrite,
255	  title={Learning to Rewrite: Generalized {LLM}-Generated Text Detection},
256	  author={Hao, Wei and Guan, Ran and Lu, Kangjie and Zhang, Shuai},
257	  booktitle={Findings of ACL},
258	  year={2025}
259	}
260	
261	@inproceedings{shi2025collapse,
262	  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},
263	  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
264	  booktitle={Advances in Neural Information Processing Systems},
265	  year={2025}
266	}
267	
268	@article{gambetta2024surplexity,
269	  title={Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},
270	  author={Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and Knott, Alistair and Pappalardo, Luca},
271	  journal={arXiv preprint arXiv:2410.12341},
272	  year={2024}
273	}
274	
275	@inproceedings{amin2025escaping,
276	  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},
277	  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},
278	  booktitle={Advances in Neural Information Processing Systems},
279	  year={2025}
280	}
281	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "937e1f9d-69f4-4128-b475-fb78015ca777",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "4c78ce90-2dd6-43e9-9f6f-7ff3357c070f",
  "sourceToolAssistantUUID": "937e1f9d-69f4-4128-b475-fb78015ca777",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-18T12:10:51.761Z_

I now have a thorough understanding of the full paper. Let me also check if there's any CC validation or power analysis section in the main paper (not just the dream version).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c78ce90-2dd6-43e9-9f6f-7ff3357c070f",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1bf1U3rfrAn13nNeR3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ed638ed-3f68-4e4a-a680-d32c298c8026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LR2xdfmQ79hFFM9JtgJj5r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4735,
      "cache_read_input_tokens": 91319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4735,
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

_source line 58 · 2026-05-18T12:10:53.745Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WNaQGe63m9Ft3aCGUrUud7`</summary>

```json
{
  "pattern": "Common Crawl|power analysis|subsampling",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ed638ed-3f68-4e4a-a680-d32c298c8026",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1bf1U3rfrAn13nNeR3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a8d3a2d-c355-4122-a52a-51df3d735f17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LR2xdfmQ79hFFM9JtgJj5r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4735,
      "cache_read_input_tokens": 91319,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4735
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 91319,
          "cache_creation_input_tokens": 4735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4735,
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

_source line 59 · 2026-05-18T12:10:53.761Z_

<details><summary>↩ Tool result · `toolu_01WNaQGe63m9Ft3aCGUrUud7`</summary>

```text
docs/paper/appendix_extended.tex:290:As a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\Kempirical{=}1$ (1v2 $\auc = 0.601$, CI $[0.586, 0.616]$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a8d3a2d-c355-4122-a52a-51df3d735f17",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "f99695e7-5b82-4e79-9b2c-ae90267de799",
  "sourceToolAssistantUUID": "9a8d3a2d-c355-4122-a52a-51df3d735f17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-18T12:10:59.441Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WCrrDoB78erFRNj34x14QR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f99695e7-5b82-4e79-9b2c-ae90267de799",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1cGG24hwjaupPo6Nia",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55586f49-bdaf-4298-b641-67d4e6c9d3ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvaZNQVHb8uJXpgNPLKEMM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 96054,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 265
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 96054,
          "cache_creation_input_tokens": 265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 265,
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

_source line 61 · 2026-05-18T12:10:59.446Z_

<details><summary>↩ Tool result · `toolu_01WCrrDoB78erFRNj34x14QR`</summary>

```text
100	
101	\subsection{Dose-Response: Contamination Ratio Effect}
102	\label{sec:dose_response}
103	
104	The main filtering experiments (Section~\ref{sec:filtering}) use 100\% synthetic data to maximize effect size.
105	To characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\%, 30\%, and 50\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\ref{tab:dose_response}).
106	
107	\begin{table}[h]
108	\centering
109	\small
110	\caption{MMLU and HellaSwag by contamination ratio and filtering strategy (5 seeds, mean $\pm$ std). Base model MMLU: 0.6018. Binary filtering retains a significant advantage on HellaSwag across all ratios ($p \leq 0.004$, Holm-Bonferroni corrected).}
111	\label{tab:dose_response}
112	\resizebox{\columnwidth}{!}{%
113	\begin{tabular}{lcccccc}
114	\toprule
115	& \multicolumn{2}{c}{\textbf{10\%}} & \multicolumn{2}{c}{\textbf{30\%}} & \multicolumn{2}{c}{\textbf{50\%}} \\
116	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}
117	\textbf{Strategy} & MMLU & HellaSwag & MMLU & HellaSwag & MMLU & HellaSwag \\
118	\midrule
119	No-filter   & $.6058{\pm}.0002$ & $.6689{\pm}.0006$ & $.6069{\pm}.0007$ & $.6664{\pm}.0018$ & $.6063{\pm}.0012$ & $.6680{\pm}.0005$ \\
120	Binary-ours & $\mathbf{.6079{\pm}.0004}$ & $\mathbf{.6727{\pm}.0007}$ & $\mathbf{.6082{\pm}.0011}$ & $\mathbf{.6725{\pm}.0006}$ & $\mathbf{.6088{\pm}.0009}$ & $\mathbf{.6731{\pm}.0004}$ \\
121	Graduated   & $.6066{\pm}.0010$ & $.6700{\pm}.0014$ & $.6072{\pm}.0008$ & $.6665{\pm}.0012$ & $.6062{\pm}.0008$ & $.6679{\pm}.0001$ \\
122	\bottomrule
123	\end{tabular}}
124	\end{table}
125	
126	At all tested ratios (10--50\%), no-filter MMLU remains above the base model (0.6018), indicating that synthetic data at these proportions is net-beneficial rather than harmful.
127	Binary filtering consistently improves over no-filter, with HellaSwag differences significant across all ratios ($p \leq 0.004$, Holm-Bonferroni corrected).
128	MMLU differences are smaller and significant only at 10\% after correction ($p = 0.001$).
129	Graduated weighting is indistinguishable from no-filter at all ratios (MMLU $p \geq 0.27$; HellaSwag $p \geq 0.06$), confirming that depth assignments beyond $\Kempirical$ inject noise regardless of contamination severity.
130	Effect sizes diminish 3--6$\times$ relative to the 100\% setting (Section~\ref{sec:filtering}), but the strategy ordering (binary $>$ graduated $\approx$ no-filter) is preserved.
131	
132	\subsection{Cross-Model Filtering Replication}
133	\label{sec:pythia_filtering}
134	
135	To test whether $\Kempirical{=}2$ correctly predicts optimal curation granularity across architectures, we replicate the filtering experiment on Pythia-1.4B (LoRA rank 8, nucleus $p{=}0.9$, $T{=}1.0$, 3 seeds; Table~\ref{tab:pythia_filtering}).
136	
137	\begin{table}[h]
138	\centering
139	\small
140	\caption{Pythia-1.4B filtering replication (3 seeds, mean $\pm$ std). Strategy ordering matches Qwen (binary $>$ no-filter $>$ graduated on MMLU).}
141	\label{tab:pythia_filtering}
142	\begin{tabular}{lcc}
143	\toprule
144	\textbf{Strategy} & \textbf{MMLU} & \textbf{HellaSwag} \\
145	\midrule
146	No-filter & $.2568{\pm}.0012$ & $.5250{\pm}.0008$ \\
147	Binary-ours & $\mathbf{.2585{\pm}.0004}$ & $.5251{\pm}.0001$ \\
148	Graduated$_{0.9}$ & $.2561{\pm}.0009$ & $\mathbf{.5253{\pm}.0007}$ \\
149	\bottomrule
150	\end{tabular}
151	\end{table}
152	
153	The strategy ordering (binary $>$ no-filter $>$ graduated on MMLU) matches Qwen (Section~\ref{sec:filtering}).
154	The small absolute differences reflect the model's near-chance MMLU baseline rather than filtering inefficacy; the consistent ordering across two architectures supports $\Kempirical{=}2$'s predictive value for curation granularity.
155	HellaSwag differences are negligible across all strategies.
156	
157	\subsection{Feature Subset Stability}
158	\label{sec:feature_subset}
159	
160	To test whether $\Kempirical{=}2$ depends on the specific 15D feature combination, we evaluate random feature subsets of varying size on Pythia-1.4B prompt-chain data (Table~\ref{tab:feature_subset}).
161	
162	\begin{table}[h]
163	\centering
164	\small
165	\caption{1v2 $\auc$ by feature subset size (Pythia-1.4B). $\Kempirical{=}2$ ($\auc > \theta{=}0.60$) is robust at $\geq$8 features.}
166	\label{tab:feature_subset}
167	\begin{tabular}{lcccc}
168	\toprule
169	\textbf{Subset} & \textbf{Tested} & \textbf{Pass} & \textbf{Min $\auc$} & \textbf{Mean $\auc$} \\
170	\midrule
171	15D (full) & 1 & 1 & 0.6262 & 0.6262 \\
172	10D        & 5 & 5 & 0.6153 & 0.6191 \\
173	8D         & 5 & 5 & 0.6056 & 0.6159 \\
174	5D         & 5 & 2 & 0.5856 & 0.5998 \\
175	3D (top-3) & 1 & 0 & 0.5871 & 0.5871 \\
176	\bottomrule
177	\end{tabular}
178	\end{table}
179	
180	$\Kempirical{=}2$ holds for all subsets of size $\geq$8 (10/10 pass, min $\auc = 0.6056$), becomes fragile at 5D (2/5 pass), and fails at 3D (top-3 surprisal features alone: $\auc = 0.5871 < \theta$).
181	The boundary does not depend on any specific feature combination but requires sufficient dimensionality ($\geq$8) to capture the multi-faceted distributional shift between generations 1 and 2.
182	
183	\subsection{self\_BLEU Feature Independence}
184	\label{sec:selfbleu_ablation}
185	
186	To verify that $\Kempirical$ does not depend on the self\_BLEU feature (which may reflect stylistic repetition rather than depth-correlated degradation), we compare 15D and 14D (self\_BLEU removed) classifiers across four model configurations (Table~\ref{tab:selfbleu_ablation}).
187	
188	\begin{table}[h]
189	\centering
190	\small
191	\caption{15D vs.\ 14D (self\_BLEU removed) 1v2 $\auc$ with bootstrap 95\% CIs. Removing self\_BLEU does not change $\Kempirical$ for any configuration. Maximum $|\Delta\auc| = 0.0031$, within bootstrap CI width (${\sim}0.018$).}
192	\label{tab:selfbleu_ablation}
193	\resizebox{\columnwidth}{!}{%
194	\begin{tabular}{lcccc}
195	\toprule
196	\textbf{Model} & $\Kempirical$ & \textbf{15D $\auc$ [CI]} & \textbf{14D $\auc$ [CI]} & $\Delta$ \\
197	\midrule
198	Qwen-base   & 2/2 & $.6288$ $[.620,\,.638]$ & $.6258$ $[.616,\,.635]$ & $-.0031$ \\
199	Pythia-1.4B  & 2/2 & $.8840$ $[.878,\,.890]$ & $.8830$ $[.876,\,.889]$ & $-.0010$ \\
200	LLaMA-8B     & 2/2 & $.6075$ $[.598,\,.617]$ & $.6074$ $[.598,\,.617]$ & $-.0001$ \\
201	Mistral-7B   & 1/1 & $.5902$ $[.580,\,.600]$ & $.5903$ $[.580,\,.600]$ & $+.0002$ \\
202	\bottomrule
203	\end{tabular}}
204	\end{table}
205	
206	All four configurations preserve their $\Kempirical$ under 14D, with negligible AUC change ($|\Delta| \leq 0.003$).
207	The self\_BLEU feature contributes minimally to the depth boundary; $\Kempirical{=}2$ is driven by surprisal and entropy features rather than lexical repetition statistics.
208	
209	\subsection{Wikipedia Domain: Scorer Confound Resolution}
210	\label{sec:wiki_domain}
211	
212	Under same-family scoring (Qwen-1.5B scorer), Wikipedia $\Kempirical$ appeared to exhibit model-family dependence: Qwen generators (1.5B and 7B) yielded $\Kempirical{=}2$, while all four non-Qwen models yielded $\Kempirical{=}1$ (Table~\ref{tab:wiki_domain}).
213	A scorer confound ablation resolves this apparent split.
214	Rescoring the same Qwen-7B Wikipedia text with Pythia-1.4B reduces 1v2 $\auc$ from $0.611$ to $0.587$ ($\Delta = -2.4$\,pp), dropping $\Kempirical$ from 2 to 1.
215	With the scorer confound controlled, all six models yield $\Kempirical{=}1$ on Wikipedia, and the domain ordering simplifies to: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$).
216	
217	\begin{table}[h]
218	\centering
219	\small
220	\caption{Wikipedia pairwise $\auc$ across 6 models. $^\dagger$Qwen rows use same-family scorer (Qwen-1.5B); cross-family scoring (Pythia-1.4B) reduces Qwen-7B to $\Kempirical{=}1$ ($\Delta = -2.4$\,pp), resolving the apparent family split.}
221	\label{tab:wiki_domain}
222	\resizebox{\columnwidth}{!}{%
223	\begin{tabular}{llccccc}
224	\toprule
225	\textbf{Model} & \textbf{Family} & \textbf{0v1} & \textbf{1v2} & \textbf{2v3} & $\Kempirical$ & \textbf{Scorer} \\
226	\midrule
227	Qwen-1.5B (base) & Qwen & ---  & .619 & .550 & 2$^\dagger$ & Qwen-1.5B \\
228	Qwen-1.5B (base) & Qwen & ---  & .599 & ---  & 1 & Pythia-1.4B \\
229	Qwen-7B          & Qwen & .967 & .611 & .556 & 2$^\dagger$ & Qwen-1.5B \\
230	Qwen-7B          & Qwen & ---  & .587 & ---  & 1 & Pythia-1.4B \\
231	\midrule
232	Pythia-1.4B   & non-Qwen & .975 & .585 & .545 & 1 & Qwen-1.5B \\
233	OLMo-1B       & non-Qwen & .993 & .499 & .501 & 1 & Qwen-1.5B \\
234	LLaMA-3.1-8B  & non-Qwen & .932 & .595 & .539 & 1 & Qwen-1.5B \\
235	Mistral-7B    & non-Qwen & .961 & .555 & .524 & 1 & Qwen-1.5B \\
236	\bottomrule
237	\multicolumn{7}{l}{\footnotesize $^\dagger$Same-family scorer; cross-family scoring yields $\Kempirical{=}1$.}
238	\end{tabular}}
239	\end{table}
240	
241	\paragraph{Per-fold transparency.}
242	For Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\theta = 0.60$).
243	The aggregate mean falls below $\theta$, confirming $\Kempirical{=}1$.
244	For Qwen-7B, the corresponding $\auc$ drops further to $0.587$.
245	
246	\subsection{ArXiv Cross-Scorer Bootstrap CIs}
247	\label{sec:arxiv_crossscorer_ci}
248	
249	\begin{table}[h]
250	\centering
251	\small
252	\caption{Bootstrap 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}
253	\label{tab:arxiv_crossscorer_ci}
254	\resizebox{\columnwidth}{!}{%
255	\begin{tabular}{lccc}
256	\toprule
257	\textbf{Generator} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & \textbf{CI lower $> \theta$} \\
258	\midrule
259	Qwen-1.5B    & 0.632 & $[0.617,\,0.646]$ & Yes \\
260	LLaMA-3.1-8B & 0.620 & $[0.605,\,0.636]$ & Yes (0.5\,pp margin) \\
261	Mistral-7B   & 0.608 & $[0.593,\,0.622]$ & No \\
262	Qwen-7B      & 0.599 & $[0.584,\,0.613]$ & No \\
263	\bottomrule
264	\end{tabular}}
265	\end{table}
266	
267	\subsection{JSD Decay Analysis}
268	\label{sec:jsd_extended}
269	
270	The token-level JSD between adjacent generations reveals two distinct decay regimes (Figure~\ref{fig:jsd_decay}).
271	For C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\times$ across all 8 models (1B--14B) with $\Kempirical{=}2$ (median cliff ratio ${\sim}$15$\times$), and subsequent pairs converge to a noise floor of ${\sim}$0.003--0.005.
272	Fitting $\jsd(k, k{+}1) \propto e^{-\lambda k}$ yields $\lambda \approx 2.2$--$3.5$ for C4 (mean ${\approx}\,2.9$), consistent with rapid mixing of $G_\delta$ toward its stationary distribution.
273	These decay rates represent qualitative characterizations from 5-point curves rather than precise estimates.
274	The empirical decay rate $\lambda$ is consistent within each domain but varies across domains: C4 yields $\lambda \approx 2.9$, Wikipedia $\lambda \approx 3.1$ (excluding OLMo, whose $\lambda = 6.3$ reflects a capacity-limited collapse: 0v1 $\jsd = 0.169$ with near-complete information loss at the first step, making the exponential fit unreliable), and arXiv $\lambda \approx 1.0$.
275	This cross-model consistency indicates that the contraction rate of $G_\delta$ is governed primarily by the structure of the input domain rather than the model architecture.
276	ArXiv text decays ${\sim}$3$\times$ slower than C4 ($\lambda \approx 1.0$ vs.\ $2.9$), with a correspondingly higher convergence floor (${\sim}$0.007--0.009 vs.\ ${\sim}$0.003--0.004).
277	Formulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, explaining the elevated $\Kempirical{=}3$.
278	The retrain-chain exhibits a fundamentally different profile: $\lambda = 0.285$ with a cliff ratio of only 1.31$\times$ and no sharp drop between adjacent pairs.
279	This gradual, sustained divergence reflects cumulative model-adaptation artifacts rather than text-intrinsic information loss, further supporting the distinction between prompt-chain and retrain-chain $\Kempirical$ (Appendix~\ref{sec:boundary_extended}).
280	
281	\subsection{Boundary Cases and Scale Effect}
282	\label{sec:boundary_extended}
283	
284	Of 9 tested model configurations on C4, 8 yield $\Kempirical{=}2$; Mistral-7B is the sole sub-2 exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, CI $[0.584, 0.603]$), validating $\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\ $0.611$--$0.696$).
285	Mistral's cross-domain profile reinforces the domain-governed interpretation: despite $\Kempirical{=}1$ on both C4 and Wikipedia, it yields $\Kempirical{=}3$ on arXiv (1v2 $\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\Kempirical{=}1$, arXiv $\Kempirical{=}3$ (2v3 $\auc = 0.608$, CI $[0.593, 0.622]$)), indicating that domain structural complexity can rescue even web-text one-wash generators (Table~\ref{tab:domain_kstar}).
286	Larger models produce more human-like text, reducing 0v1 JSD: 0.16--0.29 at $\leq$1.5B, 0.077--0.13 at 7--14B.
287	However, Qwen-14B still yields $\Kempirical{=}2$ (1v2 $\auc = 0.621$, CI $[0.612, 0.630]$), with 0v1 $\auc = 0.960$ comparable to Qwen-7B ($0.964$), indicating that scale in the 1B--14B range does not shift the discrimination boundary.
288	
289	\paragraph{Sample-size control.}
290	As a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\Kempirical{=}1$ (1v2 $\auc = 0.601$, CI $[0.586, 0.616]$).
291	Reduced sample size widens confidence intervals and produces more conservative $\Kempirical$ estimates, confirming that arXiv's $\Kempirical{=}3$ at the same sample size reflects genuine domain signal rather than a statistical artifact of smaller training sets.
292	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55586f49-bdaf-4298-b641-67d4e6c9d3ff",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "a77677ba-2841-44d9-9302-07905653f370",
  "sourceToolAssistantUUID": "55586f49-bdaf-4298-b641-67d4e6c9d3ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-18T12:11:04.918Z_

I now have a comprehensive understanding of the paper. Let me compile the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a77677ba-2841-44d9-9302-07905653f370",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1cfxo8hmSXn3Kfofqj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5574363-da05-4872-ad99-11850cdd1a89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZEai7SZUWRAqjmtByvS4W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5803,
      "cache_read_input_tokens": 96319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5803,
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

_source line 63 · 2026-05-18T12:11:05.616Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RVfngwHDcEPtvkXbE6RnNh`</summary>

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
  "parentUuid": "f5574363-da05-4872-ad99-11850cdd1a89",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1cfxo8hmSXn3Kfofqj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "332e26b1-46b6-4247-be9c-10003ff13ff8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZEai7SZUWRAqjmtByvS4W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5803,
      "cache_read_input_tokens": 96319,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5803
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 96319,
          "cache_creation_input_tokens": 5803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5803,
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

_source line 64 · 2026-05-18T12:11:05.626Z_

<details><summary>↩ Tool result · `toolu_01RVfngwHDcEPtvkXbE6RnNh`</summary>

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
  "parentUuid": "332e26b1-46b6-4247-be9c-10003ff13ff8",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "f4742a9a-64e1-41b4-b948-ec2fbf6a696f",
  "sourceToolAssistantUUID": "332e26b1-46b6-4247-be9c-10003ff13ff8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-18T12:12:28.701Z_



Now I have thoroughly reviewed all paper materials. Let me produce the review.

## Summary

This paper formalizes recursive text generation as an iterated lossy channel, introduces K* (the generational discrimination boundary beyond which adjacent depths become statistically indistinguishable), and measures it empirically across 9 model configurations (5 architecture families, 1B-14B), 3 domains, and 4 decoding strategies. The central finding is K* in {1,2,3} with a domain hierarchy: Wikipedia(1) < C4(2) < arXiv(3). The paper validates that K*-aware binary filtering outperforms graduated weighting and DSIR on downstream benchmarks.

## Strengths

- **Well-defined research question.** The paper identifies a genuine gap: no prior work estimates generational depth of recursive synthetic text, and no prior work characterizes where depth discrimination saturates. The K* formulation is clean and operationally useful.

- **Thorough experimental coverage.** 9 model configurations across 5 architecture families (1B-14B), 3 domains, 4 decoding strategies. The breadth is impressive for an empirical characterization study. The domain hierarchy finding (Wiki < C4 < arXiv) is well-supported with cross-model evidence.

- **Extensive ablations and controls.** The paper addresses many potential confounds: scorer bias (cross-scorer validation, ANOVA decomposition), generation mode (rewrite vs. continuation), token length, self-BLEU leakage, feature subset stability, threshold sensitivity, base vs. instruct models. The Wikipedia scorer confound resolution is particularly careful.

- **Mistral dissociation is compelling.** K*=1 on C4 but K*=3 on arXiv for the same model is strong evidence that domain structure, not model identity, drives K*. This is the paper's most elegant empirical argument.

- **Honest reporting of marginal cases.** The paper transparently reports that Qwen-cont CI lower exceeds theta by only 0.002, that cross-scorer validation reduces some K*=2 to K*=1, and that LLaMA has 1/5 folds below threshold. This builds credibility.

- **Practical downstream validation.** The filtering experiments connect the measurement to an actionable outcome, and the dose-response analysis across contamination ratios adds ecological validity.

- **Strong appendix.** The extended analyses (JSD decay, feature subset stability, self-BLEU ablation, retrain-chain comparison, per-fold transparency) demonstrate thorough experimental methodology.

## Weaknesses

- **[idea-level] Major: The primary measurement (K*=2 for web text) rests on extremely thin statistical margins.** Seven of eight C4 configurations have 1v2 CI lower bounds exceeding theta=0.60 by margins ranging from 0.2pp to 4.5pp (Table extended). Three configurations (Qwen-cont at +0.2pp, LLaMA at +0.3pp, OLMo at +0.5pp) are within 0.5pp of the threshold. Cross-scorer validation reduces Qwen-cont to K*=1. When the headline finding depends on CI lower bounds exceeding a threshold by fractions of a percentage point, the distinction between K*=1 and K*=2 for web text becomes fragile. The paper's own subsampling analysis shows that reducing C4 to n=2,200 flips K* from 2 to 1. This is Major because the central claim (K*=2 is the "dominant mode" for web text) is sensitive to sample size, scorer choice, and threshold placement, undermining the generalizability of the specific K* values reported.

- **[idea-level] Major: The threshold theta=0.60 is presented as principled but is effectively arbitrary, and K* values are highly sensitive to it.** The justification layers (Cohen's h=0.20, permutation null <0.55, AUC discontinuity) do not converge on a single value; they merely establish that 0.60 is "reasonable." The theta sensitivity table shows that at theta=0.55, several configs jump to K*=3; at theta=0.625, OLMo drops to K*=1. The "sharp discontinuity" argument (5-11pp gap between 1v2 and 2v3) is the strongest defense, but this gap itself varies substantially across models (Qwen-rw: 10.6pp gap; OLMo: 6.5pp gap; Qwen-cont: 5.0pp gap). For marginal configurations, the gap is comparable to the threshold sensitivity range. This is Major because the specific K* values, which constitute the paper's primary contribution, change under reasonable alternative threshold choices, and no principled way to select theta from first principles is provided.

- **[idea-level] Minor: Limited practical impact of the filtering validation.** The absolute improvement from binary K*-aware filtering is modest: +0.76pp MMLU (p=0.074, not significant) and +0.89pp HellaSwag in the 100% synthetic setting. At realistic contamination ratios (10-50%), effect sizes diminish 3-6x. The Pythia replication shows near-negligible differences (MMLU: 0.2585 vs 0.2568; HellaSwag differences negligible). While the strategy ordering is consistent, the practical significance is limited. The paper acknowledges this but still lists it as a contribution.

- **[presentation-level] Minor: The reference list is thin for the scope of claims.** The main paper cites approximately 30 references, which is adequate, but the literature map reveals many relevant works that are listed as "cited: false" (Kirchenbauer 2023 on watermarking, Ippolito 2020, Zellers 2019 on early detection, Falahati 2026 on curated synthetic data, Mady 2026 on feature-augmented detection). For a paper claiming "first systematic measurement" in a space spanning model collapse, detection, and data curation, the Related Work could be more comprehensive. The Schaeffer 2025 taxonomy (8 definitions of model collapse) is cited but K*'s position within it (Family B, D4+D6) is not explicitly discussed in the Related Work section, missing an opportunity to precisely anchor the contribution.

- **[idea-level] Minor: The DPI theoretical framing overpromises relative to its contribution.** The paper invokes DPI to "derive" that finite K* must exist, but DPI only guarantees monotone non-increasing mutual information, not that a classifier-measurable discrimination boundary exists at any particular depth. The gap between K*_theory (information-theoretic) and K*_empirical (classifier-dependent) is acknowledged in the Conclusion but insufficiently addressed in the Method section. The theoretical contribution is essentially: "information degrades monotonically, so at some point you can't tell depths apart." This is conceptually obvious and does not require a formal DPI invocation. The proof adds limited value beyond motivation.

- **[presentation-level] Minor: The Qwen family dominates the experimental configurations.** Five of nine configurations are Qwen variants (1.5B-Instruct rewrite, 1.5B-Instruct continuation, 1.5B base, 7B, 14B). While spanning different scales and training variants, this creates a family imbalance: the "5 architecture families" framing somewhat obscures that Pythia, OLMo, LLaMA, and Mistral each have only one configuration. The paper acknowledges this in Limitations but the main text's "8/9 configurations" framing could mislead readers about the diversity of evidence.

- **[presentation-level] Minor: The "one-wash laundering" terminology is memorable but potentially misleading.** For C4, K*=2 means depths 1 and 2 ARE distinguishable, but depths 2 and 3 are not. The "one-wash" framing suggests a single pass erases all depth signal, but the paper actually shows that two generations of depth signal are preserved (0v1 and 1v2). The effect is better described as "two-wash saturation." The terminology conflates "generation passes after which further passes are undetectable" with "generation passes that erase all information," which is a different claim.

## Questions for Authors

- For the marginal configurations (Qwen-cont, LLaMA, OLMo), what is the probability that K*=2 would replicate with an independent data sample of the same size? The subsampling analysis shows K*=1 at n=2,200; is there a sample size between 2,200 and 5,000 where K* transitions?

- The cross-scorer validation reduces Qwen-cont from K*=2 to K*=1. If cross-scorer is the more rigorous condition, should the headline result be "6/9 configurations yield K*=2" rather than "8/9"? How do you reconcile reporting both numbers?

- The arXiv K*=3 finding relies on n=2,200 per model, and the paper shows that C4 at n=2,200 yields K*=1. How confident are you that arXiv K*=3 would hold at n=5,000, given that larger samples tighten CIs and could either confirm or reject the boundary?

- Why is the decoding ablation only conducted on Qwen-rewrite (Table S2) and Pythia (Table S10), both of which have relatively large margins above theta? Would decoding strategy affect K* for marginal configurations like OLMo or LLaMA?

- The retrain-chain experiment yields K*>=4, dramatically different from prompt-chain K*=2. Given that real-world contamination involves both mechanisms, what is the practical guidance? Should practitioners assume K*=2 or K*=4?

## Missing Experiments / Analyses

- **Larger models (13B+, 70B+).** The 1B-14B range covers "small to medium" open-source models. The claim that K* is bounded and domain-dependent would be substantially strengthened by even one 70B configuration, especially given the trend of decreasing 0v1 JSD with scale.

- **Effect size analysis for K* determination.** Rather than a binary "CI lower > theta?" criterion, reporting Cohen's d or standardized effect sizes for each depth pair would allow readers to assess the magnitude of discriminability, not just its statistical significance.

- **Non-English domains.** The paper studies only English text. Multilingual validation (even one language) would strengthen the generalization claim.

- **Calibration of the depth classifier on wild data.** The Common Crawl validation in the dream paper version is absent from the main paper. Some form of ecological validation beyond controlled experiments would strengthen practical claims.

- **Comparison with existing binary detection methods used as depth proxies.** Section 5.6 shows binary detectors fail as depth proxies, but a more thorough comparison using the actual Drayson et al. (2025) SIR method as a filtering baseline (not just "binary-Drayson" in the filtering table) would strengthen the positioning against the closest prior work.

## Overall Assessment

Score: 4/6
Confidence: high
Recommendation: Weak Accept

This paper addresses a well-motivated and timely question: at what generational depth does recursive synthetic text become indistinguishable from deeper generations? The problem formulation is clean, the experimental coverage across models, domains, and decoding strategies is thorough, and the domain hierarchy finding (Wiki < C4 < arXiv) is genuinely interesting and well-supported, especially through the Mistral dissociation. The paper is honest about marginal cases and limitations.

However, the two Major weaknesses are significant. First, the headline K*=2 finding for web text depends on statistical margins so thin (0.2-0.5pp for three of eight configurations) that it is fragile to scorer choice, sample size, and threshold. Second, the threshold theta=0.60 is effectively arbitrary despite layered justifications, and K* values shift substantially across the tested theta range. Together, these issues mean the specific K* values reported (which are the paper's primary deliverable) may not replicate robustly. The paper would benefit from reframing K* less as a crisp integer and more as a continuous measure of discriminability that saturates rapidly, which the JSD decay analysis already supports. The filtering validation, while directionally consistent, shows effect sizes too small to be practically compelling. Despite these concerns, the research direction is valuable, the experimental methodology is sound, and the domain-dependence finding is a genuine empirical contribution to the model collapse and data curation literatures.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4742a9a-64e1-41b4-b948-ec2fbf6a696f",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1d8UF4C8LZW8oWzX54",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d26fdc95-38f8-4311-97fd-005d5e0ec10a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRK8hmWsbvncRHRjXaaGJ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 684,
      "cache_read_input_tokens": 102122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 684,
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

_source line 66 · 2026-05-18T12:12:51.431Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01Nfr2Ft4zypPKNTbwfkit3u`</summary>

```json
{
  "report": "## Summary\n\nThis paper formalizes recursive text generation as an iterated lossy channel, introduces K* (the generational discrimination boundary beyond which adjacent depths become statistically indistinguishable), and measures it empirically across 9 model configurations (5 architecture families, 1B-14B), 3 domains, and 4 decoding strategies. The central finding is K* in {1,2,3} with a domain hierarchy: Wikipedia(1) < C4(2) < arXiv(3). The paper validates that K*-aware binary filtering outperforms graduated weighting and DSIR on downstream benchmarks.\n\n## Strengths\n\n- **Well-defined research question.** The paper identifies a genuine gap: no prior work estimates generational depth of recursive synthetic text, and no prior work characterizes where depth discrimination saturates. The K* formulation is clean and operationally useful.\n\n- **Thorough experimental coverage.** 9 model configurations across 5 architecture families (1B-14B), 3 domains, 4 decoding strategies. The breadth is impressive for an empirical characterization study. The domain hierarchy finding (Wiki < C4 < arXiv) is well-supported with cross-model evidence.\n\n- **Extensive ablations and controls.** The paper addresses many potential confounds: scorer bias (cross-scorer validation, ANOVA decomposition), generation mode (rewrite vs. continuation), token length, self-BLEU leakage, feature subset stability, threshold sensitivity, base vs. instruct models. The Wikipedia scorer confound resolution is particularly careful.\n\n- **Mistral dissociation is compelling.** K*=1 on C4 but K*=3 on arXiv for the same model is strong evidence that domain structure, not model identity, drives K*. This is the paper's most elegant empirical argument.\n\n- **Honest reporting of marginal cases.** The paper transparently reports that Qwen-cont CI lower exceeds theta by only 0.002, that cross-scorer validation reduces some K*=2 to K*=1, and that LLaMA has 1/5 folds below threshold. This builds credibility.\n\n- **Practical downstream validation.** The filtering experiments connect the measurement to an actionable outcome, and the dose-response analysis across contamination ratios adds ecological validity.\n\n- **Strong appendix.** The extended analyses (JSD decay, feature subset stability, self-BLEU ablation, retrain-chain comparison, per-fold transparency) demonstrate thorough experimental methodology.\n\n## Weaknesses\n\n- **[idea-level] Major: The primary measurement (K*=2 for web text) rests on extremely thin statistical margins.** Seven of eight C4 configurations have 1v2 CI lower bounds exceeding theta=0.60 by margins ranging from 0.2pp to 4.5pp (Table extended). Three configurations (Qwen-cont at +0.2pp, LLaMA at +0.3pp, OLMo at +0.5pp) are within 0.5pp of the threshold. Cross-scorer validation reduces Qwen-cont to K*=1. When the headline finding depends on CI lower bounds exceeding a threshold by fractions of a percentage point, the distinction between K*=1 and K*=2 for web text becomes fragile. The paper's own subsampling analysis shows that reducing C4 to n=2,200 flips K* from 2 to 1. This is Major because the central claim (K*=2 is the \"dominant mode\" for web text) is sensitive to sample size, scorer choice, and threshold placement, undermining the generalizability of the specific K* values reported.\n\n- **[idea-level] Major: The threshold theta=0.60 is presented as principled but is effectively arbitrary, and K* values are highly sensitive to it.** The justification layers (Cohen's h=0.20, permutation null <0.55, AUC discontinuity) do not converge on a single value; they merely establish that 0.60 is \"reasonable.\" The theta sensitivity table shows that at theta=0.55, several configs jump to K*=3; at theta=0.625, OLMo drops to K*=1. The \"sharp discontinuity\" argument (5-11pp gap between 1v2 and 2v3) is the strongest defense, but this gap itself varies substantially across models (Qwen-rw: 10.6pp gap; OLMo: 6.5pp gap; Qwen-cont: 5.0pp gap). For marginal configurations, the gap is comparable to the threshold sensitivity range. This is Major because the specific K* values, which constitute the paper's primary contribution, change under reasonable alternative threshold choices, and no principled way to select theta from first principles is provided.\n\n- **[idea-level] Minor: Limited practical impact of the filtering validation.** The absolute improvement from binary K*-aware filtering is modest: +0.76pp MMLU (p=0.074, not significant) and +0.89pp HellaSwag in the 100% synthetic setting. At realistic contamination ratios (10-50%), effect sizes diminish 3-6x. The Pythia replication shows near-negligible differences (MMLU: 0.2585 vs 0.2568; HellaSwag differences negligible). While the strategy ordering is consistent, the practical significance is limited. The paper acknowledges this but still lists it as a contribution.\n\n- **[presentation-level] Minor: The reference list is thin for the scope of claims.** The main paper cites approximately 30 references, which is adequate, but the literature map reveals many relevant works that remain uncited (Kirchenbauer 2023 on watermarking, Ippolito 2020, Zellers 2019 on early detection). For a paper claiming \"first systematic measurement\" in a space spanning model collapse, detection, and data curation, the Related Work could be more comprehensive. The Schaeffer 2025 taxonomy (8 definitions of model collapse) is cited but K*'s position within it (Family B, D4+D6) is not explicitly discussed in the Related Work section, missing an opportunity to precisely anchor the contribution.\n\n- **[idea-level] Minor: The DPI theoretical framing overpromises relative to its contribution.** The paper invokes DPI to \"derive\" that finite K* must exist, but DPI only guarantees monotone non-increasing mutual information, not that a classifier-measurable discrimination boundary exists at any particular depth. The gap between K*_theory (information-theoretic) and K*_empirical (classifier-dependent) is acknowledged in the Conclusion but insufficiently addressed in the Method section. The theoretical contribution is essentially: \"information degrades monotonically, so at some point you can't tell depths apart.\" This is conceptually obvious and does not require a formal DPI invocation.\n\n- **[presentation-level] Minor: The Qwen family dominates the experimental configurations.** Five of nine configurations are Qwen variants (1.5B-Instruct rewrite, 1.5B-Instruct continuation, 1.5B base, 7B, 14B). While spanning different scales and training variants, this creates a family imbalance: the \"5 architecture families\" framing somewhat obscures that Pythia, OLMo, LLaMA, and Mistral each have only one configuration. The paper acknowledges this in Limitations but the main text's \"8/9 configurations\" framing could mislead readers about the diversity of evidence.\n\n- **[presentation-level] Minor: The \"one-wash laundering\" terminology is memorable but potentially misleading.** For C4, K*=2 means depths 1 and 2 ARE distinguishable, but depths 2 and 3 are not. The \"one-wash\" framing suggests a single pass erases all depth signal, but the paper actually shows that two generations of depth signal are preserved (0v1 and 1v2). The effect is better described as \"two-wash saturation.\"\n\n## Questions for Authors\n\n- For the marginal configurations (Qwen-cont, LLaMA, OLMo), what is the probability that K*=2 would replicate with an independent data sample of the same size? The subsampling analysis shows K*=1 at n=2,200; is there a sample size between 2,200 and 5,000 where K* transitions?\n\n- The cross-scorer validation reduces Qwen-cont from K*=2 to K*=1. If cross-scorer is the more rigorous condition, should the headline result be \"6/9 configurations yield K*=2\" rather than \"8/9\"? How do you reconcile reporting both numbers?\n\n- The arXiv K*=3 finding relies on n=2,200 per model, and the paper shows that C4 at n=2,200 yields K*=1. How confident are you that arXiv K*=3 would hold at n=5,000, given that larger samples tighten CIs and could either confirm or reject the boundary?\n\n- Why is the decoding ablation only conducted on Qwen-rewrite (Table S2) and Pythia (Table S10), both of which have relatively large margins above theta? Would decoding strategy affect K* for marginal configurations like OLMo or LLaMA?\n\n- The retrain-chain experiment yields K*>=4, dramatically different from prompt-chain K*=2. Given that real-world contamination involves both mechanisms, what is the practical guidance? Should practitioners assume K*=2 or K*=4?\n\n## Missing Experiments / Analyses\n\n- **Larger models (13B+, 70B+).** The 1B-14B range covers \"small to medium\" open-source models. The claim that K* is bounded and domain-dependent would be substantially strengthened by even one 70B configuration, especially given the trend of decreasing 0v1 JSD with scale.\n\n- **Effect size analysis for K* determination.** Rather than a binary \"CI lower > theta?\" criterion, reporting Cohen's d or standardized effect sizes for each depth pair would allow readers to assess the magnitude of discriminability, not just its statistical significance.\n\n- **Non-English domains.** The paper studies only English text. Multilingual validation (even one language) would strengthen the generalization claim.\n\n- **Calibration of the depth classifier on wild data.** Some form of ecological validation (e.g., Common Crawl application with quality metric correlation) beyond controlled experiments would strengthen practical claims.\n\n- **Comparison with existing binary detection methods used as depth proxies.** Section 5.6 shows binary detectors fail as depth proxies, but a more thorough comparison using the actual Drayson et al. (2025) SIR method as a filtering baseline would strengthen the positioning against the closest prior work.\n\n## Overall Assessment\n\nScore: 4/6\nConfidence: high\nRecommendation: Weak Accept\n\nThis paper addresses a well-motivated and timely question: at what generational depth does recursive synthetic text become indistinguishable from deeper generations? The problem formulation is clean, the experimental coverage across models, domains, and decoding strategies is thorough, and the domain hierarchy finding (Wiki < C4 < arXiv) is genuinely interesting and well-supported, especially through the Mistral dissociation. The paper is honest about marginal cases and limitations.\n\nHowever, the two Major weaknesses are significant. First, the headline K*=2 finding for web text depends on statistical margins so thin (0.2-0.5pp for three of eight configurations) that it is fragile to scorer choice, sample size, and threshold. Second, the threshold theta=0.60 is effectively arbitrary despite layered justifications, and K* values shift substantially across the tested theta range. Together, these issues mean the specific K* values reported (which are the paper's primary deliverable) may not replicate robustly. The paper would benefit from reframing K* less as a crisp integer and more as a continuous measure of discriminability that saturates rapidly, which the JSD decay analysis already supports. The filtering validation, while directionally consistent, shows effect sizes too small to be practically compelling. Despite these concerns, the research direction is valuable, the experimental methodology is sound, and the domain-dependence finding is a genuine empirical contribution to the model collapse and data curation literatures.",
  "project": "gen-depth-contamination",
  "tier": "best",
  "dream_id": "dream_20260518T113009",
  "overall_score": "Weak Accept (4/6)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d26fdc95-38f8-4311-97fd-005d5e0ec10a",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1d8UF4C8LZW8oWzX54",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e93692d3-7363-4bc5-9ecf-3acaa06622d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRK8hmWsbvncRHRjXaaGJ3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 684,
      "cache_read_input_tokens": 102122,
      "output_tokens": 5952,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 684
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5952,
          "cache_read_input_tokens": 102122,
          "cache_creation_input_tokens": 684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 684,
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

_source line 67 · 2026-05-18T12:12:54.429Z_

<details><summary>↩ Tool result · `toolu_01Nfr2Ft4zypPKNTbwfkit3u`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260518T113009/best/review_report.md\", \"dream_id\": \"dream_20260518T113009\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e93692d3-7363-4bc5-9ecf-3acaa06622d5",
  "isSidechain": true,
  "promptId": "02714207-f157-4f7d-a36f-82ee7d9f24c7",
  "agentId": "aea58d8549abcc920",
  "type": "user",
  "uuid": "0f06e8ee-9917-45b0-9c7d-502edc4b00e4",
  "sourceToolAssistantUUID": "e93692d3-7363-4bc5-9ecf-3acaa06622d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-18T12:13:06.310Z_

Review submitted. Here is a summary of the key findings:

**Score: 4/6 (Weak Accept), Confidence: High**

**Two Major weaknesses identified:**

1. **Thin statistical margins for the headline K\*=2 claim.** Three of eight C4 configurations have CI lower bounds exceeding theta by less than 0.5pp. Cross-scorer validation flips Qwen-cont to K\*=1. The subsampling control at n=2,200 also yields K\*=1. The specific integer K\* values are fragile to sample size, scorer choice, and threshold placement.

2. **Arbitrary threshold theta=0.60.** Despite layered justifications (Cohen's h, permutation null, AUC gap), the threshold lacks a first-principles derivation, and K\* values shift substantially across the tested range [0.55, 0.70]. The paper's primary deliverable (specific K\* integers) changes under reasonable alternative thresholds.

**Key strengths:** Well-defined problem, thorough experimental breadth (9 configs, 5 families, 3 domains), extensive confound controls, compelling Mistral C4-to-arXiv dissociation (K\*=1 to K\*=3), and honest reporting of marginal cases.

**Recommendation:** Reframe K\* less as a crisp integer and more as a continuous discriminability measure that saturates rapidly (the JSD decay analysis already supports this). The domain-dependence finding is the paper's strongest and most replicable contribution.

The review report was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260518T113009/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f06e8ee-9917-45b0-9c7d-502edc4b00e4",
  "isSidechain": true,
  "agentId": "aea58d8549abcc920",
  "requestId": "req_011CbA1m9WUH5htCqvtUnDdF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "463afa3e-7a15-4114-a9a3-8b0222835bae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d37fb44e-7e5b-48a2-b4c1-fa5a7ae0cff1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xe9t8MXNB9Bi8dvRShPMv8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6082,
      "cache_read_input_tokens": 102806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6082,
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
