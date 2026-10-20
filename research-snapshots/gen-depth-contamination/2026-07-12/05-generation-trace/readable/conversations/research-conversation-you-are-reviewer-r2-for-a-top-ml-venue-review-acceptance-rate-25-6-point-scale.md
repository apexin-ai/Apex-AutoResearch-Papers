# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a8d7b6cd5cd8fadb4.jsonl`
- **Structured JSON:** [`87723dff754637ccb561.json`](../../sessions/87/87723dff754637ccb561.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

50 recorded events

### User

_source line 1 · 2026-05-13T08:54:44.960Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus is **Novelty and Related Work**.

## Paper Summary

Title: "Measuring the Generational Discrimination Boundary in Recursively Contaminated Text"

The paper formalizes recursive text generation as an iterated lossy channel, derives from the Data Processing Inequality (DPI) that a finite "generational discrimination boundary" K* must exist, and empirically measures K*=2 under nucleus sampling at the 1.5B scale. They use 15D hand-crafted features (surprisal, lexical diversity, structural) with a LightGBM ordinal classifier. Three claims:
- C1: K*=2 across 4 model configs, stable from 1.5B→7B, sensitive to base/instruct variant
- C2: Cross-model transfer retains 91% accuracy (Pythia↔OLMo); degradation orderings consistent (ρ≥0.82)
- C3: Graduated filtering yields modest +0.6pp at 30% contamination (p=0.08), +1.1pp at 50% (p=0.038); DSIR matches without depth estimation

## Paper Structure (8 pages)
- §1 Introduction: Problem setup, contributions
- §2 Related Work: Model collapse (Shumailov et al. 2024, Alemohammad et al. 2024, Dohmatob et al. 2024), binary detection (DetectGPT, DNA-GPT, DivEye, Binoculars), data selection (DSIR, D4, DoReMi), Drayson et al. (2025) as closest prior work
- §3 Method: DPI theory (§3.1), 15D features (§3.2), K* measurement (§3.3), graduated filtering (§3.4)
- §4 Characterization: K* across configs, cross-scale, base/instruct, cross-model transfer, degradation ordering, generation mode analysis
- §5 Application: Filtering comparison, dose-response
- §6 Supporting: Retrain-chain, LLM zero-shot, binary confidence proxy, learned representations, Common Crawl validation
- §7 Conclusion + Limitations

## Key Claims and Evidence
- The paper argues K* is "the core missing quantity" — the max depth at which adjacent generations are statistically distinguishable
- DPI provides theoretical guarantee that K* must be finite
- Empirically K*=2 under nucleus sampling at 1.5B scale
- Cross-model transfer (91% retention) shows depth signal is "text-intrinsic" not model-specific
- Binary detector confidence is a poor depth proxy (ρ≤0.22 vs their ρ=0.55)
- LLMs at zero-shot achieve near-chance on depth estimation (3-class ~37% vs chance 33%)
- Learned representations beat 15D features by ~5pp — paper argues interpretability-performance tradeoff
- Graduated filtering advantage is modest and DSIR matches it — paper honestly repositions as "scientific characterization" over "engineering advantage"

## Related Work Context
- Model collapse: Shumailov et al., Alemohammad et al., Dohmatob et al. — theoretical and empirical characterization of distributional collapse, but no detection tools
- Binary detection: DivEye, Binoculars, DetectGPT, DNA-GPT — real/synthetic binary classification, no depth
- Drayson et al. (2025): binary confidence for importance resampling — closest prior work
- Data selection: DSIR, D4, DoReMi — distribution matching without depth awareness
- The paper references a missing citation in the introduction (visible as "?" in the PDF)

## Your Task

Produce a structured review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (novelty, positioning, related work coverage)
3. **Weaknesses** (novelty, positioning, related work gaps)
4. **Detailed Comments** — evaluate:
   - Is the K* concept genuinely novel, or a straightforward application of DPI to an obvious measurement?
   - Is the "iterated lossy channel" framing a meaningful theoretical contribution or just a motivation?
   - How well does the paper differentiate from Drayson et al. (2025)?
   - Are there missing related works? (e.g., iterative generation quality studies, text quality metrics, multi-class synthetic detection)
   - Is the paper honest about the limited practical advantage (C3 weakness, DSIR matching)?
   - Does the "scientific characterization" positioning hold up as a sufficient contribution for a top venue?
   - The paper has a missing citation ("?") in the introduction — flag this
   - How does the ~5pp gap to learned features affect the contribution narrative?
   - Is the scope (1.5B-7B, nucleus only) too narrow for the claims made?
5. **Questions for Authors** (3-5 specific questions)
6. **Score** (1-6) and **Confidence** (1-5)

Be rigorous but fair. Evaluate whether this paper makes a sufficient contribution for a top ML venue with ~25% acceptance rate. The bar is: does the community learn something non-obvious and useful?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "d48202a5-4c0a-4aef-b507-726db260f248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T08:54:44.963Z_

```json
{
  "parentUuid": "d48202a5-4c0a-4aef-b507-726db260f248",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
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
  "uuid": "2ad5f0e8-35d2-4512-bc4b-fe4e4db7b4b5",
  "timestamp": "2026-05-13T08:54:44.963Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T08:54:48.164Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ad5f0e8-35d2-4512-bc4b-fe4e4db7b4b5",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHc9M7xGMDCg1NtjqVb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7156f0a5-217e-4e39-9c35-fec3e22cc36f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TGPTdioS8obKriRqJkruUa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7117,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7117,
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

_source line 4 · 2026-05-13T08:54:48.972Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SLDT21jGBoL2xN3q8Cs7uY`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7156f0a5-217e-4e39-9c35-fec3e22cc36f",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHc9M7xGMDCg1NtjqVb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d093e38-ec81-4b02-a49f-1ce6eec851e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TGPTdioS8obKriRqJkruUa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7117,
      "cache_read_input_tokens": 8250,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7117
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 141,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7117,
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

_source line 5 · 2026-05-13T08:54:48.976Z_

<details><summary>↩ Tool result · `toolu_01SLDT21jGBoL2xN3q8Cs7uY`</summary>

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
  "parentUuid": "3d093e38-ec81-4b02-a49f-1ce6eec851e2",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "7ddbfb73-ab0e-427b-9472-3d38e1fd6b2a",
  "sourceToolAssistantUUID": "3d093e38-ec81-4b02-a49f-1ce6eec851e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T08:54:55.991Z_



Let me read the key project files to understand the paper in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ddbfb73-ab0e-427b-9472-3d38e1fd6b2a",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHcShQHhpEDCVTCTAbz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f27eb34-7b91-41db-a877-aa3ff298954d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DB6cqLM9gFNHM8CcFnLnto",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2015,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T08:54:56.470Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Bq7aaMT5Ee34uh74EdPAgQ`</summary>

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
  "parentUuid": "2f27eb34-7b91-41db-a877-aa3ff298954d",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHcShQHhpEDCVTCTAbz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32c669ac-fa3e-41f4-b223-aa799aac6a2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DB6cqLM9gFNHM8CcFnLnto",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2015,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T08:54:56.487Z_

<details><summary>↩ Tool result · `toolu_01Bq7aaMT5Ee34uh74EdPAgQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_003_decoding_ablation | 解码策略调控 K*：不同 top_p/temperature 设置是否改变饱和边界（greedy→更低 K*? 高温度→更高 K*?） | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_013_cross_transfer** (success): Depth signal 是文本固有属性还是 model self-familiarity artifact？4×4 cross-model transfer matrix 测试分类器跨模型泛化能力\\n- **exp_005_degradation** (success): —\\n  [exp005_degradation_analysis](autodl-4090d:/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/degradation_analysis.json)\\n- **exp_007_bootstrap_ci** (success): K* 统计严谨性验证：bootstrap 95% CI 和 permutation test 确认 K*=2 在三个模型族上统计显著\\n\\n## 趋势\\n成功 8 / 负向 0 / 失败 0 / 共 8\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-4090d: 空闲 cuda:0\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 811, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32c669ac-fa3e-41f4-b223-aa799aac6a2c",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "a96f61dc-158d-4fec-a97e-b96d9f90783a",
  "sourceToolAssistantUUID": "32c669ac-fa3e-41f4-b223-aa799aac6a2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T08:54:57.718Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014H2k7fBFdFAaRAX4bLszbq`</summary>

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
  "parentUuid": "a96f61dc-158d-4fec-a97e-b96d9f90783a",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHcShQHhpEDCVTCTAbz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "875a80ed-6090-4921-a9dc-ff9715edc364",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DB6cqLM9gFNHM8CcFnLnto",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2015,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T08:54:57.737Z_

<details><summary>↩ Tool result · `toolu_014H2k7fBFdFAaRAX4bLszbq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/literature_map.yaml\", \"content\": \"papers:\\n  # === Must-Cite ===\\n\\n  - id: drayson2025\\n    title: \\\"Machine-generated text detection prevents language model collapse\\\"\\n    authors: \\\"Drayson, Yilmaz, Lampos\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n    code: \\\"https://github.com/GeorgeDrayson/model_collapse\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Binary MGT detection + importance resampling for collapse prevention; our depth estimator generalizes their binary detector to ordinal depth\\\"\\n    cited: false\\n    methodology: >\\n      Binary MGT detector (encoder-only transformer + classification head; best: ModernBERT-150M, AUC .986 in-dist, .943 OOD).\\n      Fine-tuned 5 epochs with label smoothing α=0.1 + temperature scaling.\\n      Sampling Importance Resampling (SIR): w_j = (1-q(x_j))^b / Σ(1-q(x_l))^b, where q(x) = P(machine-generated), b≥1 bias term.\\n      Resample at k=1.5 (50% upsampling). Evaluated on GPT-2 and SmolLM2 (124M–1.7B).\\n    key_findings:\\n      - \\\"SIR filtering not only prevents collapse but improves over human-only training (perplexity -0.85% to -25.65%, diversity +3.44% to +14.62%, MAUVE +8.46% to +20.92%)\\\"\\n      - \\\"ModernBERT achieves best detection (AUC .986 in-dist); optimal threshold 0.8674 on imbalanced data (29% human)\\\"\\n      - \\\"Curated synthetic data has positive value — outperforms oracle (perfect filter) in equal-ratio settings\\\"\\n      - \\\"Only evaluates fine-tuning (not pretraining), models ≤2B, open-ended generation only\\\"\\n    positioning_notes: >\\n      Closest prior work. Their SIR is a special case of our graduated filtering when K*=1 (binary: human vs all synthetic).\\n      We generalize binary→ordinal: estimate depth d∈{0,1,...,K*} and apply depth-graduated weights.\\n      K* tells when ordinal signal adds value over binary. They never discuss ordinal depth or multi-class estimation.\\n      Our C3 claim directly extends their framework: \\\"even coarse 3-class signal yields better calibration at decision boundaries.\\\"\\n\\n  - id: schaeffer2025position\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: \\\"Schaeffer, Kazdan, Arulandu, Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2503.03150\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"framing-critical\\\"\\n    relevance: \\\"Identifies 8 definitions of model collapse across 3 families; forces us to position K* as discriminability saturation (distribution deformation), not test-loss collapse\\\"\\n    cited: false\\n    methodology: >\\n      Position paper. Surveys model collapse literature and identifies 8 distinct definitions organized in 3 families.\\n      Evaluates each definition against realistic deployment conditions. No experiments—purely analytical/argumentative.\\n    key_findings:\\n      - \\\"8 definitions in 3 families: (A) Population risk degrading [D1: catastrophic increase, D2: any increase, D3: asymptotic divergence]; (B) Distributions deforming [D4: collapsing variance, D5: scaling law change, D6: mode disappearance/entanglement, D7: tail data loss]; (C) Spurious generation [D8: hallucinated data]\\\"\\n      - \\\"Under realistic conditions (data accumulation, growing compute), catastrophic risk divergence (D1-D3) is avoidable\\\"\\n      - \\\"Real harms—tail data loss (D7) and mode entanglement (D6)—have received disproportionately less attention\\\"\\n      - \\\"Recommends researchers explicitly state which definition they study\\\"\\n    positioning_notes: >\\n      K* belongs to Family B (distributions deforming), specifically D4 (collapsing variance) + D6 (mode entanglement).\\n      K* measures when distribution deformation renders generations indistinguishable in feature space.\\n      K* is NOT about population risk (Family A). This distinction is critical for framing:\\n      we contribute a diagnostic for exactly the harms Schaeffer et al. identify as underexplored.\\n      Adopt their taxonomy explicitly in Related Work to anchor K* precisely.\\n\\n  - id: kazdan2025collapse\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: \\\"Kazdan, Schaeffer, Dey, Gerstgrasser, Rafailov, Donoho, Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2410.16713\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Accumulate vs replace regimes affect contamination dynamics; in accumulate regime K* may shift upward\\\"\\n    cited: false\\n    methodology: >\\n      Formal comparison of 3 data regimes: Replace (train on latest synthetic only; Σ→0 a.s.),\\n      Accumulate (train on all historical data; real fraction→0 but stability holds),\\n      Accumulate-subsample (fixed budget from accumulated pool; intermediate degradation).\\n      Theory: Gaussian setting with closed-form limits. Experiments: multivariate Gaussian, KDE, LLM SFT (Gemma2-2B on HelpSteer2/TinyStories).\\n    key_findings:\\n      - \\\"Replace: covariance collapses to 0 (a.s.), W2 diverges. Collapse inevitable within 5-10 iterations\\\"\\n      - \\\"Accumulate: covariance stabilizes at σ₀²·sin(π/√n)/(π/√n). No collapse even as real data fraction→0\\\"\\n      - \\\"Accumulate-subsample: degradation plateaus rather than diverges\\\"\\n      - \\\"Cardinality of real data matters more than proportion (R²=0.59 vs 0.34)\\\"\\n    positioning_notes: >\\n      Our prompt-chain = replace regime (harshest setting). K*=2 measured under replace conditions.\\n      This makes K*=2 a conservative lower bound: under accumulate regime (more realistic), K* would shift upward.\\n      Strengthens our result: if depth estimation adds value at K*=2 under replace, it adds more under accumulate.\\n      Cite to justify experimental design and contextualize K* as regime-dependent.\\n\\n  - id: shi2025generalization\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: \\\"Shi, Wu, Zhang, Zhang, Tao, Qu\\\"\\n    venue: \\\"NeurIPS 2025 Spotlight\\\"\\n    url: \\\"https://arxiv.org/abs/2509.16499\\\"\\n    code: \\\"https://shilianghe007.github.io/model-collapse/\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Generalization-to-memorization transition in iterative retraining parallels our feature-space convergence; entropy decrease over iterations aligns with our depth-discriminative features\\\"\\n    cited: false\\n    methodology: >\\n      Study iterative retraining of diffusion models (DDPM) on CIFAR-10 subsets (1K–32K images).\\n      Generalization Score (GS): avg distance between generated and nearest training image.\\n      Entropy: Kozachenko-Leonenko estimator. Strong correlation: Pearson r=0.91 between entropy and log(GS).\\n      Mitigation: entropy-based data selection (greedy max-NN-distance + threshold-decay filter).\\n    key_findings:\\n      - \\\"GS drops approximately exponentially across iterations; collapse within 5-10 iterations for large datasets\\\"\\n      - \\\"Training data entropy is a direct predictor of generalization capability (r=0.91)\\\"\\n      - \\\"Entropy-based data selection mitigates memorization transition\\\"\\n      - \\\"Diffusion models only; no LLM experiments. No theoretical analysis of WHY entropy collapses\\\"\\n      - \\\"Generated images form tight local clusters while overall variance remains relatively stable\\\"\\n    positioning_notes: >\\n      Parallel phenomenon across modalities: their entropy decline ↔ our JSD decrease (0.27→0.004).\\n      Their \\\"GS drops exponentially\\\" ↔ our feature-space divergence vanishes rapidly → K*=2.\\n      Key distinction: they measure output-distribution entropy; we measure discriminability in feature space.\\n      K* complements their entropy metric: operationalizes \\\"at what depth does entropy decline = indistinguishability?\\\"\\n      Their clustering-while-variance-stable parallels our depth features converging before global statistics.\\n      Cite for cross-modal validation of convergence phenomenon.\\n\\n  # === Should-Cite ===\\n\\n  - id: basani2026diveye\\n    title: \\\"DivEye: Diversity Boosts AI-Generated Text Detection\\\"\\n    authors: \\\"Basani, Chen\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2509.18880\\\"\\n    code: \\\"https://github.com/IBM/diveye\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Surprisal diversity features as potential baseline for depth estimation; zero-shot detector outperforms prior work by 33.2%\\\"\\n    cited: false\\n\\n  - id: amin2025escaping\\n    title: \\\"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\\\"\\n    authors: \\\"Amin et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2502.08924\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Boosting-inspired framework showing weak signal suffices for iterative training; motivates practical utility of imperfect depth estimators\\\"\\n    cited: false\\n\\n  - id: zawalski2026codec\\n    title: \\\"CoDeC: Detecting Data Contamination in LLMs via In-Context Learning\\\"\\n    authors: \\\"Zawalski et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2510.27055\\\"\\n    category: \\\"contamination\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Binary contamination detection via ICL confidence shifts; complementary to our finer-grained depth estimation approach\\\"\\n    cited: false\\n\\n  - id: gambetta2025surplexity\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse\\\"\\n    authors: \\\"Gambetta et al.\\\"\\n    venue: \\\"arXiv preprint 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2410.12341\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Surprise-based collapse metric; surplexity scores as potential feature for depth estimation pipeline and baseline comparison\\\"\\n    cited: false\\n\\n  - id: zhang2024minkpp\\n    title: \\\"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\\\"\\n    authors: \\\"Zhang, Zheng, Gao, Miao\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Binary detection baseline; does not distinguish generational depth\\\"\\n    cited: false\\n\\n  - id: shumailov2024collapse\\n    title: \\\"AI models collapse when trained on recursively generated data\\\"\\n    authors: \\\"Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal\\\"\\n    venue: \\\"Nature 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Seminal model collapse result; describes macro phenomenon but provides no detection tool for depth\\\"\\n    cited: false\\n\\n  - id: alemohammad2024selfconsuming\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Alemohammad, Casco-Rodriguez, Luber, Babaei, Letizia, Bastani, Baraniuk\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Theoretical and empirical analysis of iterative generative training; complements Shumailov with formal convergence analysis\\\"\\n    cited: false\\n\\n  - id: dohmatob2024model\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: \\\"Dohmatob, Feng, Yang, Charton, Kempe\\\"\\n    venue: \\\"ICML 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Scaling law perspective on collapse; tail distribution loss aligns with our observed feature convergence\\\"\\n    cited: false\\n\\n  - id: xie2023dsir\\n    title: \\\"Data Selection with Importance Resampling\\\"\\n    authors: \\\"Xie, Santurkar, Ma, Liang\\\"\\n    venue: \\\"ICML 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Distribution-matching data selection baseline; does not estimate recursive depth\\\"\\n    cited: false\\n\\n  - id: tirumala2024d4\\n    title: \\\"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\\\"\\n    authors: \\\"Tirumala, Markosyan, Zettlemoyer, Aghajanyan\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Deduplication + diversification baseline for data curation; orthogonal to depth-based filtering\\\"\\n    cited: false\\n\\n  - id: xie2024doremi\\n    title: \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\"\\n    authors: \\\"Xie, Pham, Dong, Du, Liu, Lu, Liang, Le, Ma, Yu\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Domain reweighting for pretraining; does not consider generational depth dimension\\\"\\n    cited: false\\n\\n  - id: kirchenbauer2023watermark\\n    title: \\\"A Watermark for Large Language Models\\\"\\n    authors: \\\"Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein\\\"\\n    venue: \\\"ICML 2023\\\"\\n    category: \\\"watermarking\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Provenance tracking via watermarking; complementary approach to depth estimation when watermarks are available\\\"\\n    cited: false\\n\\n  - id: zellers2019grover\\n    title: \\\"Defending Against Neural Fake News\\\"\\n    authors: \\\"Zellers, Holtzman, Rashkin, Bisk, Farhadi, Roesner, Choi\\\"\\n    venue: \\\"NeurIPS 2019\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Early neural text detection; binary classification paradigm that our ordinal approach generalizes\\\"\\n    cited: false\\n\\n  - id: ippolito2020detection\\n    title: \\\"Automatic Detection of Generated Text is Easiest when Humans are Fooled\\\"\\n    authors: \\\"Ippolito, Duckworth, Callison-Burch, Eck\\\"\\n    venue: \\\"ACL 2020\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Binary detection difficulty analysis; does not consider multi-generational depth\\\"\\n    cited: false\\n\", \"total_chars\": 13194, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "875a80ed-6090-4921-a9dc-ff9715edc364",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "bf305a4c-3893-4bd7-bc13-c391ce97dec1",
  "sourceToolAssistantUUID": "875a80ed-6090-4921-a9dc-ff9715edc364",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T08:54:57.849Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QgP7rZzP5UsJM4Lc8ESj4n`</summary>

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
  "parentUuid": "bf305a4c-3893-4bd7-bc13-c391ce97dec1",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHcShQHhpEDCVTCTAbz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44463e76-38a4-47b8-a6c2-d2e70189e321",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DB6cqLM9gFNHM8CcFnLnto",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15367,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2015
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 308,
          "cache_read_input_tokens": 15367,
          "cache_creation_input_tokens": 2015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2015,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T08:54:57.859Z_

<details><summary>↩ Tool result · `toolu_01QgP7rZzP5UsJM4Lc8ESj4n`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-contamination\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\\n- Fallback: EMNLP 2026 Findings\\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\\n\\n## Canonical Experimental Condition\\n\\n**Continuation mode 是 cross-model 结论的基础。**\\n\\n> \\\"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\\\"\\n\\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\\n|-----------|-------------|-------------|---------|\\n| Continuation | 91-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\\n\\n**原则**：\\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\\n- mvp-001 (Qwen-rewrite) 定位为 \\\"pilot study demonstrating feasibility\\\"，后续用 continuation mode rigorously validate\\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\\n\\n## Core Claims (2+1 结构, D012)\\n\\n### Primary: C1' (K* Characterization)\\n首次系统测量递归合成文本的 generational discrimination boundary K*。\\n\\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 4-model × 2-mode 实验矩阵系统表征 K*_empirical 的行为，包括跨模型一致性、特征退化排序、以及 generation mode 对 depth signal 的调控效应。\\n\\n**子组件：**\\n\\n**(a) K* = 2 across all tested configurations**\\n> 4-model 1v2 bootstrap 95% CI 汇总：\\n> | Model | AUC 1v2 | 95% CI | CI lower > 0.60? |\\n> |-------|---------|--------|-----------------|\\n> | Qwen-rewrite | 0.6955 | [0.6859, 0.7041] | ✅ (+8.6pp) |\\n> | Pythia-1.4B | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\\n> | OLMo-1B | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\\n> | Qwen-cont | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp, 最边缘) |\\n>\\n> - 全部 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60, 全部 permutation p < 0.002\\n> - K* 不是离散跳变值，而是 CI-bounded continuum threshold\\n> - Paper 可写：\\\"K*=2 (bootstrap 95% CI for AUC₁ᵥ₂ > 0.60 across all four model configurations; AUC₂ᵥ₃ CI upper < 0.60)\\\"\\n\\n**(b) Cross-model transfer**\\n> - Pythia↔OLMo 91% accuracy retention → K*=2 不是 model self-familiarity artifact\\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\\n> - 1v2+ transfer 取决于模型族相似度 → 与 K*=2 完美一致（K* 之上分辨力本就微弱）\\n> - depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity\\n\\n**(c) Degradation ordering consistency**\\n> - Spearman ρ ≥ 0.85 on single-feature AUC ranking（mode-controlled, continuation）\\n> - Top discriminative features shared: surp_d1_std, surp_std, surp_d2_std\\n> - Limitation: depth-pair level 一致性在 1v2 处较弱（τ~0.37）\\n> - Metric: single-feature AUC ranking（model-free, not LightGBM split count）\\n\\n**(d) Generation mode analysis (§4.x Analysis subsection)**\\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\\n> - 论文定位：Analysis subsection（\\\"How does generation mode affect depth estimation?\\\"），不是独立 claim\\n\\n### Secondary: C3 (Graduated Filtering)\\n即使在 K*=2 的粗粒度 ordinal signal（human/gen-1/gen-2+ 三级）下，K*-aware graduated filtering 仍优于 binary filtering，因为 ordinal signal 在阈值附近提供更 calibrated 的质量估计。\\n\\n### Supporting Analysis: Canonical Condition Selection\\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\\n\\n## Story Spine\\n\\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\\\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\\\"。通过 4-model × 2-mode 实验矩阵系统表征 K*，揭示控制因素（模型架构、解码策略、generation mode），为数据治理提供 actionable guidance。\\n- **Headline result template**: \\\"We establish K*=2 as the generational discrimination boundary for 1.5B-scale models under standard decoding, with depth features that are 70-85% text-intrinsic (Pythia↔OLMo 91% transfer retention). Even this coarse 3-class signal yields X% improvement over binary filtering on MMLU/HellaSwag.\\\"\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n1. **\\\"K*=2 太浅，graduated filtering 收益有限\\\"** → K* 是模型/解码策略依赖的；展示不同解码策略如何调控 K*（exp-003）；即使 K*=2，3-class 比 binary 在阈值附近更 calibrated（exp-006）\\n2. **\\\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\\\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ generation mode analysis，不是分类器本身\\n3. **\\\"Prompt-chain 不代表真实世界递归污染\\\"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法\\n4. **\\\"单模型/单数据集，泛化性不够\\\"** → 3 个模型族 × 2 种 generation mode + 4×4 cross-model transfer matrix\\n5. **\\\"同模型做生成和 surprisal 计算有 bias\\\"** → **exp-013 直接反驳**：Pythia↔OLMo 91% accuracy retention，0v1 transfer AUC > 0.96。Depth signal 主要编码在文本而非 model self-familiarity\\n6. **\\\"为什么不用 learned representations\\\"** → 作为 baseline 对比；hand-crafted features 更 interpretable 且支持 degradation ordering 分析\\n7. **\\\"Graduated filtering 没和 data selection methods 比\\\"** → exp-006 包含 DSIR baseline + α sensitivity sweep\\n8. **\\\"K* 的统计不确定性未量化\\\"** → 4-model bootstrap CI + permutation test（exp-007）\\n\\n## Venue Fit\\n\\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\\n- 2+1 claim 结构：C1' 是 comprehensive characterization study，C3 是 practical application，generation mode analysis 增加深度\\n- 风险：如果审稿人偏 methods，K*=2 + standard classifier 可能被认为贡献不足 → 强调 problem formulation + characterization + transfer analysis 的 novelty\\n\", \"total_chars\": 6221, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44463e76-38a4-47b8-a6c2-d2e70189e321",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "d54a25ec-0566-40e9-96eb-b834c78dc847",
  "sourceToolAssistantUUID": "44463e76-38a4-47b8-a6c2-d2e70189e321",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T08:55:01.552Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013SY5R7iXajGDpgtdmJ1z37`</summary>

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
  "parentUuid": "d54a25ec-0566-40e9-96eb-b834c78dc847",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHd6bhqCFBhRh9ATgat",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2062db63-1b40-49f8-a619-162017c2cd90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2GJTaHwtUkPQdzXDVXmv9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8807,
      "cache_read_input_tokens": 17382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8807,
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

_source line 14 · 2026-05-13T08:55:01.563Z_

<details><summary>↩ Tool result · `toolu_013SY5R7iXajGDpgtdmJ1z37`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2062db63-1b40-49f8-a619-162017c2cd90",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "9dd17492-f225-4b5e-b6d7-1593ddfe1226",
  "sourceToolAssistantUUID": "2062db63-1b40-49f8-a619-162017c2cd90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T08:55:02.029Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01L27P1oPJY68pPHqk4r7KZY`</summary>

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
  "parentUuid": "9dd17492-f225-4b5e-b6d7-1593ddfe1226",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHd6bhqCFBhRh9ATgat",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "787c80ce-5051-4a1a-b7fb-0280a7be6864",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2GJTaHwtUkPQdzXDVXmv9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8807,
      "cache_read_input_tokens": 17382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8807,
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

_source line 16 · 2026-05-13T08:55:02.039Z_

<details><summary>↩ Tool result · `toolu_01L27P1oPJY68pPHqk4r7KZY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/memory.md\", \"content\": \"# Memory — gen-depth-contamination\\n\\n## 已知问题\\n\\n### right-padding (2026-05-12)\\nMVP pipeline 使用 right-padding（transformers 默认）。Director 确认对 MVP 判定无影响（所有 depth 一致受影响），不中断当前实验。**full study 阶段必须修复为 `tokenizer.padding_side = \\\"left\\\"`**，否则 batch 生成时 padding tokens 会影响生成质量的绝对水平。\\n\\n## GPU 优化建议 (2026-05-12)\\n\\n### batch size 调优\\n4090D 24GB 跑 1.5B fp16 模型仅用 3.9GB 显存 (16%)，GPU 利用率 45%。\\n- Step 3 生成：batch_size 16→**64**（保守）或 128\\n- Step 4 特征提取：feat_batch_size 8→**24**（保守）或 32\\n- 预估节省 ~74 min (38%)，加 flash-attn 可再省 10-15%\\n- full study 时一并修复\\n\\n## AutoDL 环境经验\\n\\n### C4 数据集加载 (2026-05-12)\\nAutoDL 代理下 `load_dataset(\\\"allenai/c4\\\", \\\"en\\\", streaming=True)` 会触发全量文件树解析（数千个 shard 的分页 API 请求），ProxyError 无限重试。修复：用单 shard URL 直接加载 + `HF_ENDPOINT=https://hf-mirror.com` 中转。\\n\\n### 环境变量必须固化到启动脚本 (2026-05-12)\\nAutoDL 上 `source /etc/network_turbo`、SSL 证书、HF 配置等环境变量不能只在 shell session 里 export，必须写入 `run_mvp.sh` 等包装脚本，否则 tmux session 里不生效。\\n\\n### submit_training_job pid=\\\"unknown\\\" 问题 (2026-05-13)\\nsubmit_training_job 有时返回 pid=\\\"unknown\\\"，导致 registry 状态停在 PREPARING、cron 未创建。exp-017 和 exp-003 都遇到此问题。**解决方式**：提交后必须派 Worker SSH 检查实际进程状态（tmux ls + ps aux），手动修正 registry 并注册 cron。\\n\\n## 实验设计决策\\n\\n### Generation mode 影响 depth signal 强度 (2026-05-13)\\nRewrite mode（instruction prompting）比 continuation mode 多产生 ~8.4pp AUC 差距（Qwen: 0.6957 vs 0.6114）。原因推测：instruction-following 引入更大的分布偏移，放大 depth-discriminative 信号。论文中 K* 应同时报告两种 mode 的结果；C1 robustness 依赖 continuation mode（更保守的 lower bound）。\\n\\n### Degradation ordering mode-dependent (2026-05-13)\\n4-model τ 矩阵表明 generation mode 贡献 ~60-70% 的排序偏离，架构 ~30-40%。C2 claim 不能说 \\\"universal ordering\\\"，应改为 \\\"mode-conditioned consistency with architecture residuals\\\"。Director 决策 D008 的后续：4-model τ 数据已齐全，等 Director 确认 C2 最终措辞。\\n\", \"total_chars\": 1706, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "787c80ce-5051-4a1a-b7fb-0280a7be6864",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "deedf06a-1dc8-4dcc-8da7-186fe504f779",
  "sourceToolAssistantUUID": "787c80ce-5051-4a1a-b7fb-0280a7be6864",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T08:55:02.675Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TQZaaB31ZdY2zDnpwCBd7r`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "deedf06a-1dc8-4dcc-8da7-186fe504f779",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHd6bhqCFBhRh9ATgat",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dc8bdf8-7932-4f42-a123-5e88897c20c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2GJTaHwtUkPQdzXDVXmv9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8807,
      "cache_read_input_tokens": 17382,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8807
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 17382,
          "cache_creation_input_tokens": 8807,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8807,
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

_source line 18 · 2026-05-13T08:55:02.684Z_

<details><summary>↩ Tool result · `toolu_01TQZaaB31ZdY2zDnpwCBd7r`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md\", \"content\": \"# gen-depth-contamination — Research Dashboard\\n\\n> 最后更新: 2026-05-13 07:50 UTC | 更新原因: exp-006 估算 ~21h（非 72h），deadline 倒排修订，timeline 宽裕\\n\\n## 核心方向\\n递归合成文本的代际深度估计：测量 K*（饱和边界）+ graduated filtering 应用。Route B framing（K* 作为 operational quantity）。Drayson et al. (EMNLP 2025) = closest prior work (binary filtering)，我们是 ordinal 推广。2+1 claim 结构（D012）：C1'(K* characterization) + C3(graduated filtering) + supporting analysis。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（P0 实验收尾）+ 审稿通道已开\\n- **实验**: 8 DONE / 1 RUNNING / 9 planned (18 total)\\n- **K*=2**: 4/4 model configs 确认，bootstrap 95% CI 全 > 0.60\\n- **C1' 子组件**: (a) K*=2 ✅ (b) cross-transfer ✅ (c) degradation ordering ✅ (d) mode analysis ✅\\n- **C3**: exp-006 脚本就绪，等 GPU（D013 fallback 预案已建立）\\n- **paper_framing.md**: D012 重构完成（2+1 结构）\\n- **关键路径**: exp-003 (~8h) → exp-006 (~21h) → analysis + writing → 05-25 ARR\\n\\n## 近期任务\\n- [ ] exp-003 decoding ablation 完成 + 结果收集（RUNNING，~8h 剩余）\\n- [ ] exp-006 启动（exp-003 完成后 GPU **零间隔**切换，~21h，C3 核心证据）\\n- [ ] exp-003 bootstrap CI for 4 decoding configs（CPU，exp-003 完成后）\\n- [ ] exp-005 registry Spearman ρ 补全（Agent CPU 任务，进行中）\\n- [ ] exp-004 cross-scale probe Qwen-7B（P0, 8h budget，exp-006 后或并行）\\n- [ ] 论文写作启动（exp-006 结果后）\\n- [x] exp-006 脚本 + dry-run 就绪（6 策略 × 5 seeds × α sweep）\\n- [x] D012 paper_framing.md 重构完成（2+1 结构）\\n- [x] K*=2 四模型 bootstrap CI (exp-007)\\n- [x] Cross-model transfer 4×4 matrix (exp-013)\\n- [x] C2 qualified claim (D011)\\n- [x] Generation mode effect (exp-017)\\n\\n## GPU 预算\\n- 分配：1×RTX 4090D (cuda:0) on autodl-4090d\\n- 已消耗（实际）：~20h（actual/budget ratio ≈ 40%）\\n- 剩余关键：exp-006 ~21h + exp-004 ~3h (估)\\n- DDL: 05-25 ARR（12 天）\\n\\n## Deadline 倒排（修订）\\n| 日期 | 里程碑 |\\n|------|--------|\\n| ~05-14 | exp-003 完成，exp-006 立即启动 |\\n| ~05-15 | exp-006 完成（~21h 估算） |\\n| ~05-16 | exp-006 分析 + exp-004 (optional) |\\n| ~05-17 | 论文写作启动（Paper Agent） |\\n| ~05-22 | 初稿完成，提交审稿 |\\n| ~05-24 | 修订定稿 |\\n| 05-25 | ARR 提交 |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D013 | 2026-05-13 | C3 exp-006 单点依赖风险评估 + fallback story 预案 | exp-006, exp-003 |\\n| D012 | 2026-05-13 | 论文 claim 重构：4 claims → 2+1 结构（C1' K* characterizat | exp-013, exp-006 |\\n| D011 | 2026-05-13 | D010 修正：C2 从 \\\"supplementary\\\" 升级为 \\\"qualified claim\\\" | exp-005, exp-017 |\\n| D010 | 2026-05-13 | C2 Plan A 否决 → 执行 Plan B：degradation ordering 限定为  | exp-017, exp-005 |\\n| D009 | 2026-05-13 | C2 战略评估：C1 是承重墙，C3 是安全网，C2 是加分项；exp-016 列为场景 B 应急 | exp-005, exp-017, exp-006, exp-016 |\\n| D008 | 2026-05-13 | C2 claim 暂停写入论文——等 exp-017 解耦 generation mode 因素后决 | exp-005, exp-017 |\\n| D007 | 2026-05-13 | Drayson novelty 评估完成：核心 novelty 安全，Story Spine 微调， | exp-006 |\\n| D006 | 2026-05-13 | 回滚 Drayson et al. 引用清理——Reviewer 确认为真实论文 (EMNLP 20 | — |\\n| D005 | 2026-05-13 | Dream 分析完成：proceed with P0, 整合 8 项确认行动到 framing/pl | exp-006, exp-007, exp-015 |\\n| D004 | 2026-05-12 | Reviewer 审查后修正：C1 区分 K*_empirical vs K*_theory；exp | — |\\n\\n\\n\\n\", \"total_chars\": 2847, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dc8bdf8-7932-4f42-a123-5e88897c20c2",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "bfc895ac-4fdf-46d2-a9a6-ce0bb2473086",
  "sourceToolAssistantUUID": "0dc8bdf8-7932-4f42-a123-5e88897c20c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-13T08:55:05.656Z_

Now let me look at the artifacts and any paper drafts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfc895ac-4fdf-46d2-a9a6-ce0bb2473086",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHdTHejB1jLAnn7tZPg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc0f28c7-bf95-4c14-ab26-d849d7611a2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQn1HhCcEU2PTnD1ijsgaP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3370,
      "cache_read_input_tokens": 26189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3370,
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

_source line 20 · 2026-05-13T08:55:06.123Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011ZPssBS3dAFf5v8Y1yJNvk`</summary>

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
  "parentUuid": "bc0f28c7-bf95-4c14-ab26-d849d7611a2c",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHdTHejB1jLAnn7tZPg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "239ce7e9-4d08-4b61-b8e6-444fad3843b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQn1HhCcEU2PTnD1ijsgaP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3370,
      "cache_read_input_tokens": 26189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3370,
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

_source line 21 · 2026-05-13T08:55:06.134Z_

<details><summary>↩ Tool result · `toolu_011ZPssBS3dAFf5v8Y1yJNvk`</summary>

```text
artifacts/dream_reports/dream_20260512T200328/best/paper.tex
artifacts/dream_reports/dream_20260512T200328/median/paper.tex
artifacts/dream_reports/dream_20260512T200328/worst/paper.tex
artifacts/dream_reports/dream_20260513T080728/best/paper.tex
artifacts/dream_reports/dream_20260513T080728/median/paper.tex
artifacts/dream_reports/dream_20260513T080728/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "239ce7e9-4d08-4b61-b8e6-444fad3843b7",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "07658851-d0d8-4600-bcea-d51e67770822",
  "sourceToolAssistantUUID": "239ce7e9-4d08-4b61-b8e6-444fad3843b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-13T08:55:06.451Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01K8YheP3Vtxav3b1fhSwxsW`</summary>

```json
{
  "pattern": "artifacts/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07658851-d0d8-4600-bcea-d51e67770822",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHdTHejB1jLAnn7tZPg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2de3060-0441-4905-83fc-68feba0a0577",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQn1HhCcEU2PTnD1ijsgaP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3370,
      "cache_read_input_tokens": 26189,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3370
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 26189,
          "cache_creation_input_tokens": 3370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3370,
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

_source line 23 · 2026-05-13T08:55:06.462Z_

<details><summary>↩ Tool result · `toolu_01K8YheP3Vtxav3b1fhSwxsW`</summary>

```text
artifacts/_project/report/related_work_structure.md
artifacts/_project/report/gpu_optimization_report.txt
artifacts/gpu_optimization_report.txt
artifacts/_project/report/claim_routes.md
artifacts/_project/report/theory_framework.md
artifacts/_project/report/full_study_plan.md
artifacts/_project/report/methodology_draft.md
artifacts/_project/report/figure_plan.md
artifacts/dream_reports/dream_20260512T200328/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260512T200328/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260512T200328/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260512T200328/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260512T200328/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T200328/best/experiment_data.json
artifacts/dream_reports/dream_20260512T200328/best/paper.tex
artifacts/dream_reports/dream_20260512T200328/best/paper.aux
artifacts/dream_reports/dream_20260512T200328/best/paper.out
artifacts/dream_reports/dream_20260512T200328/best/paper.pdf
artifacts/dream_reports/dream_20260512T200328/best/paper.log
artifacts/dream_reports/dream_20260512T200328/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260512T200328/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T200328/median/experiment_data.json
artifacts/dream_reports/dream_20260512T200328/median/paper.tex
artifacts/dream_reports/dream_20260512T200328/median/paper.aux
artifacts/dream_reports/dream_20260512T200328/median/paper.out
artifacts/dream_reports/dream_20260512T200328/median/paper.pdf
artifacts/dream_reports/dream_20260512T200328/median/paper.log
artifacts/dream_reports/dream_20260512T200328/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260512T200328/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T200328/worst/experiment_data.json
artifacts/dream_reports/dream_20260512T200328/worst/paper.tex
artifacts/dream_reports/dream_20260512T200328/worst/paper.aux
artifacts/dream_reports/dream_20260512T200328/worst/paper.out
artifacts/dream_reports/dream_20260512T200328/worst/paper.pdf
artifacts/dream_reports/dream_20260512T200328/worst/paper.log
artifacts/dream_reports/dream_20260512T200328/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260512T200328/logs/orchestrator.log
artifacts/dream_reports/dream_20260512T200328/best/review_report.md
artifacts/dream_reports/dream_20260512T200328/logs/review_best.log
artifacts/dream_reports/dream_20260512T200328/median/review_report.md
artifacts/dream_reports/dream_20260512T200328/logs/review_median.log
artifacts/dream_reports/dream_20260512T200328/worst/review_report.md
artifacts/dream_reports/dream_20260512T200328/logs/review_worst.log
artifacts/dream_reports/dream_20260512T200328/meta.yaml
artifacts/_project/report/literature_scan_2025_2026.md
artifacts/literature_scan_2025_2026.md
artifacts/_project/report/literature_positioning_notes.md
artifacts/_project/report/literature_positioning_notes_d23bf4.md
artifacts/literature_positioning_notes.md
artifacts/_project/chart/auc_heatmap.pdf
artifacts/figures/auc_heatmap.pdf
artifacts/_project/chart/feature_importance.pdf
artifacts/figures/feature_importance.pdf
artifacts/_project/chart/jsd_decay.pdf
artifacts/figures/jsd_decay.pdf
artifacts/exp005_4model_tau_matrix.json
artifacts/exp-005/data/exp005_4model_tau_matrix.json
artifacts/bootstrap_ci_4model.json
artifacts/exp-013/data/cross_transfer_matrix.csv
artifacts/exp-013/data/cross_transfer_matrix.json
artifacts/manifest.yaml
artifacts/exp006_filtering_strategies.py
artifacts/exp006_continued_pretraining.py
artifacts/exp006_evaluate.py
artifacts/run_exp006.sh
artifacts/exp006_analyze.py
artifacts/dream_reports/dream_20260513T080728/logs/orchestrator.log
artifacts/dream_reports/dream_20260513T080728/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260513T080728/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260513T080728/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260513T080728/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260513T080728/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T080728/best/experiment_data.json
artifacts/dream_reports/dream_20260513T080728/best/paper_framing.md
artifacts/dream_reports/dream_20260513T080728/best/paper.tex
artifacts/dream_reports/dream_20260513T080728/best/paper.aux
artifacts/dream_reports/dream_20260513T080728/best/paper.out
artifacts/dream_reports/dream_20260513T080728/best/paper.pdf
artifacts/dream_reports/dream_20260513T080728/best/paper.log
artifacts/dream_reports/dream_20260513T080728/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260513T080728/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T080728/median/experiment_data.json
artifacts/dream_reports/dream_20260513T080728/median/paper_framing.md
artifacts/dream_reports/dream_20260513T080728/median/paper.tex
artifacts/dream_reports/dream_20260513T080728/median/paper.aux
artifacts/dream_reports/dream_20260513T080728/median/paper.out
artifacts/dream_reports/dream_20260513T080728/median/paper.pdf
artifacts/dream_reports/dream_20260513T080728/median/paper.log
artifacts/dream_reports/dream_20260513T080728/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260513T080728/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T080728/worst/experiment_data.json
artifacts/dream_reports/dream_20260513T080728/worst/paper_framing.md
artifacts/dream_reports/dream_20260513T080728/worst/paper.tex
artifacts/dream_reports/dream_20260513T080728/worst/paper.aux
artifacts/dream_reports/dream_20260513T080728/worst/paper.out
artifacts/dream_reports/dream_20260513T080728/worst/paper.pdf
artifacts/dream_reports/dream_20260513T080728/worst/paper.log
artifacts/dream_reports/dream_20260513T080728/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260513T080728/best/review_context.yaml
artifacts/dream_reports/dream_20260513T080728/best/review_report.md
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2de3060-0441-4905-83fc-68feba0a0577",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "72560077-8b98-459b-9245-339c4a568e64",
  "sourceToolAssistantUUID": "c2de3060-0441-4905-83fc-68feba0a0577",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-13T08:55:09.321Z_

Let me read the most recent "best" paper (the latest dream report) and its review, plus supporting materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72560077-8b98-459b-9245-339c4a568e64",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHdjR1jfj2758zqRh2x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec36bf0e-d49e-4328-91eb-0a22d6038d6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaaqNcCgffFe2279dLpXdZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2370,
      "cache_read_input_tokens": 29559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2370,
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

_source line 25 · 2026-05-13T08:55:09.685Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UunZNrbLwcBmqW2kY4qLvQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec36bf0e-d49e-4328-91eb-0a22d6038d6e",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHdjR1jfj2758zqRh2x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "079f3572-cd91-4f53-838e-9e0df6457220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaaqNcCgffFe2279dLpXdZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2370,
      "cache_read_input_tokens": 29559,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2370
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 29559,
          "cache_creation_input_tokens": 2370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2370,
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

_source line 26 · 2026-05-13T08:55:09.979Z_

<details><summary>↩ Tool result · `toolu_01UunZNrbLwcBmqW2kY4qLvQ`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{graphicx}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{xcolor}
10	\usepackage{hyperref}
11	
12	\title{Generational Depth Contamination: Measuring and Exploiting the Discrimination Boundary of Recursive Synthetic Text}
13	
14	\author{Anonymous}
15	
16	\begin{document}
17	\maketitle
18	
19	% ============================================================
20	\begin{abstract}
21	Web-scale training corpora are increasingly contaminated by machine-generated text that has been recursively regenerated across multiple generations.
22	Existing detectors treat synthetic text as a binary category (human vs.\ machine), ignoring the progressive quality degradation across generational depth.
23	We formalize recursive generation as an iterated lossy channel and invoke the Data Processing Inequality (DPI) to prove the existence of a finite generational discrimination boundary $K^*$---the deepest generation at which pairwise depth discrimination remains statistically reliable.
24	
25	Through controlled experiments spanning three model families (Qwen-2.5, Pythia, OLMo), two model scales (1.5B, 7B), multiple decoding strategies, and both base and instruction-tuned variants, we establish $K^*=2$ as the empirical boundary for 1.5B-scale models under standard nucleus decoding, rising to $K^*\geq 3$ under high-temperature decoding ($T=1.2$) and at 7B scale.
26	Decoding temperature creates a controllable gradient from $K^*=1$ (greedy) to $K^*=3$ (high temperature), demonstrating that $K^*$ captures genuine information-theoretic properties of the recursive channel rather than classifier artifacts.
27	
28	We show that even this coarse three-class ordinal signal (human / gen-1 / gen-2+) enables \emph{graduated filtering} that significantly outperforms binary filtering on downstream benchmarks: $+2.48$ pp on MMLU and $+2.70$ pp on HellaSwag ($p<0.01$, 5 seeds), with gains scaling monotonically with contamination severity.
29	Our 15-dimensional hand-crafted feature set matches frozen-embedding baselines while providing 85\% cross-model transfer retention versus 62\% for learned representations, supporting interpretable, model-agnostic deployment.
30	\end{abstract}
31	
32	% ============================================================
33	\section{Introduction}
34	
35	The proliferation of large language models (LLMs) has created a feedback loop in web-scale data: model outputs enter training corpora, and subsequent models train on---and regenerate---these outputs, producing \emph{recursive synthetic text} of increasing generational depth \cite{shumailov2024model}.
36	While binary synthetic text detectors have achieved strong performance at distinguishing human from machine text \cite{mitchell2023detectgpt,hans2024binoculars}, they do not estimate \emph{how many rounds of recursive generation} a text has undergone.
37	This distinction matters: first-generation synthetic text retains approximately 85\% of the information structure of its human source, while deeper generations undergo progressive quality collapse that binary detectors cannot resolve.
38	
39	We introduce the concept of the \textbf{generational discrimination boundary} $K^*$, defined as the maximum depth $k$ at which a pairwise classifier can reliably distinguish generation $k$ from generation $k+1$.
40	Our information-theoretic framing models recursive generation as an iterated lossy channel.
41	By the Data Processing Inequality (DPI), the mutual information $I(X; Y_k)$ between the original text $X$ and its $k$-th generation output $Y_k$ decreases monotonically, guaranteeing convergence and thus a finite $K^*$.
42	
43	Our contributions are:
44	\begin{enumerate}
45	\item \textbf{$K^*$ Characterization (C1):} We provide the first systematic measurement of $K^*$ across four model configurations, establishing $K^*=2$ for 1.5B-scale models under standard decoding.
46	    We show that $K^*$ is not a ceiling but a controllable operating point that rises with model scale ($K^*\geq 3$ at 7B) and decoding entropy ($K^*=3$ at $T=1.2$), forming a gradient from $K^*=1$ (greedy) through $K^*=2$ (standard) to $K^*=3$ (high temperature/larger model).
47	\item \textbf{Graduated Filtering (C3):} We demonstrate that $K^*$-aware graduated filtering, which assigns fractional weights based on ordinal depth estimates, significantly outperforms binary filtering on MMLU ($+2.48$ pp) and HellaSwag ($+2.70$ pp), with gains that scale monotonically with contamination rate.
48	\item \textbf{Supporting analyses:} We validate ecological validity via retrain-chain experiments, demonstrate 85\% cross-model feature transfer, show that frontier LLMs and binary detectors cannot estimate depth, and provide proof-of-concept Common Crawl validation.
49	\end{enumerate}
50	
51	% ============================================================
52	\section{Related Work}
53	
54	\paragraph{Model Collapse and Recursive Generation.}
55	Shumailov et al.\ (2024) demonstrate that iterative training on model outputs leads to ``model collapse,'' where tail distributions vanish over generations.
56	Alemohammad et al.\ (2024) and Dohmatob et al.\ (2024) provide theoretical analyses of this phenomenon.
57	These works characterize the \emph{macroscopic} phenomenon but do not provide tools for detecting or measuring generational depth in individual texts.
58	
59	\paragraph{Binary Synthetic Text Detection.}
60	DetectGPT \cite{mitchell2023detectgpt}, Binoculars \cite{hans2024binoculars}, and DivEye leverage statistical properties of model outputs for binary (human vs.\ machine) classification.
61	While effective at the human/synthetic boundary (AUC $> 0.91$), we show these methods achieve near-chance performance at distinguishing adjacent generational depths ($\text{AUC}_{1v2} \leq 0.53$).
62	
63	\paragraph{Data Selection and Curation.}
64	DSIR \cite{xie2023dsir} and related methods perform distribution matching for data selection but do not estimate recursive depth.
65	Drayson et al.\ (2025) apply binary detection scores for importance resampling to prevent model collapse---the closest prior work.
66	Our graduated filtering extends this by exploiting ordinal depth structure beyond binary decisions.
67	
68	% ============================================================
69	\section{Method}
70	
71	\subsection{Information-Theoretic Framework}
72	
73	We model recursive text generation as an iterated lossy channel.
74	Let $X$ denote the original human-written text and let $\mathcal{G}$ be the generation function of an LLM with decoding strategy $\delta$.
75	The $k$-th generation is $Y_k = \mathcal{G}(Y_{k-1})$ with $Y_0 = X$.
76	
77	By the \textbf{Data Processing Inequality (DPI)}, for any Markov chain $X \to Y_1 \to Y_2 \to \cdots$:
78	\begin{equation}
79	I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq I(X; Y_k) \geq 0
80	\end{equation}
81	Since $I(X; Y_k)$ is monotonically non-increasing and bounded below, it converges.
82	This guarantees the existence of a finite \textbf{theoretical discrimination boundary} $K^*_{\text{theory}}$: the depth beyond which pairwise discrimination is information-theoretically impossible.
83	
84	\subsection{Empirical Discrimination Boundary $K^*$}
85	
86	We define the \textbf{empirical discrimination boundary} $K^*_{\text{emp}}$ operationally:
87	\begin{equation}
88	K^* = \max\{k : \text{AUC}_{k \text{v} (k+1)} > \theta\}
89	\end{equation}
90	where $\text{AUC}_{k\text{v}(k+1)}$ is the area under the ROC curve for a binary classifier distinguishing generation $k$ from $k+1$, and $\theta = 0.60$ is a discrimination threshold.
91	$K^*_{\text{emp}} \leq K^*_{\text{theory}}$ provides a conservative lower bound.
92	
93	\subsection{Feature Design}
94	
95	We extract a 15-dimensional feature vector for each text document, organized into four groups:
96	
97	\begin{itemize}
98	\item \textbf{Vocabulary diversity} (4 features): type-token ratio, hapax legomena ratio, frequency-rank entropy, Yule's K.
99	\item \textbf{Surprisal statistics} (5 features): mean and standard deviation of token surprisal, first- and second-order surprisal differences (surp\_d1\_std, surp\_d2\_std), and max surprisal.
100	\item \textbf{Tail distribution} (3 features): fraction of tokens with surprisal $> 2\sigma$, tail weight ratio, kurtosis of surprisal distribution.
101	\item \textbf{Structural} (3 features): sentence length variance, repetition rate (3-gram), and discourse coherence score.
102	\end{itemize}
103	
104	We train LightGBM ordinal classifiers with these features for depth estimation.
105	
106	\subsection{Graduated Filtering}
107	
108	Given a contaminated corpus $\mathcal{D}$ with unknown mixture of human and multi-generation synthetic text, our graduated filtering assigns weights:
109	\begin{equation}
110	w(x) = \begin{cases}
111	1 & \text{if } \hat{d}(x) = 0 \text{ (predicted human)} \\
112	\alpha & \text{if } \hat{d}(x) = 1 \text{ (predicted gen-1)} \\
113	0 & \text{if } \hat{d}(x) \geq 2 \text{ (predicted gen-2+)}
114	\end{cases}
115	\end{equation}
116	where $\hat{d}(x)$ is the predicted depth and $\alpha \in [0, 1]$ is a discount factor for first-generation text, which retains substantial information value despite being synthetic.
117	
118	% ============================================================
119	\section{Experiments}
120	
121	\subsection{Experimental Setup}
122	
123	\paragraph{Models.} We use Qwen2.5-1.5B-Instruct, Qwen2.5-1.5B (base), Qwen2.5-7B, and Pythia-1.4B.
124	\paragraph{Data.} C4 corpus, 5K documents (1K for 7B due to compute constraints).
125	\paragraph{Generation.} Continuation mode (the model continues from a prefix) is the canonical condition. Depth chains span generations 0--5 (0--3 for 7B, 0--4 for Pythia).
126	\paragraph{Decoding.} Default: nucleus sampling $p=0.95$, $T=1.0$. Ablation covers greedy, $p=0.9/T=1.0$, $p=0.95/T=0.7$, and $p=0.95/T=1.2$.
127	\paragraph{Metrics.} Pairwise AUC, pairwise JSD, $K^*$ (AUC threshold $\theta=0.60$), ordinal accuracy, MAE, bootstrap 95\% CI (10K resamples).
128	
129	% ============================================================
130	\subsection{$K^*$ Characterization}
131	\label{sec:kstar}
132	
133	\paragraph{Decoding Strategy Ablation.}
134	We evaluate four decoding configurations on Qwen2.5-1.5B-Instruct (Table~\ref{tab:decoding}).
135	The results establish a controllable $K^*$ gradient: greedy decoding yields $K^*=1$, standard nucleus configurations ($p=0.9/T=1.0$, $p=0.95/T=0.7$, baseline $p=0.95/T=1.0$) consistently yield $K^*=2$, and high-temperature decoding ($T=1.2$) yields $K^*=3$.
136	
137	The high-temperature condition achieves $\text{AUC}_{2v3} = 0.6218$, crossing the $\theta=0.60$ threshold that all standard-temperature configurations fail to reach.
138	This gradient demonstrates that $K^*$ captures genuine information-theoretic properties of the recursive channel: higher decoding entropy preserves more distributional structure per generation, requiring additional iterations before the signal saturates.
139	
140	Feature degradation ordering remains highly consistent across all configurations, with Spearman $\rho \geq 0.878$ relative to the baseline (Table~\ref{tab:feature_ordering}).
141	This indicates that decoding strategy modulates signal \emph{strength} but not which features degrade first.
142	
143	\begin{table}[t]
144	\centering
145	\small
146	\caption{Decoding strategy ablation on Qwen2.5-1.5B-Instruct. $K^*$ forms a controllable gradient from greedy ($K^*=1$) through standard ($K^*=2$) to high-temperature ($K^*=3$).}
147	\label{tab:decoding}
148	\begin{tabular}{lccccc}
149	\toprule
150	\textbf{Config} & \textbf{$K^*$} & \textbf{AUC$_{0v1}$} & \textbf{AUC$_{1v2}$} & \textbf{AUC$_{2v3}$} & \textbf{JSD$_{0v1}$} \\
151	\midrule
152	greedy & 1 & .9965 & .5862 & .5481 & .2753 \\
153	nucleus $p$=0.9 $T$=1.0 & 2 & .9968 & .6278 & .5582 & .2814 \\
154	$p$=0.95 $T$=0.7 & 2 & .9963 & .6241 & .5558 & .2685 \\
155	baseline $p$=0.95 $T$=1.0 & 2 & .9972 & .6114 & .5609 & .2863 \\
156	$p$=0.95 $T$=1.2 & \textbf{3} & .9981 & .6823 & .6218 & .3082 \\
157	\bottomrule
158	\end{tabular}
159	\end{table}
160	
161	\begin{table}[t]
162	\centering
163	\small
164	\caption{Feature degradation ordering consistency (Spearman $\rho$ vs.\ baseline configuration).}
165	\label{tab:feature_ordering}
166	\begin{tabular}{lc}
167	\toprule
168	\textbf{Config} & \textbf{Spearman $\rho$} \\
169	\midrule
170	greedy & 0.886 \\
171	$p$=0.9 & 0.921 \\
172	$T$=0.7 & 0.914 \\
173	$T$=1.2 & 0.878 \\
174	\bottomrule
175	\end{tabular}
176	\end{table}
177	
178	\paragraph{Cross-Scale Probing (7B).}
179	Scaling from 1.5B to 7B parameters yields $K^* \geq 3$ (Table~\ref{tab:7b}), with $\text{AUC}_{1v2} = 0.6948$ ($+8.34$ pp vs.\ 1.5B) and $\text{AUC}_{2v3} = 0.6175$ (bootstrap 95\% CI: $[0.6015, 0.6338]$, lower bound above $\theta$).
180	
181	The 7B model preserves richer distributional structure per generation---rare n-grams, long-range discourse patterns, and low-frequency vocabulary---requiring more recursive iterations before the depth signal saturates.
182	Combined with the decoding ablation, two independent causal pathways elevate $K^*$ beyond 2: model scale and decoding entropy.
183	
184	\begin{table}[t]
185	\centering
186	\small
187	\caption{Qwen2.5-7B vs.\ 1.5B pairwise discrimination. 7B achieves $K^* \geq 3$.}
188	\label{tab:7b}
189	\begin{tabular}{lcccc}
190	\toprule
191	\textbf{Pair} & \textbf{7B AUC} & \textbf{7B JSD} & \textbf{1.5B AUC} & \textbf{1.5B JSD} \\
192	\midrule
193	0v1 & .9984 & .3415 & .9972 & .2863 \\
194	1v2 & .6948 & .0285 & .6114 & .0051 \\
195	2v3 & .6175 & .0112 & .5609 & .0036 \\
196	\bottomrule
197	\end{tabular}
198	\end{table}
199	
200	\begin{table}[t]
201	\centering
202	\small
203	\caption{7B bootstrap 95\% confidence intervals (10K resamples).}
204	\label{tab:7b_ci}
205	\begin{tabular}{lcccc}
206	\toprule
207	\textbf{Pair} & \textbf{AUC} & \textbf{CI lower} & \textbf{CI upper} & \textbf{CI lower $> 0.60$?} \\
208	\midrule
209	1v2 & .6948 & .6782 & .7108 & \checkmark~(+7.8 pp) \\
210	2v3 & .6175 & .6015 & .6338 & \checkmark~(+0.15 pp) \\
211	\bottomrule
212	\end{tabular}
213	\end{table}
214	
215	\paragraph{Base vs.\ Instruction-Tuned Models.}
216	Table~\ref{tab:base_instruct} compares Qwen2.5-1.5B base and instruct variants.
217	Both yield $K^*=2$, but the base model exhibits stronger pairwise signals ($\text{AUC}_{1v2} = 0.6382$ vs.\ $0.6114$, $\Delta = +2.68$ pp).
218	RLHF alignment compresses inter-generational variance by pulling outputs toward a preferred mode, reducing quantitative signal strength without altering the qualitative convergence behavior.
219	This is practically important: since wild synthetic text originates from both base and instruction-tuned models, the consistency of $K^*=2$ across variants supports the generality of our framework.
220	
221	\begin{table}[t]
222	\centering
223	\small
224	\caption{Base vs.\ Instruct comparison (Qwen2.5-1.5B, continuation mode). Both yield $K^*=2$; base signals are stronger by 2.68 pp at the 1v2 boundary.}
225	\label{tab:base_instruct}
226	\begin{tabular}{lcccccc}
227	\toprule
228	\textbf{Variant} & \textbf{$K^*$} & \textbf{AUC$_{0v1}$} & \textbf{AUC$_{1v2}$} & \textbf{AUC$_{2v3}$} & \textbf{JSD$_{0v1}$} & \textbf{Ord.\ Acc.} \\
229	\midrule
230	base & 2 & .9958 & .6382 & .5685 & .2952 & .3948 \\
231	instruct & 2 & .9972 & .6114 & .5609 & .2863 & .3819 \\
232	$\Delta$ & 0 & $-.0014$ & $+.0268$ & $+.0076$ & $+.0089$ & $+.0129$ \\
233	\bottomrule
234	\end{tabular}
235	\end{table}
236	
237	% ============================================================
238	\subsection{Ecological Validity: Retrain-Chain}
239	\label{sec:retrain}
240	
241	A natural concern is whether prompt-based generation chains reflect realistic recursive contamination, where models are actually \emph{retrained} on their own outputs.
242	We evaluate this using Pythia-1.4B with LoRA (rank=16, $\alpha=32$) retrain chains and compare against prompt chains on the same model (Table~\ref{tab:retrain}).
243	
244	$K^*$ is identical across methods ($K^*=2$) with AUC differences $< 2$ pp at all depth pairs.
245	A classifier trained on prompt-chain data retains 91.5\% accuracy when evaluated on retrain-chain data.
246	Feature distribution divergence (JSD) between methods increases with depth but remains small ($< 0.04$), confirming that inter-generational degradation dominates over method-specific artifacts.
247	
248	\begin{table}[t]
249	\centering
250	\small
251	\caption{Retrain-chain vs.\ prompt-chain (Pythia-1.4B). $K^*$ and AUC are consistent across generation methods.}
252	\label{tab:retrain}
253	\begin{tabular}{lccc}
254	\toprule
255	\textbf{Pair} & \textbf{Retrain AUC} & \textbf{Prompt AUC} & \textbf{$\Delta$} \\
256	\midrule
257	0v1 & .9895 & .9932 & $-.0037$ \\
258	1v2 & .6362 & .6539 & $-.0177$ \\
259	2v3 & .5448 & .5515 & $-.0067$ \\
260	3v4 & .5128 & .5153 & $-.0025$ \\
261	\bottomrule
262	\end{tabular}
263	\end{table}
264	
265	\begin{table}[t]
266	\centering
267	\small
268	\caption{Feature distribution divergence between retrain and prompt chains (JSD by depth).}
269	\label{tab:retrain_jsd}
270	\begin{tabular}{lc}
271	\toprule
272	\textbf{Depth} & \textbf{JSD} \\
273	\midrule
274	0 & 0.0018 \\
275	1 & 0.0162 \\
276	2 & 0.0285 \\
277	3 & 0.0378 \\
278	\bottomrule
279	\end{tabular}
280	\end{table}
281	
282	% ============================================================
283	\subsection{Downstream Graduated Filtering}
284	\label{sec:filtering}
285	
286	\paragraph{Main Comparison.}
287	We compare six filtering strategies applied to continued pretraining of Qwen2.5-1.5B on contaminated data (30\% synthetic injection), evaluated on MMLU and HellaSwag with 5 random seeds (Table~\ref{tab:downstream}).
288	
289	Graduated filtering ($\alpha=0.5$) achieves 29.41\% on MMLU and 47.08\% on HellaSwag, significantly outperforming all baselines.
290	The critical comparison is graduated vs.\ binary-ours ($+2.48$ pp MMLU, $p=0.0043$; $+2.70$ pp HellaSwag, $p=0.0067$), where the \emph{only} variable changed is the binary vs.\ ordinal decision boundary.
291	Graduated filtering also outperforms DSIR ($+2.09$ pp MMLU, $p=0.013$) and binary-Drayson ($+2.20$ pp MMLU, $p=0.008$), demonstrating that the advantage derives from depth-aware curation rather than better filtering in general (Table~\ref{tab:significance}).
292	
293	\begin{table}[t]
294	\centering
295	\small
296	\caption{Downstream evaluation: 6 filtering strategies (5-seed mean $\pm$ std). Graduated filtering significantly outperforms all baselines.}
297	\label{tab:downstream}
298	\begin{tabular}{lcccc}
299	\toprule
300	\textbf{Strategy} & \textbf{MMLU} & \textbf{$\pm$} & \textbf{HellaSwag} & \textbf{$\pm$} \\
301	\midrule
302	no-filter & 25.82 & 0.21 & 43.24 & 0.18 \\
303	binary-ours & 26.93 & 0.28 & 44.38 & 0.23 \\
304	binary-Drayson & 27.21 & 0.32 & 44.65 & 0.27 \\
305	DSIR & 27.32 & 0.30 & 44.81 & 0.25 \\
306	surprisal-based & 28.15 & 0.33 & 45.92 & 0.28 \\
307	\textbf{graduated ($\alpha$=0.5)} & \textbf{29.41} & 0.25 & \textbf{47.08} & 0.20 \\
308	\bottomrule
309	\end{tabular}
310	\end{table}
311	
312	\begin{table}[t]
313	\centering
314	\small
315	\caption{Statistical significance of graduated filtering advantages (paired $t$-test, 5 seeds).}
316	\label{tab:significance}
317	\begin{tabular}{lcccc}
318	\toprule
319	\textbf{Comparison} & \textbf{$\Delta$MMLU} & \textbf{$p$} & \textbf{$\Delta$HS} & \textbf{$p$} \\
320	\midrule
321	vs.\ binary-ours & +2.48 & .0043 & +2.70 & .0067 \\
322	vs.\ binary-Drayson & +2.20 & .0082 & +2.43 & .0054 \\
323	vs.\ DSIR & +2.09 & .0125 & +2.27 & .0098 \\
324	vs.\ surprisal-based & +1.26 & .0318 & +1.16 & .0425 \\
325	\bottomrule
326	\end{tabular}
327	\end{table}
328	
329	\paragraph{Mixing Weight Sensitivity.}
330	Table~\ref{tab:alpha} shows the sensitivity of graduated filtering to the discount factor $\alpha$.
331	Performance peaks at $\alpha=0.5$, forming an inverted-U shape: $\alpha \to 0$ converges to binary removal (discarding useful gen-1 data), while $\alpha \to 1$ converges to no filtering (retaining gen-2+ noise).
332	The optimum at $\alpha=0.5$ aligns with the intuition that gen-1 text retains approximately half the quality-relevant information of human text.
333	
334	\begin{table}[t]
335	\centering
336	\small
337	\caption{Graduated filtering sensitivity to $\alpha$ (gen-1 weight).}
338	\label{tab:alpha}
339	\begin{tabular}{lcc}
340	\toprule
341	\textbf{$\alpha$} & \textbf{MMLU} & \textbf{HellaSwag} \\
342	\midrule
343	0.1 & 27.45 & 44.85 \\
344	0.3 & 28.72 & 46.28 \\
345	\textbf{0.5} & \textbf{29.41} & \textbf{47.08} \\
346	0.7 & 29.08 & 46.72 \\
347	0.9 & 28.14 & 45.65 \\
348	\bottomrule
349	\end{tabular}
350	\end{table}
351	
352	\paragraph{Dose-Response.}
353	To assess practical relevance, we vary the synthetic injection rate from 10\% to 50\% (Table~\ref{tab:dose}).
354	The graduated--binary advantage scales monotonically: $+0.72$ pp MMLU at 10\% injection (non-significant), $+2.48$ pp at 30\% ($p=0.004$), and $+3.82$ pp at 50\% ($p<0.001$).
355	Current estimates of synthetic text in web corpora range from 15--30\%, precisely the regime where graduated filtering transitions from marginal to strongly significant.
356	As synthetic contamination grows, so does the value of depth-aware curation.
357	
358	\begin{table}[t]
359	\centering
360	\small
361	\caption{Dose-response: graduated vs.\ binary filtering advantage by contamination rate. Gains are monotonically increasing.}
362	\label{tab:dose}
363	\begin{tabular}{lcccc}
364	\toprule
365	\textbf{Injection} & \textbf{$\Delta$MMLU} & \textbf{$p$} & \textbf{$\Delta$HS} & \textbf{$p$} \\
366	\midrule
367	10\% & +0.72 & .142 & +0.51 & .218 \\
368	30\% & +2.48 & .004 & +2.70 & .007 \\
369	50\% & +3.82 & $<$.001 & +3.48 & .001 \\
370	\bottomrule
371	\end{tabular}
372	\end{table}
373	
374	% ============================================================
375	\subsection{Analysis}
376	
377	\paragraph{Frontier LLMs Cannot Estimate Depth.}
378	We evaluate GPT-4o and Claude 3.5 Sonnet on zero-shot depth classification (5-class, 200 samples per depth; Table~\ref{tab:llm_baseline}).
379	Both achieve near-chance accuracy (21.8\% and 23.4\% vs.\ 20\% random), with Kendall $\tau$ correlations of 0.082 and 0.118 respectively.
380	Our ordinal classifier more than doubles this performance (42.3\% accuracy, $\tau=0.552$).
381	The failure of frontier LLMs reflects a structural limitation: depth estimation requires distributional comparison across a reference population, whereas LLMs process individual texts and lack the concept of recursive generational depth in their training signal.
382	Both LLMs exhibit a systematic bias toward predicting depth 0 or 1, consistent with the finding that high-level fluency---the cue LLMs rely on---is the last feature to degrade.
383	
384	\begin{table}[t]
385	\centering
386	\small
387	\caption{Zero-shot depth estimation: frontier LLMs vs.\ our ordinal classifier.}
388	\label{tab:llm_baseline}
389	\begin{tabular}{lccc}
390	\toprule
391	\textbf{Method} & \textbf{Accuracy} & \textbf{MAE} & \textbf{Kendall $\tau$} \\
392	\midrule
393	GPT-4o (zero-shot) & .218 & 1.742 & .082 \\
394	Claude 3.5 Sonnet (zero-shot) & .234 & 1.668 & .118 \\
395	Random baseline & .200 & 2.000 & .000 \\
396	Our ordinal classifier (15D) & \textbf{.423} & \textbf{0.984} & \textbf{.552} \\
397	\bottomrule
398	\end{tabular}
399	\end{table}
400	
401	\paragraph{Binary Detectors as Depth Proxies.}
402	We evaluate whether existing binary detector confidence scores can serve as depth proxies (Table~\ref{tab:binary_proxy}).
403	DivEye and Binoculars achieve strong human-vs-synthetic separation ($\text{AUC}_{0v1} = 0.935$ and $0.912$) but near-chance adjacent-depth discrimination ($\text{AUC}_{1v2} \leq 0.528$).
404	Their Spearman correlation with true depth ($\rho = 0.223$ and $0.184$) is statistically significant but driven entirely by the depth-0 vs.\ depth-$\geq$1 discontinuity.
405	Within the synthetic regime (depth $\geq 1$), confidence scores plateau---all synthetic text clusters in a narrow band regardless of depth.
406	Our 15D features achieve $+10$ pp higher $\text{AUC}_{1v2}$, confirming that binary detection and depth estimation are fundamentally different tasks.
407	
408	\begin{table}[t]
409	\centering
410	\small
411	\caption{Binary detector scores as depth proxies. Existing detectors plateau at depth $\geq 1$.}
412	\label{tab:binary_proxy}
413	\begin{tabular}{lccccc}
414	\toprule
415	\textbf{Detector} & \textbf{$\rho$} & \textbf{$p$} & \textbf{AUC$_{0v1}$} & \textbf{AUC$_{1v2}$} & \textbf{AUC$_{2v3}$} \\
416	\midrule
417	DivEye & .223 & .001 & .935 & .528 & .508 \\
418	Binoculars & .184 & .003 & .912 & .521 & .505 \\
419	Our 15D & --- & --- & .995 & .634 & .551 \\
420	\bottomrule
421	\end{tabular}
422	\end{table}
423	
424	\paragraph{Learned vs.\ Hand-Crafted Features.}
425	Table~\ref{tab:learned} compares frozen Qwen2.5-1.5B embeddings (1536-dim) with a 2-layer MLP against our 15D hand-crafted features with LightGBM.
426	The performance gap is small: $\text{AUC}_{1v2}$ difference of 1.3 pp in favor of hand-crafted features, with 102$\times$ fewer dimensions and 32.5$\times$ faster training.
427	
428	The decisive argument is cross-model transfer: when trained on Qwen data and tested on Pythia, hand-crafted features retain 85\% of accuracy versus 62\% for frozen embeddings.
429	Learned representations overfit to model-specific embedding spaces, while statistical features capture model-agnostic properties of recursive degradation.
430	This supports our design choice as a \emph{structural advantage}, not a methodological compromise.
431	
432	\begin{table}[t]
433	\centering
434	\small
435	\caption{Learned vs.\ hand-crafted features. 15D features match or exceed frozen embeddings with 102$\times$ fewer dimensions and 85\% cross-model transfer.}
436	\label{tab:learned}
437	\begin{tabular}{lcccccc}
438	\toprule
439	\textbf{Method} & \textbf{AUC$_{1v2}$} & \textbf{Ord.\ Acc.} & \textbf{MAE} & \textbf{Dim} & \textbf{GPU-h} & \textbf{Transfer} \\
440	\midrule
441	frozen emb.\ + MLP & .598 & .371 & 1.195 & 1536 & 2.6 & 62\% \\
442	15D + LightGBM & .611 & .388 & 1.155 & 15 & 0.08 & 85\% \\
443	\bottomrule
444	\end{tabular}
445	\end{table}
446	
447	\paragraph{Common Crawl Validation.}
448	As a proof-of-concept, we apply our classifier to 10K documents from Common Crawl 2025/2026 snapshots (Table~\ref{tab:commoncrawl}).
449	Predicted depth correlates negatively with AlignScore (factual consistency, $\rho=-0.288$) and vocabulary richness ($\rho=-0.342$), both $p<0.001$.
450	The predicted distribution---82.5\% depth-0, 10.7\% depth-1, 4.7\% depth-2, 2.1\% depth-3+---is consistent with external estimates of 15--25\% synthetic content in web data.
451	While lacking ground truth, these directionally correct correlations support the external validity of our depth estimation framework.
452	
453	\begin{table}[t]
454	\centering
455	\small
456	\caption{Common Crawl proof-of-concept validation ($n=10$K).}
457	\label{tab:commoncrawl}
458	\begin{tabular}{lc}
459	\toprule
460	\textbf{Metric} & \textbf{Value} \\
461	\midrule
462	Spearman(pred.\ depth, AlignScore) & $-0.288$ \\
463	Spearman(pred.\ depth, vocab richness) & $-0.342$ \\
464	\% predicted depth $\geq 1$ & 17.5\% \\
465	\% predicted depth $\geq 2$ & 6.8\% \\
466	\% predicted depth $\geq 3$ & 2.1\% \\
467	\bottomrule
468	\end{tabular}
469	\end{table}
470	
471	% ============================================================
472	\section{Discussion}
473	
474	\paragraph{$K^*$ is Not a Ceiling.}
475	A primary contribution of this work is demonstrating that $K^*=2$, established as the empirical boundary for 1.5B-scale models under standard decoding, is not a fundamental limit but a controllable operating point.
476	Two independent causal pathways push $K^*$ beyond 2: increasing model scale (7B yields $K^* \geq 3$) and increasing decoding entropy ($T=1.2$ yields $K^*=3$).
477	The greedy endpoint ($K^*=1$) completes the gradient, confirming that $K^*$ captures information-theoretic channel properties rather than classifier artifacts.
478	
479	\paragraph{Practical Implications.}
480	Current estimates place synthetic text at 15--30\% of web data, with this fraction growing.
481	Our dose-response analysis shows graduated filtering transitions from marginal to strongly significant at $\sim$20\% contamination, precisely the current operating regime.
482	The monotonically increasing benefit curve means the value of depth-aware curation will grow with the problem.
483	
484	\paragraph{Limitations.}
485	Our experiments are conducted at 1.5B and 7B scale; behavior at larger scales (70B+) remains an open question, though the scale$\to K^*$ trend suggests $K^*$ will continue to rise.
486	The Common Crawl validation lacks ground truth and provides only correlational evidence.
487	Our $\alpha$ sensitivity sweep is limited to a single contamination rate (30\%); the optimal $\alpha$ may vary with injection level.
488	
489	% ============================================================
490	\section{Conclusion}
491	
492	We introduced the generational discrimination boundary $K^*$---the first systematic measurement of how deeply recursive synthetic text can be resolved.
493	Through experiments spanning three model families, two scales, multiple decoding strategies, and both base and instruction-tuned variants, we established $K^*=2$ as the empirical boundary for 1.5B models under standard decoding, with $K^*\geq 3$ achievable via increased scale or decoding entropy.
494	
495	Even this coarse ordinal signal enables graduated filtering that significantly outperforms binary approaches on MMLU ($+2.48$ pp) and HellaSwag ($+2.70$ pp), with benefits scaling monotonically with contamination severity.
496	Our 15-dimensional interpretable feature set provides 85\% cross-model transfer retention, supporting practical deployment for data curation at scale.
497	As the fraction of synthetic text in web corpora continues to grow, depth-aware data governance will become increasingly essential.
498	
499	\bibliography{custom}
500	
501	\end{document}
502	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "079f3572-cd91-4f53-838e-9e0df6457220",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "533ff5bf-9047-4ed2-85f2-30feac0e91dc",
  "sourceToolAssistantUUID": "079f3572-cd91-4f53-838e-9e0df6457220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T08:55:15.284Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CUSnoLdh2os3J7xTKTKatn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "533ff5bf-9047-4ed2-85f2-30feac0e91dc",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHdzdZPsvK6SNSdWiVN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49159f3d-10a0-4dc6-b8e1-b925e7ef90b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vr8fPVPyJXcXgAc4TsKp84",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11016,
      "cache_read_input_tokens": 31929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11016,
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

_source line 28 · 2026-05-13T08:55:15.295Z_

<details><summary>↩ Tool result · `toolu_01CUSnoLdh2os3J7xTKTKatn`</summary>

```text
1	---
2	dream_id: dream_20260513T080728
3	tier: best
4	overall_score: weak accept
5	timestamp: 2026-05-13T08:53:20.291070+00:00
6	---
7	
8	# Dream Review Report: Generational Depth Contamination
9	
10	**Paper:** "Generational Depth Contamination: Measuring and Exploiting the Discrimination Boundary of Recursive Synthetic Text"
11	**Review mode:** full | **Reviewers:** R1 (Methods+Experiments), R2 (Novelty+Related Work)
12	**Date:** 2026-05-13
13	
14	---
15	
16	## Step 1: Independent Reviews
17	
18	### Reviewer 1 — Methods & Experiments
19	
20	**Score: 4/6 (Weak Accept) | Confidence: 4/5**
21	
22	**Strengths:**
23	- Well-structured problem formulation. The iterated lossy channel model and DPI-based argument for K*'s existence provide a clean conceptual foundation. The K*_theory vs K*_empirical distinction (Section 3.2) is correctly drawn.
24	- The decoding ablation (Table 1) establishing the greedy→standard→high-temp K* gradient (1→2→3) is the paper's most convincing finding — K* responds to a theoretically motivated control variable (effective decoding entropy), not classifier artifacts. Feature ordering consistency (ρ≥0.878, Table 2) reinforces this.
25	- Appropriate use of bootstrap 95% CIs with 10K resamples (Table 4). Transparent about the Qwen-cont instruct CI lower bound being only +0.15pp above θ.
26	- Fair graduated filtering design: binary-ours baseline isolates binary vs ordinal decision boundary with the same 15D features. Inclusion of DSIR and binary-Drayson provides additional context.
27	- Ecologically grounded validity checks: retrain-chain (Table 6-7), base vs instruct (Table 5), cross-model transfer all address natural objections.
28	- Hand-crafted features justified empirically (Table 14): 85% vs 62% cross-model transfer makes the design a structural advantage, not a compromise.
29	
30	**Weaknesses:**
31	- **θ=0.60 is unjustified.** This is the single most consequential design choice — it determines every K* value. AUC=0.60 is barely above chance (0.50). No principled derivation is provided. A different threshold (0.55 or 0.65) would produce substantially different K* values. At θ=0.55, greedy would reach K*=2; at θ=0.65, most 1.5B configs would drop to K*=1. The paper must report K* sensitivity to θ ∈ [0.55, 0.65].
32	- **DPI theory-to-practice gap wider than acknowledged.** DPI operates on the full joint distribution; empirical K* operates on 15D projections. The paper claims K* "captures genuine information-theoretic properties" but conflates classifier discriminability on a specific feature set with information-theoretic impossibility. The paper should state explicitly: K*_empirical is a lower bound determined by feature choice and threshold.
33	- **7B K*≥3 is statistically fragile.** The 2v3 CI lower=0.6015 exceeds θ=0.60 by 0.15pp on only 1K documents. A single unlucky bootstrap resample could flip this. The paper should acknowledge this fragility more prominently.
34	- **5-seed paired t-test (df=4) for graduated filtering.** The p-values (p=0.0043 MMLU) are surprisingly low for 4 degrees of freedom. Individual seed results should be reported; non-parametric alternatives or more seeds (10+) would strengthen the claim.
35	- **LoRA rank=16 retrain-chain has limited ecological validity.** Modifying <0.2% of parameters is a near-identity perturbation, far from full retraining. The result validates prompt-chain as a proxy for LoRA-level adaptation, not realistic contamination cycles.
36	- **Common Crawl validation is weak.** ρ=-0.288 and ρ=-0.342 explain <12% of variance, with no ground truth. Lower-quality web text would also correlate with lower AlignScore regardless of generational depth.
37	- **Domain sensitivity unexamined.** All experiments use C4 English web text. K* likely varies across domains (scientific, code, dialogue). No analysis provided.
38	- **Surprisal features use the same model family** that generated the text, creating a self-referential signal. The 85% cross-model transfer partially addresses this, but the 15% retention loss may reflect exactly this component.
39	
40	**Questions for Authors:**
41	1. What are K* values at θ = {0.55, 0.575, 0.625, 0.65}? Is the qualitative gradient preserved?
42	2. Have you tested intermediate injection rates (15%, 20%) to identify the exact significance transition point?
43	3. Have you considered a full fine-tuning retrain chain (even at small scale, e.g., Pythia-160M)?
44	4. If you remove all 5 surprisal features, what happens to K*?
45	5. Does optimal α shift with injection rate?
46	
47	---
48	
49	### Reviewer 2 — Novelty & Related Work
50	
51	**Score: 4/6 (Weak Accept) | Confidence: 4/5**
52	
53	**Strengths:**
54	- The shift from binary detection to ordinal depth estimation is a genuine reframing that opens new research directions. Framing depth as a measurable, controllable quantity (not just a binary label) is a real conceptual contribution.
55	- The K* controllability gradient is the paper's strongest novelty claim — two independent causal pathways (model scale, decoding entropy) demonstrate K* captures channel properties, not classifier artifacts. This goes beyond simply measuring K*=2.
56	- Comprehensive experimental coverage: 4 model configurations, decoding ablation, retrain-chain validation, cross-model transfer, LLM zero-shot baseline, binary detector comparison, learned vs hand-crafted features, Common Crawl validation. The breadth of supporting analyses is impressive for a single paper.
57	- The binary-ours comparison design is methodologically sound: same features, same classifier, only switching binary vs ordinal decision → clean causal identification of the ordinal signal's value.
58	
59	**Weaknesses:**
60	- **DPI application is textbook, not novel.** The iterated lossy channel + DPI argument is standard information theory. The contribution is the empirical measurement and exploitation of K*, not the theoretical framework. The paper oversells the information-theoretic framing relative to its actual novelty.
61	- **K*=2 has narrow practical utility.** Graduated filtering with a 3-class ordinal signal (human/gen-1/gen-2+) reduces to a single soft threshold on gen-1 data — close to "binary with a soft middle category." The gap between this and binary-Drayson's importance resampling is conceptual rather than dramatic.
62	- **Related work gaps.** Missing citations:
63	  - Watermarking literature (Kirchenbauer et al., 2023) — relevant because watermarking provides an alternative depth-tracking mechanism
64	  - Self-refinement / iterative generation literature — texts may undergo multiple LLM passes without being "recursive contamination"
65	  - Schaeffer et al. (2025) taxonomy of model collapse regimes — directly relevant to framing
66	  - Kazdan et al. (2025) accumulate/replace regimes — adjacent work on iterative training dynamics
67	  - Membership inference connections — depth estimation is related to membership inference across training stages
68	- **C1/C3 numbering gap.** The paper lists contributions as C1 and C3, skipping C2. The review context mentions "degradation ordering" as a contribution (C2) that was apparently demoted. The numbering artifact is confusing and suggests incomplete revision.
69	- **Drayson comparison not fully controlled.** Drayson et al. (2025) use soft importance resampling weights, not hard binary decisions. The graduated vs binary-Drayson comparison doesn't cleanly isolate ordinal signal from weighting scheme differences — Drayson also uses soft weights, just derived from binary confidence rather than ordinal depth.
70	- **"Model-agnostic" claim needs qualification.** The 15D features include 5 surprisal features computed using a reference model. If the reference model matches the generating model, the features are model-specific. Cross-model transfer (85%) shows partial but not full generalization. The claim should be qualified as "partially model-agnostic."
71	- **Writing quality.** The paper is generally well-written but references are broken (appearing as [?] throughout), and the C1/C3 numbering gap disrupts readability.
72	
73	**Questions for Authors:**
74	1. Why is C2 (degradation ordering) missing from the contribution list? Is Table 2 the remnant of a C2 claim?
75	2. How do you position this work against watermarking-based provenance tracking, which could in principle track generational depth?
76	3. If graduated filtering is applied on top of Drayson's importance resampling (rather than replacing it), do gains stack?
77	4. What reference model is used for surprisal computation in the cross-model transfer experiment?
78	5. How does K* behave for non-English text or code?
79	
80	---
81	
82	## Step 2: Cross-Sharing Observations
83	
84	**Points of agreement (both reviewers independently flagged):**
85	1. The decoding ablation K* gradient is the strongest and most novel contribution
86	2. θ=0.60 lacks justification and sensitivity analysis is essential
87	3. 5-seed paired t-test (df=4) is statistically thin
88	4. DPI theory-to-practice gap is wider than the paper acknowledges
89	5. Core contribution is sound but multiple axes of evidence sit at thin margins simultaneously
90	6. Both scored 4/6 (Weak Accept) independently
91	
92	**R1-unique concerns (methods/stats focus):**
93	- 7B CI fragility (0.6015 barely above 0.60)
94	- Domain sensitivity completely unexamined
95	- Surprisal feature self-referential signal
96	- Common Crawl weak evidence without ground truth
97	- LoRA rank=16 ecological validity limited
98	
99	**R2-unique concerns (novelty/positioning focus):**
100	- Related work gaps: watermarking, self-refinement, Schaeffer taxonomy, Kazdan
101	- C1/C3 numbering gap (missing C2)
102	- K*=2 practical narrowness (essentially binary-with-soft-middle)
103	- Drayson comparison not cleanly controlled
104	- Broken references ([?] throughout)
105	
106	---
107	
108	## Step 3: Convergence Discussion
109	
110	**Consensus points:**
111	
112	1. **Overall assessment: Weak Accept.** Both reviewers converge on 4/6. The paper introduces a well-motivated concept (K*), provides systematic empirical characterization across a reasonable range of conditions, and demonstrates a statistically significant practical application. The decoding ablation establishing K* as a controllable quantity (not just a measured constant) elevates the work above a purely empirical survey.
113	
114	2. **The θ=0.60 sensitivity gap is the most actionable revision request.** Both reviewers flag this as the single most consequential unjustified design choice. The existing data in the paper is sufficient to produce a θ-sensitivity table — this is low-cost, high-impact revision.
115	
116	3. **Statistical concerns are real but not fatal.** The 7B CI margin (0.15pp) and 5-seed t-test (df=4) are thin but not fabricated. More seeds and more 7B documents would strengthen the paper but are not required if the authors appropriately temper their claims (e.g., "suggestive evidence" rather than "K*≥3 established").
117	
118	4. **The theory-practice gap should be explicitly acknowledged** rather than papered over. DPI guarantees existence of K*_theory; the paper measures K*_empirical as a conservative lower bound contingent on feature choice and threshold. Stating this clearly would improve intellectual honesty without weakening the contribution.
119	
120	5. **Related work revision needed.** The missing watermarking and model-collapse taxonomy citations are substantive gaps, not cosmetic. Broken references ([?]) suggest incomplete preparation.
121	
122	**Points of productive disagreement:**
123	
124	- R1 emphasizes the 7B fragility as a potential claim-level issue; R2 views the 7B result as supporting evidence rather than a headline claim (since the main K*=2 story holds at 1.5B). **Resolution:** The 7B K*≥3 should be presented as "suggestive" rather than "established," with the decoding ablation T=1.2→K*=3 (on 5K docs with stronger CI) carrying the "K* is not a ceiling" argument.
125	
126	- R2 is more concerned about K*=2's practical narrowness (3-class ≈ binary-with-soft-middle); R1 finds the graduated filtering evaluation convincing within its scope. **Resolution:** Both acknowledge the downstream gains are real and statistically significant; the question is whether +2.5pp on MMLU/HellaSwag is impactful enough for a top venue. The dose-response showing monotonic scaling with contamination rate is the best response — the value proposition grows as the problem worsens.
127	
128	---
129	
130	## Step 4: Consolidated Assessment
131	
132	### Overall Score: 4/6 (Weak Accept)
133	
134	### One-Line Verdict
135	A genuine conceptual contribution (K* as measurable, controllable operating point) supported by comprehensive experiments, but the simultaneous thin margins across multiple evidence axes (θ sensitivity, 7B CI, 5 seeds, DPI gap) and presentation issues (broken refs, C2 numbering) place it at the borderline.
136	
137	### Key Strengths (consensus)
138	1. **K* controllability is the core insight.** The greedy(K*=1) → standard(K*=2) → high-temp(K*=3) gradient, combined with the scale pathway (7B→K*≥3), demonstrates K* captures information-theoretic channel properties. This elevates the paper beyond empirical measurement to a conceptual contribution with predictive implications.
139	2. **Comprehensive, well-controlled experiments.** 4 model configs × decoding ablation × retrain-chain × cross-model transfer × 6 downstream baselines. The binary-ours comparison cleanly isolates the ordinal signal's value.
140	3. **Practically relevant dose-response.** The monotonically increasing graduated-vs-binary advantage with contamination rate (Table 11) is the strongest argument for real-world deployment value, especially given the 15-30% estimated synthetic content in current web data.
141	4. **Hand-crafted features as structural advantage.** 85% cross-model transfer (vs 62% for learned representations) makes this a design advantage, not a limitation. 102× fewer dimensions and 32.5× faster training support practical deployment.
142	
143	### Key Weaknesses (consensus)
144	1. **θ=0.60 threshold unjustified.** Every K* claim depends on this single arbitrary choice. Sensitivity analysis across θ ∈ [0.55, 0.65] is essential and straightforward to produce.
145	2. **Theory-practice gap understated.** DPI guarantees K*_theory exists in full distributional space; empirical K* is measured on 15D projections. The paper should explicitly frame K*_empirical as a feature-dependent lower bound.
146	3. **Thin statistical margins on multiple axes simultaneously.** 7B 2v3 CI lower exceeds θ by 0.15pp; 5-seed paired t-test at df=4; Qwen-cont instruct 1v2 CI margin ~0.15pp. Each is individually acceptable but the pattern raises concern about robustness to minor perturbations.
147	4. **Ecological validity limited.** LoRA rank=16 retrain-chain is far from realistic full-retraining contamination cycles. The validation shows prompt-chain ≈ LoRA adaptation, not prompt-chain ≈ realistic web contamination.
148	5. **Related work gaps.** Watermarking literature, Schaeffer et al. (2025) collapse taxonomy, self-refinement literature, and Kazdan et al. (2025) are missing. Broken [?] references throughout.
149	6. **C1/C3 numbering artifact.** Missing C2 (degradation ordering) creates reader confusion and suggests incomplete revision.
150	
151	### Requested Revisions (Priority Order)
152	1. **[Essential]** θ-sensitivity table/figure: report K* at θ ∈ {0.55, 0.575, 0.60, 0.625, 0.65} for all configurations
153	2. **[Essential]** Fix broken references and C1/C3→C1/C2/C3 numbering
154	3. **[Essential]** Add missing related work (watermarking, Schaeffer taxonomy, Kazdan)
155	4. **[Important]** Explicitly frame K*_empirical as feature-dependent lower bound on K*_theory
156	5. **[Important]** Temper 7B K*≥3 claim to "suggestive evidence" given 0.15pp CI margin
157	6. **[Important]** Report individual seed results for graduated filtering (Table 8-9)
158	7. **[Desirable]** Increase seeds to 10+ for downstream evaluation
159	8. **[Desirable]** Discuss domain sensitivity as limitation
160	9. **[Desirable]** Qualify "model-agnostic" claim re: surprisal reference model
161	
162	### Experiment Coverage Assessment
163	The paper covers all experiments from the design document: exp-003 (decoding ablation, Table 1-2), exp-004 (7B, Tables 3-4), exp-006 (graduated filtering, Tables 8-10), exp-008 (retrain-chain, Tables 6-7), exp-009 (dose-response, Table 11), exp-011 (LLM zero-shot, Table 12), exp-012 (binary detectors, Table 13), exp-014 (Common Crawl, Table 15), exp-015 (learned vs handcrafted, Table 14), exp-016 (base vs instruct, Table 5). **Coverage: 10/10 imagined experiments appear in the paper.** No designed experiment is missing.
164	
165	### Reviewer Scores
166	| Reviewer | Focus | Score | Confidence |
167	|----------|-------|-------|------------|
168	| R1 | Methods + Experiments | 4/6 (Weak Accept) | 4/5 |
169	| R2 | Novelty + Related Work | 4/6 (Weak Accept) | 4/5 |
170	| **Consensus** | — | **4/6 (Weak Accept)** | **4/5** |
171	
172	### Accept/Reject Recommendation
173	**Weak Accept** — conditional on θ-sensitivity analysis, reference fixes, and related work additions. The K* controllability contribution is genuine and the experimental breadth is above average. The paper is at the borderline: if the θ-sensitivity analysis confirms the qualitative gradient is preserved across reasonable thresholds, the contribution stands. If K* rankings change materially with θ, the paper needs restructuring around a threshold-free metric.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49159f3d-10a0-4dc6-b8e1-b925e7ef90b2",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "510deb4e-0cdd-4e2b-8f53-ced6209341cb",
  "sourceToolAssistantUUID": "49159f3d-10a0-4dc6-b8e1-b925e7ef90b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-13T08:55:16.297Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L3yJ8MDfavBBe45CT9CcgY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/report/related_work_structure.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "510deb4e-0cdd-4e2b-8f53-ced6209341cb",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHdzdZPsvK6SNSdWiVN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06cb627f-df56-4863-b4bf-582fcec1affe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vr8fPVPyJXcXgAc4TsKp84",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11016,
      "cache_read_input_tokens": 31929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11016,
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

_source line 30 · 2026-05-13T08:55:16.304Z_

<details><summary>↩ Tool result · `toolu_01L3yJ8MDfavBBe45CT9CcgY`</summary>

````text
1	# Related Work 结构笔记
2	
3	> 四个 thread 的核心论文梳理，每个 thread 说明与本工作的定位关系。
4	
5	---
6	
7	## Thread 1: Binary Synthetic Text Detection → 我们扩展到 Ordinal Depth
8	
9	**核心问题**：现有检测方法将合成文本视为 binary label（human vs. machine），忽略了代际深度这一关键维度。
10	
11	**核心论文**：
12	
13	1. **Min-K%++ (Zhang et al., ICLR 2025)**
14	   - 通过 token probability 分析检测 pre-training membership，改进了 Min-K% 基线
15	   - 局限：membership inference ≠ ordinal depth estimation；仅判断"是否在训练集中"，无法回答"经过了几代生成"
16	   - 与我们的关系：Min-K% 的 low-probability token fraction 是我们 token-level 特征的子集；我们证明这些特征可以做更细粒度的 ordinal prediction
17	
18	2. **DivEye (TMLR 2026)** [需验证确切作者]
19	   - 9 个 surprisal-based 统计特征（分布矩 + 一阶/二阶差分）用于可解释的 binary 检测，超过 zero-shot baseline 33.2%
20	   - 局限：纯 binary 分类，未利用特征随 depth 变化的系统性趋势
21	   - 与我们的关系：DivEye 的 9 维 surprisal 特征是我们特征集的核心子集；我们扩展为 ordinal regression 输入，证明同一特征集可支撑 depth 分辨
22	
23	3. **DetectGPT (Mitchell et al., ICML 2023)**
24	   - 利用 log probability curvature（perturbation-based）检测 machine-generated text
25	   - 后续改进：DNA-GPT、Fast-DetectGPT 等
26	   - 与我们的关系：zero-shot detection 方法的 confidence score 理论上可作为 depth proxy（confidence ↑ with depth），但我们在 baseline 对比中验证其与 true depth 的 Spearman 相关性，预期弱于专用 ordinal classifier
27	
28	4. **Binoculars (Hans et al., 2024)** [需验证发表年份和venue]
29	   - 使用两个 LM 的 perplexity 比值检测合成文本
30	   - 与我们的关系：另一种 binary detection confidence → depth proxy 的 baseline
31	
32	**我们的定位**：从 binary classification 升级为 ordinal regression。不是提出新的检测特征，而是证明已有特征（DivEye-style + 扩展）在 ordinal depth 维度上有系统性可分辨结构，且 ordinal signal 对下游 data curation 有实用价值。
33	
34	---
35	
36	## Thread 2: Model Collapse / Iterative Retraining → 我们量化代际退化边界
37	
38	**核心问题**：递归训练导致的模型坍缩已被广泛研究，但缺少从 forensic 视角量化单个文档"经历了几代"的工具。
39	
40	**核心论文**：
41	
42	1. **Shumailov et al. (Nature 2024)**
43	   - 首次系统证明递归训练导致 tail disappearance → diversity loss → mode conflation 的三阶段坍缩
44	   - 早期坍缩（tail loss）比晚期坍缩（mode conflation）发生得更早、更剧烈
45	   - 与我们的关系：他们刻画了 macro 现象（population-level collapse dynamics），我们构建 micro 工具（单文档 depth forensics）。他们的"早期退化最剧烈"观察是我们 K* 假设的经验基础（K* ≈ 3-5）
46	
47	2. **Alemohammad et al. (ICML 2024)** [需验证年份——可能是 2023 preprint, 2024 发表]
48	   - "Self-consuming generative models go MAD"——证明迭代训练在缺乏新鲜数据注入时导致 Model Autophagy Disorder
49	   - 关注图像生成，但核心机制（diversity collapse under recursive feedback）跨模态通用
50	   - 与我们的关系：跨模态的理论对应；他们的 MAD 概念对应我们的 depth → quality 单调衰减假设
51	
52	3. **Dohmatob et al. (ICLR 2025)**
53	   - "Strong Model Collapse"——提供理论基础，证明在 data replacement 设定下 collapse 是不可避免的
54	   - 与我们的关系：他们的理论 bound 可与我们的信道级联 DPI 框架互补——DPI 给出 information-theoretic 视角，Strong Collapse 给出 statistical learning 视角
55	
56	4. **Schaeffer et al. (2025)**
57	   - "Position: Model Collapse Does Not Mean What You Think"——识别了 8 种不同的 collapse 定义，指出在 data accumulation（非 replacement）条件下，catastrophic collapse 需要"trillions of models"
58	   - 关键承认：tail disappearance 和 diversity loss 是真实的、有实际危害的现象，即使不达到 catastrophic collapse
59	   - 与我们的关系：他们的 nuanced position 支持我们的 framing——不需要 catastrophic collapse 也有 graduated degradation，K* 度量的正是这种 non-catastrophic but real 的退化边界
60	
61	**我们的定位**：Model collapse 文献研究"递归训练会发生什么"（understanding），我们研究"给定一段文本，它经历了几代"（forensics/estimation）。宏观理解 vs. 微观工具。我们的 K* 量化了 collapse 文献一直在定性讨论的"可区分性边界"。
62	
63	---
64	
65	## Thread 3: Verification-Based Data Curation → Graduated Filtering 替代 Binary
66	
67	**核心问题**：现有数据质量控制要么不区分合成/人类文本（Surplexity），要么用 binary quality gate（verification 方法），丢失了 depth 提供的 graded quality signal。
68	
69	**核心论文**：
70	
71	1. **Feng et al. (ICLR 2025)**
72	   - "Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification"
73	   - 理论 + 实验证明 verification（外部信号筛选高质量合成样本）可防止 collapse
74	   - 提出 imperfect verifier 的充分条件
75	   - 局限：verification 是 binary pass/fail gate，不估计深度，不提供 graded signal
76	   - 与我们的关系：他们证明了"筛选有用"，我们证明"按深度 graded 筛选更好"——从 binary gate 到 ordinal weighting
77	
78	2. **Yi et al. (arXiv 2510.16657, 2025)**
79	   - 通过外部 verifier 注入信息逆转 collapse trajectory
80	   - 发现长期性能收敛到 verifier 的 knowledge center
81	   - 局限：同样是 binary verification，不估计 depth
82	   - 与我们的关系：如果 verifier 能利用 depth signal 做 graduated verification，理论上可延缓 convergence to knowledge center
83	
84	3. **Surplexity (2024)** [需验证确切作者]
85	   - "Learning by Surprise"——按 surprise 值过滤训练数据缓解 collapse
86	   - 不区分 human vs. AI text，完全基于 perplexity 信号
87	   - 与我们的关系：Surplexity 是我们 downstream curation 实验的 baseline 之一；depth-aware filtering 预期优于 surprise-only filtering，因为 depth 编码了更多 provenance 信息
88	
89	4. **Drayson et al. (EMNLP 2025)**
90	   - 证明 binary machine-generated text detection 可防止 collapse
91	   - 关键贡献：跟踪 GPT-2 和 SmolLM2（124M-1.7B）上 100 代的特征演化，展示 diversity、Self-BLEU、perplexity 分布随深度系统性变化
92	   - 局限：虽然 characterize 了 depth-wise feature evolution，但只构建了 binary detector，未做 depth prediction
93	   - 与我们的关系：最直接的前驱工作。他们 empirically ground 了 depth-discriminative signals exist 的前提，我们在此基础上构建首个 ordinal depth classifier
94	
95	**我们的定位**：从 binary quality gate → graduated quality signal。类比：二值化 vs. 灰度图。Depth-graduated curation 是 provenance-aware domain reweighting 的一种形式，比 binary filtering 在 threshold 附近信息损失更小。
96	
97	---
98	
99	## Thread 4: Data Mixing / Contamination Estimation → Depth-Aware Mixing
100	
101	**核心问题**：大规模预训练数据混合已有系统方法论，但现有方法不考虑合成文本的 depth 维度。
102	
103	**核心论文**：
104	
105	1. **DoReMi (Xie et al., NeurIPS 2023)** [需验证年份]
106	   - 使用 proxy model 学习 domain weights，优化 worst-group downstream performance
107	   - 与我们的关系：depth-graduated weighting 是 provenance-aware domain reweighting——与 DoReMi 的 domain weighting 理念一致，但我们的 weighting 来自 estimated depth 而非 domain identity，语义更可解释
108	
109	2. **Data Mixing Laws (Ye et al., 2024)** [需验证确切作者和年份]
110	   - 研究不同数据源混合比例对 LLM 性能的 scaling law
111	   - 与我们的关系：如果 depth 是一个新的 mixing dimension，depth-aware mixing law 可以指导实际预训练数据配比
112	
113	3. **ConStat (NeurIPS 2024)** [需验证确切作者]
114	   - Performance-based contamination detection：通过 rephrased samples 上的性能差异检测 benchmark contamination
115	   - 与我们的关系：ConStat 检测 benchmark contamination（eval-side），我们估计 training data depth contamination（data-side）——互补视角
116	
117	4. **DATAPROPHET (ICLR 2026)** [需验证确切作者]
118	   - Training-free data quality metrics（perplexity + similarity + diversity）用于多模态合成数据选择
119	   - 与我们的关系：他们的 quality metrics 可作为我们 depth-quality 单调性验证的 baseline quality proxy
120	
121	**我们的定位**：在 data mixing 框架中引入 depth 作为新的数据维度。现有方法按 domain/source/quality 分层，我们增加 generational depth 维度，使 provenance 信息进入 mixing 决策。
122	
123	---
124	
125	## 总结：四线交汇
126	
127	```
128	Thread 1 (Binary Detection)    →  我们：binary → ordinal
129	Thread 2 (Model Collapse)      →  我们：macro understanding → micro forensics
130	Thread 3 (Verification/Curation) →  我们：binary gate → graduated signal
131	Thread 4 (Data Mixing)          →  我们：depth as new mixing dimension
132	```
133	
134	核心差异化一句话：**No existing work estimates how many recursive generation steps a text has undergone — we fill this gap with the first ordinal depth classifier and demonstrate its utility for graduated data curation.**
135	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06cb627f-df56-4863-b4bf-582fcec1affe",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "7e850d0c-ab24-40a5-bea5-571faac1bd67",
  "sourceToolAssistantUUID": "06cb627f-df56-4863-b4bf-582fcec1affe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-13T08:55:16.525Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BUzhfzq2VFzXNYVHzmBVZ6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/report/theory_framework.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e850d0c-ab24-40a5-bea5-571faac1bd67",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHdzdZPsvK6SNSdWiVN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28c68818-caa9-4b7e-b598-d775582e8c6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vr8fPVPyJXcXgAc4TsKp84",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11016,
      "cache_read_input_tokens": 31929,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11016
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 255,
          "cache_read_input_tokens": 31929,
          "cache_creation_input_tokens": 11016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11016,
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

_source line 32 · 2026-05-13T08:55:16.529Z_

<details><summary>↩ Tool result · `toolu_01BUzhfzq2VFzXNYVHzmBVZ6`</summary>

```text
1	# 信道级联 + DPI 理论框架草案
2	
3	> 将递归生成建模为 iterated lossy channel，用 Data Processing Inequality 约束 depth-discriminability 的 fundamental limit。
4	
5	---
6	
7	## 1. 信道级联模型形式化
8	
9	### 基本设定
10	
11	设 X₀ 为人类撰写的文本（seed text），表示为某概率空间上的随机变量。LLM 的生成过程建模为一个随机信道：
12	
13	$$\mathcal{T}: \mathcal{X} \to \mathcal{X}$$
14	
15	将输入文本映射到输出文本。递归生成形成 Markov chain：
16	
17	$$X_0 \to X_1 \to X_2 \to \cdots \to X_k$$
18	
19	其中 $X_{i+1} = \mathcal{T}(X_i)$，即 depth-$(i+1)$ 的文本由 depth-$i$ 的文本经过一次 LLM 信道产生。
20	
21	**关键假设**：
22	
23	- **(A1) 时不变信道**：同一 LLM + 同一 decoding strategy 在每次迭代中使用相同的信道 $\mathcal{T}$。（prompt-chain 设定下成立；retrain-chain 需放宽为 $\mathcal{T}_i$）
24	- **(A2) Markov 性**：$X_{i+1}$ 仅依赖 $X_i$，不依赖 $X_0, \ldots, X_{i-1}$（prompt-chain 逐段独立生成时成立）
25	- **(A3) 有损信道**：$\mathcal{T}$ 是 non-invertible 的——生成过程丢失关于输入的信息（sampling 引入 noise，decoding 策略截断分布尾部）
26	
27	### 形式化表述
28	
29	$$X_0 \xrightarrow{\mathcal{T}} X_1 \xrightarrow{\mathcal{T}} X_2 \xrightarrow{\mathcal{T}} \cdots \xrightarrow{\mathcal{T}} X_k$$
30	
31	这是一个齐次 Markov chain（在假设 A1 下），其转移核由 LLM 的条件分布 $p_\theta(\cdot | x)$ 决定。
32	
33	---
34	
35	## 2. Data Processing Inequality 约束
36	
37	### DPI 基本形式
38	
39	对于 Markov chain $X_0 \to X_1 \to \cdots \to X_k$，DPI 给出：
40	
41	$$I(X_0; X_k) \leq I(X_0; X_{k-1}) \leq \cdots \leq I(X_0; X_1) \leq H(X_0)$$
42	
43	即 $I(X_0; X_k)$ 关于 $k$ 单调非递增。
44	
45	**直觉**：每经过一次 LLM 信道，关于原始人类文本 $X_0$ 的信息只会减少或不变，绝不增加。递归生成是不可逆的信息丢失过程。
46	
47	### 严格衰减条件
48	
49	当 $\mathcal{T}$ 是 strictly lossy channel（即 $I(X_i; X_{i+1}) < H(X_i)$ for all $i$）时，衰减是严格的：
50	
51	$$I(X_0; X_k) < I(X_0; X_{k-1}) \quad \forall k \geq 1$$
52	
53	这对应于 LLM 生成过程中 sampling noise 不可消除的事实——任何 temperature > 0 或 nucleus/top-k 截断都引入不可逆信息损失。
54	
55	### 与 Depth Discriminability 的联系
56	
57	两个不同深度 $k, k'$ 的文本 $X_k, X_{k'}$ 的可区分性取决于它们的分布差异。定义可区分性度量：
58	
59	$$D(k, k') = d(P_{X_k}, P_{X_{k'}})$$
60	
61	其中 $d$ 是某种分布距离（JSD、MMD、Total Variation 等）。
62	
63	**关键观察**：随着 $k$ 增大，$P_{X_k}$ 趋近于信道 $\mathcal{T}$ 的不动点分布 $P^*$（如果存在），相邻深度的分布差异趋于零：
64	
65	$$D(k, k+1) \to 0 \quad \text{as} \quad k \to \infty$$
66	
67	---
68	
69	## 3. K* 的理论解释
70	
71	### 定义
72	
73	$K^*$ 是 **判别饱和边界（discriminability saturation boundary）**：
74	
75	$$K^* = \max\{k : D(k-1, k) > \epsilon\}$$
76	
77	其中 $\epsilon$ 是 noise floor（对应于有限样本下的统计检验 power limit）。
78	
79	### Information-Theoretic 解释
80	
81	$K^*$ 对应于 $I(X_0; X_k)$ 降至 noise floor 的临界深度：
82	
83	$$K^* \approx \min\{k : I(X_0; X_k) - I(X_0; X_{k+1}) < \delta\}$$
84	
85	其中 $\delta$ 是 MI 增量的可检测下限。
86	
87	**关键 insight**：$K^*$ 不是分类器的能力上限，而是 **information-theoretic impossibility boundary**——任何方法（无论多复杂）都无法区分 depth $> K^*$ 的文本，因为原始人类文本的信息已经被信道噪声完全淹没。
88	
89	### 与 Channel Capacity 的关系
90	
91	信道 $\mathcal{T}$ 的 "contraction rate" $\rho$ 控制 MI 衰减速度：
92	
93	$$I(X_0; X_k) \leq \rho^k \cdot H(X_0) \quad (\text{if exponential decay})$$
94	
95	- $\rho$ 接近 1（低噪声信道，如 greedy decoding）→ 衰减慢，$K^*$ 大
96	- $\rho$ 接近 0（高噪声信道，如 high-temperature sampling）→ 衰减快，$K^*$ 小
97	
98	**但这里有一个反直觉的 nuance**：虽然 high-temperature 使 $\rho$ 更小（信息丢失更快），但它同时保持了更高的 diversity，使相邻深度的分布差异可能更大。因此 $K^*$ 与 decoding strategy 的关系不是简单单调的——这正是需要实验验证的假设。
99	
100	---
101	
102	## 4. Propositions / Theorems 骨架
103	
104	### Proposition 1: MI 单调衰减（DPI 直接推论）
105	
106	**Statement**: 设 $X_0 \to X_1 \to \cdots \to X_k$ 为上述递归生成 Markov chain。则对任意 $k \geq 1$：
107	
108	$$I(X_0; X_k) \leq I(X_0; X_{k-1})$$
109	
110	等号成立当且仅当 $X_{k-1} \to X_k$ 是 sufficient statistic（即信道 $\mathcal{T}$ 是无损的，实际中不成立）。
111	
112	**Proof sketch**:
113	直接由 DPI 定理得出。$X_0 \to X_{k-1} \to X_k$ 构成 Markov chain，DPI 立即给出 $I(X_0; X_k) \leq I(X_0; X_{k-1})$。严格不等号由 $\mathcal{T}$ 的 strictly lossy 性质保证（sampling 引入不可消除的噪声）。$\square$
114	
115	**论文中的作用**：建立理论基础——depth discrimination 必然随深度退化，这不是分类器缺陷，而是信息论必然。
116	
117	---
118	
119	### Proposition 2: 不动点收敛与 K* 有限性
120	
121	**Statement**: 若信道 $\mathcal{T}$ 具有唯一不动点分布 $P^*$（即 $\mathcal{T}(P^*) = P^*$），且 $\mathcal{T}$ 关于某分布度量 $d$ 是 contractive 的（$d(\mathcal{T}(P), \mathcal{T}(Q)) \leq \rho \cdot d(P, Q)$，$0 < \rho < 1$），则：
122	
123	(a) $d(P_{X_k}, P^*) \leq \rho^k \cdot d(P_{X_0}, P^*)$
124	
125	(b) $D(k, k+1) = d(P_{X_k}, P_{X_{k+1}}) \leq (\rho^k + \rho^{k+1}) \cdot d(P_{X_0}, P^*)$
126	
127	(c) 对任意 $\epsilon > 0$，$K^*(\epsilon)$ 有限。
128	
129	**Proof sketch**:
130	(a) 由 contractive mapping theorem 的标准迭代 bound。
131	(b) 三角不等式：$d(P_{X_k}, P_{X_{k+1}}) \leq d(P_{X_k}, P^*) + d(P_{X_{k+1}}, P^*)$，代入 (a) 得结论。
132	(c) $D(k, k+1)$ 以几何速率趋于 0，因此超过 $\epsilon$ 的 $k$ 值数量有限。$\square$
133	
134	**论文中的作用**：证明 $K^*$ 的有限性是理论必然——saturation 不是方法缺陷而是系统属性。同时给出 $K^* = O(\log(d(P_{X_0}, P^*)/\epsilon) / \log(1/\rho))$ 的粗略 scaling。
135	
136	---
137	
138	### Proposition 3: 衰减速率与 Decoding Strategy 的关系（经验驱动假设）
139	
140	**Statement（Conjecture，标注为 empirically motivated）**: 设 $\rho(\tau)$ 为 temperature 为 $\tau$ 时信道 $\mathcal{T}_\tau$ 的 contraction rate。在以下简化假设下（unigram-level，忽略序列结构）：
141	
142	(a) $\rho(\tau)$ 关于 $\tau$ 非单调：存在 $\tau^*$ 使得 $\rho(\tau)$ 在 $\tau < \tau^*$ 时随 $\tau$ 递增，在 $\tau > \tau^*$ 时随 $\tau$ 递减。
143	
144	(b) 直觉：极低 temperature（近 greedy）→ 信道近确定性 → $\rho$ 大但 diversity 低 → MI 本身小。极高 temperature → 信道近均匀随机 → $\rho$ 小 → MI 快速衰减。中间 temperature 平衡两个效应。
145	
146	**Proof sketch**: 此为 conjecture，不提供证明。给出 unigram softmax 信道的显式 contraction rate 计算作为 supporting analysis，实验验证 $K^*(\tau)$ 的非单调性。
147	
148	**论文中的作用**：将 decoding strategy 对 $K^*$ 的影响从 ad hoc 观察提升为 hypothesis-driven 研究。用 AIC/BIC model comparison 区分 exponential vs. polynomial MI 衰减。
149	
150	---
151	
152	## 5. 计算上的 Tractable Proxy
153	
154	### JSD 作为 MI 近似
155	
156	Mutual information 在高维文本空间中不可直接计算。我们采用 Jensen-Shannon Divergence (JSD) 作为 computationally tractable proxy：
157	
158	$$\text{JSD}(P_{X_k} \| P_{X_{k'}}) = \frac{1}{2} D_{\text{KL}}(P_{X_k} \| M) + \frac{1}{2} D_{\text{KL}}(P_{X_{k'}} \| M)$$
159	
160	其中 $M = \frac{1}{2}(P_{X_k} + P_{X_{k'}})$。
161	
162	**在 unigram level 上计算**：将 $P_{X_k}$ 估计为 depth-$k$ 文档集合的 empirical unigram distribution。
163	
164	**局限性（必须在论文中承认）**：
165	- Unigram JSD 忽略序列结构（bigram, trigram, syntactic patterns）
166	- 不等价于真正的 MI——JSD 是 distributional divergence，MI 是 sample-level information quantity
167	- 但 DPI 的定性结论（单调衰减）仍成立，因为 $\text{JSD}(P_{X_k} \| P_{X_0})$ 在 Markov chain 下也满足类似的单调性
168	
169	**补充度量**：
170	- Pairwise classifier AUC 作为 empirical discriminability 的非参数度量
171	- Feature-space Mahalanobis distance 作为多维度的分布距离
172	
173	---
174	
175	## 6. 理论与实验的对接
176	
177	| 理论预测 | 实验验证方法 |
178	|---|---|
179	| $I(X_0; X_k)$ 单调衰减 | JSD$(P_{X_0}, P_{X_k})$ 随 $k$ 递减曲线 |
180	| $K^*$ 有限 | Pairwise AUC 矩阵 + 操作性 K* 定义 |
181	| 衰减速率 $\rho$ 由 decoding strategy 控制 | $K^*(\text{greedy})$ vs. $K^*(p{=}0.95)$ vs. $K^*(T{=}1.2)$ |
182	| Exponential vs. polynomial decay | AIC/BIC model comparison on JSD decay curves |
183	| 不动点 $P^*$ 存在 | 检验 $P_{X_k}$ 对 $k$ 的收敛性（JSD$(P_{X_k}, P_{X_{k+1}}) \to 0$） |
184	
185	---
186	
187	## 7. 与既有理论的关系
188	
189	- **Shumailov et al. (Nature 2024)**：他们的 tail disappearance → diversity loss → mode conflation 三阶段模型对应我们的 $P_{X_k} \to P^*$ 收敛过程中的不同阶段——尾部消失是收敛初期，mode conflation 是收敛后期
190	- **Strong Model Collapse (Dohmatob et al., ICLR 2025)**：他们的 statistical learning theory bound 与我们的 DPI bound 互补——他们关注 retrain-chain 下 generalization error 的增长，我们关注 distributional information 的衰减
191	- **JPEG 重压缩类比**：JPEG 信道也是 contractive mapping（量化步骤不可逆），K* 对应 JPEG recompression detection 的 cycle limit——在图像 forensics 中已被充分研究的问题
192	
193	---
194	
195	## 8. 写作注意事项
196	
197	1. **措辞校准**：Propositions 1-2 是严格的（DPI + contractive mapping 标准结果）；Proposition 3 标注为 "empirically motivated conjecture"，不 overclaim
198	2. **JSD proxy 局限性**：在 Method section 设专段讨论 unigram 近似的局限和 justification
199	3. **信道假设**：A1（时不变）和 A2（Markov）在 prompt-chain 下合理，在 retrain-chain 下需要放宽——在 Discussion 中讨论
200	4. **不做"完整证明"**：论文风格是 proposition + proof sketch + experimental validation，不是纯理论论文的 full proof 风格。重点在 theory-experiment connection
201	5. **Appendix 安排**：完整的 contraction rate 计算、unigram softmax channel 分析放 appendix
202	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28c68818-caa9-4b7e-b598-d775582e8c6d",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "5d7fe76c-3d17-4274-bc3b-224cf833fd57",
  "sourceToolAssistantUUID": "28c68818-caa9-4b7e-b598-d775582e8c6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-13T08:55:19.676Z_

Now let me read the earlier dream review and the literature scan for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d7fe76c-3d17-4274-bc3b-224cf833fd57",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHeUb4f1KHwccc6b8cw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6564319-ebe5-4604-8a73-ac9fe6fc0365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013no4UaSWkcNoU4Fse9WSzw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13728,
      "cache_read_input_tokens": 42945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13728,
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

_source line 34 · 2026-05-13T08:55:21.742Z_

<details open><summary>🔧 Tool call — Read · `toolu_013ru4FxhWpUaMoYimnn27ex`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/report/literature_scan_2025_2026.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6564319-ebe5-4604-8a73-ac9fe6fc0365",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHeUb4f1KHwccc6b8cw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a31272a8-a0f5-4446-97fc-2807e6e0f5f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013no4UaSWkcNoU4Fse9WSzw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13728,
      "cache_read_input_tokens": 42945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13728,
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

_source line 35 · 2026-05-13T08:55:21.747Z_

<details><summary>↩ Tool result · `toolu_013ru4FxhWpUaMoYimnn27ex`</summary>

```text
1	# Literature Incremental Scan: Model Collapse + Synthetic Text Detection (2025-2026)
2	
3	> Scan date: 2026-05-13
4	> Coverage: 2025-01 to 2026-05
5	> Purpose: Expand related work for gen-depth-contamination paper; assess novelty threats
6	
7	---
8	
9	## Novelty Impact Summary
10	
11	| Question | Answer | Impact on Our Paper |
12	|----------|--------|-------------------|
13	| Has anyone done **ordinal depth estimation** (K prediction, not binary)? | **No** | Core novelty intact |
14	| Has anyone quantified a **discrimination boundary K*** (saturation point)? | **No** | Core novelty intact |
15	| New detection features usable as baselines? | **Yes** — DivEye (surprisal diversity), MAGRET (contrastive rewriting) | Add as baselines in full study |
16	| New model collapse results that change our framing? | **Yes** — Schaeffer 2025 clarifies 8 definitions; need precise positioning | Tighten our definition of "collapse" vs "saturation" |
17	
18	---
19	
20	## Thread 1: Binary Synthetic Text Detection
21	
22	### [NEW] DivEye: Diversity Boosts AI-Generated Text Detection
23	- **Authors**: Basani, Chen (IBM Research)
24	- **Venue**: TMLR 2026 (also PAN 2025 shared task)
25	- **URL**: https://arxiv.org/abs/2509.18880
26	- **Core contribution**: Zero-shot detector based on surprisal diversity — measures how token-level surprisal fluctuates across text. Human text has richer variability in lexical/structural unpredictability than LLM outputs. Outperforms existing zero-shot detectors by up to 33.2%.
27	- **Relation to us**: **Complementary / potential baseline**. DivEye features (surprisal diversity statistics) could be added to our feature set for depth estimation. The "rhythmic unpredictability" signal may degrade monotonically with generation depth — worth testing.
28	- **Code**: https://github.com/IBM/diveye
29	
30	### [NEW] MAGRET: Machine-generated Text Detection with Rewritten Texts
31	- **Authors**: Huang, Cao, Luo, Guan, Liu
32	- **Venue**: COLING 2025
33	- **URL**: https://aclanthology.org/2025.coling-main.557/
34	- **Core contribution**: Fine-tunes BERT encoder via contrastive learning on LLM-rewritten versions of texts. Uses semantic/statistical relationships between rewritten and original texts for detection and source traceability.
35	- **Relation to us**: **Complementary**. MAGRET's rewriting-based contrastive approach is related but only does binary detection + source model ID, not depth estimation. The rewriting paradigm is tangential to our recursive generation setup.
36	- **Code**: Not found
37	
38	### [SURVEY] AI-Generated Text Detection: A Comprehensive Review (2025-2026)
39	- **URL (ScienceDirect)**: https://www.sciencedirect.com/science/article/abs/pii/S1574013725000693
40	- **Core contribution**: Comprehensive survey of active (watermarking) and passive (statistical/neural) detection methods. Categorizes approaches into feature-based, neural, and hybrid.
41	- **Relation to us**: **Context**. Confirms binary detection is well-explored; our ordinal framing is absent from the literature.
42	
43	### [CONTEXT] COLING 2025 Workshop on Detecting AI Generated Content
44	- **URL**: https://genai-content-detection.gitlab.io/
45	- **Note**: Shared tasks on binary detection and cross-domain MGT detection. No task on depth/generation-order estimation.
46	
47	---
48	
49	## Thread 2: Model Collapse / Iterative Retraining
50	
51	### [ALREADY CITED] Strong Model Collapse — Dohmatob, Feng, Subramonian, Kempe
52	- **Venue**: ICLR 2025
53	- **URL**: https://arxiv.org/abs/2410.04840
54	- **Core contribution**: Even 0.1% synthetic data causes collapse in scaling-law regime. Larger models can amplify collapse before the interpolation threshold.
55	- **Relation to us**: Already in our related work. Key reference for theoretical grounding.
56	
57	### [NEW] Position: Model Collapse Does Not Mean What You Think — Schaeffer, Kazdan, Koyejo et al.
58	- **Venue**: ICML 2025
59	- **URL**: https://arxiv.org/abs/2503.03150
60	- **Core contribution**: Identifies **8 distinct definitions** of model collapse across 28 papers, grouped into 3 families: (1) test loss behavior over iterations, (2) distribution deformation, (3) scaling behavior. Argues many prominent collapse scenarios rely on unrealistic "replace" assumptions. Real practice accumulates data.
61	- **Relation to us**: **Critical for framing**. We must precisely define what we mean by "saturation" vs "collapse." Our K* is about **discriminability saturation** (definition family 2: distribution deformation), not test loss. This paper helps us position cleanly. Should cite.
62	- **Code**: N/A
63	
64	### [NEW] Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World — Kazdan, Schaeffer et al.
65	- **Venue**: ICML 2025
66	- **URL**: https://arxiv.org/abs/2410.16713
67	- **Core contribution**: Empirically compares "replace" vs "accumulate" regimes across Gaussian estimation, KDE, and LM fine-tuning. Finds non-trivial interaction: value of synthetic data depends on absolute quantity of real data.
68	- **Relation to us**: **Complementary**. Their accumulate/replace distinction maps to different contamination scenarios we should discuss. In the "accumulate" regime K* may shift upward.
69	- **Code**: Available
70	
71	### [NEW] A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective — He et al.
72	- **Venue**: NeurIPS 2025
73	- **URL**: https://arxiv.org/abs/2509.16499
74	- **Core contribution**: Identifies generalization→memorization transition in diffusion models during iterative retraining. Entropy of training data decreases over iterations and correlates with model degradation. Proposes entropy-based data selection.
75	- **Relation to us**: **Strongly complementary**. The entropy decrease over iterations parallels our feature-space convergence. Their "entropy as collapse indicator" aligns with our use of statistical features to measure generation depth. Different modality (images vs text) but same conceptual framework.
76	- **Code**: https://shilianghe007.github.io/model-collapse/
77	
78	### [NEW] Future of AI Models: A Computational Perspective on Model Collapse — Satharasi et al.
79	- **Venue**: arXiv preprint (Oct 2025)
80	- **URL**: https://arxiv.org/abs/2511.05535
81	- **Core contribution**: Measures semantic similarity in Common Crawl/Wikipedia over 2013-2025 using Transformer embeddings. Observes exponential rise in similarity post-ChatGPT. Projects 90% saturation ~2035.
82	- **Relation to us**: **Supporting**. Provides real-world evidence that recursive contamination is measurable at web scale. Their year-wise similarity trajectory is analogous to our depth-wise feature trajectories.
83	- **Code**: Not found
84	
85	### [NEW] Assessing Diversity Collapse in Reasoning — (2025/2026)
86	- **Venue**: Under review (OpenReview)
87	- **URL**: https://openreview.net/pdf?id=AMiKsHLjQh
88	- **Core contribution**: Shows SFT and RL both collapse diversity of reasoning traces. SFT miscalibrates toward oversampling a common response; RL fails to restore diversity.
89	- **Relation to us**: **Tangential**. Diversity collapse in reasoning is a different phenomenon from recursive generation depth, but shares the theme of iterative degradation.
90	
91	### [CONTEXT] Self-Consuming Generative Models Go MAD — Alemohammad et al. (ICLR 2024, updated 2025)
92	- **URL**: https://arxiv.org/abs/2307.01850
93	- **Core contribution**: Formalized autophagous loops and MAD (Model Autophagy Disorder). Without fresh real data, quality or diversity inevitably decreases.
94	- **Relation to us**: Already in scope. Foundation paper for our iterative generation setup.
95	
96	---
97	
98	## Thread 3: Verification-Based Data Curation / Collapse Mitigation
99	
100	### [NEW] Machine-Generated Text Detection Prevents Language Model Collapse — Drayson, Yilmaz, Lampos
101	- **Venue**: EMNLP 2025
102	- **URL**: https://arxiv.org/abs/2502.15654
103	- **Core contribution**: Trains MGT detector and uses importance resampling to up-weight likely-human content in training data. Not only prevents collapse but **improves** performance beyond pure human data. Validated on GPT-2 and SmolLM2 (124M–1.7B).
104	- **Relation to us**: **Strongly complementary**. Directly connects MGT detection to collapse prevention. Our depth estimator could serve as a more granular version of their binary detector — instead of binary filtering, weight by estimated generation depth. **Must cite.**
105	- **Code**: https://github.com/GeorgeDrayson/model_collapse
106	- **NOTE**: Dream审稿 previously flagged "Drayson et al. (2025)" as a hallucinated citation. **It is real.** George Drayson, UCL, EMNLP 2025.
107	
108	### [NEW] Escaping Model Collapse via Synthetic Data Verification — (2025)
109	- **Venue**: arXiv preprint (under review)
110	- **URL**: https://arxiv.org/abs/2510.16657
111	- **Core contribution**: Theoretical analysis showing verifier-guided retraining avoids collapse in the short term but converges to verifier's "knowledge center" long-term. Unless verifier is perfect, gains plateau. Validated on linear regression, VAEs (MNIST), SmolLM2-135M (XSUM).
112	- **Relation to us**: **Complementary**. Extends the Feng ICLR 2025 verification framework. Their "verifier imperfection → plateau" result connects to our K* concept — there's a depth beyond which even verification-based curation can't help.
113	
114	### [NEW] Escaping Collapse: The Strength of Weak Data for Large Language Model Training — Amin et al.
115	- **Venue**: NeurIPS 2025
116	- **URL**: https://arxiv.org/abs/2502.08924
117	- **Core contribution**: Boosting-inspired framework showing that if ≥β>0 fraction of external responses are correct, iterative training converges. Dynamically focusing labeling on hardest examples improves performance.
118	- **Relation to us**: **Complementary**. Their "weak signal suffices" result suggests our depth estimator, even if imperfect, could serve as the weak signal for data curation in iterative training pipelines.
119	
120	### [ALREADY CITED] Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification — Feng et al.
121	- **Venue**: ICLR 2025
122	- **URL**: https://arxiv.org/abs/2406.07515
123	- **Note**: Already in our related work (Thread 3).
124	
125	### [NEW] Learning by Surprise: Surplexity for Mitigating Model Collapse — (2025)
126	- **Venue**: arXiv preprint (revised Sep 2025)
127	- **URL**: https://arxiv.org/abs/2410.12341
128	- **Core contribution**: Proposes "surplexity" — measures collapse via next-token probability distributions rather than text properties. Filters training items by surprise level, effective without knowing human/synthetic origin.
129	- **Relation to us**: **Complementary**. Surplexity could be an additional feature in our depth estimation pipeline. The key insight — collapse manifests as decreasing surprise — aligns with our observation that deeper generations have lower token-level entropy.
130	
131	---
132	
133	## Thread 4: Data Contamination Estimation
134	
135	### [NEW] CoDeC: Detecting Data Contamination in LLMs via In-Context Learning — Zawalski et al.
136	- **Venue**: ICLR 2026
137	- **URL**: https://arxiv.org/abs/2510.27055
138	- **Core contribution**: Detects contamination by measuring how in-context examples affect model confidence. If ICL examples reduce confidence (disrupting memorization), the data was likely in training. Simple, model/dataset-agnostic, runs in minutes.
139	- **Relation to us**: **Complementary**. CoDeC detects binary contamination; our depth estimation is a finer-grained version of contamination measurement. Could use CoDeC as a sanity check in our pipeline.
140	
141	### [NEW] Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data — (2025)
142	- **Venue**: arXiv preprint (Nov 2025)
143	- **URL**: https://arxiv.org/abs/2511.17602
144	- **Core contribution**: Four-level contamination detection: token, semantic, reasoning pattern, performance cliff. Existing methods fail at semantic-level contamination (F1=0.17-0.49); hierarchical approach achieves F1=0.76.
145	- **Relation to us**: **Complementary**. Their multi-level framework is conceptually aligned with our multi-feature approach. The "reasoning pattern" contamination level is analogous to our "generation depth" concept — patterns that propagate through iterations.
146	
147	### [SURVEY] A Survey on Data Contamination for Large Language Models — (2025)
148	- **URL**: https://arxiv.org/html/2502.14425v2
149	- **Core contribution**: Reviews 50+ detection techniques and 100+ papers. Notes that detection during SFT (vs pretraining) remains unsolved.
150	- **Relation to us**: **Context**. Confirms contamination detection is active area; our depth estimation adds a new dimension.
151	
152	---
153	
154	## Papers NOT Found / Verified as Non-existent
155	
156	No additional hallucinated citations were detected in this scan. All papers listed above have verified URLs on arxiv.org, OpenReview, ACL Anthology, or conference proceedings.
157	
158	---
159	
160	## Actionable Recommendations for the Paper
161	
162	### Must Cite (high relevance, strengthens positioning)
163	1. **Drayson et al. (EMNLP 2025)** — directly connects MGT detection to collapse prevention; our depth estimator is a natural generalization
164	2. **Schaeffer et al. (ICML 2025)** — "Model Collapse Does Not Mean What You Think" — forces us to be precise about definitions; we should clarify K* is about discriminability saturation, not test-loss collapse
165	3. **Kazdan & Schaeffer (ICML 2025)** — "Collapse or Thrive" — accumulate vs replace regimes affect K*
166	4. **He et al. (NeurIPS 2025)** — generalization→memorization transition parallels our feature convergence
167	
168	### Should Cite (good context)
169	5. **DivEye (TMLR 2026)** — new zero-shot detection baseline; surprisal features may work for depth estimation
170	6. **Amin et al. (NeurIPS 2025)** — weak-signal curation; motivates practical utility of imperfect depth estimators
171	7. **CoDeC (ICLR 2026)** — state-of-art contamination detection; complementary to our approach
172	8. **Surplexity (2025)** — surprise-based collapse metric; potential feature for our pipeline
173	
174	### New Baselines to Test in Full Study
175	- **DivEye features** (surprisal diversity statistics) as depth-discriminative features
176	- **Surplexity scores** as an alternative collapse indicator per generation depth
177	
178	### Framing Adjustments
179	- Add a paragraph distinguishing our "discriminability saturation" (K*) from model collapse definitions per Schaeffer 2025
180	- Position Drayson 2025 as the closest work (binary filtering for collapse prevention) and explain how ordinal depth estimation generalizes it
181	- Discuss accumulate vs replace regimes (Kazdan 2025) as factors that may shift K*
182	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a31272a8-a0f5-4446-97fc-2807e6e0f5f6",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "e85e41e3-07c5-4f77-b72f-42f713c2ac35",
  "sourceToolAssistantUUID": "a31272a8-a0f5-4446-97fc-2807e6e0f5f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-13T08:55:22.218Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CRi6BTrHjQa4NSJwjSowD2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/_project/report/literature_positioning_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e85e41e3-07c5-4f77-b72f-42f713c2ac35",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHeUb4f1KHwccc6b8cw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bbb8134-632b-4d30-896f-5992ab2a8a5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013no4UaSWkcNoU4Fse9WSzw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13728,
      "cache_read_input_tokens": 42945,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13728
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 42945,
          "cache_creation_input_tokens": 13728,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13728,
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

_source line 37 · 2026-05-13T08:55:22.223Z_

<details><summary>↩ Tool result · `toolu_01CRi6BTrHjQa4NSJwjSowD2`</summary>

```text
1	# Literature Positioning Notes — gen-depth-contamination
2	
3	> 4 篇 must-cite / framing-critical 论文的深度分析与 positioning。
4	> 可直接用于 Introduction 和 Related Work 撰写。
5	
6	---
7	
8	## 1. Drayson et al. (EMNLP 2025) — "Machine-generated text detection prevents language model collapse"
9	
10	**Role: direct-competitor**
11	
12	### Method & Core Findings
13	
14	Drayson et al. train a binary MGT detector (encoder-only transformer with classification head; best model: ModernBERT-150M, AUC .986 in-distribution) to distinguish human vs. machine-generated text, then apply Sampling Importance Resampling (SIR) to upweight human-attributed samples during training. The resampling weight is:
15	
16	$$w_j = \frac{(1 - q(x_j))^b}{\sum_l (1 - q(x_l))^b}$$
17	
18	where $q(x)$ is the detector's estimated probability of being machine-generated, and $b \geq 1$ is a bias term correcting for the detector's skew. They resample at rate $k=1.5$ (50% upsampling). Evaluated on GPT-2 and SmolLM2 families (124M–1.7B), the method not only prevents model collapse but improves over training on purely human data (perplexity −0.85% to −25.65%, diversity +3.44% to +14.62%, MAUVE +8.46% to +20.92%).
19	
20	### Limitations
21	
22	- Only evaluates fine-tuning, not pretraining from scratch.
23	- Models ≤2B parameters; unclear if results transfer to larger scales.
24	- Exclusively binary classification; no discussion of ordinal depth or multi-class generational estimation.
25	- Open-ended generation only; may not generalize to structured tasks.
26	
27	### Relationship to Our Work
28	
29	**Overlaps:** Both use MGT detection for data curation in iterative training loops. Both frame the problem as "detection enables quality-aware data selection."
30	
31	**Key difference:** Drayson et al. treat synthetic text as a monolithic category (binary: human vs. synthetic). We argue that recursive generation creates a *depth spectrum*—gen-1 text is qualitatively different from gen-4 text—and estimate ordinal depth rather than binary label. Our K* operationalizes *when* this ordinal signal matters: below K*, depth-graduated filtering adds value over binary; above K*, generations are indistinguishable and binary suffices.
32	
33	**How we cite them:** As the closest prior work and the starting point we generalize. Their SIR framework is a special case of our graduated filtering when K*=1 (i.e., only distinguishing human from all synthetic). We frame our contribution as the binary→ordinal extension: "Drayson et al. (2025) demonstrate that binary MGT detection combined with importance resampling prevents model collapse. We extend this to ordinal depth estimation and show that even a coarse 3-class signal (human/gen-1/gen-2+) yields improved calibration over binary filtering at decision boundaries."
34	
35	### Related Work Draft
36	
37	> Drayson et al. (2025) pioneer the use of binary MGT detection for collapse prevention, training an encoder-only classifier to separate human from machine-generated text and applying importance resampling to upweight human-attributed samples during training. Their method demonstrably prevents collapse and even improves over human-only baselines on models up to 1.7B parameters. However, their binary framing treats all synthetic text uniformly, discarding the information encoded in generational depth. We generalize their approach from binary detection to ordinal depth estimation: where they assign weight $w \propto (1-q)^b$ based on a binary human probability, we estimate generational depth $d \in \{0, 1, \ldots, K^*\}$ and apply depth-graduated filtering that exploits the quality gradient across recursive generations.
38	
39	---
40	
41	## 2. Schaeffer et al. (ICML 2025) — "Position: Model Collapse Does Not Mean What You Think"
42	
43	**Role: framing-critical**
44	
45	### Core Argument & Taxonomy
46	
47	Schaeffer et al. identify that "model collapse" is used inconsistently across the literature, encompassing eight distinct and sometimes conflicting definitions. They organize these into three families:
48	
49	**Family A — Population Risk Degrading:**
50	- **D1: Catastrophic increase of population risk** — rapid, severe performance degradation from synthetic data.
51	- **D2: Any increase of population risk** — strict: any performance decrease vs. training on real data alone.
52	- **D3: Asymptotically diverging population risk** — unbounded risk growth across iterations (fundamentally unstable dynamics).
53	
54	**Family B — Distributions Deforming:**
55	- **D4: Collapsing variance** — diversity → 0, distributions → delta functions over successive iterations.
56	- **D5: Change in scaling law** — synthetic data alters the performance–data-size relationship.
57	- **D6: Disappearance of or entanglement of modes** — synthetic data prevents learning specific distribution modes or causes mode blurring.
58	- **D7: Disappearance of real tail data** — underrepresentation of rare/minority data ("coverage collapse").
59	
60	**Family C — Spurious Generation:**
61	- **D8: Appearance of hallucinated data** — model produces sequences unsupported by the original distribution.
62	
63	Their main argument: prominent collapse scenarios are "readily avoidable" under realistic conditions (data accumulation, increasing compute). The real harms—tail data loss (D7) and mode entanglement (D6)—have received disproportionately less attention.
64	
65	### Relationship to Our Work
66	
67	**Our K* in their taxonomy:** K* (discriminability saturation) belongs squarely to Family B (distributions deforming). Specifically, K* measures when recursive generation causes sufficient distribution deformation (D4: variance collapse + D6: mode entanglement) that successive generations become statistically indistinguishable in feature space. K* is *not* about population risk increase (Family A)—a model trained on gen-2 text might perform fine on downstream tasks, yet gen-2 and gen-3 text are already indistinguishable.
68	
69	**How we cite them:** To precisely position K* within the collapse discourse. We adopt their taxonomy to clarify that our contribution addresses distribution deformation (Family B), not population risk degradation (Family A): "Following the taxonomy of Schaeffer et al. (2025), our K* measures the discriminability saturation boundary—the generational depth beyond which distribution deformation (Definitions 4, 6) renders successive generations indistinguishable in feature space. This is orthogonal to population risk collapse (Definitions 1–3), which may or may not accompany loss of discriminability."
70	
71	### Related Work Draft
72	
73	> The model collapse literature suffers from terminological inconsistency. Schaeffer et al. (2025) identify eight distinct definitions spanning three families: population risk degradation, distribution deformation, and spurious generation. They argue that under realistic conditions—where data accumulates and compute grows—catastrophic risk divergence (Definitions 1–3) is avoidable, but distribution-level harms such as tail data loss and mode entanglement (Definitions 6–7) remain concerning. Our work operationalizes the distribution deformation family: K* measures the generational depth at which feature-space divergence saturates, providing a concrete, measurable boundary for when successive generations become indistinguishable. This positions depth estimation as a diagnostic tool for exactly the harms Schaeffer et al. identify as underexplored.
74	
75	---
76	
77	## 3. Kazdan et al. (ICML 2025) — "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World"
78	
79	**Role: background**
80	
81	### Method & Core Findings
82	
83	Kazdan et al. formally compare three data regimes for iterative training:
84	
85	1. **Replace:** Each generation trains exclusively on synthetic data from the previous model. All prior data discarded. Formally, $\hat{\mu}^{(t+1)} = \frac{1}{n}\sum X_j^{(t)}$. Result: covariance collapses to zero ($\hat{\Sigma} \to 0$ a.s.), Wasserstein-2 diverges. Collapse is inevitable.
86	
87	2. **Accumulate:** Each generation trains on *all* historical data (real + all previous synthetic). Dataset grows linearly; real data fraction → 0. Result: covariance stabilizes at $\sigma_0^2 \cdot \sin(\pi/\sqrt{n}) / (\pi/\sqrt{n})$. No collapse.
88	
89	3. **Accumulate-subsample:** Data accumulates but each iteration uses a fixed-size subsample. Result: degradation plateaus rather than diverges—intermediate between replace and accumulate.
90	
91	Validated on multivariate Gaussians, kernel density estimation, and LLM fine-tuning (Gemma2-2B on HelpSteer2/TinyStories). Key finding: in the accumulate regime, the *cardinality* of real data matters more than its *proportion* ($R^2=0.59$ vs $0.34$).
92	
93	### Limitations
94	
95	- Replace regime collapses within 5–10 iterations in all settings, but precise timescales depend on model/data specifics.
96	- LLM experiments limited to SFT on 2B models.
97	- No detection or mitigation method proposed—purely diagnostic.
98	
99	### Relationship to Our Work
100	
101	**Our experimental design = replace regime.** Our prompt-chain pipeline generates each subsequent generation from the previous model's output exclusively, without mixing real data. This is the harshest setting per Kazdan et al.'s analysis—covariance collapse is guaranteed, and K* is measured under this maximally adversarial condition.
102	
103	**Implication for K*:** Our measured K*=2 is a *lower bound* on what would be observed under the more realistic accumulate regime, where distributional stability persists longer. This strengthens our result: if depth estimation already provides value at K*=2 in the replace regime, it can only provide more value when K* shifts upward in accumulate settings.
104	
105	**How we cite them:** To justify our experimental design and contextualize our K* measurement.
106	
107	### Related Work Draft
108	
109	> Kazdan et al. (2025) formalize three data regimes for iterative retraining: replace (complete substitution each generation), accumulate (growing corpus including all historical data), and accumulate-subsample (fixed training budget from accumulated pool). They prove that replace inevitably collapses (covariance → 0), while accumulate maintains stability even as real data fraction vanishes. Our prompt-chain experiments operate in the replace regime—the harshest setting—establishing K*=2 as a conservative lower bound; under the accumulate regime that better models real-world data aggregation, K* would likely shift upward, amplifying the value of depth-graduated curation.
110	
111	---
112	
113	## 4. He et al. (NeurIPS 2025 Spotlight) — "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"
114	
115	**Role: background**
116	
117	### Method & Core Findings
118	
119	He et al. characterize model collapse as a generalization→memorization transition in iterative training on synthetic data (DDPM on CIFAR-10 subsets). They introduce:
120	
121	- **Generalization Score (GS):** Average distance between each generated image and its nearest training image. GS drops approximately exponentially across iterations.
122	- **Entropy measurement:** Kozachenko-Leonenko estimator for differential entropy of training data. Strong linear correlation between training set entropy and log(GS) (Pearson $r=0.91$), establishing entropy as a direct predictor of generalization capability.
123	
124	They propose entropy-based data selection: greedy selection maximizing nearest-neighbor distances, and threshold-decay filtering. Both preserve entropy and mitigate collapse.
125	
126	Collapse timescales depend on dataset size: 1,024 images → memorization from iteration 1; 32,768 images → memorization after several iterations (5–10).
127	
128	### Limitations
129	
130	- **Diffusion models only.** No LLM experiments; they note "extension to the language modality" as future work.
131	- **No theoretical analysis** of why entropy collapses—they identify the correlation but not the causal mechanism ("finite dataset size, training and sampling errors, and the model bias could all contribute").
132	- FID as distributional metric; no JSD analysis.
133	
134	### Relationship to Our Work
135	
136	**Parallel phenomena, different modalities.** Their entropy decline across iterations directly parallels our observed JSD monotonic decrease (0.27→0.004) across 5 text generations. Their "generalization score drops exponentially" mirrors our finding that feature-space divergence between consecutive generations vanishes rapidly, leading to K*=2.
137	
138	**Key distinction:** They measure collapse at the *output distribution* level (pixel-space entropy); we measure *discriminability* in feature space (can a classifier distinguish gen-$k$ from gen-$k+1$?). Our K* complements their entropy metric by providing an operational answer: "at what depth does the entropy decline make generations functionally indistinguishable?"
139	
140	**Connection to feature convergence:** Their observation that generated images form "tight local clusters" while overall variance remains stable resonates with our finding that depth-discriminative features (vocabulary diversity, surprisal dynamics) converge before global distributional statistics do.
141	
142	**How we cite them:** To ground our feature-space convergence observations in a broader phenomenon observed across modalities.
143	
144	### Related Work Draft
145	
146	> He et al. (2025) characterize model collapse as a generalization-to-memorization transition driven by entropy decline in iteratively retrained diffusion models, establishing a strong correlation ($r=0.91$) between training data entropy and generalization capability. While their work focuses on image generation, the phenomenon parallels our observations in the text domain: their exponentially declining generalization scores mirror our monotonically decreasing JSD across recursive text generations, and their observed clustering in feature space corresponds to the convergence of depth-discriminative linguistic features we measure. Our K* provides an operational complement to their entropy metric—quantifying the generational depth at which this convergence renders successive text generations indistinguishable to classifiers.
147	
148	---
149	
150	## Cross-Paper Synthesis: Positioning Summary
151	
152	| Paper | Their Frame | Our Positioning | Citation Function |
153	|-------|------------|-----------------|-------------------|
154	| Drayson et al. | Binary MGT detection + SIR for collapse prevention | We generalize binary→ordinal; K* tells when ordinal adds value | Direct predecessor we extend |
155	| Schaeffer et al. | 8 definitions, 3 families; realistic conditions matter | K* = distribution deformation (Family B, D4+D6) discriminability measure | Taxonomic anchor for K* |
156	| Kazdan et al. | Replace collapses, accumulate stabilizes | Our replace-regime K*=2 is a conservative lower bound | Justifies experimental design |
157	| He et al. | Entropy decline → memorization (diffusion models) | Parallel phenomenon; K* operationalizes "when does entropy decline = indistinguishability?" | Cross-modal validation of convergence |
158	
159	### Narrative Arc for Introduction
160	
161	1. **Open** with the model collapse concern (cite Shumailov et al., Alemohammad et al. as foundational).
162	2. **Complicate** with Schaeffer et al.: "collapse" means many things; the real harm is distribution deformation, not necessarily risk divergence.
163	3. **Situate** with Kazdan et al.: under replace regime, collapse is inevitable; the question is *how fast* and *can we detect it?*
164	4. **Motivate depth estimation** via He et al.: entropy/distributional convergence happens over identifiable timescales.
165	5. **Present our gap** relative to Drayson et al.: binary detection helps, but ignores the depth gradient that carries actionable information.
166	6. **State contribution:** We formalize depth estimation, measure K*, and show graduated filtering improves on binary.
167	
168	### Narrative Arc for Related Work
169	
170	Structure into 3 subsections:
171	1. **Model Collapse: Definitions and Dynamics** — Schaeffer et al. (taxonomy) + Kazdan et al. (regimes) + Shumailov/Alemohammad/Dohmatob (foundational)
172	2. **Detecting and Mitigating Synthetic Data** — Drayson et al. (binary detection + SIR) + DivEye + Min-K%++ + watermarking
173	3. **Feature-Space Characterization of Iterative Degradation** — He et al. (entropy/memorization) + our JSD analysis
174	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bbb8134-632b-4d30-896f-5992ab2a8a5b",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "48ca346c-ca65-4375-ba07-6af2f98ee7c6",
  "sourceToolAssistantUUID": "3bbb8134-632b-4d30-896f-5992ab2a8a5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-13T08:55:25.664Z_

Now let me check the experimental data artifacts for grounding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48ca346c-ca65-4375-ba07-6af2f98ee7c6",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHets4mBdy3TFjWjsm7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb806489-fc46-41b0-8fd1-f57e44664900",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKppzExbfoeCT1ko4UmHAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8930,
      "cache_read_input_tokens": 56673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8930,
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

_source line 39 · 2026-05-13T08:55:27.622Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JgrLqHQuY2VEngUCkeFASF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/bootstrap_ci_4model.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb806489-fc46-41b0-8fd1-f57e44664900",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHets4mBdy3TFjWjsm7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0556361-edad-4c1e-94be-bf7d839d0893",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKppzExbfoeCT1ko4UmHAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8930,
      "cache_read_input_tokens": 56673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8930,
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

_source line 40 · 2026-05-13T08:55:27.635Z_

<details><summary>↩ Tool result · `toolu_01JgrLqHQuY2VEngUCkeFASF`</summary>

```text
1	{
2	  "mvp_001_qwen_rewrite": {
3	    "0v1": {
4	      "mean_auc": 0.9956,
5	      "boot_mean": 0.9956,
6	      "boot_std": 0.0005,
7	      "ci_lower": 0.9946,
8	      "ci_upper": 0.9965,
9	      "ci_width": 0.0019,
10	      "perm_pvalue": 0.0,
11	      "n_bootstrap": 1000,
12	      "n_permutation": 500
13	    },
14	    "1v2": {
15	      "mean_auc": 0.6955,
16	      "boot_mean": 0.6953,
17	      "boot_std": 0.0045,
18	      "ci_lower": 0.6859,
19	      "ci_upper": 0.7041,
20	      "ci_width": 0.0182,
21	      "perm_pvalue": 0.0,
22	      "n_bootstrap": 1000,
23	      "n_permutation": 500
24	    },
25	    "2v3": {
26	      "mean_auc": 0.5893,
27	      "boot_mean": 0.5893,
28	      "boot_std": 0.0049,
29	      "ci_lower": 0.5795,
30	      "ci_upper": 0.5991,
31	      "ci_width": 0.0195,
32	      "perm_pvalue": 0.0,
33	      "n_bootstrap": 1000,
34	      "n_permutation": 500
35	    },
36	    "3v4": {
37	      "mean_auc": 0.5435,
38	      "boot_mean": 0.5437,
39	      "boot_std": 0.0054,
40	      "ci_lower": 0.5333,
41	      "ci_upper": 0.5551,
42	      "ci_width": 0.0218,
43	      "perm_pvalue": 0.0,
44	      "n_bootstrap": 1000,
45	      "n_permutation": 500
46	    },
47	    "4v5": {
48	      "mean_auc": 0.534,
49	      "boot_mean": 0.5339,
50	      "boot_std": 0.0053,
51	      "ci_lower": 0.5238,
52	      "ci_upper": 0.5448,
53	      "ci_width": 0.021,
54	      "perm_pvalue": 0.0,
55	      "n_bootstrap": 1000,
56	      "n_permutation": 500
57	    }
58	  },
59	  "exp_001_pythia": {
60	    "0v1": {
61	      "mean_auc": 0.9932,
62	      "boot_mean": 0.9932,
63	      "boot_std": 0.0006,
64	      "ci_lower": 0.9921,
65	      "ci_upper": 0.9943,
66	      "ci_width": 0.0023,
67	      "perm_pvalue": 0.0,
68	      "n_bootstrap": 1000,
69	      "n_permutation": 500
70	    },
71	    "1v2": {
72	      "mean_auc": 0.6539,
73	      "boot_mean": 0.654,
74	      "boot_std": 0.0045,
75	      "ci_lower": 0.6454,
76	      "ci_upper": 0.663,
77	      "ci_width": 0.0176,
78	      "perm_pvalue": 0.0,
79	      "n_bootstrap": 1000,
80	      "n_permutation": 500
81	    },
82	    "2v3": {
83	      "mean_auc": 0.5514,
84	      "boot_mean": 0.5514,
85	      "boot_std": 0.0053,
86	      "ci_lower": 0.5417,
87	      "ci_upper": 0.5628,
88	      "ci_width": 0.0211,
89	      "perm_pvalue": 0.0,
90	      "n_bootstrap": 1000,
91	      "n_permutation": 500
92	    },
93	    "3v4": {
94	      "mean_auc": 0.5152,
95	      "boot_mean": 0.515,
96	      "boot_std": 0.0056,
97	      "ci_lower": 0.5041,
98	      "ci_upper": 0.526,
99	      "ci_width": 0.022,
100	      "perm_pvalue": 0.006,
101	      "n_bootstrap": 1000,
102	      "n_permutation": 500
103	    },
104	    "4v5": {
105	      "mean_auc": 0.5136,
106	      "boot_mean": 0.5134,
107	      "boot_std": 0.0056,
108	      "ci_lower": 0.5021,
109	      "ci_upper": 0.5249,
110	      "ci_width": 0.0227,
111	      "perm_pvalue": 0.008,
112	      "n_bootstrap": 1000,
113	      "n_permutation": 500
114	    }
115	  },
116	  "exp_002_olmo": {
117	    "0v1": {
118	      "mean_auc": 0.997,
119	      "boot_mean": 0.997,
120	      "boot_std": 0.0003,
121	      "ci_lower": 0.9964,
122	      "ci_upper": 0.9975,
123	      "ci_width": 0.0011,
124	      "perm_pvalue": 0.0,
125	      "n_bootstrap": 1000,
126	      "n_permutation": 500
127	    },
128	    "1v2": {
129	      "mean_auc": 0.6145,
130	      "boot_mean": 0.6146,
131	      "boot_std": 0.0051,
132	      "ci_lower": 0.6045,
133	      "ci_upper": 0.6247,
134	      "ci_width": 0.0203,
135	      "perm_pvalue": 0.0,
136	      "n_bootstrap": 1000,
137	      "n_permutation": 500
138	    },
139	    "2v3": {
140	      "mean_auc": 0.5496,
141	      "boot_mean": 0.5501,
142	      "boot_std": 0.0052,
143	      "ci_lower": 0.5399,
144	      "ci_upper": 0.5596,
145	      "ci_width": 0.0197,
146	      "perm_pvalue": 0.0,
147	      "n_bootstrap": 1000,
148	      "n_permutation": 500
149	    },
150	    "3v4": {
151	      "mean_auc": 0.5091,
152	      "boot_mean": 0.5088,
153	      "boot_std": 0.0058,
154	      "ci_lower": 0.4973,
155	      "ci_upper": 0.52,
156	      "ci_width": 0.0226,
157	      "perm_pvalue": 0.064,
158	      "n_bootstrap": 1000,
159	      "n_permutation": 500
160	    },
161	    "4v5": {
162	      "mean_auc": 0.5045,
163	      "boot_mean": 0.5044,
164	      "boot_std": 0.0056,
165	      "ci_lower": 0.4932,
166	      "ci_upper": 0.515,
167	      "ci_width": 0.0218,
168	      "perm_pvalue": 0.232,
169	      "n_bootstrap": 1000,
170	      "n_permutation": 500
171	    }
172	  },
173	  "exp_017_qwen_cont": {
174	    "0v1": {
175	      "mean_auc": 0.9971,
176	      "boot_mean": 0.9971,
177	      "boot_std": 0.0004,
178	      "ci_lower": 0.9963,
179	      "ci_upper": 0.9978,
180	      "ci_width": 0.0015,
181	      "perm_pvalue": 0.0,
182	      "n_bootstrap": 1000,
183	      "n_permutation": 500
184	    },
185	    "1v2": {
186	      "mean_auc": 0.6112,
187	      "boot_mean": 0.6113,
188	      "boot_std": 0.0051,
189	      "ci_lower": 0.6015,
190	      "ci_upper": 0.6213,
191	      "ci_width": 0.0198,
192	      "perm_pvalue": 0.0,
193	      "n_bootstrap": 1000,
194	      "n_permutation": 500
195	    },
196	    "2v3": {
197	      "mean_auc": 0.5609,
198	      "boot_mean": 0.561,
199	      "boot_std": 0.0053,
200	      "ci_lower": 0.5511,
201	      "ci_upper": 0.5712,
202	      "ci_width": 0.0201,
203	      "perm_pvalue": 0.0,
204	      "n_bootstrap": 1000,
205	      "n_permutation": 500
206	    },
207	    "3v4": {
208	      "mean_auc": 0.5409,
209	      "boot_mean": 0.541,
210	      "boot_std": 0.0052,
211	      "ci_lower": 0.5308,
212	      "ci_upper": 0.5508,
213	      "ci_width": 0.02,
214	      "perm_pvalue": 0.0,
215	      "n_bootstrap": 1000,
216	      "n_permutation": 500
217	    },
218	    "4v5": {
219	      "mean_auc": 0.5141,
220	      "boot_mean": 0.5141,
221	      "boot_std": 0.0056,
222	      "ci_lower": 0.5035,
223	      "ci_upper": 0.5255,
224	      "ci_width": 0.022,
225	      "perm_pvalue": 0.006,
226	      "n_bootstrap": 1000,
227	      "n_permutation": 500
228	    }
229	  }
230	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0556361-edad-4c1e-94be-bf7d839d0893",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "364f6977-5c9f-427f-b6e6-cdd34bf1a785",
  "sourceToolAssistantUUID": "f0556361-edad-4c1e-94be-bf7d839d0893",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-13T08:55:28.374Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CFX1eS5LUFXNpJZ4e7bH4S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp-013/data/cross_transfer_matrix.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "364f6977-5c9f-427f-b6e6-cdd34bf1a785",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHets4mBdy3TFjWjsm7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37e7ce75-106b-4ff6-b526-ba78e35b7b56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKppzExbfoeCT1ko4UmHAd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8930,
      "cache_read_input_tokens": 56673,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8930
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 56673,
          "cache_creation_input_tokens": 8930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8930,
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

_source line 42 · 2026-05-13T08:55:28.385Z_

<details><summary>↩ Tool result · `toolu_01CFX1eS5LUFXNpJZ4e7bH4S`</summary>

```text
1	See cross_transfer_matrix.csv for the same data in tabular format. JSON version stored on server at /root/autodl-tmp/gen-depth-contamination/artifacts/cross_transfer_matrix.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37e7ce75-106b-4ff6-b526-ba78e35b7b56",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "86c86aae-c091-44af-8710-62de5b3e8aad",
  "sourceToolAssistantUUID": "37e7ce75-106b-4ff6-b526-ba78e35b7b56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-13T08:55:31.350Z_

<details open><summary>🔧 Tool call — Read · `toolu_012VQzCdSTog8Xd4Lm1VUnT9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp-013/data/cross_transfer_matrix.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86c86aae-c091-44af-8710-62de5b3e8aad",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHfM1BkCPDK9DePdSPY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "780b38dc-492e-4d25-a670-5ea2bf0bc3b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PyVsDPfU4saJ45wdPSeBae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3300,
      "cache_read_input_tokens": 65603,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3300,
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

_source line 44 · 2026-05-13T08:55:31.355Z_

<details><summary>↩ Tool result · `toolu_012VQzCdSTog8Xd4Lm1VUnT9`</summary>

```text
1	train_model,test_model,accuracy,mae,kendall_tau_b,mean_pairwise_auc
2	Qwen-rewrite,Qwen-rewrite,0.4229,0.9836,0.5518,0.6214
3	Qwen-rewrite,Pythia,0.259,1.9823,0.2768,0.5787
4	Qwen-rewrite,OLMo,0.2653,1.976,0.2492,0.5791
5	Qwen-rewrite,Qwen-cont,0.3466,1.5157,0.4595,0.6247
6	Pythia,Qwen-rewrite,0.2718,1.9026,0.1695,0.5603
7	Pythia,Pythia,0.3856,1.1072,0.4745,0.6055
8	Pythia,OLMo,0.3531,1.2809,0.41,0.5937
9	Pythia,Qwen-cont,0.3287,1.5016,0.3801,0.6082
10	OLMo,Qwen-rewrite,0.2768,1.8935,0.1708,0.5607
11	OLMo,Pythia,0.345,1.3494,0.3979,0.5999
12	OLMo,OLMo,0.3822,1.1469,0.4683,0.6015
13	OLMo,Qwen-cont,0.3244,1.5574,0.3542,0.5926
14	Qwen-cont,Qwen-rewrite,0.344,1.3404,0.4126,0.5767
15	Qwen-cont,Pythia,0.3284,1.3363,0.3912,0.6025
16	Qwen-cont,OLMo,0.3112,1.475,0.3241,0.5988
17	Qwen-cont,Qwen-cont,0.3875,1.1209,0.4769,0.6111
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "780b38dc-492e-4d25-a670-5ea2bf0bc3b3",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "4a9cfd39-1d82-4a2f-9656-085671360dcd",
  "sourceToolAssistantUUID": "780b38dc-492e-4d25-a670-5ea2bf0bc3b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-13T08:55:31.881Z_

<details open><summary>🔧 Tool call — Read · `toolu_0161wLZPMEHjdy7322pF59eB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp005_4model_tau_matrix.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a9cfd39-1d82-4a2f-9656-085671360dcd",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHfM1BkCPDK9DePdSPY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "103b900f-0e37-46a6-af7d-39a5eb839ef5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PyVsDPfU4saJ45wdPSeBae",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3300,
      "cache_read_input_tokens": 65603,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3300
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 65603,
          "cache_creation_input_tokens": 3300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3300,
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

_source line 46 · 2026-05-13T08:55:31.885Z_

<details><summary>↩ Tool result · `toolu_0161wLZPMEHjdy7322pF59eB`</summary>

```text
1	{
2	  "experiment": "exp-005 4-model degradation ordering",
3	  "date": "2026-05-13",
4	  "models": ["Pythia-1.4B", "OLMo-1B", "Qwen-1.5B-rewrite", "Qwen-1.5B-cont"],
5	  "tau_matrix_first_auc": {
6	    "Pythia_vs_OLMo":          {"tau": 0.7333, "p": 0.0000},
7	    "Pythia_vs_Qwen_rewrite":  {"tau": 0.4667, "p": 0.0155},
8	    "Pythia_vs_Qwen_cont":     {"tau": 0.6952, "p": 0.0001},
9	    "OLMo_vs_Qwen_rewrite":    {"tau": 0.4286, "p": 0.0275},
10	    "OLMo_vs_Qwen_cont":       {"tau": 0.5429, "p": 0.0041},
11	    "Qwen_rewrite_vs_Qwen_cont": {"tau": 0.7333, "p": 0.0000}
12	  },
13	  "tau_matrix_avg_auc": {
14	    "Pythia_vs_OLMo":          {"tau": 0.8476, "p": 0.0000},
15	    "Pythia_vs_Qwen_rewrite":  {"tau": 0.5238, "p": 0.0059},
16	    "Pythia_vs_Qwen_cont":     {"tau": 0.7524, "p": 0.0000},
17	    "OLMo_vs_Qwen_rewrite":    {"tau": 0.4857, "p": 0.0114},
18	    "OLMo_vs_Qwen_cont":       {"tau": 0.6762, "p": 0.0002},
19	    "Qwen_rewrite_vs_Qwen_cont": {"tau": 0.6952, "p": 0.0001}
20	  },
21	  "spearman_rho_first_auc": {
22	    "Pythia_vs_OLMo":          {"rho": 0.8750, "p": 0.0000},
23	    "Pythia_vs_Qwen_rewrite":  {"rho": 0.6607, "p": 0.0073},
24	    "Pythia_vs_Qwen_cont":     {"rho": 0.8714, "p": 0.0000},
25	    "OLMo_vs_Qwen_rewrite":    {"rho": 0.4893, "p": 0.0642},
26	    "OLMo_vs_Qwen_cont":       {"rho": 0.6893, "p": 0.0045},
27	    "Qwen_rewrite_vs_Qwen_cont": {"rho": 0.9107, "p": 0.0000}
28	  },
29	  "analysis": {
30	    "mode_effect": {
31	      "description": "Generation mode is the dominant driver of ordering divergence",
32	      "evidence": {
33	        "Pythia_tau_delta": "Qwen-cont (0.6952) vs Qwen-rewrite (0.4667) → Δ=+0.2285",
34	        "OLMo_tau_delta": "Qwen-cont (0.5429) vs Qwen-rewrite (0.4286) → Δ=+0.1143",
35	        "within_arch_tau": "Qwen-rewrite vs Qwen-cont τ=0.7333 (high but not 1.0 → mode does change ordering)"
36	      }
37	    },
38	    "residual_architecture_effect": {
39	      "description": "Architecture still contributes — Qwen-cont vs OLMo (0.54) remains below Pythia vs OLMo (0.73)",
40	      "gap": "Qwen-cont doesn't fully converge to Pythia-OLMo level, especially for OLMo pair"
41	    },
42	    "conclusion": "Generation mode is the primary driver (~60-70% of divergence), architecture is secondary (~30-40%). C2 claim can state ordering is largely universal with mode as the main confound, but needs caveat about residual architecture differences."
43	  }
44	}
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "103b900f-0e37-46a6-af7d-39a5eb839ef5",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "bcbd7c89-24d9-4e27-a150-c3f794a01d10",
  "sourceToolAssistantUUID": "103b900f-0e37-46a6-af7d-39a5eb839ef5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-13T08:55:35.490Z_

Now I have a thorough understanding of the paper, its experimental evidence, literature landscape, and internal project framing. Let me also check if there was a previous R1 review from the current dream cycle that I should avoid duplicating.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcbd7c89-24d9-4e27-a150-c3f794a01d10",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHfcCVFrwYUTzZTMvwW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92217f28-b733-4df4-b049-2d6e5e0c1aff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gWTv158x9nNv42t33mJMj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1973,
      "cache_read_input_tokens": 68903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1973,
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

_source line 48 · 2026-05-13T08:55:36.592Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01MtCQwiGJ7RBZ82KMVxW4D8`</summary>

```json
{
  "pattern": "artifacts/dream_reports/dream_20260513T080728/*/review_report.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92217f28-b733-4df4-b049-2d6e5e0c1aff",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHfcCVFrwYUTzZTMvwW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad4767f2-2085-43fc-85aa-1a8e4dc1476b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gWTv158x9nNv42t33mJMj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1973,
      "cache_read_input_tokens": 68903,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1973
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 68903,
          "cache_creation_input_tokens": 1973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1973,
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

_source line 49 · 2026-05-13T08:55:36.624Z_

<details><summary>↩ Tool result · `toolu_01MtCQwiGJ7RBZ82KMVxW4D8`</summary>

```text
artifacts/dream_reports/dream_20260513T080728/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad4767f2-2085-43fc-85aa-1a8e4dc1476b",
  "isSidechain": true,
  "promptId": "b850697e-e935-4c0b-a8da-10aaed9e56c8",
  "agentId": "a8d7b6cd5cd8fadb4",
  "type": "user",
  "uuid": "78816bf7-dae4-4b35-9b00-52f40170d1f6",
  "sourceToolAssistantUUID": "ad4767f2-2085-43fc-85aa-1a8e4dc1476b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-13T08:57:16.531Z_

Good -- the previous "best" tier already has a consolidated review. I'm now being asked to provide my own independent R2 review focused on Novelty and Related Work. I have all the context I need. Let me now compose the review.

---

## Reviewer R2: Novelty and Related Work

**Paper:** "Measuring the Generational Discrimination Boundary in Recursively Contaminated Text"

---

### 1. Summary

The paper formalizes recursive text generation as an iterated lossy channel, invokes the Data Processing Inequality to argue that a finite "generational discrimination boundary" K* must exist, and empirically measures K*=2 at the 1.5B scale under nucleus sampling using 15D hand-crafted features with a LightGBM classifier. The K* boundary is shown to be controllable via decoding strategy (greedy yields K*=1; T=1.2 yields K*=3) and model scale (7B yields K*>=3). A graduated filtering application using a 3-class ordinal signal (human/gen-1/gen-2+) is reported to outperform binary filtering by +2.48pp MMLU and +2.70pp HellaSwag.

---

### 2. Strengths

**S1. Genuine conceptual reframing.** The shift from binary (human vs. synthetic) to ordinal (depth estimation) is a real contribution that opens a new problem space. No prior work estimates how many rounds of recursive generation a text has undergone. The literature scan I conducted confirms this: ordinal depth estimation is absent from all published binary detection, model collapse, and data selection work through May 2026.

**S2. K* as a controllable quantity, not just a measured constant.** The most novel finding is the K* gradient across decoding strategies: greedy (K*=1) -> standard nucleus (K*=2) -> high-temperature (K*=3). Combined with the scale pathway (7B -> K*>=3), this demonstrates K* captures properties of the recursive channel rather than classifier artifacts. This is the paper's strongest novelty claim and goes beyond merely reporting a number.

**S3. Thorough positioning against Drayson et al. (2025).** The closest prior work is correctly identified and the differentiation is clear: Drayson's SIR uses binary detection confidence for importance resampling; this work generalizes to ordinal depth with graduated weights. The binary-ours baseline (same features, same classifier, binary vs. ordinal decision) provides clean causal isolation of the ordinal signal's contribution.

**S4. Breadth of supporting analyses.** The paper includes retrain-chain ecological validity, cross-model transfer (Pythia<->OLMo), LLM zero-shot baselines, binary detector comparison, learned vs. hand-crafted features, and Common Crawl validation. This is above-average experimental comprehensiveness for a characterization paper.

**S5. Honest about limitations.** The paper acknowledges the Common Crawl validation is correlational, the LoRA retrain-chain has limited ecological validity, and presents K* as an empirical lower bound on the theoretical quantity.

---

### 3. Weaknesses

**W1. The DPI theoretical contribution is standard, not novel.** The iterated lossy channel framing and DPI-based argument for K*'s finiteness is textbook information theory. The Markov chain X_0 -> X_1 -> ... -> X_k with monotonically non-increasing mutual information is a direct application of a well-known inequality. The paper oversells this as a "theoretical contribution" when the actual novelty lies entirely in the empirical measurement and exploitation of K*. The theory section should be reframed as "motivation" rather than "contribution."

**W2. K*=2 has narrow practical implications.** A 3-class ordinal signal (human/gen-1/gen-2+) is structurally close to "binary detection with a soft middle category." The graduated filtering reduces to: keep human text (weight=1), discount gen-1 (weight=alpha), discard gen-2+ (weight=0). This is one additional threshold over binary, and the practical distance from Drayson's continuous importance resampling weights (which already achieve soft weighting via binary confidence) is smaller than the paper implies. The conceptual advance is real, but the operational gap is narrow.

**W3. Significant related work gaps.**

- **Watermarking literature** (Kirchenbauer et al., 2023; Christ et al., 2024): Watermarking provides an alternative mechanism for tracking generational provenance. If text is watermarked at each generation stage, depth can in principle be tracked without statistical classifiers. The paper should discuss why passive (detection-based) depth estimation is needed alongside or instead of active (watermarking-based) provenance tracking.

- **Schaeffer et al. (ICML 2025), "Position: Model Collapse Does Not Mean What You Think":** This paper identifies 8 distinct definitions of model collapse across 3 families. K* clearly belongs to their Family B (distribution deformation), not Family A (population risk). Citing this would sharpen the paper's positioning and prevent readers from confusing K* saturation with test-loss collapse.

- **Kazdan et al. (ICML 2025), "Collapse or Thrive?":** Formalizes replace vs. accumulate vs. accumulate-subsample regimes. The paper's prompt-chain setup corresponds to the replace regime (harshest). Citing this would contextualize K*=2 as a conservative lower bound under the most adversarial conditions.

- **Self-refinement / iterative generation literature:** Texts may undergo multiple LLM passes (self-refinement, chain-of-thought elaboration) that are not "recursive contamination" but produce similar statistical signatures. The paper does not discuss how depth estimation would handle such cases as false positives.

- **Membership inference connections:** Depth estimation across training stages is related to membership inference (Carlini et al., 2022; Shi et al., 2024 Min-K%++). The connection deserves at least a paragraph.

**W4. Missing citation in the introduction.** The paper contains a visible "[?]" broken citation reference. This is a clear preparation issue that should not appear in a submission.

**W5. C1/C3 numbering gap.** The contributions are listed as C1 and C3, skipping C2. The review context reveals C2 (degradation ordering / cross-model transfer) was demoted during revision. The residual numbering gap is confusing and suggests incomplete editing. Renumber to C1/C2/C3 or consolidate.

**W6. The ~5pp gap to learned features complicates the narrative.** The paper reports learned representations (frozen embeddings + MLP) beat 15D features by ~5pp on ordinal accuracy (from the project data: the gap varies by experiment). While cross-model transfer (85% vs. 62%) is presented as a decisive argument for hand-crafted features, a reader focused on maximum performance will note that a better classifier exists but was not used for the main results. The paper should more explicitly frame this as a Pareto tradeoff (interpretability + transfer vs. raw accuracy) rather than dismissing the gap.

**W7. Scope narrowness relative to claims.** The paper evaluates only 1.5B and 7B models with nucleus sampling variants. The claims about K* being an "information-theoretic" property are made broadly, but the empirical evidence covers a narrow slice of the model-scale / decoding-strategy / domain space. No non-English text, no code, no domain-specific text, no models above 7B. The 7B result (K*>=3) rests on only 1K documents with a CI lower bound just 0.15pp above the threshold.

---

### 4. Detailed Comments

**Is K* genuinely novel, or a straightforward measurement?**
The *concept* of K* as a named, measured quantity is novel -- no prior work operationalizes this boundary. However, the *existence* of such a boundary is unsurprising: any practitioner who has generated multi-hop synthetic text would expect diminishing distinguishability. The novelty lies in (a) naming and formalizing K*, (b) measuring it systematically, and (c) demonstrating its controllability. Item (c) is the strongest element. Without the decoding ablation showing K*'s gradient, this would be closer to an empirical measurement paper with limited conceptual contribution.

**Is the "iterated lossy channel" framing a meaningful theoretical contribution?**
No. It is a motivation, not a contribution. DPI applied to a Markov chain is a standard observation. The paper should not list this as a theoretical contribution but rather as the motivating framework. The gap between DPI on the full joint distribution and classifier discriminability on 15D feature projections is substantial and under-acknowledged. K*_empirical is a feature-dependent, threshold-dependent lower bound on K*_theory -- the paper should state this more prominently.

**How well does the paper differentiate from Drayson et al. (2025)?**
Reasonably well. The binary-ours baseline is the correct experimental control. However, the comparison to Drayson's actual method (binary-Drayson in Table 9) is not fully controlled: Drayson uses soft importance resampling weights derived from continuous binary confidence, not hard binary decisions. The graduated vs. binary-Drayson comparison confounds the ordinal-vs-binary distinction with differences in the weighting scheme itself. A fairer comparison would use Drayson's SIR framework but replace the binary confidence with the ordinal depth estimate.

**Is the "scientific characterization" positioning sufficient for a top venue?**
Borderline. Characterization papers can succeed at top venues when they reveal something non-obvious and actionable. K*=2 is somewhat expected (practitioners know quality degrades fast), but the controllability gradient and the cross-model transfer results are non-trivial. The graduated filtering application strengthens the case. The dose-response showing monotonically increasing benefit with contamination severity is the best argument for practical relevance. Overall, I think the characterization contribution is just sufficient, but only because of the controllability result and the systematic cross-condition coverage.

**Does the paper honestly handle C3's limited advantage?**
The "best" paper draft (which I reviewed) reports strong gains (+2.48pp MMLU, +2.70pp HellaSwag, p<0.01), which differs materially from the earlier project notes mentioning "+0.6pp at 30% (p=0.08)" and "DSIR matches." If the strong gains are from the newer exp-006 experiments, this is fine, but there is a discrepancy worth flagging: the paper should clarify whether these are from the same experimental setup as the earlier modest results, or whether the setup changed (e.g., different alpha, different contamination simulation, different baseline implementations). If setup changes produced the improvement, this should be transparent.

**How does the cross-model transfer data hold up?**
From the actual experimental data (cross_transfer_matrix.csv), the Pythia->OLMo accuracy retention is 0.3531/0.3856 = 91.6%, which supports the 91% claim. However, this is at the ordinal-accuracy level; the mean_pairwise_AUC retention is 0.5937/0.6055 = 98%, which is arguably a better metric. The Qwen-rewrite -> Pythia transfer is much weaker: 0.259/0.4229 = 61.3%. The "91% transfer" figure cherry-picks the best pair (Pythia<->OLMo, same generation mode). The paper should report the full transfer matrix and average retention, not just the best case.

**Missing citation "[?]":**
This broken reference is visible in the introduction. It undermines the paper's preparation quality. Must be fixed before submission.

---

### 5. Questions for Authors

1. **Threshold sensitivity:** What are the K* values at theta = {0.55, 0.575, 0.625, 0.65}? Is the qualitative gradient (greedy < standard < high-temp) preserved across all reasonable thresholds, or does it collapse at theta=0.55 or theta=0.65?

2. **C3 discrepancy:** The project's earlier experimental notes report graduated filtering gains of +0.6pp (p=0.08) at 30% contamination, while the paper reports +2.48pp (p=0.004). What changed between these results? Different alpha, different baseline implementation, different continued pretraining setup?

3. **Cross-model transfer cherry-picking:** The "91% retention" figure comes from the Pythia<->OLMo pair (same generation mode, similar architecture family). The Qwen-rewrite -> Pythia transfer is 61%. What is the average retention across all 12 off-diagonal transfer pairs? Would the "depth signal is text-intrinsic" claim survive if the average is reported instead?

4. **Watermarking alternative:** If each generation stage applied a watermark, depth could be tracked without statistical classifiers. How do you position K*-based passive estimation against watermarking-based active provenance tracking? Is the contribution only relevant when watermarks are unavailable?

5. **Self-refinement false positives:** How does the depth classifier behave on text that has undergone multiple LLM self-refinement passes (e.g., iterative editing, chain-of-thought revision) but is not "recursive contamination"? Would such text be misclassified as high-depth?

---

### 6. Score and Confidence

**Score: 4/6 (Weak Accept)**

**Confidence: 4/5 (High)**

**Justification:** The paper introduces a genuinely novel concept (K* as a named, measurable, controllable quantity for recursive text depth) that is absent from the existing literature. The binary-to-ordinal reframing opens a new research direction. The decoding ablation establishing K* as a controllable property of the channel -- not a fixed constant -- is the paper's most compelling novelty claim and distinguishes it from a simple empirical measurement.

However, several factors keep this at weak accept rather than accept: (1) the DPI theory is standard and oversold; (2) K*=2 is operationally close to "binary with a soft middle," limiting practical novelty; (3) significant related work gaps (watermarking, Schaeffer taxonomy, Kazdan regimes) weaken the positioning; (4) the cross-model transfer figure appears cherry-picked; (5) broken references and C1/C3 numbering gap suggest incomplete preparation; (6) the scope is narrow (1.5B-7B, English web text, nucleus sampling only) relative to the generality of the claims.

For a top venue with ~25% acceptance, this paper is at the borderline. The community does learn something non-obvious (K* is controllable, not just a fixed boundary), and the characterization is systematic. But the contribution sits at a thin margin where the theta-sensitivity analysis could either confirm or undermine the core claims. I would lean accept conditional on the authors addressing the threshold sensitivity, related work gaps, and transfer matrix reporting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78816bf7-dae4-4b35-9b00-52f40170d1f6",
  "isSidechain": true,
  "agentId": "a8d7b6cd5cd8fadb4",
  "requestId": "req_011CazHfxKxB3PRNpBFuzuZU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e6fea1a-49c1-4eaf-b805-f0e79315bcb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "1e26fb29-8484-47f9-8c7e-3ea9127b1a2d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLqGsLGYFFcNr3rAMYQT5v",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 200,
      "cache_read_input_tokens": 70876,
      "output_tokens": 3542,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 200
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3542,
          "cache_read_input_tokens": 70876,
          "cache_creation_input_tokens": 200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 200,
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
