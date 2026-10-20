# Research conversation: You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ac64c321a19c91108.jsonl`
- **Structured JSON:** [`76891260600e65963012.json`](../../sessions/76/76891260600e65963012.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

64 recorded events

### User

_source line 1 · 2026-05-16T08:07:33.631Z_

You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus is **Methods and Experiments**.

## Paper Summary
Title: "Multi-Channel Schema Degradation in Training-Free LLM Information Extraction: Type Count and Confusability as Orthogonal Failure Modes"

The paper conducts controlled empirical study across 3 IE tasks (NER, RE, ED) isolating type count from type confusability as independent predictors of extraction quality in training-free LLM IE. Key claims:
1. **Confusability Independence**: Pairwise SCS independently predicts degradation (r=0.11-0.13, CIs exclude zero), validated across tasks, amplifies 3.4× with schema complexity
2. **Multi-Channel Degradation**: Two orthogonal channels—count→recall decline (attention dilution) vs confusability→type confusion (semantic interference), IntraSub ρ≥0.95 cross-task
3. **SDGD Negative Result**: Naive decomposition fails due to merge amplification (~35% structural cost)
4. **Methodological Contribution**: Centrality confound in per-type aggregation on homogeneous schemas

## Key Experimental Results (from paper)
- **SCS Validation (Table 1)**: Qwen3-32B ρ=0.168 (all pairs), 0.272 (nonzero); MiniLM ρ=0.144/0.306. All p<1e-5.
- **DocRED Count Curve (Table 2)**: Accuracy 0.875→0.392 over count 1→96 (48.3pp drop)
- **DocRED BCS-Controlled (Table 3)**: At count=16, high BCS 23.3pp worse (ρ=-0.661, slope CI [-0.909,-0.529])
- **2×2 Factorial (Table 4)**: Interaction not significant (z=-0.667, p=0.505), supporting additive/orthogonal channels
- **Error Taxonomy (Table 5)**: IntraSub: 0%→1.6%→10.6%→49.4% across BCS bins (ρ=1.0). Hallucination <3%.
- **Cross-task (Table 6)**: NER ρ=1.0, RE ρ=0.954
- **SDGD Few-NERD (Table 7)**: Single-pass 0.445, Random 0.301, SDGD-zero 0.241, SDGD-cal 0.285
- **SDGD MAVEN (Table 8)**: Single-pass 0.247, Random 0.178, SDGD-zero 0.142, SDGD-cal 0.168
- **Random vs SDGD (Table 10)**: SDGD reduces confusion (0.018 vs 0.034) but higher merge dup (2.4× vs 1.8×)
- **Per-type (Table 11)**: F1=0.292, Recall=0.586 (+59%), Precision=0.194 (-66%), 32× latency

## Imagined Experiment Coverage (from review context)
The review context lists these planned experiments: exp-005 (DocRED), exp-006 (2×2 Interaction), exp-007 (Error Taxonomy), exp-009 (SDGD-zero MAVEN), exp-010 (SDGD-cal Few-NERD), exp-011 (SDGD-cal MAVEN), exp-013 (Random Batching), exp-014 (Per-type), exp-015 (SCS Validation).

All 9 planned experiments appear to be covered in the paper.

## Your Review Tasks
Evaluate the following and provide a structured review:

1. **Experimental Design Soundness**: Are the controlled experiments (count curves, BCS-controlled comparisons, 2×2 factorial) properly designed? Are there confounds?
2. **Statistical Rigor**: Are the statistical tests appropriate? Is the evidence sufficient for the claims? How about effect sizes (r=0.11-0.13)?
3. **Metric & Evaluation Choices**: Is SCS a well-motivated proxy? Are the evaluation metrics (accuracy, F1, relaxed F1) appropriate for each task?
4. **Ablation Completeness**: Are the ablations (random batching, per-type splitting, SDGD-zero vs cal) sufficient to support conclusions?
5. **Reproducibility**: Enough detail to replicate? Missing details?
6. **SDGD Evaluation Fairness**: Is the SDGD comparison fair? Could better merge strategies change conclusions?
7. **Weaknesses in Methods/Experiments**: Any fatal flaws or major gaps?

## Output Format
```
## R1: Methods and Experiments

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

### Missing Experiments / Suggestions
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
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "3481c673-0cb2-46cc-962d-0196c4889145",
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

_source line 2 · 2026-05-16T08:07:33.637Z_

```json
{
  "parentUuid": "3481c673-0cb2-46cc-962d-0196c4889145",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
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
  "uuid": "ed7f27db-533a-41cf-b94e-05d56522016e",
  "timestamp": "2026-05-16T08:07:33.637Z",
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

_source line 3 · 2026-05-16T08:07:36.499Z_



I'll start by reading the paper and all related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed7f27db-533a-41cf-b94e-05d56522016e",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uSBX2XDBvRUHvXWbp3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "092e8325-bd55-432a-813a-af8b4e6d86a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjrTNzEHNekAcvBsJpjs5U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15377,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15377,
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

_source line 4 · 2026-05-16T08:07:37.025Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FVhWXqPBH9mw7WJiq7fTHn`</summary>

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
  "parentUuid": "092e8325-bd55-432a-813a-af8b4e6d86a9",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uSBX2XDBvRUHvXWbp3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a38c89d9-9188-48f8-b793-04a9a82a7799",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AjrTNzEHNekAcvBsJpjs5U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15377,
      "cache_read_input_tokens": 0,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15377
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 125,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15377,
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

_source line 5 · 2026-05-16T08:07:37.031Z_

<details><summary>↩ Tool result · `toolu_01FVhWXqPBH9mw7WJiq7fTHn`</summary>

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
  "parentUuid": "a38c89d9-9188-48f8-b793-04a9a82a7799",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "958de3fa-3816-4653-9288-798961a7bc2e",
  "sourceToolAssistantUUID": "a38c89d9-9188-48f8-b793-04a9a82a7799",
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

_source line 6 · 2026-05-16T08:07:39.822Z_



Let me read the paper and all relevant project files to conduct a thorough methods and experiments review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "958de3fa-3816-4653-9288-798961a7bc2e",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uSS29xi16jU5EGKoZ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61bdd243-b364-4fa6-b30a-b3ff25938112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTzDjyMPzZiGqzx9Y1q2c9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 7 · 2026-05-16T08:07:40.356Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01MHt8fkwkvwfvMPRQ7JhAFu`</summary>

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
  "parentUuid": "61bdd243-b364-4fa6-b30a-b3ff25938112",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uSS29xi16jU5EGKoZ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11480728-0695-4ad8-9dd7-b31268915d06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTzDjyMPzZiGqzx9Y1q2c9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 8 · 2026-05-16T08:07:40.526Z_

<details><summary>↩ Tool result · `toolu_01MHt8fkwkvwfvMPRQ7JhAFu`</summary>

```text
{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (42 个)\n\n- **bootstrap_ci_analysis**: DONE (success) — \n- **exp016_fewrel_error_taxonomy**: DONE (success) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp007_error_taxonomy**: DONE (success) — \n- **exp_fewrel_formal_80rel**: DONE (success) — \n- **exp_fewrel_formal**: DONE (success) — \n- **exp008_sdgd_zero_fewnerd_r2**: DONE (negative) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n- **fewrel_pilot**: DONE (success) — \n- **exp004_maven_bcs**: DONE (negative) — \n- **exp002_confusability_controlled**: DONE (success) — \n- **exp003a_prompt_v2_rerun**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp001_count_baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- exp_fewrel_v2_n25（准备中）\n- bcs_max_to_mean_fix（准备中）\n\n## 近期结论\n- **exp_confusability_batch_composition** (success): Confusability-aware batch composition (graph coloring on SCS matrix to separate high-SCS pairs) improves per-type accuracy and reduces substitution errors compared to random batching and single-pass full schema, providing a practical application of the confusability findings.\n- **exp_fewrel_16rel_bootstrap** (success): FewRel 16-type pool, 100 random 8-type batches, bootstrap CI for BCS effect (Δ_BCS). 填 tab:bcs_controlled 16-rel 行的 CI，并与 80-rel 计算 amplification ratio 正式 CI。D033 已批准。 ← 基于 exp_fewrel_formal\n- **exp_docred_confusability** (success): Schema-induced degradation (count + confusability channels) generalizes to document-level RE (DocRED, 96 relation types), strengthening cross-dataset evidence for Claims 1 and 2. ← 基于 exp_fewrel_formal_80rel\n  [DocRED SCS Matrix (96 relations)](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/scs_matrix_info.txt) | [DocRED Confusability Pilot Results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/pilot_results.txt) | [phase2_count_curve_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/count_curve_results.json) | [phase2_bcs_controlled_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bcs_controlled_results.json) | [phase2_bootstrap_analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bootstrap_analysis.json)\n\n## 趋势\n成功 20 / 负向 5 / 失败 10 / 共 38\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\ncqa1-38874: 无 GPU 信息\n\n## 告警\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\n- exp012_llama_8b: 已被终止 — unknown\n- exp_fewrel_40rel: 训练失败 — unknown\n- exp012_llama_awq: 已被终止 — unknown\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\n- exp_fewrel_40rel_r2: 训练失败 — unknown\n- exp_fewrel_40rel_r3: 训练失败 — unknown\n- exp012_llama_8b_r3: 训练失败 — unknown\n- exp_fewrel_16rel_100batch: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11480728-0695-4ad8-9dd7-b31268915d06",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "b9f3b083-97ef-44ad-9bea-ae78a4e7fc3a",
  "sourceToolAssistantUUID": "11480728-0695-4ad8-9dd7-b31268915d06",
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

_source line 9 · 2026-05-16T08:07:40.891Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MWA1xnbPayyXatcW8xocYr`</summary>

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
  "parentUuid": "b9f3b083-97ef-44ad-9bea-ae78a4e7fc3a",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uSS29xi16jU5EGKoZ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bb63d85-097e-4434-9689-e9abec041c27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTzDjyMPzZiGqzx9Y1q2c9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 10 · 2026-05-16T08:07:40.904Z_

<details><summary>↩ Tool result · `toolu_01MWA1xnbPayyXatcW8xocYr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp017_gpt4o_mini_fewrel（准备中）\\n- exp_cross_embedding_sensitivity（准备中）\\n- exp_fewrel_v2_n25（准备中）\\n- bcs_max_to_mean_fix（准备中）\\n\\n## 近期结论\\n- **exp_confusability_batch_composition** (success): Confusability-aware batch composition (graph coloring on SCS matrix to separate high-SCS pairs) improves per-type accuracy and reduces substitution errors compared to random batching and single-pass full schema, providing a practical application of the confusability findings.\\n- **exp_fewrel_16rel_bootstrap** (success): FewRel 16-type pool, 100 random 8-type batches, bootstrap CI for BCS effect (Δ_BCS). 填 tab:bcs_controlled 16-rel 行的 CI，并与 80-rel 计算 amplification ratio 正式 CI。D033 已批准。 ← 基于 exp_fewrel_formal\\n- **exp_docred_confusability** (success): Schema-induced degradation (count + confusability channels) generalizes to document-level RE (DocRED, 96 relation types), strengthening cross-dataset evidence for Claims 1 and 2. ← 基于 exp_fewrel_formal_80rel\\n  [DocRED SCS Matrix (96 relations)](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/scs_matrix_info.txt) | [DocRED Confusability Pilot Results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/pilot_results.txt) | [phase2_count_curve_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/count_curve_results.json) | [phase2_bcs_controlled_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bcs_controlled_results.json) | [phase2_bootstrap_analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bootstrap_analysis.json)\\n\\n## 趋势\\n成功 20 / 负向 5 / 失败 10 / 共 38\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-38874: 无 GPU 信息\\n\\n## 告警\\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\\n- exp012_llama_fewnerd: 训练失败 — unknown\\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\\n- exp012_llama_8b: 已被终止 — unknown\\n- exp_fewrel_40rel: 训练失败 — unknown\\n- exp012_llama_awq: 已被终止 — unknown\\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\\n- exp_fewrel_40rel_r2: 训练失败 — unknown\\n- exp_fewrel_40rel_r3: 训练失败 — unknown\\n- exp012_llama_8b_r3: 训练失败 — unknown\\n- exp_fewrel_16rel_100batch: 已被终止 — unknown\\n\", \"total_chars\": 2396, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bb63d85-097e-4434-9689-e9abec041c27",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "24f26d4b-7250-4704-9785-94256f9d69d5",
  "sourceToolAssistantUUID": "3bb63d85-097e-4434-9689-e9abec041c27",
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

_source line 11 · 2026-05-16T08:07:41.423Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01F3VMx2gFF4yNgNWeTvxsxn`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24f26d4b-7250-4704-9785-94256f9d69d5",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uSS29xi16jU5EGKoZ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e497fdd0-8df1-4683-96c6-d8042cee1236",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTzDjyMPzZiGqzx9Y1q2c9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 12 · 2026-05-16T08:07:41.436Z_

<details><summary>↩ Tool result · `toolu_01F3VMx2gFF4yNgNWeTvxsxn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ROADMAP.md\", \"content\": \"# schema-dag-extraction — Research Dashboard\\n\\n> 最后更新: 2026-05-16 06:08 UTC | 更新原因: 服务器重启恢复，更新 v2 n=25/DocRED/cross-embedding 完成状态，派 exp-018+exp-017\\n\\n## 核心方向\\n验证 type confusability 独立于 type count 驱动 training-free LLM IE 质量下降，发现 multi-channel degradation model（count→recall, confusability→type confusion）。v2 n=25 证明效应是 task-inherent property 而非 prompt artifact（D040）。详见 paper_framing.md。\\n\\n## 当前阶段\\n**Scope 扩展冲刺** — ARR May 25 提交（距今 9 天）。三条并行线推进。\\n\\n- Claim 1（count scaling）：四任务 + 双模型验证完成 ✓（DocRED 新增）\\n- Claim 2（BCS confusability）：四任务 + 双模型验证完成 ✓（DocRED 新增）\\n- Claim 3（SDGD）：正式放弃 (D019)，negative result + future work\\n- D040：v2 RE n=25 推翻 attenuation 叙述 → confusability is task-inherent ✓\\n- D038/D039：BCS 定义统一（MAX→MEAN）✓\\n- Cross-embedding sensitivity：MiniLM vs Qwen3 方向一致 ✓\\n- Reviewer 审查 D040 叙事重写 + claim 边界评估中\\n\\n## 表述硬约束（C001，全角色遵守）\\n- **C001**: count_40 子集来自 80-type pool 采样，论文必须写 \\\"40-rel subsets sampled from the 80-relation pool\\\"\\n\\n## Scope 扩展计划\\n\\n**Track A — GPU**\\n- [x] DocRED Phase 2 count curve + BCS-controlled ✓（slope −0.71, r=−0.66, p=1.5e-5）\\n- [x] Cross-embedding sensitivity ✓（方向一致，MiniLM 更适合 BCS）\\n- [x] v2 RE n=25 验证 ✓（Δ=25.5pp, r=−0.919, p<0.0001）\\n- [ ] **exp-018: Confusability-aware batch composition** — 已派 Agent 立即上 GPU\\n\\n**Track B — API**\\n- [x] OpenAI key 已存储 ✓\\n- [ ] **exp-017: GPT-4o-mini FewRel replication** — 已派 Agent 启动，API-bound 不占 GPU\\n\\n**Track C — CPU/写作**\\n- [x] D038 BCS 定义统一 ✓\\n- [x] DocRED 论文集成 ✓\\n- [ ] 3 个 Reviewer warning 修复中（docred-2019 编译、registry 过时值、Qwen3 r 值不一致）\\n- [ ] D040 叙事更新确认（§4.3/Intro/AppG）\\n- [ ] Review round（Reviewer 审查 D040 + claim 边界中）\\n- [ ] Final submission\\n\\n## 核心证据进展\\n\\n**已完成（Claim 1+2）**:\\n- exp-001: count curve (recall 0.72→0.42, WrongType 0→2434) ✓\\n- exp-002: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x ✓\\n- exp-003a: prompt v2 降低 over-prediction ✓\\n- exp-004: MAVEN 168 types, MiniLM pairwise r=0.120 ✓\\n- exp_fewrel_formal_80rel: BCS Δ=-31.2pp, slope=-0.401 ✓\\n- exp_fewrel_40rel_r4: count_40=0.588, BCS Δ=-33.3pp/-31.8pp ✓\\n- exp007/exp016 error taxonomy: IntraSub ρ=1.0/0.954 ✓\\n- bootstrap_ci_analysis: 统一 fixed-boundary B=10000 ✓\\n- exp015_scs_validation: 两种 embedding 均显著 ✓\\n- exp012_llama_fewrel_ch2: BCS Δ=-27.1pp/-23.9pp, high-BCS floor 0.51 ✓\\n- D038: BCS MAX→MEAN (slope -0.509, |r|=0.467, quartile Δ=-5.3pp) ✓\\n- **exp_docred_confusability**: BCS slope −0.71（最陡）, r=−0.66, p=1.5e-5, 96 types ✓\\n- **exp_v2_re_n25**: Δ=25.5pp, CI [22.4, 28.6], r=−0.919 — task-inherent ✓\\n- **cross_embedding_sensitivity**: MiniLM/Qwen3 方向一致，MiniLM effect size 更大 ✓\\n\\n**负向结论**:\\n- exp-008 SDGD: F1=0.241 < baseline 0.445 (D014, D019)\\n- exp004_maven_bcs: per-type BCS 正向（centrality confound）\\n- exp006_interaction_2x2: p=0.505 (D026)\\n- exp012_llama_8b_r2_exp2: NER Channel 2 未复现（floor effect）\\n\\n## 近期任务\\n- [ ] exp-018 batch composition 上 GPU（Agent 执行中）\\n- [ ] exp-017 GPT-4o-mini 启动（Agent 执行中）\\n- [ ] 3 个 Reviewer warning 修复\\n- [ ] Reviewer 审查 D040 叙事 + claim 边界评估\\n- [ ] 论文最终集成 + Review round\\n- [ ] 最终提交 ARR May 25\\n\\n## GPU 预算\\n- 服务器: cqa1-38874, 1× RTX PRO 6000 Blackwell (98GB), cuda:0\\n- 当前: 空闲 → exp-018 即将占用\\n\\n## 目标会议\\nEMNLP 2026, ARR May 25 提交（距今 9 天）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D043 | 2026-05-16 | D042 修正：exp-018 confusability-aware 与 random 无显著差异 | exp_confusability_batch_composition |\\n| D042 | 2026-05-16 | exp-018 成功：confusability-aware batching 在 RE 上 +1. | exp_confusability_batch_composition |\\n| D041 | 2026-05-16 | 放弃 exp-017 GPT-4o-mini：TUM proxy 未部署，AutoDL 无法访问 O | exp017_gpt4o_mini_fewrel |\\n| D040 | 2026-05-16 | v2 RE n=25 结果推翻 attenuation 叙述，升级为 \\\"confusability  | exp_v2_re_n25 |\\n| D039 | 2026-05-16 | D039: BCS 统一选择 Path A (MEAN)——科学诚实优先，MAX 作 sensiti | exp_fewrel_16rel_bootstrap, exp_fewrel_formal_80rel, exp_fewrel_80pool_16sub_bootstrap |\\n| D038 | 2026-05-16 | D038: BCS 定义不一致修复——统一为 MEAN pairwise SCS，重算 Table  | exp_fewrel_16rel_bootstrap, exp_fewrel_formal_80rel, exp_fewrel_80pool_16sub_bootstrap |\\n| D037 | 2026-05-16 | D037: Round 2 审稿 Action Matrix 定稿——5C+12W 逐条方案，C1  | exp-003a, exp_fewrel_formal |\\n| D036 | 2026-05-16 | D035 修订：Table 3 以回归斜率为主指标，四分位 Δ 为辅 | exp_fewrel_80pool_16sub_bootstrap, exp_fewrel_16rel_bootstrap |\\n| D035 | 2026-05-16 | D033 集成采用极端批次方法重算，保持 Table 3 方法一致性 | exp_fewrel_16rel_bootstrap, exp_fewrel_80pool_16sub_bootstrap |\\n| D034 | 2026-05-16 | Amplification 报告策略：同时报告 quartile Δ 和 BCS-accuracy  | exp_fewrel_16rel_bootstrap, exp_fewrel_80pool_16sub_bootstrap |\\n\\n\", \"total_chars\": 4380, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e497fdd0-8df1-4683-96c6-d8042cee1236",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "d9faa2d8-7420-4462-baaf-236f6d455029",
  "sourceToolAssistantUUID": "e497fdd0-8df1-4683-96c6-d8042cee1236",
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

_source line 13 · 2026-05-16T08:07:44.540Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016ykWEAR7WK7hn14npo5QUg`</summary>

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
  "parentUuid": "d9faa2d8-7420-4462-baaf-236f6d455029",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uSmRicJeJ4eCQ1iPAo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20980c09-24c9-46d9-b90f-0356cc7c8ef3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ar4pvfj5V6g8VUGsCyJsEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5534,
      "cache_read_input_tokens": 16824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5534,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 14 · 2026-05-16T08:07:44.552Z_

<details><summary>↩ Tool result · `toolu_016ykWEAR7WK7hn14npo5QUg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_framing.md\", \"content\": \"# Paper Framing — schema-dag-extraction\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\\n- Commitment deadline: August 2, 2026\\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\\n- Deadline: ARR May 25, 2026 (10 days from today)\\n\\n## Core Claims (2 claims) — Revised per D019\\n\\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.\\n\\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\\n\\n~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — \\\"why naive decomposition fails\\\" is itself a contribution.\\n\\n## Story Spine — Revised per D012\\n\\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\\n\\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\\n\\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.\\n\\n- **Three-task validation**:\\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio\\n  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel\\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\\n\\n- **Headline result template**: \\\"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid.\\\"\\n\\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\\n\\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\\n\\nThese channels are orthogonal and independently addressable.\\n\\n**Pairwise vs Aggregated Confusability**:\\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).\\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\\n\\n## Evidence Hierarchy (D012)\\n\\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\\n\\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\\n\\n**Few-NERD (NER)** — Qwen3 embeddings:\\n- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation\\n- Nonzero-only Spearman ρ=0.272 (p=5e-5)\\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\\n- Immune to type frequency confound (operates at type-pair level)\\n\\n**MAVEN (ED)** — MiniLM embeddings:\\n- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap\\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\\n- Cross-task replication on same-domain schema\\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\\n\\n### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication\\n\\nLarge effect size, cross-task (RE), scaling with schema complexity:\\n\\n**Formal 80-rel study** (exp_fewrel_formal_80rel):\\n- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97\\n- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)\\n- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)\\n- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)\\n\\n**16-rel sanity check** (exp_fewrel_formal):\\n- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\\n\\n**Pilot extreme batches** (fewrel_pilot, MiniLM):\\n- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp\\n\\nKey insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling\\n\\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\\n\\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\\n\\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\\n\\nMethodological case study on when aggregated confusability measures fail:\\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\\n- This is stronger than \\\"domain boundary\\\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\\n\\n### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)\\n\\nIntraSub rate monotonically increases with BCS on both NER and RE:\\n\\n**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0\\n**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)\\n- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon\\n- Same mechanism, different absolute magnitudes — consistent with cross-task expectations\\n\\nAdditional from extreme batch design:\\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\\n\\n## Embedding Ablation (D010)\\n\\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\\n\\n### Per-type (Layer 2)\\n| | Few-NERD | FewRel | MAVEN |\\n|---|---|---|---|\\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\\n\\n### Pairwise (Layer 1)\\n| | Few-NERD | MAVEN |\\n|---|---|---|\\n| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |\\n| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |\\n\\n### SCS→Empirical Confusion Validation (exp-015 fast)\\n| | Qwen3 | MiniLM |\\n|---|---|---|\\n| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |\\n| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |\\n\\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\\n\\n## Venue Fit Risks\\n\\n- **\\\"Just an empirical study\\\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \\\"Lost in the Middle\\\" (TACL 2024).\\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy | Experiment |\\n|---------|------------------|------------|\\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\\n\", \"total_chars\": 11568, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20980c09-24c9-46d9-b90f-0356cc7c8ef3",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "890a657f-8b84-48d4-9cc0-0ae0c9379549",
  "sourceToolAssistantUUID": "20980c09-24c9-46d9-b90f-0356cc7c8ef3",
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

_source line 15 · 2026-05-16T08:07:45.016Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019PheGrSERdzt7VRGX5Pjpu`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "890a657f-8b84-48d4-9cc0-0ae0c9379549",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uSmRicJeJ4eCQ1iPAo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f565461-636d-48b8-bcbe-63acd0391826",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ar4pvfj5V6g8VUGsCyJsEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5534,
      "cache_read_input_tokens": 16824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5534,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 16 · 2026-05-16T08:07:45.029Z_

<details><summary>↩ Tool result · `toolu_019PheGrSERdzt7VRGX5Pjpu`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'schema-dag-extraction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f565461-636d-48b8-bcbe-63acd0391826",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "40754613-057f-4cca-80d6-e6c1e2da29ba",
  "sourceToolAssistantUUID": "4f565461-636d-48b8-bcbe-63acd0391826",
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

_source line 17 · 2026-05-16T08:07:45.611Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BcY42VWEWFnMQyNWvbf21B`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40754613-057f-4cca-80d6-e6c1e2da29ba",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uSmRicJeJ4eCQ1iPAo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "950b7a84-28c6-4401-8a09-bb0ddb3e5daa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ar4pvfj5V6g8VUGsCyJsEh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5534,
      "cache_read_input_tokens": 16824,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5534
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 16824,
          "cache_creation_input_tokens": 5534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5534,
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

_source line 18 · 2026-05-16T08:07:45.622Z_

<details><summary>↩ Tool result · `toolu_01BcY42VWEWFnMQyNWvbf21B`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml\", \"content\": \"_next_id: 44\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:10 UTC\\n  summary: 项目立项，MVP 验证方案：Experiment 2 (Confusability Controlled) 为核心验证实验\\n  rationale: 'IDEA_BRIEF 的核心假设是 type confusability 独立于 type count 驱动 LLM IE 质量下降。Experiment\\n    2（固定 count 变 BCS）是最直接的假设检验。Pass 标准: |r|≥0.3 且 p<0.05。ACE05 RE + Few-NERD 双数据集验证。ARR\\n    May 25 DDL（11天），MVP 需 1-2 天完成。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:15 UTC\\n  summary: 修正 MVP 统计设计：random samples 从 10 增至 25/档，加入 per-type solo baseline 控制变量，核心指标改为\\n    Δ(solo_F1 - batch_F1)\\n  rationale: Reviewer 指出 n=12 下 |r|=0.3 对应 p≈0.34，无法同时满足 |r|≥0.3 且 p<0.05。增至 25 random\\n    batches/档 → n≈54，|r|≥0.27 即可达 p<0.05。同时加入 solo F1 控制 type 固有难度，避免将\\\"类型本身难抽取\\\"误归因于\\\"confusability\\n    效应\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 23:11 UTC\\n  summary: MVP 分析方法从 Δ(solo-batch) 切换到 within-count Pearson r(F1, BCS)，pass 标准更新为\\n    |r|≥0.3 at fixed count\\n  rationale: Exp 1 发现 count curve 方向反转（F1 随 count 上升），根因是低 count 时模型过度 hallucinate（pred/gold=8x\\n    at count=1）。solo baseline 处于极端行为模式，Δ 被跨 count 行为差异污染。改为 within-count 对比更干净：同一\\n    count 下比较不同 BCS 的 F1，直接检验 confusability 独立效应。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count curve reversed, hallucination at low count\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 23:31 UTC\\n  summary: MVP 主指标更新为 within-count r(recall, BCS)，F1 因 over-prediction confound 降为补充指标\\n  rationale: Exp 1 text-match 重评估发现：recall 单调下降（0.72→0.42，符合预期），precision 单调上升（0.11→0.52，over-prediction\\n    减少），F1 受 precision 主导而反转。within-count 分析中 precision confound 在同一 count 下近似恒定，F1\\n    仍可用；但 recall 更干净且直接反映 type confusion。WrongType 错误（text 正确但 type 错标）随 count 从 0\\n    升至 2434，直接支持 confusability 假设。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: recall monotonically decreases with count; WrongType errors increase;\\n      over-prediction confounds F1\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-15 02:34 UTC\\n  summary: 'MVP PASS（refined mechanism）: confusability 通过 type confusion 通道驱动降级，选择\\n    Narrative A (multi-channel degradation model)'\\n  rationale: Exp 2 结果：recall vs BCS 不显著（r=0.25, p=0.066），但 F1 vs BCS 在 count_12 显著（r=0.50,\\n    p=0.008），偏相关 r=0.30 p=0.026 达到 pass 标准。Confusion rate high-BCS vs low-BCS 差异 30-40x（p=0.043）。机制清晰：confusability\\n    不导致遗漏，而是导致错标。选 Narrative A（multi-channel）因为：(1) 用上所有数据（exp1 count→recall + exp2\\n    BCS→confusion）(2) 两个正交机制 story 更丰富 (3) SDGD 框架天然需要同时处理 count 和 confusability。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count drives recall decline 0.72→0.42\\n  - exp_id: exp002_confusability_controlled\\n    role: evidence\\n    result: BCS drives type confusion 30-40x, F1 partial r=0.30 p=0.026\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-15 04:04 UTC\\n  summary: 跳过 Dream 模拟，直接批准 P0 实验\\n  rationale: 'Dream 模拟因基础设施 bug 崩溃（TypeError: _run_dream_pipeline() got unexpected\\n    keyword argument ''operational_chat_id''），P0 实验已被阻塞 9+ 小时。这是平台问题不是项目问题，不应阻塞研究进度。paper_framing.md\\n    和 experiment_plan.yaml 已完成，方向清晰，可直接推进。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D007\\n  date: 2026-05-15 04:16 UTC\\n  summary: RE 第三任务需先做 BCS pilot 验证，不直接 commit\\n  rationale: Reviewer 指出 RE 的 confusability 机制与 NER/ED 可能不同——RE type confusion 取决于\\n    entity pair 语义角色而非 relation label embedding 相似度。如果 BCS 在 RE 上不 work，反而削弱 task-agnostic\\n    claim。策略：先花 1h 做 FewRel type 的 BCS 矩阵 + 小规模 pilot（5 batches），确认信号存在再 commit P0；信号不存在则\\n    claim 缩窄为 span-level IE，在 limitation 中承认。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-15 05:10 UTC\\n  summary: 重构证据层级：pairwise 分析升为主要证据，batch-level 需控制 type frequency\\n  rationale: exp003a v2 Reviewer 独立核实发现 within-count BCS-F1 正相关（高 BCS→高 F1），与假设方向相反。根因：type\\n    frequency 混淆变量（高频类型既有高 BCS 又被模型更好提取）。pairwise 分析（r=0.156, p=4.6e-12）不受此影响，仍成立。需要：(1)\\n    pairwise 升为 Channel 1 主要证据 (2) 新增 per-type F1 分析控制频率 (3) batch-level 正相关在论文中透明报告并解释混淆变量。\\n  related_experiments:\\n  - exp_id: exp003a\\n    role: trigger\\n    result: within-count r>0 contradicts hypothesis direction\\n  depends_on:\\n  - D006\\n- id: D009\\n  date: 2026-05-15 07:21 UTC\\n  summary: 'Paper story reframe: BCS proxy task-specific → SDGD-cal empirical calibration\\n    成为核心贡献'\\n  rationale: MAVEN per-type 分析显示 BCS 与 F1 正相关（ρ=+0.184, p=0.025），与 Few-NERD 方向相反且已排除\\n    frequency confound。说明 embedding-based BCS 是 task-specific proxy：对 NER 有效（type\\n    name 相似度驱动 confusion），对 ED 无效（trigger word 歧义驱动 confusion，非 type name embedding\\n    距离）。Reframe 方向：BCS proxy 有局限 → 需要 empirical confusability（从 actual confusion matrix\\n    推导）→ SDGD-cal 用 empirical calibration 解决跨任务泛化。这让 SDGD-cal 成为比 SDGD-zero 更核心的贡献。\\n  related_experiments:\\n  - exp_id: exp004_maven_bcs\\n    role: trigger\\n    result: MAVEN per-type ρ=+0.184 contradicts hypothesis\\n  - exp_id: exp003a_prompt_v2_rerun\\n    role: baseline\\n    result: Few-NERD per-type ρ=-0.293 supports hypothesis\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-15 07:37 UTC\\n  summary: FewRel pilot PASS (D007)，commit RE 为第三任务；需做 embedding ablation (MiniLM\\n    vs Qwen3 × 3 tasks)\\n  rationale: FewRel pilot 显示高 BCS→低 accuracy（Δ=-21~50pp），效应量极大，假设方向正确。但使用了 MiniLM（BCS\\n    range 0.42-0.97）而非 Qwen3（Few-NERD/MAVEN 用的）。三任务交叉对比显示：NER 弱负(Qwen3)、ED 反向(Qwen3)、RE\\n    强负(MiniLM)——无法区分 task effect vs embedding effect。需要 2×3 embedding ablation（MiniLM/Qwen3\\n    × NER/ED/RE）来厘清。这是 CPU 任务（重算 BCS 矩阵+重跑分析），成本极低但对论文 story 至关重要。\\n  related_experiments:\\n  - exp_id: fewrel_pilot\\n    role: trigger\\n    result: batch Δ=-21~50pp, hypothesis direction correct\\n  depends_on:\\n  - D007\\n  - D009\\n- id: D011\\n  date: 2026-05-15 07:41 UTC\\n  summary: '采用 Narrative A: embedding proxy 有域边界，same-domain 需 SDGD-cal empirical\\n    calibration'\\n  rationale: 三任务数据全用上：Few-NERD(NER)+FewRel(RE) 作为 cross-domain positive evidence，MAVEN(ED)\\n    作为 same-domain boundary condition。自然引出 SDGD-zero(embedding proxy, cross-domain)\\n    vs SDGD-cal(empirical confusion, task-agnostic) 的互补关系。比方案B（需先验证SDGD-cal）更安全，比方案C（浪费MAVEN数据）更坦诚。Claim\\n    1 修改为含 boundary condition 的版本。\\n  related_experiments:\\n  - exp_id: exp004_maven_bcs\\n    role: boundary_condition\\n    result: MAVEN per-type ρ=+0.184 positive\\n  - exp_id: fewrel_pilot\\n    role: cross_task_replication\\n    result: Δ=-21~50pp strong negative\\n  - exp_id: exp003a_prompt_v2_rerun\\n    role: primary_evidence\\n    result: Few-NERD per-type ρ=-0.293\\n  depends_on:\\n  - D009\\n  - D010\\n- id: D012\\n  date: 2026-05-15 09:06 UTC\\n  summary: 证据层级重排：pairwise SCS→confusion 为唯一主要证据，per-type 降为辅助（centrality confound）\\n  rationale: MAVEN MiniLM ablation 证实 per-type 正向与 embedding 选择无关（MiniLM ρ=+0.208,\\n    Qwen3 ρ=+0.184 方向一致）。但 MiniLM pairwise 在 MAVEN 上显著（r=+0.120, p≈0），Qwen3 无信号。说明：(1)\\n    pairwise confusability 在所有数据集上真实存在，(2) per-type mean BCS 混合了 confusability 和 type\\n    centrality（语义邻居多=常见类型=LLM 擅长=高 F1），频率控制无法完全消除。论文主要证据应聚焦 pairwise SCS→confusion\\n    + FewRel batch-level 强效应，per-type 作为辅助，MAVEN per-type 正向作为 centrality confound\\n    案例研究。\\n  related_experiments:\\n  - exp_id: exp004_maven_bcs\\n    role: evidence\\n    result: MiniLM pairwise r=+0.120 significant; per-type positive both embeddings\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-15 09:07 UTC\\n  summary: Narrative 精化：核心论点从 embedding domain boundary 改为 pairwise vs aggregation\\n    level confound\\n  rationale: MAVEN MiniLM ablation 证实 per-type 正向与 embedding 无关（MiniLM 无压缩也正向）。问题是\\n    per-type 聚合的 centrality confound，非 embedding proxy 失效。但 MiniLM pairwise 在 MAVEN\\n    上显著（r=+0.120）→ pairwise confusability 跨任务普遍存在。SDGD 直接用 pairwise similarity 做 graph\\n    coloring，绕过聚合 confound。论文核心论点：confusability 在 type-pair 级别操作，per-type aggregation\\n    在同域 schema 引入 centrality confound，SDGD 的 pairwise 设计天然规避此问题。2×3 embedding ablation\\n    矩阵本身成为论文 Table。\\n  related_experiments:\\n  - exp_id: exp004_maven_bcs\\n    role: evidence\\n    result: MiniLM pairwise r=+0.120 on MAVEN; per-type positive both embeddings\\n  depends_on:\\n  - D012\\n- id: D014\\n  date: 2026-05-15 11:20 UTC\\n  summary: SDGD-zero 差于 baseline，Claim 3 需重大调整或放弃\\n  rationale: exp-008 SDGD-zero F1=0.251 < single_pass=0.445 < random_batch=0.320。根因：merge\\n    amplifies hallucination——每个 batch 处理全部样本但 schema 受限，模型过度预测 batch 内类型，merge 累积\\n    FP。confusability-aware 分解比随机分组差可能因为语义不相关 types 混合导致模型缺少 disambiguation context。Claims\\n    1-2（confusability 分析）不受影响。需要决定：(A) 修复 merge 策略重跑 (B) SDGD 降为 discussion/future\\n    work (C) 等 SDGD-cal 结果再定。\\n  related_experiments:\\n  - exp_id: exp008_sdgd_zero_fewnerd\\n    role: trigger\\n    result: SDGD-zero F1=0.251 < single_pass=0.445\\n  depends_on:\\n  - D013\\n- id: D015\\n  date: 2026-05-15 13:39 UTC\\n  summary: SDGD v2 time-boxed probe (2h) before multi-model; fail → Claim 3 降为 future\\n    work\\n  rationale: SDGD-zero 负向(F1=0.251 vs single_pass=0.445)，根因 merge amplification 已诊断。v2\\n    修复(min_batch_size+confidence-gated merge)成本仅2h，成功则论文获 prescriptive contribution，失败不伤\\n    Claims 1-2。距 DDL 10 天，串行 v2→exp-012 时间充裕。成功标准：v2 F1 > 0.445。\\n  related_experiments:\\n  - exp_id: exp-008\\n    role: evidence\\n    result: 'negative: SDGD-zero F1=0.251, merge amplification confirmed'\\n  - exp_id: exp-012\\n    role: next\\n    result: 'planned: multi-model validation after v2 probe'\\n  depends_on: []\\n- id: D016\\n  date: 2026-05-15 14:57 UTC\\n  summary: exp-012 flashinfer 不兼容 Blackwell，SDGD v2 先占 GPU，flashinfer 并行修复\\n  rationale: vLLM 0.20.2 废弃 VLLM_ATTENTION_BACKEND 环境变量，flashinfer 0.6.8 无法为 SM120\\n    JIT 编译 FP8 GEMM。两次启动失败。Agent 正确决策：(1) SDGD v2 立即占 GPU 不浪费；(2) CPU worker 并行升级\\n    flashinfer + CUDA 13 nvcc；(3) exp-012 r3 排 SDGD v2 之后 (~17:30 UTC)。\\n  related_experiments:\\n  - exp_id: exp-012\\n    role: blocked\\n    result: flashinfer SM120 incompatibility\\n  - exp_id: exp-008\\n    role: retry\\n    result: SDGD v2 probe started, F1>0.445 threshold\\n  depends_on:\\n  - D015\\n  - D014\\n- id: D017\\n  date: 2026-05-15 15:00 UTC\\n  summary: Reviewer 深度审查后调整实验矩阵：exp-006/005 降优，加 3 个 0-GPU-hour 分析，SDGD v2 阈值放宽到 F1>0.40\\n  rationale: 80-rel scaling data (3.4x amplification) 已覆盖 exp-006 interaction effect。3\\n    tasks 足够，exp-005 DocRED 降 P2。Reviewer 建议 3 个 0-GPU-hour 高 ROI 分析：(1) FewRel pairwise\\n    error taxonomy 跨任务验证 Claim 2；(2) bootstrap 95% CI 加固所有 correlation；(3) exp-015\\n    fast SCS→confusion validation。SDGD v2 阈值从 F1>0.445 放宽到 F1>0.40（接近 baseline 也有\\n    story：decomposition 损失可控 + latency 优势），F1<0.35 则 drop Claim 3。Claim 表述用具体数据\\\"3.4x\\n    amplification between 16-type and 80-type\\\"替代函数形式声明。\\n  related_experiments:\\n  - exp_id: exp_fewrel_formal_80rel\\n    role: evidence\\n    result: 3.4x BCS effect scaling\\n  - exp_id: exp-006\\n    role: deprioritized\\n    result: covered by 80-rel scaling\\n  - exp_id: exp-005\\n    role: deprioritized\\n    result: P2, 3 tasks sufficient\\n  - exp_id: exp-008\\n    role: retry\\n    result: v2 running, threshold F1>0.40\\n  depends_on:\\n  - D015\\n  - D016\\n- id: D018\\n  date: 2026-05-15 15:10 UTC\\n  summary: 补充 40-rel 中间点 + 多模型备选方案（AWQ/8B）+ MAVEN case study\\n  rationale: Reviewer 二次审查指出：(1) 2 点 scaling 不够，40-rel 中间点 ~1 GPU-hour 可得 3 点 scaling\\n    curve；(2) exp-012 双 retry 失败，需备选方案——Llama-70B-AWQ 或 Llama-8B，并行下载不等 r3；(3) MAVEN\\n    case study 0 GPU-hour 补强 centrality confound narrative。多模型验证是投稿硬门槛，24h 内必须完成。\\n  related_experiments:\\n  - exp_id: exp-012\\n    role: critical_path\\n    result: dual retry failed, backup plan needed\\n  - exp_id: exp_fewrel_formal_80rel\\n    role: evidence\\n    result: need 40-rel middle point for 3-point scaling\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-15 15:47 UTC\\n  summary: SDGD v2 confirmed negative, kill per_type early, Claim 3 dropped — pivot\\n    to analysis-only paper\\n  rationale: 'SDGD v2 confidence-gated merge: sdgd_zero F1=0.241, random_batch F1=0.301,\\n    both far below baseline 0.445 and threshold F1>0.40 (D017). Per_type 66-type sequential\\n    inference blocking GPU for exp-012 critical path. v1 per_type was also below baseline\\n    (0.2915). Decomposition paradigm has intrinsic FP amplification that merge strategies\\n    cannot fully resolve. Claim 3 dropped; SDGD discussed as future work. Paper pivots\\n    to 2-claim analysis: (1) confusability independence + scaling, (2) multi-channel\\n    degradation mechanism.'\\n  related_experiments:\\n  - exp_id: exp-008\\n    role: evidence\\n    result: 'SDGD v2 negative: sdgd_zero=0.241, random=0.301, baseline=0.445'\\n  - exp_id: exp-012\\n    role: critical_path\\n    result: unblocked by killing SDGD per_type\\n  depends_on:\\n  - D017\\n  - D015\\n  - D014\\n- id: D020\\n  date: 2026-05-15 16:02 UTC\\n  summary: 启动 Paper Agent 写作，2-claim analysis paper + SDGD negative result，Dream 结构性问题同步解决\\n  rationale: Claims 1+2 证据链完整（3 任务 × 多层证据），exp-012 最后 P0 可 Patch。10 天 deadline，Paper\\n    Agent 24h pipeline 必须立即启动。Dream 两轮均 Weak Reject，主要因写作质量（related work 2 refs, effect\\n    size 未 contextualize, metric undefined）非证据不足——这些是写作阶段能解决的问题。\\n  related_experiments:\\n  - exp_id: exp-012\\n    role: pending P0, Patch in when done\\n  - exp_id: dream_20260515T140829\\n    role: structural issues identified\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-15 16:05 UTC\\n  summary: 40-rel 中间点升 P0，利用 AWQ 下载期间 GPU 空闲立即执行\\n  rationale: Scaling claim 仅 2 个数据点（16-rel=9.1pp, 80-rel=31.2pp），审稿人必问线性 vs 非线性。40-rel\\n    中间点 ~1 GPU-hour，Qwen3 已在服务器上无需下载，AWQ 下载期间 GPU 完全空闲，零机会成本。\\n  related_experiments:\\n  - exp_id: exp_fewrel_formal_80rel\\n    role: scaling baseline\\n  - exp_id: exp_fewrel_formal\\n    role: 16-rel baseline\\n  - exp_id: exp-012\\n    role: AWQ downloading, GPU idle\\n  depends_on:\\n  - D018\\n  - D020\\n- id: D022\\n  date: 2026-05-15 16:23 UTC\\n  summary: exp012 放弃 70B AWQ，转用 LLaMA-3.1-8B-Instruct\\n  rationale: 70B 在 Blackwell 上连续 3 轮失败（r1/r2 flashinfer 不兼容，AWQ 磁盘空间不足无法完成下载）。8B 已下载就绪，BF16\\n    直接加载无兼容性风险。跨 family + 跨 scale（Qwen3-32B → LLaMA-8B）的验证比同 scale 不同 family 更有论文价值——证明\\n    confusability 效应不依赖模型容量。DDL 仅剩 10 天，不能继续在 70B 兼容性上耗时间。\\n  related_experiments:\\n  - exp_id: exp-012\\n    role: target\\n    result: switching from 70B to 8B\\n  - exp_id: exp012_llama_fewnerd_r3\\n    role: predecessor\\n    result: failed (AWQ disk space insufficient)\\n  - exp_id: exp012_llama_fewnerd_r2\\n    role: predecessor\\n    result: failed (flashinfer incompatible)\\n  depends_on:\\n  - D020\\n  - D021\\n- id: D023\\n  date: 2026-05-15 16:50 UTC\\n  summary: exp012 多模型验证策略：先试 free-form generation 诊断，失败则接受 single-model limitation\\n  rationale: exp012 全系列失败（r1-r3 flashinfer SM120 不兼容，AWQ 磁盘不足，r4 8B 零预测）。8B 零输出最可能原因是\\n    vLLM structured output JSON schema 与 LLaMA tokenizer 不兼容（gen_tokens=2 = 只输出 `[]`）。诊断方案：关闭\\n    structured output 约束做 free-form generation + regex 后处理，~15 min 即可验证。成功则重跑，失败则在论文\\n    §6.3 接受 single-model limitation（Qwen3-32B 已有 3 任务 × 多层证据，单模型不构成致命弱点）。DDL 仅剩 10\\n    天，不再尝试下载新模型或升级 CUDA toolkit。\\n  related_experiments:\\n  - exp_id: exp012_llama_fewnerd_r4\\n    role: trigger\\n    result: failed - zero predictions\\n  - exp_id: exp012_llama_fewnerd_r3\\n    role: predecessor\\n    result: failed - flashinfer SM120\\n  - exp_id: exp012_llama_awq\\n    role: predecessor\\n    result: killed - disk space\\n  depends_on:\\n  - D022\\n- id: D024\\n  date: 2026-05-15 16:53 UTC\\n  summary: 多模型验证硬截止 May 18；Paper Agent 立即启动 Full Draft（单模型版本，多模型结果到位后 Patch）\\n  rationale: 'Reviewer warning: exp-012 多模型验证已失败 6+ 次（70B flashinfer 不兼容, 8B 零预测）。距\\n    ARR May 25 仅 10 天，论文零产出。策略：(1) 给多模型验证 3 天窗口（截止 May 18），Agent 正在准备 exp012_llama_8b\\n    和 exp012_llama_awq；(2) 立即启动 Paper Agent 以当前单模型证据写 Full Draft——三任务 cross-task replication\\n    是部分替代；(3) May 18 前多模型仍失败则调整 claim 措辞为 \\\"We observe with Qwen3-32B\\\" 并在 Limitation\\n    明确承认，强化 cross-task angle。不预先降级，先推进。'\\n  related_experiments:\\n  - exp_id: exp-012\\n    role: multi-model validation\\n    result: 6+ failures, still attempting\\n  - exp_id: exp-002\\n    role: primary evidence\\n    result: success\\n  - exp_id: exp-004\\n    role: cross-task MAVEN\\n    result: success\\n  - exp_id: exp-016\\n    role: cross-task FewRel\\n    result: success\\n  depends_on:\\n  - D022\\n  - D019\\n- id: D025\\n  date: 2026-05-15 18:10 UTC\\n  summary: Table 3 NER Missed 数据修正：12/14/16% 替换为实际计算值 42.8/64.8/49.9%，叙事从\\\"BCS不影响检测\\\"改为\\\"NER与RE错误机制不同\\\"\\n  rationale: Agent + Reviewer 双重验证确认 Table 3 NER Missed 12%/14%/16% 无任何实验 artifact\\n    支撑，疑似从 RE 数据外推（+2pp）。实际从 exp007 raw predictions 重新计算的值为 low=42.8%, medium=64.8%,\\n    high=49.9%，差距 30-50pp 且趋势非 flat。原叙事\\\"missed rate remains flat at 10-16%\\\"在 NER 端不成立，需限定为仅\\n    RE。NER/RE 差异本身是有意义的发现，可加强分析深度。\\n  related_experiments:\\n  - exp_id: exp007_error_taxonomy\\n    role: source\\n    result: NER missed rates 42.8/64.8/49.9% (recomputed)\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    role: source\\n    result: RE missed rates 10.4/11.3/13.1/15.7% (registry verified)\\n  depends_on: []\\n- id: D026\\n  date: 2026-05-15 18:36 UTC\\n  summary: exp006 交互效应不显著(p=0.505)，结论 negative；不在论文主体引用，至多作为 supplementary exploratory\\n    analysis\\n  rationale: 2×2 factorial 设计（count × BCS）的交互项 z=-0.667, p=0.505, estimate=-0.036，完全在噪声范围内。此外设计存在结构性混淆：BCS\\n    与 count 不正交（high count 的 BCS floor 被推高），high_count/high_bcs 的 10 个 batch BCS 完全相同（伪重复）。Reviewer\\n    建议禁止声称 multiplicative interaction。实验为 P1（D017 降优），paper story 不依赖此结果。资源转向 exp012（P0\\n    多模型验证）。\\n  related_experiments:\\n  - exp_id: exp006_interaction_2x2\\n    role: primary\\n    result: 'negative: interaction z=-0.667, p=0.505, not significant'\\n  depends_on:\\n  - D017\\n- id: D027\\n  date: 2026-05-15 20:01 UTC\\n  summary: exp012 exp1 跨模型验证成功：Channel 1 (count→recall) 在 LLaMA-3.1-8B 上复现，per-batch\\n    r=0.725\\n  rationale: LLaMA-3.1-8B recall 从 0.702 降至 0.273（-43pp），Qwen3-32B 从 0.640 降至 0.304（-34pp）。Per-batch\\n    correlation r=0.725 表明 schema 配置是困难的主要来源而非模型特异性。弱模型下降更陡，支持 schema complexity as\\n    task-inherent difficulty 叙事。exp1 数据已交 Paper Agent 写入论文。exp2（Channel 2 BCS-controlled）正在重跑。\\n  related_experiments:\\n  - exp_id: exp012_llama_8b_r2\\n    role: primary\\n    result: 'exp1 success: recall decline -43pp, per-batch r=0.725 with Qwen3-32B'\\n  depends_on: []\\n- id: D028\\n  date: 2026-05-15 20:34 UTC\\n  summary: exp012 exp2 Channel 2 跨模型复现失败：极端 batch 方向正确但效果微弱(5pp/4.3pp)，随机 batch 信号淹没在\\n    noise 中。论文不引用 exp2 数据，保持 Limitations 中\\\"Channel 2 pending\\\"的保守表述\\n  rationale: LLaMA-3.1-8B 上 BCS-controlled 效应远弱于 Qwen3-32B（Δ5pp vs 31.2pp），count_12\\n    的 BCS 分布压缩严重（Δ0.030），多个随机 batch 出现反向趋势（高 BCS 反而高 F1）。per_type_f1 全为 0（缺 char offset），无法做\\n    error taxonomy 分析。floor effect + BCS 压缩 + 模型能力不足共同导致信号不可检测。当前论文 Limitations 只\\n    claim Channel 1 replicated，这是最安全的策略。\\n  related_experiments:\\n  - exp_id: exp012_llama_8b_r2_exp2\\n    role: primary\\n    result: 'Channel 2 not replicated: extreme Δ=5pp/4.3pp, random batches noisy with\\n      counter-examples'\\n  depends_on:\\n  - D027\\n- id: D029\\n  date: 2026-05-15 21:12 UTC\\n  summary: 提分策略：(1) 40-rel 中间点已启动；(2) LLaMA-8B FewRel Channel 2 作为第二实验；(3) \\\"pending\\\"改诚实报告；目标\\n    7→8+\\n  rationale: Reviewer 独立评估：40-rel 提分 +0.5-0.75（3点scaling curve），LLaMA FewRel Channel\\n    2 提分 +0.75 if positive / +0.25 if negative（FewRel 效应大、metric 无 span 噪声，比 NER 更可能检测到跨模型信号）。\\\"pending\\\"\\n    改诚实报告避免信任风险（-0.5 vs -1.5）。最乐观 8.0-8.5，最可能 7.5-8.0。\\n  related_experiments:\\n  - exp_id: exp_fewrel_40rel_r4\\n    role: planned\\n    result: PREPARING\\n  - exp_id: exp012_llama_fewrel\\n    role: planned\\n    result: not yet created\\n  depends_on:\\n  - D027\\n  - D028\\n- id: D030\\n  date: 2026-05-15 22:37 UTC\\n  summary: exp012 两种场景预案：正向升级 cross-family claim（有限度），负向 frame 为 capacity-dependent\\n    finding；两种场景都诚实报告，不追加新模型\\n  rationale: Reviewer 预判分析：场景 A 诚实报告 7.5-8.0 分，场景 B 诚实报告 7.0-7.5 分，隐藏则 6.0-6.5。不追加模型因\\n    DDL 10 天内边际收益递减。3 tasks × 1 model 的任务多样性论点比 cross-model 更强。Claim 安全边界受 C001（40-rel\\n    来自 80-pool）和 C002（BCS amplification 仅 2 schema sizes）约束。\\n  related_experiments:\\n  - exp_id: exp012_llama_fewrel_ch2\\n    role: trigger\\n    result: running\\n  depends_on:\\n  - D022\\n- id: D031\\n  date: 2026-05-15 22:40 UTC\\n  summary: exp012 强复现（场景 A），执行 claim 升级 + 新发现\\\"model-invariant high-BCS floor\\\"加入正文\\n  rationale: LLaMA-8B BCS effect -27.1pp/-23.9pp 远超强复现阈值(15pp)，达 Qwen3 的 75-87%。高\\n    BCS 准确率跨模型恒定(0.510 vs 0.510)是预案外的新发现，表明 confusability 是 task-inherent difficulty\\n    而非 model-specific。Reviewer 评估提分至 7.75-8.25。按 D030 场景 A 预案执行 patch。NER negative\\n    由 metric/floor effect 解释，诚实报告。\\n  related_experiments:\\n  - exp_id: exp012_llama_fewrel_ch2\\n    role: evidence\\n    result: 'strong_positive: BCS Δ=-27.1pp(count_8)/-23.9pp(count_16), high-BCS floor\\n      model-invariant at 0.51'\\n  depends_on:\\n  - D030\\n  - D022\\n- id: D032\\n  date: 2026-05-15 22:41 UTC\\n  summary: 激活场景 A：Channel 2 跨模型复现成功，升级 claim 表述，不追加新模型，聚焦写作\\n  rationale: exp012 LLaMA-8B FewRel Δ=-27.1pp/-23.9pp，强复现。高 BCS floor 跨模型恒定(~0.51)是新发现。Reviewer\\n    预估 7.75-8.25。DDL 10 天内不追加模型，边际收益递减且风险高。Paper Agent 执行 Scene A patch。\\n  related_experiments:\\n  - exp_id: exp012_llama_fewrel_ch2\\n    role: evidence\\n    result: 'success: Δ=-27.1pp(count_8), -23.9pp(count_16), high-BCS floor model-invariant\\n      ~0.51'\\n  depends_on:\\n  - D030\\n  - D022\\n- id: D033\\n  date: 2026-05-16 00:23 UTC\\n  summary: 追加 16-rel 100 random batches + bootstrap CI 实验，填补 tab:bcs_controlled 空白\\n    + amplification ratio 正式 CI\\n  rationale: Reviewer 评估 Soundness 3→4 最高 ROI 方案：1-2 GPU 小时，消除表格 \\\"---\\\" 空白，让 3.4× amplification\\n    获得双端 CI 支撑。90% 概率正面结果。方案 2（FewRel pairwise）和方案 3（额外 seed）ROI 不足跳过。\\n  related_experiments:\\n  - exp_id: exp_fewrel_formal\\n    role: baseline\\n    result: 16-rel 单 batch Δ=9.1pp 无 CI\\n  depends_on:\\n  - D031\\n- id: D034\\n  date: 2026-05-16 01:55 UTC\\n  summary: Amplification 报告策略：同时报告 quartile Δ 和 BCS-accuracy 回归斜率，用斜率比较作为公平的 amplification\\n    证据（消除 BCS 域不重叠问题）\\n  rationale: D033 结果 Δ=-7.42pp（quartile）vs 原 -9.1pp（extreme batch），方法论不对称导致 ratio\\n    从 3.4× 变 4.2×。Reviewer 指出 80-pool-within BCS 范围 [0.47,0.65] 与 16-rel [0.65,0.90]\\n    几乎不重叠，Q4-Q1 Δ 不直接可比。斜率比较是标准化后的公平指标：如果斜率随 pool size 增大，则 amplification 成立且不受 BCS\\n    域差异影响。论文将报告两种指标（Δ + slope），以 slope 为主要 amplification 证据。\\n  related_experiments:\\n  - exp_id: exp_fewrel_16rel_bootstrap\\n    role: evidence\\n    result: Δ=-7.42pp CI[-9.45,-4.49], r=-0.6373\\n  - exp_id: exp_fewrel_80pool_16sub_bootstrap\\n    role: pending\\n    result: PREPARING\\n  depends_on:\\n  - D033\\n- id: D035\\n  date: 2026-05-16 01:58 UTC\\n  summary: D033 集成采用极端批次方法重算，保持 Table 3 方法一致性\\n  rationale: D033 bootstrap_ci.json 的 amplification 4.2× 混用了极端批次(80-rel分子)和四分位(16-rel分母)两种方法。论文\\n    Table 3 统一用极端批次比较，因此需用 D033 的 100 batch 数据按极端批次方法重算 16-rel Δ 和 CI。四分位 CI 作补充证据放正文，展示跨分析粒度稳健性。\\n  related_experiments:\\n  - exp_id: exp_fewrel_16rel_bootstrap\\n    role: source_data\\n    result: success, Δ_quartile=7.42pp\\n  - exp_id: exp_fewrel_80pool_16sub_bootstrap\\n    role: pending_comparison\\n    result: allocated_not_started\\n  depends_on: []\\n- id: D036\\n  date: 2026-05-16 02:14 UTC\\n  summary: D035 修订：Table 3 以回归斜率为主指标，四分位 Δ 为辅\\n  rationale: 80-pool 四分位 Δ=-3.92pp CI 跨零（[-7.79, +0.42]），但回归斜率=-0.401 CI 排除零（[-0.684,\\n    -0.062]）。两组斜率可比（-0.449 vs -0.401），说明 per-unit-BCS 效应一致。原 D035 计划用极端批次 Δ 做 Table\\n    3 主指标，但数据表明斜率是更稳健的指标。BCS range 差异（16-rel [0.65,0.90] vs 80-pool [0.46,0.68]）解释了四分位对比的弱化——80-pool\\n    类型多样性压缩了 BCS 对比空间。\\n  related_experiments:\\n  - exp_id: exp_fewrel_80pool_16sub_bootstrap\\n    role: primary\\n    result: slope=-0.401 significant, quartile CI crosses zero\\n  - exp_id: exp_fewrel_16rel_bootstrap\\n    role: comparison\\n    result: slope=-0.449, quartile significant\\n  depends_on:\\n  - D035\\n- id: D037\\n  date: 2026-05-16 03:13 UTC\\n  summary: 'D037: Round 2 审稿 Action Matrix 定稿——5C+12W 逐条方案，C1 需 v2 BCS-controlled\\n    RE 实验'\\n  rationale: Round 2 borderline (3.0/5)。Reviewer 独立审查确认：(1) C1 prompt 混淆是唯一可能推翻核心贡献的项，仅公开\\n    prompt 不够，需 v2 RE BCS-controlled 子集验证；(2) C2/C3 通过 D036 slope 叙事已部分解决，需清除 Abstract\\n    残留的 9.1pp vs 31.2pp 直接对比；(3) C4/C5 是 desk-reject 风险必须首先解决；(4) W3 cluster bootstrap\\n    是 CPU 工作可并行；(5) W5 SDGD on RE 优先级低于 C1。执行计划：Day 1 C5+C4+C1(prompt+实验)+W3+W4，Day\\n    2-3 编辑工作，Day 4-5 W5 if time。\\n  related_experiments:\\n  - exp_id: exp-003a\\n    role: v1/v2 comparison baseline\\n    result: v2 有 count curve 和 within-count 数据但无 BCS-controlled RE\\n  - exp_id: exp_fewrel_formal\\n    role: core RE evidence\\n    result: v2 prompt, BCS Δ=-31.2pp\\n  depends_on:\\n  - D036\\n- id: D038\\n  date: 2026-05-16 04:35 UTC\\n  summary: 'D038: BCS 定义不一致修复——统一为 MEAN pairwise SCS，重算 Table 4 + permutation test'\\n  rationale: Reviewer 发现 compute_bcs.py 用 MAX pairwise SCS，而论文定义和 80-pool 实验用 MEAN。16-rel\\n    bootstrap 和 80-rel formal 的 BCS 在错误 scale 上，导致 permutation test（p=0.436）混合了不同度量的斜率。方向性结论不变（斜率均为负），但精确数值和\\n    p 值需重算。修复为纯 CPU 工作（从现有 SCS matrix 重算），不需要重跑 GPU 实验。\\n  related_experiments:\\n  - exp_id: exp_fewrel_16rel_bootstrap\\n    role: affected\\n    result: BCS 用了 MAX，需重算为 MEAN\\n  - exp_id: exp_fewrel_formal_80rel\\n    role: affected\\n    result: BCS 用了 MAX，需重算为 MEAN\\n  - exp_id: exp_fewrel_80pool_16sub_bootstrap\\n    role: reference\\n    result: 已用 MEAN，无需修改\\n  depends_on:\\n  - D036\\n  - D037\\n- id: D039\\n  date: 2026-05-16 04:49 UTC\\n  summary: 'D039: BCS 统一选择 Path A (MEAN)——科学诚实优先，MAX 作 sensitivity analysis 报告'\\n  rationale: Path A (MEAN BCS) vs Path B (MAX BCS)：选择 MEAN 因为 (1) 论文公式原本就定义 MEAN，改\\n    MAX 有 metric shopping 嫌疑；(2) 核心结论不变——r=-0.467 仍 p<1e-6，Δ=-5.3pp CI 排除零；(3) permutation\\n    p=0.60 反而比旧 0.44 更支持 slope consistency claim；(4) 80-rel 斜率翻正是 BCS range 太窄 (IQR=0.033)\\n    导致的噪声，注明即可。MAX BCS 可在 appendix 作 sensitivity analysis 报告。\\n  related_experiments:\\n  - exp_id: exp_fewrel_16rel_bootstrap\\n    role: affected\\n    result: 'r: -0.637→-0.467, Δ: -7.4pp→-5.3pp'\\n  - exp_id: exp_fewrel_formal_80rel\\n    role: affected\\n    result: slope 翻正(+0.221 n.s.), BCS range=0.089 太窄\\n  - exp_id: exp_fewrel_80pool_16sub_bootstrap\\n    role: reference\\n    result: 已是 MEAN, 无变化\\n  depends_on:\\n  - D038\\n- id: D040\\n  date: 2026-05-16 05:31 UTC\\n  summary: v2 RE n=25 结果推翻 attenuation 叙述，升级为 \\\"confusability is task-inherent, not\\n    prompt artifact\\\"\\n  rationale: v2 prompt n=25 实验显示 Δ=25.5pp (CI [22.4,28.6], p<0.0001, r=−0.919)，效应巨大且高度显著。此前\\n    n=5 不显著是 underpowered + narrow BCS contrast (0.21 vs 0.44) 导致的伪阴性。v2 不消除效应意味着\\n    confusability 是 task-inherent property，直接回应 \\\"prompt artifact\\\" reviewer concern。论文\\n    §4.3、Introduction、Appendix G 均需更新，paper_framing.md 的 prompt sensitivity concern\\n    从 partially addressed 升级为 addressed。\\n  related_experiments:\\n  - exp_id: exp_v2_re_n25\\n    role: primary evidence\\n    result: Δ=25.5pp, r=−0.919, p<0.0001\\n  depends_on: []\\n- id: D041\\n  date: 2026-05-16 06:58 UTC\\n  summary: 放弃 exp-017 GPT-4o-mini：TUM proxy 未部署，AutoDL 无法访问 OpenAI API，不值得搭建基础设施\\n  rationale: AutoDL 服务器无法直接访问 OpenAI API（TUM proxy service not deployed）。距 DDL 9 天，debug\\n    基础设施的 ROI 太低。当前 2 模型族 (Qwen3-32B + LLaMA-3.1-8B) 满足跨模型验证基本要求，Discussion 已有 model\\n    coverage limitation 表述。exp-018 batch composition 的 practical contribution 优先级更高。\\n  related_experiments:\\n  - exp_id: exp017_gpt4o_mini_fewrel\\n    role: cancelled\\n    result: 'BLOCKED: TUM proxy not deployed'\\n  depends_on: []\\n- id: D042\\n  date: 2026-05-16 07:38 UTC\\n  summary: exp-018 成功：confusability-aware batching 在 RE 上 +1.44pp (显著)，无 merge amplification。进入论文收尾阶段。\\n  rationale: Graph coloring BCS 最小化分组 accuracy 0.8021 > random 0.7877±0.0178 (超 95%\\n    CI 上界 0.7967)，single_pass 0.5042 验证 schema overload。RE closed-set 无 merge amplification，与\\n    NER SDGD 失败形成对比。论文从纯诊断升级为诊断+缓解，直接回应 W6 (§5 过短) 和 SDGD 缺 actionable takeaway 的审稿意见。距\\n    DDL 9 天，核心实验已全部完成，进入写作集成 + final review。\\n  related_experiments:\\n  - exp_id: exp_confusability_batch_composition\\n    role: primary evidence\\n    result: aware=0.8021 > random=0.7877, single_pass=0.5042\\n  depends_on: []\\n- id: D043\\n  date: 2026-05-16 07:44 UTC\\n  summary: D042 修正：exp-018 confusability-aware 与 random 无显著差异 (p≈0.22)，oracle routing\\n    使 \\\"无 merge\\\" 为空真。§5 写法降级。\\n  rationale: Reviewer critical 审查发现：(1) 统计检验错误——单点 vs mean CI 不是合法检验，排名法 p≈0.19，z\\n    检验 p=0.22；(2) 实验用 oracle routing（每个样本只路由到含 gold type 的 batch），根本没有 merge 步骤，\\\"无\\n    merge amplification\\\"是空真。+29.8pp 是纯 count 效应（80→10 types），confusability-aware 额外收益\\n    +1.44pp 不显著。§5 写法从\\\"诊断+缓解\\\"降级为\\\"RE oracle routing decomposition 有效（count 效应）+ confusability-aware\\n    方向一致但不显著\\\"。\\n  related_experiments:\\n  - exp_id: exp_confusability_batch_composition\\n    role: re-evaluated\\n    result: aware vs random p≈0.22 n.s.; oracle routing, no actual merge\\n  depends_on:\\n  - D042\\n\", \"total_chars\": 27674, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "950b7a84-28c6-4401-8a09-bb0ddb3e5daa",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "b879c579-73fb-4078-99db-8411b491034e",
  "sourceToolAssistantUUID": "950b7a84-28c6-4401-8a09-bb0ddb3e5daa",
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

_source line 19 · 2026-05-16T08:07:48.918Z_

Now let me read the actual paper and additional project files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b879c579-73fb-4078-99db-8411b491034e",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uT4uSJzfe3gTrs7nic",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73f0b7e0-8ff6-4d59-8721-237edcb59215",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hKGrHPQNX3K8TmnDrtA1q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19577,
      "cache_read_input_tokens": 22358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19577,
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

_source line 20 · 2026-05-16T08:07:50.802Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014wdc4SDnX1Eg254x81P5s3`</summary>

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
  "parentUuid": "73f0b7e0-8ff6-4d59-8721-237edcb59215",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uT4uSJzfe3gTrs7nic",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0ca0866-da48-4367-9d23-9583bfbb715a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hKGrHPQNX3K8TmnDrtA1q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19577,
      "cache_read_input_tokens": 22358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19577,
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

_source line 21 · 2026-05-16T08:07:50.848Z_

<details><summary>↩ Tool result · `toolu_014wdc4SDnX1Eg254x81P5s3`</summary>

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
  "parentUuid": "d0ca0866-da48-4367-9d23-9583bfbb715a",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "ae6d1e2a-f272-424f-8590-b694aeb2dcfb",
  "sourceToolAssistantUUID": "d0ca0866-da48-4367-9d23-9583bfbb715a",
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

_source line 22 · 2026-05-16T08:07:51.804Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XgG3bacMe28wvsFg1QWcQM`</summary>

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
  "parentUuid": "ae6d1e2a-f272-424f-8590-b694aeb2dcfb",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uT4uSJzfe3gTrs7nic",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac31132e-051a-4078-b717-22df8375fccc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hKGrHPQNX3K8TmnDrtA1q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19577,
      "cache_read_input_tokens": 22358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19577,
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

_source line 23 · 2026-05-16T08:07:51.816Z_

<details><summary>↩ Tool result · `toolu_01XgG3bacMe28wvsFg1QWcQM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/memory.md\", \"content\": \"# Memory — schema-dag-extraction\\n\\n## exp-018 结果与经验（2026-05-16）\\n- **结果**: confusability_aware 0.8021 > random 0.7877±0.0178 (CI上界0.7967)，提升显著 +1.44pp\\n- single_pass 80-rel 全量仅 0.5042，schema overload 严重\\n- Graph coloring (Welsh-Powell) 将 intra-batch BCS 从 0.5585 降到 0.5524\\n- 51 types improved, 28 degraded — 效果非均匀，部分 type 受益更多\\n- **关键参数**: 80-rel pool, batch_size=8-rel per batch, 15 random seeds for CI, 960 samples\\n- **无 merge amplification** — RE closed-set 验证了 Director 的预判\\n- FLASHINFER_DISABLE_VERSION_CHECK=1 需要设置，否则 vLLM 启动失败\\n- 支持 --resume 断点续传（按 condition 粒度）\\n\\n## exp-018 定位澄清（2026-05-16, Director）\\n- exp-018 不是\\\"重试 SDGD\\\"，而是\\\"confusability-aware batching 在 RE closed-set classification 上的实用方案\\\"\\n- RE 每个 (head, tail) pair 独立分类，无实体边界合并 → 无 merge amplification 问题\\n- exp-008 SDGD 失败的 root cause = NER span overlap 的 merge amplification，不适用于 RE\\n- 论文写法：§5 SDGD 失败因 NER merge amplification，但 RE closed-set 避免了此问题 → practical recommendation\\n\\n## exp-017 GPT-4o-mini（2026-05-16, Director 决定放弃）\\n- TUM proxy 未部署在 AutoDL 服务器，无法访问 OpenAI API\\n- 闭源模型验证缺失已在 discussion.tex limitations 中说明\\n- 教训：API 实验需要预先确认 proxy 可达性\\n\\n## D035 集成方案（2026-05-16）\\n- 论文 Table 3 用**极端批次**方法（BCS 最低/最高各 ~5 batches 的 accuracy Δ），不是四分位\\n- D033 的 7.42pp 是四分位比较，需要用极端批次方法重算\\n- 80-pool-16sub 的 3.92pp 也是四分位，同样需要重算\\n- 四分位 CI 作为补充证据报告，展示效应在不同分析粒度下都稳健\\n- 两组数据一起集成到论文再编译上传\\n\\n## 80-pool-16sub 关键发现（2026-05-16）\\n- BCS 范围窄 [0.458, 0.684]（vs 独立 16-rel [0.653, 0.900]），因为从 80-rel pool 采样的 16 types 语义更分散\\n- 四分位 Δ CI 跨零 [-7.79, +0.42]，但回归斜率 CI 不跨零 [-0.684, -0.062]\\n- 效应弱于独立 16-rel pool——BCS 范围压缩导致效应量缩小，这本身支持 BCS 是驱动因素的论点\\n- 决策：用回归斜率做跨条件比较（斜率控制了 BCS 范围差异），四分位 Δ 作为直觉可读的补充\\n\\n## MAVEN per-type BCS 正相关是 artifact（2026-05-16）\\n- exp_maven_residualized_bcs 确认：控制 log_freq + degree_centrality 后相关消失\\n- MiniLM confound = frequency, Qwen3 confound = degree centrality (r=0.854)\\n- 同质 schema（MAVEN 168 event types 多来自 FrameNet）下 per-type BCS 聚合失效\\n- pairwise SCS 仍然有效\\n\\n## Few-NERD r 值差异根因（2026-05-16）\\n- 三个 r 值同源（同一 confusion matrix, 1953 pairs），差异仅因 Y 变量：rate=0.112, count=0.138, CI上界=0.156\\n- Table 2 r=0.112 正确（confusion rate，归一化 gold frequency）\\n- p-values 已修正：Few-NERD Pearson p=7×10⁻⁷, MAVEN p=7×10⁻⁴²\\n\", \"total_chars\": 2127, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac31132e-051a-4078-b717-22df8375fccc",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "8d5e1b05-3061-4ab6-a576-2c9d3f413dc2",
  "sourceToolAssistantUUID": "ac31132e-051a-4078-b717-22df8375fccc",
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

_source line 24 · 2026-05-16T08:07:52.158Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Dcgu8yXdYXNpBVQ67uz6Sr`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d5e1b05-3061-4ab6-a576-2c9d3f413dc2",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uT4uSJzfe3gTrs7nic",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4217670-eefe-4f0e-9037-e103eb5dfc81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hKGrHPQNX3K8TmnDrtA1q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19577,
      "cache_read_input_tokens": 22358,
      "output_tokens": 291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19577
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 291,
          "cache_read_input_tokens": 22358,
          "cache_creation_input_tokens": 19577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19577,
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

_source line 25 · 2026-05-16T08:07:52.169Z_

<details><summary>↩ Tool result · `toolu_01Dcgu8yXdYXNpBVQ67uz6Sr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml\", \"content\": \"paper:\\n  title: Does Type Confusability Drive Schema-Induced Degradation\\\\\\\\in Training-Free\\n    LLM Information Extraction?\\n  version: 3\\n  generated_at: '2026-05-16T02:22:29.529376+00:00'\\n  source: manual mapping from registry + paper_framing.md\\nclaims:\\n- text: 'Training-free LLM information extraction---prompting models with target schemas\\n    without fine-tuning---degrades sharply as schema complexity grows: NER recall\\n    drops from 0.72 to 0.42 with 64 candidate '\\n  type: quantitative\\n  location:\\n    section: abstract\\n    context: result_statement\\n  id: C001\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: recall count_1=0.720, count_64=0.418\\n    tier: 1\\n  deprecated: false\\n- text: 'We introduce the Schema Confusability Score (SCS) to quantify pairwise semantic\\n    overlap between types and design two complementary experimental paradigms: count\\n    cu'\\n  type: methodological\\n  location:\\n    section: abstract\\n    context: finding_statement\\n  id: C002\\n  evidence:\\n  - exp_id: exp015_scs_validation\\n    metric: 'SCS validated: Qwen3 rho=0.168 (p=7e-14), MiniLM rho=0.306 nonzero (p=5e-6)'\\n    tier: 1\\n  deprecated: false\\n- text: 'We presented a controlled empirical study isolating schema-induced degradation\\n    in training-free LLM IE into two orthogonal channels: a count channel suppressing\\n    recall as candidate types increase, and'\\n  type: quantitative\\n  location:\\n    section: conclusion\\n    context: result_statement\\n  id: C003\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: 'Channel 1: recall 0.72->0.418'\\n    tier: 1\\n  - exp_id: exp007_error_taxonomy\\n    metric: 'Channel 2: IntraSub vs BCS rho=1.0'\\n    tier: 1\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    metric: RE IntraSub vs BCS rho=0.954\\n    tier: 1\\n  deprecated: false\\n- text: We use Qwen3-32B-FP8 qwen3-2025, selected for its strong instruction-following\\n    capability, native structured JSON output support, and the practical advantage\\n    that the FP8-quantized 32B model fits on a\\n  type: quantitative\\n  location:\\n    section: experimental_setup\\n    context: result_statement\\n  id: C004\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: model setup, all experiments use Qwen3-32B-FP8 primary\\n    tier: 2\\n  deprecated: false\\n- text: We introduce the Schema Confusability Score to quantify semantic overlap between\\n    types in a schema. Given a type $t$ with name string $name(t)$, an embeddin\\n  type: methodological\\n  location:\\n    section: experimental_setup\\n    context: finding_statement\\n  id: C005\\n  evidence:\\n  - exp_id: exp015_scs_validation\\n    metric: 'SCS proxy validated: both embeddings significant (all p<1e-5)'\\n    tier: 1\\n  deprecated: false\\n- text: Channel~1\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: bold\\n  id: C006\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: recall 0.72->0.418 monotonic decline\\n    tier: 1\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: accuracy 0.857->0.504 monotonic decline\\n    tier: 1\\n  deprecated: false\\n- text: Channel~2\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: bold\\n  id: C007\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x\\n    tier: 1\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: BCS-controlled delta=-31.2pp\\n    tier: 1\\n  deprecated: false\\n- text: Training-free LLM information extraction---prompting a large language model\\n    with a target schema and asking it to extract structured information without any\\n    task-specific fine-tuning---enables rapid d\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C008\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: background framing, supported by all experiments\\n    tier: 3\\n  deprecated: false\\n- text: Second, pairwise SCS is a robust predictor of type confusion. Across Few-NERD\\n    (Pearson $r = 0.112$, $p < 10^{-12$) and MAVEN ($r = 0.129$, $p < 10^{-10$), embedding\\n    similarity between type pairs corre\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C009\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: Few-NERD pairwise Pearson r=0.112 [0.076, 0.156]\\n    tier: 1\\n  - exp_id: exp004_maven_bcs\\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\\n    tier: 1\\n  - exp_id: bootstrap_ci_analysis\\n    metric: CIs exclude zero for both\\n    tier: 1\\n  deprecated: false\\n- text: Third, confusability effects are robust across schema sizes, with BCS--accuracy\\n    slopes consistent between 16-type and 80-type pools (permutation p = 0.44)\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C010\\n  evidence:\\n  - exp_id: exp_fewrel_formal\\n    metric: 16-rel BCS effect delta=-9.1pp\\n    tier: 1\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: 80-rel BCS effect delta=-31.2pp, wider BCS range produces larger absolute\\n      gap\\n    tier: 1\\n  deprecated: false\\n- text: Fourth, per-type confusability aggregation is confounded on homogeneous schemas.\\n    On MAVEN, whose 168 event types all derive from the FrameNet ontology, the correlation\\n    between mean BCS and per-type er\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C011\\n  evidence:\\n  - exp_id: exp004_maven_bcs\\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\\n    tier: 1\\n  deprecated: false\\n- text: Fifth, confusability-aware schema decomposition fails to improve extraction.\\n    Our Schema-DAG-Guided Decomposition (SDGD) successfully separates confusable types\\n    into different batches, yet every decomp\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C012\\n  evidence:\\n  - exp_id: exp008_sdgd_v2_fewnerd\\n    metric: SDGD v2 F1=0.241 vs baseline 0.445\\n    tier: 1\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\n    metric: v1 sdgd_zero F1=0.251, also below baseline\\n    tier: 1\\n  deprecated: false\\n- text: Cross-task controlled experiments. We present BCS-controlled experiments with\\n    bootstrap confidence intervals on three datasets, establishing that the BCS--accuracy\\n    relationship is consistent across schema sizes (slope permutation p = 0.44)\\n  type: quantitative\\n  location:\\n    section: introduction\\n    context: result_statement\\n  id: C013\\n  evidence:\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: BCS--accuracy slope consistent across pools, permutation p=0.436\\n    tier: 1\\n  - exp_id: bootstrap_ci_analysis\\n    metric: FewRel count_8 delta CI [17.7, 42.7]\\n    tier: 1\\n  - exp_id: exp012_llama_fewrel_ch2\\n    metric: 'cross-model: LLaMA delta=-27.1pp (87% of Qwen3)'\\n    tier: 1\\n  deprecated: false\\n- text: We introduce the Schema Confusability Score (SCS), which quantifies pairwise\\n    semantic overlap between types using embedding cosine similarity, and its batch\\n  type: methodological\\n  location:\\n    section: introduction\\n    context: finding_statement\\n  id: C014\\n  evidence:\\n  - exp_id: exp015_scs_validation\\n    metric: SCS validated as proxy for empirical confusion\\n    tier: 2\\n  deprecated: false\\n- text: We demonstrate that pairwise SCS predicts type confusion across tasks and\\n    embedding models, while identifying a centrality confound that invalidates per-type\\n    aggrega\\n  type: methodological\\n  location:\\n    section: introduction\\n    context: finding_statement\\n  id: C015\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: Few-NERD pairwise r=0.112\\n    tier: 1\\n  - exp_id: exp004_maven_bcs\\n    metric: MAVEN centrality confound (per-type positive)\\n    tier: 1\\n  deprecated: false\\n- text: 95\\\\\\\\% CI\\n  type: quantitative\\n  location:\\n    section: results\\n    context: bold\\n  id: C016\\n  evidence:\\n  - exp_id: bootstrap_ci_analysis\\n    metric: 7 CIs all exclude null\\n    tier: 1\\n  deprecated: false\\n- text: Recall declines monotonically from 0.72 at count${\\\\\\\\,=\\\\\\\\,1$ to 0.42 at count${\\\\\\\\,=\\\\\\\\,64$,\\n    a 42\\\\\\\\% relative drop. Precision moves in the opposite direction, rising from\\n    0.11 to 0.52, reflecting a shift from\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C017\\n  evidence:\\n  - exp_id: exp001_count_baseline\\n    metric: recall 0.72->0.418, precision 0.105->0.52\\n    tier: 1\\n  deprecated: false\\n- text: Accuracy drops monotonically from 85.7\\\\\\\\% at count${\\\\\\\\,=\\\\\\\\,1$ to 50.4\\\\\\\\% at\\n    count${\\\\\\\\,=\\\\\\\\,80$, a near-halving when the model must discriminate among all 80\\n    relation types simultaneously.\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C018\\n  evidence:\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: count_1 acc=0.8573, count_80 acc=0.5042\\n    tier: 1\\n  deprecated: false\\n- text: 'In contrast to NER and RE, MAVEN relaxed F1 increases from 0.106 at count${\\\\\\\\,=\\\\\\\\,1$\\n    to 0.247 at count${\\\\\\\\,=\\\\\\\\,44$. This reversal arises from three properties of the\\n    MAVEN setup: (i)~trigger-level relaxed'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C019\\n  evidence:\\n  - exp_id: exp004_maven_bcs\\n    metric: count_1 relaxed_f1=0.106, count_44 relaxed_f1=0.247\\n    tier: 1\\n  deprecated: false\\n- text: 'The correlations are modest: $r^2  1.3--1.7\\\\\\\\%$, meaning pairwise confusability\\n    explains roughly 1.5\\\\\\\\% of the variance in type confusion. Other factors---entity\\n    frequency, prompt position effects lost-'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C020\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: Few-NERD pairwise r=0.112, r2=1.25%\\n    tier: 1\\n  - exp_id: exp004_maven_bcs\\n    metric: MAVEN pairwise r=0.129, r2=1.66%\\n    tier: 1\\n  deprecated: false\\n- text: Spearman rank correlations from the SCS validation experiment (exp-015) corroborate\\n    these findings. Across all type pairs, Qwen3 yields $ = 0.168$ ($p = 7.3  10^{-14$)\\n    and MiniLM yields $ = 0.144$ ($p\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C021\\n  evidence:\\n  - exp_id: exp015_scs_validation\\n    metric: Qwen3 rho=0.168 (p=7.3e-14), MiniLM rho=0.144 (p=1.7e-10)\\n    tier: 1\\n  deprecated: false\\n- text: BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar\\n    types; high-BCS batches contain maximally similar types. The confusability gap\\n    widens from 9.1\\\\\\\\,pp at 16 relations to 31.2\\\\\\\\\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C022\\n  evidence:\\n  - exp_id: exp_fewrel_formal\\n    metric: '16-rel: low_bcs 88.9% vs high_bcs 79.8%, delta=-9.1pp'\\n    tier: 1\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: '80-rel: low_bcs 82.3% vs high_bcs 51.0%, delta=-31.2pp'\\n    tier: 1\\n  - exp_id: exp_fewrel_40rel_r4\\n    metric: '40-rel: delta=-33.3pp (count_8), 80-pool subset'\\n    tier: 1\\n  deprecated: false\\n- text: 'At the 16-relation scale, switching from low-BCS to high-BCS batches reduces\\n    accuracy by 9.1 percentage points. Scaling to the full 80-relation pool amplifies\\n    this gap to 31.2\\\\\\\\,pp (95\\\\\\\\% CI: [17.7, 42.'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C023\\n  evidence:\\n  - exp_id: exp_fewrel_formal\\n    metric: 16-rel delta=-9.1pp\\n    tier: 1\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: 80-rel delta=-31.2pp\\n    tier: 1\\n  - exp_id: bootstrap_ci_analysis\\n    metric: CI [17.7, 42.7] for count_8, [22.9, 39.6] for count_16\\n    tier: 1\\n  deprecated: false\\n- text: Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. RE\\n    missed rates remain flat (10-16%), but NER missed rates are substantially higher\\n    (43-65%) and non-monotonic, revealing task-dependent error mechanisms.\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C024\\n  evidence:\\n  - exp_id: exp007_error_taxonomy\\n    metric: NER IntraSub 0%->49.4%; NER Missed 42.8/64.8/49.9% (non-monotonic, NOT\\n      flat)\\n    tier: 1\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    metric: RE IntraSub 0%->32.3%; RE Missed 10.4/11.3/13.1/15.7% (flat)\\n    tier: 1\\n  deprecated: false\\n- text: 'Three findings emerge. First, intra-batch substitution scales monotonically\\n    with BCS in both tasks: NER IntraSub rises from 0\\\\\\\\% (solo) to 49.4\\\\\\\\% (high BCS)\\n    with $ = 1.0$ ($p < 0.001$), and RE IntraSub'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C025\\n  evidence:\\n  - exp_id: exp007_error_taxonomy\\n    metric: NER IntraSub rho=1.0 (p<0.001)\\n    tier: 1\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    metric: RE IntraSub rho=0.954 (p<1e-6)\\n    tier: 1\\n  deprecated: false\\n- text: The extreme-batch analysis sharpens this picture. At count${\\\\\\\\,=\\\\\\\\,6$, high-BCS\\n    batches produce $27.5$ more confusion than low-BCS batches under extreme selection,\\n    versus $1.7$ under random batching. At\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C026\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: 'extreme: ratio_6=27.5, ratio_12=9.9; random: ratio_6=1.7, ratio_12=2.4'\\n    tier: 1\\n  deprecated: false\\n- text: 'Per-type analysis on MAVEN reveals an anomaly: the correlation between mean\\n    BCS and per-type error rate is positive---Qwen3 $ = +0.189$ ($p = 0.021$) and\\n    MiniLM $ = +0.208$ ($p = 0.011$)---opposite to'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C027\\n  evidence:\\n  - exp_id: exp004_maven_bcs\\n    metric: Qwen3 per-type rho=+0.189 (p=0.021), MiniLM rho=+0.208 (p=0.011)\\n    tier: 1\\n  deprecated: false\\n- text: 'Critically, the pairwise SCS--confusion correlation remains intact: MAVEN\\n    MiniLM pairwise $r = 0.129$ (CI: [0.104, 0.156], $p < 10^{-10$), consistent with\\n    the values in Table~tab:pairwise. The problem'\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C028\\n  evidence:\\n  - exp_id: exp004_maven_bcs\\n    metric: MAVEN MiniLM pairwise r=0.129\\n    tier: 1\\n  - exp_id: bootstrap_ci_analysis\\n    metric: CI [0.104, 0.156]\\n    tier: 1\\n  deprecated: false\\n- text: Few-NERD, whose 66 types span 8 coarse categories across diverse domains,\\n    does not exhibit this confound. Its per-type correlation is $ = -0.293$ ($p =\\n    0.02$, $n = 63$), in the expected negative direc\\n  type: quantitative\\n  location:\\n    section: results\\n    context: result_statement\\n  id: C029\\n  evidence:\\n  - exp_id: exp002_confusability_controlled\\n    metric: per-type Spearman rho=-0.293 (p=0.020, n=63)\\n    tier: 1\\n  deprecated: false\\n- text: Table~tab:sdgd_results reports the outcome.  Single-pass extraction achieves\\n    F1\\\\\\\\,=\\\\\\\\,0.445 (P\\\\\\\\,=\\\\\\\\,0.563, R\\\\\\\\,=\\\\\\\\,0.368).  SDGD obtains F1\\\\\\\\,=\\\\\\\\,0.251 (P\\\\\\\\,=\\\\\\\\,0.210,\\n    R\\\\\\\\,=\\\\\\\\,0.314), a 44\\\\\\\\% relative drop.  Rand\\n  type: quantitative\\n  location:\\n    section: sdgd_negative\\n    context: result_statement\\n  id: C030\\n  evidence:\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\n    metric: single_pass F1=0.4451, sdgd_zero F1=0.2514, random_batch F1=0.3197\\n    tier: 1\\n  deprecated: false\\n- text: 'The pattern across modes is consistent: decomposition boosts recall (per-type\\n    recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194\\n    versus 0.563).  The mechanism is straightfo'\\n  type: quantitative\\n  location:\\n    section: sdgd_negative\\n    context: result_statement\\n  id: C031\\n  evidence:\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\n    metric: per_type recall=0.5856, precision=0.194; single_pass recall=0.3679, precision=0.5631\\n    tier: 1\\n  deprecated: false\\n- text: A natural remedy is to resolve merge conflicts using model confidence.  Our\\n    v2 merge ranks competing predictions by the LLM's self-reported confidence and\\n    retains only the highest-scoring candidate fo\\n  type: quantitative\\n  location:\\n    section: sdgd_negative\\n    context: result_statement\\n  id: C032\\n  evidence:\\n  - exp_id: exp008_sdgd_v2_fewnerd\\n    metric: v2 sdgd_zero F1=0.2407 vs v1 0.2514, confidence-gated merge did not improve\\n    tier: 1\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 80-pool→16-sub slope = -0.401, CI [-0.701, -0.069], r = -0.221, p = 0.027\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C034\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: Independent 16-rel slope = -0.449, CI [-0.552, -0.346], r = -0.637, p < 1e-12\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C035\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: Full 80-rel slope = -0.151, CI [-0.930, +0.657], r = -0.082, p = 0.698, underpowered\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C036\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 16-rel extreme-batch Δ = +11.45pp, CI [7.66, 15.48]\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C037\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 80-pool→16-sub extreme-batch Δ = +9.79pp, CI [1.87, 17.50]\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C038\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 80-rel controlled extreme-batch Δ = +31.25pp, CI [22.92, 39.58]\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: Permutation slope-difference tests non-significant (p = 0.15-0.44)\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\ntables:\\n- caption: Dataset statistics. BCS Range indicates the min--max Batch Confusability\\n    Scores across count-curve batches (Experiment~1). Embedding column indicates the\\n    model used for SCS/BCS computation.\\n  label: tab:datasets\\n  location:\\n    section: experimental_setup\\n  cells:\\n  - exp_id: exp001_count_baseline\\n    metric: Few-NERD 66 types\\n  - exp_id: exp-004\\n    metric: MAVEN 168 event types, 77993 train mentions\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: FewRel 80 relations\\n  id: T001\\n  deprecated: false\\n- caption: Pairwise SCS--confusion correlation.\\n  label: tab:pairwise\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp002_confusability_controlled\\n    metric: Few-NERD Qwen3 pairwise r=0.112 [0.076, 0.156]\\n  - exp_id: exp004_maven_bcs\\n    metric: MAVEN MiniLM pairwise r=0.129 [0.104, 0.156]\\n  - exp_id: bootstrap_ci_analysis\\n    metric: bootstrap CIs for both\\n  id: T002\\n  deprecated: false\\n- caption: BCS-controlled FewRel accuracy.\\n  label: tab:bcs_controlled\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp_fewrel_formal\\n    metric: '16-rel: delta=-9.1pp'\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: '80-rel count_8: delta=-31.2pp, count_16: delta=-31.2pp'\\n  - exp_id: exp_fewrel_40rel_r4\\n    metric: '40-rel count_8: delta=-33.3pp, count_16: delta=-31.8pp'\\n  - exp_id: exp012_llama_fewrel_ch2\\n    metric: 'LLaMA cross-model: count_8 delta=-27.1pp, count_16 delta=-24.0pp'\\n  - exp_id: bootstrap_ci_analysis\\n    metric: 'CIs: count_8 [17.7, 42.7], count_16 [22.9, 39.6]'\\n  id: T003\\n  deprecated: false\\n- caption: Intra-batch substitution (IntraSub) rate by BCS bin.\\n  label: tab:error_taxonomy\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp007_error_taxonomy\\n    metric: NER IntraSub 0%->49.4%, rho=1.0; NER Missed 42.8/64.8/49.9% (non-monotonic)\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    metric: RE IntraSub 0%->32.3%, rho=0.954; RE Missed 10.4/11.3/13.1/15.7% (flat)\\n  id: T004\\n  deprecated: false\\n- caption: Few-NERD extraction under decomposition modes.\\n  label: tab:sdgd_results\\n  location:\\n    section: sdgd_negative\\n  cells:\\n  - exp_id: exp008_sdgd_zero_fewnerd_r2\\n    metric: 'v1: single_pass F1=0.445, sdgd_zero F1=0.251, random F1=0.320, per_type\\n      F1=0.292'\\n  - exp_id: exp008_sdgd_v2_fewnerd\\n    metric: 'v2: sdgd_zero F1=0.241, random F1=0.301'\\n  id: T005\\n  deprecated: false\\n- caption: Three-way BCS--accuracy analysis on FewRel (regression slope, quartile\\n    delta, permutation test).\\n  label: tab:within_pool\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: three_way_comparison\\n    metric: 'Independent 16-rel: slope=-0.449, CI [-0.552, -0.346], r=-0.637'\\n    source: artifacts/three_way_comparison/results_unified.json\\n  - exp_id: three_way_comparison\\n    metric: '80-pool→16-sub: slope=-0.401, CI [-0.701, -0.069], r=-0.221, p=0.027'\\n    source: artifacts/three_way_comparison/results_unified.json\\n  - exp_id: three_way_comparison\\n    metric: 'Full 80-rel: slope=-0.151, CI [-0.930, +0.657], underpowered'\\n    source: artifacts/three_way_comparison/results_unified.json\\n  - exp_id: three_way_comparison\\n    metric: 'Permutation test (16-rel vs 80-pool slopes): p=0.436'\\n    source: artifacts/three_way_comparison/results_unified.json\\n  id: T006\\n  deprecated: false\\nfigures:\\n- caption: Count scaling curves for NER (Few-NERD) and RE (FewRel)\\n  label: fig:count_curves\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp001_count_baseline\\n    metric: 'Panel (a): recall 0.72->0.418'\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: 'Panel (b): accuracy 0.857->0.504'\\n  - exp_id: exp_fewrel_40rel_r4\\n    metric: 'Panel (b): count_40=0.588'\\n  id: F001\\n  deprecated: false\\n- caption: BCS effect scaling with pool size\\n  label: fig:bcs_scaling\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp_fewrel_formal\\n    metric: 16-rel delta=9.1pp\\n  - exp_id: exp_fewrel_40rel_r4\\n    metric: 40-rel delta=33.3pp (80-pool subset)\\n  - exp_id: exp_fewrel_formal_80rel\\n    metric: 80-rel delta=31.2pp\\n  - exp_id: exp012_llama_fewrel_ch2\\n    metric: LLaMA 80-rel delta=27.1pp\\n  id: F002\\n  deprecated: false\\n- caption: Error taxonomy by BCS bin\\n  label: fig:error_taxonomy\\n  location:\\n    section: results\\n  cells:\\n  - exp_id: exp007_error_taxonomy\\n    metric: 'NER: IntraSub 0%->49.4%'\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    metric: 'RE: IntraSub 0%->32.3%'\\n  id: F003\\n  deprecated: false\\n_completeness:\\n  coverage: 32/42\\n  claims: 39\\n  tables: 6\\n  figures: 3\\n  tier_counts:\\n    tier1: 0\\n    tier2: 32\\n    tier3: 10\\n    tierX: 0\\n  last_checked: '2026-05-16T04:06:55.250751+00:00'\\n\", \"total_chars\": 22197, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4217670-eefe-4f0e-9037-e103eb5dfc81",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "6958b583-3c89-4ba9-8a7a-339cf8dfbd40",
  "sourceToolAssistantUUID": "c4217670-eefe-4f0e-9037-e103eb5dfc81",
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

_source line 26 · 2026-05-16T08:07:55.473Z_

Now let me read the actual paper sections for detailed review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6958b583-3c89-4ba9-8a7a-339cf8dfbd40",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uTYuBDPjA1JymqPB6f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "043e5430-cee7-4ecf-8c81-325ad2c4ec49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wnw5WCzmpTLc2pbLsDe8XF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11173,
      "cache_read_input_tokens": 41935,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11173,
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

_source line 27 · 2026-05-16T08:07:56.936Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CTwG2dxDSq42Xmpby2M9aH`</summary>

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
  "parentUuid": "043e5430-cee7-4ecf-8c81-325ad2c4ec49",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uTYuBDPjA1JymqPB6f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68486695-2e45-4cd4-a7c8-c9fe9544a115",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wnw5WCzmpTLc2pbLsDe8XF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11173,
      "cache_read_input_tokens": 41935,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11173,
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

_source line 28 · 2026-05-16T08:07:56.949Z_

<details><summary>↩ Tool result · `toolu_01CTwG2dxDSq42Xmpby2M9aH`</summary>

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
  "parentUuid": "68486695-2e45-4cd4-a7c8-c9fe9544a115",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "6d91df55-ba39-4e81-b2cc-49c161632495",
  "sourceToolAssistantUUID": "68486695-2e45-4cd4-a7c8-c9fe9544a115",
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

_source line 29 · 2026-05-16T08:07:57.885Z_

<details open><summary>🔧 Tool call — Read · `toolu_017yNJqyucCB9Zq5AinhtZeP`</summary>

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
  "parentUuid": "6d91df55-ba39-4e81-b2cc-49c161632495",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uTYuBDPjA1JymqPB6f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a19ca5e-19ed-405d-9866-116f9746453e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wnw5WCzmpTLc2pbLsDe8XF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11173,
      "cache_read_input_tokens": 41935,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11173,
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

_source line 30 · 2026-05-16T08:07:57.891Z_

<details><summary>↩ Tool result · `toolu_017yNJqyucCB9Zq5AinhtZeP`</summary>

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
  "parentUuid": "3a19ca5e-19ed-405d-9866-116f9746453e",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "019c1623-2983-43d9-b479-03fe5ffdbafb",
  "sourceToolAssistantUUID": "3a19ca5e-19ed-405d-9866-116f9746453e",
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

_source line 31 · 2026-05-16T08:07:58.021Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XqAdTa3wMnG27orA7jT68V`</summary>

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
  "parentUuid": "019c1623-2983-43d9-b479-03fe5ffdbafb",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uTYuBDPjA1JymqPB6f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f4606ba-834f-4763-8641-e9a35acfed55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wnw5WCzmpTLc2pbLsDe8XF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11173,
      "cache_read_input_tokens": 41935,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11173
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 41935,
          "cache_creation_input_tokens": 11173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11173,
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

_source line 32 · 2026-05-16T08:07:58.027Z_

<details><summary>↩ Tool result · `toolu_01XqAdTa3wMnG27orA7jT68V`</summary>

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
  "parentUuid": "4f4606ba-834f-4763-8641-e9a35acfed55",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "41e385a3-7aa4-47ce-83fe-f147a1f64b57",
  "sourceToolAssistantUUID": "4f4606ba-834f-4763-8641-e9a35acfed55",
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

_source line 33 · 2026-05-16T08:08:02.071Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S79LvwqY3TF9BPcPV8ntL5`</summary>

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
  "parentUuid": "41e385a3-7aa4-47ce-83fe-f147a1f64b57",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uTywpBcnPsk3XXY46J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df535739-32e7-4068-bb7d-2e01f22a47c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcRaYBRQSdzfmnY2bNjijy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11128,
      "cache_read_input_tokens": 53108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11128,
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

_source line 34 · 2026-05-16T08:08:02.095Z_

<details><summary>↩ Tool result · `toolu_01S79LvwqY3TF9BPcPV8ntL5`</summary>

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
  "parentUuid": "df535739-32e7-4068-bb7d-2e01f22a47c3",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "5d57005e-a0cc-4212-ba04-ca0456855329",
  "sourceToolAssistantUUID": "df535739-32e7-4068-bb7d-2e01f22a47c3",
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

_source line 35 · 2026-05-16T08:08:02.402Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NmgkDrcmf9Dyx16WX14Crd`</summary>

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
  "parentUuid": "5d57005e-a0cc-4212-ba04-ca0456855329",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uTywpBcnPsk3XXY46J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88b24fe1-058a-45ab-89d7-0fcff9617a2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcRaYBRQSdzfmnY2bNjijy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11128,
      "cache_read_input_tokens": 53108,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11128
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 53108,
          "cache_creation_input_tokens": 11128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11128,
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

_source line 36 · 2026-05-16T08:08:02.430Z_

<details><summary>↩ Tool result · `toolu_01NmgkDrcmf9Dyx16WX14Crd`</summary>

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
  "parentUuid": "88b24fe1-058a-45ab-89d7-0fcff9617a2e",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "c60f9a36-9d01-43ea-8dfe-f5a483dfdb93",
  "sourceToolAssistantUUID": "88b24fe1-058a-45ab-89d7-0fcff9617a2e",
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

_source line 37 · 2026-05-16T08:08:05.918Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RH3CuU7oBbitWTQTf8FUxo`</summary>

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
  "parentUuid": "c60f9a36-9d01-43ea-8dfe-f5a483dfdb93",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uUJjAoVLue3AYmWph1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "599cbe57-1d5b-48f4-aa8b-3c09f2b01884",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4Nx7GcyW37x49Q6tMoRKj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8486,
      "cache_read_input_tokens": 64236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8486,
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

_source line 38 · 2026-05-16T08:08:05.926Z_

<details><summary>↩ Tool result · `toolu_01RH3CuU7oBbitWTQTf8FUxo`</summary>

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
  "parentUuid": "599cbe57-1d5b-48f4-aa8b-3c09f2b01884",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "c8bd45a8-5aa2-41f1-ac1d-0aa25d476681",
  "sourceToolAssistantUUID": "599cbe57-1d5b-48f4-aa8b-3c09f2b01884",
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

_source line 39 · 2026-05-16T08:08:06.408Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WDFrMSQ767ZrbmV5bFbyXM`</summary>

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
  "parentUuid": "c8bd45a8-5aa2-41f1-ac1d-0aa25d476681",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uUJjAoVLue3AYmWph1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "662b0043-e682-4361-8fcf-059dd1deaf5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4Nx7GcyW37x49Q6tMoRKj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8486,
      "cache_read_input_tokens": 64236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8486,
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

_source line 40 · 2026-05-16T08:08:06.414Z_

<details><summary>↩ Tool result · `toolu_01WDFrMSQ767ZrbmV5bFbyXM`</summary>

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
  "parentUuid": "662b0043-e682-4361-8fcf-059dd1deaf5b",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "85433de9-2704-432e-9aaa-88cc1eb407bb",
  "sourceToolAssistantUUID": "662b0043-e682-4361-8fcf-059dd1deaf5b",
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

_source line 41 · 2026-05-16T08:08:06.949Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WJZAUAqo11VdBTh5N1fJbg`</summary>

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
  "parentUuid": "85433de9-2704-432e-9aaa-88cc1eb407bb",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uUJjAoVLue3AYmWph1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc1606cd-5983-4e4b-8600-cbebafd41888",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4Nx7GcyW37x49Q6tMoRKj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8486,
      "cache_read_input_tokens": 64236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8486,
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

_source line 42 · 2026-05-16T08:08:06.954Z_

<details><summary>↩ Tool result · `toolu_01WJZAUAqo11VdBTh5N1fJbg`</summary>

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
  "parentUuid": "dc1606cd-5983-4e4b-8600-cbebafd41888",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "bdb6bcbe-8c6f-4a56-9b45-78a3fc726b02",
  "sourceToolAssistantUUID": "dc1606cd-5983-4e4b-8600-cbebafd41888",
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

_source line 43 · 2026-05-16T08:08:18.205Z_

Now let me also look at the latest dream review report to understand prior review feedback.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdb6bcbe-8c6f-4a56-9b45-78a3fc726b02",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uUspVVwLxhDKkBdawd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96cb4ef2-7339-4506-b08e-dfc955c375f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2rL5y6yErk6Aa9XfXtaED",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3802,
      "cache_read_input_tokens": 72722,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3802,
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

_source line 44 · 2026-05-16T08:08:19.682Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xnr5hsDr6WLaKsPkakKjZ7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96cb4ef2-7339-4506-b08e-dfc955c375f9",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uUspVVwLxhDKkBdawd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3067044-5ab3-47da-8702-9cc11c2a0159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2rL5y6yErk6Aa9XfXtaED",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3802,
      "cache_read_input_tokens": 72722,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3802,
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

_source line 45 · 2026-05-16T08:08:19.696Z_

<details><summary>↩ Tool result · `toolu_01Xnr5hsDr6WLaKsPkakKjZ7`</summary>

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
51	\end{enumerate}
52	
53	\section{Related Work}
54	
55	\paragraph{Training-Free LLM IE.}
56	Recent work has shown that LLMs can perform IE tasks zero-shot or with minimal demonstrations.
57	GPT-NER \cite{li2023gptner} and GoLLIE \cite{sainz2024gollie} prompt LLMs directly with type definitions.
58	Performance varies widely with schema complexity, but systematic characterization of failure modes has been limited.
59	
60	\paragraph{Schema Decomposition.}
61	UniNER \cite{zhou2024universalner} extracts one entity type per pass, trading cross-type context for reduced confusion.
62	This per-type splitting represents the extreme of schema decomposition.
63	However, no principled criterion exists for when or how to decompose schemas.
64	
65	\paragraph{Confusability in Classification.}
66	The notion that semantically similar categories cause confusion is well-established in cognitive science and fine-grained classification.
67	In NLP, label confusion has been studied in text classification and NER, but not systematically isolated from label set size in the LLM IE setting.
68	
69	\section{Methodology}
70	
71	\subsection{Confusability Measures}
72	
73	\paragraph{Schema Cosine Similarity (SCS).}
74	For a pair of types $(t_i, t_j)$, we compute the cosine similarity between their label embeddings:
75	\begin{equation}
76	\text{SCS}(t_i, t_j) = \frac{\mathbf{e}_i \cdot \mathbf{e}_j}{\|\mathbf{e}_i\| \|\mathbf{e}_j\|}
77	\end{equation}
78	where $\mathbf{e}_i$ is the embedding of type $t_i$'s label text.
79	We use two embedding models: Qwen3-32B (the extraction model itself) and MiniLM-L6-v2 (a generic sentence encoder).
80	
81	\paragraph{Batch Confusability Score (BCS).}
82	For a batch of types $B = \{t_1, \ldots, t_k\}$, BCS is the mean pairwise SCS:
83	\begin{equation}
84	\text{BCS}(B) = \frac{2}{k(k-1)} \sum_{i<j} \text{SCS}(t_i, t_j)
85	\end{equation}
86	BCS captures the overall confusability pressure within a single extraction prompt.
87	
88	\subsection{Experimental Design}
89	
90	We design controlled experiments that vary type count and confusability independently.
91	
92	\paragraph{Count Curves.}
93	For each dataset, we construct batches of increasing size ($k = 1, 4, 8, 16, 32, \ldots$) by sampling types, measuring accuracy as a function of type count.
94	BCS is recorded as a covariate.
95	
96	\paragraph{BCS-Controlled Comparisons.}
97	At fixed type count $k$, we construct matched batch pairs: one with low BCS (dissimilar types) and one with high BCS (confusable types).
98	The accuracy gap $\Delta$ isolates confusability from count.
99	
100	\paragraph{2$\times$2 Factorial Design.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3067044-5ab3-47da-8702-9cc11c2a0159",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "dbd81daf-cf3b-47f2-bfbb-b88ebbea476d",
  "sourceToolAssistantUUID": "e3067044-5ab3-47da-8702-9cc11c2a0159",
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

_source line 46 · 2026-05-16T08:08:20.372Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BfM24UR4TQjkcYvkEiy4qc`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbd81daf-cf3b-47f2-bfbb-b88ebbea476d",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uUspVVwLxhDKkBdawd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20602544-54e0-40d5-a14b-1f8c9b7d878a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2rL5y6yErk6Aa9XfXtaED",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3802,
      "cache_read_input_tokens": 72722,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3802
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 72722,
          "cache_creation_input_tokens": 3802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3802,
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

_source line 47 · 2026-05-16T08:08:20.392Z_

<details><summary>↩ Tool result · `toolu_01BfM24UR4TQjkcYvkEiy4qc`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20602544-54e0-40d5-a14b-1f8c9b7d878a",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "12e26aa9-a0b1-4d44-b06a-4e57e7f6ed03",
  "sourceToolAssistantUUID": "20602544-54e0-40d5-a14b-1f8c9b7d878a",
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

_source line 48 · 2026-05-16T08:08:23.486Z_

Let me also check the writing plan and any additional experiment artifacts for details on methodology.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12e26aa9-a0b1-4d44-b06a-4e57e7f6ed03",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uVdfyPRp6YdETz5H8P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2262338c-95b6-4d81-a586-c4dc4e9bd644",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSBzH46rnaGkZrbUimcLyM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2563,
      "cache_read_input_tokens": 76524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2563,
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

_source line 49 · 2026-05-16T08:08:24.001Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KrYmyDYq99ask82braWqcu`</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2262338c-95b6-4d81-a586-c4dc4e9bd644",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uVdfyPRp6YdETz5H8P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0d070d1-425e-49a6-982b-c1a6f669d71b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSBzH46rnaGkZrbUimcLyM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2563,
      "cache_read_input_tokens": 76524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2563,
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

_source line 50 · 2026-05-16T08:08:24.017Z_

<details><summary>↩ Tool result · `toolu_01KrYmyDYq99ask82braWqcu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/writing_plan.yaml\", \"content\": \"# Writing Plan — schema-dag-extraction\\n# Generated: 2026-05-15\\n# Venue: EMNLP 2026 (ARR May 25 cycle)\\n# Format: 8 pages main text + unlimited references\\n# Mode: Full Draft (2-claim analysis paper + SDGD negative result)\\n\\nmeta:\\n  title: \\\"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\\\"\\n  venue: EMNLP 2026 Main\\n  submission_deadline: \\\"2026-05-25\\\"\\n  page_limit: 8\\n  template: \\\"acl2023\\\"  # ARR uses ACL rolling review LaTeX template\\n  template_note: \\\"No EMNLP 2026 template found locally. Using acl2023.sty (standard ARR template). Worker must download from https://github.com/acl-org/acl-style-files if not available.\\\"\\n  primary_model: \\\"Qwen3-32B-FP8\\\"\\n  secondary_model: \\\"LLaMA-3.1-8B-Instruct (exp-012, D022: 70B→8B cross-scale validation)\\\"\\n  datasets: [\\\"Few-NERD (66 types)\\\", \\\"FewRel (80 relations)\\\", \\\"MAVEN (168 event types)\\\"]\\n\\n# =============================================================================\\n# PAPER OUTLINE\\n# =============================================================================\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 250\\n    dependencies: [introduction, experiments, results, sdgd_negative, conclusion]\\n    key_content:\\n      - Problem: training-free LLM IE degrades on complex schemas; prior work conflates count and confusability\\n      - Method: first controlled empirical study isolating type confusability from count across 3 tasks\\n      - Findings: multi-channel degradation (count→recall, confusability→type confusion); pairwise SCS robust cross-task (r=0.11-0.13); effect amplifies 3.4× with schema complexity; per-type aggregation confounded on homogeneous schemas\\n      - Negative result: naive confusability-aware decomposition fails due to merge amplification\\n      - \\\"Must report r² (~1.5%) and frame as 'one factor among many but first empirically isolated'\\\"\\n\\n  - section: introduction\\n    word_budget: 1200\\n    dependencies: []\\n    key_content:\\n      - Hook: training-free LLM IE enables rapid deployment but degrades 20-60 F1 on complex schemas\\n      - Gap: all prior decomposition approaches (UniNER per-type, LLM-PEE similarity partitioning, PARSE schema rewriting) operate on unvalidated assumptions about WHAT makes schemas complex\\n      - RQ1: Does type confusability independently predict degradation beyond count?\\n      - RQ2: Through what mechanisms do count and confusability degrade performance?\\n      - RQ3: Can confusability-aware decomposition improve extraction? (→ negative result, itself informative)\\n      - Contributions list (4 items): multi-channel model, pairwise robustness + centrality confound, cross-task validation, SDGD negative result identifying merge amplification\\n      - \\\"Address Dream feedback: frame effect size honestly from the start — 'partial but first isolated signal'\\\"\\n    dream_fixes:\\n      - \\\"Effect size contextualization: r=0.11-0.13 explains ~1.5% variance; present as 'one factor among many but first empirically isolated'\\\"\\n      - \\\"Mention LLM-PEE as closest prior work in intro\\\"\\n\\n  - section: related_work\\n    word_budget: 1000\\n    dependencies: [introduction]\\n    key_content:\\n      - \\\"§2.1 Training-Free LLM IE: LLM4IE survey, InstructUIE, UniNER, GoLLIE, GLiNER, KnowCoder, GuideX, ZeroNER, Self-Improve-NER, NuNER\\\"\\n      - \\\"§2.2 Schema Complexity in IE: LLM-PEE (MUST position extensively — similarity partitioning, not confusability-aware), IEPile (hard negatives for training), PARSE, DEE, CrossAgentIE (reactive debate vs proactive decomposition), CMAS-NER, SPT, DLISC, KGGen\\\"\\n      - \\\"§2.3 Representation Degeneration: Gao et al. ICLR 2019, Ethayarajh EMNLP 2019, Cai et al. ICLR 2021 (cluster isotropy — directly explains centrality confound), Godey et al. EACL 2024\\\"\\n      - \\\"§2.4 Context Length Effects: Lost in the Middle (TACL 2024) — first connection to IE schema prompts\\\"\\n    dream_fixes:\\n      - \\\"25+ references required — literature_map has 30+ entries, use all verified\\\"\\n      - \\\"LLM-PEE positioning: discuss similarity partitioning vs confusability-aware decomposition, why no head-to-head (different task focus), our contribution is controlled analysis\\\"\\n      - \\\"CrossAgentIE: reactive debate (post-hoc resolution) vs our proactive decomposition (prevention)\\\"\\n\\n  - section: experimental_setup\\n    word_budget: 900\\n    dependencies: [introduction]\\n    key_content:\\n      - \\\"§3.1 Tasks and Datasets: Few-NERD (NER, 66 types, cross-domain), FewRel (RE, 80 relations, cross-domain), MAVEN (ED, 168 event types, same-domain FrameNet). Dataset statistics table.\\\"\\n      - \\\"§3.2 Schema Confusability Score (SCS): formal definition of pairwise SCS, Batch Confusability Score (BCS). Embedding models: Qwen3-32B hidden states, all-MiniLM-L6-v2.\\\"\\n      - \\\"§3.3 Experimental Design: Exp1 count curve, Exp2 BCS-controlled factorial design. Formal definitions of all evaluation metrics.\\\"\\n      - \\\"§3.4 Evaluation Metrics: F1 (NER, token-level text match), Accuracy (RE, exact label match), Relaxed F1 (ED — FORMAL DEFINITION REQUIRED: trigger word overlap + correct event type). Justify cross-task metric differences.\\\"\\n      - \\\"§3.5 Model and Inference: Qwen3-32B-FP8 via vLLM, prompt template, decoding params.\\\"\\n    dream_fixes:\\n      - \\\"MAVEN 'relaxed F1' must have formal definition in §3.4\\\"\\n      - \\\"Cross-task metric differences must be justified\\\"\\n      - \\\"Sample sizes: 5 batches per count level, 1000 samples, explicitly stated\\\"\\n      - \\\"Bootstrap CI methodology described here\\\"\\n\\n  - section: results\\n    word_budget: 1500\\n    dependencies: [experimental_setup]\\n    key_content:\\n      - \\\"§4.1 Count-Degradation Curves (Exp1): Few-NERD recall 0.72→0.42, FewRel acc 85.7%→50.4%, MAVEN relaxed F1 stable. Fig 1 multi-task count curves.\\\"\\n      - \\\"§4.2 Pairwise Confusability → Type Confusion (Claim 1): Few-NERD r=0.112 [0.076,0.156], MAVEN MiniLM r=0.129 [0.104,0.156]. Report r² throughout. SCS validation (exp-015): Qwen3 ρ=0.168, MiniLM ρ=0.306 nonzero.\\\"\\n      - \\\"§4.3 BCS-Controlled Experiments (Claim 1 continued): FewRel 80-rel Δ=-31.2pp [17.7,42.7]. Scaling 3.4× vs 16-rel. Tab main results.\\\"\\n      - \\\"§4.4 Multi-Channel Degradation (Claim 2): Error taxonomy — IntraSub 0%→49.4% (NER, ρ=1.0), 0%→32.3% (RE, ρ=0.954). Missed rate flat. Fig error taxonomy.\\\"\\n      - \\\"§4.5 Centrality Confound on Homogeneous Schemas: MAVEN per-type positive direction. Explanation via Cai et al. 2021 cluster isotropy. Pairwise still works → aggregation is the problem, not the signal.\\\"\\n      - \\\"All CIs from bootstrap_ci_analysis. Report r² for every correlation.\\\"\\n    dream_fixes:\\n      - \\\"Report r² throughout — r=0.112 → r²=0.013 (~1.3% variance explained)\\\"\\n      - \\\"Discuss other contributing factors: entity frequency, prompt position, type definition quality\\\"\\n      - \\\"Frame confusability as 'one factor among many but first empirically isolated'\\\"\\n      - \\\"Bootstrap CI for all key metrics (already computed)\\\"\\n      - \\\"Sample size limitations: 5 batches per count acknowledged\\\"\\n\\n  - section: sdgd_negative\\n    word_budget: 500\\n    dependencies: [results]\\n    key_content:\\n      - \\\"§5 Why Naive Decomposition Fails: SDGD-zero F1=0.241 vs single-pass 0.445. Decomposition boosts recall (0.19→0.31) but kills precision (0.32→0.21).\\\"\\n      - \\\"Merge amplification mechanism: decomposed batches produce overlapping entity predictions → union merge inflates FP.\\\"\\n      - \\\"Confidence-gated merge (v2) did not help: 0.241 vs 0.251 (v1).\\\"\\n      - \\\"Comparison with random_batch (0.320) and per_type (0.292): ALL decomposition modes worse than single-pass.\\\"\\n      - \\\"Structural insight: merge is the bottleneck, not decomposition quality.\\\"\\n      - \\\"Connection to LLM-PEE: both are similarity-based partitioning; our controlled negative result suggests the merge problem is general.\\\"\\n      - \\\"Future directions: calibration-based approaches, confidence-weighted extraction.\\\"\\n    dream_fixes:\\n      - \\\"SDGD threshold τ=0.8 sensitivity: acknowledge no ablation in limitations\\\"\\n      - \\\"Position relative to LLM-PEE: same fundamental challenge (merge amplification)\\\"\\n\\n  - section: discussion\\n    word_budget: 600\\n    dependencies: [results, sdgd_negative]\\n    key_content:\\n      - \\\"§6.1 Effect Size and Practical Implications: r²≈1.3-1.7% — confusability is one factor among many. Other factors: entity frequency, prompt position effects (Lost in the Middle), type definition quality, model capacity. First empirically isolated signal, not the only one.\\\"\\n      - \\\"§6.2 Embedding Choice: 2×3 ablation matrix summary. No single embedding dominates. Extraction-model embeddings better for cross-domain (Qwen3 on Few-NERD), generic embeddings for same-domain (MiniLM on MAVEN).\\\"\\n      - \\\"§6.3 Limitations: (a) single primary model (Qwen3-32B), LLaMA pending; (b) 5 batches per count level → limited statistical power for factorial ANOVA; (c) SDGD τ=0.8 no ablation; (d) 3 datasets may not cover all IE scenarios; (e) text_match evaluation on NER (not exact span).\\\"\\n    dream_fixes:\\n      - \\\"LLaMA non-monotonicity: if exp-012 done → Patch. If not, acknowledge 'multi-model validation pending' in limitations\\\"\\n      - \\\"Sample size: report CI widths, acknowledge ANOVA power insufficient\\\"\\n      - \\\"SDGD threshold sensitivity acknowledged\\\"\\n\\n  - section: conclusion\\n    word_budget: 250\\n    dependencies: [introduction, results, sdgd_negative, discussion]\\n    key_content:\\n      - Restate multi-channel degradation model\\n      - Pairwise confusability as robust cross-task signal\\n      - Centrality confound as methodological insight\\n      - SDGD negative result → merge amplification → future calibration-based work\\n      - \\\"Tempered claims: 'partial explanatory power' not 'comprehensive model'\\\"\\n\\n# =============================================================================\\n# VISUALIZATION PLAN\\n# =============================================================================\\n\\nvisualization_plan:\\n  - fig_id: fig_count_curves\\n    type: line_plot\\n    tool: matplotlib\\n    description: \\\"Multi-task count-degradation curves. 3 subplots: (a) Few-NERD recall vs count, (b) FewRel accuracy vs count (80-rel), (c) MAVEN relaxed F1 vs count. Error bars from 5 batches per count. X-axis: type/relation count. Y-axis: metric. Shows Channel 1 (count→recall decline).\\\"\\n    placement: \\\"Section 4.1 (Results)\\\"\\n    aspect_ratio: \\\"3:1 (three horizontal subplots)\\\"\\n    data_source: \\\"registry: exp001_count_baseline (Few-NERD), exp_fewrel_formal_80rel (FewRel), exp004_maven_bcs (MAVEN)\\\"\\n    output_path: \\\"projects/schema-dag-extraction/figures/paper/fig_count_curves.pdf\\\"\\n    notes: \\\"Include bootstrap CI as shaded region where available. MAVEN shows non-monotonic pattern — plot honestly.\\\"\\n\\n  - fig_id: fig_error_taxonomy\\n    type: grouped_bar\\n    tool: matplotlib\\n    description: \\\"Error type distribution across BCS bins. 2 subplots: (a) Few-NERD NER, (b) FewRel RE. Stacked/grouped bars showing correct%, wrong_type% (IntraSub%), missed%. BCS bins on x-axis. Shows Channel 2 (confusability→type confusion) and cross-task IntraSub replication.\\\"\\n    placement: \\\"Section 4.4 (Multi-Channel Degradation)\\\"\\n    aspect_ratio: \\\"2:1 (two horizontal subplots)\\\"\\n    data_source: \\\"registry: exp007_error_taxonomy (Few-NERD), exp016_fewrel_error_taxonomy (FewRel)\\\"\\n    output_path: \\\"projects/schema-dag-extraction/figures/paper/fig_error_taxonomy.pdf\\\"\\n    notes: \\\"Highlight IntraSub rate monotonic increase. Include ρ values on plot.\\\"\\n\\n  - fig_id: fig_bcs_scaling\\n    type: grouped_bar\\n    tool: matplotlib\\n    description: \\\"BCS effect scaling with schema complexity. Grouped bar: 16-rel vs 80-rel on FewRel. For each: low-BCS accuracy, high-BCS accuracy, Δ. Shows 3.4× amplification. Include CI error bars.\\\"\\n    placement: \\\"Section 4.3 (BCS-Controlled)\\\"\\n    aspect_ratio: \\\"1:1\\\"\\n    data_source: \\\"registry: exp_fewrel_formal (16-rel), exp_fewrel_formal_80rel (80-rel), bootstrap_ci_analysis\\\"\\n    output_path: \\\"projects/schema-dag-extraction/figures/paper/fig_bcs_scaling.pdf\\\"\\n    notes: \\\"Annotate Δ values and 3.4× amplification factor.\\\"\\n\\n  - fig_id: fig_sdgd_comparison\\n    type: bar_chart\\n    tool: matplotlib\\n    description: \\\"SDGD vs baselines on Few-NERD. Grouped bars showing F1, Precision, Recall for 4 modes: single_pass, random_batch, sdgd_zero, per_type. Clearly shows decomposition boosts recall but kills precision.\\\"\\n    placement: \\\"Section 5 (SDGD Negative Result)\\\"\\n    aspect_ratio: \\\"4:3\\\"\\n    data_source: \\\"registry: exp008_sdgd_zero_fewnerd_r2\\\"\\n    output_path: \\\"projects/schema-dag-extraction/figures/paper/fig_sdgd_comparison.pdf\\\"\\n    notes: \\\"Highlight single_pass as strongest F1. Show precision-recall tradeoff visually.\\\"\\n\\n# =============================================================================\\n# TABLE PLAN\\n# =============================================================================\\n\\ntable_plan:\\n  - table_id: tab_datasets\\n    type: statistics\\n    columns: [Dataset, Task, \\\"# Types\\\", \\\"# Samples\\\", Domain, \\\"SCS Range\\\", Embedding]\\n    data_source: \\\"registry: exp-004 (MAVEN stats), exp001 (Few-NERD), exp_fewrel_formal_80rel (FewRel)\\\"\\n    placement: \\\"Section 3.1\\\"\\n    notes: \\\"Include mean/median/max SCS for each dataset.\\\"\\n\\n  - table_id: tab_pairwise\\n    type: results\\n    columns: [Dataset, Embedding, \\\"n pairs\\\", \\\"Pearson r\\\", \\\"r²\\\", \\\"95% CI\\\", \\\"p-value\\\", \\\"ρ (nonzero)\\\"]\\n    data_source: \\\"registry: exp002_confusability_controlled, exp004_maven_bcs, exp015_scs_validation, bootstrap_ci_analysis\\\"\\n    placement: \\\"Section 4.2\\\"\\n    notes: \\\"MUST include r² column per Dream feedback. All CIs from bootstrap.\\\"\\n\\n  - table_id: tab_bcs_controlled\\n    type: results\\n    columns: [Dataset, \\\"Schema Size\\\", Count, \\\"Low-BCS Acc\\\", \\\"High-BCS Acc\\\", \\\"Δ (pp)\\\", \\\"95% CI\\\"]\\n    data_source: \\\"registry: exp_fewrel_formal, exp_fewrel_formal_80rel, bootstrap_ci_analysis\\\"\\n    placement: \\\"Section 4.3\\\"\\n    notes: \\\"Show 16-rel → 80-rel scaling. Include bootstrap CI for Δ.\\\"\\n\\n  - table_id: tab_error_taxonomy\\n    type: results\\n    columns: [Task, BCS Bin, \\\"Correct%\\\", \\\"IntraSub%\\\", \\\"Missed%\\\", ρ]\\n    data_source: \\\"registry: exp007_error_taxonomy, exp016_fewrel_error_taxonomy\\\"\\n    placement: \\\"Section 4.4\\\"\\n    notes: \\\"Cross-task comparison. Highlight ρ=1.0 (NER) and ρ=0.954 (RE).\\\"\\n\\n  - table_id: tab_sdgd\\n    type: results\\n    columns: [Mode, Batches, F1, Precision, Recall, \\\"Time (s)\\\"]\\n    data_source: \\\"registry: exp008_sdgd_zero_fewnerd_r2\\\"\\n    placement: \\\"Section 5\\\"\\n    notes: \\\"Include single_pass, random_batch, sdgd_zero, per_type. Bold single_pass F1.\\\"\\n\\n# =============================================================================\\n# LITERATURE STRATEGY\\n# =============================================================================\\n\\nliterature_strategy:\\n  citation_budget: 30\\n  macro_context: \\\"Training-free LLM IE is gaining traction for rapid deployment but quality gaps with supervised methods remain poorly understood. We provide the first controlled factor analysis.\\\"\\n\\n  micro_clusters:\\n    - cluster_name: \\\"training_free_llm_ie\\\"\\n      description: \\\"Training-free / zero-shot LLM-based IE methods\\\"\\n      target_count: 8\\n      must_cite:\\n        - uniner-2024      # ICLR 2024, per-type splitting baseline\\n        - gollie-2024       # ICLR 2024, code-style schema\\n        - gliner-2024       # NAACL 2024, non-LLM competitive baseline\\n        - knowcoder-2024    # ACL 2024, code-based schema knowledge\\n        - zeroner-2025      # ACL 2025 Findings\\n        - guidex-2025       # ACL 2025 Findings\\n      search_queries:\\n        - \\\"zero-shot LLM information extraction 2024 2025\\\"\\n        - \\\"training-free named entity recognition large language model\\\"\\n\\n    - cluster_name: \\\"schema_decomposition\\\"\\n      description: \\\"Schema decomposition / complexity management for IE\\\"\\n      target_count: 8\\n      must_cite:\\n        - llm-pee-2025      # CRITICAL: closest competitor, embedding similarity partitioning\\n        - iepile-2024        # ACL 2024, hard-negative schema\\n        - crossagentie-2025  # ACL 2025 Findings, multi-agent type confusion\\n        - kggen-2025         # NeurIPS 2025, two-stage decomposition\\n        - parse-2025         # EMNLP 2025 Industry\\n        - dee-2024           # task-level decomposition\\n      search_queries:\\n        - \\\"schema decomposition information extraction LLM\\\"\\n        - \\\"type confusion resolution information extraction\\\"\\n\\n    - cluster_name: \\\"representation_degeneration\\\"\\n      description: \\\"Embedding anisotropy and representation degeneration literature\\\"\\n      target_count: 5\\n      must_cite:\\n        - gao-repr-degen-2019     # ICLR 2019, foundational\\n        - ethayarajh-contextual-2019  # EMNLP 2019, contextual anisotropy\\n        - cai-isotropy-clusters-2021  # ICLR 2021, cluster isotropy — KEY for centrality confound\\n        - godey-anisotropy-inherent-2024  # EACL 2024\\n      search_queries:\\n        - \\\"embedding anisotropy transformer representation degeneration\\\"\\n\\n    - cluster_name: \\\"context_length_ie\\\"\\n      description: \\\"Context length effects and positional bias\\\"\\n      target_count: 2\\n      must_cite:\\n        - lost-in-middle-2024   # TACL 2024\\n      search_queries:\\n        - \\\"lost in the middle long context language model\\\"\\n\\n    - cluster_name: \\\"ie_surveys_benchmarks\\\"\\n      description: \\\"IE surveys and evaluation methodology\\\"\\n      target_count: 4\\n      must_cite:\\n        - llm4ie-survey-2024    # comprehensive survey\\n        - familiarity-2025      # NAACL 2025, evaluation methodology\\n      search_queries:\\n        - \\\"LLM information extraction survey 2024\\\"\\n        - \\\"NER evaluation methodology zero-shot\\\"\\n\\n    - cluster_name: \\\"instructuie_baselines\\\"\\n      description: \\\"Instruction-tuned universal IE baselines\\\"\\n      target_count: 3\\n      must_cite: []\\n      search_queries:\\n        - \\\"InstructUIE instruction-tuned information extraction\\\"\\n        - \\\"universal information extraction instruction tuning 2024\\\"\\n\\n# =============================================================================\\n# WRITING ORDER (strict serial)\\n# =============================================================================\\n\\nwriting_order:\\n  - section: experimental_setup\\n    rationale: \\\"Establishes methodology, metric definitions, and dataset descriptions. Foundation for all subsequent sections.\\\"\\n    worker_type: paper_writing\\n    worker_inputs:\\n      - \\\"paper_framing.md §Experimental Design\\\"\\n      - \\\"registry: exp001, exp002, exp004, exp_fewrel_formal_80rel (design fields)\\\"\\n      - \\\"latex-paper skill + red-section skill\\\"\\n      - \\\"Dream feedback: formal metric definitions, sample size disclosure\\\"\\n\\n  - section: results\\n    rationale: \\\"Core empirical findings. Depends on experimental_setup for metric definitions.\\\"\\n    worker_type: paper_writing\\n    worker_inputs:\\n      - \\\"experimental_setup.tex (completed)\\\"\\n      - \\\"registry: ALL successful experiments (metrics fields)\\\"\\n      - \\\"bootstrap_ci_analysis (all CIs)\\\"\\n      - \\\"paper_framing.md §Evidence Hierarchy\\\"\\n      - \\\"Dream feedback: r² throughout, effect size contextualization\\\"\\n\\n  - section: sdgd_negative\\n    rationale: \\\"Negative result section. Depends on results for context.\\\"\\n    worker_type: paper_writing\\n    worker_inputs:\\n      - \\\"results.tex (completed)\\\"\\n      - \\\"registry: exp008_sdgd_zero_fewnerd_r2, exp008_sdgd_v2_fewnerd\\\"\\n      - \\\"Dream feedback: SDGD threshold sensitivity, LLM-PEE connection\\\"\\n\\n  - section: related_work\\n    rationale: \\\"Positioned after empirical sections to ensure accurate framing. 25+ refs required.\\\"\\n    worker_type: paper_writing\\n    worker_inputs:\\n      - \\\"introduction.tex (not yet, but outline available)\\\"\\n      - \\\"literature_map.yaml (full)\\\"\\n      - \\\"references.bib (after Step 3)\\\"\\n      - \\\"Dream feedback: LLM-PEE extensive positioning, CrossAgentIE differentiation\\\"\\n\\n  - section: introduction\\n    rationale: \\\"Written after results and related work are stable to ensure accurate claims.\\\"\\n    worker_type: paper_writing\\n    worker_inputs:\\n      - \\\"results.tex + sdgd_negative.tex + related_work.tex (all completed)\\\"\\n      - \\\"paper_framing.md §Story Spine\\\"\\n      - \\\"Dream feedback: honest effect size framing from the start\\\"\\n\\n  - section: conclusion\\n    rationale: \\\"Mirrors introduction. Written after all body sections.\\\"\\n    worker_type: paper_writing\\n    worker_inputs:\\n      - \\\"All completed .tex sections\\\"\\n      - \\\"Dream feedback: tempered claims\\\"\\n\\n  - section: abstract\\n    rationale: \\\"Last to write — summarizes the complete paper.\\\"\\n    worker_type: paper_writing\\n    worker_inputs:\\n      - \\\"All completed .tex sections\\\"\\n      - \\\"Dream feedback: r² in abstract, honest framing\\\"\\n\\n# =============================================================================\\n# DREAM REVIEW ISSUES TRACKING\\n# =============================================================================\\n\\ndream_review_fixes:\\n  - id: DR1\\n    issue: \\\"Related work insufficient (need 25+ refs)\\\"\\n    severity: critical\\n    addressed_in: [related_work]\\n    strategy: \\\"literature_map has 30+ entries. Step 3 will gap-fill and verify all.\\\"\\n\\n  - id: DR2\\n    issue: \\\"Effect size not contextualized (r²~1.5%)\\\"\\n    severity: critical\\n    addressed_in: [abstract, introduction, results, discussion]\\n    strategy: \\\"Report r² everywhere. Frame as 'one factor among many, first empirically isolated'. Discuss other factors in §6.1.\\\"\\n\\n  - id: DR3\\n    issue: \\\"MAVEN relaxed F1 needs formal definition\\\"\\n    severity: major\\n    addressed_in: [experimental_setup]\\n    strategy: \\\"§3.4 formal definition: trigger word overlap (any token overlap) + correct event type.\\\"\\n\\n  - id: DR4\\n    issue: \\\"LLM-PEE positioning missing\\\"\\n    severity: critical\\n    addressed_in: [related_work, sdgd_negative]\\n    strategy: \\\"§2.2 extensive discussion. §5 connection to merge amplification. No head-to-head (different task/eval).\\\"\\n\\n  - id: DR5\\n    issue: \\\"LLaMA count curve non-monotonicity\\\"\\n    severity: major\\n    addressed_in: [discussion]\\n    strategy: \\\"If exp-012 done → Patch. If not → §6.3 acknowledge 'multi-model validation pending'.\\\"\\n\\n  - id: DR6\\n    issue: \\\"Sample size limitations (5 batches per count)\\\"\\n    severity: major\\n    addressed_in: [experimental_setup, discussion]\\n    strategy: \\\"Report bootstrap CI for all metrics. §6.3 acknowledge ANOVA power limitations.\\\"\\n\\n  - id: DR7\\n    issue: \\\"SDGD τ=0.8 no ablation\\\"\\n    severity: minor\\n    addressed_in: [discussion]\\n    strategy: \\\"§6.3 acknowledge. Note that all τ values face merge amplification (structural, not threshold-dependent).\\\"\\n\", \"total_chars\": 22225, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0d070d1-425e-49a6-982b-c1a6f669d71b",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "a5683c11-e6c6-4680-9902-22150ad716c4",
  "sourceToolAssistantUUID": "f0d070d1-425e-49a6-982b-c1a6f669d71b",
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

_source line 51 · 2026-05-16T08:08:24.539Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Fv8d9RooBbLk4nWyvui3uj`</summary>

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
  "parentUuid": "a5683c11-e6c6-4680-9902-22150ad716c4",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uVdfyPRp6YdETz5H8P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f614250-367f-454f-8ad0-be10780d460b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSBzH46rnaGkZrbUimcLyM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2563,
      "cache_read_input_tokens": 76524,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2563
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 215,
          "cache_read_input_tokens": 76524,
          "cache_creation_input_tokens": 2563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2563,
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

_source line 52 · 2026-05-16T08:08:24.549Z_

<details><summary>↩ Tool result · `toolu_01Fv8d9RooBbLk4nWyvui3uj`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'schema-dag-extraction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f614250-367f-454f-8ad0-be10780d460b",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "36c27f9c-3186-422c-b4c7-3a700800fce1",
  "sourceToolAssistantUUID": "3f614250-367f-454f-8ad0-be10780d460b",
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

_source line 53 · 2026-05-16T08:08:27.407Z_

Now let me check one more file to understand the prompt appendix and the literature map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36c27f9c-3186-422c-b4c7-3a700800fce1",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uVwNqV1eh7CMQgcutn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd92e85c-c71f-4ec1-a02a-a3835622d00b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NfsFqmqG66c9wuVjEJ4kM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8187,
      "cache_read_input_tokens": 79087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8187,
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

_source line 54 · 2026-05-16T08:08:28.906Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MYg6HtbfGGHzUdVJLgyGeQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd92e85c-c71f-4ec1-a02a-a3835622d00b",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uVwNqV1eh7CMQgcutn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76320bdb-541d-4fdf-8cba-85f36995ddd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NfsFqmqG66c9wuVjEJ4kM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8187,
      "cache_read_input_tokens": 79087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8187,
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

_source line 55 · 2026-05-16T08:08:28.911Z_

<details><summary>↩ Tool result · `toolu_01MYg6HtbfGGHzUdVJLgyGeQ`</summary>

```text
1	\section{Prompt Templates}
2	\label{sec:appendix_prompts}
3	
4	This appendix reproduces the complete prompt templates used for all three extraction tasks.
5	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
6	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
7	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
8	
9	\medskip\noindent
10	\textbf{Notation.}
11	Placeholders are shown in \texttt{\{braces\}}.
12	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
13	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
14	
15	\subsection{Named Entity Recognition (Few-NERD)}
16	
17	\paragraph{v1 prompt (with character offsets).}
18	
19	\begin{small}
20	\begin{verbatim}
21	Extract all named entities from the following text.
22	Only extract entities of the following types:
23	- {type_1}: {definition_1}
24	- {type_2}: {definition_2}
25	  ...
26	
27	Text: {input_text}
28	
29	Output as JSON: [{"text": "...", "type": "...",
30	                  "start": ..., "end": ...}]
31	\end{verbatim}
32	\end{small}
33	
34	\noindent
35	\textbf{v1 constrained-decoding schema:}
36	\begin{small}
37	\begin{verbatim}
38	{"type": "array",
39	 "items": {"type": "object",
40	   "properties": {
41	     "text":  {"type": "string"},
42	     "type":  {"type": "string",
43	               "enum": [&lt;sorted_types>]},
44	     "start": {"type": "integer"},
45	     "end":   {"type": "integer"}},
46	   "required": ["text","type","start","end"]}}
47	\end{verbatim}
48	\end{small}
49	
50	\paragraph{v2 prompt (text+type only).}
51	
52	\begin{small}
53	\begin{verbatim}
54	Extract all named entities from the following text.
55	Only extract entities of the following types:
56	- {type_1}: {definition_1}
57	- {type_2}: {definition_2}
58	  ...
59	
60	Text: {input_text}
61	\end{verbatim}
62	\end{small}
63	\vspace{-0.5em}
64	\noindent$\triangleright$~\textbf{Added in v2:}
65	\begin{small}
66	\begin{verbatim}
67	Only extract entities that clearly match one of the
68	given types. If no entities of these types exist in
69	the text, output an empty list [].
70	\end{verbatim}
71	\end{small}
72	\vspace{-0.5em}
73	\begin{small}
74	\begin{verbatim}
75	Output as JSON: [{"text": "...", "type": "..."}]
76	\end{verbatim}
77	\end{small}
78	
79	\noindent
80	\textbf{v2 constrained-decoding schema:}
81	\begin{small}
82	\begin{verbatim}
83	{"type": "array",
84	 "items": {"type": "object",
85	   "properties": {
86	     "text": {"type": "string"},
87	     "type": {"type": "string",
88	              "enum": [&lt;sorted_types>]}},
89	   "required": ["text","type"]}}
90	\end{verbatim}
91	\end{small}
92	
93	\paragraph{v1 $\to$ v2 differences (NER).}
94	\begin{enumerate}[leftmargin=*,itemsep=2pt]
95	\item \textbf{Offset fields removed.} The \texttt{start}/\texttt{end} integer fields are dropped from both the natural-language instruction and the JSON schema. In v1, 96.5\% of predicted offsets were hallucinated (\S\ref{sec:model}).
96	\item \textbf{Format constraints added.} Two sentences are appended: (a)~``Only extract entities that clearly match one of the given types'' suppresses spurious predictions; (b)~``If no entities \ldots output an empty list~\texttt{[]}'' provides an explicit empty-output path.
97	\end{enumerate}
98	
99	\subsection{Event Detection (MAVEN)}
100	
101	\paragraph{v1 prompt (with character offsets).}
102	
103	\begin{small}
104	\begin{verbatim}
105	Extract all event triggers from the following text.
106	A trigger is the word or phrase that most clearly
107	expresses the event occurrence. Only extract triggers
108	of the following event types:
109	- {type_1}: {definition_1}
110	- {type_2}: {definition_2}
111	  ...
112	
113	Text: {input_text}
114	
115	Output as JSON: [{"text": "...", "type": "...",
116	                  "start": ..., "end": ...}]
117	\end{verbatim}
118	\end{small}
119	
120	\paragraph{v2 prompt (text+type only).}
121	
122	\begin{small}
123	\begin{verbatim}
124	Extract all event triggers from the following text.
125	A trigger is the word or phrase that most clearly
126	expresses the event occurrence. Only extract triggers
127	of the following event types:
128	- {type_1}: {definition_1}
129	- {type_2}: {definition_2}
130	  ...
131	
132	Text: {input_text}
133	\end{verbatim}
134	\end{small}
135	\vspace{-0.5em}
136	\noindent$\triangleright$~\textbf{Added in v2:}
137	\begin{small}
138	\begin{verbatim}
139	Only extract triggers that clearly match one of the
140	given event types. If no events of these types exist
141	in the text, output an empty list [].
142	\end{verbatim}
143	\end{small}
144	\vspace{-0.5em}
145	\begin{small}
146	\begin{verbatim}
147	Output as JSON: [{"text": "...", "type": "..."}]
148	\end{verbatim}
149	\end{small}
150	
151	\noindent The JSON schemas for ED are identical to the NER schemas above; only the natural-language framing differs (``event triggers'' instead of ``named entities'').
152	
153	\paragraph{v1 $\to$ v2 differences (ED).}
154	Same two changes as NER: offset fields removed, format constraints added.
155	
156	\subsection{Relation Extraction (FewRel)}
157	
158	RE uses only a v2-style prompt (no offset fields are applicable to classification).
159	
160	\paragraph{Prompt.}
161	
162	\begin{small}
163	\begin{verbatim}
164	Given the following sentence and two entities,
165	classify the relation between them.
166	
167	Sentence: "{sentence}"
168	Head entity: "{head_entity}"
169	Tail entity: "{tail_entity}"
170	
171	Candidate relations: {type_1}, {type_2}, ...
172	
173	Output a single JSON object:
174	  {"relation": "&lt;relation_type>"}
175	If none of the candidate relations apply, output:
176	  {"relation": "none"}
177	\end{verbatim}
178	\end{small}
179	
180	\noindent
181	\textbf{Constrained-decoding schema:}
182	\begin{small}
183	\begin{verbatim}
184	{"type": "object",
185	 "properties": {
186	   "relation": {"type": "string",
187	     "enum": [&lt;sorted_types>, "none"]}},
188	 "required": ["relation"]}
189	\end{verbatim}
190	\end{small}
191	
192	\subsection{Type Definitions}
193	\label{sec:appendix_type_defs}
194	
195	All prompts include per-type natural-language definitions sourced from the respective dataset documentation:
196	\begin{itemize}[leftmargin=*,itemsep=2pt]
197	\item \textbf{Few-NERD:} 66 fine-grained entity types with definitions derived from the Few-NERD type ontology \cite{fewnerd-2021}.
198	\item \textbf{MAVEN:} 168 event types with FrameNet-based definitions \cite{maven-2020}.
199	\item \textbf{FewRel:} 80 relation types with Wikidata property descriptions \cite{fewrel-2018}.
200	\end{itemize}
201	
202	\noindent Type definitions are injected as ``\texttt{- \{type\_name\}: \{definition\}}'' lines in alphabetical order. The number of types per prompt varies by experimental condition (count${}= 1, 2, 4, \ldots, 64/80$).
203	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76320bdb-541d-4fdf-8cba-85f36995ddd2",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "550e1759-f2fd-46b8-a64c-932dc7086528",
  "sourceToolAssistantUUID": "76320bdb-541d-4fdf-8cba-85f36995ddd2",
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

_source line 56 · 2026-05-16T08:08:29.386Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Jgkwv4wiRRBTop1UycQpxY`</summary>

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
  "parentUuid": "550e1759-f2fd-46b8-a64c-932dc7086528",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uVwNqV1eh7CMQgcutn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e5bf842-ce35-45df-a8bf-0e224f1ad189",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NfsFqmqG66c9wuVjEJ4kM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8187,
      "cache_read_input_tokens": 79087,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8187
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 200,
          "cache_read_input_tokens": 79087,
          "cache_creation_input_tokens": 8187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8187,
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

_source line 57 · 2026-05-16T08:08:29.400Z_

<details><summary>↩ Tool result · `toolu_01Jgkwv4wiRRBTop1UycQpxY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\", \"content\": \"# Literature Map for schema-dag-extraction\\n# Updated: 2026-05-15\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\n\\n# =============================================================================\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\n# =============================================================================\\n\\n- id: llm-pee-2025\\n  title: \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\"\\n  year: 2025\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2503.02628\\n  role: direct-competitor\\n  relevance_note: >\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\n    Divides candidate types into partitions to reduce prompt length.\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\n\\n- id: parse-2025\\n  title: \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\"\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://arxiv.org/abs/2510.08623\\n  role: direct-competitor\\n  relevance_note: >\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\n    Does NOT model type confusability explicitly.\\n\\n- id: dee-2024\\n  title: \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\"\\n  year: 2024\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2406.01045\\n  role: direct-competitor\\n  relevance_note: >\\n    Decomposes event extraction into detection + argument extraction.\\n    Dynamic schema-aware RAG for augmented prompts.\\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\\n\\n- id: crossagentie-2025\\n  title: \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\\\"\\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.718/\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\\n    + inter-group cross-task debate (NER↔RE mutual refinement).\\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\\n    Must clearly differentiate in paper.\\n\\n- id: dlisc-2025\\n  title: \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\"\\n  year: 2025\\n  venue: arXiv (May 2025)\\n  url: https://arxiv.org/abs/2505.14992\\n  role: direct-competitor\\n  relevance_note: >\\n    Dual-LoRA with Incremental Schema Caching.\\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\\n    Focus on efficiency for on-device LLMs, not confusability analysis.\\n\\n- id: spt-2025\\n  title: \\\"Schema as Parameterized Tools for Universal Information Extraction\\\"\\n  year: 2025\\n  venue: arXiv (June 2025)\\n  url: https://arxiv.org/abs/2506.01276\\n  role: direct-competitor\\n  relevance_note: >\\n    Treats schemas as parameterized tools for LLM tool-calling.\\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\\n    Does not address type confusability.\\n\\n- id: zeroner-2025\\n  title: \\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\"\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.805/\\n  role: direct-competitor\\n  relevance_note: >\\n    Description-driven: LLM supervision → BERT student for unseen types.\\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\\n    Related to how schema semantics affect extraction quality.\\n\\n- id: cmas-ner-2025\\n  title: \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\"\\n  year: 2025\\n  venue: TheWebConf 2025\\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent collective intelligence for zero-shot NER.\\n    Addresses context correlation and indiscriminate demonstration problems.\\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\\n\\n# =============================================================================\\n# METHOD COMPONENTS — techniques we build upon or relate to\\n# =============================================================================\\n\\n- id: uniner-2024\\n  title: \\\"UniversalNER: Targeted Distillation from Large Language Models for Open NER\\\"\\n  authors: [Wenxuan Zhou et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://arxiv.org/abs/2308.03279\\n  role: method-component\\n  relevance_note: >\\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\\n    Important baseline for universal NER and schema-at-scale challenges.\\n\\n- id: gollie-2024\\n  title: \\\"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\\\"\\n  authors: [Oscar Sainz et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://hitz-zentroa.github.io/GoLLIE/\\n  role: method-component\\n  relevance_note: >\\n    Code-style schema definitions + annotation guideline following.\\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\\n    Baseline for guideline-driven schema representation.\\n\\n- id: gliner-2024\\n  title: \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08526\\n  role: method-component\\n  relevance_note: >\\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\\n\\n- id: gliner2-2025\\n  title: \\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2025\\n  venue: EMNLP 2025 Demo\\n  url: https://arxiv.org/abs/2507.18546\\n  role: method-component\\n  relevance_note: >\\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\\n    Schema-driven interface. Shows schema approach scales to multi-task.\\n\\n- id: kggen-2025\\n  title: \\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\"\\n  authors: [Mo et al.]\\n  year: 2025\\n  venue: NeurIPS 2025\\n  url: https://arxiv.org/abs/2502.09956\\n  role: method-component\\n  relevance_note: >\\n    Two-stage decomposition: entities first, then relations.\\n    Entity clustering/deduplication to reduce graph sparsity.\\n    Schema decomposition approach for KG construction.\\n\\n- id: code4uie-2024\\n  title: \\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\"\\n  authors: [Yucan Guo et al.]\\n  year: 2024\\n  venue: NeurIPS 2024 Workshop\\n  url: https://arxiv.org/abs/2311.02962\\n  role: method-component\\n  relevance_note: >\\n    Python class-based schema definitions + RAG for code generation.\\n    Unified code-style schema for all IE tasks.\\n\\n- id: iepile-2024\\n  title: \\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\"\\n  authors: [Guanzheng Chen et al., ZJU NLP]\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2402.14710\\n  role: method-component\\n  relevance_note: >\\n    0.32B token bilingual IE corpus. Hard negative schema construction =\\n    semantically proximate schemas to train type discrimination.\\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\\n    Our contribution is inference-time confusability-aware decomposition (training-free).\\n\\n- id: lost-in-middle-2024\\n  title: \\\"Lost in the Middle: How Language Models Use Long Contexts\\\"\\n  authors: [Nelson F. Liu et al.]\\n  year: 2024\\n  venue: TACL 2024\\n  url: https://arxiv.org/abs/2307.03172\\n  role: method-component\\n  relevance_note: >\\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\\n    Motivates schema decomposition to reduce prompt length.\\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\\n\\n# =============================================================================\\n# ZERO-SHOT NER / RE BASELINES\\n# =============================================================================\\n\\n- id: self-improve-ner-2024\\n  title: \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\"\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08921\\n  role: background\\n  relevance_note: >\\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\\n\\n- id: self-prompting-re-2024\\n  title: \\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\"\\n  year: 2024\\n  venue: EMNLP 2024 Findings\\n  url: https://arxiv.org/abs/2410.01154\\n  role: background\\n  relevance_note: >\\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\\n    Training-free RE baseline.\\n\\n- id: reasoning-ner-2025\\n  title: \\\"A Reasoning Paradigm for Named Entity Recognition\\\"\\n  year: 2025\\n  venue: arXiv (Nov 2025)\\n  url: https://arxiv.org/abs/2511.11978\\n  role: background\\n  relevance_note: >\\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\\n\\n- id: nuner-2024\\n  title: \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\"\\n  authors: [Sergei Bogdanov et al., NuMind]\\n  year: 2024\\n  venue: EMNLP 2024\\n  url: https://arxiv.org/abs/2402.15343\\n  role: background\\n  relevance_note: >\\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\\n\\n# =============================================================================\\n# EVALUATION / BENCHMARKING\\n# =============================================================================\\n\\n- id: familiarity-2025\\n  title: \\\"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\\\"\\n  year: 2025\\n  venue: NAACL 2025\\n  url: https://arxiv.org/abs/2412.10121\\n  role: evaluation\\n  relevance_note: >\\n    \\\"Familiarity\\\" metric for label shift in synthetic NER data.\\n    Zero-shot NER scores overestimated due to train-eval label overlap.\\n    Quantifies semantic similarity between entity types — related to type confusability.\\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\\n\\n- id: guidex-2025\\n  title: \\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\"\\n  authors: [Neil Deshpande et al.]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://arxiv.org/abs/2506.00649\\n  role: evaluation\\n  relevance_note: >\\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\\n\\n# =============================================================================\\n# SURVEYS\\n# =============================================================================\\n\\n- id: llm4ie-survey-2024\\n  title: \\\"Large Language Models for Generative Information Extraction: A Survey\\\"\\n  authors: [Derong Xu et al.]\\n  year: 2024\\n  venue: Frontiers of Computer Science\\n  url: https://arxiv.org/abs/2312.17617\\n  role: background\\n  relevance_note: >\\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\\n\\n- id: knowcoder-2024\\n  title: \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\\\"\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2403.07969\\n  role: background\\n  relevance_note: >\\n    Encodes schema knowledge via code structures into LLM.\\n    Related to code-based schema representation.\\n\\n- id: slot-2025\\n  title: \\\"SLOT: Structuring the Output of Large Language Models\\\"\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://aclanthology.org/2025.emnlp-industry.32.pdf\\n  role: background\\n  relevance_note: >\\n    Decouples output formatting from NL task. Model-agnostic structured output.\\n\\n# =============================================================================\\n# EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\\n# — supports \\\"domain boundary\\\" finding: BCS proxy fails for same-domain schemas\\n# =============================================================================\\n\\n- id: gao-repr-degen-2019\\n  title: \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\"\\n  authors: [Jun Gao, Di He, Hang Li, Xin Jiang]\\n  year: 2019\\n  venue: ICLR 2019\\n  url: https://arxiv.org/abs/1907.12009\\n  role: theoretical-foundation\\n  relevance_note: >\\n    FOUNDATIONAL. Shows that likelihood maximization + weight tying causes word embeddings\\n    to degenerate into a narrow cone with uniformly high cosine similarity.\\n    Proposed cosine regularization (MLE-CosReg) to widen the cone aperture.\\n    LINK TO OUR WORK: This is the root mechanism behind BCS compression.\\n    When Qwen3-32B encodes 168 same-domain FrameNet types, the degeneration effect\\n    concentrates them into the same narrow cone (cosine ≥ 0.90), destroying BCS discriminability.\\n    Cite as the theoretical explanation for why embedding-based confusability proxies\\n    have a principled failure mode on semantically homogeneous schemas.\\n\\n- id: ethayarajh-contextual-2019\\n  title: \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\"\\n  authors: [Kawin Ethayarajh]\\n  year: 2019\\n  venue: EMNLP 2019\\n  url: https://aclanthology.org/D19-1006/\\n  role: theoretical-foundation\\n  relevance_note: >\\n    Shows contextualized representations are anisotropic in ALL layers of BERT/ELMo/GPT-2.\\n    Upper layers are more context-specific but still not isotropic.\\n    Introduces quantitative measures of anisotropy (avg cosine sim of random word pairs).\\n    LINK TO OUR WORK: Establishes that anisotropy is pervasive across architectures —\\n    our MAVEN embedding compression is not a Qwen-specific artifact but a general property.\\n    Supports the argument that ANY embedding-based confusability proxy inherits this limitation.\\n\\n- id: cai-isotropy-clusters-2021\\n  title: \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\"\\n  authors: [Xingyu Cai, Jiaji Huang, Yuchen Bian, Kenneth Church]\\n  year: 2021\\n  venue: ICLR 2021\\n  url: https://openreview.net/forum?id=xYGNO86OWDH\\n  role: theoretical-foundation\\n  relevance_note: >\\n    ⭐ MOST DIRECTLY RELEVANT. Key insight: global anisotropy is caused by isolated clusters;\\n    WITHIN each cluster, embeddings are locally more isotropic.\\n    Resolution: the high average cosine similarity reported in prior work is an artifact of\\n    mixing embeddings from different clusters — within-cluster geometry is better behaved.\\n    LINK TO OUR WORK: This is the exact mechanism for our \\\"domain boundary\\\" finding.\\n    Cross-domain schemas (ACE vs FewNERD) span DIFFERENT clusters → BCS captures real\\n    inter-cluster distances → proxy works. Same-domain schemas (MAVEN FrameNet types)\\n    fall within ONE cluster → within-cluster variance is low → cosine sim saturates ≥ 0.90\\n    → BCS loses discriminability. Our empirical finding is a direct instantiation of their\\n    theoretical framework applied to type-level (not token-level) embeddings.\\n\\n- id: godey-anisotropy-inherent-2024\\n  title: \\\"Anisotropy Is Inherent to Self-Attention in Transformers\\\"\\n  authors: [Nathan Godey, Éric de la Clergerie, Benoît Sagot]\\n  year: 2024\\n  venue: EACL 2024\\n  url: https://aclanthology.org/2024.eacl-long.3/\\n  role: theoretical-foundation\\n  relevance_note: >\\n    Proves anisotropy is inherent to the self-attention mechanism itself, not just a\\n    consequence of cross-entropy training on long-tailed token distributions.\\n    Observed across modalities (NLP, vision), ruling out data-distribution explanations.\\n    LINK TO OUR WORK: Strengthens the argument that BCS compression is a fundamental\\n    architectural limitation, not fixable by better prompting or model choice.\\n    Supports our position that structural decomposition (SDGD) is necessary precisely\\n    because the embedding space has inherent geometric constraints.\\n\\n- id: rajaee-cluster-isotropy-2021\\n  title: \\\"A Cluster-based Approach for Improving Isotropy in Contextual Embedding Space\\\"\\n  authors: [Sara Rajaee, Mohammad Taher Pilehvar]\\n  year: 2021\\n  venue: ACL 2021\\n  url: https://aclanthology.org/2021.acl-short.73/\\n  role: theoretical-foundation\\n  relevance_note: >\\n    Shows local (within-cluster) assessment of isotropy is more accurate than global assessment.\\n    Cluster-specific dominant directions encode structural (not semantic) information;\\n    removing them improves semantic task performance.\\n    LINK TO OUR WORK: Supports that within a semantic domain (one cluster), the dominant\\n    directions capture domain-level features rather than fine-grained type distinctions.\\n    This explains why MAVEN type embeddings are compressed: the shared \\\"event-ness\\\"\\n    dominates over type-specific semantics in the local embedding geometry.\\n\\n# =============================================================================\\n# NOVELTY THREAT ASSESSMENT (2026-05-15)\\n# =============================================================================\\n#\\n# 1. \\\"Type count vs type confusability\\\" disentangling:\\n#    ✅ NOVELTY SAFE — No prior work explicitly disentangles these two factors.\\n#    - IEPILE hard negatives: closest, but for training, not inference-time decomposition.\\n#    - Familiarity metric: measures label similarity for evaluation bias, not extraction.\\n#    - CROSSAGENTIE: resolves type confusion via debate, doesn't model as degradation channel.\\n#    Our multi-channel degradation model (count + confusability + context) is novel.\\n#\\n# 2. Schema decomposition baselines to compare:\\n#    - LLM-PEE (similarity partitioning) — MUST compare\\n#    - PARSE (LLM-driven schema rewriting) — MUST compare\\n#    - DEE (task-level decomposition) — discuss in related work\\n#    - SPT (schema as tools) — discuss in related work\\n#    - DLISC (Dual-LoRA schema caching) — discuss in related work\\n#\\n# 3. \\\"Lost in the Middle\\\" for IE:\\n#    ✅ OPPORTUNITY — No follow-up work applying it to IE task found.\\n#    We can be first to connect positional bias to schema prompt design.\\n#\\n# 4. Multi-agent approaches (CROSSAGENTIE, CMAS):\\n#    Growing area. Position clearly: we reduce confusion proactively via decomposition,\\n#    they resolve it reactively via debate. Complementary, not conflicting.\\n#\\n# 5. Overall novelty position:\\n#    STRONG — no prior work proposes (a) a formal multi-channel degradation model for\\n#    schema complexity in LLM IE, or (b) a DAG-based schema decomposition optimized\\n#    for type confusability. Main risk is CROSSAGENTIE's cross-type debate framing.\\n\", \"total_chars\": 18972, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e5bf842-ce35-45df-a8bf-0e224f1ad189",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "ae5cc71a-1139-4672-bc59-0efc07bbd55a",
  "sourceToolAssistantUUID": "8e5bf842-ce35-45df-a8bf-0e224f1ad189",
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

_source line 58 · 2026-05-16T08:08:32.723Z_

Now I have a thorough understanding of the paper, experiments, decisions, and project history. Let me also check the checklist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae5cc71a-1139-4672-bc59-0efc07bbd55a",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uWJ2ZBf7Puc4PDQK8h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2cb7c849-231a-4cc6-8eca-327672959b3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015g46pPBJUd8XN1WDc8Wx24",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9176,
      "cache_read_input_tokens": 87274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9176,
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

_source line 59 · 2026-05-16T08:08:34.301Z_

<details open><summary>🔧 Tool call — Read · `toolu_014REHDnKYSah9StcVNJ6nzG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cb7c849-231a-4cc6-8eca-327672959b3d",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uWJ2ZBf7Puc4PDQK8h",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21f56db2-cacd-445b-b7e7-6184c76a5915",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015g46pPBJUd8XN1WDc8Wx24",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9176,
      "cache_read_input_tokens": 87274,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9176
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 116,
          "cache_read_input_tokens": 87274,
          "cache_creation_input_tokens": 9176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9176,
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

_source line 60 · 2026-05-16T08:08:34.307Z_

<details><summary>↩ Tool result · `toolu_014REHDnKYSah9StcVNJ6nzG`</summary>

```text
1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, non-significant factorial results, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model replication, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. An AI coding assistant was used for experiment scripting and LaTeX formatting. All scientific claims, experimental design, and analysis were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct, vLLM \cite{vllm-2023}, and all-MiniLM-L6-v2 \cite{minilm-2020} are cited in \S\ref{sec:datasets} and \S\ref{sec:model}.
34	
35	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}
36	
37	Yes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Models are used under their respective open-weight licenses.
38	
39	\item \textbf{Did you discuss if your use of existing artifacts is consistent with their intended use?}
40	
41	Yes. All datasets are used for their intended purpose (IE evaluation). No data is used outside the scope specified by the dataset creators.
42	
43	\item \textbf{Did you discuss whether the data contains personally identifiable information or offensive content?}
44	
45	N/A. We use established benchmarks that have been vetted by the research community. No new data collection or annotation was performed.
46	
47	\item \textbf{Did you provide documentation of the artifacts, e.g., coverage of languages, coverage of domains, etc.?}
48	
49	Yes. Table~\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \S\ref{sec:datasets} describes dataset provenance and sampling procedures.
50	
51	\item \textbf{Did you report relevant statistics for your dataset(s)?}
52	
53	Yes. \S\ref{sec:datasets} and Table~\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \S\ref{sec:exp_design}.
54	
55	\end{enumerate}
56	
57	\subsection*{C \quad Computational Experiments}
58	
59	\begin{enumerate}[label=\textbf{C\arabic*.},leftmargin=*,itemsep=4pt]
60	
61	\item \textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}
62	
63	Yes. \S\ref{sec:model}: Qwen3-32B (32B parameters, FP8) and Meta-Llama-3.1-8B-Instruct (8B parameters). Inference was conducted on a single RTX PRO 6000 Blackwell GPU (96\,GB) served via vLLM. Total compute was approximately 48 GPU-hours of inference (no training).
64	
65	\item \textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}
66	
67	Yes. \S\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \S\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.
68	
69	\item \textbf{Did you report descriptive statistics about your results?}
70	
71	Yes. All key metrics include 95\% bootstrap confidence intervals (1{,}000 resamples, percentile method) as stated in \S\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \S\ref{sec:count_curves}--\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.
72	
73	\item \textbf{Did you report implementation details, e.g., versions of packages?}
74	
75	Yes. \S\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\S\ref{sec:scs}). Code and scripts will be released upon acceptance.
76	
77	\end{enumerate}
78	
79	\subsection*{D \quad Human Annotators or Crowdworkers}
80	
81	\begin{enumerate}[label=\textbf{D\arabic*.},leftmargin=*,itemsep=4pt]
82	
83	\item \textbf{Did you report the full text of instructions given to participants?}
84	
85	N/A. No human annotation or crowdsourcing was conducted.
86	
87	\item \textbf{Did you report information about how you recruited and paid participants?}
88	
89	N/A.
90	
91	\item \textbf{Did you discuss whether and how consent was obtained?}
92	
93	N/A.
94	
95	\item \textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}
96	
97	N/A.
98	
99	\item \textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}
100	
101	N/A.
102	
103	\end{enumerate}
104	
105	\subsection*{E \quad AI-Assisted Research}
106	
107	\begin{enumerate}[label=\textbf{E\arabic*.},leftmargin=*,itemsep=4pt]
108	
109	\item \textbf{Did you report the use of AI assistants?}
110	
111	Yes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.
112	
113	\end{enumerate}
114	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21f56db2-cacd-445b-b7e7-6184c76a5915",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "758808f6-d059-473e-901e-2dd425ee4a61",
  "sourceToolAssistantUUID": "21f56db2-cacd-445b-b7e7-6184c76a5915",
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

_source line 61 · 2026-05-16T08:08:36.384Z_

Now I have a comprehensive understanding of the paper. Let me submit my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "758808f6-d059-473e-901e-2dd425ee4a61",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uWeuv28BFUHVkfk3ff",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eaeb8705-71f6-4aba-9a09-062c6d41a026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQEtKSURGeR2ob8dWpYQuD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2156,
      "cache_read_input_tokens": 96450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2156,
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

_source line 62 · 2026-05-16T08:08:37.006Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011qkR2u2V9opUT72UkpRcdN`</summary>

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
  "parentUuid": "eaeb8705-71f6-4aba-9a09-062c6d41a026",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uWeuv28BFUHVkfk3ff",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d087f4e-0b53-4169-8038-01821c33656f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQEtKSURGeR2ob8dWpYQuD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2156,
      "cache_read_input_tokens": 96450,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2156
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 96450,
          "cache_creation_input_tokens": 2156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2156,
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

_source line 63 · 2026-05-16T08:08:37.012Z_

<details><summary>↩ Tool result · `toolu_011qkR2u2V9opUT72UkpRcdN`</summary>

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
  "parentUuid": "1d087f4e-0b53-4169-8038-01821c33656f",
  "isSidechain": true,
  "promptId": "5e3c1bc2-a17c-499d-96b5-856b1442b20f",
  "agentId": "ac64c321a19c91108",
  "type": "user",
  "uuid": "0d3c82e8-15d6-49ce-949c-a7b2ca64c8f5",
  "sourceToolAssistantUUID": "1d087f4e-0b53-4169-8038-01821c33656f",
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

_source line 64 · 2026-05-16T08:10:17.908Z_



## R1: Methods and Experiments

### Summary
This paper conducts a controlled empirical study isolating type count from type confusability as independent predictors of extraction quality degradation in training-free LLM IE across NER, RE, and ED. The experimental design is generally sound, with count curves and BCS-controlled comparisons providing complementary evidence. However, the paper's central quantitative claims rest on modest effect sizes (r^2 = 1.3-1.7%), and several methodological choices -- single extreme batches without CIs for key comparisons, inconsistent metrics across tasks, and a single primary model -- limit the strength of the conclusions. The SDGD negative result is honestly reported but the evaluation is incomplete. The paper is at its strongest when presenting the multi-channel error taxonomy and weakest when claiming practical significance from the pairwise correlations.

### Strengths

- S1: **Well-designed controlled experiments.** The two-paradigm approach (count curves + BCS-controlled) is a clean experimental design that isolates the variables of interest. The within-pool comparison (Table 5, drawing 16-type subsets from the 80-type pool) is a particularly thoughtful control for pool composition confounds, and the permutation test for slope equivalence (p=0.60) is the right statistical tool.

- S2: **Honest and transparent reporting of effect sizes.** The paper reports r^2 = 1.3-1.7% prominently, acknowledges that ~98% of variance is unexplained, and frames confusability as "one factor among many but the first empirically isolated." This level of transparency about modest effects is commendable and appropriate. The paper also honestly reports nonzero-only correlations with the caveat about conditioning on the dependent variable.

- S3: **Cross-task error taxonomy is compelling.** The IntraSub monotonic scaling with BCS (rho=1.0 for NER, rho=0.954 for RE) across 148-154 batches is the paper's strongest evidence for the confusability channel. The observation that 100% of type confusion is intra-batch is mechanistically informative. The NER vs RE divergence on missed-entity rates (NER: 43-65% non-monotonic; RE: 10-16% flat) reveals genuine task-dependent structure.

- S4: **Centrality confound is a genuine methodological contribution.** Identifying that per-type BCS aggregation conflates confusability with centrality on homogeneous schemas (MAVEN), with residualized analysis confirming the positive correlation vanishes under control (p>0.2), is a useful finding that has implications beyond this paper.

- S5: **Comprehensive prompt sensitivity analysis.** Testing v1 vs v2 prompts with n=25 batches on RE (Delta=-25.5pp, r=-0.919, p<0.0001) and explaining the earlier n=5 non-significance as underpowered is good scientific practice. This addresses a key confound (prompt artifact) convincingly for RE.

- S6: **SDGD negative result is valuable.** The merge amplification diagnosis -- decomposition boosts recall but devastates precision, and confidence gating does not fix this -- is an informative negative finding that should save future researchers from repeating this approach blindly.

- S7: **Cross-model replication on RE.** The LLaMA-3.1-8B replication on FewRel showing Delta=-27.1pp (87% of Qwen3's effect) and the striking convergence of high-BCS accuracy to ~51% across both models is strong evidence for task-inherent difficulty rather than model-specific artifacts.

### Weaknesses

- W1: **16-rel BCS-controlled comparison lacks confidence intervals.** Table 3 reports the 16-rel extreme-batch gap as -9.1pp from a single low-BCS and single high-BCS batch, with no CI. This is a critical data point for the amplification narrative (9.1pp vs 31.2pp = "3.4x"), yet it has zero statistical uncertainty quantification. The within-pool analysis (Table 5) partially addresses this with 100 random subsets, but the extreme-batch comparison that anchors the headline claim is unreplicated. The paper later acknowledges this in Table 3's caption ("single extreme batch per level; bootstrap CIs require multiple batches") but still uses 9.1pp as a headline number in the introduction. The 3.4x amplification claim should either be dropped or replaced with a CI-backed comparison (e.g., the quartile Delta of -5.31pp vs -3.92pp from Table 5, which would give a ratio closer to 1.4x and much less impressive).

- W2: **Inconsistent metrics across tasks undermine cross-task claims.** NER uses text-match F1, RE uses accuracy, and ED uses relaxed F1. These metrics have fundamentally different sensitivity profiles. The paper claims "two degradation channels" operate across tasks, but comparing recall decline in NER (where over-prediction inflates baselines) with accuracy decline in RE (closed-set classification) with relaxed F1 increase in MAVEN (where more types improve matching) is comparing apples, oranges, and bananas. The MAVEN "reversal" (F1 increases with count) may simply reflect that relaxed F1 with token overlap is a fundamentally different evaluation regime, not a genuine mechanistic difference. The paper should discuss more carefully whether the cross-task generalization claim is warranted given these metric disparities.

- W3: **Pairwise r=0.11-0.13 is too small to be actionable.** While statistically significant due to large n (1953 and 11026 pairs), r^2=1.3-1.7% means SCS is essentially a noise variable for practical schema design. The paper attempts to bridge this with the batch-level 31.2pp gap, but this is an extreme-batch comparison (lowest vs highest BCS) that is not representative. The practical magnitude section (Section 4.3) honestly reports that the typical gap is 2.2pp (IQR span) or 3.9pp (quartile comparison). A 2-4pp accuracy difference for RE classification may not justify the complexity of confusability-aware schema management in practice. The paper should discuss this practical limitation more explicitly in the main text rather than relegating it to one paragraph.

- W4: **BCS definition instability undermines confidence.** The decision log reveals that BCS was computed as MAX pairwise SCS in some experiments but MEAN in others (D038-D039), requiring retrospective recalculation. The paper settles on MEAN but reports MAX as a sensitivity analysis. The fact that the 80-pool slope flips sign under MEAN (from negative to +0.221, non-significant) while the 16-rel slope remains significant (-0.509) raises concerns about whether BCS captures a stable underlying phenomenon or is sensitive to range and aggregation choices. The BCS IQR for 80-rel is only 0.033, essentially no variation, which makes the full 80-rel row in Table 5 uninterpretable as the paper acknowledges. This fragility should be discussed more prominently.

- W5: **FewRel evaluation design conflates train/val splits.** The paper combines FewRel training and validation splits to obtain 80 relation types. This means evaluation instances are drawn from training data, not held-out data. While the task is zero-shot LLM prompting (no fine-tuning on FewRel), training examples may differ in difficulty distribution from validation examples. The paper acknowledges this in Limitations but does not assess whether the BCS effect differs across splits.

- W6: **No pairwise analysis on FewRel/DocRED.** The paper omits FewRel from pairwise SCS-confusion analysis because "RE is a per-instance classification task where each sample maps to exactly one relation, so the directional confusion matrix is not directly comparable." But a confusion matrix IS computable for classification -- each instance's gold relation vs predicted relation gives exactly the directional confusion needed. This omission weakens the cross-task pairwise claim (currently only NER and ED, not RE). The BCS-controlled experiments on FewRel are a different type of evidence (batch-level, not pair-level).

- W7: **SDGD evaluation is incomplete and potentially unfair.** (a) Only one threshold tau is used (tau=0.8 implied from SDGD protocol, never explicitly stated in the paper). (b) Only one dataset (Few-NERD) is tested. (c) The "per-type" baseline runs 66 sequential passes, an absurdly expensive configuration that no practitioner would use. (d) The v2 confidence-gated merge reduces batches from 8 to 4 by merging small groups, changing two variables simultaneously (merge strategy and batch count). (e) The RE batch composition experiment (Section 5) uses oracle routing (each sample goes to the batch containing its gold type), which is unavailable at inference time and makes the +1.4pp gain vacuously dependent on gold labels. The paper's caption acknowledges the non-significance, but positioning this as a "directional positive" for RE alongside a "failure" for NER overstates the evidence.

- W8: **MAVEN count curve interpretation is post-hoc.** The MAVEN reversal (relaxed F1 increases with count) contradicts the count-channel hypothesis. The paper offers three post-hoc explanations (relaxed matching, same-domain hierarchy, class imbalance) but tests none of them. For instance, if the relaxed matching is the cause, switching to exact-match F1 should recover the decline. If same-domain hierarchy is the cause, the effect should disappear on a cross-domain ED dataset. Without these tests, MAVEN is essentially a counterexample to Channel 1 that is explained away rather than investigated.

- W9: **Greedy decoding with a single seed limits generalizability.** All experiments use temperature=0 and seed=42. While this ensures reproducibility, it means every result is a point estimate from a single decoding trajectory. At temperature=0, the model's behavior is deterministic conditional on the prompt, so the "5 random batches per count level" captures schema variability but NOT model stochasticity. If a different seed or temperature=0.1 changed the results meaningfully, the conclusions would be fragile. At minimum, a sensitivity analysis over 2-3 seeds should be included.

- W10: **The 2x2 factorial analysis is underpowered and inconclusive.** The interaction test (z=-0.667, p=0.505) is correctly reported as non-significant but then used to argue for "additive/orthogonal channels." The paper states this is "likely underpowered due to BCS range compression in high-count schemas," which is exactly the problem -- an underpowered test cannot distinguish additivity from low power to detect interaction. The paper should not cite this as evidence for orthogonality; the Appendix placement is appropriate but the claim of "orthogonal channels" in the abstract/title should be tempered.

### Questions for Authors

- Q1: The 16-rel extreme-batch gap of 9.1pp is from a single batch per BCS level. What is the expected variability of this estimate? Would running 25 random batches (as you did for the within-pool analysis) potentially show this gap is not significant?

- Q2: Why was pairwise confusion analysis omitted for FewRel? A K-class confusion matrix from classification provides exactly the directional confusion counts needed. This seems like a straightforward analysis that would substantially strengthen the cross-task pairwise claim.

- Q3: For the RE batch composition experiment (Table 7), what happens without oracle routing -- i.e., when each instance is sent to ALL batches and predictions are merged (as in the NER SDGD protocol)? Does the +1.4pp gain survive, or does merge amplification destroy it as in NER?

- Q4: The high-BCS accuracy floor of ~51% appears on both Qwen3-32B and LLaMA-3.1-8B. Is this close to the expected random baseline for 80-class classification (1/80 = 1.25%) or does it reflect some other ceiling? What does the confusion matrix look like at this floor -- is the model systematically predicting a few dominant relations?

- Q5: SCS uses only type name strings. Many FewRel relations have distinctive names (e.g., "country of citizenship" vs "publication date") but could have similar descriptions. Would SCS computed on type descriptions change the correlation structure? Have you tested SCS on definitions rather than names?

- Q6: For the MAVEN reversal, have you computed exact-match F1 (requiring exact span match) in addition to relaxed F1? If the reversal disappears under exact match, it would support your explanation (iii) about relaxed matching; if it persists, the reversal has a deeper explanation.

### Missing Experiments / Suggestions

- **FewRel pairwise confusion analysis.** Computing SCS-confusion correlation on the FewRel 80-class confusion matrix would close the gap in cross-task pairwise evidence and is trivially derivable from existing predictions.

- **Multiple decoding seeds.** Running the key BCS-controlled experiments with 2-3 additional seeds (or temperature=0.1) would establish whether conclusions are robust to model stochasticity, not just schema variability.

- **MAVEN exact-match F1.** Reporting both relaxed and exact-match F1 for MAVEN would disambiguate whether the count-curve reversal is a metric artifact or a genuine mechanistic difference.

- **SDGD threshold sensitivity.** Even a brief 3-point sweep (tau in {0.6, 0.8, 0.95}) on Few-NERD would show whether merge amplification is threshold-invariant as claimed.

- **DocRED pairwise analysis.** Given that DocRED shows the steepest BCS slope (-0.71), adding it to the pairwise correlation table (Table 2) would strengthen the evidence hierarchy.

- **Second model on MAVEN.** The centrality confound analysis is currently single-model (both embeddings but one extraction model). Confirming the MAVEN reversal on LLaMA-8B would strengthen the case that it is task-structural rather than model-specific.

### Preliminary Score: 4/6
### Confidence: 4/5

The paper addresses a well-motivated question with a generally sound experimental design, and the error taxonomy analysis (IntraSub scaling) and centrality confound identification are genuine contributions. The cross-model replication on RE and prompt sensitivity analysis are strengths. However, the modest pairwise effect sizes (r^2 < 2%), the single-batch 16-rel comparison anchoring the amplification claim, the missing pairwise analysis on RE, the incomplete SDGD evaluation (oracle routing, single threshold, single dataset), and the unexplored MAVEN reversal are substantive gaps. The paper is above average in transparency and below average in experimental completeness for the claims made. With the FewRel pairwise analysis, proper CIs on the 16-rel comparison, and a more tempered amplification narrative, this would be a solid contribution. In its current form, it is a borderline paper that contributes useful diagnostic insights but overclaims on some headline numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d3c82e8-15d6-49ce-949c-a7b2ca64c8f5",
  "isSidechain": true,
  "agentId": "ac64c321a19c91108",
  "requestId": "req_011Cb5uWrVBb9AmYR4NjHcLL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f97c59c4-ca8a-42ce-a444-46bd347e7412",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "08b36851-eb50-4863-8dbd-f6e8edd972e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CFAsQHjfcNfc1jWu3PXsY3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 98606,
      "output_tokens": 3577,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 786
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3577,
          "cache_read_input_tokens": 98606,
          "cache_creation_input_tokens": 786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 786,
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
