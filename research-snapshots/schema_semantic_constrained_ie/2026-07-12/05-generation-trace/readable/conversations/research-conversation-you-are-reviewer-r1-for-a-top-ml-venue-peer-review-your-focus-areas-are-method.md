# Research conversation: You are Reviewer R1 for a top ML venue peer review. Your focus areas are **Methods** and **Experiments**. Evaluate the p

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ac95df3e3c5999630.jsonl`
- **Structured JSON:** [`33e857bdba26fcafea05.json`](../../sessions/33/33e857bdba26fcafea05.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

61 recorded events

### User

_source line 1 · 2026-05-14T10:50:46.558Z_

You are Reviewer R1 for a top ML venue peer review. Your focus areas are **Methods** and **Experiments**. Evaluate the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary

**Title:** Type-Valid IE via Compiled Ontology Constraints

The paper presents ONTOCODEC, a framework that compiles IE ontology schemas into two composable constrained decoding layers for LLM-based zero-shot information extraction:
1. A **grammar layer** using XGrammar CFG constraints to enforce valid JSON structure, relation names ∈ R, entity types ∈ E
2. A **semantic layer** with a stateful entity registry + dynamic logit masking to enforce domain/range constraints

**Key results:**
- SciERC (7 relations): 94% DR reduction (15.4%→0.93%), F1-neutral (8.23→8.36)
- DocRED (96 relations): 46% DR reduction (18.7%→10.2%), F1-neutral (8.24→8.17)
- Grammar layer: ET→0%, RV→0% on both datasets (perfect generalization)
- Enabling dependency: grammar amplifies semantic effectiveness 3.9× on SciERC, 1.6× on DocRED
- CF violations introduced as side effect: 9.9% SciERC, 2.6% DocRED (100% from semantic layer)
- Latency overhead: ~23% grammar-only, ~62% full S1
- Violation landscape study: constraint tightness predicts residual DR (Spearman ρ=0.82 SciERC, ρ=0.37 DocRED)

**Experimental design from review_context.yaml (imagined experiments list):**
The full experiment plan included 6 experiments:
1. DocRED Phase 2 Unconstrained Baseline — confirms Phase 2 code path introduces no confound
2. DocRED Phase 2 Semantic-only Constrained Decoding — enabling dependency quantification on 96-relation ontology
3. DocRED Per-relation DR Analysis & Tightness-DR Spearman Correlation — per-relation distribution + tightness correlation
4. DocRED CF Composition Deep Dive — sub-type decomposition of CF violations (EVR vs WR, ambiguity vs systematic)
5. Latency Comparison: Constrained vs Unconstrained Decoding — wall time + throughput measurements
6. Cross-model Validation (Llama-3.1-8B on SciERC) — **NOT COMPLETED** (GPU time constraints)

The paper covers experiments 1-5 but NOT experiment 6 (cross-model validation).

## Your Review Task

Provide a structured review covering:

### 1. Methods Assessment
- Is the two-layer (grammar + semantic) architecture well-motivated and technically sound?
- Is the decidability taxonomy (purely local / prefix-decidable / truly non-local) correct and useful?
- Is the layer composition (bitwise AND of masks) with fallback well-designed?
- Is the enabling dependency argument convincing?
- Are there any technical gaps or flaws in the method design?

### 2. Experiments Assessment
- Are the experimental configurations (unconstrained / grammar_only / semantic_only / full_s1 / full_s2) sufficient for ablation?
- Is the evaluation methodology sound (violation rate metrics, F1 verification)?
- How strong is the evidence on SciERC? On DocRED?
- Is the tightness-DR correlation analysis (Spearman) appropriate and convincing?
- Is the CF violation analysis (Table 7, 8) thorough enough?
- Is the latency analysis adequate?
- What about the missing cross-model validation — how serious is this gap?
- Are there missing baselines or comparisons?

### 3. Strengths (bullet points)

### 4. Weaknesses (bullet points)

### 5. Questions for Authors (numbered)

### 6. Preliminary Score and Confidence
- Score: X/6
- Confidence: X/5 (1=low, 5=expert)

Be rigorous but fair. Evaluate what IS in the paper, not what you wish the paper were about.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "30c05939-903d-40f7-9b2b-e57d39a456a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T10:50:46.563Z_

```json
{
  "parentUuid": "30c05939-903d-40f7-9b2b-e57d39a456a0",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
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
  "uuid": "3715e9c1-5c63-4026-8c47-3d9616cee7a1",
  "timestamp": "2026-05-14T10:50:46.563Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T10:50:49.074Z_



I'll start by reading the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3715e9c1-5c63-4026-8c47-3d9616cee7a1",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LGEGqi6ypnRTixYCus",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c13dfd0c-6686-4b4e-9989-2cba28cc2ed1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWxgSxdyYFxZoxwYWfm1EA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15137,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15137,
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

_source line 4 · 2026-05-14T10:50:50.738Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WTVCcVhDBwuk1PkzsKU4W9`</summary>

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
  "parentUuid": "c13dfd0c-6686-4b4e-9989-2cba28cc2ed1",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LGEGqi6ypnRTixYCus",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7777f8b2-5928-4b20-acec-bb5a2be19627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWxgSxdyYFxZoxwYWfm1EA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15137,
      "cache_read_input_tokens": 0,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15137
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15137,
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

_source line 5 · 2026-05-14T10:50:50.744Z_

<details><summary>↩ Tool result · `toolu_01WTVCcVhDBwuk1PkzsKU4W9`</summary>

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
  "parentUuid": "7777f8b2-5928-4b20-acec-bb5a2be19627",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "397bc016-9a69-48f7-b839-ce05cdff550c",
  "sourceToolAssistantUUID": "7777f8b2-5928-4b20-acec-bb5a2be19627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T10:50:53.501Z_



Let me read all the key project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "397bc016-9a69-48f7-b839-ce05cdff550c",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LGYC6f3UoMweUNY8vu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "608ed18c-260a-4273-863a-0b2efbf1225e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LDUr9Zw27dtDffZFWv8bxu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 7 · 2026-05-14T10:50:54.025Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_018pY1rZYkkbSAjSS3MCfL2N`</summary>

```json
{
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "608ed18c-260a-4273-863a-0b2efbf1225e",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LGYC6f3UoMweUNY8vu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e92dfac-a48d-46fd-8aea-9caf72839e9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LDUr9Zw27dtDffZFWv8bxu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 8 · 2026-05-14T10:50:54.113Z_

<details><summary>↩ Tool result · `toolu_018pY1rZYkkbSAjSS3MCfL2N`</summary>

```text
{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (19 个)\n\n- **llama_scierc_full_s1**: QUEUED — \n- **llama_scierc_unconstrained**: QUEUED — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_grammar_only**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_scierc_full_s2**: DONE (success) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| phase2_docred_semantic_only | Semantic-only constrained decoding 在 DocRED (96 relations, avg 5.68 valid pairs) 上的 DR 降低幅度。SciERC semantic_only DR↓24% (15.37→11.65%)，DocRED 约束更紧预期效果更明显。关键验证 Claim 3 enabling dependency：semantic_only 无法消除 RV/ET（需 grammar），证明两层互补非替代。 | — | — | — |\n| phase2_docred_unconstrained | DocRED Phase 2 unconstrained baseline — 使用与 constrained 实验完全相同的 Phase 2 pipeline 和 prompt，确保消融表 F1/violation 对比公平。预期 DR~18.7%, RV~28.9%, ET~7.5%（接近 Phase 0）。 | — | — | — |\n\n## 待处理\n- llama_docred_full_s1（排队等待 GPU）\n- llama_docred_unconstrained（排队等待 GPU）\n- llama_scierc_full_s1（排队等待 GPU）\n- llama_scierc_unconstrained（排队等待 GPU）\n\n## 近期结论\n- **phase2_docred_full_s1** (success): Grammar+Semantic 双层约束 (S1) 在 DocRED (96 relations) 上能否复现 SciERC 的 DR 消除效果 (15.37%→0.93%)？DocRED 约束更紧 (avg 5.68 valid pairs)，DR baseline 更高 (18.7%)，验证 OntoCoDec 在复杂 schema 上的泛化性。\n  [DocRED full_s1 violation report](/api/workspace-files/projects/schema_semantic_constrained_ie/artifacts/phase2_docred_full_s1/report/violation_report_docred_full_s1.json)\n- **phase2_docred_grammar_only** (success): Grammar-only constrained decoding 在 DocRED (96 relation types) 上能否消除 RV violations (28.9%) 和 ET violations (7.5%)？与 SciERC grammar_only (RV 1.4%→0%, ET 0.4%→0%) 对比，验证 grammar 层在复杂 schema 上的泛化性。\n- **mvp_phase0_docred_schema_r2** (killed): Schema-informed prompt 在 DocRED (96 relation types) 上的违规率降低幅度是否小于 SciERC (7 types)？验证约束空间越大 prompt 级干预越力不从心。（从被误杀的 mvp_phase0_docred_schema 恢复，--resume）\n\n## 趋势\n成功 12 / 负向 0 / 失败 0 / 共 13\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-16980: 无 GPU 信息\n\n## 告警\n- mvp_phase0_docred_schema_r2: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e92dfac-a48d-46fd-8aea-9caf72839e9b",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "b5f77b2c-8226-4892-ae43-af09298393d4",
  "sourceToolAssistantUUID": "8e92dfac-a48d-46fd-8aea-9caf72839e9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T10:50:55.042Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GLeU2P4RohQU8xDcVKTGkJ`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5f77b2c-8226-4892-ae43-af09298393d4",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LGYC6f3UoMweUNY8vu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b36b50c7-97cb-4be6-a6fd-053782bf6a8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LDUr9Zw27dtDffZFWv8bxu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 10 · 2026-05-14T10:50:55.063Z_

<details><summary>↩ Tool result · `toolu_01GLeU2P4RohQU8xDcVKTGkJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| phase2_docred_semantic_only | Semantic-only constrained decoding 在 DocRED (96 relations, avg 5.68 valid pairs) 上的 DR 降低幅度。SciERC semantic_only DR↓24% (15.37→11.65%)，DocRED 约束更紧预期效果更明显。关键验证 Claim 3 enabling dependency：semantic_only 无法消除 RV/ET（需 grammar），证明两层互补非替代。 | — | — | — |\\n| phase2_docred_unconstrained | DocRED Phase 2 unconstrained baseline — 使用与 constrained 实验完全相同的 Phase 2 pipeline 和 prompt，确保消融表 F1/violation 对比公平。预期 DR~18.7%, RV~28.9%, ET~7.5%（接近 Phase 0）。 | — | — | — |\\n\\n## 待处理\\n- llama_docred_full_s1（排队等待 GPU）\\n- llama_docred_unconstrained（排队等待 GPU）\\n- llama_scierc_full_s1（排队等待 GPU）\\n- llama_scierc_unconstrained（排队等待 GPU）\\n\\n## 近期结论\\n- **phase2_docred_full_s1** (success): Grammar+Semantic 双层约束 (S1) 在 DocRED (96 relations) 上能否复现 SciERC 的 DR 消除效果 (15.37%→0.93%)？DocRED 约束更紧 (avg 5.68 valid pairs)，DR baseline 更高 (18.7%)，验证 OntoCoDec 在复杂 schema 上的泛化性。\\n  [DocRED full_s1 violation report](/api/workspace-files/projects/schema_semantic_constrained_ie/artifacts/phase2_docred_full_s1/report/violation_report_docred_full_s1.json)\\n- **phase2_docred_grammar_only** (success): Grammar-only constrained decoding 在 DocRED (96 relation types) 上能否消除 RV violations (28.9%) 和 ET violations (7.5%)？与 SciERC grammar_only (RV 1.4%→0%, ET 0.4%→0%) 对比，验证 grammar 层在复杂 schema 上的泛化性。\\n- **mvp_phase0_docred_schema_r2** (killed): Schema-informed prompt 在 DocRED (96 relation types) 上的违规率降低幅度是否小于 SciERC (7 types)？验证约束空间越大 prompt 级干预越力不从心。（从被误杀的 mvp_phase0_docred_schema 恢复，--resume）\\n\\n## 趋势\\n成功 12 / 负向 0 / 失败 0 / 共 13\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-16980: 无 GPU 信息\\n\\n## 告警\\n- mvp_phase0_docred_schema_r2: 已被终止 — unknown\\n\", \"total_chars\": 1767, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b36b50c7-97cb-4be6-a6fd-053782bf6a8e",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "34ddcb60-dd06-439c-9af1-ae073a982ab2",
  "sourceToolAssistantUUID": "b36b50c7-97cb-4be6-a6fd-053782bf6a8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T10:50:55.621Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012YLsDTyuNchg4SZX8QFRCe`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34ddcb60-dd06-439c-9af1-ae073a982ab2",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LGYC6f3UoMweUNY8vu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97e8d5d1-86a1-4f6a-b371-90d6215c59ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LDUr9Zw27dtDffZFWv8bxu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15137,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1448
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 276,
          "cache_read_input_tokens": 15137,
          "cache_creation_input_tokens": 1448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1448,
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

_source line 12 · 2026-05-14T10:50:55.632Z_

<details><summary>↩ Tool result · `toolu_012YLsDTyuNchg4SZX8QFRCe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/ROADMAP.md\", \"content\": \"# schema_semantic_constrained_ie — Research Dashboard\\n\\n> 最后更新: 2026-05-14 06:19 UTC | 更新原因: Reviewer 实测时间线修正 + D009 cross-model 升级为 should-have\\n\\n## 核心方向\\nSchema-semantic constrained decoding for information extraction：利用 ontology schema 在 LLM 解码时施加 grammar + semantic 双层约束，近乎消除 domain/range 违规且不损失 F1。详见 paper_framing.md。\\n\\n## 当前进展\\n**阶段**: Research — Phase 2 SciERC 完成，DocRED 跨数据集验证中 + 论文写作并行\\n**投稿目标**: EMNLP 2026 ARR May 25 | 内部初稿 DDL May 19（距今 5 天）\\n\\n**SciERC Phase 2 核心结果**（全部完成）：\\n- Full S1 (grammar+semantic): DR 15.37%→0.93% (↓94%), R-F1 +0.13pp, ET/RV→0% ← **主推策略**\\n- Full S2 (two-pass): 降级为 ablation (D007)\\n- Grammar only / Semantic only: 两层互补确认\\n\\n**DocRED Phase 2**（4 实验消融）：\\n- grammar_only: RUNNING cuda:0 (653/998, ~20s/doc, 预计 May 14 ~17:00 UTC)\\n- full_s1: RUNNING cuda:1 (568/998, 预计 May 14 ~16:30 UTC)\\n- semantic_only + unconstrained: QUEUED → 预计 May 14 晚至 May 15 凌晨完成\\n- **全部 4 实验预计 May 15 早间就绪**（Reviewer 实测，比初估提前 2-3 天）\\n\\n**Cross-model 验证** (D009, should-have)：\\n- Llama-3.1-8B SciERC: unconstrained + full_s1（2 组，4-6 GPU·h）\\n- 安排在 DocRED 完成后 (May 15)，预计 May 15-16 完成\\n\\n**论文写作进度**：\\n- ✅ §1 Intro, §4 Method, §4.x Composition, §5 SciERC, §6 RelWork, Tables×4, Figs×3\\n- ✅ §2 Background（3 subsections, ~580 words）\\n- ✅ §3 Violation Landscape（4 subsections, per-relation + prompt insufficiency）\\n- ✅ .bib 全部完成（RelWork 9篇 + 新论文 9篇，WebSearch 验证）\\n- ✅ Abstract 初稿（~231 words, DocRED placeholder）\\n- ✅ §7 Conclusion 初稿（~400 words, DocRED placeholder）\\n- ❌ §5 DocRED subsection（等实验结果 → 填 placeholder）\\n- ❌ §5 Cross-model（等 Llama 结果）\\n- May 18-19: 全文校对 + 一致性 → May 19 内部稿\\n\\n## 近期任务\\n- [ ] DocRED grammar_only + full_s1 完成 → 立即提交 QUEUED 两个\\n- [ ] §2 Background + §3 Violation Landscape 完成\\n- [ ] .bib 完成 + 引用验证\\n- [ ] DocRED 4 实验全部完成 → §5 DocRED subsection\\n- [ ] Llama-3.1-8B SciERC 环境准备 + 2 组实验 (D009)\\n- [ ] §5 Cross-model subsection\\n- [ ] Abstract + §7 Conclusion\\n- [ ] experiment_plan.yaml 补全（低优先级，提交前）\\n- [ ] 全文校对 + 一致性检查\\n\\n## GPU 预算\\n- 分配: westd-16980 cuda:0 + cuda:1 (2× GPU)\\n- 当前: 2/2 满载（grammar_only + full_s1）\\n- 预计释放: May 14 ~17:00 UTC → 立即接 QUEUED\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D009 | 2026-05-14 | Llama-3.1-8B cross-model 验证升级为 should-have，SciERC- | phase2_scierc_full_s1, phase2_scierc_unconstrained |\\n| D008 | 2026-05-14 | 补跑 DocRED semantic_only 完成跨数据集全消融；论文写作提前至 DocRED 分 | phase2_docred_grammar_only, phase2_docred_full_s1, phase2_scierc_semantic_only |\\n| D007 | 2026-05-14 | S2 降级为架构 ablation，S1 为主推策略；标题去掉 \\\"Guaranteed\\\" 改 \\\"Ne | phase2_scierc_full_s2, phase2_scierc_full_s1 |\\n| D006 | 2026-05-14 | Phase 2 SciERC 核心结果确认：Full S1 DR -94% 且 F1 无损，CF v | phase2_scierc_unconstrained, phase2_scierc_grammar_only, phase2_scierc_semantic_only, phase2_scierc_full_s1, mvp_phase0_docred_schema |\\n| D005 | 2026-05-14 | Phase 2 SciERC 核心结果确认：Full S1 DR↓94% F1无损，CF viola | phase2_scierc_unconstrained, phase2_scierc_grammar_only, phase2_scierc_semantic_only, phase2_scierc_full_s1 |\\n| D004 | 2026-05-14 | Phase 2 SciERC 核心结果确认：grammar+semantic (full_s1) D | phase2_scierc_unconstrained, phase2_scierc_grammar_only, phase2_scierc_semantic_only, phase2_scierc_full_s1 |\\n| D003 | 2026-05-13 | MVP 通过，进入 Research 阶段，立即启动 Phase 2 constrained dec | mvp_phase0_violation_rate, mvp_phase0_scierc_schema, mvp_phase0_violation_rate_docred |\\n| D002 | 2026-05-13 | SciERC Phase 0 结果确认 GO — domain_range violation ra | mvp_phase0_violation_rate |\\n| D001 | 2026-05-13 | 主目标调整为 EMNLP 2026 ARR (5/25), AAAI 2027 为后备 | — |\\n\\n\\n\", \"total_chars\": 3432, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97e8d5d1-86a1-4f6a-b371-90d6215c59ac",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "6c670b1e-f4e7-42f7-9073-5fa4ecc816f3",
  "sourceToolAssistantUUID": "97e8d5d1-86a1-4f6a-b371-90d6215c59ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T10:50:59.984Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011AUvcFnh9uva1CCB9fvCVe`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c670b1e-f4e7-42f7-9073-5fa4ecc816f3",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LGuGNJnD8NcPSByg98",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd77bf48-7854-4371-8c43-1e8298f3147c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vTbgjhsG8LZevz6ksirpJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4897,
      "cache_read_input_tokens": 16585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4897,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 14 · 2026-05-14T10:50:59.995Z_

<details><summary>↩ Tool result · `toolu_011AUvcFnh9uva1CCB9fvCVe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper_framing.md\", \"content\": \"# OntoCoDec — Paper Framing\\n\\n## Target Venue\\nEMNLP 2026 (ARR submission May 25, 2026)\\n\\n## Title\\nOntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints\\n(Note: \\\"Guaranteed\\\" dropped per Reviewer — S1 DR=0.93%, S2 DR=0.97%, neither achieves 0%. \\\"Near-Complete\\\" is honest and defensible.)\\n\\n## Core Insight\\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero F1 cost** through automatic ontology-to-decoder constraint compilation with two complementary layers.\\n\\n**Phase 2 confirmed**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%), and is **F1-neutral** (R-F1 +0.13pp, not statistically significant — correctly framed as \\\"zero cost\\\", not \\\"improvement\\\").\\n\\n## Core Claims\\n\\n### Claim 1 (Empirical): Violation Landscape\\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\\n\\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\\n\\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\\n\\n### Claim 2 (Empirical): Prompt Insufficiency\\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\\n\\n**Narrative**: This is NOT about \\\"5.78% barely above 5%\\\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\\n\\n### Claim 3 (Methodological): Composable Constraint Framework\\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\\n\\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \\\"synergistic\\\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\\n\\nThe two layers compose via bitwise AND of token masks. Recommended framing: \\\"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\\\"\\n\\n**Graceful degradation** (per Reviewer assessment, D008): When $M_{semantic} \\\\cap M_{grammar} = \\\\emptyset$ (semantic layer would mask all grammar-valid tokens), the system falls back to grammar-only control. Occurred 1/998 DocRED docs (0.1%), 0/551 SciERC sentences — consistent with tighter constraints increasing empty-intersection likelihood. Implementation is error recovery (fallback), NOT formal invariant guarantee. Do NOT frame as \\\"provable composition\\\" — fallback's existence is counter-evidence. Frame as \\\"engineering robustness\\\" in §4; mention cross-dataset observation in §5 Discussion (1-2 sentences, N=1 too weak for dedicated analysis).\\n\\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\\n\\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\\n\\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\\n\\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\\n\\n## Anticipated Reviewer Concerns\\n\\n### C1: \\\"5.78% is barely above 5% — threshold is arbitrary\\\"\\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\\n\\n### C2: \\\"Why not just post-hoc filter?\\\"\\n**Response**: (a) Post-hoc wastes compute on invalid outputs (14-15% rejection rate); (b) cannot redirect probability mass to valid alternatives; (c) for streaming/real-time extraction, post-hoc filtering is too late. Post-hoc approaches (e.g., SHACL/DL reasoner-based validation, Alviano et al. IJCAI 2025 ASP-based structured knowledge verification) validate constraints after generation but cannot correct invalid outputs during decoding. ⚠️ 原引用 \\\"LLM+ASP (ICLP 2025)\\\" 已核实为不准确（venue/方法描述均有误），已修正。\\n\\n### C3: \\\"Bitwise AND of two masks is not novel\\\"\\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\\n\\n### C4: \\\"Evaluate-for violation rate increases with schema-informed prompt\\\"\\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\\\"Method X evaluates for Task Y\\\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \\\"harder instances\\\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\\n\\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\\n\\n### C5: \\\"Only tested on one model (Qwen3-8B)\\\"\\n**Response**: Phase 0 establishes methodology; cross-model validation (Llama-3.1-8B, 70B quantized) planned for Phase 2 if time permits. The constraint compiler is model-agnostic — only the tokenizer-specific first-token verification needs re-running per model.\\n\\n### C6: \\\"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\\\"\\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Phase 2 confirms F1-neutral**: S1 R-F1 0.0836 (+0.13pp vs unconstrained 0.0823), S2 R-F1 0.0803 (-0.20pp vs unconstrained). Both within noise on ~1700 triples. Frame as: \\\"Constraint enforcement is F1-neutral — extraction quality is preserved while violations are near-eliminated.\\\" Do NOT claim F1 improvement (single seed, no bootstrap CI). Note: S2 shows marginally lower F1 and fewer triples (1644 vs 1729) — two-pass does not improve quality.\\n\\n### C7: \\\"Your method trades DR violations for CF violations (cross-field consistency)\\\"\\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\\n\\n**CF 子类型分析（根因已确认）**：\\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\\n\\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\\n\\n**论证层次**：\\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\\n\\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \\\"CF 是 semantic type enforcement 的系统性副作用\\\" 提供干净的消融证据。\\n\\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\\n\\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\\n\\n### C8: \\\"Absolute F1 is too low (~8%) — results are not meaningful\\\"\\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \\\"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\\\"\\n\\n## Paper Structure (Draft)\\n1. Introduction: Violation landscape motivation + composable constraint framework overview\\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\\n5. Experiments: Constrained vs unconstrained vs post-hoc vs prompt-based\\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology)\\n7. Conclusion\\n\\n## Claim Calibration (per Reviewer assessment)\\n\\n**Safe to claim (sufficient evidence from Phase 2)**:\\n- \\\"First systematic study of ontology constraint violations in LLM-based IE\\\"\\n- \\\"Violation rate correlates with constraint tightness, not ontology size\\\"\\n- \\\"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\\\" ✅ Phase 2 confirmed\\n- \\\"Two-layer architecture provides complementary coverage — grammar enables semantic\\\" ✅ Ablation confirmed\\n- \\\"Prompt-level intervention scales poorly with ontology complexity\\\" ✅ SciERC ↓62% vs DocRED ↓32%\\n\\n**Claim with caution**:\\n- \\\"Near-complete type-valid IE\\\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \\\"Near-Complete\\\"\\n- \\\"Principled framework applicable to arbitrary IE ontologies\\\" — validated on 2 datasets + 1 model only\\n- \\\"F1 improvement\\\" — NOT statistically significant, frame as F1-neutral only\\n- \\\"CF reveals type system ambiguity\\\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\\\"因为是 type ambiguity 所以 CF 可接受\\\"\\n\\n**Do NOT claim**:\\n- \\\"General infrastructure for IE\\\" — only zero-shot extraction validated\\n- \\\"State-of-the-art\\\" — F1 is control variable, not optimization target (see C8)\\n- \\\"Synergistic effect\\\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\\n- \\\"S2 solves CF\\\" or \\\"S2 mitigates Structure Snowballing\\\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\\n- \\\"Pilot50 DR=0%\\\" — small-sample artifact, full S2 has DR=0.97%\\n- \\\"Grammar-first invariant\\\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\\n- \\\"Robust dual-layer composition across schema complexities\\\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\\n\\n## Risk Ranking (ordered by reject probability)\\n\\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\\n2. **Single model limitation** (MEDIUM-HIGH): Only Qwen3-8B tested. Mitigation: Llama-3.1-8B cross-model validation if time permits.\\n3. **Novelty perception** (MEDIUM): \\\"PLDI'25 for code → OntoCoDec for IE\\\" attack line. Must argue IE constraint structure differs fundamentally.\\n4. **DocRED Phase 2 weak** (MEDIUM): If constrained decoding on DocRED (96 types) shows weaker gains or higher CF, claim generality is weakened.\\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral. No longer a risk.\\n\\n## Critical Path to EMNLP Submission (May 25)\\n\\n- **May 13-14**: Phase 0 complete ✅ + Phase 1 integration ✅\\n- **May 14 (now)**: Phase 2 SciERC core results confirmed ✅ (unconstrained/grammar/semantic/full_s1). full_s2 running, DocRED Phase 2 starting.\\n- **May 15-17**: DocRED Phase 2 (grammar_only + full_s1) + S2 analysis + CF deep dive + Evaluate-for error cases\\n- **May 17-19**: Cross-model (Llama-3.1-8B) if time permits + ablation gaps\\n- **May 19-24**: Paper writing (Paper Agent) + submission\\n\\n**Current bottleneck**: DocRED Phase 2 cross-dataset validation. GPU 0 should be running DocRED grammar_only NOW.\\n\\n## Status\\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\\n- Phase 2 SciERC S1: ✅ Complete (full_s1 DR↓94%, F1-neutral)\\n- Phase 2 SciERC S2: ✅ Complete (551/551, DR=0.97%, CF=8.03%, R-F1=8.03% — no advantage over S1)\\n- Phase 2 DocRED: 🔄 grammar_only running on cuda:0 (29/998)\\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9%, S2 8.03%, both from independent per-relation enforcement)\\n\", \"total_chars\": 16503, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd77bf48-7854-4371-8c43-1e8298f3147c",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "c208942d-b81c-4951-af12-4c1fc7814acd",
  "sourceToolAssistantUUID": "cd77bf48-7854-4371-8c43-1e8298f3147c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T10:51:00.962Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Q39HzedFM7AhAGfzMuPvH8`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c208942d-b81c-4951-af12-4c1fc7814acd",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LGuGNJnD8NcPSByg98",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0c0c3fe-de70-409e-bd8f-49a89921c9ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vTbgjhsG8LZevz6ksirpJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4897,
      "cache_read_input_tokens": 16585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4897,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 16 · 2026-05-14T10:51:00.973Z_

<details><summary>↩ Tool result · `toolu_01Q39HzedFM7AhAGfzMuPvH8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/decisions.yaml\", \"content\": \"_next_id: 10\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:38 UTC\\n  summary: 主目标调整为 EMNLP 2026 ARR (5/25), AAAI 2027 为后备\\n  rationale: 用户明确指出 EMNLP ARR 5/25 时间不紧、不要保守、资源会给够。12 天 AI 团队速度足够：Phase 0 (1-2天) →\\n    Phase 1 compiler (2-3天) → Phase 2 experiments (2-3天) → Paper (2-3天)。禁止 fallback\\n    思维，冲最高目标。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 19:14 UTC\\n  summary: SciERC Phase 0 结果确认 GO — domain_range violation rate 15.4%，3× 超阈值\\n  rationale: 'SciERC 全量 test set (551 sentences, 1724 triples): domain_range_violation_rate\\n    = 15.4%，远超 5% go/no-go 阈值。违规分布极不均匀 (Feature-of 33.5%, Compare 42.4% vs Used-for\\n    0.76%)，支持\\\"特定 relation types 需要 decoding-time enforcement\\\"的论文 claim。DocRED dry-run\\n    (37 docs) 同样显示 14.4%。两个数据集均为 GO 信号，MVP 核心假设得到强验证。等 schema-informed prompt 结果确认\\n    prompt 级干预不足以解决问题后正式宣布 MVP 通过。'\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: domain_range_violation_rate=15.4%, go_nogo=GO\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 21:48 UTC\\n  summary: MVP 通过，进入 Research 阶段，立即启动 Phase 2 constrained decoding 实验\\n  rationale: Phase 0 三个实验完成：SciERC 15.4%/5.78%, DocRED 18.7% domain_range violation\\n    rate。两个数据集均远超 5% 阈值，核心假设得到强验证。Phase 1 compiler 代码就绪（36 tests 通过），Phase 2 脚本就绪（S1\\n    路径可用，S2 bug 修复中）。cuda:1 空闲，立即启动 Phase 2 SciERC grammar_only/semantic_only/full_s1\\n    实验。\\n  related_experiments:\\n  - exp_id: mvp_phase0_violation_rate\\n    role: primary\\n    result: SciERC DR=15.4%, GO\\n  - exp_id: mvp_phase0_scierc_schema\\n    role: primary\\n    result: SciERC DR=5.78%, prompt insufficient\\n  - exp_id: mvp_phase0_violation_rate_docred\\n    role: primary\\n    result: DocRED DR=18.7%, GO\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 01:53 UTC\\n  summary: Phase 2 SciERC 核心结果确认：grammar+semantic (full_s1) DR↓94% F1 neutral，两层约束协同效应成立\\n  rationale: _v2 干净数据 551 样本全量结果：full_s1 DR=0.93%（baseline 15.37%，↓94%），R-F1 微升 +0.0013。grammar\\n    单独消除 RV/ET，semantic 单独降 DR 24%，组合后 94%——超加性效应。论文核心 claim 站住。早期污染数据 semantic_only\\n    DR=16.43% 已修正为 11.65%。\\n  related_experiments:\\n  - exp_id: phase2_scierc_unconstrained\\n    role: baseline\\n    result: DR=15.37%\\n  - exp_id: phase2_scierc_grammar_only\\n    role: ablation\\n    result: DR=14.84%, RV/ET=0%\\n  - exp_id: phase2_scierc_semantic_only\\n    role: ablation\\n    result: DR=11.65%\\n  - exp_id: phase2_scierc_full_s1\\n    role: core_result\\n    result: DR=0.93%, F1=0.0836\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 01:53 UTC\\n  summary: Phase 2 SciERC 核心结果确认：Full S1 DR↓94% F1无损，CF violation↑124x 作为已知 tradeoff\\n    待 S2 对比后决定处理策略\\n  rationale: v2 干净数据 551/551 全量验证，Reviewer PASS。Grammar+Semantic 协同效应成立，ablation story\\n    清晰。CF violation（0.08%→9.9%）是约束副作用，需等 S2 结果判断是在论文中作为 limitation 还是加 CF 约束修复。\\n  related_experiments:\\n  - exp_id: phase2_scierc_unconstrained\\n    role: baseline\\n    result: DR=15.37%, RV=1.39%, ET=0.4%, RF1=0.0823\\n  - exp_id: phase2_scierc_grammar_only\\n    role: ablation\\n    result: DR=14.84%, RV=0%, ET=0%, RF1=0.0823\\n  - exp_id: phase2_scierc_semantic_only\\n    role: ablation\\n    result: DR=11.65%, RV=1.51%, ET=0.4%, RF1=0.0815\\n  - exp_id: phase2_scierc_full_s1\\n    role: core_result\\n    result: DR=0.93%, RV=0%, ET=0%, RF1=0.0836, CF=9.9%\\n  depends_on: []\\n- id: D006\\n  date: 2026-05-14 01:54 UTC\\n  summary: Phase 2 SciERC 核心结果确认：Full S1 DR -94% 且 F1 无损，CF violation 上升为已知 limitation\\n  rationale: v2 干净数据全量（551/551）结果经 Reviewer PASS 验证：Full S1 DR 15.37%→0.93%（↓94%），R-F1\\n    +0.13pp，ET/RV→0%。Ablation story 清晰（grammar 管格式、semantic 管语义、双层协同）。CF violation\\n    从 0.08%→9.9% 是已知副作用，需在论文中正面报告并论述与 DR 的性质差异。Semantic-only DR=11.65% 说明两层是 multiplicative\\n    关系。决定推进 DocRED Phase 2 跨数据集验证 + 等 S2 对比。\\n  related_experiments:\\n  - exp_id: phase2_scierc_unconstrained\\n    role: baseline\\n    result: DR=15.37%, R-F1=0.0823\\n  - exp_id: phase2_scierc_grammar_only\\n    role: ablation\\n    result: DR=14.84%, RV/ET=0%, F1持平\\n  - exp_id: phase2_scierc_semantic_only\\n    role: ablation\\n    result: DR=11.65%, F1-0.08pp\\n  - exp_id: phase2_scierc_full_s1\\n    role: core_result\\n    result: DR=0.93%, R-F1=0.0836(+0.13pp)\\n  - exp_id: mvp_phase0_docred_schema\\n    role: motivation\\n    result: DocRED DR=12.8%(-32%), 验证prompt级不足\\n  depends_on: []\\n- id: D007\\n  date: 2026-05-14 02:09 UTC\\n  summary: S2 降级为架构 ablation，S1 为主推策略；标题去掉 \\\"Guaranteed\\\" 改 \\\"Near-Complete\\\"\\n  rationale: S2 全量结果(551/551)确认：DR 0.97%(vs S1 0.93%)、CF 8.03%(vs S1 9.9%，降幅不显著)、R-F1\\n    8.03%(vs S1 8.36%)。S2 在所有指标上均未优于 S1，两通道分离未能解决 CF 问题。CF 是 per-relation 独立 type\\n    enforcement 的固有限制，非架构可解。S2 定位从\\\"CF 解决方案\\\"调整为\\\"架构灵活性展示\\\"，论文中放 ablation/appendix。标题\\n    \\\"Guaranteed\\\" 与 0.93% 残余不符，改为 \\\"Near-Complete\\\"。\\n  related_experiments:\\n  - exp_id: phase2_scierc_full_s2\\n    role: primary\\n    result: DR=0.97%, CF=8.03%, R-F1=8.03% — no advantage over S1\\n  - exp_id: phase2_scierc_full_s1\\n    role: baseline\\n    result: DR=0.93%, CF=9.9%, R-F1=8.36%\\n  depends_on: []\\n- id: D008\\n  date: 2026-05-14 04:33 UTC\\n  summary: 补跑 DocRED semantic_only 完成跨数据集全消融；论文写作提前至 DocRED 分析完成后立即启动\\n  rationale: 'SciERC 有 5 路消融但 DocRED 只有 grammar_only + full_s1，缺 semantic_only。Claim\\n    3 (enabling dependency) 在 DocRED 上的证据链不完整——审稿人必问\\\"为何 DocRED 不做 semantic_only 对比\\\"。DocRED\\n    约束更紧(avg 5.68 valid pairs)，semantic_only 预期效果更差，反而是 enabling dependency 的更强证据。论文写作从\\n    5/19 提前到 DocRED 分析完成后(~5/16)，DocRED semantic_only 与写作并行，结果 patch 进去。grammar-semantic\\n    交互 bug (invariant: semantic mask ⊆ grammar allowed set) 需写入 Method section 作为\\n    resolution protocol。'\\n  related_experiments:\\n  - exp_id: phase2_docred_grammar_only\\n    role: running\\n    result: pending\\n  - exp_id: phase2_docred_full_s1\\n    role: running\\n    result: pending\\n  - exp_id: phase2_scierc_semantic_only\\n    role: reference\\n    result: DR↓24% but ET/RV not eliminated\\n  depends_on:\\n  - D006\\n  - D007\\n- id: D009\\n  date: 2026-05-14 06:19 UTC\\n  summary: Llama-3.1-8B cross-model 验证升级为 should-have，SciERC-only (unconstrained +\\n    full_s1)\\n  rationale: Reviewer 实测 DocRED 实验进度远超预期（May 15 早间全部完成 vs 原估 May 17-18），多出 2-3 天 buffer。单模型是最可能的\\n    EMNLP reviewer 批评 (C5)，2 组 SciERC 实验 4-6 GPU 小时即可完成，风险可控。constraint compiler 声称\\n    model-agnostic，跨模型验证是最直接的证据。\\n  related_experiments:\\n  - exp_id: phase2_scierc_full_s1\\n    role: baseline_same_model\\n    result: DR↓94% F1无损\\n  - exp_id: phase2_scierc_unconstrained\\n    role: baseline_same_model\\n    result: DR 15.37%\\n  depends_on:\\n  - D006\\n  - D008\\n\", \"total_chars\": 6314, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0c0c3fe-de70-409e-bd8f-49a89921c9ac",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "dd203868-251f-47dd-8640-78cb5557c7d3",
  "sourceToolAssistantUUID": "c0c0c3fe-de70-409e-bd8f-49a89921c9ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T10:51:01.431Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JRQGcRXYv9eJZnTsukj8i1`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd203868-251f-47dd-8640-78cb5557c7d3",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LGuGNJnD8NcPSByg98",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "788a2a9a-b80e-4d0b-bba9-d27bdf4a841c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vTbgjhsG8LZevz6ksirpJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4897,
      "cache_read_input_tokens": 16585,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4897
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 297,
          "cache_read_input_tokens": 16585,
          "cache_creation_input_tokens": 4897,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4897,
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

_source line 18 · 2026-05-14T10:51:01.439Z_

<details><summary>↩ Tool result · `toolu_01JRQGcRXYv9eJZnTsukj8i1`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "788a2a9a-b80e-4d0b-bba9-d27bdf4a841c",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "a52d9d2c-4600-458d-92e7-04d15ba96dbb",
  "sourceToolAssistantUUID": "788a2a9a-b80e-4d0b-bba9-d27bdf4a841c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T10:51:07.773Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AKv8nR4993W8bjC8dhQVEK`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "ARCHITECTURE.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a52d9d2c-4600-458d-92e7-04d15ba96dbb",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LHLEJB1pG1qGYKxBng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05b20ec3-76fb-490e-ab2d-73d564c0f8c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxnLow89oDzX1SUuycDe62",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9443,
      "cache_read_input_tokens": 21482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9443,
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

_source line 20 · 2026-05-14T10:51:07.787Z_

<details><summary>↩ Tool result · `toolu_01AKv8nR4993W8bjC8dhQVEK`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ARCHITECTURE.md found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05b20ec3-76fb-490e-ab2d-73d564c0f8c4",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "08df2898-db93-4e8e-8b3d-a039132f86dc",
  "sourceToolAssistantUUID": "05b20ec3-76fb-490e-ab2d-73d564c0f8c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T10:51:08.251Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012m2Lp4EDWxLLrpQnrjJebA`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08df2898-db93-4e8e-8b3d-a039132f86dc",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LHLEJB1pG1qGYKxBng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a5a0604-0aff-4efa-acbe-5a226f63f697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxnLow89oDzX1SUuycDe62",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9443,
      "cache_read_input_tokens": 21482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9443,
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

_source line 22 · 2026-05-14T10:51:08.266Z_

<details><summary>↩ Tool result · `toolu_012m2Lp4EDWxLLrpQnrjJebA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/memory.md\", \"content\": \"# Memory — schema_semantic_constrained_ie\\n\\n## 文献调研 (2026-05-13)\\n\\n### 核心结论: OntoCoDec 的 novelty 成立\\n**没有人做过 \\\"compile IE ontology domain/range → decoding-time logits masking\\\" 的完整 pipeline。**\\n\\nGap 结构：\\n- Syntactic constrained decoding for IE: well-explored (GCD, XGrammar, Outlines)\\n- Vocabulary-level: exists (GENRE, iNERD, AdaKGC)\\n- **Semantic (domain/range) decoding for IE: OPEN GAP** ← OntoCoDec\\n- Semantic type checking at decode time: only for code gen (MGD NeurIPS'23, PLDI'25)\\n- Ontology compliance for IE: only post-processing (ODKE+ Apple'25, OntoLogX'25)\\n\\n最近竞争者：PLDI'25 Type-Constrained Code Gen（同机制但领域是代码生成，必须引用并区分）\\n\\n风险：CRANE (ICML'25) 严格约束可能降低推理质量；Grammar-Aligned Decoding (NeurIPS'24) naive masking 扭曲分布\\n\\nNovelty 定位：\\\"OntoCoDec 将 type-constrained generation 引入信息抽取，编译 IE ontology axioms 为解码时语义约束，预防而非检测 type violations。\\\"\\n\\n详细报告: `artifacts/literature_map.yaml`, `artifacts/literature_survey_*.md`\\n\\n## 实验发现\\n\\n### SciERC Phase 0 — Minimal (2026-05-13)\\n- **go_nogo_metric = 15.4%** (domain_range_violation_rate), 3× 超过 5% 阈值 → GO\\n- Violation 分布极不均匀: Used-for 0.76% vs Compare 42.4% vs Feature-of 33.5%\\n- Feature-of + Compare 贡献 72% 的 domain/range violations\\n- Relation vocabulary violations 仅 1.4%\\n- 关键 insight: OntoCoDec 的价值在于精确靶向高违规 relation types\\n\\n### SciERC Phase 0 — Schema-informed (2026-05-13)\\n- **domain_range_violation_rate = 5.78%**（vs minimal 15.37%, -62.4%）\\n- 仍高于 5% 阈值 → prompt 级干预不足以替代 decoding-time enforcement\\n- Entity type violations 降到 0%，relation vocabulary 降到 0.30%\\n- Per-relation: Feature-of -22.3pp, Part-of -22.5pp, Compare -14.8pp\\n- ⚠️ Evaluate-for 反而退步 +5.8pp — prompt 复杂度反而干扰\\n- McNemar 四类全显著 p<0.01\\n- **论文 story**: LLM 能理解约束（-62%）但执行不完美（仍>5%），需要 hard constraint\\n\\n### DocRED Phase 0 — Minimal (2026-05-13)\\n- **domain_range_violation_rate = 18.7%** (16,540 triples, 998 docs)\\n- Relation vocabulary violation = 28.9% (4,775 triples) — 远高于 SciERC 1.4%\\n- Entity type violation = 7.5% (vs SciERC 0.4%)\\n- JSON parse rate = 96.4% (36 docs 解析失败)\\n- Top violators: P31 instance_of (60.4%, 322/533), P1001 applies_to_jurisdiction (44.4%)\\n- 约束更紧(avg 5.68 pairs)确实导致更高违规(18.7% vs 15.4%)\\n\\n### SciERC vs DocRED 对比 (2026-05-13)\\n| 指标 | SciERC (7 rels) | DocRED (96 rels) |\\n|------|----------------|-----------------|\\n| D/R violation | 15.4% | 18.7% (+3.3pp) |\\n| Relation vocab | 1.4% | 28.9% (+27.5pp) |\\n| Entity type | 0.4% | 7.5% (+7.1pp) |\\n| Avg valid pairs | 26.1 | 5.68 |\\n两个数据集都远超 5% 阈值 → 强 GO 信号。Vocabulary layer 在复杂 schema 上尤为关键。\\n\\n### SciERC Phase 2 — Grammar-only (2026-05-13)\\n- **Grammar 层约束是\\\"免费\\\"的**：零 F1 代价完全消除 rv (1.4%→0%) 和 et (0.4%→0%) violations\\n- entity_f1 delta = -0.03pp ≈ 0，relation_f1 delta = 0\\n- **论文 claim**: \\\"Structural constraints can be enforced at zero quality cost\\\"\\n- DR violation 基本不变 (15.37%→14.84%, -0.53pp) — 符合预期，grammar 不含 D/R 约束\\n- DR 热点: Compare 40.85%, Feature-of 31.98%, Part-of 23.38% — 这些是 semantic 层的目标\\n- **决策依据**: grammar 层可以 always-on，无需 ablation 它的\\\"代价\\\"。论文只需关注 semantic 层的 F1 trade-off。\\n\\n### SciERC Phase 2 — 全量最终结果 (2026-05-14, _v2 干净数据)\\n\\n| Mode | R-F1 | E-F1 | DR% | RV% | ET% | ΔDR |\\n|------|------|------|-----|-----|-----|-----|\\n| unconstrained | 0.0823 | 0.3101 | 15.37% | 1.39% | 0.4% | — |\\n| grammar_only | 0.0823 | 0.3098 | 14.84% | 0% | 0% | -0.53pp |\\n| semantic_only | 0.0815 | 0.3101 | 11.65% | 1.51% | 0.4% | -3.72pp |\\n| **full_s1** | **0.0836** | **0.3098** | **0.93%** | **0%** | **0%** | **-14.44pp (↓94%)** |\\n\\n**核心发现**:\\n- **full_s1 是论文核心结果**: DR 15.37%→0.93% (消除 94%), F1 反而微升 +0.0013, 零质量代价\\n- **semantic_only 有效但不够**: DR -3.72pp (↓24%), 但 RV/ET 未消除（需 grammar 层配合）\\n- 早期污染数据 (108样本) 显示 semantic_only DR=16.43%（误导），干净数据实际 11.65%\\n- **Ablation story**: grammar 处理结构约束 (RV, ET), semantic 处理类型约束 (DR), 合并达最佳效果\\n\\n**Per-relation DR (full_s1)**: Used-for/Hyponym-of/Part-of/Conjunction = 0%, Feature-of 1.21%, Compare 2.82%, Evaluate-for 5.76% (残留最多)\\n\\n### SciERC Phase 2 — S2 全量结果 (2026-05-14)\\n| Mode | R-F1 | E-F1 | DR% | CF% |\\n|------|------|------|-----|-----|\\n| full_s1 | 0.0836 | 0.3098 | 0.93% | 9.90% |\\n| full_s2 | 0.0803 | 0.3190 | 0.97% | 8.03% |\\nS1 全面略优 (R-F1 +0.33pp, DR 持平)，S2 降级为 ablation。\\n\\n### DocRED Phase 2 — Grammar-only (2026-05-14)\\n- ET: 7.5%→0%, RV: 28.9%→0.03%, DR 26.17%（grammar 不含 D/R 约束，DR 高于 unconstrained 是因为 grammar 强制合法 relation name 后改变了 triple 分布）\\n- Grammar 层在复杂 schema 上同样完美消除 ET/RV\\n\\n### DocRED Phase 2 — Full S1 结果 (2026-05-14) ⚠️ 关键\\n| 指标 | Phase 0 Unconstrained | Grammar Only | Schema Informed | Full S1 |\\n|------|----------------------|-------------|-----------------|---------|\\n| ET | 7.50% | 0% | 0.61% | **0%** |\\n| RV | 28.90% | 0.03% | 18.40% | **0.03%** |\\n| DR | 18.70% | 26.17% | 12.80% | **10.19%** |\\n| CF | 0.08% | — | 0.15% | 2.57% |\\n| Entity F1 | — | — | — | 0.6534 |\\n| Relation F1 | — | — | — | 0.082 |\\n\\n**关键发现**:\\n1. ✅ Grammar 层在 DocRED 完美泛化: ET/RV→0%（与 SciERC 一致）\\n2. ⚠️ **DR 降幅 scaling gap**: SciERC ↓94% (15.37→0.93%) vs DocRED ↓45.5% (18.7→10.19%)\\n3. 残余 DR 集中在特定关系: P190_sister_city 58%, P582_end_time 43.5%, P205_basin_country 37%, P276_location 28.4%\\n4. Top-10 高 DR 关系贡献 27% 的总 violations (478/1771)\\n5. Semantic 层在 grammar 基础上额外贡献: DR 26.17→10.19% (↓61%)\\n6. CF 从 0.08% 升到 2.57%（低于 SciERC 的 9.9%）\\n7. **Framing 影响**: \\\"near-elimination\\\" 对 ET/RV 成立，DR 需改为 \\\"significant reduction\\\"。复杂 schema 下 entity type 边界模糊是 DR 残余的主因\\n\\n### Constraint Tightness ↔ DR Violation Scaling (2026-05-14) ⚠️ 论文核心 insight\\n**根因分析确认：DR 差异由约束紧度驱动，非 semantic 层失效。**\\n\\n| Tightness 区间 | Valid pairs | DocRED 聚合 DR | SciERC 对应 |\\n|---------------|-------------|---------------|------------|\\n| ≥ 0.95 (极紧) | 1-2 pairs | 30.6% | 无此类 relation |\\n| 0.90-0.94 | 3-4 pairs | 19.3% | 无此类 relation |\\n| < 0.70 (宽松) | 11+ pairs | 0.7% | SciERC 全部在此区间 |\\n\\n- DocRED avg tightness = 0.842 vs SciERC = 0.333\\n- DocRED 中位数仅允许 5/36 type pairs，SciERC 中位数 23/36\\n- 高 tightness 下 semantic∩grammar=∅ 概率高 → fallback 到 grammar-only → DR 未被约束\\n- SciERC DR 低是因为约束本身宽松，LLM 几乎不可能违规\\n- **论文定位**：effectiveness scales inversely with constraint tightness，这是 **contribution** 而非 weakness（首个 constraint scaling 实证，无文献可比）\\n- **文献确认**：无任何论文在 DocRED 上报告 constrained decoding violation rate，我们是首个 benchmark\\n\\n### CF Violation 根因分析 (2026-05-14)\\n- **CF = 跨字段一致性违规**：同一 entity mention 在 entity list 和 relation head/tail 中被标注为不同类型\\n- 根因: semantic constraint 按 per-relation 独立强制 type，导致 entity-vs-relation type drift\\n- 主要冲突: Generic ↔ OtherScientificTerm (60 次, 占比最高)\\n- grammar_only CF=0.08% → S1 CF=9.90% → **CF 100% 来自 semantic 层**\\n- **论文 limitation**: per-relation 独立 type enforcement 的固有副作用，需 future work 做跨 relation entity type 一致性约束\\n\\n### CF 指标口径澄清 (2026-05-14)\\n- violation_checker: 合并所有 type 来源 (entity list + relation head/tail)，denominator = total_entities (2474)\\n- analyze_cf: 分 WR (Within-Relations) + EVR (Entity-vs-Relation) 两维度，denominator 不同 (checked_slots=3380)\\n- **分子一致**: S1=245=245, S2=178 vs 179 (差 1 due to analyze_cf entity_type_map overwrite bug)\\n- **论文统一用 violation_checker 口径**: S1=9.90%, S2=8.03%\\n\\n### S2 Pilot 调查 (2026-05-13)\\n- **原报告 relation_f1=0 是误读**：数据来自 10 样本 dryrun 的 violation_report，非 pilot50 评估\\n- pilot50 实际 relation_f1=0.1008 (13 TP / 146 pred / 112 gold)，与 unconstrained 0.0823 持平\\n- S2 架构可行，DR violation=0% 达标，F1 瓶颈在 entity span 质量（zero-shot entity F1≈0.29）\\n- FP 根因: 52.6% head+tail 都不匹配 gold（entity span 提取错误以平方级放大到 relation）\\n\\n## 技术路线决策\\n\\n### Phase 1 Compiler 完成 (2026-05-13)\\n**HF transformers + XGrammar (standalone)**，代码在 `/root/schema_semantic_constrained_ie/compiler/`：\\n- `ontology_compiler.py`: compile_type_constraints() + build_processor()\\n- `type_mask_processor.py`: _build_first_token_map(), _mask_entity_type/head/tail_type(), _detect_position()\\n- 24 单元测试 + 12 e2e 测试全部通过\\n- SGLang 作为后续性能优化路径，vLLM 暂不可用\\n\\n### Phase 2 脚本完成 (2026-05-13)\\n`run_constrained_extraction.py` (652 行) 支持 5 模式：unconstrained/grammar_only/semantic_only/full_s1/full_s2\\n- 所有模式 dry-run 通过 + violation_checker 兼容\\n\\n### DocRED constrained decoding 就绪 (2026-05-14)\\n`run_constrained_extraction.py --dataset docred` 零代码修改即可运行 grammar_only / full_s1 模式。\\n约束文件: `data/docred/ontology_constraints_docred.json` (6 entity types, 96 relations)\\n建议命令加 `--max_new_tokens 4096`（文档级比句子级长得多）\\n\\n### Grammar-Semantic 交互 Bug 修复 (2026-05-14)\\n**根因**: `compiler/type_mask_processor.py` → `_apply_type_mask`。full_s1 模式下 XGrammar 将 grammar-invalid tokens 设为有限负值 (-1e10)，TypeConstraintProcessor 将 semantically-disallowed types 设为 -inf。当 `allowed_types` 与 grammar-valid tokens 无交集时，所有 grammar-valid tokens 变为 -inf，而 grammar-invalid tokens 仍为 -1e10 (> -inf) → argmax 选中 grammar-invalid token → XGrammar assertion failure。\\n**修复**: `_apply_type_mask` 增加 `_GRAMMAR_MASK_THRESHOLD = -1e8` 安全检查：应用 semantic mask 前验证至少一个 semantically-allowed type 有非 grammar-masked logit；若无交集则跳过 semantic masking，交由 grammar 控制。\\n**论文意义**: 此 invariant（semantic mask ⊆ grammar allowed set）是双层约束架构的关键设计约束，应在 Method section 明确描述。在 SciERC 上未触发是因为约束更松 (avg 26.1 valid pairs vs DocRED 5.68)。\\n\\n### Llama-3.1-8B 兼容性验证 (2026-05-14)\\n- 模型已在服务器: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`\\n- 零代码修改：AutoTokenizer/AutoModelForCausalLM 模型无关，chat_template 自动适配\\n- XGrammar + TypeConstraintProcessor first-token 唯一性验证通过（SciERC 6 types + DocRED 6 types）\\n- pad_token=None 已有处理逻辑\\n\\n### First-token masking 验证 (2026-05-13)\\n简单 first-token masking 安全可用，不需要 trie-based 方案。\\nSciERC: Task=6262, Method=3523, Material=13415, Metric=54310, OtherScientificTerm=11409, Generic=19964\\nDocRED: PER=9654, ORG=44927, LOC=12052, TIME=18129, NUM=17488, MISC=44\\n上下文无关性已验证。\\n\\n## 方法论决策\\n\\n### Violation 分类体系 (2026-05-13)\\n4 类独立计数：entity_type / relation_vocabulary / domain_range / cross_field_consistency\\ngo/no-go 阈值 (5%) 基于 domain_range_violation_rate\\n\\n### Fuzzy Matching (2026-05-13)\\nDocRED: token overlap >80% 或 Levenshtein ≤2\\n\\n## 踩坑记录\\n\\n### submit_training_job 必须 bash -c 包裹 (2026-05-13)\\n- tmux session 默认用 `sh` 执行命令，`source` 和 `conda activate` 是 bash built-in\\n- **直接写 `python3 ...` 会 EXIT_CODE=127 (command not found)**\\n- **正确写法**: `bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 ...\\\"`\\n\\n### 孤儿进程清理误杀活跃实验 (2026-05-14)\\n- Worker 执行孤儿进程清理时，白名单未包含所有活跃实验 PID → SIGTERM 杀掉了 mvp_phase0_docred_schema 和 semantic_only/full_s1\\n- **防护措施**: 清理前必须查 registry 所有 RUNNING 实验的 PID 全部加入白名单; Kill 前检查输出文件行数是否已达 expected count; 只 kill 具体的孤儿 PID\\n- **恢复方式**: JSONL 逐行追加，用 --resume 从断点恢复\\n\\n### 重提交实验前必须清理旧 tmux session (2026-05-13)\\n- retry 未 kill 旧 tmux → 两进程同时写同一 JSONL → null bytes 污染\\n- **规则**: 重提交前先 `tmux kill-session -t &lt;exp_id>`\\n\\n### 禁止在 allocate_and_submit 命令内放 tmux kill-session (2026-05-14)\\n- allocate_and_submit 在 tmux session 内执行命令，`tmux kill-session -t <同名session>` 导致 session 自杀\\n- cron 追踪死 session → 5× miss → 误判 DONE(failed)\\n- **正确做法**: 单独派 Worker 先清理旧 session，确认后再 allocate_and_submit\\n\\n### Cron PID 追踪不可靠 (2026-05-14)\\n- cron 系统导致 4 次假失败（grammar_only / semantic_only / full_s1 / full_s2），每次假失败触发 cleanup worker 又误杀合法进程，恶性循环\\n- **决策**: 对长期运行实验改用手动 `wc -l` 检查输出文件行数判断完成，不依赖 PID/tmux 存活\\n- 完成判断标准: 输出文件行数 = 目标样本数\\n\\n## 环境信息\\n\\n### westd-16980 (2026-05-13)\\n- GPU: 2× NVIDIA RTX PRO 6000 Blackwell (94GB each)\\n- CUDA 12.8, Python 3.12.3 (conda base)\\n- torch 2.10.0+cu128, transformers 4.57.6\\n- 环境激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 模型路径: `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`\\n- Llama 模型路径: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`\\n- XGrammar v2 已安装\\n\\n## 数据信息\\n\\n### SciERC\\n- HuggingFace `zj88zj/SCIERC`, 551 sentences, 7 relation types, 17-35 valid pairs each（约束松散）\\n\\n### DocRED\\n- HuggingFace Hub .gz, 998 docs, 96 relation types, avg 5.68 valid pairs/relation (约束紧)\\n\\n## 分析工具 (2026-05-13)\\n- `compare_prompts.py`: minimal vs schema-informed 对比 + McNemar 检验\\n- `violation_checker.py` / `violation_checker_docred.py`: 4 类 violation 分析\\n\", \"total_chars\": 11588, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a5a0604-0aff-4efa-acbe-5a226f63f697",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "2000c015-3d3a-46ff-b569-356171be2ef6",
  "sourceToolAssistantUUID": "0a5a0604-0aff-4efa-acbe-5a226f63f697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T10:51:09.089Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AmJA3wvivaFPqLn8GAEkEE`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2000c015-3d3a-46ff-b569-356171be2ef6",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LHLEJB1pG1qGYKxBng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff39b6d4-9892-40c0-b3be-2b698c30bd60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxnLow89oDzX1SUuycDe62",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9443,
      "cache_read_input_tokens": 21482,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9443
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 21482,
          "cache_creation_input_tokens": 9443,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9443,
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

_source line 24 · 2026-05-14T10:51:09.099Z_

<details><summary>↩ Tool result · `toolu_01AmJA3wvivaFPqLn8GAEkEE`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff39b6d4-9892-40c0-b3be-2b698c30bd60",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "a8910231-309c-427a-b746-b1e3c2570581",
  "sourceToolAssistantUUID": "ff39b6d4-9892-40c0-b3be-2b698c30bd60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-14T10:51:12.312Z_

Now let me look at the actual paper artifacts and experimental results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8910231-309c-427a-b746-b1e3c2570581",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LHuPqUQVt47M9tMeXU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65228b6c-b232-4025-a180-582624733179",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYkdQmyPWXaouf79YKLyZr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7107,
      "cache_read_input_tokens": 30925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7107,
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

_source line 26 · 2026-05-14T10:51:13.733Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QdPtY8Jj7enTZbqagiHKEw`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65228b6c-b232-4025-a180-582624733179",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LHuPqUQVt47M9tMeXU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba36b45a-cbc1-4c52-813e-1ebde5389d30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYkdQmyPWXaouf79YKLyZr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7107,
      "cache_read_input_tokens": 30925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7107,
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

_source line 27 · 2026-05-14T10:51:13.762Z_

<details><summary>↩ Tool result · `toolu_01QdPtY8Jj7enTZbqagiHKEw`</summary>

```text
artifacts/_project/paper/paper_tables_draft.tex
artifacts/_project/paper/section5_scierc_draft_4796e8.tex
artifacts/_project/paper/section5_scierc_draft.tex
artifacts/_project/paper/section3_method_draft.tex
artifacts/_project/paper/section4_composition_draft.tex
artifacts/_project/paper/abstract_fd4b26.tex
artifacts/_project/paper/abstract_d3264e.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/section7_conclusion.tex
artifacts/_project/paper/section7_conclusion_550cbf.tex
artifacts/_project/paper/section6_relwork_outline.tex
artifacts/_project/paper/section2_background.tex
artifacts/_project/paper/section3_violation_landscape.tex
artifacts/_project/paper/section1_introduction_draft.tex
artifacts/_project/paper/section6_related_work.tex
artifacts/dream_reports/dream_20260514T094226/best/paper.tex
artifacts/dream_reports/dream_20260514T094226/median/paper.tex
artifacts/dream_reports/dream_20260514T094226/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba36b45a-cbc1-4c52-813e-1ebde5389d30",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "5742d5c3-aafc-454e-a0d4-711b64493f9d",
  "sourceToolAssistantUUID": "ba36b45a-cbc1-4c52-813e-1ebde5389d30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T10:51:14.192Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FqRNXqykWeFckLwZdmBrF6`</summary>

```json
{
  "pattern": "**/artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5742d5c3-aafc-454e-a0d4-711b64493f9d",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LHuPqUQVt47M9tMeXU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "631e78f3-7d2e-49d1-a6f9-a4780e2fa797",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYkdQmyPWXaouf79YKLyZr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7107,
      "cache_read_input_tokens": 30925,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7107
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 30925,
          "cache_creation_input_tokens": 7107,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7107,
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

_source line 29 · 2026-05-14T10:51:14.213Z_

<details><summary>↩ Tool result · `toolu_01FqRNXqykWeFckLwZdmBrF6`</summary>

```text
artifacts/analyze_ontology_docred.py
artifacts/violation_checker_docred.py
artifacts/run_extraction_docred.py
artifacts/compare_prompts.py
artifacts/literature_survey_constrained_decoding_ie.md
artifacts/literature_survey_ontology_constrained_ie.md
artifacts/literature_map.yaml
artifacts/run_constrained_extraction.py
artifacts/_project/report/paper_results_summary.md
artifacts/paper_results_summary.md
artifacts/related_work_survey.md
artifacts/_project/chart/fig1_overview.pdf
artifacts/_project/chart/fig2_per_relation_dr.pdf
artifacts/paper_writing_readiness.md
artifacts/_project/report/paper_writing_readiness.md
artifacts/docred_progress_check.md
artifacts/_project/chart/fig3_ablation_layers.png
artifacts/_project/paper/paper_tables_draft.tex
artifacts/_project/report/method_invariant_notes.md
artifacts/method_invariant_notes.md
artifacts/_project/paper/section5_scierc_draft_4796e8.tex
artifacts/_project/paper/section5_scierc_draft.tex
artifacts/_project/report/reference_audit_relwork.md
artifacts/reference_audit_results.md
artifacts/reference_audit_relwork.md
artifacts/_project/paper/section3_method_draft.tex
artifacts/_project/paper/section4_composition_draft.tex
artifacts/_project/paper/abstract_fd4b26.tex
artifacts/_project/paper/abstract_d3264e.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/section7_conclusion.tex
artifacts/_project/paper/section7_conclusion_550cbf.tex
artifacts/_project/paper/section6_relwork_outline.tex
artifacts/_project/paper/relwork_new_entries.bib
artifacts/_project/paper/section2_background.tex
artifacts/phase2_docred_full_s1/report/violation_report_docred_full_s1.json
artifacts/_project/report/d009_llama_prep.md
artifacts/d009_llama_prep.md
artifacts/_project/report/literature_docred_compare.md
artifacts/literature_docred_compare.md
artifacts/docred_full_s1_dr_root_cause_analysis.md
artifacts/dream_reports/dream_20260514T094226/logs/phase1_attempt0.log
artifacts/_project/intermediate/llama_scierc_experiment_commands.md
artifacts/manifest.yaml
artifacts/_project/paper/section3_violation_landscape.tex
artifacts/_project/paper/section1_introduction_draft.tex
artifacts/_project/paper/section6_related_work.tex
artifacts/dream_reports/dream_20260514T094226/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260514T094226/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260514T094226/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T094226/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T094226/best/experiment_data.json
artifacts/dream_reports/dream_20260514T094226/best/paper_framing.md
artifacts/dream_reports/dream_20260514T094226/best/paper.tex
artifacts/dream_reports/dream_20260514T094226/best/paper.aux
artifacts/dream_reports/dream_20260514T094226/best/paper.out
artifacts/dream_reports/dream_20260514T094226/best/paper.pdf
artifacts/dream_reports/dream_20260514T094226/best/paper.log
artifacts/dream_reports/dream_20260514T094226/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T094226/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T094226/median/experiment_data.json
artifacts/dream_reports/dream_20260514T094226/median/paper_framing.md
artifacts/dream_reports/dream_20260514T094226/median/references.bib
artifacts/dream_reports/dream_20260514T094226/median/paper.tex
artifacts/dream_reports/dream_20260514T094226/median/paper.bbl
artifacts/dream_reports/dream_20260514T094226/median/paper.blg
artifacts/dream_reports/dream_20260514T094226/median/paper.aux
artifacts/dream_reports/dream_20260514T094226/median/paper.out
artifacts/dream_reports/dream_20260514T094226/median/paper.pdf
artifacts/dream_reports/dream_20260514T094226/median/paper.log
artifacts/dream_reports/dream_20260514T094226/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T094226/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T094226/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T094226/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T094226/worst/paper.tex
artifacts/dream_reports/dream_20260514T094226/worst/paper.aux
artifacts/dream_reports/dream_20260514T094226/worst/paper.out
artifacts/dream_reports/dream_20260514T094226/worst/paper.pdf
artifacts/dream_reports/dream_20260514T094226/worst/paper.log
artifacts/dream_reports/dream_20260514T094226/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T094226/best/review_context.yaml
artifacts/dream_reports/dream_20260514T094226/logs/orchestrator.log
artifacts/llama_submit_commands.md
artifacts/dream_reports/dream_20260514T094226/best/review_report.md
artifacts/dream_reports/dream_20260514T094226/logs/review_best.log
artifacts/dream_reports/dream_20260514T094226/median/review_context.yaml
artifacts/dream_reports/dream_20260514T094226/logs/review_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "631e78f3-7d2e-49d1-a6f9-a4780e2fa797",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "b12b87c4-eb52-4e5c-b59b-cd1eeee04358",
  "sourceToolAssistantUUID": "631e78f3-7d2e-49d1-a6f9-a4780e2fa797",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T10:51:18.295Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UBVsCbt1T7gUMzJuwSUwm9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b12b87c4-eb52-4e5c-b59b-cd1eeee04358",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LJGf1irbedmMaR3W3b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "238c4f05-1ad7-4bb5-9a11-b3fe752e374b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014tFPSdAqPpSqhPoCj3PgUm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2114,
      "cache_read_input_tokens": 38032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2114,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 31 · 2026-05-14T10:51:18.302Z_

<details><summary>↩ Tool result · `toolu_01UBVsCbt1T7gUMzJuwSUwm9`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{natbib}
12	\usepackage{tabularx}
13	\usepackage{array}
14	
15	\newcommand{\sys}{OntoCoDec}
16	\newcommand{\drr}{domain/range violation rate}
17	
18	\title{\sys{}: Near-Complete Type-Valid Information Extraction\\via Compiled Ontology Constraints}
19	
20	\author{Anonymous}
21	\date{}
22	
23	\begin{document}
24	\maketitle
25	
26	%% ============================================================
27	%% ABSTRACT
28	%% ============================================================
29	\begin{abstract}
30	LLM-based information extraction (IE) systems produce systematic ontology constraint violations---15.4\% of triples on SciERC and 18.7\% on DocRED violate domain/range type constraints.
31	Schema-informed prompting reduces violations by up to 62\% on simple ontologies but scales poorly to complex ones (only 32\% on DocRED's 96-relation ontology), and can even \emph{increase} violations for specific relation types.
32	We present \sys{}, a framework that automatically compiles IE ontology schemas into two composable constrained decoding layers: (1)~a \emph{grammar layer} that enforces structural validity and vocabulary compliance via context-free grammar constraints, and (2)~a \emph{semantic layer} that enforces cross-field domain/range constraints through a stateful entity registry with dynamic logit masking.
33	The two layers compose via bitwise AND of token masks with an enabling dependency: grammar ensures every relation type is valid, enabling semantic lookup of domain/range rules.
34	On SciERC, \sys{} achieves near-complete violation elimination (domain/range violations 15.4\%$\to$0.93\%, $\downarrow$94\%) at zero F1 cost.
35	On DocRED, a complex ontology with inherently high constraint tightness, \sys{} achieves predictable partial reduction (19.0\%$\to$10.19\%, $\downarrow$46\%), with 67\% of relation types reaching $<$2\% violation rate.
36	Residual violations concentrate in a predictable minority of high-tightness relations (Spearman $\rho$=0.52 between constraint tightness and violation rate, $p<$0.001), providing practitioners with a priori estimates of constraint effectiveness.
37	Grammar-layer enforcement generalizes perfectly across datasets (entity-type and relation-vocabulary violations $\to$0\%) and models (Qwen3-8B, Llama-3.1-8B).
38	\end{abstract}
39	
40	%% ============================================================
41	%% 1. INTRODUCTION
42	%% ============================================================
43	\section{Introduction}
44	
45	Large language models have emerged as powerful zero-shot information extraction systems, capable of extracting structured relational triples from unstructured text without task-specific training.
46	However, their outputs frequently violate the type constraints specified by the target ontology.
47	A relation such as \texttt{Feature-of} may require its head entity to be of type \texttt{OtherScientificTerm} and its tail of type \texttt{Method}, yet the model generates type-incompatible entity pairs in over 33\% of instances.
48	
49	These violations are not merely cosmetic. Downstream knowledge graph population, reasoning engines, and regulatory compliance systems require structurally valid triples.
50	Post-hoc filtering discards 14--15\% of generated triples, wasting compute without redirecting probability mass toward valid alternatives.
51	Schema-informed prompting---explicitly describing domain/range constraints in the prompt---provides partial relief but is fundamentally unreliable: on SciERC, it reduces overall violations from 15.4\% to 5.78\% ($\downarrow$62\%), yet the \texttt{Evaluate-for} relation's violation rate \emph{increases} from 24.1\% to 29.9\%, indicating active interference between prompt-level constraint signals and the model's learned type associations.
52	Moreover, prompt-level intervention scales poorly with ontology complexity: on DocRED (96 relations), reduction drops to only 32\%.
53	
54	We make three contributions:
55	
56	\noindent\textbf{(1) Violation Landscape Study.}
57	We present the first systematic measurement of ontology constraint violations in LLM-based IE across two datasets and two models.
58	We show that violation rates are driven by \emph{constraint tightness}---the fraction of the entity-type space excluded by a relation's domain/range rules---not ontology size.
59	SciERC (7 relations) and DocRED (96 relations) exhibit comparable overall violation rates (15.4\% vs.\ 18.7\%) despite a 14$\times$ difference in ontology size.
60	
61	\noindent\textbf{(2) \sys{} Framework.}
62	We propose a two-layer constrained decoding framework that automatically compiles IE ontology schemas into composable decoder constraints.
63	The grammar layer (built on XGrammar) enforces JSON structure, entity-type vocabulary, and relation-type vocabulary via context-free grammar constraints.
64	The semantic layer (TypeConstraintProcessor) maintains a stateful entity registry during autoregressive generation and dynamically masks logits to enforce domain/range type compatibility.
65	The layers compose via bitwise AND with an enabling dependency: grammar ensures valid relation vocabulary, enabling semantic domain/range lookup.
66	
67	\noindent\textbf{(3) Tightness--Violation Correlation.}
68	We establish that per-relation constraint tightness predicts residual violation rates (Spearman $\rho$=0.52, $p<$0.001 on DocRED), with violations concentrating in a predictable minority of high-tightness relations (top 15 relations account for 76.3\% of all violations).
69	This provides practitioners with an a priori diagnostic for estimating constraint effectiveness on new ontologies.
70	
71	%% ============================================================
72	%% 2. BACKGROUND
73	%% ============================================================
74	\section{Background}
75	
76	\subsection{IE Ontology Constraints}
77	
78	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \mathcal{D})$ defines a set of valid entity types $\mathcal{E}$, relation types $\mathcal{R}$, and domain/range constraints $\mathcal{D}: \mathcal{R} \to 2^{\mathcal{E}} \times 2^{\mathcal{E}}$.
79	For each relation $r \in \mathcal{R}$, the constraint $\mathcal{D}(r) = (\mathcal{E}_h^r, \mathcal{E}_t^r)$ specifies the valid head entity types $\mathcal{E}_h^r \subseteq \mathcal{E}$ and tail entity types $\mathcal{E}_t^r \subseteq \mathcal{E}$.
80	A triple $(e_h, r, e_t)$ with $\text{type}(e_h) \notin \mathcal{E}_h^r$ or $\text{type}(e_t) \notin \mathcal{E}_t^r$ constitutes a \emph{domain/range violation}.
81	
82	We define the \emph{constraint tightness} of a relation $r$ as:
83	\begin{equation}
84	    \text{tightness}(r) = 1 - \frac{|\mathcal{E}_h^r| \cdot |\mathcal{E}_t^r|}{|\mathcal{E}|^2}
85	    \label{eq:tightness}
86	\end{equation}
87	A tightness of 1.0 means only one entity-type pair is valid; 0.0 means all pairs are valid (no constraint). This metric captures the fraction of the type space excluded by a relation's constraints.
88	
89	\subsection{Grammar-Constrained Decoding}
90	
91	Grammar-constrained decoding restricts the output of autoregressive language models to strings accepted by a formal grammar, typically a context-free grammar (CFG).
92	At each decoding step, a token mask $M_t \in \{0,1\}^{|V|}$ is computed over the vocabulary $V$, zeroing out logits for tokens that would lead to strings outside the grammar's language.
93	XGrammar compiles grammars into pushdown automata with precomputed token masks, achieving near-zero overhead.
94	
95	Grammar-constrained decoding can enforce structural constraints (valid JSON, correct field names) and vocabulary constraints (entity types $\in \mathcal{E}$, relation types $\in \mathcal{R}$).
96	However, it cannot enforce \emph{cross-field} constraints: whether a generated entity type is compatible with the relation type in the same triple requires maintaining state across generation positions, which is beyond CFG expressiveness.
97	
98	\subsection{Constraint Decidability Taxonomy}
99	
100	We classify IE ontology constraints by prefix-decidability during autoregressive generation:
101	\begin{itemize}
102	    \item \textbf{Type (a) -- Purely local:} Entity type $\in \mathcal{E}$, relation type $\in \mathcal{R}$. Decidable from the current token position alone. Enforceable by grammar.
103	    \item \textbf{Type (b) -- Prefix-decidable with state:} Domain/range compatibility. Requires maintaining an entity registry across generation positions. Enforceable by stateful logit masking (semantic layer).
104	    \item \textbf{Type (c) -- Truly non-local:} Forward coreference (entity mentioned later constrains earlier type assignment). Requires future context; out of scope for forward-only decoding.
105	\end{itemize}
106	
107	%% ============================================================
108	%% 3. VIOLATION LANDSCAPE STUDY
109	%% ============================================================
110	\section{Violation Landscape Study}
111	\label{sec:landscape}
112	
113	Before proposing a solution, we systematically measure the extent and distribution of ontology constraint violations in LLM-based zero-shot IE.
114	
115	\subsection{Experimental Setup}
116	
117	We evaluate Qwen3-8B on two IE benchmarks with structured ontology definitions:
118	
119	\noindent\textbf{SciERC} contains 551 scientific abstracts annotated with 6 entity types and 7 relation types. The ontology is compact but several relations have tight domain/range constraints.
120	
121	\noindent\textbf{DocRED} contains 998 Wikipedia documents annotated with 6 entity types and 96 relation types drawn from Wikidata. The ontology is large and heterogeneous, with wide variance in constraint tightness (mean tightness 0.842, range 0.50--0.97).
122	
123	We measure four violation types: (1)~\emph{entity-type violations} (ET): generated entity type $\notin \mathcal{E}$; (2)~\emph{relation-vocabulary violations} (RV): generated relation type $\notin \mathcal{R}$; (3)~\emph{domain/range violations} (DR): entity type incompatible with relation's domain/range constraints; (4)~\emph{cross-field consistency violations} (CF): same entity assigned different types across relations.
124	
125	\subsection{Unconstrained Baseline Results}
126	
127	Table~\ref{tab:landscape} summarizes the violation landscape.
128	Both datasets exhibit substantial DR rates (15.4\% SciERC, 18.7\% DocRED) despite the 14$\times$ difference in ontology size, confirming that violation rates are driven by constraint structure rather than ontology scale.
129	
130	Schema-informed prompting---embedding explicit domain/range constraint descriptions in the prompt---reduces DR by 62\% on SciERC but only 32\% on DocRED, demonstrating that prompt-level intervention scales poorly with ontology complexity.
131	On SciERC, three relation types retain $>$10\% DR even with schema-informed prompting (Compare: 27.6\%, Evaluate-for: 29.9\%, Feature-of: 11.3\%).
132	The \texttt{Evaluate-for} violation rate \emph{increases} with schema-informed prompting (24.1\%$\to$29.9\%), indicating prior-constraint conflict.
133	
134	\begin{table}[t]
135	\centering
136	\small
137	\caption{Violation landscape: unconstrained LLM-based IE (Qwen3-8B, zero-shot). DR = domain/range violation rate. Schema = schema-informed prompt.}
138	\label{tab:landscape}
139	\begin{tabular}{lcccc}
140	\toprule
141	\textbf{Dataset} & $|\mathcal{R}|$ & \textbf{DR (\%)} & \textbf{Schema DR (\%)} & \textbf{$\Delta$ DR} \\
142	\midrule
143	SciERC  & 7  & 15.4 & 5.78 & $\downarrow$62\% \\
144	DocRED  & 96 & 18.7 & 12.8 & $\downarrow$32\% \\
145	\bottomrule
146	\end{tabular}
147	\end{table}
148	
149	\subsection{Per-Relation Violation Distribution}
150	
151	Violations are not uniformly distributed across relation types.
152	On SciERC, \texttt{Used-for} has only 0.8\% DR while \texttt{Compare} reaches 42.4\%.
153	The key differentiator is constraint tightness: \texttt{Compare} requires both arguments to be of type \texttt{Method}, excluding $>$97\% of the entity-type space, while \texttt{Used-for} accepts a broad range of type pairs.
154	
155	On DocRED (Section~\ref{sec:tightness}), we formally quantify this relationship: Spearman $\rho$=0.52 ($p<$0.001) between constraint tightness and per-relation DR, with a clear monotonic trend across tightness buckets.
156	
157	%% ============================================================
158	%% 4. ONTOCODEC FRAMEWORK
159	%% ============================================================
160	\section{The \sys{} Framework}
161	\label{sec:method}
162	
163	\sys{} automatically compiles an IE ontology schema $\mathcal{O}$ into constrained decoding layers that enforce type validity during autoregressive generation.
164	The framework consists of three components: an ontology compiler, a grammar constraint layer, and a semantic constraint layer.
165	
166	\subsection{Ontology Compiler}
167	
168	The compiler takes as input an ontology definition $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \mathcal{D})$ and produces:
169	\begin{enumerate}
170	    \item A context-free grammar $G$ encoding valid JSON structure with entity-type and relation-type vocabularies;
171	    \item A domain/range lookup table $T: \mathcal{R} \to 2^{\mathcal{E}} \times 2^{\mathcal{E}}$ for runtime type checking.
172	\end{enumerate}
173	The compilation is fully automatic---practitioners provide only the ontology definition (entity types, relation types, and domain/range constraints), requiring zero additional code for schema compliance.
174	
175	\subsection{Grammar Layer}
176	
177	The grammar layer compiles $G$ into an XGrammar pushdown automaton.
178	At each decoding step $t$, it computes a mask $M_t^{\text{gram}} \in \{0,1\}^{|V|}$ that allows only tokens leading to valid JSON with:
179	\begin{itemize}
180	    \item Correct JSON structure (entity list + relation list with typed fields)
181	    \item Entity types $\in \mathcal{E}$
182	    \item Relation types $\in \mathcal{R}$
183	\end{itemize}
184	This eliminates entity-type violations (ET$\to$0\%) and relation-vocabulary violations (RV$\to$0\%) by construction, regardless of the model or ontology size.
185	
186	\subsection{Semantic Layer: TypeConstraintProcessor}
187	
188	The semantic layer maintains a stateful entity registry $\mathcal{S}$ during generation.
189	As entities are generated in the entity list portion of the output, $\mathcal{S}$ records each entity's name and type.
190	When the model generates a relation triple, the processor:
191	\begin{enumerate}
192	    \item Identifies the current generation position (head entity type, relation type, or tail entity type);
193	    \item Looks up the relation type $r$ in the domain/range table $T$;
194	    \item Computes a mask $M_t^{\text{sem}}$ that allows only entity types compatible with $\mathcal{D}(r)$.
195	\end{enumerate}
196	
197	The semantic layer enforces Type~(b) constraints (prefix-decidable with state) that are beyond CFG expressiveness.
198	
199	\subsection{Layer Composition}
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "238c4f05-1ad7-4bb5-9a11-b3fe752e374b",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "03754b27-a7ef-4cda-86ec-2dafcc732e58",
  "sourceToolAssistantUUID": "238c4f05-1ad7-4bb5-9a11-b3fe752e374b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T10:51:18.769Z_

<details open><summary>🔧 Tool call — Read · `toolu_013XhP5BDt6YDWYEETjBvbQ4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03754b27-a7ef-4cda-86ec-2dafcc732e58",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LJGf1irbedmMaR3W3b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb74ee95-ce6a-4dd5-bf17-2784e1b3b89a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014tFPSdAqPpSqhPoCj3PgUm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2114,
      "cache_read_input_tokens": 38032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2114,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 33 · 2026-05-14T10:51:18.775Z_

<details><summary>↩ Tool result · `toolu_013XhP5BDt6YDWYEETjBvbQ4`</summary>

```text
1	tier: best
2	narrative_guidance: '原始 framing 成立，微调定位。Title 保持 ''Near-Complete''，abstract 明确限定：
3	
4	  ''near-complete for tightly-constrained ontologies (94% DR reduction on SciERC),
5	
6	  with predictable partial reduction for complex ontologies (46-55% on DocRED)''。
7	
8	  核心 novelty 三叉：(1) 首个 violation landscape 系统研究，
9	
10	  (2) grammar 层完美跨数据集泛化（ET/RV→0%），
11	
12	  (3) tightness-DR 相关性作为独立 analytical contribution。
13	
14	  DocRED 10.19% 残留 DR 不是弱点而是 tightness theory 的验证数据点。Claims 无需降级。
15	
16	  CF rate 在 DocRED 上显著低于 SciERC（~2.6% vs 9.9%），
17	
18	  进一步支持 "CF 根因是 type system 模糊性" 论点。
19	
20	  '
21	imagined_experiments:
22	- name: DocRED Phase 2 unconstrained baseline
23	  plan_id: P_docred_unconstrained
24	  description: 'DocRED 998 文档，Phase2 code path 无约束运行。
25	
26	    验证 Phase2 环境下的 unconstrained DR 与 Phase0 一致（18-20%），
27	
28	    为计算 DR reduction 提供可比基线。
29	
30	    '
31	  expected_results:
32	    documents: 998
33	    documents_checked: 962
34	    parse_failures: 36
35	    json_parse_rate: 0.964
36	    total_triples: 16600
37	    total_entities: 19200
38	    entity_type_violation_rate: 0.075
39	    relation_vocabulary_violation_rate: 0.289
40	    domain_range_violation_rate: 0.19
41	    domain_range_violations: 3154
42	    cross_field_consistency_violation_rate: 0.001
43	    entity_f1: 59.0
44	    relation_f1: 8.2
45	    relation_precision: 7.0
46	    relation_recall: 9.9
47	    dr_reduction_full_s1_vs_unconstrained_pct: 46.4
48	  result_rationale: 'Phase2 SciERC unconstrained 与 Phase0 完全一致（DR=15.37%），
49	
50	    证明 Phase2 code path 不引入偏差。DocRED 应同样复现 Phase0 数字。
51	
52	    DR 预测 19.0%（vs Phase0 18.7%）：Phase2 unconstrained 使用相同 generation 参数，
53	
54	    但 code path 中的 JSON 后处理可能与 Phase0 略有差异（如 unicode 处理），
55	
56	    导致少量 triples 解析方式不同，~0.3pp 方差在正常范围。
57	
58	    Parse rate 保持 ~96.4%——无 grammar 约束时 JSON 格式错误率是模型固有属性。
59	
60	    RV=28.9% 和 ET=7.5% 复现 Phase0，均为模型在无约束下的自然错误率。
61	
62	    F1 与 grammar_only(8.24) 和 full_s1(8.17) 持平，确认约束 F1-neutral。
63	
64	    dr_reduction 46.4% = (19.0-10.19)/19.0，落入 best 档 [46,55] 下界。
65	
66	    '
67	  tables:
68	  - 'Table 3: DocRED Constrained Decoding Ablation — unconstrained column'
69	  - 'Table 1: Cross-dataset Violation Landscape — DocRED Phase2 unconstrained row'
70	  figures_description:
71	  - 'Figure 4: Enabling dependency grouped bar chart — unconstrained 作为基线参照'
72	  analysis: '关键验证点：Phase2 unconstrained DR ≈ Phase0 DR（±1pp），
73	
74	    确保 reduction 计算分母可比。若偏差 >2pp 需审查 code path 差异。
75	
76	    46.4% reduction 支持 "predictable partial reduction for complex ontologies" 叙事。
77	
78	    '
79	- name: DocRED Phase 2 semantic-only constrained decoding
80	  plan_id: P_docred_semantic_only
81	  description: '仅启用 semantic 层（TypeConstraintProcessor），不启用 grammar 层。
82	
83	    验证 enabling dependency 在复杂 ontology 上跨数据集复现：
84	
85	    无 grammar 保障 relation vocabulary → semantic 层大面积盲区 → DR reduction 显著弱于 full_s1。
86	
87	    '
88	  expected_results:
89	    documents: 998
90	    documents_checked: 958
91	    parse_failures: 40
92	    json_parse_rate: 0.96
93	    total_triples: 16500
94	    total_entities: 19100
95	    entity_type_violation_rate: 0.073
96	    relation_vocabulary_violation_rate: 0.287
97	    domain_range_violation_rate: 0.155
98	    domain_range_violations: 2558
99	    cross_field_consistency_violation_rate: 0.025
100	    entity_f1: 58.5
101	    relation_f1: 8.0
102	    relation_precision: 6.9
103	    relation_recall: 9.5
104	    dr_reduction_vs_unconstrained_pct: 18.4
105	    semantic_enabling_ratio: 2.52
106	  result_rationale: "Enabling dependency 机制：\n1. DocRED unconstrained RV=29%，即 ~29%\
107	    \ triples 使用不在 ontology 中的 relation type。\n   Semantic 层对这些 triples 完全无法检查——未知\
108	    \ relation 查不到 domain/range 规则。\n2. 在剩余 ~71% 合法 relation type 的 triples 中，semantic\
109	    \ 执行 domain/range 检查。\n   但无 grammar 结构保障，JSON 解析失败率 ~4%（vs grammar_only 1.5%），\n\
110	    \   进一步削弱 semantic 的有效覆盖面。实际 semantic 能检查的 triples 约 67-68%。\n3. DR 从 19.0% 降至\
111	    \ 15.5%（-18.4%），远弱于 full_s1 的 46.4%。\n   SciERC 上 semantic_only reduction=24.2%，DocRED\
112	    \ 更低（18.4%）正因 RV 更高\n   （29% vs 1.4%），semantic 盲区更大。\n4. enabling_ratio = (19.0-10.19)/(19.0-15.5)\
113	    \ = 8.81/3.5 = 2.52。\n   Full_s1 的 DR reduction 效力是 semantic_only 的 2.52 倍。\n\
114	    \   SciERC ratio=3.88 更高是因为 SciERC full_s1 几乎完全消除了 DR（0.93%）。\n5. CF 升至 2.5%（vs\
115	    \ unconstrained ~0.1%），模式与 SciERC semantic_only(2.71%) 一致：\n   semantic per-relation\
116	    \ 独立 enforcement 引入跨 relation type 不一致。\n   DocRED CF 略低因为 DocRED entity types\
117	    \ 语义边界更清晰。\n"
118	  tables:
119	  - 'Table 3: DocRED Constrained Decoding Ablation — semantic_only column'
120	  figures_description:
121	  - 'Figure 4: Enabling dependency grouped bar chart — semantic_only 柱明显高于 full_s1'
122	  - 'Figure S1 (Appendix): SciERC vs DocRED enabling ratio 对比'
123	  analysis: 'enabling_ratio=2.52 在 best 档 [2.0, 3.5] 内。
124	
125	    与 SciERC(3.88) 对比，DocRED ratio 更低的原因可量化归因于 RV 差异：
126	
127	    DocRED 29% triples 使用无效 relation（SciERC 仅 1.4%），semantic 盲区面积成比例增大。
128	
129	    论文核心论述：grammar-enables-semantic 在 ontology 复杂度增加时**更加必要**——
130	
131	    DocRED 29% RV 使 semantic 层近三分之一 triples 完全无法检查。
132	
133	    '
134	- name: Latency comparison (constrained vs unconstrained)
135	  plan_id: P011
136	  description: '测量 unconstrained / grammar_only / semantic_only / full_s1 / full_s2
137	
138	    的 tokens/second 和 wall-clock time，量化约束开销的实用性边界。
139	
140	    '
141	  expected_results:
142	    scierc:
143	      unconstrained_tok_per_sec: 13.0
144	      grammar_only_tok_per_sec: 11.5
145	      semantic_only_tok_per_sec: 9.8
146	      full_s1_tok_per_sec: 9.5
147	      full_s2_tok_per_sec: 6.0
148	      overhead_ratio:
149	        grammar_only: 1.13
150	        semantic_only: 1.33
151	        full_s1: 1.37
152	        full_s2: 2.17
153	    docred:
154	      unconstrained_tok_per_sec: 12.5
155	      grammar_only_tok_per_sec: 11.0
156	      full_s1_tok_per_sec: 9.0
157	      overhead_ratio:
158	        grammar_only: 1.14
159	        full_s1: 1.39
160	    wall_clock_per_sample_sec:
161	      scierc_unconstrained: 16
162	      scierc_full_s1: 22
163	      docred_unconstrained: 64
164	      docred_full_s1: 89
165	  result_rationale: "1. Grammar-only 开销 ~13%：XGrammar 用 pushdown automaton + C++ backend\
166	    \ 计算 token mask，\n   高度优化。文献报告 overhead <10%（Dong et al. 2024），但 IE schema 嵌套结构\n\
167	    \   比纯 JSON grammar 复杂（entity list + relation list + nested types），实际稍高。\n2. Semantic\
168	    \ 层额外开销 ~20%：TypeConstraintProcessor 是 Python 实现，\n   每 token 需检查 entity registry\
169	    \ 状态 + 判断生成位置 + 动态计算 logit mask。\n   Python GIL 与 GPU inference 的交互是主要瓶颈。\n3.\
170	    \ Full_s1 ≈ semantic 开销：bitwise AND 两个 mask 是 O(vocab_size) 操作，\n   可忽略不计，所以 full_s1\
171	    \ ≈ max(grammar, semantic) ≈ semantic。\n4. Full_s2 ~2.2x：两个完整 forward pass，\n\
172	    \   Pass 2 还需编译 input-dependent grammar，额外消耗 ~0.1-0.2x。\n5. DocRED 和 SciERC 的\
173	    \ overhead ratio 接近（1.37 vs 1.39），\n   说明开销是 per-token 而非 per-document，与文档长度无关。\n"
174	  tables:
175	  - 'Table 6: Inference Latency Overhead (或 Appendix Table A2)'
176	  figures_description:
177	  - 'Figure S2 (Appendix): Latency overhead bar chart'
178	  analysis: '1.37x overhead 完全可接受。Post-hoc filtering 需重新生成 ~15% 被拒 triples
179	
180	    （等效 ~1.15x 但无法引导到有效输出，且对 streaming 场景不可用）。
181	
182	    S2 的 2.2x 开销 + 无质量优势，进一步确认 S1 为推荐策略。
183	
184	    建议在 §5 用 1 句话报告 overhead，不需单独 section。
185	
186	    '
187	- name: Llama-3.1-8B cross-model violation rate (SciERC)
188	  plan_id: P012
189	  description: '在 Llama-3.1-8B 上复现 SciERC minimal prompt + 可选 full_s1，
190	
191	    验证 violation landscape 和 grammar 泛化性的模型无关性。
192	
193	    '
194	  expected_results:
195	    unconstrained:
196	      total_triples: 1550
197	      total_entities: 2200
198	      json_parse_rate: 0.98
199	      entity_type_violation_rate: 0.006
200	      relation_vocabulary_violation_rate: 0.025
201	      domain_range_violation_rate: 0.145
202	      cross_field_consistency_violation_rate: 0.001
203	      relation_f1: 6.5
204	      entity_f1: 28.0
205	      per_relation_dr:
206	        Used-for: 0.005
207	        Feature-of: 0.3
208	        Compare: 0.38
209	        Evaluate-for: 0.22
210	        Part-of: 0.2
211	        Hyponym-of: 0.12
212	        Conjunction: 0.0
213	    grammar_only:
214	      entity_type_violation_rate: 0.0
215	      relation_vocabulary_violation_rate: 0.0
216	      domain_range_violation_rate: 0.14
217	    full_s1:
218	      entity_type_violation_rate: 0.0
219	      relation_vocabulary_violation_rate: 0.0
220	      domain_range_violation_rate: 0.012
221	      cross_field_consistency_violation_rate: 0.085
222	      relation_f1: 6.8
223	    cross_model_dr_delta_pp:
224	      unconstrained: -0.9
225	      full_s1: 0.3
226	    per_relation_rank_spearman: 0.89
227	  result_rationale: "1. Llama DR ≈ 14.5%（vs Qwen 15.4%，delta=-0.9pp）：\n   Violations\
228	    \ 主要由 ontology constraint structure 驱动。两个 8B 模型在相同 ontology 上\n   的 violation\
229	    \ rate 高度相关——差异来源于训练数据分布（Llama 学术文本比例可能不同），\n   而非根本性的 type assignment 差异。±3pp\
230	    \ 范围内变动。\n2. Grammar 层 ET→0%, RV→0%：grammar 约束是 CFG-expressible，\n   只依赖 tokenizer\
231	    \ vocabulary mapping。XGrammar 自动适配 Llama 的 SentencePiece tokenizer\n   （vs Qwen\
232	    \ 的 tiktoken-based）。ET/RV 消除是 grammar 固有能力，完全模型无关。\n3. Full_s1 DR ≈ 1.2%（vs Qwen\
233	    \ 0.93%）：\n   残留 DR 略高因为 Llama 的 logit distribution 与 Qwen 不同——\n   semantic mask\
234	    \ 后次优 token 是否仍违反约束，取决于模型特定的 token 概率排序。\n   但量级一致（均 <2%），确认方法泛化性。\n4. F1 略低（6.5\
235	    \ vs 8.23）：Llama-3.1-8B 在 zero-shot structured output 上\n   弱于 Qwen3-8B（后者有 code/structured\
236	    \ output 针对性训练）。不影响约束效果评估。\n5. Per-relation rank Spearman ρ=0.89：两个模型的 per-relation\
237	    \ violation 排序\n   高度一致（Compare > Feature-of > Evaluate-for > ...），因为排序由 constraint\
238	    \ tightness 驱动。\n"
239	  tables:
240	  - 'Table 5: Cross-model Violation Rate Comparison'
241	  figures_description:
242	  - 'Figure 5: Cross-model per-relation DR scatter (Qwen x, Llama y), R²>0.75'
243	  analysis: '若 per-relation rank Spearman ρ>0.8，可额外 claim：
244	
245	    "per-relation violation susceptibility is a property of ontology constraint structure,
246	
247	    not the generating model"。Grammar ET/RV→0% 是最干净的跨模型证据。
248	
249	    注意：P012 是 stretch goal，若时间不足可降级为 appendix 或 future work，
250	
251	    不影响 core claims。
252	
253	    '
254	- name: DocRED per-relation tightness-DR Spearman correlation
255	  plan_id: P_analytical_tightness
256	  description: '从 phase2_docred_full_s1 per-relation DR 数据 + DocRED ontology constraint
257	    tightness
258	
259	    计算 Spearman rank correlation。已有 Pearson r=0.3682 (n=90)。
260	
261	    Spearman ρ 预期更高因为关系为单调非线性。
262	
263	    '
264	  expected_results:
265	    pearson_r: 0.3682
266	    pearson_r_note: 已实测（来自 root cause analysis）
267	    spearman_rho: 0.52
268	    spearman_p_value: 2.0e-06
269	    n_relations_analyzed: 82
270	    filter_criterion: ≥10 triples per relation（排除低频噪声）
271	    bucket_level_trend:
272	      tightness_0.95_1.00:
273	        n_rels: 4
274	        agg_dr: 0.306
275	      tightness_0.90_0.94:
276	        n_rels: 15
277	        agg_dr: 0.193
278	      tightness_0.85_0.89:
279	        n_rels: 28
280	        agg_dr: 0.129
281	      tightness_0.80_0.84:
282	        n_rels: 23
283	        agg_dr: 0.07
284	      tightness_0.70_0.79:
285	        n_rels: 18
286	        agg_dr: 0.09
287	      tightness_lt_0.70:
288	        n_rels: 2
289	        agg_dr: 0.007
290	    bucket_level_note: Bucket data 已实测（来自 root cause analysis），展示清晰单调趋势
291	    top10_violation_concentration: 0.78
292	    extreme_relations:
293	      P1198_unemployment_rate:
294	        tightness: 0.944
295	        dr: 0.833
296	        n: 6
297	      P6_head_of_government:
298	        tightness: 0.889
299	        dr: 0.846
300	        n: 13
301	      P35_head_of_state:
302	        tightness: 0.889
303	        dr: 0.647
304	        n: 17
305	      P582_end_time:
306	        tightness: 0.917
307	        dr: 0.435
308	        n: 186
309	      P205_basin_country:
310	        tightness: 0.972
311	        dr: 0.37
312	        n: 108
313	  result_rationale: "1. Pearson r=0.37 已实测。Spearman ρ 预期更高（~0.52）因为：\n   (a) 关系是单调但非线性的——bucket\
314	    \ 数据清晰展示从 0.7% 到 30.6% 的单调上升\n       （仅 0.70-0.79 bucket 有轻微 inversion，agg_DR=9.0%\
315	    \ vs 0.80-0.84 的 7.0%）；\n   (b) Spearman 使用 rank，消除了 DR 右偏分布的 outlier 影响；\n  \
316	    \ (c) 过滤 ≥10 triples 排除了低频关系的小样本噪声（这些关系 DR 要么 0% 要么 100%）。\n2. Pearson r 被低频高\
317	    \ DR 关系拉低：P1198_unemployment_rate（6 triples, DR=83.3%）\n   等极端值在 Pearson 下产生高杠杆效应。Spearman\
318	    \ rank transformation 削弱此影响。\n3. 0.70-0.79 bucket inversion 的原因：该区间包含 P463_member_of（tightness=0.722,\n\
319	    \   DR=9.5%, n=745）——高频关系的 DR 拉高了整个 bucket 的聚合值。\n   这是个别关系的特性，不破坏整体单调趋势。\n4.\
320	    \ ρ=0.52 位于 best 档 [0.5, 0.8] 下端，反映了 tightness 不是 DR 的唯一决定因素：\n   relation frequency、entity\
321	    \ type distribution、model-specific prior 也有贡献。\n   但 tightness 是最强的单一预测因子，ρ=0.52\
322	    \ 在 n=82 下 p<0.001 显著。\n"
323	  tables:
324	  - 'Table 4: DocRED Per-relation DR by Tightness Bucket（已有 bucket 实测数据）'
325	  figures_description:
326	  - 'Figure 3: Scatter plot — x=tightness, y=full_s1 DR, point_size=log(n_triples).
327	    拟合线 + ρ=0.52 annotation. 左下密集聚集（低 tightness, DR≈0%）vs 右上散布（高 tightness, DR 10-85%）'
328	  analysis: 'ρ=0.52 + bucket 单调趋势 + top 15 贡献 76.3% violations = 三重证据支持 tightness
329	    theory。
330	
331	    论文 framing：不强调 ρ 的绝对值（0.52 不算 "strong"），
332	
333	    而强调 (a) bucket 趋势的清晰单调性，(b) violation 的极度集中性（top 15 = 76.3%），
334	
335	    (c) 实用 insight：practitioners 可从 ontology 定义直接预估约束效果。
336	
337	    Fig 3 scatter plot 是 paper 最重要的 figure 之一——一图讲清核心 story。
338	
339	    '
340	- name: DocRED CF violation root cause analysis
341	  plan_id: P_analytical_cf
342	  description: '对 phase2_docred_full_s1 的 519 个 CF violations 进行子类型分解，
343	
344	    与 SciERC CF 模式对比验证 type system ambiguity 假说。
345	
346	    '
347	  expected_results:
348	    cf_violations: 519
349	    cf_denominator_entities: 20218
350	    cf_rate: 0.0257
351	    evr_count: 460
352	    evr_fraction_of_cf: 0.886
353	    evr_entity_rate: 0.023
354	    within_rel_count: 50
355	    within_rel_fraction: 0.096
356	    top_conflict_patterns:
357	    - pattern: ORG↔LOC
358	      count: 120
359	      pct_of_cf: 0.231
360	      example: 国家名在 country_of_citizenship 中标 LOC, 在 headquarters 中标 ORG
361	    - pattern: PER↔ORG
362	      count: 85
363	      pct_of_cf: 0.164
364	      example: 王朝/政权名在 head_of_state 中标 ORG, 在 instance_of 中标 PER
365	    - pattern: TIME↔NUM
366	      count: 65
367	      pct_of_cf: 0.125
368	      example: 年份在 date_of_birth 中标 TIME, 在 P571_inception 中标 NUM
369	    ablation_evidence:
370	      grammar_only_cf: 14
371	      grammar_only_cf_rate: 0.0007
372	      full_s1_cf: 519
373	      full_s1_cf_rate: 0.0257
374	      delta: 505
375	      semantic_attribution: 100% — 505/505 增量 CF 来自 semantic 层
376	    cross_dataset_comparison:
377	      scierc_cf: 0.099
378	      docred_cf: 0.026
379	      ratio: 3.8
380	      explanation: DocRED entity types (PER/ORG/LOC/TIME/NUM/MISC) 语义边界远清晰于 SciERC
381	        (Generic/OtherScientificTerm/Material/Method)
382	    trade_off_ratio:
383	      dr_reduction_pp: 8.81
384	      cf_increase_pp: 2.47
385	      benefit_cost: 3.57
386	  result_rationale: "1. CF=2.57% 远低于 SciERC 9.9%：核心原因是 type system 语义清晰度差异。\n   DocRED\
387	    \ 的 PER/ORG/LOC/TIME/NUM/MISC 在绝大多数上下文中有明确分类标准\n   （人名=PER, 组织=ORG, 地名=LOC），边界模糊区域有限（主要是\
388	    \ ORG↔LOC 的国家实体）。\n   SciERC 的 Generic/OtherScientificTerm/Material/Method 在学术领域大量重叠\n\
389	    \   （\"neural network\" 可以是 Method 也可以是 OtherScientificTerm）。\n2. EVR 占 89%（vs\
390	    \ SciERC >90%）：子类型分布一致。EVR = 同一 entity 在 entity list\n   和 relation triple 中被赋予不同\
391	    \ type，根因是 semantic 层按 relation-specific\n   domain/range 约束选择 type，不维护全局 entity-type\
392	    \ 一致性。\n3. ORG↔LOC 是最大冲突模式（23%）：这是 NER 领域公认的困难 case——\n   国家/城市作为政治实体(ORG) vs\
393	    \ 地理实体(LOC) 是 type system 设计的固有模糊区。\n4. Grammar_only CF=14（0.07%）→ full_s1 CF=519（2.57%），增量\
394	    \ 100% 来自 semantic 层。\n   干净的消融证据：grammar 不引入 CF，CF 是 semantic type enforcement\
395	    \ 的系统性副作用。\n5. Trade-off ratio 3.57:1（每增加 1pp CF 换取 3.57pp DR reduction）。\n  \
396	    \ 结合 DR=hard constraint（triple 不可用）vs CF=soft preference（individual triples 仍\
397	    \ valid），\n   trade-off 高度有利。DocRED 上比 SciERC（93pp/10pp=9.3:1）差但仍 positive。\n"
398	  tables:
399	  - 'Table 5: CF Analysis — Sub-type Breakdown and Cross-dataset Comparison'
400	  figures_description:
401	  - 'Figure S3 (Appendix): CF conflict pattern distribution (DocRED vs SciERC 并列)'
402	  analysis: 'DocRED CF=2.57% 在 best 档 [2%, 3%] 内。
403	
404	    Cross-dataset CF 对比（2.57% vs 9.9%）为 "CF 根因是 type system ambiguity" 提供强证据：
405	
406	    type system 边界越模糊 → CF 越高。这个 finding 应在 §5.3 展开（独立 insight 价值），
407	
408	    同时 §7 保留 CF 作为 limitation + future work（global entity-type consensus）。
409	
410	    论文绝不能暗示 "因为 DocRED CF 低所以 CF 问题不重要"——SciERC 9.9% 仍然 non-trivial。
411	
412	    '
413	- name: Cross-dataset grammar layer generalization verification
414	  plan_id: P_analytical_grammar_gen
415	  description: '系统性汇总 grammar 层在 SciERC（7 relations）和 DocRED（96 relations）上
416	
417	    的 ET/RV 消除率，确认完美泛化作为独立贡献。
418	
419	    '
420	  expected_results:
421	    scierc_grammar_only:
422	      et_violation_rate: 0.0
423	      rv_violation_rate: 0.0
424	      et_violations: 0
425	      rv_violations: 0
426	      total_triples: 1725
427	    docred_grammar_only:
428	      et_violation_rate: 0.0
429	      rv_violation_rate: 0.0003
430	      et_violations: 0
431	      rv_violations: 5
432	      total_triples: 17341
433	    scierc_full_s1:
434	      et_violation_rate: 0.0
435	      rv_violation_rate: 0.0
436	    docred_full_s1:
437	      et_violation_rate: 0.0
438	      rv_violation_rate: 0.0003
439	    cross_dataset_summary:
440	      et_elimination: 100% on both datasets (0/1725 SciERC, 0/17341 DocRED)
441	      rv_elimination: 100% SciERC (0/1725), 99.97% DocRED (5/17341)
442	      ontology_size_invariance: 7 relations → 96 relations (14x) with no degradation
443	  result_rationale: "1. ET/RV 是 CFG-expressible constraints：entity_type ∈ {valid_types},\n\
444	    \   relation_type ∈ {valid_relations}。XGrammar pushdown automaton 可精确 enforce，\n\
445	    \   不依赖生成历史或语义状态，因此与模型和 ontology 大小无关。\n2. SciERC ET=0, RV=0 完美。DocRED ET=0 完美；RV=5/17341=0.03%\
446	    \ 有微小残留。\n   这 5 个 RV 可能源于 tokenizer 边界效应——DocRED 某些 relation name\n   （如 P1001_applies_to_jurisdiction）在\
447	    \ tokenization 时可能触发 XGrammar\n   的 token boundary edge case。5/17341 是 noise level，不影响结论。\n\
448	    3. 从 7 relations 到 96 relations（14x），ET/RV 消除率保持 99.97-100%。\n   Grammar compilation\
449	    \ 自动将 ontology schema 转化为 CFG，\n   schema size 只增加 production rule 数量，不降低 enforcement\
450	    \ 精确性。\n4. 数据已全部就位（来自 phase2_scierc_grammar_only 和 phase2_docred_grammar_only），\n\
451	    \   这是 compilation + formatting，不需新实验。\n"
452	  tables:
453	  - 'Table 2/3: ET 和 RV 列横跨所有配置和数据集'
454	  figures_description:
455	  - 无需独立 figure——Table 中 ET/RV 列的 0%/0.03% 已足够说明
456	  analysis: 'Grammar 完美泛化是 paper 的 "clean win"，无需 caveat。
457	
458	    建议 §5 第一段就报告此 finding（ET/RV→0% across datasets），
459	
460	    先给 reviewer 一个 unambiguously positive result，建立信任后再讨论 DR 的 nuance。
461	
462	    论文可 claim："Grammar-constrained decoding is a solved problem for ontology vocabulary
463	
464	    and entity type compliance in IE—it scales perfectly from 7 to 96 relation types."
465	
466	    '
467	- name: DocRED per-relation DR bimodal distribution analysis
468	  plan_id: P_analytical_bimodal
469	  description: '分析 96 个 DocRED relations 的 full_s1 per-relation DR 分布形态，
470	
471	    验证 >65% 关系 DR<2% 的双峰假设。
472	
473	    '
474	  expected_results:
475	    total_relations: 96
476	    active_relations: 87
477	    filter_5plus_triples: 82
478	    dr_distribution:
479	      dr_eq_0pct: 18
480	      dr_lt_2pct: 55
481	      dr_2_to_10pct: 12
482	      dr_10_to_20pct: 7
483	      dr_20_to_40pct: 6
484	      dr_gt_40pct: 8
485	    near_zero_fraction: 0.67
486	    near_zero_fraction_note: 55/82 = 67%（≥5 triples 的 relations 中 DR<2%）
487	    distribution_statistics:
488	      median_dr: 0.008
489	      mean_dr: 0.102
490	      mean_median_ratio: 12.75
491	      std_dr: 0.18
492	      skewness: 2.1
493	      gini_coefficient: 0.82
494	    top15_concentration: 0.763
495	    top15_concentration_note: 已实测：top 15 relations 贡献 1352/1771 = 76.3% 总违规
496	  result_rationale: "1. 67% relations DR<2%（best 档下界 65%）：DocRED 虽然 avg tightness=0.842（高），\n\
497	    \   但 tightness 分布也有 variance——0.70-0.84 区间的 41 个 relations 中，\n   许多的实际 DR 较低是因为\
498	    \ (a) 高频 entity types（PER, ORG, LOC）自然匹配这些 relation\n   的 domain/range，(b) 模型的\
499	    \ distributional prior 与 ontology 约束高度对齐。\n   仅在 tightness 极高（>0.90）时，prior-constraint\
500	    \ mismatch 才产生显著 DR。\n2. Mean>>Median（12.75x）：经典 heavy-tail 特征。\n   8 个 DR>40%\
501	    \ 的 extreme relations（P1198, P6, P171, P35 等，全部 tightness>0.88）\n   将 mean 拉至\
502	    \ 10.2%（= overall 10.19%），但 median 0.8% 代表 \"典型\" relation 体验。\n3. Gini=0.82：violation\
503	    \ 分布极不平等。类比帕累托法则：~12% 的 relations 贡献 ~80% violations。\n   这不是随机噪声，而是 ontology\
504	    \ constraint structure 的系统性产物。\n4. 双峰形成机制：constraint tightness 作为 bifurcation\
505	    \ parameter——\n   tightness < ~0.80 时 semantic mask 只排除少量 low-probability tokens，\n\
506	    \   model 自然分布已近乎合法，DR→0%（左峰）；\n   tightness > ~0.90 时 mask 必须排除 high-probability\
507	    \ tokens，\n   model 被迫使用低概率 token，DR 急剧上升（右尾）。\n   0.80-0.90 是 transition zone，DR\
508	    \ 分散，中间 bin 较薄。\n"
509	  tables:
510	  - 'Table 4: DocRED Per-relation DR Summary Statistics'
511	  figures_description:
512	  - 'Figure 2: Histogram — 96 relations 的 full_s1 DR 分布. 左峰 (0-2%, ~55 relations)
513	    显著高于右尾 (>20%, ~14 relations). Vertical dashed line at DR=2%. Inset: log-scale
514	    清晰展示右尾结构'
515	  analysis: 'near_zero_fraction=67% 在 best 档 [65%, 80%] 下端。
516	
517	    这个分布图的论文价值：visually 传达 "10.19% overall DR 不是均匀分布的失败"——
518	
519	    对 2/3 的 relations，constrained decoding 已实现 near-complete compliance；
520	
521	    残留 DR 集中在可预测的少数 high-tightness relations。
522	
523	    Fig 2 + Fig 3 (tightness scatter) 构成核心 evidence pair：
524	
525	    分布展示现象（双峰），scatter 解释机制（tightness 驱动）。'
526	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb74ee95-ce6a-4dd5-bf17-2784e1b3b89a",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "889b7b1f-6cd1-4001-9a02-a271313dedbe",
  "sourceToolAssistantUUID": "cb74ee95-ce6a-4dd5-bf17-2784e1b3b89a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T10:51:19.411Z_

<details open><summary>🔧 Tool call — Read · `toolu_0195PCkMa7aDt8etsN1mGRH3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "889b7b1f-6cd1-4001-9a02-a271313dedbe",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LJGf1irbedmMaR3W3b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "134fab54-b9be-4ce1-aa4d-8584f8497d9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014tFPSdAqPpSqhPoCj3PgUm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2114,
      "cache_read_input_tokens": 38032,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2114
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 297,
          "cache_read_input_tokens": 38032,
          "cache_creation_input_tokens": 2114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2114,
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

_source line 35 · 2026-05-14T10:51:19.424Z_

<details><summary>↩ Tool result · `toolu_0195PCkMa7aDt8etsN1mGRH3`</summary>

```text
1	narrative_guidance: '原始 framing 成立，微调定位。Title 保持 ''Near-Complete''，abstract 明确限定：
2	
3	  ''near-complete for tightly-constrained ontologies (94% DR reduction on SciERC),
4	
5	  with predictable partial reduction for complex ontologies (46-55% on DocRED)''。
6	
7	  核心 novelty 三叉：(1) 首个 violation landscape 系统研究，
8	
9	  (2) grammar 层完美跨数据集泛化（ET/RV→0%），
10	
11	  (3) tightness-DR 相关性作为独立 analytical contribution。
12	
13	  DocRED 10.19% 残留 DR 不是弱点而是 tightness theory 的验证数据点。Claims 无需降级。
14	
15	  CF rate 在 DocRED 上显著低于 SciERC（~2.6% vs 9.9%），
16	
17	  进一步支持 "CF 根因是 type system 模糊性" 论点。
18	
19	  '
20	imagined_experiments:
21	- name: DocRED Phase 2 unconstrained baseline
22	  plan_id: P_docred_unconstrained
23	  description: 'DocRED 998 文档，Phase2 code path 无约束运行。
24	
25	    验证 Phase2 环境下的 unconstrained DR 与 Phase0 一致（18-20%），
26	
27	    为计算 DR reduction 提供可比基线。
28	
29	    '
30	  expected_results:
31	    documents: 998
32	    documents_checked: 962
33	    parse_failures: 36
34	    json_parse_rate: 0.964
35	    total_triples: 16600
36	    total_entities: 19200
37	    entity_type_violation_rate: 0.075
38	    relation_vocabulary_violation_rate: 0.289
39	    domain_range_violation_rate: 0.19
40	    domain_range_violations: 3154
41	    cross_field_consistency_violation_rate: 0.001
42	    entity_f1: 59.0
43	    relation_f1: 8.2
44	    relation_precision: 7.0
45	    relation_recall: 9.9
46	    dr_reduction_full_s1_vs_unconstrained_pct: 46.4
47	  result_rationale: 'Phase2 SciERC unconstrained 与 Phase0 完全一致（DR=15.37%），
48	
49	    证明 Phase2 code path 不引入偏差。DocRED 应同样复现 Phase0 数字。
50	
51	    DR 预测 19.0%（vs Phase0 18.7%）：Phase2 unconstrained 使用相同 generation 参数，
52	
53	    但 code path 中的 JSON 后处理可能与 Phase0 略有差异（如 unicode 处理），
54	
55	    导致少量 triples 解析方式不同，~0.3pp 方差在正常范围。
56	
57	    Parse rate 保持 ~96.4%——无 grammar 约束时 JSON 格式错误率是模型固有属性。
58	
59	    RV=28.9% 和 ET=7.5% 复现 Phase0，均为模型在无约束下的自然错误率。
60	
61	    F1 与 grammar_only(8.24) 和 full_s1(8.17) 持平，确认约束 F1-neutral。
62	
63	    dr_reduction 46.4% = (19.0-10.19)/19.0，落入 best 档 [46,55] 下界。
64	
65	    '
66	  tables:
67	  - 'Table 3: DocRED Constrained Decoding Ablation — unconstrained column'
68	  - 'Table 1: Cross-dataset Violation Landscape — DocRED Phase2 unconstrained row'
69	  figures_description:
70	  - 'Figure 4: Enabling dependency grouped bar chart — unconstrained 作为基线参照'
71	  analysis: '关键验证点：Phase2 unconstrained DR ≈ Phase0 DR（±1pp），
72	
73	    确保 reduction 计算分母可比。若偏差 >2pp 需审查 code path 差异。
74	
75	    46.4% reduction 支持 "predictable partial reduction for complex ontologies" 叙事。
76	
77	    '
78	- name: DocRED Phase 2 semantic-only constrained decoding
79	  plan_id: P_docred_semantic_only
80	  description: '仅启用 semantic 层（TypeConstraintProcessor），不启用 grammar 层。
81	
82	    验证 enabling dependency 在复杂 ontology 上跨数据集复现：
83	
84	    无 grammar 保障 relation vocabulary → semantic 层大面积盲区 → DR reduction 显著弱于 full_s1。
85	
86	    '
87	  expected_results:
88	    documents: 998
89	    documents_checked: 958
90	    parse_failures: 40
91	    json_parse_rate: 0.96
92	    total_triples: 16500
93	    total_entities: 19100
94	    entity_type_violation_rate: 0.073
95	    relation_vocabulary_violation_rate: 0.287
96	    domain_range_violation_rate: 0.155
97	    domain_range_violations: 2558
98	    cross_field_consistency_violation_rate: 0.025
99	    entity_f1: 58.5
100	    relation_f1: 8.0
101	    relation_precision: 6.9
102	    relation_recall: 9.5
103	    dr_reduction_vs_unconstrained_pct: 18.4
104	    semantic_enabling_ratio: 2.52
105	  result_rationale: "Enabling dependency 机制：\n1. DocRED unconstrained RV=29%，即 ~29%\
106	    \ triples 使用不在 ontology 中的 relation type。\n   Semantic 层对这些 triples 完全无法检查——未知\
107	    \ relation 查不到 domain/range 规则。\n2. 在剩余 ~71% 合法 relation type 的 triples 中，semantic\
108	    \ 执行 domain/range 检查。\n   但无 grammar 结构保障，JSON 解析失败率 ~4%（vs grammar_only 1.5%），\n\
109	    \   进一步削弱 semantic 的有效覆盖面。实际 semantic 能检查的 triples 约 67-68%。\n3. DR 从 19.0% 降至\
110	    \ 15.5%（-18.4%），远弱于 full_s1 的 46.4%。\n   SciERC 上 semantic_only reduction=24.2%，DocRED\
111	    \ 更低（18.4%）正因 RV 更高\n   （29% vs 1.4%），semantic 盲区更大。\n4. enabling_ratio = (19.0-10.19)/(19.0-15.5)\
112	    \ = 8.81/3.5 = 2.52。\n   Full_s1 的 DR reduction 效力是 semantic_only 的 2.52 倍。\n\
113	    \   SciERC ratio=3.88 更高是因为 SciERC full_s1 几乎完全消除了 DR（0.93%）。\n5. CF 升至 2.5%（vs\
114	    \ unconstrained ~0.1%），模式与 SciERC semantic_only(2.71%) 一致：\n   semantic per-relation\
115	    \ 独立 enforcement 引入跨 relation type 不一致。\n   DocRED CF 略低因为 DocRED entity types\
116	    \ 语义边界更清晰。\n"
117	  tables:
118	  - 'Table 3: DocRED Constrained Decoding Ablation — semantic_only column'
119	  figures_description:
120	  - 'Figure 4: Enabling dependency grouped bar chart — semantic_only 柱明显高于 full_s1'
121	  - 'Figure S1 (Appendix): SciERC vs DocRED enabling ratio 对比'
122	  analysis: 'enabling_ratio=2.52 在 best 档 [2.0, 3.5] 内。
123	
124	    与 SciERC(3.88) 对比，DocRED ratio 更低的原因可量化归因于 RV 差异：
125	
126	    DocRED 29% triples 使用无效 relation（SciERC 仅 1.4%），semantic 盲区面积成比例增大。
127	
128	    论文核心论述：grammar-enables-semantic 在 ontology 复杂度增加时**更加必要**——
129	
130	    DocRED 29% RV 使 semantic 层近三分之一 triples 完全无法检查。
131	
132	    '
133	- name: Latency comparison (constrained vs unconstrained)
134	  plan_id: P011
135	  description: '测量 unconstrained / grammar_only / semantic_only / full_s1 / full_s2
136	
137	    的 tokens/second 和 wall-clock time，量化约束开销的实用性边界。
138	
139	    '
140	  expected_results:
141	    scierc:
142	      unconstrained_tok_per_sec: 13.0
143	      grammar_only_tok_per_sec: 11.5
144	      semantic_only_tok_per_sec: 9.8
145	      full_s1_tok_per_sec: 9.5
146	      full_s2_tok_per_sec: 6.0
147	      overhead_ratio:
148	        grammar_only: 1.13
149	        semantic_only: 1.33
150	        full_s1: 1.37
151	        full_s2: 2.17
152	    docred:
153	      unconstrained_tok_per_sec: 12.5
154	      grammar_only_tok_per_sec: 11.0
155	      full_s1_tok_per_sec: 9.0
156	      overhead_ratio:
157	        grammar_only: 1.14
158	        full_s1: 1.39
159	    wall_clock_per_sample_sec:
160	      scierc_unconstrained: 16
161	      scierc_full_s1: 22
162	      docred_unconstrained: 64
163	      docred_full_s1: 89
164	  result_rationale: "1. Grammar-only 开销 ~13%：XGrammar 用 pushdown automaton + C++ backend\
165	    \ 计算 token mask，\n   高度优化。文献报告 overhead <10%（Dong et al. 2024），但 IE schema 嵌套结构\n\
166	    \   比纯 JSON grammar 复杂（entity list + relation list + nested types），实际稍高。\n2. Semantic\
167	    \ 层额外开销 ~20%：TypeConstraintProcessor 是 Python 实现，\n   每 token 需检查 entity registry\
168	    \ 状态 + 判断生成位置 + 动态计算 logit mask。\n   Python GIL 与 GPU inference 的交互是主要瓶颈。\n3.\
169	    \ Full_s1 ≈ semantic 开销：bitwise AND 两个 mask 是 O(vocab_size) 操作，\n   可忽略不计，所以 full_s1\
170	    \ ≈ max(grammar, semantic) ≈ semantic。\n4. Full_s2 ~2.2x：两个完整 forward pass，\n\
171	    \   Pass 2 还需编译 input-dependent grammar，额外消耗 ~0.1-0.2x。\n5. DocRED 和 SciERC 的\
172	    \ overhead ratio 接近（1.37 vs 1.39），\n   说明开销是 per-token 而非 per-document，与文档长度无关。\n"
173	  tables:
174	  - 'Table 6: Inference Latency Overhead (或 Appendix Table A2)'
175	  figures_description:
176	  - 'Figure S2 (Appendix): Latency overhead bar chart'
177	  analysis: '1.37x overhead 完全可接受。Post-hoc filtering 需重新生成 ~15% 被拒 triples
178	
179	    （等效 ~1.15x 但无法引导到有效输出，且对 streaming 场景不可用）。
180	
181	    S2 的 2.2x 开销 + 无质量优势，进一步确认 S1 为推荐策略。
182	
183	    建议在 §5 用 1 句话报告 overhead，不需单独 section。
184	
185	    '
186	- name: Llama-3.1-8B cross-model violation rate (SciERC)
187	  plan_id: P012
188	  description: '在 Llama-3.1-8B 上复现 SciERC minimal prompt + 可选 full_s1，
189	
190	    验证 violation landscape 和 grammar 泛化性的模型无关性。
191	
192	    '
193	  expected_results:
194	    unconstrained:
195	      total_triples: 1550
196	      total_entities: 2200
197	      json_parse_rate: 0.98
198	      entity_type_violation_rate: 0.006
199	      relation_vocabulary_violation_rate: 0.025
200	      domain_range_violation_rate: 0.145
201	      cross_field_consistency_violation_rate: 0.001
202	      relation_f1: 6.5
203	      entity_f1: 28.0
204	      per_relation_dr:
205	        Used-for: 0.005
206	        Feature-of: 0.3
207	        Compare: 0.38
208	        Evaluate-for: 0.22
209	        Part-of: 0.2
210	        Hyponym-of: 0.12
211	        Conjunction: 0.0
212	    grammar_only:
213	      entity_type_violation_rate: 0.0
214	      relation_vocabulary_violation_rate: 0.0
215	      domain_range_violation_rate: 0.14
216	    full_s1:
217	      entity_type_violation_rate: 0.0
218	      relation_vocabulary_violation_rate: 0.0
219	      domain_range_violation_rate: 0.012
220	      cross_field_consistency_violation_rate: 0.085
221	      relation_f1: 6.8
222	    cross_model_dr_delta_pp:
223	      unconstrained: -0.9
224	      full_s1: 0.3
225	    per_relation_rank_spearman: 0.89
226	  result_rationale: "1. Llama DR ≈ 14.5%（vs Qwen 15.4%，delta=-0.9pp）：\n   Violations\
227	    \ 主要由 ontology constraint structure 驱动。两个 8B 模型在相同 ontology 上\n   的 violation\
228	    \ rate 高度相关——差异来源于训练数据分布（Llama 学术文本比例可能不同），\n   而非根本性的 type assignment 差异。±3pp\
229	    \ 范围内变动。\n2. Grammar 层 ET→0%, RV→0%：grammar 约束是 CFG-expressible，\n   只依赖 tokenizer\
230	    \ vocabulary mapping。XGrammar 自动适配 Llama 的 SentencePiece tokenizer\n   （vs Qwen\
231	    \ 的 tiktoken-based）。ET/RV 消除是 grammar 固有能力，完全模型无关。\n3. Full_s1 DR ≈ 1.2%（vs Qwen\
232	    \ 0.93%）：\n   残留 DR 略高因为 Llama 的 logit distribution 与 Qwen 不同——\n   semantic mask\
233	    \ 后次优 token 是否仍违反约束，取决于模型特定的 token 概率排序。\n   但量级一致（均 <2%），确认方法泛化性。\n4. F1 略低（6.5\
234	    \ vs 8.23）：Llama-3.1-8B 在 zero-shot structured output 上\n   弱于 Qwen3-8B（后者有 code/structured\
235	    \ output 针对性训练）。不影响约束效果评估。\n5. Per-relation rank Spearman ρ=0.89：两个模型的 per-relation\
236	    \ violation 排序\n   高度一致（Compare > Feature-of > Evaluate-for > ...），因为排序由 constraint\
237	    \ tightness 驱动。\n"
238	  tables:
239	  - 'Table 5: Cross-model Violation Rate Comparison'
240	  figures_description:
241	  - 'Figure 5: Cross-model per-relation DR scatter (Qwen x, Llama y), R²>0.75'
242	  analysis: '若 per-relation rank Spearman ρ>0.8，可额外 claim：
243	
244	    "per-relation violation susceptibility is a property of ontology constraint structure,
245	
246	    not the generating model"。Grammar ET/RV→0% 是最干净的跨模型证据。
247	
248	    注意：P012 是 stretch goal，若时间不足可降级为 appendix 或 future work，
249	
250	    不影响 core claims。
251	
252	    '
253	- name: DocRED per-relation tightness-DR Spearman correlation
254	  plan_id: P_analytical_tightness
255	  description: '从 phase2_docred_full_s1 per-relation DR 数据 + DocRED ontology constraint
256	    tightness
257	
258	    计算 Spearman rank correlation。已有 Pearson r=0.3682 (n=90)。
259	
260	    Spearman ρ 预期更高因为关系为单调非线性。
261	
262	    '
263	  expected_results:
264	    pearson_r: 0.3682
265	    pearson_r_note: 已实测（来自 root cause analysis）
266	    spearman_rho: 0.52
267	    spearman_p_value: 2.0e-06
268	    n_relations_analyzed: 82
269	    filter_criterion: ≥10 triples per relation（排除低频噪声）
270	    bucket_level_trend:
271	      tightness_0.95_1.00:
272	        n_rels: 4
273	        agg_dr: 0.306
274	      tightness_0.90_0.94:
275	        n_rels: 15
276	        agg_dr: 0.193
277	      tightness_0.85_0.89:
278	        n_rels: 28
279	        agg_dr: 0.129
280	      tightness_0.80_0.84:
281	        n_rels: 23
282	        agg_dr: 0.07
283	      tightness_0.70_0.79:
284	        n_rels: 18
285	        agg_dr: 0.09
286	      tightness_lt_0.70:
287	        n_rels: 2
288	        agg_dr: 0.007
289	    bucket_level_note: Bucket data 已实测（来自 root cause analysis），展示清晰单调趋势
290	    top10_violation_concentration: 0.78
291	    extreme_relations:
292	      P1198_unemployment_rate:
293	        tightness: 0.944
294	        dr: 0.833
295	        n: 6
296	      P6_head_of_government:
297	        tightness: 0.889
298	        dr: 0.846
299	        n: 13
300	      P35_head_of_state:
301	        tightness: 0.889
302	        dr: 0.647
303	        n: 17
304	      P582_end_time:
305	        tightness: 0.917
306	        dr: 0.435
307	        n: 186
308	      P205_basin_country:
309	        tightness: 0.972
310	        dr: 0.37
311	        n: 108
312	  result_rationale: "1. Pearson r=0.37 已实测。Spearman ρ 预期更高（~0.52）因为：\n   (a) 关系是单调但非线性的——bucket\
313	    \ 数据清晰展示从 0.7% 到 30.6% 的单调上升\n       （仅 0.70-0.79 bucket 有轻微 inversion，agg_DR=9.0%\
314	    \ vs 0.80-0.84 的 7.0%）；\n   (b) Spearman 使用 rank，消除了 DR 右偏分布的 outlier 影响；\n  \
315	    \ (c) 过滤 ≥10 triples 排除了低频关系的小样本噪声（这些关系 DR 要么 0% 要么 100%）。\n2. Pearson r 被低频高\
316	    \ DR 关系拉低：P1198_unemployment_rate（6 triples, DR=83.3%）\n   等极端值在 Pearson 下产生高杠杆效应。Spearman\
317	    \ rank transformation 削弱此影响。\n3. 0.70-0.79 bucket inversion 的原因：该区间包含 P463_member_of（tightness=0.722,\n\
318	    \   DR=9.5%, n=745）——高频关系的 DR 拉高了整个 bucket 的聚合值。\n   这是个别关系的特性，不破坏整体单调趋势。\n4.\
319	    \ ρ=0.52 位于 best 档 [0.5, 0.8] 下端，反映了 tightness 不是 DR 的唯一决定因素：\n   relation frequency、entity\
320	    \ type distribution、model-specific prior 也有贡献。\n   但 tightness 是最强的单一预测因子，ρ=0.52\
321	    \ 在 n=82 下 p<0.001 显著。\n"
322	  tables:
323	  - 'Table 4: DocRED Per-relation DR by Tightness Bucket（已有 bucket 实测数据）'
324	  figures_description:
325	  - 'Figure 3: Scatter plot — x=tightness, y=full_s1 DR, point_size=log(n_triples).
326	    拟合线 + ρ=0.52 annotation. 左下密集聚集（低 tightness, DR≈0%）vs 右上散布（高 tightness, DR 10-85%）'
327	  analysis: 'ρ=0.52 + bucket 单调趋势 + top 15 贡献 76.3% violations = 三重证据支持 tightness
328	    theory。
329	
330	    论文 framing：不强调 ρ 的绝对值（0.52 不算 "strong"），
331	
332	    而强调 (a) bucket 趋势的清晰单调性，(b) violation 的极度集中性（top 15 = 76.3%），
333	
334	    (c) 实用 insight：practitioners 可从 ontology 定义直接预估约束效果。
335	
336	    Fig 3 scatter plot 是 paper 最重要的 figure 之一——一图讲清核心 story。
337	
338	    '
339	- name: DocRED CF violation root cause analysis
340	  plan_id: P_analytical_cf
341	  description: '对 phase2_docred_full_s1 的 519 个 CF violations 进行子类型分解，
342	
343	    与 SciERC CF 模式对比验证 type system ambiguity 假说。
344	
345	    '
346	  expected_results:
347	    cf_violations: 519
348	    cf_denominator_entities: 20218
349	    cf_rate: 0.0257
350	    evr_count: 460
351	    evr_fraction_of_cf: 0.886
352	    evr_entity_rate: 0.023
353	    within_rel_count: 50
354	    within_rel_fraction: 0.096
355	    top_conflict_patterns:
356	    - pattern: ORG↔LOC
357	      count: 120
358	      pct_of_cf: 0.231
359	      example: 国家名在 country_of_citizenship 中标 LOC, 在 headquarters 中标 ORG
360	    - pattern: PER↔ORG
361	      count: 85
362	      pct_of_cf: 0.164
363	      example: 王朝/政权名在 head_of_state 中标 ORG, 在 instance_of 中标 PER
364	    - pattern: TIME↔NUM
365	      count: 65
366	      pct_of_cf: 0.125
367	      example: 年份在 date_of_birth 中标 TIME, 在 P571_inception 中标 NUM
368	    ablation_evidence:
369	      grammar_only_cf: 14
370	      grammar_only_cf_rate: 0.0007
371	      full_s1_cf: 519
372	      full_s1_cf_rate: 0.0257
373	      delta: 505
374	      semantic_attribution: 100% — 505/505 增量 CF 来自 semantic 层
375	    cross_dataset_comparison:
376	      scierc_cf: 0.099
377	      docred_cf: 0.026
378	      ratio: 3.8
379	      explanation: DocRED entity types (PER/ORG/LOC/TIME/NUM/MISC) 语义边界远清晰于 SciERC
380	        (Generic/OtherScientificTerm/Material/Method)
381	    trade_off_ratio:
382	      dr_reduction_pp: 8.81
383	      cf_increase_pp: 2.47
384	      benefit_cost: 3.57
385	  result_rationale: "1. CF=2.57% 远低于 SciERC 9.9%：核心原因是 type system 语义清晰度差异。\n   DocRED\
386	    \ 的 PER/ORG/LOC/TIME/NUM/MISC 在绝大多数上下文中有明确分类标准\n   （人名=PER, 组织=ORG, 地名=LOC），边界模糊区域有限（主要是\
387	    \ ORG↔LOC 的国家实体）。\n   SciERC 的 Generic/OtherScientificTerm/Material/Method 在学术领域大量重叠\n\
388	    \   （\"neural network\" 可以是 Method 也可以是 OtherScientificTerm）。\n2. EVR 占 89%（vs\
389	    \ SciERC >90%）：子类型分布一致。EVR = 同一 entity 在 entity list\n   和 relation triple 中被赋予不同\
390	    \ type，根因是 semantic 层按 relation-specific\n   domain/range 约束选择 type，不维护全局 entity-type\
391	    \ 一致性。\n3. ORG↔LOC 是最大冲突模式（23%）：这是 NER 领域公认的困难 case——\n   国家/城市作为政治实体(ORG) vs\
392	    \ 地理实体(LOC) 是 type system 设计的固有模糊区。\n4. Grammar_only CF=14（0.07%）→ full_s1 CF=519（2.57%），增量\
393	    \ 100% 来自 semantic 层。\n   干净的消融证据：grammar 不引入 CF，CF 是 semantic type enforcement\
394	    \ 的系统性副作用。\n5. Trade-off ratio 3.57:1（每增加 1pp CF 换取 3.57pp DR reduction）。\n  \
395	    \ 结合 DR=hard constraint（triple 不可用）vs CF=soft preference（individual triples 仍\
396	    \ valid），\n   trade-off 高度有利。DocRED 上比 SciERC（93pp/10pp=9.3:1）差但仍 positive。\n"
397	  tables:
398	  - 'Table 5: CF Analysis — Sub-type Breakdown and Cross-dataset Comparison'
399	  figures_description:
400	  - 'Figure S3 (Appendix): CF conflict pattern distribution (DocRED vs SciERC 并列)'
401	  analysis: 'DocRED CF=2.57% 在 best 档 [2%, 3%] 内。
402	
403	    Cross-dataset CF 对比（2.57% vs 9.9%）为 "CF 根因是 type system ambiguity" 提供强证据：
404	
405	    type system 边界越模糊 → CF 越高。这个 finding 应在 §5.3 展开（独立 insight 价值），
406	
407	    同时 §7 保留 CF 作为 limitation + future work（global entity-type consensus）。
408	
409	    论文绝不能暗示 "因为 DocRED CF 低所以 CF 问题不重要"——SciERC 9.9% 仍然 non-trivial。
410	
411	    '
412	- name: Cross-dataset grammar layer generalization verification
413	  plan_id: P_analytical_grammar_gen
414	  description: '系统性汇总 grammar 层在 SciERC（7 relations）和 DocRED（96 relations）上
415	
416	    的 ET/RV 消除率，确认完美泛化作为独立贡献。
417	
418	    '
419	  expected_results:
420	    scierc_grammar_only:
421	      et_violation_rate: 0.0
422	      rv_violation_rate: 0.0
423	      et_violations: 0
424	      rv_violations: 0
425	      total_triples: 1725
426	    docred_grammar_only:
427	      et_violation_rate: 0.0
428	      rv_violation_rate: 0.0003
429	      et_violations: 0
430	      rv_violations: 5
431	      total_triples: 17341
432	    scierc_full_s1:
433	      et_violation_rate: 0.0
434	      rv_violation_rate: 0.0
435	    docred_full_s1:
436	      et_violation_rate: 0.0
437	      rv_violation_rate: 0.0003
438	    cross_dataset_summary:
439	      et_elimination: 100% on both datasets (0/1725 SciERC, 0/17341 DocRED)
440	      rv_elimination: 100% SciERC (0/1725), 99.97% DocRED (5/17341)
441	      ontology_size_invariance: 7 relations → 96 relations (14x) with no degradation
442	  result_rationale: "1. ET/RV 是 CFG-expressible constraints：entity_type ∈ {valid_types},\n\
443	    \   relation_type ∈ {valid_relations}。XGrammar pushdown automaton 可精确 enforce，\n\
444	    \   不依赖生成历史或语义状态，因此与模型和 ontology 大小无关。\n2. SciERC ET=0, RV=0 完美。DocRED ET=0 完美；RV=5/17341=0.03%\
445	    \ 有微小残留。\n   这 5 个 RV 可能源于 tokenizer 边界效应——DocRED 某些 relation name\n   （如 P1001_applies_to_jurisdiction）在\
446	    \ tokenization 时可能触发 XGrammar\n   的 token boundary edge case。5/17341 是 noise level，不影响结论。\n\
447	    3. 从 7 relations 到 96 relations（14x），ET/RV 消除率保持 99.97-100%。\n   Grammar compilation\
448	    \ 自动将 ontology schema 转化为 CFG，\n   schema size 只增加 production rule 数量，不降低 enforcement\
449	    \ 精确性。\n4. 数据已全部就位（来自 phase2_scierc_grammar_only 和 phase2_docred_grammar_only），\n\
450	    \   这是 compilation + formatting，不需新实验。\n"
451	  tables:
452	  - 'Table 2/3: ET 和 RV 列横跨所有配置和数据集'
453	  figures_description:
454	  - 无需独立 figure——Table 中 ET/RV 列的 0%/0.03% 已足够说明
455	  analysis: 'Grammar 完美泛化是 paper 的 "clean win"，无需 caveat。
456	
457	    建议 §5 第一段就报告此 finding（ET/RV→0% across datasets），
458	
459	    先给 reviewer 一个 unambiguously positive result，建立信任后再讨论 DR 的 nuance。
460	
461	    论文可 claim："Grammar-constrained decoding is a solved problem for ontology vocabulary
462	
463	    and entity type compliance in IE—it scales perfectly from 7 to 96 relation types."
464	
465	    '
466	- name: DocRED per-relation DR bimodal distribution analysis
467	  plan_id: P_analytical_bimodal
468	  description: '分析 96 个 DocRED relations 的 full_s1 per-relation DR 分布形态，
469	
470	    验证 >65% 关系 DR<2% 的双峰假设。
471	
472	    '
473	  expected_results:
474	    total_relations: 96
475	    active_relations: 87
476	    filter_5plus_triples: 82
477	    dr_distribution:
478	      dr_eq_0pct: 18
479	      dr_lt_2pct: 55
480	      dr_2_to_10pct: 12
481	      dr_10_to_20pct: 7
482	      dr_20_to_40pct: 6
483	      dr_gt_40pct: 8
484	    near_zero_fraction: 0.67
485	    near_zero_fraction_note: 55/82 = 67%（≥5 triples 的 relations 中 DR<2%）
486	    distribution_statistics:
487	      median_dr: 0.008
488	      mean_dr: 0.102
489	      mean_median_ratio: 12.75
490	      std_dr: 0.18
491	      skewness: 2.1
492	      gini_coefficient: 0.82
493	    top15_concentration: 0.763
494	    top15_concentration_note: 已实测：top 15 relations 贡献 1352/1771 = 76.3% 总违规
495	  result_rationale: "1. 67% relations DR<2%（best 档下界 65%）：DocRED 虽然 avg tightness=0.842（高），\n\
496	    \   但 tightness 分布也有 variance——0.70-0.84 区间的 41 个 relations 中，\n   许多的实际 DR 较低是因为\
497	    \ (a) 高频 entity types（PER, ORG, LOC）自然匹配这些 relation\n   的 domain/range，(b) 模型的\
498	    \ distributional prior 与 ontology 约束高度对齐。\n   仅在 tightness 极高（>0.90）时，prior-constraint\
499	    \ mismatch 才产生显著 DR。\n2. Mean>>Median（12.75x）：经典 heavy-tail 特征。\n   8 个 DR>40%\
500	    \ 的 extreme relations（P1198, P6, P171, P35 等，全部 tightness>0.88）\n   将 mean 拉至\
501	    \ 10.2%（= overall 10.19%），但 median 0.8% 代表 \"典型\" relation 体验。\n3. Gini=0.82：violation\
502	    \ 分布极不平等。类比帕累托法则：~12% 的 relations 贡献 ~80% violations。\n   这不是随机噪声，而是 ontology\
503	    \ constraint structure 的系统性产物。\n4. 双峰形成机制：constraint tightness 作为 bifurcation\
504	    \ parameter——\n   tightness < ~0.80 时 semantic mask 只排除少量 low-probability tokens，\n\
505	    \   model 自然分布已近乎合法，DR→0%（左峰）；\n   tightness > ~0.90 时 mask 必须排除 high-probability\
506	    \ tokens，\n   model 被迫使用低概率 token，DR 急剧上升（右尾）。\n   0.80-0.90 是 transition zone，DR\
507	    \ 分散，中间 bin 较薄。\n"
508	  tables:
509	  - 'Table 4: DocRED Per-relation DR Summary Statistics'
510	  figures_description:
511	  - 'Figure 2: Histogram — 96 relations 的 full_s1 DR 分布. 左峰 (0-2%, ~55 relations)
512	    显著高于右尾 (>20%, ~14 relations). Vertical dashed line at DR=2%. Inset: log-scale
513	    清晰展示右尾结构'
514	  analysis: 'near_zero_fraction=67% 在 best 档 [65%, 80%] 下端。
515	
516	    这个分布图的论文价值：visually 传达 "10.19% overall DR 不是均匀分布的失败"——
517	
518	    对 2/3 的 relations，constrained decoding 已实现 near-complete compliance；
519	
520	    残留 DR 集中在可预测的少数 high-tightness relations。
521	
522	    Fig 2 + Fig 3 (tightness scatter) 构成核心 evidence pair：
523	
524	    分布展示现象（双峰），scatter 解释机制（tightness 驱动）。'
525	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "134fab54-b9be-4ce1-aa4d-8584f8497d9e",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "cd710995-90d2-4f05-add3-5b66f08128fa",
  "sourceToolAssistantUUID": "134fab54-b9be-4ce1-aa4d-8584f8497d9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-14T10:51:22.575Z_

Now let me read the rest of the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd710995-90d2-4f05-add3-5b66f08128fa",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LJewiEmRvYrNts3EQ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3f51304-e925-4dd7-9d85-0fc24a308771",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsZxHJZkAMD3X287GbRxaz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26971,
      "cache_read_input_tokens": 40146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 26971,
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

_source line 37 · 2026-05-14T10:51:25.380Z_

<details open><summary>🔧 Tool call — Read · `toolu_018XcksdbwdYHpEtPKtSiXKG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper.tex",
  "offset": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3f51304-e925-4dd7-9d85-0fc24a308771",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LJewiEmRvYrNts3EQ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffdbd7f6-3c22-4890-9357-ed167b49de8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsZxHJZkAMD3X287GbRxaz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26971,
      "cache_read_input_tokens": 40146,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 26971
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 40146,
          "cache_creation_input_tokens": 26971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 26971,
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

_source line 38 · 2026-05-14T10:51:25.395Z_

<details><summary>↩ Tool result · `toolu_018XcksdbwdYHpEtPKtSiXKG`</summary>

```text
200	
201	The two layers compose via bitwise AND:
202	\begin{equation}
203	    M_t = M_t^{\text{gram}} \wedge M_t^{\text{sem}}
204	    \label{eq:compose}
205	\end{equation}
206	
207	This composition has an \emph{enabling dependency}: the grammar layer ensures every generated relation type $r \in \mathcal{R}$, which is a prerequisite for the semantic layer to look up $\mathcal{D}(r)$.
208	Without grammar enforcement, the semantic layer encounters unknown relation types for which no domain/range rules exist, rendering it unable to enforce constraints on those triples.
209	
210	\textbf{Graceful degradation.}
211	When $M_t^{\text{sem}} \cap M_t^{\text{gram}} = \emptyset$ (the semantic layer would mask all grammar-valid tokens), the system falls back to grammar-only constraints: $M_t = M_t^{\text{gram}}$.
212	This maintains structural validity as a guaranteed floor.
213	In practice, this fallback is rare: 1/998 documents on DocRED (0.1\%), 0/551 on SciERC.
214	
215	\subsection{Decoding Strategies}
216	
217	We evaluate two strategies:
218	
219	\noindent\textbf{S1 (Single-pass):} Both grammar and semantic layers are active throughout generation. Recommended as the primary strategy due to simplicity and marginally better metrics.
220	
221	\noindent\textbf{S2 (Two-pass):} Pass~1 extracts entities with grammar-only constraints; Pass~2 generates relations with an input-dependent grammar compiled from Pass~1 entities.
222	S2 is an architectural variant demonstrating framework flexibility; it does not improve over S1 on any metric (Section~\ref{sec:exp}).
223	
224	%% ============================================================
225	%% 5. EXPERIMENTS
226	%% ============================================================
227	\section{Experiments}
228	\label{sec:exp}
229	
230	\subsection{Setup}
231	
232	We evaluate \sys{} on SciERC (551 sentences) and DocRED (998 documents) using Qwen3-8B in a zero-shot setting.
233	We compare five configurations: \emph{unconstrained} (baseline), \emph{grammar-only} (grammar layer only), \emph{semantic-only} (semantic layer only), \emph{full S1} (both layers, single-pass), and \emph{full S2} (both layers, two-pass).
234	Cross-model generalization is evaluated with Llama-3.1-8B on SciERC.
235	F1 is reported as a control variable to verify that constraints do not degrade extraction quality, not as an optimization target.
236	
237	\subsection{Grammar Layer: Perfect Cross-Dataset Generalization}
238	
239	Table~\ref{tab:grammar} presents grammar-layer results across datasets.
240	Grammar-constrained decoding eliminates entity-type violations entirely (ET$\to$0\%) and relation-vocabulary violations to near-zero (RV$\to$0\% on SciERC, 0.03\% on DocRED) across both datasets, scaling from 7 to 96 relation types (14$\times$) with no degradation.
241	The 5 residual RV violations on DocRED (out of 17,341 triples) likely stem from tokenizer boundary effects on long relation names.
242	
243	\begin{table}[t]
244	\centering
245	\small
246	\caption{Grammar layer eliminates ET and RV violations across datasets. Grammar-only configuration; violations in constrained output.}
247	\label{tab:grammar}
248	\begin{tabular}{lccccc}
249	\toprule
250	\textbf{Dataset} & $|\mathcal{R}|$ & \textbf{Triples} & \textbf{ET (\%)} & \textbf{RV (\%)} \\
251	\midrule
252	SciERC  & 7  & 1,725  & 0.0 & 0.0 \\
253	DocRED  & 96 & 17,341 & 0.0 & 0.03 \\
254	\bottomrule
255	\end{tabular}
256	\end{table}
257	
258	\subsection{SciERC: Near-Complete Violation Elimination}
259	
260	Table~\ref{tab:scierc} presents the full ablation on SciERC.
261	Full S1 reduces DR from 15.4\% to 0.93\% ($\downarrow$94\%) while maintaining F1 (8.36\% vs.\ 8.23\% unconstrained; the +0.13pp difference is not statistically significant).
262	
263	The enabling dependency between layers is quantified by the \emph{enabling ratio}: the DR reduction achieved by full S1 divided by that of semantic-only.
264	On SciERC, full S1 achieves 14.4pp DR reduction vs.\ semantic-only's 3.7pp, yielding an enabling ratio of 3.88$\times$.
265	Semantic-only achieves only 24.2\% DR reduction because $\sim$1.4\% of triples use out-of-vocabulary relation types for which no domain/range rules can be looked up.
266	
267	Full S2 shows no improvement over S1: DR 0.97\% (vs.\ 0.93\%), CF 8.03\% (vs.\ 9.90\%), R-F1 8.03\% (vs.\ 8.36\%).
268	S2 is positioned as an architectural variant, not a recommended strategy.
269	
270	\begin{table}[t]
271	\centering
272	\small
273	\caption{SciERC constrained decoding ablation (Qwen3-8B, 551 sentences). DR = domain/range violation rate (\%), CF = cross-field consistency violation rate (\%), R-F1 = relation F1 (\%).}
274	\label{tab:scierc}
275	\begin{tabular}{lcccccc}
276	\toprule
277	\textbf{Config} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{R-F1} & \textbf{DR $\Delta$} \\
278	\midrule
279	Unconstrained   & $>$0 & 1.4 & 15.4 & $<$0.1 & 8.23 & --- \\
280	Grammar-only    & 0.0  & 0.0 & $\sim$15.4 & $<$0.1 & --- & $\sim$0\% \\
281	Semantic-only   & ---  & --- & 11.7 & 2.7  & --- & $\downarrow$24\% \\
282	Full S1         & 0.0  & 0.0 & 0.93 & 9.9  & 8.36 & $\downarrow$94\% \\
283	Full S2         & 0.0  & 0.0 & 0.97 & 8.0  & 8.03 & $\downarrow$94\% \\
284	\bottomrule
285	\end{tabular}
286	\end{table}
287	
288	\subsection{DocRED: Predictable Partial Reduction}
289	
290	Table~\ref{tab:docred} presents results on DocRED.
291	Full S1 reduces DR from 19.0\% to 10.19\% ($\downarrow$46.4\%).
292	While the absolute reduction is lower than SciERC's 94\%, this is predicted by DocRED's higher mean constraint tightness (0.842): tighter constraints force the semantic mask to exclude high-probability tokens, making violations harder to prevent without quality degradation.
293	
294	The enabling dependency is preserved: semantic-only achieves only 18.4\% DR reduction (enabling ratio 2.52$\times$).
295	This ratio is lower than SciERC's 3.88$\times$ because DocRED's unconstrained RV is much higher (28.9\% vs.\ 1.4\%), meaning the semantic layer is blind to nearly one-third of triples without grammar enforcement.
296	This confirms that the enabling dependency becomes \emph{more necessary} as ontology complexity increases.
297	
298	F1 is preserved: R-F1 8.17\% (full S1) vs.\ 8.20\% (unconstrained), confirming F1-neutral enforcement.
299	
300	\begin{table}[t]
301	\centering
302	\small
303	\caption{DocRED constrained decoding ablation (Qwen3-8B, 998 documents). ET/RV/DR/CF as violation rates (\%).}
304	\label{tab:docred}
305	\begin{tabular}{lcccccc}
306	\toprule
307	\textbf{Config} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{R-F1} & \textbf{DR $\Delta$} \\
308	\midrule
309	Unconstrained   & 7.5  & 28.9 & 19.0 & $<$0.1 & 8.20 & --- \\
310	Grammar-only    & 0.0  & 0.03 & ---  & $<$0.1 & 8.24 & --- \\
311	Semantic-only   & 7.3  & 28.7 & 15.5 & 2.5  & 8.00 & $\downarrow$18\% \\
312	Full S1         & 0.0  & 0.03 & 10.19 & 2.6  & 8.17 & $\downarrow$46\% \\
313	\bottomrule
314	\end{tabular}
315	\end{table}
316	
317	\subsection{Per-Relation DR Distribution on DocRED}
318	\label{sec:bimodal}
319	
320	The aggregate 10.19\% DR on DocRED masks a highly skewed per-relation distribution.
321	Table~\ref{tab:bimodal} summarizes the distribution across 82 relation types with $\geq$5 triples.
322	
323	\begin{table}[t]
324	\centering
325	\small
326	\caption{DocRED full S1 per-relation DR distribution (82 relations with $\geq$5 triples). Violations are concentrated in a small minority of high-DR relations.}
327	\label{tab:bimodal}
328	\begin{tabular}{lcc}
329	\toprule
330	\textbf{DR Range} & \textbf{\# Relations} & \textbf{Cumulative \%} \\
331	\midrule
332	DR = 0\%      & 18 & 22\% \\
333	0\% $<$ DR $<$ 2\%   & 37 & 67\% \\
334	2\%--10\%     & 12 & 82\% \\
335	10\%--20\%    & 7  & 90\% \\
336	20\%--40\%    & 6  & 98\% \\
337	$>$ 40\%      & 8  & 100\% \\
338	\midrule
339	\multicolumn{3}{l}{\textit{Summary statistics:}} \\
340	\multicolumn{2}{l}{Median DR} & 0.8\% \\
341	\multicolumn{2}{l}{Mean DR} & 10.2\% \\
342	\multicolumn{2}{l}{Gini coefficient} & 0.82 \\
343	\multicolumn{2}{l}{Top 15 relations' share of violations} & 76.3\% \\
344	\bottomrule
345	\end{tabular}
346	\end{table}
347	
348	67\% of relations achieve DR $<$ 2\% (near-complete compliance), while the top 15 high-violation relations contribute 76.3\% of all violations.
349	The mean/median ratio of 12.75$\times$ and Gini coefficient of 0.82 confirm extreme concentration.
350	This is not random noise but a systematic consequence of ontology constraint structure, as Section~\ref{sec:tightness} demonstrates.
351	
352	\subsection{Tightness--Violation Correlation}
353	\label{sec:tightness}
354	
355	We compute the Spearman rank correlation between constraint tightness (Eq.~\ref{eq:tightness}) and per-relation DR on DocRED.
356	Table~\ref{tab:tightness} shows a clear monotonic trend across tightness buckets.
357	
358	\begin{table}[t]
359	\centering
360	\small
361	\caption{DocRED per-relation DR by constraint tightness bucket (full S1). Higher tightness $\to$ higher residual DR. Spearman $\rho$=0.52, $p<$0.001.}
362	\label{tab:tightness}
363	\begin{tabular}{lccc}
364	\toprule
365	\textbf{Tightness Bucket} & \textbf{\# Rels} & \textbf{Agg.\ DR (\%)} \\
366	\midrule
367	$<$ 0.70          & 2  & 0.7 \\
368	0.70--0.79        & 18 & 9.0 \\
369	0.80--0.84        & 23 & 7.0 \\
370	0.85--0.89        & 28 & 12.9 \\
371	0.90--0.94        & 15 & 19.3 \\
372	0.95--1.00        & 4  & 30.6 \\
373	\bottomrule
374	\end{tabular}
375	\end{table}
376	
377	The Spearman $\rho$=0.52 ($n$=82, $p<$0.001) confirms a statistically significant positive correlation.
378	While the correlation is moderate in absolute terms, the bucket-level monotonic trend and extreme violation concentration (76.3\% in top 15 relations) provide strong practical utility: practitioners can estimate constraint effectiveness from the ontology definition alone, before any model inference.
379	
380	The mechanism is intuitive: high-tightness relations exclude most of the entity-type space, forcing the semantic mask to block high-probability tokens.
381	When the model's distributional prior strongly favors invalid type assignments (e.g., \texttt{P6\_head\_of\_government} with tightness 0.889 and DR 84.6\%), even per-token logit masking cannot fully redirect probability mass without degrading generation coherence.
382	
383	Illustrative extreme cases include \texttt{P6\_head\_of\_government} (tightness 0.889, DR 84.6\%, $n$=13) and \texttt{P582\_end\_time} (tightness 0.917, DR 43.5\%, $n$=186), both of which have very narrow valid type pairs.
384	In contrast, \texttt{P17\_country} and similar low-tightness relations achieve near-zero DR.
385	
386	\subsection{Cross-Model Generalization}
387	\label{sec:crossmodel}
388	
389	To verify that our findings are not model-specific, we replicate the SciERC experiments with Llama-3.1-8B.
390	Table~\ref{tab:crossmodel} compares violation rates across models.
391	
392	\begin{table}[t]
393	\centering
394	\small
395	\caption{Cross-model comparison on SciERC. Grammar enforcement (ET/RV$\to$0\%) and DR reduction generalize across models. $\rho$ = per-relation DR rank Spearman correlation between models.}
396	\label{tab:crossmodel}
397	\begin{tabular}{llcccc}
398	\toprule
399	\textbf{Model} & \textbf{Config} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{R-F1} \\
400	\midrule
401	\multirow{3}{*}{Qwen3-8B}
402	& Unconstrained & $>$0 & 1.4 & 15.4 & 8.23 \\
403	& Grammar       & 0.0  & 0.0 & ---  & --- \\
404	& Full S1       & 0.0  & 0.0 & 0.93 & 8.36 \\
405	\midrule
406	\multirow{3}{*}{Llama-3.1-8B}
407	& Unconstrained & 0.6  & 2.5 & 14.5 & 6.50 \\
408	& Grammar       & 0.0  & 0.0 & 14.0 & --- \\
409	& Full S1       & 0.0  & 0.0 & 1.2  & 6.80 \\
410	\bottomrule
411	\multicolumn{6}{l}{\textit{Cross-model per-relation DR Spearman} $\rho$=0.89} \\
412	\end{tabular}
413	\end{table}
414	
415	Grammar enforcement achieves ET/RV$\to$0\% on both models, confirming that grammar constraints are model-agnostic (they depend only on the tokenizer vocabulary mapping, automatically adapted by XGrammar).
416	
417	Full S1 reduces DR from 14.5\% to 1.2\% on Llama ($\downarrow$92\%), comparable to Qwen's $\downarrow$94\%.
418	The cross-model per-relation DR Spearman $\rho$=0.89 indicates that the \emph{per-relation violation susceptibility is a property of the ontology constraint structure, not the generating model}---both models violate the same relations at similar rates, driven by constraint tightness.
419	
420	\subsection{Cross-Field Consistency Analysis}
421	\label{sec:cf}
422	
423	Constrained decoding introduces a trade-off: while DR violations decrease, cross-field consistency (CF) violations increase.
424	CF violations occur when the same entity is assigned different types across different relations---each individual triple remains type-valid, but cross-triple consistency is broken.
425	
426	Table~\ref{tab:cf} presents the CF analysis.
427	
428	\begin{table}[t]
429	\centering
430	\small
431	\caption{Cross-field consistency (CF) analysis. CF increases with semantic enforcement but at a favorable trade-off ratio (DR reduction per CF increase). EVR = entity-vs-relation type drift (dominant CF sub-type).}
432	\label{tab:cf}
433	\begin{tabular}{lccccc}
434	\toprule
435	\textbf{Dataset} & \textbf{Config} & \textbf{CF (\%)} & \textbf{DR (\%)} & \textbf{DR:CF} \\
436	\midrule
437	\multirow{3}{*}{SciERC}
438	& Unconstrained & $<$0.1 & 15.4 & --- \\
439	& Grammar-only  & 0.08   & $\sim$15.4 & --- \\
440	& Full S1       & 9.9    & 0.93 & 1.5:1 \\
441	\midrule
442	\multirow{3}{*}{DocRED}
443	& Unconstrained & $<$0.1 & 19.0 & --- \\
444	& Grammar-only  & 0.07   & ---  & --- \\
445	& Full S1       & 2.6    & 10.19 & 3.6:1 \\
446	\bottomrule
447	\end{tabular}
448	\end{table}
449	
450	\textbf{CF is 100\% attributable to the semantic layer.}
451	Grammar-only CF rates ($\leq$0.08\%) are identical to unconstrained baselines, confirming that grammar enforcement introduces no CF.
452	All CF increase comes from the semantic layer's per-relation independent type enforcement: the semantic mask selects the locally optimal type for each relation's domain/range constraints, without maintaining global entity-type consensus.
453	
454	\textbf{Root cause: type system ambiguity.}
455	On SciERC, 90\% of CF violations are entity-vs-relation type drift (EVR), where the same entity receives different types in the entity list vs.\ relation triples.
456	The dominant conflict patterns---Generic$\leftrightarrow$OtherScientificTerm (60 cases), Material$\leftrightarrow$OtherScientificTerm (28), Material$\leftrightarrow$Method (20)---reflect genuine semantic boundary ambiguity in SciERC's type system.
457	
458	The cross-dataset comparison provides strong evidence for this hypothesis: DocRED CF (2.6\%) is 3.8$\times$ lower than SciERC CF (9.9\%).
459	DocRED's entity types (PER/ORG/LOC/TIME/NUM/MISC) have far clearer semantic boundaries than SciERC's (Generic/OtherScientificTerm/Material/Method), confirming that \emph{CF rate is driven by type system ambiguity}.
460	On DocRED, the dominant CF pattern is ORG$\leftrightarrow$LOC (23.1\% of CF), corresponding to the well-known NER ambiguity of geopolitical entities.
461	
462	\textbf{Severity distinction.}
463	DR violations produce structurally invalid triples unusable by downstream systems (hard constraint).
464	CF violations produce individually valid triples with cross-triple inconsistency (soft preference).
465	The trade-off is favorable: on DocRED, each 1pp CF increase buys 3.57pp DR reduction.
466	
467	\subsection{Inference Latency}
468	
469	Table~\ref{tab:latency} reports inference overhead.
470	Full S1 incurs 1.37--1.39$\times$ overhead across datasets---the grammar layer adds $\sim$13\% (XGrammar's optimized C++ pushdown automaton) and the semantic layer adds $\sim$20\% (Python-based per-token logit masking).
471	The overhead is per-token and independent of document length.
472	Full S2 incurs 2.17$\times$ overhead due to two forward passes, with no quality benefit.
473	
474	\begin{table}[t]
475	\centering
476	\small
477	\caption{Inference latency overhead (tokens/second relative to unconstrained).}
478	\label{tab:latency}
479	\begin{tabular}{lcccc}
480	\toprule
481	\textbf{Dataset} & \textbf{Grammar} & \textbf{Semantic} & \textbf{Full S1} & \textbf{Full S2} \\
482	\midrule
483	SciERC & 1.13$\times$ & 1.33$\times$ & 1.37$\times$ & 2.17$\times$ \\
484	DocRED & 1.14$\times$ & --- & 1.39$\times$ & --- \\
485	\bottomrule
486	\end{tabular}
487	\end{table}
488	
489	%% ============================================================
490	%% 6. RELATED WORK
491	%% ============================================================
492	\section{Related Work}
493	
494	\textbf{Constrained decoding for structured generation.}
495	Grammar-constrained decoding has been applied to JSON generation, code synthesis, and SQL queries.
496	XGrammar and related systems compile formal grammars into efficient token masks.
497	Recent work on code generation applies type-checking during decoding in programming language contexts.
498	\sys{} extends this paradigm to IE ontology constraints, introducing semantic-layer enforcement for cross-field constraints beyond CFG expressiveness.
499	
500	\textbf{LLM-based information extraction.}
501	Zero-shot and few-shot LLM-based IE has shown strong results on standard benchmarks.
502	However, prior work focuses primarily on F1 metrics and largely ignores ontology compliance.
503	To our knowledge, no prior work systematically measures or addresses ontology constraint violations in LLM-generated extractions.
504	
505	\textbf{Ontology-aware IE.}
506	Traditional IE systems incorporate ontology constraints through training-time loss functions, post-hoc filtering, or ILP-based inference.
507	Post-hoc filtering cannot redirect probability mass toward valid outputs and wastes compute on invalid generations.
508	Training-time approaches require task-specific supervision.
509	\sys{} operates at decoding time with zero training, automatically compiled from ontology definitions.
510	
511	\textbf{Constraint satisfaction in NLP.}
512	Lexically constrained decoding enforces keyword inclusion during generation.
513	Neurologic and A*-based methods handle more complex constraints.
514	These approaches target surface-level lexical constraints rather than semantic type constraints.
515	\sys{}'s semantic layer addresses a different constraint class---cross-field type compatibility---requiring stateful tracking during generation.
516	
517	%% ============================================================
518	%% 7. CONCLUSION
519	%% ============================================================
520	\section{Conclusion}
521	
522	We presented \sys{}, a framework for enforcing ontology type constraints during LLM-based information extraction via compiled constrained decoding.
523	Our violation landscape study reveals that LLM-based IE systems produce systematic, non-uniformly distributed ontology violations driven by constraint tightness.
524	\sys{}'s two-layer architecture---grammar for structural/vocabulary compliance, semantic for cross-field domain/range enforcement---composes via bitwise AND with an enabling dependency, achieving near-complete violation elimination on tightly-constrained ontologies (94\% DR reduction on SciERC) and predictable partial reduction on complex ontologies (46\% on DocRED), all at zero F1 cost and $<$1.4$\times$ latency overhead.
525	Grammar-layer enforcement generalizes perfectly across datasets and models.
526	
527	The tightness--violation correlation (Spearman $\rho$=0.52) provides practitioners with an a priori diagnostic for estimating constraint effectiveness from ontology definitions alone, without model inference.
528	
529	\textbf{Limitations.}
530	Cross-field consistency violations are an inherent trade-off of per-relation independent type enforcement (9.9\% on SciERC, 2.6\% on DocRED), with CF rate driven by type system ambiguity.
531	Future work should explore global entity-type consensus mechanisms---e.g., a pre-decoding entity-type resolution pass---to maintain cross-relation consistency.
532	Our evaluation covers two datasets and two models; broader validation across ontologies, languages, and model scales is needed.
533	The current implementation uses a Python-based semantic layer; a C++ implementation would reduce the 20\% semantic overhead.
534	
535	\bibliographystyle{plainnat}
536	
537	\end{document}
538	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffdbd7f6-3c22-4890-9357-ed167b49de8c",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "de8915e3-62c2-41bf-831c-8205dee487da",
  "sourceToolAssistantUUID": "ffdbd7f6-3c22-4890-9357-ed167b49de8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-14T10:51:28.274Z_

Now let me also check if there is a previous review report to understand what has already been said.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de8915e3-62c2-41bf-831c-8205dee487da",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LK6UcVGpgUQzjLeUCV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8b78a75-9288-4391-8909-a46cbbe36ad1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019cu94KvZJBgv52LRSMma2e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7256,
      "cache_read_input_tokens": 67117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7256,
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

_source line 40 · 2026-05-14T10:51:30.569Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FcRTzho6kZKmYNU8CHtVE2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8b78a75-9288-4391-8909-a46cbbe36ad1",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LK6UcVGpgUQzjLeUCV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "386c6bb7-755c-4dfd-b455-d56961b5c342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019cu94KvZJBgv52LRSMma2e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7256,
      "cache_read_input_tokens": 67117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7256,
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

_source line 41 · 2026-05-14T10:51:30.582Z_

<details><summary>↩ Tool result · `toolu_01FcRTzho6kZKmYNU8CHtVE2`</summary>

```text
1	---
2	dream_id: dream_20260514T094226
3	tier: best
4	overall_score: 4 - Weak Accept
5	timestamp: 2026-05-14T10:49:45.272992+00:00
6	---
7	
8	# Dream Review Report: OntoCoDec
9	
10	**Paper**: OntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints
11	**Review mode**: Full (2 Reviewers + Roundtable)
12	**Date**: 2026-05-14
13	
14	---
15	
16	## Reviewer 1 (R1) — Methods & Experiments
17	
18	### Summary
19	The paper identifies systematic ontology constraint violations in LLM-based IE (15–19% DR), proposes OntoCoDec — a two-layer constrained decoding framework (grammar + semantic) composed via bitwise AND — and evaluates on SciERC and DocRED. SciERC achieves 94% DR reduction at zero F1 cost; DocRED achieves 46% reduction with residual violations concentrated in high-tightness relations (Spearman ρ=0.52). Cross-model validation with Llama-3.1-8B on SciERC confirms generalization.
20	
21	### Strengths
22	- **Well-motivated problem with clean empirical grounding.** The violation landscape study (§3) precedes the method, providing independent empirical value. The Evaluate-for regression under schema-informed prompting (24.1%→29.9%, §3.2) is a compelling demonstration that prompt-level intervention can be actively counterproductive.
23	- **Principled layer decomposition.** The decidability taxonomy (§2.3: Type a/b/c) gives a formally clean justification for why two layers are needed. The enabling dependency is well-argued and quantified: semantic-only achieves only 24% DR reduction on SciERC (Table 3) because ~1.4% of triples use OOV relation types; this blindness balloons to 29% on DocRED. The enabling ratio metric (3.88× SciERC, 2.52× DocRED) is a useful quantification.
24	- **Grammar layer is a "solved problem" result.** ET/RV→0% across both datasets and both models, scaling from 7 to 96 relation types with no degradation (Table 2, Table 7). Clean, unambiguous, practically useful.
25	- **Honest framing of DocRED results.** The paper does not oversell 46% reduction. The tightness-violation correlation transforms a weaker result into an analytical contribution by explaining *why* reduction is partial and making it predictable. 67% of relations reaching <2% DR (Table 5) shows the method works well for most relations.
26	- **Proactive CF disclosure with root cause analysis.** §5.8 attributes CF 100% to the semantic layer, identifies EVR as dominant sub-type (>90%), traces root conflict patterns. Cross-dataset CF comparison (9.9% vs. 2.6%) supporting the type-system ambiguity hypothesis is a legitimate insight.
27	- **Graceful degradation documented.** Fallback when M_sem ∩ M_gram = ∅ (1/998 DocRED, 0/551 SciERC) is the correct engineering response.
28	
29	### Weaknesses
30	- **"Near-Complete" in the title is misleading for DocRED.** SciERC achieves 94% DR reduction, but DocRED achieves only 46% with 10.19% residual DR. The abstract differentiates ("predictable partial reduction"), but the title implies near-complete performance across settings. This will attract reviewer skepticism.
31	- **No statistical significance testing or confidence intervals.** All results are single-seed, single-run. The F1-neutrality claim (8.36 vs. 8.23 on SciERC, Table 3) is asserted without bootstrap CIs. With ~1700 triples, the +0.13pp difference needs statistical backing, not assertion.
32	- **Spearman ρ=0.52 is moderate, not strong.** The paper acknowledges this (§5.6) but the claim that practitioners can use this for "a priori estimates of constraint effectiveness" (abstract) overstates practical utility of a correlation explaining ~27% of rank variance. Moreover, the 0.70–0.79 bucket (DR=9.0%) is higher than the 0.80–0.84 bucket (DR=7.0%) in Table 6, breaking strict monotonicity — this inversion is not discussed.
33	- **CF trade-off under-discussed as a practical limitation.** On SciERC, CF increases from <0.1% to 9.9% — a ~100× increase. While the DR vs. CF severity distinction is valid in principle, the paper does not empirically demonstrate that downstream tasks are unaffected by 9.9% entity-type inconsistency.
34	- **Limited model diversity.** Two 8B models from different families is the bare minimum. No larger models (70B), no closed-source API models, no instruction-tuned vs. base model comparison. The "model-agnostic" claim rests on N=2 models at a single scale.
35	- **Unexplained table inconsistencies.** Table 1 reports DocRED unconstrained DR=18.7% but Table 4 uses 19.0%. Several cells show "—" in Tables 3–4 (grammar-only R-F1, grammar-only DR on DocRED, semantic-only R-F1). If these experiments were run, numbers should be reported; if not, these are missing ablation datapoints.
36	- **Data provenance concern.** The DocRED unconstrained and semantic-only numbers in Table 4 closely match projections in the experiment design document. If any of these are projected rather than measured, this is a critical integrity issue. Authors should confirm all reported numbers come from completed experiments.
37	
38	### Missing Experiments
39	- **DocRED Phase 2 unconstrained baseline**: Paper uses numbers that may mix Phase 0 (18.7%) and Phase 2 (19.0%) code paths. A clean Phase 2 unconstrained run through the identical pipeline as full S1 is needed for rigorous ablation.
40	- **Llama-3.1-8B on DocRED**: Cross-model validation limited to SciERC, where the method already works well. DocRED cross-model validation would be more informative about robustness where the method is weaker.
41	- **Bootstrap CIs for F1 and DR**: Single-point estimates without uncertainty quantification across all tables.
42	
43	### Questions for Authors
44	1. Were the DocRED unconstrained (DR=19.0%) and semantic-only (DR=15.5%) numbers in Table 4 obtained from completed Phase 2 experiments using the identical code path as full S1? Please provide experiment IDs and timestamps.
45	2. What drives the tightness bucket inversion (0.70–0.79 at 9.0% vs. 0.80–0.84 at 7.0% in Table 6)? Is it dominated by a single high-frequency relation?
46	3. The 1/998 graceful degradation trigger on DocRED — what was the resulting DR for that document?
47	4. Why no Llama-3.1-8B evaluation on DocRED?
48	5. The residual 0.93% DR on SciERC — which relations contribute? Could relation-specific strategies further reduce this?
49	
50	### Score: 4 (Weak Accept) | Confidence: 4/5
51	
52	---
53	
54	## Reviewer 2 (R2) — Novelty & Related Work
55	
56	### Summary
57	The paper applies constrained decoding to enforce ontology type constraints in LLM-based IE, combining XGrammar (grammar layer) with a custom LogitsProcessor (semantic layer). The violation landscape study (§3) documents a real problem. The tightness-violation correlation (§5.6) is an analytical contribution. However, the technical novelty is limited — the grammar layer is off-the-shelf XGrammar, the semantic layer is a straightforward logit mask with a dictionary lookup, and the composition is trivial bitwise AND.
58	
59	### Strengths
60	- **Violation landscape study has independent empirical value.** §3 provides the first systematic measurement of ontology constraint violations in LLM-based IE across two datasets. The finding that violation rates are driven by constraint tightness rather than ontology size (15.4% vs. 18.7% despite 14× size difference) is a genuine insight.
61	- **Prompt insufficiency finding is compelling.** The Evaluate-for regression (24.1%→29.9%) under schema-informed prompting demonstrates a failure mode that motivates decoding-time intervention.
62	- **Clean ablation design.** The 5-configuration ablation (unconstrained / grammar-only / semantic-only / full S1 / full S2) with the enabling ratio metric cleanly decomposes contributions.
63	- **Honest claim calibration.** The paper distinguishes SciERC "near-complete" from DocRED "predictable partial reduction" in the abstract, which shows intellectual honesty even if the title oversells.
64	- **Tightness-violation correlation as analytical contribution.** The Spearman ρ=0.52 with bucket-level monotonic trend provides practitioners a diagnostic tool, independent of the method itself.
65	
66	### Weaknesses
67	- **Core technical contribution is engineering integration, not research advance.** The grammar layer is XGrammar applied to an IE-specific EBNF schema — this is an application of existing technology, not a methodological advance. The semantic layer is a LogitsProcessor that maintains a dictionary {entity_name → type} and masks logits based on a lookup table — this is algorithmically straightforward. The bitwise AND composition is the obvious and only reasonable choice. The "enabling dependency" is an empirical observation about why grammar helps semantic, not a technical design innovation.
68	- **DocRED results undermine the headline claim.** 46% DR reduction with 10.19% residual is "partial," not "near-complete." The paper's narrative framing cannot change the fact that the method leaves >10% of triples with type violations on the more realistic dataset. For practitioners working with large, heterogeneous ontologies (which is the common case), this result is underwhelming.
69	- **CF trade-off partially offsets gains.** On SciERC, going from <0.1% CF to 9.9% CF while reducing DR from 15.4% to 0.93% means the total constraint violation burden shifts rather than disappears. The DR:CF ratio (1.5:1 on SciERC, Table 8) is not overwhelmingly favorable. The paper's argument that DR is "hard" and CF is "soft" is valid but unsubstantiated by downstream task evaluation.
70	- **Absolute F1 of ~8% raises transfer concerns.** Both models achieve only ~8% relation F1, suggesting that zero-shot IE quality is too low for practical use regardless of type compliance. The paper frames F1 as a "control variable," but if the base extraction is this poor, enforcing type validity on mostly-wrong extractions is of limited practical value. The paper does not discuss this elephant in the room.
71	- **Narrow experimental scope.** Two datasets, two models (both 8B), zero-shot only. No evaluation on few-shot, instruction-tuned models, or fine-tuned extractors where the violation landscape may be entirely different. The generality claims outpace the evidence.
72	
73	### Novelty Assessment
74	The paper's novelty rests on three pillars: (1) the violation landscape study, (2) the OntoCoDec framework, and (3) the tightness-violation correlation. Pillar (1) is a legitimate empirical contribution — no prior work has systematically measured ontology violations in LLM-based IE. Pillar (3) is a useful analytical finding, though ρ=0.52 is moderate. Pillar (2) — the framework itself — is the weakest in novelty. The grammar layer is a direct application of XGrammar with an IE-specific schema; prior work like PICARD (Scholak et al., 2021) already demonstrated incremental parsing constraints during decoding for SQL, which is methodologically analogous. The semantic layer is a standard LogitsProcessor pattern available in HuggingFace Transformers. The composition is trivial. What is novel is the *application domain* (IE ontology constraints) and the *empirical characterization* (enabling dependency, tightness correlation), not the *technique* itself. For a top ML venue, this puts the contribution at the boundary — strong enough for an applications track or workshop, borderline for a main conference.
75	
76	### Related Work Gaps
77	- **PICARD (Scholak et al., 2021)**: Most significant omission. Incremental parsing for SQL constrained decoding is methodologically very close — it also maintains state during decoding to enforce cross-field constraints (column types must match SQL operation requirements). The paper should explicitly compare its approach to PICARD's.
78	- **GenIE (Josifoski et al., 2022)**: Generative IE with constrained decoding using a trie-based prefix tree for entity disambiguation. Directly relevant — constrains IE output during decoding.
79	- **REBEL (Cabot & Navigli, 2021)** and **TANL (Paolini et al., 2021)**: End-to-end RE models that implicitly learn type constraints through training. The paper should discuss why decoding-time enforcement is preferable to training-time learning.
80	- **SynCode (Ugare et al., 2024)**: Grammar-augmented generation with semantic actions — directly comparable to the grammar+semantic layering.
81	- **GoLLIE (Sainz et al., 2024)**: Guideline-following IE that embeds schema information in prompts with structured output — a prompt-based competitor.
82	- **Post-hoc type checking in KG completion**: Work by Bordes et al., TransE/TransR type constraints, etc. The paper's "no prior work" claim on violation measurement may be too strong — type constraint enforcement has been studied extensively in KG embedding literature.
83	
84	### Questions for Authors
85	1. How does the semantic layer differ technically from a standard HuggingFace LogitsProcessor with a dictionary? What is the algorithmic novelty beyond the application domain?
86	2. How does OntoCoDec compare to PICARD's approach of incremental parsing with semantic state? Both maintain cross-field state during autoregressive decoding.
87	3. If a fine-tuned IE model (e.g., REBEL, GoLLIE) already achieves low violation rates through training, does OntoCoDec provide additional value? Has this been tested?
88	4. The ~8% relation F1 means most extracted triples are incorrect regardless of type validity. How does enforcing type constraints on predominantly wrong triples benefit practitioners?
89	5. Would the violation landscape look fundamentally different with few-shot prompting or instruction-tuned models? If violations drop substantially with better prompting, the motivation for decoding-time enforcement weakens.
90	
91	### Score: 3 (Weak Reject) | Confidence: 4/5
92	
93	---
94	
95	## Roundtable Discussion
96	
97	### Step 2: Cross-Sharing — Points of Agreement
98	
99	Both reviewers agree on:
100	1. **The violation landscape study (§3) is a genuine empirical contribution.** The finding that violation rates are driven by constraint tightness rather than ontology size, and that schema-informed prompting can increase violations (Evaluate-for), has independent value.
101	2. **Grammar layer generalization is a clean, unambiguous win.** ET/RV→0% across datasets and models is a strong result requiring no caveats.
102	3. **"Near-Complete" in the title oversells the DocRED result.** 46% DR reduction with 10.19% residual is "partial," not "near-complete." Both reviewers flag this as a framing concern.
103	4. **CF trade-off is insufficiently validated.** The severity distinction (DR=hard, CF=soft) is argued but not empirically demonstrated via downstream task impact.
104	5. **Narrow experimental scope.** Two datasets, two models at the same scale, zero-shot only. Both reviewers want broader validation.
105	6. **Missing confidence intervals.** All single-seed, single-run results lack statistical rigor for a top venue.
106	
107	### Step 2: Cross-Sharing — Points of Disagreement
108	
109	- **Novelty threshold.** R1 finds the technical contribution sufficient (principled decomposition, enabling dependency quantification, tightness predictor). R2 considers the framework an engineering integration of known techniques (XGrammar + LogitsProcessor + bitwise AND), with novelty residing only in the application domain and empirical characterization.
110	- **Significance of ~8% F1.** R2 flags this as a fundamental concern — enforcing type validity on mostly-wrong extractions has limited practical value. R1 accepts the paper's framing that F1 is a control variable, not an optimization target, and that the constraint methodology is orthogonal to extraction quality.
111	- **Overall assessment.** R1: 4 (Weak Accept). R2: 3 (Weak Reject).
112	
113	### Step 3: Convergence
114	
115	After cross-sharing, we converge on the following assessment:
116	
117	**The violation landscape study and tightness-violation correlation are the paper's strongest contributions** — these would survive even if the framework were removed. The framework itself is competent engineering with a clean decomposition, but the individual components (XGrammar, LogitsProcessor, bitwise AND) are not technically novel. The "enabling dependency" is an empirical observation, not a design innovation.
118	
119	**The ~8% F1 concern is partially mitigated** by the paper's framing: the method is proposed as a constraint enforcement layer, orthogonal to extraction quality. However, the paper should acknowledge that in the ~8% F1 regime, most extracted triples are factually wrong regardless of type validity, and the practical benefit of type-valid-but-factually-wrong triples is limited. A stronger paper would evaluate on a higher-F1 baseline (few-shot or fine-tuned) where type compliance matters more.
120	
121	**The DocRED framing issue is real but manageable.** The paper's internal treatment is honest ("predictable partial reduction"), but the title needs qualification. The per-relation distribution analysis (67% < 2% DR) is a fair counterargument — the method works for most relations, and the failures are predictable.
122	
123	**Data provenance is a concern for R1 but cannot be definitively adjudicated in review.** If all numbers are from completed experiments, the paper stands; if any are projected, this is a serious issue. We flag this as a question for authors.
124	
125	**Converged score: 4 (Weak Accept), leaning borderline.** The empirical contributions (violation landscape, tightness analysis, grammar generalization) have genuine value. The framework, while not technically novel, is well-designed and practically useful. The paper would benefit from: (1) title/framing adjustment, (2) confidence intervals, (3) broader model/dataset evaluation, (4) downstream task validation for CF impact, (5) explicit comparison to PICARD and GenIE, (6) discussion of the low-F1 regime limitation.
126	
127	---
128	
129	## Step 4: Consolidated Assessment
130	
131	### Overall Score: 4 (Weak Accept)
132	
133	### Headline
134	A well-executed empirical study of ontology constraint violations in LLM-based IE, with a competent (though not technically novel) two-layer constrained decoding framework. Strong SciERC results (94% DR reduction), weaker but honestly-framed DocRED results (46%). The tightness-violation correlation is an independent analytical contribution. Below the novelty bar for a top ML venue main track, but appropriate for an applications/systems track.
135	
136	### Strengths (Consolidated)
137	1. **Violation landscape study** (§3) is the first systematic measurement of ontology constraint violations in LLM-based IE — genuine empirical contribution with independent value.
138	2. **Grammar layer generalization** is perfect: ET/RV→0% across 2 datasets (7→96 relations), 2 models, with no degradation. A clean "solved problem" result.
139	3. **Tightness-violation correlation** (ρ=0.52, bucket-level monotonic trend, top-15 concentration=76.3%) provides practitioners a useful diagnostic for estimating constraint effectiveness from ontology definitions alone.
140	4. **Honest framing**: The paper differentiates SciERC "near-complete" from DocRED "predictable partial reduction" and proactively discloses the CF trade-off with root cause analysis.
141	5. **Clean ablation design**: 5 configurations with enabling ratio quantification cleanly decomposes the contribution of each layer.
142	6. **F1-neutral enforcement**: Constraints do not degrade extraction quality (8.36 vs. 8.23 SciERC, 8.17 vs. 8.20 DocRED).
143	7. **Schema-informed prompting insufficiency**: The Evaluate-for regression (24.1%→29.9%) is a compelling motivation for decoding-time intervention.
144	
145	### Weaknesses (Consolidated)
146	1. **Limited technical novelty**: Grammar layer = XGrammar application; semantic layer = standard LogitsProcessor with dictionary; composition = bitwise AND. The enabling dependency is an empirical observation, not a design innovation. Engineering integration of known techniques.
147	2. **Title oversells**: "Near-Complete" holds for SciERC (94%) but not DocRED (46%, 10.19% residual). Title should be qualified or changed.
148	3. **CF trade-off unvalidated**: SciERC CF increases from <0.1% to 9.9% (~100×). The DR-is-hard/CF-is-soft argument is not backed by downstream task evaluation. On SciERC, DR:CF ratio is only 1.5:1 (Table 8).
149	4. **No statistical rigor**: All single-seed, single-run, no bootstrap CIs. F1-neutrality claim needs statistical testing.
150	5. **~8% relation F1 regime**: Both models achieve only ~8% relation F1 in zero-shot IE. Enforcing type validity on predominantly wrong extractions has limited practical value. The paper does not discuss this.
151	6. **Narrow scope**: 2 datasets, 2 models (both 8B), zero-shot only. No few-shot, no fine-tuned baselines, no larger models, no instruction-tuned models.
152	7. **Tightness bucket inversion**: 0.70–0.79 bucket (DR=9.0%) > 0.80–0.84 bucket (DR=7.0%) in Table 6, breaking strict monotonicity. Not discussed.
153	8. **Related work gaps**: PICARD (incremental parsing for SQL), GenIE (constrained decoding for IE), REBEL, TANL, SynCode, GoLLIE are not discussed. PICARD is methodologically very close.
154	9. **Table inconsistencies**: DocRED unconstrained DR is 18.7% in Table 1 but 19.0% in Table 4. Several "—" cells in Tables 3–4 where data likely exists.
155	10. **Data provenance uncertainty**: Some DocRED ablation numbers may match experiment design projections rather than completed experiments.
156	
157	### Recommendations for Improvement
158	1. Retitle to remove or qualify "Near-Complete" — e.g., "OntoCoDec: Enforcing Ontology Type Constraints in LLM-based IE via Compiled Constrained Decoding"
159	2. Add bootstrap confidence intervals for all F1 and DR numbers
160	3. Evaluate on at least one fine-tuned or few-shot baseline to show value in a higher-F1 regime
161	4. Add Llama-3.1-8B evaluation on DocRED for cross-model validation where the method is weaker
162	5. Explicitly compare to PICARD and GenIE in related work
163	6. Discuss the low-F1 regime limitation and when type enforcement matters practically
164	7. Explain the tightness bucket inversion in Table 6
165	8. Fill in missing table cells or explain their absence
166	9. Reconcile the 18.7% vs. 19.0% DocRED unconstrained DR discrepancy
167	10. Validate CF impact on a downstream task (even a simple KG consistency check)
168	
169	### Confidence: 4/5
170	Both reviewers have high confidence in their assessments. The convergence point reflects genuine disagreement on the novelty threshold, resolved in favor of weak accept due to the empirical contributions' value.
171	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "386c6bb7-755c-4dfd-b455-d56961b5c342",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "693e64c2-2e8c-43e9-be8f-4bccbfdbf9d4",
  "sourceToolAssistantUUID": "386c6bb7-755c-4dfd-b455-d56961b5c342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T10:51:31.296Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XypJWZy4sdBKGg8qTitgwi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/experiment_data.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "693e64c2-2e8c-43e9-be8f-4bccbfdbf9d4",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LK6UcVGpgUQzjLeUCV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "267cea7a-9652-41b6-9c97-1ac2c7114f02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019cu94KvZJBgv52LRSMma2e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7256,
      "cache_read_input_tokens": 67117,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7256
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 67117,
          "cache_creation_input_tokens": 7256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7256,
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

_source line 43 · 2026-05-14T10:51:31.302Z_

<details><summary>↩ Tool result · `toolu_01XypJWZy4sdBKGg8qTitgwi`</summary>

```text
1	[
2	  {
3	    "name": "DocRED Phase 2 unconstrained baseline",
4	    "description": "DocRED 998 文档，Phase2 code path 无约束运行。\n验证 Phase2 环境下的 unconstrained DR 与 Phase0 一致（18-20%），\n为计算 DR reduction 提供可比基线。\n",
5	    "results": {
6	      "documents": 998,
7	      "documents_checked": 962,
8	      "parse_failures": 36,
9	      "json_parse_rate": 0.964,
10	      "total_triples": 16600,
11	      "total_entities": 19200,
12	      "entity_type_violation_rate": 0.075,
13	      "relation_vocabulary_violation_rate": 0.289,
14	      "domain_range_violation_rate": 0.19,
15	      "domain_range_violations": 3154,
16	      "cross_field_consistency_violation_rate": 0.001,
17	      "entity_f1": 59.0,
18	      "relation_f1": 8.2,
19	      "relation_precision": 7.0,
20	      "relation_recall": 9.9,
21	      "dr_reduction_full_s1_vs_unconstrained_pct": 46.4
22	    },
23	    "tables": [
24	      "Table 3: DocRED Constrained Decoding Ablation — unconstrained column",
25	      "Table 1: Cross-dataset Violation Landscape — DocRED Phase2 unconstrained row"
26	    ],
27	    "figures": [],
28	    "analysis": "关键验证点：Phase2 unconstrained DR ≈ Phase0 DR（±1pp），\n确保 reduction 计算分母可比。若偏差 >2pp 需审查 code path 差异。\n46.4% reduction 支持 \"predictable partial reduction for complex ontologies\" 叙事。\n\n\nPhase2 SciERC unconstrained 与 Phase0 完全一致（DR=15.37%），\n证明 Phase2 code path 不引入偏差。DocRED 应同样复现 Phase0 数字。\nDR 预测 19.0%（vs Phase0 18.7%）：Phase2 unconstrained 使用相同 generation 参数，\n但 code path 中的 JSON 后处理可能与 Phase0 略有差异（如 unicode 处理），\n导致少量 triples 解析方式不同，~0.3pp 方差在正常范围。\nParse rate 保持 ~96.4%——无 grammar 约束时 JSON 格式错误率是模型固有属性。\nRV=28.9% 和 ET=7.5% 复现 Phase0，均为模型在无约束下的自然错误率。\nF1 与 grammar_only(8.24) 和 full_s1(8.17) 持平，确认约束 F1-neutral。\ndr_reduction 46.4% = (19.0-10.19)/19.0，落入 best 档 [46,55] 下界。\n"
29	  },
30	  {
31	    "name": "DocRED Phase 2 semantic-only constrained decoding",
32	    "description": "仅启用 semantic 层（TypeConstraintProcessor），不启用 grammar 层。\n验证 enabling dependency 在复杂 ontology 上跨数据集复现：\n无 grammar 保障 relation vocabulary → semantic 层大面积盲区 → DR reduction 显著弱于 full_s1。\n",
33	    "results": {
34	      "documents": 998,
35	      "documents_checked": 958,
36	      "parse_failures": 40,
37	      "json_parse_rate": 0.96,
38	      "total_triples": 16500,
39	      "total_entities": 19100,
40	      "entity_type_violation_rate": 0.073,
41	      "relation_vocabulary_violation_rate": 0.287,
42	      "domain_range_violation_rate": 0.155,
43	      "domain_range_violations": 2558,
44	      "cross_field_consistency_violation_rate": 0.025,
45	      "entity_f1": 58.5,
46	      "relation_f1": 8.0,
47	      "relation_precision": 6.9,
48	      "relation_recall": 9.5,
49	      "dr_reduction_vs_unconstrained_pct": 18.4,
50	      "semantic_enabling_ratio": 2.52
51	    },
52	    "tables": [
53	      "Table 3: DocRED Constrained Decoding Ablation — semantic_only column"
54	    ],
55	    "figures": [],
56	    "analysis": "enabling_ratio=2.52 在 best 档 [2.0, 3.5] 内。\n与 SciERC(3.88) 对比，DocRED ratio 更低的原因可量化归因于 RV 差异：\nDocRED 29% triples 使用无效 relation（SciERC 仅 1.4%），semantic 盲区面积成比例增大。\n论文核心论述：grammar-enables-semantic 在 ontology 复杂度增加时**更加必要**——\nDocRED 29% RV 使 semantic 层近三分之一 triples 完全无法检查。\n\n\nEnabling dependency 机制：\n1. DocRED unconstrained RV=29%，即 ~29% triples 使用不在 ontology 中的 relation type。\n   Semantic 层对这些 triples 完全无法检查——未知 relation 查不到 domain/range 规则。\n2. 在剩余 ~71% 合法 relation type 的 triples 中，semantic 执行 domain/range 检查。\n   但无 grammar 结构保障，JSON 解析失败率 ~4%（vs grammar_only 1.5%），\n   进一步削弱 semantic 的有效覆盖面。实际 semantic 能检查的 triples 约 67-68%。\n3. DR 从 19.0% 降至 15.5%（-18.4%），远弱于 full_s1 的 46.4%。\n   SciERC 上 semantic_only reduction=24.2%，DocRED 更低（18.4%）正因 RV 更高\n   （29% vs 1.4%），semantic 盲区更大。\n4. enabling_ratio = (19.0-10.19)/(19.0-15.5) = 8.81/3.5 = 2.52。\n   Full_s1 的 DR reduction 效力是 semantic_only 的 2.52 倍。\n   SciERC ratio=3.88 更高是因为 SciERC full_s1 几乎完全消除了 DR（0.93%）。\n5. CF 升至 2.5%（vs unconstrained ~0.1%），模式与 SciERC semantic_only(2.71%) 一致：\n   semantic per-relation 独立 enforcement 引入跨 relation type 不一致。\n   DocRED CF 略低因为 DocRED entity types 语义边界更清晰。\n"
57	  },
58	  {
59	    "name": "Latency comparison (constrained vs unconstrained)",
60	    "description": "测量 unconstrained / grammar_only / semantic_only / full_s1 / full_s2\n的 tokens/second 和 wall-clock time，量化约束开销的实用性边界。\n",
61	    "results": {
62	      "scierc": {
63	        "unconstrained_tok_per_sec": 13.0,
64	        "grammar_only_tok_per_sec": 11.5,
65	        "semantic_only_tok_per_sec": 9.8,
66	        "full_s1_tok_per_sec": 9.5,
67	        "full_s2_tok_per_sec": 6.0,
68	        "overhead_ratio": {
69	          "grammar_only": 1.13,
70	          "semantic_only": 1.33,
71	          "full_s1": 1.37,
72	          "full_s2": 2.17
73	        }
74	      },
75	      "docred": {
76	        "unconstrained_tok_per_sec": 12.5,
77	        "grammar_only_tok_per_sec": 11.0,
78	        "full_s1_tok_per_sec": 9.0,
79	        "overhead_ratio": {
80	          "grammar_only": 1.14,
81	          "full_s1": 1.39
82	        }
83	      },
84	      "wall_clock_per_sample_sec": {
85	        "scierc_unconstrained": 16,
86	        "scierc_full_s1": 22,
87	        "docred_unconstrained": 64,
88	        "docred_full_s1": 89
89	      }
90	    },
91	    "tables": [
92	      "Table 6: Inference Latency Overhead (或 Appendix Table A2)"
93	    ],
94	    "figures": [],
95	    "analysis": "1.37x overhead 完全可接受。Post-hoc filtering 需重新生成 ~15% 被拒 triples\n（等效 ~1.15x 但无法引导到有效输出，且对 streaming 场景不可用）。\nS2 的 2.2x 开销 + 无质量优势，进一步确认 S1 为推荐策略。\n建议在 §5 用 1 句话报告 overhead，不需单独 section。\n\n\n1. Grammar-only 开销 ~13%：XGrammar 用 pushdown automaton + C++ backend 计算 token mask，\n   高度优化。文献报告 overhead <10%（Dong et al. 2024），但 IE schema 嵌套结构\n   比纯 JSON grammar 复杂（entity list + relation list + nested types），实际稍高。\n2. Semantic 层额外开销 ~20%：TypeConstraintProcessor 是 Python 实现，\n   每 token 需检查 entity registry 状态 + 判断生成位置 + 动态计算 logit mask。\n   Python GIL 与 GPU inference 的交互是主要瓶颈。\n3. Full_s1 ≈ semantic 开销：bitwise AND 两个 mask 是 O(vocab_size) 操作，\n   可忽略不计，所以 full_s1 ≈ max(grammar, semantic) ≈ semantic。\n4. Full_s2 ~2.2x：两个完整 forward pass，\n   Pass 2 还需编译 input-dependent grammar，额外消耗 ~0.1-0.2x。\n5. DocRED 和 SciERC 的 overhead ratio 接近（1.37 vs 1.39），\n   说明开销是 per-token 而非 per-document，与文档长度无关。\n"
96	  },
97	  {
98	    "name": "Llama-3.1-8B cross-model violation rate (SciERC)",
99	    "description": "在 Llama-3.1-8B 上复现 SciERC minimal prompt + 可选 full_s1，\n验证 violation landscape 和 grammar 泛化性的模型无关性。\n",
100	    "results": {
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "267cea7a-9652-41b6-9c97-1ac2c7114f02",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "63650bb3-a508-46d9-8801-4640aae1d585",
  "sourceToolAssistantUUID": "267cea7a-9652-41b6-9c97-1ac2c7114f02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-14T10:51:35.041Z_

Now let me check the actual violation report data from the real experiments to verify against imagined data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63650bb3-a508-46d9-8801-4640aae1d585",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LKXj9qoVYfX74oX1NR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2244a84-1de0-449d-9db6-c09e18502fbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxK6ufJP4ZxuLuhYQnCJtr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9769,
      "cache_read_input_tokens": 74373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9769,
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

_source line 45 · 2026-05-14T10:51:39.186Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Mb1z8i2oNqsZYGbC7zoMvq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/phase2_docred_full_s1/report/violation_report_docred_full_s1.json",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2244a84-1de0-449d-9db6-c09e18502fbc",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LKXj9qoVYfX74oX1NR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2713149-2887-4b17-9f82-73dc95765ca2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxK6ufJP4ZxuLuhYQnCJtr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9769,
      "cache_read_input_tokens": 74373,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9769
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 74373,
          "cache_creation_input_tokens": 9769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9769,
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

_source line 46 · 2026-05-14T10:51:39.193Z_

<details><summary>↩ Tool result · `toolu_01Mb1z8i2oNqsZYGbC7zoMvq`</summary>

```text
1	Remote file: /root/schema_semantic_constrained_ie/outputs/violation_report_docred_full_s1.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2713149-2887-4b17-9f82-73dc95765ca2",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "68790b6c-9bb1-4668-8c77-9e6ec99faaa7",
  "sourceToolAssistantUUID": "f2713149-2887-4b17-9f82-73dc95765ca2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T10:51:39.224Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RaSzFwWUP8hXtKyn4b3ZQk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/paper_results_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68790b6c-9bb1-4668-8c77-9e6ec99faaa7",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LKXj9qoVYfX74oX1NR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17648640-306f-4073-9395-b7f9a3db358a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxK6ufJP4ZxuLuhYQnCJtr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9769,
      "cache_read_input_tokens": 74373,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9769
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 74373,
          "cache_creation_input_tokens": 9769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9769,
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

_source line 48 · 2026-05-14T10:51:39.234Z_

<details><summary>↩ Tool result · `toolu_01RaSzFwWUP8hXtKyn4b3ZQk`</summary>

```text
1	# OntoCoDec Paper Results Summary
2	
3	> Generated: 2026-05-14 | Model: Qwen3-8B | SciERC: 551 samples | DocRED: 998 docs
4	
5	---
6	
7	## A. SciERC Phase 2 Main Table (Paper Table 1 Candidate)
8	
9	All experiments use identical code path (`run_constrained_extraction.py`), same prompt, same model, same test set (551 sentences).
10	
11	| Mode | DR↓ | RV↓ | ET↓ | CF | R-F1 | E-F1 | Triples | Entities |
12	|------|-----|-----|-----|----|------|------|---------|----------|
13	| unconstrained | 15.37% | 1.39% | 0.40% | 0.08% | 0.0823 | 0.3101 | 1724 | 2474 |
14	| grammar_only | 14.84% | 0% | 0% | 0.08% | 0.0823 | 0.3098 | 1725 | 2474 |
15	| semantic_only | 11.65% | 1.51% | 0.40% | 2.71% | 0.0815 | 0.3101 | 1726 | 2474 |
16	| **full_s1** | **0.93%** | **0%** | **0%** | **9.90%** | **0.0836** | **0.3098** | **1729** | **2474** |
17	| full_s2 | 0.97% | 0% | 0% | 8.03% | 0.0803 | 0.3190 | 1644 | 2228 |
18	
19	### Delta vs Unconstrained
20	
21	| Mode | ΔDR (pp) | ΔDR (rel%) | ΔRV | ΔET | ΔCF | ΔR-F1 (pp) | ΔE-F1 (pp) |
22	|------|----------|------------|-----|-----|-----|-------------|-------------|
23	| grammar_only | -0.53 | ↓3.4% | ↓100% | ↓100% | 0 | 0.00 | -0.03 |
24	| semantic_only | -3.72 | ↓24.2% | +0.12pp | 0 | +2.63pp | -0.08 | 0.00 |
25	| **full_s1** | **-14.44** | **↓93.9%** | **↓100%** | **↓100%** | **+9.82pp** | **+0.13** | **-0.03** |
26	| full_s2 | -14.40 | ↓93.7% | ↓100% | ↓100% | +7.95pp | -0.20 | +0.89 |
27	
28	**Experiment IDs**: `phase2_scierc_unconstrained`, `phase2_scierc_grammar_only`, `phase2_scierc_semantic_only`, `phase2_scierc_full_s1`, `phase2_scierc_full_s2`
29	
30	---
31	
32	## B. DocRED Phase 0 Comparison Table (Paper Table 2 Candidate)
33	
34	Prompt-level intervention on complex schema (96 relation types, avg 5.68 valid pairs/relation).
35	
36	| Mode | DR | RV | ET | CF | Parse Rate | Triples | Entities |
37	|------|----|----|----|----|------------|---------|----------|
38	| unconstrained | 18.70% | 28.90% | 7.50% | 0.08% | 96.40% | 16540 | 19099 |
39	| schema-informed | 12.84% | 18.41% | 0.61% | 0.15% | 94.49% | 16782 | 19524 |
40	
41	### Delta
42	
43	| Metric | Δpp | Relative ↓ |
44	|--------|-----|------------|
45	| DR | -5.86 | ↓31.3% |
46	| RV | -10.49 | ↓36.3% |
47	| ET | -6.89 | ↓91.9% |
48	| CF | +0.07 | — |
49	
50	### Cross-Dataset Prompt Effectiveness (SciERC vs DocRED)
51	
52	| Dataset | Relations | Avg Valid Pairs | DR (minimal) | DR (schema) | DR Reduction |
53	|---------|-----------|-----------------|--------------|-------------|--------------|
54	| SciERC | 7 | 26.1 | 15.37% | 5.78% | ↓62.4% |
55	| DocRED | 96 | 5.68 | 18.70% | 12.84% | ↓31.3% |
56	
57	Prompt-level intervention scales poorly with ontology complexity: 62% reduction on 7 relations → 31% on 96 relations.
58	
59	**Experiment IDs**: `mvp_phase0_violation_rate_docred`, `mvp_phase0_docred_schema`, `mvp_phase0_violation_rate`, `mvp_phase0_scierc_schema`
60	
61	---
62	
63	## C. Per-Relation DR Breakdown (Paper Figure Candidate)
64	
65	### SciERC: DR violation rate (%) by relation type across decoding modes
66	
67	| Relation | Unconstrained | Grammar | Semantic | Full S1 | Full S2 | S1 Δ (pp) |
68	|----------|:------------:|:-------:|:--------:|:-------:|:-------:|:---------:|
69	| Compare | 42.42 | 40.85 | 29.23 | 2.82 | 4.60 | -39.60 |
70	| Feature-of | 33.54 | 31.98 | 26.28 | 1.21 | 1.22 | -32.33 |
71	| Part-of | 25.00 | 23.38 | 11.27 | 0.00 | 1.25 | -25.00 |
72	| Evaluate-for | 24.06 | 23.13 | 23.13 | 5.76 | 5.08 | -18.30 |
73	| Hyponym-of | 14.52 | 14.40 | 7.09 | 0.00 | 0.00 | -14.52 |
74	| Used-for | 0.76 | 0.25 | 0.77 | 0.00 | 0.12 | -0.76 |
75	| Conjunction | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
76	
77	### Per-Relation Triple Counts (denominator context)
78	
79	| Relation | Unconstrained | Grammar | Semantic | Full S1 | Full S2 |
80	|----------|:------------:|:-------:|:--------:|:-------:|:-------:|
81	| Used-for | 787 | 791 | — | — | 855 |
82	| Feature-of | 486 | 494 | — | — | 328 |
83	| Evaluate-for | 133 | 134 | — | — | 118 |
84	| Hyponym-of | 124 | 125 | — | — | 97 |
85	| Part-of | 72 | 77 | — | — | 80 |
86	| Compare | 66 | 71 | — | — | 87 |
87	| Conjunction | 32 | 33 | — | — | 79 |
88	
89	**Key patterns**:
90	- Grammar layer alone has negligible DR effect (↓3.4% relative) — expected, no D/R constraints in grammar
91	- Semantic-only reduces DR for high-violation relations (Compare -13pp, Feature-of -7pp) but residual remains high
92	- Full S1 achieves near-zero DR across all relations; residual concentrates on Evaluate-for (5.76%) and Compare (2.82%)
93	- S2 slightly worse than S1 on Compare (4.60 vs 2.82), Part-of (1.25 vs 0.00), Used-for (0.12 vs 0.00)
94	
95	### SciERC Phase 0: Schema-Informed Prompt Per-Relation DR
96	
97	| Relation | Minimal | Schema-informed | Δpp |
98	|----------|:-------:|:---------------:|:---:|
99	| Feature-of | 33.54% | ~11.2% | -22.3 |
100	| Part-of | 25.00% | ~2.5% | -22.5 |
101	| Compare | 42.42% | ~27.6% | -14.8 |
102	| Evaluate-for | 24.06% | ~29.9% | **+5.8** |
103	| Hyponym-of | 14.52% | — | — |
104	| Used-for | 0.76% | — | — |
105	
106	Evaluate-for **regresses** with schema-informed prompt — prior-constraint conflict.
107	
108	---
109	
110	## D. Key Findings
111	
112	### D1. Claim Support Mapping
113	
114	**Claim 1 — Violation Landscape** (systematic, non-trivial violation rates):
115	- `mvp_phase0_violation_rate`: SciERC DR=15.37%, 3× above 5% threshold
116	- `mvp_phase0_violation_rate_docred`: DocRED DR=18.70%, comparable despite 14× larger ontology
117	- Per-relation: Compare 42.4%, Feature-of 33.5% vs Used-for 0.76% — violation driven by constraint tightness, not ontology size
118	
119	**Claim 2 — Prompt Insufficiency** (prompt reduces but cannot eliminate):
120	- `mvp_phase0_scierc_schema`: SciERC DR 15.37%→5.78% (↓62.4%), still >5%
121	- `mvp_phase0_docred_schema`: DocRED DR 18.70%→12.84% (↓31.3%), scales poorly
122	- Evaluate-for regression +5.8pp demonstrates prompt unreliability at per-relation level
123	
124	**Claim 3 — Composable Constraint Framework** (grammar enables semantic):
125	- `phase2_scierc_grammar_only`: RV 1.39%→0%, ET 0.40%→0%, DR unchanged (14.84%). F1 neutral.
126	- `phase2_scierc_semantic_only`: DR ↓24.2% but RV/ET persist — semantic needs grammar as prerequisite
127	- `phase2_scierc_full_s1`: DR ↓93.9%, RV→0%, ET→0%. Layers complementary with enabling dependency.
128	
129	**Claim 4 — S1 vs S2 Trade-off** (architectural ablation):
130	- `phase2_scierc_full_s1`: DR=0.93%, CF=9.90%, R-F1=0.0836
131	- `phase2_scierc_full_s2`: DR=0.97%, CF=8.03%, R-F1=0.0803
132	- S1 recommended: simpler, marginally better DR and F1. S2 is variant showing framework flexibility.
133	
134	### D2. CF Violation Root Cause Analysis
135	
136	| Metric | grammar_only | full_s1 | full_s2 |
137	|--------|:-----------:|:-------:|:-------:|
138	| CF rate | 0.08% | 9.90% | 8.03% |
139	
140	**CF is 100% introduced by the semantic layer** (grammar_only CF = unconstrained CF = 0.08%).
141	
142	**Subtypes**:
143	- **EVR (entity-vs-relation type drift)**: >90% of CF. Same entity assigned different types in entity list vs relation triples.
144	  - S1: 245 entities (7.34% of entity mentions)
145	  - S2: 178 entities (5.54%, ↓27% vs S1)
146	- **Within-relation** (same entity typed differently across relations):
147	  - S1: 10 (0.36%)
148	  - S2: 18 (0.72%)
149	
150	**Top conflict patterns** (SciERC type system ambiguity):
151	| Type Pair | Count |
152	|-----------|:-----:|
153	| Generic ↔ OtherScientificTerm | 60 |
154	| Material ↔ OtherScientificTerm | 28 |
155	| Material ↔ Method | 20 |
156	
157	These reflect genuine semantic boundary ambiguity in SciERC's type system — the same term can be legitimately categorized as either type depending on context.
158	
159	**Severity distinction**:
160	- DR violations = structurally invalid triples (downstream systems reject) → hard constraint
161	- CF violations = individual triples remain type-valid, only cross-triple consistency broken → soft preference
162	
163	### D3. S1 vs S2 Trade-off Summary
164	
165	| Dimension | S1 (single-pass) | S2 (two-pass) | Winner |
166	|-----------|:-----------------:|:-------------:|:------:|
167	| DR | 0.93% | 0.97% | S1 (marginal) |
168	| CF | 9.90% | 8.03% | S2 (not significant) |
169	| R-F1 | 0.0836 | 0.0803 | S1 |
170	| E-F1 | 0.3098 | 0.3190 | S2 |
171	| Triples generated | 1729 | 1644 | S1 (more output) |
172	| Entities generated | 2474 | 2228 | S1 (more output) |
173	| Simplicity | Single pass | Two passes | S1 |
174	
175	**Recommendation**: S1 as primary method, S2 as ablation/appendix. S2 does NOT solve CF — the 1.87pp difference is not significant at n≈2400 entities.
176	
177	### D4. F1 Neutrality Evidence
178	
179	| Mode | R-F1 | vs unconstrained |
180	|------|:----:|:----------------:|
181	| unconstrained | 0.0823 | — |
182	| grammar_only | 0.0823 | +0.00pp |
183	| semantic_only | 0.0815 | -0.08pp |
184	| full_s1 | 0.0836 | +0.13pp |
185	| full_s2 | 0.0803 | -0.20pp |
186	
187	All within noise on ~1700 triples, single seed. **Frame as F1-neutral, NOT F1-improvement.** No bootstrap CI computed.
188	
189	---
190	
191	## E. Pending Experiments
192	
193	### Running
194	1. **DocRED Phase 2 grammar_only** (`phase2_docred_grammar_only`): 998 docs on cuda:0, started 2026-05-14T01:55
195	2. **DocRED Phase 2 full_s1** (`phase2_docred_full_s1`): 998 docs on cuda:1, started 2026-05-14T02:07
196	
197	### Needed for Paper
198	3. **DocRED Phase 2 full_s1 completion** → validates cross-dataset generalization (Table 2 extension)
199	4. **DocRED Phase 2 semantic_only** → completes ablation story on complex schema
200	
201	### Stretch Goals
202	5. **Cross-model validation** (Llama-3.1-8B) → addresses Reviewer C5
203	6. **Bootstrap CI for F1** → statistical backing for F1-neutrality claim
204	7. **DocRED Phase 2 full_s2** → S1/S2 comparison on complex schema
205	
206	---
207	
208	## Appendix: Raw Experiment Registry
209	
210	| Exp ID | Status | Dataset | Mode | Samples | Wall Clock |
211	|--------|--------|---------|------|---------|------------|
212	| mvp_phase0_violation_rate | DONE | SciERC | minimal prompt | 551 | 1.13 GPU-hr |
213	| mvp_phase0_scierc_schema | DONE | SciERC | schema-informed prompt | 551 | 1.01 GPU-hr |
214	| mvp_phase0_violation_rate_docred | DONE | DocRED | minimal prompt | 998 | — |
215	| mvp_phase0_docred_schema | DONE | DocRED | schema-informed prompt | 998 | 3.75 GPU-hr |
216	| phase2_scierc_unconstrained | DONE | SciERC | unconstrained decoding | 551 | 1.44 GPU-hr |
217	| phase2_scierc_grammar_only | DONE | SciERC | grammar-only decoding | 551 | — |
218	| phase2_scierc_semantic_only | DONE | SciERC | semantic-only decoding | 551 | 0.73 GPU-hr |
219	| phase2_scierc_full_s1 | DONE | SciERC | full S1 (grammar+semantic) | 551 | 0.73 GPU-hr |
220	| phase2_scierc_full_s2 | DONE | SciERC | full S2 (two-pass) | 551 | 0.10 GPU-hr |
221	| phase2_s2_pilot50 | DONE | SciERC | S2 pilot (50 samples) | 50 | — |
222	| phase2_docred_grammar_only | RUNNING | DocRED | grammar-only decoding | 998 | — |
223	| phase2_docred_full_s1 | RUNNING | DocRED | full S1 (grammar+semantic) | 998 | — |
224	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17648640-306f-4073-9395-b7f9a3db358a",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "9205ccf3-d4c1-4cea-91cb-d596707103d3",
  "sourceToolAssistantUUID": "17648640-306f-4073-9395-b7f9a3db358a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-14T10:51:42.905Z_

Now let me read the DocRED root cause analysis for tightness correlation data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9205ccf3-d4c1-4cea-91cb-d596707103d3",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LL7eatfYcJjeXzfKrx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6acb6ffd-e227-4829-bfb7-1f4944a947e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PrZ3VxBkH8EhkbL5cZbCip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5183,
      "cache_read_input_tokens": 84142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5183,
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

_source line 50 · 2026-05-14T10:51:44.810Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LKiaSZaJV5xHTkRPExw2JL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/docred_full_s1_dr_root_cause_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6acb6ffd-e227-4829-bfb7-1f4944a947e6",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LL7eatfYcJjeXzfKrx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f43860f-ece7-4bf4-abb3-580c72346712",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PrZ3VxBkH8EhkbL5cZbCip",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5183,
      "cache_read_input_tokens": 84142,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5183
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 84142,
          "cache_creation_input_tokens": 5183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5183,
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

_source line 51 · 2026-05-14T10:51:44.823Z_

<details><summary>↩ Tool result · `toolu_01LKiaSZaJV5xHTkRPExw2JL`</summary>

```text
1	# DocRED full_s1 DR 10.19% 根因分析
2	
3	## 1. 核心结论
4	
5	DocRED full_s1 的 DR=10.19% 远高于 SciERC full_s1 的 DR=0.93%，**根因是 DocRED 的 ontology constraints 远比 SciERC 更紧**：
6	
7	| 指标 | SciERC | DocRED |
8	|------|--------|--------|
9	| Entity types | 6 | 6 |
10	| Max possible pairs | 36 | 36 |
11	| Relations | 7 | 96 |
12	| **Avg tightness** | **0.333** | **0.842** |
13	| Median valid_pairs/relation | 23 | 5 |
14	| Relations with tightness ≥ 0.85 | 0/7 (0%) | 50/96 (52%) |
15	| Relations with tightness ≥ 0.95 | 0/7 (0%) | 4/96 (4%) |
16	
17	SciERC 的约束极宽松（Used-for 允许 35/36 对），DocRED 的约束极严格（中位数仅 5 对，最少 1 对）。
18	
19	## 2. Semantic 层效果评估
20	
21	Semantic 层确实大幅降低了 DR，但无法完全消除高 tightness relations 的 violations：
22	
23	| 配置 | DR | 说明 |
24	|------|------|------|
25	| Grammar-only | 26.17% | 4538/17340 violations |
26	| **Full_s1** | **10.19%** | **1771/17372 violations** |
27	| 绝对改善 | **15.98pp** | |
28	| 相对改善 | **61.0%** | |
29	
30	Semantic 层在大多数 relations 上有效，仅 2 个 relation 完全无改善（P171 parent taxon、P676 lyrics by）。
31	
32	## 3. Tightness 与 DR 的关系
33	
34	Pearson r(tightness, DR_rate) = **0.3682** (n=90, ≥5 triples)
35	
36	按 tightness 分桶的聚合 DR：
37	
38	| Tightness 区间 | Valid pairs | Relations | Agg DR | Violations |
39	|----------------|------------|-----------|--------|------------|
40	| 0.95-1.00 | 1-2 pairs | 4 | **30.6%** | 78/255 |
41	| 0.90-0.94 | 3-4 pairs | 15 | **19.3%** | 230/1192 |
42	| 0.85-0.89 | 4-5 pairs | 28 | **12.9%** | 658/5107 |
43	| 0.80-0.84 | 6-7 pairs | 23 | 7.0% | 322/4587 |
44	| 0.70-0.79 | 8-11 pairs | 18 | 9.0% | 477/5305 |
45	| <0.70 | 11+ pairs | 2 | 0.7% | 6/910 |
46	
47	**明确的单调趋势**：tightness 越高 → DR 越高。
48	
49	## 4. Top 15 高违规 Relations
50	
51	| Rel | Name | Pairs | Tight | Total | Viol | DR% | GO→S1 改善 |
52	|-----|------|-------|-------|-------|------|-----|-----------|
53	| P1001 | applies to jurisdiction | 8 | 0.778 | 966 | 194 | 20.1% | +19.1pp |
54	| P737 | influenced by | 4 | 0.889 | 581 | 131 | 22.6% | +26.5pp |
55	| P276 | location | 5 | 0.861 | 451 | 128 | 28.4% | +20.2pp |
56	| P1344 | participant of | 7 | 0.806 | 488 | 95 | 19.5% | +17.0pp |
57	| P582 | end time | 3 | 0.917 | 186 | 81 | 43.5% | +19.1pp |
58	| P800 | notable work | 4 | 0.889 | 372 | 79 | 21.2% | +15.2pp |
59	| P50 | author | 8 | 0.778 | 433 | 72 | 16.6% | +15.8pp |
60	| P463 | member of | 10 | 0.722 | 745 | 71 | 9.5% | +9.7pp |
61	| P607 | conflict | 7 | 0.806 | 278 | 68 | 24.5% | +15.2pp |
62	| P740 | location of formation | 6 | 0.833 | 1124 | 58 | 5.2% | +16.6pp |
63	| P206 | located in/next to water | 4 | 0.889 | 652 | 55 | 8.4% | +30.2pp |
64	| P576 | dissolved/abolished | 4 | 0.889 | 146 | 53 | 36.3% | +9.4pp |
65	| P1056 | product/material produced | 2 | 0.944 | 156 | 48 | 30.8% | +46.7pp |
66	| P205 | basin country | 1 | 0.972 | 108 | 40 | 37.0% | +27.5pp |
67	| P1366 | replaced by | 5 | 0.861 | 120 | 31 | 25.8% | +24.6pp |
68	
69	Top 15 贡献 1352/1771 = **76.3%** 的总违规。
70	
71	## 5. Extreme DR Relations (DR > 40%)
72	
73	| Rel | Name | Pairs | DR% |
74	|-----|------|-------|-----|
75	| P1198 | unemployment rate | 2 | 83.3% |
76	| P6 | head of government | 4 | 84.6% |
77	| P171 | parent taxon | 4 | 77.8% |
78	| P35 | head of state | 4 | 64.7% |
79	| P190 | sister city | 1 | 58.0% |
80	| P488 | chairperson | 3 | 52.4% |
81	| P1336 | territory claimed by | 3 | 45.0% |
82	| P582 | end time | 3 | 43.5% |
83	
84	这些 relations 都是 1-4 valid pairs，constraint 极紧。
85	
86	## 6. Fallback 日志状态
87	
88	日志中无 `grammar_first_skip` / `fallback` 信息 — **fallback counter 代码在 full_s1 跑完后才加入**。因此无法直接计算 fallback 频次，上述分析基于 JSONL 输出的 violation 模式推断。
89	
90	## 7. 根因总结
91	
92	DR 10.19% 的根因是**约束紧度差异**，而非 semantic 层失效：
93	
94	1. **DocRED avg tightness = 0.842 vs SciERC = 0.333**：DocRED 每个 relation 平均仅允许 5.7 个 type pairs（SciERC 允许 24 个），LLM 生成违规 pair 的概率成倍增加
95	2. **Semantic 层实际生效**：DR 从 26.17%→10.19%（-61%），几乎所有 relation 都有改善
96	3. **剩余 10.19% 来自高 tightness relations**：tightness≥0.85 的 50 个 relations 贡献了绝大部分违规。这些 relation 仅允许 1-5 个 pairs，即使 semantic mask 缩小了候选空间，LLM 仍会在 token-level 生成不在允许集内的 type
97	4. **SciERC 本身约束太松**：最紧的 Compare 也有 17/36 pairs (tightness=0.528)，任何 type pair 几乎都能命中，所以 DR 天然低
98	
99	**推论**：要进一步降低 DocRED DR，需要强化高 tightness relations 的约束执行，例如：
100	- 在 fallback 时不完全退回 grammar-only，而是用 relaxed semantic mask
101	- 对 tightness≥0.9 的 relations，在 prompt 中显式列出允许的 type pairs
102	- 对极端 relations（1-2 pairs），考虑硬约束 post-filtering
103	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f43860f-ece7-4bf4-abb3-580c72346712",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "3b66c752-67d6-4efc-a338-92ccca08d32d",
  "sourceToolAssistantUUID": "4f43860f-ece7-4bf4-abb3-580c72346712",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-14T10:51:49.137Z_

Now I have a comprehensive understanding of the paper, its experimental setup, actual vs. imagined data, and the existing review. Let me now read the review context to understand what tier this dream review is for, and then produce my R1 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b66c752-67d6-4efc-a338-92ccca08d32d",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LLXuMABUEpxrQEnPuG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c3b038f-675d-4665-8a86-bcd3f044fabb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNN3o2t3Q65fMZMqHcZL9P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2697,
      "cache_read_input_tokens": 89325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2697,
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

_source line 53 · 2026-05-14T10:51:52.169Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ev2SCzJU2PLWLatVVn1qwC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper_framing.md",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c3b038f-675d-4665-8a86-bcd3f044fabb",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LLXuMABUEpxrQEnPuG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff003173-3409-42fd-9bde-d463d4a53339",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNN3o2t3Q65fMZMqHcZL9P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2697,
      "cache_read_input_tokens": 89325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2697,
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

_source line 54 · 2026-05-14T10:51:52.174Z_

<details><summary>↩ Tool result · `toolu_01Ev2SCzJU2PLWLatVVn1qwC`</summary>

```text
1	# OntoCoDec — Paper Framing
2	
3	## Target Venue
4	EMNLP 2026 (ARR submission May 25, 2026)
5	
6	## Title
7	OntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints
8	(Note: "Guaranteed" dropped per Reviewer — S1 DR=0.93%, S2 DR=0.97%, neither achieves 0%. "Near-Complete" is honest and defensible.)
9	
10	## Core Insight
11	LLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero F1 cost** through automatic ontology-to-decoder constraint compilation with two complementary layers.
12	
13	**Phase 2 confirmed**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%), and is **F1-neutral** (R-F1 +0.13pp, not statistically significant — correctly framed as "zero cost", not "improvement").
14	
15	## Core Claims
16	
17	### Claim 1 (Empirical): Violation Landscape
18	LLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).
19	
20	**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.
21	
22	**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.
23	
24	### Claim 2 (Empirical): Prompt Insufficiency
25	Schema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:
26	- Overall: 15.4% → 5.78% (-62.4%), still above 5%
27	- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)
28	- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses
29	
30	**Narrative**: This is NOT about "5.78% barely above 5%". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.
31	
32	### Claim 3 (Methodological): Composable Constraint Framework
33	OntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:
34	1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)
35	2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking
36	
37	The two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT "synergistic" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.
38	
39	The two layers compose via bitwise AND of token masks. Recommended framing: "Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor."
40	
41	**Graceful degradation** (per Reviewer assessment, D008): When $M_{semantic} \cap M_{grammar} = \emptyset$ (semantic layer would mask all grammar-valid tokens), the system falls back to grammar-only control. Occurred 1/998 DocRED docs (0.1%), 0/551 SciERC sentences — consistent with tighter constraints increasing empty-intersection likelihood. Implementation is error recovery (fallback), NOT formal invariant guarantee. Do NOT frame as "provable composition" — fallback's existence is counter-evidence. Frame as "engineering robustness" in §4; mention cross-dataset observation in §5 Discussion (1-2 sentences, N=1 too weak for dedicated analysis).
42	
43	**Decidability taxonomy**: Constraints classified by prefix-decidability:
44	- (a) Purely local: entity type ∈ vocabulary (grammar layer)
45	- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)
46	- (c) Truly non-local: forward coreference — out of scope for forward-only decoding
47	
48	### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation
49	- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.
50	- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff003173-3409-42fd-9bde-d463d4a53339",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "beba7dd1-9dcd-4a76-86e1-2976088daf84",
  "sourceToolAssistantUUID": "ff003173-3409-42fd-9bde-d463d4a53339",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-14T10:51:56.458Z_

I now have a thorough understanding of the complete paper, the experimental data (both real and imagined), the project history, and the existing review. Let me now submit my review report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "beba7dd1-9dcd-4a76-86e1-2976088daf84",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LM6MEZMKkMWPRiBbTq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8320b1c5-985f-4273-97e3-8172a0f8a24f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Se8Brzu8n8zK6LyL5c2zBj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1720,
      "cache_read_input_tokens": 92022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1720,
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

_source line 56 · 2026-05-14T10:51:57.490Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019HGhTJtTxLHaLTDjBBaxzN`</summary>

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
  "parentUuid": "8320b1c5-985f-4273-97e3-8172a0f8a24f",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LM6MEZMKkMWPRiBbTq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f01c8be-4390-4fdf-9409-e3e8227a7f88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Se8Brzu8n8zK6LyL5c2zBj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1720,
      "cache_read_input_tokens": 92022,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1720
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 92022,
          "cache_creation_input_tokens": 1720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1720,
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

_source line 57 · 2026-05-14T10:51:57.493Z_

<details><summary>↩ Tool result · `toolu_019HGhTJtTxLHaLTDjBBaxzN`</summary>

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
  "parentUuid": "0f01c8be-4390-4fdf-9409-e3e8227a7f88",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "4e20fc3a-96a6-434b-aa36-183810c8541b",
  "sourceToolAssistantUUID": "0f01c8be-4390-4fdf-9409-e3e8227a7f88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-14T10:52:01.514Z_



Now let me submit my comprehensive R1 review focused on Methods and Experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e20fc3a-96a6-434b-aa36-183810c8541b",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LMTf8or9DG5TeoNkJp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1198170b-8ea2-42c8-a7c8-c75b87e05a7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0142qKdB7iyRaVDmuBi3oBUn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 707,
      "cache_read_input_tokens": 93742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 707,
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

_source line 59 · 2026-05-14T10:54:44.886Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01TJkGrPHCrBsF3HxXnXUoF9`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "tier": "best",
  "dream_id": "dream_20260514T094226",
  "overall_score": "4 - Weak Accept",
  "report": "\n# Dream Review Report: OntoCoDec (R1 — Methods & Experiments)\n\n**Paper**: OntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints\n**Reviewer**: R1 (Methods & Experiments focus)\n**Date**: 2026-05-14\n\n---\n\n## 1. Methods Assessment\n\n### 1.1 Two-Layer Architecture: Motivation and Soundness\n\nThe grammar + semantic decomposition is well-motivated by the decidability taxonomy. The key insight is correct: structural/vocabulary constraints (ET, RV) are CFG-expressible and can be perfectly enforced by a pushdown automaton, while cross-field domain/range constraints require state maintained across generation positions and fall outside CFG expressiveness. This clean separation into \"what a grammar can do\" vs. \"what requires stateful tracking\" provides principled justification for two layers rather than one monolithic system.\n\nThe grammar layer's use of XGrammar is a sound engineering choice — compiling the ontology's entity and relation type vocabularies into a CFG that also enforces JSON structure is straightforward but effective. The semantic layer's entity registry design (recording entity names/types as they are generated, then using this state to mask logits when relation argument types are being generated) is the correct architecture for enforcing prefix-decidable constraints during autoregressive decoding.\n\n**Concern**: The semantic layer is described at a high level but lacks important implementation details. How exactly is \"current generation position\" detected during autoregressive decoding? Is this done via string matching on partial output, grammar state introspection, or some other mechanism? Position detection errors would cause the semantic layer to apply masks at wrong positions, potentially degrading both constraint enforcement and generation quality. The paper should describe this mechanism precisely.\n\n### 1.2 Decidability Taxonomy\n\nThe three-way classification (purely local / prefix-decidable with state / truly non-local) is correct and useful. It maps cleanly to the two implemented layers plus a principled out-of-scope boundary. The taxonomy is not deeply novel — similar classifications exist in the type-checking and program analysis literature — but its application to IE constraint enforcement is appropriate and clarifying.\n\nOne gap: the taxonomy does not address constraints that are prefix-decidable but require non-trivial lookahead or backtracking within the current triple. For example, if head entity type influences which relation types are valid (not just the reverse), this creates a chicken-and-egg problem within a single triple that the current taxonomy does not distinguish from Type (b). The paper's output format (entity list first, then relation list) sidesteps this by establishing entity types before relations are generated, but this design dependency should be made explicit as it is load-bearing for the taxonomy's applicability.\n\n### 1.3 Layer Composition and Fallback\n\nThe bitwise AND composition is the natural and correct choice — it enforces the intersection of both constraint sets. The enabling dependency argument is well-constructed: grammar ensures relation types are in the valid vocabulary, which is a prerequisite for the semantic layer to look up domain/range rules. Without grammar, the semantic layer encounters unknown relation types and degrades to a no-op for those triples. This is empirically verified: semantic-only achieves only 24% DR reduction (SciERC) vs. full S1's 94%.\n\nThe graceful degradation (fallback to grammar-only when semantic AND grammar masks have empty intersection) is a necessary engineering safeguard. The paper correctly reports its rarity (1/998 DocRED, 0/551 SciERC) without over-claiming it as a formal invariant.\n\n**Concern**: The fallback mechanism means the system silently abandons semantic constraints when they conflict with grammar constraints. The paper should analyze what happens in these cases: does the fallback produce DR violations? If so, this is a predictable failure mode that practitioners should be warned about. The root cause analysis mentions that fallback counter code was added after the full_s1 run completed, meaning the actual fallback frequency is inferred rather than directly measured — this should be acknowledged.\n\n### 1.4 Enabling Dependency\n\nThe enabling dependency argument is the most interesting methodological claim. It is convincing on SciERC (enabling ratio 3.88x) and preserved on DocRED (2.52x), with the lower DocRED ratio explained by higher RV rates (29% vs 1.4%) creating a larger \"blind spot\" for the semantic layer. The mechanistic explanation is sound: if ~29% of triples use out-of-vocabulary relation types, the semantic layer literally cannot look up constraints for them.\n\nHowever, the \"enabling ratio\" metric conflates two distinct effects: (1) grammar eliminating RV so that the semantic layer can look up constraints, and (2) grammar enforcing valid JSON structure so that triple fields are correctly parsed. Both contribute, but the paper presents them as a single \"enabling\" mechanism. Decomposing these two effects (e.g., by measuring semantic effectiveness on the subset of triples with valid relation types in the unconstrained output) would strengthen the claim.\n\n### 1.5 Technical Gaps\n\n1. **No formal guarantees on the semantic layer**: The grammar layer provides formal guarantees (CFG acceptance), but the semantic layer's correctness depends on accurate position detection during autoregressive generation. If position detection fails (e.g., due to unexpected token boundaries), the semantic mask may not be applied, leading to silent violations. The paper does not discuss the reliability of position detection.\n\n2. **Entity registry assumes entities precede relations in output**: The semantic layer depends on entities being generated before relations so that the registry is populated when relation constraints are checked. This is enforced by the grammar (JSON structure), creating a hidden coupling between layers that should be documented as a design constraint.\n\n3. **No discussion of beam search or sampling**: All experiments appear to use greedy decoding. Constrained decoding with beam search raises composition issues (different beams may have different entity registries). The paper should state the decoding strategy and discuss generalization to non-greedy settings.\n\n---\n\n## 2. Experiments Assessment\n\n### 2.1 Ablation Completeness\n\nThe five-configuration ablation (unconstrained / grammar_only / semantic_only / full_s1 / full_s2) is well-designed and sufficient for decomposing contributions. Each configuration isolates a specific component:\n- Grammar-only: validates grammar layer in isolation (ET/RV elimination, DR unchanged)\n- Semantic-only: validates semantic layer in isolation (partial DR reduction, ET/RV persist)\n- Full S1: validates composition (near-complete DR elimination + ET/RV elimination)\n- Full S2: validates alternative architecture (no improvement over S1)\n\nThe ablation is clean on SciERC (all 5 configurations completed with 551 samples each). On DocRED, the ablation is **complete in the paper's tables** but there is a significant provenance concern: the project status shows DocRED unconstrained and semantic-only as still running (\"RUNNING\" in the report) or as imagined experiments. The paper reports specific numbers for these configurations (DR=19.0% unconstrained, DR=15.5% semantic-only) that match the \"expected_results\" in the imagined experiments YAML file almost exactly. This raises the possibility that some DocRED ablation numbers are projected rather than measured.\n\n**This is the most serious concern in the review.** If the DocRED unconstrained (19.0%) and semantic-only (15.5%) numbers are projections, the enabling ratio (2.52x) and DR reduction (46%) calculations rest on imagined data. The paper must confirm all reported numbers come from completed experiments and provide experiment IDs and completion timestamps.\n\n### 2.2 Evaluation Methodology\n\nThe four violation types (ET, RV, DR, CF) are well-defined and independently measured, providing a comprehensive picture of constraint compliance. Using F1 as a control variable rather than an optimization target is the correct framing for this work.\n\n**Weaknesses in evaluation methodology**:\n\n1. **No statistical significance testing.** All results are single-seed, single-run. The F1-neutrality claim (8.36 vs 8.23 on SciERC) is asserted without bootstrap confidence intervals. On ~1700 triples, the standard error of F1 is non-trivial; the +0.13pp difference could easily be noise, but this needs to be demonstrated, not assumed. Similarly, the DR differences between S1 (0.93%) and S2 (0.97%) should have significance tests to justify the claim that S1 is \"marginally better.\"\n\n2. **No per-document variance analysis.** DR and F1 are reported as aggregate numbers. Understanding per-document variance (e.g., does DR=10.19% on DocRED mean 10% of documents have very high DR, or all documents have moderate DR?) would provide practitioners with realistic expectations.\n\n3. **Fuzzy matching for evaluation.** The memory notes mention DocRED uses \"token overlap >80% or Levenshtein ≤2\" for entity matching. This is a reasonable choice but should be reported in the paper, as it affects F1 calculations and could interact with constraint enforcement (constrained outputs may have different surface forms than unconstrained outputs).\n\n### 2.3 Evidence Strength: SciERC\n\nThe SciERC evidence is strong and internally consistent:\n- DR reduction 94% is a clear, large effect that is unlikely to be noise\n- ET/RV elimination is perfect (0/1725 triples)\n- F1 neutrality is plausible (single-seed caveat acknowledged)\n- Per-relation breakdown shows expected patterns (high-tightness relations have residual DR)\n- The enabling dependency is well-quantified (3.88x ratio)\n- S1 vs S2 comparison is informative (S2 offers no advantage)\n\nThe main caveat is that SciERC is a small, simple ontology (7 relations, loose constraints). The method's near-perfect performance here may be partly because the constraints are so loose that violations are \"easy\" to prevent — the model's distributional prior already nearly satisfies most constraints.\n\n### 2.4 Evidence Strength: DocRED\n\nThe DocRED evidence is weaker but more interesting:\n- DR reduction of 46% is meaningful but far from the \"near-complete\" headline\n- ET/RV elimination generalizes perfectly (ET→0%, RV→0.03%)\n- The tightness-DR correlation provides an analytical explanation for lower effectiveness\n- Per-relation distribution shows bimodal pattern (67% of relations <2% DR)\n\n**Concerns**:\n1. **Data provenance** (repeated from 2.1): The DocRED unconstrained and semantic-only numbers may not be from completed experiments.\n2. **Grammar-only DR anomaly**: Grammar-only DR on DocRED is reported as 26.17%, *higher* than unconstrained (18.7%). The paper does not report this number in the main DocRED table (it shows \"---\" for grammar-only DR). The root cause analysis explains this as \"grammar forcing valid relation names changes the triple distribution,\" but this is a concerning result that deserves discussion — it means grammar enforcement, while eliminating RV/ET, actually *increases* domain/range violations by changing which relations the model generates.\n3. **DocRED unconstrained DR discrepancy**: Table 1 reports 18.7% (Phase 0) while Table 4 reports 19.0% (Phase 2). If these come from different code paths, the delta calculations in Table 4 should use the Phase 2 baseline, but this needs explicit reconciliation.\n\n### 2.5 Tightness-DR Correlation\n\nThe Spearman rho=0.52 (p<0.001, n=82) is statistically significant but moderate. It explains roughly 27% of rank variance, meaning 73% of per-relation DR variation is driven by other factors (relation frequency, entity type distribution, model-specific priors). The paper handles this well in the text, emphasizing the bucket-level monotonic trend and violation concentration rather than the absolute correlation value.\n\n**Concerns**:\n1. **Bucket inversion**: The 0.70-0.79 bucket (DR=9.0%) has higher aggregate DR than the 0.80-0.84 bucket (DR=7.0%). This breaks strict monotonicity. The root cause analysis attributes this to P463_member_of (tightness=0.722, DR=9.5%, n=745) — a single high-frequency relation dominating the bucket. This explanation is plausible but must be reported in the paper; currently it is not discussed.\n\n2. **Confound between tightness and frequency**: High-tightness relations tend to be lower-frequency (fewer training examples for the model). The correlation may partly capture frequency effects rather than pure constraint tightness effects. A partial correlation controlling for relation frequency would strengthen the analysis.\n\n3. **Overclaim in abstract**: The abstract states practitioners can get \"a priori estimates of constraint effectiveness\" from tightness. With rho=0.52, such estimates would have very wide prediction intervals. The practical utility is more \"identify which relations will be problematic\" (top-15 concentration) than \"predict exact DR for a new ontology.\"\n\n### 2.6 CF Violation Analysis\n\nThe CF analysis is one of the paper's stronger analytical contributions:\n- Clean ablation evidence: grammar-only CF = unconstrained CF (~0.08%), 100% of CF increase comes from the semantic layer\n- Cross-dataset comparison (9.9% SciERC vs 2.6% DocRED) supporting the type-system ambiguity hypothesis\n- Sub-type decomposition (EVR dominant at >90%)\n- Top conflict patterns revealing genuine type ambiguity (Generic vs OtherScientificTerm, ORG vs LOC)\n\n**Concerns**:\n1. The DR:CF trade-off ratio is presented favorably (3.6:1 on DocRED, but only 1.5:1 on SciERC). The SciERC ratio means that for roughly every 1.5pp of DR reduction, 1pp of CF is introduced — this is not overwhelmingly favorable, especially since the \"hard vs soft\" severity distinction is argued but never validated on a downstream task.\n\n2. The paper does not discuss whether CF violations are correlated with DR violations at the per-document level. If CF concentrates in the same documents where DR was high (i.e., the system is trading one problem for another in the same documents), the practical impact is different than if CF is distributed across different documents.\n\n### 2.7 Latency Analysis\n\nThe latency analysis is adequate: 1.37-1.39x overhead for full S1 is practically acceptable. The per-token nature of overhead (invariant to document length) is a useful finding. S2's 2.17x overhead with no quality benefit further justifies S1 as the recommended strategy.\n\nThe analysis could be strengthened by reporting variance across documents and the relationship between latency overhead and document length/complexity.\n\n### 2.8 Missing Cross-Model Validation\n\nThe cross-model validation with Llama-3.1-8B on SciERC is reported in the paper (Table 7), showing DR 14.5%→1.2% (92% reduction) and per-relation Spearman rho=0.89 between models. However, the experiment status shows these experiments as \"QUEUED\" (not completed). The numbers in the paper match the \"expected_results\" in the imagined experiments YAML file exactly (DR=14.5% unconstrained, DR=1.2% full_s1, rho=0.89).\n\n**This is the second major data provenance concern.** If the Llama-3.1-8B experiments were not actually completed, reporting their results as if they were is fabrication. The paper should either: (a) confirm these experiments were completed and provide timestamps, or (b) remove the cross-model section and acknowledge it as future work.\n\nEven if the Llama experiments are real, the cross-model validation is limited to SciERC (where the method already works well). Llama on DocRED — where the method is weaker — would be more informative.\n\n### 2.9 Missing Baselines and Comparisons\n\n1. **No post-hoc filtering baseline**: The paper argues against post-hoc filtering in the introduction but never implements it as a baseline. A simple post-hoc filter (remove triples with type violations) would show the F1 cost of discarding invalid triples vs. OntoCoDec's approach of preventing them. This is a straightforward baseline that would strengthen the paper.\n\n2. **No comparison with PICARD or GenIE**: PICARD (Scholak et al., 2021) applies incremental parsing with semantic state during autoregressive decoding for SQL — methodologically very close to OntoCoDec's approach. GenIE (Josifoski et al., 2022) applies constrained decoding for IE with trie-based prefix trees. Neither is cited or compared.\n\n3. **No few-shot or fine-tuned baseline**: All experiments are zero-shot with ~8% relation F1. The violation landscape and constraint effectiveness may be very different with few-shot prompting or fine-tuned models where base F1 is higher. If violations are substantially lower with better base extractors, the motivation for decoding-time enforcement weakens.\n\n4. **No SciERC Spearman correlation**: The tightness-DR correlation is only computed on DocRED. SciERC has only 7 relations (too few for meaningful Spearman), but this asymmetry means the correlation claim rests on a single dataset. At minimum, reporting the SciERC per-relation DR vs. tightness qualitatively would show whether the trend is consistent.\n\n---\n\n## 3. Strengths\n\n- **Violation landscape study is an independent empirical contribution.** The systematic measurement of ontology constraint violations across two datasets, with per-relation distribution analysis and the finding that violation rates correlate with constraint tightness rather than ontology size, has standalone value regardless of the framework.\n\n- **Clean ablation design with the enabling ratio metric.** The 5-configuration ablation with the enabling ratio quantification (3.88x SciERC, 2.52x DocRED) cleanly decomposes the contribution of each layer and demonstrates that the layers are complementary rather than redundant.\n\n- **Grammar layer is a \"solved problem\" result.** ET/RV→0% across both datasets (7→96 relations, 14x scale) is an unambiguous, practically useful finding. This alone has engineering value.\n\n- **Honest framing of limitations.** The paper distinguishes \"near-complete\" (SciERC) from \"predictable partial reduction\" (DocRED) in the abstract. CF violations are proactively disclosed with root cause analysis. S2 is honestly positioned as offering no advantage over S1.\n\n- **Tightness-violation correlation transforms a weakness into an insight.** Rather than hiding the DocRED 10.19% residual DR, the paper explains *why* reduction is partial and provides practitioners with a diagnostic tool (tightness predicts difficulty).\n\n- **Evaluate-for regression is a compelling motivating example.** Schema-informed prompting *increasing* violations for a specific relation type (24.1%→29.9%) is a vivid demonstration that prompt-level intervention can be counterproductive, strongly motivating decoding-time enforcement.\n\n---\n\n## 4. Weaknesses\n\n- **Data provenance is uncertain for several reported numbers.** DocRED unconstrained, DocRED semantic-only, and Llama-3.1-8B experiments appear in the paper with specific numbers, but project status shows some of these experiments as still running or queued. The reported numbers closely match \"expected_results\" from the experiment design. If any numbers are projected rather than measured, this is a critical integrity issue.\n\n- **No statistical significance testing or confidence intervals.** All results are single-seed, single-run. F1-neutrality and DR differences between configurations lack statistical validation. For a top venue, this is below the expected standard of evidence.\n\n- **\"Near-Complete\" in the title does not apply to DocRED.** 46% DR reduction with 10.19% residual is \"partial.\" The title creates expectations the paper cannot meet for the more realistic, complex-ontology setting.\n\n- **Grammar-only DR increase on DocRED is unreported and concerning.** Grammar-only DR on DocRED is 26.17% (vs 18.7% unconstrained) — grammar enforcement *increases* DR by changing which relations the model generates. This important finding is hidden in the root cause analysis and not discussed in the paper.\n\n- **CF trade-off lacks downstream validation.** The \"DR is hard, CF is soft\" severity argument is qualitative. On SciERC, the DR:CF ratio is only 1.5:1 — for every 1.5pp of DR reduced, 1pp of CF is introduced. Without downstream task evaluation, the practical acceptability of this trade-off is unsubstantiated.\n\n- **Low absolute F1 (~8%) limits practical relevance.** In the zero-shot regime, most extracted triples are factually incorrect regardless of type validity. Enforcing type constraints on predominantly wrong triples provides limited practical benefit. The paper does not discuss this limitation.\n\n- **Missing key baselines.** No post-hoc filtering baseline, no comparison with PICARD or GenIE, no few-shot evaluation. These are standard comparisons a reviewer would expect.\n\n- **Tightness bucket inversion unreported.** The 0.70-0.79 bucket having higher DR than 0.80-0.84 breaks the claimed monotonic trend but is not discussed in the paper.\n\n- **Narrow experimental scope.** Two datasets, two models at 8B scale, zero-shot only. The \"model-agnostic\" claim rests on N=2 models, one of which may not have been actually evaluated.\n\n---\n\n## 5. Questions for Authors\n\n1. **Were all DocRED ablation numbers (unconstrained DR=19.0%, semantic-only DR=15.5%) and Llama-3.1-8B numbers (unconstrained DR=14.5%, full_s1 DR=1.2%) obtained from completed experiments?** Please provide experiment IDs and completion timestamps. If any numbers are projected from experiment designs, this must be disclosed.\n\n2. **Why is grammar-only DR on DocRED (26.17%) higher than unconstrained DR (18.7%)?** This means grammar enforcement increases domain/range violations. What is the mechanism? If grammar constrains the model to use only valid relation types, does it shift probability mass toward relation types with tighter domain/range constraints?\n\n3. **What decoding strategy is used — greedy, beam search, or sampling?** How would the constraint composition behave with beam search (where different beams may have different entity registries)?\n\n4. **How is \"current generation position\" detected in the semantic layer?** Is it based on grammar state, string matching on partial output, or token counting? What is the failure rate of position detection?\n\n5. **The 0.70-0.79 tightness bucket (DR=9.0%) has higher aggregate DR than the 0.80-0.84 bucket (DR=7.0%). What explains this monotonicity violation?** Is it dominated by P463_member_of?\n\n6. **What is the per-document variance of DR on DocRED?** Does 10.19% mean all documents have ~10% DR, or is it driven by a minority of high-DR documents?\n\n7. **Has a partial correlation between tightness and DR been computed controlling for relation frequency?** High-tightness relations tend to be low-frequency; the correlation may partly capture frequency effects.\n\n8. **Why no post-hoc filtering baseline?** A simple filter removing type-invalid triples would provide a direct comparison: post-hoc filtering achieves DR=0% trivially but at an F1 cost that OntoCoDec avoids. This comparison would sharpen the paper's contribution.\n\n9. **The residual 0.93% DR on SciERC — what happens to these triples?** Are they cases where the fallback was triggered, or cases where the semantic mask was applied but the model still chose a violating type despite masking? The latter should be impossible by construction; the former would indicate the fallback frequency is higher than reported.\n\n10. **Would the violation landscape look fundamentally different with few-shot prompting?** If 3-5 examples substantially reduce violations, the motivation for decoding-time enforcement weakens. Has any informal investigation been done?\n\n---\n\n## 6. Preliminary Score and Confidence\n\n**Score: 4/6 (Weak Accept)**\n\nThe paper makes genuine empirical contributions: the violation landscape study, the grammar layer's perfect generalization, and the tightness-violation correlation have independent value. The method is well-designed with a clean ablation story. The honest framing of limitations (DocRED partial reduction, CF trade-off, S2 offering no advantage) builds trust.\n\nHowever, significant concerns lower confidence: (1) data provenance uncertainty for multiple reported numbers, (2) absence of statistical significance testing, (3) missing standard baselines (post-hoc filtering, PICARD, few-shot), (4) the title overselling DocRED results, and (5) the low F1 regime limiting practical relevance. The technical novelty of the framework itself is limited — the individual components are existing techniques (XGrammar, LogitsProcessor, bitwise AND), and the \"enabling dependency\" is an empirical observation rather than a design innovation.\n\nThe paper is above the bar for empirical contributions and honest reporting, but below the bar for technical novelty and experimental rigor expected at a top venue main track. It would be a strong candidate for an applications or systems track.\n\n**Confidence: 4/5**\n\nI have high confidence in the methods and experiments assessment. I have carefully cross-referenced reported numbers against experiment status, reviewed the actual code architecture, and verified the analytical claims. The data provenance concern is based on concrete evidence (experiment status showing \"RUNNING\"/\"QUEUED\" for experiments whose numbers appear in the paper), though I cannot definitively determine whether experiments were completed between the status snapshot and paper generation.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1198170b-8ea2-42c8-a7c8-c75b87e05a7b",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2LMTf8or9DG5TeoNkJp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b293934-99e8-4f7e-971d-65321a7c01d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0142qKdB7iyRaVDmuBi3oBUn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 707,
      "cache_read_input_tokens": 93742,
      "output_tokens": 6235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 707
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6235,
          "cache_read_input_tokens": 93742,
          "cache_creation_input_tokens": 707,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 707,
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

_source line 60 · 2026-05-14T10:54:48.291Z_

<details><summary>↩ Tool result · `toolu_01TJkGrPHCrBsF3HxXnXUoF9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/review_report.md\", \"dream_id\": \"dream_20260514T094226\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b293934-99e8-4f7e-971d-65321a7c01d8",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "ac95df3e3c5999630",
  "type": "user",
  "uuid": "094d918f-1a6c-49d7-972e-5e44d5061eea",
  "sourceToolAssistantUUID": "1b293934-99e8-4f7e-971d-65321a7c01d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-14T10:55:04.940Z_

Review submitted. Here is a summary of the R1 review:

**Score: 4/6 (Weak Accept) | Confidence: 4/5**

**Key findings from the review:**

**Methods**: The two-layer grammar+semantic architecture is well-motivated by the decidability taxonomy. Layer composition via bitwise AND with graceful degradation is correctly designed. The enabling dependency is the most interesting methodological claim, convincingly quantified via the enabling ratio (3.88x SciERC, 2.52x DocRED). Technical gaps include underspecified position detection in the semantic layer, hidden dependency on output ordering (entities before relations), and no discussion of non-greedy decoding strategies.

**Experiments - Strengths**: Clean 5-configuration ablation, grammar layer perfectly generalizes across datasets (ET/RV to 0%), tightness-violation correlation transforms DocRED's weaker results into an analytical contribution, CF analysis with cross-dataset comparison is thorough.

**Experiments - Critical Concerns**:
1. **Data provenance**: DocRED unconstrained, DocRED semantic-only, and Llama-3.1-8B experiments appear in the paper but project status shows them as RUNNING/QUEUED. Reported numbers match "expected_results" from imagined experiments YAML. If any are projected rather than measured, this is a critical integrity issue.
2. **No statistical significance testing** -- all single-seed, single-run, no bootstrap CIs.
3. **Grammar-only DR on DocRED is 26.17% (higher than unconstrained 18.7%)** -- grammar enforcement increases DR by shifting relation distribution, but this is unreported in the paper.
4. **Missing baselines**: no post-hoc filtering, no PICARD/GenIE comparison, no few-shot evaluation.
5. **Title oversells**: "Near-Complete" does not apply to DocRED (46% reduction, 10.19% residual).
6. **Tightness bucket inversion** (0.70-0.79 > 0.80-0.84) breaks claimed monotonicity but is not discussed.

The report was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "094d918f-1a6c-49d7-972e-5e44d5061eea",
  "isSidechain": true,
  "agentId": "ac95df3e3c5999630",
  "requestId": "req_011Cb2La3p3c1iGZi44BjuTN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1597bc0c-7288-4c3d-a7f6-1af037b137ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01URpSbdWRbyJ4GqZMBE4ccU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6471,
      "cache_read_input_tokens": 94449,
      "output_tokens": 551,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6471
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 551,
          "cache_read_input_tokens": 94449,
          "cache_creation_input_tokens": 6471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6471,
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
