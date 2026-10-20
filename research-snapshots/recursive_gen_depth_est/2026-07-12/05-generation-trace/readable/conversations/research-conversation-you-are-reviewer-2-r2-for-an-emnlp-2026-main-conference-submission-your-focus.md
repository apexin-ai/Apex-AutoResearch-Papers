# Research conversation: You are Reviewer 2 (R2) for an EMNLP 2026 Main conference submission. Your focus areas are **novelty/significance** and 

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a48c96b0a4b83f8d3.jsonl`
- **Structured JSON:** [`3bbd25bceff1826305d4.json`](../../sessions/3b/3bbd25bceff1826305d4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

39 recorded events

### User

_source line 1 · 2026-05-17T09:00:43.436Z_

You are Reviewer 2 (R2) for an EMNLP 2026 Main conference submission. Your focus areas are **novelty/significance** and **related work positioning**.

## ARR Scoring Scale
- Overall: 1 (do not resubmit) to 5 (award-worthy). 4 = accept to conference, 3 = Findings, 2 = resubmit.
- Soundness: 1 (major issues) to 5 (excellent). 4 = strong, 3 = acceptable, 2 = poor.
- Excitement: 1 (not exciting) to 5 (highly exciting). 4 = exciting, 3 = interesting.
- Confidence: 1-5. Reproducibility: 1-5.
- Half-point increments allowed.

## Paper Summary

**Title**: "Characterizing Recursive Generation Depth: Feature-Based Estimation, Degradation Atlas, and Boundary Conditions"

**Core task**: Ordinal generation depth estimation — predicting how many recursive fine-tuning and re-generation cycles (depth d ∈ {0,1,2,3}) text has undergone, from text alone.

**Method**: 
- Recursive generation protocol: 3 base models (Pythia-1.4B, OLMo-1B, GPT-2 XL) × 3 decoding strategies (nucleus p=0.95, temp τ=0.9, top-k k=50) × 4 depths (d=0..3). BOS-seeded unconditional generation, 498-token passages, 1000 passages per condition. LoRA fine-tuning (rank 16, α=32) at each depth iteration.
- Feature extraction: 19 statistical features from a Pythia-160M reference model (6 perplexity stats, 5 surprisal stats, 4 lexical diversity, 4 distributional shape).
- Classification: Random Forest (500 trees, max depth 12) and L2-regularized logistic regression, stratified 5-fold CV.
- New metric: Effective Discriminable Depth (EDD) = max depth where all adjacent-depth AUC ≥ threshold T.

**Key results**:
- Controlled settings (within-strategy, BOS-seeded, 1-1.5B): 70-85% 4-class accuracy.
- Depth Degradation Atlas findings: (i) perplexity tail statistics universally dominate; (ii) inter-depth distances are non-uniform, EDD=3 at T=0.75; (iii) temperature sampling causes feature-boundary reversal at depth-1/depth-2 interface (cross-strategy LOO d1v2 AUC collapses to 0.13).
- Boundary conditions: 14B scale → 55% (EDD=1); prompted generation → 50% (EDD=1); web-crawl → 23-30% FPR.
- DCOL end-to-end learning fails (6 variants, best 64.5% vs RF 78.2%).
- Cross-strategy pipeline: strategy clf 57.5%, predicted two-stage (70.6%) < naive pooled (72.0%).

**Contributions claimed**:
1. Task formalization + benchmark
2. Depth Degradation Atlas (primary)
3. Boundary condition characterization
4. Negative result on end-to-end learning

**Related work sections**: Model Collapse & Recursive Training (Shumailov et al. 2024, Alemohammad et al. 2024, Dohmatob et al. 2024, Gerstgrasser et al. 2024, Drayson et al. 2025); Machine-Generated Text Detection (DetectGPT, Fast-DetectGPT, Binoculars, DivEye, LOKI, RADAR, authorship attribution); Watermarking (Kirchenbauer et al. 2023); Decoding Strategy Effects (Holtzman et al. 2020, Garcés Arias et al. 2025); Data Quality and Curation (DSIR, QuRating).

**Reference list**: ~22 references total.

## Your Review Task

Write a detailed review covering:

1. **Summary** (3-4 sentences)
2. **Strengths** (bulleted, with evidence)
3. **Weaknesses** (bulleted, with evidence, distinguishing major vs minor)
4. **Novelty assessment**: 
   - Is "ordinal generation depth estimation" genuinely a new task? How does it relate to model collapse characterization (which already studies depth-dependent degradation)?
   - Is the Depth Degradation Atlas a novel methodological contribution or primarily a systematic experiment?
   - Is the EDD metric novel and useful beyond this specific paper?
   - Are any of the findings surprising given prior work on model collapse and AI-text detection?
5. **Related work gaps**: 
   - Are important baselines missing? E.g., could existing detectors (Binoculars, Fast-DetectGPT) be adapted as baselines for depth estimation by calibrating their scores?
   - Is the related work on data contamination / synthetic data detection sufficient?
   - ~22 references seems low for EMNLP. What areas need more citations?
   - Is there work on multi-class AI-text detection or fine-grained provenance that should be discussed?
6. **Significance and impact**: Who benefits from this work? Is the practical impact convincing given the boundary conditions?
7. **Presentation quality**: Is the paper well-written? Is the story coherent? Any structural issues?
8. **Questions for authors** (up to 5)
9. **Scores**: Overall, Soundness, Excitement, Confidence, Reproducibility (use ARR scale with half-points)

Be rigorous but fair. Consider: does this paper advance understanding of a real problem, or is it a niche exercise with narrow applicability?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "90cec23e-0fd4-47a9-808a-25b14cd1804b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T09:00:43.443Z_

```json
{
  "parentUuid": "90cec23e-0fd4-47a9-808a-25b14cd1804b",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
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
  "uuid": "a12660d5-2aa6-488f-8bf3-db9247170624",
  "timestamp": "2026-05-17T09:00:43.443Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-17T09:00:47.635Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Pyn84xbcboW1oc443egSRx`</summary>

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
  "parentUuid": "a12660d5-2aa6-488f-8bf3-db9247170624",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sJERSzZegMDAVWss8h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e0cda44-f5ed-466a-95dc-c8bf520ca4c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYjKmx5GRYXjMp4qHUfFUu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8505,
      "cache_read_input_tokens": 8251,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8505
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 88,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 8505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8505,
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

_source line 4 · 2026-05-17T09:00:47.639Z_

<details><summary>↩ Tool result · `toolu_01Pyn84xbcboW1oc443egSRx`</summary>

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
  "parentUuid": "7e0cda44-f5ed-466a-95dc-c8bf520ca4c4",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "6b314f06-7d91-4ddf-9434-475e62aa76aa",
  "sourceToolAssistantUUID": "7e0cda44-f5ed-466a-95dc-c8bf520ca4c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T09:00:51.573Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01697ZrdrCVx5PFiYnK8AEoN`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b314f06-7d91-4ddf-9434-475e62aa76aa",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sJYLiZuMyyi1utSFaw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a15d3653-c68b-468c-9759-218a5e314f42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQGbQxLnzoa4VUTysXN5Lb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 16756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1270,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 6 · 2026-05-17T09:00:51.618Z_

<details><summary>↩ Tool result · `toolu_01697ZrdrCVx5PFiYnK8AEoN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **cross_strategy_pipeline_001** (success): Strategy classifier achieves >90% accuracy on 19 statistical features; two-stage pipeline (predict strategy then route to per-strategy depth RF) recovers cross-strategy depth accuracy to >=70% vs naive LOO 59.1% ← 基于 cross_strategy_loo_001\\n- **gen_length_ablation_001** (negative): Depth signal scales with passage length: 128-token passages are detectable but weaker; 512-token passages match 256-token baseline; cross-length accuracy spread ≤ 5pp ← 基于 mvp_pipeline_pythia_002\\n- **cross_seed_transfer_001** (success): If depth signal is an inherent property of recursive generation, an RF trained on seed=42 features should generalize to seed=43 features with cross-seed acc ≥ 75% (Δ ≤ 3pp vs within-seed) ← 基于 second_seed_replication_001\\n\\n## 趋势\\n成功 54 / 负向 9 / 失败 10 / 共 88\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ngpu-6000pro-2: 无 GPU 信息\\n\\n## 告警\\n- mvp_pipeline_001: 已被终止 — unknown\\n- mvp_pipeline_002: 已被终止 — unknown\\n- mvp_pipeline_003: 已被终止 — unknown\\n- mvp_pipeline_004: 已被终止 — unknown\\n- mvp_pipeline_base_002: 已被终止 — unknown\\n- mvp_pipeline_base_003: 已被终止 — unknown\\n- mvp_pipeline_pythia_001: 已被终止 — unknown\\n- mvp_pipeline_qwen_base_004: 已被终止 — unknown\\n- cross_model_olmo_001: 训练失败 — unknown\\n- dcol_deberta_001: 训练失败 — unknown\\n- cross_model_olmo_temp09_001: 已被终止 — unknown\\n- dcol_deberta_002: 训练失败 — unknown\\n- dcol_deberta_003: 已被终止 — unknown\\n- olmo_temp09_002: 已被终止 — unknown\\n- dcol_deberta_004: 已被终止 — unknown\\n- dcol_deberta_005: 训练失败 — unknown\\n- cross_model_loo_001: 已被终止 — unknown\\n- depth_extension_binary_pairwise_001: 训练失败 — unknown\\n- depth_extension_olmo_d4d5_001: 训练失败 — unknown\\n- pythia7b_cross_scale_001: 已被终止 — unknown\\n- wild_data_redpajama_dolma_001: 已被终止 — unknown\\n- wild_data_calibration_002: 训练失败 — unknown\\n- cross_scale_llama3_8b_001: 训练失败 — unknown\\n- cross_model_recursive_chain_001: 训练失败 — unknown\\n- cross_scale_llama3_8b_002: 训练失败 — unknown\\n\", \"total_chars\": 2002, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a15d3653-c68b-468c-9759-218a5e314f42",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "42b10619-3c2f-4eee-8363-2f248083e55d",
  "sourceToolAssistantUUID": "a15d3653-c68b-468c-9759-218a5e314f42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T09:00:52.070Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MungvY33LvLGa9PY3M2JDQ`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42b10619-3c2f-4eee-8363-2f248083e55d",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sJYLiZuMyyi1utSFaw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f38b401-be44-45bf-90d6-9c5f5b76140f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQGbQxLnzoa4VUTysXN5Lb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 16756,
      "output_tokens": 202,
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
          "output_tokens": 202,
          "cache_read_input_tokens": 16756,
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

_source line 8 · 2026-05-17T09:00:52.094Z_

<details><summary>↩ Tool result · `toolu_01MungvY33LvLGa9PY3M2JDQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml\", \"content\": \"# Literature Map — recursive_gen_depth_est\\n# Last updated: 2026-05-15\\n# Purpose: Systematic reference tracking for EMNLP ARR May 25 submission\\n# Total entries: 43 (35 original + 8 R2-N2 supplement)\\n#\\n# Tags used for cite_in: introduction, related-work, background, method,\\n#   experiments, discussion, limitations, dcol-section\\n\\n# =============================================================\\n# MODEL COLLAPSE — foundational theory & recursive generation\\n# =============================================================\\n\\nshumailov2024_nature:\\n  title: \\\"AI models collapse when trained on recursively generated data\\\"\\n  authors: [Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal]\\n  venue: Nature\\n  year: 2024\\n  doi: \\\"10.1038/s41586-024-07566-y\\\"\\n  tags: [model-collapse, recursive-generation, tail-erosion]\\n  relevance: direct\\n  cite_in: [introduction, related-work, background]\\n  notes: >\\n    Foundational model collapse paper. Tail erosion across recursive generations.\\n    Perplexity monotonically increases over 40 generations. Does NOT compare\\n    sampling strategies—uses standard sampling (T=1).\\n\\nmarchi2024_heat_death:\\n  title: \\\"Heat Death of Generative Models in Closed-Loop Learning\\\"\\n  authors: [Marchi, Soatto, Chaudhari, Tabuada]\\n  venue: ICASSP 2025\\n  year: 2024\\n  arxiv: \\\"2404.02325\\\"\\n  tags: [temperature, convergence, dynamical-systems, mode-collapse]\\n  relevance: direct\\n  cite_in: [discussion]\\n  notes: >\\n    Proves any T!=1 causes asymptotic degeneration. T<1 amplifies probability\\n    differences (mode collapse), T>1 contracts toward uniform. Key theoretical\\n    support for our tau=0.9 accelerated convergence finding.\\n\\ndohmatob2024_tale_of_tails:\\n  title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n  authors: [Dohmatob, Feng, Yang, Charton, Kempe]\\n  venue: ICML 2024\\n  year: 2024\\n  arxiv: \\\"2402.07043\\\"\\n  tags: [scaling-laws, tail-narrowing, tail-cutting, temperature, top-p, top-k]\\n  relevance: direct\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Distinguishes tail narrowing (temperature: q_i^T ~ i^{-beta/T}) from\\n    tail cutting (top-p/top-k: hard truncation). Different degradation patterns.\\n    Explains why temp produces different statistical fingerprint from truncation.\\n\\ndohmatob2025_strong_collapse:\\n  title: \\\"Strong Model Collapse\\\"\\n  authors: [Dohmatob, Feng, Subramonian, Kempe]\\n  venue: ICLR 2025 Spotlight\\n  year: 2025\\n  arxiv: \\\"2410.04840\\\"\\n  tags: [model-collapse, scaling, synthetic-data]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Even 0.1% synthetic data fraction causes collapse. Larger models amplify collapse.\\n    Bias-variance decomposition via random projections.\\n\\ndohmatob2024_demystified:\\n  title: \\\"Model Collapse Demystified: The Case of Regression\\\"\\n  authors: [Dohmatob, Feng, Kempe]\\n  venue: NeurIPS 2024\\n  year: 2024\\n  arxiv: \\\"2402.07712\\\"\\n  tags: [model-collapse, regression, random-matrix-theory]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Test error grows linearly with iteration count in regression.\\n    Supports our finding of monotonically evolving features across depths.\\n\\nalemohammad2024_mad:\\n  title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n  authors: [Alemohammad, Casco-Rodriguez, et al.]\\n  venue: ICLR 2024\\n  year: 2024\\n  arxiv: \\\"2307.01850\\\"\\n  tags: [autophagous, sampling-bias, precision-recall, MAD]\\n  relevance: indirect\\n  cite_in: [introduction, related-work]\\n  notes: >\\n    Biased sampling keeps precision but kills recall. Unbiased causes mode drift.\\n    tau=0.9 maps to their biased sampling regime.\\n\\ngerstgrasser2024_accumulate:\\n  title: \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\"\\n  authors: [Gerstgrasser, Schaeffer, et al.]\\n  venue: arXiv preprint\\n  year: 2024\\n  arxiv: \\\"2404.01413\\\"\\n  tags: [model-collapse, data-accumulation, mitigation]\\n  relevance: indirect\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Data accumulation prevents collapse (bounded test error).\\n    Important caveat: in accumulation regime, depth signal may be weaker.\\n\\ndrayson2025_detection_prevents_collapse:\\n  title: \\\"Machine-generated text detection prevents language model collapse\\\"\\n  authors: [Drayson et al.]\\n  venue: EMNLP 2025 Findings\\n  year: 2025\\n  arxiv: \\\"2502.15654\\\"\\n  tags: [temperature, diversity, recursive-training, detection]\\n  relevance: direct\\n  cite_in: [related-work]\\n  notes: >\\n    Temperature tau=0.9 produces most repetitive outputs; diversity drops ~70%\\n    over 99 recursive generations (GPT-2, SmolLM2). Perplexity degradation more\\n    moderate than deterministic methods. Detection as filter vs our depth estimation.\\n\\nbakshi2026_collapse_improvement:\\n  title: \\\"From Collapse to Improvement: Statistical Perspectives on Iterative Training\\\"\\n  authors: [Bakshi, Chakraborty]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2602.10531\\\"\\n  tags: [model-collapse, non-monotonic, data-mixing]\\n  relevance: indirect\\n  cite_in: [discussion]\\n  notes: >\\n    Iterative training with fresh real data can *improve* performance.\\n    Non-monotonic dynamics complicate simple depth-signal assumptions.\\n\\nwang2026_contamination:\\n  title: \\\"Can Generative AI Survive Data Contamination? Theoretical Guarantees\\\"\\n  authors: [Wang, Niu, Li]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2602.16065\\\"\\n  tags: [model-collapse, contamination, theoretical]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Extends collapse theory beyond Gaussian/discrete to realistic distributions.\\n    Provides theoretical grounding for depth signal existence.\\n\\nfalahati2026_curated:\\n  title: \\\"Curated Synthetic Data Doesn't Have to Collapse\\\"\\n  authors: [Falahati, Amiri, Larson, Golab]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2605.07724\\\"\\n  tags: [curation, collapse-prevention, pluralistic]\\n  relevance: indirect\\n  cite_in: [discussion, limitations]\\n  notes: >\\n    Pluralistic curation prevents collapse. Harder case for our method —\\n    curated pipelines may produce depth-invariant text.\\n\\nknowledge_collapse2025:\\n  title: \\\"Knowledge Collapse in LLMs: Fluency Survives but Facts Fail\\\"\\n  authors: [Keisha, Wu, Wang, Koshiyama, Treleaven]\\n  venue: arXiv preprint\\n  year: 2025\\n  arxiv: \\\"2509.04796\\\"\\n  tags: [knowledge-collapse, fluency, factual-degradation]\\n  relevance: indirect\\n  cite_in: [discussion]\\n  notes: >\\n    Three-stage collapse: factual accuracy degrades while fluency persists.\\n    Surface perplexity features still capture depth signal despite fluency preservation.\\n\\nsynthetic_eggs2026:\\n  title: \\\"Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning\\\"\\n  authors: [Schaffelder, Gatt]\\n  venue: ACL 2026 Findings\\n  year: 2026\\n  arxiv: \\\"2511.01490\\\"\\n  tags: [diversity, collapse-mitigation, Self-BLEU]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Multi-source synthetic data reduces collapse. Their diversity metrics\\n    (Self-BLEU, lexical diversity) are candidate depth features.\\n\\nmohamed2025_broken_telephone:\\n  title: \\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\"\\n  authors: [Mohamed, Geng, Vazirgiannis, Shang]\\n  venue: ACL 2025\\n  year: 2025\\n  arxiv: \\\"2502.20258\\\"\\n  tags: [iterative-generation, information-distortion, translation-chain]\\n  relevance: indirect\\n  cite_in: [discussion]\\n  notes: >\\n    Iterative generation (translation/paraphrase chains) produces monotonically\\n    increasing information distortion. Cross-task evidence that iterated signals\\n    accumulate — supports our depth signal persistence finding.\\n\\nsigma2026_spectral:\\n  title: \\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\"\\n  authors: [\\\"(multiple)\\\"]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2601.03385\\\"\\n  tags: [spectral-analysis, gram-matrix, representation-collapse, 50-generations]\\n  relevance: direct\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Gram matrix spectral analysis tracks representation space contraction over\\n    50 recursive generations. Proposes Sigma-UB metric. Complementary to our\\n    EDD — they measure geometric collapse, we measure statistical distinguishability.\\n    Tests 50 generations but does NOT do inter-generation classification.\\n\\n# --- R2-N2 supplement: model collapse empirical ---\\n\\nshi2025_closer_look:\\n  title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n  authors: [Shi, Wu, Zhang, Zhang, Tao, Qu]\\n  venue: NeurIPS 2025 (Spotlight)\\n  year: 2025\\n  arxiv: \\\"2509.16499\\\"\\n  tags: [model-collapse, entropy, memorization, intrinsic-dimension]\\n  relevance: direct\\n  role: background\\n  verified: true\\n  integration: \\\"整合，entropy ↔ depth signal 支撑特征选择论证\\\"\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Identifies generalization-to-memorization transition during recursive training.\\n    Entropy of training data decreases over iterations, strongly correlated with\\n    model degradation. Entropy decline IS a measurable depth signal — directly\\n    supports our statistical feature approach to depth estimation.\\n\\nyi2026_escaping_collapse:\\n  title: \\\"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\\\"\\n  authors: [Yi, Liu, Cheng, Xu]\\n  venue: 3rd DATA-FM Workshop @ ICLR 2026\\n  year: 2026\\n  arxiv: \\\"2510.16657\\\"\\n  tags: [model-collapse, verification, synthetic-data, mitigation]\\n  relevance: indirect\\n  role: background\\n  verified: true\\n  integration: \\\"引用但降级——related work 提一句，不支撑核心 claim（workshop paper）\\\"\\n  cite_in: [related-work]\\n  notes: >\\n    Verifier-guided retraining prevents collapse. Our depth estimation\\n    can serve AS the verifier — depth score enables graduated filtering\\n    rather than binary accept/reject. NOTE: workshop paper, not main conference.\\n\\n# =============================================================\\n# DECODING STRATEGIES\\n# =============================================================\\n\\nholtzman2020_nucleus:\\n  title: \\\"The Curious Case of Neural Text Degeneration\\\"\\n  authors: [Holtzman, Buys, Du, Forbes, Choi]\\n  venue: ICLR 2020\\n  year: 2020\\n  arxiv: \\\"1904.09751\\\"\\n  tags: [nucleus-sampling, temperature, text-degeneration, unreliable-tail]\\n  relevance: indirect\\n  cite_in: [background, method]\\n  notes: >\\n    Proposes nucleus sampling. Temperature+top-k leads to repetition.\\n    Key concept: unreliable tail of low-probability tokens.\\n\\nfinlayson2024_closing:\\n  title: \\\"Closing the Curious Case of Neural Text Degeneration\\\"\\n  authors: [Finlayson, Hewitt, Koller, Swayamdipta, Sabharwal]\\n  venue: ICLR 2024\\n  year: 2024\\n  arxiv: \\\"2310.01693\\\"\\n  tags: [softmax-bottleneck, truncation-sampling, precise-sampling]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Truncation sampling eliminates softmax bottleneck errors. Mechanistic\\n    difference between truncation and scaling approaches.\\n\\ngarces_arias2025_decoding_decoded:\\n  title: \\\"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\\\"\\n  authors: [Garces Arias et al.]\\n  venue: COLING 2025\\n  year: 2025\\n  tags: [decoding, hyperparameters, model-dependent]\\n  relevance: direct\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Confirms optimal decoding configuration is model-dependent.\\n    Directly supports D006 finding (strategy effect is model-dependent).\\n    Key external validation for our interaction effects claim.\\n\\nwiher2022_decoding:\\n  title: \\\"On Decoding Strategies for Neural Text Generators\\\"\\n  authors: [Wiher, Meister, Cotterell]\\n  venue: TACL 2022\\n  year: 2022\\n  tags: [decoding, task-dependent, evaluation]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Decoding strategy effects are task-dependent.\\n    Supports our finding that strategy effects on depth signal vary by model.\\n\\nbasu2021_mirostat:\\n  title: \\\"Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity\\\"\\n  authors: [Basu, Sachdev, Kamdar, Nishi]\\n  venue: ICLR 2021\\n  year: 2021\\n  tags: [perplexity-control, sampling, cross-entropy]\\n  relevance: indirect\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Perplexity and sampling parameters have non-linear relationship.\\n    Relevant to p90_ppl capturing depth signal better than mean_ppl\\n    under heavy-tailed distributions.\\n\\n# =============================================================\\n# BINARY / ZERO-SHOT DETECTION\\n# =============================================================\\n\\nmitchell2023_detectgpt:\\n  title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n  authors: [Mitchell, Lee, Khazatsky, Manning, Finn]\\n  venue: ICML 2023\\n  year: 2023\\n  arxiv: \\\"2301.11305\\\"\\n  tags: [zero-shot, detection, curvature, perturbation, binary]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Foundational zero-shot detector using log-probability curvature via\\n    random perturbations. Binary only. Fast-DetectGPT improves efficiency.\\n\\nsadasivan2023_paraphrase:\\n  title: \\\"Can AI-Generated Text be Reliably Detected?\\\"\\n  authors: [Sadasivan, Kumar, Balasubramanian, Wang, Feizi]\\n  venue: arXiv preprint\\n  year: 2023\\n  arxiv: \\\"2303.11156\\\"\\n  tags: [detection-limits, paraphrase-attack, impossibility]\\n  relevance: indirect\\n  cite_in: [related-work, limitations]\\n  notes: >\\n    Shows paraphrase attacks evade all detectors; proves impossibility\\n    result when model and human distributions overlap sufficiently.\\n    Important limitation context for our depth estimation approach.\\n\\nbinoculars2024:\\n  title: \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\"\\n  authors: [Hans, Schwarzschild, Manber, et al.]\\n  venue: ICML 2024\\n  year: 2024\\n  arxiv: \\\"2401.12070\\\"\\n  tags: [zero-shot, detection, perplexity-ratio, binary]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Two-model perplexity ratio for zero-shot binary detection.\\n    We extend beyond binary to ordinal depth.\\n\\nfast_detectgpt2024:\\n  title: \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\"\\n  authors: [Bao et al.]\\n  venue: ICLR 2024\\n  year: 2024\\n  arxiv: \\\"2310.05130\\\"\\n  tags: [zero-shot, detection, curvature, binary]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Conditional probability curvature for efficient binary detection.\\n    Cannot distinguish depth levels.\\n\\ndiveye2026:\\n  title: \\\"DivEye: Diversity Boosts AI-Generated Text Detection\\\"\\n  authors: [Basani, Chen]\\n  venue: ICLR 2026 / TMLR\\n  year: 2026\\n  arxiv: \\\"2509.18880\\\"\\n  tags: [surprisal-diversity, statistical-features, detection]\\n  relevance: direct\\n  cite_in: [related-work, method]\\n  notes: >\\n    Token-level surprisal diversity features for binary detection.\\n    Feature overlap with our pipeline. We extend similar features\\n    to ordinal depth regression.\\n\\nloki2025:\\n  title: \\\"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\\\"\\n  authors: [Ye, Zhou, Huang, Zhang, Bai, Kang, He, Lin, Wang, Wu, Wu, Chen, Lin, He, Li]\\n  venue: ICLR 2025 Spotlight\\n  year: 2025\\n  arxiv: \\\"2410.09732\\\"\\n  tags: [benchmark, multimodal, detection]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Multimodal synthetic data detection benchmark. Binary only, no depth.\\n\\ngehrmann2019_gltr:\\n  title: \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\"\\n  authors: [Gehrmann, Strobelt, Rush]\\n  venue: ACL 2019\\n  year: 2019\\n  arxiv: \\\"1906.04043\\\"\\n  tags: [detection, statistical-features, perplexity, rank, entropy]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Foundational statistical detection using log-likelihood, rank, entropy.\\n    Our feature system extends this paradigm to recursive depth estimation.\\n\\npudasaini2026_detection_fails:\\n  title: \\\"Why AI-Generated Text Detection Fails: Evidence from Explainable AI\\\"\\n  authors: [Pudasaini et al.]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2603.23146\\\"\\n  tags: [detection-failure, distribution-shift, fragility]\\n  relevance: indirect\\n  cite_in: [limitations]\\n  notes: >\\n    Detection features degrade under distribution shift.\\n    If binary features are domain-fragile, ordinal depth features may be too.\\n\\n# --- R2-N2 supplement: detection methods ---\\n\\ntulchinskii2024_intrinsic_dim:\\n  title: \\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\"\\n  authors: [Tulchinskii, Kuznetsov, et al.]\\n  venue: NeurIPS 2023\\n  year: 2023\\n  arxiv: \\\"2306.04723\\\"\\n  tags: [intrinsic-dimension, geometric-features, detection, cross-domain]\\n  relevance: direct\\n  role: method-component\\n  cite_in: [related-work, method]\\n  notes: >\\n    Intrinsic dimension of text embeddings ~9 for human, ~7.5 for AI-generated.\\n    Geometric invariant enables cross-domain, cross-model robust detection.\\n    Complementary feature family to our statistical perplexity features —\\n    intrinsic dimension could serve as additional depth feature.\\n\\nverma2024_ghostbuster:\\n  title: \\\"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\\\"\\n  authors: [Verma, Fleisig, Tomlin, Klein]\\n  venue: NAACL 2024\\n  year: 2024\\n  arxiv: \\\"2305.15047\\\"\\n  tags: [detection, structured-search, statistical-features, cross-domain]\\n  relevance: indirect\\n  role: direct-competitor\\n  cite_in: [related-work]\\n  notes: >\\n    Structured search over combinations of weaker LM features for detection.\\n    99.0 F1 cross-domain. Binary only. Feature engineering approach parallels\\n    our multi-feature pipeline but targets binary classification, not ordinal depth.\\n\\nli2024_mage:\\n  title: \\\"MAGE: Machine-generated Text Detection in the Wild\\\"\\n  authors: [Li, Li, et al.]\\n  venue: ACL 2024\\n  year: 2024\\n  arxiv: \\\"2305.13242\\\"\\n  tags: [benchmark, cross-domain, cross-model, detection]\\n  relevance: indirect\\n  role: evaluation\\n  cite_in: [related-work]\\n  notes: >\\n    Cross-domain cross-model detection benchmark. Finds significant OOD\\n    performance degradation — same generalization challenge our cross-model\\n    depth estimation faces. Binary detection only.\\n\\nwu2025_detection_survey:\\n  title: \\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\"\\n  authors: [Wu, Yang, Zhan, Yuan, Chao, Wong]\\n  venue: Computational Linguistics, Vol. 51, Issue 1\\n  year: 2025\\n  arxiv: \\\"2310.14724\\\"\\n  tags: [survey, detection-taxonomy, watermarking, statistical, neural]\\n  relevance: indirect\\n  role: background\\n  verified: true\\n  integration: \\\"整合，survey 定位\\\"\\n  cite_in: [related-work]\\n  notes: >\\n    Comprehensive survey of detection paradigms: watermarking, statistical,\\n    neural, human-assisted. Positions our work as extending the statistical\\n    paradigm from binary detection to ordinal depth estimation.\\n\\n# =============================================================\\n# ADJACENT TASK — editing extent, attribution\\n# =============================================================\\n\\neditlens2026:\\n  title: \\\"EditLens: Quantifying the Extent of AI Editing in Text\\\"\\n  authors: [Thai et al.]\\n  venue: ICLR 2026\\n  year: 2026\\n  arxiv: \\\"2510.03154\\\"\\n  tags: [editing-extent, continuous-score, mixed-authorship]\\n  relevance: direct\\n  cite_in: [introduction, related-work]\\n  notes: >\\n    Closest conceptual neighbor — both go beyond binary classification.\\n    EditLens = single-pass editing extent; ours = multi-generation depth.\\n\\nuchendu2020_attribution:\\n  title: \\\"Authorship Attribution for Neural Text Generation\\\"\\n  authors: [Uchendu, Le, Shu, Lee]\\n  venue: EMNLP 2020\\n  year: 2020\\n  tags: [attribution, multi-source, authorship]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Multi-source attribution (which model?). We solve a different axis\\n    (how many iterations?) — complementary problems.\\n\\npu2026_generator_barrier:\\n  title: \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\"\\n  authors: [Pu, Cheng, Yuan, Wu, Bi]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2604.13692\\\"\\n  tags: [disentanglement, cross-generator, generalization]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Cross-generator generalization via disentanglement.\\n    Analogous to our cross-model generalization challenge.\\n\\n# --- R2-N2 supplement: attribution paradigms ---\\n\\nbevendorff2025_two_paradigms:\\n  title: \\\"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\\\"\\n  authors: [Bevendorff, Wiegmann, Richter, Potthast, Stein]\\n  venue: ACL 2025 Findings\\n  year: 2025\\n  tags: [attribution, verification, detection-paradigm, authorship]\\n  relevance: direct\\n  role: background\\n  verified: true\\n  integration: \\\"整合，'第三范式' framing（attribution/verification 之外的正交第三维度）\\\"\\n  cite_in: [related-work]\\n  notes: >\\n    Reframes LLM detection as authorship verification (not attribution).\\n    Our depth estimation is a third paradigm — ordinal characterization\\n    beyond binary verification or multi-class attribution. Key framing\\n    reference for positioning our contribution.\\n\\n# =============================================================\\n# METHOD COMPONENT — ordinal classification\\n# =============================================================\\n\\ncoral2020:\\n  title: \\\"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\\\"\\n  authors: [Cao, Mirjalili, Raschka]\\n  venue: Pattern Recognition Letters\\n  year: 2020\\n  arxiv: \\\"1901.07884\\\"\\n  tags: [ordinal-classification, rank-consistency, cumulative-logits]\\n  relevance: direct\\n  cite_in: [method, experiments]\\n  notes: >\\n    CORAL ordinal classification framework used in our baseline battery.\\n    Rank-consistent cumulative logits for ordinal targets.\\n\\ncloc2025:\\n  title: \\\"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\\\"\\n  authors: [Pitawela, Carneiro, et al.]\\n  venue: CVPR 2025\\n  year: 2025\\n  arxiv: \\\"2504.17813\\\"\\n  tags: [contrastive-learning, ordinal, multi-margin, N-pair]\\n  relevance: direct\\n  cite_in: [method, dcol-section]\\n  notes: >\\n    DCOL is our adaptation of CLOC to text depth estimation.\\n    Multi-margin N-pair loss for ordinal-aware contrastive learning.\\n    Must cite as methodological basis for DCOL section.\\n\\n# =============================================================\\n# WATERMARKING\\n# =============================================================\\n\\nkirchenbauer2023_watermark:\\n  title: \\\"A Watermark for Large Language Models\\\"\\n  authors: [Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein]\\n  venue: ICML 2023\\n  year: 2023\\n  arxiv: \\\"2301.10226\\\"\\n  tags: [watermarking, proactive-detection, green-list]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Proactive detection via watermarking. Complementary —\\n    watermarking requires generator cooperation; our method is post-hoc.\\n\\n# =============================================================\\n# DATA CURATION\\n# =============================================================\\n\\ndsir2023:\\n  title: \\\"Data Selection for Language Models via Importance Resampling\\\"\\n  authors: [Xie, Santurkar, Ma, Liang]\\n  venue: NeurIPS 2023\\n  year: 2023\\n  arxiv: \\\"2302.03169\\\"\\n  tags: [data-selection, importance-resampling, curation]\\n  relevance: indirect\\n  cite_in: [discussion]\\n  notes: >\\n    Quality-based data selection for LM training.\\n    Our depth estimation enables depth-graduated curation (Claim 3 / Discussion).\\n\\nqurating2024:\\n  title: \\\"QuRating: Selecting High-Quality Data for Training Language Models\\\"\\n  authors: [Wettig, Gupta, et al.]\\n  venue: ICML 2024\\n  year: 2024\\n  arxiv: \\\"2402.09739\\\"\\n  tags: [quality-rating, data-curation, LLM-judgments]\\n  relevance: indirect\\n  cite_in: [discussion]\\n  notes: >\\n    LLM-based quality rating for data selection.\\n    Our depth score is a complementary quality axis.\\n\\n# --- R2-N2 supplement: data curation at scale ---\\n\\npenedo2024_fineweb:\\n  title: \\\"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\\\"\\n  authors: [Penedo, Kydlicek, et al.]\\n  venue: NeurIPS 2024\\n  year: 2024\\n  arxiv: \\\"2406.17557\\\"\\n  tags: [data-curation, quality-filtering, deduplication, web-scale]\\n  relevance: indirect\\n  role: background\\n  cite_in: [discussion]\\n  notes: >\\n    15T token dataset with systematic quality filtering pipeline (dedup,\\n    heuristic filters, classifier-based selection). Our depth estimation\\n    adds a synthetic contamination axis complementary to FineWeb-style\\n    quality curation — depth score can flag recursively degraded text\\n    that passes standard quality filters.\\n\\n# =============================================================\\n# COVARIATE SHIFT — technical background\\n# =============================================================\\n\\nsugiyama2007_importance_weighting:\\n  title: \\\"Covariate Shift Adaptation by Importance Weighted Cross Validation\\\"\\n  authors: [Sugiyama, Krauledat, Mueller]\\n  venue: JMLR\\n  year: 2007\\n  tags: [covariate-shift, importance-weighting, domain-adaptation]\\n  relevance: background\\n  cite_in: [discussion]\\n  notes: >\\n    Theoretical foundation for covariate shift correction.\\n    Our z-score normalization is a simplified distribution alignment.\\n\\n# =============================================================\\n# COVERAGE CHECKLIST (paper_framing.md Dream D002 requirements)\\n# =============================================================\\n# [x] watermarking: kirchenbauer2023_watermark\\n# [x] model collapse theory: shumailov2024_nature, alemohammad2024_mad,\\n#     dohmatob2024_tale_of_tails, dohmatob2025_strong_collapse,\\n#     dohmatob2024_demystified, gerstgrasser2024_accumulate\\n# [x] model collapse empirical: drayson2025, bakshi2026, marchi2024,\\n#     shi2025_closer_look (VERIFIED), yi2026_escaping_collapse (VERIFIED, workshop)\\n# [x] data curation: dsir2023, qurating2024, penedo2024_fineweb (NEW)\\n# [x] multi-source attribution: uchendu2020_attribution,\\n#     bevendorff2025_two_paradigms (VERIFIED)\\n# [x] binary detectors: mitchell2023_detectgpt, sadasivan2023_paraphrase,\\n#     binoculars2024, fast_detectgpt2024, diveye2026, loki2025,\\n#     tulchinskii2024_intrinsic_dim (NEW), verma2024_ghostbuster (NEW),\\n#     li2024_mage (NEW)\\n# [x] detection survey: wu2025_detection_survey (VERIFIED)\\n# [x] decoding strategy effects: garces_arias2025, holtzman2020_nucleus,\\n#     wiher2022_decoding, basu2021_mirostat, finlayson2024_closing\\n# [x] ordinal classification: coral2020, cloc2025\\n# [x] adjacent tasks: editlens2026\\n# [x] covariate shift: sugiyama2007\\n# [x] statistical detection foundation: gehrmann2019_gltr\\n#\\n# Total unique entries: 43 (35 original + 8 R2-N2 supplement)\\n# 2024-2026 papers: 30/43 (70% recent coverage)\\n# Direct relevance: 12 entries\\n\", \"total_chars\": 26296, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f38b401-be44-45bf-90d6-9c5f5b76140f",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "831243bc-71aa-45ce-80e3-2d0d0473acc8",
  "sourceToolAssistantUUID": "7f38b401-be44-45bf-90d6-9c5f5b76140f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T09:00:56.996Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XXiNGHmTVny4UGnzCbeyBs`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "831243bc-71aa-45ce-80e3-2d0d0473acc8",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sJsTALMwzFDYzVmxGm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbd1ebf1-ffcb-4984-8bb1-fce2061e5d2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WV6CjGvqHQfEpY82GQrp2Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10601,
      "cache_read_input_tokens": 18026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10601,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 10 · 2026-05-17T09:00:57.009Z_

<details><summary>↩ Tool result · `toolu_01XXiNGHmTVny4UGnzCbeyBs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper_framing.md\", \"content\": \"# Paper Framing — recursive_gen_depth_est\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\\n- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)\\n- EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit\\n\\n## Core Claims (3 条 + Discussion implication)\\n\\n1. **Ordinal depth estimation is feasible, accurate, and robust across scales and generation modes**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features from reference-model perplexity distributions. On our 3-model × 3-strategy benchmark (1–1.5B), Random Forest classifiers on 19 statistical features achieve 70–85% four-class accuracy (chance=25%), with the best configuration (GPT-2 XL, temp τ=0.9) reaching 85.4%. Feature-based methods (RF, CORAL, DivEye) consistently outperform single-feature baselines across all settings. **Scale robustness**: Clean FP16 13B experiment (Qwen2.5-14B, no quantization) confirms depth signal persists at mainstream model scale, addressing the \\\"small model only\\\" concern from prior 7B QLoRA experiments. **Ecological validity**: Prompted generation experiment (topic-seeded text, not BOS-only unconditional) confirms depth signal is not an artifact of unnatural generation mode.\\n\\n2. **Depth Degradation Atlas — systematic characterization of recursive collapse** (PRIMARY): We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) perplexity tail statistics (p90_ppl) and surprisal variance (var_surprisal) as the dominant depth signal family — consistently occupying the top-4 features across all models and strategies, though their relative ranking is model-dependent, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable, and (d) **strategy-dependent feature trajectory reversal** — temperature sampling causes the depth-1→depth-2 feature boundary to invert relative to nucleus/top-k (cross-strategy LOO d1v2 AUC as low as 0.13), demonstrating that decoding strategy fundamentally shapes the degradation trajectory rather than merely attenuating it, and (e) **accelerated convergence mechanism** — root cause analysis confirms a genuine structural distributional shift: temperature's uniform logit scaling (vs nucleus/top-k truncation) accelerates convergence to the attractor distribution, so temp09 depth N features ≈ nucleus/topk50 depth N+1 (GPT-2 XL temp09 d1 p90_ppl median=92.2, falls into nucleus/topk50 d2 range 65–92). This is not a simple scale artifact fixable by normalization — z-score normalization improves overall LR cross-strategy accuracy (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), and does **not** improve tree-based classifiers (RF Δ<0.02pp) — confirming a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation methods could recover the d1/d2 boundary remains open. This atlas spans 3 model families × 3 decoding strategies, with scale consistency confirmed at 14B.\\n\\n3. **Cross-strategy depth estimation via two-stage pipeline + strategy-invariant signal discovery**: Naive cross-strategy transfer degrades to 59.1% with d1v2 boundary inversion. We propose a two-stage solution: (a) strategy identification classifier (57.8% — strategies share more feature space than expected), then (b) strategy-conditioned depth classifiers. The pipeline improves cross-strategy accuracy by **+11.5pp** on average (59.1% → 70.5%), with per-model results: GPT-2 XL 73.0%, OLMo 69.4%, Pythia 69.3%. Oracle ceiling at 78.3%. **Caveat**: improvement is consistent across models but absolute accuracy varies (2/3 models individually below 70%); paper must claim \\\"+11.5pp improvement\\\" rather than \\\"≥70% universal recovery\\\". The surprising finding: even with imperfect strategy routing, the pipeline works because depth signal has a **strategy-invariant core** (~60% accuracy floor) plus a strategy-specific component. This reframes cross-strategy transfer from \\\"broken\\\" to \\\"substantially improved with clear ceiling for future work\\\".\\n\\n4. **[Discussion — Practical Implication]** Depth-graduated curation as alternative to binary filtering: predicted depth provides a finer-grained quality proxy than binary real/synthetic labels, enabling graduated weighting strategies. Conceptual argument supported by depth-accuracy correlation in 3×3 matrix data; full experimental validation deferred to future work (D012).\\n\\n## Story Spine\\n\\n- **Problem**: Web-scraped training corpora increasingly contain multi-generational synthetic content from uncontrolled model→data→model feedback loops. Existing detectors answer \\\"is this synthetic?\\\" but not \\\"how many recursive cycles has this undergone?\\\" — a critical distinction since 1st-gen synthetic data can improve training while deeply recursive text drives distribution collapse.\\n\\n- **Existing approaches & gaps**: Binary detectors (LOKI, DivEye, Binoculars) classify real vs. synthetic but discard ordinal depth information. EditLens estimates single-pass AI editing extent but not recursive depth. Model collapse studies (Drayson et al. EMNLP 2025; Shumailov et al. Nature 2024) characterize degradation patterns but assume depth is known a priori — no method estimates depth from text alone.\\n\\n- **Our framing**: We formalize ordinal generation depth estimation as a new task, construct a multi-generational benchmark spanning 1B–14B models across 3 decoding strategies and 4 depths, and provide the first **Depth Degradation Atlas** — a systematic empirical map of how text statistical properties evolve across recursive depths, models, and strategies. The Atlas reveals (a) perplexity tail statistics as universal depth markers across all settings, (b) model-dependent strategy interaction effects with an identified root cause, and (c) the Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable. We show that feature-based classifiers achieve 70–85% four-class accuracy, and propose a two-stage strategy-aware pipeline that solves the cross-strategy deployment challenge. The depth signal persists under prompted generation (not just BOS-seeded), confirming ecological relevance.\\n\\n- **Headline result template**: \\\"On our multi-generational benchmark spanning model scales from 1B to 14B and 3 decoding strategies, feature-based ordinal depth estimation achieves 70–85% accuracy (chance=25%), with perplexity tail statistics (p90_ppl, var_surprisal) consistently among the top-4 features across all settings. The depth signal persists under prompted (topic-seeded) generation and at 14B scale without quantization. The Depth Degradation Atlas reveals that effective discriminable depth extends to depth 3 in 7/9 settings (T=0.75). We identify strategy-dependent feature trajectory reversal and propose a two-stage pipeline that restores near within-strategy accuracy for cross-strategy deployment.\\\"\\n- **Note**: 4-class (depth 0-3) is the confirmed setting. 6-class (depth 0-5) completed via plan_011.\\n\\n## DCOL Status — Contingency Activated (D010/D011, 2026-05-15)\\n\\nDCOL v1–v5 全部失败（embedding collapse / OOM / catastrophic forgetting / 超参违规 / NaN 梯度爆炸）。\\n\\n- **Claim 2 (Atlas/EDD) 升为 PRIMARY contribution**\\n- **Claim 1**: Feature-based methods (RF/CORAL/DivEye) 作为 depth estimation 方法，不依赖 DCOL\\n- **DCOL v6 (RoBERTa-large)**: 非阻塞尝试。成功 → Section 5 bonus；失败 → negative analysis section（\\\"contrastive ordinal learning 在文本深度估计的固有局限\\\"）\\n- **Paper type**: Task formalization + systematic empirical study + practical framework（非 method paper）\\n- Atlas + EDD + feature universality + model-strategy interaction = 充分支撑 EMNLP \\\"New Missions\\\" track\\n\\n## Venue Fit Risks\\n\\n- **\\\"Just an empirical study\\\" risk**: Primary risk now that DCOL is demoted. Mitigation: (a) task formalization is a genuine contribution — no prior work estimates ordinal depth from text alone; (b) Atlas + EDD are novel analytical tools, not just tables; (c) feature universality finding (p90_ppl/var_surprisal top-4 across 9 settings) is a scientific claim with practical implications; (d) model-strategy interaction effects are a new finding; (e) **cross-strategy two-stage pipeline (Claim 3)** is a concrete practical contribution, not just analysis. EMNLP \\\"New Missions\\\" track explicitly values problem formalization.\\n- **Controlled vs wild gap**: Mitigation: prompted generation experiment validates signal under realistic generation conditions (topic-seeded, not BOS-only). Honest scoping — controlled setting is primary, prompted generation bridges toward ecological validity.\\n- **\\\"No novel method\\\" concern**: Mitigation: (a) RF/CORAL are tools, not the contribution; (b) the two-stage cross-strategy pipeline IS a novel practical method for strategy-aware depth estimation; (c) 13B clean experiment shows method scales without modification. Analogous to benchmark/analysis papers at top venues (e.g., HELM, MMLU).\\n- **\\\"Small model only\\\" concern**: Eliminated by clean 13B FP16 experiment. Prior 7B QLoRA results were contradictory due to quantization artifacts; 13B clean run provides definitive scale evidence.\\n\\n## Dream-Derived Requirements (D002, 2026-05-14)\\n\\n三档(best 3.0 / median 3.0 / worst 2.5)一致指出的结构性必修项：\\n\\n### 论文写作硬约束\\n1. **DCOL loss 描述** — 若 v6 成功：Eq.1 必须包含 attractive + repulsive 双项（N-pair formulation）。若 v6 失败：negative analysis section 描述失败模式和根因分析，无需完整 loss 公式\\n2. **至少4张图** — (a) AUC decay curve across depth pairs w/ EDD threshold line (b) feature trajectory panel (top-5 features × depth, stratified by model) (c) confusion matrix heatmap (d) Atlas feature×depth heatmap grid。\\\"Atlas without maps is a contradiction\\\"\\n3. **Bibliography 25+ references** — 必须覆盖: watermarking (Kirchenbauer ICML 2023), model collapse theory (Alemohammad ICLR 2024, Dohmatob 2024, Gerstgrasser 2024), data curation (DSIR, QuRating), multi-source attribution (Uchendu 2020), binary detectors (Binoculars Hans ICML 2024, Fast-DetectGPT Bao 2024), decoding strategy effects (Garces Arias COLING 2025, Holtzman ICLR 2020)\\n4. **Surprisal reference model** — 必须明确指定 reference model、说明 cross-model LOO 时如何处理、讨论 circularity\\n\\n### 指标报告硬约束\\n5. **d1-d5 only accuracy** — 作为 companion metric 报告，隔离 ordinal depth estimation 与 binary human-vs-machine detection\\n6. **EDD threshold sensitivity** — 报告 AUC threshold 在 0.65/0.70/0.75/0.80 四档下的 EDD 值\\n7. **k-NN inference 完整规格** — k 值、distance metric、sensitivity analysis\\n\\n### Framing 方向\\n8. **Atlas/EDD 为 primary contribution** — DCOL 定位为 \\\"one strong method within the framework\\\"，不作为 co-primary。三档审稿均认为 DCOL 是 incremental adaptation of CLOC。与 DCOL Contingency 一致。\\n9. **\\\"First systematic empirical map\\\" 需限定** — Shumailov/Drayson 已有 characterization, 我们的新颖性在 ordinal estimation lens + EDD formalization + multi-model multi-strategy coverage\\n\\n### Cross-Strategy 反转硬约束 (D015, Reviewer 降级条件)\\n10. **三档策略分类** — 论文不得将 nucleus 和 temperature 归为同一类 \\\"soft sampling\\\"。必须采用三档：nucleus（baseline 稳定）、temperature（信号增强但存在 d1v2 方向反转风险）、topk（信号衰减但方向一致）。D004 的 \\\"soft sampling\\\" 分组已被反转数据推翻。\\n11. **Discussion 必须含 per-strategy d1v2 AUC 表** — 包含 0.13/0.25 反转值 + **已确认的机制**：temperature 均匀缩放 logit（非截断）加速模型收敛到 attractor 分布（genuine structural distributional shift），temp09 depth N ≈ nucleus/topk50 depth N+1。z-score 标准化提升整体 LR 跨策略 acc（25%→61%）但**不恢复** pairwise d1v2 AUC（GPT-2 XL 0.50→0.24, OLMo 0.50→0.19），证实这是结构性几何偏移而非可校正的尺度差异。\\n12. **Limitations 必须写明跨策略部署约束** — \\\"跨策略部署时需先验知道目标策略类型，否则 d1/d2 预测可能反转。\\\"不可仅将反转作为正面发现消化。\\n\\n## Anticipated Reviewer Concerns\\n\\n1. \\\"EDD might be very low (depth 2-3), making the task trivial beyond shallow depths\\\" → Report EDD transparently; argue even low EDD is scientifically valuable (determines the boundary) and practically sufficient (shallow vs deep is the actionable distinction for curation). Data: 7/9 settings EDD≥3 at T=0.75. **Depth extension bootstrap (D027)**: 三模型 d3v4 AUC 聚集在 0.75 附近 (Pythia 0.784 p=0.001 ✅, OLMo 0.765 p=0.091 ⚠️, GPT-2 XL 0.750 p=0.505 ❌)，仅 Pythia 统计显著。**禁止**写 \\\"three models all achieve statistically significant EDD=4\\\"。正确措辞：\\\"d3v4 AUC consistently clusters near the 0.75 threshold (0.750–0.784) across all three models, while d4v5 AUC uniformly falls below 0.70 (0.681–0.694)\\\"——强调方向一致性 + 完整报告 CI 和 p-values。D024 连续衰减曲线叙事被 bootstrap 数据强力支持。\\n2. \\\"Why ordinal and not just binary?\\\" → d0v1 AUC=0.998 vs d1v2=0.861 vs d2v3=0.801 — ordinal structure captures monotonically decreasing but still significant discrimination at all adjacent pairs\\n3. \\\"Generalization to unseen models/strategies?\\\" → Cross-model LOO: mean 66.4% (holdout Pythia 62.4%, OLMo 69.2%, GPT-2 XL 67.6%) — all >chance but depth_0 recall >98% inflates headline. **Must report per-class recall** (depth_2 recall as low as 26.8%). Cross-strategy LOO: mean 59.1% (51.5–69.4%), topk50 holdout consistently worst. **temp09 holdout shows d1v2 AUC reversal** (GPT-2 XL 0.13, OLMo 0.25) — root cause confirmed as genuine structural distributional shift (temperature accelerates convergence to attractor distribution). Z-score normalization improves overall LR acc (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), confirming a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation could recover d1v2 AUC remains open. Discuss as \\\"strategy shapes degradation trajectory\\\" finding — temp09 cross-strategy d1v2 generalization remains an open problem (D013/D015/D021).\\n4. \\\"No novel method — just RF on features\\\" → (a) Contribution is task formalization + Atlas + EDD + systematic findings, not just method; (b) the two-stage cross-strategy pipeline (Claim 3) IS a novel practical method that solves the deployment challenge; (c) 13B clean experiment confirms the approach scales without modification. Analogous to benchmark papers (HELM, MMLU). Feature universality across 9+ settings is itself a finding.\\n5. \\\"d0 confound inflates headline metrics\\\" → Report d1-only accuracy alongside full accuracy; 3-class (d1/d2/d3) results already show 59–82% accuracy\\n6. \\\"EDD threshold is arbitrary\\\" → Sensitivity analysis at 0.65/0.70/0.75/0.80 completed (Dream D002)\\n7. \\\"No figures for Atlas\\\" → Minimum 4 figures (Dream D002)\\n8. \\\"Bibliography too thin\\\" → 25+ refs covering all relevant subfields (Dream D002)\\n9. \\\"Model-strategy interaction is just noise\\\" → Three-tier pattern confirmed: nucleus=stable baseline, temperature=enhances signal but reverses d1v2 feature boundary in cross-strategy transfer, topk=attenuates signal but preserves direction (D015). Garces Arias (COLING 2025) independently confirms model-dependent strategy effects.\\n10. \\\"Cross-strategy deployment is unreliable\\\" → **Now addressed by Claim 3**: Two-stage pipeline (strategy identification → strategy-conditioned depth classification) provides a practical solution. Strategy classifier expected >90% accuracy on 19 features (strategy distributions are highly separable). After strategy identification, depth classification uses strategy-matched RF, restoring near within-strategy accuracy. The root cause (temperature's accelerated convergence) is identified and the mechanism explained — this is no longer an open problem but a solved deployment challenge.\\n11. \\\"Signal is an artifact of unconditional BOS-seeded generation\\\" → Prompted generation experiment (plan_016) tests depth signal under topic-seeded generation. If signal persists → validates ecological relevance; if not → important finding about generation mode dependence (written as limitation).\\n12. \\\"Only tested on small models (1–1.5B)\\\" → Clean 13B FP16 experiment (Qwen2.5-14B, plan_017) confirms scale robustness without quantization confounds. Prior 7B QLoRA results were contradictory — now superseded by clean experiment.\\n\", \"total_chars\": 15939, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbd1ebf1-ffcb-4984-8bb1-fce2061e5d2e",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "b6ec62a4-b49e-41f9-82d1-c7a5c1ac9484",
  "sourceToolAssistantUUID": "bbd1ebf1-ffcb-4984-8bb1-fce2061e5d2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T09:00:57.269Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QdN4Rxqof1HJvSMq1qrmmd`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6ec62a4-b49e-41f9-82d1-c7a5c1ac9484",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sJsTALMwzFDYzVmxGm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47541347-a82f-4d1e-befa-28171d06bae1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WV6CjGvqHQfEpY82GQrp2Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10601,
      "cache_read_input_tokens": 18026,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10601
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 18026,
          "cache_creation_input_tokens": 10601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10601,
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

_source line 12 · 2026-05-17T09:00:57.278Z_

<details><summary>↩ Tool result · `toolu_01QdN4Rxqof1HJvSMq1qrmmd`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'recursive_gen_depth_est'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47541347-a82f-4d1e-befa-28171d06bae1",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "cf9ef016-b57d-4b1b-aa2b-21d5587234ee",
  "sourceToolAssistantUUID": "47541347-a82f-4d1e-befa-28171d06bae1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T09:01:02.251Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01AAK2yRBTj6aBqoEB1CdkSK`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf9ef016-b57d-4b1b-aa2b-21d5587234ee",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sKFmbKEwTbMUmP5ZDW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb18c880-00f7-4dd8-ac70-b69a69807722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qp88k57EJY4fdKWVUsSyf1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5531,
      "cache_read_input_tokens": 28627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5531,
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

_source line 14 · 2026-05-17T09:01:02.277Z_

<details><summary>↩ Tool result · `toolu_01AAK2yRBTj6aBqoEB1CdkSK`</summary>

```text
artifacts/dream_reports/dream_20260514T140607/best/paper.tex
artifacts/dream_reports/dream_20260514T140607/median/paper.tex
artifacts/dream_reports/dream_20260514T140607/worst/paper.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/atlas.tex
docs/paper/abstract.tex
docs/paper/method.tex
docs/paper/conclusion.tex
docs/paper/section_appendix.tex
docs/paper/discussion.tex
docs/paper/generalization.tex
artifacts/dream_reports/dream_20260517T075852/best/paper.tex
artifacts/dream_reports/dream_20260517T075852/median/paper.tex
artifacts/dream_reports/dream_20260517T075852/worst/paper.tex
docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb18c880-00f7-4dd8-ac70-b69a69807722",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "b9069c3b-a2c1-425e-b893-2f8db09e1792",
  "sourceToolAssistantUUID": "cb18c880-00f7-4dd8-ac70-b69a69807722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T09:01:03.993Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01L6KTCiS1Fr33eDfeTrvXUu`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9069c3b-a2c1-425e-b893-2f8db09e1792",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sKFmbKEwTbMUmP5ZDW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a655c003-0e16-421b-bd68-6f97ba388a9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qp88k57EJY4fdKWVUsSyf1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5531,
      "cache_read_input_tokens": 28627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5531,
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

_source line 16 · 2026-05-17T09:01:04.017Z_

<details><summary>↩ Tool result · `toolu_01L6KTCiS1Fr33eDfeTrvXUu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/ROADMAP.md\", \"content\": \"# recursive_gen_depth_est — Research Dashboard\\n\\n> 最后更新: 2026-05-17 06:08 UTC | 更新原因: D035 all experiments done, paper patch complete, submitted for final review R8\\n\\n## 核心方向\\n递归生成深度估计：给定文本，预测其经历了多少轮 model→data→model 递归训练循环。\\n**Primary contribution**: Depth Degradation Atlas + EDD metric + feature consistency findings。\\n详见 paper_framing.md（Plan A, D011）。\\n\\n## 当前进展\\n- **阶段**: **论文 Final Review**（D035 patch 完成，提交审稿中）\\n- **目标**: EMNLP 2026 Findings track, ARR May cycle (DDL May 25)\\n- **论文状态**: 19 页（8 页正文），编译干净，D035 全部 6 个实验结果已写入\\n- **实验**: 87 total (53 success, 7 negative, 10 failed, 17 killed)\\n\\n## D035 实验结果总结\\n| 实验 | 结论 | 论文位置 |\\n|------|------|----------|\\n| Second-seed replication | ✅ 77.15%, Δ=-1.05pp | Limitations + Appendix |\\n| Cross-seed transfer | ✅ 76.76%, Δ=-1.30pp | Appendix |\\n| Mixed-depth corpus | ⚠️ macro ok, d1 超标 | Appendix |\\n| Gen-length ablation | ❌ spread 9.47pp (but informative) | Appendix |\\n| Reference-free baseline | ❌ 53.68% < 60% | Limitations 1-2 句 |\\n| Ensemble reference | ❌ 73.65% < best | Limitations 1-2 句 |\\n\\n## 投稿准备\\n- [x] D035 实验全部完成\\n- [x] Paper Agent patch 写入\\n- [ ] **最终审稿 R8**（已提交，等审批）\\n- [ ] 审稿修改（如有）\\n- [ ] ARR 投稿提交\\n\\n## GPU 预算\\n- 本项目分配: gpu-6000pro-2 cuda:0, cuda:1 (2× RTX 6000 Pro)\\n- 已消耗: ~52 GPU·h\\n- 当前: **空闲**（所有实验完成）\\n\\n## 教训\\n- DCOL: DeBERTa disentangled attention 与 contrastive loss 数值不兼容\\n- kill 实验时必须验证进程确实死亡\\n- EDD 报告必须附 bootstrap CI + p-value (D027)\\n- 审稿团队可能用旧版本——提交前确认 PDF 是最新编译版\\n- instruction-tuning 归因需实验验证因果方向（BASE U-shape vs Instruct monotonic）\\n- Z-score 对 tree-based 方法（RF）无理论效果——实验前应验证假设的理论基础\\n- 简单 mean ensemble 稀释强信号——reference model 选择比 ensemble 更重要\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D035 | 2026-05-17 | D034 修正：投稿前补 3 个高 ROI 实验（second-seed / mixed-corpu | — |\\n| D034 | 2026-05-16 | 目标调整为 EMNLP Findings；Tables 加 CI 完成；论文 ready for A | lora_rank_ablation_001, gpt2xl_ref_ablation_001 |\\n| D033 | 2026-05-16 | R5 审稿 Action Matrix：冲 Main Conference，补 LoRA rank  | baseline_battery_001, cross_scale_llama3_base_001 |\\n| D032 | 2026-05-16 | Llama BASE 推翻 instruction-tuning 归因：BASE 非单调 / Ins | cross_scale_llama3_base_001, cross_scale_llama3_8b_003 |\\n| D031 | 2026-05-16 | 反向链实验确认 depth signal 与模型链顺序无关，N4 architecture-dept | cross_model_reverse_chain_001, cross_model_recursive_chain_002 |\\n| D030 | 2026-05-16 | R4 审稿回应策略：全面降级 overclaiming + 补 Llama-3.1-8B base  | cross_scale_llama3_8b_003, cross_scale_qwen7b_001 |\\n| D029 | 2026-05-15 | 域偏差叙事调整：从\\\"无偏差\\\"改为\\\"depth dominates, residual exists\\\" | w2_domain_bias_001 |\\n| D028 | 2026-05-15 | Cross-strategy normalization claim 从 \\\"不可修复的结构性偏移\\\"  | lr_zscore_cross_strategy_001, cross_strategy_loo_001 |\\n| D027 | 2026-05-15 | EDD=4 三模型一致性声明降级：Pythia 显著 (p=0.001)，OLMo 边际 (p=0. | depth_extension_binary_pairwise_002, depth_extension_gpt2xl_d4d5_001, depth_extension_olmo_d4d5_002 |\\n| D026 | 2026-05-15 | 修正 EDD=4 三模型声明：从\\\"均 EDD=4\\\"转向\\\"一致的 depth-4 衰减边界，统计强度分 | depth_extension_binary_pairwise_002, depth_extension_gpt2xl_d4d5_001, depth_extension_olmo_d4d5_002 |\\n\\n\\n\", \"total_chars\": 2975, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a655c003-0e16-421b-bd68-6f97ba388a9e",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "efe25fcc-e840-4fbf-84e8-ff01210a7944",
  "sourceToolAssistantUUID": "a655c003-0e16-421b-bd68-6f97ba388a9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T09:01:07.653Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TvCWmWMANyMAbdDwbNtWBg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efe25fcc-e840-4fbf-84e8-ff01210a7944",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sKmS3UcvW6EKqqWKz1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab830fff-1011-42ad-92f0-3eb1b70721cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017w9CauQkKqFSt9smbC3R4a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2248,
      "cache_read_input_tokens": 34158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2248,
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

_source line 18 · 2026-05-17T09:01:07.660Z_

<details><summary>↩ Tool result · `toolu_01TvCWmWMANyMAbdDwbNtWBg`</summary>

```text
1	\begin{abstract}
2	As large language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises, yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.
4	A Random Forest over 19 perplexity-based features achieves 70--85\% four-class accuracy (chance = 25\%), with perplexity tail statistics emerging as consistent depth markers; a parsimonious subset of 5 features retains 97.6\% of full performance.
5	We define the \emph{Effective Discriminable Depth} (EDD) metric, finding $\mathrm{EDD}_{0.75}{=}4$ for the best-characterized family, and show that cross-model transfer reaches 66.4\% (2.7$\times$ chance).
6	Systematic generalization across seven axes (including cross-scale with 7B models at 70.2\%, cross-domain, and LoRA-rank ablation) confirms that depth signal is robust and resides in distributional statistics inaccessible from surface text (zero-shot LLMs: 30--36\%, 42\,pp below RF).
7	\end{abstract}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab830fff-1011-42ad-92f0-3eb1b70721cb",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "40705724-7a1a-4c6b-bb7d-357e55dd5276",
  "sourceToolAssistantUUID": "ab830fff-1011-42ad-92f0-3eb1b70721cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T09:01:08.060Z_

<details open><summary>🔧 Tool call — Read · `toolu_015nUqNumTMF9YannFehTTGZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40705724-7a1a-4c6b-bb7d-357e55dd5276",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sKmS3UcvW6EKqqWKz1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c34e4749-7893-4765-bd2d-862abd58be2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017w9CauQkKqFSt9smbC3R4a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2248,
      "cache_read_input_tokens": 34158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2248,
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

_source line 20 · 2026-05-17T09:01:08.067Z_

<details><summary>↩ Tool result · `toolu_015nUqNumTMF9YannFehTTGZ`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	
8	Existing tools address adjacent but distinct problems.
9	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
10	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.
13	
14	We find that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are \textbf{consistent in direction but scale-dependent in magnitude} across the three model families and three decoding strategies studied.
15	Specifically, perplexity tail statistics (the 90th-percentile perplexity, \textsc{p90\_ppl}, and surprisal variance, \textsc{var\_surprisal}) emerge as dominant depth indicators, ranking in the top two features by importance in 9/9 and 8/9 model--strategy configurations, respectively.
16	Instruction-tuned variants exhibit monotonically decreasing AUC (regularization), whereas base models can show non-monotonic trajectories, suggesting that instruction tuning acts as a regularizer on the depth signal rather than introducing degradation.
17	
18	We formalize recursive generation depth estimation as ordinal classification and introduce a lightweight pipeline: compute 19 reference-model perplexity features (effective dimensionality ${\approx}$4--5 due to multicollinearity; \S\ref{sec:atlas:features}) and classify with a Random Forest into $K{+}1$ depth classes.
19	To characterize how recursive generation reshapes these features, we construct the \emph{Depth Degradation Atlas}: a $3 \times 3$ grid of model families $\times$ decoding strategies spanning 4 depths (180K samples).
20	The atlas reveals strategy-dependent degradation trajectories and we introduce the \emph{Effective Discriminable Depth} (EDD) metric to quantify how far into the recursion chain adjacent depths remain distinguishable.
21	
22	Our contributions are:
23	\begin{itemize}
24	    \item \textbf{Task formalization and benchmark.} We define recursive generation depth estimation as ordinal classification, introduce the EDD metric, and construct a 180K-sample benchmark spanning 3 model families $\times$ 3 decoding strategies $\times$ 4 depths.
25	
26	    \item \textbf{Depth Degradation Atlas.} A systematic $3 \times 3$ characterization reveals that perplexity tail statistics dominate depth discrimination (top-2 in 9/9 and 8/9 cells), decoding strategy reshapes degradation trajectories qualitatively, and $\mathrm{EDD}_{0.75}{=}4$ for the best-characterized family (Pythia, $p{=}0.001$; consistent across all three families).
27	
28	    \item \textbf{Generalization across seven axes.} Cross-model recursive chains (84.75\%), cross-scale observations on two 7B models (70.2\% and 60.1\%), cross-domain transfer (arXiv 74.1\%), temperature robustness ($\tau \in [0.5, 0.9]$), and reference model robustness (67--79\% accuracy across three reference models). A surface-text ablation (zero-shot LLMs at 30--36\%, 42\,pp below RF) confirms the signal resides in distributional statistics, while requiring only 19 features and a Random Forest for GPU-free inference.
29	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c34e4749-7893-4765-bd2d-862abd58be2a",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "f31b1f04-9e46-4db9-870b-08c32f27552e",
  "sourceToolAssistantUUID": "c34e4749-7893-4765-bd2d-862abd58be2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T09:01:11.486Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RvmAT7yGZtWi4gP1WURpLt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f31b1f04-9e46-4db9-870b-08c32f27552e",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sL41C9LDSyfpU4WnQJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d198262-54f5-461c-8f18-17cd6dd931ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ggMm8yphAVQ4HA9Q6RLSC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1754,
      "cache_read_input_tokens": 36406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1754,
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

_source line 22 · 2026-05-17T09:01:11.492Z_

<details><summary>↩ Tool result · `toolu_01RvmAT7yGZtWi4gP1WURpLt`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails; \citet{dohmatob2024_tale_of_tails} formalize this via scaling laws \cite{seddik2024synthetic}, \citet{dohmatob2025_strong_collapse} establish strong collapse guarantees, and the MAD framework \cite{alemohammad2024_mad} extends the analysis to self-consuming models.
6	Subsequent work addresses mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026}.
7	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple distinct phenomena, underscoring the need for operationally precise metrics.
8	Dohmatob et al.\ predict that recursive training erodes distributional tails as a theoretical scaling law \citep{dohmatob2024_tale_of_tails}; we operationalize this prediction into a deployable ordinal classifier, revealing strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.
9	All assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
10	
11	\paragraph{AI Text Detection.}
12	The detection literature \cite{wu2025_detection_survey} spans statistical methods (DetectGPT \cite{mitchell2023_detectgpt}, Fast-DetectGPT \cite{fast_detectgpt2024}, Binoculars \cite{binoculars2024}, DivEye \cite{diveye2026}, GLTR \cite{gehrmann2019_gltr}, Ghostbuster \cite{verma2024_ghostbuster}, DNA-GPT \cite{yang2024_dnagpt}) and watermarking \cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \cite{sadasivan2023_paraphrase}, distribution shift \cite{pudasaini2026_detection_fails}, and generator barriers \cite{pu2026_generator_barrier}.
13	M4-SemEval \cite{wang2024_m4_semeval} benchmarks multilingual detection.
14	All these methods perform binary classification, discarding ordinal depth information; our approach outputs ordinal depth labels, complementing rather than replacing binary detection.
15	
16	\paragraph{Adjacent Tasks.}
17	EditLens \cite{editlens2026} estimates editing extent but does not model recursive chains; \citet{uchendu2020_attribution} classify \emph{which} model generated text; LOKI \cite{loki2025} benchmarks synthetic data detection across modalities.
18	\citet{mohamed2025_broken_telephone} study iterative generation as a ``broken telephone'' effect, characterizing \emph{how} text degrades without classifying which iteration a passage comes from.
19	Our task performs the inverse, ordinal depth estimation from text alone, discriminating between adjacent depths rather than merely detecting aggregate degradation.
20	
21	\paragraph{Ordinal Classification.}
22	Ordinal classification has a long history \cite{mccullagh1980_ordinal}: \citet{frank2001} reduce ordinal problems to nested binary tasks, and \citet{rennie2005} introduce loss functions tailored to discrete ordered labels.
23	CORAL \cite{coral2020} enforces rank consistency via ordered binary tasks; CLOC \cite{cloc2025} extends contrastive learning with multi-margin ordinal losses.
24	We adopt both as baselines (\S\ref{sec:generalization}) to confirm the signal is accessible to principled ordinal methods.
25	
26	\paragraph{Decoding Strategy Effects.}
27	Decoding strategies shape text statistics in ways that interact with depth signals \cite{holtzman2020_nucleus,finlayson2024_closing,garces_arias2025_decoding_decoded,wiher2022_decoding,basu2021_mirostat}.
28	Our Depth Degradation Atlas (\S\ref{sec:atlas}) reveals that these strategies induce qualitatively different degradation trajectories under recursive generation: temperature sampling accelerates convergence to a low-entropy attractor while top-$k$ attenuates the depth signal, effects beyond single-pass text quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d198262-54f5-461c-8f18-17cd6dd931ab",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "64a93cc0-7e5b-455e-965a-54a7fea080df",
  "sourceToolAssistantUUID": "1d198262-54f5-461c-8f18-17cd6dd931ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T09:01:11.816Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TfiiNNpGTe8BepDQ6c9N46`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64a93cc0-7e5b-455e-965a-54a7fea080df",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sL41C9LDSyfpU4WnQJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1b03e69-2f69-4a17-9c88-83da771b3bd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ggMm8yphAVQ4HA9Q6RLSC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1754,
      "cache_read_input_tokens": 36406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1754,
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

_source line 24 · 2026-05-17T09:01:11.827Z_

<details><summary>↩ Tool result · `toolu_01TfiiNNpGTe8BepDQ6c9N46`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark covers depths d0--d3 across all $3 \times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K samples total).
30	For depth extension experiments (\S\ref{sec:atlas}), we extend one pipeline (Pythia-1.4B, nucleus) to d0--d5.
31	
32	\paragraph{Generation pipeline.}
33	Starting from a Wikipedia subset as seed text ($\mathcal{D}_0$), each generation cycle proceeds in three steps: (1)~LoRA finetuning \cite{hu2022lora} on $\mathcal{D}_{k-1}$, freezing base model weights and training low-rank update matrices ($<$1\% additional parameters; $r{=}16$, $\alpha{=}32$, lr $2{\times}10^{-4}$, batch size 8, 3 epochs, dropout $0.05$, architecture-specific targets); (2)~sampling 5{,}000 passages from the LoRA-finetuned model (max 512 tokens, BOS-seeded, no prompt conditioning) under the specified decoding strategy; (3)~the generated corpus becomes $\mathcal{D}_k$ for the next cycle.
34	Each depth is produced by a model explicitly trained on the prior depth's data, not by sampling from the unmodified base model.
35	Our BOS-seeded generation may amplify depth signal relative to prompted settings; extending to prompt-conditioned generation is future work.
36	There is no per-passage lineage across depths, ensuring cross-validation splits do not introduce information leakage.
37	
38	\paragraph{Reference model.}
39	All statistical features (\S\ref{sec:method:features}) are computed using Pythia-1.4B as fixed reference model, the smallest generator whose training corpus partially overlaps with the others.
40	For Pythia this constitutes self-model measurement, yet its accuracy (78.2\%) does not exceed GPT-2~XL (85.4\%), indicating no systematic self-model advantage.
41	Ablations with OLMo-1B and GPT-2 XL as alternative references yield 67--79\% accuracy (Appendix~\ref{app:ref_ablation}), confirming reference model robustness; further discussion in Limitations.
42	
43	\subsection{Statistical Feature Design}
44	\label{sec:method:features}
45	
46	We extract a feature vector $\mathbf{f}(x)$ comprising 19 candidate features from the reference-model perplexity distribution over each passage $x$; ablation (\S\ref{sec:atlas:features}) shows the top 5 achieve 97.6\% of full-set performance, and variance inflation analysis reveals VIF${>}$10 for 14--16 features, placing the effective independent dimensionality at ${\approx}$4--5.
47	The features fall into four categories (Table~\ref{tab:features}).
48	
49	\begin{table}[t]
50	\centering
51	\small
52	\caption{The 19 statistical features comprising $\mathbf{f}(x)$, grouped by category. All perplexity and surprisal features are computed from the reference model (Pythia-1.4B).}
53	\label{tab:features}
54	\begin{tabular}{@{}llr@{}}
55	\toprule
56	Category & Features & $n$ \\
57	\midrule
58	Perplexity & mean, var, skewness, kurtosis, & 9 \\
59	statistics & p10, p25, p50, p75, p90 & \\
60	\addlinespace
61	Surprisal & mean, var, entropy & 3 \\
62	statistics & & \\
63	\addlinespace
64	Lexical & type--token ratio, hapax ratio, & 4 \\
65	diversity & bigram entropy, trigram entropy & \\
66	\addlinespace
67	Repetition & repeated 2/3/4-gram fractions & 3 \\
68	\bottomrule
69	\end{tabular}
70	\end{table}
71	
72	\emph{Perplexity statistics} (9 features) capture the per-token perplexity distribution via moments (mean, variance, skewness, kurtosis) and quantiles (p10--p90); tail quantiles prove especially informative as recursive finetuning erodes the high-perplexity tail (\S\ref{sec:atlas}).
73	\emph{Surprisal statistics} (3 features): mean, variance, and entropy of $-\log p(\text{token})$; surprisal variance captures second-order structure not redundant with perplexity moments.
74	\emph{Lexical diversity} (4 features): type--token ratio, hapax ratio, bigram/trigram entropy.
75	\emph{Repetition} (3 features): repeated $n$-gram fractions for $n \in \{2, 3, 4\}$.
76	
77	\subsection{Effective Discriminable Depth}
78	\label{sec:method:edd}
79	
80	Aggregate multi-class accuracy obscures whether discriminability degrades at specific depth boundaries.
81	We introduce the \emph{Effective Discriminable Depth} (EDD) to formalize the frontier beyond which adjacent depths become statistically indistinguishable.
82	
83	\paragraph{Pairwise discriminability.}
84	Let $\mathcal{D} = \{0, 1, \dots, K\}$ denote the depth set and $T \in (0.5, 1.0]$ a discrimination threshold.
85	For each adjacent pair $(d, d{+}1)$, we define the pairwise discriminability $\mathrm{AUC}(d, d{+}1)$ as the area under the ROC curve of a dedicated binary Random Forest classifier (500 trees, $\lfloor\sqrt{19}\rfloor$ candidate features per split) trained on class-balanced data from $\mathbf{f}(x)$ (\S\ref{sec:method:features}) to distinguish depth-$d$ from depth-$(d{+}1)$ samples, evaluated via 5-fold stratified cross-validation.
86	Each pair uses an independent classifier, avoiding the decision boundary dilution that arises in multi-class settings (\S\ref{sec:atlas:edd}).
87	
88	\begin{definition}[Effective Discriminable Depth]
89	\label{def:edd}
90	The \emph{Effective Discriminable Depth} at threshold $T$ is:
91	\begin{equation}
92	\mathrm{EDD}_T = \max \bigl\{ d^*{+}1 \,:\, \forall\, d' \leq d^*,\; \mathrm{AUC}(d', d'{+}1) \geq T \bigr\}
93	\label{eq:edd}
94	\end{equation}
95	where $d^* \in \{0, \dots, K{-}1\}$. If\, $\mathrm{AUC}(0,1) < T$, then $\mathrm{EDD}_T = 0$.
96	\end{definition}
97	
98	$\mathrm{EDD}_T$ is the deepest depth $d$ such that every adjacent pair from $(0,1)$ through $(d{-}1, d)$ remains discriminable at level $T$.
99	The universal quantifier ensures EDD reports the longest \emph{contiguous} discriminable prefix rather than an isolated high-AUC pair at greater depth.\footnote{Our AUC profiles are empirically monotonically decreasing for the 1--1.5B base models (\S\ref{sec:atlas}), so in practice $\mathrm{EDD}_T = \max\{d'{+}1 : \mathrm{AUC}(d', d'{+}1) \geq T\}$. Qwen2.5-7B exhibits a U-shaped AUC pattern rather than monotonic decay; a base-model control shows non-monotonic decay persists without instruction tuning (\S\ref{sec:gen:crossscale}). For non-monotonic profiles, the contiguous formulation is more conservative (see Limitations).}
100	We set $T{=}0.75$ as default; sensitivity at $T \in \{0.65, 0.70, 0.75, 0.80\}$ is reported in \S\ref{sec:atlas}.
101	
102	\paragraph{Classifiers.}
103	Our primary classifier is a Random Forest (200 trees, unconstrained depth, 5-fold stratified cross-validation).
104	We compare against CORAL ordinal regression \cite{coral2020}, DivEye \cite{diveye2026}, a 2-layer cross-entropy MLP, logistic regression, and a single-feature baseline using mean perplexity alone; results appear in \S\ref{sec:generalization}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1b03e69-2f69-4a17-9c88-83da771b3bd9",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "b3df6e63-6b34-417d-a915-db4e6ce28588",
  "sourceToolAssistantUUID": "a1b03e69-2f69-4a17-9c88-83da771b3bd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T09:01:16.839Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Jq5Pu7br68SyVrSuCRaK2E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3df6e63-6b34-417d-a915-db4e6ce28588",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sLLKxjcku7NomPdmK1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c35698a-5037-4813-bffb-f6132a301f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015LdNEE1XNCgza84V7YXjvQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4352,
      "cache_read_input_tokens": 38160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4352,
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

_source line 26 · 2026-05-17T09:01:16.846Z_

<details><summary>↩ Tool result · `toolu_01Jq5Pu7br68SyVrSuCRaK2E`</summary>

```text
1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 69.6\% (Pythia, top-$k$) to 85.4\% (GPT-2~XL, temperature), all exceeding the 25\% chance baseline by a wide margin.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (76.6--85.4\%), followed by OLMo (74.2--82.0\%) and Pythia (69.6--78.2\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 8.4~pp, comparable to the 7.1~pp mean within-strategy model gap; decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) across the $3 \times 3$ atlas, with d1--d3 three-class accuracy in parentheses (chance = 25\% / 33\%). Depth-0 recall exceeds 98\% in all cells.}
22	\label{tab:main_matrix}
23	\begin{tabular}{@{}lccc@{}}
24	\toprule
25	& Nucleus & Temp.\ $\tau{=}0.9$ & Top-$k$ \\
26	\midrule
27	Pythia-1.4B  & 78.2\,(71.2) & 76.3\,(70.6) & 69.6\,(58.8) \\
28	OLMo-1B     & 78.8\,(75.0) & 82.0\,(76.3) & 74.2\,(66.1) \\
29	GPT-2~XL    & 83.3\,(79.0) & 85.4\,(82.6) & 76.6\,(69.5) \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
34	\paragraph{Per-class recall distribution.}
35	Depth-0 recall exceeds 98\% in all 9 cells, confirming that human-written text is trivially separable from any generation depth.
36	Among generated depths, d2 consistently yields the lowest recall (46--73\% across cells), followed by d3 (58--82\%) and d1 (72--91\%).
37	For example, Pythia-1.4B nucleus achieves per-class recall of d0$\,{=}\,$99\%, d1$\,{=}\,$82\%, d2$\,{=}\,$59\%, d3$\,{=}\,$72\%.
38	The strongest d2 recall is obtained by GPT-2~XL nucleus (73\%).
39	The d2 trough reflects its position at the center of the depth gradient: d2 features overlap with both the d1 distribution above and d3 below, making it the most confusable class, consistent with the d2-vs-d3 pair being the EDD bottleneck (\S\ref{sec:atlas:edd}).
40	Full per-class recall for all cells appears in Appendix~\ref{app:per_class}.
41	
42	%% ----------------------------------------------------------------
43	\subsection{Feature Consistency Across the Grid}
44	\label{sec:atlas:features}
45	
46	Despite the 15.8~pp accuracy spread across cells, a small feature family dominates in every setting.
47	Perplexity tail statistics as a feature group dominate depth discrimination: the 90th-percentile perplexity (\texttt{p90\_ppl}) ranks top-2 by Gini importance in all 9 cells; surprisal variance (\texttt{var\_surprisal}) in 8/9 under SHAP (7/9 under Gini; Appendix~\ref{app:permutation}).\footnote{Individual feature rankings should be interpreted cautiously given high multicollinearity (VIF${>}$10 for 14--16/19 features); the group-level dominance of perplexity tail statistics is robust across importance measures.}
48	Table~\ref{tab:feature_importance} shows the full per-cell ranking.
49	
50	Cross-model feature-rank Spearman correlation averages $\bar{\rho} = 0.868$ (range $[0.619, 0.954]$): models agree on which features carry depth information even when they differ in absolute accuracy.
51	Among strategies, top-$k$ yields the highest cross-model rank correlation ($\rho = 0.811$): the deterministic vocabulary truncation imposes a more uniform feature landscape across architectures, at the cost of weaker overall signal (\S\ref{sec:atlas:strategy}).
52	
53	Percentile-based features outperform their moment-based counterparts.
54	Token-level perplexity distributions are heavy-tailed: individual outlier passages can dominate the arithmetic mean of their depth class, whereas \texttt{p90\_ppl} is robust to such extremes while still capturing the tail erosion that signals generation depth.
55	
56	Feature ablation confirms this concentration: the top-2 features (\texttt{p90\_ppl} + \texttt{var\_surprisal}) alone reach 91.1\% of full accuracy (71.5\%), and the top-5 features achieve 97.6\% (76.5\% vs.\ 78.4\%), with perplexity statistics alone reaching 76.6\% (vs.\ surprisal 73.2\%, other categories ${\leq}$47\%).
57	Variance inflation analysis reveals VIF${>}$10 for 14--16 of 19 features, placing the effective independent dimensionality at ${\approx}$4--5.
58	Forward selection independently confirms the dominant pair: \texttt{p90\_ppl} is selected first in 6/9 cells, \texttt{var\_surprisal} in 3/9.
59	
60	The feature hierarchy also shifts with depth.
61	At shallow boundaries (d1 vs.\ d2), \texttt{var\_surprisal} dominates importance; at deeper boundaries (d3 vs.\ d4, d4 vs.\ d5), tail perplexity statistics (\texttt{p90\_ppl}, \texttt{kurtosis\_ppl}) take over.
62	This transition aligns with model-collapse dynamics~\cite{shumailov2024_nature}: early recursion narrows the surprisal distribution (captured by its variance), while later steps erode the perplexity tail (captured by upper quantiles and kurtosis).
63	
64	\begin{table}[t]
65	\centering
66	\small
67	\caption{Top-5 features by Gini importance. \textbf{Bold}: top-2. \texttt{p90\_ppl} top-2 in 9/9; \texttt{var\_surprisal} 8/9 under SHAP (7/9 under Gini).}
68	\label{tab:feature_importance}
69	\resizebox{\columnwidth}{!}{%
70	\begin{tabular}{@{}l l@{}}
71	\toprule
72	Cell & Top-5 features (Gini importance, ranked) \\
73	\midrule
74	Pythia, nuc.       & \textbf{var\_surp\,(.17)}, \textbf{p90\_ppl\,(.15)}, m\_ppl\,(.11), var\_ppl\,(.08), p75\,(.07) \\
75	Pythia, $\tau$     & \textbf{var\_surp\,(.17)}, \textbf{p90\_ppl\,(.14)}, m\_ppl\,(.11), p75\,(.07), m\_surp\,(.07) \\
76	Pythia, top-$k$    & \textbf{var\_surp\,(.16)}, \textbf{p90\_ppl\,(.12)}, m\_ppl\,(.11), var\_ppl\,(.07), m\_surp\,(.06) \\
77	GPT-2\,XL, nuc.    & \textbf{var\_surp\,(.21)}, \textbf{p90\_ppl\,(.21)}, p75\,(.10), m\_surp\,(.07), m\_ppl\,(.06) \\
78	GPT-2\,XL, $\tau$  & \textbf{p90\_ppl\,(.25)}, \textbf{p75\,(.15)}, m\_surp\,(.13), var\_surp\,(.12), p50\,(.05) \\
79	GPT-2\,XL, top-$k$ & \textbf{p90\_ppl\,(.24)}, \textbf{p75\,(.12)}, var\_surp\,(.10), m\_surp\,(.09), ttr\,(.04) \\
80	OLMo, nuc.         & \textbf{p90\_ppl\,(.18)}, \textbf{var\_surp\,(.15)}, p75\,(.11), m\_surp\,(.07), ttr\,(.06) \\
81	OLMo, $\tau$       & \textbf{p90\_ppl\,(.21)}, \textbf{var\_surp\,(.16)}, p75\,(.12), m\_surp\,(.09), ttr\,(.05) \\
82	OLMo, top-$k$      & \textbf{p90\_ppl\,(.20)}, \textbf{var\_surp\,(.17)}, p75\,(.10), m\_surp\,(.07), m\_ppl\,(.05) \\
83	\bottomrule
84	\end{tabular}}
85	\end{table}
86	
87	\begin{figure}[t]
88	\centering
89	\includegraphics[width=\columnwidth]{figures/fig_atlas_heatmap.pdf}
90	\caption{Atlas feature importance heatmap. Rows: 19 features grouped by category (\S\ref{sec:method:features}); columns: 9 model--strategy cells. Color intensity encodes RF Gini importance. The perplexity-tail and surprisal-variance blocks maintain high importance across all cells.}
91	\label{fig:atlas_heatmap}
92	\end{figure}
93	
94	%% ----------------------------------------------------------------
95	\subsection{Monotonicity and Inter-Depth Distances}
96	\label{sec:atlas:monotonicity}
97	
98	Depth features exhibit strong monotonic trends: perplexity tail statistics (\texttt{p90\_ppl}, \texttt{mean\_surprisal}) decrease with depth (Spearman $\rho = -1.0$ across cell-level medians) while repetition features increase, reflecting the complementary narrowing and self-repetition of distribution collapse.
99	Inter-depth distances are non-uniform: d0-vs-d1 AUC exceeds 0.99 in all 9 cells, whereas d2-vs-d3 ranges from 0.69 to 0.89; separating adjacent deep generations requires the tail statistics identified in \S\ref{sec:atlas:features}.
100	
101	\begin{figure}[t]
102	\centering
103	\includegraphics[width=\columnwidth]{figures/fig_feature_trajectory.pdf}
104	\caption{Feature trajectories across depths $d{=}0$ to $d{=}3$, stratified by model (columns) and strategy (line style). Top row: \texttt{p90\_ppl} (monotonically decreasing). Middle: \texttt{var\_surprisal} (decreasing). Bottom: \texttt{rep\_3gram} (increasing). Shaded bands: interquartile range. The $d{=}0 \to d{=}1$ gap exceeds all subsequent inter-depth gaps.}
105	\label{fig:feature_trajectory}
106	\end{figure}
107	
108	%% ----------------------------------------------------------------
109	\subsection{EDD Analysis}
110	\label{sec:atlas:edd}
111	
112	We extend the benchmark to depth $d{=}5$ for all three models under nucleus sampling.
113	Each model's depth-3 LoRA checkpoint is used to finetune and generate depth-4 data, and the process repeats for depth~5; feature extraction uses the same reference model (Pythia-1.4B).
114	We train dedicated binary RF classifiers (500 trees) for each adjacent pair, as defined in Eq.~\ref{eq:edd}.
115	
116	\paragraph{AUC decay profile.}
117	Figure~\ref{fig:auc_decay} plots the binary pairwise AUC decay curves.
118	For Pythia-1.4B (nucleus), AUC decays monotonically: d0-vs-d1 $= 0.999$, d1-vs-d2 $= 0.925$, d2-vs-d3 $= 0.823$, d3-vs-d4 $= 0.784$, d4-vs-d5 $= 0.683$.
119	The steepest drop occurs between the d1-vs-d2 and d2-vs-d3 pairs; the curve then flattens as the system approaches an indistinguishable regime gradually rather than crossing a sharp boundary.
120	
121	\paragraph{Cross-model convergence at depth 4--5.}
122	The d3-vs-d4 AUC consistently clusters near the $T{=}0.75$ threshold across all three models (Pythia $0.784$, OLMo $0.765$, GPT-2~XL $0.750$), while d4-vs-d5 uniformly falls below $0.70$ ($0.681$--$0.684$).
123	The directional pattern is consistent, but statistical strength is stratified: bootstrap testing ($10{,}000$ resamples, $H_0{:}\, \mathrm{AUC} \leq 0.75$) yields $p = 0.001$ for Pythia (significant), $p = 0.091$ for OLMo (marginal), and $p = 0.505$ for GPT-2~XL (non-significant).
124	All three models cross the $T{=}0.75$ threshold within the d3--d4 region, establishing a consistent depth-4 decay boundary with graded confidence rather than uniform statistical significance.
125	The d4-vs-d5 saturation is unambiguous across models, supporting the interpretation of d3--d4 as a \emph{transition zone} from discriminable to indistinguishable regime.
126	
127	\paragraph{EDD threshold sensitivity.}
128	Table~\ref{tab:edd_sensitivity} reports $\mathrm{EDD}_T$ across the primary 9-cell benchmark (depths 0--3) at four threshold values.
129	At $T{=}0.65$, all 9 cells achieve $\mathrm{EDD} = 3$; at $T{=}0.75$, 7 of 9 cells maintain $\mathrm{EDD} \geq 3$; at $T{=}0.80$, the count drops to 5 of 9.
130	The cells losing $\mathrm{EDD}{=}3$ first are consistently the top-$k$ configurations (Pythia top-$k$ at $T{=}0.70$, then OLMo top-$k$ at $T{=}0.75$), where the d2-vs-d3 pair is the consistent bottleneck across all 9 cells.
131	
132	\begin{table}[t]
133	\centering
134	\small
135	\caption{Number of atlas cells achieving $\mathrm{EDD} \geq 3$ at each threshold $T$, across 9 model--strategy cells (depths 0--3). The d2-vs-d3 boundary is the bottleneck; top-$k$ cells drop first.}
136	\label{tab:edd_sensitivity}
137	\begin{tabular}{@{}lcccc@{}}
138	\toprule
139	& $T{=}0.65$ & $T{=}0.70$ & $T{=}0.75$ & $T{=}0.80$ \\
140	\midrule
141	Cells with $\mathrm{EDD} \geq 3$ & 9/9 & 8/9 & 7/9 & 5/9 \\
142	\bottomrule
143	\end{tabular}
144	\end{table}
145	
146	\begin{figure}[t]
147	\centering
148	\includegraphics[width=\columnwidth]{figures/fig_auc_decay.pdf}
149	\caption{Binary pairwise AUC decay curves for three models (nucleus sampling, depths 0--5). Horizontal dashed lines mark $T \in \{0.65, 0.70, 0.75, 0.80\}$. All three curves converge below 0.70 at d4-vs-d5, while d3-vs-d4 AUC clusters in the range 0.750--0.784. Shaded bands: bootstrap 95\% CIs.}
150	\label{fig:auc_decay}
151	\end{figure}
152	
153	\paragraph{Decision boundary dilution.}
154	\label{sec:atlas:edd:dilution}
155	EDD uses binary-pair classifiers to avoid \emph{decision boundary dilution}: in Pythia nucleus, d2\,vs.\,d3 AUC degrades from 0.804 (4-class) to 0.689 (6-class), a 14.3\% relative decline despite identical data, because shared decision boundaries dilute per-pair capacity.
156	Binary classifiers eliminate this confound, isolating true adjacent-pair discriminability.
157	
158	%% ----------------------------------------------------------------
159	\subsection{Strategy-Dependent Trajectories}
160	\label{sec:atlas:strategy}
161	
162	The three decoding strategies induce qualitatively distinct degradation trajectories.
163	Nucleus ($p{=}0.95$) produces the most consistent accuracy (78.2--83.3\%) and serves as the reference trajectory.
164	Temperature ($\tau{=}0.9$) yields the highest accuracy in 2/3 models (GPT-2~XL 85.4\%, OLMo 82.0\%) because uniform logit scaling accelerates convergence to an attractor distribution~\cite{shumailov2024_nature}, amplifying the statistical fingerprint. However, this acceleration creates a boundary reversal risk: temperature depth-$N$ features approximate nucleus/top-$k$ depth-$(N{+}1)$ features, causing cross-strategy classifiers to systematically overpredict depth (\S\ref{sec:generalization}).
165	Top-$k$ ($k{=}50$) produces the lowest accuracy (69.6--76.6\%) because hard vocabulary truncation removes depth-discriminative low-probability tokens, though feature direction is preserved (cross-model $\rho = 0.811$).
166	The strategy effect (8.4~pp range) exceeds the model effect (7.1~pp), indicating deployment-time knowledge of the decoding strategy matters at least as much as the generator model.
167	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c35698a-5037-4813-bffb-f6132a301f48",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "2afe9cbe-27c8-4119-acdc-113a2c7315d0",
  "sourceToolAssistantUUID": "0c35698a-5037-4813-bffb-f6132a301f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T09:01:17.127Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XgN7pMGjoGnuUEsNCqW5RU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2afe9cbe-27c8-4119-acdc-113a2c7315d0",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sLLKxjcku7NomPdmK1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8621b7c8-d740-4cb2-8061-2661e9db2643",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015LdNEE1XNCgza84V7YXjvQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4352,
      "cache_read_input_tokens": 38160,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4352
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 38160,
          "cache_creation_input_tokens": 4352,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4352,
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

_source line 28 · 2026-05-17T09:01:17.132Z_

<details><summary>↩ Tool result · `toolu_01XgN7pMGjoGnuUEsNCqW5RU`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	We formalized recursive generation depth estimation and showed that perplexity tail statistics achieve 70--85\% four-class accuracy ($\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\% of full performance and classifier-agnostic convergence within $\leq$0.4pp.
5	These features generalize across model families without retraining, positioning depth estimation as an early-warning signal for model collapse~\cite{shumailov2024_nature,shi2025_closer_look}; zero-shot LLMs at 30--36\% (\S\ref{sec:gen:baselines}) confirm the signal is inaccessible from surface text alone.
6	Cross-strategy transfer remains the primary bottleneck; see Limitations for detailed analysis.
7	Depth-graduated curation complements binary detection~\cite{dsir2023,qurating2024} and watermarking~\cite{kirchenbauer2023_watermark} as a provenance signal~\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\ref{app:curation_poc}) and adversarial robustness remains untested.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8621b7c8-d740-4cb2-8061-2661e9db2643",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "a5fad6ea-b9df-4eb3-8a97-c7c92200af4e",
  "sourceToolAssistantUUID": "8621b7c8-d740-4cb2-8061-2661e9db2643",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T09:01:21.890Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GofLMAbtj3mQfFohZ4Xdq3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5fad6ea-b9df-4eb3-8a97-c7c92200af4e",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sLijbmwAxEX6jTtpT9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb94001b-af71-4104-bc1f-5563734b80d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhhM115WrfFeZgLVcQCzaD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5683,
      "cache_read_input_tokens": 42512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5683,
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

_source line 30 · 2026-05-17T09:01:21.897Z_

<details><summary>↩ Tool result · `toolu_01GofLMAbtj3mQfFohZ4Xdq3`</summary>

```text
1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether atlas accuracy (69.6--85.4\%) reflects genuine statistical regularities, evaluating along seven axes: four below (\S\ref{sec:gen:baselines}--\S\ref{sec:gen:crossscale}) and three in the Appendix (end-to-end learning, temperature robustness, cross-boundary transfer).
5	
6	\subsection{Classifier Comparison and Surface-Text Ablation}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} evaluates bagging (RF) and gradient boosting (XGBoost, LightGBM) on the same 19 features; per-cell spread is $\leq$0.4pp, establishing a feature-determined ceiling.
10	On Pythia nucleus, CORAL ordinal regression \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match the within-cell RF of Table~\ref{tab:main_matrix} within 0.1\,pp (bootstrap $p>0.05$, Bonferroni-corrected); all feature-based methods significantly outperform CE-MLP (74.9\%, $p<0.001$) and logistic regression (75.0\%).
11	
12	\paragraph{Surface-text ablation.}
13	Single-feature regression on mean perplexity performs at chance (25.1\%); two zero-shot LLMs (DeepSeek V3.2, 36.2\%; Qwen2.5-7B-Instruct, 30.4\%; each 500 samples, prompt in Appendix~\ref{app:zeroshot_prompt}) also fail, confirming that the depth signal resides in distributional statistics inaccessible from surface text alone (42\,pp gap vs.\ RF at 78.2\%).
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\caption{Classifier convergence: 4-class accuracy (\%) across three atlas cells. RF (bagging), XGBoost and LightGBM (gradient boosting) operate on the same 19 features; $\Delta_{\max}$: largest per-cell spread. Chance = 25\%. RF values differ from Table~\ref{tab:main_matrix} by $\leq$0.7pp due to matched-fold evaluation.}
19	\label{tab:baselines}
20	\begin{tabular}{@{}lcccc@{}}
21	\toprule
22	Cell & RF & XGB & LGBM & $\Delta_{\max}$ \\
23	\midrule
24	Pythia, nuc. & 78.8 & 79.0 & 78.9 & 0.2 \\
25	GPT-2~XL, $\tau$ & 85.8 & 86.2 & 86.2 & 0.4 \\
26	Pythia, top-$k$ & 68.9 & 68.9 & 68.7 & 0.2 \\
27	\bottomrule
28	\end{tabular}
29	\end{table}
30	
31	Convergence confirms the signal resides in the features, not the classifier.
32	Figure~\ref{fig:confusion_matrix} shows d0 near-perfectly identified; errors concentrate at d2/d3 in-distribution and spread to d1--d3 under transfer.
33	
34	\begin{figure}[t]
35	\centering
36	\includegraphics[width=\columnwidth]{figures/fig_confusion_matrix.pdf}
37	\caption{Confusion matrices for the best in-distribution setting (GPT-2 XL, temp $\tau{=}0.9$, 85.4\%) and the best cross-model leave-one-out transfer (OLMo holdout, 69.2\%). d0 recall exceeds 99\% in both; errors spread across the d1--d3 range under transfer.}
38	\label{fig:confusion_matrix}
39	\end{figure}
40	
41	\subsection{Cross-Model Transfer}
42	\label{sec:gen:crossmodel}
43	
44	We perform leave-one-model-family-out evaluation: train on two families (nucleus only), test on the held-out third (Table~\ref{tab:cross_model}).
45	
46	\begin{table}[t]
47	\centering
48	\small
49	\caption{Cross-model transfer (leave-one-out, nucleus only). Chance = 25\% / 33\% (d1--d3). d1--d3 bal.\ acc: Pythia 49.9\%, OLMo 59.2\%, GPT-2~XL 57.2\% (mean 55.4\%).}
50	\label{tab:cross_model}
51	\begin{tabular}{lccccc}
52	\toprule
53	Holdout & Acc & d0 & d1 & d2 & d3 \\
54	 & (\%) & Rec. & Rec. & Rec. & Rec. \\
55	\midrule
56	Pythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\
57	OLMo & \textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\
58	GPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\
59	\midrule
60	Mean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\
61	\bottomrule
62	\end{tabular}
63	\end{table}
64	
65	Mean transfer accuracy is 66.4\% (2.7$\times$ chance); d0 recall ($>$98\%) inflates the headline while d2 drops to 26.8\% (Pythia holdout); excluding d0, d1--d3 balanced accuracy averages 55.4\%.
66	
67	\subsection{Cross-Strategy Transfer}
68	\label{sec:gen:crossstrategy}
69	
70	We train on two decoding strategies and test on the held-out third (Table~\ref{tab:cross_strategy}).
71	
72	\begin{table}[t]
73	\centering
74	\small
75	\caption{Cross-strategy transfer (leave-one-out). Chance = 25\% / 33\% (d1--d3). d0 recall $\geq$89\% inflates headline; d1--d3 mean: 45.9\%.}
76	\label{tab:cross_strategy}
77	\begin{tabular}{lccc}
78	\toprule
79	Holdout & Pythia & OLMo & GPT-2 XL \\
80	 & Acc (\%) & Acc (\%) & Acc (\%) \\
81	\midrule
82	nucleus & \textbf{69.4} & \textbf{65.4} & \textbf{59.9} \\
83	temp ($\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\
84	top-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\
85	\bottomrule
86	\end{tabular}
87	\end{table}
88	
89	Mean cross-strategy accuracy (59.1\%) falls 7pp below cross-model transfer (66.4\%); excluding d0, d1--d3 accuracy drops to 45.9\% (chance = 33\%).
90	d2 recall varies sharply: nucleus holdouts retain 30--54\%, top-$k$ holdouts fall to 8--19\%, and temperature holdouts span 3.7--39.5\% (median 8.9\%).
91	Training on nucleus + top-$k$ and testing on temperature inverts the d1/d2 boundary (d1v2 AUC $<$ 0.5); per-strategy z-score normalization partially recovers it but leaves a residual gap (Limitations).
92	A multi-temperature ablation (Appendix~\ref{app:multi_tau}) confirms that within-$\tau$ depth signal holds for $\tau \leq 0.9$ (d1v2 AUC $>0.80$, accuracy within 3pp of $\tau{=}0.7$) but collapses at $\tau{=}1.1$; cross-$\tau$ LOO transfer (mean 46.7\%) is harder than cross-strategy transfer.
93	
94	End-to-end PLMs (DeBERTa-v3, RoBERTa) achieve only ${\sim}$59\%, lagging RF by 19pp, confirming depth signal is inaccessible to standard PLM representations (Appendix~\ref{app:e2e}).
95	
96	%% ----------------------------------------------------------------
97	\subsection{Preliminary Cross-Scale Observations}
98	\label{sec:gen:crossscale}
99	
100	To test whether depth signal persists at larger scale, we extend the benchmark to Qwen2.5-7B-Instruct~\cite{qwen2.5} and Llama-3.1-8B-Instruct~\cite{llama3} under 4-bit NF4 QLoRA (nucleus $p{=}0.95$, 500 samples/depth, depths 0--5).
101	Both models exceed chance: Llama-3.1-8B achieves 70.2\% (95\% CI $[68.3, 72.4]$, $\mathrm{EDD}_{0.70}{=}4$) and Qwen2.5-7B 60.1\% ($[58.0, 62.1]$, $\mathrm{EDD}_{0.70}{>}5$), with weaker per-step signal than 1--1.5B models (mean consecutive AUC ${\approx}$0.78 vs.\ 0.85).
102	The two instruction-tuned models exhibit divergent AUC trajectories: Llama-3.1-8B decays monotonically (consistent with 1--1.5B), while Qwen2.5-7B shows a U-shaped recovery.
103	
104	\paragraph{Base vs.\ Instruction-Tuned Control.}
105	A base-model control (Llama-3.1-8B) achieves 59.9\% with non-monotonic AUC decay, while the instruction-tuned variant reaches 70.2\% with strictly monotonic decay, suggesting instruction-tuning \emph{regularizes} recursive degradation patterns rather than introducing confounding artifacts.
106	
107	Four confounds (quantization, reduced $n$, single strategy, vocabulary mismatch) limit causal attribution; full results including per-pair AUC tables appear in Appendix~\ref{app:cross_scale_full}.
108	Cross-model recursive chains (84.75\%), validated by a reverse-chain control (85.75\%; Appendix~\ref{app:cross_boundary}), and cross-domain transfer (arXiv 74.1\%) further confirm signal universality.
109	
110	\paragraph{LoRA rank sensitivity.}
111	Depth signal persists across LoRA ranks 4--64 (accuracy spread 4.65\,pp; Appendix~\ref{app:cross_scale_full}), confirming the phenomenon is not an artifact of a specific fine-tuning configuration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb94001b-af71-4104-bc1f-5563734b80d7",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "84631076-915d-4121-8d83-147faeaf7ad1",
  "sourceToolAssistantUUID": "cb94001b-af71-4104-bc1f-5563734b80d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T09:01:22.003Z_

<details open><summary>🔧 Tool call — Read · `toolu_012k7aaiTx8fSA4Ctk3vFb6A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84631076-915d-4121-8d83-147faeaf7ad1",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sLijbmwAxEX6jTtpT9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a12013f4-b612-49d4-8d85-8803ae1f6b15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhhM115WrfFeZgLVcQCzaD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5683,
      "cache_read_input_tokens": 42512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5683,
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

_source line 32 · 2026-05-17T09:01:22.009Z_

<details><summary>↩ Tool result · `toolu_012k7aaiTx8fSA4Ctk3vFb6A`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Cross-strategy deployment constraint.}
5	Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
6	Per-strategy z-score normalization partially corrects the inversion under logistic regression (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but yields negligible improvement for the Random Forest classifier used throughout the main experiments ($\Delta < 0.02$\,pp), and even in the best case (logistic regression) leaves a residual gap relative to within-strategy performance (${\sim}0.83$), indicating that a two-stage pipeline (strategy identification + strategy-conditioned classification) is needed for reliable cross-strategy deployment.
7	
8	\paragraph{d0 inflation of headline metrics.}
9	Depth~0 (human-written text) is near-perfectly separable (recall $>$98\% across all nine model--strategy settings), inflating headline accuracy.
10	Cross-model transfer accuracy of 66.4\% is substantially driven by d0; d2 recall drops to 26.8\% in the worst case (Pythia holdout).
11	
12	\paragraph{Controlled vs.\ ecological setting.}
13	The primary benchmark uses Wikipedia seed text with controlled recursive generation (LoRA fine-tuning, 1--1.5B parameter models); cross-scale experiments extend to 7--8B instruction-tuned models (\S\ref{sec:gen:crossscale}).
14	This protocol isolates the recursive depth variable but diverges from wild recursive contamination, where models are pretrained on mixed corpora containing prior-generation outputs at unknown proportions; the fingerprints we identify may attenuate or shift under such diffuse exposure.
15	Depth signal is the dominant classification factor (5-fold CV 59--82\%, up to 2.5$\times$ chance): LOGO accuracy (72.1\%) matches standard CV (72.0\%), and seed-group prediction is at chance (10.2\% vs.\ 10\%; Appendix~\ref{app:domain_bias}).
16	Cross-scale experiments include both instruction-tuned and base variants; the base model shows weaker but above-chance depth signal (59.9\% vs.\ 70.2\%) with non-monotonic AUC decay, suggesting instruction-tuning regularizes degradation patterns.
17	Real-world documents may also interleave segments at different recursive generation depths; extending to segment-level estimation introduces a granularity--statistical-power tradeoff.
18	
19	\paragraph{Domain-dependent false positive rate.}
20	On editorial text (WikiText-103), all classifiers achieve $\geq$98.5\% d0 accuracy, but on web-crawl data (C4, 5{,}000 passages), FPR ranges from 4.7\% (OLMo) to 22.4\% (GPT-2~XL).
21	Misclassifications concentrate in template/SEO content with elevated repetition features (\texttt{rep\_3gram} $+$37\%, \texttt{rep\_4gram} $+$75\% vs.\ correctly classified d0); the model gap likely reflects training data composition (OLMo's Dolma includes diverse web data vs.\ Pythia/GPT-2~XL's Wikipedia/WebText).
22	Deployment on heterogeneous web corpora requires model- and domain-specific calibration.
23	
24	\paragraph{Adversarial robustness.}
25	Adversarial paraphrasing \cite{sadasivan2023_paraphrase} could disrupt the perplexity tail features that drive classification; depth estimation's robustness under such attacks is untested.
26	
27	\paragraph{EDD monotonicity assumption.}
28	Our EDD definition (Eq.~\ref{eq:edd}) requires all pairwise AUCs up to depth $d^*$ to exceed $T$, which is well-behaved when AUC decays monotonically, as observed in all our configurations.
29	However, \citet{bakshi2026_collapse_improvement} show that early recursion can temporarily \emph{improve} model quality, which could produce non-monotonic AUC profiles (e.g., a dip at d1/d2 followed by recovery at d2/d3).
30	Our cross-strategy transfer results provide an empirical example: training on nucleus + top-$k$ and testing on temperature yields d1-vs-d2 AUC as low as 0.129 (GPT-2~XL) and 0.253 (OLMo), violating the monotonicity assumption.
31	In such cases EDD would conservatively report a lower value than the deepest discriminable pair, potentially underestimating the true discriminable range; extending EDD to handle non-contiguous discriminable regions is future work.
32	The choice of threshold $T$ is also application-dependent: at $T{=}0.80$, several cells lose one depth level relative to $T{=}0.75$.
33	
34	\paragraph{Reference model dependency.}
35	Reference model choice affects classification accuracy by up to 11\,pp; same-family references yield optimal performance, though all configurations exceed $2.5\times$ chance.
36	Surprisal-based features are computed relative to Pythia-1.4B, which coincides with one of the three generators.
37	For the Pythia pipeline this constitutes self-model feature extraction, while OLMo and GPT-2~XL measurements are cross-model.
38	Empirically, the self-model configuration does not yield the highest accuracy (Pythia 78.2\% vs.\ GPT-2~XL 85.4\%), suggesting the overlap does not confer a systematic advantage.
39	An ablation with OLMo-1B and GPT-2 XL as alternative references shows accuracy ranging from 67--79\% across three reference architectures (Appendix~\ref{app:ref_ablation}), all exceeding $2.5\times$ chance; same-family reference yields optimal performance ($\Delta{\leq}$11\,pp).
40	The choice of reference model affects feature values; a different reference model may shift absolute feature magnitudes and potentially alter discriminability at depth boundaries.
41	Reference-free surface features alone achieve 53.7\% (confirming partial signal in lexical statistics) but 25pp below the full pipeline, underscoring that surprisal-based features are essential.
42	Simple multi-reference ensembling does not outperform the best single reference (73.7\% vs.\ 78.6\%).
43	
44	\paragraph{Single LoRA instance.}
45	Independent replication with seed=43 yields 77.15\% (95\% CI [76.4, 78.15], $\Delta{=}{-}1.05$\,pp vs.\ baseline); cross-seed transfer retains 76.76\% ($\Delta{=}{-}1.30$\,pp vs.\ within-seed avg), confirming depth signal is inherent to the recursive process rather than specific LoRA weights (Appendix~\ref{app:seed_replication}).
46	Top-5 feature importance is identical across seeds.
47	
48	\paragraph{Additional caveats.}
49	Depth signal scales with passage length (128 tokens: 68.4\%, 512 tokens: 77.8\%; Appendix~\ref{app:length_ablation}), saturating near 500 tokens; shorter passages remain above chance but with reduced discriminability.
50	Detection features degrade under domain shift \cite{pudasaini2026_detection_fails}; our depth features are likely susceptible.
51	\citet{falahati2026_curated} show that curated synthetic data need not trigger collapse, attenuating the fingerprints we exploit.
52	
53	\section*{Ethics Statement}
54	
55	This work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2~XL) and Wikipedia text as seed data.
56	No human subjects were involved, no private or sensitive data were collected, and no new models were released.
57	Our method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research.
58	Code and data will be released upon acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a12013f4-b612-49d4-8d85-8803ae1f6b15",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "268e4103-bf9c-4c73-b276-85356442444c",
  "sourceToolAssistantUUID": "a12013f4-b612-49d4-8d85-8803ae1f6b15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T09:01:27.268Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qf4BzJvGoEtGPWoGA9qneE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "268e4103-bf9c-4c73-b276-85356442444c",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sM5j9qbBR7qrfLFV6Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce576ace-5205-45cc-9e65-bfb3460b6469",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkT5CRWF3qgTCFmRBxpUNc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5321,
      "cache_read_input_tokens": 48195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5321,
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

_source line 34 · 2026-05-17T09:01:27.285Z_

<details><summary>↩ Tool result · `toolu_01Qf4BzJvGoEtGPWoGA9qneE`</summary>

```text
1	\section{Additional Results}
2	\label{app:additional}
3	
4	\subsection{Top-$k$ Feature Trajectories}
5	\label{app:topk_trajectories}
6	
7	Figure~\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
8	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
9	Concretely, the d0$\to$d1 drop in \textsc{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
10	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
11	
12	\subsection{Permutation Importance}
13	\label{app:permutation}
14	
15	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
16	The top-2 features are stable across measures: \textsc{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \textsc{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \textsc{p75\_ppl} displaces \textsc{var\_surprisal} to rank 3).
17	Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
18	Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.84$, Gini--permutation $\rho{=}0.76$.
19	Per-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical, confirming that the top features are robust to the choice of importance measure at the aggregate level while per-cell rankings exhibit model-dependent variation.
20	
21	\subsection{Per-Class Recall}
22	\label{app:per_class}
23	
24	Table~\ref{tab:per_class_recall} reports per-class recall across all 9 atlas cells (4-class in-distribution, 5-fold CV).
25	Depth~0 recall exceeds 98\% uniformly.
26	Among generated depths, d2 is the hardest class in every cell; the deficit is most pronounced under top-$k$ sampling (46--53\%), where vocabulary truncation removes the tail tokens that carry depth-discriminative signal.
27	
28	\begin{table}[h]
29	\centering
30	\small
31	\caption{Per-class recall (\%) for all 9 atlas cells. d2 is the lowest-recall class in every cell. Boldface marks the highest d2 recall.}
32	\label{tab:per_class_recall}
33	\begin{tabular}{@{}lcccc@{}}
34	\toprule
35	Cell & d0 & d1 & d2 & d3 \\
36	\midrule
37	Pythia, nuc.       & 99.7 & 81.9 & 58.7 & 72.3 \\
38	Pythia, $\tau$     & 99.7 & 81.3 & 53.9 & 72.1 \\
39	Pythia, top-$k$    & 99.5 & 72.3 & 45.6 & 57.5 \\
40	OLMo, nuc.         & 98.8 & 80.5 & 61.5 & 74.3 \\
41	OLMo, $\tau$       & 99.7 & 87.7 & 66.1 & 77.2 \\
42	OLMo, top-$k$      & 99.5 & 78.5 & 51.2 & 65.6 \\
43	GPT-2~XL, nuc.     & 99.2 & 85.9 & \textbf{73.3} & 77.5 \\
44	GPT-2~XL, $\tau$   & 99.5 & 90.9 & 68.8 & 81.9 \\
45	GPT-2~XL, top-$k$  & 98.5 & 79.5 & 52.5 & 71.1 \\
46	\bottomrule
47	\end{tabular}
48	\end{table}
49	
50	\subsection{DCOL Iteration Details}
51	\label{app:dcol_iterations}
52	
53	Table~\ref{tab:dcol_iterations} summarizes all six DCOL iterations.
54	DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.
55	
56	\begin{table}[h]
57	\centering
58	\small
59	\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.2\%.}
60	\label{tab:dcol_iterations}
61	\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}
62	\toprule
63	Ver. & Backbone & Config & Outcome \\
64	\midrule
65	v1 & DeBERTa & FT, m\_lr $10^{-3}$ & Embed.\ collapse (31.5\%) \\
66	v2 & DeBERTa & FT, m\_lr $10^{-4}$ & OOM \\
67	v3 & DeBERTa & FT, m\_lr $10^{-4}$ & Forgetting + OOM \\
68	v4 & DeBERTa & LoRA, m\_lr $10^{-3}$ & Embed.\ collapse \\
69	v5 & DeBERTa & LoRA, m\_lr $10^{-4}$ & NaN gradients \\
70	v6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\% ($-$13.7pp) \\
71	\bottomrule
72	\end{tabular}
73	\end{table}
74	
75	\subsection{Zero-Shot LLM Prompt Template}
76	\label{app:zeroshot_prompt}
77	
78	Both DeepSeek V3.2 and Qwen2.5-7B-Instruct use identical prompting.
79	The system message defines recursive generation depth with per-depth descriptions (depth~0: human-written; depth~1--3: successive LLM generation cycles) and lists expected textual patterns at each depth (vocabulary richness, repetition, coherence).
80	The user message presents the passage (truncated to ${\approx}$384 words) and requests a JSON response containing an integer depth prediction (0--3), a confidence score, and a one-sentence reasoning.
81	No in-context examples are provided.
82	
83	\begin{quote}
84	\small
85	\textbf{System:} ``You are an expert at detecting AI-generated text and estimating its generation depth. `Recursive generation depth' refers to how many times a text has been through an LLM generation cycle: Depth~0: Original human-written text [\ldots] Depth~3: Text generated by an LLM given depth-2 text as input. Key patterns by depth: Depth~0 (human): Rich vocabulary [\ldots] Depth~3 (third-gen): Noticeable repetition, formulaic structure [\ldots]''
86	
87	\textbf{User:} ``Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3). TEXT: \{text\}. Respond with ONLY a JSON object: \{\texttt{"depth"}: $\langle$int 0--3$\rangle$, \texttt{"confidence"}: $\langle$float 0--1$\rangle$, \texttt{"reasoning"}: $\langle$str$\rangle$\}''
88	\end{quote}
89	
90	\subsection{Temperature Robustness}
91	\label{app:multi_tau}
92	
93	The cross-strategy results in \S\ref{sec:gen:crossstrategy} use a single temperature ($\tau{=}0.9$).
94	To test whether depth signal generalizes across temperatures, we repeat the classification pipeline at $\tau \in \{0.5, 0.7, 0.9, 1.1\}$ on Pythia-1.4B.
95	
96	\paragraph{Within-$\tau$ robustness.}
97	For $\tau \in [0.5, 0.9]$, d1-vs-d2 AUC exceeds 0.80 (peak 0.851 at $\tau{=}0.7$, comparable to nucleus $p{=}0.95$'s 0.861) and 4-class accuracy ranges from 75.4\% to 77.3\% (Table~\ref{tab:multi_tau_within}), confirming the depth signal is not an artifact of a single temperature.
98	The same top-5 features (\texttt{var\_surprisal}, \texttt{p90\_ppl}, \texttt{mean\_ppl}, \texttt{mean\_surprisal}, \texttt{p75\_ppl}) dominate across all $\tau$ values with only minor rank-order variation.
99	
100	\paragraph{Collapse at $\tau{=}1.1$: memorization as prerequisite.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce576ace-5205-45cc-9e65-bfb3460b6469",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "dfca2ca1-7a89-4b89-a154-7f927dde66ab",
  "sourceToolAssistantUUID": "ce576ace-5205-45cc-9e65-bfb3460b6469",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T09:01:27.426Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GspPcqyYBNt4xvHeSjHM2h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfca2ca1-7a89-4b89-a154-7f927dde66ab",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sM5j9qbBR7qrfLFV6Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93e13bf2-83dd-418c-be72-6c6493c9d751",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkT5CRWF3qgTCFmRBxpUNc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5321,
      "cache_read_input_tokens": 48195,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5321
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 48195,
          "cache_creation_input_tokens": 5321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5321,
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

_source line 36 · 2026-05-17T09:01:27.445Z_

<details><summary>↩ Tool result · `toolu_01GspPcqyYBNt4xvHeSjHM2h`</summary>

```text
1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	\usepackage{amsthm}
18	
19	\theoremstyle{definition}
20	\newtheorem{definition}{Definition}
21	
22	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{abstract}
30	
31	\input{introduction}
32	
33	\input{related_work}
34	
35	\input{method}
36	
37	\input{atlas}
38	
39	\input{generalization}
40	
41	\input{discussion}
42	
43	\input{conclusion}
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{section_appendix}
49	
50	\end{document}
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93e13bf2-83dd-418c-be72-6c6493c9d751",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "e0dfa1c3-e284-4a7d-a4bb-4220ee98e562",
  "sourceToolAssistantUUID": "93e13bf2-83dd-418c-be72-6c6493c9d751",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T09:01:35.655Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BhoaoHiTdiZQqmt1WjRbRs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "offset": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0dfa1c3-e284-4a7d-a4bb-4220ee98e562",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sMVC3RyWbxKvJswadF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "326f83db-f4bc-4f69-87a3-0511eabb86c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ufqk2sx8ctk72b4XXb6kvC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3388,
      "cache_read_input_tokens": 53516,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3388
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 53516,
          "cache_creation_input_tokens": 3388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3388,
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

_source line 38 · 2026-05-17T09:01:36.040Z_

<details><summary>↩ Tool result · `toolu_01BhoaoHiTdiZQqmt1WjRbRs`</summary>

```text
100	\paragraph{Collapse at $\tau{=}1.1$: memorization as prerequisite.}
101	At $\tau{=}1.1$, 4-class accuracy drops to 57.2\% and d1v2 AUC falls to 0.528.
102	Training loss reveals the mechanism: at low temperature ($\tau{=}0.5$), fine-tuning loss decreases steeply across recursive depths ($2.27 \to 0.42 \to 0.16$), indicating rapid memorization of the model's own output.
103	At $\tau{=}1.1$, loss remains nearly flat ($2.27 \to 1.91 \to 1.85$); high-entropy output resists memorization, so depth-dependent distributional shifts do not accumulate.
104	This establishes \emph{memorization as a prerequisite} for detectable depth signal: recursive depth is discriminable only when successive fine-tuning iterations progressively reshape the output distribution.
105	
106	\paragraph{Cross-$\tau$ non-transferability.}
107	Leave-one-$\tau$-out transfer yields mean accuracy of 46.7\% with mean d1v2 AUC of 0.319 (Table~\ref{tab:multi_tau_cross}), worse than cross-strategy transfer (59.1\%; \S\ref{sec:gen:crossstrategy}).
108	Holdout $\tau{=}0.5$ produces inverted d1v2 AUC (0.176), confirming that different temperatures produce surprisal distributions with incompatible shapes.
109	This extends the strategy-specificity finding: even within a single decoding family, the feature space is temperature-specific, reinforcing the need for strategy-conditioned classifiers.
110	
111	\paragraph{Ecological validity.}
112	On WikiText-103 (546 editorial passages), all three model-specific RF classifiers achieve $\geq$98.5\% d0 accuracy despite $+$621\% domain shift in mean perplexity, partly an easy case, as WikiText's higher perplexity places it farther from d1--d3 in feature space.
113	On noisier web-crawl data (5{,}000 C4 passages), FPR ranges from 4.7\% (OLMo) to 22.4\% (GPT-2~XL), concentrated in template/SEO content with high n-gram repetition (Table~\ref{tab:calibration}); deployment on heterogeneous web data requires model-specific calibration.
114	
115	\begin{table}[h]
116	\centering
117	\small
118	\caption{Within-$\tau$ 4-class classification (Pythia-1.4B, 5-fold CV). d$i$v$j$: pairwise AUC for depth $i$ vs.\ depth $j$.}
119	\label{tab:multi_tau_within}
120	\begin{tabular}{@{}lcccc@{}}
121	\toprule
122	$\tau$ & 4-class acc (\%) & d1v2 AUC & d0v1 AUC & d2v3 AUC \\
123	\midrule
124	0.5 & 77.3 & 0.842 & 0.996 & 0.764 \\
125	0.7 & 75.4 & 0.851 & 0.997 & 0.720 \\
126	0.9 & 75.9 & 0.808 & 0.991 & 0.781 \\
127	1.1 & 57.2 & 0.528 & 0.988 & 0.599 \\
128	\bottomrule
129	\end{tabular}
130	\end{table}
131	
132	\begin{table}[h]
133	\centering
134	\small
135	\caption{Cross-$\tau$ leave-one-out transfer (Pythia-1.4B). Train on three temperatures, test on the held-out one.}
136	\label{tab:multi_tau_cross}
137	\begin{tabular}{@{}lcc@{}}
138	\toprule
139	Holdout & Acc (\%) & d1v2 AUC \\
140	\midrule
141	$\tau{=}0.5$ & 52.2 & 0.176 \\
142	$\tau{=}0.7$ & 41.0 & 0.299 \\
143	$\tau{=}0.9$ & 46.4 & 0.277 \\
144	$\tau{=}1.1$ & 47.1 & 0.525 \\
145	\midrule
146	Mean & 46.7 & 0.319 \\
147	\bottomrule
148	\end{tabular}
149	\end{table}
150	
151	\subsection{Feature Overlap Analysis}
152	\label{app:feature_overlap}
153	
154	We probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base.
155	PLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics; \textsc{var\_surprisal} and \textsc{p90\_ppl} yield negative $R^2$ under linear probing, indicating these features are not linearly accessible in the pretrained representation space.
156	This confirms that the 19pp accuracy gap between feature-based and end-to-end methods (\S\ref{app:e2e}) stems from complementary, not redundant, representations: PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.
157	
158	\subsection{End-to-End Learning}
159	\label{app:e2e}
160	
161	DeBERTa-v3-base \cite{he2021_deberta_v3} and RoBERTa-base \cite{liu2019_roberta} finetuned end-to-end achieve 58.3\% ($\pm$4.7\%) and 59.5\% ($\pm$3.2\%) respectively, lagging the RF baseline (78.2\%) by 19.9pp and 18.7pp.
162	The 1.2pp inter-backbone gap rules out architecture bias; Table~\ref{tab:e2e_detail} shows both backbones share the same failure mode (high d0 F1, $>$0.94, but collapsed d1/d2 performance, F1 $\leq$ 0.42), while RF achieves 0.596 d2 recall, a $>$2$\times$ advantage at the hardest depth class.
163	
164	\begin{table}[h]
165	\centering
166	\small
167	\caption{Per-class performance for end-to-end PLM classifiers vs.\ RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall (the class with the largest PLM--RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 scores despite adequate d0/d3.}
168	\label{tab:e2e_detail}
169	\begin{tabular}{@{}lccccc@{}}
170	\toprule
171	Method & Acc (\%) & d0 & d1 & d2 & d3 \\
172	\midrule
173	DeBERTa-v3 & 58.3\,$\pm$\,4.7 & .947 & .378 & .247 & .656 \\
174	RoBERTa-base & 59.5\,$\pm$\,3.2 & .958 & .416 & .261 & .647 \\
175	\midrule
176	RF (19 feat.) & 78.2 & --- & --- & .596$^\dagger$ & --- \\
177	\bottomrule
178	\multicolumn{6}{@{}l}{\footnotesize $^\dagger$Recall; shown for the depth class with the largest PLM--RF gap.}
179	\end{tabular}
180	\end{table}
181	
182	\paragraph{Feature space divergence.}
183	SHAP TreeExplainer analysis confirms that perplexity and surprisal features account for 88.8\% of RF's total contribution.
184	Three independent importance measures (SHAP, Gini, and permutation) show strong concordance (Kendall's $W{=}0.90$, $p{<}0.005$; pairwise Spearman $\rho$: SHAP--Gini $0.93$, SHAP--permutation $0.84$; \S\ref{app:permutation}), with \texttt{p90\_ppl} appearing in the SHAP top-2 in 9/9 cells and \texttt{var\_surprisal} in 8/9.
185	Linear probing of PLM [CLS] representations yields negative $R^2$ for both \texttt{var\_surprisal} and \texttt{p90\_ppl} (\S\ref{app:feature_overlap}), indicating that pretrained representations lack the linear structure needed to recover perplexity tail statistics, a systematic representational gap rather than a backbone-specific artifact.
186	
187	DCOL \cite{cloc2025} reached 64.5\% (\S\ref{app:dcol_iterations}); all end-to-end approaches (58--65\%) underperform feature-based methods, suggesting depth estimation benefits from targeted statistical features that capture distributional tail properties absent from PLM representations.
188	This comparison is bounded by backbone scale ($\leq$125M parameters); whether larger PLMs (e.g., 7B+) can close the gap via richer internal representations remains an open question.
189	
190	\subsection{Domain Bias Analysis}
191	\label{app:domain_bias}
192	
193	To assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.
194	
195	\paragraph{Methodological note.}
196	An initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\%, seed-group prediction 20.8\%).
197	We discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.
198	The results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.
199	
200	\paragraph{Sub-A: Standard CV.}
201	Five-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\% to 82\% across the 9 atlas cells (up to 2.5$\times$ above the 33.3\% chance level), confirming that depth signal is the dominant classification factor.
202	
203	\paragraph{Sub-B: LOGO evaluation.}
204	We assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.
205	LOGO mean accuracy is 72.1\% (range 59.5--81.6\%), matching standard CV (72.0\%) within noise (before fix: 64.0\%, reflecting the depth--group confound).
206	Per-cell fold standard deviations range from 0.4pp to 1.4pp, indicating that cross-group generalization is as reliable as within-group classification.
207	
208	\paragraph{Sub-C: Negative control.}
209	We train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\%).
210	Depth prediction accuracy averages 72.0\%; seed-group prediction averages 10.2\%, indistinguishable from chance (before fix: 20.8\%, inflated by the depth--group confound).
211	The depth-to-seed-group accuracy ratio is 7.1$\times$, confirming that the feature representation encodes depth but not seed-article identity.
212	
213	Taken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.
214	
215	\subsection{Wild-Data Calibration}
216	\label{app:calibration}
217	
218	Table~\ref{tab:calibration} reports d0 accuracy and false positive rate (FPR) for all three model-specific nucleus RF classifiers on two out-of-distribution human-text corpora: WikiText-103 (546 editorial passages) and C4 (5{,}000 web-crawl passages).
219	
220	\begin{table}[h]
221	\centering
222	\small
223	\caption{Wild-data d0 accuracy and FPR for nucleus RF classifiers. All passages are human-written (true d0). FPR = fraction misclassified as d1+. 95\% Wilson CIs computed for C4 ($n{=}5{,}000$).}
224	\label{tab:calibration}
225	\begin{tabular}{@{}llrccc@{}}
226	\toprule
227	Model & Source & $n$ & d0 (\%) & FPR (\%) & 95\% Wilson CI \\
228	\midrule
229	Pythia-1.4B & WikiText & 546 & 100.0 & 0.0 & --- \\
230	 & C4 & 5{,}000 & 79.8 & 20.2 & [19.1, 21.3] \\
231	\addlinespace
232	GPT-2~XL & WikiText & 546 & 99.3 & 0.7 & --- \\
233	 & C4 & 5{,}000 & 77.6 & 22.4 & [21.3, 23.6] \\
234	\addlinespace
235	OLMo-1B & WikiText & 546 & 98.5 & 1.5 & --- \\
236	 & C4 & 5{,}000 & 95.3 & 4.7 & [4.2, 5.3] \\
237	\bottomrule
238	\end{tabular}
239	\end{table}
240	
241	On WikiText-103, all three classifiers achieve $\geq$98.5\% d0 accuracy, confirming that editorial text is reliably distinguished from recursive generations across model families.
242	On C4, FPR varies sharply: OLMo (4.7\%) vs.\ Pythia (20.2\%) and GPT-2~XL (22.4\%).
243	C4 misclassifications concentrate in template and SEO content with elevated repetition features (\texttt{rep\_3gram} $+$37\%, \texttt{rep\_4gram} $+$75\% vs.\ correctly classified d0 passages), rather than in random noise.
244	The model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2~XL (trained primarily on Wikipedia/WebText) map template-heavy content into the d1+ region.
245	Among C4 false positives for GPT-2~XL, predictions distribute as d1 (9.0\%), d2 (3.7\%), d3 (9.6\%); for OLMo, d1 (2.9\%), d2 (0.5\%), d3 (1.3\%). The non-uniform depth distribution suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.
246	
247	\subsection{Downstream Curation PoC}
248	\label{app:curation_poc}
249	
250	To validate that depth estimation translates to actionable data curation, we conduct a proof-of-concept downstream evaluation.
251	We fine-tune Pythia-410M with LoRA ($r{=}16$, $\alpha{=}32$) for 3 epochs on 8 data conditions derived from the Pythia nucleus depth-estimation corpus, repeating each condition over 5 random seeds.
252	Conditions vary the selection mechanism (RF-predicted depth, oracle depth, random subsampling) and stringency (strict $\approx$25\%, moderate $\approx$50\%, soft threshold).
253	Table~\ref{tab:curation_poc} reports per-condition perplexity; Table~\ref{tab:curation_comparisons} reports pairwise contrasts.
254	
255	\begin{table}[h]
256	\centering
257	\small
258	\caption{Curation PoC: per-condition perplexity (Pythia-410M LoRA, 5 seeds). $\Delta$ is signed so that positive values indicate lower (better) perplexity than unfiltered. $^*$\,: $p<0.05$ (paired $t$-test vs.\ unfiltered).}
259	\label{tab:curation_poc}
260	\resizebox{\columnwidth}{!}{%
261	\begin{tabular}{@{}lcccccc@{}}
262	\toprule
263	Condition & Mean PPL & Std & $n$ & $\Delta$ vs Unfilt. & $p$ & $d_z$ \\
264	\midrule
265	unfiltered        & 15.776 & 0.066 & 10{,}000 & ---      & ---   & ---      \\
266	rf\_soft          & 15.733 & 0.038 &  4{,}422 & +0.043   & 0.407 &  0.41    \\
267	rf\_moderate      & 15.756 & 0.056 &  4{,}940 & +0.021   & 0.492 &  0.34    \\
268	rf\_strict        & 15.810 & 0.061 &  2{,}496 & $-$0.034 & 0.607 & $-$0.25  \\
269	oracle\_moderate  & 15.809 & 0.103 &  5{,}000 & $-$0.033 & 0.485 & $-$0.34  \\
270	oracle\_strict    & 15.879 & 0.128 &  2{,}500 & $-$0.103 & 0.216 & $-$0.66  \\
271	random\_soft      & 16.062 & 0.079 &  4{,}422 & $-$0.286 & ${<}$0.001$^*$ & $-$2.77  \\
272	random\_moderate  & 15.998 & 0.090 &  4{,}940 & $-$0.222 & 0.028$^*$ & $-$1.50  \\
273	random\_strict    & 16.239 & 0.165 &  2{,}496 & $-$0.463 & 0.013$^*$ & $-$1.89  \\
274	\bottomrule
275	\end{tabular}}
276	\end{table}
277	
278	\begin{table}[h]
279	\centering
280	\small
281	\caption{Pairwise comparisons (paired $t$-test, 5 seeds). $^*$\,: $p<0.05$; $^{**}$\,: $p<0.01$.}
282	\label{tab:curation_comparisons}
283	\begin{tabular}{@{}lccc@{}}
284	\toprule
285	Comparison & $\Delta$ PPL & $t$ & $p$ \\
286	\midrule
287	rf\_strict vs random\_strict     & 0.429 & $-$7.05 & 0.002$^{**}$ \\
288	rf\_moderate vs random\_moderate & 0.242 & $-$3.77 & 0.020$^*$    \\
289	rf\_soft vs random\_soft         & 0.328 & $-$17.98 & ${<}$0.001$^{**}$ \\
290	rf\_soft vs unfiltered           & 0.043 &    0.93 & 0.407        \\
291	\bottomrule
292	\end{tabular}
293	\end{table}
294	
295	\subsection{Reference Model Ablation}
296	\label{app:ref_ablation}
297	
298	\begin{table}[h]
299	\centering
300	\caption{Reference model ablation. Classification accuracy (5-fold CV) on Pythia-1.4B generated text (nucleus, d0--d3) using different reference models for feature extraction.}
301	\label{tab:ref_ablation}
302	\begin{tabular}{lcc}
303	\toprule
304	Reference Model & Architecture & Accuracy (\%) \\
305	\midrule
306	Pythia-1.4B (self) & GPT-NeoX & 78.6 $\pm$ 0.6 \\
307	OLMo-1B (cross) & OLMo & 74.5 $\pm$ 0.7 \\
308	\bottomrule
309	\end{tabular}
310	\end{table}
311	
312	\subsection{Cross-Scale Full Results}
313	\label{app:cross_scale_full}
314	
315	This section provides the full cross-scale analysis summarized in \S\ref{sec:gen:crossscale}.
316	We extend the benchmark to two 7--8B models: Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct, both under 4-bit NF4 QLoRA fine-tuning, generating depths $d \in \{0, 1, \ldots, 5\}$ with nucleus sampling ($p{=}0.95$, 500 samples per depth).
317	Feature extraction uses the same reference model (Pythia-1.4B) and 19-feature pipeline as all prior experiments.
318	
319	\paragraph{Scale comparison.}
320	Table~\ref{tab:cross_scale} contrasts the two 7--8B models with the three 1--1.5B models on matched evaluation (nucleus sampling, depths 0--3).
321	
322	\begin{table}[h]
323	\centering
324	\small
325	\caption{Cross-scale comparison: 4-class RF accuracy (\%, depths 0--3, nucleus), $\mathrm{EDD}_{T{=}0.70}$ (depths 0--5), and d0-vs-d1 AUC. CI: 95\% bootstrap. Chance = 25\%.}
326	\label{tab:cross_scale}
327	\begin{tabular}{@{}lccc@{}}
328	\toprule
329	Model & 4-class acc & $\mathrm{EDD}_{T{=}0.70}$ & d0v1 AUC \\
330	\midrule
331	GPT-2~XL (1.5B) & 83.3 & 4 & 0.999 \\
332	OLMo-1B & 78.8 & 4 & 0.997 \\
333	Pythia-1.4B & 78.2 & 4 & 0.998 \\
334	\midrule
335	Llama-3.1-8B & 70.2\,[68.3, 72.4] & 4 & 0.949 \\
336	Qwen2.5-7B & 60.1\,[58.0, 62.1] & ${>}5$ & 0.969 \\
337	\bottomrule
338	\end{tabular}
339	\end{table}
340	
341	\paragraph{(1) Depth signal persists at 7--8B scale.}
342	Both 7--8B models substantially exceed the 25\% chance baseline: Llama-3.1-8B achieves 70.2\% (95\% CI $[68.3, 72.4]$) and Qwen2.5-7B achieves 60.1\% ($[58.0, 62.1]$), confirming that recursive depth remains estimable from perplexity-based features even when the generator is 5--7$\times$ larger than the reference model.
343	Depth-0 separability is preserved in both models: d0v1 AUC is 0.949 (Llama-3.1) and 0.969 (Qwen2.5).
344	
345	\paragraph{(2) EDD at 7--8B scale.}
346	At threshold $T{=}0.70$, Qwen2.5-7B maintains all consecutive-pair AUCs above 0.70 through depth~5 (Table~\ref{tab:cross_scale_auc}), yielding $\mathrm{EDD}_{T{=}0.70} > 5$, exceeding the $\mathrm{EDD}{=}4$ observed at 1--1.5B.
347	Llama-3.1-8B matches the smaller models at $\mathrm{EDD}{=}4$: its monotonic decay causes d4v5 (0.618) to drop below $T$, despite stronger signal at shallower depths.
348	Both larger generators produce weaker per-step signal than the 1--1.5B models (mean consecutive AUC: 0.786 for Llama-3.1, 0.782 for Qwen2.5, vs.\ 0.852 at 1--1.5B).
349	
350	\begin{table}[h]
351	\centering
352	\small
353	\caption{Consecutive binary AUC for 7--8B models (nucleus $p{=}0.95$). Llama-3.1-8B exhibits monotonic decay (d4v5 drops below $T{=}0.70$); Qwen2.5-7B shows a non-monotonic (U-shaped) pattern with all pairs above $T$.}
354	\label{tab:cross_scale_auc}
355	\begin{tabular}{@{}lccccc@{}}
356	\toprule
357	Model & d0v1 & d1v2 & d2v3 & d3v4 & d4v5 \\
358	\midrule
359	Llama-3.1-8B & 0.949 & 0.877 & 0.771 & 0.716 & 0.618 \\
360	Qwen2.5-7B & 0.969 & 0.729 & 0.709 & 0.732 & 0.772 \\
361	\bottomrule
362	\end{tabular}
363	\end{table}
364	
365	\paragraph{(3) Divergent AUC trajectories and instruction-tuning effect.}
366	Among instruction-tuned models, Llama-3.1-8B exhibits monotonic AUC decay consistent with the 1--1.5B pattern, while Qwen2.5-7B shows a U-shaped recovery beyond d2v3 (Table~\ref{tab:cross_scale_auc}).
367	A base-model control (Llama-3.1-8B without instruction tuning) clarifies the causal direction: the base model achieves 59.9\% four-class accuracy (95\% CI [57.8, 62.15], $\mathrm{EDD}_{0.70}{=}2$) with non-monotonic AUC decay (Table~\ref{tab:llama3_base_auc}), while the instruction-tuned variant reaches 70.2\% with strictly monotonic decay.
368	The base-model control experiment suggests instruction-tuning regularizes rather than confounds the depth signal.
369	
370	\begin{table}[h]
371	\centering
372	\small
373	\caption{Pairwise AUC: Llama-3.1-8B Base vs.\ Instruct.}
374	\label{tab:llama3_base_auc}
375	\begin{tabular}{lccccc}
376	\toprule
377	Variant & $d_{0\text{v}1}$ & $d_{1\text{v}2}$ & $d_{2\text{v}3}$ & $d_{3\text{v}4}$ & $d_{4\text{v}5}$ \\
378	\midrule
379	Base & 0.918 & 0.794 & 0.682 & 0.730 & 0.595 \\
380	Instruct & 0.965 & 0.874 & 0.771 & 0.716 & 0.618 \\
381	\bottomrule
382	\end{tabular}
383	\end{table}
384	
385	The base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries, confirming depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.
386	
387	\paragraph{Caveats.}
388	For Qwen2.5-7B, the CI lower bound (58.0\%) does not exclude sub-60\% accuracy; Llama-3.1-8B's lower bound (68.3\%) is more comfortably above chance but still below the 75--83\% range at 1--1.5B.
389	The divergent AUC trajectories across two models caution against strong generalizations from only two 7--8B data points: both the monotonic (Llama-3.1) and non-monotonic (Qwen2.5) patterns are single observations, and further architectures are needed to establish which is the dominant regime at this scale.
390	
391	\paragraph{Confounds.}
392	\label{app:cross_scale_confounds}
393	Four confounds limit these results: (1)~4-bit NF4 QLoRA quantization (absent at 1--1.5B) may distort the perplexity distribution independently of depth; (2)~smaller sample size (500 vs.\ 5{,}000 per depth) widens confidence intervals; (3)~evaluation is limited to nucleus sampling, leaving other strategies untested at this scale; (4)~vocabulary mismatch between 7--8B generators and the 1.4B reference model.
394	The base-model control partially addresses a former confound (instruction-tuning): since the base variant shows weaker signal with non-monotonic decay while the instruction-tuned variant shows stronger monotonic signal, instruction-tuning regularizes rather than confounds depth estimation.
395	The remaining confounds are not mutually independent (quantization and vocabulary mismatch both affect the perplexity distribution), making it infeasible to attribute the observed accuracy gap (60--70\% vs.\ 78--85\% at 1--1.5B) to any single factor.
396	
397	\subsection{Cross-Boundary Generalization}
398	\label{app:cross_boundary}
399	
400	The preceding experiments assume a single model family generates all recursive depths.
401	In practice, recursive contamination may traverse model boundaries: text generated by model~A is used to train model~B, whose output trains model~C.
402	We probe whether the depth signal persists under two relaxations of the single-model assumption.
403	
404	\paragraph{Cross-model recursive chains.}
405	We construct a heterogeneous chain: human text (d0) $\to$ Pythia-1.4B generates d1 $\to$ OLMo-1B finetuned on Pythia-d1 generates d2 $\to$ GPT-2~XL finetuned on OLMo-d2 generates d3.
406	Each recursive step uses a \emph{different} model family, eliminating the possibility that depth signal arises from a single model's idiosyncratic behavior.
407	A 4-class Random Forest achieves 84.75\% accuracy (95\% CI $[81.0, 88.25]$), with per-depth F1 scores of 0.98 (d0), 0.88 (d1), 0.76 (d2), and 0.76 (d3).
408	Pairwise AUC remains high: d0-vs-d1 = 0.999 and d2-vs-d3 = 0.841.
409	These results suggest that distributional artifacts of recursive generation persist across model boundaries, providing preliminary evidence consistent with a process-level depth signal rather than individual generator artifacts.
410	
411	\paragraph{Confound discussion.}
412	The heterogeneous chain confounds architecture identity with depth (d1=Pythia, d2=OLMo, d3=GPT-2~XL).
413	However, if the classifier exploited architecture fingerprints rather than depth signal, near-perfect accuracy would be expected since architecture perfectly determines depth label.
414	The observed 84.75\% with monotonically decreasing per-depth F1 (d0=0.98, d1=0.88, d2=0.76, d3=0.76) is more consistent with a depth-signal interpretation, as architecture fingerprinting would not produce this graded pattern.
415	We address this confound directly with a reverse-chain control below.
416	
417	\paragraph{Reverse-chain control.}
418	To empirically test the architecture confound hypothesis, we constructed a reverse chain (GPT-2~XL $\to$ OLMo $\to$ Pythia) reversing the model-depth assignment.
419	The reverse chain achieves 85.75\% (95\% CI [82.0, 89.25]), statistically indistinguishable from the forward chain (84.75\%, [81.0, 88.25]).
420	If the classifier exploited architecture fingerprints rather than depth signal, reversing the chain should invert depth predictions; the equivalent accuracy under both orderings provides empirical evidence against the architecture confound.
421	
422	\paragraph{Cross-domain transfer.}
423	All prior experiments use WikiText-103 as the seed corpus.
424	To test domain dependence, we repeat the pipeline with arXiv abstracts as the seed text (Pythia-1.4B, nucleus $p{=}0.95$, 500 samples per depth, d0--d3).
425	Five-fold cross-validation yields 74.1\% $\pm$ 2.0\% accuracy, compared to ${\sim}$78\% on the WikiText seed.
426	Per-depth F1 shows the familiar pattern: d0 = 1.00, d1 = 0.78, d2 = 0.52, d3 = 0.66, with d2 remaining the most challenging class.
427	The 4pp accuracy gap relative to WikiText likely reflects the narrower stylistic range of scientific abstracts, which may reduce the distributional contrast between adjacent depths.
428	These results provide preliminary evidence that the perplexity-based features capture properties of the recursive generation process rather than domain-specific artifacts of the seed corpus.
429	
430	\subsection{Cross-Seed Replication}
431	\label{app:seed_replication}
432	
433	Table~\ref{tab:seed_replication} reports within-seed and cross-seed classification accuracy for Pythia-1.4B (nucleus, depths 0--3) under two independent LoRA training seeds.
434	
435	\begin{table}[h]
436	\centering
437	\small
438	\caption{Cross-seed transfer (Pythia-1.4B nucleus). Baseline seed=42 is the primary benchmark LoRA; seed=43 is an independent replication. $\Delta$: difference from respective comparison point.}
439	\label{tab:seed_replication}
440	\begin{tabular}{@{}lcc@{}}
441	\toprule
442	Condition & Acc (\%) & $\Delta$ (pp) \\
443	\midrule
444	Within-seed (seed=42) & 78.20 & --- \\
445	Within-seed (seed=43) & 77.15 & $-$1.05$^\dagger$ \\
446	\midrule
447	Cross-seed (train 42$\to$test 43) & 77.85 & \\
448	Cross-seed (train 43$\to$test 42) & 75.68 & \\
449	Cross-seed avg & 76.76 & $-$1.30$^\ddagger$ \\
450	\bottomrule
451	\multicolumn{3}{@{}l}{\footnotesize $^\dagger$vs.\ baseline (78.20\%). $^\ddagger$vs.\ within-seed avg (78.07\%).}
452	\end{tabular}
453	\end{table}
454	
455	The seed=43 LoRA achieves 77.15\% (95\% CI [76.4, 78.15]), within 1.05\,pp of the seed=42 baseline.
456	Cross-seed transfer averages 76.76\%, a 1.30\,pp deficit relative to within-seed performance.
457	Top-5 feature importance is identical across seeds (\texttt{var\_surprisal}, \texttt{p90\_ppl}, \texttt{mean\_ppl}, \texttt{var\_ppl}, \texttt{p75\_ppl}), confirming that depth signal arises from the recursive process itself rather than idiosyncratic LoRA weight configurations.
458	
459	\subsection{Generation Length Ablation}
460	\label{app:length_ablation}
461	
462	Table~\ref{tab:length_ablation} reports classification accuracy as a function of passage length (Pythia-1.4B nucleus, depths 0--3).
463	
464	\begin{table}[h]
465	\centering
466	\small
467	\caption{Generation length ablation (Pythia-1.4B nucleus, 5-fold CV). Accuracy increases monotonically with passage length; the 9.47\,pp spread confirms that longer passages provide stronger statistical signal.}
468	\label{tab:length_ablation}
469	\begin{tabular}{@{}lc@{}}
470	\toprule
471	Passage length (tokens) & Acc (\%) \\
472	\midrule
473	128 & 68.35 \\
474	256 & 73.80 \\
475	512 & 77.82 \\
476	\bottomrule
477	\end{tabular}
478	\end{table}
479	
480	Depth signal is detectable from 128 tokens (2.7$\times$ chance) and saturates near 500 tokens.
481	The monotonic increase reflects the statistical nature of the features: longer passages yield more stable estimates of perplexity percentiles and surprisal variance, reducing within-class overlap at adjacent depth boundaries.
482	
483	\subsection{Mixed-Depth Corpus}
484	\label{app:mixed_depth}
485	
486	Per-passage classification is largely independent of corpus composition: evaluating on a corpus containing mixed proportions of d0--d3 passages (rather than balanced classes) yields macro-recall $\Delta{=}{-}1.62$\,pp relative to the balanced benchmark (within the 2\,pp tolerance).
487	Individual class deltas range from $-$0.45\,pp to $-$2.43\,pp (d1 shows the largest shift), confirming that the RF classifier operates on per-sample features without sensitivity to the class distribution of the evaluation corpus.
488	Macro-recall $\Delta$ = $-$1.62\,pp (within the 2\,pp threshold); individual class variations (max 2.43\,pp on d1) arise from held-out sample composition rather than classifier sensitivity to corpus distribution, as the Random Forest produces identical per-sample predictions regardless of batch context.
489	
490	\subsection{Extended Discussion}
491	\label{app:extended_discussion}
492	
493	\paragraph{Depth-graduated curation.}
494	Current data curation operates on a binary human-vs-machine distinction \cite{dsir2023,qurating2024}.
495	Recursive generation depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.
496	The 70--85\% in-distribution accuracy and $\mathrm{EDD}_{0.75}{=}4$ suggest depth-graduated filtering is feasible within known model--strategy configurations, though the d1/d2 boundary inversion under cross-strategy transfer (\S\ref{sec:gen:crossstrategy}) means reliable curation requires either known decoding strategy metadata or an upstream strategy-identification step; a pilot study (Appendix~\ref{app:curation_poc}) yields an inconclusive RF-vs-unfiltered comparison ($p>0.4$), though RF-filtered subsets significantly outperform size-matched random subsampling ($p<0.001$--$0.02$); large-scale validation remains open.
497	Importance weighting \cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding.
498	
499	\paragraph{Toward a provenance toolkit.}
500	Depth estimation complements existing provenance methods along orthogonal axes.
501	Watermarking \cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.
502	Source attribution \cite{uchendu2020_attribution} identifies the generating model but not the generation history.
503	Depth estimation characterizes \emph{iterative reuse} regardless of generator cooperation or identity.
504	A layered provenance system combining these three signals (watermark presence, source model, and recursive generation depth) could support more nuanced data auditing than any single method.
505	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "326f83db-f4bc-4f69-87a3-0511eabb86c3",
  "isSidechain": true,
  "promptId": "b457cc73-1371-4047-9c5b-c1b7599b3551",
  "agentId": "a48c96b0a4b83f8d3",
  "type": "user",
  "uuid": "1b482005-d2de-4e7e-8630-cfb8536753b6",
  "sourceToolAssistantUUID": "326f83db-f4bc-4f69-87a3-0511eabb86c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-17T09:03:07.651Z_

Now I have a comprehensive view of the paper. Let me write the review.

---

## Review: "How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints"

### 1. Summary

This paper formalizes "recursive generation depth estimation" as an ordinal classification task, asking how many model-to-data-to-model fine-tuning cycles a passage has undergone. The authors construct a 180K-sample benchmark (3 model families x 3 decoding strategies x 4 depths), extract 19 perplexity-based statistical features from a reference model, and classify with a Random Forest achieving 70-85% four-class accuracy. They introduce the Effective Discriminable Depth (EDD) metric, construct a "Depth Degradation Atlas" showing that perplexity tail statistics dominate across all settings, and characterize generalization along seven axes including cross-model transfer (66.4%), cross-scale (7B models at 60-70%), and cross-domain (arXiv, 74.1%).

### 2. Strengths

- **Clear task formalization with practical motivation.** The distinction between first-generation synthetic text (potentially benign) and deeply recursive text (driving collapse) is well-motivated and genuinely underexplored. The problem statement is crisp and the paper's scope is well-defined.

- **Thorough experimental coverage.** The 3x3 atlas grid, seven generalization axes, multiple ablation studies (seed replication, passage length, reference model, LoRA rank, temperature robustness), and negative results (DCOL, end-to-end learning) demonstrate substantial experimental effort. The paper tests its own assumptions more rigorously than many submissions.

- **Honest reporting of limitations.** The paper transparently reports d0 inflation of headline metrics, the cross-strategy d1/d2 boundary inversion, the reference model dependency, and the inconclusive curation PoC. This intellectual honesty is commendable and helps the reader assess practical applicability.

- **EDD metric is a reasonable contribution.** Formalizing the "how deep can we see" question as a metric with threshold sensitivity analysis is useful. The monotonic AUC decay curves with bootstrap CIs are informative.

- **Feature consistency finding is robust.** The convergence of p90_ppl and var_surprisal as dominant features across 9 cells, confirmed by three importance measures (Gini, SHAP, permutation; Kendall's W=0.90), is the paper's strongest empirical finding.

- **Negative results add value.** The end-to-end learning failure (PLMs at 58-60% vs RF at 78%) with the linear probing explanation (negative R^2 for key features) is informative for the community.

### 3. Weaknesses

**Major:**

- **Limited novelty beyond systematic experimentation.** The core method is Random Forest on perplexity statistics. The features (perplexity quantiles, surprisal moments, lexical diversity, n-gram repetition) are standard in AI-text detection. The paper's novelty rests on applying known tools to a new task formalization, but the formalization itself is a relatively thin conceptual layer over existing model-collapse characterization work. Shumailov et al. (2024) already showed perplexity increases over recursive generations; this paper essentially classifies what depth that perplexity level corresponds to.

- **Ecological validity gap undermines practical claims.** The primary benchmark uses BOS-seeded unconditional generation from 1-1.5B models with LoRA fine-tuning on single-source seed text. Real recursive contamination involves (a) prompted generation, (b) mixed corpora at unknown proportions, (c) models orders of magnitude larger, and (d) diverse fine-tuning objectives. The cross-scale experiments (7B) use QLoRA with only 500 samples per depth, and the 20-22% FPR on C4 web-crawl suggests the method is far from deployable. The paper acknowledges this but continues to frame its contribution as practically relevant for "data curation" and "early warning" of collapse.

- **The "Atlas" is descriptive, not predictive.** Despite the evocative name, the Depth Degradation Atlas is a set of tables and figures describing how features change across a specific experimental grid. It does not provide a predictive model, theoretical framework, or transferable principles beyond "perplexity tail statistics decrease with depth" (already predicted by Dohmatob et al. 2024's scaling laws). The atlas does not generalize to new models/strategies without running the full experimental pipeline again.

- **Cross-strategy transfer is essentially broken for practical use.** Cross-strategy d1-d3 balanced accuracy of 45.9% (chance = 33%) means the method is nearly useless without knowing the decoding strategy a priori. The d1/d2 AUC inversion under temperature (as low as 0.13) is a fundamental limitation, not merely an "interesting finding." The two-stage pipeline claimed in the paper_framing is not actually presented in the paper text beyond mentioning it as future work in Limitations.

- **Scale degradation raises questions about the task's future relevance.** At 7B, accuracy drops to 60-70% (from 70-85% at 1-1.5B), and the authors note "weaker per-step signal." As frontier models grow to 70B+, the perplexity tail erosion that drives discriminability may become undetectable by Pythia-1.4B features. The paper does not adequately address whether its approach has a future.

**Minor:**

- **Reference model circularity.** Using Pythia-1.4B as both a generator and the reference model for feature extraction introduces a theoretical circularity. While the paper shows no systematic self-model advantage, the ablation is limited (only 2 alternative references, one yielding only a table with Pythia and OLMo).

- **d0 is doing heavy lifting.** Near-perfect d0 recall (>98%) inflates all headline metrics. The meaningful task is d1-d3 discrimination, where 3-class accuracy ranges from 58.8% to 82.6%. This should be the primary metric.

- **Limited classifier exploration.** The paper claims RF achieves a "feature-determined ceiling" based on convergence with XGBoost/LightGBM, but this only proves tree ensembles converge, not that the ceiling is absolute. Neural approaches on the same 19 features (e.g., small MLPs with ordinal losses) are not explored.

- **Curation PoC is inconclusive.** The pilot downstream evaluation shows no significant RF-vs-unfiltered difference (p>0.4). Claiming depth-graduated curation as a "practical implication" is unsupported.

### 4. Novelty Assessment

**Is "ordinal generation depth estimation" genuinely new?**
Partially. The task formalization as ordinal classification from text alone is new in the specific sense that no prior paper states this as an explicit classification objective. However, model collapse studies (Shumailov et al. 2024, Dohmatob et al. 2024) already demonstrate depth-dependent degradation curves that are implicitly performing the inverse (measuring features as a function of known depth). This paper inverts the direction (estimating depth from features), but the conceptual leap is modest.

**Is the Depth Degradation Atlas novel?**
It is primarily a systematic experiment, not a methodological contribution. The name "Atlas" suggests a reusable resource, but it is specific to 3 models at 1-1.5B scale with 3 decoding strategies. The main finding (perplexity tails dominate) is predicted by existing theory. The strategy-dependent trajectory finding is genuinely interesting but would not alone justify a full paper.

**Is EDD novel and useful?**
EDD is a clean formalization of an intuitive concept. It has utility within this paper and potentially for future work on recursive generation. However, it is essentially "the last depth where binary AUC exceeds a threshold," which is conceptually simple. Its value depends on whether the task gains traction.

**Are findings surprising given prior work?**
The feature dominance finding (perplexity tails) directly follows from Dohmatob et al.'s (2024) scaling law prediction of tail erosion. The cross-strategy non-transferability is somewhat surprising and is the most novel empirical finding. The end-to-end learning failure is interesting but narrow.

### 5. Related Work Gaps

- **Missing calibrated detector baselines.** Binoculars and Fast-DetectGPT produce continuous scores. These could be calibrated for ordinal depth estimation by binning their output into depth classes or using their scores as features. Not comparing against this obvious baseline is a significant omission.

- **Insufficient coverage of multi-class/fine-grained detection.** The paper cites only binary detectors but does not engage with work on multi-class provenance estimation, source attribution with confidence scores, or text forensics beyond binary classification.

- **Data contamination literature is thin.** Given the practical framing around synthetic data contamination in training corpora, references to FineWeb filtering pipelines (Penedo et al. 2024), DataComp, or other large-scale data quality efforts should be more prominent.

- **~43 references in the literature map but the actual paper appears to cite fewer.** The related work section, while well-organized, is compressed. For EMNLP, expanding the model collapse and detection subsections with 5-10 additional references would strengthen positioning.

- **Missing: Zellers et al. (2019) Grover, RADAR (Hu et al. 2023), and other trained detectors** that could in principle be adapted for ordinal estimation.

- **No engagement with distribution testing literature.** Two-sample tests (MMD, KL divergence estimation) between adjacent-depth corpora would provide a non-ML baseline and connect to statistical testing theory.

### 6. Significance and Impact

The practical impact is unconvincing given the boundary conditions. The method works well in controlled settings (known model, known strategy, same scale, same seed corpus) but degrades substantially under any relaxation. The 20-22% FPR on web-crawl data, the cross-strategy breakdown, and the scale degradation collectively suggest the method is far from deployment-ready.

The scientific contribution is more defensible: characterizing what is and is not detectable about recursive generation from text statistics has value for understanding model collapse. However, the finding that "perplexity statistics capture depth in a controlled setting" is incremental given existing collapse characterization work.

The audience for this work is researchers studying model collapse and synthetic data contamination. For them, the EDD framework and the strategy-dependent trajectory findings are useful additions. The practical data curation community would need substantially more robust methods.

### 7. Presentation Quality

The paper is generally well-written with clear structure. The narrative flows logically from problem statement through method to atlas to generalization. Specific observations:

- The paper is appropriately scoped and does not overclaim (unlike the earlier paper_framing, the actual paper text is measured).
- Tables are informative and well-formatted.
- The Limitations section is unusually thorough, almost preemptively addressing all reviewer concerns, which is both a strength (honesty) and a weakness (it undermines the paper's own claims).
- The title is catchy and appropriate.
- Section 6 (Discussion) is too compressed at 7 lines. The discussion of implications deserves more space.
- The curation PoC being relegated to the appendix with inconclusive results weakens the "practical implication" narrative.

### 8. Questions for Authors

1. Why not include Binoculars or Fast-DetectGPT scores as depth-estimation features (or baselines calibrated for ordinal prediction)? Their perplexity-based scores seem directly relevant.

2. How would you handle the case where a passage has undergone recursive generation by multiple different models at different depths (heterogeneous contamination)? Your cross-model chain experiment uses a fixed sequence; what about unknown/random orderings?

3. Given scale degradation (60-70% at 7B vs 70-85% at 1.5B), do you expect this approach to be viable for detecting depth from frontier models (70B+)? If not, what alternative would you suggest?

4. The d0 separability (>98% recall) suggests the true difficulty is d1-d3 discrimination. Would you consider reframing the paper around the 3-class d1-d3 task, where your results are more honestly represented?

5. Your curation PoC shows RF-filtered is not significantly better than unfiltered. How do you reconcile this with the claim that depth estimation enables "graduated curation"?

### 9. Scores

| Dimension | Score |
|-----------|-------|
| **Overall** | 2.5 |
| **Soundness** | 3.5 |
| **Excitement** | 2.0 |
| **Confidence** | 4.0 |
| **Reproducibility** | 4.0 |

**Justification:** The paper is technically competent with thorough experiments and honest reporting (Soundness 3.5). However, the novelty is limited: the method is standard (RF on perplexity features), the primary finding (perplexity tails capture depth) is predicted by existing theory, and the practical applicability is severely constrained by the boundary conditions the paper itself identifies (Excitement 2.0). The work reads as a careful empirical characterization of a controlled setting that may not generalize to realistic conditions. For EMNLP Main, I would expect either (a) a genuinely novel method, (b) surprising findings that change how we think about the problem, or (c) demonstrated practical utility. This paper partially achieves (b) with the strategy-dependent trajectory finding but falls short on (a) and (c). I recommend this for resubmission with stronger ecological validation or reframing as a Findings-track contribution focused on the empirical characterization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b482005-d2de-4e7e-8630-cfb8536753b6",
  "isSidechain": true,
  "agentId": "a48c96b0a4b83f8d3",
  "requestId": "req_011Cb7sN7JC5yxVs18iiVhh3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc4b0fcf-3602-46d3-b312-6578042a2ab9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1446a884-2136-4659-bcf0-843e85ca00ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9eRSs2nA76Pc11VXLkb34",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10917,
      "cache_read_input_tokens": 56904,
      "output_tokens": 3278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10917
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3278,
          "cache_read_input_tokens": 56904,
          "cache_creation_input_tokens": 10917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10917,
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
