# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus areas are **novelty**, **related work positioning**, and *

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-afdff64cf4a9a2f1e.jsonl`
- **Structured JSON:** [`b339e774f18c6d0f6373.json`](../../sessions/b3/b339e774f18c6d0f6373.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

63 recorded events

### User

_source line 1 · 2026-05-13T08:48:22.161Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus areas are **novelty**, **related work positioning**, and **broader impact/significance**. Use a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept. Target venue acceptance rate ~25%.

## Paper Summary

**Title:** "Generational Depth Contamination: Measuring and Exploiting the Discrimination Boundary of Recursive Synthetic Text"

**Core idea:** Web training data is contaminated by recursively regenerated synthetic text. Existing detectors are binary (human vs machine). This paper formalizes recursive generation as an iterated lossy channel, invokes DPI to prove a finite "generational discrimination boundary" K* — the deepest generation at which pairwise depth discrimination remains statistically reliable. They then exploit the ordinal depth signal for "graduated filtering" that outperforms binary filtering.

**Claims:**
- C1 (K* Characterization): K*=2 for 1.5B models under standard decoding; K*≥3 at 7B scale and T=1.2. Greedy→K*=1 creates a controllable gradient.
- C3 (Graduated Filtering): K*-aware graduated filtering significantly outperforms binary filtering: +2.48pp MMLU, +2.70pp HellaSwag (p<0.01, 5 seeds). Gains scale monotonically with contamination rate.

**Related work cited:**
- Model Collapse: Shumailov et al. (2024), Alemohammad et al. (2024), Dohmatob et al. (2024) — characterize macroscopic collapse but don't provide depth detection tools
- Binary Detection: DetectGPT, Binoculars, DivEye — effective at human/synthetic boundary but near-chance at adjacent depths
- Data Curation: DSIR (distribution matching), Drayson et al. (2025) (binary importance resampling) — closest prior work, but binary

**Method:**
- Information-theoretic framework: recursive generation as iterated lossy channel, DPI guarantees finite K*
- 15D hand-crafted features (vocab diversity, surprisal, tail distribution, structural) + LightGBM
- Graduated filtering with 3-class ordinal signal and α-weighted gen-1
- θ=0.60 threshold for empirical K*

**Key results:**
- K*=2 (1.5B standard), K*=1 (greedy), K*=3 (T=1.2 or 7B scale)
- Feature degradation ordering consistent across configs (ρ≥0.878)
- Graduated filtering: +2.48pp MMLU, +2.70pp HellaSwag vs binary (p<0.01)
- Dose-response: gains monotonically increase with contamination rate
- LLM zero-shot ≈ random; binary detectors plateau at depth≥1
- 15D hand-crafted > frozen embeddings (1536D) with 85% vs 62% cross-model transfer
- Common Crawl: correlational validation (ρ=-0.288 AlignScore, ρ=-0.342 vocab richness)
- Retrain-chain validates prompt-chain as proxy (K* identical, AUC diff <2pp)

**Models:** Qwen2.5 (1.5B instruct, 1.5B base, 7B), Pythia-1.4B. No OLMo results in paper despite being mentioned in abstract context.

## Your Task (R2: Novelty + Related Work)

Produce a structured review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (bullet points, focus on novelty of contribution, significance, positioning vs prior work)
3. **Weaknesses** (bullet points, focus on novelty concerns, missing related work, scope of impact)
4. **Detailed Comments** — address at minimum:
   - How novel is the K* concept? Is it a genuine conceptual contribution or a straightforward application of DPI?
   - Is the "iterated lossy channel" framing novel or well-known in information theory?
   - How does this work relate to the model collapse literature more precisely? The boundary between "measuring depth" and "detecting collapse" seems thin.
   - Is the related work section comprehensive? Missing citations? (Consider: watermarking literature, data provenance, membership inference, iterative self-refinement, LLM-as-judge literature on quality estimation)
   - The paper lists C1 and C3 as contributions but skips C2 — is there a missing "degradation ordering" contribution?
   - Significance: is K*=2 practically useful given the coarse 3-class signal?
   - The "graduated filtering" concept seems simple (just α-weighting gen-1). Is this a meaningful contribution or incremental?
   - How does this compare to Drayson et al. (2025) more carefully? Is the improvement primarily from having 3 classes vs 2?
   - Broader impact: does this paper open new research directions?
   - Writing quality and presentation
5. **Questions for Authors** (3-5 specific questions)
6. **Score** (1-6) with one-line justification
7. **Confidence** (1-5: 1=low, 5=expert)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "aee8876d-7994-44e6-8255-382ac28c1010",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T08:48:22.166Z_

```json
{
  "parentUuid": "aee8876d-7994-44e6-8255-382ac28c1010",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
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
  "uuid": "658a47b0-f711-4ba0-9710-66b9b7bde89c",
  "timestamp": "2026-05-13T08:48:22.166Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T08:48:25.148Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "658a47b0-f711-4ba0-9710-66b9b7bde89c",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH7vi5fF1WD1tybvnXw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54d9b6ba-4626-4de8-84df-615598ec67da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014o6DgF1VbBv2xht9ik9WjB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7121,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7121,
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

_source line 4 · 2026-05-13T08:48:25.588Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KgqTnFZfRV6wVckj6rcFaV`</summary>

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
  "parentUuid": "54d9b6ba-4626-4de8-84df-615598ec67da",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH7vi5fF1WD1tybvnXw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0d1544f-2a18-433e-bacc-1e0ce5073abd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014o6DgF1VbBv2xht9ik9WjB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7121,
      "cache_read_input_tokens": 8250,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7121
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 124,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 7121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7121,
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

_source line 5 · 2026-05-13T08:48:25.591Z_

<details><summary>↩ Tool result · `toolu_01KgqTnFZfRV6wVckj6rcFaV`</summary>

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
  "parentUuid": "b0d1544f-2a18-433e-bacc-1e0ce5073abd",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "0ca4f29f-1075-4d31-bd31-9cf944ee820c",
  "sourceToolAssistantUUID": "b0d1544f-2a18-433e-bacc-1e0ce5073abd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T08:48:27.933Z_



Let me read the paper and project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ca4f29f-1075-4d31-bd31-9cf944ee820c",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH8BZntpNFzHJiAuLzn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce952a78-731c-44cf-8c68-46c7910546eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DkbxY7VMvWT1iD4QrDQYwZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 7 · 2026-05-13T08:48:28.559Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01NXHh6LzZAaYdTFVVVSPLL2`</summary>

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
  "parentUuid": "ce952a78-731c-44cf-8c68-46c7910546eb",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH8BZntpNFzHJiAuLzn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "011d51be-7ba5-44a8-972e-08c305a3ebff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DkbxY7VMvWT1iD4QrDQYwZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 8 · 2026-05-13T08:48:28.612Z_

<details><summary>↩ Tool result · `toolu_01NXHh6LzZAaYdTFVVVSPLL2`</summary>

```text
{"result":"# 项目 gen-depth-contamination 概况\n\n## 实验状态 (9 个)\n\n- **exp_013_cross_transfer**: DONE (success) — \n- **exp_005_degradation**: DONE (success) — \n- **exp_007_bootstrap_ci**: DONE (success) — \n- **exp_003_decoding_ablation**: RUNNING — \n- **exp_017_qwen_continuation**: DONE (success) — \n- **exp_010_ordinal_baseline**: DONE (success) — \n- **exp_002_olmo_depth**: DONE (success) — \n- **exp_001_pythia_depth**: DONE (success) — \n- **mvp_pilot_sat_v1**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-13\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_003_decoding_ablation | 解码策略调控 K*：不同 top_p/temperature 设置是否改变饱和边界（greedy→更低 K*? 高温度→更高 K*?） | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_013_cross_transfer** (success): Depth signal 是文本固有属性还是 model self-familiarity artifact？4×4 cross-model transfer matrix 测试分类器跨模型泛化能力\n- **exp_005_degradation** (success): —\n  [exp005_degradation_analysis](autodl-4090d:/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/degradation_analysis.json)\n- **exp_007_bootstrap_ci** (success): K* 统计严谨性验证：bootstrap 95% CI 和 permutation test 确认 K*=2 在三个模型族上统计显著\n\n## 趋势\n成功 8 / 负向 0 / 失败 0 / 共 8\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-4090d: 空闲 cuda:0\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "011d51be-7ba5-44a8-972e-08c305a3ebff",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "60a0b8d7-1b96-4c0f-b05c-b0e6e61c40c3",
  "sourceToolAssistantUUID": "011d51be-7ba5-44a8-972e-08c305a3ebff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T08:48:29.390Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YBo8G62SLdGyRmUc1bJHib`</summary>

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
  "parentUuid": "60a0b8d7-1b96-4c0f-b05c-b0e6e61c40c3",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH8BZntpNFzHJiAuLzn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ff84de8-05ba-4011-8ad7-dfc5c7f77aa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DkbxY7VMvWT1iD4QrDQYwZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 10 · 2026-05-13T08:48:29.400Z_

<details><summary>↩ Tool result · `toolu_01YBo8G62SLdGyRmUc1bJHib`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_003_decoding_ablation | 解码策略调控 K*：不同 top_p/temperature 设置是否改变饱和边界（greedy→更低 K*? 高温度→更高 K*?） | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_013_cross_transfer** (success): Depth signal 是文本固有属性还是 model self-familiarity artifact？4×4 cross-model transfer matrix 测试分类器跨模型泛化能力\\n- **exp_005_degradation** (success): —\\n  [exp005_degradation_analysis](autodl-4090d:/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/degradation_analysis.json)\\n- **exp_007_bootstrap_ci** (success): K* 统计严谨性验证：bootstrap 95% CI 和 permutation test 确认 K*=2 在三个模型族上统计显著\\n\\n## 趋势\\n成功 8 / 负向 0 / 失败 0 / 共 8\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-4090d: 空闲 cuda:0\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 811, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ff84de8-05ba-4011-8ad7-dfc5c7f77aa1",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "38d51442-f81d-4721-9c9c-4fca2a9cf77f",
  "sourceToolAssistantUUID": "0ff84de8-05ba-4011-8ad7-dfc5c7f77aa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T08:48:29.689Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Gs7YpFeLidhvU6S8YNArf6`</summary>

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
  "parentUuid": "38d51442-f81d-4721-9c9c-4fca2a9cf77f",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH8BZntpNFzHJiAuLzn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f30c7e42-638c-425b-bff5-d6f269e72e0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DkbxY7VMvWT1iD4QrDQYwZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15371,
      "output_tokens": 268,
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
          "output_tokens": 268,
          "cache_read_input_tokens": 15371,
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

_source line 12 · 2026-05-13T08:48:29.703Z_

<details><summary>↩ Tool result · `toolu_01Gs7YpFeLidhvU6S8YNArf6`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f30c7e42-638c-425b-bff5-d6f269e72e0f",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "d4caf95a-d5d2-431b-8353-e5395f06c151",
  "sourceToolAssistantUUID": "f30c7e42-638c-425b-bff5-d6f269e72e0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T08:48:32.660Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01EyV6M1Rqk2ea4zuNp9Ze8m`</summary>

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
  "parentUuid": "d4caf95a-d5d2-431b-8353-e5395f06c151",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH8VAx7zs7Ke85ZMoa5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b21a34ce-e397-4314-bd19-79589dcfb55b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xNMdoNo6KVaDYpkwiHXfJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1698,
      "cache_read_input_tokens": 16817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1698,
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

_source line 14 · 2026-05-13T08:48:32.671Z_

<details><summary>↩ Tool result · `toolu_01EyV6M1Rqk2ea4zuNp9Ze8m`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/literature_map.yaml\", \"content\": \"papers:\\n  # === Must-Cite ===\\n\\n  - id: drayson2025\\n    title: \\\"Machine-generated text detection prevents language model collapse\\\"\\n    authors: \\\"Drayson, Yilmaz, Lampos\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n    code: \\\"https://github.com/GeorgeDrayson/model_collapse\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Binary MGT detection + importance resampling for collapse prevention; our depth estimator generalizes their binary detector to ordinal depth\\\"\\n    cited: false\\n    methodology: >\\n      Binary MGT detector (encoder-only transformer + classification head; best: ModernBERT-150M, AUC .986 in-dist, .943 OOD).\\n      Fine-tuned 5 epochs with label smoothing α=0.1 + temperature scaling.\\n      Sampling Importance Resampling (SIR): w_j = (1-q(x_j))^b / Σ(1-q(x_l))^b, where q(x) = P(machine-generated), b≥1 bias term.\\n      Resample at k=1.5 (50% upsampling). Evaluated on GPT-2 and SmolLM2 (124M–1.7B).\\n    key_findings:\\n      - \\\"SIR filtering not only prevents collapse but improves over human-only training (perplexity -0.85% to -25.65%, diversity +3.44% to +14.62%, MAUVE +8.46% to +20.92%)\\\"\\n      - \\\"ModernBERT achieves best detection (AUC .986 in-dist); optimal threshold 0.8674 on imbalanced data (29% human)\\\"\\n      - \\\"Curated synthetic data has positive value — outperforms oracle (perfect filter) in equal-ratio settings\\\"\\n      - \\\"Only evaluates fine-tuning (not pretraining), models ≤2B, open-ended generation only\\\"\\n    positioning_notes: >\\n      Closest prior work. Their SIR is a special case of our graduated filtering when K*=1 (binary: human vs all synthetic).\\n      We generalize binary→ordinal: estimate depth d∈{0,1,...,K*} and apply depth-graduated weights.\\n      K* tells when ordinal signal adds value over binary. They never discuss ordinal depth or multi-class estimation.\\n      Our C3 claim directly extends their framework: \\\"even coarse 3-class signal yields better calibration at decision boundaries.\\\"\\n\\n  - id: schaeffer2025position\\n    title: \\\"Position: Model Collapse Does Not Mean What You Think\\\"\\n    authors: \\\"Schaeffer, Kazdan, Arulandu, Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2503.03150\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"framing-critical\\\"\\n    relevance: \\\"Identifies 8 definitions of model collapse across 3 families; forces us to position K* as discriminability saturation (distribution deformation), not test-loss collapse\\\"\\n    cited: false\\n    methodology: >\\n      Position paper. Surveys model collapse literature and identifies 8 distinct definitions organized in 3 families.\\n      Evaluates each definition against realistic deployment conditions. No experiments—purely analytical/argumentative.\\n    key_findings:\\n      - \\\"8 definitions in 3 families: (A) Population risk degrading [D1: catastrophic increase, D2: any increase, D3: asymptotic divergence]; (B) Distributions deforming [D4: collapsing variance, D5: scaling law change, D6: mode disappearance/entanglement, D7: tail data loss]; (C) Spurious generation [D8: hallucinated data]\\\"\\n      - \\\"Under realistic conditions (data accumulation, growing compute), catastrophic risk divergence (D1-D3) is avoidable\\\"\\n      - \\\"Real harms—tail data loss (D7) and mode entanglement (D6)—have received disproportionately less attention\\\"\\n      - \\\"Recommends researchers explicitly state which definition they study\\\"\\n    positioning_notes: >\\n      K* belongs to Family B (distributions deforming), specifically D4 (collapsing variance) + D6 (mode entanglement).\\n      K* measures when distribution deformation renders generations indistinguishable in feature space.\\n      K* is NOT about population risk (Family A). This distinction is critical for framing:\\n      we contribute a diagnostic for exactly the harms Schaeffer et al. identify as underexplored.\\n      Adopt their taxonomy explicitly in Related Work to anchor K* precisely.\\n\\n  - id: kazdan2025collapse\\n    title: \\\"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\\\"\\n    authors: \\\"Kazdan, Schaeffer, Dey, Gerstgrasser, Rafailov, Donoho, Koyejo\\\"\\n    venue: \\\"ICML 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2410.16713\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Accumulate vs replace regimes affect contamination dynamics; in accumulate regime K* may shift upward\\\"\\n    cited: false\\n    methodology: >\\n      Formal comparison of 3 data regimes: Replace (train on latest synthetic only; Σ→0 a.s.),\\n      Accumulate (train on all historical data; real fraction→0 but stability holds),\\n      Accumulate-subsample (fixed budget from accumulated pool; intermediate degradation).\\n      Theory: Gaussian setting with closed-form limits. Experiments: multivariate Gaussian, KDE, LLM SFT (Gemma2-2B on HelpSteer2/TinyStories).\\n    key_findings:\\n      - \\\"Replace: covariance collapses to 0 (a.s.), W2 diverges. Collapse inevitable within 5-10 iterations\\\"\\n      - \\\"Accumulate: covariance stabilizes at σ₀²·sin(π/√n)/(π/√n). No collapse even as real data fraction→0\\\"\\n      - \\\"Accumulate-subsample: degradation plateaus rather than diverges\\\"\\n      - \\\"Cardinality of real data matters more than proportion (R²=0.59 vs 0.34)\\\"\\n    positioning_notes: >\\n      Our prompt-chain = replace regime (harshest setting). K*=2 measured under replace conditions.\\n      This makes K*=2 a conservative lower bound: under accumulate regime (more realistic), K* would shift upward.\\n      Strengthens our result: if depth estimation adds value at K*=2 under replace, it adds more under accumulate.\\n      Cite to justify experimental design and contextualize K* as regime-dependent.\\n\\n  - id: shi2025generalization\\n    title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n    authors: \\\"Shi, Wu, Zhang, Zhang, Tao, Qu\\\"\\n    venue: \\\"NeurIPS 2025 Spotlight\\\"\\n    url: \\\"https://arxiv.org/abs/2509.16499\\\"\\n    code: \\\"https://shilianghe007.github.io/model-collapse/\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Generalization-to-memorization transition in iterative retraining parallels our feature-space convergence; entropy decrease over iterations aligns with our depth-discriminative features\\\"\\n    cited: false\\n    methodology: >\\n      Study iterative retraining of diffusion models (DDPM) on CIFAR-10 subsets (1K–32K images).\\n      Generalization Score (GS): avg distance between generated and nearest training image.\\n      Entropy: Kozachenko-Leonenko estimator. Strong correlation: Pearson r=0.91 between entropy and log(GS).\\n      Mitigation: entropy-based data selection (greedy max-NN-distance + threshold-decay filter).\\n    key_findings:\\n      - \\\"GS drops approximately exponentially across iterations; collapse within 5-10 iterations for large datasets\\\"\\n      - \\\"Training data entropy is a direct predictor of generalization capability (r=0.91)\\\"\\n      - \\\"Entropy-based data selection mitigates memorization transition\\\"\\n      - \\\"Diffusion models only; no LLM experiments. No theoretical analysis of WHY entropy collapses\\\"\\n      - \\\"Generated images form tight local clusters while overall variance remains relatively stable\\\"\\n    positioning_notes: >\\n      Parallel phenomenon across modalities: their entropy decline ↔ our JSD decrease (0.27→0.004).\\n      Their \\\"GS drops exponentially\\\" ↔ our feature-space divergence vanishes rapidly → K*=2.\\n      Key distinction: they measure output-distribution entropy; we measure discriminability in feature space.\\n      K* complements their entropy metric: operationalizes \\\"at what depth does entropy decline = indistinguishability?\\\"\\n      Their clustering-while-variance-stable parallels our depth features converging before global statistics.\\n      Cite for cross-modal validation of convergence phenomenon.\\n\\n  # === Should-Cite ===\\n\\n  - id: basani2026diveye\\n    title: \\\"DivEye: Diversity Boosts AI-Generated Text Detection\\\"\\n    authors: \\\"Basani, Chen\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2509.18880\\\"\\n    code: \\\"https://github.com/IBM/diveye\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Surprisal diversity features as potential baseline for depth estimation; zero-shot detector outperforms prior work by 33.2%\\\"\\n    cited: false\\n\\n  - id: amin2025escaping\\n    title: \\\"Escaping Collapse: The Strength of Weak Data for Large Language Model Training\\\"\\n    authors: \\\"Amin et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2502.08924\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Boosting-inspired framework showing weak signal suffices for iterative training; motivates practical utility of imperfect depth estimators\\\"\\n    cited: false\\n\\n  - id: zawalski2026codec\\n    title: \\\"CoDeC: Detecting Data Contamination in LLMs via In-Context Learning\\\"\\n    authors: \\\"Zawalski et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2510.27055\\\"\\n    category: \\\"contamination\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Binary contamination detection via ICL confidence shifts; complementary to our finer-grained depth estimation approach\\\"\\n    cited: false\\n\\n  - id: gambetta2025surplexity\\n    title: \\\"Learning by Surprise: Surplexity for Mitigating Model Collapse\\\"\\n    authors: \\\"Gambetta et al.\\\"\\n    venue: \\\"arXiv preprint 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2410.12341\\\"\\n    category: \\\"verification-curation\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Surprise-based collapse metric; surplexity scores as potential feature for depth estimation pipeline and baseline comparison\\\"\\n    cited: false\\n\\n  - id: zhang2024minkpp\\n    title: \\\"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\\\"\\n    authors: \\\"Zhang, Zheng, Gao, Miao\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Binary detection baseline; does not distinguish generational depth\\\"\\n    cited: false\\n\\n  - id: shumailov2024collapse\\n    title: \\\"AI models collapse when trained on recursively generated data\\\"\\n    authors: \\\"Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal\\\"\\n    venue: \\\"Nature 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Seminal model collapse result; describes macro phenomenon but provides no detection tool for depth\\\"\\n    cited: false\\n\\n  - id: alemohammad2024selfconsuming\\n    title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n    authors: \\\"Alemohammad, Casco-Rodriguez, Luber, Babaei, Letizia, Bastani, Baraniuk\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Theoretical and empirical analysis of iterative generative training; complements Shumailov with formal convergence analysis\\\"\\n    cited: false\\n\\n  - id: dohmatob2024model\\n    title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n    authors: \\\"Dohmatob, Feng, Yang, Charton, Kempe\\\"\\n    venue: \\\"ICML 2024\\\"\\n    category: \\\"model-collapse\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Scaling law perspective on collapse; tail distribution loss aligns with our observed feature convergence\\\"\\n    cited: false\\n\\n  - id: xie2023dsir\\n    title: \\\"Data Selection with Importance Resampling\\\"\\n    authors: \\\"Xie, Santurkar, Ma, Liang\\\"\\n    venue: \\\"ICML 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Distribution-matching data selection baseline; does not estimate recursive depth\\\"\\n    cited: false\\n\\n  - id: tirumala2024d4\\n    title: \\\"D4: Improving LLM Pretraining via Document De-Duplication and Diversification\\\"\\n    authors: \\\"Tirumala, Markosyan, Zettlemoyer, Aghajanyan\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Deduplication + diversification baseline for data curation; orthogonal to depth-based filtering\\\"\\n    cited: false\\n\\n  - id: xie2024doremi\\n    title: \\\"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\\\"\\n    authors: \\\"Xie, Pham, Dong, Du, Liu, Lu, Liang, Le, Ma, Yu\\\"\\n    venue: \\\"NeurIPS 2023\\\"\\n    category: \\\"data-selection\\\"\\n    role: \\\"evaluation\\\"\\n    relevance: \\\"Domain reweighting for pretraining; does not consider generational depth dimension\\\"\\n    cited: false\\n\\n  - id: kirchenbauer2023watermark\\n    title: \\\"A Watermark for Large Language Models\\\"\\n    authors: \\\"Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein\\\"\\n    venue: \\\"ICML 2023\\\"\\n    category: \\\"watermarking\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Provenance tracking via watermarking; complementary approach to depth estimation when watermarks are available\\\"\\n    cited: false\\n\\n  - id: zellers2019grover\\n    title: \\\"Defending Against Neural Fake News\\\"\\n    authors: \\\"Zellers, Holtzman, Rashkin, Bisk, Farhadi, Roesner, Choi\\\"\\n    venue: \\\"NeurIPS 2019\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Early neural text detection; binary classification paradigm that our ordinal approach generalizes\\\"\\n    cited: false\\n\\n  - id: ippolito2020detection\\n    title: \\\"Automatic Detection of Generated Text is Easiest when Humans are Fooled\\\"\\n    authors: \\\"Ippolito, Duckworth, Callison-Burch, Eck\\\"\\n    venue: \\\"ACL 2020\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Binary detection difficulty analysis; does not consider multi-generational depth\\\"\\n    cited: false\\n\", \"total_chars\": 13194, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b21a34ce-e397-4314-bd19-79589dcfb55b",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "4ae2f161-7e1b-46f4-be4f-c5f0d4410021",
  "sourceToolAssistantUUID": "b21a34ce-e397-4314-bd19-79589dcfb55b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T08:48:33.599Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Byg7bPa2RVhH8dvHhzJu3Z`</summary>

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
  "parentUuid": "4ae2f161-7e1b-46f4-be4f-c5f0d4410021",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH8VAx7zs7Ke85ZMoa5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7522ec90-9be8-48cf-9e3f-fe9c7a535afd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xNMdoNo6KVaDYpkwiHXfJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1698,
      "cache_read_input_tokens": 16817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1698,
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

_source line 16 · 2026-05-13T08:48:33.609Z_

<details><summary>↩ Tool result · `toolu_01Byg7bPa2RVhH8dvHhzJu3Z`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-contamination\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\\n- Fallback: EMNLP 2026 Findings\\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\\n\\n## Canonical Experimental Condition\\n\\n**Continuation mode 是 cross-model 结论的基础。**\\n\\n> \\\"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\\\"\\n\\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\\n|-----------|-------------|-------------|---------|\\n| Continuation | 91-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\\n\\n**原则**：\\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\\n- mvp-001 (Qwen-rewrite) 定位为 \\\"pilot study demonstrating feasibility\\\"，后续用 continuation mode rigorously validate\\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\\n\\n## Core Claims (2+1 结构, D012)\\n\\n### Primary: C1' (K* Characterization)\\n首次系统测量递归合成文本的 generational discrimination boundary K*。\\n\\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 4-model × 2-mode 实验矩阵系统表征 K*_empirical 的行为，包括跨模型一致性、特征退化排序、以及 generation mode 对 depth signal 的调控效应。\\n\\n**子组件：**\\n\\n**(a) K* = 2 across all tested configurations**\\n> 4-model 1v2 bootstrap 95% CI 汇总：\\n> | Model | AUC 1v2 | 95% CI | CI lower > 0.60? |\\n> |-------|---------|--------|-----------------|\\n> | Qwen-rewrite | 0.6955 | [0.6859, 0.7041] | ✅ (+8.6pp) |\\n> | Pythia-1.4B | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\\n> | OLMo-1B | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\\n> | Qwen-cont | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp, 最边缘) |\\n>\\n> - 全部 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60, 全部 permutation p < 0.002\\n> - K* 不是离散跳变值，而是 CI-bounded continuum threshold\\n> - Paper 可写：\\\"K*=2 (bootstrap 95% CI for AUC₁ᵥ₂ > 0.60 across all four model configurations; AUC₂ᵥ₃ CI upper < 0.60)\\\"\\n\\n**(b) Cross-model transfer**\\n> - Pythia↔OLMo 91% accuracy retention → K*=2 不是 model self-familiarity artifact\\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\\n> - 1v2+ transfer 取决于模型族相似度 → 与 K*=2 完美一致（K* 之上分辨力本就微弱）\\n> - depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity\\n\\n**(c) Degradation ordering consistency**\\n> - Spearman ρ ≥ 0.85 on single-feature AUC ranking（mode-controlled, continuation）\\n> - Top discriminative features shared: surp_d1_std, surp_std, surp_d2_std\\n> - Limitation: depth-pair level 一致性在 1v2 处较弱（τ~0.37）\\n> - Metric: single-feature AUC ranking（model-free, not LightGBM split count）\\n\\n**(d) Generation mode analysis (§4.x Analysis subsection)**\\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\\n> - 论文定位：Analysis subsection（\\\"How does generation mode affect depth estimation?\\\"），不是独立 claim\\n\\n### Secondary: C3 (Graduated Filtering)\\n即使在 K*=2 的粗粒度 ordinal signal（human/gen-1/gen-2+ 三级）下，K*-aware graduated filtering 仍优于 binary filtering，因为 ordinal signal 在阈值附近提供更 calibrated 的质量估计。\\n\\n### Supporting Analysis: Canonical Condition Selection\\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\\n\\n## Story Spine\\n\\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\\\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\\\"。通过 4-model × 2-mode 实验矩阵系统表征 K*，揭示控制因素（模型架构、解码策略、generation mode），为数据治理提供 actionable guidance。\\n- **Headline result template**: \\\"We establish K*=2 as the generational discrimination boundary for 1.5B-scale models under standard decoding, with depth features that are 70-85% text-intrinsic (Pythia↔OLMo 91% transfer retention). Even this coarse 3-class signal yields X% improvement over binary filtering on MMLU/HellaSwag.\\\"\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n1. **\\\"K*=2 太浅，graduated filtering 收益有限\\\"** → K* 是模型/解码策略依赖的；展示不同解码策略如何调控 K*（exp-003）；即使 K*=2，3-class 比 binary 在阈值附近更 calibrated（exp-006）\\n2. **\\\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\\\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ generation mode analysis，不是分类器本身\\n3. **\\\"Prompt-chain 不代表真实世界递归污染\\\"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法\\n4. **\\\"单模型/单数据集，泛化性不够\\\"** → 3 个模型族 × 2 种 generation mode + 4×4 cross-model transfer matrix\\n5. **\\\"同模型做生成和 surprisal 计算有 bias\\\"** → **exp-013 直接反驳**：Pythia↔OLMo 91% accuracy retention，0v1 transfer AUC > 0.96。Depth signal 主要编码在文本而非 model self-familiarity\\n6. **\\\"为什么不用 learned representations\\\"** → 作为 baseline 对比；hand-crafted features 更 interpretable 且支持 degradation ordering 分析\\n7. **\\\"Graduated filtering 没和 data selection methods 比\\\"** → exp-006 包含 DSIR baseline + α sensitivity sweep\\n8. **\\\"K* 的统计不确定性未量化\\\"** → 4-model bootstrap CI + permutation test（exp-007）\\n\\n## Venue Fit\\n\\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\\n- 2+1 claim 结构：C1' 是 comprehensive characterization study，C3 是 practical application，generation mode analysis 增加深度\\n- 风险：如果审稿人偏 methods，K*=2 + standard classifier 可能被认为贡献不足 → 强调 problem formulation + characterization + transfer analysis 的 novelty\\n\", \"total_chars\": 6221, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7522ec90-9be8-48cf-9e3f-fe9c7a535afd",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "9ee50536-7b2a-4ff0-8596-2637249860eb",
  "sourceToolAssistantUUID": "7522ec90-9be8-48cf-9e3f-fe9c7a535afd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T08:48:34.116Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TqpNtfLGVdNGZ7evy7F7aK`</summary>

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
  "parentUuid": "9ee50536-7b2a-4ff0-8596-2637249860eb",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH8VAx7zs7Ke85ZMoa5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cb32baf-34fe-4ea2-88c4-8bc0cce66fb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xNMdoNo6KVaDYpkwiHXfJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1698,
      "cache_read_input_tokens": 16817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1698,
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

_source line 18 · 2026-05-13T08:48:34.130Z_

<details><summary>↩ Tool result · `toolu_01TqpNtfLGVdNGZ7evy7F7aK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md\", \"content\": \"# gen-depth-contamination — Research Dashboard\\n\\n> 最后更新: 2026-05-13 07:50 UTC | 更新原因: exp-006 估算 ~21h（非 72h），deadline 倒排修订，timeline 宽裕\\n\\n## 核心方向\\n递归合成文本的代际深度估计：测量 K*（饱和边界）+ graduated filtering 应用。Route B framing（K* 作为 operational quantity）。Drayson et al. (EMNLP 2025) = closest prior work (binary filtering)，我们是 ordinal 推广。2+1 claim 结构（D012）：C1'(K* characterization) + C3(graduated filtering) + supporting analysis。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（P0 实验收尾）+ 审稿通道已开\\n- **实验**: 8 DONE / 1 RUNNING / 9 planned (18 total)\\n- **K*=2**: 4/4 model configs 确认，bootstrap 95% CI 全 > 0.60\\n- **C1' 子组件**: (a) K*=2 ✅ (b) cross-transfer ✅ (c) degradation ordering ✅ (d) mode analysis ✅\\n- **C3**: exp-006 脚本就绪，等 GPU（D013 fallback 预案已建立）\\n- **paper_framing.md**: D012 重构完成（2+1 结构）\\n- **关键路径**: exp-003 (~8h) → exp-006 (~21h) → analysis + writing → 05-25 ARR\\n\\n## 近期任务\\n- [ ] exp-003 decoding ablation 完成 + 结果收集（RUNNING，~8h 剩余）\\n- [ ] exp-006 启动（exp-003 完成后 GPU **零间隔**切换，~21h，C3 核心证据）\\n- [ ] exp-003 bootstrap CI for 4 decoding configs（CPU，exp-003 完成后）\\n- [ ] exp-005 registry Spearman ρ 补全（Agent CPU 任务，进行中）\\n- [ ] exp-004 cross-scale probe Qwen-7B（P0, 8h budget，exp-006 后或并行）\\n- [ ] 论文写作启动（exp-006 结果后）\\n- [x] exp-006 脚本 + dry-run 就绪（6 策略 × 5 seeds × α sweep）\\n- [x] D012 paper_framing.md 重构完成（2+1 结构）\\n- [x] K*=2 四模型 bootstrap CI (exp-007)\\n- [x] Cross-model transfer 4×4 matrix (exp-013)\\n- [x] C2 qualified claim (D011)\\n- [x] Generation mode effect (exp-017)\\n\\n## GPU 预算\\n- 分配：1×RTX 4090D (cuda:0) on autodl-4090d\\n- 已消耗（实际）：~20h（actual/budget ratio ≈ 40%）\\n- 剩余关键：exp-006 ~21h + exp-004 ~3h (估)\\n- DDL: 05-25 ARR（12 天）\\n\\n## Deadline 倒排（修订）\\n| 日期 | 里程碑 |\\n|------|--------|\\n| ~05-14 | exp-003 完成，exp-006 立即启动 |\\n| ~05-15 | exp-006 完成（~21h 估算） |\\n| ~05-16 | exp-006 分析 + exp-004 (optional) |\\n| ~05-17 | 论文写作启动（Paper Agent） |\\n| ~05-22 | 初稿完成，提交审稿 |\\n| ~05-24 | 修订定稿 |\\n| 05-25 | ARR 提交 |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D013 | 2026-05-13 | C3 exp-006 单点依赖风险评估 + fallback story 预案 | exp-006, exp-003 |\\n| D012 | 2026-05-13 | 论文 claim 重构：4 claims → 2+1 结构（C1' K* characterizat | exp-013, exp-006 |\\n| D011 | 2026-05-13 | D010 修正：C2 从 \\\"supplementary\\\" 升级为 \\\"qualified claim\\\" | exp-005, exp-017 |\\n| D010 | 2026-05-13 | C2 Plan A 否决 → 执行 Plan B：degradation ordering 限定为  | exp-017, exp-005 |\\n| D009 | 2026-05-13 | C2 战略评估：C1 是承重墙，C3 是安全网，C2 是加分项；exp-016 列为场景 B 应急 | exp-005, exp-017, exp-006, exp-016 |\\n| D008 | 2026-05-13 | C2 claim 暂停写入论文——等 exp-017 解耦 generation mode 因素后决 | exp-005, exp-017 |\\n| D007 | 2026-05-13 | Drayson novelty 评估完成：核心 novelty 安全，Story Spine 微调， | exp-006 |\\n| D006 | 2026-05-13 | 回滚 Drayson et al. 引用清理——Reviewer 确认为真实论文 (EMNLP 20 | — |\\n| D005 | 2026-05-13 | Dream 分析完成：proceed with P0, 整合 8 项确认行动到 framing/pl | exp-006, exp-007, exp-015 |\\n| D004 | 2026-05-12 | Reviewer 审查后修正：C1 区分 K*_empirical vs K*_theory；exp | — |\\n\\n\\n\\n\", \"total_chars\": 2847, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cb32baf-34fe-4ea2-88c4-8bc0cce66fb0",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "6057efd0-590d-426d-b36d-ae61b1ed9823",
  "sourceToolAssistantUUID": "4cb32baf-34fe-4ea2-88c4-8bc0cce66fb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T08:48:34.671Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JGcV6VFqMpCXQAqXmCt4r9`</summary>

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
  "parentUuid": "6057efd0-590d-426d-b36d-ae61b1ed9823",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH8VAx7zs7Ke85ZMoa5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0324b58a-9ba4-4329-857d-f912cc62f6d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xNMdoNo6KVaDYpkwiHXfJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1698,
      "cache_read_input_tokens": 16817,
      "output_tokens": 384,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1698
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 384,
          "cache_read_input_tokens": 16817,
          "cache_creation_input_tokens": 1698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1698,
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

_source line 20 · 2026-05-13T08:48:34.684Z_

<details><summary>↩ Tool result · `toolu_01JGcV6VFqMpCXQAqXmCt4r9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/memory.md\", \"content\": \"# Memory — gen-depth-contamination\\n\\n## 已知问题\\n\\n### right-padding (2026-05-12)\\nMVP pipeline 使用 right-padding（transformers 默认）。Director 确认对 MVP 判定无影响（所有 depth 一致受影响），不中断当前实验。**full study 阶段必须修复为 `tokenizer.padding_side = \\\"left\\\"`**，否则 batch 生成时 padding tokens 会影响生成质量的绝对水平。\\n\\n## GPU 优化建议 (2026-05-12)\\n\\n### batch size 调优\\n4090D 24GB 跑 1.5B fp16 模型仅用 3.9GB 显存 (16%)，GPU 利用率 45%。\\n- Step 3 生成：batch_size 16→**64**（保守）或 128\\n- Step 4 特征提取：feat_batch_size 8→**24**（保守）或 32\\n- 预估节省 ~74 min (38%)，加 flash-attn 可再省 10-15%\\n- full study 时一并修复\\n\\n## AutoDL 环境经验\\n\\n### C4 数据集加载 (2026-05-12)\\nAutoDL 代理下 `load_dataset(\\\"allenai/c4\\\", \\\"en\\\", streaming=True)` 会触发全量文件树解析（数千个 shard 的分页 API 请求），ProxyError 无限重试。修复：用单 shard URL 直接加载 + `HF_ENDPOINT=https://hf-mirror.com` 中转。\\n\\n### 环境变量必须固化到启动脚本 (2026-05-12)\\nAutoDL 上 `source /etc/network_turbo`、SSL 证书、HF 配置等环境变量不能只在 shell session 里 export，必须写入 `run_mvp.sh` 等包装脚本，否则 tmux session 里不生效。\\n\\n### submit_training_job pid=\\\"unknown\\\" 问题 (2026-05-13)\\nsubmit_training_job 有时返回 pid=\\\"unknown\\\"，导致 registry 状态停在 PREPARING、cron 未创建。exp-017 和 exp-003 都遇到此问题。**解决方式**：提交后必须派 Worker SSH 检查实际进程状态（tmux ls + ps aux），手动修正 registry 并注册 cron。\\n\\n## 实验设计决策\\n\\n### Generation mode 影响 depth signal 强度 (2026-05-13)\\nRewrite mode（instruction prompting）比 continuation mode 多产生 ~8.4pp AUC 差距（Qwen: 0.6957 vs 0.6114）。原因推测：instruction-following 引入更大的分布偏移，放大 depth-discriminative 信号。论文中 K* 应同时报告两种 mode 的结果；C1 robustness 依赖 continuation mode（更保守的 lower bound）。\\n\\n### Degradation ordering mode-dependent (2026-05-13)\\n4-model τ 矩阵表明 generation mode 贡献 ~60-70% 的排序偏离，架构 ~30-40%。C2 claim 不能说 \\\"universal ordering\\\"，应改为 \\\"mode-conditioned consistency with architecture residuals\\\"。Director 决策 D008 的后续：4-model τ 数据已齐全，等 Director 确认 C2 最终措辞。\\n\", \"total_chars\": 1706, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0324b58a-9ba4-4329-857d-f912cc62f6d2",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "a04456d8-ca1d-4535-bc7f-f5358b1f0d01",
  "sourceToolAssistantUUID": "0324b58a-9ba4-4329-857d-f912cc62f6d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-13T08:48:37.775Z_

Now let me read the actual paper artifacts and key experimental results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a04456d8-ca1d-4535-bc7f-f5358b1f0d01",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH8rXb3owQ7Gjn4BDgR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8df2975-0fda-44dc-8315-54c9ec586648",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WAeSNHE5fhoYkvastUzV6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11366,
      "cache_read_input_tokens": 18515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11366,
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

_source line 22 · 2026-05-13T08:48:38.411Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PcUvQLAhxZTmpvwC2EUatk`</summary>

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
  "parentUuid": "a8df2975-0fda-44dc-8315-54c9ec586648",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH8rXb3owQ7Gjn4BDgR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fb36562-de60-4994-8e58-2873f49850df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WAeSNHE5fhoYkvastUzV6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11366,
      "cache_read_input_tokens": 18515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11366,
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

_source line 23 · 2026-05-13T08:48:38.423Z_

<details><summary>↩ Tool result · `toolu_01PcUvQLAhxZTmpvwC2EUatk`</summary>

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
  "parentUuid": "9fb36562-de60-4994-8e58-2873f49850df",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "5686dd8d-fda3-4a4e-aaa0-975d43670cb7",
  "sourceToolAssistantUUID": "9fb36562-de60-4994-8e58-2873f49850df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-13T08:48:39.183Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01BJJNEgyDDuPyVXortV6mgK`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5686dd8d-fda3-4a4e-aaa0-975d43670cb7",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH8rXb3owQ7Gjn4BDgR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50f9210e-942b-4b06-af1b-24ae93c54012",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WAeSNHE5fhoYkvastUzV6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11366,
      "cache_read_input_tokens": 18515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11366,
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

_source line 25 · 2026-05-13T08:48:39.193Z_

<details><summary>↩ Tool result · `toolu_01BJJNEgyDDuPyVXortV6mgK`</summary>

```text
artifacts/dream_reports/dream_20260512T200328/best/paper.pdf
artifacts/dream_reports/dream_20260512T200328/median/paper.pdf
artifacts/dream_reports/dream_20260512T200328/worst/paper.pdf
artifacts/_project/chart/auc_heatmap.pdf
artifacts/figures/auc_heatmap.pdf
artifacts/_project/chart/feature_importance.pdf
artifacts/figures/feature_importance.pdf
artifacts/_project/chart/jsd_decay.pdf
artifacts/figures/jsd_decay.pdf
artifacts/dream_reports/dream_20260513T080728/best/paper.pdf
artifacts/dream_reports/dream_20260513T080728/median/paper.pdf
artifacts/dream_reports/dream_20260513T080728/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50f9210e-942b-4b06-af1b-24ae93c54012",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "7ca712d6-9641-4f8b-b8ed-3fe36205d97c",
  "sourceToolAssistantUUID": "50f9210e-942b-4b06-af1b-24ae93c54012",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-13T08:48:39.711Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0147kzNpAcAE5uZPVYgFtbRu`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "ARCHITECTURE.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ca712d6-9641-4f8b-b8ed-3fe36205d97c",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH8rXb3owQ7Gjn4BDgR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e9d1cd2-56b4-4245-96c7-2b74d8b65711",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WAeSNHE5fhoYkvastUzV6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11366,
      "cache_read_input_tokens": 18515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11366,
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

_source line 27 · 2026-05-13T08:48:39.722Z_

<details><summary>↩ Tool result · `toolu_0147kzNpAcAE5uZPVYgFtbRu`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ARCHITECTURE.md found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e9d1cd2-56b4-4245-96c7-2b74d8b65711",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "652fc2a8-c4f9-45bf-b6ad-568d90aee21a",
  "sourceToolAssistantUUID": "7e9d1cd2-56b4-4245-96c7-2b74d8b65711",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-13T08:48:40.255Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AJENXyenVYFJ3ZDyrZsAbq`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "652fc2a8-c4f9-45bf-b6ad-568d90aee21a",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH8rXb3owQ7Gjn4BDgR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27a3e355-cb6c-4ba2-9d21-5ea87578f749",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WAeSNHE5fhoYkvastUzV6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11366,
      "cache_read_input_tokens": 18515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11366,
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

_source line 29 · 2026-05-13T08:48:40.269Z_

<details><summary>↩ Tool result · `toolu_01AJENXyenVYFJ3ZDyrZsAbq`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27a3e355-cb6c-4ba2-9d21-5ea87578f749",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "d2d29b18-c2c7-4543-8d31-7230e7a1c177",
  "sourceToolAssistantUUID": "27a3e355-cb6c-4ba2-9d21-5ea87578f749",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-13T08:48:44.246Z_

Let me read the latest dream report paper (the best version) to get the full paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2d29b18-c2c7-4543-8d31-7230e7a1c177",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH9GFr8tsMxwCoXEq9A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e70aed5b-16ef-4855-afb5-f4b7237ece13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2orA38PWBuVpfspH5FpAP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 922,
      "cache_read_input_tokens": 29881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 922,
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

_source line 31 · 2026-05-13T08:48:45.127Z_

<details open><summary>🔧 Tool call — Read · `toolu_016ScsNvHMiJrsS1zXhX8Qx1`</summary>

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
  "parentUuid": "e70aed5b-16ef-4855-afb5-f4b7237ece13",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH9GFr8tsMxwCoXEq9A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d18d144-380e-4949-b436-e8035a13bcec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2orA38PWBuVpfspH5FpAP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 922,
      "cache_read_input_tokens": 29881,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 922
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 29881,
          "cache_creation_input_tokens": 922,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 922,
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

_source line 32 · 2026-05-13T08:48:45.793Z_

<details><summary>↩ Tool result · `toolu_016ScsNvHMiJrsS1zXhX8Qx1`</summary>

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
  "parentUuid": "4d18d144-380e-4949-b436-e8035a13bcec",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "c2db9f30-6fb4-4927-a54f-1a2ba1679c55",
  "sourceToolAssistantUUID": "4d18d144-380e-4949-b436-e8035a13bcec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-13T08:48:51.806Z_

Now let me also look at the earlier dream report for comparison, and check for any additional experimental details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2db9f30-6fb4-4927-a54f-1a2ba1679c55",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH9fmDQpZZS7JKDox4B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e37ff0bb-b4e0-4c2d-8d8e-9ee3370e159b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011vN8VqUS3FAmS6Q6PtYeYc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11012,
      "cache_read_input_tokens": 30803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11012,
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

_source line 34 · 2026-05-13T08:48:52.892Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LHRWbdzw4q3PGzQa2sToxP`</summary>

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
  "parentUuid": "e37ff0bb-b4e0-4c2d-8d8e-9ee3370e159b",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH9fmDQpZZS7JKDox4B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f849151-2de3-4eae-823a-e3e923489681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011vN8VqUS3FAmS6Q6PtYeYc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11012,
      "cache_read_input_tokens": 30803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11012,
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

_source line 35 · 2026-05-13T08:48:52.908Z_

<details><summary>↩ Tool result · `toolu_01LHRWbdzw4q3PGzQa2sToxP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/decisions.yaml\", \"content\": \"_next_id: 14\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 10:58 UTC\\n  summary: MVP 方案：Qwen2.5-1.8B + C4 5K docs 做 pilot saturation study，验证代际深度可分辨性\\n  rationale: Phase 0 pilot saturation study 是天然的 MVP gate——如果不同代际深度的文本在特征空间上不可区分，整个项目没有意义。选\\n    Qwen2.5-1.8B 因为体积小、开源、生成速度快。5K docs 足够统计显著性但不浪费 GPU。Pass 标准 K*≥3 对应至少 4 个有意义的类别（human/gen1/gen2/gen3+），AUC>0.70\\n    确保特征有实质区分力。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 15:10 UTC\\n  summary: MVP 初步结果 K*=2（边界），修复 right-padding 后重跑确认再锁路线\\n  rationale: AUC(2v3)=0.5797 距阈值 0.60 仅差 0.02，right-padding bug 可能系统性压低 K*。修复成本（1行代码+3h\\n    GPU）远低于错选路线的代价。\\n  related_experiments:\\n  - exp_id: mvp_pilot_sat_v1\\n    role: primary\\n    result: K*=2 (borderline), AUC(0v1)=0.9952, AUC(1v2)=0.6712, AUC(2v3)=0.5797\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-12 19:27 UTC\\n  summary: MVP Conditional Pass, K*=2, 锁定 Route B (Saturation Characterization), 进入\\n    research 阶段\\n  rationale: v3 definitive run 确认 K*=2：AUC(0v1)=0.9956, AUC(1v2)=0.6957, AUC(2v3)=0.5893(<0.60)。JSD\\n    严格单调递减支持 DPI 理论。Depth signal 存在但饱和在 depth 2-3。Route B 将 K* 本身定位为首次测量的基本科学量，比 Route\\n    A（depth classifier 可行性）更 robust——不依赖阈值选择。3-class 系统（human/gen-1/gen-2+）仍比 binary\\n    更有信息量。\\n  related_experiments:\\n  - exp_id: mvp_pilot_sat_v1\\n    role: primary\\n    result: K*=2, AUC(0v1)=0.9956, AUC(1v2)=0.6957, AUC(2v3)=0.5893, JSD monotonic\\n      decay\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 20:08 UTC\\n  summary: Reviewer 审查后修正：C1 区分 K*_empirical vs K*_theory；exp-013 (cross-model transfer)\\n    从 P1 提升至 P0\\n  rationale: Reviewer 指出 C1 混淆了经验值和理论值——实测 K*=2 是特定特征+分类器下的 practical boundary，不等于信息论\\n    impossibility boundary。更好的特征/分类器可能推高 K*。修正为\\\"K*_empirical 是 K*_theory 的保守下界\\\"。exp-013\\n    (cross-model transfer, 仅 2h) 直接回答审稿人最危险的攻击面：depth signal 是文本固有属性还是 model self-familiarity？Transfer\\n    失败则 C1 需根本调整。性价比极高，必须 P0。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 00:23 UTC\\n  summary: Dream 分析完成：proceed with P0, 整合 8 项确认行动到 framing/plan\\n  rationale: Dream 三档评分 Best=Weak Accept / Median=Borderline / Worst=Weak Reject。跨三档一致的结构性问题（通用建议）已整合：(1)\\n    IT/fundamental framing 已在 D004 校正，进一步软化 \\\"universal\\\" 措辞; (2) related work 扩展到 4\\n    方向; (3) exp-006 加 DSIR baseline + α ablation + 5 seeds; (4) exp-007 加 bootstrap\\n    CI + permutation-test; (5) exp-015 从 P2 升 P1; (6) 3-class accuracy 显式报告。6 项观察项待真实实验验证：Drayson\\n    et al. 存在性待查、cross-model transfer framing、domain sensitivity、method-code consistency、learned\\n    probe strength、cross-scale probe power。无需 re-dream——确认行动项均为增量调整，不改变 framing 结构。\\n  related_experiments:\\n  - exp_id: exp-006\\n    role: updated\\n    result: 加 DSIR baseline + α ablation + 5 seeds, GPU 48h→72h\\n  - exp_id: exp-007\\n    role: updated\\n    result: 加 bootstrap CI + permutation-test, GPU 1h→2h\\n  - exp_id: exp-015\\n    role: promoted\\n    result: P2→P1\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 00:58 UTC\\n  summary: '回滚 Drayson et al. 引用清理——Reviewer 确认为真实论文 (EMNLP 2025 #1506)'\\n  rationale: D005 中基于 web search 无结果将 Drayson et al. (2025) 判定为 Dream 幻觉引用并指示 Agent\\n    清理。Reviewer 独立核实找到 arXiv:2502.15654 + UCL Discovery PDF + GitHub repo，确认为真实发表论文。这是我们最相关的\\n    prior work（binary filtering 防 collapse），我们的 ordinal depth estimation 是其自然推广。教训：单次\\n    web search 不足以判定引用为幻觉，应交叉验证（arXiv ID + 作者机构 + 会议 proceedings）。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-13 02:06 UTC\\n  summary: Drayson novelty 评估完成：核心 novelty 安全，Story Spine 微调，exp-006 加公平 binary baseline\\n  rationale: Reviewer 独立评估确认：(1) Drayson 做 binary detection 防 collapse（宏观训练动态），我们做\\n    ordinal depth estimation + K* measurement（单样本深度估计）——问题定义层面的扩展，非渐进改进；(2) Drayson\\n    100 代是训练迭代不是文本递归深度，不构成 novelty 威胁；(3) Story Spine 加入 Drayson 作为 closest prior\\n    work 但保持 gap statement 完整；(4) exp-006 加 binary-ours baseline（同 15D 特征做 binary，唯一变量\\n    = binary/ordinal），确保 C3 对比公平。\\n  related_experiments:\\n  - exp_id: exp-006\\n    role: updated\\n    result: 加 binary-ours 公平对比 baseline\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-13 02:45 UTC\\n  summary: C2 claim 暂停写入论文——等 exp-017 解耦 generation mode 因素后决定措辞\\n  rationale: exp-005 结果显示 Kendall τ 仅 Pythia-OLMo 达 0.8476（≥0.8），Pythia-Qwen 0.5238、OLMo-Qwen\\n    0.4857 均不达标。1/3 通过率不支持 C2 当前 \\\"τ≥0.8 across all tested families\\\" 的表述。关键混杂因素：Pythia/OLMo\\n    用 continuation 模式，Qwen 用 rewrite 模式。exp-017（Qwen continuation，~4h 后完成）将区分是 mode-dependent\\n    还是 model-dependent。若 Qwen continuation τ≥0.8 → C2 限定为 \\\"consistent within continuation\\n    mode\\\"；若仍低 → C2 大幅弱化为 \\\"partially consistent\\\" 或限定 base model 范围。\\n  related_experiments:\\n  - exp_id: exp-005\\n    role: evidence\\n    result: partial_consistency_1of3_pairs\\n  - exp_id: exp-017\\n    role: pending_resolution\\n    result: running\\n  depends_on: []\\n- id: D009\\n  date: 2026-05-13 03:35 UTC\\n  summary: C2 战略评估：C1 是承重墙，C3 是安全网，C2 是加分项；exp-016 列为场景 B 应急\\n  rationale: 'Reviewer 深度评估指出第三混杂因素：instruct-tuning。Qwen-Instruct vs Pythia/OLMo base\\n    的差异不仅是 generation mode。exp-017 无法完全解耦 mode 和 instruct-tuning 的联合效应。场景 A (τ≥0.8):\\n    C2 改为 mode-dependent insight (7/10)，可撑 EMNLP Main。场景 B (τ<0.7): C2 降级为 supplementary\\n    finding (3/10)，C1+C3 仍可投 Main/Findings，取决于 C3 效果大小。exp-006 (graduated filtering)\\n    优先级应提升作为 C2 弱化的安全网。exp-016 (Qwen base continuation) 作为场景 B 应急实验预备——可解耦 instruct-tuning\\n    vs architecture 效应，仅 6h GPU。'\\n  related_experiments:\\n  - exp_id: exp-005\\n    role: evidence\\n    result: partial_consistency\\n  - exp_id: exp-017\\n    role: pending_resolution\\n    result: running\\n  - exp_id: exp-006\\n    role: priority_elevated\\n    result: planned\\n  - exp_id: exp-016\\n    role: contingency_scenario_B\\n    result: planned\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-13 06:20 UTC\\n  summary: C2 Plan A 否决 → 执行 Plan B：degradation ordering 限定为 \\\"within architecture\\n    family\\\"，降级为 supplementary finding\\n  rationale: exp-017 (Qwen continuation) 结果明确：控制 generation mode 后，Qwen top feature\\n    仍是 freq_entropy（vs Pythia/OLMo 的 surp_d1_mean）。分歧是 model-dependent 而非 mode-dependent。按\\n    D009 预案，C2 降级为 supplementary finding，措辞改为 \\\"feature degradation ordering consistent\\n    within architecture family (base models τ=0.85), but diverges across architecture\\n    types\\\"。同时发现 generation mode effect 很大（rewrite→continuation AUC 1v2 下降 0.084），论文需增加\\n    mode effect 讨论段。C1 不受影响（4/4 条件 K*=2）。C3 重要性提升为论文第二支柱。\\n  related_experiments:\\n  - exp_id: exp-017\\n    role: decisive_evidence\\n    result: plan_a_rejected\\n  - exp_id: exp-005\\n    role: initial_evidence\\n    result: partial_consistency\\n  depends_on:\\n  - D008\\n  - D009\\n- id: D011\\n  date: 2026-05-13 06:24 UTC\\n  summary: D010 修正：C2 从 \\\"supplementary\\\" 升级为 \\\"qualified claim\\\"——使用 single-feature AUC\\n    + Spearman ρ≥0.85 + mode-controlled 条件\\n  rationale: 'Reviewer 4-model 降解分析修正了此前结论。LightGBM split count 和 single-feature AUC\\n    给出矛盾排名：split count 显示 Qwen-cont freq_entropy #1（与 Pythia/OLMo 分歧），但 single-feature\\n    AUC 显示 Qwen-cont top-3 与 Pythia/OLMo 完全一致（surp_d1_std, surp_std, surp_d2_std）。Single-feature\\n    AUC 更直接衡量代际区分力，更适合 C2 语义。Spearman ρ: Pythia-OLMo=0.95, Pythia-Qwen_cont=0.9143,\\n    OLMo-Qwen_cont=0.85——全部≥0.85。C2 可行路径：(1) 用 single-feature AUC ranking 定义 ordering；(2)\\n    用 Spearman ρ≥0.85 作为一致性阈值；(3) 限定 mode-controlled 条件；(4) 透明报告 depth-pair level\\n    差异（1v2 对 τ 仅 0.35-0.39）和 τ vs ρ 选择理由。风险：depth-pair 1v2 一致性差（τ~0.37），审稿人可能做 depth-stratified\\n    分析。'\\n  related_experiments:\\n  - exp_id: exp-005\\n    role: 4model_reanalysis\\n    result: rho_ge_0.85_all_pairs\\n  - exp_id: exp-017\\n    role: mode_control\\n    result: convergence_confirmed\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-13 07:29 UTC\\n  summary: 论文 claim 重构：4 claims → 2+1 结构（C1' K* characterization + C3 graduated filtering\\n    + supporting analysis）\\n  rationale: Reviewer 评估指出 4 claims (C1/C2/C3/C4) 对 EMNLP Main 太散，每个不够厚。重构为：Primary\\n    C1' = 首次系统测量 K*_empirical（含 DPI 理论 + 4-model 验证 + cross-model transfer + degradation\\n    ordering + generation mode analysis）；Secondary C3 = graduated filtering > binary；Supporting\\n    = generation mode effect + metric analysis 作为 §4.4 subsection。C4 从独立 claim 降级为方法论洞见（Canonical\\n    Condition Selection），C2 ordering 融入 C1' characterization。Canonical condition framing：continuation\\n    mode 作为 cross-model 基础，MVP rewrite 定位为 pilot study。exp-006 是关键路径：exp-003 完成后立即启动，72h\\n    GPU，deadline 05-25 ARR 倒推无延迟容忍。\\n  related_experiments:\\n  - exp_id: exp-013\\n    role: evidence_for_restructure\\n    result: mode_effect_is_methodological\\n  - exp_id: exp-006\\n    role: critical_path\\n    result: planned\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-13 07:37 UTC\\n  summary: C3 exp-006 单点依赖风险评估 + fallback story 预案\\n  rationale: Reviewer 正确指出 C3 (graduated filtering) 完全依赖 exp-006 单个实验。Fallback 预案：(1)\\n    如果 graduated 显著优于 binary → C3 成立，2+1 claim 结构完整；(2) 如果 graduated ≈ binary（无统计显著差异）→\\n    C3 改为 informative negative：\\\"K*=2 的粗粒度 ordinal signal 不足以在 downstream 层面超越 binary\\\"，论文\\n    story 调整为纯 characterization paper（C1' 独立支撑），graduated filtering 作为 negative result\\n    讨论（对论文质量有加分，EMNLP 重视 negative findings）；(3) 如果 graduated 比 binary 差 → 同场景 2，额外分析原因（3-class\\n    ordinal noise vs binary robustness）。场景 1 是预期结果（K* 附近 ordinal signal 提供更 calibrated\\n    的质量估计），但场景 2 也不致命——C1' 本身有足够深度（K* characterization + degradation ordering + mode\\n    effect + cross-model transfer）。关键行动：exp-003 完成后 GPU 零间隔切换 exp-006，不容任何空转。\\n  related_experiments:\\n  - exp_id: exp-006\\n    role: target\\n    result: planned\\n  - exp_id: exp-003\\n    role: predecessor\\n    result: running\\n  depends_on:\\n  - D012\\n\", \"total_chars\": 9371, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f849151-2de3-4eae-823a-e3e923489681",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "81349671-5df3-40a1-990b-eee09ba5b6c9",
  "sourceToolAssistantUUID": "4f849151-2de3-4eae-823a-e3e923489681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-13T08:48:54.121Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01M7jbLRtGaEbLSjhqWmxfQZ`</summary>

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
  "parentUuid": "81349671-5df3-40a1-990b-eee09ba5b6c9",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH9fmDQpZZS7JKDox4B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29a4deec-1377-4d5b-b102-d7d5a9dd969e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011vN8VqUS3FAmS6Q6PtYeYc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11012,
      "cache_read_input_tokens": 30803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11012,
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

_source line 37 · 2026-05-13T08:48:54.138Z_

<details><summary>↩ Tool result · `toolu_01M7jbLRtGaEbLSjhqWmxfQZ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29a4deec-1377-4d5b-b102-d7d5a9dd969e",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "bf448682-f73c-465b-8073-3973ee151159",
  "sourceToolAssistantUUID": "29a4deec-1377-4d5b-b102-d7d5a9dd969e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-13T08:48:54.444Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019UaqKMWfD59Kd8wpJW6gCf`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf448682-f73c-465b-8073-3973ee151159",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazH9fmDQpZZS7JKDox4B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9264a75-8e73-45bc-b537-9bbc82fb2680",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011vN8VqUS3FAmS6Q6PtYeYc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11012,
      "cache_read_input_tokens": 30803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11012,
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

_source line 39 · 2026-05-13T08:48:54.453Z_

<details><summary>↩ Tool result · `toolu_019UaqKMWfD59Kd8wpJW6gCf`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9264a75-8e73-45bc-b537-9bbc82fb2680",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "b0866d4f-6a48-432e-99e3-a0d713df28e2",
  "sourceToolAssistantUUID": "c9264a75-8e73-45bc-b537-9bbc82fb2680",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-13T08:49:00.857Z_

Now let me also read the earlier dream report to check what reviewers previously flagged.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0866d4f-6a48-432e-99e3-a0d713df28e2",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazHAKP97TeLsbW3tcoFG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a832d90e-0e23-4863-9bfe-e5903d23f080",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0143GsPjFmYzqkaoHp27EnXV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5691,
      "cache_read_input_tokens": 41815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5691,
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

_source line 41 · 2026-05-13T08:49:03.478Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ts7GVFQ2kMZvV8sWKxYgu4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a832d90e-0e23-4863-9bfe-e5903d23f080",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazHAKP97TeLsbW3tcoFG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f0ca056-8683-4fda-b9f4-8a6022a030df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0143GsPjFmYzqkaoHp27EnXV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5691,
      "cache_read_input_tokens": 41815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5691,
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

_source line 42 · 2026-05-13T08:49:03.483Z_

<details><summary>↩ Tool result · `toolu_01Ts7GVFQ2kMZvV8sWKxYgu4`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{amsmath,amssymb,amsfonts}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{graphicx}
9	\usepackage{natbib}
10	\usepackage{hyperref}
11	\usepackage[margin=2.5cm]{geometry}
12	\usepackage{xcolor}
13	\usepackage{enumitem}
14	
15	\hypersetup{colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue}
16	
17	\title{$K^*$: Measuring the Generational Discrimination Boundary\\in Recursive Synthetic Text}
18	
19	\author{
20	  Anonymous Authors\\
21	  \textit{Under Review at EMNLP 2026}
22	}
23	
24	\date{}
25	
26	\begin{document}
27	\maketitle
28	
29	% ============================================================
30	\begin{abstract}
31	Web-scale corpora are increasingly contaminated by multi-generational synthetic text, yet existing detection methods treat synthetic content as a binary category, ignoring the non-linear quality degradation across recursive generations. We formalize recursive text generation as an iterated lossy channel and derive, via the Data Processing Inequality, the existence of a \emph{saturation boundary} $K^*$---the generational depth beyond which pairwise discrimination becomes statistically indistinguishable from chance. Through controlled experiments across three model families (Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B) and a 7B cross-scale probe, we establish $K^*{=}2$ at the 1--1.5B scale under standard decoding, rising to $K^*{=}3$ under high-temperature decoding ($T{=}1.2$) or at the 7B scale. We reveal a universal degradation ordering: vocabulary diversity collapses before distributional dynamics (Kendall $\tau{=}0.84$ across model pairs). Finally, we show that even a coarse 3-class depth signal (human / gen-1 / gen-2+) yields 2.2 and 2.1 percentage-point improvements over binary filtering on MMLU and HellaSwag respectively ($p{<}0.05$), with the advantage monotonically increasing with contamination severity. Our results establish $K^*$ as a fundamental, modulable quantity that provides actionable guidance for depth-aware data curation.
32	\end{abstract}
33	
34	% ============================================================
35	\section{Introduction}
36	\label{sec:intro}
37	
38	The proliferation of large language models (LLMs) has led to an accelerating feedback loop: models generate text that enters web corpora, which in turn train future models \citep{shumailov2024model}. This recursive contamination is not merely a binary phenomenon---first-generation synthetic text retains most of the distributional properties of its human seed, while fourth-generation text may exhibit severe distributional collapse. Yet the dominant paradigm in synthetic text detection treats all machine-generated content identically, drawing a single boundary between ``human'' and ``synthetic'' \citep{mitchell2023detectgpt,hans2024binoculars}.
39	
40	This binary framing is fundamentally inadequate for data curation. A data curator who indiscriminately removes all synthetic-flagged content discards high-quality first-generation text alongside severely degraded later generations. Conversely, retaining all content below a lenient threshold admits deeply recursive text whose distributional pathologies can propagate into downstream models.
41	
42	We propose a shift from binary detection to \emph{generational depth estimation}: given a text, estimate how many rounds of recursive generation it has undergone. This reframing raises a natural question: \textit{how deep can we see?} The Data Processing Inequality (DPI) guarantees that mutual information between the original human text and its $k$-th generation descendant decreases monotonically. At some depth, the signal must vanish. We call this depth the \emph{saturation boundary} $K^*$ and argue it is a fundamental information-theoretic quantity, not merely a classifier performance ceiling.
43	
44	Our contributions are threefold:
45	
46	\begin{enumerate}[leftmargin=*,itemsep=2pt]
47	    \item \textbf{Saturation Boundary ($K^*$).} We provide the first systematic measurement of $K^*$ across model families and decoding strategies. We establish $K^*{=}2$ for 1--1.5B-scale models under standard nucleus sampling, and demonstrate that $K^*$ is modulable: it rises to 3 under high-temperature decoding or at the 7B scale.
48	
49	    \item \textbf{Degradation Ordering.} We show that linguistic features collapse in a consistent order across model families: vocabulary diversity saturates at depth 1, while surprisal dynamics persist to depth 2 (mean Kendall $\tau{=}0.84$). This ordering reflects information-theoretic structure, not model-specific artifacts.
50	
51	    \item \textbf{Graduated Filtering.} We demonstrate that a 3-class ordinal depth signal (human / gen-1 / gen-2+) yields statistically significant improvements over binary filtering: $+2.24$ pp on MMLU and $+2.07$ pp on HellaSwag ($p{<}0.05$), with the advantage growing monotonically with contamination rate.
52	\end{enumerate}
53	
54	% ============================================================
55	\section{Related Work}
56	\label{sec:related}
57	
58	\paragraph{Synthetic text detection.}
59	Binary detection methods range from watermarking \citep{kirchenbauer2023watermark} to statistical tests on token likelihood \citep{mitchell2023detectgpt,hans2024binoculars}. DivEye \citep{tulchinskii2024diveye} uses intrinsic dimensionality; Min-K\%++ \citep{zhang2024minkpp} uses minimum-probability tokens. All produce a scalar confidence score optimized for a binary decision boundary. We show (Section~\ref{sec:binary_baseline}) that these scores correlate weakly with generational depth (Spearman $\rho \leq 0.23$), confirming that binary detection and depth estimation are distinct problems.
60	
61	\paragraph{Model collapse.}
62	\citet{shumailov2024model} characterize the macroscopic phenomenon of iterative retraining on synthetic data, showing progressive loss of distributional tails. \citet{dohmatob2024model} provide theoretical bounds on convergence rates. Our work complements this line by providing \emph{detection} tools: rather than studying what happens when models are retrained on their own output, we ask whether the depth of recursive generation can be estimated from text alone.
63	
64	\paragraph{Data quality estimation.}
65	Verification-based methods use external models to assess factual consistency \citep{feng2024factuality} or apply quality classifiers as binary gates \citep{wettig2024qurating}. These approaches do not estimate recursive depth. Our graduated filtering framework subsumes binary quality gates as a special case ($K^*{=}1$).
66	
67	% ============================================================
68	\section{Method}
69	\label{sec:method}
70	
71	\subsection{Recursive Generation as an Iterated Lossy Channel}
72	\label{sec:theory}
73	
74	Let $X_0$ denote human-written text drawn from distribution $P_0$. A language model $\mathcal{M}$ with decoding strategy $\mathcal{D}$ defines a stochastic channel $\mathcal{C}_{\mathcal{M},\mathcal{D}}: P_k \mapsto P_{k+1}$, where $P_k$ is the distribution of generation-$k$ text. The Data Processing Inequality guarantees:
75	\begin{equation}
76	I(X_0; X_{k+1}) \leq I(X_0; X_k) \quad \forall k \geq 0
77	\label{eq:dpi}
78	\end{equation}
79	where $I(\cdot;\cdot)$ denotes mutual information. Since the channel is lossy (non-invertible), the inequality is strict, and the sequence $\{I(X_0; X_k)\}_{k=0}^{\infty}$ converges monotonically to a limit that depends on the fixed-point structure of $\mathcal{C}$.
80	
81	We define the \emph{saturation boundary} $K^*$ as:
82	\begin{equation}
83	K^* = \max\{k : \text{AUC}(P_{k-1}, P_k) \geq \theta\}
84	\label{eq:kstar}
85	\end{equation}
86	where $\text{AUC}(P_{k-1}, P_k)$ is the area under the ROC curve for pairwise discrimination between adjacent generations using a fixed feature set, and $\theta$ is a discrimination threshold (we use $\theta{=}0.60$ throughout). $K^*$ quantifies the depth at which adjacent generations become statistically indistinguishable.
87	
88	\paragraph{$K^*$ is an information-theoretic quantity.}
89	While the operational definition of $K^*$ depends on the feature set and threshold $\theta$, we argue that it reflects an underlying information-theoretic boundary. The monotonic decay of Jensen--Shannon divergence (JSD) between adjacent generations (e.g., $0.243 \to 0.014 \to 0.005 \to 0.003 \to 0.002$ for Pythia-1.4B) mirrors the DPI-mandated decay of mutual information. The sharp drop between generations 0--1 and 1--2 (a 17$\times$ reduction in JSD) followed by a slow asymptotic approach to zero is the empirical signature of an information bottleneck.
90	
91	\subsection{Feature Design}
92	\label{sec:features}
93	
94	We extract a 15-dimensional feature vector from each text, organized into three groups designed to capture complementary aspects of distributional degradation:
95	
96	\paragraph{Vocabulary diversity (5 features).}
97	Type-token ratio, hapax legomena ratio, Yule's $K$, entropy of the unigram distribution, and Simpson's diversity index. These capture the narrowing of the lexical distribution that accompanies recursive generation.
98	
99	\paragraph{Surprisal dynamics (5 features).}
100	Mean surprisal, surprisal variance, lag-1 autocorrelation of surprisal, auto-mutual information of the surprisal sequence, and mean pointwise mutual information of bigrams. These capture higher-order distributional structure that persists beyond lexical collapse.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f0ca056-8683-4fda-b9f4-8a6022a030df",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "627362b5-141e-473e-bb01-555d6e7172a7",
  "sourceToolAssistantUUID": "4f0ca056-8683-4fda-b9f4-8a6022a030df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-13T08:49:04.007Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018Tp7p8gBdNUZ5WrShJmxMC`</summary>

```json
{
  "pattern": "**/dream_*/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "627362b5-141e-473e-bb01-555d6e7172a7",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazHAKP97TeLsbW3tcoFG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "998462ef-fd2d-45d6-a76b-267df5a8c6f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0143GsPjFmYzqkaoHp27EnXV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5691,
      "cache_read_input_tokens": 41815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5691,
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

_source line 44 · 2026-05-13T08:49:04.029Z_

<details><summary>↩ Tool result · `toolu_018Tp7p8gBdNUZ5WrShJmxMC`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "998462ef-fd2d-45d6-a76b-267df5a8c6f7",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "2ce5d776-1ffd-4422-bf9d-f745f24fd769",
  "sourceToolAssistantUUID": "998462ef-fd2d-45d6-a76b-267df5a8c6f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-13T08:49:06.883Z_

Now let me check the dream review reports themselves.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ce5d776-1ffd-4422-bf9d-f745f24fd769",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazHB2CowW5XC4ZZ6bJEJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2f8069c-efd1-4e1f-96eb-69d0f650d479",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016y6oW7shFXH8gzUd4eXTGc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3043,
      "cache_read_input_tokens": 47506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3043,
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

_source line 46 · 2026-05-13T08:49:07.514Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Y6vBnjCeUBtHUpXmneenMm`</summary>

```json
{
  "pattern": "**/dream_*/**/*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2f8069c-efd1-4e1f-96eb-69d0f650d479",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazHB2CowW5XC4ZZ6bJEJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1589faf4-7aed-4bb2-ae82-dd430161606e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016y6oW7shFXH8gzUd4eXTGc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3043,
      "cache_read_input_tokens": 47506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3043,
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

_source line 47 · 2026-05-13T08:49:07.526Z_

<details><summary>↩ Tool result · `toolu_01Y6vBnjCeUBtHUpXmneenMm`</summary>

```text
artifacts/dream_reports/dream_20260512T200328/best/experiment_data.json
artifacts/dream_reports/dream_20260512T200328/median/experiment_data.json
artifacts/dream_reports/dream_20260512T200328/worst/experiment_data.json
artifacts/dream_reports/dream_20260513T080728/best/experiment_data.json
artifacts/dream_reports/dream_20260513T080728/median/experiment_data.json
artifacts/dream_reports/dream_20260513T080728/worst/experiment_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1589faf4-7aed-4bb2-ae82-dd430161606e",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "794d3e99-e7fb-46a1-a0a3-4c6c1d16d81f",
  "sourceToolAssistantUUID": "1589faf4-7aed-4bb2-ae82-dd430161606e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-13T08:49:07.818Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TEzAS7CU6mFN18h1X9W2wF`</summary>

```json
{
  "pattern": "**/dream_*/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "794d3e99-e7fb-46a1-a0a3-4c6c1d16d81f",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazHB2CowW5XC4ZZ6bJEJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "afdbe214-8173-4b9c-a91e-c531baaca5ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016y6oW7shFXH8gzUd4eXTGc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3043,
      "cache_read_input_tokens": 47506,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3043
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 47506,
          "cache_creation_input_tokens": 3043,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3043,
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

_source line 49 · 2026-05-13T08:49:07.833Z_

<details><summary>↩ Tool result · `toolu_01TEzAS7CU6mFN18h1X9W2wF`</summary>

```text
artifacts/dream_reports/dream_20260512T200328/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T200328/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T200328/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T200328/meta.yaml
artifacts/dream_reports/dream_20260513T080728/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T080728/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T080728/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T080728/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afdbe214-8173-4b9c-a91e-c531baaca5ea",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "8c226a9d-c595-4cdf-8d2d-3ecbbd64935a",
  "sourceToolAssistantUUID": "afdbe214-8173-4b9c-a91e-c531baaca5ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-13T08:49:10.800Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TRVNAj7NrpRCLLyMW4zDTK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c226a9d-c595-4cdf-8d2d-3ecbbd64935a",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazHBJ9FzaESAMFUNT3qw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fea37bf7-7479-40fe-a76f-6b78d70ef748",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VE1s1ZLkbyDNsSE5hMFxCA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 587,
      "cache_read_input_tokens": 50549,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 587
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 50549,
          "cache_creation_input_tokens": 587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 587,
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

_source line 51 · 2026-05-13T08:49:11.085Z_

<details><summary>↩ Tool result · `toolu_01TRVNAj7NrpRCLLyMW4zDTK`</summary>

```text
1	narrative_guidance: 'C1'' 全面成立 + C3 downstream 收益显著。exp-003 解码消融建立 K* 可调控梯度（greedy
2	  K*=1 → standard K*=2 → high-temp K*=3）， 直接消解 "K*=2 太浅" 审稿人顾虑。exp-004 7B 确认 scale
3	  → K* 因果链（K*≥3），与 exp-003 形成两条独立路径推高 K*。 exp-006 graduated filtering 在 MMLU/HellaSwag
4	  上均显著优于 binary（Δ≥2pp, p<0.01），exp-009 dose-response 单调递增。 exp-015 15D hand-crafted
5	  features 与 frozen embeddings 差距 <1.5pp，支撑 interpretable features 叙事。 Qwen-cont 的
6	  0.0015 margin 脆弱性被 exp-003 新 configs 的一致 K*=2 所补偿——多条件汇聚证据远强于单点 CI。 所有完成实验的实际数据与
7	  best 档预测高度一致，原始 2+1 claim 结构可直接支撑 EMNLP 2026 Main，reviewer score 预期 3.5-4.0。
8	
9	  '
10	imagined_experiments:
11	- name: Qwen2.5-1.5B 解码策略消融
12	  plan_id: exp-003
13	  description: 'Qwen2.5-1.5B-Instruct continuation mode, C4 5K docs, depth 0-5, 4
14	    解码配置: greedy / nucleus p=0.9 T=1.0 / nucleus p=0.95 T=0.7 / nucleus p=0.95 T=1.2。
15	    Baseline 为 exp-017 (nucleus p=0.95, T=1.0, continuation): 1v2 AUC=0.6114, K*=2。
16	
17	    '
18	  expected_results:
19	    greedy:
20	      k_star: 1
21	      pairwise_auc:
22	        0v1: 0.9965
23	        1v2: 0.5862
24	        2v3: 0.5481
25	        3v4: 0.5225
26	        4v5: 0.5108
27	      pairwise_jsd:
28	        0v1: 0.2753
29	        1v2: 0.0038
30	        2v3: 0.0029
31	        3v4: 0.0022
32	        4v5: 0.0019
33	      ordinal_accuracy: 0.3412
34	    nucleus_p0.9_T1.0:
35	      k_star: 2
36	      pairwise_auc:
37	        0v1: 0.9968
38	        1v2: 0.6278
39	        2v3: 0.5582
40	        3v4: 0.5312
41	        4v5: 0.5124
42	      pairwise_jsd:
43	        0v1: 0.2814
44	        1v2: 0.0057
45	        2v3: 0.0035
46	        3v4: 0.0028
47	        4v5: 0.0024
48	      ordinal_accuracy: 0.3685
49	    T0.7_p0.95:
50	      k_star: 2
51	      pairwise_auc:
52	        0v1: 0.9963
53	        1v2: 0.6241
54	        2v3: 0.5558
55	        3v4: 0.5286
56	        4v5: 0.5115
57	      pairwise_jsd:
58	        0v1: 0.2685
59	        1v2: 0.0052
60	        2v3: 0.0033
61	        3v4: 0.0026
62	        4v5: 0.0022
63	      ordinal_accuracy: 0.3648
64	    T1.2_p0.95:
65	      k_star: 3
66	      pairwise_auc:
67	        0v1: 0.9981
68	        1v2: 0.6823
69	        2v3: 0.6218
70	        3v4: 0.5614
71	        4v5: 0.5305
72	      pairwise_jsd:
73	        0v1: 0.3082
74	        1v2: 0.0118
75	        2v3: 0.0056
76	        3v4: 0.0035
77	        4v5: 0.0027
78	      ordinal_accuracy: 0.3975
79	    cross_config_spearman_rho_feature_ordering:
80	      greedy_vs_baseline: 0.886
81	      p0.9_vs_baseline: 0.921
82	      T0.7_vs_baseline: 0.914
83	      T1.2_vs_baseline: 0.878
84	    k_star_summary: K*=2 in 3/4 configs (p=0.9, T=0.7, T=1.2≥2); K*=1 for greedy;
85	      K*=3 for T=1.2
86	  result_rationale: '解码策略通过控制 token 采样的有效熵，直接调控递归信道的信息保持率。 Greedy 解码（argmax）将输出钉死在条件分布的
87	    mode 上：gen-1 已高度确定性，gen-2 对 gen-1 施加相同的 argmax 压缩后几乎无新增信息损失可测—— 因此 1v2 AUC=0.586
88	    低于 θ=0.60 阈值，K*=1。这不是检测失败，而是 greedy 信道本身在首代就完成了绝大部分信息丢弃。 p=0.9（vs baseline p=0.95）仅移除尾部
89	    5% 概率质量的差异，效应量小——1v2 AUC 从 0.611 降到 0.628，仍稳定在 K*=2。 T=0.7 压缩 softmax 温度使分布更 peaked，效应与收窄
90	    nucleus 类似，1v2=0.624 保持 K*=2。 T=1.2 是关键条件：高温度展平分布→每代输出保留更多"非主流" token 选择→这些 tail
91	    tokens 携带的分布结构需要更多代际才能被递归"洗掉"。 信息论机制：T=1.2 抬高了初始互信息 I(X;Y₁)，DPI 保证 I(X;Yₖ) 单调递减，但更高起点意味着
92	    2v3 AUC=0.622 仍高于 0.60→K*=3。 Feature ordering 一致性（ρ≥0.878）表明解码策略改变信号强度但不改变哪些特征最先饱和——退化顺序是信息论结构性规律。
93	
94	    '
95	  tables:
96	  - caption: '解码策略消融: K* 与关键 pairwise AUC'
97	    columns:
98	    - decoding_config
99	    - K*
100	    - AUC_0v1
101	    - AUC_1v2
102	    - AUC_2v3
103	    - AUC_3v4
104	    - JSD_0v1
105	    rows:
106	    - - greedy
107	      - 1
108	      - 0.9965
109	      - 0.5862
110	      - 0.5481
111	      - 0.5225
112	      - 0.2753
113	    - - nucleus p=0.9 T=1.0
114	      - 2
115	      - 0.9968
116	      - 0.6278
117	      - 0.5582
118	      - 0.5312
119	      - 0.2814
120	    - - p=0.95 T=0.7
121	      - 2
122	      - 0.9963
123	      - 0.6241
124	      - 0.5558
125	      - 0.5286
126	      - 0.2685
127	    - - p=0.95 T=1.2
128	      - 3
129	      - 0.9981
130	      - 0.6823
131	      - 0.6218
132	      - 0.5614
133	      - 0.3082
134	    - - baseline (p=0.95 T=1.0)
135	      - 2
136	      - 0.9972
137	      - 0.6114
138	      - 0.5609
139	      - 0.5408
140	      - 0.2863
141	  - caption: Feature degradation ordering 一致性 (Spearman ρ vs baseline)
142	    columns:
143	    - config
144	    - spearman_rho
145	    rows:
146	    - - greedy
147	      - 0.886
148	    - - p=0.9
149	      - 0.921
150	    - - T=0.7
151	      - 0.914
152	    - - T=1.2
153	      - 0.878
154	  figures_description:
155	  - 'K* vs 解码有效熵散点图: x轴为各解码配置的实际 token 分布熵估计，y轴为 K*。Greedy 在最左 K*=1，standard configs
156	    居中 K*=2，T=1.2 在最右 K*=3，形成清晰阶跃。'
157	  - '五配置 JSD decay 曲线族谱图: T=1.2 曲线在 depth=3 才穿过 θ=0.60 对应的 JSD 阈值线，greedy 在 depth=1
158	    就穿过，其余在 depth=2。'
159	  - 'Bootstrap CI 对比图: 各配置的 1v2 AUC 95% CI 与 θ=0.60 阈值线的关系，视觉化 K* 判定。'
160	  analysis: 'T=1.2 → K*=3 + greedy → K*=1 建立了完整的 K* 可调控梯度，这是论文最有力的发现之一。 审稿人无法再说 "K*=2
161	    is a ceiling"——它是 standard 解码下的 operating point，可被解码熵上下调控。 3/4 configs K*≥2 表明
162	    K*=2 在合理解码空间内高度稳健；greedy 的 K*=1 不是弱点而是优势： 它证明 K* 捕捉的是信道的真实信息论性质，而非分类器的统计 artifact。
163	    Feature ordering ρ≥0.878 跨所有配置，扩展了 exp-005 的 degradation ordering 一致性结论到新解码条件。
164	
165	    '
166	- name: Qwen2.5-7B 跨规模探测
167	  plan_id: exp-004
168	  description: 'Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth 0-3。 测试模型规模是否是
169	    K* 的杠杆。1K docs（vs 5K）引入更大方差但降低 GPU 成本。
170	
171	    '
172	  expected_results:
173	    pairwise_auc:
174	      0v1: 0.9984
175	      1v2: 0.6948
176	      2v3: 0.6175
177	    pairwise_auc_std:
178	      0v1: 0.0004
179	      1v2: 0.0092
180	      2v3: 0.0108
181	    pairwise_jsd:
182	      0v1: 0.3415
183	      1v2: 0.0285
184	      2v3: 0.0112
185	    k_star: 3
186	    ordinal_accuracy_4class: 0.4752
187	    ordinal_mae: 0.724
188	    bootstrap_ci_1v2:
189	    - 0.6782
190	    - 0.7108
191	    bootstrap_ci_2v3:
192	    - 0.6015
193	    - 0.6338
194	    top3_features:
195	    - surp_d1_std
196	    - surp_std
197	    - freq_entropy
198	    comparison_vs_1.5B:
199	      delta_auc_1v2: '+0.0834'
200	      delta_auc_2v3: '+0.0566'
201	      delta_jsd_0v1: '+0.0552'
202	  result_rationale: '7B 模型的参数空间是 1.5B 的 ~4.7 倍，编码了更丰富的语言分布。递归生成时，每代输出保留更多原始分布的细微结构：
203	    rare n-grams、长距离 discourse patterns、低频词汇的上下文相关用法。这些信息在 1.5B 级模型中首代就大部分丢失， 但在 7B
204	    中至少保持到第二代——因此 2v3 AUC=0.618 仍高于 θ=0.60，K*≥3。 具体机制：7B 的 next-token 分布有更长的"有意义尾巴"（tail
205	    tokens 仍携带语义区分力）， 递归第二代保留了这些 tail 的部分结构特征，到第三代才显著丢失。 1v2 AUC=0.695 较 1.5B 的 0.611
206	    提升 8.3pp，JSD_0v1=0.342 较 1.5B 的 0.286 提升 19%—— 更大模型的输出在特征空间中占据更大体积，递归压缩的"距离"更长。
207	    1K docs 的样本量约束使 CI 较宽（±0.015 vs 5K docs 的 ±0.010），但 2v3 CI lower=0.602 仍 comfortably
208	    高于 0.60。 Ordinal accuracy 4-class=0.475（chance=0.25），MAE=0.724，均显著优于 1.5B 的 6-class
209	    表现， 确认更多参数→更多可利用的代际特征梯度。
210	
211	    '
212	  tables:
213	  - caption: Qwen2.5-7B vs 1.5B pairwise discrimination 对比
214	    columns:
215	    - depth_pair
216	    - 7B_AUC
217	    - 7B_JSD
218	    - 1.5B_AUC_cont
219	    - 1.5B_JSD_cont
220	    rows:
221	    - - 0v1
222	      - 0.9984
223	      - 0.3415
224	      - 0.9972
225	      - 0.2863
226	    - - 1v2
227	      - 0.6948
228	      - 0.0285
229	      - 0.6114
230	      - 0.0051
231	    - - 2v3
232	      - 0.6175
233	      - 0.0112
234	      - 0.5609
235	      - 0.0036
236	  - caption: 7B bootstrap 95% CI
237	    columns:
238	    - depth_pair
239	    - AUC
240	    - CI_lower
241	    - CI_upper
242	    - CI_lower > 0.60?
243	    rows:
244	    - - 1v2
245	      - 0.6948
246	      - 0.6782
247	      - 0.7108
248	      - ✅ +7.8pp
249	    - - 2v3
250	      - 0.6175
251	      - 0.6015
252	      - 0.6338
253	      - ✅ +0.15pp
254	  figures_description:
255	  - 'Scale-K* 关系图: x轴为模型参数量（log scale: 1B, 1.4B, 1.5B, 7B），y轴为 K*。1B-1.5B 区间 K*=2
256	    稳定，7B 跳到 K*=3。虚线外推暗示更大模型 K*≥4。'
257	  - '7B vs 1.5B JSD decay 对比: 7B 曲线整体上移且右移，穿过 θ 阈值的 depth 更深，视觉化 scale → K* 效应。'
258	  analysis: '7B K*≥3 确认模型规模是 K* 的因果杠杆，与 exp-003 T=1.2 → K*=3 形成两条独立路径。 结合两者可写: "K*=2
259	    is not a ceiling but a floor that rises with model scale (7B) and decoding entropy
260	    (T=1.2)." 2v3 CI lower=0.602 虽然 margin 较小（受 1K docs 限制），但方向明确且与 1v2 的强信号一致。 如需更强统计力度，可考虑增至
261	    2K docs（额外 4 GPU-hours），但当前结果已足以支撑 claim。 对 ordinal_accuracy_best_model 的贡献: 7B
262	    4-class=0.475 落入 best 档范围 [0.42, 0.48]。
263	
264	    '
265	- name: Downstream graduated filtering 评估
266	  plan_id: exp-006
267	  description: 'Qwen2.5-1.5B depth chain (continuation mode), 比较 6 种过滤策略: no-filter
268	    / binary-ours (15D binary) / binary-Drayson (importance resampling) / graduated
269	    (3-class ordinal) / surprisal-based (单特征) / DSIR (分布匹配)。Continued pretraining
270	    + lm-eval-harness (MMLU, HellaSwag)。 5 seeds, paired t-test。graduated 加 α sensitivity
271	    sweep (α ∈ {0.1, 0.3, 0.5, 0.7, 0.9})。
272	
273	    '
274	  expected_results:
275	    mmlu_accuracy_pp:
276	      no_filter: 25.82
277	      binary_ours: 26.93
278	      binary_drayson: 27.21
279	      graduated_best_alpha: 29.41
280	      surprisal_based: 28.15
281	      dsir: 27.32
282	    hellaswag_accuracy_pp:
283	      no_filter: 43.24
284	      binary_ours: 44.38
285	      binary_drayson: 44.65
286	      graduated_best_alpha: 47.08
287	      surprisal_based: 45.92
288	      dsir: 44.81
289	    mmlu_std_5seeds:
290	      no_filter: 0.21
291	      binary_ours: 0.28
292	      binary_drayson: 0.32
293	      graduated: 0.25
294	      surprisal_based: 0.33
295	      dsir: 0.3
296	    hellaswag_std_5seeds:
297	      no_filter: 0.18
298	      binary_ours: 0.23
299	      binary_drayson: 0.27
300	      graduated: 0.2
301	      surprisal_based: 0.28
302	      dsir: 0.25
303	    key_deltas:
304	      graduated_minus_binary_ours_mmlu_pp: 2.48
305	      graduated_minus_binary_ours_hellaswag_pp: 2.7
306	      graduated_minus_dsir_mmlu_pp: 2.09
307	      graduated_minus_dsir_hellaswag_pp: 2.27
308	    paired_ttest_pvalues:
309	      graduated_vs_binary_ours_mmlu: 0.0043
310	      graduated_vs_binary_ours_hellaswag: 0.0067
311	      graduated_vs_dsir_mmlu: 0.0125
312	      graduated_vs_dsir_hellaswag: 0.0098
313	    alpha_sensitivity_mmlu:
314	      alpha_0.1: 27.45
315	      alpha_0.3: 28.72
316	      alpha_0.5: 29.41
317	      alpha_0.7: 29.08
318	      alpha_0.9: 28.14
319	    alpha_sensitivity_hellaswag:
320	      alpha_0.1: 44.85
321	      alpha_0.3: 46.28
322	      alpha_0.5: 47.08
323	      alpha_0.7: 46.72
324	      alpha_0.9: 45.65
325	    optimal_alpha: 0.5
326	  result_rationale: 'Binary filtering 的核心困境: gen-1 文本保留了原始文本 ~85% 的信息（0v1 AUC>0.99
327	    说明 gen-1 与 human 可区分， 但 1v2 AUC~0.61 说明 gen-1 仍保留了大部分质量）。Binary 策略要么丢掉这些高质量 gen-1（过严→训练数据量骤降），
328	    要么连 gen-2+ 一起保留（过松→引入已过 K* 的噪声数据）。 Graduated filtering 通过 3-class ordinal signal
329	    精确解耦: 对 gen-1 施加 α 衰减权重（降低但不移除）， 对 gen-2+ 完全移除。最优 α=0.5 意味着 gen-1 以半权重参与训练——保留了其信息价值同时抑制了合成偏差。
330	    MMLU 收益（+2.48pp）高于 HellaSwag，因为 MMLU 对知识密度更敏感：graduated 保留的 gen-1 中知识保真度高， binary
331	    移除后的知识缺口比常识推理缺口更难弥补。 Binary-Drayson 的 importance resampling 略优于 binary-ours（soft
332	    vs hard 决策边界），但仍做二值判断→无法利用 ordinal signal。 DSIR 做分布匹配但不估计 depth→对 depth-specific
333	    污染效果有限。 Surprisal-based 策略用单一特征（surprisal mean）做 proxy filtering，优于 binary 但不及
334	    graduated 的多维 ordinal signal。 α sensitivity 呈倒 U 形: α 太小（0.1）几乎等于 binary 移除，α
335	    太大（0.9）几乎等于 no-filter。 5 seeds paired t-test p<0.01 确认 graduated vs binary-ours
336	    的差异非采样噪声。
337	
338	    '
339	  tables:
340	  - caption: 6 策略 downstream 评估 (5 seeds mean ± std)
341	    columns:
342	    - strategy
343	    - MMLU_pp
344	    - MMLU_std
345	    - HellaSwag_pp
346	    - HS_std
347	    rows:
348	    - - no-filter
349	      - 25.82
350	      - 0.21
351	      - 43.24
352	      - 0.18
353	    - - binary-ours
354	      - 26.93
355	      - 0.28
356	      - 44.38
357	      - 0.23
358	    - - binary-Drayson
359	      - 27.21
360	      - 0.32
361	      - 44.65
362	      - 0.27
363	    - - graduated (α=0.5)
364	      - 29.41
365	      - 0.25
366	      - 47.08
367	      - 0.2
368	    - - surprisal-based
369	      - 28.15
370	      - 0.33
371	      - 45.92
372	      - 0.28
373	    - - DSIR
374	      - 27.32
375	      - 0.3
376	      - 44.81
377	      - 0.25
378	  - caption: 关键对比统计显著性 (paired t-test, 5 seeds)
379	    columns:
380	    - comparison
381	    - Δ_MMLU_pp
382	    - p_MMLU
383	    - Δ_HellaSwag_pp
384	    - p_HellaSwag
385	    rows:
386	    - - graduated vs binary-ours
387	      - 2.48
388	      - 0.0043
389	      - 2.7
390	      - 0.0067
391	    - - graduated vs DSIR
392	      - 2.09
393	      - 0.0125
394	      - 2.27
395	      - 0.0098
396	    - - graduated vs binary-Drayson
397	      - 2.2
398	      - 0.0082
399	      - 2.43
400	      - 0.0054
401	    - - graduated vs surprisal-based
402	      - 1.26
403	      - 0.0318
404	      - 1.16
405	      - 0.0425
406	  - caption: α sensitivity sweep (graduated, MMLU)
407	    columns:
408	    - α
409	    - MMLU_pp
410	    - HellaSwag_pp
411	    rows:
412	    - - 0.1
413	      - 27.45
414	      - 44.85
415	    - - 0.3
416	      - 28.72
417	      - 46.28
418	    - - 0.5
419	      - 29.41
420	      - 47.08
421	    - - 0.7
422	      - 29.08
423	      - 46.72
424	    - - 0.9
425	      - 28.14
426	      - 45.65
427	  figures_description:
428	  - '6 策略 benchmark bar chart (error bars = 1 std over 5 seeds): graduated 最高，与 binary-ours
429	    之间有清晰 gap。'
430	  - 'α sensitivity curve (倒 U 形): 最优 α=0.5，α→0 趋向 binary 性能，α→1 趋向 no-filter 性能。'
431	  - 'Filtering precision-recall 在 gen-1 附近: graduated 的 calibrated soft boundary vs
432	    binary 的 hard step function，视觉化 ordinal signal 的阈值优势。'
433	  analysis: 'graduated vs binary-ours Δ≥2.48pp (MMLU) 和 2.70pp (HellaSwag) 均落入 best
434	    档 [2.0, 4.0] 且 p<0.01。 C3 成立: 即使 K*=2 的粗粒度 3-class ordinal signal 也能在 downstream
435	    产生显著收益。 Binary-ours vs graduated 的唯一变量是 binary/ordinal decision→公平验证了 ordinal
436	    structure 的价值。 DSIR 和 binary-Drayson 的存在证明 graduated 的优势不仅来自"更好的 filtering"而是来自
437	    depth-aware 决策。 α=0.5 的最优性直观: gen-1 质量约为 human 的 ~85%（基于 1v2 AUC），半权重大致反映这个质量折扣。
438	
439	    '
440	- name: Retrain-chain 生态效度验证
441	  plan_id: exp-008
442	  description: 'Pythia-1.4B LoRA (rank=16, alpha=32) retrain-chain vs prompt-chain,
443	    C4 5K docs, depth 0-4。验证 prompt-chain 是否是 retrain-chain 的合理实验代理。
444	
445	    '
446	  expected_results:
447	    retrain_chain:
448	      k_star: 2
449	      pairwise_auc:
450	        0v1: 0.9895
451	        1v2: 0.6362
452	        2v3: 0.5448
453	        3v4: 0.5128
454	      pairwise_jsd:
455	        0v1: 0.2058
456	        1v2: 0.0118
457	        2v3: 0.0044
458	        3v4: 0.0029
459	    prompt_chain_actual:
460	      k_star: 2
461	      pairwise_auc:
462	        0v1: 0.9932
463	        1v2: 0.6539
464	        2v3: 0.5515
465	        3v4: 0.5153
466	    kstar_diff: 0
467	    auc_1v2_diff: -0.0177
468	    feature_distribution_jsd_retrain_vs_prompt:
469	      depth_0: 0.0018
470	      depth_1: 0.0162
471	      depth_2: 0.0285
472	      depth_3: 0.0378
473	    cross_method_transfer_retention: 0.915
474	  result_rationale: 'LoRA rank=16 (alpha=32) 只修改了参数空间中一个 16 维的低秩子空间， 实际参数变化量 < 模型总参数的
475	    0.2%——这意味着 retrain-chain 的每代"模型"与原始 Pythia-1.4B 高度相似。 因此 retrain-chain 的行为应近似于
476	    prompt-chain：两者都是同一个（或近似相同的）模型对自身输出的迭代。 K* diff=0：DPI 约束是拓扑性的——只要信道是有损的（LoRA 微调后仍是有损信道），收敛行为保持。
477	    AUC 差异 -0.018：retrain-chain 略低，因为 LoRA 微调在每代引入微小但累积的分布偏移， 这些偏移模糊了"纯递归"的代际边界——相当于在递归信道上叠加了一层
478	    adaptation noise。 Feature distribution JSD 随 depth 递增是预期行为：更深代际累积了更多 retrain 偏移。
479	    但 JSD < 0.04 在所有 depth，远低于代际间的 JSD（~0.01-0.21）， 确认 prompt-chain 的代际差异主导了 retrain
480	    偏移效应。 Cross-method transfer retention 91.5%: prompt-chain 上训练的 classifier 在 retrain-chain
481	    上保持高性能。
482	
483	    '
484	  tables:
485	  - caption: Retrain-chain vs prompt-chain 对比 (Pythia-1.4B)
486	    columns:
487	    - depth_pair
488	    - retrain_AUC
489	    - prompt_AUC
490	    - Δ_AUC
491	    rows:
492	    - - 0v1
493	      - 0.9895
494	      - 0.9932
495	      - -0.0037
496	    - - 1v2
497	      - 0.6362
498	      - 0.6539
499	      - -0.0177
500	    - - 2v3
501	      - 0.5448
502	      - 0.5515
503	      - -0.0067
504	    - - 3v4
505	      - 0.5128
506	      - 0.5153
507	      - -0.0025
508	  - caption: Feature 分布偏移 (retrain vs prompt JSD by depth)
509	    columns:
510	    - depth
511	    - JSD
512	    rows:
513	    - - 0
514	      - 0.0018
515	    - - 1
516	      - 0.0162
517	    - - 2
518	      - 0.0285
519	    - - 3
520	      - 0.0378
521	  figures_description:
522	  - 'Retrain vs prompt JSD decay 对比: 两条曲线近乎重叠，附 bootstrap 95% CI shading。'
523	  - 'Feature space t-SNE: retrain 和 prompt 在同一 depth 的点高度混合，depth 之间有清晰分离。不同颜色区分 method，不同标记区分
524	    depth。'
525	  analysis: 'K* diff=0 且 AUC 差异 < 2pp，直接回应 "prompt-chain 不代表真实递归污染" 的审稿人顾虑。 Prompt-chain
526	    作为 controlled proxy 的生态效度得到确认。 Feature JSD 随 depth 缓慢递增的模式可作为 supplementary 报告:
527	    它表明 retrain adaptation 的效应虽然累积但始终被代际退化信号所主导。 Cross-method transfer 91.5% 与 exp-013
528	    的 Pythia↔OLMo 91-92% 一致—— 换言之，prompt vs retrain 的差异与同族不同模型的差异量级相当。
529	
530	    '
531	- name: Contamination dose-response
532	  plan_id: exp-009
533	  description: '10%/30%/50% synthetic injection 比例下 graduated vs binary filtering
534	    的收益差异。 基于 exp-006 的实验框架，仅变化 injection 比例。5 seeds, MMLU+HellaSwag。
535	
536	    '
537	  expected_results:
538	    graduated_vs_binary_delta_mmlu_pp:
539	      injection_10pct: 0.72
540	      injection_30pct: 2.48
541	      injection_50pct: 3.82
542	    graduated_vs_binary_delta_hellaswag_pp:
543	      injection_10pct: 0.51
544	      injection_30pct: 2.7
545	      injection_50pct: 3.48
546	    graduated_vs_binary_pvalue_mmlu:
547	      injection_10pct: 0.142
548	      injection_30pct: 0.0043
549	      injection_50pct: 0.0008
550	    graduated_vs_binary_pvalue_hellaswag:
551	      injection_10pct: 0.218
552	      injection_30pct: 0.0067
553	      injection_50pct: 0.0012
554	    trend: monotonically increasing with injection rate
555	    significance_threshold_pct: ~20% injection for p<0.05
556	  result_rationale: '10% injection 时，训练数据中仅 10% 是合成文本（其中 gen-1 约 5%，gen-2+ 约 5%），
557	    binary 策略移除全部 10% 的信息损失较小，错分 gen-1 的代价也小（因为总量少）→graduated 的边际收益有限（<1pp, p>0.05）。
558	    30% 对应 exp-006 主实验条件，graduated 优势 ~2.5pp。 50% injection 是 graduated 价值最大化的条件:
559	    半数数据是合成的，其中 gen-1 占 ~25% 的全部训练数据。 Binary 面临极端权衡——移除全部 50% 导致训练数据减半（catastrophic
560	    data loss）， 保留则引入 ~25% gen-2+ 噪声。Graduated 精确解耦: gen-1 以 α=0.5 权重保留→等效保留 12.5%
561	    高质量数据， gen-2+ 移除→等效移除 25% 噪声。净效果: graduated 比 binary 多保留 12.5% 有用数据同时多移除等量噪声。
562	    单调递增趋势是 C3 的核心叙事: "The value of depth-aware curation scales with contamination
563	    severity."
564	
565	    '
566	  tables:
567	  - caption: 'Dose-response: graduated vs binary Δ by contamination rate'
568	    columns:
569	    - injection_rate
570	    - Δ_MMLU_pp
571	    - p_MMLU
572	    - Δ_HellaSwag_pp
573	    - p_HellaSwag
574	    rows:
575	    - - 10%
576	      - 0.72
577	      - 0.142
578	      - 0.51
579	      - 0.218
580	    - - 30%
581	      - 2.48
582	      - 0.0043
583	      - 2.7
584	      - 0.0067
585	    - - 50%
586	      - 3.82
587	      - 0.0008
588	      - 3.48
589	      - 0.0012
590	  figures_description:
591	  - 'Dose-response curve: x轴 injection rate, y轴 graduated−binary Δ (pp)。MMLU/HellaSwag
592	    两条线均单调递增。横虚线标注 2pp 和 p=0.05 阈值。'
593	  - 'Stacked bar: 各 injection rate 下 no-filter/binary/graduated 绝对性能对比。随着 injection
594	    rate 升高，no-filter 下降最快，graduated 最稳健。'
595	  analysis: '单调递增的 dose-response 关系是 graduated filtering 实际部署价值的最直接证据。 10% injection
596	    下 p>0.05 是预期中的——低污染率下任何 filtering 策略都足够好，无需精细化。 50% injection 下 Δ=3.82pp (MMLU)
597	    落入 best 档上限附近 [2.0, 4.0]。 这为 practical impact 叙事提供核心论据: 当前 web 数据合成文本比例估计 15-30%（且在增长），
598	    graduated filtering 在这个区间恰好开始产生统计显著收益，随比例增长价值越大。
599	
600	    '
601	- name: LLM zero-shot depth estimation baseline
602	  plan_id: exp-011
603	  description: 'GPT-4o / Claude 3.5 Sonnet 对 depth 0-4 文本做 zero-shot depth 判断。 200
604	    samples per depth (共 1000 样本), 5-class classification。 验证 depth estimation 不能被
605	    frontier LLM 的通用能力"免费"解决。
606	
607	    '
608	  expected_results:
609	    gpt4o:
610	      accuracy: 0.218
611	      mae: 1.742
612	      kendall_tau_with_true_depth: 0.082
613	      confusion_matrix_diagonal_pct: 0.218
614	    claude_3_5_sonnet:
615	      accuracy: 0.234
616	      mae: 1.668
617	      kendall_tau_with_true_depth: 0.118
618	      confusion_matrix_diagonal_pct: 0.234
619	    our_ordinal_classifier:
620	      accuracy: 0.423
621	      mae: 0.984
622	      kendall_tau_with_true_depth: 0.552
623	    random_baseline:
624	      accuracy: 0.2
625	      mae: 2.0
626	    llm_common_failure_mode: LLM 倾向将所有文本判为 depth 0 或 1，几乎不预测 depth≥3
627	  result_rationale: 'LLM zero-shot depth estimation 近乎随机，三个结构性原因: (1) Depth signal
628	    是统计性的——需要同一 domain 的多样本分布对比，单文本缺乏参照系。 LLM 每次只看一篇文本，无法感知"这篇相对于同源文本的 vocabulary
629	    diversity 降低了多少"。 (2) LLM 的"质量判断"偏向 fluency/coherence/factuality，而这些高层语义特征恰恰是最后才饱和的（与
630	    C2 degradation ordering 一致）。 即使 gen-3 的 vocabulary diversity 已严重退化，LLM 仍判定其"写得不错"因为它仍然
631	    fluent。 (3) Depth 是一个 training-data 中从未出现过的概念——LLM 没有被训练理解"递归生成导致的信息损失梯度"， 其世界模型中不存在"第
632	    N 代合成文本"这个 schema。 Claude 略优于 GPT-4o（差异在 noise range 内）可能反映 Claude 对文本微妙模式的 slightly
633	    better sensitivity。 两者均远低于 15D ordinal classifier（accuracy 0.42 vs 0.22），倍率 ~1.9x。
634	
635	    '
636	  tables:
637	  - caption: 'Zero-shot depth estimation: frontier LLM vs ordinal classifier'
638	    columns:
639	    - method
640	    - accuracy
641	    - MAE
642	    - Kendall_τ
643	    rows:
644	    - - GPT-4o (zero-shot)
645	      - 0.218
646	      - 1.742
647	      - 0.082
648	    - - Claude 3.5 Sonnet (zero-shot)
649	      - 0.234
650	      - 1.668
651	      - 0.118
652	    - - Random baseline
653	      - 0.2
654	      - 2.0
655	      - 0.0
656	    - - Our ordinal classifier (15D)
657	      - 0.423
658	      - 0.984
659	      - 0.552
660	  figures_description:
661	  - 'Confusion matrix 三面板: LLM 预测分布近乎 uniform（微偏向 depth 0-1），ordinal classifier 对角线主导。'
662	  - 'Per-depth accuracy breakdown: LLM 在 depth=0 的 accuracy 最高（~0.35）但仍低于 classifier（~0.70），depth≥2
663	    完全随机。'
664	  analysis: 'LLM zero-shot 仅比 random chance 高 1.8-3.4pp，而 ordinal classifier 高出 22.3pp。
665	    这确立了 depth estimation 作为需要专门方法的 task——不能被 frontier LLM 的 general intelligence
666	    "免费"解决。 这是论文 problem formulation 的关键支撑: 我们定义的问题是 genuinely novel 且有技术门槛的。 LLM
667	    偏向预测 depth=0/1 的 failure mode 与 C2 一致——高层语义质量在前几代保持， 导致 LLM "认为大部分文本都是 human-written
668	    或 first-generation"。
669	
670	    '
671	- name: Binary detector confidence 作为 depth proxy
672	  plan_id: exp-012
673	  description: 'DivEye / Binoculars score 与 true depth 的 Spearman correlation, 在 exp-001
674	    (Pythia) 和 exp-002 (OLMo) depth chain 上评估。
675	
676	    '
677	  expected_results:
678	    diveye:
679	      spearman_rho_with_depth: 0.223
680	      spearman_p_value: 0.001
681	      auc_0v1: 0.935
682	      auc_1v2: 0.528
683	      auc_2v3: 0.508
684	    binoculars:
685	      spearman_rho_with_depth: 0.184
686	      spearman_p_value: 0.003
687	      auc_0v1: 0.912
688	      auc_1v2: 0.521
689	      auc_2v3: 0.505
690	    our_15d_features:
691	      auc_0v1: 0.995
692	      auc_1v2: 0.634
693	      auc_2v3: 0.5505
694	    binary_score_depth_correlation_interpretation: 'Binary scores 在 depth=0→1 处有大跳跃然后
695	      plateau—— 所有 depth≥1 的合成文本在 binary score 空间中挤在一个窄 band 内。
696	
697	      '
698	  result_rationale: 'Binary detectors 的训练目标是最大化 real/synthetic 决策边界，不是估计 "how synthetic"。
699	    其 confidence score 在 depth=0→1 跳跃后迅速饱和，原因: (1) DivEye 和 Binoculars 使用的 summary
700	    statistics（如 min-k% perplexity、cross-entropy ratio） 在 gen-1 就已经偏离 human 文本的分布，之后
701	    gen-2→gen-5 的偏移量极小（增量 < noise）。 (2) 这些 detectors 被优化为在 human/synthetic 边界处有最大
702	    separability—— 边界远处（depth≥2）的分辨力从未被训练目标所选择。 Spearman ρ 显著但极弱（0.18-0.22），因为 depth=0
703	    vs depth≥1 的 rank 差异贡献了大部分 correlation， depth≥1 内部几乎无 rank 信息。 DivEye 略优于 Binoculars
704	    因为其 vocabulary diversity 相关特征恰好也编码了少量 depth 信息。 关键对比: 我们的 15D features 在 1v2 AUC
705	    上高出 binary detectors ~10pp， 证明 binary confidence ≠ depth，depth estimation 需要专用特征。
706	
707	    '
708	  tables:
709	  - caption: Binary detector scores 作为 depth proxy
710	    columns:
711	    - detector
712	    - Spearman_ρ
713	    - p_value
714	    - AUC_0v1
715	    - AUC_1v2
716	    - AUC_2v3
717	    rows:
718	    - - DivEye
719	      - 0.223
720	      - 0.001
721	      - 0.935
722	      - 0.528
723	      - 0.508
724	    - - Binoculars
725	      - 0.184
726	      - 0.003
727	      - 0.912
728	      - 0.521
729	      - 0.505
730	    - - Our 15D features
731	      - —
732	      - —
733	      - 0.995
734	      - 0.634
735	      - 0.551
736	  figures_description:
737	  - 'Binary score vs true depth scatter: score 在 depth=0→1 有大跳跃，depth≥1 几乎平坦 (ceiling
738	    effect)。附 LOESS smooth line。'
739	  - 'Pairwise AUC decay 对比: binary detectors 在 1v2 处即降至 chance level，我们的 features
740	    保持到 depth=2。'
741	  analysis: 'Binary detectors 在 0v1 处强劲（AUC 0.91-0.94）但 1v2 处近乎 chance level（0.52-0.53），
742	    直接证明 "binary detection ≠ depth estimation"。 这是论文 related work positioning 的关键数据:
743	    existing methods solve a different (easier) problem。 Spearman ρ 的统计显著性反映的是 binary
744	    信号本身（depth=0 vs all），而非 ordinal depth estimation 能力。
745	
746	    '
747	- name: Common Crawl 自然验证
748	  plan_id: exp-014
749	  description: '对 Common Crawl 2025/2026 snapshot 10K 样本做 depth 预测， 与 AlignScore (事实一致性)
750	    和 vocabulary richness 指标做 correlation。 无 ground truth，仅间接验证。
751	
752	    '
753	  expected_results:
754	    spearman_predicted_depth_vs_alignscore: -0.288
755	    spearman_predicted_depth_vs_vocab_richness: -0.342
756	    spearman_p_values:
757	      alignscore: <0.001
758	      vocab_richness: <0.001
759	    pct_samples_predicted_depth_geq_1: 17.5
760	    pct_samples_predicted_depth_geq_2: 6.8
761	    pct_samples_predicted_depth_geq_3: 2.1
762	    predicted_depth_distribution:
763	      depth_0: 82.5
764	      depth_1: 10.7
765	      depth_2: 4.7
766	      depth_3_plus: 2.1
767	  result_rationale: 'Common Crawl 中的真实合成文本比例和代际深度无 ground truth，只能通过与外部质量指标的 correlation
768	    间接验证。 Predicted depth 与 AlignScore 呈负相关（ρ≈-0.29），因为更深代际的文本在递归"电话游戏"中积累了更多事实偏差。
769	    与 vocabulary richness 的负相关更强（ρ≈-0.34），与 C2 degradation ordering 一致: vocabulary
770	    diversity 是最先退化的特征组，predicted depth 高的文本确实词汇更贫乏。 ~17.5% 样本被预测为 depth≥1 与 2025-2026
771	    时期 web 合成文本比例的外部估计（15-25%）一致。 Depth≥2 仅 6.8%——大部分合成文本是"首代"（直接由模型生成），多代递归仍是小众现象。
772	    相关性不高（|ρ|<0.35）是预期中的: wild data 的噪声（domain 多样性、unknown model 族、未知解码策略） 稀释了在 controlled
773	    实验中观察到的信号。这些结果属于 "proof of concept" 级别。
774	
775	    '
776	  tables:
777	  - caption: Common Crawl 自然验证
778	    columns:
779	    - metric
780	    - value
781	    rows:
782	    - - Spearman(pred depth, AlignScore)
783	      - -0.288
784	    - - Spearman(pred depth, vocab richness)
785	      - -0.342
786	    - - '% pred depth ≥ 1'
787	      - 17.5%
788	    - - '% pred depth ≥ 2'
789	      - 6.8%
790	    - - '% pred depth ≥ 3'
791	      - 2.1%
792	  figures_description:
793	  - 'Predicted depth 分布直方图: depth=0 占 82.5%，depth=1 占 10.7%，depth=2+ 占 6.8%。'
794	  - 'Predicted depth vs AlignScore scatter (LOESS smooth): 清晰下降趋势但散点稀疏。'
795	  - 'Predicted depth vs vocabulary richness scatter: 负相关趋势更清晰。'
796	  analysis: '自然验证提供 "proof of concept" 级别的 wild-data 证据。 相关性方向正确且显著，足以支持 appendix
797	    或 discussion section 的 generalizability 论述。 不足以作为 main claim 的证据但有效回应 "只在 controlled
798	    设置下验证" 的审稿人顾虑。 Predicted depth 分布与 web 合成文本比例估计的一致性增加了 classifier 的可信度。
799	
800	    '
801	- name: Learned representation baseline
802	  plan_id: exp-015
803	  description: 'Frozen Qwen2.5-1.5B embeddings (last hidden state, 1536-dim) + 2-layer
804	    MLP vs hand-crafted 15D features + LightGBM。在 Qwen continuation depth chain 上评估。
805	
806	    '
807	  expected_results:
808	    frozen_embeddings_mlp:
809	      auc_1v2: 0.5982
810	      mean_pw_auc: 0.5865
811	      ordinal_accuracy: 0.3708
812	      mae: 1.195
813	      training_time_gpu_hours: 2.6
814	      feature_dim: 1536
815	    handcrafted_15d:
816	      auc_1v2: 0.6112
817	      mean_pw_auc: 0.6048
818	      ordinal_accuracy: 0.3875
819	      mae: 1.155
820	      training_time_gpu_hours: 0.08
821	      feature_dim: 15
822	    gap_auc_1v2_pp: 1.3
823	    gap_mean_pw_auc_pp: 1.83
824	    gap_ordinal_accuracy_pp: 1.67
825	    cross_model_transfer_frozen:
826	      frozen_on_qwen_test_pythia_retention: 0.62
827	      handcrafted_on_qwen_test_pythia_retention: 0.85
828	  result_rationale: 'Frozen embeddings 包含丰富的语义信息但存在三个结构性劣势: (1) 1536 维中绝大部分编码内容语义（topic,
829	    entity, style），而非递归退化信号—— MLP 需要从高维空间中"挖掘"少数相关维度。在 5K 训练样本下，这个搜索问题容易过拟合。 (2) Frozen
830	    embeddings 来自同一模型（Qwen2.5-1.5B），引入自我参照偏差: 模型对自己生成的文本有系统性 embedding 偏向，但这种偏向在 cross-model
831	    设置下不 transfer—— 因此 frozen 的 cross-model retention 仅 62%，远低于 15D 的 85%。 (3) Embedding
832	    空间中的 depth signal 不是线性可分的，2-layer MLP 的容量有限。 Hand-crafted 15D 的优势: 每个特征都直接编码与递归退化相关的统计量（diversity/surprisal/tail
833	    weight）， 人类先验弥补了维度不足。AUC gap 1.30pp < 3pp (best 档要求 < 3pp)。 更关键的是 interpretability
834	    优势: 15D 支持 degradation ordering 分析（exp-005/C2）和 feature group ablation， 这是 frozen
835	    embeddings 无法提供的。论文叙事需要 interpretable features 来讲述 "which linguistic properties
836	    degrade first" 的故事。
837	
838	    '
839	  tables:
840	  - caption: Learned vs hand-crafted features 对比
841	    columns:
842	    - method
843	    - AUC_1v2
844	    - mean_pw_AUC
845	    - ordinal_acc
846	    - MAE
847	    - dim
848	    - GPU_hours
849	    rows:
850	    - - frozen embeddings + MLP
851	      - 0.5982
852	      - 0.5865
853	      - 0.3708
854	      - 1.195
855	      - 1536
856	      - 2.6
857	    - - hand-crafted 15D
858	      - 0.6112
859	      - 0.6048
860	      - 0.3875
861	      - 1.155
862	      - 15
863	      - 0.08
864	  - caption: Cross-model transfer 对比 (train Qwen → test Pythia)
865	    columns:
866	    - method
867	    - in_domain_acc
868	    - cross_model_acc
869	    - retention_pct
870	    rows:
871	    - - frozen embeddings
872	      - 0.3708
873	      - 0.2299
874	      - 62%
875	    - - hand-crafted 15D
876	      - 0.3875
877	      - 0.3294
878	      - 85%
879	  figures_description:
880	  - 'Performance vs interpretability 双轴图: 15D 在 Pareto 前沿（低维高性能），frozen 在高维略低性能区。'
881	  - 'Cross-model transfer retention bar chart: frozen 62% vs 15D 85%，视觉化 interpretable
882	    features 的 generalization 优势。'
883	  analysis: 'AUC gap 1.30pp < 3pp 满足 best 档假设。15D hand-crafted 在所有指标上优于或持平 frozen
884	    embeddings， 且维度低 102 倍、训练快 32.5 倍。 Cross-model transfer 的巨大差距（85% vs 62%）是 decisive
885	    argument: frozen embeddings 过拟合 model-specific embedding space，而 15D 统计特征是 model-agnostic
886	    的。 这验证了论文 "选择 interpretable features 不是方法论妥协而是设计优势" 的叙事， 同时回应审稿人 "为什么不用 learned
887	    representations" 的问题。
888	
889	    '
890	- name: Base vs Instruct 模型对比
891	  plan_id: exp-016
892	  description: 'Qwen2.5-1.5B base model (非 instruct 微调版) continuation mode, C4 5K
893	    docs, depth 0-5。 与 exp-017 (Qwen2.5-1.5B-Instruct continuation) 对比，分离 RLHF/instruction-tuning
894	    对 K* 的影响。
895	
896	    '
897	  expected_results:
898	    base:
899	      k_star: 2
900	      pairwise_auc:
901	        0v1: 0.9958
902	        1v2: 0.6382
903	        2v3: 0.5685
904	        3v4: 0.5358
905	        4v5: 0.5148
906	      pairwise_jsd:
907	        0v1: 0.2952
908	        1v2: 0.0068
909	        2v3: 0.0042
910	        3v4: 0.0032
911	        4v5: 0.0028
912	      ordinal_accuracy: 0.3948
913	      top3_features:
914	      - surp_d1_std
915	      - surp_std
916	      - freq_entropy
917	    instruct_actual:
918	      k_star: 2
919	      pairwise_auc:
920	        0v1: 0.9972
921	        1v2: 0.6114
922	        2v3: 0.5609
923	        3v4: 0.5408
924	        4v5: 0.5139
925	    base_vs_instruct_diff:
926	      delta_auc_1v2: '+0.0268'
927	      delta_auc_2v3: '+0.0076'
928	      delta_jsd_0v1: '+0.0089'
929	    feature_shift:
930	      surprisal_mean_base_vs_instruct: -0.14 std units
931	      vocab_diversity_base_vs_instruct: +0.06 std units
932	  result_rationale: 'RLHF/instruction-tuning 将模型输出拉向 "人类偏好的模式"——更规范的句式、更安全的措辞、更集中的
933	    vocabulary 选择。 这种 alignment 相当于对输出分布施加了额外的低熵约束，使得即使 gen-0→gen-1 的转换也已经部分"标准化"了。
934	    结果: instruct 模型的递归代际间差异更小，因为每代输出都被拉向同一个 "preferred mode"。 Base model 没有这个约束，输出更接近预训练数据的原始分布→递归代际间保留更多分布结构→1v2
935	    AUC 高 2.7pp。 但 K* 仍为 2: alignment 的影响是 quantitative（减弱信号 2.7pp）而非 qualitative（改变收敛行为）。
936	    DPI 的信息论约束在有无 RLHF 的情况下都成立——只要模型是有限容量的 lossy channel。 Surprisal mean 偏移为负（instruct
937	    更"可预测"，反映 RLHF 倾向于生成预期输出）; vocabulary diversity 偏移为正（instruct 词汇稍更多样，反映 RLHF 鼓励的表达丰富性）。
938	    两种偏移方向一致且量级小（< 0.15 std），为 discussion 段落提供数据。
939	
940	    '
941	  tables:
942	  - caption: Base vs Instruct 对比 (Qwen2.5-1.5B, continuation mode)
943	    columns:
944	    - variant
945	    - K*
946	    - AUC_0v1
947	    - AUC_1v2
948	    - AUC_2v3
949	    - JSD_0v1
950	    - ordinal_acc
951	    rows:
952	    - - base
953	      - 2
954	      - 0.9958
955	      - 0.6382
956	      - 0.5685
957	      - 0.2952
958	      - 0.3948
959	    - - instruct (exp-017)
960	      - 2
961	      - 0.9972
962	      - 0.6114
963	      - 0.5609
964	      - 0.2863
965	      - 0.3819
966	    - - Δ (base − instruct)
967	      - 0
968	      - '-0.0014'
969	      - '+0.0268'
970	      - '+0.0076'
971	      - '+0.0089'
972	      - '+0.0129'
973	  figures_description:
974	  - 'Base vs instruct JSD decay 对比: base 曲线在 depth 1-2 段系统性高于 instruct，差距在 depth≥3
975	    后消失。'
976	  - 'Feature distribution violin plots: base vs instruct 在 depth=1 的 surprisal mean
977	    和 vocab diversity 分布差异。'
978	  analysis: 'Base 信号更强但 K* 不变——RLHF alignment 压缩了代际差异但未改变信息论收敛行为。 这对实际应用有关键意义: 野外合成文本可能来自
979	    base 或 instruct 模型， K*=2 在两种设置下一致意味着 graduated filtering 框架对两者都适用。 Base model
980	    1v2 AUC=0.638 的 CI 预期 lower bound ~0.628（远高于 0.60）， 为 Qwen-cont instruct 的 0.0015
981	    margin 脆弱性提供了安全网: 即使 instruct 模型在重复实验中偶尔 CI lower 落到 0.599，base model 的稳健 K*=2
982	    仍支撑 claim。'
983	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fea37bf7-7479-40fe-a76f-6b78d70ef748",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "c57acc1a-233f-45fb-873b-a4a8e33669c6",
  "sourceToolAssistantUUID": "fea37bf7-7479-40fe-a76f-6b78d70ef748",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-13T08:49:14.881Z_

I now have a comprehensive understanding of the paper, its experimental results, the project decisions, and the literature positioning. Let me now also check if the cross-model transfer experiment details are available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c57acc1a-233f-45fb-873b-a4a8e33669c6",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazHBXtzTmL4bkqoLz17W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e69d869c-4fdb-4543-88e1-c06b48195e32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PeHmjwatCNzXpZwpkWS5Xo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18464,
      "cache_read_input_tokens": 51136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18464,
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

_source line 53 · 2026-05-13T08:49:17.239Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0192Va88sjFznuj1jMGi6m6s`</summary>

```json
{
  "pattern": "**/exp_013*/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e69d869c-4fdb-4543-88e1-c06b48195e32",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazHBXtzTmL4bkqoLz17W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38d2d1b8-b717-46e2-9955-4d9eb5c9c642",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PeHmjwatCNzXpZwpkWS5Xo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18464,
      "cache_read_input_tokens": 51136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18464,
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

_source line 54 · 2026-05-13T08:49:17.264Z_

<details><summary>↩ Tool result · `toolu_0192Va88sjFznuj1jMGi6m6s`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38d2d1b8-b717-46e2-9955-4d9eb5c9c642",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "472c1c82-aa5f-4fdc-aa62-2d40de43ca58",
  "sourceToolAssistantUUID": "38d2d1b8-b717-46e2-9955-4d9eb5c9c642",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-13T08:49:17.738Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VJPsgi1NcNntgBvmncTEbr`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "472c1c82-aa5f-4fdc-aa62-2d40de43ca58",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazHBXtzTmL4bkqoLz17W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4cd8caf-c4de-42e7-a591-58529b955c6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PeHmjwatCNzXpZwpkWS5Xo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18464,
      "cache_read_input_tokens": 51136,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18464
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 51136,
          "cache_creation_input_tokens": 18464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18464,
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

_source line 56 · 2026-05-13T08:49:17.749Z_

<details><summary>↩ Tool result · `toolu_01VJPsgi1NcNntgBvmncTEbr`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_provenance.yaml found for 'gen-depth-contamination'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4cd8caf-c4de-42e7-a591-58529b955c6d",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "c523bef3-987a-4d07-8fea-de143225c3e7",
  "sourceToolAssistantUUID": "c4cd8caf-c4de-42e7-a591-58529b955c6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-13T08:49:20.599Z_

I now have sufficient material to write a thorough R2 review. Let me submit it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c523bef3-987a-4d07-8fea-de143225c3e7",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazHC2cPvx7mtzo1Fi9bw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1f7404a-a248-4e87-949a-2f4911666fe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdoE7qgDC5c955wH9DmoPA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 462,
      "cache_read_input_tokens": 69600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 462,
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

_source line 58 · 2026-05-13T08:49:21.245Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Pan2M7eLVFTCqB8AddmX6t`</summary>

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
  "parentUuid": "b1f7404a-a248-4e87-949a-2f4911666fe8",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazHC2cPvx7mtzo1Fi9bw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd4b158b-d85d-4968-831e-346768975f57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdoE7qgDC5c955wH9DmoPA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 462,
      "cache_read_input_tokens": 69600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 462,
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

_source line 59 · 2026-05-13T08:49:21.247Z_

<details><summary>↩ Tool result · `toolu_01Pan2M7eLVFTCqB8AddmX6t`</summary>

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
  "parentUuid": "cd4b158b-d85d-4968-831e-346768975f57",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "a2057fb7-c101-4bb4-bb8b-0d9c00bbff2b",
  "sourceToolAssistantUUID": "cd4b158b-d85d-4968-831e-346768975f57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-13T08:49:24.285Z_



Now I have all the information needed. Let me compose and submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2057fb7-c101-4bb4-bb8b-0d9c00bbff2b",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazHCHtAL9bZ2x9zEVAaq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8106ebd6-0467-4a67-a20e-38127719c6ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Xf7njGgTP7T8rEw8DYao5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 70062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 688,
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

_source line 61 · 2026-05-13T08:51:01.868Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01PLYuzbQh5VbfyM6zZMC1Wy`</summary>

```json
{
  "report": "\n# Reviewer 2 (R2): Novelty, Related Work, and Broader Impact\n\n## 1. Summary\n\nThis paper formalizes recursive synthetic text generation as an iterated lossy channel, invokes DPI to argue for a finite \"generational discrimination boundary\" K*, and provides the first systematic empirical measurement of K* across model families, scales, and decoding strategies. The main finding is K*=2 for 1.5B models under standard decoding, rising to K*>=3 at 7B scale or high temperature. A secondary contribution shows that even a coarse 3-class ordinal signal (human/gen-1/gen-2+) enables \"graduated filtering\" that outperforms binary filtering by +2.48pp MMLU and +2.70pp HellaSwag.\n\n## 2. Strengths\n\n- **Well-defined research question.** The shift from binary detection to ordinal depth estimation is a genuine reframing. Asking \"how many recursive generations deep is this text?\" rather than \"is this human or machine?\" is a meaningful conceptual advance that opens a new axis for data curation research.\n\n- **K* as a controllable operating point, not a ceiling.** The decoding ablation (greedy K*=1, standard K*=2, high-temp K*=3) and the scale ablation (7B K*>=3) together constitute the paper's strongest novelty claim. Demonstrating two independent causal pathways that modulate K* strengthens the argument that K* captures channel properties rather than classifier artifacts.\n\n- **Thorough empirical coverage for a short paper.** Four model configurations, decoding ablation, base vs. instruct comparison, retrain-chain ecological validity, cross-model transfer, LLM zero-shot baseline, binary detector baseline, learned vs. hand-crafted feature comparison, Common Crawl validation, and dose-response analysis. The breadth is commendable.\n\n- **Fair comparison design for C3.** The binary-ours baseline (same 15D features, same LightGBM, only the binary/ordinal decision changes) isolates the contribution of ordinal depth signal from feature engineering advantages. This is methodologically sound.\n\n- **Cross-model transfer result is important.** Pythia-to-OLMo 91% retention and 85% hand-crafted vs. 62% frozen embedding transfer rates address a critical concern about model self-familiarity artifacts and support practical deployment.\n\n- **Retrain-chain validation.** Showing K* is identical and AUC differs by <2pp between prompt-chain and retrain-chain directly addresses the most natural ecological validity concern.\n\n## 3. Weaknesses\n\n- **The DPI invocation is standard, not novel.** The paper frames the \"iterated lossy channel + DPI guarantees finite K*\" as a theoretical contribution, but this is a straightforward application of a textbook result. Any Markov chain with a non-invertible channel has monotonically decreasing mutual information. The theoretical contribution is the operationalization (measuring K*), not the existence proof. The paper sometimes overstates the theoretical depth, e.g., calling K* \"a fundamental information-theoretic quantity\" when what is measured is an empirical, feature-dependent, threshold-dependent proxy.\n\n- **K*=2 yields only a 3-class signal, and the practical utility is narrow.** The graduated filtering reduces to: keep human at weight 1, discount gen-1 at alpha=0.5, discard gen-2+. This is a single additional decision boundary beyond binary. While the +2.48pp improvement is statistically significant, the mechanism is essentially \"don't throw away gen-1 data.\" A simpler framing—\"soft-threshold binary filtering\"—might achieve similar results without the depth estimation machinery.\n\n- **Missing related work in several areas:**\n  - **Watermarking and data provenance:** Kirchenbauer et al. (2023) is cited in the earlier draft's related work but absent from the current version. Watermarking provides an alternative (complementary) approach to depth tracking when the generating model is cooperative. This omission weakens the positioning.\n  - **Membership inference attacks:** The connection between depth estimation and membership inference (e.g., Min-K%++, LOSS attack) is not discussed. These methods also use distributional statistics to infer properties of text origin.\n  - **Iterative self-refinement literature:** Work on LLM self-refinement (Madaan et al., 2023, \"Self-Refine\") and constitutional AI involves recursive generation but for quality improvement. Discussing why depth estimation is different when recursive generation is intentionally lossy vs. intentionally improving would strengthen the framing.\n  - **LLM-as-judge for quality estimation:** The paper tests GPT-4o and Claude for zero-shot depth estimation but does not discuss the broader LLM-as-judge literature (Zheng et al., 2023). The failure mode analysis could be deeper.\n  - **Schaeffer et al. (2025), \"Position: Model Collapse Does Not Mean What You Think\":** The literature map identifies this as framing-critical (8 definitions of collapse in 3 families), but it does not appear in the paper. Anchoring K* within their taxonomy (Family B: distributions deforming) would significantly strengthen positioning.\n  - **Kazdan et al. (2025):** The accumulate vs. replace regime distinction is directly relevant—prompt-chain = replace regime, making K*=2 a conservative bound. Not cited.\n\n- **The paper lists contributions C1 and C3 but skips C2.** The earlier version had a \"degradation ordering\" claim (C2: features collapse in consistent order, Kendall tau >= 0.84). The current version mentions feature ordering consistency (Spearman rho >= 0.878) in passing but does not elevate it as a contribution. This creates a confusing gap in the numbering (C1, C3) and leaves implicit a result that deserves explicit discussion—either as a contribution or as a deliberate omission with explanation.\n\n- **Comparison with Drayson et al. (2025) needs more depth.** The paper acknowledges Drayson as the closest prior work but the comparison is surface-level. Key questions unanswered: (1) How does the graduated filtering's alpha-weighting compare to Drayson's SIR with bias term b? (2) Is the improvement primarily from having 3 classes vs. 2, or from the specific feature set? The binary-ours baseline partially addresses this, but the binary-Drayson baseline implementation details are not given—was it their exact method or a reimplementation?\n\n- **Statistical concerns with 5-seed t-tests.** Paired t-tests with n=5 have very low power and are sensitive to normality assumptions. The p-values (0.004-0.013) are surprisingly low for 4 degrees of freedom. A permutation test or bootstrap test would be more appropriate. The standard deviations are also suspiciously low (0.20-0.33 pp across seeds), raising questions about whether the 5 seeds are truly independent runs with different random initializations.\n\n- **No OLMo results in the paper despite being mentioned.** The abstract and framing mention \"three model families (Qwen-2.5, Pythia, OLMo)\" but OLMo results appear only in cross-model transfer, not in the main K* characterization tables. This inconsistency should be resolved.\n\n- **Common Crawl validation is weak.** Correlations of rho=-0.288 and rho=-0.342 with no ground truth provide almost no evidentiary value. The paper acknowledges this, but including it risks giving a false sense of external validation.\n\n## 4. Detailed Comments\n\n### Novelty of K*\n\nK* as a concept sits at an interesting junction. The existence of a discrimination boundary is trivially guaranteed by DPI—this is not novel. What IS novel is (a) the proposal to systematically measure it, (b) demonstrating it is surprisingly shallow (K*=2), and (c) showing it is controllable via decoding strategy and scale. The novelty is primarily empirical and operational, not theoretical. The paper would benefit from more explicitly owning this: \"Our contribution is not the existence of K* but its first systematic measurement and the discovery that it is shallow yet controllable.\"\n\n### Iterated Lossy Channel Framing\n\nThe framing itself is not new—recursive generation as a Markov chain with information loss has been discussed in the model collapse literature (Shumailov et al. 2024, Alemohammad et al. 2024). The paper's specific contribution is connecting this framing to a practical, measurable quantity (K*) rather than to macroscopic collapse phenomena. This distinction could be made more crisply.\n\n### Boundary Between Depth Estimation and Collapse Detection\n\nThe paper argues it provides \"detection tools\" complementary to the collapse literature, but the boundary is thinner than presented. Measuring K* IS measuring when collapse-like convergence renders generations indistinguishable. The paper should more directly engage with Schaeffer et al.'s (2025) taxonomy to clarify that K* measures discriminability saturation under distribution deformation (their Family B), not population risk divergence (Family A).\n\n### The Missing C2\n\nThe decisions.yaml reveals an extensive deliberation about C2 (degradation ordering). The final paper embeds ordering results within C1 but does not explain the C1/C3 numbering gap. For reader clarity, either renumber to C1/C2 or explicitly note that the ordering is a subcomponent of C1 rather than a standalone claim.\n\n### Significance of K*=2\n\nK*=2 is simultaneously the paper's most interesting and most limiting finding. Interesting because it means the recursive degradation signal vanishes remarkably fast. Limiting because a 3-class system provides minimal granularity. The paper's best defense—that K* is not a ceiling but rises with scale and decoding entropy—is well-executed. However, the practical implication is that for current-generation 1.5B models, the depth estimation framework reduces to \"human / probably-gen-1 / probably-gen-2+,\" which is close to binary with a soft middle category.\n\n### Graduated Filtering: Simple or Meaningful?\n\nThe graduated filtering mechanism (Eq. 3) is extremely simple: assign weight 1/alpha/0 to three predicted classes. The conceptual contribution is the idea of treating gen-1 as partially valuable rather than discarding it. This could arguably be achieved without depth estimation—e.g., by using binary detector confidence as a soft weight. The paper tests binary detector scores as depth proxies (Table 8) and shows they don't work well, but doesn't test them as soft filtering weights (i.e., using DivEye confidence directly as w(x) rather than for depth estimation). This missing comparison leaves an alternative explanation open.\n\n### Comparison with Drayson et al. (2025)\n\nFrom the literature map, Drayson's SIR uses weights w_j = (1-q(x_j))^b where q(x) is binary detection probability and b>=1 is a bias term. This is ALSO a soft weighting scheme—it doesn't hard-threshold at binary. The crucial question is whether graduated filtering's improvement over binary-Drayson (+2.20pp) comes from the ordinal signal or from the specific alpha=0.5 weighting scheme being better calibrated than SIR's (1-q)^b. Without matching the weighting families, this comparison is not fully controlled.\n\n### Broader Impact and New Research Directions\n\nThe paper opens several interesting directions: (1) K* as a function of model scale suggests a \"depth estimation arms race\" as models grow; (2) the connection between K* and decoding strategy has implications for watermarking (higher-entropy decoding preserves more depth signal); (3) graduated filtering could generalize to continuous depth-weighted curation. These are genuinely interesting but mostly implicit in the current draft.\n\n### Writing Quality\n\nGenerally clear and well-organized. The experimental coverage is comprehensive for the page count. The tables are informative. Main writing issues: (1) the C1/C3 numbering gap is confusing; (2) the theoretical framing oversells the DPI contribution; (3) the limitations section is too brief given the number of caveats.\n\n## 5. Questions for Authors\n\n1. **On the alpha-weighting vs. SIR comparison:** Drayson et al.'s SIR also uses soft weights (not hard binary thresholds). Can you provide a controlled comparison where the only variable is ordinal-vs-binary signal, holding the weighting family constant? For example, compare alpha-weighting with 3-class ordinal prediction vs. alpha-weighting with binary confidence as the weight.\n\n2. **On the 5-seed significance tests:** With only 5 seeds (4 degrees of freedom), the reported p-values of 0.004 seem remarkably low. Can you provide the individual seed results so reviewers can verify the computation? Would you consider a permutation test as a more robust alternative?\n\n3. **On K* at larger scales:** You show K*>=3 at 7B. Do you have any evidence (even preliminary) for models at 13B+ or 70B? The trend of K* increasing with scale is the most practically important prediction for real-world deployment, where contamination is dominated by frontier models.\n\n4. **On the missing watermarking discussion:** If text is watermarked (e.g., Kirchenbauer et al. 2023), the depth estimation problem becomes trivially solvable by watermark propagation tracking. How does your framework complement or interact with watermarking-based provenance? Is K* relevant only for unwatermarked text?\n\n5. **On the feature set's claim of being \"model-agnostic\":** The surprisal features require a reference model to compute token surprisal. Which model is used for surprisal computation? If it's the same model that generated the text, the 85% cross-model transfer claim needs careful qualification. If it's a fixed reference model, how sensitive are results to the choice of reference?\n\n## 6. Score\n\n**Score: 4 (Weak Accept)**\n\nThe paper identifies a genuinely interesting research question (ordinal depth estimation of recursive synthetic text) and provides thorough empirical characterization across multiple axes. The K* controllability result (greedy->standard->high-temp gradient) is the strongest novelty element. However, the theoretical contribution is overstated (DPI application is standard), the practical utility is constrained by K*=2 yielding only 3 classes, the related work has notable gaps (watermarking, self-refinement, Schaeffer taxonomy), the graduated filtering mechanism is extremely simple, and the comparison with Drayson et al. needs tightening. The paper is above average in thoroughness but the novelty is primarily empirical-operational rather than conceptual or methodological.\n\n## 7. Confidence\n\n**Confidence: 4 (High)**\n\nI am familiar with the synthetic text detection, model collapse, and data curation literatures. I have carefully read the full paper and supporting experimental documentation. My main uncertainty is around the practical significance of K*=2 at larger model scales, where I have less direct experience with depth estimation experiments.\n",
  "project": "gen-depth-contamination",
  "tier": "best",
  "dream_id": "dream_20260513T080728",
  "overall_score": "Weak Accept (4/6)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8106ebd6-0467-4a67-a20e-38127719c6ef",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazHCHtAL9bZ2x9zEVAaq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ae9e411-aafe-4e3d-adba-247d638b2484",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Xf7njGgTP7T8rEw8DYao5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 70062,
      "output_tokens": 3698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 688
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3698,
          "cache_read_input_tokens": 70062,
          "cache_creation_input_tokens": 688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 688,
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

_source line 62 · 2026-05-13T08:51:05.119Z_

<details><summary>↩ Tool result · `toolu_01PLYuzbQh5VbfyM6zZMC1Wy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/best/review_report.md\", \"dream_id\": \"dream_20260513T080728\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ae9e411-aafe-4e3d-adba-247d638b2484",
  "isSidechain": true,
  "promptId": "836b3bd8-05f8-4326-b99e-8ef10de54d0a",
  "agentId": "afdff64cf4a9a2f1e",
  "type": "user",
  "uuid": "1ce23f0f-869d-4889-90a2-8bb17fb15fc2",
  "sourceToolAssistantUUID": "6ae9e411-aafe-4e3d-adba-247d638b2484",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-13T08:51:16.915Z_

Review submitted. Here is a summary of the key findings:

**Score: 4/6 (Weak Accept), Confidence: 4/5 (High)**

**What works well:**
- The shift from binary detection to ordinal depth estimation is a genuine reframing that opens new research directions
- The K* controllability gradient (greedy K*=1 -> standard K*=2 -> high-temp K*=3) is the paper's strongest novelty — two independent causal pathways (scale, decoding entropy) demonstrate K* captures channel properties, not classifier artifacts
- Comprehensive experimental coverage: 4 model configs, decoding ablation, retrain-chain validation, cross-model transfer (91% retention), fair binary-ours baseline isolating the ordinal signal
- The binary-ours comparison design is methodologically sound

**Main concerns raised:**
1. **DPI application is textbook, not novel** — the contribution is empirical measurement, not theoretical. Paper oversells the information-theoretic framing
2. **K*=2 practical utility is narrow** — graduated filtering reduces to a single soft threshold on gen-1 data, close to "binary with a soft middle category"
3. **Related work gaps** — missing watermarking (Kirchenbauer), self-refinement literature, Schaeffer et al. (2025) taxonomy (framing-critical per own literature map but absent from paper), Kazdan et al. (2025) accumulate/replace regimes, membership inference connections
4. **C1/C3 numbering gap** — C2 (degradation ordering) was demoted but the numbering was not fixed, creating reader confusion
5. **Drayson comparison not fully controlled** — Drayson's SIR also uses soft weights, so the graduated vs. binary-Drayson comparison doesn't isolate ordinal signal from weighting scheme differences
6. **Statistical concern** — 5-seed paired t-tests (4 df) yielding p=0.004 is surprisingly strong; permutation tests would be more appropriate
7. **Surprisal features require a reference model** — the "model-agnostic" claim needs qualification depending on which model computes surprisal

The review report was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260513T080728/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ce23f0f-869d-4889-90a2-8bb17fb15fc2",
  "isSidechain": true,
  "agentId": "afdff64cf4a9a2f1e",
  "requestId": "req_011CazHKwSZscgUxf4FRaLao",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9afa6844-0e11-4581-8f21-75b9241cff85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "a5ad6c09-3f62-4a50-ac24-2966b7e8297b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rs6kKMbN18487mw5tfkha",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3828,
      "cache_read_input_tokens": 70750,
      "output_tokens": 564,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3828
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 564,
          "cache_read_input_tokens": 70750,
          "cache_creation_input_tokens": 3828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3828,
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
