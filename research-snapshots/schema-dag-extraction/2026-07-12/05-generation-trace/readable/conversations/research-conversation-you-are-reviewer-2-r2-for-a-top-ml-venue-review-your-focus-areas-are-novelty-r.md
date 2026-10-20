# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus areas are **novelty**, **related work**, **framing/positio

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a802b76b50c1643e5.jsonl`
- **Structured JSON:** [`654816d0b7e6de421f11.json`](../../sessions/65/654816d0b7e6de421f11.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-16T08:18:20.504Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus areas are **novelty**, **related work**, **framing/positioning**, and **contribution significance**. Use a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept. Target acceptance rate ~25%.

## Paper Summary
Title: "Characterizing and Diagnosing Schema-Induced Failure Modes in Training-Free LLM Information Extraction"

The paper proposes a diagnostic framework for understanding why training-free LLM IE degrades on complex schemas. It identifies two "orthogonal" degradation channels: (1) type count→recall loss via attention dilution, (2) type confusability→substitution errors via semantic interference. It introduces Schema Confusability Score (SCS = cosine similarity of type embeddings), an error taxonomy (IntraSub/ExtraSub/Boundary/Hallucination), and Schema-DAG Guided Decomposition (SDGD). 

**Contributions claimed:**
1. Multi-channel degradation framework (count→recall, confusability→type confusion)
2. Pairwise confusability validation (SCS vs empirical confusion, ρ=0.17-0.31, R²=3-9%)
3. Systematic negative results on schema decomposition (SDGD fails, random > SDGD, merge amplification)
4. Prescriptive schema design guidelines (decision tree in Section 5.3)

**Related work covered (Section 2, very brief ~half page):**
- Training-free IE: GPT-NER, UniNER, GoLLIE
- Schema complexity: "Lost in the Middle" (Liu et al., 2024)
- Schema decomposition: LLM-PEE

**Key results:**
- Error taxonomy: IntraSub correlates with BCS (ρ=1.0 NER, ρ=0.954 RE) — but only 4 bins
- SCS validation: statistically significant but R²=3-9% (weak signal)
- SDGD fails everywhere: single-pass F1=0.445 vs SDGD-zero 0.241 on Few-NERD; single-pass 0.245 vs SDGD-zero 0.152 on MAVEN
- Random batching beats SDGD (p=0.03)
- SDGD-cal marginal improvement (+2.7pp Few-NERD, +0.9pp MAVEN) confirms problem is merge, not estimation
- Schema design guidelines: 5 rules (prefer single-pass, use random batching if needed, avoid per-type, prefer hierarchical schemas, don't rely on SCS alone)
- DocRED BCS effect inconclusive (p=0.14-0.21)
- 2×2 interaction non-significant (p=0.50)

**Experimental setup:**
- Single model: Qwen3-32B only
- 3 datasets: Few-NERD (NER, 66 types), DocRED (RE, 96 types), MAVEN (ED, 168 types)
- No comparison with other schema decomposition methods beyond UniNER-style per-type
- SCS uses only cosine similarity of embeddings (type name + definition)

## Your Task
Write a detailed review covering:
1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, specific)
3. **Weaknesses** (bulleted, specific, with severity: minor/major/critical)
4. **Questions for authors** (numbered)
5. **Assessment of contribution significance**
6. **Preliminary score** (1-6) with confidence (1-5)

Focus on:
- Is the "multi-channel degradation framework" genuinely novel, or does it formalize well-known intuitions?
- Is the error taxonomy a methodological contribution or descriptive analysis?
- Do negative results constitute sufficient contribution for a top venue?
- Is the related work adequate? Major missing references?
- Are the schema design guidelines actionable and well-supported?
- Does the paper advance understanding beyond "similar things are confused more often"?
- Is framing as "diagnostic framework" appropriate for what is essentially an empirical analysis paper?
- How does this compare to concurrent work on structured extraction (e.g., code-generation approaches like GoLLIE that avoid schema confusion by design)?


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "9ba3170b-5399-4d0c-a428-e8e726613446",
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

_source line 2 · 2026-05-16T08:18:20.510Z_

```json
{
  "parentUuid": "9ba3170b-5399-4d0c-a428-e8e726613446",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
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
  "uuid": "551b2ffc-885b-44ae-917f-783ed6654658",
  "timestamp": "2026-05-16T08:18:20.510Z",
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

_source line 3 · 2026-05-16T08:18:24.571Z_



I'll review the paper materials to provide a thorough assessment. Let me first read the relevant project files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "551b2ffc-885b-44ae-917f-783ed6654658",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vFsDXjjNUZDPHSZpQC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73065505-23bb-48fe-834a-be0197c8d668",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013S1zu8b3wHNJcizABibXXs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6880,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6880,
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

_source line 4 · 2026-05-16T08:18:25.172Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017XQ4Rs3dUQqRsXBSBuEajK`</summary>

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
  "parentUuid": "73065505-23bb-48fe-834a-be0197c8d668",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vFsDXjjNUZDPHSZpQC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8bc485bd-f0e2-4501-b3bd-7abe8c91b9a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013S1zu8b3wHNJcizABibXXs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6880,
      "cache_read_input_tokens": 8249,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6880
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 128,
          "cache_read_input_tokens": 8249,
          "cache_creation_input_tokens": 6880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6880,
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

_source line 5 · 2026-05-16T08:18:25.176Z_

<details><summary>↩ Tool result · `toolu_017XQ4Rs3dUQqRsXBSBuEajK`</summary>

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
  "parentUuid": "8bc485bd-f0e2-4501-b3bd-7abe8c91b9a4",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "1738b499-af81-4869-97ab-90dcefc6742d",
  "sourceToolAssistantUUID": "8bc485bd-f0e2-4501-b3bd-7abe8c91b9a4",
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

_source line 6 · 2026-05-16T08:18:28.073Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_016qj7SyWCwHKBEyiFqMMczM`</summary>

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
  "parentUuid": "1738b499-af81-4869-97ab-90dcefc6742d",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vGDBpeY3cYw1BD72So",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb2bb6f1-33e7-4947-a8bf-a9374fd42f6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGHECkjjVjVhYEB1ZnigZ9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
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

_source line 7 · 2026-05-16T08:18:28.257Z_

<details><summary>↩ Tool result · `toolu_016qj7SyWCwHKBEyiFqMMczM`</summary>

```text
{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (42 个)\n\n- **bootstrap_ci_analysis**: DONE (success) — \n- **exp016_fewrel_error_taxonomy**: DONE (success) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp007_error_taxonomy**: DONE (success) — \n- **exp_fewrel_formal_80rel**: DONE (success) — \n- **exp_fewrel_formal**: DONE (success) — \n- **exp008_sdgd_zero_fewnerd_r2**: DONE (negative) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n- **fewrel_pilot**: DONE (success) — \n- **exp004_maven_bcs**: DONE (negative) — \n- **exp002_confusability_controlled**: DONE (success) — \n- **exp003a_prompt_v2_rerun**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp001_count_baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- exp_fewrel_v2_n25（准备中）\n- bcs_max_to_mean_fix（准备中）\n\n## 近期结论\n- **exp_confusability_batch_composition** (success): Confusability-aware batch composition (graph coloring on SCS matrix to separate high-SCS pairs) improves per-type accuracy and reduces substitution errors compared to random batching and single-pass full schema, providing a practical application of the confusability findings.\n- **exp_fewrel_16rel_bootstrap** (success): FewRel 16-type pool, 100 random 8-type batches, bootstrap CI for BCS effect (Δ_BCS). 填 tab:bcs_controlled 16-rel 行的 CI，并与 80-rel 计算 amplification ratio 正式 CI。D033 已批准。 ← 基于 exp_fewrel_formal\n- **exp_docred_confusability** (success): Schema-induced degradation (count + confusability channels) generalizes to document-level RE (DocRED, 96 relation types), strengthening cross-dataset evidence for Claims 1 and 2. ← 基于 exp_fewrel_formal_80rel\n  [DocRED SCS Matrix (96 relations)](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/scs_matrix_info.txt) | [DocRED Confusability Pilot Results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/pilot_results.txt) | [phase2_count_curve_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/count_curve_results.json) | [phase2_bcs_controlled_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bcs_controlled_results.json) | [phase2_bootstrap_analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bootstrap_analysis.json)\n\n## 趋势\n成功 20 / 负向 5 / 失败 10 / 共 38\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\ncqa1-38874: 无 GPU 信息\n\n## 告警\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd: 训练失败 — unknown\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\n- exp012_llama_8b: 已被终止 — unknown\n- exp_fewrel_40rel: 训练失败 — unknown\n- exp012_llama_awq: 已被终止 — unknown\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\n- exp_fewrel_40rel_r2: 训练失败 — unknown\n- exp_fewrel_40rel_r3: 训练失败 — unknown\n- exp012_llama_8b_r3: 训练失败 — unknown\n- exp_fewrel_16rel_100batch: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb2bb6f1-33e7-4947-a8bf-a9374fd42f6f",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "433bea95-6bd7-453d-9253-1456cefe3658",
  "sourceToolAssistantUUID": "eb2bb6f1-33e7-4947-a8bf-a9374fd42f6f",
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

_source line 8 · 2026-05-16T08:18:28.549Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NfmdnH5eGMsjZMPijuWK7W`</summary>

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
  "parentUuid": "433bea95-6bd7-453d-9253-1456cefe3658",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vGDBpeY3cYw1BD72So",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0b05c58-e4c1-4f59-bfc7-20590c6395d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGHECkjjVjVhYEB1ZnigZ9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15129,
      "output_tokens": 160,
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
          "output_tokens": 160,
          "cache_read_input_tokens": 15129,
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

_source line 9 · 2026-05-16T08:18:28.564Z_

<details><summary>↩ Tool result · `toolu_01NfmdnH5eGMsjZMPijuWK7W`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp017_gpt4o_mini_fewrel（准备中）\\n- exp_cross_embedding_sensitivity（准备中）\\n- exp_fewrel_v2_n25（准备中）\\n- bcs_max_to_mean_fix（准备中）\\n\\n## 近期结论\\n- **exp_confusability_batch_composition** (success): Confusability-aware batch composition (graph coloring on SCS matrix to separate high-SCS pairs) improves per-type accuracy and reduces substitution errors compared to random batching and single-pass full schema, providing a practical application of the confusability findings.\\n- **exp_fewrel_16rel_bootstrap** (success): FewRel 16-type pool, 100 random 8-type batches, bootstrap CI for BCS effect (Δ_BCS). 填 tab:bcs_controlled 16-rel 行的 CI，并与 80-rel 计算 amplification ratio 正式 CI。D033 已批准。 ← 基于 exp_fewrel_formal\\n- **exp_docred_confusability** (success): Schema-induced degradation (count + confusability channels) generalizes to document-level RE (DocRED, 96 relation types), strengthening cross-dataset evidence for Claims 1 and 2. ← 基于 exp_fewrel_formal_80rel\\n  [DocRED SCS Matrix (96 relations)](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/scs_matrix_info.txt) | [DocRED Confusability Pilot Results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/pilot_results.txt) | [phase2_count_curve_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/count_curve_results.json) | [phase2_bcs_controlled_results](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bcs_controlled_results.json) | [phase2_bootstrap_analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bootstrap_analysis.json)\\n\\n## 趋势\\n成功 20 / 负向 5 / 失败 10 / 共 38\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-38874: 无 GPU 信息\\n\\n## 告警\\n- exp008_sdgd_zero_fewnerd: 训练失败 — unknown\\n- exp012_llama_fewnerd: 训练失败 — unknown\\n- exp012_llama_fewnerd_r2: 训练失败 — unknown\\n- exp012_llama_fewnerd_r3: 训练失败 — unknown\\n- exp012_llama_8b: 已被终止 — unknown\\n- exp_fewrel_40rel: 训练失败 — unknown\\n- exp012_llama_awq: 已被终止 — unknown\\n- exp012_llama_fewnerd_r4: 训练失败 — unknown\\n- exp012_llama_8b_fewnerd: 训练失败 — unknown\\n- exp_fewrel_40rel_r2: 训练失败 — unknown\\n- exp_fewrel_40rel_r3: 训练失败 — unknown\\n- exp012_llama_8b_r3: 训练失败 — unknown\\n- exp_fewrel_16rel_100batch: 已被终止 — unknown\\n\", \"total_chars\": 2396, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0b05c58-e4c1-4f59-bfc7-20590c6395d2",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "6e8424aa-dee3-4a4a-9c35-c539294b1fe7",
  "sourceToolAssistantUUID": "d0b05c58-e4c1-4f59-bfc7-20590c6395d2",
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

_source line 10 · 2026-05-16T08:18:31.714Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01D4PMcRRHQ8veSZrZNR8YmR`</summary>

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
  "parentUuid": "6e8424aa-dee3-4a4a-9c35-c539294b1fe7",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vGTkRSx7eHmrzu3j5L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d536c19-c741-4ac3-8ea0-26740d9fb565",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBfKM9KH4SaKpTcXy8Pri5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2757,
      "cache_read_input_tokens": 16579,
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

_source line 11 · 2026-05-16T08:18:31.727Z_

<details><summary>↩ Tool result · `toolu_01D4PMcRRHQ8veSZrZNR8YmR`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'schema-dag-extraction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d536c19-c741-4ac3-8ea0-26740d9fb565",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "923b0ced-b0ae-47ad-90d4-3b6ad799970d",
  "sourceToolAssistantUUID": "0d536c19-c741-4ac3-8ea0-26740d9fb565",
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

_source line 12 · 2026-05-16T08:18:32.697Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015pFZ71dsF2khfBxGjt1iJ2`</summary>

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
  "parentUuid": "923b0ced-b0ae-47ad-90d4-3b6ad799970d",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vGTkRSx7eHmrzu3j5L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f58e711b-3a8c-4bd3-9f56-be0b86951e4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBfKM9KH4SaKpTcXy8Pri5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2757,
      "cache_read_input_tokens": 16579,
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

_source line 13 · 2026-05-16T08:18:32.718Z_

<details><summary>↩ Tool result · `toolu_015pFZ71dsF2khfBxGjt1iJ2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/memory.md\", \"content\": \"# Memory — schema-dag-extraction\\n\\n## exp-018 结果与经验（2026-05-16）\\n- **结果**: confusability_aware 0.8021 > random 0.7877±0.0178 (CI上界0.7967)，提升显著 +1.44pp\\n- single_pass 80-rel 全量仅 0.5042，schema overload 严重\\n- Graph coloring (Welsh-Powell) 将 intra-batch BCS 从 0.5585 降到 0.5524\\n- 51 types improved, 28 degraded — 效果非均匀，部分 type 受益更多\\n- **关键参数**: 80-rel pool, batch_size=8-rel per batch, 15 random seeds for CI, 960 samples\\n- **无 merge amplification** — RE closed-set 验证了 Director 的预判\\n- FLASHINFER_DISABLE_VERSION_CHECK=1 需要设置，否则 vLLM 启动失败\\n- 支持 --resume 断点续传（按 condition 粒度）\\n\\n## exp-018 定位澄清（2026-05-16, Director）\\n- exp-018 不是\\\"重试 SDGD\\\"，而是\\\"confusability-aware batching 在 RE closed-set classification 上的实用方案\\\"\\n- RE 每个 (head, tail) pair 独立分类，无实体边界合并 → 无 merge amplification 问题\\n- exp-008 SDGD 失败的 root cause = NER span overlap 的 merge amplification，不适用于 RE\\n- 论文写法：§5 SDGD 失败因 NER merge amplification，但 RE closed-set 避免了此问题 → practical recommendation\\n\\n## exp-017 GPT-4o-mini（2026-05-16, Director 决定放弃）\\n- TUM proxy 未部署在 AutoDL 服务器，无法访问 OpenAI API\\n- 闭源模型验证缺失已在 discussion.tex limitations 中说明\\n- 教训：API 实验需要预先确认 proxy 可达性\\n\\n## D035 集成方案（2026-05-16）\\n- 论文 Table 3 用**极端批次**方法（BCS 最低/最高各 ~5 batches 的 accuracy Δ），不是四分位\\n- D033 的 7.42pp 是四分位比较，需要用极端批次方法重算\\n- 80-pool-16sub 的 3.92pp 也是四分位，同样需要重算\\n- 四分位 CI 作为补充证据报告，展示效应在不同分析粒度下都稳健\\n- 两组数据一起集成到论文再编译上传\\n\\n## 80-pool-16sub 关键发现（2026-05-16）\\n- BCS 范围窄 [0.458, 0.684]（vs 独立 16-rel [0.653, 0.900]），因为从 80-rel pool 采样的 16 types 语义更分散\\n- 四分位 Δ CI 跨零 [-7.79, +0.42]，但回归斜率 CI 不跨零 [-0.684, -0.062]\\n- 效应弱于独立 16-rel pool——BCS 范围压缩导致效应量缩小，这本身支持 BCS 是驱动因素的论点\\n- 决策：用回归斜率做跨条件比较（斜率控制了 BCS 范围差异），四分位 Δ 作为直觉可读的补充\\n\\n## MAVEN per-type BCS 正相关是 artifact（2026-05-16）\\n- exp_maven_residualized_bcs 确认：控制 log_freq + degree_centrality 后相关消失\\n- MiniLM confound = frequency, Qwen3 confound = degree centrality (r=0.854)\\n- 同质 schema（MAVEN 168 event types 多来自 FrameNet）下 per-type BCS 聚合失效\\n- pairwise SCS 仍然有效\\n\\n## Few-NERD r 值差异根因（2026-05-16）\\n- 三个 r 值同源（同一 confusion matrix, 1953 pairs），差异仅因 Y 变量：rate=0.112, count=0.138, CI上界=0.156\\n- Table 2 r=0.112 正确（confusion rate，归一化 gold frequency）\\n- p-values 已修正：Few-NERD Pearson p=7×10⁻⁷, MAVEN p=7×10⁻⁴²\\n\", \"total_chars\": 2127, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f58e711b-3a8c-4bd3-9f56-be0b86951e4d",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "55dd9c66-7296-42d2-817a-2a5081300b8f",
  "sourceToolAssistantUUID": "f58e711b-3a8c-4bd3-9f56-be0b86951e4d",
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

_source line 14 · 2026-05-16T08:18:33.073Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0124oCjp2UNkNu5NsbWb6D84`</summary>

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
  "parentUuid": "55dd9c66-7296-42d2-817a-2a5081300b8f",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vGTkRSx7eHmrzu3j5L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5af5db4-50e7-4e85-b070-95c76389217c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBfKM9KH4SaKpTcXy8Pri5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2757,
      "cache_read_input_tokens": 16579,
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
          "cache_read_input_tokens": 16579,
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

_source line 15 · 2026-05-16T08:18:33.083Z_

<details><summary>↩ Tool result · `toolu_0124oCjp2UNkNu5NsbWb6D84`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\", \"content\": \"# Literature Map for schema-dag-extraction\\n# Updated: 2026-05-15\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\n\\n# =============================================================================\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\n# =============================================================================\\n\\n- id: llm-pee-2025\\n  title: \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\"\\n  year: 2025\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2503.02628\\n  role: direct-competitor\\n  relevance_note: >\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\n    Divides candidate types into partitions to reduce prompt length.\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\n\\n- id: parse-2025\\n  title: \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\"\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://arxiv.org/abs/2510.08623\\n  role: direct-competitor\\n  relevance_note: >\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\n    Does NOT model type confusability explicitly.\\n\\n- id: dee-2024\\n  title: \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\"\\n  year: 2024\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2406.01045\\n  role: direct-competitor\\n  relevance_note: >\\n    Decomposes event extraction into detection + argument extraction.\\n    Dynamic schema-aware RAG for augmented prompts.\\n    KEY DIFF: task-level decomposition (detection vs argument), not schema-level type decomposition.\\n\\n- id: crossagentie-2025\\n  title: \\\"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot IE\\\"\\n  authors: [Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, Xuan Wang]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.718/\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent: intra-group cross-type debate (resolves entity-label conflicts)\\n    + inter-group cross-task debate (NER↔RE mutual refinement).\\n    ⚠️ MODERATE NOVELTY CONCERN: cross-type debate explicitly addresses type confusion.\\n    KEY DIFF: reactive debate to resolve confusion post-hoc vs our proactive decomposition to prevent it.\\n    Must clearly differentiate in paper.\\n\\n- id: dlisc-2025\\n  title: \\\"Effective and Efficient Schema-aware Information Extraction Using On-Device LLMs\\\"\\n  year: 2025\\n  venue: arXiv (May 2025)\\n  url: https://arxiv.org/abs/2505.14992\\n  role: direct-competitor\\n  relevance_note: >\\n    Dual-LoRA with Incremental Schema Caching.\\n    Identification LoRA retrieves relevant schemas, Extraction LoRA performs IE.\\n    Focus on efficiency for on-device LLMs, not confusability analysis.\\n\\n- id: spt-2025\\n  title: \\\"Schema as Parameterized Tools for Universal Information Extraction\\\"\\n  year: 2025\\n  venue: arXiv (June 2025)\\n  url: https://arxiv.org/abs/2506.01276\\n  role: direct-competitor\\n  relevance_note: >\\n    Treats schemas as parameterized tools for LLM tool-calling.\\n    Schema retrieval + generation + infilling. Novel schema-LLM interface.\\n    Does not address type confusability.\\n\\n- id: zeroner-2025\\n  title: \\\"ZeroNER: Fueling Zero-Shot NER via Entity Type Descriptions\\\"\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://aclanthology.org/2025.findings-acl.805/\\n  role: direct-competitor\\n  relevance_note: >\\n    Description-driven: LLM supervision → BERT student for unseen types.\\n    +16% F1 over LLMs on hard zero-shot. Leverages type descriptions.\\n    Related to how schema semantics affect extraction quality.\\n\\n- id: cmas-ner-2025\\n  title: \\\"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition\\\"\\n  year: 2025\\n  venue: TheWebConf 2025\\n  url: https://dl.acm.org/doi/10.1145/3696410.3714923\\n  role: direct-competitor\\n  relevance_note: >\\n    Multi-agent collective intelligence for zero-shot NER.\\n    Addresses context correlation and indiscriminate demonstration problems.\\n    Outperforms on 6 benchmarks including domain-specific and general-domain.\\n\\n# =============================================================================\\n# METHOD COMPONENTS — techniques we build upon or relate to\\n# =============================================================================\\n\\n- id: uniner-2024\\n  title: \\\"UniversalNER: Targeted Distillation from Large Language Models for Open NER\\\"\\n  authors: [Wenxuan Zhou et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://arxiv.org/abs/2308.03279\\n  role: method-component\\n  relevance_note: >\\n    Instruction-tuning on ChatGPT-generated NER data. 43 datasets, 9 domains, 13K+ types.\\n    UniNER-7B outperforms ChatGPT by 7 F1 points.\\n    Important baseline for universal NER and schema-at-scale challenges.\\n\\n- id: gollie-2024\\n  title: \\\"GoLLIE: Annotation Guidelines Following Large Language Model for Information Extraction\\\"\\n  authors: [Oscar Sainz et al.]\\n  year: 2024\\n  venue: ICLR 2024\\n  url: https://hitz-zentroa.github.io/GoLLIE/\\n  role: method-component\\n  relevance_note: >\\n    Code-style schema definitions + annotation guideline following.\\n    Strong zero-shot on unseen IE tasks. Code-Llama based.\\n    Baseline for guideline-driven schema representation.\\n\\n- id: gliner-2024\\n  title: \\\"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08526\\n  role: method-component\\n  relevance_note: >\\n    Compact bidirectional encoder for zero-shot NER with parallel extraction.\\n    Outperforms InstructUIE and larger models. Non-LLM competitive baseline.\\n\\n- id: gliner2-2025\\n  title: \\\"GLiNER2: Efficient Multi-Task IE System with Schema-Driven Interface\\\"\\n  authors: [Urchade Zaratiana et al.]\\n  year: 2025\\n  venue: EMNLP 2025 Demo\\n  url: https://arxiv.org/abs/2507.18546\\n  role: method-component\\n  relevance_note: >\\n    Extends GLiNER to multi-task IE (NER+RE+classification). 205M params, CPU-efficient.\\n    Schema-driven interface. Shows schema approach scales to multi-task.\\n\\n- id: kggen-2025\\n  title: \\\"KGGen: Extracting Knowledge Graphs from Plain Text with Language Models\\\"\\n  authors: [Mo et al.]\\n  year: 2025\\n  venue: NeurIPS 2025\\n  url: https://arxiv.org/abs/2502.09956\\n  role: method-component\\n  relevance_note: >\\n    Two-stage decomposition: entities first, then relations.\\n    Entity clustering/deduplication to reduce graph sparsity.\\n    Schema decomposition approach for KG construction.\\n\\n- id: code4uie-2024\\n  title: \\\"Retrieval-Augmented Code Generation for Universal Information Extraction\\\"\\n  authors: [Yucan Guo et al.]\\n  year: 2024\\n  venue: NeurIPS 2024 Workshop\\n  url: https://arxiv.org/abs/2311.02962\\n  role: method-component\\n  relevance_note: >\\n    Python class-based schema definitions + RAG for code generation.\\n    Unified code-style schema for all IE tasks.\\n\\n- id: iepile-2024\\n  title: \\\"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus\\\"\\n  authors: [Guanzheng Chen et al., ZJU NLP]\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2402.14710\\n  role: method-component\\n  relevance_note: >\\n    0.32B token bilingual IE corpus. Hard negative schema construction =\\n    semantically proximate schemas to train type discrimination.\\n    ⚠️ RELATED: hard negatives ≈ confusable schemas, but for TRAINING, not inference-time.\\n    Our contribution is inference-time confusability-aware decomposition (training-free).\\n\\n- id: lost-in-middle-2024\\n  title: \\\"Lost in the Middle: How Language Models Use Long Contexts\\\"\\n  authors: [Nelson F. Liu et al.]\\n  year: 2024\\n  venue: TACL 2024\\n  url: https://arxiv.org/abs/2307.03172\\n  role: method-component\\n  relevance_note: >\\n    LLMs degrade when relevant info is in middle of long contexts (U-shaped attention).\\n    Motivates schema decomposition to reduce prompt length.\\n    No IE-specific follow-up found — opportunity for us to be first to connect this to IE.\\n\\n# =============================================================================\\n# ZERO-SHOT NER / RE BASELINES\\n# =============================================================================\\n\\n- id: self-improve-ner-2024\\n  title: \\\"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models\\\"\\n  year: 2024\\n  venue: NAACL 2024\\n  url: https://arxiv.org/abs/2311.08921\\n  role: background\\n  relevance_note: >\\n    Self-improving framework using LLM self-generated examples for zero-shot NER.\\n\\n- id: self-prompting-re-2024\\n  title: \\\"Unleashing the Power of LLMs in Zero-shot Relation Extraction via Self-Prompting\\\"\\n  year: 2024\\n  venue: EMNLP 2024 Findings\\n  url: https://arxiv.org/abs/2410.01154\\n  role: background\\n  relevance_note: >\\n    Three-stage self-prompting for zero-shot RE. Generates synthetic ICL samples.\\n    Training-free RE baseline.\\n\\n- id: reasoning-ner-2025\\n  title: \\\"A Reasoning Paradigm for Named Entity Recognition\\\"\\n  year: 2025\\n  venue: arXiv (Nov 2025)\\n  url: https://arxiv.org/abs/2511.11978\\n  role: background\\n  relevance_note: >\\n    CoT-based reasoning for NER. Outperforms GPT-4 by 12.3 F1 in zero-shot.\\n    Shifts NER from pattern matching to explicit reasoning. Strong zero-shot baseline.\\n\\n- id: nuner-2024\\n  title: \\\"NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data\\\"\\n  authors: [Sergei Bogdanov et al., NuMind]\\n  year: 2024\\n  venue: EMNLP 2024\\n  url: https://arxiv.org/abs/2402.15343\\n  role: background\\n  relevance_note: >\\n    Contrastive pre-training on LLM-annotated data. Strong few-shot NER foundation model.\\n\\n# =============================================================================\\n# EVALUATION / BENCHMARKING\\n# =============================================================================\\n\\n- id: familiarity-2025\\n  title: \\\"Familiarity: Better Evaluation of Zero-Shot NER by Quantifying Label Shifts in Synthetic Training Data\\\"\\n  year: 2025\\n  venue: NAACL 2025\\n  url: https://arxiv.org/abs/2412.10121\\n  role: evaluation\\n  relevance_note: >\\n    \\\"Familiarity\\\" metric for label shift in synthetic NER data.\\n    Zero-shot NER scores overestimated due to train-eval label overlap.\\n    Quantifies semantic similarity between entity types — related to type confusability.\\n    KEY DIFF: measures evaluation bias, not extraction-time confusability.\\n\\n- id: guidex-2025\\n  title: \\\"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\\\"\\n  authors: [Neil Deshpande et al.]\\n  year: 2025\\n  venue: ACL 2025 Findings\\n  url: https://arxiv.org/abs/2506.00649\\n  role: evaluation\\n  relevance_note: >\\n    Auto-generates domain-specific schemas + guidelines + synthetic labels.\\n    SOTA on 7 zero-shot NER benchmarks (+7 F1). Strong baseline.\\n\\n# =============================================================================\\n# SURVEYS\\n# =============================================================================\\n\\n- id: llm4ie-survey-2024\\n  title: \\\"Large Language Models for Generative Information Extraction: A Survey\\\"\\n  authors: [Derong Xu et al.]\\n  year: 2024\\n  venue: Frontiers of Computer Science\\n  url: https://arxiv.org/abs/2312.17617\\n  role: background\\n  relevance_note: >\\n    Comprehensive survey of LLM-based IE covering prompting, fine-tuning, benchmarks.\\n\\n- id: knowcoder-2024\\n  title: \\\"KnowCoder: Coding Structured Knowledge into LLMs for Universal IE\\\"\\n  year: 2024\\n  venue: ACL 2024\\n  url: https://arxiv.org/abs/2403.07969\\n  role: background\\n  relevance_note: >\\n    Encodes schema knowledge via code structures into LLM.\\n    Related to code-based schema representation.\\n\\n- id: slot-2025\\n  title: \\\"SLOT: Structuring the Output of Large Language Models\\\"\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://aclanthology.org/2025.emnlp-industry.32.pdf\\n  role: background\\n  relevance_note: >\\n    Decouples output formatting from NL task. Model-agnostic structured output.\\n\\n# =============================================================================\\n# EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\\n# — supports \\\"domain boundary\\\" finding: BCS proxy fails for same-domain schemas\\n# =============================================================================\\n\\n- id: gao-repr-degen-2019\\n  title: \\\"Representation Degeneration Problem in Training Natural Language Generation Models\\\"\\n  authors: [Jun Gao, Di He, Hang Li, Xin Jiang]\\n  year: 2019\\n  venue: ICLR 2019\\n  url: https://arxiv.org/abs/1907.12009\\n  role: theoretical-foundation\\n  relevance_note: >\\n    FOUNDATIONAL. Shows that likelihood maximization + weight tying causes word embeddings\\n    to degenerate into a narrow cone with uniformly high cosine similarity.\\n    Proposed cosine regularization (MLE-CosReg) to widen the cone aperture.\\n    LINK TO OUR WORK: This is the root mechanism behind BCS compression.\\n    When Qwen3-32B encodes 168 same-domain FrameNet types, the degeneration effect\\n    concentrates them into the same narrow cone (cosine ≥ 0.90), destroying BCS discriminability.\\n    Cite as the theoretical explanation for why embedding-based confusability proxies\\n    have a principled failure mode on semantically homogeneous schemas.\\n\\n- id: ethayarajh-contextual-2019\\n  title: \\\"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\\\"\\n  authors: [Kawin Ethayarajh]\\n  year: 2019\\n  venue: EMNLP 2019\\n  url: https://aclanthology.org/D19-1006/\\n  role: theoretical-foundation\\n  relevance_note: >\\n    Shows contextualized representations are anisotropic in ALL layers of BERT/ELMo/GPT-2.\\n    Upper layers are more context-specific but still not isotropic.\\n    Introduces quantitative measures of anisotropy (avg cosine sim of random word pairs).\\n    LINK TO OUR WORK: Establishes that anisotropy is pervasive across architectures —\\n    our MAVEN embedding compression is not a Qwen-specific artifact but a general property.\\n    Supports the argument that ANY embedding-based confusability proxy inherits this limitation.\\n\\n- id: cai-isotropy-clusters-2021\\n  title: \\\"Isotropy in the Contextual Embedding Space: Clusters and Manifolds\\\"\\n  authors: [Xingyu Cai, Jiaji Huang, Yuchen Bian, Kenneth Church]\\n  year: 2021\\n  venue: ICLR 2021\\n  url: https://openreview.net/forum?id=xYGNO86OWDH\\n  role: theoretical-foundation\\n  relevance_note: >\\n    ⭐ MOST DIRECTLY RELEVANT. Key insight: global anisotropy is caused by isolated clusters;\\n    WITHIN each cluster, embeddings are locally more isotropic.\\n    Resolution: the high average cosine similarity reported in prior work is an artifact of\\n    mixing embeddings from different clusters — within-cluster geometry is better behaved.\\n    LINK TO OUR WORK: This is the exact mechanism for our \\\"domain boundary\\\" finding.\\n    Cross-domain schemas (ACE vs FewNERD) span DIFFERENT clusters → BCS captures real\\n    inter-cluster distances → proxy works. Same-domain schemas (MAVEN FrameNet types)\\n    fall within ONE cluster → within-cluster variance is low → cosine sim saturates ≥ 0.90\\n    → BCS loses discriminability. Our empirical finding is a direct instantiation of their\\n    theoretical framework applied to type-level (not token-level) embeddings.\\n\\n- id: godey-anisotropy-inherent-2024\\n  title: \\\"Anisotropy Is Inherent to Self-Attention in Transformers\\\"\\n  authors: [Nathan Godey, Éric de la Clergerie, Benoît Sagot]\\n  year: 2024\\n  venue: EACL 2024\\n  url: https://aclanthology.org/2024.eacl-long.3/\\n  role: theoretical-foundation\\n  relevance_note: >\\n    Proves anisotropy is inherent to the self-attention mechanism itself, not just a\\n    consequence of cross-entropy training on long-tailed token distributions.\\n    Observed across modalities (NLP, vision), ruling out data-distribution explanations.\\n    LINK TO OUR WORK: Strengthens the argument that BCS compression is a fundamental\\n    architectural limitation, not fixable by better prompting or model choice.\\n    Supports our position that structural decomposition (SDGD) is necessary precisely\\n    because the embedding space has inherent geometric constraints.\\n\\n- id: rajaee-cluster-isotropy-2021\\n  title: \\\"A Cluster-based Approach for Improving Isotropy in Contextual Embedding Space\\\"\\n  authors: [Sara Rajaee, Mohammad Taher Pilehvar]\\n  year: 2021\\n  venue: ACL 2021\\n  url: https://aclanthology.org/2021.acl-short.73/\\n  role: theoretical-foundation\\n  relevance_note: >\\n    Shows local (within-cluster) assessment of isotropy is more accurate than global assessment.\\n    Cluster-specific dominant directions encode structural (not semantic) information;\\n    removing them improves semantic task performance.\\n    LINK TO OUR WORK: Supports that within a semantic domain (one cluster), the dominant\\n    directions capture domain-level features rather than fine-grained type distinctions.\\n    This explains why MAVEN type embeddings are compressed: the shared \\\"event-ness\\\"\\n    dominates over type-specific semantics in the local embedding geometry.\\n\\n# =============================================================================\\n# NOVELTY THREAT ASSESSMENT (2026-05-15)\\n# =============================================================================\\n#\\n# 1. \\\"Type count vs type confusability\\\" disentangling:\\n#    ✅ NOVELTY SAFE — No prior work explicitly disentangles these two factors.\\n#    - IEPILE hard negatives: closest, but for training, not inference-time decomposition.\\n#    - Familiarity metric: measures label similarity for evaluation bias, not extraction.\\n#    - CROSSAGENTIE: resolves type confusion via debate, doesn't model as degradation channel.\\n#    Our multi-channel degradation model (count + confusability + context) is novel.\\n#\\n# 2. Schema decomposition baselines to compare:\\n#    - LLM-PEE (similarity partitioning) — MUST compare\\n#    - PARSE (LLM-driven schema rewriting) — MUST compare\\n#    - DEE (task-level decomposition) — discuss in related work\\n#    - SPT (schema as tools) — discuss in related work\\n#    - DLISC (Dual-LoRA schema caching) — discuss in related work\\n#\\n# 3. \\\"Lost in the Middle\\\" for IE:\\n#    ✅ OPPORTUNITY — No follow-up work applying it to IE task found.\\n#    We can be first to connect positional bias to schema prompt design.\\n#\\n# 4. Multi-agent approaches (CROSSAGENTIE, CMAS):\\n#    Growing area. Position clearly: we reduce confusion proactively via decomposition,\\n#    they resolve it reactively via debate. Complementary, not conflicting.\\n#\\n# 5. Overall novelty position:\\n#    STRONG — no prior work proposes (a) a formal multi-channel degradation model for\\n#    schema complexity in LLM IE, or (b) a DAG-based schema decomposition optimized\\n#    for type confusability. Main risk is CROSSAGENTIE's cross-type debate framing.\\n\", \"total_chars\": 18972, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5af5db4-50e7-4e85-b070-95c76389217c",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "0991c1b5-1ce3-47c8-a227-bd0f4724e56d",
  "sourceToolAssistantUUID": "c5af5db4-50e7-4e85-b070-95c76389217c",
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

_source line 16 · 2026-05-16T08:18:36.354Z_

Now let me read the actual paper artifacts and key experimental results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0991c1b5-1ce3-47c8-a227-bd0f4724e56d",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vGoEhMJ9HdF5ywJyGE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98381626-3f0c-49a5-a041-587cf88a9fb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrmuLLhBw6ivKhJ1EV9FB6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8227,
      "cache_read_input_tokens": 19336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8227,
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

_source line 17 · 2026-05-16T08:18:38.235Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DcfTSQtUKpFshipP8iYvS6`</summary>

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
  "parentUuid": "98381626-3f0c-49a5-a041-587cf88a9fb6",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vGoEhMJ9HdF5ywJyGE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42a9ba63-5ce2-4384-9e82-02ec653e31b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrmuLLhBw6ivKhJ1EV9FB6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8227,
      "cache_read_input_tokens": 19336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8227,
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

_source line 18 · 2026-05-16T08:18:38.267Z_

<details><summary>↩ Tool result · `toolu_01DcfTSQtUKpFshipP8iYvS6`</summary>

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
  "parentUuid": "42a9ba63-5ce2-4384-9e82-02ec653e31b1",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "1b6e47f3-b522-4a55-a49a-cd6e1fd06812",
  "sourceToolAssistantUUID": "42a9ba63-5ce2-4384-9e82-02ec653e31b1",
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

_source line 19 · 2026-05-16T08:18:38.843Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XsZ9Y2DkziCmu8h74WNA9G`</summary>

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
  "parentUuid": "1b6e47f3-b522-4a55-a49a-cd6e1fd06812",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vGoEhMJ9HdF5ywJyGE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "804f66a1-548f-4888-83a5-795c3810c1a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrmuLLhBw6ivKhJ1EV9FB6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8227,
      "cache_read_input_tokens": 19336,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8227
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 19336,
          "cache_creation_input_tokens": 8227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8227,
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

_source line 20 · 2026-05-16T08:18:38.878Z_

<details><summary>↩ Tool result · `toolu_01XsZ9Y2DkziCmu8h74WNA9G`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ROADMAP.md\", \"content\": \"# schema-dag-extraction — Research Dashboard\\n\\n> 最后更新: 2026-05-16 06:08 UTC | 更新原因: 服务器重启恢复，更新 v2 n=25/DocRED/cross-embedding 完成状态，派 exp-018+exp-017\\n\\n## 核心方向\\n验证 type confusability 独立于 type count 驱动 training-free LLM IE 质量下降，发现 multi-channel degradation model（count→recall, confusability→type confusion）。v2 n=25 证明效应是 task-inherent property 而非 prompt artifact（D040）。详见 paper_framing.md。\\n\\n## 当前阶段\\n**Scope 扩展冲刺** — ARR May 25 提交（距今 9 天）。三条并行线推进。\\n\\n- Claim 1（count scaling）：四任务 + 双模型验证完成 ✓（DocRED 新增）\\n- Claim 2（BCS confusability）：四任务 + 双模型验证完成 ✓（DocRED 新增）\\n- Claim 3（SDGD）：正式放弃 (D019)，negative result + future work\\n- D040：v2 RE n=25 推翻 attenuation 叙述 → confusability is task-inherent ✓\\n- D038/D039：BCS 定义统一（MAX→MEAN）✓\\n- Cross-embedding sensitivity：MiniLM vs Qwen3 方向一致 ✓\\n- Reviewer 审查 D040 叙事重写 + claim 边界评估中\\n\\n## 表述硬约束（C001，全角色遵守）\\n- **C001**: count_40 子集来自 80-type pool 采样，论文必须写 \\\"40-rel subsets sampled from the 80-relation pool\\\"\\n\\n## Scope 扩展计划\\n\\n**Track A — GPU**\\n- [x] DocRED Phase 2 count curve + BCS-controlled ✓（slope −0.71, r=−0.66, p=1.5e-5）\\n- [x] Cross-embedding sensitivity ✓（方向一致，MiniLM 更适合 BCS）\\n- [x] v2 RE n=25 验证 ✓（Δ=25.5pp, r=−0.919, p<0.0001）\\n- [ ] **exp-018: Confusability-aware batch composition** — 已派 Agent 立即上 GPU\\n\\n**Track B — API**\\n- [x] OpenAI key 已存储 ✓\\n- [ ] **exp-017: GPT-4o-mini FewRel replication** — 已派 Agent 启动，API-bound 不占 GPU\\n\\n**Track C — CPU/写作**\\n- [x] D038 BCS 定义统一 ✓\\n- [x] DocRED 论文集成 ✓\\n- [ ] 3 个 Reviewer warning 修复中（docred-2019 编译、registry 过时值、Qwen3 r 值不一致）\\n- [ ] D040 叙事更新确认（§4.3/Intro/AppG）\\n- [ ] Review round（Reviewer 审查 D040 + claim 边界中）\\n- [ ] Final submission\\n\\n## 核心证据进展\\n\\n**已完成（Claim 1+2）**:\\n- exp-001: count curve (recall 0.72→0.42, WrongType 0→2434) ✓\\n- exp-002: pairwise r=0.156 (p<1e-11), confusion ratio 10-28x ✓\\n- exp-003a: prompt v2 降低 over-prediction ✓\\n- exp-004: MAVEN 168 types, MiniLM pairwise r=0.120 ✓\\n- exp_fewrel_formal_80rel: BCS Δ=-31.2pp, slope=-0.401 ✓\\n- exp_fewrel_40rel_r4: count_40=0.588, BCS Δ=-33.3pp/-31.8pp ✓\\n- exp007/exp016 error taxonomy: IntraSub ρ=1.0/0.954 ✓\\n- bootstrap_ci_analysis: 统一 fixed-boundary B=10000 ✓\\n- exp015_scs_validation: 两种 embedding 均显著 ✓\\n- exp012_llama_fewrel_ch2: BCS Δ=-27.1pp/-23.9pp, high-BCS floor 0.51 ✓\\n- D038: BCS MAX→MEAN (slope -0.509, |r|=0.467, quartile Δ=-5.3pp) ✓\\n- **exp_docred_confusability**: BCS slope −0.71（最陡）, r=−0.66, p=1.5e-5, 96 types ✓\\n- **exp_v2_re_n25**: Δ=25.5pp, CI [22.4, 28.6], r=−0.919 — task-inherent ✓\\n- **cross_embedding_sensitivity**: MiniLM/Qwen3 方向一致，MiniLM effect size 更大 ✓\\n\\n**负向结论**:\\n- exp-008 SDGD: F1=0.241 < baseline 0.445 (D014, D019)\\n- exp004_maven_bcs: per-type BCS 正向（centrality confound）\\n- exp006_interaction_2x2: p=0.505 (D026)\\n- exp012_llama_8b_r2_exp2: NER Channel 2 未复现（floor effect）\\n\\n## 近期任务\\n- [ ] exp-018 batch composition 上 GPU（Agent 执行中）\\n- [ ] exp-017 GPT-4o-mini 启动（Agent 执行中）\\n- [ ] 3 个 Reviewer warning 修复\\n- [ ] Reviewer 审查 D040 叙事 + claim 边界评估\\n- [ ] 论文最终集成 + Review round\\n- [ ] 最终提交 ARR May 25\\n\\n## GPU 预算\\n- 服务器: cqa1-38874, 1× RTX PRO 6000 Blackwell (98GB), cuda:0\\n- 当前: 空闲 → exp-018 即将占用\\n\\n## 目标会议\\nEMNLP 2026, ARR May 25 提交（距今 9 天）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D043 | 2026-05-16 | D042 修正：exp-018 confusability-aware 与 random 无显著差异 | exp_confusability_batch_composition |\\n| D042 | 2026-05-16 | exp-018 成功：confusability-aware batching 在 RE 上 +1. | exp_confusability_batch_composition |\\n| D041 | 2026-05-16 | 放弃 exp-017 GPT-4o-mini：TUM proxy 未部署，AutoDL 无法访问 O | exp017_gpt4o_mini_fewrel |\\n| D040 | 2026-05-16 | v2 RE n=25 结果推翻 attenuation 叙述，升级为 \\\"confusability  | exp_v2_re_n25 |\\n| D039 | 2026-05-16 | D039: BCS 统一选择 Path A (MEAN)——科学诚实优先，MAX 作 sensiti | exp_fewrel_16rel_bootstrap, exp_fewrel_formal_80rel, exp_fewrel_80pool_16sub_bootstrap |\\n| D038 | 2026-05-16 | D038: BCS 定义不一致修复——统一为 MEAN pairwise SCS，重算 Table  | exp_fewrel_16rel_bootstrap, exp_fewrel_formal_80rel, exp_fewrel_80pool_16sub_bootstrap |\\n| D037 | 2026-05-16 | D037: Round 2 审稿 Action Matrix 定稿——5C+12W 逐条方案，C1  | exp-003a, exp_fewrel_formal |\\n| D036 | 2026-05-16 | D035 修订：Table 3 以回归斜率为主指标，四分位 Δ 为辅 | exp_fewrel_80pool_16sub_bootstrap, exp_fewrel_16rel_bootstrap |\\n| D035 | 2026-05-16 | D033 集成采用极端批次方法重算，保持 Table 3 方法一致性 | exp_fewrel_16rel_bootstrap, exp_fewrel_80pool_16sub_bootstrap |\\n| D034 | 2026-05-16 | Amplification 报告策略：同时报告 quartile Δ 和 BCS-accuracy  | exp_fewrel_16rel_bootstrap, exp_fewrel_80pool_16sub_bootstrap |\\n\\n\", \"total_chars\": 4380, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "804f66a1-548f-4888-83a5-795c3810c1a0",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "6a61419d-5b1f-4e1d-94d3-c999862d0400",
  "sourceToolAssistantUUID": "804f66a1-548f-4888-83a5-795c3810c1a0",
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

_source line 21 · 2026-05-16T08:18:42.782Z_

<details open><summary>🔧 Tool call — Read · `toolu_013J8TDs9sKWnyqH2SV9PQSB`</summary>

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
  "parentUuid": "6a61419d-5b1f-4e1d-94d3-c999862d0400",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vHDsHJCc27KkpYTC7y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae31b38c-aeac-416a-924b-57a250ac9700",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVHMf4yU2Q8yXKYMYpaWtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3418,
      "cache_read_input_tokens": 27563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3418,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 22 · 2026-05-16T08:18:42.803Z_

<details><summary>↩ Tool result · `toolu_013J8TDs9sKWnyqH2SV9PQSB`</summary>

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
  "parentUuid": "ae31b38c-aeac-416a-924b-57a250ac9700",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "fb1d414b-1e19-4057-97c8-7aa8e19ca811",
  "sourceToolAssistantUUID": "ae31b38c-aeac-416a-924b-57a250ac9700",
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

_source line 23 · 2026-05-16T08:18:43.250Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y5pEpK3Wuf6LsA6vtzdoFB`</summary>

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
  "parentUuid": "fb1d414b-1e19-4057-97c8-7aa8e19ca811",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vHDsHJCc27KkpYTC7y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "548f1b3d-2f3a-41eb-bf92-a391a9797e37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVHMf4yU2Q8yXKYMYpaWtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3418,
      "cache_read_input_tokens": 27563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3418,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 24 · 2026-05-16T08:18:43.262Z_

<details><summary>↩ Tool result · `toolu_01Y5pEpK3Wuf6LsA6vtzdoFB`</summary>

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
  "parentUuid": "548f1b3d-2f3a-41eb-bf92-a391a9797e37",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "085d5c4e-d1e7-43ba-9fc5-1ec4261a16dd",
  "sourceToolAssistantUUID": "548f1b3d-2f3a-41eb-bf92-a391a9797e37",
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

_source line 25 · 2026-05-16T08:18:43.536Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QJwLhZeEQ5qgH9snZnx4sZ`</summary>

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
  "parentUuid": "085d5c4e-d1e7-43ba-9fc5-1ec4261a16dd",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vHDsHJCc27KkpYTC7y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40476f4f-6b47-4818-b1a7-338908c46223",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVHMf4yU2Q8yXKYMYpaWtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3418,
      "cache_read_input_tokens": 27563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3418,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 26 · 2026-05-16T08:18:43.543Z_

<details><summary>↩ Tool result · `toolu_01QJwLhZeEQ5qgH9snZnx4sZ`</summary>

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
  "parentUuid": "40476f4f-6b47-4818-b1a7-338908c46223",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "c2dcef57-0080-47ff-aa22-e799c368d44a",
  "sourceToolAssistantUUID": "40476f4f-6b47-4818-b1a7-338908c46223",
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

_source line 27 · 2026-05-16T08:18:47.505Z_

<details open><summary>🔧 Tool call — Read · `toolu_016cnwcdtDgUsAfS23k4nXQC`</summary>

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
  "parentUuid": "c2dcef57-0080-47ff-aa22-e799c368d44a",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vHa3iuVyygiCTaET78",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "399b8835-f7bb-4e75-80b7-e60b3c6c69d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019TygAWfMxAQW4gqcfgEffK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9791,
      "cache_read_input_tokens": 30981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9791,
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

_source line 28 · 2026-05-16T08:18:47.512Z_

<details><summary>↩ Tool result · `toolu_016cnwcdtDgUsAfS23k4nXQC`</summary>

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
  "parentUuid": "399b8835-f7bb-4e75-80b7-e60b3c6c69d0",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "5b87ffb5-6eaf-49e0-8149-45bfa90a0c66",
  "sourceToolAssistantUUID": "399b8835-f7bb-4e75-80b7-e60b3c6c69d0",
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

_source line 29 · 2026-05-16T08:18:48.013Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WrdwfUQZncGg9gDZEjBC2z`</summary>

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
  "parentUuid": "5b87ffb5-6eaf-49e0-8149-45bfa90a0c66",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vHa3iuVyygiCTaET78",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82faaf3e-1f6f-4b3c-8b63-bba6a2d2e6f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019TygAWfMxAQW4gqcfgEffK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9791,
      "cache_read_input_tokens": 30981,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9791
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 30981,
          "cache_creation_input_tokens": 9791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9791,
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

_source line 30 · 2026-05-16T08:18:48.026Z_

<details><summary>↩ Tool result · `toolu_01WrdwfUQZncGg9gDZEjBC2z`</summary>

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
  "parentUuid": "82faaf3e-1f6f-4b3c-8b63-bba6a2d2e6f1",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "253acf4c-3283-44f4-b1bc-7fdc0d482d2a",
  "sourceToolAssistantUUID": "82faaf3e-1f6f-4b3c-8b63-bba6a2d2e6f1",
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

_source line 31 · 2026-05-16T08:18:52.437Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UwYedYw5LaoHCszAkugXn5`</summary>

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
  "parentUuid": "253acf4c-3283-44f4-b1bc-7fdc0d482d2a",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vHu2UwJsA2PWmR8rtL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7c87bbf-9045-49a3-a07f-12479e7e45bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPwBAPSwsRB9s2eGgWv5FK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8464,
      "cache_read_input_tokens": 40772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8464,
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

_source line 32 · 2026-05-16T08:18:52.448Z_

<details><summary>↩ Tool result · `toolu_01UwYedYw5LaoHCszAkugXn5`</summary>

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
  "parentUuid": "f7c87bbf-9045-49a3-a07f-12479e7e45bd",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "c5a86b1f-0ff2-49ba-aa83-26066df20e06",
  "sourceToolAssistantUUID": "f7c87bbf-9045-49a3-a07f-12479e7e45bd",
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

_source line 33 · 2026-05-16T08:18:53.108Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EV6R4tTf6eXK7d6fpBMVca`</summary>

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
  "parentUuid": "c5a86b1f-0ff2-49ba-aa83-26066df20e06",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vHu2UwJsA2PWmR8rtL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "571cc913-4648-47cb-a687-402ee2bf5155",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPwBAPSwsRB9s2eGgWv5FK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8464,
      "cache_read_input_tokens": 40772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8464,
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

_source line 34 · 2026-05-16T08:18:53.125Z_

<details><summary>↩ Tool result · `toolu_01EV6R4tTf6eXK7d6fpBMVca`</summary>

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
  "parentUuid": "571cc913-4648-47cb-a687-402ee2bf5155",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "63e7ab1e-3f06-4c20-896c-d6739a265258",
  "sourceToolAssistantUUID": "571cc913-4648-47cb-a687-402ee2bf5155",
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

_source line 35 · 2026-05-16T08:18:55.797Z_

<details open><summary>🔧 Tool call — Read · `toolu_015JaDoQ4Fy7jvwDGRErcgNM`</summary>

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
  "parentUuid": "63e7ab1e-3f06-4c20-896c-d6739a265258",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vJGyqRMBYpP8TvhvnG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd1cfa71-b607-4df1-bc47-c9ef468bd3be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRjcPQQH3yHyVF6dBvvyGs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2118,
      "cache_read_input_tokens": 49236,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2118
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 49236,
          "cache_creation_input_tokens": 2118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2118,
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

_source line 36 · 2026-05-16T08:18:55.803Z_

<details><summary>↩ Tool result · `toolu_015JaDoQ4Fy7jvwDGRErcgNM`</summary>

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
  "parentUuid": "bd1cfa71-b607-4df1-bc47-c9ef468bd3be",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "2c0c04a0-f624-436c-9d1c-ef5c7178c292",
  "sourceToolAssistantUUID": "bd1cfa71-b607-4df1-bc47-c9ef468bd3be",
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

_source line 37 · 2026-05-16T08:18:58.614Z_

Now let me look at the latest DREAM review report to understand the current assessment state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c0c04a0-f624-436c-9d1c-ef5c7178c292",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vJU2r1sif4jEFqWmFs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8840cb6f-d3e9-4f99-b3b6-9b89f0238813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoZwQmatVcqdph1gGFgXdr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3036,
      "cache_read_input_tokens": 51354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3036,
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

_source line 38 · 2026-05-16T08:19:00.496Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Mzt5yUvy4eCwhB6hSpPNZ8`</summary>

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
  "parentUuid": "8840cb6f-d3e9-4f99-b3b6-9b89f0238813",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vJU2r1sif4jEFqWmFs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5cf20844-3507-4602-a42c-773af77b93e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoZwQmatVcqdph1gGFgXdr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3036,
      "cache_read_input_tokens": 51354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3036,
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

_source line 39 · 2026-05-16T08:19:00.502Z_

<details><summary>↩ Tool result · `toolu_01Mzt5yUvy4eCwhB6hSpPNZ8`</summary>

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
  "parentUuid": "5cf20844-3507-4602-a42c-773af77b93e9",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "14842d26-4f06-4c12-8350-131ae3b0c70d",
  "sourceToolAssistantUUID": "5cf20844-3507-4602-a42c-773af77b93e9",
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

_source line 40 · 2026-05-16T08:19:01.027Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RLAM3eCpeuNF4VorCR57tH`</summary>

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
  "parentUuid": "14842d26-4f06-4c12-8350-131ae3b0c70d",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vJU2r1sif4jEFqWmFs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f00235c-9892-4d98-b2d1-5cd9ed6734e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoZwQmatVcqdph1gGFgXdr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3036,
      "cache_read_input_tokens": 51354,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3036
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 51354,
          "cache_creation_input_tokens": 3036,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3036,
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

_source line 41 · 2026-05-16T08:19:01.046Z_

<details><summary>↩ Tool result · `toolu_01RLAM3eCpeuNF4VorCR57tH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_framing.md\", \"content\": \"# Paper Framing — schema-dag-extraction\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\\n- Commitment deadline: August 2, 2026\\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\\n- Deadline: ARR May 25, 2026 (10 days from today)\\n\\n## Core Claims (2 claims) — Revised per D019\\n\\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.\\n\\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\\n\\n~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — \\\"why naive decomposition fails\\\" is itself a contribution.\\n\\n## Story Spine — Revised per D012\\n\\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\\n\\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\\n\\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.\\n\\n- **Three-task validation**:\\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio\\n  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel\\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\\n\\n- **Headline result template**: \\\"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid.\\\"\\n\\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\\n\\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\\n\\nThese channels are orthogonal and independently addressable.\\n\\n**Pairwise vs Aggregated Confusability**:\\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).\\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\\n\\n## Evidence Hierarchy (D012)\\n\\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\\n\\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\\n\\n**Few-NERD (NER)** — Qwen3 embeddings:\\n- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation\\n- Nonzero-only Spearman ρ=0.272 (p=5e-5)\\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\\n- Immune to type frequency confound (operates at type-pair level)\\n\\n**MAVEN (ED)** — MiniLM embeddings:\\n- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap\\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\\n- Cross-task replication on same-domain schema\\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\\n\\n### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication\\n\\nLarge effect size, cross-task (RE), scaling with schema complexity:\\n\\n**Formal 80-rel study** (exp_fewrel_formal_80rel):\\n- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97\\n- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)\\n- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)\\n- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)\\n\\n**16-rel sanity check** (exp_fewrel_formal):\\n- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\\n\\n**Pilot extreme batches** (fewrel_pilot, MiniLM):\\n- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp\\n\\nKey insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling\\n\\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\\n\\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\\n\\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\\n\\nMethodological case study on when aggregated confusability measures fail:\\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\\n- This is stronger than \\\"domain boundary\\\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\\n\\n### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)\\n\\nIntraSub rate monotonically increases with BCS on both NER and RE:\\n\\n**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0\\n**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)\\n- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon\\n- Same mechanism, different absolute magnitudes — consistent with cross-task expectations\\n\\nAdditional from extreme batch design:\\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\\n\\n## Embedding Ablation (D010)\\n\\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\\n\\n### Per-type (Layer 2)\\n| | Few-NERD | FewRel | MAVEN |\\n|---|---|---|---|\\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\\n\\n### Pairwise (Layer 1)\\n| | Few-NERD | MAVEN |\\n|---|---|---|\\n| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |\\n| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |\\n\\n### SCS→Empirical Confusion Validation (exp-015 fast)\\n| | Qwen3 | MiniLM |\\n|---|---|---|\\n| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |\\n| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |\\n\\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\\n\\n## Venue Fit Risks\\n\\n- **\\\"Just an empirical study\\\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \\\"Lost in the Middle\\\" (TACL 2024).\\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy | Experiment |\\n|---------|------------------|------------|\\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\\n\", \"total_chars\": 11568, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f00235c-9892-4d98-b2d1-5cd9ed6734e9",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "90935f0a-6046-4a3a-923b-ec21453c1799",
  "sourceToolAssistantUUID": "5f00235c-9892-4d98-b2d1-5cd9ed6734e9",
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

_source line 42 · 2026-05-16T08:19:04.124Z_

Now I have a thorough understanding of the paper. Let me load the tool to submit the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90935f0a-6046-4a3a-923b-ec21453c1799",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vJraAmwUesix7cz5g9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff6f3599-c063-4432-8779-290eb47996c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011bPvMeWAFdrxP1ZtB4RJm2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6722,
      "cache_read_input_tokens": 54390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6722,
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

_source line 43 · 2026-05-16T08:19:04.618Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MPrUd8JbLC9UfiQu6Z2ihE`</summary>

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
  "parentUuid": "ff6f3599-c063-4432-8779-290eb47996c3",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vJraAmwUesix7cz5g9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca444c92-09e0-4a7f-9175-e43fcbcf149b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011bPvMeWAFdrxP1ZtB4RJm2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6722,
      "cache_read_input_tokens": 54390,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6722
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 111,
          "cache_read_input_tokens": 54390,
          "cache_creation_input_tokens": 6722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6722,
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

_source line 44 · 2026-05-16T08:19:04.621Z_

<details><summary>↩ Tool result · `toolu_01MPrUd8JbLC9UfiQu6Z2ihE`</summary>

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
  "parentUuid": "ca444c92-09e0-4a7f-9175-e43fcbcf149b",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "400e9db4-acda-4509-b328-d95b7440120b",
  "sourceToolAssistantUUID": "ca444c92-09e0-4a7f-9175-e43fcbcf149b",
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

_source line 45 · 2026-05-16T08:19:10.572Z_



Now I have all the information needed to write a thorough R2 review. Let me compose it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "400e9db4-acda-4509-b328-d95b7440120b",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vKHrSpSkiQj7QGgJvP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6699ef0b-6647-4b84-a8c5-c7c7a96057d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXhwznC8B9YmE2pCCuPMXG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 61112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 689,
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

_source line 46 · 2026-05-16T08:20:35.576Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_011X4jUdM4BssJ2cXZAkMJfA`</summary>

```json
{
  "report": "\n# Reviewer 2 (R2): Novelty, Related Work, Framing, Contribution Significance\n\n## 1. Summary\n\nThis paper conducts a controlled empirical study to disentangle two factors driving degradation in training-free LLM information extraction on complex schemas: type count (which suppresses recall) and type confusability (which causes type substitution errors). The authors introduce the Schema Confusability Score (SCS), demonstrate its correlation with empirical confusion across NER, RE, and ED tasks, identify a centrality confound on homogeneous schemas, and show that naive schema decomposition fails for NER due to merge amplification while yielding a marginal (non-significant) gain for RE. The paper is framed as a \"diagnostic framework\" but is substantively an empirical analysis paper with negative practical results.\n\n## 2. Strengths\n\n- **Well-designed controlled experiments.** The two-paradigm design (count curves + BCS-controlled) is methodologically sound and represents genuine effort to isolate confounding factors. The within-pool analysis (drawing 16-type subsets from the 80-type pool) is a particularly careful control that strengthens the causal interpretation. The permutation test for cross-pool slope consistency (p=0.60) is the right statistical approach.\n\n- **Honest and transparent reporting of negative results.** The paper is admirably forthright about SDGD's failure, the non-significant factorial interaction (p=0.50), the modest pairwise effect sizes (R^2 = 1.3-1.7%), the non-significant RE batch composition gain (p~0.19), and the DocRED BCS effect at higher counts. This level of transparency is uncommon and commendable.\n\n- **Centrality confound analysis is a genuine methodological insight.** The identification that per-type BCS aggregation conflates confusability with centrality on same-domain schemas (MAVEN), supported by the residualized analysis and connected to the embedding anisotropy literature, is the paper's strongest conceptual contribution. The connection to Cai et al. (2021) on local isotropy within clusters is well-motivated.\n\n- **Cross-model and cross-dataset validation.** Testing on Llama-3.1-8B and across four datasets (Few-NERD, FewRel, DocRED, MAVEN) spanning three tasks provides reasonable breadth. The convergent high-BCS floor (~51%) across models is an interesting empirical observation.\n\n- **Thorough limitations section.** Ten specific, substantive limitations are listed, covering model coverage, effect sizes, metric scope, and causal mechanism. This is well above average for the field.\n\n## 3. Weaknesses\n\n- **(Major) The \"multi-channel degradation framework\" formalizes well-known intuitions without substantial novelty.** That more categories cause confusion and that similar categories are more easily confused are foundational observations in psychophysics, categorical perception, and fine-grained classification. The paper's framing as a \"framework\" overstates what is essentially empirical quantification of these known effects in a specific (LLM IE) setting. The \"two channels\" are not discovered mechanisms but labels for expected phenomena. The paper would benefit from honestly positioning itself as \"quantifying the magnitude and separability of known factors in a new setting\" rather than \"identifying\" or \"discovering\" channels. Claiming these as \"orthogonal\" is also misleading given the non-significant interaction test (p=0.50) -- non-significance does not establish orthogonality, it merely fails to reject additivity.\n\n- **(Major) Pairwise SCS explains 1.3-1.7% of variance -- the practical utility of the confusability metric is questionable.** The authors acknowledge this but argue the signal \"compounds at the batch level.\" However, the compounding argument is not rigorously established. The 31.2pp extreme-batch gap is between the *most extreme* possible batches across 80 types; the typical-batch gap is 2-4pp (Section 4.3). For a metric proposed as a \"diagnostic tool,\" explaining ~1.5% of pairwise variance and producing ~3pp typical-batch differences is underwhelming. The paper does not convincingly demonstrate that SCS provides actionable information beyond \"avoid putting obviously similar types together\" -- which practitioners already know.\n\n- **(Major) The main practical contribution (SDGD / confusability-aware batching) either fails or is non-significant.** SDGD fails catastrophically on NER. The RE batch composition gain is +1.4pp with p~0.19, which is not significant. The paper frames this as a \"directionally consistent\" result, but at a top venue, non-significant results cannot be claimed as evidence for a method's utility. The confusability-aware strategy ranks 13th out of 15 random seeds -- essentially indistinguishable from random. This means the paper has no actionable positive practical result.\n\n- **(Major) Incomplete related work -- several directly relevant lines of work are missing or underexplored.** The related work section, while improved from earlier drafts, still misses or underengages with:\n  1. **Fine-grained classification and label confusion literature** -- extensive work in computer vision (e.g., hierarchical classification, label smoothing based on semantic similarity) directly parallels the confusability findings. The observation that similar labels confuse classifiers is well-established in that community.\n  2. **Prompt engineering for structured output** -- work on structured/constrained decoding (e.g., LMQL, Guidance, Outlines) that avoids type confusion entirely by construction.\n  3. **Code-generation approaches (GoLLIE, CodeIE)** that sidestep schema confusion by representing types as code constructs rather than natural language labels in a list -- GoLLIE is cited but the key insight (that code-style schemas may inherently reduce confusability by leveraging syntactic structure) is not discussed.\n  4. **The cognitive science literature on similarity-based interference** in categorization (e.g., exemplar models, prototype theory) that would provide theoretical grounding for the \"semantic interference\" channel.\n  5. **CROSSAGENTIE** (cited but insufficiently engaged) -- their cross-type debate mechanism directly addresses type confusion post-hoc, and the paper should discuss whether their approach implicitly validates the confusability channel.\n\n- **(Major) Single primary model severely limits generalizability claims.** Qwen3-32B is the primary model for all experiments. Llama-3.1-8B validation is partial (Channel 2 not reproduced on NER). No proprietary models tested. The convergent high-BCS floor at ~51% is observed on exactly two models -- calling this a \"task-inherent difficulty ceiling\" is a stretch. The paper acknowledges this in limitations but the claims in the body text often read as more general than the evidence warrants.\n\n- **(Minor) The error taxonomy is descriptive, not a methodological contribution.** Categorizing errors into IntraSub/ExtraSub/Boundary/Hallucination and showing that IntraSub correlates with BCS is descriptive analysis, not a new methodology. The high Spearman rho values (1.0 for NER, 0.954 for RE) are computed over only 4-5 bins, making these rank correlations almost trivially perfect. With 4 bins, any monotonic trend gives rho=1.0. This should not be presented as strong evidence.\n\n- **(Minor) SCS is cosine similarity of type name embeddings -- this is an extremely simple metric.** No type definitions, no examples, no ontological structure. The paper demonstrates that this simple metric captures *something* but the R^2 values suggest it captures very little. More sophisticated confusability measures (e.g., using type definitions, few-shot examples, or the model's own attention patterns) are not explored. Calling this a \"Score\" and giving it an acronym elevates a basic similarity computation beyond what it warrants.\n\n- **(Minor) The \"schema design guidelines\" in the discussion are generic.** \"Prefer single-pass,\" \"use random batching if needed,\" \"prefer hierarchical schemas\" -- these are either obvious or insufficiently supported by the experiments. The paper does not test hierarchical schemas; it only observes that cross-domain schemas behave differently from same-domain ones.\n\n- **(Minor) MAVEN results weaken the narrative.** The count curve goes in the opposite direction (performance increases with more types), the per-type BCS correlation is opposite to the hypothesis, and the pairwise signal exists only with MiniLM (not Qwen3). While the centrality confound analysis is interesting, having one of three primary tasks contradict the main story is a significant caveat.\n\n## 4. Questions for Authors\n\n1. Given that pairwise SCS explains only 1.3-1.7% of variance and the typical-batch accuracy gap is 2-4pp, what is the concrete use case for SCS that goes beyond the intuition \"don't put similar types together\"? Can you provide a scenario where computing SCS would change a practitioner's decision?\n\n2. The non-significant interaction (p=0.50) is described as \"underpowered.\" What sample size would be needed to detect the interaction at the observed effect size? Have you conducted a power analysis? Without one, claiming underpoweredness is speculative.\n\n3. Why was no attempt made to use more informative confusability metrics (e.g., incorporating type definitions, annotation guidelines, or few-shot confusion matrices)? The SCS metric uses only type name strings, which seems to leave substantial signal on the table.\n\n4. GoLLIE and similar code-generation approaches represent types as Python classes rather than items in a list. Have you considered whether such representations inherently reduce the confusability channel? This seems like a natural baseline that would contextualize the practical significance of your findings.\n\n5. The convergent high-BCS floor at ~51% is observed on exactly two models. What is your basis for describing this as a \"task-inherent difficulty ceiling\" rather than a coincidence? Would you expect this to hold for GPT-4 or Claude?\n\n6. For the RE batch composition experiment, the confusability-aware strategy produces an intra-batch BCS reduction of only 0.006 (0.552 vs 0.559). Is this simply a ceiling effect of graph coloring at this granularity? What BCS reduction would be needed to produce a significant accuracy gain, based on your regression models?\n\n7. The claim that the two channels are \"orthogonal\" appears throughout the framing materials and earlier drafts. The current paper is more careful, but the title of the DREAM-generated paper still says \"orthogonal failure modes.\" Can you precisely define what \"orthogonal\" means here given the non-significant interaction test?\n\n## 5. Assessment of Contribution Significance\n\nThe paper's contributions, taken individually, are each below the threshold for a top venue:\n\n- **The \"multi-channel degradation framework\"** formalizes known intuitions. The observation that count and similarity independently affect classification is not novel in itself; what would be novel is a precise mechanistic account (e.g., at the attention level) of how this happens in LLMs specifically.\n\n- **Pairwise confusability validation** produces statistically significant but practically tiny effects (R^2 < 2%). The BCS-controlled experiments show larger gaps but only under extreme conditions; typical conditions yield ~3pp differences.\n\n- **Negative results on SDGD** are informative but the merge amplification phenomenon is essentially \"running the same model on the same text multiple times produces inconsistent outputs\" -- this is a known property of LLMs, not a discovery.\n\n- **Confusability-aware RE batching** is non-significant (p~0.19).\n\n- **The centrality confound** is the most interesting finding but is a supporting observation, not a primary contribution.\n\nTaken together, the paper provides a useful but incremental empirical characterization. It is a solid workshop paper or a reasonable Findings paper. The controlled experimental design is above average, the transparency is commendable, but the novelty and practical impact do not reach the bar for a main conference paper at a top venue.\n\nThe paper would be substantially strengthened by: (1) mechanistic analysis (e.g., attention patterns showing how confusable types interfere), (2) a confusability metric with higher predictive power, (3) a practical mitigation that actually works with statistical significance, or (4) validation on proprietary models to establish generality.\n\n## 6. Preliminary Score and Confidence\n\n**Score: 3 (Weak Reject)**\n\n**Confidence: 4 (High)**\n\n**Justification:** The experimental methodology is careful and the transparency is commendable, but the core contributions do not clear the novelty and significance bar for a top venue. The \"framework\" formalizes known intuitions, the confusability metric has very low explanatory power, all practical interventions either fail or are non-significant, and MAVEN partially contradicts the narrative. The paper reads as a thorough empirical exploration rather than a paper with a clear, strong takeaway that advances the field. The related work has notable gaps. For EMNLP main, I would need either a stronger novel insight, a working practical method, or mechanistic depth that the current version does not provide. I would support acceptance at Findings.\n",
  "project": "schema-dag-extraction",
  "tier": "median",
  "dream_id": "dream_20260516T073533",
  "overall_score": "weak reject",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6699ef0b-6647-4b84-a8c5-c7c7a96057d8",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vKHrSpSkiQj7QGgJvP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33d768c9-5620-429a-97e9-ee52c95cecce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXhwznC8B9YmE2pCCuPMXG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 61112,
      "output_tokens": 3252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 689
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3252,
          "cache_read_input_tokens": 61112,
          "cache_creation_input_tokens": 689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 689,
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

_source line 47 · 2026-05-16T08:20:39.640Z_

<details><summary>↩ Tool result · `toolu_011X4jUdM4BssJ2cXZAkMJfA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/review_report.md\", \"dream_id\": \"dream_20260516T073533\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33d768c9-5620-429a-97e9-ee52c95cecce",
  "isSidechain": true,
  "promptId": "19c67cf1-1292-4914-ba7f-8695efc53dd4",
  "agentId": "a802b76b50c1643e5",
  "type": "user",
  "uuid": "f3be42bc-f27a-41fb-9e12-3983302f4d31",
  "sourceToolAssistantUUID": "33d768c9-5620-429a-97e9-ee52c95cecce",
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

_source line 48 · 2026-05-16T08:20:49.920Z_

Review submitted. Here is a summary of the assessment:

**Score: 3 (Weak Reject) | Confidence: 4/5**

**Key findings from the review:**

**Strengths acknowledged:**
- Well-designed controlled experiments with careful within-pool controls and appropriate statistical methods
- Exceptional transparency about negative results, modest effect sizes, and non-significant findings
- The centrality confound analysis (MAVEN) is a genuine methodological insight, well-connected to the embedding anisotropy literature
- Cross-model/cross-dataset validation provides reasonable breadth

**Major weaknesses identified:**
1. The "multi-channel degradation framework" formalizes well-known intuitions (similar categories confuse classifiers, more categories reduce accuracy) without substantial novelty -- framing as "discovery" overstates the contribution
2. Pairwise SCS explains only 1.3-1.7% of variance; typical-batch gaps are ~3pp -- the metric's practical utility is questionable
3. All practical interventions fail (SDGD) or are non-significant (RE batching at p~0.19, ranking 13th/15 random seeds)
4. Incomplete related work: missing fine-grained classification confusion literature, constrained decoding approaches, cognitive science foundations, and insufficient engagement with code-generation approaches (GoLLIE) that sidestep confusability by design
5. Single primary model (Qwen3-32B) limits generalizability; Channel 2 not reproduced on NER for Llama-8B

**Recommendation:** Solid work for Findings track but below the bar for EMNLP main. Would need mechanistic depth (attention-level analysis), a higher-power confusability metric, or a working practical mitigation to reach main conference acceptance.

Report saved to: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/review_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3be42bc-f27a-41fb-9e12-3983302f4d31",
  "isSidechain": true,
  "agentId": "a802b76b50c1643e5",
  "requestId": "req_011Cb5vS823mn3oEondGYTDN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eaafaee7-4ec1-4b88-b86c-5bed46a91ddd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "cb6965cd-db2a-41dc-ac23-0e72d1208059",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ib1YvUdtxPhVre8cVH45F",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3381,
      "cache_read_input_tokens": 61801,
      "output_tokens": 466,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3381
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 466,
          "cache_read_input_tokens": 61801,
          "cache_creation_input_tokens": 3381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3381,
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
