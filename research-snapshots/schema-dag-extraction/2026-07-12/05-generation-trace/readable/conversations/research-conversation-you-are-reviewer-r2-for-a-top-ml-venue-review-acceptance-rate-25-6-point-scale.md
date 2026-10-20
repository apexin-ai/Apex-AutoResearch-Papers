# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a2d75a1acd67982ee.jsonl`
- **Structured JSON:** [`8ca34c0046d45b30c0ae.json`](../../sessions/8c/8ca34c0046d45b30c0ae.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-16T08:07:51.662Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus is **Novelty and Related Work**.

## Paper Summary
Title: "Multi-Channel Schema Degradation in Training-Free LLM Information Extraction: Type Count and Confusability as Orthogonal Failure Modes"

The paper conducts controlled empirical study across 3 IE tasks (NER, RE, ED) isolating type count from type confusability as independent predictors of extraction quality in training-free LLM IE. Key claims:
1. **Confusability Independence**: Pairwise SCS independently predicts degradation (r=0.11-0.13, CIs exclude zero), validated across tasks, amplifies 3.4× with schema complexity
2. **Multi-Channel Degradation**: Two orthogonal channels—count→recall decline (attention dilution) vs confusability→type confusion (semantic interference), IntraSub ρ≥0.95 cross-task
3. **SDGD Negative Result**: Naive decomposition fails due to merge amplification (~35% structural cost)
4. **Methodological Contribution**: Centrality confound in per-type aggregation on homogeneous schemas

## Paper Structure
- Section 1 (Introduction): Motivation, claims LLM IE degrades on complex schemas but mechanisms unknown. References UniNER, LLM-PEE.
- Section 2 (Related Work): Three paragraphs covering Training-Free LLM IE, Schema Decomposition, Confusability in Classification. Cites GPT-NER, GoLLIE, UniNER.
- Section 3 (Methodology): SCS/BCS definitions, experimental design (count curves, BCS-controlled, 2×2 factorial, error taxonomy), datasets (Few-NERD, FewRel, DocRED, MAVEN), SDGD description.
- Sections 4-5 (Experiments, Discussion): 11 tables covering SCS validation, DocRED study, interaction effects, error taxonomy, SDGD variants, ablations. Discussion of small r, centrality confound, merge amplification.
- Section 6 (Conclusion): Summarizes findings, points to calibration-based future work.
- References: Only 4 citations ([1]-[4]).
- Limitations: Acknowledges limited LLMs, English-only, simple merge, narrow factorial range.

## Datasets and Models
- Few-NERD (66 NER types), FewRel (16/80 RE relations), DocRED (96 RE relations), MAVEN (168 ED event types)
- Qwen3-32B (primary), LLaMA-3.3-70B (replication, 87% consistency)

## Key Results
- SCS validates as proxy (ρ=0.14-0.31, all p<1e-5)
- Count curves show 48pp decline on DocRED
- BCS-controlled: 23.3pp gap at count=16 on DocRED
- 2×2 interaction not significant (p=0.505) → additive/orthogonal
- Error taxonomy: IntraSub ρ=1.0 (NER), 0.954 (RE)
- SDGD: all decomposition < single-pass, ~35% structural cost
- Per-type splitting: +59% recall but -66% precision

## Your Review Tasks
Evaluate the following and provide a structured review:

1. **Novelty Assessment**: Is the research question novel? Is "disentangling count from confusability" a genuinely new contribution? How does this relate to prior work on label confusion, fine-grained classification, schema decomposition?
2. **Related Work Coverage**: The paper cites only 4 references. Is this adequate? What critical related work is missing? Consider: structured prediction with LLMs, prompt engineering for IE, label confusion in NLP, cognitive science of categorization, other decomposition approaches.
3. **Claim vs Evidence Gap**: Are the 4 stated contributions actually novel? Is the "first controlled empirical study" claim justified?
4. **Positioning and Framing**: Is the paper well-positioned for a top ML venue? Is it more of an empirical analysis paper or a methods paper? Does it offer sufficient actionable insights?
5. **Significance and Impact**: Will this work influence future research or practice? Are the findings surprising or confirmatory?
6. **Writing Quality**: Is the paper well-organized and clearly written?
7. **Breadth of Related Work on Label Confusion**: Prior work in NLP has studied label confusion extensively (confusion matrices, hierarchical label structures, label smoothing, etc.). Does this paper adequately differentiate itself?

## Output Format
```
## R2: Novelty and Related Work

### Summary
[2-3 sentences]

### Strengths
- S1: ...
- S2: ...
- ...

### Weaknesses
- W1: ...
- W2: ...
- ...

### Questions for Authors
- Q1: ...
- ...

### Missing Related Work
- ...

### Preliminary Score: X/6
### Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "afb7d380-6c61-4b55-aa00-c079e7b76fb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T08:07:51.665Z_

```json
{
  "parentUuid": "afb7d380-6c61-4b55-aa00-c079e7b76fb7",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
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
  "uuid": "dea2456e-abda-4488-a5ed-6cba44dc3b66",
  "timestamp": "2026-05-16T08:07:51.665Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T08:07:54.764Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dea2456e-abda-4488-a5ed-6cba44dc3b66",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uTWamtk4GRC5oWJLXA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42e63673-1914-4a88-b6bc-b35770cd1980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DHv4MduBVRNtTGV9Qbmdtj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7075,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7075,
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

_source line 4 · 2026-05-16T08:07:55.190Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018HJLpF9ikfAaf81wtMxgxL`</summary>

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
  "parentUuid": "42e63673-1914-4a88-b6bc-b35770cd1980",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uTWamtk4GRC5oWJLXA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2078c87f-15c3-41a9-b6e0-8f43b470d345",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DHv4MduBVRNtTGV9Qbmdtj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7075,
      "cache_read_input_tokens": 8249,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7075
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 124,
          "cache_read_input_tokens": 8249,
          "cache_creation_input_tokens": 7075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7075,
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

_source line 5 · 2026-05-16T08:07:55.193Z_

<details><summary>↩ Tool result · `toolu_018HJLpF9ikfAaf81wtMxgxL`</summary>

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
  "parentUuid": "2078c87f-15c3-41a9-b6e0-8f43b470d345",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "e7fadcbf-a109-4d76-ac5a-67ac4df2428d",
  "sourceToolAssistantUUID": "2078c87f-15c3-41a9-b6e0-8f43b470d345",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-16T08:07:57.756Z_



Let me read the paper and project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7fadcbf-a109-4d76-ac5a-67ac4df2428d",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uTnC8QFkdd9GoRMHcz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "374dac0e-2e11-481a-a406-747a3c30c434",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BW55Eqq8FBNVpEKcJdR7qr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15324,
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

_source line 7 · 2026-05-16T08:07:58.685Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_017DXA2RscBMeQ7LoDK8jFsW`</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "374dac0e-2e11-481a-a406-747a3c30c434",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uTnC8QFkdd9GoRMHcz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7702fa7e-ae01-4d2e-854c-f301f9ba6f4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BW55Eqq8FBNVpEKcJdR7qr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15324,
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

_source line 8 · 2026-05-16T08:07:58.870Z_

<details><summary>↩ Tool result · `toolu_017DXA2RscBMeQ7LoDK8jFsW`</summary>

```text
{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (42 个)\n\n- **bootstrap_ci_analysis**: DONE (success) — \n- **exp016_fewrel_error_taxonomy**: DONE (success) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp007_error_taxonomy**: DONE (success) — \n- **exp_fewrel_formal_80rel**: DONE (success) — \n- **exp_fewrel_formal**: DONE (success) — \n- **exp008_sdgd_zero_fewnerd_r2**: DONE (negative) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n- **fewrel_pilot**: DONE (success) — \n- **exp004_maven_bcs**: DONE (negative) — \n- **exp002_confusability_controlled**: DONE (success) — \n- **exp003a_prompt_v2_rerun**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp001_count_baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- exp_fewrel_v2_n25（准备中）\n- bcs_max_to_mean_fix（准备中）\n\n## 近期结论\n- **exp_confusability_batch_composition** (success): Confusability-aware batch composition (graph coloring on SCS matrix to separate high-SCS pairs) improves per-type accuracy and reduces substitution errors compared to random batching and single-pass full schema, providing a practical application of the confusability findings.\n- **exp_fewrel_16rel_bootstrap** (success): FewRel 16-type pool, 100 random 8-type batches, bootstrap CI for BCS effect (Δ_BCS). 填 tab:bcs_controlled 16-rel 行的 CI，并与 80-rel 计算 amplification ratio 正式 CI。D033 已批准。 ← 基于 exp_fewrel_formal\n- **exp_docred_confusability** (success): Schema-induced degradation (count + confusability channels) generalizes to document-level RE (DocRED, 96 relation types), strengthening cross-dataset evidence for Claims 1 and 2. ← 基于 exp_fewrel_formal_80rel\n  [DocRED SCS Matrix (96 relations)](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/scs_matrix_info.txt) | [DocRED Confusability Pilot Results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/pilot_results.txt) | [phase2_count_curve_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/count_curve_results.json) | [phase2_bcs_controlled_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bcs_controlled_results.json) | [phase2_bootstrap_analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bootstrap_analysis.json)\n\n## 趋势\n成功 20 / 负向 5 / 失败 10 / 共 38\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\ncqa1-38874: 无 GPU 信息\n\n## 告警\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\n- exp012_llama_8b: 已被终止 — unknown\n- exp_fewrel_40rel: 训练失败 — unknown\n- exp012_llama_awq: 已被终止 — unknown\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\n- exp_fewrel_40rel_r2: 训练失败 — unknown\n- exp_fewrel_40rel_r3: 训练失败 — unknown\n- exp012_llama_8b_r3: 训练失败 — unknown\n- exp_fewrel_16rel_100batch: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7702fa7e-ae01-4d2e-854c-f301f9ba6f4b",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "ec4433d4-04a4-4c15-86fb-b8d3bf810cac",
  "sourceToolAssistantUUID": "7702fa7e-ae01-4d2e-854c-f301f9ba6f4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T08:07:59.179Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VyvsLemSqJ9HQEBFZG7jiE`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec4433d4-04a4-4c15-86fb-b8d3bf810cac",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uTnC8QFkdd9GoRMHcz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89563560-eece-4ef4-9703-19dcd77aa115",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BW55Eqq8FBNVpEKcJdR7qr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15324,
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

_source line 10 · 2026-05-16T08:07:59.189Z_

<details><summary>↩ Tool result · `toolu_01VyvsLemSqJ9HQEBFZG7jiE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp017_gpt4o_mini_fewrel（准备中）\\n- exp_cross_embedding_sensitivity（准备中）\\n- exp_fewrel_v2_n25（准备中）\\n- bcs_max_to_mean_fix（准备中）\\n\\n## 近期结论\\n- **exp_confusability_batch_composition** (success): Confusability-aware batch composition (graph coloring on SCS matrix to separate high-SCS pairs) improves per-type accuracy and reduces substitution errors compared to random batching and single-pass full schema, providing a practical application of the confusability findings.\\n- **exp_fewrel_16rel_bootstrap** (success): FewRel 16-type pool, 100 random 8-type batches, bootstrap CI for BCS effect (Δ_BCS). 填 tab:bcs_controlled 16-rel 行的 CI，并与 80-rel 计算 amplification ratio 正式 CI。D033 已批准。 ← 基于 exp_fewrel_formal\\n- **exp_docred_confusability** (success): Schema-induced degradation (count + confusability channels) generalizes to document-level RE (DocRED, 96 relation types), strengthening cross-dataset evidence for Claims 1 and 2. ← 基于 exp_fewrel_formal_80rel\\n  [DocRED SCS Matrix (96 relations)](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/scs_matrix_info.txt) | [DocRED Confusability Pilot Results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/pilot_results.txt) | [phase2_count_curve_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/count_curve_results.json) | [phase2_bcs_controlled_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bcs_controlled_results.json) | [phase2_bootstrap_analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bootstrap_analysis.json)\\n\\n## 趋势\\n成功 20 / 负向 5 / 失败 10 / 共 38\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-38874: 无 GPU 信息\\n\\n## 告警\\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\\n- exp012_llama_fewnerd: 训练失败 — unknown\\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\\n- exp012_llama_8b: 已被终止 — unknown\\n- exp_fewrel_40rel: 训练失败 — unknown\\n- exp012_llama_awq: 已被终止 — unknown\\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\\n- exp_fewrel_40rel_r2: 训练失败 — unknown\\n- exp_fewrel_40rel_r3: 训练失败 — unknown\\n- exp012_llama_8b_r3: 训练失败 — unknown\\n- exp_fewrel_16rel_100batch: 已被终止 — unknown\\n\", \"total_chars\": 2396, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89563560-eece-4ef4-9703-19dcd77aa115",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "21b07f28-8078-439e-8b0f-178e09f9c407",
  "sourceToolAssistantUUID": "89563560-eece-4ef4-9703-19dcd77aa115",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T08:07:59.586Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YYTEHi1oDS1aAob6VmeL11`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21b07f28-8078-439e-8b0f-178e09f9c407",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uTnC8QFkdd9GoRMHcz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab83252c-c6f5-4a71-b269-1a2addad0855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BW55Eqq8FBNVpEKcJdR7qr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15324,
      "output_tokens": 265,
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
          "output_tokens": 265,
          "cache_read_input_tokens": 15324,
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

_source line 12 · 2026-05-16T08:07:59.602Z_

<details><summary>↩ Tool result · `toolu_01YYTEHi1oDS1aAob6VmeL11`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'schema-dag-extraction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab83252c-c6f5-4a71-b269-1a2addad0855",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "9e59147a-40ac-4294-950c-95b18688d3cb",
  "sourceToolAssistantUUID": "ab83252c-c6f5-4a71-b269-1a2addad0855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T08:08:02.872Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BShy3ZjrMUWSpdZEM7fn3f`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e59147a-40ac-4294-950c-95b18688d3cb",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uU6bQy3phW56UYkdoD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11d5cd69-63c1-407a-9301-d369cda770e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KegbyGqS9F4MJQzghnAVA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2942,
      "cache_read_input_tokens": 16770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 14 · 2026-05-16T08:08:02.887Z_

<details><summary>↩ Tool result · `toolu_01BShy3ZjrMUWSpdZEM7fn3f`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\", \"content\": \"# Literature Map for schema-dag-extraction\\n# Updated: 2026-05-15\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\n\\n# =============================================================================\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\n# =============================================================================\\n\\n- id: llm-pee-2025\\n  title: \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\"\\n  year: 2025\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2503.02628\\n  role: direct-competitor\\n  relevance_note: >\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\n    Divides candidate types into partitions to reduce prompt length.\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\n\\n- id: parse-2025\\n  title: \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\"\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://arxiv.org/abs/2510.08623\\n  role: direct-competitor\\n  relevance_note: >\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\n    Does NOT model type confusability explicitly.\\n\\n- id: dee-2024\\n  title: \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\"\\n  year: 2024\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2406.01045\\n  role: direct-competitor\\n  relevance_note: >\\n    Decomposes event extraction into detection + argument extraction.\\n    Dynamic schema-aware RAG for augmented prompts.\\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\\n\\n- id: crossagentie-2025\\n  title: \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\\\"\\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.718/\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\\n    + inter-group cross-task debate (NER↔RE mutual refinement).\\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\\n    Must clearly differentiate in paper.\\n\\n- id: dlisc-2025\\n  title: \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\"\\n  year: 2025\\n  venue: arXiv (May 2025)\\n  url: https://arxiv.org/abs/2505.14992\\n  role: direct-competitor\\n  relevance_note: >\\n    Dual-LoRA with Incremental Schema Caching.\\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\\n    Focus on efficiency for on-device LLMs, not confusability analysis.\\n\\n- id: spt-2025\\n  title: \\\"Schema as Parameterized Tools for Universal Information Extraction\\\"\\n  year: 2025\\n  venue: arXiv (June 2025)\\n  url: https://arxiv.org/abs/2506.01276\\n  role: direct-competitor\\n  relevance_note: >\\n    Treats schemas as parameterized tools for LLM tool-calling.\\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\\n    Does not address type confusability.\\n\\n- id: zeroner-2025\\n  title: \\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\"\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.805/\\n  role: direct-competitor\\n  relevance_note: >\\n    Description-driven: LLM supervision → BERT student for unseen types.\\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\\n    Related to how schema semantics affect extraction quality.\\n\\n- id: cmas-ner-2025\\n  title: \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\"\\n  year: 2025\\n  venue: TheWebConf 2025\\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent collective intelligence for zero-shot NER.\\n    Addresses context correlation and indiscriminate demonstration problems.\\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\\n\\n# =============================================================================\\n# METHOD COMPONENTS — techniques we build upon or relate to\\n# =============================================================================\\n\\n- id: uniner-2024\\n  title: \\\"UniversalNER: Targeted Distillation from Large Language Models for Open NER\\\"\\n  authors: [Wenxuan Zhou et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://arxiv.org/abs/2308.03279\\n  role: method-component\\n  relevance_note: >\\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\\n    Important baseline for universal NER and schema-at-scale challenges.\\n\\n- id: gollie-2024\\n  title: \\\"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\\\"\\n  authors: [Oscar Sainz et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://hitz-zentroa.github.io/GoLLIE/\\n  role: method-component\\n  relevance_note: >\\n    Code-style schema definitions + annotation guideline following.\\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\\n    Baseline for guideline-driven schema representation.\\n\\n- id: gliner-2024\\n  title: \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08526\\n  role: method-component\\n  relevance_note: >\\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\\n\\n- id: gliner2-2025\\n  title: \\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2025\\n  venue: EMNLP 2025 Demo\\n  url: https://arxiv.org/abs/2507.18546\\n  role: method-component\\n  relevance_note: >\\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\\n    Schema-driven interface. Shows schema approach scales to multi-task.\\n\\n- id: kggen-2025\\n  title: \\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\"\\n  authors: [Mo et al.]\\n  year: 2025\\n  venue: NeurIPS 2025\\n  url: https://arxiv.org/abs/2502.09956\\n  role: method-component\\n  relevance_note: >\\n    Two-stage decomposition: entities first, then relations.\\n    Entity clustering/deduplication to reduce graph sparsity.\\n    Schema decomposition approach for KG construction.\\n\\n- id: code4uie-2024\\n  title: \\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\"\\n  authors: [Yucan Guo et al.]\\n  year: 2024\\n  venue: NeurIPS 2024 Workshop\\n  url: https://arxiv.org/abs/2311.02962\\n  role: method-component\\n  relevance_note: >\\n    Python class-based schema definitions + RAG for code generation.\\n    Unified code-style schema for all IE tasks.\\n\\n- id: iepile-2024\\n  title: \\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\"\\n  authors: [Guanzheng Chen et al., ZJU NLP]\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2402.14710\\n  role: method-component\\n  relevance_note: >\\n    0.32B token bilingual IE corpus. Hard negative schema construction =\\n    semantically proximate schemas to train type discrimination.\\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\\n    Our contribution is inference-time confusability-aware decomposition (training-free).\\n\\n- id: lost-in-middle-2024\\n  title: \\\"Lost in the Middle: How Language Models Use Long Contexts\\\"\\n  authors: [Nelson F. Liu et al.]\\n  year: 2024\\n  venue: TACL 2024\\n  url: https://arxiv.org/abs/2307.03172\\n  role: method-component\\n  relevance_note: >\\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\\n    Motivates schema decomposition to reduce prompt length.\\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\\n\\n# =============================================================================\\n# ZERO-SHOT NER / RE BASELINES\\n# =============================================================================\\n\\n- id: self-improve-ner-2024\\n  title: \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\"\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08921\\n  role: background\\n  relevance_note: >\\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\\n\\n- id: self-prompting-re-2024\\n  title: \\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\"\\n  year: 2024\\n  venue: EMNLP 2024 Findings\\n  url: https://arxiv.org/abs/2410.01154\\n  role: background\\n  relevance_note: >\\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\\n    Training-free RE baseline.\\n\\n- id: reasoning-ner-2025\\n  title: \\\"A Reasoning Paradigm for Named Entity Recognition\\\"\\n  year: 2025\\n  venue: arXiv (Nov 2025)\\n  url: https://arxiv.org/abs/2511.11978\\n  role: background\\n  relevance_note: >\\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\\n\\n- id: nuner-2024\\n  title: \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\"\\n  authors: [Sergei Bogdanov et al., NuMind]\\n  year: 2024\\n  venue: EMNLP 2024\\n  url: https://arxiv.org/abs/2402.15343\\n  role: background\\n  relevance_note: >\\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\\n\\n# =============================================================================\\n# EVALUATION / BENCHMARKING\\n# =============================================================================\\n\\n- id: familiarity-2025\\n  title: \\\"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\\\"\\n  year: 2025\\n  venue: NAACL 2025\\n  url: https://arxiv.org/abs/2412.10121\\n  role: evaluation\\n  relevance_note: >\\n    \\\"Familiarity\\\" metric for label shift in synthetic NER data.\\n    Zero-shot NER scores overestimated due to train-eval label overlap.\\n    Quantifies semantic similarity between entity types — related to type confusability.\\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\\n\\n- id: guidex-2025\\n  title: \\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\"\\n  authors: [Neil Deshpande et al.]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://arxiv.org/abs/2506.00649\\n  role: evaluation\\n  relevance_note: >\\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\\n\\n# =============================================================================\\n# SURVEYS\\n# =============================================================================\\n\\n- id: llm4ie-survey-2024\\n  title: \\\"Large Language Models for Generative Information Extraction: A Survey\\\"\\n  authors: [Derong Xu et al.]\\n  year: 2024\\n  venue: Frontiers of Computer Science\\n  url: https://arxiv.org/abs/2312.17617\\n  role: background\\n  relevance_note: >\\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\\n\\n- id: knowcoder-2024\\n  title: \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\\\"\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2403.07969\\n  role: background\\n  relevance_note: >\\n    Encodes schema knowledge via code structures into LLM.\\n    Related to code-based schema representation.\\n\\n- id: slot-2025\\n  title: \\\"SLOT: Structuring the Output of Large Language Models\\\"\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://aclanthology.org/2025.emnlp-industry.32.pdf\\n  role: background\\n  relevance_note: >\\n    Decouples output formatting from NL task. Model-agnostic structured output.\\n\\n# =============================================================================\\n# EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\\n# — supports \\\"domain boundary\\\" finding: BCS proxy fails for same-domain schemas\\n# =============================================================================\\n\\n- id: gao-repr-degen-2019\\n  title: \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\"\\n  authors: [Jun Gao, Di He, Hang Li, Xin Jiang]\\n  year: 2019\\n  venue: ICLR 2019\\n  url: https://arxiv.org/abs/1907.12009\\n  role: theoretical-foundation\\n  relevance_note: >\\n    FOUNDATIONAL. Shows that likelihood maximization + weight tying causes word embeddings\\n    to degenerate into a narrow cone with uniformly high cosine similarity.\\n    Proposed cosine regularization (MLE-CosReg) to widen the cone aperture.\\n    LINK TO OUR WORK: This is the root mechanism behind BCS compression.\\n    When Qwen3-32B encodes 168 same-domain FrameNet types, the degeneration effect\\n    concentrates them into the same narrow cone (cosine ≥ 0.90), destroying BCS discriminability.\\n    Cite as the theoretical explanation for why embedding-based confusability proxies\\n    have a principled failure mode on semantically homogeneous schemas.\\n\\n- id: ethayarajh-contextual-2019\\n  title: \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\"\\n  authors: [Kawin Ethayarajh]\\n  year: 2019\\n  venue: EMNLP 2019\\n  url: https://aclanthology.org/D19-1006/\\n  role: theoretical-foundation\\n  relevance_note: >\\n    Shows contextualized representations are anisotropic in ALL layers of BERT/ELMo/GPT-2.\\n    Upper layers are more context-specific but still not isotropic.\\n    Introduces quantitative measures of anisotropy (avg cosine sim of random word pairs).\\n    LINK TO OUR WORK: Establishes that anisotropy is pervasive across architectures —\\n    our MAVEN embedding compression is not a Qwen-specific artifact but a general property.\\n    Supports the argument that ANY embedding-based confusability proxy inherits this limitation.\\n\\n- id: cai-isotropy-clusters-2021\\n  title: \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\"\\n  authors: [Xingyu Cai, Jiaji Huang, Yuchen Bian, Kenneth Church]\\n  year: 2021\\n  venue: ICLR 2021\\n  url: https://openreview.net/forum?id=xYGNO86OWDH\\n  role: theoretical-foundation\\n  relevance_note: >\\n    ⭐ MOST DIRECTLY RELEVANT. Key insight: global anisotropy is caused by isolated clusters;\\n    WITHIN each cluster, embeddings are locally more isotropic.\\n    Resolution: the high average cosine similarity reported in prior work is an artifact of\\n    mixing embeddings from different clusters — within-cluster geometry is better behaved.\\n    LINK TO OUR WORK: This is the exact mechanism for our \\\"domain boundary\\\" finding.\\n    Cross-domain schemas (ACE vs FewNERD) span DIFFERENT clusters → BCS captures real\\n    inter-cluster distances → proxy works. Same-domain schemas (MAVEN FrameNet types)\\n    fall within ONE cluster → within-cluster variance is low → cosine sim saturates ≥ 0.90\\n    → BCS loses discriminability. Our empirical finding is a direct instantiation of their\\n    theoretical framework applied to type-level (not token-level) embeddings.\\n\\n- id: godey-anisotropy-inherent-2024\\n  title: \\\"Anisotropy Is Inherent to Self-Attention in Transformers\\\"\\n  authors: [Nathan Godey, Éric de la Clergerie, Benoît Sagot]\\n  year: 2024\\n  venue: EACL 2024\\n  url: https://aclanthology.org/2024.eacl-long.3/\\n  role: theoretical-foundation\\n  relevance_note: >\\n    Proves anisotropy is inherent to the self-attention mechanism itself, not just a\\n    consequence of cross-entropy training on long-tailed token distributions.\\n    Observed across modalities (NLP, vision), ruling out data-distribution explanations.\\n    LINK TO OUR WORK: Strengthens the argument that BCS compression is a fundamental\\n    architectural limitation, not fixable by better prompting or model choice.\\n    Supports our position that structural decomposition (SDGD) is necessary precisely\\n    because the embedding space has inherent geometric constraints.\\n\\n- id: rajaee-cluster-isotropy-2021\\n  title: \\\"A Cluster-based Approach for Improving Isotropy in Contextual Embedding Space\\\"\\n  authors: [Sara Rajaee, Mohammad Taher Pilehvar]\\n  year: 2021\\n  venue: ACL 2021\\n  url: https://aclanthology.org/2021.acl-short.73/\\n  role: theoretical-foundation\\n  relevance_note: >\\n    Shows local (within-cluster) assessment of isotropy is more accurate than global assessment.\\n    Cluster-specific dominant directions encode structural (not semantic) information;\\n    removing them improves semantic task performance.\\n    LINK TO OUR WORK: Supports that within a semantic domain (one cluster), the dominant\\n    directions capture domain-level features rather than fine-grained type distinctions.\\n    This explains why MAVEN type embeddings are compressed: the shared \\\"event-ness\\\"\\n    dominates over type-specific semantics in the local embedding geometry.\\n\\n# =============================================================================\\n# NOVELTY THREAT ASSESSMENT (2026-05-15)\\n# =============================================================================\\n#\\n# 1. \\\"Type count vs type confusability\\\" disentangling:\\n#    ✅ NOVELTY SAFE — No prior work explicitly disentangles these two factors.\\n#    - IEPILE hard negatives: closest, but for training, not inference-time decomposition.\\n#    - Familiarity metric: measures label similarity for evaluation bias, not extraction.\\n#    - CROSSAGENTIE: resolves type confusion via debate, doesn't model as degradation channel.\\n#    Our multi-channel degradation model (count + confusability + context) is novel.\\n#\\n# 2. Schema decomposition baselines to compare:\\n#    - LLM-PEE (similarity partitioning) — MUST compare\\n#    - PARSE (LLM-driven schema rewriting) — MUST compare\\n#    - DEE (task-level decomposition) — discuss in related work\\n#    - SPT (schema as tools) — discuss in related work\\n#    - DLISC (Dual-LoRA schema caching) — discuss in related work\\n#\\n# 3. \\\"Lost in the Middle\\\" for IE:\\n#    ✅ OPPORTUNITY — No follow-up work applying it to IE task found.\\n#    We can be first to connect positional bias to schema prompt design.\\n#\\n# 4. Multi-agent approaches (CROSSAGENTIE, CMAS):\\n#    Growing area. Position clearly: we reduce confusion proactively via decomposition,\\n#    they resolve it reactively via debate. Complementary, not conflicting.\\n#\\n# 5. Overall novelty position:\\n#    STRONG — no prior work proposes (a) a formal multi-channel degradation model for\\n#    schema complexity in LLM IE, or (b) a DAG-based schema decomposition optimized\\n#    for type confusability. Main risk is CROSSAGENTIE's cross-type debate framing.\\n\", \"total_chars\": 18972, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11d5cd69-63c1-407a-9301-d369cda770e6",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "35529c0f-7e10-4571-adfd-acf875b894af",
  "sourceToolAssistantUUID": "11d5cd69-63c1-407a-9301-d369cda770e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T08:08:03.319Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HbSXekicsW2U7Dcr3UumAW`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35529c0f-7e10-4571-adfd-acf875b894af",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uU6bQy3phW56UYkdoD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aded0726-19f7-4646-882d-4a21648d797d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KegbyGqS9F4MJQzghnAVA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2942,
      "cache_read_input_tokens": 16770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 16 · 2026-05-16T08:08:03.334Z_

<details><summary>↩ Tool result · `toolu_01HbSXekicsW2U7Dcr3UumAW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_framing.md\", \"content\": \"# Paper Framing — schema-dag-extraction\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\\n- Commitment deadline: August 2, 2026\\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\\n- Deadline: ARR May 25, 2026 (10 days from today)\\n\\n## Core Claims (2 claims) — Revised per D019\\n\\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.\\n\\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\\n\\n~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — \\\"why naive decomposition fails\\\" is itself a contribution.\\n\\n## Story Spine — Revised per D012\\n\\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\\n\\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\\n\\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.\\n\\n- **Three-task validation**:\\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio\\n  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel\\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\\n\\n- **Headline result template**: \\\"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid.\\\"\\n\\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\\n\\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\\n\\nThese channels are orthogonal and independently addressable.\\n\\n**Pairwise vs Aggregated Confusability**:\\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).\\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\\n\\n## Evidence Hierarchy (D012)\\n\\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\\n\\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\\n\\n**Few-NERD (NER)** — Qwen3 embeddings:\\n- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation\\n- Nonzero-only Spearman ρ=0.272 (p=5e-5)\\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\\n- Immune to type frequency confound (operates at type-pair level)\\n\\n**MAVEN (ED)** — MiniLM embeddings:\\n- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap\\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\\n- Cross-task replication on same-domain schema\\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\\n\\n### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication\\n\\nLarge effect size, cross-task (RE), scaling with schema complexity:\\n\\n**Formal 80-rel study** (exp_fewrel_formal_80rel):\\n- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97\\n- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)\\n- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)\\n- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)\\n\\n**16-rel sanity check** (exp_fewrel_formal):\\n- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\\n\\n**Pilot extreme batches** (fewrel_pilot, MiniLM):\\n- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp\\n\\nKey insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling\\n\\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\\n\\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\\n\\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\\n\\nMethodological case study on when aggregated confusability measures fail:\\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\\n- This is stronger than \\\"domain boundary\\\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\\n\\n### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)\\n\\nIntraSub rate monotonically increases with BCS on both NER and RE:\\n\\n**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0\\n**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)\\n- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon\\n- Same mechanism, different absolute magnitudes — consistent with cross-task expectations\\n\\nAdditional from extreme batch design:\\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\\n\\n## Embedding Ablation (D010)\\n\\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\\n\\n### Per-type (Layer 2)\\n| | Few-NERD | FewRel | MAVEN |\\n|---|---|---|---|\\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\\n\\n### Pairwise (Layer 1)\\n| | Few-NERD | MAVEN |\\n|---|---|---|\\n| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |\\n| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |\\n\\n### SCS→Empirical Confusion Validation (exp-015 fast)\\n| | Qwen3 | MiniLM |\\n|---|---|---|\\n| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |\\n| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |\\n\\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\\n\\n## Venue Fit Risks\\n\\n- **\\\"Just an empirical study\\\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \\\"Lost in the Middle\\\" (TACL 2024).\\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy | Experiment |\\n|---------|------------------|------------|\\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\\n\", \"total_chars\": 11568, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aded0726-19f7-4646-882d-4a21648d797d",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "118dd0a2-38b8-4cb8-99d4-6990a1c2493e",
  "sourceToolAssistantUUID": "aded0726-19f7-4646-882d-4a21648d797d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T08:08:03.866Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KmG1JRJc9hQwjzR3JqCj2y`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "118dd0a2-38b8-4cb8-99d4-6990a1c2493e",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uU6bQy3phW56UYkdoD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e33d9e4-672c-4c87-bff2-c9c33355329f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KegbyGqS9F4MJQzghnAVA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2942,
      "cache_read_input_tokens": 16770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 18 · 2026-05-16T08:08:03.881Z_

<details><summary>↩ Tool result · `toolu_01KmG1JRJc9hQwjzR3JqCj2y`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/memory.md\", \"content\": \"# Memory — schema-dag-extraction\\n\\n## exp-018 结果与经验（2026-05-16）\\n- **结果**: confusability_aware 0.8021 > random 0.7877±0.0178 (CI上界0.7967)，提升显著 +1.44pp\\n- single_pass 80-rel 全量仅 0.5042，schema overload 严重\\n- Graph coloring (Welsh-Powell) 将 intra-batch BCS 从 0.5585 降到 0.5524\\n- 51 types improved, 28 degraded — 效果非均匀，部分 type 受益更多\\n- **关键参数**: 80-rel pool, batch_size=8-rel per batch, 15 random seeds for CI, 960 samples\\n- **无 merge amplification** — RE closed-set 验证了 Director 的预判\\n- FLASHINFER_DISABLE_VERSION_CHECK=1 需要设置，否则 vLLM 启动失败\\n- 支持 --resume 断点续传（按 condition 粒度）\\n\\n## exp-018 定位澄清（2026-05-16, Director）\\n- exp-018 不是\\\"重试 SDGD\\\"，而是\\\"confusability-aware batching 在 RE closed-set classification 上的实用方案\\\"\\n- RE 每个 (head, tail) pair 独立分类，无实体边界合并 → 无 merge amplification 问题\\n- exp-008 SDGD 失败的 root cause = NER span overlap 的 merge amplification，不适用于 RE\\n- 论文写法：§5 SDGD 失败因 NER merge amplification，但 RE closed-set 避免了此问题 → practical recommendation\\n\\n## exp-017 GPT-4o-mini（2026-05-16, Director 决定放弃）\\n- TUM proxy 未部署在 AutoDL 服务器，无法访问 OpenAI API\\n- 闭源模型验证缺失已在 discussion.tex limitations 中说明\\n- 教训：API 实验需要预先确认 proxy 可达性\\n\\n## D035 集成方案（2026-05-16）\\n- 论文 Table 3 用**极端批次**方法（BCS 最低/最高各 ~5 batches 的 accuracy Δ），不是四分位\\n- D033 的 7.42pp 是四分位比较，需要用极端批次方法重算\\n- 80-pool-16sub 的 3.92pp 也是四分位，同样需要重算\\n- 四分位 CI 作为补充证据报告，展示效应在不同分析粒度下都稳健\\n- 两组数据一起集成到论文再编译上传\\n\\n## 80-pool-16sub 关键发现（2026-05-16）\\n- BCS 范围窄 [0.458, 0.684]（vs 独立 16-rel [0.653, 0.900]），因为从 80-rel pool 采样的 16 types 语义更分散\\n- 四分位 Δ CI 跨零 [-7.79, +0.42]，但回归斜率 CI 不跨零 [-0.684, -0.062]\\n- 效应弱于独立 16-rel pool——BCS 范围压缩导致效应量缩小，这本身支持 BCS 是驱动因素的论点\\n- 决策：用回归斜率做跨条件比较（斜率控制了 BCS 范围差异），四分位 Δ 作为直觉可读的补充\\n\\n## MAVEN per-type BCS 正相关是 artifact（2026-05-16）\\n- exp_maven_residualized_bcs 确认：控制 log_freq + degree_centrality 后相关消失\\n- MiniLM confound = frequency, Qwen3 confound = degree centrality (r=0.854)\\n- 同质 schema（MAVEN 168 event types 多来自 FrameNet）下 per-type BCS 聚合失效\\n- pairwise SCS 仍然有效\\n\\n## Few-NERD r 值差异根因（2026-05-16）\\n- 三个 r 值同源（同一 confusion matrix, 1953 pairs），差异仅因 Y 变量：rate=0.112, count=0.138, CI上界=0.156\\n- Table 2 r=0.112 正确（confusion rate，归一化 gold frequency）\\n- p-values 已修正：Few-NERD Pearson p=7×10⁻⁷, MAVEN p=7×10⁻⁴²\\n\", \"total_chars\": 2127, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e33d9e4-672c-4c87-bff2-c9c33355329f",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "bdee7edb-cf4b-46e3-8dd1-e814e03d8365",
  "sourceToolAssistantUUID": "5e33d9e4-672c-4c87-bff2-c9c33355329f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-16T08:08:06.873Z_

Now let me look at the actual paper files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdee7edb-cf4b-46e3-8dd1-e814e03d8365",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uURHZGwiANBemSjebr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e52ed1f6-5b73-42d6-9dbd-69a1c3650e5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWu7tiz6HGaoz73eUFRCcU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12391,
      "cache_read_input_tokens": 19712,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12391,
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

_source line 20 · 2026-05-16T08:08:07.358Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012zrLXB7aDZFc7SrHe7d124`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e52ed1f6-5b73-42d6-9dbd-69a1c3650e5a",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uURHZGwiANBemSjebr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aadf4bb8-91b5-4a00-a4a9-adbd4485ac75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWu7tiz6HGaoz73eUFRCcU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12391,
      "cache_read_input_tokens": 19712,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12391,
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

_source line 21 · 2026-05-16T08:08:07.389Z_

<details><summary>↩ Tool result · `toolu_012zrLXB7aDZFc7SrHe7d124`</summary>

```text
artifacts/dream_reports/dream_20260515T053106/best/paper.tex
artifacts/dream_reports/dream_20260515T053106/median/paper.tex
artifacts/dream_reports/dream_20260515T053106/worst/paper.tex
artifacts/dream_reports/dream_20260515T113743/best/paper.tex
artifacts/dream_reports/dream_20260515T113743/median/paper.tex
artifacts/dream_reports/dream_20260515T113743/worst/paper.tex
artifacts/dream_reports/dream_20260515T140829/best/paper.tex
artifacts/dream_reports/dream_20260515T140829/median/paper.tex
artifacts/dream_reports/dream_20260515T140829/worst/paper.tex
artifacts/_project/paper/dataset_stats.tex
artifacts/paper/tables/dataset_stats.tex
artifacts/_project/paper/sdgd_negative.tex
artifacts/_project/paper/experimental_setup.tex
docs/paper/conclusion.tex
docs/paper/prompt_appendix.tex
artifacts/_project/paper/results.tex
docs/paper/related_work.tex
docs/paper/checklist.tex
docs/paper/experimental_setup.tex
docs/paper/results.tex
docs/paper/main.tex
docs/paper/discussion.tex
artifacts/dream_reports/dream_20260516T073533/best/paper.tex
docs/paper/sdgd_negative.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
artifacts/dream_reports/dream_20260516T073533/median/paper.tex
artifacts/dream_reports/dream_20260516T073533/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aadf4bb8-91b5-4a00-a4a9-adbd4485ac75",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "b49a38e1-7b7a-4cea-971c-82608cd98405",
  "sourceToolAssistantUUID": "aadf4bb8-91b5-4a00-a4a9-adbd4485ac75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T08:08:07.721Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01W9zEXq69W9e89KcFhxT8Z4`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b49a38e1-7b7a-4cea-971c-82608cd98405",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uURHZGwiANBemSjebr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1194bd34-f097-4365-a37a-e0625fd035ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWu7tiz6HGaoz73eUFRCcU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12391,
      "cache_read_input_tokens": 19712,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12391
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 19712,
          "cache_creation_input_tokens": 12391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12391,
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

_source line 23 · 2026-05-16T08:08:07.746Z_

<details><summary>↩ Tool result · `toolu_01W9zEXq69W9e89KcFhxT8Z4`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1194bd34-f097-4365-a37a-e0625fd035ca",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "635bdf7d-f257-4116-8901-901b5a74abff",
  "sourceToolAssistantUUID": "1194bd34-f097-4365-a37a-e0625fd035ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T08:08:10.794Z_

<details open><summary>🔧 Tool call — Read · `toolu_017x8RRtEzQpJ8Q9aJJThDxA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "635bdf7d-f257-4116-8901-901b5a74abff",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uUhQvEVi9oGR9ppSjV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83133f03-7a81-4439-bce9-9a0939f683ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FG3TpuHzK61eZ7eHaN2YWj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 32103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 772,
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

_source line 25 · 2026-05-16T08:08:10.809Z_

<details><summary>↩ Tool result · `toolu_017x8RRtEzQpJ8Q9aJJThDxA`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	
16	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\input{abstract}
24	
25	\input{introduction}
26	
27	\input{related_work}
28	
29	\input{experimental_setup}
30	
31	\input{results}
32	
33	\input{sdgd_negative}
34	
35	\input{discussion}
36	
37	\section*{Limitations}
38	\begin{enumerate}[leftmargin=*,itemsep=2pt]
39	\item \textbf{Single primary model.} The primary experiments use Qwen3-32B. Channel~1 has been validated on Llama-3.1-8B-Instruct (recall decline $-$43\,pp, $r = 0.725$). Channel~2 was validated on FewRel RE ($\Delta = -27.1$\,pp at count 8, $-23.9$\,pp at count 16), with high-BCS accuracy converging to a floor consistent across both tested models ($\approx$0.51). On Few-NERD NER, Channel~2 was not robustly detectable at 8B scale, likely due to floor effects and the noisier text-match metric.
40	
41	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of the variance in type confusion. Entity frequency, prompt position effects, mention ambiguity, context complexity, and type definition quality likely account for the remaining variance.
42	
43	\item \textbf{Cross-pool slope consistency.} The BCS--accuracy slopes are statistically indistinguishable across pools (permutation $p = 0.598$), indicating consistent per-unit sensitivity. The 80-relation extreme-batch gap (31.2\,pp) reflects the wider BCS range in that pool, not a stronger underlying effect; the independent 16-relation pool yields a bootstrapped quartile $\Delta$ of $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]). A within-pool comparison (Table~\ref{tab:within_pool}) confirms this interpretation: slope $-$0.401, CI excludes zero.
44	
45	\item \textbf{Non-significant factorial test.} A within-dataset factorial analysis (count $\times$ BCS) on Few-NERD did not reach significance (Appendix~\ref{sec:appendix_factorial}). The cross-pool slope consistency suggests that confusability sensitivity is stable rather than amplifying with schema size; larger pools simply expose more of the BCS spectrum.
46	
47	\item \textbf{Decomposition scope.} RE batch composition is tested on a single dataset (FewRel) with one model; whether the +1.4\,pp gain generalizes to other RE datasets, ED tasks, or models remains untested. Calibration-aware or joint-decoding merge alternatives for NER remain unexplored.
48	
49	\item \textbf{Metric scope.} SCS/BCS relies on embedding cosine similarity; alternative metrics such as label entropy or ontological depth may capture complementary dimensions of schema difficulty.
50	
51	\item \textbf{FewRel evaluation scope.} FewRel evaluation combines training and validation splits to obtain 80 relation types, as the validation split covers only 16 relations. FewRel is a classification task (given entity pair, predict relation) rather than open extraction; our results characterize schema effects on classification accuracy rather than end-to-end extraction.
52	
53	\item \textbf{RE format specificity.} RE's clean channel separation may partly reflect its closed-set classification format, which eliminates the entity detection dimension; whether the pattern holds for open extraction remains to be tested.
54	
55	\item \textbf{Model coverage.} Our experiments cover two open-weight model families (Qwen3-32B and Llama-3.1-8B); whether the same patterns hold for proprietary models (e.g., GPT-4, Gemini) remains to be verified.
56	
57	\item \textbf{Causal mechanism.} The present study establishes correlational evidence linking schema confusability to type substitution; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway.
58	\end{enumerate}
59	
60	\input{checklist}
61	
62	\bibliography{references}
63	
64	\appendix
65	
66	\section{Additional Figures}
67	\label{sec:appendix_figures}
68	
69	\begin{table}[h]
70	\centering
71	\small
72	\begin{tabular}{lrr}
73	\toprule
74	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
75	\midrule
76	1 & 0.702 & 0.640 \\
77	64 & 0.273 & 0.304 \\
78	\midrule
79	Decline & $-$43\,pp & $-$34\,pp \\
80	\bottomrule
81	\end{tabular}
82	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
83	\label{tab:cross_model}
84	\end{table}
85	
86	\begin{table}[h]
87	\centering
88	\small
89	\resizebox{\columnwidth}{!}{%
90	\begin{tabular}{crrrrrr}
91	\toprule
92	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
93	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
94	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
95	\midrule
96	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
97	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
98	\bottomrule
99	\end{tabular}}
100	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
101	\label{tab:cross_model_bcs}
102	\end{table}
103	
104	\begin{table}[h]
105	\centering
106	\small
107	\resizebox{\columnwidth}{!}{%
108	\begin{tabular}{llrrrrrrr}
109	\toprule
110	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
111	\cmidrule(lr){3-7}
112	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
113	\midrule
114	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
115	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}10^{-6}$ \\
116	\midrule
117	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
118	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
119	\bottomrule
120	\end{tabular}}
121	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}
122	\label{tab:error_taxonomy}
123	\end{table}
124	
125	\begin{figure}[h]
126	\centering
127	\includegraphics[width=\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}
128	\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic.}
129	\label{fig:error_taxonomy}
130	\end{figure}
131	
132	\section{SDGD Full Protocol and Results}
133	\label{sec:appendix_sdgd}
134	
135	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
136	
137	Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\ref{tab:sdgd_results}).
138	
139	\begin{table}[h]
140	\centering
141	\small
142	\resizebox{\columnwidth}{!}{%
143	\begin{tabular}{lrccc}
144	\toprule
145	\textbf{Mode} & \textbf{\# Batches} & \textbf{Precision} & \textbf{Recall} & \textbf{F1} \\
146	\midrule
147	single\_pass & 1 & 0.563 & 0.368 & 0.445 \\
148	\midrule
149	sdgd\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\
150	random\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\
151	per\_type & 66 & 0.194 & 0.586 & 0.292 \\
152	\midrule
153	sdgd\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\
154	random\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\
155	\bottomrule
156	\end{tabular}}
157	\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \texttt{min\_batch\_size=8} (reducing 8$\to$4 batches for sdgd\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}
158	\label{tab:sdgd_results}
159	\end{table}
160	
161	Decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.
162	
163	Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\_zero: 0.210$\to$0.324; random\_batch: 0.249$\to$0.331), but at the cost of disproportionate recall loss (0.314$\to$0.191; 0.446$\to$0.276), yielding lower F1 in both modes (sdgd\_zero: 0.251$\to$0.241; random\_batch: 0.320$\to$0.301).
164	
165	\section{Factorial Analysis}
166	\label{sec:appendix_factorial}
167	
168	We conducted a within-dataset $2\!\times\!2$ factorial analysis (count $\times$ BCS) on Few-NERD to test whether the two degradation channels exhibit a statistical interaction. The interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), likely underpowered due to BCS range compression in high-count schemas. Cross-pool slope analysis on FewRel (\S\ref{sec:bcs_controlled}) shows consistent BCS--accuracy sensitivity across pool sizes (permutation $p = 0.598$), suggesting that the per-unit confusability effect is stable rather than amplifying with schema size. A formal factorial test on FewRel was not conducted because the BCS-controlled design varies confusability within fixed count levels rather than crossing both factors.
169	
170	\section{Within-Pool CI Details}
171	\label{sec:appendix_within_pool}
172	
173	The quartile $\Delta$ for 80-pool 16-relation subsets ($-$3.92\,pp, 95\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.
174	
175	\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}
176	\label{sec:appendix_residualized_bcs}
177	
178	Section~\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.
179	
180	\paragraph{Confound identification.}
181	For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
182	\begin{itemize}[itemsep=2pt,leftmargin=*]
183	\item \textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.
184	\item \textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.
185	\end{itemize}
186	
187	\paragraph{Partial correlation results.}
188	Table~\ref{tab:residualized_bcs} reports raw Spearman $\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.
189	
190	\begin{table}[h]
191	\centering
192	\small
193	\resizebox{\columnwidth}{!}{%
194	\begin{tabular}{llcccc}
195	\toprule
196	\textbf{Embedding} & \textbf{Control} & \textbf{Raw $\rho$} & \textbf{Raw $p$} & \textbf{Partial $r$} & \textbf{Partial $p$} \\
197	\midrule
198	MiniLM & --- & $+$0.208 & 0.011 & --- & --- \\
199	MiniLM & log freq & --- & --- & $+$0.133 & 0.107 \\
200	MiniLM & log freq $+$ degree & --- & --- & --- & 0.226 \\
201	\midrule
202	Qwen3 & --- & $+$0.184 & 0.025 & --- & --- \\
203	Qwen3 & degree centrality & --- & --- & $+$0.063 & 0.442 \\
204	Qwen3 & log freq $+$ degree & --- & --- & --- & 0.439 \\
205	\bottomrule
206	\end{tabular}}
207	\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \texttt{exp\_maven\_residualized\_bcs}.}
208	\label{tab:residualized_bcs}
209	\end{table}
210	
211	\paragraph{Interpretation.}
212	The two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.
213	
214	Under joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 10^{-10}$; Table~\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.
215	
216	\input{prompt_appendix}
217	
218	\section{Prompt Version Sensitivity Analysis}
219	\label{sec:appendix_prompt_sensitivity}
220	
221	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
222	
223	\paragraph{RE (FewRel).}
224	Under the v1 prompt, the extreme-batch BCS gap is $-$31.2\,pp (low-BCS 82.3\% vs.\ high-BCS 51.0\%; Table~\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI: [22.4, 28.6]; $p < 0.0001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.
225	
226	\paragraph{NER (Few-NERD).}
227	The batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\,=\,12$, $r = +0.58$ ($p = 0.002$, 95\% CI: [0.19, 0.81]) vs.\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \S\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.
228	
229	\paragraph{Interpretation.}
230	The $n{=}25$ v2 result confirms that the confusability effect is robust to prompt design: the gap narrows modestly ($-$5.7\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\% vs.\ 82.3\%), but type confusion under high confusability persists (59.7\% vs.\ 51.0\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.
231	
232	\section{BCS Aggregation Sensitivity}
233	\label{sec:appendix_bcs_sensitivity}
234	
235	We define Batch Confusability Score (BCS) as the \emph{mean} pairwise SCS across all type pairs in a batch (\S\ref{sec:bcs_controlled}). An alternative definition takes the \emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.
236	
237	\begin{table}[h]
238	\centering
239	\small
240	\resizebox{\columnwidth}{!}{%
241	\begin{tabular}{llcccc}
242	\toprule
243	\textbf{Aggregation} & \textbf{Condition} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} \\
244	\midrule
245	MEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}10^{-6}$ \\
246	MEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
247	\midrule
248	MAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}10^{-12}$ \\
249	MAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
250	\bottomrule
251	\end{tabular}}
252	\caption{BCS--accuracy regression under mean vs.\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p = 0.598$; MAX $p = 0.436$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}
253	\label{tab:bcs_aggregation}
254	\end{table}
255	
256	MAX aggregation yields stronger correlations ($r = -0.637$ vs.\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch drives substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.
257	
258	\end{document}
259	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83133f03-7a81-4439-bce9-9a0939f683ff",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "6700804a-ba29-42f7-90ce-5f7f2c55e3de",
  "sourceToolAssistantUUID": "83133f03-7a81-4439-bce9-9a0939f683ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-16T08:08:11.403Z_

<details open><summary>🔧 Tool call — Read · `toolu_016xWjyKPBb2NNmcfCrtbPPL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6700804a-ba29-42f7-90ce-5f7f2c55e3de",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uUhQvEVi9oGR9ppSjV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed3736ce-bfc5-4ccb-afc1-5f2814d696fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FG3TpuHzK61eZ7eHaN2YWj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 32103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 772,
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

_source line 27 · 2026-05-16T08:08:11.415Z_

<details><summary>↩ Tool result · `toolu_016xWjyKPBb2NNmcfCrtbPPL`</summary>

```text
1	% References for Schema-DAG-Extraction
2	% Generated: 2026-05-15
3	% Sources: literature_map.yaml + references_survey.md
4	
5	% =============================================================================
6	% DIRECT COMPETITORS
7	% =============================================================================
8	
9	@inproceedings{llm-pee-2025,
10	    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},
11	    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
12	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
13	    year      = {2025},
14	    url       = {https://aclanthology.org/2025.emnlp-main.1743/},
15	}
16	
17	@article{parse-2025,
18	    title   = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},
19	    author  = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},
20	    journal = {arXiv preprint arXiv:2510.08623},
21	    year    = {2025},
22	    url     = {https://arxiv.org/abs/2510.08623},
23	}
24	
25	@inproceedings{dee-2024,
26	    title     = {Decompose, Enrich, and Extract! Schema-aware Event Extraction using {LLM}s},
27	    author    = {Shiri, Fatemeh and Nguyen, Van and Moghimifar, Farhad and Yoo, John and Haffari, Gholamreza and Li, Yuan-Fang},
28	    booktitle = {Proceedings of the IEEE International Conference on Tools with Artificial Intelligence},
29	    year      = {2024},
30	    url       = {https://arxiv.org/abs/2406.01045},
31	}
32	
33	@inproceedings{crossagentie-2025,
34	    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},
35	    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},
36	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
37	    year      = {2025},
38	    url       = {https://aclanthology.org/2025.findings-acl.718/},
39	}
40	
41	@article{dlisc-2025,
42	    title   = {Effective and Efficient Schema-aware Information Extraction Using On-Device {LLM}s},
43	    author  = {Wen, Zhihao and Liang, Sheng and Wu, Yaxiong and Zhang, Yongyue and Liu, Yong},
44	    journal = {arXiv preprint arXiv:2505.14992},
45	    year    = {2025},
46	    url     = {https://arxiv.org/abs/2505.14992},
47	}
48	
49	@article{spt-2025,
50	    title   = {Schema as Parameterized Tools for Universal Information Extraction},
51	    author  = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},
52	    journal = {arXiv preprint arXiv:2506.01276},
53	    year    = {2025},
54	    url     = {https://arxiv.org/abs/2506.01276},
55	}
56	
57	
58	@inproceedings{cmas-ner-2025,
59	    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},
60	    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},
61	    booktitle = {Proceedings of the ACM Web Conference 2025},
62	    year      = {2025},
63	    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},
64	    doi       = {10.1145/3696410.3714923},
65	}
66	
67	% =============================================================================
68	% METHOD COMPONENTS
69	% =============================================================================
70	
71	@inproceedings{uniner-2024,
72	    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
73	    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
74	    booktitle = {International Conference on Learning Representations},
75	    year      = {2024},
76	    url       = {https://arxiv.org/abs/2308.03279},
77	}
78	
79	@inproceedings{gollie-2024,
80	    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
81	    author    = {Sainz, Oscar and Garc{\'\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},
82	    booktitle = {International Conference on Learning Representations},
83	    year      = {2024},
84	    url       = {https://arxiv.org/abs/2310.03668},
85	}
86	
87	@inproceedings{gliner-2024,
88	    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},
89	    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},
90	    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},
91	    year      = {2024},
92	    url       = {https://arxiv.org/abs/2311.08526},
93	}
94	
95	@inproceedings{gliner2-2025,
96	    title     = {{GLiNER2}: Efficient Multi-Task {IE} System with Schema-Driven Interface},
97	    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},
98	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},
99	    year      = {2025},
100	    url       = {https://arxiv.org/abs/2507.18546},
101	}
102	
103	@inproceedings{kggen-2025,
104	    title     = {{KGGen}: Extracting Knowledge Graphs from Plain Text with Language Models},
105	    author    = {Mo, Belinda and Yu, Kyssen and Kazdan, Joshua and Cabezas, Joan and Mpala, Proud and Yu, Lisa and Cundy, Chris and Kanatsoulis, Charilaos and Koyejo, Sanmi},
106	    booktitle = {Advances in Neural Information Processing Systems},
107	    year      = {2025},
108	    url       = {https://arxiv.org/abs/2502.09956},
109	}
110	
111	
112	@inproceedings{iepile-2024,
113	    title     = {{IEPile}: Unearthing Large-Scale Schema-Based Information Extraction Corpus},
114	    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},
115	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
116	    year      = {2024},
117	    url       = {https://arxiv.org/abs/2402.14710},
118	}
119	
120	@article{lost-in-middle-2024,
121	    title   = {Lost in the Middle: How Language Models Use Long Contexts},
122	    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},
123	    journal = {Transactions of the Association for Computational Linguistics},
124	    volume  = {12},
125	    pages   = {157--173},
126	    year    = {2024},
127	    url     = {https://arxiv.org/abs/2307.03172},
128	    doi     = {10.1162/tacl_a_00638},
129	}
130	
131	% =============================================================================
132	% ZERO-SHOT NER / RE BASELINES
133	% =============================================================================
134	
135	
136	
137	@inproceedings{nuner-2024,
138	    title     = {{NuNER}: Entity Recognition Encoder Pre-training via {LLM}-Annotated Data},
139	    author    = {Bogdanov, Sergei and Constantin, Alexandre and Bernard, Timoth{\'e}e and Crabb{\'e}, Benoit and Bernard, Etienne},
140	    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
141	    year      = {2024},
142	    url       = {https://arxiv.org/abs/2402.15343},
143	}
144	
145	% =============================================================================
146	% EVALUATION / BENCHMARKING
147	% =============================================================================
148	
149	@inproceedings{familiarity-2025,
150	    title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},
151	    author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},
152	    booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics},
153	    year      = {2025},
154	    url       = {https://arxiv.org/abs/2412.10121},
155	}
156	
157	@inproceedings{guidex-2025,
158	    title     = {{GuideX}: Guided Synthetic Data Generation for Zero-Shot Information Extraction},
159	    author    = {De La Fuente, Neil and Sainz, Oscar and Garc{\'\i}a-Ferrero, Iker and Agirre, Eneko},
160	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
161	    year      = {2025},
162	    url       = {https://arxiv.org/abs/2506.00649},
163	}
164	
165	% =============================================================================
166	% SURVEYS / BACKGROUND
167	% =============================================================================
168	
169	@article{llm4ie-survey-2024,
170	    title   = {Large Language Models for Generative Information Extraction: A Survey},
171	    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},
172	    journal = {Frontiers of Computer Science},
173	    volume  = {18},
174	    number  = {6},
175	    year    = {2024},
176	    url     = {https://arxiv.org/abs/2312.17617},
177	    doi     = {10.1007/s11704-024-40555-y},
178	}
179	
180	@inproceedings{knowcoder-2024,
181	    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},
182	    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
183	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
184	    year      = {2024},
185	    url       = {https://arxiv.org/abs/2403.07969},
186	}
187	
188	@inproceedings{slot-2025,
189	    title     = {{SLOT}: Structuring the Output of Large Language Models},
190	    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},
191	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},
192	    year      = {2025},
193	    url       = {https://aclanthology.org/2025.emnlp-industry.32/},
194	}
195	
196	% =============================================================================
197	% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION
198	% =============================================================================
199	
200	@inproceedings{gao-repr-degen-2019,
201	    title     = {Representation Degeneration Problem in Training Natural Language Generation Models},
202	    author    = {Gao, Jun and He, Di and Tan, Xu and Qin, Tao and Wang, Liwei and Liu, Tie-Yan},
203	    booktitle = {International Conference on Learning Representations},
204	    year      = {2019},
205	    url       = {https://arxiv.org/abs/1907.12009},
206	}
207	
208	@inproceedings{ethayarajh-contextual-2019,
209	    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},
210	    author    = {Ethayarajh, Kawin},
211	    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},
212	    year      = {2019},
213	    url       = {https://aclanthology.org/D19-1006/},
214	}
215	
216	@inproceedings{cai-isotropy-clusters-2021,
217	    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},
218	    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},
219	    booktitle = {International Conference on Learning Representations},
220	    year      = {2021},
221	    url       = {https://openreview.net/forum?id=xYGNO86OWDH},
222	}
223	
224	@inproceedings{godey-anisotropy-inherent-2024,
225	    title     = {Anisotropy Is Inherent to Self-Attention in Transformers},
226	    author    = {Godey, Nathan and de la Clergerie, {\'E}ric and Sagot, Beno{\^\i}t},
227	    booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics},
228	    year      = {2024},
229	    url       = {https://aclanthology.org/2024.eacl-long.3/},
230	}
231	
232	
233	% =============================================================================
234	% ADDITIONAL REFERENCES (from references_survey.md only)
235	% =============================================================================
236	
237	@article{instructuie-2023,
238	    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},
239	    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},
240	    journal = {arXiv preprint arXiv:2304.08085},
241	    year    = {2023},
242	    url     = {https://arxiv.org/abs/2304.08085},
243	}
244	
245	@inproceedings{codeie-2023,
246	    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
247	    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
248	    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},
249	    year      = {2023},
250	    url       = {https://aclanthology.org/2023.acl-long.855/},
251	}
252	
253	@inproceedings{adelie-2024,
254	    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},
255	    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},
256	    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
257	    year      = {2024},
258	    url       = {https://aclanthology.org/2024.emnlp-main.419/},
259	}
260	
261	@inproceedings{oneke-2025,
262	    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},
263	    author    = {Luo, Yujie and Yan, Lingyong and Liu, Zhenghao and Ji, Yixin and Wang, Weiqi and Yu, Shi and Yan, Yukun and Wang, Shuo and Zhang, Yue and Cao, Shulin and Ren, Weicheng and Gui, Honghao and Bi, Zhen and Huang, Yongfei and Yao, Yuan and Zhang, Ningyu and Chen, Huajun},
264	    booktitle = {Companion Proceedings of the ACM Web Conference 2025},
265	    year      = {2025},
266	    url       = {https://arxiv.org/abs/2412.20005},
267	    doi       = {10.1145/3701716.3715189},
268	}
269	
270	
271	@inproceedings{llm-calibration-survey-2024,
272	    title     = {A Survey of Confidence Estimation and Calibration in Large Language Models},
273	    author    = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},
274	    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},
275	    year      = {2024},
276	    url       = {https://aclanthology.org/2024.naacl-long.366/},
277	}
278	
279	
280	% =============================================================================
281	% DATASETS
282	% =============================================================================
283	
284	@inproceedings{fewnerd-2021,
285	    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},
286	    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},
287	    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},
288	    year      = {2021},
289	    url       = {https://aclanthology.org/2021.acl-long.248/},
290	}
291	
292	@inproceedings{fewrel-2018,
293	    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},
294	    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},
295	    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
296	    year      = {2018},
297	    url       = {https://aclanthology.org/D18-1514/},
298	}
299	
300	@inproceedings{maven-2020,
301	    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},
302	    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},
303	    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
304	    year      = {2020},
305	    url       = {https://aclanthology.org/2020.emnlp-main.129/},
306	}
307	
308	@inproceedings{docred-2019,
309	    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},
310	    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},
311	    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
312	    year      = {2019},
313	    url       = {https://aclanthology.org/P19-1074/},
314	}
315	
316	% =============================================================================
317	% MODELS AND TOOLS
318	% =============================================================================
319	
320	@article{qwen3-2025,
321	    title   = {Qwen3 Technical Report},
322	    author  = {{Qwen Team}},
323	    journal = {arXiv preprint arXiv:2505.09388},
324	    year    = {2025},
325	    url     = {https://arxiv.org/abs/2505.09388},
326	}
327	
328	@article{llama3-2024,
329	    title   = {The {Llama} 3 Herd of Models},
330	    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela and others},
331	    journal = {arXiv preprint arXiv:2407.21783},
332	    year    = {2024},
333	    url     = {https://arxiv.org/abs/2407.21783},
334	}
335	
336	@inproceedings{sentence-bert-2019,
337	    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},
338	    author    = {Reimers, Nils and Gurevych, Iryna},
339	    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},
340	    year      = {2019},
341	    url       = {https://aclanthology.org/D19-1410/},
342	}
343	
344	@inproceedings{minilm-2020,
345	    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},
346	    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},
347	    booktitle = {Advances in Neural Information Processing Systems},
348	    volume    = {33},
349	    year      = {2020},
350	    url       = {https://arxiv.org/abs/2002.10957},
351	}
352	
353	@inproceedings{reflect-learn-2026,
354	    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},
355	    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},
356	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
357	    pages     = {34923--34931},
358	    year      = {2026},
359	    url       = {https://arxiv.org/abs/2508.10036},
360	    doi       = {10.1609/aaai.v40i41.40796},
361	}
362	
363	@article{sclar-sensitivity-2024,
364	    title   = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},
365	    author  = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},
366	    journal = {Transactions of the Association for Computational Linguistics},
367	    volume  = {12},
368	    year    = {2024},
369	    url     = {https://arxiv.org/abs/2310.11324},
370	}
371	
372	@inproceedings{vllm-2023,
373	    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},
374	    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},
375	    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},
376	    year      = {2023},
377	    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},
378	}
379	
380	@inproceedings{xie-zeroshot-ner-2023,
381	    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},
382	    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},
383	    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
384	    year      = {2023},
385	    url       = {https://aclanthology.org/2023.emnlp-main.493/},
386	}
387	
388	@article{chatgpt-ie-eval-2023,
389	    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},
390	    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},
391	    journal = {arXiv preprint arXiv:2304.11633},
392	    year    = {2023},
393	    url     = {https://arxiv.org/abs/2304.11633},
394	}
395	
396	@inproceedings{wadhwa-re-llm-2023,
397	    title     = {Revisiting Relation Extraction in the era of Large Language Models},
398	    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},
399	    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},
400	    pages     = {15566--15589},
401	    year      = {2023},
402	    url       = {https://aclanthology.org/2023.acl-long.868/},
403	}
404	
405	@inproceedings{relationprompt-2022,
406	    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},
407	    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},
408	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},
409	    pages     = {45--57},
410	    year      = {2022},
411	    url       = {https://aclanthology.org/2022.findings-acl.5/},
412	}
413	
414	@article{promptner-2023,
415	    title   = {{PromptNER}: Prompting For Named Entity Recognition},
416	    author  = {Ashok, Dhananjay and Lipton, Zachary C.},
417	    journal = {arXiv preprint arXiv:2305.15444},
418	    year    = {2023},
419	    url     = {https://arxiv.org/abs/2305.15444},
420	}
421	
422	@article{json-schema-bench-2025,
423	    title   = {Generating Structured Outputs from Language Models: Benchmark and Studies},
424	    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},
425	    journal = {arXiv preprint arXiv:2501.10868},
426	    year    = {2025},
427	    url     = {https://arxiv.org/abs/2501.10868},
428	}
429	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed3736ce-bfc5-4ccb-afc1-5f2814d696fa",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "e776a3ec-8493-4446-9779-e82b7bdb5556",
  "sourceToolAssistantUUID": "ed3736ce-bfc5-4ccb-afc1-5f2814d696fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T08:08:11.694Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Jr5U11z7JXJWUVq576977Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e776a3ec-8493-4446-9779-e82b7bdb5556",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uUhQvEVi9oGR9ppSjV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "428405fb-fadd-4bbe-af51-6be7401f789f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FG3TpuHzK61eZ7eHaN2YWj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 32103,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 772
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 32103,
          "cache_creation_input_tokens": 772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 772,
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

_source line 29 · 2026-05-16T08:08:11.699Z_

<details><summary>↩ Tool result · `toolu_01Jr5U11z7JXJWUVq576977Q`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Training-Free LLM Information Extraction}
5	\label{sec:rw_training_free}
6	
7	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025}. Early evaluations of ChatGPT's extraction capabilities \cite{chatgpt-ie-eval-2023} and relation extraction under LLMs \cite{wadhwa-re-llm-2023} establish baselines for training-free IE. For relation extraction, \citet{relationprompt-2022} leverage prompts to generate synthetic training data for zero-shot relation triplet extraction. For NER, approaches include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, bidirectional encoders \cite{gliner-2024,gliner2-2025}, and guided synthesis \cite{guidex-2025,nuner-2024}; \citet{familiarity-2025} quantify label shifts in zero-shot NER evaluation. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
8	
9	\subsection{Schema Complexity in IE}
10	\label{sec:rw_schema}
11	
12	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which addresses event extraction with massive type inventories by partitioning schemas based on type embedding similarity. LLM-PEE clusters event types and assigns each cluster to a separate extraction prompt, demonstrating improved performance on schemas with hundreds of types. Our work is complementary in three respects. First, whereas LLM-PEE develops an engineering solution---partition to improve extraction---we conduct controlled empirical analysis to understand \emph{why} extraction degrades. Second, LLM-PEE does not disentangle the effects of type count from type confusability; their partitioning simultaneously reduces both. Our BCS-controlled experiments (\S\ref{sec:bcs_controlled}) isolate these as independent degradation channels. Third, our pairwise SCS analysis provides a theoretical explanation for why their similarity-based partitioning works: it reduces Batch Confusability Scores, directly targeting the Channel~2 degradation mechanism. Our SDGD experiments (\S\ref{sec:sdgd}) further reveal that the merge step---not partitioning quality---is the bottleneck in decompose-then-merge pipelines, a limitation that applies to LLM-PEE's approach as well.
13	
14	Other approaches address schema complexity from different angles: hard negative mining during training \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, event schema decomposition \cite{dee-2024}, multi-agent debate for cross-type IE \cite{crossagentie-2025,cmas-ner-2025}, schema-as-tool parameterization \cite{spt-2025}, on-device schema-aware IE \cite{dlisc-2025}, schema-constrained knowledge graph generation \cite{kggen-2025}, and active prompting guided by introspective confusion analysis \cite{reflect-learn-2026}. All treat schema complexity as an engineering problem; we instead treat it as a scientific question about the independent mechanisms by which schema properties degrade extraction.
15	
16	\subsection{Representation Degeneration and Embedding Anisotropy}
17	\label{sec:rw_anisotropy}
18	
19	Our centrality confound (\S\ref{sec:centrality_confound}) connects to this literature: embeddings degenerate into narrow cones \cite{gao-repr-degen-2019,ethayarajh-contextual-2019}, but local clusters can be isotropic \cite{cai-isotropy-clusters-2021}---explaining why MAVEN's single-ontology types conflate confusability with centrality. Since anisotropy is inherent to self-attention \cite{godey-anisotropy-inherent-2024}, this confound likely persists across architectures.
20	
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "428405fb-fadd-4bbe-af51-6be7401f789f",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "e0d7dc8a-9215-4abf-97ff-3285ccc6fa40",
  "sourceToolAssistantUUID": "428405fb-fadd-4bbe-af51-6be7401f789f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T08:08:15.633Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GYUANukidhfCe4Dj74jbBE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0d7dc8a-9215-4abf-97ff-3285ccc6fa40",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uUzM9m94jmyUoBLcMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "970d44b8-0d7b-4438-b089-ffb6332ec972",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxbpBPPuBSmgAGEUGmVt9C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16979,
      "cache_read_input_tokens": 32875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16979,
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

_source line 31 · 2026-05-16T08:08:15.639Z_

<details><summary>↩ Tool result · `toolu_01GYUANukidhfCe4Dj74jbBE`</summary>

```text
1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level). Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and four datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall in NER and RE, but reverses direction in MAVEN (168 event types) due to centrality confounds in same-domain schemas as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE (a closed-set classification task); in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes and prompt designs: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.60$), with the quartile gap reaching $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]), though pairwise effect sizes are modest ($r^2 = 1.3\text{--}1.7\%$) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability-aware decomposition yields an informative negative result for NER---merge amplification destroys precision across all strategies---but succeeds for RE, where confusability-aware batch composition recovers +1.4\,pp accuracy over random batching, demonstrating a directionally consistent application of our diagnostic framework.
3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "970d44b8-0d7b-4438-b089-ffb6332ec972",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "95d96170-09ba-476e-a882-856962242f51",
  "sourceToolAssistantUUID": "970d44b8-0d7b-4438-b089-ffb6332ec972",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T08:08:16.122Z_

<details open><summary>🔧 Tool call — Read · `toolu_016PderSaej2u1YE64Mwioej`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95d96170-09ba-476e-a882-856962242f51",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uUzM9m94jmyUoBLcMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c60696bd-c23d-40ef-bee3-5124f041dbb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxbpBPPuBSmgAGEUGmVt9C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16979,
      "cache_read_input_tokens": 32875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16979,
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

_source line 33 · 2026-05-16T08:08:16.129Z_

<details><summary>↩ Tool result · `toolu_016PderSaej2u1YE64Mwioej`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combination---accounts for the observed gains. More broadly, all prior approaches conflate two distinct mechanisms that could independently degrade extraction: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these factors, decomposition strategies cannot be principled: they optimize a black-box objective without understanding its components.
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
9	
10	To answer these questions, we conduct the first controlled empirical study that isolates type confusability from type count across three IE tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED). We introduce the \emph{Schema Confusability Score} (SCS), which quantifies pairwise semantic overlap between types using embedding cosine similarity, and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). We design two complementary experimental paradigms: \emph{count curves} that vary schema size while randomizing confusability, and \emph{BCS-controlled experiments} that fix schema size while varying confusability. We evaluate on four datasets spanning diverse schema structures: Few-NERD \cite{fewnerd-2021} (66 entity types across 8 domains), FewRel \cite{fewrel-2018} (80 relation types, sentence-level), DocRED \cite{docred-2019} (96 relation types, document-level), and MAVEN \cite{maven-2020} (168 event types from a single ontology). All experiments use Qwen3-32B in a zero-shot prompting setup with bootstrap confidence intervals.
11	
12	Our experiments yield five findings: (1)~schema-induced degradation operates through two channels---count-driven recall decline (up to $-$49\,pp on DocRED) and confusability-driven type confusion---that are separable in RE; in NER, confusability additionally impairs entity detection; (2)~pairwise SCS predicts type confusion across tasks ($r = 0.112$--$0.129$), modest in magnitude but the first factor empirically isolated in controlled zero-shot IE; (3)~confusability effects are robust across schema sizes, granularities, and prompt designs, with BCS--accuracy slopes consistent between 16-type and 80-type pools (permutation $p = 0.60$) and replicating on DocRED's 96-relation document-level schema (slope $= -0.71$, $R^2 = 0.53$); (4)~per-type confusability aggregation is confounded by centrality on homogeneous schemas; and (5)~confusability-aware NER decomposition fails due to merge amplification (best F1 = 0.32 vs.\ single-pass 0.45), but confusability-aware RE batch composition yields a directional +1.4\,pp gain over random batching ($p \approx 0.19$, not significant), suggesting task-dependent applicability of the diagnostic framework.
13	
14	Our contributions are:
15	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
16	    \item \textbf{Robust multi-channel degradation pattern.} We identify two empirical degradation channels---count and confusability---across NER, RE (sentence- and document-level), and ED, revealing task-dependent channel behavior.
17	    \item \textbf{Pairwise confusability as a statistically significant but modest predictor.} We demonstrate that pairwise SCS predicts type confusion across tasks and embedding models, while identifying a centrality confound that invalidates per-type aggregation on homogeneous schemas.
18	    \item \textbf{Cross-task controlled experiments.} We present BCS-controlled experiments with bootstrap confidence intervals on four datasets, establishing that the BCS--accuracy relationship is consistent across schema sizes (slope permutation $p = 0.60$) and replicates at document level (DocRED slope $= -0.71$, $R^2 = 0.53$).
19	    \item \textbf{From diagnosis to mitigation.} Our SDGD experiments identify merge amplification as a structural challenge for NER decomposition, and show that for RE---where fixed entity pairs eliminate span reconciliation---a confusability-aware batching strategy yields directional improvement (+1.4\,pp) over random batching, suggesting practical utility of confusability diagnostics (\S\ref{sec:sdgd}).
20	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c60696bd-c23d-40ef-bee3-5124f041dbb3",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "c384334d-bfdd-4641-87cb-0cb214a96b1e",
  "sourceToolAssistantUUID": "c60696bd-c23d-40ef-bee3-5124f041dbb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-16T08:08:16.806Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GLmiWi5PhHGscX2NHXEanc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c384334d-bfdd-4641-87cb-0cb214a96b1e",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uUzM9m94jmyUoBLcMW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83f77cc1-dfb0-4cb7-8680-c132ad525ecc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxbpBPPuBSmgAGEUGmVt9C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16979,
      "cache_read_input_tokens": 32875,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16979
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 32875,
          "cache_creation_input_tokens": 16979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16979,
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

_source line 35 · 2026-05-16T08:08:16.834Z_

<details><summary>↩ Tool result · `toolu_01GLmiWi5PhHGscX2NHXEanc`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions and schema design.}
5	The two-channel decomposition applies most cleanly to cross-domain schemas; for same-domain schemas, pairwise SCS should be used directly or with centrality factored out (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% on both tested models; one possible explanation is a task-inherent difficulty ceiling that scaling alone cannot overcome, though broader model coverage is needed to confirm this hypothesis. RE's clean channel separation may partly reflect its closed-set classification format, which eliminates the entity detection dimension; whether the pattern holds for open extraction remains to be tested. The effect further generalizes to document-level RE (DocRED, 96 types), where steeper BCS--accuracy slopes ($-$0.71) may reflect the compounding of cross-sentence reasoning difficulty with type confusion. Practitioners should monitor BCS when assembling schemas and prefer cross-domain type groupings that minimize intra-batch similarity. Prompt design also modulates the confusability effect: switching from v1 to v2 prompts reduces the RE BCS gap from 31.2\,pp to 25.5\,pp ($n{=}25$, $p < 0.0001$, $r = -0.919$; Appendix~\ref{sec:appendix_prompt_sensitivity}), confirming that format constraints partially mitigate but do not eliminate type confusion.
6	
7	\paragraph{Future directions.}
8	For NER, naive decompose-then-merge pipelines fail due to merge amplification (\S\ref{sec:sdgd}). Three directions may address this: (1)~calibration-aware merge with cross-batch confidence normalization; (2)~confusability-aware joint decoding; and (3)~hierarchical coarse-to-fine extraction. For RE, confusability-aware batch composition shows initial promise (+1.4\,pp); extending this to broader RE benchmarks and document-level tasks is a natural next step.
9	
10	\section{Conclusion}
11	\label{sec:conclusion}
12	
13	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE, with Channel~2 additionally impairing entity detection in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\Delta = -27$\,pp) and across extraction granularities (DocRED document-level RE: count decline $-$49\,pp; BCS slope $= -0.71$, $R^2 = 0.53$), with high-BCS accuracy converging to a floor consistent across both tested models. We further identified a centrality confound on same-domain schemas, demonstrated that merge amplification is a structural challenge for NER decomposition, and showed that confusability-aware batch composition recovers +1.4\,pp on RE where span reconciliation is unnecessary. Cross-batch calibration or joint decoding for NER, and broader validation of RE batch composition, are the key next steps.
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83f77cc1-dfb0-4cb7-8680-c132ad525ecc",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "9f1f5500-78cd-4e5e-bad6-9e2b091ae4fd",
  "sourceToolAssistantUUID": "83f77cc1-dfb0-4cb7-8680-c132ad525ecc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-16T08:08:19.900Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Db1xhhwDW3XgLzKP1CGpFx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f1f5500-78cd-4e5e-bad6-9e2b091ae4fd",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uVNRwMoXdAYiBGKmJF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59b7a399-110b-4c50-8e7f-5468eb59e384",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNdYjcZNkGxuvn3Myd4uoz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3288,
      "cache_read_input_tokens": 49854,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3288,
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

_source line 37 · 2026-05-16T08:08:19.914Z_

<details><summary>↩ Tool result · `toolu_01Db1xhhwDW3XgLzKP1CGpFx`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample balanced instances and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.
17	
18	\paragraph{MAVEN (ED).}
19	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
20	
21	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{llrrlll}
28	\toprule
29	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embedding} \\
30	\midrule
31	Few-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\
32	FewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\
33	DocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\
34	MAVEN & ED & 168 & 18{,}904\rlap{$^\dagger$} & Same & 0.87--0.97 & MiniLM \\
35	\bottomrule
36	\end{tabular}}
37	\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}
38	\label{tab:datasets}
39	\end{table}
40	
41	\subsection{Schema Confusability Score (SCS)}
42	\label{sec:scs}
43	
44	We introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\text{name}(t)$, an embedding function $\text{embed}(\cdot)$ maps the type name to a vector representation. The \textbf{pairwise SCS} between types $t_i$ and $t_j$ is:
45	{\small
46	\[
47	\text{SCS}(t_i, t_j) = \cos\bigl(\text{embed}(\text{name}(t_i)),\; \text{embed}(\text{name}(t_j))\bigr)
48	\]
49	}
50	
51	For a batch of types $B = \{t_1, \ldots, t_k\}$, the \textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:
52	\[
53	\text{BCS}(B) = \frac{1}{\binom{k}{2}} \sum_{i < j,\; t_i, t_j \in B} \text{SCS}(t_i, t_j)
54	\]
55	
56	We compute SCS with two embedding models: (1)~Qwen3-32B \cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. Both use type name strings only, without definitions or descriptions, to reflect the information available to the model at inference time.
57	
58	\subsection{Experimental Design}
59	\label{sec:exp_design}
60	
61	We conduct two complementary experimental paradigms.
62	
63	\paragraph{Experiment 1: Count Curves.}
64	We vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \{1, 2, 6, 12, 22, 44, 64\} for Few-NERD, \{1, 4, 8, 16, 32, 64, 80\} for FewRel, \{1, 4, 8, 16, 32, 64, 96\} for DocRED, and \{1, 6, 12, 22, 44, 64\} for MAVEN.
65	
66	\paragraph{Experiment 2: BCS-Controlled.}
67	We fix the type count and vary the Batch Confusability Score to isolate the effect of inter-type similarity from schema size. For each count level, we construct one low-BCS batch (types with the lowest pairwise similarities), one high-BCS batch (types with the highest pairwise similarities), and 25 random batches (27 total per count level). We run this paradigm on Few-NERD at count$\,\in\{6, 12\}$, on FewRel at count$\,\in\{8, 16\}$ (evaluated on both a 16-relation pool and the full 80-relation pool), and on DocRED at count$\,\in\{16, 32\}$. To control for cross-pool type differences, we additionally draw 16-relation subsets from the 80-relation pool and evaluate under the same protocol, enabling a within-pool comparison that isolates confusability from pool composition. For MAVEN, we conduct analogous BCS-controlled experiments at count$\,\in\{6, 12\}$ with 27 batches per level; however, the same-domain nature of MAVEN's FrameNet-derived types introduces a centrality confound that complicates BCS interpretation. We report these results separately in \S\ref{sec:centrality_confound}.
68	
69	\subsection{Evaluation Metrics}
70	\label{sec:metrics}
71	
72	We use task-appropriate metrics that reflect the distinct nature of each extraction problem.
73	
74	\paragraph{NER (Few-NERD): Text-match F1.}
75	A predicted entity is a true positive if the predicted text string exactly matches (case-insensitive) a gold entity text \emph{and} the predicted type matches the gold type. This text-match evaluation operates at the entity level rather than the token level. We report Precision, Recall, and F1.
76	
77	\paragraph{RE (FewRel, DocRED): Accuracy.}
78	Each sample has exactly one ground-truth relation. A prediction is correct if the predicted relation label exactly matches the gold label. We report Accuracy. The same metric applies to both sentence-level (FewRel) and document-level (DocRED) RE.
79	
80	\paragraph{ED (MAVEN): Relaxed F1.}
81	A predicted trigger is a true positive if (a)~any token overlap exists between the predicted trigger span and a gold trigger span, \emph{and} (b)~the predicted event type matches the gold event type. This relaxed matching is necessary because event triggers are inherently ambiguous in boundary (e.g., ``was killed'' vs.\ ``killed''). We report Relaxed F1.
82	
83	
84	\subsection{Model and Inference}
85	\label{sec:model}
86	
87	\paragraph{Primary model.}
88	We use Qwen3-32B-FP8 \cite{qwen3-2025}, served via vLLM (v0.20.2) \cite{vllm-2023} on a single 96\,GB GPU. We use two prompt versions: v1 requests character offsets alongside entity text (fabricated in 96.5\% of cases, so we evaluate via text matching; \S\ref{sec:metrics}); v2 drops offset requirements and adds format constraints, doubling precision with minimal recall loss. The v1/v2 distinction applies only to NER and ED; for RE, a single prompt version was used throughout all experiments. Both versions provide a JSON-formatted type schema; the model outputs structured JSON. Switching from v1 to v2 on NER reduces over-prediction (pred/gold ratio from 6.85 to 2.97 at count${}\,=\,1$), shifting the precision--recall tradeoff: count${}\,=\,1$ recall decreases from 0.72 to 0.64 ($-$11\%) while precision doubles (0.11 to 0.22). Both prompt versions produce qualitatively consistent count-degradation curves and BCS effects. We use greedy decoding (temperature${}\,=\,0$) and a fixed seed (42) for reproducibility, and report both prompt versions where applicable to quantify formatting sensitivity \cite{sclar-sensitivity-2024} (full prompt templates in Appendix~\ref{sec:appendix_prompts}).
89	
90	\paragraph{Cross-model validation.}
91	We replicate both paradigms on Meta-Llama-3.1-8B-Instruct \cite{llama3-2024} ($4\times$ smaller, different model family). All key metrics include 95\% bootstrap CIs (1{,}000 resamples, percentile method).
92	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59b7a399-110b-4c50-8e7f-5468eb59e384",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "2adb7038-f81d-410d-93b1-a09899d839af",
  "sourceToolAssistantUUID": "59b7a399-110b-4c50-8e7f-5468eb59e384",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T08:08:20.382Z_

<details open><summary>🔧 Tool call — Read · `toolu_018PErVKHX5ahgRWagcEeJRU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2adb7038-f81d-410d-93b1-a09899d839af",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uVNRwMoXdAYiBGKmJF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6949fe8-2ea4-4050-84a2-1299075e3589",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNdYjcZNkGxuvn3Myd4uoz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3288,
      "cache_read_input_tokens": 49854,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3288,
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

_source line 39 · 2026-05-16T08:08:20.389Z_

<details><summary>↩ Tool result · `toolu_018PErVKHX5ahgRWagcEeJRU`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\ref{fig:main_results}a).
25	
26	\paragraph{NER (Few-NERD).}
27	Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.527 at count${}\,=\,22$ to 0.551 at count${}\,=\,44$; bootstrap 95\% CIs overlap: [0.484, 0.569] vs.\ [0.525, 0.570], indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
28	
29	\paragraph{RE (FewRel).}
30	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a near-halving when the model must discriminate among all 80 relation types simultaneously. (The count${}\,=\,40$ evaluation uses 40-relation subsets sampled from the 80-relation pool, not an independent schema.)
31	
32	\paragraph{Document-level RE (DocRED).}
33	Accuracy declines monotonically from 88.0\% at count${}\,=\,1$ through 52.4\% at count${}\,=\,16$ to 38.7\% at count${}\,=\,96$ (all 96 relation types), a 56\% relative drop. The degradation pattern is consistent with sentence-level FewRel, confirming that count-driven degradation generalizes to document-level RE with longer contexts and cross-sentence reasoning.
34	
35	\paragraph{ED (MAVEN).}
36	In contrast to NER and RE, MAVEN relaxed F1 \emph{increases} from 0.106 at count${}\,=\,1$ to 0.247 at count${}\,=\,44$. This reversal arises from three properties of the MAVEN setup: (i)~trigger-level relaxed matching, which requires only token overlap rather than exact span match; (ii)~MAVEN's 168 event types derive from the FrameNet ontology, forming a same-domain hierarchy where co-presented types provide disambiguating context; and (iii)~extreme class imbalance---rare event types benefit from being presented alongside related types that prime the model toward the correct semantic region. We investigate this reversal further in \S\ref{sec:centrality_confound}.
37	
38	\paragraph{Cross-model replication.}
39	Channel~1 replicates across model families: on Few-NERD, Meta-Llama-3.1-8B-Instruct shows a $-$43\,pp recall decline (0.702 at count${}\,=\,1$ to 0.273 at count${}\,=\,64$), compared to $-$34\,pp for Qwen3-32B (Table~\ref{tab:cross_model} in the Appendix). Per-batch recall correlation between the two models is $r = 0.725$, indicating that schema configuration drives difficulty rather than model-specific factors.
40	
41	\paragraph{Summary.}
42	Schema size degrades extraction quality for NER and both RE datasets (Channel~1: count $\to$ recall/accuracy decline), but this pattern does not hold universally. MAVEN's reversed trend demonstrates that task structure and evaluation protocol mediate the count--performance relationship. DocRED confirms that the count channel generalizes from sentence-level to document-level RE with a larger schema (96 types). Both channels replicate on Llama-3.1-8B: the count channel ($r = 0.725$) and the confusability channel on RE (\S\ref{sec:bcs_controlled}).
43	
44	\subsection{Pairwise Confusability and Type Confusion}
45	\label{sec:pairwise}
46	
47	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
48	
49	\begin{table}[t]
50	\centering
51	\small
52	\resizebox{\columnwidth}{!}{%
53	\begin{tabular}{llrrrrr}
54	\toprule
55	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \textbf{95\% CI} & \textbf{$p$} \\
56	\midrule
57	Few-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & $7{\times}10^{-7}$ \\
58	MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & $7{\times}10^{-42}$ \\
59	\bottomrule
60	\end{tabular}}
61	\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\to}t_j) + C(t_j{\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}1{,}000$).}
62	\label{tab:pairwise}
63	\end{table}
64	
65	The correlations are statistically significant but modest: $r^2 \approx 1.3\text{--}1.7\%$, meaning pairwise confusability explains roughly 1.5\% of the variance in type confusion. Type-level cluster bootstrap, which accounts for the non-independence of pairs sharing a type, yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$); the pair-level CIs in Table~\ref{tab:pairwise} are tighter because they treat pairs as independent. We omit FewRel from the pairwise analysis: RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable to the span-level confusion rates used for NER and ED. The BCS-controlled experiments (\S\ref{sec:bcs_controlled}) provide stronger, quasi-experimental evidence for the confusability effect on RE.
66	
67	Spearman rank correlations corroborate these findings. Across all type pairs, Qwen3 yields $\rho = 0.168$ ($p = 7.3 \times 10^{-14}$) and MiniLM yields $\rho = 0.144$ ($p = 1.7 \times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\rho = 0.272$ for Qwen3 and $\rho = 0.306$ for MiniLM. However, this increase warrants caution: conditioning on nonzero confusion selects for the dependent variable, which can inflate correlations. We report both estimates for transparency; the all-pairs correlations ($r = 0.112\text{--}0.129$) provide the unbiased baseline, while the nonzero-subset values ($\rho = 0.27\text{--}0.31$) characterize the signal among types the model actually confuses.
68	
69	The remaining ${\sim}$98\% of variance in type confusion likely reflects multiple factors: entity and relation frequency in the evaluation corpus, prompt position effects \cite{lost-in-middle-2024}, mention-level ambiguity (e.g., ``Washington'' as person vs.\ location), context complexity, and type definition quality. We frame pairwise SCS as capturing one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design and partitioning---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into accuracy gaps reaching 31.2\,pp under extreme-batch comparison (persisting at $\Delta = -25.5$\,pp under v2 prompts, $r = -0.919$; \S\ref{sec:bcs_controlled}; typical-batch gap ${\approx}\,2\text{--}4$\,pp, \S\ref{sec:practical_magnitude}), demonstrating practical significance for schema optimization.
70	
71	\subsection{BCS-Controlled Experiments}
72	\label{sec:bcs_controlled}
73	
74	To move from correlational to quasi-experimental evidence, we fix the type count and vary BCS. While BCS-controlled batches manipulate aggregate confusability, high-BCS types may differ in other properties (definition granularity, frequency); the within-pool analysis (\S\ref{sec:within_pool}) partially mitigates but does not eliminate these residual confounds. Table~\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes.
75	
76	\begin{table}[t]
77	\centering
78	\small
79	\resizebox{\columnwidth}{!}{%
80	\begin{tabular}{lcrrrr}
81	\toprule
82	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
83	\midrule
84	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
85	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
86	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
87	\bottomrule
88	\end{tabular}}
89	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
90	\label{tab:bcs_controlled}
91	\end{table}
92	
93	At the 16-relation scale, the extreme-batch gap is 9.1\,pp (single batch per level; Table~\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$5.31\,pp (CI: [$-$7.44, $-$3.19]; Table~\ref{tab:within_pool}). At 80 relations, the gap reaches 31.2\,pp (extreme-batch comparison; 95\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\,=\,16$, the extreme-batch gap remains 31.2\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\,=\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\,pp (count 8) and $-$31.8\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.
94	
95	\paragraph{Document-level RE (DocRED).}
96	The confusability effect replicates on DocRED's 96-relation schema. At count${}\,=\,16$, the BCS gap is $-$23.3\,pp (low-BCS 67.9\% vs.\ high-BCS 44.7\%; OLS slope $= -0.713$, 95\% CI: [$-$0.909, $-$0.529]; Spearman $\rho = -0.661$, $p = 1.5 \times 10^{-5}$). At count${}\,=\,32$, the gap narrows to $-$17.6\,pp (low-BCS 57.8\% vs.\ high-BCS 40.3\%; slope $= -0.690$, CI: [$-$0.854, $-$0.519]; $\rho = -0.509$, $p = 0.002$). BCS explains 44--53\% of cross-batch accuracy variance ($R^2 = 0.525$ at count 16, $0.443$ at count 32), substantially higher than FewRel's independent 16-relation pool ($R^2 = 0.218$), likely reflecting DocRED's wider confusability range. Quartile gaps are 18.7\,pp (CI: [7.1, 24.0]) at count 16 and 10.5\,pp (CI: [2.2, 17.4]) at count 32. These results confirm that confusability-driven degradation generalizes to document-level RE with a larger type inventory. Across all evaluated RE settings, BCS slopes range from $-$0.40 (within-pool FewRel subsets) to $-$0.71 (DocRED), with significance in all conditions where BCS range is sufficient.
97	
98	The larger absolute gap at 80 relations (FewRel) does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\S\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.60$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\ 0.48--0.71 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.
99	
100	\paragraph{Within-pool controlled comparison.}
101	\label{sec:within_pool}
102	A potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol (Table~\ref{tab:within_pool}).
103	
104	\begin{table}[t]
105	\centering
106	\small
107	\resizebox{\columnwidth}{!}{%
108	\begin{tabular}{lrrrrrrr}
109	\toprule
110	& \multicolumn{4}{c}{\textbf{Regression (BCS $\to$ Accuracy)}} & \multicolumn{2}{c}{\textbf{Quartile $\Delta$}} \\
111	\cmidrule(lr){2-5} \cmidrule(lr){6-7}
112	\textbf{Setting} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
113	\midrule
114	Independent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}10^{-6}$ & $-$5.31 & [$-$7.44, $-$3.19] \\
115	80-pool $\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 & $-$3.92 & [$-$8.17, $+$0.38] \\
116	Full 80-rel ($n{=}25$)$^\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & 0.762 & $-$1.04 & [$-$10.12, $+$8.04] \\
117	\midrule
118	\multicolumn{7}{l}{\footnotesize Permutation test (16-rel vs.\ 80-pool slopes): $p = 0.598$ (5{,}000 permutations)} \\
119	\multicolumn{7}{l}{\footnotesize $^\dagger$BCS range (IQR\,=\,0.033) insufficient for regression; slope not interpretable.} \\
120	\bottomrule
121	\end{tabular}}
122	\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref{sec:appendix_within_pool} for CI interpretation.}
123	\label{tab:within_pool}
124	\end{table}
125	
126	The within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p = 0.598$), and the smaller absolute quartile gap ($-$3.92\,pp vs.\ $-$5.31\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\ 0.48--0.71; see Appendix~\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (quartile gaps: $-$3.92\,pp vs.\ $-$5.31\,pp; Table~\ref{tab:within_pool}).
127	
128	\paragraph{Practical magnitude.}
129	\label{sec:practical_magnitude}
130	For representative batches drawn from the 80-relation pool ($n{=}100$ random 16-type subsets; Table~\ref{tab:within_pool}), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0]), roughly 7\% of the 31.2\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\%, versus 78.9\% for top-quartile batches, a gap of 3.9\,pp. The 31.2\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\,pp.
131	
132	\paragraph{Cross-model validation.}
133	The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\,pp at count${}\,=\,8$ (low-BCS 78.1\% vs.\ high-BCS 51.0\%) and $-$23.9\,pp at count${}\,=\,16$ (75.5\% vs.\ 51.6\%), reaching 77--87\% of Qwen3-32B's $-$31.2\,pp extreme-batch gap. Strikingly, high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge to $\approx$51\% under high confusability (count${}\,=\,8$: 51.0\% vs.\ 51.0\%; count${}\,=\,16$: 51.6\% vs.\ 51.6\%), while cross-model divergence is confined to the low-BCS regime where model capacity matters. This consistent empirical pattern indicates that confusable type sets create a task-inherent difficulty floor that holds across the tested models.
134	
135	\paragraph{Prompt sensitivity.}
136	The confusability effect persists under alternative prompt designs. Under the v2 prompt---which imposes stricter output format constraints---the extreme-batch BCS gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI: [22.4, 28.6]; $n{=}25$ batches per group; $p < 0.0001$), with a BCS--accuracy correlation of $r = -0.919$. Compared to v1's $-$31.2\,pp gap, v2 shows a modest attenuation ($-$5.7\,pp) while the effect direction, significance, and correlation strength are fully preserved. A preliminary $n{=}5$ evaluation suggested non-significance (CI crossing zero), but this reflected insufficient statistical power and narrow BCS contrast (0.21 vs.\ 0.44 in the $n{=}25$ design) rather than absence of the effect. The pairwise SCS--confusion correlation is embedding-based and thus prompt-invariant; NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\ $r = +0.50$ under v1). Prompt design modulates the baseline around which type confusion operates, but does not eliminate the confusability effect---ruling out prompt-specific confounding as the primary driver of the observed BCS--accuracy relationship (full analysis in Appendix~\ref{sec:appendix_prompt_sensitivity}).
137	
138	\subsection{Multi-Channel Degradation}
139	\label{sec:multi_channel}
140	
141	We decompose extraction errors into an error taxonomy (full data in Table~\ref{tab:error_taxonomy}, Appendix~\ref{sec:appendix_figures}; see also Figure~\ref{fig:error_taxonomy} in Appendix~\ref{sec:appendix_figures}). Intra-batch substitution (IntraSub) scales monotonically with BCS in both tasks: $\rho = 1.0$ ($p < 0.001$, $n=148$ batches) for NER and $\rho = 0.954$ ($p < 10^{-6}$, $n=154$ batches) for RE. Critically, 100\% of type confusion errors in RE are intra-batch---the model exclusively confuses types present in the current prompt. The tasks diverge on missed-entity rates: RE rates remain flat (10--16\%), but NER rates are substantially higher (43--65\%) and non-monotonic, suggesting that confusable type sets impair entity detection itself in span-level extraction. Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches, confirming that BCS captures a functionally relevant dimension of schema difficulty.
142	
143	These results establish two degradation channels: \textbf{Channel~1} (count $\to$ recall decline, \S\ref{sec:count_curves}) and \textbf{Channel~2} (confusability $\to$ type confusion). In RE, the channels are cleanly separable---confusability is associated with elevated substitution errors while detection remains stable. In NER, Channel~2 additionally impairs entity detection, suggesting that for span-level extraction, type ambiguity and boundary ambiguity are coupled.
144	
145	\subsection{Centrality Confound on Homogeneous Schemas}
146	\label{sec:centrality_confound}
147	
148	Per-type analysis on MAVEN reveals an anomalous \emph{positive} BCS--error correlation (Qwen3 $\rho = +0.184$, $p = 0.025$; MiniLM $\rho = +0.208$, $p = 0.011$), opposite to the confusability hypothesis. This traces to same-domain embedding collapse \cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly in representation space, so a type's mean BCS conflates confusability with centrality---high-BCS types are also well-represented types that the model extracts reliably. Few-NERD's cross-domain schema does not exhibit this confound ($\rho = -0.293$, $p = 0.02$, $n = 63$), as its types span multiple embedding clusters. Critically, the pairwise SCS signal remains intact on MAVEN ($r = 0.129$, $p < 10^{-10}$; Table~\ref{tab:pairwise}); the problem lies in per-type aggregation, not the underlying pairwise relationship. A residualized analysis controlling for log frequency and degree centrality confirms the positive correlation vanishes ($p > 0.2$; Appendix~\ref{sec:appendix_residualized_bcs}). Mean BCS is thus a reliable schema difficulty predictor only for cross-domain schemas; same-domain schemas require pairwise SCS or explicit centrality adjustment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6949fe8-2ea4-4050-84a2-1299075e3589",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "d937e9c8-0ece-4593-a8fc-01de7998b566",
  "sourceToolAssistantUUID": "e6949fe8-2ea4-4050-84a2-1299075e3589",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T08:08:20.702Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AuGFuKfhRaKRxQhCg6ozCP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d937e9c8-0ece-4593-a8fc-01de7998b566",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uVNRwMoXdAYiBGKmJF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9234b8ed-be6c-426d-9b61-5ece876bf620",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNdYjcZNkGxuvn3Myd4uoz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3288,
      "cache_read_input_tokens": 49854,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3288
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 49854,
          "cache_creation_input_tokens": 3288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3288,
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

_source line 41 · 2026-05-16T08:08:20.710Z_

<details><summary>↩ Tool result · `toolu_01AuGFuKfhRaKRxQhCg6ozCP`</summary>

```text
1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches, merging predictions via set union. Every decomposition mode---SDGD (F1\,=\,0.241), random batching (0.320), per-type (0.292)---falls below the single-pass baseline (0.445) on Few-NERD NER (Table~\ref{tab:sdgd_results}).
5	
6	\paragraph{Merge amplification as the bottleneck.}
7	The failure mechanism is \emph{merge amplification}: presenting the same text $k$ times with different type subsets causes each pass to independently generate entity predictions. Single-pass precision is 0.563; after union merge with 8 batches, precision drops to 0.210--0.249, while recall increases only modestly (0.368 $\to$ 0.314--0.446). The net effect is a precision collapse that overwhelms any recall gains. Confidence gating---retaining only the highest-confidence prediction per span---improves precision but at the cost of disproportionate recall loss, yielding lower F1 in both modes (Appendix~\ref{sec:appendix_sdgd}). The fundamental issue is that LLM predictions are not calibrated across passes \cite{llm-calibration-survey-2024}, and no merge strategy we tested can compensate.
8	
9	\paragraph{Why NER fails but RE does not.}
10	Merge amplification is specific to span-level tasks where overlapping predictions from multiple passes require reconciliation. In NER, each pass independently proposes entity spans; union merge must resolve conflicting span boundaries and type assignments, and this reconciliation degrades systematically with the number of passes. RE classification, by contrast, operates on fixed (head, tail) pairs with no span reconciliation, assuming an oracle or learned router that assigns each instance to the batch containing its gold type. Each pair receives an independent classification that does not interact with predictions from other passes, eliminating the mechanism that caused SDGD to fail.
11	
12	\paragraph{Confusability-aware batch composition for RE.}
13	We test whether confusability-aware batching improves RE accuracy by applying graph coloring to partition 80 FewRel relations into low-confusability batches. Table~\ref{tab:batch_composition} compares three conditions: confusability-aware assignment via graph coloring, random batching (15 seeds), and the single-pass baseline with all 80 types.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\begin{tabular}{lcc}
19	\toprule
20	\textbf{Condition} & \textbf{Accuracy} & \textbf{Mean BCS} \\
21	\midrule
22	Confusability-aware (graph coloring) & \textbf{0.802} & 0.552 \\
23	Random batching (15 seeds) & 0.788 $\pm$ 0.018 & 0.559 \\
24	Single-pass (80 types) & 0.504 & 0.557 \\
25	\bottomrule
26	\end{tabular}
27	\caption{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\,pp over random assignment, though the difference is not statistically significant given the single graph-coloring configuration ($n{=}1$) and narrow BCS margin (0.006). Single-pass with all 80 types suffers severe schema overload.}
28	\label{tab:batch_composition}
29	\end{table}
30	
31	The confusability-aware strategy achieves 0.802 accuracy compared to random batching (0.788 $\pm$ 0.018). Although the +1.4\,pp gain is directionally consistent with the confusability hypothesis, it does not reach statistical significance (rank 13/15 among random seeds, one-sided $p \approx 0.19$); the narrow BCS margin between conditions (0.006) limits the achievable separation at this partition granularity. This suggests that confusability-aware grouping warrants further investigation at finer partition granularity.
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9234b8ed-be6c-426d-9b61-5ece876bf620",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "7775f9a7-2c60-4818-890f-4838fe4cfb51",
  "sourceToolAssistantUUID": "9234b8ed-be6c-426d-9b61-5ece876bf620",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-16T08:08:24.500Z_

Now I have a thorough understanding of the paper. Let me also check the latest dream report for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7775f9a7-2c60-4818-890f-4838fe4cfb51",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uVexcGxwQR48ccaTUH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfe9fab6-0c68-48ce-875b-5a0f6ead1f34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017enQNb4GfSxeJPsSX4P7vP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11516,
      "cache_read_input_tokens": 53142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11516,
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

_source line 43 · 2026-05-16T08:08:26.541Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RpXcic3ECL7RhxMEqeyhr2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfe9fab6-0c68-48ce-875b-5a0f6ead1f34",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uVexcGxwQR48ccaTUH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52691d03-82b2-4e5b-be2f-4aeaab0c8813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017enQNb4GfSxeJPsSX4P7vP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11516,
      "cache_read_input_tokens": 53142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11516,
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

_source line 44 · 2026-05-16T08:08:26.547Z_

<details><summary>↩ Tool result · `toolu_01RpXcic3ECL7RhxMEqeyhr2`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{amsmath}
5	\usepackage{amssymb}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{hyperref}
11	\usepackage{enumitem}
12	
13	\title{Multi-Channel Schema Degradation in Training-Free LLM Information Extraction:\\Type Count and Confusability as Orthogonal Failure Modes}
14	
15	\author{Anonymous}
16	
17	\begin{document}
18	\maketitle
19	
20	\begin{abstract}
21	Training-free LLM-based information extraction degrades severely on complex schemas, but the mechanisms underlying this degradation remain poorly understood.
22	We conduct a controlled empirical study across three IE tasks---NER (Few-NERD, 66 types), RE (FewRel, 80 relations; DocRED, 96 relations), and ED (MAVEN, 168 event types)---isolating type count from type confusability as independent predictors of extraction quality.
23	We find that pairwise type confusability (measured via schema cosine similarity, SCS) independently predicts extraction degradation across all tasks ($r{=}0.11$--$0.13$, all CIs exclude zero), with 10--28$\times$ more type confusion errors in high-confusability batches.
24	The confusability effect amplifies with schema complexity: 3.4$\times$ stronger on 80-type vs.\ 16-type schemas ($\Delta{=}{-}31.2$pp vs.\ ${-}9.1$pp).
25	Error taxonomy analysis reveals orthogonal degradation channels: type count drives recall decline via attention dilution, while confusability drives type confusion via semantic interference (IntraSub $\rho{\geq}0.95$ across NER and RE).
26	We further show that naive confusability-aware schema decomposition (SDGD) fails due to merge amplification---a structural challenge where decompose-then-merge introduces more errors than it resolves---pointing to calibration-based approaches as a principled alternative.
27	\end{abstract}
28	
29	\section{Introduction}
30	
31	Large language models (LLMs) have emerged as powerful tools for training-free information extraction (IE), enabling zero-shot and few-shot extraction across diverse schemas without task-specific training \cite{wei2023zeroshot}.
32	However, performance degrades substantially as schema complexity increases: a 20--60 F1 gap between training-free LLM IE and supervised methods is commonly observed on complex schemas.
33	
34	Prior work has addressed this degradation through schema decomposition strategies.
35	UniNER \cite{zhou2024universalner} splits extraction into per-type passes, gaining 3.3 F1 but losing cross-type context.
36	LLM-PEE uses type similarity as an implicit confusability proxy but never validates this assumption empirically.
37	Critically, no prior work isolates \emph{what} makes schemas complex for LLMs: is it the sheer number of types, the semantic similarity between types, or their interaction?
38	
39	We conduct the first controlled empirical study that disentangles type count from type confusability in training-free LLM IE across three tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).
40	Our experimental design varies count and confusability independently, enabling causal identification of their separate effects.
41	
42	Our contributions are:
43	\begin{enumerate}
44	\item \textbf{Confusability Independence.} We demonstrate that pairwise type confusability independently predicts extraction degradation beyond type count ($r{=}0.11$--$0.13$, all bootstrap CIs exclude zero), validated across NER, RE, and ED. The effect amplifies 3.4$\times$ with schema complexity and is robust across two embedding families (Qwen3-32B, MiniLM-L6-v2).
45	
46	\item \textbf{Multi-Channel Degradation Model.} We identify two orthogonal degradation channels: count$\to$recall decline (attention dilution) and confusability$\to$type confusion (semantic interference), with cross-task IntraSub correlation $\rho{\geq}0.95$.
47	
48	\item \textbf{Decomposition Negative Result.} We show that naive confusability-aware decomposition (SDGD) fails due to merge amplification (${\sim}35\%$ structural cost across two datasets), establishing that the value of confusability lies in diagnosis, not decomposition.
49	
50	\item \textbf{Methodological Contribution.} We identify a centrality confound in per-type aggregation of confusability on semantically homogeneous schemas, and demonstrate that pairwise analysis avoids this confound.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52691d03-82b2-4e5b-be2f-4aeaab0c8813",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "6b0cce0a-eeb9-4307-9d92-74e6bb865c9d",
  "sourceToolAssistantUUID": "52691d03-82b2-4e5b-be2f-4aeaab0c8813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-16T08:08:29.646Z_

Now let me load the submit tool to deliver the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b0cce0a-eeb9-4307-9d92-74e6bb865c9d",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uW6gBJXkFdjhxCKKFd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "771064db-7f52-4e1a-9fcd-ac7b8b62d41b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFDBNio2w2fPoqG227bNay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1505,
      "cache_read_input_tokens": 64658,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1505,
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

_source line 46 · 2026-05-16T08:08:30.401Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01347ETfJazEQo7nYuWjnjit`</summary>

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
  "parentUuid": "771064db-7f52-4e1a-9fcd-ac7b8b62d41b",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uW6gBJXkFdjhxCKKFd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3d9b2ea-5ef3-4e9f-bbe8-ad1dc2b9e1c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFDBNio2w2fPoqG227bNay",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1505,
      "cache_read_input_tokens": 64658,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1505
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 64658,
          "cache_creation_input_tokens": 1505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1505,
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

_source line 47 · 2026-05-16T08:08:30.404Z_

<details><summary>↩ Tool result · `toolu_01347ETfJazEQo7nYuWjnjit`</summary>

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
  "parentUuid": "e3d9b2ea-5ef3-4e9f-bbe8-ad1dc2b9e1c4",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "a2d75a1acd67982ee",
  "type": "user",
  "uuid": "e09f6895-5822-42b9-af42-af04e4d8e930",
  "sourceToolAssistantUUID": "e3d9b2ea-5ef3-4e9f-bbe8-ad1dc2b9e1c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-16T08:09:37.449Z_



I now have a thorough understanding of the paper. Let me synthesize my review.

## R2: Novelty and Related Work

### Summary
The paper conducts a controlled empirical study disentangling type count from type confusability as independent predictors of extraction quality degradation in training-free LLM IE across NER, RE, and ED. The core novelty claim is that no prior work has isolated these two factors in a controlled experimental design. The actual paper (as opposed to the dream report summary provided in the prompt) is substantially more nuanced and honest than the dream version -- it cites ~30+ references, not 4, and carefully qualifies effect sizes. However, the novelty is incremental: the observation that semantically similar labels cause confusion is well-established in classification literature, and the paper's main contribution is formalizing and measuring this in the specific context of training-free LLM IE with controlled experiments.

### Strengths
- S1: **Genuine gap in controlled empirical analysis.** The paper correctly identifies that prior decomposition work (LLM-PEE, UniNER, PARSE) conflates count and confusability. The BCS-controlled experimental design that fixes count while varying confusability is methodologically sound and, to the best of my knowledge, novel for training-free LLM IE. This is a real contribution to experimental methodology in this subfield.
- S2: **Honest treatment of effect sizes and negative results.** The paper does not overclaim. Pairwise r^2 of 1.3-1.7% is reported transparently with appropriate caveats. The SDGD negative result (merge amplification) is genuinely informative and well-analyzed. The +1.4pp RE batching gain is correctly described as directionally consistent but not significant. This level of intellectual honesty is commendable and rare.
- S3: **Cross-task and cross-model validation.** Testing across NER, RE (sentence and document level), and ED with two model families (Qwen3-32B and Llama-3.1-8B) and two embedding models (Qwen3, MiniLM) provides reasonable breadth. The consistent high-BCS accuracy floor (~51%) across models is an interesting empirical finding.
- S4: **Centrality confound identification.** The discovery that per-type BCS aggregation is confounded by centrality on same-domain schemas (MAVEN), with the residualized analysis confirming the confound, is a genuine methodological contribution that future work on schema difficulty metrics should heed.
- S5: **Related work section is comprehensive.** Contrary to the prompt's claim of "only 4 citations," the actual paper cites 30+ references covering training-free IE, schema decomposition, multi-agent approaches, embedding anisotropy, and more. The positioning against LLM-PEE is particularly well done.

### Weaknesses
- W1: **Limited conceptual novelty beyond measurement.** The idea that semantically similar labels cause classification confusion is not new -- it is a basic observation in any multi-class classification setting. The paper's contribution is measuring this in training-free LLM IE with controlled experiments, but the conceptual insight ("similar labels confuse classifiers") does not advance theoretical understanding. The "two-channel" framing (count -> recall, confusability -> type confusion) is descriptive rather than mechanistic -- "attention dilution" and "semantic interference" are post-hoc labels, not validated mechanisms. The paper acknowledges this in limitations (item 10: "correlational evidence... mechanistic analysis at the attention or logit level is needed") but the framing throughout the paper implies more mechanistic understanding than is warranted.
- W2: **The pairwise effect size is very small (r^2 = 1.3-1.7%).** While the paper is honest about this, 98.5% of variance is unexplained. The practical utility of SCS as a "predictor" is questionable when it explains so little. The batch-level BCS effects are larger (31.2pp extreme gap), but these rely on extreme-batch comparisons that are unlikely to arise in practice -- the paper's own analysis shows typical-batch gaps of only 2-4pp. The disconnect between "statistically significant pairwise signal" and "practically meaningful batch effect" is not fully resolved.
- W3: **Missing related work on label confusion in NLP.** The paper does not engage with the substantial literature on label confusion in NLP and ML more broadly: (a) confusion matrix analysis and hierarchical label structures in NER (e.g., Ringland et al. 2019 on fine-grained NER label hierarchies); (b) label smoothing and soft labeling approaches that explicitly model inter-label similarity; (c) curriculum learning and hard example mining based on label confusion; (d) the cognitive science of categorization (prototype theory, exemplar models) which directly addresses why similar categories are harder to discriminate; (e) the extensive literature on few-shot and zero-shot classification where label semantics drive performance (e.g., Yin et al. 2019 on entailment-based zero-shot classification). The paper positions itself as if "confusability as a predictor" is entirely novel, but the insight that label similarity predicts confusion has deep roots.
- W4: **Missing related work on structured prediction with LLMs.** The paper does not cite or discuss: (a) GPT-NER (Wei et al. 2023) which is referenced in the dream report summary but absent from the actual paper; (b) work on constrained decoding for structured outputs (e.g., guidance, outlines) which directly addresses the merge problem; (c) retrieval-augmented IE approaches that dynamically select relevant schema subsets (which is essentially what BCS-controlled batching does); (d) the broader literature on prompt engineering for classification tasks with many labels.
- W5: **"First controlled empirical study" claim is overstated.** IEPile (2024) explicitly constructs "hard negative schemas" -- semantically proximate types designed to train type discrimination. While IEPile targets training rather than inference, it demonstrates awareness that confusable schemas degrade performance and uses controlled schema manipulation. Familiarity (NAACL 2025) quantifies label similarity for evaluation bias -- another controlled analysis of label semantics affecting NER. CROSSAGENTIE's cross-type debate explicitly addresses type confusion. The paper's contribution is better described as "the first controlled study isolating count from confusability at inference time in zero-shot LLM IE" -- a narrower but more accurate claim.
- W6: **The SDGD negative result, while honest, leaves the paper without a strong actionable contribution.** The +1.4pp RE batching gain is not significant (p~0.19). The paper is essentially a diagnostic study that says "confusability matters but we cannot fix it." For a top venue, this raises the "so what?" question. The future directions (calibration-aware merge, joint decoding, hierarchical extraction) are speculative.
- W7: **MAVEN results undermine rather than support the main narrative.** The count curve on MAVEN goes in the opposite direction (F1 increases with count). The per-type BCS correlation is positive (opposite to hypothesis). These are explained away via centrality confounds and same-domain effects, but it means the paper's core claims hold on only a subset of tested conditions. The "centrality confound" explanation, while plausible, has not been validated on other same-domain datasets.

### Questions for Authors
- Q1: How does the BCS--accuracy relationship compare to simpler baselines, such as the average string edit distance between type labels, or the number of shared words in type names? If these simpler features predict confusion equally well, the embedding-based SCS metric adds little.
- Q2: The "attention dilution" mechanism for Channel 1 is never empirically validated (acknowledged in limitations). Have you examined attention patterns or logit distributions to confirm this is the mechanism, rather than, e.g., instruction following degradation with longer prompts?
- Q3: IEPile constructs hard negative schemas during training -- have you compared your SCS metric to their schema construction strategy? Their approach effectively operationalizes confusability for training; how does it differ from yours at the metric level?
- Q4: The paper tests only zero-shot prompting. Many practical training-free IE systems use few-shot examples. Does confusability interact with the number of in-context examples? A few demonstrations per type might disambiguate confusable types, potentially eliminating Channel 2 entirely.
- Q5: For the RE batch composition experiment, you test a single graph coloring configuration. Have you tried multiple coloring algorithms or threshold values? The 0.006 BCS margin between confusability-aware and random batching suggests the graph coloring is not finding much room for improvement -- why?
- Q6: The cross-model validation uses Llama-3.1-8B, which is 4x smaller than Qwen3-32B. This conflates model family with model scale. Have you considered testing Qwen3-8B or Llama-3.1-70B to separate these factors?

### Missing Related Work
- Label confusion and hierarchical label structures in NER (Ringland et al. 2019; Ling & Weld 2012 on fine-grained entity typing)
- Entailment-based zero-shot text classification (Yin et al. 2019) where label semantics directly drive classification
- Label smoothing (Szegedy et al. 2016; Muller et al. 2019) as an explicit model of inter-class similarity
- GPT-NER (Wei et al. 2023) and other prompt-based NER approaches
- Prototype networks and metric learning for few-shot classification, where inter-class distance is the core modeling assumption
- Curriculum learning / hard example mining based on confusion patterns
- Schema-guided dialogue state tracking (Rastogi et al. 2020, SGD benchmark) where schema complexity similarly degrades zero-shot performance
- Dynamic schema selection / retrieval-augmented approaches for IE
- The cognitive science literature on categorization difficulty (Rosch 1978; Nosofsky 1986) which provides theoretical grounding for why similar categories are harder to discriminate

### Preliminary Score: 4/6
### Confidence: 4/5

**Justification:** The paper addresses a real gap in controlled empirical analysis of schema complexity in LLM IE. The experimental design is sound, the honesty about effect sizes and negative results is commendable, and the centrality confound finding is a genuine methodological contribution. However, the conceptual novelty is limited (similar labels cause confusion is well-known), the pairwise effect sizes are very small, the paper lacks actionable methods (SDGD fails, RE batching is not significant), and there are notable gaps in related work coverage regarding label confusion in NLP more broadly. The work is best characterized as a careful empirical analysis paper rather than a methods paper, and at a Weak Accept level it provides useful measurements and methodology that the community can build on, even though it does not deliver a breakthrough insight or practical tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e09f6895-5822-42b9-af42-af04e4d8e930",
  "isSidechain": true,
  "agentId": "a2d75a1acd67982ee",
  "requestId": "req_011Cb5uWNBauwGpNedKaTWZS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "924e4fdb-a55c-43ff-8819-9ebf8f2bfd8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017aQndK2M9Nek1D8oZULB72",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 66163,
      "output_tokens": 2556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 680
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2556,
          "cache_read_input_tokens": 66163,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 680,
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
