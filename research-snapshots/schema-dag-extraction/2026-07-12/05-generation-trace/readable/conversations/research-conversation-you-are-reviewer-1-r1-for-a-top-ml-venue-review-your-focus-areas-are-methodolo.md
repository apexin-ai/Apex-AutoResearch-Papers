# Research conversation: You are Reviewer 1 (R1) for a top ML venue review. Your focus areas are **methodology** and **experiments**. Use a 6-poi

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 1
- **Tool calls:** 27
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a1d69f340e08c49a0.jsonl`
- **Structured JSON:** [`1fb7181cac5cfaa4007a.json`](../../sessions/1f/1fb7181cac5cfaa4007a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

65 recorded events

### User

_source line 1 · 2026-05-16T08:18:02.903Z_

You are Reviewer 1 (R1) for a top ML venue review. Your focus areas are **methodology** and **experiments**. Use a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept. Target acceptance rate ~25%.

## Paper Summary
Title: "Characterizing and Diagnosing Schema-Induced Failure Modes in Training-Free LLM Information Extraction"

The paper proposes a diagnostic framework for understanding why training-free LLM IE degrades on complex schemas. It identifies two "orthogonal" degradation channels: (1) type count→recall loss via attention dilution, (2) type confusability→substitution errors via semantic interference. It introduces Schema Confusability Score (SCS, cosine similarity of type embeddings), an error taxonomy (IntraSub/ExtraSub/Boundary/Hallucination), and Schema-DAG Guided Decomposition (SDGD). Main findings: error taxonomy shows IntraSub correlates with BCS (ρ=1.0 NER, ρ=0.954 RE); SCS is a weak proxy for empirical confusion (R²=3-9%); SDGD fails across all configs—single-pass > random batching > SDGD.

## Key Experimental Results to Evaluate

**1. DocRED Confusability Study (Section 4.1)**
- Count curve: 0.82→0.31 accuracy as types increase 1→96
- BCS effect at count=16: Δ=−8.3pp but CI crosses zero [−16.1, +0.5]
- Pearson r=−0.22 (p=0.14), Spearman ρ=−0.19 (p=0.21) — NOT significant
- Only n=5 batches per condition

**2. 2×2 Interaction (Section 4.2)**
- {low count(6), high count(12)} × {low BCS, high BCS} on Few-NERD
- Interaction z=−0.67, p=0.50 — NOT significant
- BCS range limited (0.79–0.87), count span small (6 vs 12)
- Cell means: 0.33/0.31/0.32/0.28

**3. Error Taxonomy (Section 4.3)**
- IntraSub: 0%→49.4% as BCS increases (zero→high bin)
- Cross-task ρ=1.0 (NER, 4 bins), ρ=0.954 (RE, 5 bins)
- Only 4 BCS bins; thresholds appear post-hoc

**4. SCS Validation (Section 4.4)**
- All pairs: ρ=0.168 (Qwen3), ρ=0.144 (MiniLM), R²=2.1-2.8%
- Nonzero only: ρ=0.272-0.306, R²=7.4-9.4%
- n=1953 all pairs, n=216 nonzero only

**5. SDGD-zero on MAVEN (Section 4.5)**
- Single-pass F1=0.245 > Random(k=12) 0.178 > SDGD-zero 0.152 > Per-type 0.135
- Merge amplification factor 3.2×

**6. SDGD-cal on Few-NERD (Section 4.6)**
- SDGD-cal F1=0.268 vs SDGD-zero 0.241 (+2.7pp) vs single-pass 0.445
- Calibration matrix 94% sparse (10 examples, 66 types)

**7. SDGD-cal on MAVEN (Section 4.7)**
- SDGD-cal F1=0.161 vs SDGD-zero 0.152 (+0.9pp) vs single-pass 0.245
- 15,620 API calls (22× single-pass)

**8. Random vs SDGD Ablation (Section 4.8)**
- Random consistently > SDGD-zero at matched k (p=0.03)
- SDGD batch size σ_b=5.7-8.3 vs random 0.9-1.2

**9. Per-type Splitting (Section 4.9)**
- Recall=0.586 (highest) but precision=0.194, merge conflict rate 34%

**10. Experimental design context** (from planned experiments):
- All experiments use Qwen3-32B only (single model)
- Few-NERD (66 NER types), DocRED (96 RE types), MAVEN (168 ED types)
- DocRED n=5 batches per condition is very low
- 2×2 design: only ~13 batches per cell
- Error taxonomy: 4 bins with post-hoc thresholds
- SCS validated on Few-NERD only (not DocRED or MAVEN)
- No second model tested

## Your Task
Write a detailed review covering:
1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, specific)
3. **Weaknesses** (bulleted, specific, with severity: minor/major/critical)
4. **Questions for authors** (numbered)
5. **Missing experiments or analyses**
6. **Preliminary score** (1-6) with confidence (1-5)

Focus on: statistical rigor, experimental design flaws, whether claims are supported by evidence, confound handling, effect sizes vs statistical significance, adequacy of baselines and ablations.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "e612aae1-3e43-475d-9673-32a2c832fdc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T08:18:02.909Z_

```json
{
  "parentUuid": "e612aae1-3e43-475d-9673-32a2c832fdc8",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
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
  "uuid": "9a0bb09f-2d29-4b9f-a6ea-884fb7f66150",
  "timestamp": "2026-05-16T08:18:02.909Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T08:18:06.036Z_



I need to read the paper and project files to give a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a0bb09f-2d29-4b9f-a6ea-884fb7f66150",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vEZxBaUte1EBXXyWgR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7236c5b9-2a3c-4a2f-a056-1ea280d94123",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EUKynfSht3p9A654G7hXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15469,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15469,
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

_source line 4 · 2026-05-16T08:18:06.620Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EbhaECPC3UExWZkYR3FGjN`</summary>

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
  "parentUuid": "7236c5b9-2a3c-4a2f-a056-1ea280d94123",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vEZxBaUte1EBXXyWgR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfe8615c-e84f-4f14-95ad-80850208d42b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EUKynfSht3p9A654G7hXZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15469,
      "cache_read_input_tokens": 0,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15469
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 122,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15469,
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

_source line 5 · 2026-05-16T08:18:06.629Z_

<details><summary>↩ Tool result · `toolu_01EbhaECPC3UExWZkYR3FGjN`</summary>

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
  "parentUuid": "dfe8615c-e84f-4f14-95ad-80850208d42b",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "40241aa7-0fce-450b-98cc-cfe8c125f970",
  "sourceToolAssistantUUID": "dfe8615c-e84f-4f14-95ad-80850208d42b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T08:18:09.454Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01EugHYuAWTyVgzMxUa5gJmq`</summary>

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
  "parentUuid": "40241aa7-0fce-450b-98cc-cfe8c125f970",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vErBFL5pr2rutN5SEy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b32f6ba-a752-4bed-a434-c32f21a73111",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VpSL4UhEi7aiuzSRmFs77a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 15469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
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

_source line 7 · 2026-05-16T08:18:09.644Z_

<details><summary>↩ Tool result · `toolu_01EugHYuAWTyVgzMxUa5gJmq`</summary>

```text
{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (42 个)\n\n- **bootstrap_ci_analysis**: DONE (success) — \n- **exp016_fewrel_error_taxonomy**: DONE (success) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp007_error_taxonomy**: DONE (success) — \n- **exp_fewrel_formal_80rel**: DONE (success) — \n- **exp_fewrel_formal**: DONE (success) — \n- **exp008_sdgd_zero_fewnerd_r2**: DONE (negative) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n- **fewrel_pilot**: DONE (success) — \n- **exp004_maven_bcs**: DONE (negative) — \n- **exp002_confusability_controlled**: DONE (success) — \n- **exp003a_prompt_v2_rerun**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp001_count_baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- exp_fewrel_v2_n25（准备中）\n- bcs_max_to_mean_fix（准备中）\n\n## 近期结论\n- **exp_confusability_batch_composition** (success): Confusability-aware batch composition (graph coloring on SCS matrix to separate high-SCS pairs) improves per-type accuracy and reduces substitution errors compared to random batching and single-pass full schema, providing a practical application of the confusability findings.\n- **exp_fewrel_16rel_bootstrap** (success): FewRel 16-type pool, 100 random 8-type batches, bootstrap CI for BCS effect (Δ_BCS). 填 tab:bcs_controlled 16-rel 行的 CI，并与 80-rel 计算 amplification ratio 正式 CI。D033 已批准。 ← 基于 exp_fewrel_formal\n- **exp_docred_confusability** (success): Schema-induced degradation (count + confusability channels) generalizes to document-level RE (DocRED, 96 relation types), strengthening cross-dataset evidence for Claims 1 and 2. ← 基于 exp_fewrel_formal_80rel\n  [DocRED SCS Matrix (96 relations)](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/scs_matrix_info.txt) | [DocRED Confusability Pilot Results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/pilot_results.txt) | [phase2_count_curve_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/count_curve_results.json) | [phase2_bcs_controlled_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bcs_controlled_results.json) | [phase2_bootstrap_analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bootstrap_analysis.json)\n\n## 趋势\n成功 20 / 负向 5 / 失败 10 / 共 38\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\ncqa1-38874: 无 GPU 信息\n\n## 告警\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\n- exp012_llama_8b: 已被终止 — unknown\n- exp_fewrel_40rel: 训练失败 — unknown\n- exp012_llama_awq: 已被终止 — unknown\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\n- exp_fewrel_40rel_r2: 训练失败 — unknown\n- exp_fewrel_40rel_r3: 训练失败 — unknown\n- exp012_llama_8b_r3: 训练失败 — unknown\n- exp_fewrel_16rel_100batch: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b32f6ba-a752-4bed-a434-c32f21a73111",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "c26581cc-a421-4f58-b78c-242b8474a35e",
  "sourceToolAssistantUUID": "8b32f6ba-a752-4bed-a434-c32f21a73111",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T08:18:09.927Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TWATC6B4y33Fv73bxB7cjB`</summary>

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
  "parentUuid": "c26581cc-a421-4f58-b78c-242b8474a35e",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vErBFL5pr2rutN5SEy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "985f2d36-f7c0-497e-a511-fe9b6b852cc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VpSL4UhEi7aiuzSRmFs77a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 15469,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1444
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 160,
          "cache_read_input_tokens": 15469,
          "cache_creation_input_tokens": 1444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1444,
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

_source line 9 · 2026-05-16T08:18:09.950Z_

<details><summary>↩ Tool result · `toolu_01TWATC6B4y33Fv73bxB7cjB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp017_gpt4o_mini_fewrel（准备中）\\n- exp_cross_embedding_sensitivity（准备中）\\n- exp_fewrel_v2_n25（准备中）\\n- bcs_max_to_mean_fix（准备中）\\n\\n## 近期结论\\n- **exp_confusability_batch_composition** (success): Confusability-aware batch composition (graph coloring on SCS matrix to separate high-SCS pairs) improves per-type accuracy and reduces substitution errors compared to random batching and single-pass full schema, providing a practical application of the confusability findings.\\n- **exp_fewrel_16rel_bootstrap** (success): FewRel 16-type pool, 100 random 8-type batches, bootstrap CI for BCS effect (Δ_BCS). 填 tab:bcs_controlled 16-rel 行的 CI，并与 80-rel 计算 amplification ratio 正式 CI。D033 已批准。 ← 基于 exp_fewrel_formal\\n- **exp_docred_confusability** (success): Schema-induced degradation (count + confusability channels) generalizes to document-level RE (DocRED, 96 relation types), strengthening cross-dataset evidence for Claims 1 and 2. ← 基于 exp_fewrel_formal_80rel\\n  [DocRED SCS Matrix (96 relations)](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/scs_matrix_info.txt) | [DocRED Confusability Pilot Results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/pilot_results.txt) | [phase2_count_curve_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/count_curve_results.json) | [phase2_bcs_controlled_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bcs_controlled_results.json) | [phase2_bootstrap_analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bootstrap_analysis.json)\\n\\n## 趋势\\n成功 20 / 负向 5 / 失败 10 / 共 38\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-38874: 无 GPU 信息\\n\\n## 告警\\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\\n- exp012_llama_fewnerd: 训练失败 — unknown\\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\\n- exp012_llama_8b: 已被终止 — unknown\\n- exp_fewrel_40rel: 训练失败 — unknown\\n- exp012_llama_awq: 已被终止 — unknown\\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\\n- exp_fewrel_40rel_r2: 训练失败 — unknown\\n- exp_fewrel_40rel_r3: 训练失败 — unknown\\n- exp012_llama_8b_r3: 训练失败 — unknown\\n- exp_fewrel_16rel_100batch: 已被终止 — unknown\\n\", \"total_chars\": 2396, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "985f2d36-f7c0-497e-a511-fe9b6b852cc3",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "b8264f26-6b15-480e-94b7-7ec19e641b76",
  "sourceToolAssistantUUID": "985f2d36-f7c0-497e-a511-fe9b6b852cc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T08:18:13.130Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UuAmZN2bx9hwy1qEaWP8a9`</summary>

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
  "parentUuid": "b8264f26-6b15-480e-94b7-7ec19e641b76",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vF6Cc3wVscpPwxktJX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cc4707d-0f2f-4209-87f0-02410fba921d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdivMLhqRCtB5897jvsv66",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2757,
      "cache_read_input_tokens": 16913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2757,
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

_source line 11 · 2026-05-16T08:18:13.142Z_

<details><summary>↩ Tool result · `toolu_01UuAmZN2bx9hwy1qEaWP8a9`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'schema-dag-extraction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cc4707d-0f2f-4209-87f0-02410fba921d",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "5fbe0307-9717-42b5-90b5-2db7c13d204b",
  "sourceToolAssistantUUID": "1cc4707d-0f2f-4209-87f0-02410fba921d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T08:18:14.069Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UNv3qRTzAPsBWuKxV8rGpB`</summary>

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
  "parentUuid": "5fbe0307-9717-42b5-90b5-2db7c13d204b",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vF6Cc3wVscpPwxktJX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2df9922d-6d17-4395-ad05-c0c6292f2bdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdivMLhqRCtB5897jvsv66",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2757,
      "cache_read_input_tokens": 16913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2757,
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

_source line 13 · 2026-05-16T08:18:14.079Z_

<details><summary>↩ Tool result · `toolu_01UNv3qRTzAPsBWuKxV8rGpB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ROADMAP.md\", \"content\": \"# schema-dag-extraction — Research Dashboard\\n\\n> 最后更新: 2026-05-16 06:08 UTC | 更新原因: 服务器重启恢复，更新 v2 n=25/DocRED/cross-embedding 完成状态，派 exp-018+exp-017\\n\\n## 核心方向\\n验证 type confusability 独立于 type count 驱动 training-free LLM IE 质量下降，发现 multi-channel degradation model（count→recall, confusability→type confusion）。v2 n=25 证明效应是 task-inherent property 而非 prompt artifact（D040）。详见 paper_framing.md。\\n\\n## 当前阶段\\n**Scope 扩展冲刺** — ARR May 25 提交（距今 9 天）。三条并行线推进。\\n\\n- Claim 1（count scaling）：四任务 + 双模型验证完成 ✓（DocRED 新增）\\n- Claim 2（BCS confusability）：四任务 + 双模型验证完成 ✓（DocRED 新增）\\n- Claim 3（SDGD）：正式放弃 (D019)，negative result + future work\\n- D040：v2 RE n=25 推翻 attenuation 叙述 → confusability is task-inherent ✓\\n- D038/D039：BCS 定义统一（MAX→MEAN）✓\\n- Cross-embedding sensitivity：MiniLM vs Qwen3 方向一致 ✓\\n- Reviewer 审查 D040 叙事重写 + claim 边界评估中\\n\\n## 表述硬约束（C001，全角色遵守）\\n- **C001**: count_40 子集来自 80-type pool 采样，论文必须写 \\\"40-rel subsets sampled from the 80-relation pool\\\"\\n\\n## Scope 扩展计划\\n\\n**Track A — GPU**\\n- [x] DocRED Phase 2 count curve + BCS-controlled ✓（slope −0.71, r=−0.66, p=1.5e-5）\\n- [x] Cross-embedding sensitivity ✓（方向一致，MiniLM 更适合 BCS）\\n- [x] v2 RE n=25 验证 ✓（Δ=25.5pp, r=−0.919, p<0.0001）\\n- [ ] **exp-018: Confusability-aware batch composition** — 已派 Agent 立即上 GPU\\n\\n**Track B — API**\\n- [x] OpenAI key 已存储 ✓\\n- [ ] **exp-017: GPT-4o-mini FewRel replication** — 已派 Agent 启动，API-bound 不占 GPU\\n\\n**Track C — CPU/写作**\\n- [x] D038 BCS 定义统一 ✓\\n- [x] DocRED 论文集成 ✓\\n- [ ] 3 个 Reviewer warning 修复中（docred-2019 编译、registry 过时值、Qwen3 r 值不一致）\\n- [ ] D040 叙事更新确认（§4.3/Intro/AppG）\\n- [ ] Review round（Reviewer 审查 D040 + claim 边界中）\\n- [ ] Final submission\\n\\n## 核心证据进展\\n\\n**已完成（Claim 1+2）**:\\n- exp-001: count curve (recall 0.72→0.42, WrongType 0→2434) ✓\\n- exp-002: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x ✓\\n- exp-003a: prompt v2 降低 over-prediction ✓\\n- exp-004: MAVEN 168 types, MiniLM pairwise r=0.120 ✓\\n- exp_fewrel_formal_80rel: BCS Δ=-31.2pp, slope=-0.401 ✓\\n- exp_fewrel_40rel_r4: count_40=0.588, BCS Δ=-33.3pp/-31.8pp ✓\\n- exp007/exp016 error taxonomy: IntraSub ρ=1.0/0.954 ✓\\n- bootstrap_ci_analysis: 统一 fixed-boundary B=10000 ✓\\n- exp015_scs_validation: 两种 embedding 均显著 ✓\\n- exp012_llama_fewrel_ch2: BCS Δ=-27.1pp/-23.9pp, high-BCS floor 0.51 ✓\\n- D038: BCS MAX→MEAN (slope -0.509, |r|=0.467, quartile Δ=-5.3pp) ✓\\n- **exp_docred_confusability**: BCS slope −0.71（最陡）, r=−0.66, p=1.5e-5, 96 types ✓\\n- **exp_v2_re_n25**: Δ=25.5pp, CI [22.4, 28.6], r=−0.919 — task-inherent ✓\\n- **cross_embedding_sensitivity**: MiniLM/Qwen3 方向一致，MiniLM effect size 更大 ✓\\n\\n**负向结论**:\\n- exp-008 SDGD: F1=0.241 < baseline 0.445 (D014, D019)\\n- exp004_maven_bcs: per-type BCS 正向（centrality confound）\\n- exp006_interaction_2x2: p=0.505 (D026)\\n- exp012_llama_8b_r2_exp2: NER Channel 2 未复现（floor effect）\\n\\n## 近期任务\\n- [ ] exp-018 batch composition 上 GPU（Agent 执行中）\\n- [ ] exp-017 GPT-4o-mini 启动（Agent 执行中）\\n- [ ] 3 个 Reviewer warning 修复\\n- [ ] Reviewer 审查 D040 叙事 + claim 边界评估\\n- [ ] 论文最终集成 + Review round\\n- [ ] 最终提交 ARR May 25\\n\\n## GPU 预算\\n- 服务器: cqa1-38874, 1× RTX PRO 6000 Blackwell (98GB), cuda:0\\n- 当前: 空闲 → exp-018 即将占用\\n\\n## 目标会议\\nEMNLP 2026, ARR May 25 提交（距今 9 天）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D043 | 2026-05-16 | D042 修正：exp-018 confusability-aware 与 random 无显著差异 | exp_confusability_batch_composition |\\n| D042 | 2026-05-16 | exp-018 成功：confusability-aware batching 在 RE 上 +1. | exp_confusability_batch_composition |\\n| D041 | 2026-05-16 | 放弃 exp-017 GPT-4o-mini：TUM proxy 未部署，AutoDL 无法访问 O | exp017_gpt4o_mini_fewrel |\\n| D040 | 2026-05-16 | v2 RE n=25 结果推翻 attenuation 叙述，升级为 \\\"confusability  | exp_v2_re_n25 |\\n| D039 | 2026-05-16 | D039: BCS 统一选择 Path A (MEAN)——科学诚实优先，MAX 作 sensiti | exp_fewrel_16rel_bootstrap, exp_fewrel_formal_80rel, exp_fewrel_80pool_16sub_bootstrap |\\n| D038 | 2026-05-16 | D038: BCS 定义不一致修复——统一为 MEAN pairwise SCS，重算 Table  | exp_fewrel_16rel_bootstrap, exp_fewrel_formal_80rel, exp_fewrel_80pool_16sub_bootstrap |\\n| D037 | 2026-05-16 | D037: Round 2 审稿 Action Matrix 定稿——5C+12W 逐条方案，C1  | exp-003a, exp_fewrel_formal |\\n| D036 | 2026-05-16 | D035 修订：Table 3 以回归斜率为主指标，四分位 Δ 为辅 | exp_fewrel_80pool_16sub_bootstrap, exp_fewrel_16rel_bootstrap |\\n| D035 | 2026-05-16 | D033 集成采用极端批次方法重算，保持 Table 3 方法一致性 | exp_fewrel_16rel_bootstrap, exp_fewrel_80pool_16sub_bootstrap |\\n| D034 | 2026-05-16 | Amplification 报告策略：同时报告 quartile Δ 和 BCS-accuracy  | exp_fewrel_16rel_bootstrap, exp_fewrel_80pool_16sub_bootstrap |\\n\\n\", \"total_chars\": 4380, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2df9922d-6d17-4395-ad05-c0c6292f2bdf",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "975fdd0f-0de6-423e-a14a-a8e87ee6fa67",
  "sourceToolAssistantUUID": "2df9922d-6d17-4395-ad05-c0c6292f2bdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T08:18:14.361Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BzatA1HA2vLXLmy3nEJTTX`</summary>

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
  "parentUuid": "975fdd0f-0de6-423e-a14a-a8e87ee6fa67",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vF6Cc3wVscpPwxktJX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4155d47-8aba-416b-8032-6b49364e94b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdivMLhqRCtB5897jvsv66",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2757,
      "cache_read_input_tokens": 16913,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2757
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 286,
          "cache_read_input_tokens": 16913,
          "cache_creation_input_tokens": 2757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2757,
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

_source line 15 · 2026-05-16T08:18:14.375Z_

<details><summary>↩ Tool result · `toolu_01BzatA1HA2vLXLmy3nEJTTX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/memory.md\", \"content\": \"# Memory — schema-dag-extraction\\n\\n## exp-018 结果与经验（2026-05-16）\\n- **结果**: confusability_aware 0.8021 > random 0.7877±0.0178 (CI上界0.7967)，提升显著 +1.44pp\\n- single_pass 80-rel 全量仅 0.5042，schema overload 严重\\n- Graph coloring (Welsh-Powell) 将 intra-batch BCS 从 0.5585 降到 0.5524\\n- 51 types improved, 28 degraded — 效果非均匀，部分 type 受益更多\\n- **关键参数**: 80-rel pool, batch_size=8-rel per batch, 15 random seeds for CI, 960 samples\\n- **无 merge amplification** — RE closed-set 验证了 Director 的预判\\n- FLASHINFER_DISABLE_VERSION_CHECK=1 需要设置，否则 vLLM 启动失败\\n- 支持 --resume 断点续传（按 condition 粒度）\\n\\n## exp-018 定位澄清（2026-05-16, Director）\\n- exp-018 不是\\\"重试 SDGD\\\"，而是\\\"confusability-aware batching 在 RE closed-set classification 上的实用方案\\\"\\n- RE 每个 (head, tail) pair 独立分类，无实体边界合并 → 无 merge amplification 问题\\n- exp-008 SDGD 失败的 root cause = NER span overlap 的 merge amplification，不适用于 RE\\n- 论文写法：§5 SDGD 失败因 NER merge amplification，但 RE closed-set 避免了此问题 → practical recommendation\\n\\n## exp-017 GPT-4o-mini（2026-05-16, Director 决定放弃）\\n- TUM proxy 未部署在 AutoDL 服务器，无法访问 OpenAI API\\n- 闭源模型验证缺失已在 discussion.tex limitations 中说明\\n- 教训：API 实验需要预先确认 proxy 可达性\\n\\n## D035 集成方案（2026-05-16）\\n- 论文 Table 3 用**极端批次**方法（BCS 最低/最高各 ~5 batches 的 accuracy Δ），不是四分位\\n- D033 的 7.42pp 是四分位比较，需要用极端批次方法重算\\n- 80-pool-16sub 的 3.92pp 也是四分位，同样需要重算\\n- 四分位 CI 作为补充证据报告，展示效应在不同分析粒度下都稳健\\n- 两组数据一起集成到论文再编译上传\\n\\n## 80-pool-16sub 关键发现（2026-05-16）\\n- BCS 范围窄 [0.458, 0.684]（vs 独立 16-rel [0.653, 0.900]），因为从 80-rel pool 采样的 16 types 语义更分散\\n- 四分位 Δ CI 跨零 [-7.79, +0.42]，但回归斜率 CI 不跨零 [-0.684, -0.062]\\n- 效应弱于独立 16-rel pool——BCS 范围压缩导致效应量缩小，这本身支持 BCS 是驱动因素的论点\\n- 决策：用回归斜率做跨条件比较（斜率控制了 BCS 范围差异），四分位 Δ 作为直觉可读的补充\\n\\n## MAVEN per-type BCS 正相关是 artifact（2026-05-16）\\n- exp_maven_residualized_bcs 确认：控制 log_freq + degree_centrality 后相关消失\\n- MiniLM confound = frequency, Qwen3 confound = degree centrality (r=0.854)\\n- 同质 schema（MAVEN 168 event types 多来自 FrameNet）下 per-type BCS 聚合失效\\n- pairwise SCS 仍然有效\\n\\n## Few-NERD r 值差异根因（2026-05-16）\\n- 三个 r 值同源（同一 confusion matrix, 1953 pairs），差异仅因 Y 变量：rate=0.112, count=0.138, CI上界=0.156\\n- Table 2 r=0.112 正确（confusion rate，归一化 gold frequency）\\n- p-values 已修正：Few-NERD Pearson p=7×10⁻⁷, MAVEN p=7×10⁻⁴²\\n\", \"total_chars\": 2127, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4155d47-8aba-416b-8032-6b49364e94b2",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "4416580e-2e3a-4899-9de8-85f44f3f547d",
  "sourceToolAssistantUUID": "e4155d47-8aba-416b-8032-6b49364e94b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-16T08:18:17.661Z_

Now let me read the paper itself and key experimental artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4416580e-2e3a-4899-9de8-85f44f3f547d",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vFR5AZPR3YjNaxeDKj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "067df463-ce22-4e97-b929-ced5e08db117",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWaooFN5akXeFkTTBXqk6N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4490,
      "cache_read_input_tokens": 19670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4490,
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

_source line 17 · 2026-05-16T08:18:18.170Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011RS6ZWZTXRyvap2wtAap6x`</summary>

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
  "parentUuid": "067df463-ce22-4e97-b929-ced5e08db117",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vFR5AZPR3YjNaxeDKj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cd30812-f956-4c10-990b-4597f2e3d2ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWaooFN5akXeFkTTBXqk6N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4490,
      "cache_read_input_tokens": 19670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4490,
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

_source line 18 · 2026-05-16T08:18:18.202Z_

<details><summary>↩ Tool result · `toolu_011RS6ZWZTXRyvap2wtAap6x`</summary>

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
  "parentUuid": "6cd30812-f956-4c10-990b-4597f2e3d2ff",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "d17e4d90-0916-4aab-a68f-15bbf7e5da33",
  "sourceToolAssistantUUID": "6cd30812-f956-4c10-990b-4597f2e3d2ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T08:18:19.065Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014ZXgNdqMTZsqhPdooeoqTT`</summary>

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
  "parentUuid": "d17e4d90-0916-4aab-a68f-15bbf7e5da33",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vFR5AZPR3YjNaxeDKj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a136a7a-8a5b-4160-8912-6991d5193bf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWaooFN5akXeFkTTBXqk6N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4490,
      "cache_read_input_tokens": 19670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4490,
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

_source line 20 · 2026-05-16T08:18:19.076Z_

<details><summary>↩ Tool result · `toolu_014ZXgNdqMTZsqhPdooeoqTT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_framing.md\", \"content\": \"# Paper Framing — schema-dag-extraction\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\\n- Commitment deadline: August 2, 2026\\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\\n- Deadline: ARR May 25, 2026 (10 days from today)\\n\\n## Core Claims (2 claims) — Revised per D019\\n\\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.\\n\\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\\n\\n~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — \\\"why naive decomposition fails\\\" is itself a contribution.\\n\\n## Story Spine — Revised per D012\\n\\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\\n\\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\\n\\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.\\n\\n- **Three-task validation**:\\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio\\n  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel\\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\\n\\n- **Headline result template**: \\\"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid.\\\"\\n\\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\\n\\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\\n\\nThese channels are orthogonal and independently addressable.\\n\\n**Pairwise vs Aggregated Confusability**:\\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).\\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\\n\\n## Evidence Hierarchy (D012)\\n\\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\\n\\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\\n\\n**Few-NERD (NER)** — Qwen3 embeddings:\\n- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation\\n- Nonzero-only Spearman ρ=0.272 (p=5e-5)\\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\\n- Immune to type frequency confound (operates at type-pair level)\\n\\n**MAVEN (ED)** — MiniLM embeddings:\\n- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap\\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\\n- Cross-task replication on same-domain schema\\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\\n\\n### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication\\n\\nLarge effect size, cross-task (RE), scaling with schema complexity:\\n\\n**Formal 80-rel study** (exp_fewrel_formal_80rel):\\n- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97\\n- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)\\n- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)\\n- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)\\n\\n**16-rel sanity check** (exp_fewrel_formal):\\n- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\\n\\n**Pilot extreme batches** (fewrel_pilot, MiniLM):\\n- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp\\n\\nKey insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling\\n\\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\\n\\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\\n\\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\\n\\nMethodological case study on when aggregated confusability measures fail:\\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\\n- This is stronger than \\\"domain boundary\\\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\\n\\n### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)\\n\\nIntraSub rate monotonically increases with BCS on both NER and RE:\\n\\n**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0\\n**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)\\n- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon\\n- Same mechanism, different absolute magnitudes — consistent with cross-task expectations\\n\\nAdditional from extreme batch design:\\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\\n\\n## Embedding Ablation (D010)\\n\\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\\n\\n### Per-type (Layer 2)\\n| | Few-NERD | FewRel | MAVEN |\\n|---|---|---|---|\\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\\n\\n### Pairwise (Layer 1)\\n| | Few-NERD | MAVEN |\\n|---|---|---|\\n| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |\\n| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |\\n\\n### SCS→Empirical Confusion Validation (exp-015 fast)\\n| | Qwen3 | MiniLM |\\n|---|---|---|\\n| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |\\n| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |\\n\\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\\n\\n## Venue Fit Risks\\n\\n- **\\\"Just an empirical study\\\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \\\"Lost in the Middle\\\" (TACL 2024).\\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy | Experiment |\\n|---------|------------------|------------|\\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\\n\", \"total_chars\": 11568, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a136a7a-8a5b-4160-8912-6991d5193bf4",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "93a882c0-bd4a-44e2-a8e2-b99d17719998",
  "sourceToolAssistantUUID": "7a136a7a-8a5b-4160-8912-6991d5193bf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T08:18:19.630Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014E4TobDv6hFpsg4G9rsppG`</summary>

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
  "parentUuid": "93a882c0-bd4a-44e2-a8e2-b99d17719998",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vFR5AZPR3YjNaxeDKj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f347bb0-2be9-4fc6-986b-96c1407f50c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWaooFN5akXeFkTTBXqk6N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4490,
      "cache_read_input_tokens": 19670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4490,
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

_source line 22 · 2026-05-16T08:18:19.645Z_

<details><summary>↩ Tool result · `toolu_014E4TobDv6hFpsg4G9rsppG`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'schema-dag-extraction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f347bb0-2be9-4fc6-986b-96c1407f50c2",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "a09a1b5a-c814-4245-808b-46d780d43608",
  "sourceToolAssistantUUID": "8f347bb0-2be9-4fc6-986b-96c1407f50c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T08:18:22.262Z_

Let me read the actual paper sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a09a1b5a-c814-4245-808b-46d780d43608",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vFocyxaDrx66ETKa5y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ffa471f-b5e1-4fbc-a837-c11ed4ff9ea8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Npt1qGG9ufXQZuM1bzwZdL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5164,
      "cache_read_input_tokens": 24160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5164,
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

_source line 24 · 2026-05-16T08:18:23.738Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T7Wk8bHSfuAzRDpkicq3sB`</summary>

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
  "parentUuid": "2ffa471f-b5e1-4fbc-a837-c11ed4ff9ea8",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vFocyxaDrx66ETKa5y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55d20236-a3e1-4627-b4ac-72c0bedc03d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Npt1qGG9ufXQZuM1bzwZdL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5164,
      "cache_read_input_tokens": 24160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5164,
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

_source line 25 · 2026-05-16T08:18:23.747Z_

<details><summary>↩ Tool result · `toolu_01T7Wk8bHSfuAzRDpkicq3sB`</summary>

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
  "parentUuid": "55d20236-a3e1-4627-b4ac-72c0bedc03d8",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "4f327688-78d7-4f0e-b22e-094944651cc0",
  "sourceToolAssistantUUID": "55d20236-a3e1-4627-b4ac-72c0bedc03d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-16T08:18:24.212Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KohSSVFhzx1NyF8SUoEKuU`</summary>

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
  "parentUuid": "4f327688-78d7-4f0e-b22e-094944651cc0",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vFocyxaDrx66ETKa5y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "751988f0-732d-4ebf-9b51-6f7745fedd19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Npt1qGG9ufXQZuM1bzwZdL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5164,
      "cache_read_input_tokens": 24160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5164,
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

_source line 27 · 2026-05-16T08:18:24.218Z_

<details><summary>↩ Tool result · `toolu_01KohSSVFhzx1NyF8SUoEKuU`</summary>

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
  "parentUuid": "751988f0-732d-4ebf-9b51-6f7745fedd19",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "9e0ee1d8-36fc-4f91-8a0a-8dfed444a3c7",
  "sourceToolAssistantUUID": "751988f0-732d-4ebf-9b51-6f7745fedd19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T08:18:24.697Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KcvmMjTFVgU25bmsNKtrH5`</summary>

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
  "parentUuid": "9e0ee1d8-36fc-4f91-8a0a-8dfed444a3c7",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vFocyxaDrx66ETKa5y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a72490de-0fbb-40ab-a1eb-65e4a56cfc37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Npt1qGG9ufXQZuM1bzwZdL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5164,
      "cache_read_input_tokens": 24160,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5164
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 24160,
          "cache_creation_input_tokens": 5164,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5164,
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

_source line 29 · 2026-05-16T08:18:24.702Z_

<details><summary>↩ Tool result · `toolu_01KcvmMjTFVgU25bmsNKtrH5`</summary>

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
  "parentUuid": "a72490de-0fbb-40ab-a1eb-65e4a56cfc37",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "e1898564-1875-4140-9ab9-ec52de1b3f4e",
  "sourceToolAssistantUUID": "a72490de-0fbb-40ab-a1eb-65e4a56cfc37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T08:18:28.891Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YETdhnHd4VeAsHWXcLhdKq`</summary>

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
  "parentUuid": "e1898564-1875-4140-9ab9-ec52de1b3f4e",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vGBNgN1tFEGbczY12J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db6354c9-8891-4a70-a68d-f3ff97d98bef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxubR7G6ZJSerieTa6XfNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9800,
      "cache_read_input_tokens": 29324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9800,
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

_source line 31 · 2026-05-16T08:18:28.903Z_

<details><summary>↩ Tool result · `toolu_01YETdhnHd4VeAsHWXcLhdKq`</summary>

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
  "parentUuid": "db6354c9-8891-4a70-a68d-f3ff97d98bef",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "549d2de9-eb0a-4f46-8391-98317c2bb79b",
  "sourceToolAssistantUUID": "db6354c9-8891-4a70-a68d-f3ff97d98bef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T08:18:30.240Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LbGLivYxa7YdQwRQXJNfk3`</summary>

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
  "parentUuid": "549d2de9-eb0a-4f46-8391-98317c2bb79b",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vGBNgN1tFEGbczY12J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd52138b-f09d-4ec8-b010-0bf3affec8c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxubR7G6ZJSerieTa6XfNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9800,
      "cache_read_input_tokens": 29324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9800,
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

_source line 33 · 2026-05-16T08:18:30.245Z_

<details><summary>↩ Tool result · `toolu_01LbGLivYxa7YdQwRQXJNfk3`</summary>

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
  "parentUuid": "cd52138b-f09d-4ec8-b010-0bf3affec8c4",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "42a3f812-731c-4898-82a1-8f4867e4a5f5",
  "sourceToolAssistantUUID": "cd52138b-f09d-4ec8-b010-0bf3affec8c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-16T08:18:30.292Z_

<details open><summary>🔧 Tool call — Read · `toolu_0141npGMLALzxpoJo1pUf68y`</summary>

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
  "parentUuid": "42a3f812-731c-4898-82a1-8f4867e4a5f5",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vGBNgN1tFEGbczY12J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed99e056-9a64-48d6-a713-f21dc300e636",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxubR7G6ZJSerieTa6XfNd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9800,
      "cache_read_input_tokens": 29324,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9800
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 29324,
          "cache_creation_input_tokens": 9800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9800,
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

_source line 35 · 2026-05-16T08:18:30.300Z_

<details><summary>↩ Tool result · `toolu_0141npGMLALzxpoJo1pUf68y`</summary>

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
  "parentUuid": "ed99e056-9a64-48d6-a713-f21dc300e636",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "ec4dbd3d-609f-49e9-b45b-c6ab1921207c",
  "sourceToolAssistantUUID": "ed99e056-9a64-48d6-a713-f21dc300e636",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-16T08:18:34.397Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DCYBmZC7RQaMxqDc4CPh3i`</summary>

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
  "parentUuid": "ec4dbd3d-609f-49e9-b45b-c6ab1921207c",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vGb3UJr5xFj6E4BGgg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9431edb9-24ce-40d4-a0b6-9d9e0d69a0c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013caVeCD8ta7T7xx5y2cSdK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11516,
      "cache_read_input_tokens": 39124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11516,
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

_source line 37 · 2026-05-16T08:18:34.404Z_

<details><summary>↩ Tool result · `toolu_01DCYBmZC7RQaMxqDc4CPh3i`</summary>

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
  "parentUuid": "9431edb9-24ce-40d4-a0b6-9d9e0d69a0c3",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "d8dcf74e-5577-4adf-8977-94a90b63f48d",
  "sourceToolAssistantUUID": "9431edb9-24ce-40d4-a0b6-9d9e0d69a0c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T08:18:34.829Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NH9DfzSyEjLupV71jmza4q`</summary>

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
  "parentUuid": "d8dcf74e-5577-4adf-8977-94a90b63f48d",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vGb3UJr5xFj6E4BGgg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b45d8ee-1283-4cb2-be36-a4b8a3b330fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013caVeCD8ta7T7xx5y2cSdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11516,
      "cache_read_input_tokens": 39124,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11516
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 39124,
          "cache_creation_input_tokens": 11516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11516,
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

_source line 39 · 2026-05-16T08:18:34.834Z_

<details><summary>↩ Tool result · `toolu_01NH9DfzSyEjLupV71jmza4q`</summary>

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
  "parentUuid": "6b45d8ee-1283-4cb2-be36-a4b8a3b330fd",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "eda8802c-38a0-4cef-81ee-6d08dce9d370",
  "sourceToolAssistantUUID": "6b45d8ee-1283-4cb2-be36-a4b8a3b330fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-16T08:18:37.885Z_

Now let me also look at the dream review reports to see if prior reviews exist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eda8802c-38a0-4cef-81ee-6d08dce9d370",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vGvrb9v49H9F92UbF5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aeb346cf-34e9-40b4-9742-899d5f309b22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EphoWY4NYFbd2PgR2Uz4q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2096,
      "cache_read_input_tokens": 50640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2096,
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

_source line 41 · 2026-05-16T08:18:39.297Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EZYezVNY7PYiqxFsx1g9pJ`</summary>

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
  "parentUuid": "aeb346cf-34e9-40b4-9742-899d5f309b22",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vGvrb9v49H9F92UbF5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "818ef9f3-63e8-45f6-ac44-e319aba504a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EphoWY4NYFbd2PgR2Uz4q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2096,
      "cache_read_input_tokens": 50640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2096,
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

_source line 42 · 2026-05-16T08:18:39.315Z_

<details><summary>↩ Tool result · `toolu_01EZYezVNY7PYiqxFsx1g9pJ`</summary>

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
  "parentUuid": "818ef9f3-63e8-45f6-ac44-e319aba504a6",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "bcd761f3-7bfb-444b-bcb1-ff7ea05cea99",
  "sourceToolAssistantUUID": "818ef9f3-63e8-45f6-ac44-e319aba504a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T08:18:39.926Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DogcXNqSXWLYcKBa6m4jiR`</summary>

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
  "parentUuid": "bcd761f3-7bfb-444b-bcb1-ff7ea05cea99",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vGvrb9v49H9F92UbF5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2ee817f-e3a3-483d-8c0c-1d4e2b093480",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EphoWY4NYFbd2PgR2Uz4q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2096,
      "cache_read_input_tokens": 50640,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2096
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 50640,
          "cache_creation_input_tokens": 2096,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2096,
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

_source line 44 · 2026-05-16T08:18:39.956Z_

<details><summary>↩ Tool result · `toolu_01DogcXNqSXWLYcKBa6m4jiR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml\", \"content\": \"_next_id: 44\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:10 UTC\\n  summary: 项目立项，MVP 验证方案：Experiment 2 (Confusability Controlled) 为核心验证实验\\n  rationale: 'IDEA_BRIEF 的核心假设是 type confusability 独立于 type count 驱动 LLM IE 质量下降。Experiment\\n    2（固定 count 变 BCS）是最直接的假设检验。Pass 标准: |r|≥0.3 且 p<0.05。ACE05 RE + Few-NERD 双数据集验证。ARR\\n    May 25 DDL（11天），MVP 需 1-2 天完成。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:15 UTC\\n  summary: 修正 MVP 统计设计：random samples 从 10 增至 25/档，加入 per-type solo baseline 控制变量，核心指标改为\\n    Δ(solo_F1 - batch_F1)\\n  rationale: Reviewer 指出 n=12 下 |r|=0.3 对应 p≈0.34，无法同时满足 |r|≥0.3 且 p<0.05。增至 25 random\\n    batches/档 → n≈54，|r|≥0.27 即可达 p<0.05。同时加入 solo F1 控制 type 固有难度，避免将\\\"类型本身难抽取\\\"误归因于\\\"confusability\\n    效应\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 23:11 UTC\\n  summary: MVP 分析方法从 Δ(solo-batch) 切换到 within-count Pearson r(F1, BCS)，pass 标准更新为\\n    |r|≥0.3 at fixed count\\n  rationale: Exp 1 发现 count curve 方向反转（F1 随 count 上升），根因是低 count 时模型过度 hallucinate（pred/gold=8x\\n    at count=1）。solo baseline 处于极端行为模式，Δ 被跨 count 行为差异污染。改为 within-count 对比更干净：同一\\n    count 下比较不同 BCS 的 F1，直接检验 confusability 独立效应。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count curve reversed, hallucination at low count\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 23:31 UTC\\n  summary: MVP 主指标更新为 within-count r(recall, BCS)，F1 因 over-prediction confound 降为补充指标\\n  rationale: Exp 1 text-match 重评估发现：recall 单调下降（0.72→0.42，符合预期），precision 单调上升（0.11→0.52，over-prediction\\n    减少），F1 受 precision 主导而反转。within-count 分析中 precision confound 在同一 count 下近似恒定，F1\\n    仍可用；但 recall 更干净且直接反映 type confusion。WrongType 错误（text 正确但 type 错标）随 count 从 0\\n    升至 2434，直接支持 confusability 假设。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: recall monotonically decreases with count; WrongType errors increase;\\n      over-prediction confounds F1\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-15 02:34 UTC\\n  summary: 'MVP PASS（refined mechanism）: confusability 通过 type confusion 通道驱动降级，选择\\n    Narrative A (multi-channel degradation model)'\\n  rationale: Exp 2 结果：recall vs BCS 不显著（r=0.25, p=0.066），但 F1 vs BCS 在 count_12 显著（r=0.50,\\n    p=0.008），偏相关 r=0.30 p=0.026 达到 pass 标准。Confusion rate high-BCS vs low-BCS 差异 30-40x（p=0.043）。机制清晰：confusability\\n    不导致遗漏，而是导致错标。选 Narrative A（multi-channel）因为：(1) 用上所有数据（exp1 count→recall + exp2\\n    BCS→confusion）(2) 两个正交机制 story 更丰富 (3) SDGD 框架天然需要同时处理 count 和 confusability。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count drives recall decline 0.72→0.42\\n  - exp_id: exp002_confusability_controlled\\n    role: evidence\\n    result: BCS drives type confusion 30-40x, F1 partial r=0.30 p=0.026\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-15 04:04 UTC\\n  summary: 跳过 Dream 模拟，直接批准 P0 实验\\n  rationale: 'Dream 模拟因基础设施 bug 崩溃（TypeError: _run_dream_pipeline() got unexpected\\n    keyword argument ''operational_chat_id''），P0 实验已被阻塞 9+ 小时。这是平台问题不是项目问题，不应阻塞研究进度。paper_framing.md\\n    和 experiment_plan.yaml 已完成，方向清晰，可直接推进。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D007\\n  date: 2026-05-15 04:16 UTC\\n  summary: RE 第三任务需先做 BCS pilot 验证，不直接 commit\\n  rationale: Reviewer 指出 RE 的 confusability 机制与 NER/ED 可能不同——RE type confusion 取决于\\n    entity pair 语义角色而非 relation label embedding 相似度。如果 BCS 在 RE 上不 work，反而削弱 task-agnostic\\n    claim。策略：先花 1h 做 FewRel type 的 BCS 矩阵 + 小规模 pilot（5 batches），确认信号存在再 commit P0；信号不存在则\\n    claim 缩窄为 span-level IE，在 limitation 中承认。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-15 05:10 UTC\\n  summary: 重构证据层级：pairwise 分析升为主要证据，batch-level 需控制 type frequency\\n  rationale: exp003a v2 Reviewer 独立核实发现 within-count BCS-F1 正相关（高 BCS→高 F1），与假设方向相反。根因：type\\n    frequency 混淆变量（高频类型既有高 BCS 又被模型更好提取）。pairwise 分析（r=0.156, p=4.6e-12）不受此影响，仍成立。需要：(1)\\n    pairwise 升为 Channel 1 主要证据 (2) 新增 per-type F1 分析控制频率 (3) batch-level 正相关在论文中透明报告并解释混淆变量。\\n  related_experiments:\\n  - exp_id: exp003a\\n    role: trigger\\n    result: within-count r>0 contradicts hypothesis direction\\n  depends_on:\\n  - D006\\n- id: D009\\n  date: 2026-05-15 07:21 UTC\\n  summary: 'Paper story reframe: BCS proxy task-specific → SDGD-cal empirical calibration\\n    成为核心贡献'\\n  rationale: MAVEN per-type 分析显示 BCS 与 F1 正相关（ρ=+0.184, p=0.025），与 Few-NERD 方向相反且已排除\\n    frequency confound。说明 embedding-based BCS 是 task-specific proxy：对 NER 有效（type\\n    name 相似度驱动 confusion），对 ED 无效（trigger word 歧义驱动 confusion，非 type name embedding\\n    距离）。Reframe 方向：BCS proxy 有局限 → 需要 empirical confusability（从 actual confusion matrix\\n    推导）→ SDGD-cal 用 empirical calibration 解决跨任务泛化。这让 SDGD-cal 成为比 SDGD-zero 更核心的贡献。\\n  related_experiments:\\n  - exp_id: exp004_maven_bcs\\n    role: trigger\\n    result: MAVEN per-type ρ=+0.184 contradicts hypothesis\\n  - exp_id: exp003a_prompt_v2_rerun\\n    role: baseline\\n    result: Few-NERD per-type ρ=-0.293 supports hypothesis\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-15 07:37 UTC\\n  summary: FewRel pilot PASS (D007)，commit RE 为第三任务；需做 embedding ablation (MiniLM\\n    vs Qwen3 × 3 tasks)\\n  rationale: FewRel pilot 显示高 BCS→低 accuracy（Δ=-21~50pp），效应量极大，假设方向正确。但使用了 MiniLM（BCS\\n    range 0.42-0.97）而非 Qwen3（Few-NERD/MAVEN 用的）。三任务交叉对比显示：NER 弱负(Qwen3)、ED 反向(Qwen3)、RE\\n    强负(MiniLM)——无法区分 task effect vs embedding effect。需要 2×3 embedding ablation（MiniLM/Qwen3\\n    × NER/ED/RE）来厘清。这是 CPU 任务（重算 BCS 矩阵+重跑分析），成本极低但对论文 story 至关重要。\\n  related_experiments:\\n  - exp_id: fewrel_pilot\\n    role: trigger\\n    result: batch Δ=-21~50pp, hypothesis direction correct\\n  depends_on:\\n  - D007\\n  - D009\\n- id: D011\\n  date: 2026-05-15 07:41 UTC\\n  summary: '采用 Narrative A: embedding proxy 有域边界，same-domain 需 SDGD-cal empirical\\n    calibration'\\n  rationale: 三任务数据全用上：Few-NERD(NER)+FewRel(RE) 作为 cross-domain positive evidence，MAVEN(ED)\\n    作为 same-domain boundary condition。自然引出 SDGD-zero(embedding proxy, cross-domain)\\n    vs SDGD-cal(empirical confusion, task-agnostic) 的互补关系。比方案B（需先验证SDGD-cal）更安全，比方案C（浪费MAVEN数据）更坦诚。Claim\\n    1 修改为含 boundary condition 的版本。\\n  related_experiments:\\n  - exp_id: exp004_maven_bcs\\n    role: boundary_condition\\n    result: MAVEN per-type ρ=+0.184 positive\\n  - exp_id: fewrel_pilot\\n    role: cross_task_replication\\n    result: Δ=-21~50pp strong negative\\n  - exp_id: exp003a_prompt_v2_rerun\\n    role: primary_evidence\\n    result: Few-NERD per-type ρ=-0.293\\n  depends_on:\\n  - D009\\n  - D010\\n- id: D012\\n  date: 2026-05-15 09:06 UTC\\n  summary: 证据层级重排：pairwise SCS→confusion 为唯一主要证据，per-type 降为辅助（centrality confound）\\n  rationale: MAVEN MiniLM ablation 证实 per-type 正向与 embedding 选择无关（MiniLM ρ=+0.208,\\n    Qwen3 ρ=+0.184 方向一致）。但 MiniLM pairwise 在 MAVEN 上显著（r=+0.120, p≈0），Qwen3 无信号。说明：(1)\\n    pairwise confusability 在所有数据集上真实存在，(2) per-type mean BCS 混合了 confusability 和 type\\n    centrality（语义邻居多=常见类型=LLM 擅长=高 F1），频率控制无法完全消除。论文主要证据应聚焦 pairwise SCS→confusion\\n    + FewRel batch-level 强效应，per-type 作为辅助，MAVEN per-type 正向作为 centrality confound\\n    案例研究。\\n  related_experiments:\\n  - exp_id: exp004_maven_bcs\\n    role: evidence\\n    result: MiniLM pairwise r=+0.120 significant; per-type positive both embeddings\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-15 09:07 UTC\\n  summary: Narrative 精化：核心论点从 embedding domain boundary 改为 pairwise vs aggregation\\n    level confound\\n  rationale: MAVEN MiniLM ablation 证实 per-type 正向与 embedding 无关（MiniLM 无压缩也正向）。问题是\\n    per-type 聚合的 centrality confound，非 embedding proxy 失效。但 MiniLM pairwise 在 MAVEN\\n    上显著（r=+0.120）→ pairwise confusability 跨任务普遍存在。SDGD 直接用 pairwise similarity 做 graph\\n    coloring，绕过聚合 confound。论文核心论点：confusability 在 type-pair 级别操作，per-type aggregation\\n    在同域 schema 引入 centrality confound，SDGD 的 pairwise 设计天然规避此问题。2×3 embedding ablation\\n    矩阵本身成为论文 Table。\\n  related_experiments:\\n  - exp_id: exp004_maven_bcs\\n    role: evidence\\n    result: MiniLM pairwise r=+0.120 on MAVEN; per-type positive both embeddings\\n  depends_on:\\n  - D012\\n- id: D014\\n  date: 2026-05-15 11:20 UTC\\n  summary: SDGD-zero 差于 baseline，Claim 3 需重大调整或放弃\\n  rationale: exp-008 SDGD-zero F1=0.251 < single_pass=0.445 < random_batch=0.320。根因：merge\\n    amplifies hallucination——每个 batch 处理全部样本但 schema 受限，模型过度预测 batch 内类型，merge 累积\\n    FP。confusability-aware 分解比随机分组差可能因为语义不相关 types 混合导致模型缺少 disambiguation context。Claims\\n    1-2（confusability 分析）不受影响。需要决定：(A) 修复 merge 策略重跑 (B) SDGD 降为 discussion/future\\n    work (C) 等 SDGD-cal 结果再定。\\n  related_experiments:\\n  - exp_id: exp008_sdgd_zero_fewnerd\\n    role: trigger\\n    result: SDGD-zero F1=0.251 < single_pass=0.445\\n  depends_on:\\n  - D013\\n- id: D015\\n  date: 2026-05-15 13:39 UTC\\n  summary: SDGD v2 time-boxed probe (2h) before multi-model; fail → Claim 3 降为 future\\n    work\\n  rationale: SDGD-zero 负向(F1=0.251 vs single_pass=0.445)，根因 merge amplification 已诊断。v2\\n    修复(min_batch_size+confidence-gated merge)成本仅2h，成功则论文获 prescriptive contribution，失败不伤\\n    Claims 1-2。距 DDL 10 天，串行 v2→exp-012 时间充裕。成功标准：v2 F1 > 0.445。\\n  related_experiments:\\n  - exp_id: exp-008\\n    role: evidence\\n    result: 'negative: SDGD-zero F1=0.251, merge amplification confirmed'\\n  - exp_id: exp-012\\n    role: next\\n    result: 'planned: multi-model validation after v2 probe'\\n  depends_on: []\\n- id: D016\\n  date: 2026-05-15 14:57 UTC\\n  summary: exp-012 flashinfer 不兼容 Blackwell，SDGD v2 先占 GPU，flashinfer 并行修复\\n  rationale: vLLM 0.20.2 废弃 VLLM_ATTENTION_BACKEND 环境变量，flashinfer 0.6.8 无法为 SM120\\n    JIT 编译 FP8 GEMM。两次启动失败。Agent 正确决策：(1) SDGD v2 立即占 GPU 不浪费；(2) CPU worker 并行升级\\n    flashinfer + CUDA 13 nvcc；(3) exp-012 r3 排 SDGD v2 之后 (~17:30 UTC)。\\n  related_experiments:\\n  - exp_id: exp-012\\n    role: blocked\\n    result: flashinfer SM120 incompatibility\\n  - exp_id: exp-008\\n    role: retry\\n    result: SDGD v2 probe started, F1>0.445 threshold\\n  depends_on:\\n  - D015\\n  - D014\\n- id: D017\\n  date: 2026-05-15 15:00 UTC\\n  summary: Reviewer 深度审查后调整实验矩阵：exp-006/005 降优，加 3 个 0-GPU-hour 分析，SDGD v2 阈值放宽到 F1>0.40\\n  rationale: 80-rel scaling data (3.4x amplification) 已覆盖 exp-006 interaction effect。3\\n    tasks 足够，exp-005 DocRED 降 P2。Reviewer 建议 3 个 0-GPU-hour 高 ROI 分析：(1) FewRel pairwise\\n    error taxonomy 跨任务验证 Claim 2；(2) bootstrap 95% CI 加固所有 correlation；(3) exp-015\\n    fast SCS→confusion validation。SDGD v2 阈值从 F1>0.445 放宽到 F1>0.40（接近 baseline 也有\\n    story：decomposition 损失可控 + latency 优势），F1<0.35 则 drop Claim 3。Claim 表述用具体数据\\\"3.4x\\n    amplification between 16-type and 80-type\\\"替代函数形式声明。\\n  related_experiments:\\n  - exp_id: exp_fewrel_formal_80rel\\n    role: evidence\\n    result: 3.4x BCS effect scaling\\n  - exp_id: exp-006\\n    role: deprioritized\\n    result: covered by 80-rel scaling\\n  - exp_id: exp-005\\n    role: deprioritized\\n    result: P2, 3 tasks sufficient\\n  - exp_id: exp-008\\n    role: retry\\n    result: v2 running, threshold F1>0.40\\n  depends_on:\\n  - D015\\n  - D016\\n- id: D018\\n  date: 2026-05-15 15:10 UTC\\n  summary: 补充 40-rel 中间点 + 多模型备选方案（AWQ/8B）+ MAVEN case study\\n  rationale: Reviewer 二次审查指出：(1) 2 点 scaling 不够，40-rel 中间点 ~1 GPU-hour 可得 3 点 scaling\\n    curve；(2) exp-012 双 retry 失败，需备选方案——Llama-70B-AWQ 或 Llama-8B，并行下载不等 r3；(3) MAVEN\\n    case study 0 GPU-hour 补强 centrality confound narrative。多模型验证是投稿硬门槛，24h 内必须完成。\\n  related_experiments:\\n  - exp_id: exp-012\\n    role: critical_path\\n    result: dual retry failed, backup plan needed\\n  - exp_id: exp_fewrel_formal_80rel\\n    role: evidence\\n    result: need 40-rel middle point for 3-point scaling\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-15 15:47 UTC\\n  summary: SDGD v2 confirmed negative, kill per_type early, Claim 3 dropped — pivot\\n    to analysis-only paper\\n  rationale: 'SDGD v2 confidence-gated merge: sdgd_zero F1=0.241, random_batch F1=0.301,\\n    both far below baseline 0.445 and threshold F1>0.40 (D017). Per_type 66-type sequential\\n    inference blocking GPU for exp-012 critical path. v1 per_type was also below baseline\\n    (0.2915). Decomposition paradigm has intrinsic FP amplification that merge strategies\\n    cannot fully resolve. Claim 3 dropped; SDGD discussed as future work. Paper pivots\\n    to 2-claim analysis: (1) confusability independence + scaling, (2) multi-channel\\n    degradation mechanism.'\\n  related_experiments:\\n  - exp_id: exp-008\\n    role: evidence\\n    result: 'SDGD v2 negative: sdgd_zero=0.241, random=0.301, baseline=0.445'\\n  - exp_id: exp-012\\n    role: critical_path\\n    result: unblocked by killing SDGD per_type\\n  depends_on:\\n  - D017\\n  - D015\\n  - D014\\n- id: D020\\n  date: 2026-05-15 16:02 UTC\\n  summary: 启动 Paper Agent 写作，2-claim analysis paper + SDGD negative result，Dream 结构性问题同步解决\\n  rationale: Claims 1+2 证据链完整（3 任务 × 多层证据），exp-012 最后 P0 可 Patch。10 天 deadline，Paper\\n    Agent 24h pipeline 必须立即启动。Dream 两轮均 Weak Reject，主要因写作质量（related work 2 refs, effect\\n    size 未 contextualize, metric undefined）非证据不足——这些是写作阶段能解决的问题。\\n  related_experiments:\\n  - exp_id: exp-012\\n    role: pending P0, Patch in when done\\n  - exp_id: dream_20260515T140829\\n    role: structural issues identified\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-15 16:05 UTC\\n  summary: 40-rel 中间点升 P0，利用 AWQ 下载期间 GPU 空闲立即执行\\n  rationale: Scaling claim 仅 2 个数据点（16-rel=9.1pp, 80-rel=31.2pp），审稿人必问线性 vs 非线性。40-rel\\n    中间点 ~1 GPU-hour，Qwen3 已在服务器上无需下载，AWQ 下载期间 GPU 完全空闲，零机会成本。\\n  related_experiments:\\n  - exp_id: exp_fewrel_formal_80rel\\n    role: scaling baseline\\n  - exp_id: exp_fewrel_formal\\n    role: 16-rel baseline\\n  - exp_id: exp-012\\n    role: AWQ downloading, GPU idle\\n  depends_on:\\n  - D018\\n  - D020\\n- id: D022\\n  date: 2026-05-15 16:23 UTC\\n  summary: exp012 放弃 70B AWQ，转用 LLaMA-3.1-8B-Instruct\\n  rationale: 70B 在 Blackwell 上连续 3 轮失败（r1/r2 flashinfer 不兼容，AWQ 磁盘空间不足无法完成下载）。8B 已下载就绪，BF16\\n    直接加载无兼容性风险。跨 family + 跨 scale（Qwen3-32B → LLaMA-8B）的验证比同 scale 不同 family 更有论文价值——证明\\n    confusability 效应不依赖模型容量。DDL 仅剩 10 天，不能继续在 70B 兼容性上耗时间。\\n  related_experiments:\\n  - exp_id: exp-012\\n    role: target\\n    result: switching from 70B to 8B\\n  - exp_id: exp012_llama_fewnerd_r3\\n    role: predecessor\\n    result: failed (AWQ disk space insufficient)\\n  - exp_id: exp012_llama_fewnerd_r2\\n    role: predecessor\\n    result: failed (flashinfer incompatible)\\n  depends_on:\\n  - D020\\n  - D021\\n- id: D023\\n  date: 2026-05-15 16:50 UTC\\n  summary: exp012 多模型验证策略：先试 free-form generation 诊断，失败则接受 single-model limitation\\n  rationale: exp012 全系列失败（r1-r3 flashinfer SM120 不兼容，AWQ 磁盘不足，r4 8B 零预测）。8B 零输出最可能原因是\\n    vLLM structured output JSON schema 与 LLaMA tokenizer 不兼容（gen_tokens=2 = 只输出 `[]`）。诊断方案：关闭\\n    structured output 约束做 free-form generation + regex 后处理，~15 min 即可验证。成功则重跑，失败则在论文\\n    §6.3 接受 single-model limitation（Qwen3-32B 已有 3 任务 × 多层证据，单模型不构成致命弱点）。DDL 仅剩 10\\n    天，不再尝试下载新模型或升级 CUDA toolkit。\\n  related_experiments:\\n  - exp_id: exp012_llama_fewnerd_r4\\n    role: trigger\\n    result: failed - zero predictions\\n  - exp_id: exp012_llama_fewnerd_r3\\n    role: predecessor\\n    result: failed - flashinfer SM120\\n  - exp_id: exp012_llama_awq\\n    role: predecessor\\n    result: killed - disk space\\n  depends_on:\\n  - D022\\n- id: D024\\n  date: 2026-05-15 16:53 UTC\\n  summary: 多模型验证硬截止 May 18；Paper Agent 立即启动 Full Draft（单模型版本，多模型结果到位后 Patch）\\n  rationale: 'Reviewer warning: exp-012 多模型验证已失败 6+ 次（70B flashinfer 不兼容, 8B 零预测）。距\\n    ARR May 25 仅 10 天，论文零产出。策略：(1) 给多模型验证 3 天窗口（截止 May 18），Agent 正在准备 exp012_llama_8b\\n    和 exp012_llama_awq；(2) 立即启动 Paper Agent 以当前单模型证据写 Full Draft——三任务 cross-task replication\\n    是部分替代；(3) May 18 前多模型仍失败则调整 claim 措辞为 \\\"We observe with Qwen3-32B\\\" 并在 Limitation\\n    明确承认，强化 cross-task angle。不预先降级，先推进。'\\n  related_experiments:\\n  - exp_id: exp-012\\n    role: multi-model validation\\n    result: 6+ failures, still attempting\\n  - exp_id: exp-002\\n    role: primary evidence\\n    result: success\\n  - exp_id: exp-004\\n    role: cross-task MAVEN\\n    result: success\\n  - exp_id: exp-016\\n    role: cross-task FewRel\\n    result: success\\n  depends_on:\\n  - D022\\n  - D019\\n- id: D025\\n  date: 2026-05-15 18:10 UTC\\n  summary: Table 3 NER Missed 数据修正：12/14/16% 替换为实际计算值 42.8/64.8/49.9%，叙事从\\\"BCS不影响检测\\\"改为\\\"NER与RE错误机制不同\\\"\\n  rationale: Agent + Reviewer 双重验证确认 Table 3 NER Missed 12%/14%/16% 无任何实验 artifact\\n    支撑，疑似从 RE 数据外推（+2pp）。实际从 exp007 raw predictions 重新计算的值为 low=42.8%, medium=64.8%,\\n    high=49.9%，差距 30-50pp 且趋势非 flat。原叙事\\\"missed rate remains flat at 10-16%\\\"在 NER 端不成立，需限定为仅\\n    RE。NER/RE 差异本身是有意义的发现，可加强分析深度。\\n  related_experiments:\\n  - exp_id: exp007_error_taxonomy\\n    role: source\\n    result: NER missed rates 42.8/64.8/49.9% (recomputed)\\n  - exp_id: exp016_fewrel_error_taxonomy\\n    role: source\\n    result: RE missed rates 10.4/11.3/13.1/15.7% (registry verified)\\n  depends_on: []\\n- id: D026\\n  date: 2026-05-15 18:36 UTC\\n  summary: exp006 交互效应不显著(p=0.505)，结论 negative；不在论文主体引用，至多作为 supplementary exploratory\\n    analysis\\n  rationale: 2×2 factorial 设计（count × BCS）的交互项 z=-0.667, p=0.505, estimate=-0.036，完全在噪声范围内。此外设计存在结构性混淆：BCS\\n    与 count 不正交（high count 的 BCS floor 被推高），high_count/high_bcs 的 10 个 batch BCS 完全相同（伪重复）。Reviewer\\n    建议禁止声称 multiplicative interaction。实验为 P1（D017 降优），paper story 不依赖此结果。资源转向 exp012（P0\\n    多模型验证）。\\n  related_experiments:\\n  - exp_id: exp006_interaction_2x2\\n    role: primary\\n    result: 'negative: interaction z=-0.667, p=0.505, not significant'\\n  depends_on:\\n  - D017\\n- id: D027\\n  date: 2026-05-15 20:01 UTC\\n  summary: exp012 exp1 跨模型验证成功：Channel 1 (count→recall) 在 LLaMA-3.1-8B 上复现，per-batch\\n    r=0.725\\n  rationale: LLaMA-3.1-8B recall 从 0.702 降至 0.273（-43pp），Qwen3-32B 从 0.640 降至 0.304（-34pp）。Per-batch\\n    correlation r=0.725 表明 schema 配置是困难的主要来源而非模型特异性。弱模型下降更陡，支持 schema complexity as\\n    task-inherent difficulty 叙事。exp1 数据已交 Paper Agent 写入论文。exp2（Channel 2 BCS-controlled）正在重跑。\\n  related_experiments:\\n  - exp_id: exp012_llama_8b_r2\\n    role: primary\\n    result: 'exp1 success: recall decline -43pp, per-batch r=0.725 with Qwen3-32B'\\n  depends_on: []\\n- id: D028\\n  date: 2026-05-15 20:34 UTC\\n  summary: exp012 exp2 Channel 2 跨模型复现失败：极端 batch 方向正确但效果微弱(5pp/4.3pp)，随机 batch 信号淹没在\\n    noise 中。论文不引用 exp2 数据，保持 Limitations 中\\\"Channel 2 pending\\\"的保守表述\\n  rationale: LLaMA-3.1-8B 上 BCS-controlled 效应远弱于 Qwen3-32B（Δ5pp vs 31.2pp），count_12\\n    的 BCS 分布压缩严重（Δ0.030），多个随机 batch 出现反向趋势（高 BCS 反而高 F1）。per_type_f1 全为 0（缺 char offset），无法做\\n    error taxonomy 分析。floor effect + BCS 压缩 + 模型能力不足共同导致信号不可检测。当前论文 Limitations 只\\n    claim Channel 1 replicated，这是最安全的策略。\\n  related_experiments:\\n  - exp_id: exp012_llama_8b_r2_exp2\\n    role: primary\\n    result: 'Channel 2 not replicated: extreme Δ=5pp/4.3pp, random batches noisy with\\n      counter-examples'\\n  depends_on:\\n  - D027\\n- id: D029\\n  date: 2026-05-15 21:12 UTC\\n  summary: 提分策略：(1) 40-rel 中间点已启动；(2) LLaMA-8B FewRel Channel 2 作为第二实验；(3) \\\"pending\\\"改诚实报告；目标\\n    7→8+\\n  rationale: Reviewer 独立评估：40-rel 提分 +0.5-0.75（3点scaling curve），LLaMA FewRel Channel\\n    2 提分 +0.75 if positive / +0.25 if negative（FewRel 效应大、metric 无 span 噪声，比 NER 更可能检测到跨模型信号）。\\\"pending\\\"\\n    改诚实报告避免信任风险（-0.5 vs -1.5）。最乐观 8.0-8.5，最可能 7.5-8.0。\\n  related_experiments:\\n  - exp_id: exp_fewrel_40rel_r4\\n    role: planned\\n    result: PREPARING\\n  - exp_id: exp012_llama_fewrel\\n    role: planned\\n    result: not yet created\\n  depends_on:\\n  - D027\\n  - D028\\n- id: D030\\n  date: 2026-05-15 22:37 UTC\\n  summary: exp012 两种场景预案：正向升级 cross-family claim（有限度），负向 frame 为 capacity-dependent\\n    finding；两种场景都诚实报告，不追加新模型\\n  rationale: Reviewer 预判分析：场景 A 诚实报告 7.5-8.0 分，场景 B 诚实报告 7.0-7.5 分，隐藏则 6.0-6.5。不追加模型因\\n    DDL 10 天内边际收益递减。3 tasks × 1 model 的任务多样性论点比 cross-model 更强。Claim 安全边界受 C001（40-rel\\n    来自 80-pool）和 C002（BCS amplification 仅 2 schema sizes）约束。\\n  related_experiments:\\n  - exp_id: exp012_llama_fewrel_ch2\\n    role: trigger\\n    result: running\\n  depends_on:\\n  - D022\\n- id: D031\\n  date: 2026-05-15 22:40 UTC\\n  summary: exp012 强复现（场景 A），执行 claim 升级 + 新发现\\\"model-invariant high-BCS floor\\\"加入正文\\n  rationale: LLaMA-8B BCS effect -27.1pp/-23.9pp 远超强复现阈值(15pp)，达 Qwen3 的 75-87%。高\\n    BCS 准确率跨模型恒定(0.510 vs 0.510)是预案外的新发现，表明 confusability 是 task-inherent difficulty\\n    而非 model-specific。Reviewer 评估提分至 7.75-8.25。按 D030 场景 A 预案执行 patch。NER negative\\n    由 metric/floor effect 解释，诚实报告。\\n  related_experiments:\\n  - exp_id: exp012_llama_fewrel_ch2\\n    role: evidence\\n    result: 'strong_positive: BCS Δ=-27.1pp(count_8)/-23.9pp(count_16), high-BCS floor\\n      model-invariant at 0.51'\\n  depends_on:\\n  - D030\\n  - D022\\n- id: D032\\n  date: 2026-05-15 22:41 UTC\\n  summary: 激活场景 A：Channel 2 跨模型复现成功，升级 claim 表述，不追加新模型，聚焦写作\\n  rationale: exp012 LLaMA-8B FewRel Δ=-27.1pp/-23.9pp，强复现。高 BCS floor 跨模型恒定(~0.51)是新发现。Reviewer\\n    预估 7.75-8.25。DDL 10 天内不追加模型，边际收益递减且风险高。Paper Agent 执行 Scene A patch。\\n  related_experiments:\\n  - exp_id: exp012_llama_fewrel_ch2\\n    role: evidence\\n    result: 'success: Δ=-27.1pp(count_8), -23.9pp(count_16), high-BCS floor model-invariant\\n      ~0.51'\\n  depends_on:\\n  - D030\\n  - D022\\n- id: D033\\n  date: 2026-05-16 00:23 UTC\\n  summary: 追加 16-rel 100 random batches + bootstrap CI 实验，填补 tab:bcs_controlled 空白\\n    + amplification ratio 正式 CI\\n  rationale: Reviewer 评估 Soundness 3→4 最高 ROI 方案：1-2 GPU 小时，消除表格 \\\"---\\\" 空白，让 3.4× amplification\\n    获得双端 CI 支撑。90% 概率正面结果。方案 2（FewRel pairwise）和方案 3（额外 seed）ROI 不足跳过。\\n  related_experiments:\\n  - exp_id: exp_fewrel_formal\\n    role: baseline\\n    result: 16-rel 单 batch Δ=9.1pp 无 CI\\n  depends_on:\\n  - D031\\n- id: D034\\n  date: 2026-05-16 01:55 UTC\\n  summary: Amplification 报告策略：同时报告 quartile Δ 和 BCS-accuracy 回归斜率，用斜率比较作为公平的 amplification\\n    证据（消除 BCS 域不重叠问题）\\n  rationale: D033 结果 Δ=-7.42pp（quartile）vs 原 -9.1pp（extreme batch），方法论不对称导致 ratio\\n    从 3.4× 变 4.2×。Reviewer 指出 80-pool-within BCS 范围 [0.47,0.65] 与 16-rel [0.65,0.90]\\n    几乎不重叠，Q4-Q1 Δ 不直接可比。斜率比较是标准化后的公平指标：如果斜率随 pool size 增大，则 amplification 成立且不受 BCS\\n    域差异影响。论文将报告两种指标（Δ + slope），以 slope 为主要 amplification 证据。\\n  related_experiments:\\n  - exp_id: exp_fewrel_16rel_bootstrap\\n    role: evidence\\n    result: Δ=-7.42pp CI[-9.45,-4.49], r=-0.6373\\n  - exp_id: exp_fewrel_80pool_16sub_bootstrap\\n    role: pending\\n    result: PREPARING\\n  depends_on:\\n  - D033\\n- id: D035\\n  date: 2026-05-16 01:58 UTC\\n  summary: D033 集成采用极端批次方法重算，保持 Table 3 方法一致性\\n  rationale: D033 bootstrap_ci.json 的 amplification 4.2× 混用了极端批次(80-rel分子)和四分位(16-rel分母)两种方法。论文\\n    Table 3 统一用极端批次比较，因此需用 D033 的 100 batch 数据按极端批次方法重算 16-rel Δ 和 CI。四分位 CI 作补充证据放正文，展示跨分析粒度稳健性。\\n  related_experiments:\\n  - exp_id: exp_fewrel_16rel_bootstrap\\n    role: source_data\\n    result: success, Δ_quartile=7.42pp\\n  - exp_id: exp_fewrel_80pool_16sub_bootstrap\\n    role: pending_comparison\\n    result: allocated_not_started\\n  depends_on: []\\n- id: D036\\n  date: 2026-05-16 02:14 UTC\\n  summary: D035 修订：Table 3 以回归斜率为主指标，四分位 Δ 为辅\\n  rationale: 80-pool 四分位 Δ=-3.92pp CI 跨零（[-7.79, +0.42]），但回归斜率=-0.401 CI 排除零（[-0.684,\\n    -0.062]）。两组斜率可比（-0.449 vs -0.401），说明 per-unit-BCS 效应一致。原 D035 计划用极端批次 Δ 做 Table\\n    3 主指标，但数据表明斜率是更稳健的指标。BCS range 差异（16-rel [0.65,0.90] vs 80-pool [0.46,0.68]）解释了四分位对比的弱化——80-pool\\n    类型多样性压缩了 BCS 对比空间。\\n  related_experiments:\\n  - exp_id: exp_fewrel_80pool_16sub_bootstrap\\n    role: primary\\n    result: slope=-0.401 significant, quartile CI crosses zero\\n  - exp_id: exp_fewrel_16rel_bootstrap\\n    role: comparison\\n    result: slope=-0.449, quartile significant\\n  depends_on:\\n  - D035\\n- id: D037\\n  date: 2026-05-16 03:13 UTC\\n  summary: 'D037: Round 2 审稿 Action Matrix 定稿——5C+12W 逐条方案，C1 需 v2 BCS-controlled\\n    RE 实验'\\n  rationale: Round 2 borderline (3.0/5)。Reviewer 独立审查确认：(1) C1 prompt 混淆是唯一可能推翻核心贡献的项，仅公开\\n    prompt 不够，需 v2 RE BCS-controlled 子集验证；(2) C2/C3 通过 D036 slope 叙事已部分解决，需清除 Abstract\\n    残留的 9.1pp vs 31.2pp 直接对比；(3) C4/C5 是 desk-reject 风险必须首先解决；(4) W3 cluster bootstrap\\n    是 CPU 工作可并行；(5) W5 SDGD on RE 优先级低于 C1。执行计划：Day 1 C5+C4+C1(prompt+实验)+W3+W4，Day\\n    2-3 编辑工作，Day 4-5 W5 if time。\\n  related_experiments:\\n  - exp_id: exp-003a\\n    role: v1/v2 comparison baseline\\n    result: v2 有 count curve 和 within-count 数据但无 BCS-controlled RE\\n  - exp_id: exp_fewrel_formal\\n    role: core RE evidence\\n    result: v2 prompt, BCS Δ=-31.2pp\\n  depends_on:\\n  - D036\\n- id: D038\\n  date: 2026-05-16 04:35 UTC\\n  summary: 'D038: BCS 定义不一致修复——统一为 MEAN pairwise SCS，重算 Table 4 + permutation test'\\n  rationale: Reviewer 发现 compute_bcs.py 用 MAX pairwise SCS，而论文定义和 80-pool 实验用 MEAN。16-rel\\n    bootstrap 和 80-rel formal 的 BCS 在错误 scale 上，导致 permutation test（p=0.436）混合了不同度量的斜率。方向性结论不变（斜率均为负），但精确数值和\\n    p 值需重算。修复为纯 CPU 工作（从现有 SCS matrix 重算），不需要重跑 GPU 实验。\\n  related_experiments:\\n  - exp_id: exp_fewrel_16rel_bootstrap\\n    role: affected\\n    result: BCS 用了 MAX，需重算为 MEAN\\n  - exp_id: exp_fewrel_formal_80rel\\n    role: affected\\n    result: BCS 用了 MAX，需重算为 MEAN\\n  - exp_id: exp_fewrel_80pool_16sub_bootstrap\\n    role: reference\\n    result: 已用 MEAN，无需修改\\n  depends_on:\\n  - D036\\n  - D037\\n- id: D039\\n  date: 2026-05-16 04:49 UTC\\n  summary: 'D039: BCS 统一选择 Path A (MEAN)——科学诚实优先，MAX 作 sensitivity analysis 报告'\\n  rationale: Path A (MEAN BCS) vs Path B (MAX BCS)：选择 MEAN 因为 (1) 论文公式原本就定义 MEAN，改\\n    MAX 有 metric shopping 嫌疑；(2) 核心结论不变——r=-0.467 仍 p<1e-6，Δ=-5.3pp CI 排除零；(3) permutation\\n    p=0.60 反而比旧 0.44 更支持 slope consistency claim；(4) 80-rel 斜率翻正是 BCS range 太窄 (IQR=0.033)\\n    导致的噪声，注明即可。MAX BCS 可在 appendix 作 sensitivity analysis 报告。\\n  related_experiments:\\n  - exp_id: exp_fewrel_16rel_bootstrap\\n    role: affected\\n    result: 'r: -0.637→-0.467, Δ: -7.4pp→-5.3pp'\\n  - exp_id: exp_fewrel_formal_80rel\\n    role: affected\\n    result: slope 翻正(+0.221 n.s.), BCS range=0.089 太窄\\n  - exp_id: exp_fewrel_80pool_16sub_bootstrap\\n    role: reference\\n    result: 已是 MEAN, 无变化\\n  depends_on:\\n  - D038\\n- id: D040\\n  date: 2026-05-16 05:31 UTC\\n  summary: v2 RE n=25 结果推翻 attenuation 叙述，升级为 \\\"confusability is task-inherent, not\\n    prompt artifact\\\"\\n  rationale: v2 prompt n=25 实验显示 Δ=25.5pp (CI [22.4,28.6], p<0.0001, r=−0.919)，效应巨大且高度显著。此前\\n    n=5 不显著是 underpowered + narrow BCS contrast (0.21 vs 0.44) 导致的伪阴性。v2 不消除效应意味着\\n    confusability 是 task-inherent property，直接回应 \\\"prompt artifact\\\" reviewer concern。论文\\n    §4.3、Introduction、Appendix G 均需更新，paper_framing.md 的 prompt sensitivity concern\\n    从 partially addressed 升级为 addressed。\\n  related_experiments:\\n  - exp_id: exp_v2_re_n25\\n    role: primary evidence\\n    result: Δ=25.5pp, r=−0.919, p<0.0001\\n  depends_on: []\\n- id: D041\\n  date: 2026-05-16 06:58 UTC\\n  summary: 放弃 exp-017 GPT-4o-mini：TUM proxy 未部署，AutoDL 无法访问 OpenAI API，不值得搭建基础设施\\n  rationale: AutoDL 服务器无法直接访问 OpenAI API（TUM proxy service not deployed）。距 DDL 9 天，debug\\n    基础设施的 ROI 太低。当前 2 模型族 (Qwen3-32B + LLaMA-3.1-8B) 满足跨模型验证基本要求，Discussion 已有 model\\n    coverage limitation 表述。exp-018 batch composition 的 practical contribution 优先级更高。\\n  related_experiments:\\n  - exp_id: exp017_gpt4o_mini_fewrel\\n    role: cancelled\\n    result: 'BLOCKED: TUM proxy not deployed'\\n  depends_on: []\\n- id: D042\\n  date: 2026-05-16 07:38 UTC\\n  summary: exp-018 成功：confusability-aware batching 在 RE 上 +1.44pp (显著)，无 merge amplification。进入论文收尾阶段。\\n  rationale: Graph coloring BCS 最小化分组 accuracy 0.8021 > random 0.7877±0.0178 (超 95%\\n    CI 上界 0.7967)，single_pass 0.5042 验证 schema overload。RE closed-set 无 merge amplification，与\\n    NER SDGD 失败形成对比。论文从纯诊断升级为诊断+缓解，直接回应 W6 (§5 过短) 和 SDGD 缺 actionable takeaway 的审稿意见。距\\n    DDL 9 天，核心实验已全部完成，进入写作集成 + final review。\\n  related_experiments:\\n  - exp_id: exp_confusability_batch_composition\\n    role: primary evidence\\n    result: aware=0.8021 > random=0.7877, single_pass=0.5042\\n  depends_on: []\\n- id: D043\\n  date: 2026-05-16 07:44 UTC\\n  summary: D042 修正：exp-018 confusability-aware 与 random 无显著差异 (p≈0.22)，oracle routing\\n    使 \\\"无 merge\\\" 为空真。§5 写法降级。\\n  rationale: Reviewer critical 审查发现：(1) 统计检验错误——单点 vs mean CI 不是合法检验，排名法 p≈0.19，z\\n    检验 p=0.22；(2) 实验用 oracle routing（每个样本只路由到含 gold type 的 batch），根本没有 merge 步骤，\\\"无\\n    merge amplification\\\"是空真。+29.8pp 是纯 count 效应（80→10 types），confusability-aware 额外收益\\n    +1.44pp 不显著。§5 写法从\\\"诊断+缓解\\\"降级为\\\"RE oracle routing decomposition 有效（count 效应）+ confusability-aware\\n    方向一致但不显著\\\"。\\n  related_experiments:\\n  - exp_id: exp_confusability_batch_composition\\n    role: re-evaluated\\n    result: aware vs random p≈0.22 n.s.; oracle routing, no actual merge\\n  depends_on:\\n  - D042\\n\", \"total_chars\": 27674, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2ee817f-e3a3-483d-8c0c-1d4e2b093480",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "91d45bbd-728d-43f5-b12e-1623bde9f799",
  "sourceToolAssistantUUID": "a2ee817f-e3a3-483d-8c0c-1d4e2b093480",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-16T08:18:44.217Z_

Now I have a comprehensive understanding of the paper, its experimental design, decision history, and results. Let me load the submission tool and write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91d45bbd-728d-43f5-b12e-1623bde9f799",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vHJZZBFZwTB4WRgZA9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02d4703c-dabf-4fca-8811-41c0b3295681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FLKLZ3Bw6ACKt5DC1thuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17434,
      "cache_read_input_tokens": 52736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17434,
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

_source line 46 · 2026-05-16T08:18:45.170Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EzecMth23gUap5sX6Pe876`</summary>

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
  "parentUuid": "02d4703c-dabf-4fca-8811-41c0b3295681",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vHJZZBFZwTB4WRgZA9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c757216-9734-415d-b5cf-ee1f6f1945c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FLKLZ3Bw6ACKt5DC1thuu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17434,
      "cache_read_input_tokens": 52736,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17434
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 52736,
          "cache_creation_input_tokens": 17434,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17434,
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

_source line 47 · 2026-05-16T08:18:45.173Z_

<details><summary>↩ Tool result · `toolu_01EzecMth23gUap5sX6Pe876`</summary>

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
  "parentUuid": "2c757216-9734-415d-b5cf-ee1f6f1945c0",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "a251f679-80b4-425e-8303-3ec9bd469ddc",
  "sourceToolAssistantUUID": "2c757216-9734-415d-b5cf-ee1f6f1945c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-16T08:18:48.105Z_



Now let me also check the latest dream ID to use.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a251f679-80b4-425e-8303-3ec9bd469ddc",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vHgrFLr9hYvn7TheKB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15a7979b-9833-4c7f-90e2-be32d036f1f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bk3WdRBx5xvnkVFGuqbLw1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 70170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 699,
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

_source line 49 · 2026-05-16T08:18:49.785Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FLhFqDyL2QtSu2qcW8oMwm`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/",
  "description": "List dream report directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15a7979b-9833-4c7f-90e2-be32d036f1f5",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vHgrFLr9hYvn7TheKB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ff0ba11-185a-4878-a06c-d5a1ae7b701e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bk3WdRBx5xvnkVFGuqbLw1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 70170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 699,
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

_source line 50 · 2026-05-16T08:18:49.996Z_

<details><summary>↩ Tool result · `toolu_01FLhFqDyL2QtSu2qcW8oMwm`</summary>

```text
total 32
drwxr-xr-x  7 ubuntu ubuntu 4096 May 16 07:35 .
drwxr-xr-x 30 ubuntu ubuntu 4096 May 16 05:28 ..
drwxr-xr-x  3 ubuntu ubuntu 4096 May 15 02:48 dream_20260515T024826
drwxr-xr-x  6 ubuntu ubuntu 4096 May 15 06:32 dream_20260515T053106
drwxr-xr-x  6 ubuntu ubuntu 4096 May 15 12:38 dream_20260515T113743
drwxr-xr-x  6 ubuntu ubuntu 4096 May 15 14:57 dream_20260515T140829
drwxr-xr-x  6 ubuntu ubuntu 4096 May 16 08:02 dream_20260516T073533
lrwxrwxrwx  1 ubuntu ubuntu  125 May 15 14:57 latest -> /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ff0ba11-185a-4878-a06c-d5a1ae7b701e",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "93f9a203-e04d-4688-95c9-11e545aae5ab",
  "sourceToolAssistantUUID": "2ff0ba11-185a-4878-a06c-d5a1ae7b701e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T08:18:53.041Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PAdeFbWWAkq9qRFkxBM9De`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/",
  "description": "List latest dream report contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93f9a203-e04d-4688-95c9-11e545aae5ab",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vJ3K45T67y3skvU2t1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09a5e644-95ab-4b67-a0f7-11f808d8cdfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYQAvMN1D1ZYRQgL68Yt2t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 70869,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 442
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 70869,
          "cache_creation_input_tokens": 442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 442,
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

_source line 52 · 2026-05-16T08:18:53.137Z_

<details><summary>↩ Tool result · `toolu_01PAdeFbWWAkq9qRFkxBM9De`</summary>

```text
total 24
drwxr-xr-x 6 ubuntu ubuntu 4096 May 16 08:02 .
drwxr-xr-x 7 ubuntu ubuntu 4096 May 16 07:35 ..
drwxr-xr-x 2 ubuntu ubuntu 4096 May 16 08:12 best
drwxr-xr-x 2 ubuntu ubuntu 4096 May 16 08:17 logs
drwxr-xr-x 2 ubuntu ubuntu 4096 May 16 08:16 median
drwxr-xr-x 2 ubuntu ubuntu 4096 May 16 08:17 worst
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09a5e644-95ab-4b67-a0f7-11f808d8cdfe",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "92c50af2-531d-40fc-b11b-28dd3a47af71",
  "sourceToolAssistantUUID": "09a5e644-95ab-4b67-a0f7-11f808d8cdfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T08:18:56.250Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HvVe5LosrHeafZoQiZeoNx`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/",
  "description": "Check if review already exists for best tier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92c50af2-531d-40fc-b11b-28dd3a47af71",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vJGgy1cd2SAhe9BBQx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b602c496-7c47-42cd-9d91-55d59961200b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCjZgQ1amYeLGSu2db4wj1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 301,
      "cache_read_input_tokens": 71311,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 301
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 71311,
          "cache_creation_input_tokens": 301,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 301,
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

_source line 54 · 2026-05-16T08:18:56.306Z_

<details><summary>↩ Tool result · `toolu_01HvVe5LosrHeafZoQiZeoNx`</summary>

```text
total 352
drwxr-xr-x 2 ubuntu ubuntu   4096 May 16 08:12 .
drwxr-xr-x 6 ubuntu ubuntu   4096 May 16 08:02 ..
-rw-r--r-- 1 ubuntu ubuntu  30809 May 16 07:54 experiment_data.json
-rw-r--r-- 1 ubuntu ubuntu  29457 May 16 07:54 imagined_experiments.yaml
-rw-r--r-- 1 ubuntu ubuntu   9683 May 16 07:57 paper.aux
-rw-r--r-- 1 ubuntu ubuntu  19774 May 16 07:57 paper.log
-rw-r--r-- 1 ubuntu ubuntu   3017 May 16 07:57 paper.out
-rw-r--r-- 1 ubuntu ubuntu 152317 May 16 07:57 paper.pdf
-rw-r--r-- 1 ubuntu ubuntu  26037 May 16 07:57 paper.tex
-rw-r--r-- 1 ubuntu ubuntu  11744 May 16 07:54 paper_framing.md
-rw-r--r-- 1 ubuntu ubuntu  29446 May 16 08:06 review_context.yaml
lrwxrwxrwx 1 ubuntu ubuntu    140 May 16 08:06 review_input_db82206b.pdf -> /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.pdf
-rw-r--r-- 1 ubuntu ubuntu  12489 May 16 08:12 review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b602c496-7c47-42cd-9d91-55d59961200b",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "5359f29c-5630-487e-bd74-6f64d1bdaf19",
  "sourceToolAssistantUUID": "b602c496-7c47-42cd-9d91-55d59961200b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-16T08:19:01.231Z_

There's already a review_report.md. Let me check what tier this review should be for, and check the existing review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5359f29c-5630-487e-bd74-6f64d1bdaf19",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vJe2rvqGEL147t7rVk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a237e75-46f9-4dc0-b8a2-034ed0a71067",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018R3y27jZ9GdmApryJpasNL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 71612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 582,
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

_source line 56 · 2026-05-16T08:19:01.843Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DdKBssgwzMP1zarvRMc4ub`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a237e75-46f9-4dc0-b8a2-034ed0a71067",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vJe2rvqGEL147t7rVk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "190ad725-d27b-44c6-bd88-309443c86672",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018R3y27jZ9GdmApryJpasNL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 71612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 582,
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

_source line 57 · 2026-05-16T08:19:01.850Z_

<details><summary>↩ Tool result · `toolu_01DdKBssgwzMP1zarvRMc4ub`</summary>

```text
1	---
2	dream_id: dream_20260516T073533
3	tier: best
4	overall_score: Weak Accept (4/6)
5	timestamp: 2026-05-16T08:12:04.849232+00:00
6	---
7	
8	# Dream Review Report: Multi-Channel Schema Degradation in Training-Free LLM IE
9	
10	**Paper:** "Multi-Channel Schema Degradation in Training-Free LLM Information Extraction: Type Count and Confusability as Orthogonal Failure Modes"
11	
12	**Review Mode:** Full (2-reviewer roundtable)
13	
14	---
15	
16	## Roundtable Summary
17	
18	Two independent reviewers assessed this paper—R1 focusing on methods/experiments, R2 on novelty/related work. Both converged on **4/6 (Weak Accept)** with high confidence (4/5). The paper addresses a genuine gap in controlled empirical analysis of schema complexity in training-free LLM IE, with honest reporting and a sound experimental design. However, both reviewers raised convergent concerns about small effect sizes, limited actionable contribution, MAVEN results undermining the main narrative, and notable presentation gaps.
19	
20	---
21	
22	## Consolidated Strengths
23	
24	### S1: Well-Designed Controlled Experiments (R1, R2)
25	The two-paradigm approach—count curves (varying type count while recording BCS) and BCS-controlled comparisons (fixing count while varying confusability)—is a clean experimental design that properly isolates variables. The 2×2 factorial on Few-NERD adds a formal interaction test. This controlled methodology is, to the reviewers' knowledge, novel for training-free LLM IE evaluation.
26	
27	### S2: Compelling Error Taxonomy Analysis (R1)
28	The IntraSub scaling with BCS (ρ=1.0 on NER, ρ=0.954 on RE) across four BCS bins is the paper's strongest evidence. The observation that IntraSub rises from 0% to 49.4% while hallucination stays below 3% provides genuine mechanistic insight: LLMs' primary failure mode on complex schemas is type misassignment, not fabrication. Cross-task replication strengthens this finding.
29	
30	### S3: Honest Reporting of Effect Sizes and Negative Results (R1, R2)
31	The paper transparently reports that pairwise r²=1.3–1.7% (only ~1.5% of variance explained), does not overclaim on the SDGD negative result, and properly acknowledges limitations. This intellectual honesty is commendable.
32	
33	### S4: Centrality Confound as Methodological Contribution (R1, R2)
34	Both reviewers independently identified the centrality confound discovery on MAVEN (per-type BCS shows *positive* correlation with F1 on homogeneous schemas) as a genuine methodological contribution with implications beyond this paper. Future work on schema difficulty metrics should heed this finding.
35	
36	### S5: Cross-Task and Cross-Model Breadth (R2)
37	Testing across NER (Few-NERD), RE (FewRel, DocRED), and ED (MAVEN) with two extraction models (Qwen3-32B, LLaMA-3.3-70B) and two embedding families provides reasonable experimental breadth. The 87% cross-model consistency claim, while not shown in detail, supports generalizability.
38	
39	---
40	
41	## Consolidated Weaknesses
42	
43	### W1: Small Pairwise Effect Sizes Limit Practical Significance (R1, R2) — Major
44	The headline r=0.11–0.13 (r²≈1.5%) means SCS explains almost none of the variance in pairwise confusion. While statistically significant due to large n (1953+ pairs), this is too small to be actionable for schema design. The batch-level effects are larger (23–31pp extreme-batch gaps), but these compare hand-picked extremes—typical-batch BCS variation likely produces much smaller gaps. The paper bridges pairwise and batch evidence well in principle, but the disconnect between "statistically significant but tiny pairwise signal" and "large extreme-batch gap" should be discussed more explicitly as a limitation.
45	
46	### W2: MAVEN Results Undermine the Main Narrative (R1, R2) — Major
47	The MAVEN count curve reportedly goes in the *opposite* direction of the main hypothesis (the paper mentions this in Discussion). The centrality confound explanation is plausible but not validated on other same-domain datasets. This means the paper's core "count→recall decline" channel holds on only a subset of tested conditions. Without exact-match F1 on MAVEN or testing on another same-domain ED dataset, MAVEN is essentially a counterexample that is explained away rather than investigated.
48	
49	### W3: Only 4 References — Seriously Inadequate Related Work (R2) — Major
50	The paper cites only 4 references: Wei et al. (2023), Zhou et al. (2024/UniNER), Li et al. (2023/GPT-NER), and Sainz et al. (2024/GoLLIE). This is far below the standard for any venue. Critical missing work includes:
51	- **Label confusion in NLP**: Confusion matrix analysis, hierarchical label structures in NER, label smoothing approaches
52	- **Entailment-based zero-shot classification** (Yin et al. 2019) where label semantics directly drive performance
53	- **Schema-guided approaches**: SGD benchmark, dynamic schema selection
54	- **Fine-grained entity typing**: Extensive literature on type confusion in fine-grained NER/RE
55	- **Cognitive science**: Prototype theory, exemplar models explaining why similar categories are harder to discriminate
56	- **Other decomposition/multi-agent IE approaches**: CROSSAGENTIE, IEPile hard-negative schema construction
57	- **LLM-PEE**: Referenced in the introduction text but not in the reference list
58	
59	This gap makes it impossible to properly assess the paper's novelty claims against existing literature.
60	
61	### W4: FewRel Key Results Not Shown in Tables (R1) — Moderate
62	The abstract claims "3.4× stronger on 80-type vs. 16-type schemas (Δ=−31.2pp vs. −9.1pp)" and "r=0.11–0.13" as headline numbers, but the paper body only shows DocRED BCS-controlled results (Tables 2–3) and Few-NERD error taxonomy (Table 5). The FewRel BCS-controlled tables that produce these headline numbers are absent. This is a significant presentation gap—reviewers cannot verify the most-cited numbers in the abstract.
63	
64	### W5: Limited Conceptual Novelty (R2) — Moderate
65	"Semantically similar labels cause confusion" is a well-established observation in classification, cognitive science, and NLP. The paper's contribution is formalizing and measuring this in training-free LLM IE with controlled experiments—a narrower contribution than the framing suggests. The "two-channel" framework (count→recall, confusability→confusion) is descriptive rather than mechanistic; "attention dilution" and "semantic interference" are post-hoc labels that are never empirically validated at the attention/logit level.
66	
67	### W6: No Actionable Method Emerges (R1, R2) — Moderate
68	SDGD fails (−35% structural cost). The paper's prescriptive conclusion—pursue calibration-based approaches—is speculative and untested. For a top venue, the "so what?" question is legitimate: the paper identifies a diagnostic signal but cannot demonstrate how to use it. The value proposition is purely analytical.
69	
70	### W7: Underpowered 2×2 Factorial (R1) — Moderate
71	The interaction test (z=−0.667, p=0.505) is non-significant but used to argue for "orthogonal channels." The count range is narrow (6 vs 12), which the paper itself acknowledges limits power. An underpowered null result cannot distinguish true additivity from inability to detect interaction. The "orthogonal" claim in the title and abstract should be tempered.
72	
73	### W8: Single Model/Seed for Most Experiments (R1) — Minor
74	All experiments use Qwen3-32B with temperature=0 and presumably a single seed. The LLaMA replication is mentioned (87% consistency) but not shown in detail. The batch-level randomness captures schema variability but not model stochasticity. A 2–3 seed sensitivity analysis would strengthen confidence.
75	
76	### W9: Inconsistent Metrics Across Tasks (R1) — Minor
77	NER uses text-match F1, RE uses accuracy, ED uses relaxed F1. These have different sensitivity profiles. The cross-task generalization claim ("two channels operate across all tasks") is weakened when the metrics are not comparable. The MAVEN "reversal" may simply reflect that relaxed F1 behaves fundamentally differently from exact-match metrics.
78	
79	---
80	
81	## Experiment Coverage Assessment
82	
83	Comparing the paper against the planned experiment list from the review context:
84	
85	| Experiment | Plan ID | Covered? | Notes |
86	|---|---|---|---|
87	| DocRED Confusability Study | exp-005 | ✅ Full | Tables 2–3, strong results |
88	| Interaction Effect 2×2 | exp-006 | ✅ Full | Table 4, non-significant interaction |
89	| Error Taxonomy | exp-007 | ✅ Full | Tables 5–6, strongest evidence |
90	| SDGD-zero MAVEN | exp-009 | ✅ Full | Table 8 |
91	| SDGD-cal Few-NERD | exp-010 | ✅ Full | Table 7 |
92	| SDGD-cal MAVEN | exp-011 | ✅ Full | Table 8 |
93	| Random Batching Ablation | exp-013 | ✅ Full | Table 10 |
94	| Per-type Splitting | exp-014 | ✅ Full | Table 11 |
95	| SCS Validation | exp-015 | ✅ Full | Table 1 |
96	
97	All 9 planned experiments are covered. The paper also includes the FewRel results referenced in the abstract (though not tabulated in the body), LLaMA cross-model validation (mentioned but not detailed), and the centrality confound analysis on MAVEN.
98	
99	---
100	
101	## Questions for Authors (Consolidated)
102	
103	1. **FewRel tables**: The abstract cites Δ=−31.2pp (80-type) and Δ=−9.1pp (16-type) as headline numbers. Where are the supporting tables? These should appear in the main paper.
104	
105	2. **Pairwise analysis on RE**: A confusion matrix is trivially computable for FewRel (classification task). Why was pairwise SCS–confusion correlation omitted for RE? Adding it would substantially strengthen the cross-task pairwise claim.
106	
107	3. **MAVEN exact-match F1**: Have you computed exact-match F1 for MAVEN? If the count-curve reversal disappears under exact match, it supports the relaxed-matching explanation. If it persists, the reversal has a deeper cause.
108	
109	4. **SCS on type descriptions**: SCS uses only type name strings. Many relation types have similar names but distinctive definitions. Would SCS computed on definitions change the correlation structure?
110	
111	5. **Few-shot interaction**: The paper tests only zero-shot. Does confusability interact with the number of in-context examples? Few-shot demonstrations might disambiguate confusable types, potentially eliminating Channel 2.
112	
113	6. **Reference list**: The paper has only 4 citations. Is this the intended final version? LLM-PEE is discussed in the introduction but not cited.
114	
115	---
116	
117	## Scores
118	
119	| | R1 (Methods/Experiments) | R2 (Novelty/Related Work) | Consensus |
120	|---|---|---|---|
121	| **Score** | 4/6 (Weak Accept) | 4/6 (Weak Accept) | **4/6 (Weak Accept)** |
122	| **Confidence** | 4/5 | 4/5 | 4/5 |
123	
124	### Score Justification
125	
126	**For acceptance (strengths):**
127	- Genuine gap addressed: first controlled disentanglement of count vs confusability in training-free LLM IE
128	- Error taxonomy (IntraSub ρ≥0.95) is strong mechanistic evidence
129	- Centrality confound is a real methodological contribution
130	- SDGD negative result is informative and honestly reported
131	- Good experimental breadth (4 datasets, 3 tasks, 2 models, 2 embeddings)
132	
133	**Against acceptance (weaknesses):**
134	- Very small pairwise effect sizes (r²≈1.5%) limit practical significance
135	- Only 4 references—far below venue standards, makes novelty assessment impossible
136	- MAVEN results contradict the main narrative; explanation is post-hoc and untested
137	- No actionable method emerges (SDGD fails, future directions speculative)
138	- FewRel headline numbers not shown in tables
139	- "Orthogonal" claim rests on an underpowered null result
140	- Conceptual novelty is limited (similar labels → confusion is well-known)
141	
142	### Overall Assessment
143	
144	This is a careful empirical analysis paper that addresses a genuine gap in understanding schema complexity effects on training-free LLM IE. The experimental design is sound, the error taxonomy analysis is compelling, and the centrality confound finding is a useful methodological contribution. However, the paper is hampered by (1) very small effect sizes that question practical utility, (2) a critically inadequate reference list, (3) MAVEN results that partially contradict the main thesis, and (4) no actionable downstream method. In its current form, it provides useful measurements for the community but falls short of the novelty and impact expected at a top venue. With a substantially expanded related work section, the missing FewRel tables, MAVEN exact-match analysis, and a more tempered framing of "orthogonal" channels, this would be a solid contribution at a Weak Accept level.
145	
146	**Recommendation: Weak Accept (4/6)** — conditionally, pending major revision of reference list and FewRel table inclusion.
147	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "190ad725-d27b-44c6-bd88-309443c86672",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "2165f7ad-dcc1-478f-a905-1b0f9381f11c",
  "sourceToolAssistantUUID": "190ad725-d27b-44c6-bd88-309443c86672",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-16T08:19:03.179Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01W5kgrVqQqQLkR7GxLSe5SA`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/review_report.md 2>/dev/null && echo \"EXISTS\" || echo \"NO_REPORT\"",
  "description": "Check if median tier review exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2165f7ad-dcc1-478f-a905-1b0f9381f11c",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vJe2rvqGEL147t7rVk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1e19d87-cf0e-4b47-b622-bc2b9c17880f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018R3y27jZ9GdmApryJpasNL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 71612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 582,
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

_source line 59 · 2026-05-16T08:19:03.255Z_

<details><summary>↩ Tool result · `toolu_01W5kgrVqQqQLkR7GxLSe5SA`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/review_report.md
EXISTS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1e19d87-cf0e-4b47-b622-bc2b9c17880f",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "d4682550-e659-4187-a2b1-d3baa6d4e946",
  "sourceToolAssistantUUID": "c1e19d87-cf0e-4b47-b622-bc2b9c17880f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-16T08:19:03.824Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ALVhz2swtjzMXheSqQWDE9`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/worst/review_report.md 2>/dev/null && echo \"EXISTS\" || echo \"NO_REPORT\"",
  "description": "Check if worst tier review exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4682550-e659-4187-a2b1-d3baa6d4e946",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vJe2rvqGEL147t7rVk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42c03bfc-5d06-462c-af01-9ab328ab703b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018R3y27jZ9GdmApryJpasNL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 71612,
      "output_tokens": 382,
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
          "output_tokens": 382,
          "cache_read_input_tokens": 71612,
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

_source line 61 · 2026-05-16T08:19:03.876Z_

<details><summary>↩ Tool result · `toolu_01ALVhz2swtjzMXheSqQWDE9`</summary>

```text
NO_REPORT
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42c03bfc-5d06-462c-af01-9ab328ab703b",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "8547bcb3-921e-45b8-b1a1-f36723c32790",
  "sourceToolAssistantUUID": "42c03bfc-5d06-462c-af01-9ab328ab703b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-16T08:19:13.454Z_

The `best` and `median` tiers already have reviews; `worst` does not. But I notice the existing "best" review was based on an earlier version of the paper (the dream-generated paper.tex), not the actual current paper in `docs/paper/`. The current paper has evolved significantly since then (D038-D043 decisions, v2 n=25 results, DocRED, batch composition, etc.).

Since I'm asked to write a review as R1 focusing on methodology and experiments, and the `worst` tier is the one missing a review, let me write the review for the worst-case scenario. But actually, re-reading the prompt -- I'm just asked to write a review. Let me check what the current paper actually says versus the dream version and write my R1 review of the actual paper (the one in `docs/paper/`).

Let me now write the comprehensive R1 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8547bcb3-921e-45b8-b1a1-f36723c32790",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vK4cDp3VSpKa6cNBQD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5344ff57-8d94-4555-a47e-dafdf212b1e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GspQaKZnXY7AjT3E7WZQ9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4270,
      "cache_read_input_tokens": 72194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4270,
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

_source line 63 · 2026-05-16T08:20:57.394Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01ApUNd9QFT2XT1kGR7CLGgk`</summary>

```json
{
  "project": "schema-dag-extraction",
  "tier": "worst",
  "dream_id": "dream_20260516T073533",
  "overall_score": "Weak Reject (3/6)",
  "report": "&lt;![CDATA[---\ndream_id: dream_20260516T073533\ntier: worst\noverall_score: Weak Reject (3/6)\nreviewer: R1 (Methodology & Experiments)\nconfidence: 4/5\n---\n\n# R1 Review: Methodology & Experiments Focus\n\n**Paper:** \"Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?\"\n\n---\n\n## 1. Summary\n\nThis paper conducts a controlled empirical study isolating type count from type confusability as independent drivers of performance degradation in training-free (zero-shot) LLM information extraction. Using four datasets (Few-NERD, FewRel, DocRED, MAVEN) across NER, RE, and ED tasks, the authors introduce the Schema Confusability Score (SCS/BCS) and propose a two-channel degradation model: count drives recall decline, while confusability drives type substitution errors. The paper reports an informative negative result for confusability-aware schema decomposition (SDGD) in NER, and a small (+1.4pp, non-significant) gain for RE batch composition. While the experimental design is principled, the paper's core claims rest on a mix of modest effects, underpowered tests, and results that partially contradict the main thesis.\n\n---\n\n## 2. Strengths\n\n- **Principled controlled experimental design.** The two-paradigm approach (count curves + BCS-controlled experiments) is well-motivated and represents a genuine methodological improvement over prior work that conflates count and confusability. The within-pool control (drawing 16-rel subsets from the 80-rel pool) to isolate confusability from pool composition is particularly well thought out.\n\n- **Honest and transparent reporting throughout.** The authors do not hide inconvenient results: the non-significant factorial test (p=0.50), MAVEN's reversed count curve, SDGD's failure, the non-significant batch composition gain (+1.4pp, p~0.19), and the modest pairwise r^2 of 1.3-1.7% are all reported openly. The decisions log (D019, D026, D043) confirms these were not cherry-picked away. This level of transparency is commendable.\n\n- **Error taxonomy is the strongest evidence.** The IntraSub monotonic scaling with BCS (rho=1.0 NER, rho=0.954 RE) computed over n=148 and n=154 batches respectively is compelling. The observation that 100% of RE type confusion errors are intra-batch provides genuine mechanistic insight. Cross-task replication on both NER and RE strengthens this finding substantially.\n\n- **Centrality confound analysis is a useful methodological contribution.** Identifying that per-type BCS aggregation conflates confusability with centrality on same-domain schemas (MAVEN), with residualized analysis confirming the raw positive correlation vanishes under joint control (p>0.2), is a finding the community can use. The demonstration that pairwise SCS remains valid while per-type aggregation fails is informative.\n\n- **Cross-model validation on RE.** The Llama-3.1-8B replication showing BCS gaps of -27.1pp (count=8) and -23.9pp (count=16), with high-BCS accuracy converging to ~51% on both models, is good evidence that confusability effects are not model-specific for RE.\n\n- **DocRED extension strengthens generalizability.** The document-level RE replication with BCS slopes of -0.71 (steeper than FewRel) and R^2=0.53 confirms the pattern extends beyond sentence-level classification.\n\n---\n\n## 3. Weaknesses\n\n### Critical\n\n- **W1: The \"orthogonal channels\" claim is unsupported by the evidence.** The paper claims count and confusability are \"orthogonal\" degradation channels, but the only direct test of this -- the 2x2 factorial (Section 4.2 / Appendix D) -- is non-significant (z=-0.67, p=0.50). A non-significant interaction test with n~13 batches per cell, BCS range compressed to 0.79-0.87, and count span of only 6 vs 12 cannot distinguish true additivity from inability to detect interaction. The permutation test on cross-pool slopes (p=0.598) tests slope *equality*, not independence of the two factors. Absent a properly powered interaction test, the \"orthogonal\" framing in the title-level claim (\"two degradation channels\") is not warranted. **Severity: Critical** -- the two-channel decomposition is the paper's central organizing claim.\n\n- **W2: Pairwise effect sizes are too small to support the headline claims.** r=0.112 (Few-NERD) and r=0.129 (MAVEN) correspond to r^2=1.3% and 1.7% -- SCS explains essentially none of the variance in type confusion at the pairwise level. The paper acknowledges this but then pivots to extreme-batch comparisons (31.2pp gap) to argue for \"practical significance.\" This conflation is problematic: the extreme-batch gap reflects hand-selected type compositions at the tails of the BCS distribution, not the typical schema designer's experience. The within-pool typical gap is only 2.2pp (95% CI: [0.4, 4.0]) -- barely above noise for practical schema optimization. The paper's framing oscillates between claiming the pairwise signal is \"modest but significant\" and leveraging the extreme-batch gap as if it represents typical operating conditions. **Severity: Critical** -- the disconnect between pairwise r^2~1.5% and the 31.2pp extreme-batch headline number makes the contribution hard to assess.\n\n### Major\n\n- **W3: Cross-model validation is incomplete for Channel 2 on NER.** The paper acknowledges that \"Channel 2 was not robustly detectable at 8B scale\" for NER (Limitations item 1). This means the core two-channel claim is validated on only one model for NER. The RE validation is strong (Llama replicates), but NER is the primary task in the paper. The floor-effect explanation is plausible but not verified -- was the count range insufficient, or does confusability genuinely not matter for smaller models on NER? This asymmetry weakens the cross-task generalization claim.\n\n- **W4: MAVEN results partially contradict the main thesis and the explanation is post-hoc.** MAVEN's count curve goes in the opposite direction (F1 increases with count), and per-type BCS correlates positively with F1. The centrality confound explanation is reasonable, but it means Channel 1 (count -> recall decline) fails on 1 of 4 datasets, and Channel 2 (confusability -> degradation) fails at the per-type level on 1 of 3 datasets. The pairwise signal survives on MAVEN (MiniLM r=0.129), but only with MiniLM -- Qwen3 pairwise is non-significant (r=-0.007, p=0.41). This means the pairwise signal is embedding-dependent on MAVEN, requiring the right embedding model to detect confusability -- a significant practical limitation that undermines the claim of a general phenomenon.\n\n- **W5: BCS-controlled design has residual confounds that are acknowledged but not resolved.** The paper states: \"high-BCS types may differ in other properties (definition granularity, frequency)\" (Section 4.3). The within-pool analysis partially mitigates this, but the 80-pool 16-sub quartile Delta CI crosses zero ([-8.17, +0.38]), meaning the confusability effect is not significant in the most tightly controlled condition. The significant regression slope (-0.401, CI excludes zero) rescues the finding, but the tension between the two analyses (quartile non-significant, slope significant) suggests the effect is fragile and sensitive to analytic choices.\n\n- **W6: Error taxonomy bins are post-hoc with only 4-5 levels.** The IntraSub rho=1.0 (NER) is computed over 4 BCS bins -- with 4 ranked values, rho=1.0 is obtained whenever the ordering is monotonic, which requires only that the 4 bin means are ordered. This is suggestive but not a rigorous statistical test. The RE rho=0.954 over 5 bins is similarly constrained. The rho values are computed over the n=148/154 individual batches (not bins), which is better, but the binning thresholds appear to be chosen post-hoc to create visually compelling monotonic trends. Were different binning schemes tested? How sensitive is the monotonicity to bin boundary choices?\n\n- **W7: The confusability-aware RE batch composition result is non-significant and relies on oracle routing.** The +1.4pp gain (p~0.19) does not reach significance. More critically, as noted in decision D043, the experiment uses oracle routing -- each sample is routed to the batch containing its gold type. This means there is no merge step, and the \"no merge amplification\" claim is vacuously true. The 29.8pp gain over single-pass is purely a count effect (80 -> ~10 types per batch), not a confusability effect. This section overstates the practical contribution.\n\n### Minor\n\n- **W8: DocRED confusability study uses only n=5 batches per condition (count curve) and n~25-27 batches for BCS-controlled.** While the BCS-controlled results are significant, the count curve with n=5 random batches per level has high sampling variance. The paper does not report CIs for the count curve, making it hard to assess whether the monotonic decline is robust or within noise.\n\n- **W9: FewRel evaluation combines train + val splits.** This is acknowledged in Limitations, but it means the 80-relation pool includes relations the model may have seen during pretraining (Wikidata relations in training data). The paper cannot rule out differential memorization as a confound -- some relations may be easier because the model has seen more examples during pretraining, not because of confusability.\n\n- **W10: Single prompt seed (42) for all experiments.** Temperature=0 with greedy decoding reduces stochasticity, but the choice of seed can still affect vLLM's batching and scheduling. No seed sensitivity analysis is provided.\n\n---\n\n## 4. Questions for Authors\n\n1. **Interaction test power analysis.** What sample size would be needed to detect a meaningful interaction (e.g., 5pp) at 80% power? Given the observed cell means (0.33/0.31/0.32/0.28), was the 2x2 design fundamentally underpowered, or is the interaction genuinely absent?\n\n2. **Typical-batch magnitude.** The within-pool typical BCS gap is 2.2pp (Table 5). For a practitioner deciding whether to optimize schema confusability, is 2.2pp worth the engineering cost? How does this compare to gains from better prompt engineering (v1 vs v2 yields ~5.7pp change)?\n\n3. **Error taxonomy bin sensitivity.** Were the 4 BCS bins for NER (solo/low/mid/high) determined before or after seeing the data? What happens with 3 bins, 5 bins, or continuous BCS as predictor?\n\n4. **MAVEN Qwen3 pairwise failure.** The pairwise SCS-confusion correlation is significant with MiniLM (r=0.129) but non-significant with Qwen3 (r=-0.007) on MAVEN. Why does the extraction model's own embeddings fail to capture the confusability signal on this dataset? This seems to directly undermine the theoretical motivation for SCS.\n\n5. **Oracle routing in RE batch composition.** If oracle routing is removed (i.e., samples are assigned to batches via a classifier or heuristic), what happens to the +1.4pp gain? Is the confusability-aware result purely an artifact of knowing the gold labels at test time?\n\n6. **Cluster bootstrap CIs.** The paper notes that cluster bootstrap (accounting for non-independence of pairs sharing a type) yields wider CIs. For Few-NERD, [0.069, 0.219] vs pair-level [0.076, 0.156]. Were all primary analyses also computed with cluster bootstrap? If the pairwise r=0.112 is the main evidence, the appropriate CI is the wider one.\n\n7. **Prompt v1 fabricated offsets.** The paper states v1 prompts produce fabricated character offsets in 96.5% of cases. Does this fabrication correlate with BCS? If the model spends capacity fabricating offsets, this could introduce a systematic confound in v1 experiments.\n\n---\n\n## 5. Missing Experiments or Analyses\n\n1. **Properly powered factorial test.** The 2x2 design (Section 4.2) should be redone with adequate sample sizes (n>=50 per cell), wider count range (e.g., 8 vs 32), and wider BCS range. Without this, the \"orthogonal channels\" claim is aspirational.\n\n2. **Continuous BCS regression for error taxonomy.** Rather than binning BCS into 4-5 levels, regress IntraSub rate on continuous BCS with bootstrap CIs on the slope. This would avoid post-hoc binning concerns and provide a more rigorous test of monotonicity.\n\n3. **A second open-weight model for NER Channel 2.** The Llama-8B failure could be due to model capacity, but a mid-sized model (e.g., Llama-3.1-70B or Qwen2.5-14B) would disambiguate floor effects from genuine absence of confusability effects.\n\n4. **Ablation on SCS using type definitions vs. type names.** SCS currently uses only type name strings. Many confusable types have distinctive definitions (e.g., \"parent organization\" vs \"subsidiary\" are similar names but distinct concepts). Computing SCS on definitions could either strengthen or weaken the pairwise signal, and would test whether the measure captures the right notion of similarity.\n\n5. **Realistic (non-oracle) routing for RE batch composition.** The oracle routing assumption makes the RE decomposition result uninterpretable for practical use. A realistic router (e.g., a lightweight classifier or embedding-based assignment) would make the finding actionable.\n\n6. **Effect of in-context examples.** The paper tests only zero-shot. Even 1-2 demonstrations per type could disambiguate confusable types, potentially eliminating Channel 2. This would clarify whether confusability is inherent to the task or specific to the zero-shot setting.\n\n7. **Proprietary model validation.** All experiments use open-weight models. Given that GPT-4 and Claude are the most common deployment targets for training-free IE, at least one proprietary model comparison (even on a subset of experiments) would substantially strengthen generalizability.\n\n---\n\n## 6. Preliminary Score\n\n**Score: 3/6 (Weak Reject)**\n**Confidence: 4/5**\n\n### Justification\n\n**For acceptance:**\n- Principled experimental design that properly isolates variables\n- Error taxonomy (IntraSub rho>=0.95) is genuinely compelling mechanistic evidence\n- Centrality confound finding is a useful methodological contribution\n- Transparent, honest reporting of negative and weak results\n- Cross-model RE validation is strong\n\n**Against acceptance:**\n- The \"orthogonal channels\" organizing claim rests on an underpowered null result (p=0.50), which is the paper's central thesis\n- Pairwise effect sizes (r^2~1.5%) are too small for practical significance; the extreme-batch gap (31.2pp) creates a misleading impression of the typical effect magnitude (2.2pp)\n- MAVEN contradicts both channels at some analysis level, and the pairwise signal is embedding-dependent (works with MiniLM, fails with Qwen3)\n- Cross-model NER Channel 2 validation failed\n- The only actionable result (RE batch composition) is non-significant (p~0.19) and uses oracle routing, making it vacuously free of merge issues\n- The 80-pool within-pool quartile Delta CI crosses zero in the most tightly controlled analysis\n- No properly powered interaction test exists anywhere in the paper\n\n**Overall:** The paper is a careful, honest empirical study that asks the right question. The error taxonomy analysis is its strongest contribution. However, the gap between what the paper claims (two orthogonal degradation channels; confusability as an independent predictor with practical implications) and what the evidence supports (a tiny pairwise signal, one strong task-specific finding on RE, and several null or contradictory results elsewhere) is too large. The typical-batch confusability effect of ~2pp, combined with the failed NER cross-model validation, non-significant factorial test, and non-significant batch composition result, suggests that confusability -- while real -- is a minor factor compared to type count, prompt design, and other uncontrolled variables. For a top venue, the contribution needs either stronger effects or a method that successfully exploits the diagnostic signal. The paper is close but not there yet.\n\n**Path to acceptance:** (1) Drop or substantially temper the \"orthogonal\" framing -- present the two channels as an observational pattern, not a validated decomposition. (2) Lead with the error taxonomy as the main contribution rather than the pairwise correlations. (3) Provide a properly powered interaction test. (4) Replace the oracle-routed RE experiment with a realistic routing baseline. (5) Add a mid-scale model for NER Channel 2 validation.]]>"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5344ff57-8d94-4555-a47e-dafdf212b1e7",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vK4cDp3VSpKa6cNBQD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00967712-65b1-4a90-b12c-277b2d3851fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GspQaKZnXY7AjT3E7WZQ9i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4270,
      "cache_read_input_tokens": 72194,
      "output_tokens": 4523,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4270
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4523,
          "cache_read_input_tokens": 72194,
          "cache_creation_input_tokens": 4270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4270,
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

_source line 64 · 2026-05-16T08:20:58.254Z_

<details><summary>↩ Tool result · `toolu_01ApUNd9QFT2XT1kGR7CLGgk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/worst/review_report.md\", \"dream_id\": \"dream_20260516T073533\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00967712-65b1-4a90-b12c-277b2d3851fd",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a1d69f340e08c49a0",
  "type": "user",
  "uuid": "783ac461-41a0-42bc-ada3-b6fe98dc190e",
  "sourceToolAssistantUUID": "00967712-65b1-4a90-b12c-277b2d3851fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-16T08:21:08.233Z_

Review submitted. Here is the summary:

**R1 Review (Methodology & Experiments): Weak Reject (3/6), Confidence 4/5**

Key findings:

**Strongest evidence:** The error taxonomy showing IntraSub monotonically scaling with BCS (rho=1.0 NER, rho=0.954 RE over n=148/154 batches) is compelling. The centrality confound analysis on MAVEN is a genuine methodological contribution. Cross-model RE validation with Llama-3.1-8B is solid.

**Critical weaknesses driving the score:**

1. The "orthogonal channels" central claim rests on a non-significant factorial test (p=0.50) with an underpowered design (n~13/cell, narrow BCS range 0.79-0.87, count span only 6 vs 12). The permutation test (p=0.598) tests slope equality, not factor independence.

2. Pairwise r^2 of 1.3-1.7% means SCS explains almost nothing at the pair level. The 31.2pp extreme-batch headline number misrepresents the typical operating condition (within-pool typical gap = 2.2pp). The 80-pool within-pool quartile Delta CI crosses zero ([-8.17, +0.38]).

3. MAVEN contradicts both channels at some analysis level, and the pairwise signal is embedding-dependent (MiniLM works, Qwen3 fails with r=-0.007).

4. NER Channel 2 cross-model validation failed on Llama-8B.

5. The RE batch composition result is non-significant (p~0.19) and uses oracle routing, making the "no merge amplification" claim vacuously true.

**Path to acceptance:** Temper the "orthogonal" framing, lead with error taxonomy, add a powered interaction test, replace oracle routing with a realistic baseline, and validate NER Channel 2 on a mid-scale model.

Report saved to `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/worst/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "783ac461-41a0-42bc-ada3-b6fe98dc190e",
  "isSidechain": true,
  "agentId": "a1d69f340e08c49a0",
  "requestId": "req_011Cb5vTVeqLiaXjKfMyQmmF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04468ac9-294b-45c0-bbb2-71a0fa1efbf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DveU72EDCW8ozamS3R17Yv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4649,
      "cache_read_input_tokens": 76464,
      "output_tokens": 525,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4649
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 525,
          "cache_read_input_tokens": 76464,
          "cache_creation_input_tokens": 4649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4649,
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
