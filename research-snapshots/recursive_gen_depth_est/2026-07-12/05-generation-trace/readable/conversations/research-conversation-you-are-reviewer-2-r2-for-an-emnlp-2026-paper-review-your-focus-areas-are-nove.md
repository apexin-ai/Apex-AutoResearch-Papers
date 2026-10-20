# Research conversation: You are Reviewer 2 (R2) for an EMNLP 2026 paper review. Your focus areas are **Novelty** and **Related Work**. ## Venue 

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a4d26d750abf8bf19.jsonl`
- **Structured JSON:** [`9548bb981d37390c109c.json`](../../sessions/95/9548bb981d37390c109c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-14T14:51:40.157Z_

You are Reviewer 2 (R2) for an EMNLP 2026 paper review. Your focus areas are **Novelty** and **Related Work**. 

## Venue Standards
EMNLP 2026 uses ACL Rolling Review (ARR). Score scale:
- 5 = Consider for Award (top 2.5%)
- 4 = Conference (accept to main conference)
- 3.5 = Borderline Conference
- 3 = Findings
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle
- 1.5 = Resubmit after next cycle
- 1 = Do not resubmit

Dimensions: Soundness (1-5), Excitement (1-5), Overall Assessment (1-5, with half-points allowed).

## Paper Summary
**Title:** "Ordinal Depth Estimation of Recursive Generation: A Depth Degradation Atlas for Model Collapse Characterization"

This paper formalizes ordinal generation depth estimation — predicting how many recursive generation cycles (d ∈ {0,1,...,5}) a text has undergone. Three contributions:
1. **DCOL** (Depth Contrastive Ordinal Learning): DeBERTa-v3-large + N-pair contrastive loss with learnable non-uniform margins, surprisal-augmented anchor selection, and strategy conditioning. Achieves 57.1% 6-class acc (chance=16.7%), 82.3% 4-class acc, outperforming best baseline (CORAL) by +3.3pp.
2. **Depth Degradation Atlas**: Systematic characterization across 3 models (Pythia-1.4B, OLMo-1B, GPT-2 XL) × 3 decoding strategies × 6 depths. Key finding: Effective Discriminable Depth (EDD) ≈ 3. Surprisal variance is the most stable depth signal (monotonicity 0.847).
3. **Depth-graduated curation proof-of-concept**: Graduated weighting reduces PPL by 3.1% over binary filtering (p=0.038).

## Paper Details (from the 10-page PDF)

### Related Work (Section 2):
- **Model collapse and recursive generation**: Cites Shumailov et al. (2024, Nature) on distribution collapse from iterative self-training. Cites Drayson et al. (EMNLP 2025) on non-monotonic degradation patterns. Claims these assume depth is known; this paper estimates it from text.
- **Synthetic text detection**: Mentions LOKI, DivEye, Binoculars as binary detectors. Mentions EditLens for single-pass AI editing. Claims extension from binary to ordinal.
- **Ordinal classification**: Cites CORAL (Cao et al., 2020) for ordinal regression. Cites CLOC (CVPR 2025) for contrastive ordinal learning in age estimation. Claims adaptation to text domain with three modifications.
- Related work section is brief (~0.5 page), only 3 references in bibliography.

### Method (Section 3):
- Problem formulation: d ∈ {0,...,K}, non-uniform inter-depth distances.
- Benchmark: 3 models × 3 strategies × 6 depths, ~1200 samples/depth/strategy.
- 19 statistical features across surprisal, perplexity, lexical, distribution categories.
- DCOL: DeBERTa-v3-large + N-pair contrastive loss with learnable margins + surprisal anchors + strategy conditioning. Ordinal regression head with cumulative probabilities.

### Key Results:
- DCOL: 57.1% 6-class, 82.3% 4-class. Best baseline CORAL: 53.8% 6-class. Δ = +3.3pp.
- DeBERTa E2E (CE loss, no features) achieves 55.3% 6-class — actually outperforms CORAL.
- Ablation shows each DCOL component contributes 0.9–2.4pp. Without all three modifications, drops to 53.1% (below CORAL).
- EDD ≈ 3 across models/strategies.
- Cross-model generalization: 47.0% mean (6-class), OLMo rotation fails 0.45 gate.
- Cross-strategy: 52.0% mean, easier than cross-model.
- Downstream curation: 3.1% PPL reduction (p=0.038).
- 7B cross-scale: zero-shot degrades ~21pp, fine-tuning recovers.
- Wild data: moderate correlations (ρ ≤ 0.34).

### Discussion and Limitations (Sections 5-6):
- Frames EDD as scientific contribution to model collapse community.
- "Feature handoff" concept: surprisal variance dominates within EDD, Zipf α beyond.
- Explicit limitations: cross-model gap, effective granularity limited to 4 classes, scale transfer gap, controlled-vs-wild gap, moderate DCOL advantage.

## Your Task
Write a detailed R2 review focusing on:
1. **Novelty assessment** — Is the problem formulation genuinely new? Is the DCOL method sufficiently novel vs. existing contrastive ordinal methods? Is the Atlas a novel contribution?
2. **Related work coverage** — Are important related works missing? Is the positioning accurate? Only 3 references seems very sparse for a top venue paper.
3. **Significance and impact** — Would this paper advance the field? Is EDD a useful concept? Will the community adopt the Atlas?
4. **Framing and claims** — Are claims well-calibrated to the evidence? Is the paper over-claiming or appropriately scoped?
5. **Writing quality and presentation**

Structure your review as:
```
## R2 Review: Novelty & Related Work

### Summary
[2-3 sentences]

### Strengths (Novelty)
[Bulleted]

### Strengths (Presentation & Framing)
[Bulleted]

### Weaknesses (Novelty)
[Bulleted, with severity: major/minor]

### Weaknesses (Related Work)
[Bulleted, with severity: major/minor]

### Weaknesses (Claims & Framing)
[Bulleted, with severity: major/minor]

### Questions for Authors
[Numbered]

### Preliminary Scores
- Soundness: X/5
- Excitement: X/5
- Overall: X/5
- Confidence: X/5
```

Be rigorous but fair. This is for EMNLP — a top NLP venue. Consider whether this paper makes a sufficient contribution above the acceptance threshold. The related work section having only 3 references is a notable concern — assess whether important prior work is missing. Do NOT mention any tier information (best/median/worst). Evaluate the paper purely on its own merits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "f0ca34ab-bd20-4d07-a274-7546548a3428",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T14:51:40.160Z_

```json
{
  "parentUuid": "f0ca34ab-bd20-4d07-a274-7546548a3428",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
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
  "uuid": "69f8a25d-c275-4be4-91fb-83ddeb97cf33",
  "timestamp": "2026-05-14T14:51:40.160Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T14:51:45.113Z_



I'll start by reading the project files to get full context on the paper before writing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69f8a25d-c275-4be4-91fb-83ddeb97cf33",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2edgEyFFmpERqHV2EUN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84af935a-36da-463e-8522-2594de4a670d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JAcE8VbyCcJRvLHqQuyr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7515,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7515,
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

_source line 4 · 2026-05-14T14:51:45.926Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01C3B3w7zZ157u1vQesazpJT`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84af935a-36da-463e-8522-2594de4a670d",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2edgEyFFmpERqHV2EUN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ac18759-79b9-4e9f-ad70-7595b21d67bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JAcE8VbyCcJRvLHqQuyr2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7515,
      "cache_read_input_tokens": 8251,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7515
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 7515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7515,
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

_source line 5 · 2026-05-14T14:51:45.934Z_

<details><summary>↩ Tool result · `toolu_01C3B3w7zZ157u1vQesazpJT`</summary>

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
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ac18759-79b9-4e9f-ad70-7595b21d67bf",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "9c6d66bd-a775-4f63-8d41-9f6dbcb56044",
  "sourceToolAssistantUUID": "6ac18759-79b9-4e9f-ad70-7595b21d67bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T14:51:48.338Z_



Let me read the key project files to get full context before writing the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c6d66bd-a775-4f63-8d41-9f6dbcb56044",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2ee6TzU6iEg8i3MtGrn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e450ee34-9b13-4334-aa14-486eb686960e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSDCjbJmqBLfRbyZrD5Exk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1860,
      "cache_read_input_tokens": 15766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1860,
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

_source line 7 · 2026-05-14T14:51:49.847Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RLF6JDL4Qw7NXQyrbr9Zq7`</summary>

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
  "parentUuid": "e450ee34-9b13-4334-aa14-486eb686960e",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2ee6TzU6iEg8i3MtGrn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ede82556-a97c-4dd9-8494-71fffcfd40a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSDCjbJmqBLfRbyZrD5Exk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1860,
      "cache_read_input_tokens": 15766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1860,
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

_source line 8 · 2026-05-14T14:51:49.863Z_

<details><summary>↩ Tool result · `toolu_01RLF6JDL4Qw7NXQyrbr9Zq7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| cross_model_gpt2xl_001 | — | — | — | — |\\n\\n## 待处理\\n- pythia_topk50_001（准备中）\\n- pythia_temp09_001（准备中）\\n\\n## 近期结论\\n- **cross_model_olmo_001** (negative): —\\n- **mvp_pipeline_pythia_002** (success): —\\n- **mvp_pipeline_qwen_base_004** (killed): —\\n\\n## 趋势\\n成功 1 / 负向 1 / 失败 0 / 共 10\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n- mvp_pipeline_001: 已被终止 — unknown\\n- mvp_pipeline_002: 已被终止 — unknown\\n- mvp_pipeline_003: 已被终止 — unknown\\n- mvp_pipeline_004: 已被终止 — unknown\\n- mvp_pipeline_base_002: 已被终止 — unknown\\n- mvp_pipeline_base_003: 已被终止 — unknown\\n- mvp_pipeline_pythia_001: 已被终止 — unknown\\n- mvp_pipeline_qwen_base_004: 已被终止 — unknown\\n\", \"total_chars\": 782, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ede82556-a97c-4dd9-8494-71fffcfd40a7",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "ad0d39cf-3077-4792-8cfa-3a3883e05cfb",
  "sourceToolAssistantUUID": "ede82556-a97c-4dd9-8494-71fffcfd40a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T14:51:50.330Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DsKBRhYmR53fafBYi5xQuo`</summary>

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
  "parentUuid": "ad0d39cf-3077-4792-8cfa-3a3883e05cfb",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2ee6TzU6iEg8i3MtGrn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21e90bb7-9ac3-426d-98bf-ebce1e174ce9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSDCjbJmqBLfRbyZrD5Exk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1860,
      "cache_read_input_tokens": 15766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1860,
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

_source line 10 · 2026-05-14T14:51:50.345Z_

<details><summary>↩ Tool result · `toolu_01DsKBRhYmR53fafBYi5xQuo`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'recursive_gen_depth_est'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21e90bb7-9ac3-426d-98bf-ebce1e174ce9",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "db3561c1-3bc2-496f-a685-91d3d1b97f4c",
  "sourceToolAssistantUUID": "21e90bb7-9ac3-426d-98bf-ebce1e174ce9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T14:51:51.273Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WNbxQkKGs61dWTg3MdWStj`</summary>

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
  "parentUuid": "db3561c1-3bc2-496f-a685-91d3d1b97f4c",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2ee6TzU6iEg8i3MtGrn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a113b7b-8249-4595-9c72-e795e6ef7cea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSDCjbJmqBLfRbyZrD5Exk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1860,
      "cache_read_input_tokens": 15766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1860,
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

_source line 12 · 2026-05-14T14:51:51.284Z_

<details><summary>↩ Tool result · `toolu_01WNbxQkKGs61dWTg3MdWStj`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'recursive_gen_depth_est'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a113b7b-8249-4595-9c72-e795e6ef7cea",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "a90e174a-f2cb-4173-a267-b508492545dc",
  "sourceToolAssistantUUID": "1a113b7b-8249-4595-9c72-e795e6ef7cea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T14:51:51.440Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LhYmnLjefWxjfCLqnD3q74`</summary>

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
  "parentUuid": "a90e174a-f2cb-4173-a267-b508492545dc",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2ee6TzU6iEg8i3MtGrn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb47cfa2-4f8e-42dd-b656-a04ca0536343",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSDCjbJmqBLfRbyZrD5Exk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1860,
      "cache_read_input_tokens": 15766,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1860
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 404,
          "cache_read_input_tokens": 15766,
          "cache_creation_input_tokens": 1860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1860,
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

_source line 14 · 2026-05-14T14:51:51.450Z_

<details><summary>↩ Tool result · `toolu_01LhYmnLjefWxjfCLqnD3q74`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper_framing.md\", \"content\": \"# Paper Framing — recursive_gen_depth_est\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\\n- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)\\n- EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit\\n\\n## Core Claims (3 条)\\n\\n1. **Ordinal depth estimation is feasible and accurate**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features and contrastive ordinal learning. On our benchmark, DCOL achieves significantly higher accuracy than binary detection baselines and standard classification approaches. (MVP signal: 78.2% 4-class accuracy with simple RF on Pythia chain)\\n\\n2. **Depth Degradation Atlas — systematic characterization of recursive collapse**: We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) surprisal variance as the strongest depth signal, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), and (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable. This atlas spans 3 model families × 3 decoding strategies.\\n\\n3. **Depth-graduated curation outperforms binary filtering**: Using predicted depth as a continuous quality proxy enables more nuanced data curation — graduated weighting by depth retains high-quality shallow-generation content while down-weighting deeply recursive text, outperforming binary real/synthetic filtering on downstream task quality. (Proof-of-concept scope, ~1 page)\\n\\n## Story Spine\\n\\n- **Problem**: Web-scraped training corpora increasingly contain multi-generational synthetic content from uncontrolled model→data→model feedback loops. Existing detectors answer \\\"is this synthetic?\\\" but not \\\"how many recursive cycles has this undergone?\\\" — a critical distinction since 1st-gen synthetic data can improve training while deeply recursive text drives distribution collapse.\\n\\n- **Existing approaches & gaps**: Binary detectors (LOKI, DivEye, Binoculars) classify real vs. synthetic but discard ordinal depth information. EditLens estimates single-pass AI editing extent but not recursive depth. Model collapse studies (Drayson et al. EMNLP 2025; Shumailov et al. Nature 2024) characterize degradation patterns but assume depth is known a priori — no method estimates depth from text alone.\\n\\n- **Our framing**: We formalize ordinal generation depth estimation as a new task, construct a multi-generational benchmark (3 models × 3 strategies × 5+ depths), and propose DCOL — a contrastive ordinal learning method with learnable non-uniform margins that captures the actual geometry of recursive degradation. Crucially, we don't just build a classifier — we provide a Depth Degradation Atlas mapping how features evolve across depths, models, and strategies, including the EDD boundary where discrimination saturates.\\n\\n- **Headline result template**: \\\"On our multi-generational benchmark spanning 3 model families and 3 decoding strategies, our method achieves X% ordinal depth estimation accuracy (chance=25% for 4-class), with cross-model generalization accuracy of Y%, while the best binary detection baseline repurposed for depth estimation achieves only Z%.\\\"\\n- **Note**: 4-class (depth 0-3) is the confirmed setting. 6-class (depth 0-5) pending plan_011 results.\\n\\n## DCOL Contingency\\nIf DCOL improvement over RF/feature-based methods is < 5pp:\\n- Claim 2 (Atlas) becomes the PRIMARY contribution\\n- DCOL is repositioned as \\\"one strong method within the depth estimation framework\\\"\\n- Story shifts from \\\"method paper\\\" to \\\"task formalization + systematic empirical study + practical framework\\\"\\n- This is still a strong paper — the MVP RF already achieves 78.2%, the Atlas and EDD are novel regardless of method\\n\\n## Venue Fit Risks\\n\\n- **Novelty concern**: DCOL is adapted from CLOC (CVPR 2025). Mitigation: novelty emphasis on problem formalization + Atlas + EDD metric; DCOL is framed as a strong method within the framework, not the sole contribution. Three text-specific modifications (strategy-aware margins, surprisal-augmented anchors, non-uniform learned margins) differentiate from direct CLOC transfer.\\n- **\\\"Just an empirical study\\\" risk**: Mitigation: method (DCOL) + Atlas (scientific contribution) + curation (practical application) = three-line contribution with clear primary/secondary hierarchy.\\n- **Controlled vs wild gap**: Mitigation: honest scoping — controlled setting is primary, wild-data calibration is probed, ecological transfer is future work.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. \\\"EDD might be very low (depth 2-3), making the task trivial beyond shallow depths\\\" → Report EDD transparently; argue even low EDD is scientifically valuable (determines the boundary) and practically sufficient (shallow vs deep is the actionable distinction for curation)\\n2. \\\"Why ordinal and not just binary?\\\" → MVP already shows: d0v1 AUC=0.998 vs d1v2=0.861 vs d2v3=0.801 — ordinal structure captures monotonically decreasing but still significant discrimination at all adjacent pairs\\n3. \\\"Generalization to unseen models/strategies?\\\" → Leave-one-out experiments are core evaluation\\n4. \\\"Non-monotonic degradation (Drayson et al.)?\\\" → Learnable margins as soft inductive bias; ablation comparing DCOL vs fixed-margin CORAL vs CE loss\\n\", \"total_chars\": 5471, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb47cfa2-4f8e-42dd-b656-a04ca0536343",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "8ce964e2-d768-4a4a-bac2-5f44062e1e73",
  "sourceToolAssistantUUID": "eb47cfa2-4f8e-42dd-b656-a04ca0536343",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T14:51:54.417Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0168MKwK1q9wVeaKRziTzetp`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ce964e2-d768-4a4a-bac2-5f44062e1e73",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2eeW6oPurte2BHA8544",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37073328-c30d-4d3c-b535-7c5158e44809",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EE3mF9AeNRDPQ7qqu4QpuG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2787,
      "cache_read_input_tokens": 17626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2787,
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

_source line 16 · 2026-05-14T14:51:54.429Z_

<details><summary>↩ Tool result · `toolu_0168MKwK1q9wVeaKRziTzetp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/memory.md\", \"content\": \"# Memory — recursive_gen_depth_est\\n\\n## 关键决策\\n\\n### 模型选择：Pythia-1.4B 为 MVP 模型（2026-05-14）\\nQwen2.5 系列预训练代码占比太高 → 换用 Pythia-1.4B（The Pile, 代码仅 3.3%）。\\n\\n### Research Phase 模型架构确认（2026-05-14）\\n\\n| 模型 | model_type | 参数量 | LoRA targets | 路径 | 注意事项 |\\n|------|-----------|--------|-------------|------|---------|\\n| Pythia-1.4B | gpt_neox | 1.41B | `query_key_value` | `/root/autodl-tmp/models/pythia-1.4b/` | pad_token 已自带 |\\n| OLMo-1B | olmo | 1.18B | `q_proj,v_proj` | `/root/autodl-tmp/models/olmo-1b/` | 用 `allenai/OLMo-1B-hf`（非 OLMo-1B，后者需 hf_olmo 自定义代码）。BOS=None, PAD=1 |\\n| GPT-2 XL | gpt2 | 1.56B | `c_attn,c_proj` | `/root/autodl-tmp/models/gpt2-xl/` | 用 Conv1D 不是 nn.Linear，PEFT 自动处理。pad_token=None 需设为 eos_token |\\n\\n### 文本长度 confound 修复（Reviewer 2026-05-14）\\nmax_new_tokens=512，特征提取统一截断到 498 tokens。\\n\\n### GPU 硬件（2026-05-14）\\ngpu-6000pro-2: 2× NVIDIA RTX PRO 6000 Blackwell 98GB。\\n\\n## MVP 结果（2026-05-14, mvp_pipeline_pythia_002, SUCCESS）\\n\\n### 核心发现\\n- **4-class acc=78.2%** (chance=25%), 过滤代码后 81.6%（信号非域混淆）\\n- **3-class acc=70.8%** (d1/d2/d3 only, chance=33.3%)——去掉 depth-0 \\\"easy win\\\" 后信号依然强\\n- d0v1 AUC=0.998, d1v2=0.861, d2v3=0.801\\n- 3-class: d1v2=0.854, d2v3=0.793\\n- **最重要特征**: var_surprisal > p90_ppl > mean_ppl\\n- 训练 loss: 2.241→1.389→1.025（模式坍缩信号）\\n- 代码污染（宽标准）: d0=0.5%, d1=17.8%, d2=22.4%, d3=27.4%\\n- Stratified split 稳定: 78.2% → 78.1% (-0.1pp)\\n\\n### 代码过滤标准差异\\n- 窄标准(4 patterns): d1=7.4%, d2=11.8%, d3=15.3%\\n- 宽标准(18 patterns): d1=17.8%, d2=22.4%, d3=27.4%\\n- 差异来自 def/function/var/div/php/SQL 等额外 pattern\\n\\n## 经验教训\\n\\n- 代码占比高的模型不能用于递归生成实验\\n- 域一致性检查是必做步骤\\n- 控制实验验证信号真实性：过滤代码后 acc 提升 → 域混淆排除\\n- AutoDL: HF 下载慢用 ModelScope CDN\\n- Worker 汇报需验证：读 log 确认实际执行\\n- OLMo-1B 必须用 HF 格式（allenai/OLMo-1B-hf），原始格式需自定义代码\\n- GPT-2 XL 的 attention 用 Conv1D，LoRA target 是 c_attn/c_proj\\n\", \"total_chars\": 1747, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37073328-c30d-4d3c-b535-7c5158e44809",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "3d79760f-be03-4c59-8e98-9822758870d5",
  "sourceToolAssistantUUID": "37073328-c30d-4d3c-b535-7c5158e44809",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T14:51:55.356Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SA2w5y4AnUqji1d1f55fdV`</summary>

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
  "parentUuid": "3d79760f-be03-4c59-8e98-9822758870d5",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2eeW6oPurte2BHA8544",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "450abec3-bd86-4a9d-9258-63acdf2f74b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EE3mF9AeNRDPQ7qqu4QpuG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2787,
      "cache_read_input_tokens": 17626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2787,
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

_source line 18 · 2026-05-14T14:51:55.365Z_

<details><summary>↩ Tool result · `toolu_01SA2w5y4AnUqji1d1f55fdV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/ROADMAP.md\", \"content\": \"# recursive_gen_depth_est — Research Dashboard\\n\\n> 最后更新: 2026-05-14 14:06 UTC | 更新原因: MVP PASS, 进入 research phase, framing + plan 完成, Dream 运行中\\n\\n## 核心方向\\n递归生成深度估计：给定文本，预测其经历了多少轮 model→data→model 递归训练循环。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-14 通过，4-class acc 78.2%）\\n- **核心信号**: surprisal 方差 > perplexity P90 > mean perplexity 是最强深度特征\\n- **覆盖率**: 1/3 模型 (Pythia), 1/3 策略 (nucleus), 4/6 深度 (0-3)\\n- **基础设施**: westb-52439 (2× NVIDIA RTX PRO 6000 Blackwell 98GB)\\n- **Dream**: dream_20260514T140607 运行中，等待回调再批准 P0 实验\\n\\n## Claims (详见 paper_framing.md)\\n1. Ordinal depth estimation feasible + accurate (DCOL method)\\n2. Depth Degradation Atlas (systematic characterization + EDD)\\n3. Depth-graduated curation > binary filtering (proof-of-concept)\\n\\n## 实验计划 (详见 experiment_plan.yaml)\\n- **P0** (45 GPU·h): 3 模型链 (Pythia/OLMo/GPT-2 XL) × 3 策略 + DCOL 训练 + leave-one-model-out + Atlas\\n- **P1** (38 GPU·h): leave-one-strategy-out + DeBERTa E2E + baseline battery + ablations + depth 5 + granularity\\n- **P2** (45 GPU·h): downstream curation + 7B probe + wild calibration\\n\\n## 近期任务\\n- [x] MVP PASS (Pythia-1.4B, 78.2% acc, 0.861 d1v2 AUC)\\n- [x] paper_framing.md 完成\\n- [x] experiment_plan.yaml 完成\\n- [ ] Dream 模拟完成 → 审查行动项 → 批准 P0 ← 等待中\\n- [ ] P0 实验启动（OLMo-1B + GPT-2 XL 递归链 + Pythia 补充策略）\\n\\n## GPU 预算\\n- 本项目分配: westb-52439 cuda:0, cuda:1 (2× Blackwell 98GB)\\n- MVP 消耗: 1.78 GPU·h\\n- P0 预估: 45 GPU·h (~1 day on 2 GPUs)\\n- P0+P1: 83 GPU·h (~2 days)\\n\\n## 教训\\n- Qwen2.5 预训练代码占比过高，LoRA + 无条件生成产出代码 → 换 Pythia (The Pile, 3.3% 代码)\\n- 手动抽查 8 条不够做域一致性判断，需 grep 定量扫描\\n- 指令冲突导致 Agent 来回切换模型 → 统一指令后用 replace_agent_queue 清队列\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D001 | 2026-05-14 | MVP PASS — 递归生成深度可从统计特征高精度区分，进入 research phase | mvp_pipeline_pythia_002 |\\n\\n\\n\", \"total_chars\": 1764, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "450abec3-bd86-4a9d-9258-63acdf2f74b8",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "f945ca1e-f88f-4704-9417-1448dd51e7fb",
  "sourceToolAssistantUUID": "450abec3-bd86-4a9d-9258-63acdf2f74b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T14:51:55.763Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WXa9pP9edW6abLKBk629gW`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f945ca1e-f88f-4704-9417-1448dd51e7fb",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2eeW6oPurte2BHA8544",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03e813fd-afbd-44ce-8b02-3fb5b9c54f34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EE3mF9AeNRDPQ7qqu4QpuG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2787,
      "cache_read_input_tokens": 17626,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2787
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 17626,
          "cache_creation_input_tokens": 2787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2787,
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

_source line 20 · 2026-05-14T14:51:55.795Z_

<details><summary>↩ Tool result · `toolu_01WXa9pP9edW6abLKBk629gW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/decisions.yaml\", \"content\": \"_next_id: 2\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 14:03 UTC\\n  summary: MVP PASS — 递归生成深度可从统计特征高精度区分，进入 research phase\\n  rationale: Pythia-1.4B 4-depth pipeline 验证核心假设：4-class acc 78.2% (>>40% threshold),\\n    d1v2 AUC 0.861 (>>0.6 threshold)。控制实验排除域混淆（过滤代码后 acc 提升至 81.6%）。Top 特征为 surprisal\\n    variance 和 perplexity percentiles，说明信号来自分布窄化而非内容差异。\\n  related_experiments:\\n  - exp_id: mvp_pipeline_pythia_002\\n    role: primary\\n    result: 4-class acc 78.2%, d1v2 AUC 0.861, content-type control 81.6%\\n  depends_on: []\\n\", \"total_chars\": 517, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03e813fd-afbd-44ce-8b02-3fb5b9c54f34",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "cd83d667-b73b-4b4e-a9e1-16768f38afa2",
  "sourceToolAssistantUUID": "03e813fd-afbd-44ce-8b02-3fb5b9c54f34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-14T14:51:58.871Z_

Now let me look at the artifacts directory for the actual paper or any additional experimental results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd83d667-b73b-4b4e-a9e1-16768f38afa2",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2eepXpMTXRpvztSvuZf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "231d6153-4d6a-45d2-90f0-b75ce07fa35d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5jGK3FbKyAckbQJggk4F7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3306,
      "cache_read_input_tokens": 20413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3306,
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

_source line 22 · 2026-05-14T14:51:59.356Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01R2cF8gcwiVXs1Qco8k9Mmr`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "231d6153-4d6a-45d2-90f0-b75ce07fa35d",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2eepXpMTXRpvztSvuZf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96f35585-9465-45b5-bcf0-e60a6a348b8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5jGK3FbKyAckbQJggk4F7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3306,
      "cache_read_input_tokens": 20413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3306,
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

_source line 23 · 2026-05-14T14:51:59.373Z_

<details><summary>↩ Tool result · `toolu_01R2cF8gcwiVXs1Qco8k9Mmr`</summary>

```text
artifacts/dream_reports/dream_20260514T140607/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260514T140607/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260514T140607/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260514T140607/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T140607/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T140607/best/experiment_data.json
artifacts/dream_reports/dream_20260514T140607/best/paper_framing.md
artifacts/dream_reports/dream_20260514T140607/best/paper.tex
artifacts/dream_reports/dream_20260514T140607/best/paper.aux
artifacts/dream_reports/dream_20260514T140607/best/paper.out
artifacts/dream_reports/dream_20260514T140607/best/paper.pdf
artifacts/dream_reports/dream_20260514T140607/best/paper.log
artifacts/dream_reports/dream_20260514T140607/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T140607/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T140607/median/experiment_data.json
artifacts/dream_reports/dream_20260514T140607/median/paper_framing.md
artifacts/dream_reports/dream_20260514T140607/median/paper.tex
artifacts/dream_reports/dream_20260514T140607/median/paper.aux
artifacts/dream_reports/dream_20260514T140607/median/paper.out
artifacts/dream_reports/dream_20260514T140607/median/paper.pdf
artifacts/dream_reports/dream_20260514T140607/median/paper.log
artifacts/dream_reports/dream_20260514T140607/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T140607/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T140607/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T140607/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T140607/worst/paper.tex
artifacts/dream_reports/dream_20260514T140607/worst/paper.aux
artifacts/dream_reports/dream_20260514T140607/worst/paper.out
artifacts/dream_reports/dream_20260514T140607/worst/paper.pdf
artifacts/dream_reports/dream_20260514T140607/worst/paper.log
artifacts/dream_reports/dream_20260514T140607/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T140607/best/review_context.yaml
artifacts/dream_reports/dream_20260514T140607/logs/orchestrator.log
artifacts/dream_reports/dream_20260514T140607/best/review_report.md
artifacts/dream_reports/dream_20260514T140607/logs/review_best.log
artifacts/dream_reports/dream_20260514T140607/median/review_context.yaml
artifacts/dream_reports/dream_20260514T140607/logs/review_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96f35585-9465-45b5-bcf0-e60a6a348b8b",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "84175d8c-4636-4117-93c8-4dcd746e2562",
  "sourceToolAssistantUUID": "96f35585-9465-45b5-bcf0-e60a6a348b8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T14:52:00.349Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019F7kvwmeA6v73Nj6G8gtyK`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84175d8c-4636-4117-93c8-4dcd746e2562",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2eepXpMTXRpvztSvuZf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "398ee998-1caf-4e35-8beb-94425678ae79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5jGK3FbKyAckbQJggk4F7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3306,
      "cache_read_input_tokens": 20413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3306,
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

_source line 25 · 2026-05-14T14:52:00.416Z_

<details><summary>↩ Tool result · `toolu_019F7kvwmeA6v73Nj6G8gtyK`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'recursive_gen_depth_est'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "398ee998-1caf-4e35-8beb-94425678ae79",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "9caf8c13-1d3d-4743-8e7e-2088f94ff71b",
  "sourceToolAssistantUUID": "398ee998-1caf-4e35-8beb-94425678ae79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T14:52:00.797Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YBjR1c9sTo6Nspx44kSiwz`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9caf8c13-1d3d-4743-8e7e-2088f94ff71b",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2eepXpMTXRpvztSvuZf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78c3f774-573d-45b3-8091-6abe508a1781",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5jGK3FbKyAckbQJggk4F7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3306,
      "cache_read_input_tokens": 20413,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3306
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 305,
          "cache_read_input_tokens": 20413,
          "cache_creation_input_tokens": 3306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3306,
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

_source line 27 · 2026-05-14T14:52:00.808Z_

<details><summary>↩ Tool result · `toolu_01YBjR1c9sTo6Nspx44kSiwz`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'recursive_gen_depth_est'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78c3f774-573d-45b3-8091-6abe508a1781",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "cf25802f-db12-480f-85ed-54d93326a8c8",
  "sourceToolAssistantUUID": "78c3f774-573d-45b3-8091-6abe508a1781",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-14T14:52:04.148Z_

Let me read the median tier paper (which is what I should be reviewing as R2) and check the best tier's review report for context on what R1 may have covered.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf25802f-db12-480f-85ed-54d93326a8c8",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2efC38mRVti5CtNuAVZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20baad9d-5942-439b-a457-e4be983a99ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CYqQF7CEhSfAyZfkNV17yt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1353,
      "cache_read_input_tokens": 23719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1353,
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

_source line 29 · 2026-05-14T14:52:05.129Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Dj1bZ7yJP5MBE9ASWUH4Mj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20baad9d-5942-439b-a457-e4be983a99ef",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2efC38mRVti5CtNuAVZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b9bb1af-6c8f-4402-b91d-a2cedd276840",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CYqQF7CEhSfAyZfkNV17yt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1353,
      "cache_read_input_tokens": 23719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1353,
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

_source line 30 · 2026-05-14T14:52:05.464Z_

<details><summary>↩ Tool result · `toolu_01Dj1bZ7yJP5MBE9ASWUH4Mj`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=2.5cm]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{tabularx}
12	\usepackage{enumitem}
13	\usepackage{hyperref}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	%\usepackage{natbib}
17	
18	\title{Ordinal Depth Estimation of Recursive Generation:\\A Depth Degradation Atlas for Model Collapse Characterization}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	% ============================================================
26	\begin{abstract}
27	Web-scraped corpora increasingly contain multi-generational synthetic text produced by uncontrolled model$\to$data$\to$model feedback loops.
28	Existing detectors answer \emph{whether} text is synthetic but not \emph{how many recursive cycles} it has undergone---a distinction that matters because shallow-generation text can be benign while deeply recursive text drives distribution collapse.
29	We formalize \textbf{ordinal generation depth estimation} as a new task and construct a multi-generational benchmark spanning 3 model families (Pythia-1.4B, OLMo-1B, GPT-2~XL) $\times$ 3 decoding strategies $\times$ 6 depths.
30	We propose \textbf{DCOL} (Depth Contrastive Ordinal Learning), a DeBERTa-based method with learnable non-uniform margins that captures the geometry of recursive degradation.
31	DCOL achieves 57.1\% 6-class accuracy (chance = 16.7\%) and 82.3\% 4-class accuracy, outperforming the best baseline (CORAL) by +3.3 percentage points (pp).
32	Beyond the classifier, we contribute a \textbf{Depth Degradation Atlas}---a systematic characterization of how statistical features evolve across depths, models, and strategies---revealing an \textbf{Effective Discriminable Depth (EDD)} of $\approx$3, beyond which adjacent depths become indistinguishable.
33	Cross-model leave-one-out generalization averages 47.0\% (6-class) with variance across rotations, and a downstream curation proof-of-concept shows that depth-graduated weighting reduces perplexity by 3.1\% over binary filtering ($p=0.038$).
34	We release the benchmark and Atlas to support future work on recursive contamination characterization.
35	\end{abstract}
36	
37	% ============================================================
38	\section{Introduction}
39	\label{sec:intro}
40	
41	The proliferation of large language model (LLM) outputs on the web has created a new challenge for training data curation: \emph{recursive synthetic contamination}.
42	When model-generated text is scraped, used to train new models, and those models generate yet more text, the resulting feedback loop produces multi-generational synthetic content whose quality degrades with each cycle~\cite{shumailov2024model}.
43	Model collapse studies have documented this degradation~\cite{drayson2025emnlp}, but they assume the recursion depth is known a priori.
44	In practice, curators face unlabeled text and must infer depth from the text itself.
45	
46	Existing synthetic text detectors operate in a binary paradigm---\emph{real} vs.\ \emph{synthetic}---discarding ordinal information about \emph{how many} recursive cycles a text has undergone.
47	This is a consequential limitation: first-generation synthetic text may be high-quality and useful for training, while deeply recursive text exhibits statistical degradation (narrowed surprisal distributions, shifted perplexity, Zipf distortion) that can harm downstream models.
48	A curation strategy that distinguishes these cases can retain useful synthetic content while filtering harmful recursive artifacts.
49	
50	We make three contributions:
51	
52	\begin{enumerate}[leftmargin=*,topsep=2pt,itemsep=1pt]
53	\item \textbf{Ordinal depth estimation framework.} We formalize the task of predicting generation depth $d \in \{0,1,\ldots,K\}$ from text alone, propose DCOL with learnable non-uniform margins, and show it achieves 82.3\% 4-class accuracy (57.1\% 6-class), outperforming 8 baselines including CORAL, cross-entropy DeBERTa, and zero-shot GPT-4o.
54	
55	\item \textbf{Depth Degradation Atlas.} We provide the first systematic empirical map of recursive degradation across 3 model families $\times$ 3 decoding strategies, identifying surprisal variance as the most stable depth signal (monotonicity score 0.847), documenting non-uniform inter-depth distances, and establishing the Effective Discriminable Depth (EDD $\approx 3$) boundary.
56	
57	\item \textbf{Depth-graduated curation (proof-of-concept).} Graduated weighting by predicted depth reduces fine-tuning perplexity by 3.1\% over binary filtering ($p=0.038$), demonstrating the practical value of ordinal depth information.
58	\end{enumerate}
59	
60	% ============================================================
61	\section{Related Work}
62	\label{sec:related}
63	
64	\paragraph{Model collapse and recursive generation.}
65	Shumailov et al.\ (2024) demonstrate that iterative training on self-generated data leads to distribution collapse, with tails of the original distribution vanishing progressively.
66	Drayson et al.\ (EMNLP 2025) extend this analysis to characterize non-monotonic degradation patterns in specific settings.
67	These studies assume depth is known; we estimate it from text.
68	
69	\paragraph{Synthetic text detection.}
70	Binary detectors such as LOKI, DivEye, and Binoculars classify text as real or synthetic using statistical features or model-based scores.
71	EditLens estimates single-pass AI editing extent but does not address recursive depth.
72	Our work extends the detection paradigm from binary to ordinal.
73	
74	\paragraph{Ordinal classification.}
75	CORAL~\cite{cao2020coral} learns ordinal regression with consistent rank predictions via cumulative probabilities.
76	CLOC (CVPR 2025) applies contrastive learning with ordinal margins to age estimation.
77	We adapt the contrastive ordinal framework to text, introducing strategy-aware margins, surprisal-augmented anchors, and non-uniform learned margins.
78	
79	% ============================================================
80	\section{Method}
81	\label{sec:method}
82	
83	\subsection{Problem Formulation}
84	
85	Given a text passage $x$, we estimate its ordinal generation depth $d \in \{0, 1, \ldots, K\}$, where $d=0$ denotes human-written text and $d=k$ denotes text produced by the $k$-th recursive generation cycle.
86	The key structural property is that inter-depth distances are \emph{non-uniform}: the distribution shift from $d=0$ to $d=1$ is far larger than from $d=2$ to $d=3$, reflecting the diminishing marginal degradation in recursive generation.
87	
88	\subsection{Benchmark Construction}
89	
90	We construct recursive generation chains using three model families---Pythia-1.4B, OLMo-1B, and GPT-2~XL---each with three decoding strategies: nucleus sampling ($p=0.95$), temperature sampling ($\tau=0.9$), and top-$k$ sampling ($k=50$).
91	For each of the 9 model$\times$strategy combinations, we produce chains of depth $0$ through $5$ (6 levels), with approximately 1{,}200 samples per depth per strategy.
92	Depth-$0$ texts are drawn from a held-out human corpus; each subsequent depth is generated by prompting the model with the previous depth's output.
93	
94	\subsection{Feature Extraction}
95	
96	We extract 19 statistical features from each text, spanning:
97	\begin{itemize}[leftmargin=*,topsep=2pt,itemsep=1pt]
98	\item \textbf{Surprisal statistics}: mean, variance, p75, p90 of token-level surprisal
99	\item \textbf{Perplexity statistics}: mean, p75, p90 of passage-level perplexity
100	\item \textbf{Lexical statistics}: Zipf's $\alpha$, type-token ratio, hapax ratio, repetition rate
101	\item \textbf{Distribution statistics}: entropy, KL divergence from reference, tail probability mass
102	\end{itemize}
103	These features serve both the Random Forest (RF) baseline and as analysis dimensions in the Atlas.
104	
105	\subsection{DCOL: Depth Contrastive Ordinal Learning}
106	
107	DCOL uses a DeBERTa-v3-large encoder to produce passage embeddings $\mathbf{h} = f_\theta(x)$.
108	Training uses an $N$-pair contrastive loss with ordinal margins:
109	\begin{equation}
110	\mathcal{L} = \sum_{(i,j)} \max\bigl(0, \|\mathbf{h}_i - \mathbf{h}_j\|_2 - m(|d_i - d_j|)\bigr)^2
111	\end{equation}
112	where $m(\Delta d)$ is a margin function that enforces larger separation for more distant depths.
113	
114	Three text-specific modifications distinguish DCOL from generic contrastive ordinal methods:
115	
116	\begin{enumerate}[leftmargin=*,topsep=2pt,itemsep=1pt]
117	\item \textbf{Learnable non-uniform margins.} Instead of fixed margins $m(\Delta d) = \alpha \cdot \Delta d$, we parameterize $m$ with per-adjacent-pair learnable scalars, allowing the model to discover that $m(0\to1) \gg m(2\to3)$.
118	\item \textbf{Surprisal-augmented anchor selection.} Hard negative mining prioritizes pairs whose surprisal variance is close but depth differs, focusing contrastive learning on the most informative comparisons.
119	\item \textbf{Strategy conditioning.} A lightweight strategy embedding modulates the encoder, accounting for decoding-strategy-specific degradation patterns.
120	\end{enumerate}
121	
122	For classification, an ordinal regression head maps embeddings to cumulative probabilities, predicting depth as the largest $d$ for which $P(D > d) > 0.5$.
123	
124	% ============================================================
125	\section{Experiments}
126	\label{sec:experiments}
127	
128	\subsection{Per-Model Recursive Chain Benchmarks}
129	\label{sec:per_model}
130	
131	We first evaluate depth estimation independently on each model family using RF classifiers with 19 statistical features to establish that recursive degradation signals exist across architectures.
132	
133	\begin{table}[t]
134	\centering
135	\small
136	\caption{Per-model 4-class depth estimation (RF + 19 features). Accuracy with 95\% CI, MAE, and per-pair AUC. $\sim$1{,}200 samples per depth per strategy.}
137	\label{tab:per_model}
138	\begin{tabular}{@{}lccccc@{}}
139	\toprule
140	\textbf{Model} & \textbf{Acc.\ (4-cl)} & \textbf{MAE} & \textbf{AUC$_{0v1}$} & \textbf{AUC$_{1v2}$} & \textbf{AUC$_{2v3}$} \\
141	\midrule
142	GPT-2 XL & .798 [.785,.811] & .218 & .998 & .874 & .812 \\
143	Pythia-1.4B & .782 & .237 & .998 & .861 & .801 \\
144	OLMo-1B & .754 [.740,.768] & .268 & .994 & .838 & .771 \\
145	\bottomrule
146	\end{tabular}
147	\end{table}
148	
149	Table~\ref{tab:per_model} shows results pooled across strategies.
150	GPT-2~XL exhibits the strongest depth signals (79.8\% 4-class accuracy), consistent with its weaker generation ability producing faster degradation.
151	OLMo-1B shows the weakest signals (75.4\%), attributable to Dolma-trained generation producing more human-like shallow outputs.
152	Across all models, AUC decreases monotonically from $>$0.99 (depth 0v1) to $\sim$0.77--0.81 (depth 2v3), confirming that depth discrimination degrades but remains well above chance within the first three generations.
153	
154	\paragraph{Per-strategy breakdown.}
155	Table~\ref{tab:olmo_strategy} and Table~\ref{tab:gpt2_strategy} report per-strategy results for OLMo-1B and GPT-2~XL, respectively.
156	Nucleus sampling consistently yields the strongest depth signals, while temperature sampling produces the weakest---temperature's unrestricted rescaling of the logit space adds noise that partially masks depth-related degradation.
157	
158	\begin{table}[t]
159	\centering
160	\small
161	\caption{OLMo-1B per-strategy 4-class results.}
162	\label{tab:olmo_strategy}
163	\begin{tabular}{@{}lcccc@{}}
164	\toprule
165	\textbf{Strategy} & \textbf{Acc.} & \textbf{MAE} & \textbf{AUC$_{1v2}$} & \textbf{AUC$_{2v3}$} \\
166	\midrule
167	Nucleus $p$=0.95 & .768 & .252 & .849 & .784 \\
168	Top-$k$ $k$=50 & .752 & .271 & .839 & .770 \\
169	Temperature $\tau$=0.9 & .741 & .281 & .827 & .758 \\
170	\bottomrule
171	\end{tabular}
172	\end{table}
173	
174	\begin{table}[t]
175	\centering
176	\small
177	\caption{GPT-2~XL per-strategy 4-class results.}
178	\label{tab:gpt2_strategy}
179	\begin{tabular}{@{}lcccc@{}}
180	\toprule
181	\textbf{Strategy} & \textbf{Acc.} & \textbf{MAE} & \textbf{AUC$_{1v2}$} & \textbf{AUC$_{2v3}$} \\
182	\midrule
183	Nucleus $p$=0.95 & .812 & .204 & .885 & .823 \\
184	Top-$k$ $k$=50 & .799 & .217 & .876 & .815 \\
185	Temperature $\tau$=0.9 & .783 & .234 & .861 & .798 \\
186	\bottomrule
187	\end{tabular}
188	\end{table}
189	
190	\subsection{DCOL and Baseline Comparison}
191	\label{sec:baselines}
192	
193	We compare DCOL against 8 baselines, pooled across all 3 models $\times$ 3 strategies (Table~\ref{tab:baselines}).
194	
195	\begin{table}[t]
196	\centering
197	\small
198	\caption{Full baseline comparison, pooled across 3 models $\times$ 3 strategies. $\Delta$ is relative to best baseline (CORAL).}
199	\label{tab:baselines}
200	\begin{tabular}{@{}lcccc@{}}
201	\toprule
202	\textbf{Method} & \textbf{Acc.\ (6-cl)} & \textbf{MAE (6-cl)} & \textbf{Acc.\ (4-cl)} & \textbf{$\Delta$ (pp)} \\
203	\midrule
204	DCOL (ours) & .571 & .462 & .823 & +3.3 \\
205	CORAL (DeBERTa) & .538 & .491 & .806 & --- \\
206	CE (DeBERTa) & .519 & .512 & .793 & $-$1.9 \\
207	DeBERTa E2E (CE) & .553 & .478 & .809 & +1.5 \\
208	RF + 19 features & .497 & .538 & .778 & $-$4.1 \\
209	Binary cascade & .461 & .574 & .723 & $-$7.7 \\
210	DivEye features & .432 & .612 & .698 & $-$10.6 \\
211	LOKI features & .408 & .641 & .672 & $-$13.0 \\
212	Perplexity regression & .389 & .673 & .651 & $-$14.9 \\
213	Zero-shot GPT-4o & .287 & .892 & .418 & $-$25.1 \\
214	\bottomrule
215	\end{tabular}
216	\end{table}
217	
218	DCOL achieves 57.1\% 6-class accuracy and 82.3\% 4-class accuracy with 95\% CI [.811, .835].
219	The best baseline is CORAL (53.8\%), which shares DeBERTa's backbone and ordinal structure; DCOL's advantage of +3.3pp comes from learned non-uniform margins and contrastive training.
220	DCOL outperforms the best non-ordinal method (DeBERTa E2E at 55.3\%) by +1.8pp in 6-class accuracy, and the feature-based RF baseline by +7.4pp.
221	
222	Zero-shot GPT-4o performs near chance (28.7\% vs.\ 16.7\% chance), confirming that recursive depth is not a surface-level property accessible to general-purpose LLMs without task-specific training.
223	
224	\paragraph{End-to-end DeBERTa analysis.}
225	The end-to-end DeBERTa classifier (CE loss, no hand-crafted features) achieves 55.3\% 6-class and 80.9\% 4-class accuracy (Table~\ref{tab:e2e}).
226	It outperforms RF+features by +5.6pp (6-class), indicating that raw text encodes degradation signals beyond the 19 hand-crafted features.
227	DCOL's additional +1.8pp over E2E comes from ordinal inductive bias, not representation capacity: pairwise AUCs at depth 2v3 (.856 vs .838) and 3v4 (.714 vs .698) show that ordinal margins help most at the harder adjacent-pair boundaries.
228	
229	\begin{table}[t]
230	\centering
231	\small
232	\caption{End-to-end DeBERTa vs DCOL vs RF.}
233	\label{tab:e2e}
234	\begin{tabular}{@{}lccc@{}}
235	\toprule
236	\textbf{Method} & \textbf{Acc.\ (6-cl)} & \textbf{MAE (6-cl)} & \textbf{Acc.\ (4-cl)} \\
237	\midrule
238	DCOL (contrastive ordinal) & .571 & .462 & .823 \\
239	DeBERTa E2E (CE) & .553 & .478 & .809 \\
240	RF + 19 features & .497 & .538 & .778 \\
241	\bottomrule
242	\end{tabular}
243	\end{table}
244	
245	\subsection{DCOL Component Ablation}
246	\label{sec:ablation}
247	
248	We ablate DCOL's three text-specific modifications (Table~\ref{tab:ablation}).
249	
250	\begin{table}[t]
251	\centering
252	\small
253	\caption{DCOL component ablation (6-class accuracy, pooled).}
254	\label{tab:ablation}
255	\begin{tabular}{@{}lcc@{}}
256	\toprule
257	\textbf{Variant} & \textbf{Acc.\ (6-cl)} & \textbf{$\Delta$ (pp)} \\
258	\midrule
259	Full DCOL & .571 & --- \\
260	$-$ Strategy conditioning & .562 & $-$0.9 \\
261	$-$ Surprisal anchors & .558 & $-$1.3 \\
262	$-$ Learnable margins & .547 & $-$2.4 \\
263	$-$ All three (vanilla contrastive) & .531 & $-$4.0 \\
264	\bottomrule
265	\end{tabular}
266	\end{table}
267	
268	Learnable non-uniform margins contribute the largest increment ($-$2.4pp when removed), confirming that the non-uniform inter-depth geometry is a key structural property.
269	Surprisal-augmented anchor selection contributes $-$1.3pp; strategy conditioning contributes $-$0.9pp (its benefit is more pronounced in per-strategy evaluation than in pooled numbers).
270	Removing all three reduces accuracy to 53.1\%, below CORAL's 53.8\%, indicating that the vanilla contrastive loss alone underperforms CORAL's rank loss---the text-specific modifications are necessary for DCOL to surpass ordinal regression baselines.
271	
272	\subsection{Depth Degradation Atlas}
273	\label{sec:atlas}
274	
275	The Atlas systematically characterizes recursive degradation across all 9 model$\times$strategy combinations.
276	
277	\paragraph{Effective Discriminable Depth (EDD).}
278	We define EDD as the maximum depth $d$ for which adjacent-pair AUC($d$ vs $d{+}1$) $\geq$ 0.72.
279	Table~\ref{tab:edd} reports EDD per combination.
280	
281	\begin{table}[t]
282	\centering
283	\small
284	\caption{EDD per model $\times$ strategy combination. Median EDD = 3.}
285	\label{tab:edd}
286	\begin{tabular}{@{}lccc@{}}
287	\toprule
288	\textbf{Model} & \textbf{Nucleus} & \textbf{Temperature} & \textbf{Top-$k$} \\
289	\midrule
290	Pythia-1.4B & 3 & 3 & 3 \\
291	OLMo-1B & 3 & 2 & 3 \\
292	GPT-2 XL & 4 & 3 & 3 \\
293	\bottomrule
294	\end{tabular}
295	\end{table}
296	
297	The median EDD across all 9 combinations is 3, meaning ordinal depth estimation is feasible at 4-class granularity (depths 0--3).
298	The range spans 2 (OLMo + temperature, where high intrinsic generation diversity compounds with temperature noise to saturate signals early) to 4 (GPT-2~XL + nucleus, where weaker generation and truncated sampling preserve depth signals longer).
299	This variation itself is a key finding: EDD is not a universal constant but depends on model capability and decoding strategy.
300	
301	\paragraph{Feature monotonicity.}
302	Table~\ref{tab:monotonicity} reports monotonicity scores (mean across 9 combinations) for the top-5 features.
303	
304	\begin{table}[t]
305	\centering
306	\small
307	\caption{Top-5 features by monotonicity score (mean across 9 combos). Rank stability = number of combos where the feature ranks $\leq k$.}
308	\label{tab:monotonicity}
309	\begin{tabular}{@{}lcc@{}}
310	\toprule
311	\textbf{Feature} & \textbf{Mono.\ score} & \textbf{Rank stability} \\
312	\midrule
313	\texttt{var\_surprisal} & 0.847 & 1/9 rank 1 \\
314	\texttt{p90\_ppl} & 0.823 & 6/9 rank $\leq$ 3 \\
315	\texttt{mean\_ppl} & 0.801 & 7/9 rank $\leq$ 4 \\
316	\texttt{zipf\_alpha} & 0.768 & 5/9 rank $\leq$ 5 \\
317	\texttt{mean\_surprisal} & 0.752 & 8/9 rank $\leq$ 6 \\
318	\bottomrule
319	\end{tabular}
320	\end{table}
321	
322	Surprisal variance (\texttt{var\_surprisal}) is the strongest and most stable depth signal (0.847), reflecting the progressive narrowing of surprisal distributions under recursive generation.
323	Perplexity tail statistics (\texttt{p90\_ppl}) rank second, capturing the loss of high-perplexity passages as recursion compresses the distribution.
324	Two of the 9 combinations exhibit non-monotonic feature behavior beyond the EDD boundary (OLMo+temperature at depth 3$\to$4, Pythia+top-$k$ at depth 4$\to$5); we interpret these as noise oscillations after signal saturation rather than genuine non-monotonic degradation.
325	
326	\subsection{Depth Extension and EDD Validation}
327	\label{sec:extension}
328	
329	We extend Pythia chains to depth 6 to validate the EDD boundary.
330	Table~\ref{tab:extension} shows pairwise AUCs.
331	
332	\begin{table}[t]
333	\centering
334	\small
335	\caption{Extended-depth pairwise AUC (Pythia-1.4B, nucleus).}
336	\label{tab:extension}
337	\begin{tabular}{@{}lccccccc@{}}
338	\toprule
339	\textbf{Pair} & 0v1 & 1v2 & 2v3 & 3v4 & 4v5 & 5v6 \\
340	\midrule
341	AUC & .998 & .861 & .801 & .708 & .621 & .573 \\
342	\bottomrule
343	\end{tabular}
344	\end{table}
345	
346	AUC declines monotonically, crossing the 0.72 threshold between depth 3v4 (0.708), confirming EDD = 3.
347	Bhattacharyya overlap between feature distributions rises from 0.82 (depth 4--5) to 0.91 (depth 5--6), approaching complete overlap.
348	Notably, feature importance shifts beyond the EDD: \texttt{var\_surprisal} drops from rank 1 to rank 3 while \texttt{zipf\_alpha} rises from rank 4 to rank 2 at depth 4+, suggesting that once surprisal variance is ``compressed to floor,'' lexical frequency distribution becomes the residual discriminative signal.
349	
350	\subsection{Granularity Ablation}
351	\label{sec:granularity}
352	
353	Table~\ref{tab:granularity} reports DCOL accuracy across classification granularities.
354	
355	\begin{table}[t]
356	\centering
357	\small
358	\caption{Granularity ablation (DCOL, pooled). Lift = accuracy $-$ chance.}
359	\label{tab:granularity}
360	\begin{tabular}{@{}lccc@{}}
361	\toprule
362	\textbf{Granularity} & \textbf{Acc.} & \textbf{Chance} & \textbf{Lift (pp)} \\
363	\midrule
364	Binary (0 vs 1+) & .946 & .500 & +44.6 \\
365	3-class (0, 1, 2+) & .867 & .333 & +53.4 \\
366	4-class (0, 1, 2, 3+) & .823 & .250 & +57.3 \\
367	6-class (0--5) & .571 & .167 & +40.4 \\
368	\bottomrule
369	\end{tabular}
370	\end{table}
371	
372	Lift over chance peaks at 4-class (+57.3pp), making it the optimal information--feasibility tradeoff.
373	The drop in lift from 4-class to 6-class reflects the inclusion of depths 4 and 5, which are largely indistinguishable (as predicted by EDD $\approx$ 3).
374	We report 6-class results throughout this paper for completeness but recommend 4-class (depths 0--3) as the practical operating granularity; depth 4+ should be treated as a collapsed ``deep recursive'' category.
375	
376	\subsection{Cross-Model Generalization}
377	\label{sec:cross_model}
378	
379	We evaluate leave-one-model-out (LOMO) generalization, training DCOL on two model families and testing on the held-out third (Table~\ref{tab:lomo}).
380	
381	\begin{table}[t]
382	\centering
383	\small
384	\caption{Leave-one-model-out cross-generalization.}
385	\label{tab:lomo}
386	\begin{tabular}{@{}llcccc@{}}
387	\toprule
388	\textbf{Held-out} & \textbf{Train on} & \textbf{Acc.\ (6-cl)} & \textbf{Acc.\ (4-cl)} & \textbf{MAE} & \textbf{Gate$_{.45}$} \\
389	\midrule
390	Pythia & OLMo, GPT-2 XL & .483 & .721 & .547 & PASS \\
391	OLMo & Pythia, GPT-2 XL & .421 & .673 & .601 & FAIL \\
392	GPT-2 XL & Pythia, OLMo & .507 & .748 & .521 & PASS \\
393	\midrule
394	\multicolumn{2}{@{}l}{Mean $\pm$ std} & .470 $\pm$ .036 & .714 $\pm$ .031 & .556 $\pm$ .033 & 2/3 \\
395	\bottomrule
396	\end{tabular}
397	\end{table}
398	
399	Mean 6-class accuracy is 47.0\% ($\pm$3.6\%), with 2 of 3 rotations passing the 0.45 gate.
400	The Hold-OLMo rotation is weakest (42.1\%): OLMo was trained on Dolma, whose distribution diverges most from the Pile-trained (Pythia) and WebText-trained (GPT-2~XL) models used in training, making it the hardest transfer target.
401	Hold-GPT-2~XL is strongest (50.7\%) because the Pythia+OLMo combination provides sufficient training diversity.
402	The 4-class mean (71.4\%) remains well above chance (25\%), indicating that coarse-grained ordinal estimation within the EDD boundary transfers across model families, even if fine-grained 6-class transfer is unreliable.
403	
404	\subsection{Cross-Strategy Generalization}
405	\label{sec:cross_strategy}
406	
407	Leave-one-strategy-out (LOSO) results (Table~\ref{tab:loso}) show that strategy generalization is easier than model generalization.
408	
409	\begin{table}[t]
410	\centering
411	\small
412	\caption{Leave-one-strategy-out cross-generalization.}
413	\label{tab:loso}
414	\begin{tabular}{@{}lcc@{}}
415	\toprule
416	\textbf{Held-out strategy} & \textbf{Acc.\ (6-cl)} & \textbf{Acc.\ (4-cl)} \\
417	\midrule
418	Nucleus & .528 & .786 \\
419	Temperature & .492 & .753 \\
420	Top-$k$ & .541 & .798 \\
421	\midrule
422	Mean $\pm$ std & .520 $\pm$ .021 & .779 $\pm$ .019 \\
423	\bottomrule
424	\end{tabular}
425	\end{table}
426	
427	Mean 6-class accuracy is 52.0\% ($\pm$2.1\%), compared to 47.0\% ($\pm$3.6\%) for model generalization.
428	Hold-temperature is weakest (49.2\%) because temperature sampling rescales the full logit distribution rather than truncating tails, producing surface statistics more distinct from nucleus/top-$k$.
429	The lower variance ($\sigma$ = 2.1pp vs 3.6pp) indicates that depth signals are primarily determined by model capability rather than decoding strategy---a finding consistent with the Atlas analysis (\S\ref{sec:atlas}).
430	
431	\subsection{Downstream Curation Proof-of-Concept}
432	\label{sec:curation}
433	
434	We test whether predicted depth enables better data curation than binary filtering (Table~\ref{tab:curation}).
435	A 1B-parameter model is fine-tuned on corpora curated with four strategies: no filtering, binary removal of all predicted-synthetic text, graduated weighting ($w = 1/(d_{\text{pred}}+1)$), and oracle weighting using true depth.
436	
437	\begin{table}[t]
438	\centering
439	\small
440	\caption{Downstream curation comparison.}
441	\label{tab:curation}
442	\begin{tabular}{@{}lccc@{}}
443	\toprule
444	\textbf{Curation method} & \textbf{PPL} & \textbf{Task Acc.} \\
445	\midrule
446	No filter & 19.85 & .703 \\
447	Binary filter & 18.72 & .724 \\
448	Graduated weighting (predicted) & 18.14 & .731 \\
449	Oracle weighting (true depth) & 17.91 & .738 \\
450	\bottomrule
451	\end{tabular}
452	\end{table}
453	
454	Graduated weighting reduces perplexity by 3.1\% relative to binary filtering ($p=0.038$) and by 8.6\% relative to no filtering.
455	The gap to oracle weighting (18.14 vs 17.91) quantifies the cost of depth prediction errors.
456	Downstream task accuracy follows the same ordering, though the gap between graduated and binary (73.1\% vs 72.4\%) is smaller, as perplexity differences attenuate when propagated to task performance.
457	
458	We scope this as a proof-of-concept with explicit limitations: (1) tested at a single model scale (1B), (2) graduated vs binary confidence intervals partially overlap, and (3) curation effectiveness depends on depth prediction quality.
459	
460	\subsection{Cross-Scale Probe: 7B Models}
461	\label{sec:7b}
462	
463	We probe whether depth signals transfer across model scales by testing DCOL trained on 1--1.5B models against 7B-model recursive chains (Table~\ref{tab:7b}).
464	
465	\begin{table}[t]
466	\centering
467	\small
468	\caption{Cross-scale transfer to 7B model.}
469	\label{tab:7b}
470	\begin{tabular}{@{}lcc@{}}
471	\toprule
472	\textbf{Setting} & \textbf{Acc.\ (4-cl)} & \textbf{Acc.\ (6-cl)} \\
473	\midrule
474	Zero-shot transfer (1--1.5B $\to$ 7B) & .614 & .372 \\
475	Fine-tuned on 7B data & .791 & .518 \\
476	1--1.5B in-distribution (ref.) & .823 & .571 \\
477	\bottomrule
478	\end{tabular}
479	\end{table}
480	
481	Zero-shot transfer degrades substantially (4-class: 61.4\% vs 82.3\% in-distribution), reflecting that 7B models produce higher-quality generation that shifts the depth boundaries---depth-1 text from a 7B model resembles depth-0 quality at the 1B scale.
482	However, fine-tuning on 7B data recovers to 79.1\% (4-class), indicating depth signals exist at the larger scale but require recalibration.
483	EDD at 7B is 3 (nucleus) and 2 (temperature), suggesting that stronger models reach signal saturation at shallower depths.
484	This motivates future work on scale-invariant depth estimation.
485	
486	\subsection{Wild-Data Calibration}
487	\label{sec:wild}
488	
489	We apply the trained DCOL model to a sample of RedPajama/Dolma web text as an ecological validity probe (Table~\ref{tab:wild}).
490	
491	\begin{table}[t]
492	\centering
493	\small
494	\caption{Wild-data depth score correlations with quality proxies.}
495	\label{tab:wild_corr}
496	\begin{tabular}{@{}lcc@{}}
497	\toprule
498	\textbf{Quality proxy} & \textbf{Spearman $\rho$} & \textbf{$p$-value} \\
499	\midrule
500	Perplexity (GPT-2) & .341 & .002 \\
501	AlignScore & .283 & .014 \\
502	\bottomrule
503	\end{tabular}
504	\end{table}
505	
506	\begin{table}[t]
507	\centering
508	\small
509	\caption{Predicted depth distribution on RedPajama sample.}
510	\label{tab:wild}
511	\begin{tabular}{@{}lcccc@{}}
512	\toprule
513	\textbf{Depth} & 0 & 1 & 2 & 3+ \\
514	\midrule
515	\% of sample & 72 & 16 & 6 & 6 \\
516	\bottomrule
517	\end{tabular}
518	\end{table}
519	
520	DCOL depth scores show moderate positive correlation with perplexity ($\rho = 0.341$, $p = 0.002$) and weaker correlation with AlignScore ($\rho = 0.283$, $p = 0.014$).
521	The majority of wild data is scored as depth 0 (72\%), with 28\% receiving depth $\geq$1.
522	The 6\% scored as depth 3+ may include overestimates, as low-quality human text in the wild can exhibit statistical profiles similar to deeply recursive content.
523	We present this as a calibration analysis rather than validation, since no ground-truth depth labels exist for wild data.
524	The controlled benchmark remains our primary evaluation setting.
525	
526	% ============================================================
527	\section{Discussion}
528	\label{sec:discussion}
529	
530	\paragraph{EDD as a scientific contribution.}
531	The finding that EDD $\approx$ 3 across model families and decoding strategies provides a concrete answer to a previously open question: \emph{how deep can we look into recursive generation?}
532	For the model collapse community, this establishes a quantitative boundary on the depth at which statistical signals saturate.
533	The variation of EDD across conditions (2--4) reveals that model capability and decoding strategy interact to determine this boundary, with weaker models and truncation-based sampling preserving signals longer.
534	
535	\paragraph{Feature dynamics beyond EDD.}
536	The Atlas reveals that different features dominate at different depth ranges: surprisal variance is paramount within EDD, but Zipf's $\alpha$ becomes more discriminative beyond it.
537	This ``feature handoff'' suggests that recursive degradation is not a uniform process but proceeds in phases---first compressing the surprisal distribution, then distorting lexical frequency structure.
538	
539	\paragraph{Limitations.}
540	\begin{itemize}[leftmargin=*,topsep=2pt,itemsep=1pt]
541	\item \textbf{Cross-model gap.} The OLMo rotation fails the 0.45 6-class gate (42.1\%), indicating that cross-model transfer is unreliable when training distributions diverge substantially. Domain adaptation may be needed for deployment across diverse model families.
542	\item \textbf{Effective granularity.} While we report 6-class results, actual discriminative power is limited to 4 classes (depths 0--3). Depths 4+ collapse into an indistinguishable category.
543	\item \textbf{Scale transfer.} Zero-shot transfer to 7B models degrades by $\sim$21pp (4-class), requiring scale-specific calibration.
544	\item \textbf{Controlled vs wild gap.} Our benchmark uses controlled recursive chains; wild synthetic text is produced under diverse, unknown conditions. The moderate wild-data correlations ($\rho \leq 0.34$) indicate this gap is nontrivial.
545	\item \textbf{DCOL advantage magnitude.} DCOL outperforms the best baseline (CORAL) by +3.3pp. The contribution is real but moderate; much of the ordinal estimation capability comes from the ordinal framework itself rather than DCOL-specific innovations.
546	\end{itemize}
547	
548	% ============================================================
549	\section{Conclusion}
550	\label{sec:conclusion}
551	
552	We introduced ordinal generation depth estimation as a new task, moving beyond binary synthetic detection to characterize \emph{how deeply recursive} text content is.
553	Our Depth Degradation Atlas establishes EDD $\approx$ 3 as the boundary of feasible ordinal discrimination, documents surprisal variance as the most stable depth signal, and maps the interaction between model capability and decoding strategy in determining degradation patterns.
554	DCOL achieves 82.3\% 4-class accuracy with moderate but consistent gains over baselines.
555	A proof-of-concept shows that depth-graduated curation outperforms binary filtering, though with modest effect size.
556	We hope the Atlas---particularly the EDD metric and feature monotonicity analysis---proves directly useful to the model collapse community as a reference for understanding and mitigating recursive contamination.
557	
558	\begin{thebibliography}{9}
559	\bibitem{shumailov2024model}
560	Shumailov, I., et al.
561	\newblock AI models collapse when trained on recursively generated data.
562	\newblock {\em Nature}, 631:755--760, 2024.
563	
564	\bibitem{drayson2025emnlp}
565	Drayson, H., et al.
566	\newblock Characterizing non-monotonic degradation in recursive model generation.
567	\newblock In {\em Proc.\ EMNLP}, 2025.
568	
569	\bibitem{cao2020coral}
570	Cao, W., Mirjalili, V., and Raschka, S.
571	\newblock Rank consistent ordinal regression for neural networks with application to age estimation.
572	\newblock {\em Pattern Recognition Letters}, 140:325--331, 2020.
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
  "parentUuid": "3b9bb1af-6c8f-4402-b91d-a2cedd276840",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "e9ff8a3f-ad88-4bc6-a3ee-b7b4a2c8dcd7",
  "sourceToolAssistantUUID": "3b9bb1af-6c8f-4402-b91d-a2cedd276840",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T14:52:05.503Z_

<details open><summary>🔧 Tool call — Read · `toolu_015ousUuREdDp5G4k67zbT5o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9ff8a3f-ad88-4bc6-a3ee-b7b4a2c8dcd7",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2efC38mRVti5CtNuAVZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bac1a146-7909-489a-b8e1-27c79daecfc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CYqQF7CEhSfAyZfkNV17yt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1353,
      "cache_read_input_tokens": 23719,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1353
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 23719,
          "cache_creation_input_tokens": 1353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1353,
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

_source line 32 · 2026-05-14T14:52:05.814Z_

<details><summary>↩ Tool result · `toolu_015ousUuREdDp5G4k67zbT5o`</summary>

```text
1	narrative_guidance: 'EDD≈3是核心科学发现，论文叙事围绕"ordinal depth estimation在EDD边界内可行"展开。 DCOL优于baseline但优势中等（+3-7pp），叙事重心从方法突破转向"序数框架+Atlas"的组合贡献。
2	  Atlas权重上升为论文核心——文档化递归退化的边界和模式对model collapse社区直接有用。 Claim 3缩减为proof-of-concept。跨模型泛化诚实报告per-rotation结果，弱rotation作为limitation。
3	  有效粒度声明降级：6-class数字报告但承认depth 4+坍缩，实际可行粒度为4-class（depths 0-3）。
4	
5	  '
6	imagined_experiments:
7	- name: OLMo-1B recursive chain benchmark
8	  plan_id: plan_002
9	  description: OLMo-1B在3种策略下生成5层递归链，提取19维统计特征，RF分类
10	  expected_results:
11	    full_4class_acc: 0.754
12	    full_4class_acc_ci:
13	    - 0.74
14	    - 0.768
15	    full_mae: 0.268
16	    full_auc_0v1: 0.994
17	    full_auc_1v2: 0.838
18	    full_auc_2v3: 0.771
19	    filtered_4class_acc: 0.789
20	    filtered_4class_acc_ci:
21	    - 0.775
22	    - 0.803
23	    filtered_mae: 0.225
24	    best_model: RandomForest
25	    top_features:
26	    - var_surprisal
27	    - mean_ppl
28	    - p90_ppl
29	    - zipf_alpha
30	    - mean_surprisal
31	    feature_dim: 19
32	    samples_per_depth_per_strategy: ~1200
33	  result_rationale: 'OLMo-1B在Dolma上训练，分布与Pythia的Pile有差异。Dolma以清洗后的web text为主， 初始生成（depth
34	    0→1）的分布偏移略小于Pythia，导致depth 0v1的AUC微降（0.994 vs 0.998）。 但OLMo的Dolma训练使其对web-text
35	    domain更稳定，depth 2v3退化信号略弱（0.771 vs 0.801）， 因为OLMo的生成在浅层更"像人类"，深层退化启动更晚。整体4-class
36	    acc低于Pythia约3pp， 符合median档"信号真实但模型间有波动"的预期。var_surprisal仍是最强特征， 但zipf_alpha在OLMo上排名上升——OLMo的tokenizer和训练数据使词频分布对递归深度更敏感。
37	
38	    '
39	  tables:
40	  - name: 'Table: OLMo-1B per-strategy 4-class accuracy'
41	    rows:
42	    - strategy: nucleus_p0.95
43	      acc_4class: 0.768
44	      mae: 0.252
45	      auc_0v1: 0.995
46	      auc_1v2: 0.849
47	      auc_2v3: 0.784
48	    - strategy: temperature_0.9
49	      acc_4class: 0.741
50	      mae: 0.281
51	      auc_0v1: 0.993
52	      auc_1v2: 0.827
53	      auc_2v3: 0.758
54	    - strategy: topk_50
55	      acc_4class: 0.752
56	      mae: 0.271
57	      auc_0v1: 0.994
58	      auc_1v2: 0.839
59	      auc_2v3: 0.77
60	  figures_description:
61	  - 'Fig: OLMo per-strategy adjacent-depth AUC曲线，显示3种策略在depth 2→3处均出现明显下降'
62	  analysis: 'OLMo结果确认递归退化信号跨模型存在但强度有差异。temperature策略在OLMo上表现最弱， 因为τ=0.9引入的随机性与OLMo自身生成的多样性叠加，模糊了深度信号。
63	    这预示cross-model泛化中OLMo作为held-out时可能是较难的rotation。
64	
65	    '
66	- name: GPT-2 XL recursive chain benchmark
67	  plan_id: plan_003
68	  description: GPT-2 XL 1.5B在3种策略下生成5层递归链，提取19维统计特征，RF分类
69	  expected_results:
70	    full_4class_acc: 0.798
71	    full_4class_acc_ci:
72	    - 0.785
73	    - 0.811
74	    full_mae: 0.218
75	    full_auc_0v1: 0.998
76	    full_auc_1v2: 0.874
77	    full_auc_2v3: 0.812
78	    filtered_4class_acc: 0.831
79	    filtered_4class_acc_ci:
80	    - 0.818
81	    - 0.844
82	    filtered_mae: 0.183
83	    best_model: RandomForest
84	    top_features:
85	    - var_surprisal
86	    - p90_ppl
87	    - mean_ppl
88	    - mean_surprisal
89	    - p75_ppl
90	    feature_dim: 19
91	    samples_per_depth_per_strategy: ~1200
92	  result_rationale: 'GPT-2 XL是collapse文献中最被研究的模型，其WebText训练集相对较小且老旧。 关键：GPT-2 XL的生成能力弱于Pythia和OLMo，递归生成退化更快更明显，
93	    导致相邻深度间的统计差异更大。depth 0v1的AUC（0.998）与Pythia持平， 但depth 1v2（0.874 vs 0.861）和depth
94	    2v3（0.812 vs 0.801）均高于Pythia。 这意味着GPT-2 XL的EDD可能略高于3（但在6-class下仍然depth 4+坍缩）。
95	    4-class acc 0.798略高于Pythia的0.782，因为GPT-2 XL的退化信号更强。 top features排名与Pythia几乎一致，说明var_surprisal作为核心信号具有跨模型稳定性。
96	
97	    '
98	  tables:
99	  - name: 'Table: GPT-2 XL per-strategy 4-class accuracy'
100	    rows:
101	    - strategy: nucleus_p0.95
102	      acc_4class: 0.812
103	      mae: 0.204
104	      auc_0v1: 0.998
105	      auc_1v2: 0.885
106	      auc_2v3: 0.823
107	    - strategy: temperature_0.9
108	      acc_4class: 0.783
109	      mae: 0.234
110	      auc_0v1: 0.997
111	      auc_1v2: 0.861
112	      auc_2v3: 0.798
113	    - strategy: topk_50
114	      acc_4class: 0.799
115	      mae: 0.217
116	      auc_0v1: 0.998
117	      auc_1v2: 0.876
118	      auc_2v3: 0.815
119	  figures_description:
120	  - 'Fig: GPT-2 XL与Pythia的adjacent-depth AUC对比，GPT-2 XL在所有对上均略高'
121	  analysis: 'GPT-2 XL展现最强的深度信号，符合其作为"能力较弱模型退化更快"的预期。 这对Atlas叙事有利——不同模型的退化速率不同，但模式（monotonic
122	    decrease in AUC）一致。 GPT-2 XL的强信号也意味着在cross-model实验中，它作为训练集的一部分会贡献最多信息， 作为held-out测试集则最容易通过gate。
123	
124	    '
125	- name: DCOL contrastive ordinal training
126	  plan_id: plan_004
127	  description: DeBERTa-v3-large编码器 + 多margin N-pair contrastive loss，6-class depth
128	    estimation
129	  expected_results:
130	    dcol_6class_acc_pooled: 0.571
131	    dcol_6class_acc_ci:
132	    - 0.556
133	    - 0.586
134	    dcol_mae_6class: 0.462
135	    dcol_4class_acc: 0.823
136	    dcol_4class_acc_ci:
137	    - 0.811
138	    - 0.835
139	    dcol_mae_4class: 0.192
140	    dcol_auc_0v1: 0.999
141	    dcol_auc_1v2: 0.912
142	    dcol_auc_2v3: 0.856
143	    dcol_auc_3v4: 0.714
144	    dcol_auc_4v5: 0.628
145	    best_lr: 2.0e-05
146	    best_margin_schedule: learned_non_uniform
147	    convergence_epoch: 7
148	    training_hours_actual: 12.5
149	  result_rationale: 'DCOL利用DeBERTa编码器从原始文本学习表示，contrastive ordinal loss强制相邻深度的embedding
150	    距离反映实际退化幅度。6-class pooled acc 0.571处于median范围[0.52,0.62]中段。 关键：DCOL相比RF+features的提升集中在depth
151	    1-3的区分（AUC 1v2从0.86→0.91，2v3从0.80→0.86）， 因为contrastive learning能捕捉features无法编码的微妙语义退化模式。
152	    但depth 3v4的AUC仅0.714——刚好在EDD边界上，depth 4v5的0.628接近随机（chance~0.5）。 这证实EDD≈3：DCOL在depth
153	    0-3上显著优于RF，但无法突破depth 3+的信号天花板。 4-class acc 0.823高于RF的0.782（pooled across 3 models），验证了contrastive
154	    learning 在EDD内的有效性。non_uniform learned margins优于fixed margins， 因为实际inter-depth距离高度不均匀（depth
155	    0→1远大于depth 2→3）。
156	
157	    '
158	  tables:
159	  - name: 'Table: DCOL vs RF feature-based, pooled across 3 models × 3 strategies'
160	    rows:
161	    - method: DCOL (DeBERTa + contrastive)
162	      acc_6class: 0.571
163	      mae_6class: 0.462
164	      acc_4class: 0.823
165	      mae_4class: 0.192
166	    - method: RF + 19 features
167	      acc_6class: 0.497
168	      mae_6class: 0.538
169	      acc_4class: 0.778
170	      mae_4class: 0.241
171	    - method: CORAL (DeBERTa + fixed margin)
172	      acc_6class: 0.538
173	      mae_6class: 0.491
174	      acc_4class: 0.806
175	      mae_4class: 0.211
176	    - method: CE (DeBERTa + cross-entropy)
177	      acc_6class: 0.519
178	      mae_6class: 0.512
179	      acc_4class: 0.793
180	      mae_4class: 0.224
181	  figures_description:
182	  - 'Fig: DCOL训练loss曲线 + per-class accuracy随epoch变化，depth 4-5的accuracy在epoch 4后plateau'
183	  - 'Fig: Learned margin值可视化——margin(0,1) >> margin(2,3) >> margin(3,4)，反映退化的非均匀性'
184	  analysis: 'DCOL在EDD边界内（depth 0-3）的优势明确，但对depth 4+无能为力。 这支持median叙事：方法有效但有天花板，天花板由信号本身（而非方法）决定。
185	    CORAL作为ablation的中间点（0.538 vs DCOL 0.571 vs CE 0.519）说明 ordinal inductive bias有帮助，learned
186	    margins在此基础上进一步提升。 但DCOL vs CORAL仅+3.3pp，说明增益部分来自ordinal structure本身而非contrastive
187	    learning独有。
188	
189	    '
190	- name: Leave-one-model-out generalization
191	  plan_id: plan_005
192	  description: 3个rotation：每次留一个模型族作test，用另外两个训练DCOL
193	  expected_results:
194	    rotation_hold_pythia:
195	      train_on:
196	      - OLMo-1B
197	      - GPT-2 XL
198	      test_on: Pythia-1.4B
199	      acc_6class: 0.483
200	      acc_4class: 0.721
201	      mae_6class: 0.547
202	    rotation_hold_olmo:
203	      train_on:
204	      - Pythia-1.4B
205	      - GPT-2 XL
206	      test_on: OLMo-1B
207	      acc_6class: 0.421
208	      acc_4class: 0.673
209	      mae_6class: 0.601
210	    rotation_hold_gpt2xl:
211	      train_on:
212	      - Pythia-1.4B
213	      - OLMo-1B
214	      test_on: GPT-2 XL
215	      acc_6class: 0.507
216	      acc_4class: 0.748
217	      mae_6class: 0.521
218	    cross_model_loo_6class_acc_mean: 0.47
219	    cross_model_loo_6class_acc_std: 0.036
220	    cross_model_loo_4class_acc_mean: 0.714
221	    gate_pass_count: 2/3 rotations ≥ 0.45 (6-class), OLMo rotation at 0.421 misses
222	  result_rationale: '跨模型泛化是median档的核心挑战。mean 6-class acc 0.470处于[0.42,0.52]范围内。 Hold-OLMo是最弱rotation（0.421，未通过0.45
223	    gate）：OLMo在Dolma上训练， 其生成分布与Pile-trained Pythia和WebText-trained GPT-2 XL差异最大。 Pythia和GPT-2
224	    XL都在"early web text"类型数据上训练，彼此更相似， 所以hold-GPT2XL rotation最强（0.507）——Pythia+OLMo的组合已覆盖足够多样性。
225	    Hold-Pythia居中（0.483），因为OLMo+GPT2XL的组合提供了合理的训练分布。 4-class acc均显著高于6-class，再次确认depth
226	    4+的信号不跨模型迁移。 std=0.036反映"有波动"的median特征——不是所有rotation都稳定通过。
227	
228	    '
229	  tables:
230	  - name: 'Table: Leave-one-model-out 6-class results'
231	    rows:
232	    - rotation: Hold Pythia
233	      acc_6class: 0.483
234	      acc_4class: 0.721
235	      mae: 0.547
236	      gate_45: PASS
237	    - rotation: Hold OLMo
238	      acc_6class: 0.421
239	      acc_4class: 0.673
240	      mae: 0.601
241	      gate_45: FAIL
242	    - rotation: Hold GPT-2 XL
243	      acc_6class: 0.507
244	      acc_4class: 0.748
245	      mae: 0.521
246	      gate_45: PASS
247	    - rotation: Mean ± std
248	      acc_6class: 0.470 ± 0.036
249	      acc_4class: 0.714 ± 0.031
250	      mae: 0.556 ± 0.033
251	      gate_45: 2/3
252	  figures_description:
253	  - 'Fig: 3-rotation confusion matrices并排，Hold-OLMo显示depth 2和depth 3高度混淆'
254	  - 'Fig: Per-rotation per-depth accuracy heatmap，depth 0在所有rotation上 > 90%'
255	  analysis: 'OLMo rotation的失败需要在论文中诚实报告为limitation。叙事可以是： "跨模型泛化在架构/数据相似的模型间成立，但对训练分布差异大的模型需要域适应"。
256	    4-class acc 0.714 mean说明"在EDD内的粗粒度估计"仍然跨模型可行， 这支持降级后的Claim 1声明。补充feature importance
257	    drift分析解释OLMo为什么难。
258	
259	    '
260	- name: Depth Degradation Atlas
261	  plan_id: plan_006
262	  description: 9个model×strategy combo的特征单调性分析、EDD计算、跨模型/策略热力图
263	  expected_results:
264	    edd_per_combo:
265	      pythia_nucleus: 3
266	      pythia_temperature: 3
267	      pythia_topk: 3
268	      olmo_nucleus: 3
269	      olmo_temperature: 2
270	      olmo_topk: 3
271	      gpt2xl_nucleus: 4
272	      gpt2xl_temperature: 3
273	      gpt2xl_topk: 3
274	    edd_median: 3
275	    edd_mean: 3.0
276	    edd_min: 2
277	    edd_max: 4
278	    monotonicity_score_top5_mean: 0.782
279	    monotonicity_score_top5_range:
280	    - 0.71
281	    - 0.85
282	    top5_features_by_monotonicity:
283	    - var_surprisal
284	    - p90_ppl
285	    - mean_ppl
286	    - zipf_alpha
287	    - mean_surprisal
288	    feature_monotonicity_var_surprisal: 0.847
289	    feature_monotonicity_p90_ppl: 0.823
290	    feature_monotonicity_mean_ppl: 0.801
291	    feature_monotonicity_zipf_alpha: 0.768
292	    feature_monotonicity_mean_surprisal: 0.752
293	    non_monotonic_combos:
294	    - olmo_temperature_depth3→4_mean_ppl
295	    - pythia_topk_depth4→5_var_surprisal
296	    min_adjacent_auc_within_edd: 0.771
297	  result_rationale: 'EDD median=3横跨9个combo，但分布有意义的变化。GPT-2 XL nucleus是唯一EDD=4的combo，
298	    因为GPT-2 XL退化最快（前述），nucleus采样保留了最多信号。OLMo temperature是唯一EDD=2的combo， 因为OLMo的生成多样性本就高，叠加temperature的随机性导致depth
299	    2→3的信号就已饱和。 这种跨combo的EDD变化本身就是Atlas的核心科学贡献——EDD不是一个固定常数而是取决于模型能力和解码策略。 top5特征的单调性得分mean
300	    0.782处于[0.7,0.85]范围。var_surprisal最高（0.847）， 因为递归生成使surprisal分布progressively narrowing——这是最稳定的退化信号。
301	    两个非单调combo出现在depth 3→4之后，符合"EDD边界后信号坍缩"的预期。 min_adjacent_auc_within_edd=0.771（出现在OLMo
302	    temperature的depth 1v2），处于[0.72,0.80]范围。
303	
304	    '
305	  tables:
306	  - name: 'Table: EDD per model × strategy'
307	    rows:
308	    - model: Pythia-1.4B
309	      nucleus: 3
310	      temperature: 3
311	      topk: 3
312	    - model: OLMo-1B
313	      nucleus: 3
314	      temperature: 2
315	      topk: 3
316	    - model: GPT-2 XL
317	      nucleus: 4
318	      temperature: 3
319	      topk: 3
320	  - name: 'Table: Top-10 feature monotonicity scores (mean across 9 combos)'
321	    rows:
322	    - feature: var_surprisal
323	      mono_score: 0.847
324	      rank_stability: 1/9 combos rank 1
325	    - feature: p90_ppl
326	      mono_score: 0.823
327	      rank_stability: 6/9 combos rank ≤ 3
328	    - feature: mean_ppl
329	      mono_score: 0.801
330	      rank_stability: 7/9 combos rank ≤ 4
331	    - feature: zipf_alpha
332	      mono_score: 0.768
333	      rank_stability: 5/9 combos rank ≤ 5
334	    - feature: mean_surprisal
335	      mono_score: 0.752
336	      rank_stability: 8/9 combos rank ≤ 6
337	  figures_description:
338	  - 'Fig: 9-panel heatmap（3 models × 3 strategies），每panel显示19个特征在6个depth上的z-score，EDD边界用虚线标注'
339	  - 'Fig: var_surprisal在9个combo上的depth-wise分布boxplot，显示depth 0-3单调递减，depth 4-5重叠'
340	  - 'Fig: EDD boundary可视化——adjacent-depth AUC随depth递减，0.72阈值线标注EDD截断点'
341	  - 'Fig: 非单调异常案例的feature trajectory（OLMo temperature的mean_ppl在depth 3→4回升）'
342	  analysis: 'Atlas是median档下论文的核心贡献。EDD=3的中位数意味着"ordinal depth estimation在4级粒度上可行"，
343	    这本身就是对model collapse社区的直接贡献——之前没有人系统量化"从哪个depth开始区分变得不可能"。 EDD跨combo的变化（2-4）提供了丰富的分析空间：为什么OLMo+temperature最早饱和？
344	    为什么GPT-2 XL+nucleus能多撑一层？这些问题直接关联模型能力和解码策略的交互效应。 非单调现象（2/9 combos在EDD之后）可以解释为"信号坍缩后的噪声震荡"而非真实的非单调退化。
345	
346	    '
347	- name: Leave-one-strategy-out robustness
348	  plan_id: plan_007
349	  description: 3个rotation：每次留一种策略作test，用另外两种训练DCOL
350	  expected_results:
351	    rotation_hold_nucleus:
352	      train_on:
353	      - temperature
354	      - topk
355	      test_on: nucleus
356	      acc_6class: 0.528
357	      acc_4class: 0.786
358	    rotation_hold_temperature:
359	      train_on:
360	      - nucleus
361	      - topk
362	      test_on: temperature
363	      acc_6class: 0.492
364	      acc_4class: 0.753
365	    rotation_hold_topk:
366	      train_on:
367	      - nucleus
368	      - temperature
369	      test_on: topk
370	      acc_6class: 0.541
371	      acc_4class: 0.798
372	    strategy_loo_6class_acc_mean: 0.52
373	    strategy_loo_6class_acc_std: 0.021
374	  result_rationale: '策略间泛化优于模型间泛化（mean 0.520 vs 0.470），因为不同解码策略影响的是生成文本的 表面统计特性（多样性、重复率），而递归退化的核心信号（surprisal
375	    variance压缩、 perplexity drift）跨策略更稳定。Hold-temperature最弱（0.492）是因为temperature采样
376	    产生的分布与nucleus/topk的截断采样在尾部行为上差异最大——temperature不截断分布， 而是rescale整个logit空间，导致生成文本的统计profile不同。
377	    Hold-topk最强（0.541）是因为topk_50与nucleus_0.95在实际效果上最接近 （都是尾部截断，只是截断方式不同），所以nucleus训练集已包含了大部分topk的信号。
378	    std=0.021远小于cross-model的0.036，说明策略间差异比模型间差异小。
379	
380	    '
381	  tables:
382	  - name: 'Table: Leave-one-strategy-out results'
383	    rows:
384	    - rotation: Hold nucleus
385	      acc_6class: 0.528
386	      acc_4class: 0.786
387	    - rotation: Hold temperature
388	      acc_6class: 0.492
389	      acc_4class: 0.753
390	    - rotation: Hold topk
391	      acc_6class: 0.541
392	      acc_4class: 0.798
393	    - rotation: Mean ± std
394	      acc_6class: 0.520 ± 0.021
395	      acc_4class: 0.779 ± 0.019
396	  figures_description:
397	  - 'Fig: Strategy-out vs Model-out泛化gap对比bar chart'
398	  analysis: '策略泛化比模型泛化容易的结论对论文positioning有利——说明depth信号主要与模型能力相关， 而非解码策略的artifact。这强化了Atlas中"模型能力决定EDD"的叙事。
399	    Hold-temperature的相对弱势可引出discussion：temperature采样作为最"自由"的策略， 其生成文本的统计分布最不受约束，可能需要专门的domain
400	    adaptation。
401	
402	    '
403	- name: DeBERTa end-to-end classifier
404	  plan_id: plan_008
405	  description: DeBERTa-v3-large直接text→6-class depth分类，无手工特征
406	  expected_results:
407	    e2e_6class_acc: 0.553
408	    e2e_6class_acc_ci:
409	    - 0.537
410	    - 0.569
411	    e2e_mae_6class: 0.478
412	    e2e_4class_acc: 0.809
413	    e2e_4class_acc_ci:
414	    - 0.796
415	    - 0.822
416	    e2e_mae_4class: 0.206
417	    e2e_auc_0v1: 0.998
418	    e2e_auc_1v2: 0.897
419	    e2e_auc_2v3: 0.838
420	    e2e_auc_3v4: 0.698
421	    e2e_auc_4v5: 0.614
422	    training_hours: 9.2
423	    best_lr: 1.0e-05
424	  result_rationale: 'End-to-end DeBERTa（CE loss）的6-class acc 0.553略低于DCOL的0.571， 但高于RF+features的0.497。这是median档的典型结果：end-to-end能学到features
425	    无法捕捉的语义退化信号（如coherence loss、topic drift），但没有DCOL的ordinal inductive bias，它在相邻深度的区分上不如DCOL精确——特别是depth
426	    2v3（0.838 vs 0.856） 和depth 3v4（0.698 vs 0.714）的AUC差距。End-to-end不如DCOL的原因是CE loss
427	    将每个class独立对待，不利用ordinal structure，而递归深度本质上是有序的。 但end-to-end优于RF说明原始文本中确实存在features未编码的退化信号。
428	    这对论文叙事的含义：DCOL = end-to-end表示能力 + ordinal structure，两者都有贡献。
429	
430	    '
431	  tables:
432	  - name: 'Table: End-to-end vs DCOL vs RF'
433	    rows:
434	    - method: DCOL (contrastive ordinal)
435	      acc_6class: 0.571
436	      mae_6class: 0.462
437	      acc_4class: 0.823
438	    - method: DeBERTa E2E (CE)
439	      acc_6class: 0.553
440	      mae_6class: 0.478
441	      acc_4class: 0.809
442	    - method: RF + 19 features
443	      acc_6class: 0.497
444	      mae_6class: 0.538
445	      acc_4class: 0.778
446	  figures_description:
447	  - 'Fig: 三种方法的per-depth accuracy雷达图，DCOL在depth 2-3上优势最明显'
448	  analysis: 'DCOL vs E2E仅+1.8pp（6-class），这在median档下说明contrastive ordinal loss的增益 存在但不压倒性。论文需要将此差距诚实报告并通过ablation（plan_010）分解贡献来源。
449	
450	    '
451	- name: Baseline battery
452	  plan_id: plan_009
453	  description: 7个baseline：DivEye features回归、perplexity回归、CORAL、CE、zero-shot LLM、binary
454	    ensemble、LOKI features
455	  expected_results:
456	    baselines:
457	      diveye_ordinal_regression:
458	        acc_6class: 0.432
459	        mae_6class: 0.612
460	        acc_4class: 0.698
461	      perplexity_regression:
462	        acc_6class: 0.389
463	        mae_6class: 0.673
464	        acc_4class: 0.651
465	      coral_deberta:
466	        acc_6class: 0.538
467	        mae_6class: 0.491
468	        acc_4class: 0.806
469	      ce_deberta:
470	        acc_6class: 0.519
471	        mae_6class: 0.512
472	        acc_4class: 0.793
473	      zeroshot_llm_gpt4o:
474	        acc_6class: 0.287
475	        mae_6class: 0.892
476	        acc_4class: 0.418
477	      binary_ensemble_cascade:
478	        acc_6class: 0.461
479	        mae_6class: 0.574
480	        acc_4class: 0.723
481	      loki_features_regression:
482	        acc_6class: 0.408
483	        mae_6class: 0.641
484	        acc_4class: 0.672
485	    best_baseline: coral_deberta
486	    best_baseline_6class_acc: 0.538
487	    dcol_delta_over_best_baseline_pp: 3.3
488	    dcol_delta_over_best_nonordinal_pp: 5.2
489	  result_rationale: 'CORAL是最强baseline（0.538），因为它也利用了ordinal structure，与DCOL共享DeBERTa
490	    backbone。 DCOL vs CORAL的+3.3pp处于median的[3,7]范围下端，说明DCOL的增量贡献（learnable margins
491	    + contrastive loss + strategy conditioning）存在但中等。CE DeBERTa次之（0.519）， 说明DeBERTa的表示能力本身就很强，ordinal
492	    bias带来的额外增益约2pp。 DivEye features（0.432）比RF+19 features（0.497）低，因为DivEye的特征是为binary
493	    detection 设计的，缺少var_surprisal等对depth敏感的特征。Zero-shot LLM表现最差（0.287，接近 6-class chance
494	    16.7%但显著高于），说明LLM的深度判断能力很弱——深度不是surface-level可感知的属性。 Binary ensemble cascade（先判binary再细分）达到0.461，优于feature
495	    regression但弱于 end-to-end方法，因为cascade的error propagation导致浅层误差累积。 DCOL delta +3.3pp在median范围内偏低，叙事需要强调"框架+Atlas"而非"方法突破"。
496	
497	    '
498	  tables:
499	  - name: 'Table: Full baseline comparison (pooled across 3 models × 3 strategies)'
500	    rows:
501	    - method: DCOL (ours)
502	      acc_6class: 0.571
503	      mae_6class: 0.462
504	      acc_4class: 0.823
505	      delta_vs_best: +3.3pp
506	    - method: CORAL (DeBERTa)
507	      acc_6class: 0.538
508	      mae_6class: 0.491
509	      acc_4class: 0.806
510	      delta_vs_best: —
511	    - method: CE (DeBERTa)
512	      acc_6class: 0.519
513	      mae_6class: 0.512
514	      acc_4class: 0.793
515	      delta_vs_best: -1.9pp
516	    - method: RF + 19 features
517	      acc_6class: 0.497
518	      mae_6class: 0.538
519	      acc_4class: 0.778
520	      delta_vs_best: -4.1pp
521	    - method: Binary cascade
522	      acc_6class: 0.461
523	      mae_6class: 0.574
524	      acc_4class: 0.723
525	      delta_vs_best: -7.7pp
526	    - method: DivEye features
527	      acc_6class: 0.432
528	      mae_6class: 0.612
529	      acc_4class: 0.698
530	      delta_vs_best: -10.6pp
531	    - method: LOKI features
532	      acc_6class: 0.408
533	      mae_6class: 0.641
534	      acc_4class: 0.672
535	      delta_vs_best: -13.0pp
536	    - method: Perplexity regression
537	      acc_6class: 0.389
538	      mae_6class: 0.673
539	      acc_4class: 0.651
540	      delta_vs_best: -14.9pp
541	    - method: Zero-shot GPT-4o
542	      acc_6class: 0.287
543	      mae_6class: 0.892
544	      acc_4class: 0.418
545	      delta_vs_best: -25.1pp
546	  figures_description:
547	  - 'Fig: 所有方法的6-class acc bar chart，按性能排序，chance line标注'
548	  - 'Fig: MAE vs accuracy scatter plot，DCOL在Pareto前沿'
549	  analysis: 'Baseline battery确认DCOL优于所有baseline但优势中等。CORAL作为最强competitor 说明ordinal
550	    structure是关键——DCOL的额外+3.3pp来自learned margins和contrastive learning， 但大部分gain来自ordinal
551	    formulation本身。这强化median叙事的重心： "ordinal框架是核心贡献，DCOL是该框架下的一个strong实现"。 Zero-shot
552	    LLM的失败是一个有趣的negative result，值得在paper中简短讨论。
553	
554	    '
555	- name: DCOL component ablation
556	  plan_id: plan_010
557	  description: 移除surprisal anchors / learnable margins / strategy conditioning各一个，测量增量贡献
558	  expected_results:
559	    full_dcol:
560	      acc_6class: 0.571
561	      mae_6class: 0.462
562	    ablation_no_surprisal_anchors:
563	      acc_6class: 0.558
564	      mae_6class: 0.475
565	      delta_pp: -1.3
566	    ablation_no_learnable_margins:
567	      acc_6class: 0.547
568	      mae_6class: 0.485
569	      delta_pp: -2.4
570	    ablation_no_strategy_conditioning:
571	      acc_6class: 0.562
572	      mae_6class: 0.469
573	      delta_pp: -0.9
574	    ablation_none_of_three:
575	      acc_6class: 0.531
576	      mae_6class: 0.498
577	      delta_pp: -4.0
578	  result_rationale: 'Learnable margins的消融影响最大（-2.4pp），因为inter-depth距离的非均匀性是 递归退化的核心特征——fixed
579	    margins迫使模型假设所有相邻depth等距，这与实际不符。 Surprisal anchors的消融影响次之（-1.3pp），因为var_surprisal是最强特征，
580	    将其嵌入anchor selection有助于contrastive learning聚焦于最有信息量的样本对。 Strategy conditioning影响最小（-0.9pp），因为在pooled
581	    setting下策略间差异 已经被训练数据的多样性部分覆盖——conditioning的主要作用是在per-strategy evaluation 上提升，pooled数字上反映较弱。三个组件全部移除等价于vanilla
582	    DeBERTa + N-pair loss， acc降至0.531，仍高于CORAL（0.538→此处应低于CORAL），说明N-pair contrastive
583	    loss 本身相比CORAL的rank loss有约-0.7pp的差距，三个text-specific modifications 弥补了这个差距并额外提升+4.0pp。
584	
585	    '
586	  tables:
587	  - name: 'Table: DCOL ablation'
588	    rows:
589	    - variant: Full DCOL
590	      acc_6class: 0.571
591	      delta: —
592	    - variant: – strategy conditioning
593	      acc_6class: 0.562
594	      delta: '-0.9'
595	    - variant: – surprisal anchors
596	      acc_6class: 0.558
597	      delta: '-1.3'
598	    - variant: – learnable margins
599	      acc_6class: 0.547
600	      delta: '-2.4'
601	    - variant: – all three (vanilla contrastive)
602	      acc_6class: 0.531
603	      delta: '-4.0'
604	  figures_description:
605	  - 'Fig: Ablation waterfall chart，从vanilla到full DCOL的累积增益'
606	  analysis: '每个组件贡献1-2.4pp，没有单一组件是决定性的。这对median叙事的含义： DCOL的三个text-specific modifications各自有小但一致的贡献，
607	    组合起来提供了4pp的总增益。论文应将此framing为"method engineering"而非"method breakthrough"。
608	
609	    '
610	- name: Depth extension to 5+ generations and EDD analysis
611	  plan_id: plan_011
612	  description: Pythia链延伸到depth 5，分析depth 3-5的信号饱和
613	  expected_results:
614	    pythia_extended_auc_3v4: 0.708
615	    pythia_extended_auc_4v5: 0.621
616	    pythia_extended_auc_5v6: 0.573
617	    feature_overlap_depth4_5_bhattacharyya: 0.82
618	    feature_overlap_depth5_6_bhattacharyya: 0.91
619	    edd_pythia_extended: 3
620	    depth4_5_top_feature_rank_change: zipf_alpha从rank 4升至rank 2，var_surprisal从rank
621	      1降至rank 3
622	  result_rationale: '延伸到depth 5-6后，AUC持续下降：3v4=0.708（已低于原EDD阈值0.72），4v5=0.621， 5v6=0.573（接近random的0.5）。Bhattacharyya
623	    overlap从depth 4-5的0.82升至depth 5-6的0.91， 说明特征分布高度重叠。EDD仍为3，因为depth 3v4已低于0.72。
624	    有趣的现象：在depth 4+，var_surprisal不再是最区分性特征，因为surprisal的variance 已经被"压缩到底"——所有深层生成文本的surprisal分布都变得窄且相似。
625	    此时zipf_alpha变得相对更区分，因为词频分布的Zipf参数对极深层退化仍有微弱敏感度。 这种feature rank变化是Atlas中一个有价值的发现点。
626	
627	    '
628	  tables:
629	  - name: 'Table: Extended depth AUC (Pythia, nucleus)'
630	    rows:
631	    - pair: 0v1
632	      auc: 0.998
633	    - pair: 1v2
634	      auc: 0.861
635	    - pair: 2v3
636	      auc: 0.801
637	    - pair: 3v4
638	      auc: 0.708
639	    - pair: 4v5
640	      auc: 0.621
641	    - pair: 5v6
642	      auc: 0.573
643	  figures_description:
644	  - 'Fig: AUC decay curve across 6 adjacent pairs，EDD=3阈值线标注'
645	  - 'Fig: Top-5 feature importance随depth pair变化的stream plot，显示rank crossover'
646	  analysis: '延伸实验定量确认了depth 3是"有效区分边界"——depth 3之后的AUC衰减斜率平缓化， 趋向0.5。这为EDD=3提供了额外的经验支持。Feature
647	    rank变化的发现值得在Atlas section 详细讨论，因为它说明"退化不只是''所有特征同步衰减''而是''不同退化阶段的主导信号切换''"。
648	
649	    '
650	- name: Granularity ablation
651	  plan_id: plan_012
652	  description: 对比binary / 3-class / 4-class / 6-class分类粒度
653	  expected_results:
654	    binary_acc: 0.946
655	    binary_auc: 0.983
656	    three_class_acc: 0.867
657	    three_class_mae: 0.141
658	    four_class_acc: 0.823
659	    four_class_mae: 0.192
660	    six_class_acc: 0.571
661	    six_class_mae: 0.462
662	    chance_levels:
663	      binary: 0.5
664	      three_class: 0.333
665	      four_class: 0.25
666	      six_class: 0.167
667	    lift_over_chance:
668	      binary: +44.6pp
669	      three_class: +53.4pp
670	      four_class: +57.3pp
671	      six_class: +40.4pp
672	  result_rationale: 'Binary（depth 0 vs depth 1+）几乎perfect（0.946），因为depth 0→1的gap远大于其他对。
673	    随粒度增加，absolute acc下降但lift over chance先增后减：4-class的lift最高（+57.3pp）， 说明4-class是"信息量/可行性"的最优平衡点。6-class的lift降至+40.4pp，
674	    因为depth 4和depth 5的加入拖累了整体——它们与depth 3高度混淆。 3-class（0,1,2+）的0.867说明"有多深"这个问题在粗粒度上非常可行。
675	    这些数字共同支持论文叙事：ordinal depth estimation在EDD内可行， 推荐4-class作为实际应用的粒度选择，6-class数字仅作为upper
676	    bound report。
677	
678	    '
679	  tables:
680	  - name: 'Table: Granularity ablation (DCOL, pooled)'
681	    rows:
682	    - granularity: Binary (0 vs 1+)
683	      acc: 0.946
684	      chance: 0.5
685	      lift_pp: 44.6
686	    - granularity: 3-class (0,1,2+)
687	      acc: 0.867
688	      chance: 0.333
689	      lift_pp: 53.4
690	    - granularity: 4-class (0,1,2,3+)
691	      acc: 0.823
692	      chance: 0.25
693	      lift_pp: 57.3
694	    - granularity: 6-class (0-5)
695	      acc: 0.571
696	      chance: 0.167
697	      lift_pp: 40.4
698	  figures_description:
699	  - 'Fig: Accuracy vs granularity折线图，附chance baseline和lift标注'
700	  analysis: '4-class是sweet spot的结论直接支持EDD=3叙事，也回应了reviewer concern "EDD might be low"。
701	    论文可以argue：4-class粒度（0=原始, 1=first gen, 2=second gen, 3+=deep recursive） 在curation场景中已经足够——用户最需要区分的是"原始vs浅层生成vs深层递归"。
702	
703	    '
704	- name: Downstream curation proof-of-concept
705	  plan_id: plan_013
706	  description: Depth-graduated weighting vs binary filtering，在1B模型fine-tuning上测试
707	  expected_results:
708	    binary_filter_ppl: 18.72
709	    graduated_weighting_ppl: 18.14
710	    no_filter_ppl: 19.85
711	    oracle_depth_weighting_ppl: 17.91
712	    ppl_reduction_graduated_vs_binary_pct: 3.1
713	    ppl_reduction_graduated_vs_nofilter_pct: 8.6
714	    graduated_vs_binary_p_value: 0.038
715	    downstream_task_acc_binary: 0.724
716	    downstream_task_acc_graduated: 0.731
717	    downstream_task_acc_nofilter: 0.703
718	  result_rationale: 'Graduated weighting（1/k权重，k=predicted depth+1）的PPL比binary低3.1%，
719	    处于median的[2,5]范围内。p-value=0.038勉强显著（<0.05），但远未达到强显著。 这是因为graduated weighting的优势主要来自对depth
720	    1-2的差异化处理—— binary filter将所有"synthetic"同等对待，而graduated保留了quality尚可的depth 1内容 并只强力down-weight
721	    depth 2+。Oracle depth weighting（用真实depth而非predicted） 的PPL=17.91比graduated的18.14低，gap=1.3%说明prediction
722	    error（DCOL的misclassification） 确实影响了curation效果，但graduated仍然明显优于binary。 Downstream
723	    task acc的差距更小（0.731 vs 0.724），因为PPL的差异在传导到task performance 时会被衰减。在median档下，这个proof-of-concept足以"展示方向"但不能做强声明。
724	
725	    '
726	  tables:
727	  - name: 'Table: Curation comparison'
728	    rows:
729	    - method: No filter
730	      ppl: 19.85
731	      task_acc: 0.703
732	    - method: Binary filter (remove synthetic)
733	      ppl: 18.72
734	      task_acc: 0.724
735	    - method: Graduated weighting (predicted depth)
736	      ppl: 18.14
737	      task_acc: 0.731
738	    - method: Oracle weighting (true depth)
739	      ppl: 17.91
740	      task_acc: 0.738
741	  figures_description:
742	  - 'Fig: 4种curation策略的PPL对比bar chart，with error bars'
743	  - 'Fig: Weighting function sensitivity分析——1/k vs 1/k² vs exponential decay'
744	  analysis: '3.1%的PPL reduction和p=0.038的显著性在median档下是"正向但不强"的结果。 论文应将此section控制在~1页，framing为proof-of-concept，明确stated
745	    limitation： (1) 只在一个model scale上测试，(2) graduated vs binary的差距在error bar内有overlap，
746	    (3) curation效果依赖depth prediction质量。
747	
748	    '
749	- name: 7B cross-scale probe
750	  plan_id: plan_014
751	  description: Qwen2.5-7B或Llama-3.1-8B生成3层递归链，用小模型训练的DCOL做zero-shot迁移
752	  expected_results:
753	    zero_shot_transfer_4class_acc: 0.614
754	    zero_shot_transfer_6class_acc: 0.372
755	    fine_tuned_on_7b_4class_acc: 0.791
756	    edd_7b_nucleus: 3
757	    edd_7b_temperature: 2
758	    auc_0v1_7b: 0.989
759	    auc_1v2_7b: 0.824
760	    auc_2v3_7b: 0.741
761	  result_rationale: '7B模型的生成质量显著高于1-1.5B模型，导致递归退化信号更弱——更好的模型在浅层 生成"更像人类"的文本，depth信号被压缩。Zero-shot
762	    transfer的4-class acc 0.614 远低于in-distribution的0.823，说明1.5B模型上学到的表示不能直接迁移到7B。 这是因为7B模型的"depth
763	    1"文本质量接近1.5B模型的"depth 0"，导致decision boundary错位。 但fine-tune后恢复到0.791，说明depth信号在7B上仍然存在，只是需要recalibration。
764	    EDD在7B上仍为3（nucleus）但temperature降至2，因为7B+temperature的生成多样性 使得depth 2→3就已不可区分。这进一步支持了Atlas中"模型能力越强，EDD越可能降低"的假设。
765	
766	    '
767	  tables:
768	  - name: 'Table: Cross-scale transfer (7B)'
769	    rows:
770	    - setting: Zero-shot (train on 1-1.5B, test on 7B)
771	      acc_4class: 0.614
772	      acc_6class: 0.372
773	    - setting: Fine-tuned on 7B data
774	      acc_4class: 0.791
775	      acc_6class: 0.518
776	    - setting: 1-1.5B in-distribution (reference)
777	      acc_4class: 0.823
778	      acc_6class: 0.571
779	  figures_description:
780	  - 'Fig: 小模型vs大模型的feature分布对比violin plot——7B的分布更紧凑'
781	  analysis: 'Cross-scale transfer是limitation而非failure。Zero-shot的gap说明需要scale-aware
782	    calibration，但fine-tune后的接近恢复说明depth信号是universal的，只是magnitude不同。 论文中这可以framing为future
783	    work方向：scale-invariant depth estimation。
784	
785	    '
786	- name: Wild-data calibration
787	  plan_id: plan_015
788	  description: DCOL depth scores on RedPajama/Dolma vs perplexity/AlignScore质量代理
789	  expected_results:
790	    spearman_dcol_vs_ppl: 0.341
791	    spearman_dcol_vs_alignscore: 0.283
792	    spearman_dcol_vs_ppl_p_value: 0.002
793	    spearman_dcol_vs_alignscore_p_value: 0.014
794	    pct_wild_data_scored_depth0: 0.72
795	    pct_wild_data_scored_depth1plus: 0.28
796	    pct_wild_data_scored_depth3plus: 0.06
797	  result_rationale: 'Wild data上没有ground-truth depth，只能用proxy验证。Spearman相关0.341（DCOL
798	    score vs PPL） 是中等正相关——高DCOL depth score（预测为深层递归）的文本确实倾向于有更高perplexity， 但相关性不强，因为wild
799	    data中高PPL的原因很多（不只是递归深度还有domain、quality等）。 AlignScore的相关更弱（0.283），因为AlignScore衡量的是factual
800	    consistency而非statistical degradation——递归深度高不一定意味着factually inconsistent。 72%的wild
801	    data被scored为depth 0是合理的——大部分web text仍然是人类写的。 6%被scored为depth 3+可能overestimate，因为模型在controlled
802	    setting训练， wild data中的低质量人类文本可能被误判为深层递归。 p-values显著但相关系数中等，符合median档"有正向信号但不强"的预期。
803	
804	    '
805	  tables:
806	  - name: 'Table: Wild-data correlation with quality proxies'
807	    rows:
808	    - proxy: Perplexity (GPT-2)
809	      spearman: 0.341
810	      p_value: 0.002
811	    - proxy: AlignScore
812	      spearman: 0.283
813	      p_value: 0.014
814	  - name: 'Table: Predicted depth distribution on RedPajama sample'
815	    rows:
816	    - depth: 0 (human)
817	      pct: 72
818	    - depth: '1'
819	      pct: 16
820	    - depth: '2'
821	      pct: 6
822	    - depth: 3+
823	      pct: 6
824	  figures_description:
825	  - 'Fig: DCOL predicted depth vs perplexity散点图（RedPajama 10K sample），with regression
826	    line'
827	  - 'Fig: Predicted depth分布histogram on wild data'
828	  analysis: Wild-data结果只能作为calibration而非validation。中等相关说明DCOL的depth score 在wild setting下有一定语义一致性，但controlled→wild的gap明显。
829	    论文应将此作为"ecological validity probe"而非core result， 明确声明"controlled setting是primary，wild
830	    transfer是future work"。
831	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bac1a146-7909-489a-b8e1-27c79daecfc4",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "61440c5e-de5d-4c2e-a4bc-99117c8ce5b4",
  "sourceToolAssistantUUID": "bac1a146-7909-489a-b8e1-27c79daecfc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-14T14:52:09.183Z_

Now let me check the best tier's review report for context on what R1 covered.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61440c5e-de5d-4c2e-a4bc-99117c8ce5b4",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2efZTEvcCexpmAVMTzu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b9fd77b-0968-4762-95e2-7654590ca8cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFZTF8BpAkiydGLdmPk8oL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28134,
      "cache_read_input_tokens": 25072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28134,
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

_source line 34 · 2026-05-14T14:52:11.544Z_

<details open><summary>🔧 Tool call — Read · `toolu_0111sPREcmS34VURc9xBotfw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b9fd77b-0968-4762-95e2-7654590ca8cb",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2efZTEvcCexpmAVMTzu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62b32ade-e332-4f37-8b1d-5ab68f21761d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFZTF8BpAkiydGLdmPk8oL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28134,
      "cache_read_input_tokens": 25072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28134,
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

_source line 35 · 2026-05-14T14:52:11.550Z_

<details><summary>↩ Tool result · `toolu_0111sPREcmS34VURc9xBotfw`</summary>

```text
1	---
2	dream_id: dream_20260514T140607
3	tier: best
4	overall_score: borderline accept
5	timestamp: 2026-05-14T14:48:22.312721+00:00
6	---
7	
8	
9	# Dream Review Report: Ordinal Depth Estimation of Recursive LLM Generations via Contrastive Learning with Learnable Margins
10	
11	**Venue:** EMNLP 2026 (ACL Rolling Review)
12	**Review Mode:** Full (2 Reviewers + Roundtable)
13	**Date:** 2026-05-14
14	
15	---
16	
17	## Reviewer Scores Summary
18	
19	| Dimension | R1 (Methods+Experiments) | R2 (Novelty+Related Work) | Consensus |
20	|-----------|--------------------------|---------------------------|-----------|
21	| Soundness | 3/5 | 4/5 | 3.5/5 |
22	| Excitement | 4/5 | 3/5 | 3.5/5 |
23	| Overall Assessment | 3/5 | 3/5 | **3/5 (Borderline Accept)** |
24	| Confidence | 4/5 | 4/5 | — |
25	
26	---
27	
28	## R1 Review: Methods and Experiments
29	
30	### Summary
31	
32	The paper formalizes ordinal generation depth estimation and proposes DCOL with three text-specific modifications atop a DeBERTa encoder. Experimental coverage is impressive (14 experiments spanning benchmark construction, generalization, ablation, and downstream application), and the Atlas provides a useful empirical characterization. However, several methodological concerns — the loss formulation, surprisal circularity, benchmark confounds, and underspecified inference — prevent full endorsement.
33	
34	### Strengths
35	
36	1. **Comprehensive experimental design.** All 14 planned experiments are covered. The combination of leave-one-model-out (Table 8), leave-one-strategy-out (Table 9), cross-scale transfer (Table 10), ablation (Table 11), granularity analysis (Table 12), wild-data calibration (Table 13), and downstream application (Table 14) addresses most natural reviewer questions preemptively.
37	
38	2. **Well-motivated method design.** The observation-to-design-to-validation loop is clean: the Atlas documents non-uniform inter-depth geometry (d01/d34 ratio = 2.83), this motivates learnable non-uniform margins, and the learned margin ratios (1.00, 0.68, 0.52, 0.41, 0.35) correlate strongly (r > 0.95) with the empirical distances.
39	
40	3. **Strong baselines and fair comparisons.** Seven baselines spanning binary detector repurposing, ordinal regression, standard classification, direct regression, and zero-shot prompting. The inclusion of CORAL-DeBERTa (same encoder) isolates DCOL's modifications from encoder choice.
41	
42	4. **Ablation is convincing.** Each component contributes 2–4pp independently; sum of individual drops (9.2pp) slightly exceeds joint drop (8.1pp) indicating mild positive interaction; "w/o all three" (64.1%) still outperforms CORAL (62.1%) by 2.0pp, cleanly separating framework from modification contributions.
43	
44	5. **Atlas as independent scientific contribution.** The EDD metric, monotonicity analysis, and non-uniform geometry documentation have value beyond DCOL. var_surprisal's 0.961 monotonicity is a genuinely useful result for the model collapse community.
45	
46	6. **Statistical significance reported** for DCOL vs. CORAL (paired bootstrap, p < 0.001) with confidence intervals for key metrics.
47	
48	### Weaknesses
49	
50	1. **(Major) Loss formulation (Eq. 1) appears incomplete.** The loss L = Σ max(0, ||f(xi) - f(xj)|| - m(δij))² only penalizes when embedding distance *exceeds* the margin — a ceiling/pull term. There is no repulsive mechanism pushing apart samples at different depths. As written, the loss is trivially minimized by collapsing all embeddings to a single point. Either this is a presentation error (missing the repulsive term) or additional loss terms exist but are not described. This is a critical reproducibility concern.
51	
52	2. **(Major) Circularity in surprisal-augmented anchors.** The surprisal features appear to be computed using Pythia-1.4B as reference model. For Pythia-generated text, this creates a tautological signal — the generating model's own surprisal on its own output conflates model identity with depth. The paper does not specify: (a) which reference model is used across all three families, (b) whether the same reference is used for all text, (c) how this affects cross-model generalization. The surprisal anchors contribute 3.1pp in ablation, so this is not ignorable.
53	
54	3. **(Major) Depth-0 confound.** Depth-0 is Wikipedia (human); depths 1–5 are model-generated. The d0 vs. d1 AUC of 0.998 is essentially binary human-vs-machine detection, not depth estimation. Per-class accuracy (d0: 91.2% vs. d1: 79.3%) and binary detection (96.1%) confirm the d0 signal is dominated by the human-vs-synthetic distinction. The 72.2% headline is substantially inflated by near-perfect d0 classification. A 5-class (d1–d5) accuracy should be reported alongside.
55	
56	4. **(Major) k-NN inference underspecified.** No k value, distance metric, or sensitivity analysis provided. If results are brittle to k, the method has a hidden hyperparameter undermining reported numbers.
57	
58	5. **(Minor) Cross-scale evaluation is limited.** The 8B probe uses only 3-class (depth 0–2), making it incomparable to 6-class main results. Only one larger model tested, only to depth 2. The claim "depth signals transfer across model scales" is stronger than this evidence supports.
59	
60	6. **(Minor) Downstream curation lacks task-based evaluation.** PPL on held-out RedPajama subset could reflect distributional matching rather than genuine quality improvement. No evaluation on downstream tasks (MMLU, reasoning).
61	
62	7. **(Minor) No error analysis.** No discussion of what text properties make depth estimation harder, no confusion matrix shown (only described).
63	
64	8. **(Minor) Wild-data calibration has no ground truth.** Correlations with PPL/AlignScore are suggestive but could mean DCOL is learning a perplexity proxy. Partial correlation (-0.198) mitigates this partially.
65	
66	### Questions for Authors
67	
68	1. Provide the complete training objective including the repulsive/floor term.
69	2. Which reference model computes surprisal? Is it the same for all three model families?
70	3. What k is used in k-NN? What is the sensitivity?
71	4. What is the 5-class (d1–d5 only) accuracy?
72	5. How is the margin monotonicity constraint implemented (projection? reparameterization?)?
73	6. How is strategy conditioning handled at inference on wild data where strategy is unknown?
74	7. Has depth-0 been tested with non-Wikipedia seed corpora?
75	8. Can you provide error bars for the non-monotonic d4v5 AUC in Table 4?
76	
77	### Scores
78	- Soundness: 3/5
79	- Excitement: 4/5
80	- Overall Assessment: 3/5
81	- Confidence: 4/5
82	
83	---
84	
85	## R2 Review: Novelty and Related Work
86	
87	### Summary
88	
89	The paper introduces a well-defined new task (ordinal depth estimation) and provides the first systematic characterization of recursive degradation dynamics (Atlas). However, the DCOL method is an incremental adaptation of CLOC (CVPR 2025) with three standard engineering modifications, the related work has significant gaps, and certain claims are overstated relative to the evidence.
90	
91	### Strengths
92	
93	1. **Genuine task novelty.** Ordinal depth estimation is a legitimately new problem formulation. The insight that binary detection discards actionable ordinal information is simple but important. The task definition is clean and the benchmark construction is well-motivated.
94	
95	2. **Atlas is a meaningful scientific contribution.** The systematic characterization of 19 features across 3 models × 3 strategies × 6 depths, the EDD metric, and the documentation of non-uniform inter-depth geometry go beyond what Drayson et al. (2025) provide. Drayson et al. characterize degradation in Pythia only; this paper extends to three architectures and formalizes the findings.
96	
97	3. **The graduated curation paradigm is a useful conceptual contribution.** Even as a proof-of-concept, the insight that depth-aware weighting is a Pareto improvement over binary filtering (more data retained, lower PPL) is valuable for the data curation community.
98	
99	4. **Comprehensive evaluation.** The paper addresses cross-model, cross-strategy, and cross-scale generalization — a thorough treatment of the external validity question.
100	
101	5. **Elegant granularity analysis.** The finding that above-chance margin *increases* with finer granularity (Table 12) is a genuinely surprising and well-presented result that justifies the ordinal framing.
102	
103	### Weaknesses
104	
105	1. **(Major) Incremental methodology.** DCOL is CLOC + three off-the-shelf modifications:
106	   - Learnable margins are standard in metric learning (Wu et al. 2017, Roth et al. 2020).
107	   - Surprisal-augmented anchors are feature concatenation before a projection head — a standard technique.
108	   - Strategy-aware conditioning is a lightweight FiLM-style modulation.
109	   Each contributes only 2–4pp. The paper should position DCOL as "CLOC adapted for text depth estimation" rather than a novel framework. The novelty lies in the task and the Atlas, not the method.
110	
111	2. **(Major) Significant related work gaps.**
112	   - **Watermarking:** Kirchenbauer et al. (2023) is entirely absent — watermarking-based provenance tracking is a direct alternative to post-hoc depth estimation.
113	   - **Data quality / curation:** DSIR (Xie et al. 2023), QuRating (Wettig et al. 2024) — the graduated curation contribution should be positioned against the data selection literature.
114	   - **Multi-class synthetic attribution:** Uchendu et al. (2020) and subsequent work on authorship attribution across multiple generators — a precursor to multi-class synthetic text analysis.
115	   - **Data provenance:** The broader data attribution and provenance literature (e.g., data Shapley, influence functions) is relevant to tracking generation history.
116	   - **Model collapse theory:** Alemohammad et al. (2023) "Self-Consuming Generative Models Go MAD" and Briesch et al. (2023) are missing.
117	   - **Binary detection:** Fast-DetectGPT (Bao et al. 2024) should be included in the baseline battery.
118	
119	3. **(Major) Overstated "fundamentally different" claim.** The paper claims ordinal depth estimation is "fundamentally different from binary detection" (Section 1). But the features powering depth estimation (surprisal variance, perplexity statistics) are the *same* features used by binary detectors. The contribution is an ordinal *generalization* of binary detection — important, but not "fundamentally different." A more honest framing: "binary detection is a special case; ordinal estimation extracts strictly more information from the same signal space."
120	
121	4. **(Minor) Circularity in margin-geometry validation.** Reporting Pearson r > 0.95 between learned margins and empirical inter-depth distances is circular: the margins were *trained* on the same data from which the Atlas distances were computed. The margins *should* correlate — this validates convergence, not the design principle. A genuine validation would train margins on one model family and show they match the Atlas geometry of a held-out family.
122	
123	5. **(Minor) EDD threshold sensitivity.** EDD is defined with a fixed AUC ≥ 0.75 threshold. No sensitivity analysis is provided. If the threshold were 0.80, EDD values would change substantially (several entries in Table 2 would drop by 1). The paper should discuss threshold choice or provide a range.
124	
125	6. **(Minor) Graduated vs. binary comparison fairness.** Binary filtering retains 71.6% of data; graduated retains 92.3%. The PPL improvement could partly reflect having 20% more training data, not the weighting scheme. A fair comparison would match data volume — e.g., binary filtering with a higher threshold retaining ~92% of data.
126	
127	### Questions for Authors
128	
129	1. How does DCOL differ from CLOC beyond the three modifications? Is the base contrastive framework identical?
130	2. Can the margin-geometry correlation be validated on a held-out model family not used in training?
131	3. What happens to EDD if the threshold is changed to 0.70 or 0.80?
132	4. Is the reference model for surprisal features the same model that generated the text? How does this affect the claim that depth signals are "model-agnostic"?
133	5. Has the graduated curation been compared against volume-matched binary filtering (same data retention rate)?
134	6. How does DCOL handle text generated by mixed or unknown strategies in deployment?
135	
136	### Missing References
137	
138	- Kirchenbauer et al. (2023) — watermarking for LLM outputs
139	- Xie et al. (2023) — DSIR data selection
140	- Wettig et al. (2024) — QuRating data quality
141	- Uchendu et al. (2020) — multi-class authorship attribution for generators
142	- Alemohammad et al. (2023) — self-consuming generative models
143	- Briesch et al. (2023) — LLMs suffering from own output
144	- Bao et al. (2024) — Fast-DetectGPT
145	- Guo et al. (2024) — linguistic diversity decline in recursive generations
146	
147	### Scores
148	- Soundness: 4/5
149	- Excitement: 3/5
150	- Overall Assessment: 3/5
151	- Confidence: 4/5
152	
153	---
154	
155	## Roundtable Discussion
156	
157	### Step 2: Cross-Sharing
158	
159	R1 and R2 exchanged reviews. Key observations from each reviewer on the other's points:
160	
161	**R1 on R2's concerns:**
162	- Agrees that DCOL's novelty is incremental — the observation-to-design loop is clean but the components themselves are standard. The paper's main novelty is the task + Atlas, not DCOL per se.
163	- Agrees the related work gaps are significant, especially watermarking (Kirchenbauer et al.) and data curation literature (DSIR, QuRating).
164	- Notes the "fundamentally different" framing is indeed overstated — "ordinal generalization" is more accurate.
165	
166	**R2 on R1's concerns:**
167	- Agrees the loss formulation issue (Eq. 1 missing repulsive term) is the single most critical technical concern. If this is a presentation error, it's fixable; if it's a genuine design flaw, it undermines the entire method.
168	- Finds the d0 confound argument compelling — the 6-class headline number is inflated. A 5-class (d1–d5) metric should be foregrounded.
169	- The surprisal circularity is concerning but considers it partially mitigated by the cross-model LOO results (60.1%) where the reference model is presumably not the generating model for the held-out family.
170	
171	### Step 3: Convergence
172	
173	**Points of agreement:**
174	1. The **task formulation** (ordinal depth estimation) is genuinely novel and timely — both reviewers value this.
175	2. The **Atlas** is an independent scientific contribution with value beyond DCOL.
176	3. The **loss formulation** in Eq. 1 is either incomplete or incorrectly presented — this is the top priority for revision.
177	4. The **related work** has significant gaps that need addressing (watermarking, data curation, multi-class attribution).
178	5. The **6-class headline** is inflated by the d0 confound — a d1–d5 metric should be reported.
179	6. The **DCOL method** is technically competent but incrementally novel — the paper should reframe DCOL as an adaptation of CLOC, not a novel framework.
180	7. The **experimental coverage** is a clear strength — 14 experiments addressing diverse validity questions.
181	8. **Overall assessment: 3/5** (borderline accept) — the task and Atlas are strong enough to carry the paper, but methodological and positioning issues need attention.
182	
183	**Points of partial disagreement:**
184	- R1 rates Excitement 4/5 (problem is highly novel and timely), R2 rates 3/5 (execution is incremental). Convergence: **3.5/5** — the problem is exciting but the methodological contribution is moderate.
185	- R1 rates Soundness 3/5 (loss formulation, circularity), R2 rates 4/5 (experimental design is thorough). Convergence: **3.5/5** — sound experimental design with a critical presentation gap in the loss function.
186	
187	### Step 4: Consolidated Assessment
188	
189	**Overall Score: 3/5 — Borderline Accept**
190	
191	**Verdict:** This paper makes a genuine contribution by formalizing a new task (ordinal depth estimation) and providing the first cross-model empirical characterization of recursive degradation dynamics. The experimental coverage is exemplary. However, the paper has three categories of issues that prevent a strong accept:
192	
193	**(1) Critical technical gap:** The loss function (Eq. 1) as presented is incomplete — it lacks a repulsive term and would be trivially minimized by embedding collapse. This must be clarified for reproducibility.
194	
195	**(2) Positioning and framing issues:** DCOL is an incremental adaptation of CLOC, not a novel framework. The "fundamentally different from binary detection" claim is overstated. The 6-class headline is inflated by the near-trivial d0 classification. The related work has notable gaps (watermarking, data curation, multi-class attribution).
196	
197	**(3) Methodological concerns:** Surprisal anchor circularity, k-NN inference underspecification, limited cross-scale evaluation, and the downstream curation experiment lacking task-based evaluation.
198	
199	**If the authors address (1) and (2) in revision — clarifying the complete loss, repositioning DCOL as adapted-CLOC, reporting d1–d5 accuracy, and filling related work gaps — the paper would likely reach a solid accept.** The task formalization and Atlas alone justify publication at a top venue if the method section meets basic reproducibility standards.
200	
201	**Recommendation for authors (priority-ordered):**
202	1. Provide the complete training loss (including repulsive/floor term)
203	2. Report 5-class (d1–d5) accuracy as a secondary headline metric
204	3. Clarify the reference model used for surprisal computation
205	4. Specify k-NN hyperparameters and sensitivity
206	5. Add missing citations (Kirchenbauer, DSIR, Alemohammad, Fast-DetectGPT, Uchendu)
207	6. Reframe DCOL as "CLOC adapted for text depth estimation" — the novelty is the task + Atlas
208	7. Add EDD threshold sensitivity analysis
209	8. Discuss graduated vs. binary curation with matched data volume
210	
211	---
212	
213	## Experiment Coverage Assessment
214	
215	All 14 imagined experiments are represented in the paper:
216	
217	| # | Experiment | Status | Coverage Quality |
218	|---|-----------|--------|-----------------|
219	| 1 | OLMo-1B Recursive Chain | ✓ | Table 3 — full results |
220	| 2 | GPT-2 XL Recursive Chain | ✓ | Table 3 — full results |
221	| 3 | DCOL Training | ✓ | Tables 5, 6 — full results |
222	| 4 | Leave-One-Model-Out | ✓ | Table 8 — full results |
223	| 5 | Depth Degradation Atlas | ✓ | Tables 1, 2, §3.4 — comprehensive |
224	| 6 | Leave-One-Strategy-Out | ✓ | Table 9 — full results |
225	| 7 | DeBERTa E2E | ✓ | Table 7 — full results |
226	| 8 | Baseline Battery | ✓ | Table 5 — 7 baselines |
227	| 9 | DCOL Ablation | ✓ | Table 11 — full results |
228	| 10 | Depth Extension | ✓ | Table 4, §5.2 — full results |
229	| 11 | Granularity Ablation | ✓ | Table 12 — full results |
230	| 12 | Graduated Curation | ✓ | Table 14 — full results |
231	| 13 | 7B Cross-Scale Probe | ✓ | Table 10 — reduced scope (3-class) |
232	| 14 | Wild-Data Calibration | ✓ | Table 13 — full results |
233	
234	**Coverage: 14/14 experiments present.** The cross-scale probe (#13) has reduced scope (3-class instead of 6-class, depth 0–2 only), which is noted as a minor weakness. All other experiments match or exceed the imagined design's scope.
235	
236	**Notable:** The paper includes no figures (only tables), which is unusual for a 10-page paper at EMNLP. The imagined experiment design describes several key visualizations (confusion matrix heatmap, Atlas heatmap grid, AUC decay curves, feature importance comparison, t-SNE, waterfall chart) that are entirely absent from the paper. This is a significant presentation gap — these visualizations would substantially improve readability and impact.
237	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62b32ade-e332-4f37-8b1d-5ab68f21761d",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "1cbcc4ea-6aba-4572-ae1b-22acfbb1c096",
  "sourceToolAssistantUUID": "62b32ade-e332-4f37-8b1d-5ab68f21761d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T14:52:12.728Z_

<details open><summary>🔧 Tool call — Read · `toolu_019HsVe5feb8GxpoAnQ77LFR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/imagined_experiments.yaml",
  "offset": 0,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cbcc4ea-6aba-4572-ae1b-22acfbb1c096",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2efZTEvcCexpmAVMTzu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a537658-49d0-4204-8388-02a9db6b5730",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFZTF8BpAkiydGLdmPk8oL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28134,
      "cache_read_input_tokens": 25072,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 28134
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 246,
          "cache_read_input_tokens": 25072,
          "cache_creation_input_tokens": 28134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 28134,
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

_source line 37 · 2026-05-14T14:52:12.733Z_

<details><summary>↩ Tool result · `toolu_019HsVe5feb8GxpoAnQ77LFR`</summary>

```text
0	tier: median
1	narrative_guidance: 'EDD≈3是核心科学发现，论文叙事围绕"ordinal depth estimation在EDD边界内可行"展开。 DCOL优于baseline但优势中等（+3-7pp），叙事重心从方法突破转向"序数框架+Atlas"的组合贡献。
2	  Atlas权重上升为论文核心——文档化递归退化的边界和模式对model collapse社区直接有用。 Claim 3缩减为proof-of-concept。跨模型泛化诚实报告per-rotation结果，弱rotation作为limitation。
3	  有效粒度声明降级：6-class数字报告但承认depth 4+坍缩，实际可行粒度为4-class（depths 0-3）。
4	
5	  '
6	imagined_experiments:
7	- name: OLMo-1B recursive chain benchmark
8	  plan_id: plan_002
9	  description: OLMo-1B在3种策略下生成5层递归链，提取19维统计特征，RF分类
10	  expected_results:
11	    full_4class_acc: 0.754
12	    full_4class_acc_ci:
13	    - 0.74
14	    - 0.768
15	    full_mae: 0.268
16	    full_auc_0v1: 0.994
17	    full_auc_1v2: 0.838
18	    full_auc_2v3: 0.771
19	    filtered_4class_acc: 0.789
20	    filtered_4class_acc_ci:
21	    - 0.775
22	    - 0.803
23	    filtered_mae: 0.225
24	    best_model: RandomForest
25	    top_features:
26	    - var_surprisal
27	    - mean_ppl
28	    - p90_ppl
29	    - zipf_alpha
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a537658-49d0-4204-8388-02a9db6b5730",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "6d7ea2fa-4a5d-4d56-bb90-0dcc4d97d5c3",
  "sourceToolAssistantUUID": "7a537658-49d0-4204-8388-02a9db6b5730",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-14T14:52:16.692Z_

Now I have comprehensive context. Let me also check the best-tier paper for comparison, since the best-tier review already exists and I need to write the median-tier R2 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d7ea2fa-4a5d-4d56-bb90-0dcc4d97d5c3",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2eg57wFNcahMZRK3CSu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92213b0d-672d-4d68-8dc9-32e7dfd183d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHJA5fjQFYknQoSrGDr3Y9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6710,
      "cache_read_input_tokens": 53206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6710,
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

_source line 39 · 2026-05-14T14:52:18.914Z_

<details open><summary>🔧 Tool call — Read · `toolu_013z17KPjaKuAXESaQh1dHft`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92213b0d-672d-4d68-8dc9-32e7dfd183d7",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2eg57wFNcahMZRK3CSu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed55ec47-b465-40d8-ae1a-cf5a70c29084",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHJA5fjQFYknQoSrGDr3Y9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6710,
      "cache_read_input_tokens": 53206,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6710
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 53206,
          "cache_creation_input_tokens": 6710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6710,
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

_source line 40 · 2026-05-14T14:52:18.929Z_

<details><summary>↩ Tool result · `toolu_013z17KPjaKuAXESaQh1dHft`</summary>

```text
1	# Paper Framing — recursive_gen_depth_est
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25, 2026)
5	- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)
6	- EMNLP 2026 special theme "New Missions for NLP Research" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit
7	
8	## Core Claims (3 条)
9	
10	1. **Ordinal depth estimation is feasible and accurate**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features and contrastive ordinal learning. On our benchmark, DCOL achieves significantly higher accuracy than binary detection baselines and standard classification approaches. (MVP signal: 78.2% 4-class accuracy with simple RF on Pythia chain)
11	
12	2. **Depth Degradation Atlas — systematic characterization of recursive collapse**: We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) surprisal variance as the strongest depth signal, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), and (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable. This atlas spans 3 model families × 3 decoding strategies.
13	
14	3. **Depth-graduated curation outperforms binary filtering**: Using predicted depth as a continuous quality proxy enables more nuanced data curation — graduated weighting by depth retains high-quality shallow-generation content while down-weighting deeply recursive text, outperforming binary real/synthetic filtering on downstream task quality. (Proof-of-concept scope, ~1 page)
15	
16	## Story Spine
17	
18	- **Problem**: Web-scraped training corpora increasingly contain multi-generational synthetic content from uncontrolled model→data→model feedback loops. Existing detectors answer "is this synthetic?" but not "how many recursive cycles has this undergone?" — a critical distinction since 1st-gen synthetic data can improve training while deeply recursive text drives distribution collapse.
19	
20	- **Existing approaches & gaps**: Binary detectors (LOKI, DivEye, Binoculars) classify real vs. synthetic but discard ordinal depth information. EditLens estimates single-pass AI editing extent but not recursive depth. Model collapse studies (Drayson et al. EMNLP 2025; Shumailov et al. Nature 2024) characterize degradation patterns but assume depth is known a priori — no method estimates depth from text alone.
21	
22	- **Our framing**: We formalize ordinal generation depth estimation as a new task, construct a multi-generational benchmark (3 models × 3 strategies × 5+ depths), and propose DCOL — a contrastive ordinal learning method with learnable non-uniform margins that captures the actual geometry of recursive degradation. Crucially, we don't just build a classifier — we provide a Depth Degradation Atlas mapping how features evolve across depths, models, and strategies, including the EDD boundary where discrimination saturates.
23	
24	- **Headline result template**: "On our multi-generational benchmark spanning 3 model families and 3 decoding strategies, DCOL achieves X% ordinal depth estimation accuracy (chance=16.7% for 6-class), with cross-model generalization accuracy of Y%, while the best binary detection baseline repurposed for depth estimation achieves only Z%."
25	
26	## Venue Fit Risks
27	
28	- **Novelty concern**: DCOL is adapted from CLOC (CVPR 2025). Mitigation: novelty emphasis on problem formalization + Atlas + EDD metric; DCOL is framed as a strong method within the framework, not the sole contribution. Three text-specific modifications (strategy-aware margins, surprisal-augmented anchors, non-uniform learned margins) differentiate from direct CLOC transfer.
29	- **"Just an empirical study" risk**: Mitigation: method (DCOL) + Atlas (scientific contribution) + curation (practical application) = three-line contribution with clear primary/secondary hierarchy.
30	- **Controlled vs wild gap**: Mitigation: honest scoping — controlled setting is primary, wild-data calibration is probed, ecological transfer is future work.
31	
32	## Anticipated Reviewer Concerns
33	
34	1. "EDD might be very low (depth 2-3), making the task trivial beyond shallow depths" → Report EDD transparently; argue even low EDD is scientifically valuable (determines the boundary) and practically sufficient (shallow vs deep is the actionable distinction for curation)
35	2. "Why ordinal and not just binary?" → MVP already shows: d0v1 AUC=0.998 vs d1v2=0.861 vs d2v3=0.801 — ordinal structure captures monotonically decreasing but still significant discrimination at all adjacent pairs
36	3. "Generalization to unseen models/strategies?" → Leave-one-out experiments are core evaluation
37	4. "Non-monotonic degradation (Drayson et al.)?" → Learnable margins as soft inductive bias; ablation comparing DCOL vs fixed-margin CORAL vs CE loss
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed55ec47-b465-40d8-ae1a-cf5a70c29084",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "d407ecf1-5c85-4102-a7d4-7c948a36f6c3",
  "sourceToolAssistantUUID": "ed55ec47-b465-40d8-ae1a-cf5a70c29084",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-14T14:52:22.515Z_

I now have thorough context on the paper. Let me now write the R2 review for the median tier and submit it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d407ecf1-5c85-4102-a7d4-7c948a36f6c3",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2egXfNKTDn1YWTFDBss",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1736e9b0-cd02-48cf-8ab4-c7c98bbedd58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QL4MVhwJyaSSzXTrfZ3fSU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1472,
      "cache_read_input_tokens": 59916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1472,
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

_source line 42 · 2026-05-14T14:54:14.276Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01ESgFdUHnMzC7Z4aL16ggQL`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "tier": "median",
  "dream_id": "dream_20260514T140607",
  "overall_score": "borderline findings",
  "report": "---\ndream_id: dream_20260514T140607\ntier: median\noverall_score: borderline findings\ntimestamp: 2026-05-14T15:30:00+00:00\n---\n\n\n# Dream Review Report: Ordinal Depth Estimation of Recursive Generation: A Depth Degradation Atlas for Model Collapse Characterization\n\n**Venue:** EMNLP 2026 (ACL Rolling Review)\n**Review Mode:** R2 — Novelty & Related Work\n**Date:** 2026-05-14\n\n---\n\n## R2 Review: Novelty & Related Work\n\n### Summary\n\nThis paper formalizes ordinal generation depth estimation -- predicting how many recursive model-to-data-to-model cycles a text has undergone -- and proposes DCOL, a DeBERTa-based contrastive ordinal classifier with learnable non-uniform margins. Alongside the classifier, the paper contributes a Depth Degradation Atlas documenting how statistical features evolve across depths, models, and strategies, establishing an Effective Discriminable Depth (EDD) of approximately 3. The task formulation is genuinely novel and timely, and the Atlas provides useful empirical characterization. However, the DCOL method is a straightforward adaptation of existing contrastive ordinal learning with modest gains (+3.3pp over CORAL), the related work section is critically sparse (only 3 references in the bibliography), and certain claims exceed what the evidence supports.\n\n### Strengths (Novelty)\n\n- **Legitimate task novelty.** Ordinal depth estimation is a well-defined new problem. The insight that binary detection (real vs. synthetic) discards actionable ordinal information about recursive contamination severity is simple but important. No prior work has formalized this task, and the problem is well-motivated by the model collapse literature.\n\n- **EDD is a useful conceptual contribution.** Defining the Effective Discriminable Depth as the boundary beyond which adjacent depths become indistinguishable provides a concrete, quantitative answer to a previously unasked question. The finding that EDD varies across model-strategy combinations (range 2-4, median 3) is itself informative -- it shows this boundary is not universal but depends on model capability and decoding strategy.\n\n- **Atlas goes beyond prior characterization work.** Drayson et al. (2025) characterized non-monotonic degradation for individual settings. This paper systematically maps 19 features across 9 model-strategy combinations and 6 depths, yielding the \"feature handoff\" insight (surprisal variance dominates within EDD, Zipf alpha beyond) and documenting non-uniform inter-depth distances. This extends the empirical landscape meaningfully.\n\n- **Graduated curation as a conceptual paradigm.** Even at proof-of-concept scale, the idea that predicted depth can serve as a continuous quality proxy for data curation -- retaining useful shallow-generation content while down-weighting deeply recursive text -- is a useful contribution to the data curation discourse.\n\n### Strengths (Presentation & Framing)\n\n- **Appropriately scoped limitations section.** The paper is commendably honest about its weaknesses: the OLMo cross-model failure, effective granularity limited to 4 classes, scale transfer gap, controlled-vs-wild gap, and the moderate DCOL advantage. This calibrated self-assessment builds trust.\n\n- **Granularity analysis is well-designed.** Reporting accuracy across binary / 3-class / 4-class / 6-class granularities with lift-over-chance analysis gives a clear picture of the information-feasibility tradeoff. The finding that lift peaks at 4-class (+57.3pp) directly supports the EDD narrative.\n\n- **Clear experimental progression.** The paper proceeds logically from per-model validation to pooled comparisons to generalization to downstream application. Each experiment answers a natural follow-up question from the preceding one.\n\n### Weaknesses (Novelty)\n\n- **(Major) DCOL is an incremental adaptation of CLOC with minimal methodological novelty.** The base contrastive ordinal framework is taken directly from CLOC (CVPR 2025), an age estimation method. The three \"text-specific modifications\" -- learnable non-uniform margins, surprisal-augmented anchor selection, and strategy conditioning -- are individually standard techniques in metric learning. Learnable margins appear in Wu et al. (2017) and Roth et al. (2020). Anchor selection guided by auxiliary features is a standard hard-negative mining strategy. Strategy conditioning is lightweight FiLM-style modulation. Each contributes only 0.9-2.4pp. The paper should explicitly acknowledge DCOL as \"CLOC adapted for text depth estimation\" rather than presenting it as a novel framework. The current framing overstates the methodological contribution.\n\n- **(Major) The DCOL advantage over strong baselines is modest and partially attributable to ordinal structure itself, not DCOL-specific innovations.** DCOL achieves 57.1% vs. CORAL's 53.8% (+3.3pp) and DeBERTa E2E's 55.3% (+1.8pp). The ablation reveals that removing all three text-specific modifications drops accuracy to 53.1% -- below CORAL (53.8%). This means the vanilla contrastive framework without DCOL's modifications actually underperforms CORAL's rank loss. The +3.3pp gain over CORAL is the sum of three engineering choices, not a fundamental methodological advance. At EMNLP, a +3.3pp improvement with a confidence interval that potentially overlaps the baseline warrants caution in how the method contribution is framed.\n\n- **(Minor) The benchmark construction, while necessary, follows a standard recipe.** Generating recursive chains by prompting models with their own output and extracting statistical features is methodologically straightforward. The benchmark is a necessary scaffold for the research question but is not itself a novel methodological contribution -- it is competent execution of an obvious approach once the task is defined.\n\n### Weaknesses (Related Work)\n\n- **(Major) The bibliography contains only 3 references -- this is critically inadequate for EMNLP.** A 10-page paper at a top venue should cite 30-50 references to properly position its contributions. The current related work section is approximately half a page with three paragraphs, each citing 1-3 works. Entire relevant subfields are unrepresented:\n\n  - **Watermarking-based provenance:** Kirchenbauer et al. (2023, \"A Watermark for Large Language Models\") is a glaring omission. Watermarking enables proactive provenance tracking of generation chains -- a direct alternative to post-hoc depth estimation. The paper should discuss why post-hoc estimation is needed when watermarking exists (answer: watermarks require generator cooperation, which is absent in uncontrolled feedback loops).\n\n  - **Data quality and selection literature:** DSIR (Xie et al., 2023), QuRating (Wettig et al., 2024), and the broader data-centric AI literature are directly relevant to the graduated curation contribution. The paper claims depth-graduated weighting outperforms binary filtering but does not position this against existing quality-aware data selection methods.\n\n  - **Multi-class synthetic text attribution:** Uchendu et al. (2020, \"Authorship Attribution for Neural Text Generation\") and follow-up work on attributing text to specific generators represent a precursor to multi-class synthetic text analysis. While attribution and depth estimation are different tasks, the machine learning techniques overlap substantially.\n\n  - **Model collapse theory beyond Shumailov:** Alemohammad et al. (2023, \"Self-Consuming Generative Models Go MAD\"), Briesch et al. (2023), and Guo et al. (2024, on linguistic diversity decline) are all relevant to the theoretical grounding of why depth estimation matters. The paper cites only Shumailov et al. and Drayson et al. for the entire model collapse literature.\n\n  - **Binary detection methods:** The paper mentions LOKI, DivEye, and Binoculars but does not cite them in the bibliography. Fast-DetectGPT (Bao et al., 2024) and DetectGPT (Mitchell et al., 2023) should be properly cited and ideally included as baselines (or their features used as baselines, as partially done).\n\n  - **Ordinal classification beyond CORAL:** The ordinal learning literature includes SORD (Diaz & Marathe, 2019), unimodal regularization (Beckham & Pal, 2017), and stick-breaking approaches. Citing only CORAL and CLOC gives an incomplete picture of the ordinal classification landscape.\n\n- **(Major) Positioning against binary detection is incomplete.** The paper claims to extend \"from binary to ordinal\" but does not engage substantively with what binary detectors actually measure. Many binary detectors use the same features this paper relies on (surprisal statistics, perplexity). The paper should clarify whether ordinal depth estimation is genuinely a new signal or whether it is ordinal regression on features already known to correlate with \"synthetic-ness.\" The d0-vs-d1 AUC of 0.998 suggests that at the coarsest level, the paper is recovering the same signal as binary detectors.\n\n- **(Minor) EditLens is mentioned but not cited.** The bibliography lacks a reference for EditLens, LOKI, DivEye, and Binoculars. Mentioning methods without proper citations is a significant formatting issue for a venue submission.\n\n### Weaknesses (Claims & Framing)\n\n- **(Major) The d0 confound inflates headline accuracy.** Depth 0 is human-written text; depth 1+ is model-generated. The d0-vs-d1 AUC of 0.998 indicates this boundary is essentially binary human-vs-machine detection, a solved problem. The 6-class accuracy of 57.1% and 4-class accuracy of 82.3% are substantially boosted by near-perfect d0 classification. The paper should report a d1-d5 (5-class, synthetic-only) accuracy as a complementary metric to show how well the method discriminates among different generations of synthetic text, which is the genuinely novel aspect of the task. Without this, the headline numbers conflate \"detecting synthetic text\" (well-studied) with \"estimating recursive depth\" (novel).\n\n- **(Major) \"First systematic empirical map\" claim needs qualification.** The Atlas covers 3 models, all in the 1-1.5B parameter range, and 3 decoding strategies. This is a reasonable starting point but calling it \"first systematic empirical map of recursive degradation\" overstates the coverage. Models of different architecture families (encoder-decoder, mixture-of-experts), different scales (7B+, 70B+), and different modalities are not represented. The claim should be scoped: \"the first systematic characterization at the 1B scale across three autoregressive model families.\"\n\n- **(Minor) The cross-model generalization framing buries the negative result.** The paper reports \"mean 47.0% 6-class\" but the OLMo rotation fails at 42.1% and does not pass the self-defined 0.45 gate. One out of three rotations failing a self-defined quality gate is a substantial negative result, not a minor caveat. The paper acknowledges this in limitations but the abstract and introduction present cross-model generalization more optimistically than warranted. Stating \"cross-model leave-one-out generalization averages 47.0%\" without immediately noting \"with one of three rotations failing\" in the abstract is selectively optimistic.\n\n- **(Minor) Downstream curation effect size is marginal.** The 3.1% PPL reduction (p=0.038) over binary filtering is barely significant. The confidence intervals for graduated vs. binary weighting likely overlap. Furthermore, the comparison may be confounded by data volume: binary filtering retains less data than graduated weighting, so the PPL improvement could partly reflect having more training data rather than better weighting. The paper appropriately scopes this as a proof-of-concept, but the abstract presents it as a concrete contribution rather than a preliminary finding.\n\n- **(Minor) EDD threshold is arbitrary and sensitivity is not analyzed.** EDD is defined as the maximum depth where adjacent-pair AUC >= 0.72. This threshold is not motivated. If it were 0.75, some combinations would drop from EDD=3 to EDD=2. If it were 0.70, some would increase. A sensitivity analysis showing EDD as a function of the threshold (e.g., a simple table or curve) would strengthen the claim that EDD is approximately 3 \"robustly.\"\n\n### Questions for Authors\n\n1. How does DCOL differ from CLOC beyond the three listed modifications? Is the base contrastive loss formulation, the mining strategy, and the ordinal head identical to CLOC?\n\n2. Which reference model is used to compute surprisal features across all three model families? If Pythia-1.4B is used as the reference model for Pythia-generated text, this creates a circularity where the generating model's own surprisal on its output conflates model identity with depth signal. How does this affect the cross-model results?\n\n3. What is the 5-class (d1-d5) accuracy, excluding depth 0? This would isolate the genuinely novel \"ordinal depth discrimination\" signal from the well-studied \"human vs. machine\" signal.\n\n4. How does EDD change if the threshold is set to 0.70 or 0.75 instead of 0.72?\n\n5. Has the graduated curation experiment been compared against a volume-matched binary filtering baseline (i.e., binary filtering with a softer threshold that retains the same percentage of data as graduated weighting)?\n\n6. How does DCOL handle text generated by unknown strategies at inference time? The strategy conditioning module requires a strategy label -- what happens when this is unavailable, as would be the case for any real-world deployment?\n\n7. The paper mentions 19 statistical features but only discusses 5 in the monotonicity analysis. Are the remaining 14 features uninformative? Could a more compact feature set achieve similar performance?\n\n8. Why are there only 3 references in the bibliography? Is this an artifact of the submission format, or does the paper genuinely not cite works beyond Shumailov, Drayson, and Cao?\n\n### Missing References (non-exhaustive)\n\nThe following are works that should be cited and discussed:\n- Kirchenbauer et al. (2023) -- watermarking for LLM outputs (provenance alternative)\n- Mitchell et al. (2023) -- DetectGPT (binary detection baseline)\n- Bao et al. (2024) -- Fast-DetectGPT (binary detection baseline)\n- Alemohammad et al. (2023) -- self-consuming generative models (model collapse theory)\n- Briesch et al. (2023) -- LLMs suffering from own output (model collapse)\n- Guo et al. (2024) -- linguistic diversity decline in recursive generations\n- Uchendu et al. (2020) -- multi-class authorship attribution for generators\n- Xie et al. (2023) -- DSIR data selection (curation baseline)\n- Wettig et al. (2024) -- QuRating data quality (curation baseline)\n- Diaz & Marathe (2019) -- SORD soft ordinal regression\n- Beckham & Pal (2017) -- unimodal regularization for ordinal classification\n- Wu et al. (2017) -- learnable margins in metric learning\n- Roth et al. (2020) -- revisiting training strategies for metric learning\n\n### Preliminary Scores\n\n- Soundness: 3/5\n- Excitement: 2.5/5\n- Overall: 2.5/5\n- Confidence: 4/5\n\n### Score Justification\n\n**Soundness (3/5):** The experimental design is thorough -- per-model benchmarks, cross-model/strategy generalization, ablation, downstream application, and wild-data calibration form a comprehensive evaluation. However, the loss formulation in Eq. 1 appears to only include a pull/ceiling term with no repulsive mechanism (collapsing all embeddings to a point trivially satisfies it), which is either a critical omission in the writing or a genuine flaw. The d0 confound inflates headline numbers. These issues prevent a higher soundness score despite strong experimental coverage.\n\n**Excitement (2.5/5):** The task formulation is timely and the Atlas is useful, but the execution is incremental. DCOL's +3.3pp over CORAL is modest. The effective task granularity is limited to 4 classes. Cross-model generalization is unreliable (1/3 rotations fail). Wild-data correlations are weak (rho <= 0.34). The practical impact pathway -- from controlled benchmark to real-world data curation -- has several unsolved gaps. For the median tier of results, the excitement is dampened by the limited margin of improvement and constrained generalization.\n\n**Overall (2.5/5):** The paper sits at the borderline between Findings and main conference. The task definition and Atlas are genuine contributions that advance understanding of recursive contamination. However, the critically sparse related work (3 references), incremental methodology, inflated headline metrics (d0 confound), and modest effect sizes collectively place this below the main conference threshold. With a substantially expanded related work section, honest d1-d5 metrics, and repositioning of DCOL as adapted-CLOC, this could reach Findings quality. The gap to main conference acceptance requires either stronger empirical results (larger cross-model/wild-data performance) or deeper methodological novelty.\n\n**Confidence (4/5):** I am familiar with the synthetic text detection, model collapse, ordinal classification, and contrastive learning literatures. The related work gaps identified are based on direct knowledge of the cited and missing works.\n\n---\n\n## Comparison with Best-Tier Review Context\n\nThe median-tier paper shares the same structure and claims as the best tier but with weaker empirical results in several dimensions:\n- DCOL's advantage over CORAL is +3.3pp (same as best tier's reported number, but in the best tier the ablation showed larger per-component contributions and vanilla-contrastive still outperformed CORAL)\n- Cross-model mean is 47.0% with OLMo failing the gate (best tier reported 60.1% mean or similar, with all rotations passing)\n- Wild-data correlations are moderate (rho <= 0.34)\n- The 3-reference bibliography is identical across tiers, confirming this is a structural issue with the paper rather than a tier-specific concern\n\nThe core weakness pattern is consistent: the task and Atlas are solid contributions, but the method is incremental, the related work is critically underdeveloped, and the headline claims need better calibration to the actual evidence.\n\n---\n\n## Recommendation Summary\n\n**For revision (priority-ordered):**\n1. Expand related work from 3 to 25+ references, covering watermarking, data curation, multi-class attribution, model collapse theory, and ordinal classification\n2. Report d1-d5 (synthetic-only) accuracy as a secondary headline metric\n3. Reposition DCOL explicitly as \"CLOC adapted for text depth estimation\" -- the novelty is the task + Atlas\n4. Provide EDD threshold sensitivity analysis\n5. Clarify the complete loss function (is there a repulsive term?)\n6. Clarify the reference model for surprisal computation and address potential circularity\n7. Compare graduated vs. binary curation with matched data volume\n8. Add figures -- the paper is entirely tables, which is unusual and reduces accessibility"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1736e9b0-cd02-48cf-8ab4-c7c98bbedd58",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2egXfNKTDn1YWTFDBss",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "404f59ba-c843-4ba6-9933-5cbe2c771dbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QL4MVhwJyaSSzXTrfZ3fSU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1472,
      "cache_read_input_tokens": 59916,
      "output_tokens": 4782,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1472
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4782,
          "cache_read_input_tokens": 59916,
          "cache_creation_input_tokens": 1472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1472,
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

_source line 43 · 2026-05-14T14:54:17.676Z_

<details><summary>↩ Tool result · `toolu_01ESgFdUHnMzC7Z4aL16ggQL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/review_report.md\", \"dream_id\": \"dream_20260514T140607\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "404f59ba-c843-4ba6-9933-5cbe2c771dbf",
  "isSidechain": true,
  "promptId": "04c2d15f-0957-478f-95a7-0d9ef34a19e1",
  "agentId": "a4d26d750abf8bf19",
  "type": "user",
  "uuid": "c079f318-a199-4c7a-96c9-ac561f7517d6",
  "sourceToolAssistantUUID": "404f59ba-c843-4ba6-9933-5cbe2c771dbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-14T14:54:31.775Z_

The R2 review for the median tier has been submitted. Here is a summary of the key findings:

**Overall Score: 2.5/5 (Borderline Findings)**

The review identifies the task formulation (ordinal depth estimation) and the Depth Degradation Atlas as genuine contributions, but flags several issues that place this below the main conference threshold for the median tier:

**Critical weaknesses:**
1. **Bibliography has only 3 references** -- critically inadequate for EMNLP. Missing entire subfields: watermarking (Kirchenbauer 2023), data curation (DSIR, QuRating), multi-class attribution (Uchendu 2020), model collapse theory (Alemohammad 2023), and proper citations for binary detectors mentioned in text.
2. **DCOL is an incremental adaptation of CLOC** with three standard engineering modifications contributing only 0.9-2.4pp each. The vanilla contrastive framework without modifications (53.1%) actually underperforms CORAL (53.8%), meaning the +3.3pp gain is entirely from engineering choices, not fundamental methodological advance.
3. **Depth-0 confound inflates headline metrics** -- the d0-vs-d1 boundary is essentially solved binary detection (AUC 0.998), not depth estimation. A d1-d5 accuracy is needed as a complementary metric.
4. **Loss formulation (Eq. 1) appears incomplete** -- only includes a pull term with no repulsive mechanism.

**Strengths acknowledged:**
- Genuine task novelty and timely problem
- EDD as a useful quantitative concept
- Atlas extends prior characterization work meaningfully
- Honest, well-calibrated limitations section
- Comprehensive experimental progression

The report was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c079f318-a199-4c7a-96c9-ac561f7517d6",
  "isSidechain": true,
  "agentId": "a4d26d750abf8bf19",
  "requestId": "req_011Cb2eqH3Y8rsTGYbCdHSmB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76cc1af6-30f6-4371-9c98-a1d870399cef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "4ea398ee-be27-4c61-8a35-22ee8aa61ddb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LSUn4mcDkeYXtDGwHHcW8N",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4910,
      "cache_read_input_tokens": 61388,
      "output_tokens": 465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 465,
          "cache_read_input_tokens": 61388,
          "cache_creation_input_tokens": 4910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4910,
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
