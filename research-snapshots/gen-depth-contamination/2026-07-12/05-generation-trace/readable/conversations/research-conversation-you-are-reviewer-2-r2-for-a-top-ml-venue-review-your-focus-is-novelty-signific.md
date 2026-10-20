# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty, significance, and related work**. Review the

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad50a0cc021cfbc74.jsonl`
- **Structured JSON:** [`bdab214688c38beed77b.json`](../../sessions/bd/bdab214688c38beed77b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-16T08:14:28.274Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty, significance, and related work**. Review the following paper and produce a structured review.

## Paper Summary

**Title**: "Recursive Generation Has a Universal Discrimination Boundary: K*=2 Across Six Architecture Families at 1B–8B Scale"

**Core claim**: Recursive LLM generation can be formalized as an iterated lossy channel via the Data Processing Inequality (DPI). The paper defines an empirical discrimination boundary K* — the maximum generation depth at which adjacent generations remain statistically distinguishable. Through 18 experimental conditions spanning 6 model families, 8 decoding configs, 3 text lengths, and a 4×4 cross-scorer matrix, K*=2 holds in 17/18 conditions (94%).

**Contributions** (as stated):
1. Formalize K* as an operational quantity derived from DPI; first systematic empirical measurement
2. Demonstrate K*=2 universality across 6 architectures at 1B–8B, 8 decoding configs, 3 text lengths, 4×4 cross-scorer matrix (17/18 conditions)
3. Show K*=2 as actionable data curation guideline: binary filtering at K* outperforms graduated weighting and alternatives

**Related Work** (as covered in paper):
- Machine-generated text detection: Solaiman et al. 2019 (perplexity), Mitchell et al. 2023 (DetectGPT, log-rank perturbation), Bao et al. 2024 (Fast-DetectGPT, curvature). Paper says these are binary and don't model recursive depth.
- Model collapse: Shumailov et al. 2024, Alemohammad et al. 2024, Dohmatob et al. 2024. Paper says it complements by characterizing detection-side boundary.
- Data selection: DSIR (Xie et al. 2023), D4 (Tirumala et al. 2024), DoReMi (Xie et al. 2024), Drayson et al. 2025 (binary MGT detection for importance resampling).

**Method details**:
- DPI formalization: recursive generation as Markov chain X0→X1→...→Xk, mutual info non-increasing
- 15D hand-crafted features + LightGBM classifier
- K* defined operationally with θ=0.60 threshold
- 18 experimental conditions, 17/18 yield K*=2
- ANOVA on cross-scorer matrix shows generator dominates (68% variance)
- Downstream validation: binary filtering at K* outperforms graduated weighting (MMLU: 0.5941 vs 0.5892)

**Key results**:
- 6 architecture families: Pythia, OLMo, Qwen-1.5B, Qwen-7B, LLaMA-3.1-8B, Mistral-7B
- Scale: 1B to 8B parameters
- AUC decay pattern: 0v1 > 0.95 universally, 1v2 ∈ [0.61, 0.70], 2v3 < 0.57 universally
- Single exception: OLMo×OLMo self-scorer (K*=1)

## Your Review Task

Evaluate **novelty, significance, and related work** rigorously. Consider:

### Novelty
- Is the K* formalization genuinely novel? Or is it a straightforward application of DPI?
- Is the idea of measuring recursive generation depth new?
- Does the 15D feature + LightGBM approach represent methodological novelty?
- How does this compare to simply running existing detectors (DetectGPT etc.) at multiple depths?

### Significance
- How important is the K*=2 finding for the field?
- Is the practical implication (binary filtering suffices) actually surprising or already assumed?
- Would this change how practitioners build data curation pipelines?
- Is the scale of experiments (max 8B, only continuation mode) sufficient for the strength of claims?

### Related Work
- Are there important missing references? Consider:
  - Watermarking literature (Kirchenbauer et al. 2023)
  - More recent model collapse work
  - Multi-generation detection work if any exists
  - Information-theoretic approaches to LLM analysis
  - Stylometric approaches to authorship/generation detection
- Is the positioning against prior work fair and accurate?
- Does the paper adequately differentiate from Drayson et al. 2025?

### Clarity and Presentation
- Is the paper well-written?
- Are claims appropriately scoped?
- Is the limitation section adequate?

### Output Format

Produce your review in this exact structure:

```
## R2 Review: Novelty, Significance, and Related Work

### Summary
[2-3 sentences]

### Strengths
- S1: ...
- S2: ...
- S3: ...
[up to 5]

### Weaknesses
- W1: ...
- W2: ...
- W3: ...
[up to 7]

### Questions for Authors
- Q1: ...
[up to 5]

### Missing References
- ...

### Scores
- Novelty: [1-4]
- Significance: [1-4]
- Clarity: [1-4]
- Confidence: [1-5]
- Overall recommendation: [1-6 scale, 1=Strong Reject, 6=Strong Accept]
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "7cdf6293-23e2-4f84-8813-1e934e88aa9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T08:14:28.279Z_

```json
{
  "parentUuid": "7cdf6293-23e2-4f84-8813-1e934e88aa9f",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
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
  "uuid": "bf89731e-8da4-45b7-8e33-cc738f1e59ec",
  "timestamp": "2026-05-16T08:14:28.279Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T08:14:31.693Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DmqDVYxtztCPLH8uQRRWJu`</summary>

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
  "parentUuid": "bf89731e-8da4-45b7-8e33-cc738f1e59ec",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5uxkHbGv3MZcekniQK8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfb82f19-153a-4dfa-a9ec-467bef6a5e6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLco15WJNejWB9auqgffSV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7172,
      "cache_read_input_tokens": 8250,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7172
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 88,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7172,
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

_source line 4 · 2026-05-16T08:14:31.697Z_

<details><summary>↩ Tool result · `toolu_01DmqDVYxtztCPLH8uQRRWJu`</summary>

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
  "parentUuid": "dfb82f19-153a-4dfa-a9ec-467bef6a5e6d",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "ad1de239-92b2-42f3-a9d6-cc204feb31b6",
  "sourceToolAssistantUUID": "dfb82f19-153a-4dfa-a9ec-467bef6a5e6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T08:14:35.116Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QSh5kSWikABpxhC7JXr9pR`</summary>

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
  "parentUuid": "ad1de239-92b2-42f3-a9d6-cc204feb31b6",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5uy184fHP1ANRZE2GYH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42e9225c-43c1-4169-91b4-8cd26ffa82c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dewf9fPdmtWMbmtNueYTRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 15422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 6 · 2026-05-16T08:14:35.132Z_

<details><summary>↩ Tool result · `toolu_01QSh5kSWikABpxhC7JXr9pR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_021_length_ablation | 文本长度消融：128/256/512 tokens 下 K* 是否稳定？验证 K*=2 不依赖于 256-token 固定长度设定。Qwen2.5-1.5B (base) continuation, C4 5K, depth 0-5。 | — | — | — |\\n| exp_018_llama8b_depth | Cross-family K* 验证：LLaMA-3.1-8B continuation mode 的 K* 是否 = 2？首次超出 Qwen 家族，验证 K* universality 跨模型架构。C4 5K, depth 0-5, scorer=Qwen2.5-1.5B base。 | — | — | — |\\n| exp_019_mistral7b_depth | Cross-family K* 验证：Mistral-7B-v0.3 continuation mode 的 K* 是否 = 2？第二个非 Qwen 家族模型。C4 5K, depth 0-5, scorer=Mistral-7B-v0.3 (self-scorer)。与 exp-001/002/017 self-scoring 方法一致，exp_A_alt_scorer 已证明 scorer 不影响 K*。 | — | — | — |\\n\\n## 待处理\\n- exp_022_cross_scorer_matrix: 完整 4×4 cross-scorer 矩阵：4 generator (Qwen-rw/Qwen-cont/Pythia/OLMo) × 4 scorer (Qwen-Instruct/Qwen-base/Pythia/OLMo) 的 K* 和 pairwise AUC，量化 self-scoring advantage 并验证 scorer 独立性。（排队等待 GPU）\\n\\n## 近期结论\\n- **exp_016_base_vs_instruct** (success): Base vs Instruct K* 对比：Qwen2.5-1.5B (base) continuation mode 的 K* 是否与 exp-017 (Instruct continuation, K*=2) 一致？封堵 \\\"K*=2 是 instruct-tuning 副产物\\\" 攻击面。唯一变量 = base vs instruct。 ← 基于 exp_017_qwen_continuation\\n  [exp016_bootstrap_ci](/api/workspace-files/projects/gen-depth-contamination/artifacts/exp_016_base_vs_instruct/data/exp016_bootstrap_ci.json)\\n- **exp_003_decoding_ablation** (success): 解码策略调控 K*：不同 top_p/temperature 设置是否改变饱和边界（greedy→更低 K*? 高温度→更高 K*?）\\n  [exp003_config12_analysis](/api/workspace-files/projects/gen-depth-contamination/artifacts/exp_003_decoding_ablation/report/exp003_analysis_report.md) | [exp003_decoding_ablation_figure](/api/workspace-files/projects/gen-depth-contamination/artifacts/exp_003_decoding_ablation/chart/exp003_figure_info.md) | [exp003_bootstrap_ci](westc-26893:/root/autodl-tmp/gen-depth-contamination/artifacts/exp003_bootstrap_ci.json)\\n- **exp_012_binary_confidence** (success): Binary detector confidence (DivEye log-PPL + Binoculars ratio) 与 true depth 的 Spearman correlation，验证 binary confidence ≠ depth。Binoculars: observer=Pythia-1.4b, performer=OLMo-1B-0724-hf。\\n\\n## 趋势\\n成功 21 / 负向 0 / 失败 0 / 共 21\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-22115: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\nwestc-26893: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 2282, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42e9225c-43c1-4169-91b4-8cd26ffa82c1",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "a753fe1d-7af8-4b4f-898b-ffc941740050",
  "sourceToolAssistantUUID": "42e9225c-43c1-4169-91b4-8cd26ffa82c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T08:14:36.158Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PJS8GVGSBAbuWtLnmVpyq6`</summary>

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
  "parentUuid": "a753fe1d-7af8-4b4f-898b-ffc941740050",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5uy184fHP1ANRZE2GYH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0894dde3-8a35-46a9-b22d-fb6c1ff851d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dewf9fPdmtWMbmtNueYTRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 15422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 8 · 2026-05-16T08:14:36.170Z_

<details><summary>↩ Tool result · `toolu_01PJS8GVGSBAbuWtLnmVpyq6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/literature_map.yaml\", \"content\": \"papers:\\n  # === Must-Cite ===\\n\\n  - id: drayson2025\\n    title: \\\"Machine-generated text detection prevents language model collapse\\\"\\n    authors: \\\"Drayson, Yilmaz, Lampos\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n    code: \\\"https://github.com/GeorgeDrayson/model_collapse\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Binary MGT detection + importance resampling for collapse prevention; our depth estimator generalizes their binary detector to ordinal depth\\\"\\n    cited: false\\n    methodology: >\\n      Binary MGT detector (encoder-only transformer + classification head; best: ModernBERT-150M, AUC .986 in-dist, .943 OOD).\\n      Fine-tuned 5 epochs with label smoothing α=0.1 + temperature scaling.\\n      Sampling Importance Resampling (SIR): w_j = (1-q(x_j))^b / Σ(1-q(x_l))^b, where q(x) = P(machine-generated), b≥1 bias term.\\n      Resample at k=1.5 (50% upsampling). Evaluated on GPT-2 and SmolLM2 (124M–1.7B).\\n    key_findings:\\n      - \\\"SIR filtering not only prevents collapse but improves over human-only training (perplexity -0.85% to -25.65%, diversity +3.44% to +14.62%, MAUVE +8.46% to +20.92%)\\\"\\n      - \\\"ModernBERT achieves best detection (AUC .986 in-dist); optimal threshold 0.8674 on imbalanced data (29% human)\\\"\\n      - \\\"Curated synthetic data has positive value — outperforms oracle (perfect filter) in equal-ratio settings\\\"\\n      - \\\"Only evaluates fine-tuning (not pretraining), models ≤2B, open-ended generation only\\\"\\n    positioning_notes: >\\n      Closest prior work. Their SIR is a special case of our graduated filtering when K*=1 (binary: human vs all synthetic).\\n      We generalize binary→ordinal: estimate depth d∈{0,1,...,K*} and apply depth-graduated weights.\\n      K* tells when ordinal signal adds value over binary. They never discuss ordinal depth or multi-class estimation.\\n      Our C3 claim directly extends their framework: \\\"even coarse 3-class signal yields better calibration at decision boundaries.\\\"\\n\\n  - id: schaeffer2025position\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: \\\"Schaeffer, Kazdan, Arulandu, Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2503.03150\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"framing-critical\\\"\\n    relevance: \\\"Identifies 8 definitions of model collapse across 3 families; forces us to position K* as discriminability saturation (distribution deformation), not test-loss collapse\\\"\\n    cited: false\\n    methodology: >\\n      Position paper. Surveys model collapse literature and identifies 8 distinct definitions organized in 3 families.\\n      Evaluates each definition against realistic deployment conditions. No experiments—purely analytical/argumentative.\\n    key_findings:\\n      - \\\"8 definitions in 3 families: (A) Population risk degrading [D1: catastrophic increase, D2: any increase, D3: asymptotic divergence]; (B) Distributions deforming [D4: collapsing variance, D5: scaling law change, D6: mode disappearance/entanglement, D7: tail data loss]; (C) Spurious generation [D8: hallucinated data]\\\"\\n      - \\\"Under realistic conditions (data accumulation, growing compute), catastrophic risk divergence (D1-D3) is avoidable\\\"\\n      - \\\"Real harms—tail data loss (D7) and mode entanglement (D6)—have received disproportionately less attention\\\"\\n      - \\\"Recommends researchers explicitly state which definition they study\\\"\\n    positioning_notes: >\\n      K* belongs to Family B (distributions deforming), specifically D4 (collapsing variance) + D6 (mode entanglement).\\n      K* measures when distribution deformation renders generations indistinguishable in feature space.\\n      K* is NOT about population risk (Family A). This distinction is critical for framing:\\n      we contribute a diagnostic for exactly the harms Schaeffer et al. identify as underexplored.\\n      Adopt their taxonomy explicitly in Related Work to anchor K* precisely.\\n\\n  - id: kazdan2025collapse\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: \\\"Kazdan, Schaeffer, Dey, Gerstgrasser, Rafailov, Donoho, Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2410.16713\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Accumulate vs replace regimes affect contamination dynamics; in accumulate regime K* may shift upward\\\"\\n    cited: false\\n    methodology: >\\n      Formal comparison of 3 data regimes: Replace (train on latest synthetic only; Σ→0 a.s.),\\n      Accumulate (train on all historical data; real fraction→0 but stability holds),\\n      Accumulate-subsample (fixed budget from accumulated pool; intermediate degradation).\\n      Theory: Gaussian setting with closed-form limits. Experiments: multivariate Gaussian, KDE, LLM SFT (Gemma2-2B on HelpSteer2/TinyStories).\\n    key_findings:\\n      - \\\"Replace: covariance collapses to 0 (a.s.), W2 diverges. Collapse inevitable within 5-10 iterations\\\"\\n      - \\\"Accumulate: covariance stabilizes at σ₀²·sin(π/√n)/(π/√n). No collapse even as real data fraction→0\\\"\\n      - \\\"Accumulate-subsample: degradation plateaus rather than diverges\\\"\\n      - \\\"Cardinality of real data matters more than proportion (R²=0.59 vs 0.34)\\\"\\n    positioning_notes: >\\n      Our prompt-chain = replace regime (harshest setting). K*=2 measured under replace conditions.\\n      This makes K*=2 a conservative lower bound: under accumulate regime (more realistic), K* would shift upward.\\n      Strengthens our result: if depth estimation adds value at K*=2 under replace, it adds more under accumulate.\\n      Cite to justify experimental design and contextualize K* as regime-dependent.\\n\\n  - id: shi2025generalization\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: \\\"Shi, Wu, Zhang, Zhang, Tao, Qu\\\"\\n    venue: \\\"NeurIPS 2025 Spotlight\\\"\\n    url: \\\"https://arxiv.org/abs/2509.16499\\\"\\n    code: \\\"https://shilianghe007.github.io/model-collapse/\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Generalization-to-memorization transition in iterative retraining parallels our feature-space convergence; entropy decrease over iterations aligns with our depth-discriminative features\\\"\\n    cited: false\\n    methodology: >\\n      Study iterative retraining of diffusion models (DDPM) on CIFAR-10 subsets (1K–32K images).\\n      Generalization Score (GS): avg distance between generated and nearest training image.\\n      Entropy: Kozachenko-Leonenko estimator. Strong correlation: Pearson r=0.91 between entropy and log(GS).\\n      Mitigation: entropy-based data selection (greedy max-NN-distance + threshold-decay filter).\\n    key_findings:\\n      - \\\"GS drops approximately exponentially across iterations; collapse within 5-10 iterations for large datasets\\\"\\n      - \\\"Training data entropy is a direct predictor of generalization capability (r=0.91)\\\"\\n      - \\\"Entropy-based data selection mitigates memorization transition\\\"\\n      - \\\"Diffusion models only; no LLM experiments. No theoretical analysis of WHY entropy collapses\\\"\\n      - \\\"Generated images form tight local clusters while overall variance remains relatively stable\\\"\\n    positioning_notes: >\\n      Parallel phenomenon across modalities: their entropy decline ↔ our JSD decrease (0.27→0.004).\\n      Their \\\"GS drops exponentially\\\" ↔ our feature-space divergence vanishes rapidly → K*=2.\\n      Key distinction: they measure output-distribution entropy; we measure discriminability in feature space.\\n      K* complements their entropy metric: operationalizes \\\"at what depth does entropy decline = indistinguishability?\\\"\\n      Their clustering-while-variance-stable parallels our depth features converging before global statistics.\\n      Cite for cross-modal validation of convergence phenomenon.\\n\\n  # === Should-Cite ===\\n\\n  - id: basani2026diveye\\n    title: \\\"DivEye: Diversity Boosts AI-Generated Text Detection\\\"\\n    authors: \\\"Basani, Chen\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2509.18880\\\"\\n    code: \\\"https://github.com/IBM/diveye\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Surprisal diversity features as potential baseline for depth estimation; zero-shot detector outperforms prior work by 33.2%\\\"\\n    cited: false\\n\\n  - id: amin2025escaping\\n    title: \\\"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\\\"\\n    authors: \\\"Amin et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2502.08924\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Boosting-inspired framework showing weak signal suffices for iterative training; motivates practical utility of imperfect depth estimators\\\"\\n    cited: false\\n\\n  - id: zawalski2026codec\\n    title: \\\"CoDeC: Detecting Data Contamination in LLMs via In-Context Learning\\\"\\n    authors: \\\"Zawalski et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2510.27055\\\"\\n    category: \\\"contamination\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Binary contamination detection via ICL confidence shifts; complementary to our finer-grained depth estimation approach\\\"\\n    cited: false\\n\\n  - id: gambetta2025surplexity\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse\\\"\\n    authors: \\\"Gambetta et al.\\\"\\n    venue: \\\"arXiv preprint 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2410.12341\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Surprise-based collapse metric; surplexity scores as potential feature for depth estimation pipeline and baseline comparison\\\"\\n    cited: false\\n\\n  - id: zhang2024minkpp\\n    title: \\\"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\\\"\\n    authors: \\\"Zhang, Zheng, Gao, Miao\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Binary detection baseline; does not distinguish generational depth\\\"\\n    cited: false\\n\\n  - id: shumailov2024collapse\\n    title: \\\"AI models collapse when trained on recursively generated data\\\"\\n    authors: \\\"Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal\\\"\\n    venue: \\\"Nature 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Seminal model collapse result; describes macro phenomenon but provides no detection tool for depth\\\"\\n    cited: false\\n\\n  - id: alemohammad2024selfconsuming\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Alemohammad, Casco-Rodriguez, Luber, Babaei, Letizia, Bastani, Baraniuk\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Theoretical and empirical analysis of iterative generative training; complements Shumailov with formal convergence analysis\\\"\\n    cited: false\\n\\n  - id: dohmatob2024model\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: \\\"Dohmatob, Feng, Yang, Charton, Kempe\\\"\\n    venue: \\\"ICML 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Scaling law perspective on collapse; tail distribution loss aligns with our observed feature convergence\\\"\\n    cited: false\\n\\n  - id: xie2023dsir\\n    title: \\\"Data Selection with Importance Resampling\\\"\\n    authors: \\\"Xie, Santurkar, Ma, Liang\\\"\\n    venue: \\\"ICML 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Distribution-matching data selection baseline; does not estimate recursive depth\\\"\\n    cited: false\\n\\n  - id: tirumala2024d4\\n    title: \\\"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\\\"\\n    authors: \\\"Tirumala, Markosyan, Zettlemoyer, Aghajanyan\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Deduplication + diversification baseline for data curation; orthogonal to depth-based filtering\\\"\\n    cited: false\\n\\n  - id: xie2024doremi\\n    title: \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\"\\n    authors: \\\"Xie, Pham, Dong, Du, Liu, Lu, Liang, Le, Ma, Yu\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Domain reweighting for pretraining; does not consider generational depth dimension\\\"\\n    cited: false\\n\\n  - id: kirchenbauer2023watermark\\n    title: \\\"A Watermark for Large Language Models\\\"\\n    authors: \\\"Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein\\\"\\n    venue: \\\"ICML 2023\\\"\\n    category: \\\"watermarking\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Provenance tracking via watermarking; complementary approach to depth estimation when watermarks are available\\\"\\n    cited: false\\n\\n  - id: zellers2019grover\\n    title: \\\"Defending Against Neural Fake News\\\"\\n    authors: \\\"Zellers, Holtzman, Rashkin, Bisk, Farhadi, Roesner, Choi\\\"\\n    venue: \\\"NeurIPS 2019\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Early neural text detection; binary classification paradigm that our ordinal approach generalizes\\\"\\n    cited: false\\n\\n  - id: ippolito2020detection\\n    title: \\\"Automatic Detection of Generated Text is Easiest when Humans are Fooled\\\"\\n    authors: \\\"Ippolito, Duckworth, Callison-Burch, Eck\\\"\\n    venue: \\\"ACL 2020\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Binary detection difficulty analysis; does not consider multi-generational depth\\\"\\n    cited: false\\n\\n  # === New additions (scan 2026-04-28 to 2026-05-14) ===\\n\\n  - id: falahati2026curated\\n    title: \\\"Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences\\\"\\n    authors: \\\"Falahati, Amiri, Larson, Golab\\\"\\n    venue: \\\"arXiv preprint 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2605.07724\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Proves pluralistic reward-based curation prevents collapse via Nash bargaining convergence; directly relevant to our graduated filtering—multi-reward curation is orthogonal to depth-based curation, potentially complementary\\\"\\n    cited: false\\n    date_found: \\\"2026-05-14\\\"\\n    positioning_notes: >\\n      Shows that curation strategy matters for collapse prevention: single-reward collapses, multi-reward stabilizes.\\n      Our depth estimator provides a different curation axis: instead of multiple rewards, we use generational depth.\\n      Potential synergy: combine their pluralistic rewards with our depth signal for even stronger filtering.\\n      Does NOT address generational depth or K*. No direct challenge to K*=2.\\n\\n  - id: mady2026feataugmented\\n    title: \\\"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\\\"\\n    authors: \\\"Mady, Reschke, Schuller\\\"\\n    venue: \\\"arXiv preprint 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2605.03969\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Attention-based linguistic feature fusion for cross-domain/cross-generator binary detection; DeBERTa-v3-base+FeatAttn achieves 85.9% balanced accuracy under distribution shift on M4. Feature augmentation architecture applicable to depth estimation pipeline\\\"\\n    cited: false\\n    date_found: \\\"2026-05-14\\\"\\n    positioning_notes: >\\n      Binary detector (human vs AI) with strong cross-generator generalization via feature augmentation.\\n      Their FeatAttn module could be adapted for our ordinal depth classifier—fuse linguistic features with encoder representations.\\n      Key limitation: binary only, no depth awareness. In-domain 99.5% but brittle under shift.\\n      Our K* result implies even perfect binary detection hits diminishing returns past depth 2.\\n\\n  - id: pu2026generator\\n    title: \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\"\\n    authors: \\\"Pu, Cheng, Yuan, Wu, Bi\\\"\\n    venue: \\\"arXiv preprint 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2604.13692\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Generator-agnostic detection via disentangled representations (dual-bottleneck + cross-view regularization); up to 24.2% accuracy gain on MAGE benchmark (20 LLMs). Disentanglement of semantic vs generator artifacts is architecturally relevant for our depth estimator\\\"\\n    cited: false\\n    date_found: \\\"2026-05-14\\\"\\n    positioning_notes: >\\n      Key insight: separate semantic content from generator-specific artifacts parallels our need to isolate depth signal from generator identity.\\n      Dual-bottleneck architecture enforces compact, minimal latent codes; could inspire our depth encoder design.\\n      Tests on 20 LLMs across 7 categories but only binary classification. No multi-generation or depth estimation.\\n      Our depth estimator needs similar generator invariance: depth signal should hold across model families.\\n\", \"total_chars\": 16560, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0894dde3-8a35-46a9-b22d-fb6c1ff851d3",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "197e07c3-468a-4ba8-9171-b6e94a4769df",
  "sourceToolAssistantUUID": "0894dde3-8a35-46a9-b22d-fb6c1ff851d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T08:14:36.232Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FM3oNvMBZyBscamiVb8Y6v`</summary>

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
  "parentUuid": "197e07c3-468a-4ba8-9171-b6e94a4769df",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5uy184fHP1ANRZE2GYH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31af87c1-f6e9-4842-91a6-3bef78acd64d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dewf9fPdmtWMbmtNueYTRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 15422,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 10 · 2026-05-16T08:14:36.244Z_

<details><summary>↩ Tool result · `toolu_01FM3oNvMBZyBscamiVb8Y6v`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31af87c1-f6e9-4842-91a6-3bef78acd64d",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "070cc489-91b3-4e4a-ba20-6e59fcd52820",
  "sourceToolAssistantUUID": "31af87c1-f6e9-4842-91a6-3bef78acd64d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T08:14:42.716Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KkgFa4MA6eQPU6TqdnGvFP`</summary>

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
  "parentUuid": "070cc489-91b3-4e4a-ba20-6e59fcd52820",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5uyXmJLxvcynPYPKsDD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1241752-b889-44c2-a57b-681771666aee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Xqee2JcLskg1wsgk9sd49",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7559,
      "cache_read_input_tokens": 16691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7559,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 12 · 2026-05-16T08:14:42.737Z_

<details><summary>↩ Tool result · `toolu_01KkgFa4MA6eQPU6TqdnGvFP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-contamination\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\\n- Fallback: EMNLP 2026 Findings\\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\\n\\n## Canonical Experimental Condition\\n\\n**Continuation mode 是 cross-model 结论的基础。**\\n\\n> \\\"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\\\"\\n\\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\\n|-----------|-------------|-------------|---------|\\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\\n\\n**原则**：\\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\\n- mvp-001 (Qwen-rewrite) 定位为 \\\"pilot study demonstrating feasibility\\\"，后续用 continuation mode rigorously validate\\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\\n\\n## Core Claims (2+1 结构, D012)\\n\\n### Primary: C1' (K* Characterization)\\n首次系统测量递归合成文本的 generational discrimination boundary K*，并揭示其 universality。\\n\\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 10 条件实验矩阵（5 model-mode configurations + 4 decoding strategies + 1 cross-scale 7B）系统表征 K*_empirical 的行为，发现 K*=2 在所有 10 个测试条件下保持不变，展现出跨模型架构、跨解码策略、跨生成模式、跨模型规模（1B–7B）、跨 instruct/base 的 universality。\\n\\n**子组件：**\\n\\n**(a) K*=2 universality across architectures, generation modes, and decoding strategies**\\n> **4/4 model-mode configurations 与 4/4 decoding strategies 全部 K*=2：**\\n>\\n> *Model × mode (exp-007):*\\n> | Model | AUC 1v2 | 95% CI | CI lower > 0.60? |\\n> |-------|---------|--------|-----------------|\\n> | Qwen-rewrite | 0.6955 | [0.6859, 0.7041] | ✅ (+8.6pp) |\\n> | Pythia-1.4B | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\\n> | OLMo-1B | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\\n> | Qwen-cont | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp, 最边缘) |\\n>\\n> *Decoding strategy invariance (exp-003):*\\n> | Decoding | AUC 1v2 | K* |\\n> |----------|---------|-----|\\n> | greedy | 0.6893 | 2 |\\n> | nucleus p=0.9 | 0.6866 | 2 |\\n> | temp=0.7 | 0.6887 | 2 |\\n> | temp=1.2 | 0.7039 | 2 |\\n>\\n> - 全部 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60, 全部 permutation p < 0.002\\n> - 4 decoding strategies 的 AUC 1v2 range [0.6866, 0.7039]，K* 完全不变\\n> - K*=2 在所有 10 个测试条件下保持不变（5 model-mode configurations + 4 decoding strategies + 1 cross-scale 7B）\\n> - ⚠️ θ-sensitivity: θ=0.60 下 4/4 K*=2；θ=0.70 下仅 Config4-T12 K*=2（1v2=0.7039 仅超 0.70 阈值 0.004），其余 3 config K*=1。论文以 θ=0.60 为主结论，θ=0.70 边界效应作 footnote\\n> - ⚠️ 特征排序分化: K* 跨 config 稳定，但特征重要性排序不完全一致——Greedy vs T1.2 Spearman=0.53, p=0.041（Bonferroni 校正后阈值 0.0083，不显著）。论文中措辞应为 \\\"suggestive\\\" 而非确定性结论。Config4-T12 正确 top-3 features: hapax_ratio, ttr, surp_skew（非 freq_entropy）\\n> - ⚠️ K*=2 边缘性双端注意: Qwen-cont 1v2 CI lower=0.6015（+0.15pp 高于 θ）+ Qwen-rw 2v3 CI upper=0.5991（-0.09pp 低于 θ），K*=2 边界在两端都极边缘。Discussion/Limitations 需同时提及\\n> - Paper 可写：\\\"K*=2 is established as a consistent discrimination boundary across all 8 tested conditions (4 model-mode configurations and 4 decoding strategies; bootstrap 95% CI for AUC₁ᵥ₂ > 0.60; AUC₂ᵥ₃ CI upper < 0.60), suggesting universality beyond the ≤1.5B scale studied.\\\"\\n> - ⚠️ 措辞策略（D017 Reviewer 评估）：分两层——\\\"established as consistent\\\" 用确定性语言（8/8 有统计检验支撑），\\\"suggesting universality beyond\\\" 对外推 hedging。不升级为 \\\"establishing universal\\\"——3 模型 ≤1.5B 会引发审稿人质疑消耗 rebuttal 预算\\n> - ⚠️ C1' 子组件定位：呈现为\\\"对同一 claim 的 4 个 evidence 维度\\\"而非 4 个独立 finding。§4 标题用 \\\"K* Characterization\\\"，每个子节开头显式回答一个 reviewer concern，子节间用 transitional sentences 链接\\n\\n**(b) Cross-model transfer**\\n> - Pythia↔OLMo 90-92% accuracy retention → K*=2 不是 model self-familiarity artifact\\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\\n> - 1v2+ transfer 取决于模型族相似度 → 与 K*=2 完美一致（K* 之上分辨力本就微弱）\\n> - transfer retention 80-92% suggests depth signal has a large text-intrinsic component（不量化具体比例，因 transfer accuracy retention ≠ 信号分解）\\n> - ⚠️ 数值精度：Pythia→OLMo 91.6%, OLMo→Pythia 90.3%，范围 90-92%（非 91-92%）；Qwen-cont↔Pythia 84.7%/85.2%，范围 84-85%（非 83-85%）\\n\\n**(c) Degradation ordering consistency**\\n> - Spearman ρ ≥ 0.85 on single-feature AUC ranking（mode-controlled, continuation）\\n> - Top discriminative features shared: surp_d1_std, surp_std, surp_d2_std\\n> - Limitation: depth-pair level 一致性在 1v2 处较弱（τ~0.37）\\n> - Metric: single-feature AUC ranking（model-free, not LightGBM split count）\\n\\n**(e) Representation dependence of K* (§4.x Neural Probe / §5.x Discussion)**\\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe, each model probing its own generations）:\\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\\n> - **K*(neural) 不具备 universality**：仅 Qwen-cont 达到 K*=3，Pythia/OLMo 仍为 K*=2\\n> - **Self-familiarity 解释**：每个模型用自己的 frozen embeddings 探测自己生成的文本。Qwen 对 Qwen-generated 文本更敏感（self-familiarity），K*=3 是 model-specific artifact 而非 universal signal\\n> - **K*(theory) ≥ 3 弱化**：只能 claim \\\"K*(theory) ≥ 3 for Qwen representations\\\"，不能泛化为所有模型\\n> - **Interpretability–deployability tradeoff 加强**：15D features 给出 universal K*=2（3/3 模型一致），neural probe 给出 model-dependent K*∈{2,3}。Model-free 方案的 universality 优势在 cross-model 结果下更明显\\n> - 所有 3 模型 neural 2v3 AUC > lgbm 2v3 AUC（+3.9pp 到 +5.5pp），说明 learned representations 确实恢复了额外 depth signal，但不足以在所有模型上推过 θ=0.60\\n> - 论文定位：**正面发现**——cross-model validation 揭示 K*(neural) 是 representation-dependent，验证了选择 model-free 15D features 作为 headline K* characterization 的正确性\\n> - 预防审稿人 \\\"why bury the stronger result?\\\"：K*(neural)=3 仅对 Qwen 成立且是 self-familiarity driven，不适合作为 headline result；15D K*=2 的 universality（10/10 conditions + 3/3 models）才是可靠可部署的结论\\n\\n**(d) Generation mode analysis (§4.x Analysis subsection)**\\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\\n> - 论文定位：Analysis subsection（\\\"How does generation mode affect depth estimation?\\\"），不是独立 claim\\n\\n### Secondary: C3 (K*-Aware Data Curation Validation)\\nK*=2 correctly predicts that graduated refinement beyond the binary boundary provides no additional benefit: binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). K* serves as an actionable curation guideline — the discrimination boundary directly determines the optimal filtering granularity.\\n\\n### Supporting Analysis: Canonical Condition Selection\\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\\n\\n## Story Spine\\n\\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\\\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\\\"。通过 10 条件实验矩阵（5 model-mode configurations + 4 decoding strategies + 1 cross-scale 7B）系统表征 K*，揭示其 universality：**K*=2 在所有 10 个测试条件下不变**，表明递归生成存在一个与具体模型架构和解码策略无关的 universal discrimination boundary。这一发现为数据治理提供 actionable guidance——depth-aware filtering 在 K* 以内有效，且无需针对不同模型或解码配置分别调优。\\n- **Headline result template**: \\\"Recursive generation has a universal discrimination boundary at K*=2: invariant across 4 model-mode configurations, 4 decoding strategies, and 1 cross-scale probe (10 conditions total, 1B–7B scale, base+instruct), with cross-model transfer retention of 80-92% confirming depth features are largely text-intrinsic. K*=2 correctly predicts that graduated refinement beyond the binary boundary provides no additional benefit — binary filtering at K* (0.5941 MMLU) outperforms all tested alternatives including graduated weighting, surprisal selection, and DSIR.\\\"\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n1. **\\\"Universality claim 只基于小模型，能推广到更大模型吗？\\\"** → exp-004 已将规模扩展至 7B（Qwen2.5-7B, continuation mode, scorer=Qwen2.5-1.5B），K*=2 依然成立，bootstrap 95% CI 确认。结合 4 个 ≤1.5B 架构族（GPT-2 style, Pythia, OLMo, Qwen），K*=2 在 1B–7B 范围内稳定。DPI 理论保证 K*_theory 对任意规模模型存在；进一步扩展至 13B+/70B+ 是重要 future work\\n2. **\\\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\\\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ universality 发现，不是分类器本身\\n3. **\\\"Prompt-chain 不代表真实世界递归污染\\\"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法\\n4. **\\\"K*=2 太浅，graduated filtering 收益有限\\\"** → K*=2 恰好预测了这一结果：binary filtering at K* boundary (0.5941 MMLU) outperforms graduated weighting (best 0.5892), surprisal selection (0.5894), and DSIR (~0.5867). 这验证了 K* 作为 actionable curation guideline 的价值——discrimination boundary 直接决定了最优 filtering 粒度。K* 的 universality 意味着实践者无需为每个模型/解码配置单独标定阈值\\n5. **\\\"同模型做生成和 surprisal 计算有 bias\\\"** → **exp-013 直接反驳**：Pythia↔OLMo 90-92% accuracy retention，0v1 transfer AUC > 0.96。Depth signal 主要编码在文本而非 model self-familiarity\\n6. **\\\"为什么不用 learned representations\\\"** → **exp-015 直接回应**：frozen LLM embeddings + MLP probe 达到 K*=3（vs 15D K*=2），揭示 representation-dependent hierarchy: K*_theory ≥ K*_neural ≥ K*_15D。Hand-crafted 15D features 的优势在于 model-free transferability（80-92% cross-model retention）、可解释性（支持 degradation ordering 分析）、实用可部署性。Neural representations 多辨别 1 个深度级别但代价是 model dependence + ~100x 计算开销。这一 tradeoff 证明 15D features 是 practical choice，同时表明 theoretical boundary 延伸至 K*=2 之上\\n7. **\\\"Graduated filtering 没和 data selection methods 比\\\"** → exp-006 包含 DSIR baseline + α sensitivity sweep\\n8. **\\\"Decoding strategy 只测了 4 种，coverage 不够\\\"** → 覆盖了实践中最常见的 decoding 配置（greedy, nucleus sampling, temperature scaling high/low）；4/4 完全一致强化 universality claim；extreme decoding（top-k=1 之外的 pathological 配置）留作 future work\\n9. **\\\"为什么不直接用 LLM 做 depth estimation\\\"** → **exp-011 直接反驳**：GPT-5.5 和 Claude Opus 4.6 在 500 样本 zero-shot 5-class depth 分类上仅 33.1-33.2% accuracy（MAE ~1.1），低于 OBD 15-feature LightGBM 的 38.6%。二者 binary detection 均 ~88%，说明 LLM 能区分 human vs synthetic 但无法估计递归深度。depth estimation 是非平凡任务，需要专用特征工程\\n\\n## Venue Fit\\n\\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with universality finding，C3 是 practical application，generation mode analysis 增加深度\\n- Universality narrative 比 controllability 更有 impact：从 \\\"K* depends on X, Y, Z\\\" 升级为 \\\"K*=2 is a universal boundary\\\"，审稿人更容易记住和传播\\n- 风险：universality claim 在 ≤1.5B 规模下的外推性是最大攻击面 → 论文中 scope 明确、limitation 诚实、DPI 理论支撑泛化的合理性\\n\", \"total_chars\": 11421, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1241752-b889-44c2-a57b-681771666aee",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "ea3ae9bc-8eec-41e7-b655-73d99c8e22e1",
  "sourceToolAssistantUUID": "a1241752-b889-44c2-a57b-681771666aee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T08:14:43.947Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Hmp33zWjGUcMUXBn53NheH`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea3ae9bc-8eec-41e7-b655-73d99c8e22e1",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5uyXmJLxvcynPYPKsDD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d92fd8c8-3089-469c-a227-882e6f81ef46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Xqee2JcLskg1wsgk9sd49",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7559,
      "cache_read_input_tokens": 16691,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7559
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 200,
          "cache_read_input_tokens": 16691,
          "cache_creation_input_tokens": 7559,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7559,
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

_source line 14 · 2026-05-16T08:14:43.964Z_

<details><summary>↩ Tool result · `toolu_01Hmp33zWjGUcMUXBn53NheH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/memory.md\", \"content\": \"# Memory — gen-depth-contamination\\n\\n## 关键发现\\n\\n### Base vs Instruct K* 一致 [2026-05-16, exp-016]\\n- Qwen2.5-1.5B base continuation K*=2，与 exp-017 Instruct continuation K*=2 完全一致\\n- Base 0v1=0.987 略低于 Instruct 0.997——base 生成文本更接近 human（instruct-tuning 增加 stylistic divergence）\\n- Base 1v2=0.626 略高于 Instruct 0.611——base continuation depth 1→2 特征衰减更可分辨\\n- Top features 高度一致（freq_entropy, surp_std, surp_d1_skew 共享 top-3）\\n- **K*=2 不是 instruct-tuning 副产物**——封堵 reviewer 攻击面\\n- K* universality 从 9 → 10 条件\\n\\n### 7B Cross-scale 发现 [2026-05-15, exp-004]\\n- 0v1 AUC = 0.964 是所有模型中最低的（其他模型 0.98-0.998）——expected，7B 更 human-like，生成文本与人类更相似\\n- 1v2 AUC = 0.618 > θ=0.60，K*=2 confirmed。CI lower=0.608>0.60（robust）\\n- **freq_entropy 首次成为 top-1 feature**（其他模型中 surp_* 系列主导）——7B 的 surprise 分布更接近人类，frequency-based feature 反而更有区分力\\n- exp-004 数据生成中断后可 resume：数据生成（depth-by-depth JSONL）与 feature extraction 可解耦恢复，已有 depth 文件不需重跑\\n\\n### W6 Token Length Confound 分析 [2026-05-16, depth_token_length Worker]\\n- **depth 0（人类文本）平均 191 tokens，depth 1+ 为 195-256 tokens**——depth 0 反而更短\\n- 这与 reviewer concern \\\"EOS 截断导致 depth 1+ 短于 depth 0\\\" **方向相反**\\n- 如果长度是 confound，它让 0v1 检测更难（不能靠\\\"更短=机器生成\\\"作弊），不是虚高 AUC\\n- EOS 截断率差异大：Qwen-rewrite 7-11%、Pythia 34-36%、Qwen-7B 45-47%\\n- depth 1-5 之间无系统性递减——长度 confound 不影响 K* 判定\\n\\n### Cross-scorer K* 按 generator data 分裂 [2026-05-15, EXP-A]\\n替代 scorer (Pythia/OLMo) 下：Qwen-RW 数据 → K*=2（AUC 1v2 ~0.70），Qwen-cont 数据 → K*=1（AUC 1v2 ~0.59，未过 θ=0.60）。差异来自 generator data 性质（rewrite mode 信号更强），不是 scorer 选择。Feature importance ρ≥0.90 跨所有 4 条件，确认 scorer 无关性。**叙事影响**：K*=2 限定为 \\\"self-scoring lower bound\\\"，不能 claim universal。与 exp-013 cross-transfer \\\"self-familiarity effect\\\" 一致。\\n\\n### K*(neural probe) 模型相关 [2026-05-15, exp-015 v4 verified]\\nPythia K*_neural=2, OLMo K*_neural=2, Qwen-cont K*_neural=3。Qwen-cont 升高源于 self-familiarity effect（instruction-tuned model 对自身输出的 hidden state 有更丰富的 mode-specific artifacts）。15D hand-crafted features K*=2 universal，更稳健可迁移。\\n\\n### exp-015 GPU OOM 教训 [2026-05-14]\\nexp-006 (15.5GB) + exp-015 (~9GB) 超出 4090D 24GB 显存。**硬规则**: 后续 GPU 并行必须用 `torch.cuda.max_memory_allocated()` 报告 peak VRAM，不用 nvidia-smi 静态快照（低估 peak usage）。GPU 共享实验必须独占，不并行。\\n\\n### Rebuttal 实验汇总 [2026-05-15]\\n- EXP-A (FR-2 Critical): Cross-scorer K*∈{1,2}，按 generator data 分裂。ρ≥0.90 确认 feature ranking stable。\\n- EXP-B (FR-3 Critical): 14D (去 self_BLEU) K*=2 stable across all models。\\n- EXP-C (FR-11): 10K permutation, all boundary p<0.0001。\\n- EXP-D (FR-12): OBD N=500 accuracy=0.380 [0.340, 0.424] > LLMs (0.332/0.331)。\\n- EXP-E (FR-5): Holm-Bonferroni 10/15 MMLU significant, binary-ours significantly best。\\n\\n## 经验\\n\\n### AutoDL / 服务器\\n- ModelScope CDN 下载 HuggingFace 模型比直连快（国内网络）\\n- source /etc/network_turbo 启用代理加速\\n- HF_HUB_DISABLE_XET=1 避免 xet_get 401 错误\\n- SSL 证书需设 REQUESTS_CA_BUNDLE + SSL_CERT_FILE\\n- conda 环境：source /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\n- 服务器别名从 autodl-4090d 改为 westc-26893（exp-003 cron 失败教训）\\n- **westc-26893 实例重启中断 exp-016**（2026-05-16），depth 0-3 已完成的数据可通过 rsync 迁移到新机器断点续跑\\n- **新机器 cqa1-22115**: 4×RTX 4090D 24GB，SSH port 22115\\n\\n### 实验管理\\n- submit_training_job 必须用于后台训练（不用 nohup）——自动 tmux + cron 监控\\n- Registry 状态必须顺序推进：PREPARING → PENDING → QUEUED → ALLOCATED → RUNNING → DONE\\n- GPU 编号始终从 0 开始（框架自动映射物理 GPU）\\n- **exp-006 实际速度 ~45.2min/run**（training 37.5min + eval 7.7min, range 44-49min）。99min 估计是错误的，monitor Worker 从实际 run 时间戳验证 45.2min 正确。\\n- exp-006 lm-eval 配置：batch_size=\\\"auto\\\", device=cuda:0, **MMLU 0-shot + HellaSwag 0-shot**（lm-eval 默认 0），eval 仅占 17% 总耗时 [2026-05-14]\\n- **exp-006 实际目录结构**：输出在 `outputs/exp006/`（非 `runs/exp006_graduated_filtering/`）。6 策略：`no-filter, binary-ours, binary-drayson, graduated, surprisal, dsir`。graduated 用 α∈{0.1,0.3,0.5,0.7,0.9} sweep。eval 结果格式：`scores.mmlu[\\\"acc,none\\\"]`, `scores.hellaswag[\\\"acc_norm,none\\\"]` [2026-05-14]\\n- **Registry DONE→RUNNING 需走完整状态链**：DONE → PREPARING → QUEUED → ALLOCATED → RUNNING（不能直接跳转）。retry_count 自动+1 [2026-05-16]\\n\\n### 论文写作\\n- Claude proxy model ID: 'claude-opus-4-6'（无 anthropic/ 前缀）\\n- 6 处 bib 条目有 hallucinated author first names，需验证所有 2025-2026 引用\\n- Qwen-cont/Qwen-rw 需一致使用 Qwen-continuation/Qwen-rewrite（running text）\\n- 90-92%（非 91-92%）for Pythia↔OLMo transfer retention\\n- discussion.tex 不应量化 \\\"70-85% text-intrinsic / 15-30% model-specific\\\" decomposition——数据不支持精确拆分\\n- Related Work 引用补充完成：probing classifiers (alain2017/conneau2018/belinkov2022/frank2001) + Strong Model Collapse (dohmatob2025) + Beyond Model Collapse (feng2025) + Fast-DetectGPT (bao2024) [2026-05-14]\\n- OBD 全称统一为 \\\"Ordinal Binary Decomposition\\\" [2026-05-14]\\n- $\\\\Kempirical^{\\\\text{neural}}$ 是 neural K* 的统一记号（非 $\\\\Kstar_{\\\\text{neural}}$）[2026-05-14]\\n- Holm-Bonferroni 实现已经 Reviewer 确认正确（EXP-E），不需要修 bug [2026-05-15]\\n- Binoculars performer 模型 ID: allenai/OLMo-1B-0724-hf（非 allenai/OLMo-1B-0724，后者 404）[2026-05-15]\\n\", \"total_chars\": 4760, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d92fd8c8-3089-469c-a227-882e6f81ef46",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "5509403b-663a-4c3e-9f91-c4291b60f24c",
  "sourceToolAssistantUUID": "d92fd8c8-3089-469c-a227-882e6f81ef46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T08:14:48.152Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0189LD2pHVD8ZhgcYm31ffYE`</summary>

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
  "parentUuid": "5509403b-663a-4c3e-9f91-c4291b60f24c",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5uyuP4KSpysMQkAVi27",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "039032ad-e61a-4ede-af86-0731f7ee4a16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4cq6vEFmhGqcCp6QcRCue",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8894,
      "cache_read_input_tokens": 24250,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8894
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 24250,
          "cache_creation_input_tokens": 8894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8894,
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

_source line 16 · 2026-05-16T08:14:48.204Z_

<details><summary>↩ Tool result · `toolu_0189LD2pHVD8ZhgcYm31ffYE`</summary>

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
docs/paper/related_work.tex
docs/paper/experiments_c3.tex
docs/paper/appendix.tex
docs/paper/method.tex
docs/paper/experiments_c1.tex
docs/paper/introduction.tex
docs/paper/appendix_extended.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/discussion.tex
artifacts/dream_reports/dream_20260516T073047/best/paper.tex
artifacts/dream_reports/dream_20260516T073047/median/paper.tex
artifacts/dream_reports/dream_20260516T073047/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "039032ad-e61a-4ede-af86-0731f7ee4a16",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "3f93995a-c072-49a8-863f-ccaa2da6aca9",
  "sourceToolAssistantUUID": "039032ad-e61a-4ede-af86-0731f7ee4a16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T08:14:51.509Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T1t8r7J7Syy6oAc6Zv6S8L`</summary>

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
  "parentUuid": "3f93995a-c072-49a8-863f-ccaa2da6aca9",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5uzDbBdinrqEPFJnV9E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "772634bc-5a6b-4996-9852-f114ea7ce076",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGCWetNiXtWQP89g88kyyM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 534,
      "cache_read_input_tokens": 33144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 534,
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

_source line 18 · 2026-05-16T08:14:51.522Z_

<details><summary>↩ Tool result · `toolu_01T1t8r7J7Syy6oAc6Zv6S8L`</summary>

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
35	We measure the discrimination boundary $\Kempirical$---the maximum depth at which adjacent generations remain distinguishable---using 15 statistical features and an OBD-LightGBM classifier.
36	Across 6 model configurations (1B--7B, base and instruct) and 4 decoding strategies, $\Kempirical{=}2$ at $\theta{=}0.60$ (Cohen's $h{\approx}0.20$), consistent across all 10 tested conditions under self-scoring (most marginal: 0.2\,pp above $\theta$): a single generation step is reliably detectable, but the second renders text statistically indistinguishable from deeper synthetic content---a \emph{one-wash laundering} effect.
37	Model-free statistical features enable 80--92\% cross-model transfer retention among continuation-mode generators with scorer-invariant feature ordering ($\rho > 0.90$), and cross-scorer validation confirms that $\Kempirical$ is governed by the generation process rather than the scoring model.
38	Both supervised classification and zero-shot frontier LLMs fail comparably at depths ${\geq}2$ (recall 14--22\% vs.\ 8--38\%), providing converging evidence consistent with $\Kempirical{=}2$ reflecting a data-intrinsic boundary rather than a method limitation.
39	Downstream, $\Kempirical{=}2$ correctly predicts that binary curation minimizes degradation most effectively among all tested strategies.
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
67	Our findings are bounded by (1)~model scale ($\leq$7B, with only one 7B configuration tested; a dedicated base-vs.-instruct ablation at 1.5B confirms $\Kempirical{=}2$ is independent of instruction tuning, but the 7B condition uses cross-scale scoring rather than self-scoring), (2)~prompt-chain rather than retrain-chain protocols (our $\Kempirical$ is a conservative upper bound on retrain-chain $\Kstar$ under monotonic-degradation assumptions), (3)~English C4 text only, (4)~four decoding strategies, (5)~threshold sensitivity ($\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; all ten conditions yield point-estimate $\Kempirical{=}2$ at $\theta{=}0.60$, with 9/10 confirmed by bootstrap CI---one decoding variant has 2v3 CI upper marginally at 0.601), (6)~marginal boundary (Qwen-continuation 1v2 CI lower bound exceeds $\theta$ by only 0.002; cross-scorer validation with both Pythia and OLMo scorers drops this condition to $\Kempirical{=}1$, Section~\ref{sec:transfer}), (7)~the 15D feature set yields a feature-set-specific lower bound ($\Ktheory$ may be strictly higher), (8)~the neural probe boundary is model-dependent ($\Kempirical^{\text{neural}}{=}3$ for Qwen only; $2$ for Pythia/OLMo), likely reflecting self-familiarity rather than a universal signal, (9)~while overall feature rankings are highly consistent across models ($\rho \geq 0.85$), depth-pair-level agreement weakens at the 1v2 boundary ($\tau \approx 0.37$), indicating that per-feature contributions at the critical boundary vary across models, (10)~cross-model scoring reduces $\Kempirical$ from 2 to 1 for continuation-mode data (Table~\ref{tab:crossscorer}), indicating that the 1v2 boundary signal has a model-specific component consistent with the representation-dependent neural probe finding; in deployment the scorer model is known, making self-scoring the natural choice, but unknown-generator scenarios remain a limitation, (11)~all experiments use 256-token segments matching common web-scale chunking; $\Kempirical$ is defined conditionally on segment length, and longer documents with more stable per-document statistics could yield higher $\Kempirical$, and (12)~structural composition: depth~0 texts are human-authored (mean ${\approx}$191 subword tokens after truncation) while depth~1+ are machine-generated (mean 193--256 tokens depending on model; Table~\ref{tab:token_length}); this length asymmetry makes 0v1 detection \emph{more conservative} (shorter texts provide less feature-extraction context), not inflated, and depths 1--5 exhibit no systematic length trend (within-model range $\leq$ 6 tokens; EOS truncation rates stable across depths within each model), so the critical $\Kempirical{=}2$ finding---based on 1v2 vs.\ 2v3 comparisons---is unaffected by this confound (Section~\ref{sec:length_confound}).
68	Detailed analysis appears in Appendix~\ref{sec:extended_limitations}.
69	
70	% === Ethics Statement (ACL required, unnumbered) ===
71	\section*{Ethics Statement}
72	
73	Generational depth estimation is intended for data curation and corpus auditing---positive-sum applications that improve training data quality.
74	Our experiments use the publicly available C4 corpus and do not involve personally identifiable information.
75	A potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\auc \geq 0.96$ at 0v1) remains robust.
76	
77	\bibliography{references}
78	
79	\input{appendix}
80	\input{appendix_extended}
81	
82	\end{document}
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "772634bc-5a6b-4996-9852-f114ea7ce076",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "a7c3de4a-30f9-4ee6-9992-1c3bc3396797",
  "sourceToolAssistantUUID": "772634bc-5a6b-4996-9852-f114ea7ce076",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T08:14:51.592Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ShybyVbsjefytndWqa7Apg`</summary>

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
  "parentUuid": "a7c3de4a-30f9-4ee6-9992-1c3bc3396797",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5uzDbBdinrqEPFJnV9E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a01045ac-1709-41f2-a3f6-910c62890a87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGCWetNiXtWQP89g88kyyM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 534,
      "cache_read_input_tokens": 33144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 534,
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

_source line 20 · 2026-05-16T08:14:51.598Z_

<details><summary>↩ Tool result · `toolu_01ShybyVbsjefytndWqa7Apg`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, linguistic diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence dynamics~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model}.
6	Our $\Kstar$ aligns with Schaeffer et al.'s Family~B (collapsing variance); our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}, making $\Kempirical = 2$ a conservative lower bound.
7	This literature characterizes macro retrain-chain dynamics but provides no per-text depth estimation---the gap we address.
8	
9	\paragraph{Beyond binary detection.}
10	Binary detectors~\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation; CoDeC~\cite{zawalski2026codec} addresses data contamination via membership inference.
11	Robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}.
12	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}, but no method estimates recursive generation depth.
13	
14	\paragraph{Data selection and curation.}
15	DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling---a special case of our framework when $\Kstar = 1$.
16	Without knowing $\Kempirical$, curation strategies cannot determine whether finer-grained depth weighting adds signal or noise.
17	
18	\paragraph{Ordinal classification and probing.}
19	Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; our neural probe extends the probing protocol~\cite{alain2017understanding, belinkov2022probing} to measure how representation choice affects the discrimination boundary.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a01045ac-1709-41f2-a3f6-910c62890a87",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "23871e7a-5a79-40b9-a6cc-e72433054a5e",
  "sourceToolAssistantUUID": "a01045ac-1709-41f2-a3f6-910c62890a87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T08:14:52.074Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R3vjA3nV7XQdPhkfbgoGU8`</summary>

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
  "parentUuid": "23871e7a-5a79-40b9-a6cc-e72433054a5e",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5uzDbBdinrqEPFJnV9E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1aa2f18-9ee3-4b9f-a575-7bb39650788d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGCWetNiXtWQP89g88kyyM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 534,
      "cache_read_input_tokens": 33144,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 534
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 33144,
          "cache_creation_input_tokens": 534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 534,
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

_source line 22 · 2026-05-16T08:14:52.079Z_

<details><summary>↩ Tool result · `toolu_01R3vjA3nV7XQdPhkfbgoGU8`</summary>

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
17	Together with Markov chain convergence, this guarantees a finite $\Ktheory$ beyond which adjacent generations are indistinguishable.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\{k \geq 1 : \auc_{k-1,k} > \theta\},
22	  \label{eq:kstar}
23	\end{equation}
24	where $\auc_{k-1,k}$ is the point-estimate pairwise AUC and $\theta = 0.60$ corresponds to Cohen's $h \approx 0.20$\footnote{$h = 2\arcsin\!\sqrt{0.60} - 2\arcsin\!\sqrt{0.50} \approx 0.2014$, a ``small'' effect size by Cohen's (1988) convention.} (a conventional small-effect-size threshold), well above the permutation null (95th percentile $< 0.55$).
25	Bootstrap 95\% CIs (1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
26	$\theta{=}0.60$ is justified independently by Cohen's $h \approx 0.20$ and a 10K permutation test ($p < 0.002$); the filtering evaluation (Section~\ref{sec:filtering}) uses the OBD classifier as-is rather than re-optimizing $\theta$, avoiding circularity.
27	$\Kempirical$ varies with $\theta$: at $\theta{=}0.55$, $\Kempirical{=}2$--$3$ depending on configuration ($\Kempirical{=}3$ for Qwen variants, $\Kempirical{=}2$ for Pythia and OLMo); at $\theta{=}0.65$, continuation modes drop to $\Kempirical{=}1$; at $\theta{=}0.70$, $\Kempirical{=}1$ universally (Section~\ref{sec:kstar_boundary}).
28	
29	\subsection{Features and Classifier}
30	\label{sec:features}
31	
32	Each document is characterized by a 15-dimensional feature vector spanning four groups: \emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).
33	All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
34	Self-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.
35	Removing self-BLEU reduces mean $\auc_{1v2}$ by $< 1$\,pp across all models (14D $\Kempirical = 2$ for all 4 configurations); in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss.
36	Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.
37	
38	We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
39	OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression).
40	
41	\subsection{Experimental Setup}
42	\label{sec:experimental_setup}
43	
44	We evaluate six configurations spanning three model families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B (continuation), Pythia-1.4B and OLMo-1B (continuation).
45	Each uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
46	Default decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.
47	Continuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.
48	Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.
49	
50	\begin{table}[t]
51	\centering
52	\small
53	\caption{Experimental configurations.}
54	\label{tab:setup}
55	\begin{tabular}{llcc}
56	\toprule
57	\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
58	\midrule
59	Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\
60	Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\
61	Qwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\
62	Pythia    & Pythia-1.4B            & Continuation & 5{,}000 \\
63	OLMo      & OLMo-1B               & Continuation & 5{,}000 \\
64	Qwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\
65	\bottomrule
66	\end{tabular}
67	\end{table}
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1aa2f18-9ee3-4b9f-a575-7bb39650788d",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "593202a2-3cc0-47d2-9d2d-4e47955d4188",
  "sourceToolAssistantUUID": "a1aa2f18-9ee3-4b9f-a575-7bb39650788d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T08:14:56.573Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GK3JXqx6E1p6RDBmkZkNst`</summary>

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
  "parentUuid": "593202a2-3cc0-47d2-9d2d-4e47955d4188",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5uzWHXWQHo6Ndrdppgb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83168614-a98c-468e-bebc-642b7d89fa4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDLXjyabmd48bPMuU1WCMy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5142,
      "cache_read_input_tokens": 33678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5142,
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

_source line 24 · 2026-05-16T08:14:56.580Z_

<details><summary>↩ Tool result · `toolu_01GK3JXqx6E1p6RDBmkZkNst`</summary>

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
10	The gap cuts across three communities.
11	Binary detection methods~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate, and their confidence scores fail to discriminate beyond the binary boundary (Section~\ref{sec:binary_confidence}).
12	Data contamination detection via membership inference~\cite{zawalski2026codec} addresses a different question (whether specific texts appeared in training data) and likewise provides no depth signal.
13	The model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} characterizes recursive degradation at the macro level but provides no per-text depth estimation tool.
14	Data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.
15	No existing method estimates how many rounds of recursive generation a text has undergone, nor quantifies the boundary beyond which such estimation becomes infeasible.
16	
17	The Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
18	We empirically measure $\Kempirical$---the maximum depth at which a classifier reliably distinguishes adjacent generations---using 15 statistical features and an Ordinal Binary Decomposition (OBD) LightGBM classifier.
19	We operationalize $\Kempirical$ as the deepest $k \geq 1$ where the bootstrap 95\% CI for pairwise $\auc_{k-1,k}$ exceeds $\theta = 0.60$.
20	
21	Our contributions center on two empirical findings:
22	\begin{enumerate}[label=(\alph*),nosep]
23	  \item \textbf{$\Kempirical = 2$ at $\theta{=}0.60$} (Cohen's $h{\approx}0.20$) across 6 model configurations (1B--7B, base and instruct) and 4 decoding strategies, with all 1v2 CI lower bounds exceeding $\theta$ and all 2v3 CI upper bounds below $\theta$ ($p \leq 0.002$; Section~\ref{sec:kstar_boundary}).
24	  Generation mode appears to have a larger effect than model architecture ($+$8.4\,pp rewrite vs.\ continuation within Qwen; $3.9$\,pp spread across continuation-mode models), though formal interaction testing is beyond our current scope.
25	  This is independently corroborated: both supervised OBD and zero-shot frontier LLMs fail comparably at depths $\geq 2$ (McNemar $p > 0.05$), providing converging evidence consistent with $\Kempirical{=}2$ reflecting a data-intrinsic boundary (Section~\ref{sec:why_kstar}).
26	  \item \textbf{Model-free cross-model transfer}: 15 statistical features enable 80--92\% accuracy retention across continuation-mode generators with scorer-invariant feature ordering ($\rho > 0.90$; Section~\ref{sec:transfer}), with surprisal-variance features dominating ($\rho \geq 0.85$).
27	  Cross-scorer validation confirms that $\Kempirical$ is governed by the generation process rather than the scoring model.
28	\end{enumerate}
29	
30	\noindent As a downstream validation, $\Kempirical = 2$ correctly predicts the strategy ordering in data filtering: binary curation at the $\Kempirical$ boundary minimizes degradation most effectively (MMLU $0.5941$ vs.\ base $0.6018$), while graduated ($0.5892$) and surprisal-based ($0.5894$) strategies provide no additional benefit (Section~\ref{sec:filtering}).
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83168614-a98c-468e-bebc-642b7d89fa4a",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "5dcc6f02-132e-4928-b996-3587ca81065f",
  "sourceToolAssistantUUID": "83168614-a98c-468e-bebc-642b7d89fa4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T08:14:56.999Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XGC1zQLPu2ifK1SjL73XNY`</summary>

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
  "parentUuid": "5dcc6f02-132e-4928-b996-3587ca81065f",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5uzWHXWQHo6Ndrdppgb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12997860-7747-4543-be12-2d1f5af95916",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDLXjyabmd48bPMuU1WCMy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5142,
      "cache_read_input_tokens": 33678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5142,
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

_source line 26 · 2026-05-16T08:14:57.018Z_

<details><summary>↩ Tool result · `toolu_01XGC1zQLPu2ifK1SjL73XNY`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on six model configurations:
5	Pythia-1.4B and OLMo-1B in continuation mode, Qwen2.5-1.5B-Instruct in both rewrite and continuation modes, Qwen2.5-1.5B (base) in continuation mode, and Qwen2.5-7B in continuation mode (cross-scale scoring with Qwen2.5-1.5B).
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{$\Kempirical = 2$ Across All Configurations}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.}
17	\label{tab:kstar_ci}
18	\begin{tabular}{lcccccccccc}
19	\toprule
20	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
21	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
22	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
23	\midrule
24	0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] \\
25	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
26	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
27	3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\
28	4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\
29	\bottomrule
30	\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all five 1v2 comparisons.} \\
31	\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}
32	\end{tabular}
33	\end{table*}
34	
35	\begin{figure}[t]
36	\centering
37	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
38	\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\theta = 0.60$.}
39	\label{fig:auc_decay}
40	\end{figure}
41	
42	Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show a consistent pattern: 0v1 discrimination is near-perfect ($\auc \geq 0.96$), followed by a sharp drop at 1v2 ($\auc$: 0.6112--0.6955), with 2v3 falling below $\theta$ (0.5492--0.5893) and deeper pairs converging toward chance.
43	All five 1v2 point estimates exceed $\theta$, confirmed by bootstrap CIs (most marginal lower bound: Qwen-1.5B-continuation at 0.602); all five 2v3 point estimates and CI upper bounds fall below $\theta$ (permutation $p < 0.001$ for all boundary comparisons).
44	This establishes $\Kempirical = 2$ as consistent across all 10 tested conditions (6 independent model-mode configurations and 4 decoding-strategy ablation variants on the Qwen-rewrite configuration; Table~\ref{tab:s2_decoding}).
45	Under cross-model scoring, Qwen-continuation $\Kempirical$ drops to 1 (Section~\ref{sec:transfer}), indicating a model-specific component in the most marginal 1v2 boundary signal.
46	The sharp step-function pattern reflects the concentration of information loss: human text exhibits heavy-tailed, bursty surprisal patterns that are substantially altered by even a single autoregressive pass.
47	Subsequent generations operate on already-smoothed distributions, yielding progressively smaller marginal changes that fall below detectability within two steps.
48	
49	The 1v2 $\auc$ varies across models: Qwen-rewrite (0.6955) $>$ Pythia (0.6539) $>$ OLMo (0.6145) $\approx$ Qwen-continuation (0.6112).
50	The spread due to generation mode within a single model ($\Delta = 8.4$\,pp) exceeds the spread across models in the same mode ($\Delta = 3.9$\,pp), suggesting that generation mode appears to have a larger effect than model architecture, though formal interaction testing is beyond our current scope.
51	
52	\paragraph{Cross-scale validation.}
53	Qwen2.5-7B in continuation mode (scored by Qwen2.5-1.5B) confirms $\Kempirical = 2$: 1v2 $\auc = 0.6168$ $[0.608,\,0.626]$ (CI lower bound $> \theta$), 2v3 $\auc = 0.5492$ $[0.539,\,0.559]$ (Table~\ref{tab:kstar_ci}).
54	The 0v1 $\auc$ drops to 0.9638 (${\sim}$3\,pp below ${\leq}$1.5B models), consistent with larger models generating more human-like text; yet the $\Kempirical$ boundary remains unchanged, extending the invariance from 1.5B to 7B.
55	
56	\paragraph{Base-vs.-instruct ablation.}
57	Qwen2.5-1.5B (base) in continuation mode yields $\Kempirical = 2$: 0v1 $\auc = 0.987$, 1v2 $\auc = 0.626$, 2v3 $\auc = 0.550$ (Table~\ref{tab:setup}).
58	The 0v1 signal is slightly lower than the matched Instruct model ($0.987$ vs.\ $0.997$), consistent with base models producing less stylistically divergent text, but $\Kempirical$ is identical, confirming that the depth boundary is not an instruction-tuning artifact.
59	
60	\begin{figure}[t]
61	\centering
62	\includegraphics[width=\columnwidth]{figures/fig_kstar_theta.pdf}
63	\caption{$\Kempirical$ as a function of $\theta$ across six model-mode configurations, computed using the 95\% CI lower bound criterion (Eq.~\ref{eq:kstar}). The dashed line marks the operational threshold $\theta{=}0.60$ used throughout, where all configurations yield $\Kempirical{=}2$. Qwen-rewrite yields the highest $\Kempirical$ at all $\theta$; at $\theta{=}0.70$, $\Kempirical{=}1$ universally.}
64	\label{fig:kstar_theta}
65	\end{figure}
66	
67	Figure~\ref{fig:kstar_theta} shows $\Kempirical$ as a function of $\theta$ (conservative CI-lower-bound variant): unanimous $\Kempirical = 2$ holds within $\theta \in [0.580, 0.600]$.
68	At $\theta = 0.55$, $\Kempirical = 3$ for Qwen-rewrite and Qwen-continuation while Pythia, OLMo, and Qwen-7B remain at $\Kempirical = 2$; at $\theta = 0.65$, all continuation modes drop to $\Kempirical = 1$ while rewrite retains $\Kempirical = 2$; at $\theta = 0.70$, $\Kempirical = 1$ universally.
69	All four decoding configurations (greedy, nucleus $p{=}0.9$, $T{=}0.70$, $T{=}1.2$) likewise yield $\Kempirical = 2$ at $\theta = 0.60$, with 1v2 $\auc$ in $[0.6866, 0.7039]$ (bootstrap CI lower bounds $\geq 0.677$, all ${>}\theta$; Table~\ref{tab:s2_decoding}).
70	Bootstrap CIs confirm 2v3 upper bounds below $\theta$ for 3/4 decoding variants; the nucleus $p{=}0.9$ condition (2v3 $\auc = 0.5917$, CI $[0.582, 0.601]$) has its upper bound marginally straddling $\theta$ by 0.001, consistent with measurement noise.
71	
72	%% ====================================================================
73	\subsection{Cross-Model Transfer}
74	\label{sec:transfer}
75	
76	\begin{figure}[t]
77	\centering
78	\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
79	\caption{Cross-model transfer heatmap (6-class ordinal accuracy). Pythia$\leftrightarrow$OLMo achieves 90--92\% retention; Qwen-rewrite$\to$continuation-mode models: 61--63\%.}
80	\label{fig:transfer_heatmap}
81	\end{figure}
82	
83	The universality of $\Kempirical = 2$ raises a natural question: does the depth boundary reflect properties of the text itself, or generator-specific artifacts?
84	Cross-model transfer experiments address this directly.
85	
86	Figure~\ref{fig:transfer_heatmap} shows the transfer accuracy matrix (full matrix in Table~\ref{tab:s1_transfer}).
87	Continuation-mode transfer is high: Pythia$\leftrightarrow$OLMo retains 90--92\% of within-model accuracy, Qwen-cont$\leftrightarrow$Pythia 84--85\%, and Qwen-cont$\leftrightarrow$OLMo 80--85\%.
88	At the 0v1 boundary, cross-model $\auc$ exceeds 0.96 for all pairs (range: 0.963--0.991).
89	These retention rates suggest that depth features transfer across generators when computed by a fixed scorer.
90	The high retention indicates that the relative importance of depth features is encoded in distributional text properties---surprisal variance, lexical diversity---rather than in generator-specific fingerprints, enabling generator-agnostic deployment when a consistent scorer is used.
91	
92	Qwen-rewrite classifiers transfer poorly (61--63\% retention to Pythia/OLMo), confirming reliance on mode-specific artifacts.
93	Cross-mode transfer is asymmetric: continuation$\to$rewrite retains 89\% while rewrite$\to$continuation retains 82\%, indicating that continuation-mode features form a generalizable subset.
94	
95	\paragraph{Cross-scorer validation.}
96	To test whether depth signals depend on the scorer model, we replace the Qwen self-scorer with two alternative scorers (Pythia-1.4B, OLMo-1B) for feature extraction on Qwen-generated text.
97	Feature rankings remain highly correlated across all scorer pairs (Spearman $\rho > 0.90$), confirming that feature ordering is text-intrinsic.
98	Absolute discriminability, however, is scorer-sensitive at the $\Kempirical$ boundary.
99	For Qwen-rewrite, $\Kempirical = 2$ is scorer-invariant: 1v2 $\auc$ remains stable under cross-scoring (Pythia: 0.7012, OLMo: 0.6947; self-scorer baseline: 0.6955; Table~\ref{tab:crossscorer}).
100	For Qwen-continuation---already the most marginal self-scorer condition (CI lower bound exceeds $\theta$ by only 0.2\,pp; Table~\ref{tab:kstar_ci})---$\Kempirical$ drops from 2 to 1 under both alternative scorers (1v2 $\auc$: $0.6112 \to 0.5923$ [Pythia], $0.5858$ [OLMo], both below $\theta$).
101	This dissociation---scorer-invariant feature rankings but scorer-sensitive boundary classification---indicates that cross-scoring preserves the relative importance structure of depth features while attenuating the absolute signal, with consequences only where the self-scorer margin is already thin.
102	Crucially, both alternative scorers agree on $\Kempirical$ for each generation mode ($\Kempirical = 2$ for rewrite, $1$ for continuation), indicating that $\Kempirical$ is determined by the generation process rather than the choice of scoring model.
103	
104	%% ====================================================================
105	\subsection{Feature Degradation Ordering}
106	\label{sec:feature_degradation}
107	
108	\begin{table*}[t]
109	\centering
110	\small
111	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
112	\label{tab:top_features}
113	\begin{tabular}{cllll}
114	\toprule
115	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
116	\midrule
117	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
118	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_std}} \\
119	3 & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_d2\_std}} \\
120	\bottomrule
121	\end{tabular}
122	\end{table*}
123	
124	Having established that depth signals transfer across models, we next identify which specific features drive this transferable signal.
125	Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
126	The top-3 features---\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}---are shared across all three families, all measuring surprisal variability.
127	This shared ordering reveals a common mechanism: autoregressive generation progressively damps surprisal variability.
128	\texttt{surp\_d1\_std}---the standard deviation of token-to-token surprisal changes---decreases monotonically with depth as the irregular spikes characteristic of human writing are smoothed out, while \texttt{surp\_std} and \texttt{surp\_d2\_std} reflect the narrowing of the overall surprisal distribution.
129	Qwen-rewrite diverges, with \texttt{freq\_entropy} as its top feature---corroborating the cross-model transfer findings.
130	A limitation is that depth-pair-level agreement weakens ($\tau \approx 0.37$ at 1v2), indicating per-feature contributions at the boundary vary across models.
131	
132	%% ====================================================================
133	\subsection{Generation Mode}
134	\label{sec:generation_mode}
135	
136	The preceding analyses use continuation mode as the default; we now compare generation modes to validate this choice.
137	Within Qwen2.5-1.5B-Instruct, rewrite mode yields 1v2 $\auc = 0.6955$ versus continuation's $0.6112$ ($\Delta = +8.4$\,pp).
138	The amplified detectability reflects instruction-following artifacts that are discriminable but mode-specific rather than transferable across generators, as confirmed by the poor cross-model transfer of rewrite-mode classifiers (61--63\% vs.\ 80--92\% for continuation).
139	Continuation mode is therefore recommended as the canonical condition for cross-model comparisons.
140	
141	%% ====================================================================
142	\subsection{Neural Probe}
143	\label{sec:neural_probe}
144	
145	A natural question is whether $\Kempirical = 2$ is an artifact of our 15-dimensional feature set, or whether richer representations can push the boundary deeper.
146	Replacing hand-crafted features with frozen encoder hidden states (MLP probe; Table~\ref{tab:s7_neural_probe}), we evaluate $\Kempirical^{\text{neural}}$ across all three model families (Table~\ref{tab:neural_probe_crossmodel}).
147	Qwen-continuation achieves 2v3 $\auc = 0.6159$ $[0.610, 0.622]$, yielding $\Kempirical^{\text{neural}} = 3$.
148	However, Pythia ($\auc_{2v3} = 0.5963$ $[0.589, 0.603]$) and OLMo ($\auc_{2v3} = 0.5892$ $[0.582, 0.597]$) both fall below $\theta$, giving $\Kempirical^{\text{neural}} = 2$.
149	The Qwen-only elevation likely reflects self-familiarity: each model's frozen embeddings probe its own generations, and Qwen's instruction-tuned representations encode mode-specific artifacts that boost boundary discrimination---the same artifacts that transfer poorly across model families (Section~\ref{sec:transfer}).
150	The 15D model-free features yield $\Kempirical = 2$ universally (3/3 models), validating their choice for cross-model deployment.
151	
152	\begin{minipage}{\columnwidth}
153	\centering
154	\footnotesize
155	\captionof{table}{Neural probe pairwise $\auc$ with bootstrap 95\% CIs (frozen-encoder MLP). $\Kempirical^{\text{neural}} = 3$ for Qwen only; Pythia and OLMo match the 15D boundary at $\Kempirical^{\text{neural}} = 2$.}
156	\label{tab:neural_probe_crossmodel}
157	\begin{tabular}{lccc}
158	\toprule
159	\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
160	\midrule
161	Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
162	Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
163	OLMo-1B    & 0.5892 & $[0.582,\,0.597]$ & 2 \\
164	\bottomrule
165	\end{tabular}
166	\end{minipage}
167	
168	%% ====================================================================
169	\subsection{Binary Detector Confidence and Depth}
170	\label{sec:binary_confidence}
171	
172	A natural question is whether binary detector confidence---even without ordinal training---implicitly encodes depth information.
173	We evaluate DivEye~\cite{basani2026diveye} (log-PPL) and Binoculars~\cite{hans2024binoculars} (cross-model PPL ratio; observer: Pythia-1.4B, performer: OLMo-1B) across all four model-mode configurations, reporting both Spearman $\rho$ with true depth and 6-class depth classification accuracy.
174	
175	Moderate rank correlations exist ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}), but these do not translate to practical depth discrimination: binary detectors effectively separate human from machine text (0v1 $\auc$: 0.54--0.85, depending on observer-generator matching), but confidence scores collapse to noise for depths $\geq 1$.
176	Six-class accuracy confirms this: most configurations fall at or below the random baseline of 0.167; only Qwen-rewrite (0.199) and Qwen-continuation (0.183) marginally exceed it, while Pythia (0.130) and OLMo (0.127) fall below.
177	Pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$ for most detector--generator pairs: all pairs $\geq$1v2 fall to 0.50--0.60, well below the OBD-15D baseline (0v1 $> 0.99$, 1v2: 0.61--0.70, $\Kempirical = 2$).
178	Multiple conditions exhibit non-monotonic AUC at deeper pairs (e.g., 2v3 $<$ 3v4 $<$ 4v5 for Qwen-continuation), violating the monotonic ordering required for depth interpretation.
179	The observed rank correlation is thus an artifact of 0v1 separation rather than fine-grained depth signal.
180	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12997860-7747-4543-be12-2d1f5af95916",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "4182023d-5cdb-4d40-90f5-2f8cedfcb338",
  "sourceToolAssistantUUID": "12997860-7747-4543-be12-2d1f5af95916",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T08:15:01.375Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GkNBeCdzzXmor6oyj5qyA2`</summary>

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
  "parentUuid": "4182023d-5cdb-4d40-90f5-2f8cedfcb338",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5uzsVjWY3exmB7wjkX6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2ca5558-b525-4a2c-a270-1acc7e642240",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHPn8gQMSpCC3FLQ2RsApE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7499,
      "cache_read_input_tokens": 38820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7499,
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

_source line 28 · 2026-05-16T08:15:01.390Z_

<details><summary>↩ Tool result · `toolu_01GkNBeCdzzXmor6oyj5qyA2`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{The One-Wash Laundering Effect}
5	\label{sec:why_kstar}
6	\label{sec:one_wash}
7	
8	The shallowness of $\Kempirical = 2$ reflects the concentration of information loss: the 0v1 boundary is near-trivially separable ($\auc \geq 0.96$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$---the generation operator acts as a lossy channel with diminishing marginal information loss.
9	Consistency across four decoding strategies (Table~\ref{tab:s2_decoding}) reinforces that $\Kempirical$ is governed by the generation process rather than the sampling algorithm.
10	Even at the most marginal 1v2 condition (Qwen-continuation, CI lower bound exceeds $\theta$ by only 0.2\,pp), $\Kempirical = 2$ survives under self-scoring; on the 2v3 side, CI upper bounds confirm non-discrimination in 9/10 conditions, with the single borderline case (nucleus $p{=}0.9$, CI upper${} = 0.601$) consistent with measurement noise at near-threshold values.
11	Cross-scale validation at 7B (Section~\ref{sec:kstar_boundary}) extends this from 1.5B to 7B despite reduced 0v1 signal ($0.9638$ vs.\ $> 0.99$).
12	
13	The practical consequence is a three-tier taxonomy: human-authored (depth~0), first-generation synthetic (depth~1), and deeper synthetic (depth~$\geq 2$).
14	A single generation pass suffices to render text statistically indistinguishable from multiply recycled content---a \emph{one-wash laundering} effect that limits depth-aware corpus curation to a binary boundary.
15	This connects to model collapse: Shumailov et al.~\cite{shumailov2024collapse} observed that tail-distribution degradation is most acute in the earliest generations; our prompt-chain results show an analogous per-text pattern.
16	
17	Per-depth analysis provides the most direct evidence that this boundary is not methodological.
18	OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 69--77\% depth-0 recall and 8--38\% for depths 2--4 (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).
19	This convergence across fundamentally different approaches---supervised statistical classification and zero-shot frontier LLMs---provides converging evidence that the saturation reflects a data-intrinsic boundary rather than a method limitation.
20	Binary detector confidence corroborates: despite moderate Spearman correlations ($|\rho|$ up to 0.46), 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), and Qwen-rewrite exhibits a sign reversal ($\rho > 0$), disqualifying confidence as a reliable depth proxy.
21	
22	\subsection{Why Graduated Filtering Fails}
23	\label{sec:negative_graduated}
24	
25	Since 2v3 $\auc < \theta$ for all configurations, depth assignments for $d \geq 2$ approximate random labels; graduated weighting injects noise into importance weights, explaining the monotonic improvement with $\alpha$ as it converges toward binary thresholding (Appendix~\ref{sec:extended_limitations}).
26	DSIR fails for a different reason---bigram feature hashing captures domain shift but not depth-correlated distributional signatures.
27	
28	\subsection{Representation Dependence of the Boundary}
29	\label{sec:repr_dependence}
30	
31	$\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$, while Pythia and OLMo match the 15D boundary at $\Kempirical^{\text{neural}} = 2$ (Table~\ref{tab:neural_probe_crossmodel}).
32	The hierarchy $\Kempirical^{15\text{D}}{=}2 < \Kempirical^{\text{neural}} \in \{2,3\}$ reflects an interpretability--sensitivity tradeoff: learned representations recover additional depth signal sufficient to push $\Kempirical$ to 3 for one model (Qwen), but this gain is model-dependent---the 15D features trade one depth level of sensitivity for cross-model universality (10/10 conditions $\Kempirical{=}2$, 3/3 models identical), making them the preferred operational choice.
33	Cross-scorer validation reinforces this: alternative scorers preserve feature rankings ($\rho > 0.90$) but reduce the marginal Qwen-continuation boundary from $\Kempirical = 2$ to 1, while rewrite-mode $\Kempirical = 2$ is preserved---$\Kempirical$ is governed by the generation operator rather than the scoring model.
34	A base-vs.-instruct ablation at 1.5B confirms $\Kempirical{=}2$ is independent of instruction tuning (Section~\ref{sec:kstar_boundary}).
35	A potential length confound is also ruled out: in continuation mode the generation prompt is discarded so all depths $\geq 1$ are purely machine-generated, token counts are stable within depths 1--5 ($\leq$ 6-token range), and the length asymmetry (depth~0 ${\sim}$191 vs.\ depth~1+ 193--256 tokens) makes 0v1 detection more conservative, not inflated (Appendix~\ref{sec:extended_limitations}).
36	\label{sec:length_confound}
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2ca5558-b525-4a2c-a270-1acc7e642240",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "76d51d04-f56e-4a29-a547-3d3c506434bf",
  "sourceToolAssistantUUID": "c2ca5558-b525-4a2c-a270-1acc7e642240",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T08:15:01.792Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E3hZPCXNZowjdoYtt1RPRd`</summary>

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
  "parentUuid": "76d51d04-f56e-4a29-a547-3d3c506434bf",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5uzsVjWY3exmB7wjkX6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59949cab-40d0-47af-8f75-ac2187e35708",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHPn8gQMSpCC3FLQ2RsApE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7499,
      "cache_read_input_tokens": 38820,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7499
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 38820,
          "cache_creation_input_tokens": 7499,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7499,
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

_source line 30 · 2026-05-16T08:15:01.798Z_

<details><summary>↩ Tool result · `toolu_01E3hZPCXNZowjdoYtt1RPRd`</summary>

```text
1	\section{Application: $\Kstar$-Aware Data Filtering}
2	\label{sec:filtering}
3	
4	$\Kempirical = 2$ makes a falsifiable prediction: binary curation should suffice, and graduated performance should converge toward binary as the decay steepness increases.
5	We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} ($w = 1 - P(\text{synthetic})$ from 15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \cdot \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal} (retain above median), and (vi)~\textbf{DSIR}~\citep{xie2023dsir}.
6	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{Downstream filtering performance (5 seeds). Full $\alpha$ sweep and significance tests in Appendix~\ref{sec:extended_limitations}.}
12	\label{tab:tab_filtering_main}
13	\input{tables/tab_filtering_main}
14	\end{table}
15	
16	Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
17	These effects are measured in a 100\% synthetic upper-bound setting; real-world contamination ratios are typically lower, and effect sizes would scale accordingly.
18	The strategy ordering is interpretable through $\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.
19	Graduated filtering converges monotonically toward binary: at $\alpha{=}0.9$, it matches binary-ours on HellaSwag exactly ($\Delta = 0$, $p_{\text{corr}} = 1.00$) but remains significantly worse on MMLU ($p_{\text{corr}} = 0.011$).
20	DSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\ref{fig:filtering_strategies} in Appendix).
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59949cab-40d0-47af-8f75-ac2187e35708",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "68179a8f-0ae0-414d-af04-3488d6593d29",
  "sourceToolAssistantUUID": "59949cab-40d0-47af-8f75-ac2187e35708",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T08:15:04.972Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ji78xH7JUQA94vDaN7hgY8`</summary>

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
  "parentUuid": "68179a8f-0ae0-414d-af04-3488d6593d29",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5v1Dm8doACCCPTjwAL5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ee2d7dc-0b71-48a1-94ae-2301550001b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A41fxkh8Auiqss4cANWtrX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2515,
      "cache_read_input_tokens": 46319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2515,
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

_source line 32 · 2026-05-16T08:15:04.976Z_

<details><summary>↩ Tool result · `toolu_01Ji78xH7JUQA94vDaN7hgY8`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic measurement of the generational depth discrimination boundary $\Kempirical$ for recursive synthetic text.
5	Two primary findings emerge:
6	(a)~$\Kempirical = 2$ at $\theta{=}0.60$ (Cohen's $h{\approx}0.20$), consistent across all tested configurations from 1B to 7B under self-scoring ($p \leq 0.002$; most marginal: 0.2\,pp above $\theta$), implying a one-wash laundering effect.
7	Convergent failure of both supervised classifiers and frontier LLMs at depths $\geq 2$ (McNemar $p > 0.05$) provides converging evidence consistent with this reflecting a data-intrinsic boundary rather than a method limitation.
8	Generation mode appears to have a larger effect than model architecture ($\Delta = 8.4$\,pp), but rewrite-mode advantages are non-transferable (61--63\% vs.\ 80--92\%).
9	(b)~Model-free statistical features enable 80--92\% cross-model transfer retention among continuation-mode generators with scorer-invariant feature ordering ($\rho > 0.90$), with surprisal-variance features dominating across model families ($\rho \geq 0.85$); cross-scorer validation confirms that $\Kempirical$ is governed by the generation process rather than the scoring model, enabling depth estimation for text from unknown generators without retraining.
10	As a downstream validation, $\Kempirical = 2$ correctly predicts the optimal curation granularity: binary filtering minimizes degradation most effectively; finer ordinal structure and depth-agnostic methods (DSIR) provide no benefit.
11	
12	Future work includes scaling beyond 7B, extending to naturalistic multi-domain corpora, and developing model-agnostic neural probes.
13	Our prompt-chain protocol isolates generation-level information loss in a controlled setting; establishing the retrain-chain $\Kstar$ relationship, where training dynamics introduce additional degradation, is a natural next step.
14	The 100\% synthetic filtering experiment characterizes an upper bound; mixed-corpus dose-response studies remain open.
15	Our base-vs.-instruct ablation confirms $\Kempirical{=}2$ is independent of instruction tuning, though broader architecture variation warrants further investigation.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ee2d7dc-0b71-48a1-94ae-2301550001b0",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "4ff3855d-f715-416f-8bc6-7444e7e9749b",
  "sourceToolAssistantUUID": "8ee2d7dc-0b71-48a1-94ae-2301550001b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T08:15:05.429Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G7PTJDZPMpHk6WbdEAVJ6f`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ff3855d-f715-416f-8bc6-7444e7e9749b",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5v1Dm8doACCCPTjwAL5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba2396dd-2375-43e5-838c-5d71369b1cdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A41fxkh8Auiqss4cANWtrX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2515,
      "cache_read_input_tokens": 46319,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2515
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 46319,
          "cache_creation_input_tokens": 2515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2515,
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

_source line 34 · 2026-05-16T08:15:05.436Z_

<details><summary>↩ Tool result · `toolu_01G7PTJDZPMpHk6WbdEAVJ6f`</summary>

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
20	%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)
21	\begin{table*}[t]
22	  \centering
23	  \caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}
24	  \label{tab:s1_transfer}
25	  \begin{tabular}{lcccc}
26	    \toprule
27	    \multirow{2}{*}{\textbf{Train Model}} & \multicolumn{4}{c}{\textbf{Test Model}} \\
28	    \cmidrule(lr){2-5}
29	    & Qwen-rw & Pythia & OLMo & Qwen-cont \\
30	    \midrule
31	    Qwen-rw   & \textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\
32	    Pythia    & 0.2718 & \textbf{0.3856} & 0.3531 & 0.3287 \\
33	    OLMo      & 0.2768 & 0.3450 & \textbf{0.3822} & 0.3244 \\
34	    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \textbf{0.3875} \\
35	    \bottomrule
36	  \end{tabular}
37	  \vspace{4pt}
38	
39	  \footnotesize
40	  \textit{Transfer retention} between models $A$ and $B$ is defined as $\frac{1}{2}\bigl(\frac{\mathrm{acc}(A \to B)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}} + \frac{\mathrm{acc}(B \to A)}{\sqrt{\mathrm{acc}(A \to A) \cdot \mathrm{acc}(B \to B)}}\bigr)$.
41	  Notable pairs: Pythia$\leftrightarrow$OLMo 91--92\%, Qwen-cont$\leftrightarrow$Pythia 83--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\%, Qwen-rw$\to$Pythia/OLMo 61--63\%.
42	\end{table*}
43	
44	%%% Table S2: Decoding Ablation AUC (exp-003)
45	\begin{table*}[t]
46	  \centering
47	  \caption{Pairwise AUC with bootstrap 95\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\,vs.\,2 and 2\,vs.\,3 marks the empirical detectability boundary $\Kempirical=2$. Bottom rows report cross-configuration Spearman $\rho$ on per-feature discriminative-power rankings.}
48	  \label{tab:s2_decoding}
49	  \footnotesize
50	  \begin{tabular}{lcccc}
51	    \toprule
52	    \textbf{Depth Pair} & \textbf{Greedy} & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
53	    \midrule
54	    0 vs.\ 1 & $.980\;[.977,\,.982]$ & $.995\;[.993,\,.996]$ & $.988\;[.986,\,.990]$ & $.998\;[.998,\,.999]$ \\
55	    1 vs.\ 2 & $.689\;[.680,\,.698]$ & $.687\;[.677,\,.695]$ & $.689\;[.680,\,.697]$ & $.704\;[.695,\,.713]$ \\
56	    \cmidrule(lr){1-5}
57	    2 vs.\ 3 & $.561\;[.552,\,.571]$ & $.592\;[.582,\,.601]$\rlap{$^\dagger$} & $.590\;[.581,\,.600]$ & $.582\;[.572,\,.592]$ \\
58	    3 vs.\ 4 & $.540\;[.531,\,.550]$ & $.547\;[.537,\,.557]$ & $.539\;[.529,\,.549]$ & $.529\;[.519,\,.540]$ \\
59	    4 vs.\ 5 & $.514\;[.503,\,.524]$ & $.507\;[.496,\,.517]^{\ddagger}$ & $.535\;[.524,\,.545]$ & $.524\;[.513,\,.535]$ \\
60	    \midrule
61	    \multicolumn{5}{l}{\textbf{Cross-config feature Spearman $\rho$}} \\
62	    \midrule
63	    \multicolumn{2}{l}{Greedy vs.\ Nuc $p{=}0.9$} & 0.600 &
64	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}0.7$} & 0.782 \\
65	    \multicolumn{2}{l}{Greedy vs.\ $T{=}0.7$} & 0.914 &
66	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}1.2$} & 0.893 \\
67	    \multicolumn{2}{l}{Greedy vs.\ $T{=}1.2$} & 0.532 &
68	    \multicolumn{1}{l}{$T{=}0.7$ vs.\ $T{=}1.2$} & 0.668 \\
69	    \bottomrule
70	    \multicolumn{5}{l}{${}^{\dagger}$\,CI upper bound (0.601) marginally exceeds $\theta{=}0.60$ by 0.001.} \\
71	    \multicolumn{5}{l}{${}^{\ddagger}$\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}
72	  \end{tabular}
73	\end{table*}
74	
75	%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)
76	\begin{table*}[t]
77	  \centering
78	  \caption{LLM zero-shot depth classification: $5{\times}5$ confusion matrices
79	    (Exp-011). Both frontier LLMs achieve high binary detection accuracy
80	    (GPT-5.5: 0.8780; Claude Opus~4.6: 0.8818) but near-chance 5-class
81	    accuracy (${\sim}0.33$ vs.\ OBD-LightGBM baseline 0.386, evaluated on the full test set $N{=}5{,}000$). GPT-5.5
82	    strongly identifies depth-0 text (recall${=}0.7700$) but collapses on
83	    depth-4 (recall${=}0.0800$), misclassifying 50/100 depth-4 samples as
84	    depth-2. Claude Opus~4.6 shows more uniform errors across depths 1--4,
85	    with depth-4 recall (0.3700) substantially exceeding GPT-5.5.
86	    Per-depth recall comparison with OBD-LightGBM in Table~\ref{tab:s3c_perdepth}.}
87	  \label{tab:s3_llm_zeroshot}
88	
89	  \vspace{0.5em}
90	  \begin{subtable}{0.48\textwidth}
91	    \centering
92	    \caption{GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)}
93	    \label{tab:s3a_gpt55}
94	    \small
95	    \begin{tabular}{lcccccc}
96	      \toprule
97	      & \multicolumn{5}{c}{Predicted Depth} & \\
98	      \cmidrule(lr){2-6}
99	      True & 0 & 1 & 2 & 3 & 4 & Rec. \\
100	      \midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba2396dd-2375-43e5-838c-5d71369b1cdf",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "10e5ec01-1444-4fac-b9fc-dbd6380fad2a",
  "sourceToolAssistantUUID": "ba2396dd-2375-43e5-838c-5d71369b1cdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-16T08:15:08.540Z_

Now I have a comprehensive understanding of the paper. Let me produce the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10e5ec01-1444-4fac-b9fc-dbd6380fad2a",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5v1VNjwT9YyyATVxbRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33d0b685-05fb-4cfe-82e7-6a3f03f86138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LKBbTk3hfN4TzgevQzMi2W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3607,
      "cache_read_input_tokens": 48834,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3607,
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

_source line 36 · 2026-05-16T08:15:09.244Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PfJtopJPN3WjSKqHRf8T9f`</summary>

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
  "parentUuid": "33d0b685-05fb-4cfe-82e7-6a3f03f86138",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5v1VNjwT9YyyATVxbRe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f40324e-b4cd-4fbb-b5ea-783fe2cfe6ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LKBbTk3hfN4TzgevQzMi2W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3607,
      "cache_read_input_tokens": 48834,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3607
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 48834,
          "cache_creation_input_tokens": 3607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3607,
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

_source line 37 · 2026-05-16T08:15:09.247Z_

<details><summary>↩ Tool result · `toolu_01PfJtopJPN3WjSKqHRf8T9f`</summary>

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
  "parentUuid": "8f40324e-b4cd-4fbb-b5ea-783fe2cfe6ce",
  "isSidechain": true,
  "promptId": "93a6ccff-8c6c-4d04-9121-1e07bf4f1539",
  "agentId": "ad50a0cc021cfbc74",
  "type": "user",
  "uuid": "29945bc8-577e-40a1-8008-fd4c7acb5f1b",
  "sourceToolAssistantUUID": "8f40324e-b4cd-4fbb-b5ea-783fe2cfe6ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-16T08:16:20.488Z_


## R2 Review: Novelty, Significance, and Related Work

### Summary
The paper formalizes recursive LLM generation as an iterated lossy channel, defines an empirical discrimination boundary K* (the maximum depth at which adjacent generations are statistically distinguishable), and measures K*=2 across 18 experimental conditions spanning 6 model families. The downstream implication is that binary filtering (human vs. synthetic) suffices for data curation—graduated depth weighting adds no benefit beyond the K*=2 boundary.

### Strengths
- S1: The K* formalization, while conceptually straightforward from DPI, is a genuinely useful operational definition that bridges information theory and practical data curation. Defining an empirical measurable quantity that directly informs pipeline design decisions is a contribution even if the theoretical grounding is simple.
- S2: The experimental coverage is impressive in breadth: 6 model configurations, 4 decoding strategies, base/instruct ablation, cross-scorer matrix, neural probe, and LLM zero-shot validation all converging on the same result. The convergent evidence from fundamentally different methods (OBD classifier vs. frontier LLMs both failing at depth >= 2) strengthens the claim that K*=2 is data-intrinsic.
- S3: The "one-wash laundering" framing is memorable and has clear practical implications—it gives practitioners a concrete, actionable threshold for data curation decisions.
- S4: Honest reporting of marginality (Qwen-continuation CI lower bound exceeds theta by only 0.2pp; cross-scorer dropping K* to 1) and thorough limitation section with 12 explicit caveats. This is unusually transparent for a paper making a "universality" claim.
- S5: The cross-model transfer analysis (80-92% retention) and cross-scorer validation provide compelling evidence that the depth signal is largely text-intrinsic rather than a scorer artifact.

### Weaknesses
- W1: **Novelty of DPI application is limited.** The Data Processing Inequality guarantees information decay in any Markov chain—this is textbook information theory. The "contribution" is measuring where the empirical boundary falls, but the theoretical framework adds no new insight beyond what any graduate student would derive in an afternoon. The paper acknowledges this implicitly but frames it as a deeper contribution than it is.
- W2: **The universality claim is overstated relative to evidence.** The title claims "Universal Discrimination Boundary" and "Six Architecture Families," but (a) 4 of 6 are <= 1.5B parameters, (b) the single 7B model uses cross-scale scoring rather than self-scoring, (c) the cross-scorer experiment shows K* drops to 1 for continuation mode, and (d) the OLMo x OLMo self-scorer exception (K*=1 in the updated 18-condition framing) undermines universality. The paper essentially shows K*=2 is *common* under self-scoring at small scale, not *universal*.
- W3: **The practical significance of K*=2 is arguably a negative result dressed as a contribution.** If binary filtering suffices (as practitioners likely already assumed given the strength of 0v1 detection), then the entire depth estimation apparatus beyond binary is unnecessary. The paper demonstrates that its own multi-class approach adds no value over simple binary detection—this is informative but limits impact.
- W4: **Scale limitation is severe for the claimed universality.** Max 8B, with only one model above 1.5B. Modern frontier models (70B+, MoE architectures like Mixtral/DeepSeek) may have fundamentally different generation characteristics. The paper's own finding that 7B has lower 0v1 AUC (0.964 vs >0.99) suggests larger models produce more human-like text, potentially shifting K* upward at scale—exactly the regime where universality claims matter most.
- W5: **Methodological novelty is minimal.** 15D hand-crafted features + LightGBM is standard ML engineering. OBD follows Frank & Hall (2001). The features themselves (surprisal moments, TTR, hapax ratio) are well-established in stylometry and MGT detection. There is no novel detection method here—only a novel experimental protocol for measuring something.
- W6: **Prompt-chain vs. retrain-chain ecological validity.** The paper studies prompt-chains (recursive generation without retraining), but the motivating problem is web contamination from retrain-chains (models trained on outputs of earlier models). These are fundamentally different processes. The paper acknowledges this but still draws conclusions about "recursive contamination" broadly. The relationship between prompt-chain K* and retrain-chain K* is entirely uncharacterized.
- W7: **Threshold sensitivity undermines the headline result.** K*=2 holds only at theta=0.60. At theta=0.55, K* varies from 2-3 across models. At theta=0.65, continuation modes all drop to K*=1. The "universal K*=2" is really "at one particular threshold choice, most models happen to agree." The Cohen's h=0.20 justification is post-hoc—there is no principled reason why 0.60 is the "right" threshold for this specific application.

### Questions for Authors
- Q1: Have you computed K* for any model above 8B? Given that 0v1 AUC already drops from 0.99+ to 0.964 at 7B, what is your prediction for 70B+ models? Would K* potentially increase (more information preserved per generation) or remain at 2?
- Q2: The cross-scorer experiment shows K* drops from 2 to 1 for continuation mode under alternative scorers. In real deployment where the generator is unknown, does this not invalidate the K*=2 claim for the most practically relevant scenario?
- Q3: Could you run existing binary detectors (DetectGPT, Fast-DetectGPT, Binoculars) on generation-1 vs generation-2 text to confirm they also fail? This would more directly establish that K*=2 is not specific to your feature set. The binary confidence analysis (Section 4.5) shows these detectors have K*<=1, which actually contradicts rather than supports your K*=2 claim—it means your 15D features are doing something that existing methods cannot, undermining the "data-intrinsic boundary" interpretation.
- Q4: The downstream validation shows binary-ours achieves MMLU 0.5941 vs base 0.6018—a degradation of -0.77pp. Is this practically meaningful? The absolute differences between strategies (binary 0.5941 vs graduated 0.5892 = 0.49pp) seem within noise for a 5-seed evaluation. Are these differences robust to more seeds or different downstream tasks?
- Q5: How sensitive is K*=2 to the choice of seed corpus? C4 is a specific distribution. Would K* differ for code, dialogue, scientific text, or other domains with different surprisal characteristics?

### Missing References
- **Watermarking as provenance tracking**: Kirchenbauer et al. 2023 ("A Watermark for Large Language Models") is in the literature map but apparently not cited in the paper. Watermarking provides an alternative approach to generational tracking when available, and the relationship between watermark degradation across generations and K* is a natural connection.
- **Information-theoretic bounds on LLM generation**: Meister et al. 2023 ("Locally Typical Sampling" / information-theoretic characterization of decoding) and related work on entropy/information constraints in generation—relevant to the DPI framing.
- **Stylometric authorship analysis**: Extensive literature on stylometric features for authorship attribution (Stamatatos 2009, Neal et al. 2017) that uses similar features (TTR, hapax, etc.) for distinguishing writing styles. The 15D feature set heavily overlaps with this tradition but is not positioned against it.
- **Multi-turn generation analysis**: Li et al. 2024 ("Self-play fine-tuning") and other work studying how text properties change across iterative generation rounds—not identical but related.
- **Gerstgrasser et al. 2024** ("Is Model Collapse Inevitable?") appears in the related work citation list but deserves explicit positioning since it argues collapse is NOT inevitable under certain conditions, directly relevant to K*.
- **Feng et al. 2025** ("Beyond Model Collapse") is mentioned in the memory as added to related work but should be explicitly discussed for how it relates to the K* boundary.

### Scores
- Novelty: 2
- Significance: 2
- Clarity: 3
- Confidence: 4
- Overall recommendation: 3 (Weak Reject)

**Justification**: The paper is well-executed and clearly written, with thorough experiments and honest limitations. However, the core novelty is primarily empirical measurement rather than methodological or theoretical innovation. The DPI formalization is elementary, the features/classifier are standard, and the main finding (K*=2, binary suffices) is arguably predictable given the known strength of 0v1 detection and rapid convergence of generative Markov chains. The "universality" claim is overclaimed relative to the scale and diversity of models tested. The practical implication—use binary filtering—is what most practitioners already do. The paper would benefit from (a) scaling to 70B+ to truly test universality, (b) retrain-chain experiments to validate ecological relevance, and (c) a more honest framing as a careful empirical study rather than a universal law discovery.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29945bc8-577e-40a1-8008-fd4c7acb5f1b",
  "isSidechain": true,
  "agentId": "ad50a0cc021cfbc74",
  "requestId": "req_011Cb5v1meXosUdx4RyGDYrQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "325c8ff8-2e96-4adb-90d8-f8cc47a9105a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "f435afbf-9516-4ae9-a254-af07d6e2235e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9x9jZBgttPUXX8owMBT5j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 684,
      "cache_read_input_tokens": 52441,
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
