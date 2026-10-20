# Research conversation: You are Reviewer R2 for a top ML venue peer review. Your focus areas are **Novelty** and **Related Work**. Evaluate the 

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 1
- **Tool calls:** 28
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aa8b4c8fb42cb17c7.jsonl`
- **Structured JSON:** [`072ce6f9abed747583a8.json`](../../sessions/07/072ce6f9abed747583a8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

65 recorded events

### User

_source line 1 · 2026-05-14T10:51:06.720Z_

You are Reviewer R2 for a top ML venue peer review. Your focus areas are **Novelty** and **Related Work**. Evaluate the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary

**Title:** Type-Valid IE via Compiled Ontology Constraints

The paper presents ONTOCODEC, a framework that compiles IE ontology schemas into two composable constrained decoding layers for LLM-based zero-shot information extraction:
1. A **grammar layer** using XGrammar CFG constraints to enforce valid JSON structure, relation names ∈ R, entity types ∈ E
2. A **semantic layer** with a stateful entity registry + dynamic logit masking to enforce domain/range constraints

**Key results:**
- SciERC (7 relations): 94% DR reduction (15.4%→0.93%), F1-neutral
- DocRED (96 relations): 46% DR reduction (18.7%→10.2%), F1-neutral
- Grammar layer: ET→0%, RV→0% on both datasets
- Single model (Qwen3-8B), zero-shot setting only
- Violation landscape study as independent empirical contribution
- Constraint tightness predicts residual DR (Spearman correlation)

**Related work covered in paper (§6):**
- Constrained Decoding for Structured Generation: Willard & Louf 2023 (JSON), Scholak et al. 2021 (PICARD for SQL), XGrammar (Dong et al. 2024), GCD (Geng et al. 2024 — grammar + semantic for code gen)
- LLM-based IE: Wei et al. 2023 (zero-shot), Li et al. 2023 (CodeIE few-shot), Wang et al. 2023 (InstructUIE), GoLLIE (Sainz et al. 2024)
- Ontology-Based Validation: SHACL, description logic reasoners (post-hoc)
- Structured Output Quality: CRANE (Zheng et al. 2024), Structure Snowballing (Wu et al. 2024)

**From the review context (experiment plan):**
- Cross-model validation (Llama-3.1-8B) was planned but NOT completed
- The paper frames DocRED as a "stress test" rather than a primary showcase
- Title changed from "Near-Complete" to current form

## Your Review Task

Provide a structured review covering:

### 1. Novelty Assessment
- How novel is the core idea of compiling ontology schemas into constrained decoding layers?
- How novel is the specific two-layer decomposition (grammar + semantic)?
- Is the violation landscape study a genuine empirical contribution, or is this expected behavior?
- Is the "enabling dependency" insight between grammar and semantic layers novel?
- Is the constraint tightness analysis novel?
- How does this compare to GCD (Geng et al. 2024) which also integrates grammar + semantic constraints (for code generation)?
- Does the paper clearly articulate what is NEW vs what is engineering/application of known techniques?

### 2. Related Work Assessment
- Is the related work coverage adequate for a top venue?
- Are there important missing references? Consider:
  - Schema-guided dialogue / structured prediction with ontology constraints
  - Knowledge graph completion with type constraints
  - Type-constrained embedding methods
  - Other constrained decoding work beyond what's cited
  - IE-specific constraint enforcement (e.g., DeepStruct, StructGPT, etc.)
- Is the positioning against GoLLIE fair and accurate?
- Is the positioning against post-hoc validation approaches complete?
- Does the paper overclaim novelty in any area?

### 3. Clarity and Presentation
- Is the paper well-written and clearly structured?
- Are the contributions clearly stated?
- Is the notation consistent?
- Are tables and figures effective?

### 4. Strengths (bullet points)

### 5. Weaknesses (bullet points)

### 6. Questions for Authors (numbered)

### 7. Preliminary Score and Confidence
- Score: X/6
- Confidence: X/5

Be rigorous but fair. Focus on whether the novelty meets the bar for a top ML venue (~25% acceptance).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "ded7d963-b4ea-40c2-baf4-c240f5e85ddc",
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

_source line 2 · 2026-05-14T10:51:06.722Z_

```json
{
  "parentUuid": "ded7d963-b4ea-40c2-baf4-c240f5e85ddc",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
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
  "uuid": "96dd3fe6-27da-48d5-9a44-c64ec2efe76c",
  "timestamp": "2026-05-14T10:51:06.722Z",
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

_source line 3 · 2026-05-14T10:51:09.504Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96dd3fe6-27da-48d5-9a44-c64ec2efe76c",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LHiRnKqjKKbATmPSbx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5abb5f1-7406-4fda-98e7-fb538e271e28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ld5KEGy2imUEjhCh8i9F16",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6897,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6897,
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

_source line 4 · 2026-05-14T10:51:10.847Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HnWQBqpum123CPWRJWNUCe`</summary>

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
  "parentUuid": "e5abb5f1-7406-4fda-98e7-fb538e271e28",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LHiRnKqjKKbATmPSbx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "756a8da0-0cb2-4fb7-9aaf-54726294e516",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ld5KEGy2imUEjhCh8i9F16",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6897,
      "cache_read_input_tokens": 8252,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6897
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 6897,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6897,
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

_source line 5 · 2026-05-14T10:51:10.850Z_

<details><summary>↩ Tool result · `toolu_01HnWQBqpum123CPWRJWNUCe`</summary>

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
  "parentUuid": "756a8da0-0cb2-4fb7-9aaf-54726294e516",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "8651e93a-0d8b-44c6-8269-ece4fec11fea",
  "sourceToolAssistantUUID": "756a8da0-0cb2-4fb7-9aaf-54726294e516",
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

_source line 6 · 2026-05-14T10:51:14.254Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_019zzr2Sa9b6zJjnA4WqGrm6`</summary>

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
  "parentUuid": "8651e93a-0d8b-44c6-8269-ece4fec11fea",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LJ2TzM7SBhLc9A6LB9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65903725-64ee-48dd-83f2-852560385bc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMhCnzJpV6Ezu5X977hTqy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 7 · 2026-05-14T10:51:14.337Z_

<details><summary>↩ Tool result · `toolu_019zzr2Sa9b6zJjnA4WqGrm6`</summary>

```text
{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (19 个)\n\n- **llama_scierc_full_s1**: QUEUED — \n- **llama_scierc_unconstrained**: QUEUED — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_grammar_only**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_scierc_full_s2**: DONE (success) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| phase2_docred_semantic_only | Semantic-only constrained decoding 在 DocRED (96 relations, avg 5.68 valid pairs) 上的 DR 降低幅度。SciERC semantic_only DR↓24% (15.37→11.65%)，DocRED 约束更紧预期效果更明显。关键验证 Claim 3 enabling dependency：semantic_only 无法消除 RV/ET（需 grammar），证明两层互补非替代。 | — | — | — |\n| phase2_docred_unconstrained | DocRED Phase 2 unconstrained baseline — 使用与 constrained 实验完全相同的 Phase 2 pipeline 和 prompt，确保消融表 F1/violation 对比公平。预期 DR~18.7%, RV~28.9%, ET~7.5%（接近 Phase 0）。 | — | — | — |\n\n## 待处理\n- llama_docred_full_s1（排队等待 GPU）\n- llama_docred_unconstrained（排队等待 GPU）\n- llama_scierc_full_s1（排队等待 GPU）\n- llama_scierc_unconstrained（排队等待 GPU）\n\n## 近期结论\n- **phase2_docred_full_s1** (success): Grammar+Semantic 双层约束 (S1) 在 DocRED (96 relations) 上能否复现 SciERC 的 DR 消除效果 (15.37%→0.93%)？DocRED 约束更紧 (avg 5.68 valid pairs)，DR baseline 更高 (18.7%)，验证 OntoCoDec 在复杂 schema 上的泛化性。\n  [DocRED full_s1 violation report](/api/workspace-files/projects/schema_semantic_constrained_ie/artifacts/phase2_docred_full_s1/report/violation_report_docred_full_s1.json)\n- **phase2_docred_grammar_only** (success): Grammar-only constrained decoding 在 DocRED (96 relation types) 上能否消除 RV violations (28.9%) 和 ET violations (7.5%)？与 SciERC grammar_only (RV 1.4%→0%, ET 0.4%→0%) 对比，验证 grammar 层在复杂 schema 上的泛化性。\n- **mvp_phase0_docred_schema_r2** (killed): Schema-informed prompt 在 DocRED (96 relation types) 上的违规率降低幅度是否小于 SciERC (7 types)？验证约束空间越大 prompt 级干预越力不从心。（从被误杀的 mvp_phase0_docred_schema 恢复，--resume）\n\n## 趋势\n成功 12 / 负向 0 / 失败 0 / 共 13\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-16980: 无 GPU 信息\n\n## 告警\n- mvp_phase0_docred_schema_r2: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65903725-64ee-48dd-83f2-852560385bc1",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "13211861-ec6a-48f0-ba54-35c7ca7ee74c",
  "sourceToolAssistantUUID": "65903725-64ee-48dd-83f2-852560385bc1",
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

_source line 8 · 2026-05-14T10:51:14.959Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01USXUFs4GHfeW1FUCbDk23x`</summary>

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
  "parentUuid": "13211861-ec6a-48f0-ba54-35c7ca7ee74c",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LJ2TzM7SBhLc9A6LB9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25f465e5-d444-4b93-a093-87b0b72e1198",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMhCnzJpV6Ezu5X977hTqy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15149,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 15149,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1447,
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

_source line 9 · 2026-05-14T10:51:14.969Z_

<details><summary>↩ Tool result · `toolu_01USXUFs4GHfeW1FUCbDk23x`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| phase2_docred_semantic_only | Semantic-only constrained decoding 在 DocRED (96 relations, avg 5.68 valid pairs) 上的 DR 降低幅度。SciERC semantic_only DR↓24% (15.37→11.65%)，DocRED 约束更紧预期效果更明显。关键验证 Claim 3 enabling dependency：semantic_only 无法消除 RV/ET（需 grammar），证明两层互补非替代。 | — | — | — |\\n| phase2_docred_unconstrained | DocRED Phase 2 unconstrained baseline — 使用与 constrained 实验完全相同的 Phase 2 pipeline 和 prompt，确保消融表 F1/violation 对比公平。预期 DR~18.7%, RV~28.9%, ET~7.5%（接近 Phase 0）。 | — | — | — |\\n\\n## 待处理\\n- llama_docred_full_s1（排队等待 GPU）\\n- llama_docred_unconstrained（排队等待 GPU）\\n- llama_scierc_full_s1（排队等待 GPU）\\n- llama_scierc_unconstrained（排队等待 GPU）\\n\\n## 近期结论\\n- **phase2_docred_full_s1** (success): Grammar+Semantic 双层约束 (S1) 在 DocRED (96 relations) 上能否复现 SciERC 的 DR 消除效果 (15.37%→0.93%)？DocRED 约束更紧 (avg 5.68 valid pairs)，DR baseline 更高 (18.7%)，验证 OntoCoDec 在复杂 schema 上的泛化性。\\n  [DocRED full_s1 violation report](/api/workspace-files/projects/schema_semantic_constrained_ie/artifacts/phase2_docred_full_s1/report/violation_report_docred_full_s1.json)\\n- **phase2_docred_grammar_only** (success): Grammar-only constrained decoding 在 DocRED (96 relation types) 上能否消除 RV violations (28.9%) 和 ET violations (7.5%)？与 SciERC grammar_only (RV 1.4%→0%, ET 0.4%→0%) 对比，验证 grammar 层在复杂 schema 上的泛化性。\\n- **mvp_phase0_docred_schema_r2** (killed): Schema-informed prompt 在 DocRED (96 relation types) 上的违规率降低幅度是否小于 SciERC (7 types)？验证约束空间越大 prompt 级干预越力不从心。（从被误杀的 mvp_phase0_docred_schema 恢复，--resume）\\n\\n## 趋势\\n成功 12 / 负向 0 / 失败 0 / 共 13\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-16980: 无 GPU 信息\\n\\n## 告警\\n- mvp_phase0_docred_schema_r2: 已被终止 — unknown\\n\", \"total_chars\": 1767, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25f465e5-d444-4b93-a093-87b0b72e1198",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "06df7892-e908-4b76-8f21-43453947fd81",
  "sourceToolAssistantUUID": "25f465e5-d444-4b93-a093-87b0b72e1198",
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

_source line 10 · 2026-05-14T10:51:18.898Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015amtAB7gyHMj3ECRkTrnAe`</summary>

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
  "parentUuid": "06df7892-e908-4b76-8f21-43453947fd81",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LJKwxEZysDYcReWDrw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ccc8fed-6eef-47e4-bad1-399590b5c665",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5gwdHU5aCkvoYgZn3hedQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2680,
      "cache_read_input_tokens": 16596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2680,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 11 · 2026-05-14T10:51:18.910Z_

<details><summary>↩ Tool result · `toolu_015amtAB7gyHMj3ECRkTrnAe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper_framing.md\", \"content\": \"# OntoCoDec — Paper Framing\\n\\n## Target Venue\\nEMNLP 2026 (ARR submission May 25, 2026)\\n\\n## Title\\nOntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints\\n(Note: \\\"Guaranteed\\\" dropped per Reviewer — S1 DR=0.93%, S2 DR=0.97%, neither achieves 0%. \\\"Near-Complete\\\" is honest and defensible.)\\n\\n## Core Insight\\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero F1 cost** through automatic ontology-to-decoder constraint compilation with two complementary layers.\\n\\n**Phase 2 confirmed**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%), and is **F1-neutral** (R-F1 +0.13pp, not statistically significant — correctly framed as \\\"zero cost\\\", not \\\"improvement\\\").\\n\\n## Core Claims\\n\\n### Claim 1 (Empirical): Violation Landscape\\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\\n\\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\\n\\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\\n\\n### Claim 2 (Empirical): Prompt Insufficiency\\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\\n\\n**Narrative**: This is NOT about \\\"5.78% barely above 5%\\\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\\n\\n### Claim 3 (Methodological): Composable Constraint Framework\\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\\n\\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \\\"synergistic\\\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\\n\\nThe two layers compose via bitwise AND of token masks. Recommended framing: \\\"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\\\"\\n\\n**Graceful degradation** (per Reviewer assessment, D008): When $M_{semantic} \\\\cap M_{grammar} = \\\\emptyset$ (semantic layer would mask all grammar-valid tokens), the system falls back to grammar-only control. Occurred 1/998 DocRED docs (0.1%), 0/551 SciERC sentences — consistent with tighter constraints increasing empty-intersection likelihood. Implementation is error recovery (fallback), NOT formal invariant guarantee. Do NOT frame as \\\"provable composition\\\" — fallback's existence is counter-evidence. Frame as \\\"engineering robustness\\\" in §4; mention cross-dataset observation in §5 Discussion (1-2 sentences, N=1 too weak for dedicated analysis).\\n\\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\\n\\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\\n\\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\\n\\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\\n\\n## Anticipated Reviewer Concerns\\n\\n### C1: \\\"5.78% is barely above 5% — threshold is arbitrary\\\"\\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\\n\\n### C2: \\\"Why not just post-hoc filter?\\\"\\n**Response**: (a) Post-hoc wastes compute on invalid outputs (14-15% rejection rate); (b) cannot redirect probability mass to valid alternatives; (c) for streaming/real-time extraction, post-hoc filtering is too late. Post-hoc approaches (e.g., SHACL/DL reasoner-based validation, Alviano et al. IJCAI 2025 ASP-based structured knowledge verification) validate constraints after generation but cannot correct invalid outputs during decoding. ⚠️ 原引用 \\\"LLM+ASP (ICLP 2025)\\\" 已核实为不准确（venue/方法描述均有误），已修正。\\n\\n### C3: \\\"Bitwise AND of two masks is not novel\\\"\\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\\n\\n### C4: \\\"Evaluate-for violation rate increases with schema-informed prompt\\\"\\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\\\"Method X evaluates for Task Y\\\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \\\"harder instances\\\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\\n\\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\\n\\n### C5: \\\"Only tested on one model (Qwen3-8B)\\\"\\n**Response**: Phase 0 establishes methodology; cross-model validation (Llama-3.1-8B, 70B quantized) planned for Phase 2 if time permits. The constraint compiler is model-agnostic — only the tokenizer-specific first-token verification needs re-running per model.\\n\\n### C6: \\\"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\\\"\\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Phase 2 confirms F1-neutral**: S1 R-F1 0.0836 (+0.13pp vs unconstrained 0.0823), S2 R-F1 0.0803 (-0.20pp vs unconstrained). Both within noise on ~1700 triples. Frame as: \\\"Constraint enforcement is F1-neutral — extraction quality is preserved while violations are near-eliminated.\\\" Do NOT claim F1 improvement (single seed, no bootstrap CI). Note: S2 shows marginally lower F1 and fewer triples (1644 vs 1729) — two-pass does not improve quality.\\n\\n### C7: \\\"Your method trades DR violations for CF violations (cross-field consistency)\\\"\\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\\n\\n**CF 子类型分析（根因已确认）**：\\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\\n\\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\\n\\n**论证层次**：\\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\\n\\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \\\"CF 是 semantic type enforcement 的系统性副作用\\\" 提供干净的消融证据。\\n\\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\\n\\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\\n\\n### C8: \\\"Absolute F1 is too low (~8%) — results are not meaningful\\\"\\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \\\"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\\\"\\n\\n## Paper Structure (Draft)\\n1. Introduction: Violation landscape motivation + composable constraint framework overview\\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\\n5. Experiments: Constrained vs unconstrained vs post-hoc vs prompt-based\\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology)\\n7. Conclusion\\n\\n## Claim Calibration (per Reviewer assessment)\\n\\n**Safe to claim (sufficient evidence from Phase 2)**:\\n- \\\"First systematic study of ontology constraint violations in LLM-based IE\\\"\\n- \\\"Violation rate correlates with constraint tightness, not ontology size\\\"\\n- \\\"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\\\" ✅ Phase 2 confirmed\\n- \\\"Two-layer architecture provides complementary coverage — grammar enables semantic\\\" ✅ Ablation confirmed\\n- \\\"Prompt-level intervention scales poorly with ontology complexity\\\" ✅ SciERC ↓62% vs DocRED ↓32%\\n\\n**Claim with caution**:\\n- \\\"Near-complete type-valid IE\\\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \\\"Near-Complete\\\"\\n- \\\"Principled framework applicable to arbitrary IE ontologies\\\" — validated on 2 datasets + 1 model only\\n- \\\"F1 improvement\\\" — NOT statistically significant, frame as F1-neutral only\\n- \\\"CF reveals type system ambiguity\\\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\\\"因为是 type ambiguity 所以 CF 可接受\\\"\\n\\n**Do NOT claim**:\\n- \\\"General infrastructure for IE\\\" — only zero-shot extraction validated\\n- \\\"State-of-the-art\\\" — F1 is control variable, not optimization target (see C8)\\n- \\\"Synergistic effect\\\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\\n- \\\"S2 solves CF\\\" or \\\"S2 mitigates Structure Snowballing\\\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\\n- \\\"Pilot50 DR=0%\\\" — small-sample artifact, full S2 has DR=0.97%\\n- \\\"Grammar-first invariant\\\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\\n- \\\"Robust dual-layer composition across schema complexities\\\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\\n\\n## Risk Ranking (ordered by reject probability)\\n\\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\\n2. **Single model limitation** (MEDIUM-HIGH): Only Qwen3-8B tested. Mitigation: Llama-3.1-8B cross-model validation if time permits.\\n3. **Novelty perception** (MEDIUM): \\\"PLDI'25 for code → OntoCoDec for IE\\\" attack line. Must argue IE constraint structure differs fundamentally.\\n4. **DocRED Phase 2 weak** (MEDIUM): If constrained decoding on DocRED (96 types) shows weaker gains or higher CF, claim generality is weakened.\\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral. No longer a risk.\\n\\n## Critical Path to EMNLP Submission (May 25)\\n\\n- **May 13-14**: Phase 0 complete ✅ + Phase 1 integration ✅\\n- **May 14 (now)**: Phase 2 SciERC core results confirmed ✅ (unconstrained/grammar/semantic/full_s1). full_s2 running, DocRED Phase 2 starting.\\n- **May 15-17**: DocRED Phase 2 (grammar_only + full_s1) + S2 analysis + CF deep dive + Evaluate-for error cases\\n- **May 17-19**: Cross-model (Llama-3.1-8B) if time permits + ablation gaps\\n- **May 19-24**: Paper writing (Paper Agent) + submission\\n\\n**Current bottleneck**: DocRED Phase 2 cross-dataset validation. GPU 0 should be running DocRED grammar_only NOW.\\n\\n## Status\\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\\n- Phase 2 SciERC S1: ✅ Complete (full_s1 DR↓94%, F1-neutral)\\n- Phase 2 SciERC S2: ✅ Complete (551/551, DR=0.97%, CF=8.03%, R-F1=8.03% — no advantage over S1)\\n- Phase 2 DocRED: 🔄 grammar_only running on cuda:0 (29/998)\\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9%, S2 8.03%, both from independent per-relation enforcement)\\n\", \"total_chars\": 16503, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ccc8fed-6eef-47e4-bad1-399590b5c665",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "72a9a111-9d32-4dde-aef6-7e9d4dd53ebb",
  "sourceToolAssistantUUID": "9ccc8fed-6eef-47e4-bad1-399590b5c665",
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

_source line 12 · 2026-05-14T10:51:19.859Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KNSrLstjCTPtHPBoqLHb2J`</summary>

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
  "parentUuid": "72a9a111-9d32-4dde-aef6-7e9d4dd53ebb",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LJKwxEZysDYcReWDrw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9307e1ec-431c-470a-89cd-fc8190b9564a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5gwdHU5aCkvoYgZn3hedQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2680,
      "cache_read_input_tokens": 16596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2680,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 13 · 2026-05-14T10:51:19.868Z_

<details><summary>↩ Tool result · `toolu_01KNSrLstjCTPtHPBoqLHb2J`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9307e1ec-431c-470a-89cd-fc8190b9564a",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "090ad175-4393-489e-9241-f02d312746e3",
  "sourceToolAssistantUUID": "9307e1ec-431c-470a-89cd-fc8190b9564a",
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

_source line 14 · 2026-05-14T10:51:20.421Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018bGCXMQeUhWpKvXyuWymEU`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "090ad175-4393-489e-9241-f02d312746e3",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LJKwxEZysDYcReWDrw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6393c76f-933e-427c-9d89-90d4d38a2235",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5gwdHU5aCkvoYgZn3hedQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2680,
      "cache_read_input_tokens": 16596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2680,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 15 · 2026-05-14T10:51:20.437Z_

<details><summary>↩ Tool result · `toolu_018bGCXMQeUhWpKvXyuWymEU`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6393c76f-933e-427c-9d89-90d4d38a2235",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "7a6373b7-e42f-4a05-b36b-5470b9967e08",
  "sourceToolAssistantUUID": "6393c76f-933e-427c-9d89-90d4d38a2235",
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

_source line 16 · 2026-05-14T10:51:20.867Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CQ24zY9XmjeukvuabJtX6C`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a6373b7-e42f-4a05-b36b-5470b9967e08",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LJKwxEZysDYcReWDrw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47340d4d-e6fa-4db3-b218-4596b5b3a191",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5gwdHU5aCkvoYgZn3hedQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2680,
      "cache_read_input_tokens": 16596,
      "output_tokens": 392,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2680
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 392,
          "cache_read_input_tokens": 16596,
          "cache_creation_input_tokens": 2680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2680,
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

_source line 17 · 2026-05-14T10:51:20.885Z_

<details><summary>↩ Tool result · `toolu_01CQ24zY9XmjeukvuabJtX6C`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026\\n  track: long paper (ARR)\\n  template: \\\"\\\"\\n  template_note: \\\"本地无 EMNLP/ACL 模板。Worker 需下载 ACL 2023 rolling review 模板（acl2023.sty）到 templates/latex/emnlp2026/，或直接用 ARR 官方 Overleaf 模板。\\\"\\n  page_limit: 8  # + unlimited references + appendix\\n  deadline: 2026-05-25\\n  core_claim: >\\n    LLM-based IE 系统存在系统性 ontology constraint violations（15-19% per-triple），\\n    prompt-level 干预统计有效但 per-relation 不可靠（甚至恶化），OntoCoDec 通过\\n    grammar+semantic 双层 compiled constrained decoding 实现 94% DR reduction 且 F1-neutral。\\n  title: \\\"OntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints\\\"\\n  created_at: 2026-05-14T12:00:00Z\\n  approved_at: 2026-05-14\\n  director_adjustments:\\n    - \\\"tab2+tab3 合并为一张 cross-dataset prompt comparison 表\\\"\\n    - \\\"tab4_s1_vs_s2 + fig3_ablation_layers 移至 Appendix\\\"\\n    - \\\"§5.3 S1 vs S2 在 main text 仅 1-2 句提及，详见 Appendix\\\"\\n    - \\\"Main text: tab1 + tab2_merged + tab5 + tab6 = 4 tables; fig1 + fig2 = 2 figures\\\"\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 250\\n    core_bullets:\\n      - \\\"问题：LLM-based IE 系统在 zero-shot 设置下系统性违反 ontology type constraints（SciERC 15.4%, DocRED 18.7% per-triple DR violation）\\\"\\n      - \\\"Prompt 不够：Schema-informed prompting 降低 62% violation 但 per-relation 不可靠，Evaluate-for 反而恶化 +5.8pp\\\"\\n      - \\\"方法：OntoCoDec 自动编译 IE ontology 为两层约束——grammar（JSON+vocabulary via XGrammar）+ semantic（cross-field domain/range via stateful entity registry + logit masking），bitwise AND 组合\\\"\\n      - \\\"结果：SciERC DR 15.37%→0.93%（↓94%），ET/RV→0%，F1-neutral（+0.13pp）\\\"\\n      - \\\"Limitation flag：CF violation 9.9% 作为 per-relation independent enforcement 的固有 trade-off\\\"\\n    dependencies: [experiments, method]\\n    tables: []\\n    figures: []\\n    registry_refs: [phase2_scierc_unconstrained, phase2_scierc_full_s1, mvp_phase0_scierc_schema]\\n\\n  - section: introduction\\n    word_budget: 1200\\n    core_bullets:\\n      - \\\"Hook: LLM 在 SciERC 上 42% 的 Compare 关系三元组违反 domain/range 约束——即使模型能正确提取实体和关系名，生成的三元组在 ontology 中是非法的\\\"\\n      - \\\"Gap: 现有 constrained decoding for IE 止步于 syntactic/vocabulary 层（GCD, AdaKGC, XGrammar）；semantic type constraints（domain/range）仅 post-hoc 验证（ODKE+, OntoLogX）或限于代码生成（PLDI'25, MGD）\\\"\\n      - \\\"Insight: IE ontology constraints 有 decidability hierarchy——entity type ∈ vocab 是 purely local（grammar 可解），relation argument types 兼容 domain/range 是 prefix-decidable with state（需 entity registry），forward coreference 是 truly non-local（超出 forward-only decoding 范围）\\\"\\n      - \\\"Mechanism: OntoCoDec 自动编译 ontology schema 为两层 token-level constraints，grammar 层确保结构有效性从而 enable semantic 层做 domain/range enforcement\\\"\\n      - \\\"Contributions: [C1] 首个系统性 violation landscape 研究——violation rate 由 constraint tightness 驱动而非 ontology size；[C2] OntoCoDec compiled constrained decoding framework with decidability taxonomy；[C3] 94% DR reduction at zero F1 cost 的实证验证\\\"\\n    dependencies: [experiments]\\n    citation_hints:\\n      - \\\"SciERC dataset: Luan et al. 2018\\\"\\n      - \\\"DocRED dataset: Yao et al. 2019\\\"\\n      - \\\"XGrammar: cite framework\\\"\\n      - \\\"GCD for IE: Geng et al. EMNLP 2023\\\"\\n      - \\\"PLDI'25 type-constrained code gen\\\"\\n      - \\\"ODKE+ Apple 2025\\\"\\n    figures: [fig1_overview]\\n    tables: []\\n    registry_refs: [mvp_phase0_violation_rate, phase2_scierc_full_s1]\\n\\n  - section: background\\n    word_budget: 600\\n    core_bullets:\\n      - \\\"IE ontology structure：entity types E, relation types R, domain/range mapping σ: R→P(E×E)\\\"\\n      - \\\"Grammar-constrained decoding：CFG/JSON Schema → token mask → autoregressive enforcement（XGrammar）\\\"\\n      - \\\"Problem statement：给定 ontology O=(E,R,σ) 和 LLM M，编译 O 为 decoding-time constraints 使输出满足 type validity\\\"\\n    dependencies: []\\n    citation_hints:\\n      - \\\"XGrammar framework\\\"\\n      - \\\"Outlines/SGLang for grammar decoding context\\\"\\n    figures: []\\n    tables: []\\n    registry_refs: []\\n\\n  - section: violation_landscape\\n    word_budget: 1200\\n    core_bullets:\\n      - \\\"§3.1 实验设置：SciERC（7 relations, avg 26.1 valid pairs）+ DocRED（96 relations, avg 5.68 valid pairs），Qwen3-8B zero-shot，4 类 violation metrics（DR/RV/ET/CF）\\\"\\n      - \\\"§3.2 Violation 分布：SciERC DR=15.37%，DocRED DR=18.70%——comparable rates despite 14× ontology size difference → violation 由 constraint tightness 驱动\\\"\\n      - \\\"§3.3 Per-relation analysis：Compare 42.4%, Feature-of 33.5% vs Used-for 0.76% vs Conjunction 0%——tight constraints（few valid type pairs）→ high violation\\\"\\n      - \\\"§3.4 Prompt insufficiency：Schema-informed prompting SciERC ↓62.4% 但 DocRED 仅 ↓31.3%；per-relation：Evaluate-for 反而恶化 +5.8pp（prior-constraint conflict）\\\"\\n      - \\\"Standalone contribution：即使不用 OntoCoDec，violation landscape 本身是对 LLM IE 可靠性的系统性分析\\\"\\n    dependencies: []\\n    citation_hints:\\n      - \\\"SciERC: Luan et al. 2018\\\"\\n      - \\\"DocRED: Yao et al. 2019\\\"\\n      - \\\"Qwen3: cite model\\\"\\n    figures: [fig2_per_relation_dr]\\n    tables: [tab2_prompt_cross_dataset]  # merged tab2+tab3\\n    registry_refs: [mvp_phase0_violation_rate, mvp_phase0_scierc_schema, mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema]\\n\\n  - section: method\\n    word_budget: 1500\\n    core_bullets:\\n      - \\\"§4.1 Decidability taxonomy：(a) purely local（entity/relation type ∈ vocab）→ grammar layer；(b) prefix-decidable with state（domain/range compatibility）→ semantic layer；(c) truly non-local（forward coreference）→ out of scope\\\"\\n      - \\\"§4.2 Grammar layer：Ontology O → JSON Schema（enum entity_types, enum relation_types, array structure）→ XGrammar CFG → per-token mask M_g\\\"\\n      - \\\"§4.3 Semantic layer（TypeConstraintProcessor）：stateful entity registry tracking (entity_name → entity_type) as entities are generated；relation field → lookup valid domain/range pairs → dynamic logit mask M_s\\\"\\n      - \\\"§4.4 Composition：M_final = M_g ∧ M_s（bitwise AND）。Grammar 是 semantic 的 enabling prerequisite：无 grammar 保证，semantic 层遇 unknown relation type 无法查 domain/range rules\\\"\\n      - \\\"§4.4 内附 Grammar-First Invariant（1-2 句设计原则，不升级为独立 claim）：'We enforce a grammar-first invariant: the semantic mask is applied only when it preserves at least one grammar-valid token, falling back to grammar-only otherwise.' 强化 enabling dependency 论点——grammar 既是 vocabulary prerequisite 也是 safety net。\\\"\\n      - \\\"§4.5 S1 single-pass strategy（主推）。S2 two-pass variant 见 Appendix\\\"\\n    dependencies: []\\n    citation_hints:\\n      - \\\"XGrammar for grammar compilation\\\"\\n      - \\\"Synchromesh NeurIPS'22 for CSD concept\\\"\\n      - \\\"PLDI'25 for prefix automata analogy\\\"\\n    figures: [fig1_overview]\\n    tables: []\\n    registry_refs: []\\n    notation_table:\\n      O: \\\"ontology (E, R, σ)\\\"\\n      E: \\\"set of entity types\\\"\\n      R: \\\"set of relation types\\\"\\n      σ: \\\"domain/range mapping R → P(E×E)\\\"\\n      M_g: \\\"grammar layer token mask\\\"\\n      M_s: \\\"semantic layer token mask\\\"\\n\\n  - section: experiments\\n    word_budget: 2000\\n    core_bullets:\\n      - \\\"§5.1 Setup：SciERC test（551 sentences），DocRED dev（998 docs），Qwen3-8B，4 decoding modes（unconstrained/grammar/semantic/full_s1），metrics（DR/RV/ET/CF/R-F1/E-F1）\\\"\\n      - \\\"§5.2 Main results（tab1）：Full S1 DR↓94%（15.37→0.93），ET/RV→0%，R-F1 +0.13pp（F1-neutral）。Grammar alone 消除 ET/RV 但不影响 DR；Semantic alone ↓24% DR 但无法消除 ET/RV → grammar 是 semantic 的前置条件\\\"\\n      - \\\"§5.3 S1 vs S2：1-2 句提及 'We also evaluate a two-pass variant (S2); results comparable to S1, details in Appendix A'\\\"\\n      - \\\"§5.4 Cross-dataset（DocRED, tab6）：Phase 0 prompt comparison + Phase 2 constrained results [TODO if available]\\\"\\n      - \\\"§5.3 CF Analysis（tab5，双位置之一：finding）：CF 100% 由 semantic 层引入（grammar CF=0.08%=unconstrained，干净消融证据）。根因是 EVR（entity-vs-relation type drift）>90%，top 冲突 Generic↔OtherScientificTerm——揭示 type system 语义边界模糊性，per-relation independent enforcement 暴露 ontology 中隐藏歧义。⚠️ 禁止 framing 为 'CF is inherent type ambiguity therefore acceptable'——正确 framing：'CF analysis reveals non-obvious type ambiguity patterns (finding), but 9.9% CF remains an open challenge for practical deployment (limitation)'\\\"\\n      - \\\"§5.x Limitation paragraph：CF=9.9% 明确列为 open problem；single model（Qwen3-8B）；zero-shot only；residual DR on Evaluate-for（5.76%）\\\"\\n    dependencies: []\\n    citation_hints:\\n      - \\\"SciERC: Luan et al. 2018\\\"\\n      - \\\"DocRED: Yao et al. 2019\\\"\\n    figures: [fig2_per_relation_dr]  # fig3 moved to appendix\\n    tables: [tab1_main_results, tab5_cf_analysis, tab6_docred_constrained]  # tab4 moved to appendix\\n    registry_refs:\\n      - phase2_scierc_unconstrained\\n      - phase2_scierc_grammar_only\\n      - phase2_scierc_semantic_only\\n      - phase2_scierc_full_s1\\n      - phase2_scierc_full_s2\\n      - mvp_phase0_violation_rate_docred\\n      - mvp_phase0_docred_schema\\n      - phase2_docred_grammar_only  # [TODO: RUNNING]\\n      - phase2_docred_full_s1  # [TODO: RUNNING]\\n\\n  - section: related_work\\n    word_budget: 800\\n    core_bullets:\\n      - \\\"Cluster 1 — Constrained decoding for IE：GCD (EMNLP'23), AdaKGC (EMNLP'23), GoLLIE (ICLR'24) 止步 syntactic/vocabulary 层，不做 cross-field semantic constraints → OntoCoDec 补充 semantic 层\\\"\\n      - \\\"Cluster 2 — Semantic constrained decoding (code gen)：Synchromesh (NeurIPS'22), MGD (NeurIPS'23), PLDI'25 在代码生成中做 type checking → OntoCoDec 将同一思路迁移到 IE ontology\\\"\\n      - \\\"Cluster 3 — Ontology-guided IE：ODKE+ (Apple'25), OntoLogX ('25), SPIRES ('24) 用 ontology 指导 IE 但 post-hoc enforcement → OntoCoDec 在 decode-time prevent violations\\\"\\n      - \\\"Cluster 4 — Type constraint enforcement (pre-LLM)：Roth & Yih (AAAI'04) ILP, KnowCoder (ACL'24) hierarchy → OntoCoDec 在 autoregressive decoding 中实现类似保证\\\"\\n      - \\\"Cluster 5 — Constrained decoding risks：CRANE (ICML'25), Grammar-Aligned (NeurIPS'24), Hidden Cost (RANLP'25) → OntoCoDec 的 F1-neutral 结果回应此顾虑\\\"\\n    dependencies: [introduction]\\n    citation_hints:\\n      - \\\"见 literature_map.yaml must_cite 列表\\\"\\n    figures: []\\n    tables: []\\n    registry_refs: []\\n\\n  - section: conclusion\\n    word_budget: 400\\n    core_bullets:\\n      - \\\"Summary：OntoCoDec 通过 compiled ontology constraints 实现 near-complete type-valid IE（DR↓94%，F1-neutral）\\\"\\n      - \\\"Key insight：violation rate 由 constraint tightness 驱动，grammar 层是 semantic 层的 enabling prerequisite\\\"\\n      - \\\"Limitations（双位置之二：open problem）：CF=9.9% 作为 open challenge 明确列出——per-relation independent enforcement 的系统性副作用，practical deployment 需解决。Single model（Qwen3-8B）；zero-shot only。⚠️ 不能只有 §5 finding 没有 §7 limitation\\\"\\n      - \\\"Future work：global entity-type consensus during decoding（解决 CF）；cross-model validation；fine-tuned model integration\\\"\\n    dependencies: [experiments, method]\\n    tables: []\\n    figures: []\\n    registry_refs: []\\n\\n  - section: appendix\\n    word_budget: 1500\\n    core_bullets:\\n      - \\\"Appendix A — S1 vs S2 decoding strategies：tab4_s1_vs_s2 + fig3_ablation_layers + detailed analysis\\\"\\n      - \\\"Appendix B — Per-relation detailed breakdowns（all 7 SciERC relations across all modes）\\\"\\n      - \\\"Appendix C — Prompt templates（minimal vs schema-informed）\\\"\\n      - \\\"Appendix D — DocRED ontology statistics\\\"\\n    dependencies: [experiments]\\n    tables: [tab4_s1_vs_s2]\\n    figures: [fig3_ablation_layers]\\n    registry_refs: [phase2_scierc_full_s1, phase2_scierc_full_s2]\\n\\nvisualization_plan:\\n  # Main text figures\\n  - fig_id: fig1_overview\\n    type: conceptual\\n    tool: matplotlib\\n    description: >\\n      OntoCoDec 架构总览图。左侧：Ontology Schema（entity types, relation types, domain/range rules）。\\n      中间：Compiler 将 schema 编译为两层约束——上层 Grammar Layer（JSON Schema → XGrammar CFG → M_g），\\n      下层 Semantic Layer（domain/range rules → TypeConstraintProcessor with entity registry → M_s）。\\n      右侧：LLM decoding 过程，每步 logits 经 M_g ∧ M_s masking 后 sampling。\\n      底部注明 S1（single-pass）为主策略。\\n    placement: introduction\\n    aspect_ratio: \\\"16:9\\\"\\n    data_source: \\\"manual\\\"\\n\\n  - fig_id: fig2_per_relation_dr\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Grouped bar chart：7 个 SciERC relation types（x 轴），每个有 4 个 bar\\n      （unconstrained / grammar_only / semantic_only / full_s1），\\n      y 轴为 DR violation rate (%)。展示 full_s1 在所有 relation 上 near-zero，\\n      而 unconstrained 在 tight-constraint relations 上高 violation。\\n      辅助线标 5% threshold。按 unconstrained violation rate 降序排列 relations。\\n    placement: experiments\\n    aspect_ratio: \\\"3:1\\\"\\n    data_source: \\\"registry: phase2_scierc_unconstrained, phase2_scierc_grammar_only, phase2_scierc_semantic_only, phase2_scierc_full_s1\\\"\\n\\n  # Appendix figures\\n  - fig_id: fig3_ablation_layers\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Heatmap：4 种 violation types（DR/RV/ET/CF）× 4 decoding modes\\n      （unconstrained/grammar/semantic/full_s1），展示每层约束消除哪些\\n      violation types。突出 grammar 消除 RV+ET、semantic+grammar 消除 DR、CF 作为 trade-off。\\n    placement: appendix\\n    aspect_ratio: \\\"4:3\\\"\\n    data_source: \\\"registry: phase2_scierc_unconstrained, phase2_scierc_grammar_only, phase2_scierc_semantic_only, phase2_scierc_full_s1\\\"\\n\\ntable_plan:\\n  # Main text tables (4 tables)\\n  - table_id: tab1_main_results\\n    caption: \\\"SciERC constrained decoding results. DR/RV/ET/CF are per-triple violation rates (↓). R-F1/E-F1 are extraction F1 scores.\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Mode, DR(%), RV(%), ET(%), CF(%), R-F1, E-F1]\\n    data_source: \\\"registry: phase2_scierc_unconstrained, phase2_scierc_grammar_only, phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2\\\"\\n    notes: \\\"加粗 full_s1 行。S2 行可保留以做 inline comparison。\\\"\\n    baseline_row: \\\"unconstrained\\\"\\n\\n  - table_id: tab2_prompt_cross_dataset\\n    caption: \\\"Cross-dataset prompt-level intervention. Schema-informed prompting reduces violations but scales poorly with ontology complexity.\\\"\\n    placement: violation_landscape\\n    type: comparison\\n    columns: [Dataset, \\\"|R|\\\", \\\"Avg Valid Pairs\\\", Prompt, DR(%), RV(%), ET(%), \\\"DR Reduction\\\"]\\n    data_source: \\\"registry: mvp_phase0_violation_rate, mvp_phase0_scierc_schema, mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema\\\"\\n    notes: \\\"合并原 tab2+tab3。突出 SciERC ↓62% vs DocRED ↓31%。\\\"\\n\\n  - table_id: tab5_cf_analysis\\n    caption: \\\"Cross-field consistency violation analysis. CF is 100% introduced by the semantic layer.\\\"\\n    placement: experiments\\n    type: statistics\\n    columns: [Mode, \\\"CF(%)\\\", \\\"EVR entities\\\", \\\"EVR rate\\\", \\\"Top conflict pattern\\\"]\\n    data_source: \\\"registry: phase2_scierc_unconstrained, phase2_scierc_grammar_only, phase2_scierc_full_s1, phase2_scierc_full_s2\\\"\\n    notes: \\\"数据部分来自 CF 根因分析脚本输出\\\"\\n\\n  - table_id: tab6_docred_constrained\\n    caption: \\\"Cross-dataset validation: Constrained decoding results on DocRED (96 relation types).\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Mode, DR(%), RV(%), ET(%), R-F1]\\n    data_source: \\\"registry: mvp_phase0_violation_rate_docred, phase2_docred_grammar_only, phase2_docred_full_s1\\\"\\n    notes: \\\"[TODO] DocRED Phase 2 实验运行中，数据到后 Patch 填入\\\"\\n\\n  # Appendix tables\\n  - table_id: tab4_s1_vs_s2\\n    caption: \\\"S1 (single-pass) vs S2 (two-pass) decoding strategies on SciERC.\\\"\\n    placement: appendix\\n    type: ablation\\n    columns: [Strategy, DR(%), CF(%), R-F1, E-F1, Triples]\\n    data_source: \\\"registry: phase2_scierc_full_s1, phase2_scierc_full_s2\\\"\\n    baseline_row: \\\"S1 (recommended)\\\"\\n    notes: \\\"S2 无优势，定位为 architectural variant。\\\"\\n\\nliterature_strategy:\\n  citation_budget: 35\\n  macro_context:\\n    - \\\"constrained decoding for structured generation\\\"\\n    - \\\"ontology-guided information extraction\\\"\\n    - \\\"type constraint enforcement in NLP/IE\\\"\\n  micro_clusters:\\n    - cluster_name: \\\"constrained_decoding_for_ie\\\"\\n      search_queries:\\n        - \\\"constrained decoding information extraction 2024 2025\\\"\\n        - \\\"grammar-constrained generation NER relation extraction\\\"\\n      must_cite:\\n        - \\\"Geng et al. EMNLP 2023 (GCD)\\\"\\n        - \\\"AdaKGC EMNLP 2023\\\"\\n        - \\\"GoLLIE ICLR 2024\\\"\\n      target_count: 5\\n\\n    - cluster_name: \\\"semantic_constrained_decoding\\\"\\n      search_queries:\\n        - \\\"semantic constrained decoding type checking 2024 2025\\\"\\n        - \\\"type-constrained code generation LLM\\\"\\n      must_cite:\\n        - \\\"Synchromesh NeurIPS 2022\\\"\\n        - \\\"MGD NeurIPS 2023\\\"\\n        - \\\"PLDI 2025 type-constrained code gen\\\"\\n        - \\\"CRANE ICML 2025\\\"\\n        - \\\"Grammar-Aligned Decoding NeurIPS 2024\\\"\\n      target_count: 6\\n\\n    - cluster_name: \\\"ontology_guided_ie\\\"\\n      search_queries:\\n        - \\\"ontology-guided LLM knowledge extraction 2024 2025\\\"\\n        - \\\"schema-guided information extraction\\\"\\n      must_cite:\\n        - \\\"ODKE+ Apple 2025\\\"\\n        - \\\"SPIRES/OntoGPT Bioinformatics 2024\\\"\\n        - \\\"OntoLogX 2025\\\"\\n        - \\\"KnowCoder ACL 2024\\\"\\n      target_count: 6\\n\\n    - cluster_name: \\\"type_constraint_enforcement\\\"\\n      search_queries:\\n        - \\\"type constraint entity relation extraction\\\"\\n        - \\\"domain range constraint knowledge graph\\\"\\n      must_cite:\\n        - \\\"Roth & Yih 2004\\\"\\n      target_count: 3\\n\\n    - cluster_name: \\\"constrained_decoding_frameworks\\\"\\n      search_queries:\\n        - \\\"XGrammar grammar-guided generation\\\"\\n        - \\\"structured output LLM framework\\\"\\n      must_cite:\\n        - \\\"XGrammar 2024\\\"\\n      target_count: 2\\n\\n    - cluster_name: \\\"constrained_decoding_risks\\\"\\n      search_queries:\\n        - \\\"constrained decoding quality degradation 2024 2025\\\"\\n        - \\\"structured output hidden cost\\\"\\n      must_cite:\\n        - \\\"Hidden Cost RANLP 2025\\\"\\n      target_count: 3\\n\\n    - cluster_name: \\\"datasets_and_baselines\\\"\\n      search_queries: []\\n      must_cite:\\n        - \\\"SciERC Luan et al. 2018\\\"\\n        - \\\"DocRED Yao et al. 2019\\\"\\n        - \\\"EKAW 2024 ontology-constrained beam\\\"\\n      target_count: 4\\n\\nwriting_order:\\n  - experiments\\n  - method\\n  - violation_landscape\\n  - introduction\\n  - related_work\\n  - abstract\\n  - conclusion\\n  - appendix\\n\", \"total_chars\": 17380, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47340d4d-e6fa-4db3-b218-4596b5b3a191",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "813a1a41-5e7a-45bc-b72d-63646e713423",
  "sourceToolAssistantUUID": "47340d4d-e6fa-4db3-b218-4596b5b3a191",
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

_source line 18 · 2026-05-14T10:51:23.756Z_

Now let me read the actual paper artifacts and key experimental results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "813a1a41-5e7a-45bc-b72d-63646e713423",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LJm7XraJgZBM566NWh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9127f7a1-9826-485f-8238-e3f7f1b2bb73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014D3jQrjwMxaHgKh3gw8sKE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13632,
      "cache_read_input_tokens": 19276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13632,
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

_source line 19 · 2026-05-14T10:51:26.331Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PuKqRcbHwmVjfHyZ9oQ9AR`</summary>

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
  "parentUuid": "9127f7a1-9826-485f-8238-e3f7f1b2bb73",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LJm7XraJgZBM566NWh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f4bb60d-bb38-4f55-8f99-6294b2a7e938",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014D3jQrjwMxaHgKh3gw8sKE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13632,
      "cache_read_input_tokens": 19276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13632,
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

_source line 20 · 2026-05-14T10:51:26.348Z_

<details><summary>↩ Tool result · `toolu_01PuKqRcbHwmVjfHyZ9oQ9AR`</summary>

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
  "parentUuid": "8f4bb60d-bb38-4f55-8f99-6294b2a7e938",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "0a0aee12-a935-4200-ac46-9e5ffe3a6c19",
  "sourceToolAssistantUUID": "8f4bb60d-bb38-4f55-8f99-6294b2a7e938",
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

_source line 21 · 2026-05-14T10:51:27.172Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017P5NRyXdYh3VSzSY6kcRoe`</summary>

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
  "parentUuid": "0a0aee12-a935-4200-ac46-9e5ffe3a6c19",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LJm7XraJgZBM566NWh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "013d4f86-2fea-4991-8ed5-2562d02c152a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014D3jQrjwMxaHgKh3gw8sKE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13632,
      "cache_read_input_tokens": 19276,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13632,
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

_source line 22 · 2026-05-14T10:51:27.187Z_

<details><summary>↩ Tool result · `toolu_017P5NRyXdYh3VSzSY6kcRoe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/ROADMAP.md\", \"content\": \"# schema_semantic_constrained_ie — Research Dashboard\\n\\n> 最后更新: 2026-05-14 06:19 UTC | 更新原因: Reviewer 实测时间线修正 + D009 cross-model 升级为 should-have\\n\\n## 核心方向\\nSchema-semantic constrained decoding for information extraction：利用 ontology schema 在 LLM 解码时施加 grammar + semantic 双层约束，近乎消除 domain/range 违规且不损失 F1。详见 paper_framing.md。\\n\\n## 当前进展\\n**阶段**: Research — Phase 2 SciERC 完成，DocRED 跨数据集验证中 + 论文写作并行\\n**投稿目标**: EMNLP 2026 ARR May 25 | 内部初稿 DDL May 19（距今 5 天）\\n\\n**SciERC Phase 2 核心结果**（全部完成）：\\n- Full S1 (grammar+semantic): DR 15.37%→0.93% (↓94%), R-F1 +0.13pp, ET/RV→0% ← **主推策略**\\n- Full S2 (two-pass): 降级为 ablation (D007)\\n- Grammar only / Semantic only: 两层互补确认\\n\\n**DocRED Phase 2**（4 实验消融）：\\n- grammar_only: RUNNING cuda:0 (653/998, ~20s/doc, 预计 May 14 ~17:00 UTC)\\n- full_s1: RUNNING cuda:1 (568/998, 预计 May 14 ~16:30 UTC)\\n- semantic_only + unconstrained: QUEUED → 预计 May 14 晚至 May 15 凌晨完成\\n- **全部 4 实验预计 May 15 早间就绪**（Reviewer 实测，比初估提前 2-3 天）\\n\\n**Cross-model 验证** (D009, should-have)：\\n- Llama-3.1-8B SciERC: unconstrained + full_s1（2 组，4-6 GPU·h）\\n- 安排在 DocRED 完成后 (May 15)，预计 May 15-16 完成\\n\\n**论文写作进度**：\\n- ✅ §1 Intro, §4 Method, §4.x Composition, §5 SciERC, §6 RelWork, Tables×4, Figs×3\\n- ✅ §2 Background（3 subsections, ~580 words）\\n- ✅ §3 Violation Landscape（4 subsections, per-relation + prompt insufficiency）\\n- ✅ .bib 全部完成（RelWork 9篇 + 新论文 9篇，WebSearch 验证）\\n- ✅ Abstract 初稿（~231 words, DocRED placeholder）\\n- ✅ §7 Conclusion 初稿（~400 words, DocRED placeholder）\\n- ❌ §5 DocRED subsection（等实验结果 → 填 placeholder）\\n- ❌ §5 Cross-model（等 Llama 结果）\\n- May 18-19: 全文校对 + 一致性 → May 19 内部稿\\n\\n## 近期任务\\n- [ ] DocRED grammar_only + full_s1 完成 → 立即提交 QUEUED 两个\\n- [ ] §2 Background + §3 Violation Landscape 完成\\n- [ ] .bib 完成 + 引用验证\\n- [ ] DocRED 4 实验全部完成 → §5 DocRED subsection\\n- [ ] Llama-3.1-8B SciERC 环境准备 + 2 组实验 (D009)\\n- [ ] §5 Cross-model subsection\\n- [ ] Abstract + §7 Conclusion\\n- [ ] experiment_plan.yaml 补全（低优先级，提交前）\\n- [ ] 全文校对 + 一致性检查\\n\\n## GPU 预算\\n- 分配: westd-16980 cuda:0 + cuda:1 (2× GPU)\\n- 当前: 2/2 满载（grammar_only + full_s1）\\n- 预计释放: May 14 ~17:00 UTC → 立即接 QUEUED\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D009 | 2026-05-14 | Llama-3.1-8B cross-model 验证升级为 should-have，SciERC- | phase2_scierc_full_s1, phase2_scierc_unconstrained |\\n| D008 | 2026-05-14 | 补跑 DocRED semantic_only 完成跨数据集全消融；论文写作提前至 DocRED 分 | phase2_docred_grammar_only, phase2_docred_full_s1, phase2_scierc_semantic_only |\\n| D007 | 2026-05-14 | S2 降级为架构 ablation，S1 为主推策略；标题去掉 \\\"Guaranteed\\\" 改 \\\"Ne | phase2_scierc_full_s2, phase2_scierc_full_s1 |\\n| D006 | 2026-05-14 | Phase 2 SciERC 核心结果确认：Full S1 DR -94% 且 F1 无损，CF v | phase2_scierc_unconstrained, phase2_scierc_grammar_only, phase2_scierc_semantic_only, phase2_scierc_full_s1, mvp_phase0_docred_schema |\\n| D005 | 2026-05-14 | Phase 2 SciERC 核心结果确认：Full S1 DR↓94% F1无损，CF viola | phase2_scierc_unconstrained, phase2_scierc_grammar_only, phase2_scierc_semantic_only, phase2_scierc_full_s1 |\\n| D004 | 2026-05-14 | Phase 2 SciERC 核心结果确认：grammar+semantic (full_s1) D | phase2_scierc_unconstrained, phase2_scierc_grammar_only, phase2_scierc_semantic_only, phase2_scierc_full_s1 |\\n| D003 | 2026-05-13 | MVP 通过，进入 Research 阶段，立即启动 Phase 2 constrained dec | mvp_phase0_violation_rate, mvp_phase0_scierc_schema, mvp_phase0_violation_rate_docred |\\n| D002 | 2026-05-13 | SciERC Phase 0 结果确认 GO — domain_range violation ra | mvp_phase0_violation_rate |\\n| D001 | 2026-05-13 | 主目标调整为 EMNLP 2026 ARR (5/25), AAAI 2027 为后备 | — |\\n\\n\\n\", \"total_chars\": 3432, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "013d4f86-2fea-4991-8ed5-2562d02c152a",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "5f2faf56-fa2a-4c01-a00d-45c7b7717d21",
  "sourceToolAssistantUUID": "013d4f86-2fea-4991-8ed5-2562d02c152a",
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

_source line 23 · 2026-05-14T10:51:27.456Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019XMvxCr7SyC728FJ49NpFU`</summary>

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
  "parentUuid": "5f2faf56-fa2a-4c01-a00d-45c7b7717d21",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LJm7XraJgZBM566NWh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "634d61f9-c524-4bb4-9ff5-88f48f2e1e89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014D3jQrjwMxaHgKh3gw8sKE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13632,
      "cache_read_input_tokens": 19276,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13632
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 300,
          "cache_read_input_tokens": 19276,
          "cache_creation_input_tokens": 13632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13632,
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

_source line 24 · 2026-05-14T10:51:27.475Z_

<details><summary>↩ Tool result · `toolu_019XMvxCr7SyC728FJ49NpFU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/memory.md\", \"content\": \"# Memory — schema_semantic_constrained_ie\\n\\n## 文献调研 (2026-05-13)\\n\\n### 核心结论: OntoCoDec 的 novelty 成立\\n**没有人做过 \\\"compile IE ontology domain/range → decoding-time logits masking\\\" 的完整 pipeline。**\\n\\nGap 结构：\\n- Syntactic constrained decoding for IE: well-explored (GCD, XGrammar, Outlines)\\n- Vocabulary-level: exists (GENRE, iNERD, AdaKGC)\\n- **Semantic (domain/range) decoding for IE: OPEN GAP** ← OntoCoDec\\n- Semantic type checking at decode time: only for code gen (MGD NeurIPS'23, PLDI'25)\\n- Ontology compliance for IE: only post-processing (ODKE+ Apple'25, OntoLogX'25)\\n\\n最近竞争者：PLDI'25 Type-Constrained Code Gen（同机制但领域是代码生成，必须引用并区分）\\n\\n风险：CRANE (ICML'25) 严格约束可能降低推理质量；Grammar-Aligned Decoding (NeurIPS'24) naive masking 扭曲分布\\n\\nNovelty 定位：\\\"OntoCoDec 将 type-constrained generation 引入信息抽取，编译 IE ontology axioms 为解码时语义约束，预防而非检测 type violations。\\\"\\n\\n详细报告: `artifacts/literature_map.yaml`, `artifacts/literature_survey_*.md`\\n\\n## 实验发现\\n\\n### SciERC Phase 0 — Minimal (2026-05-13)\\n- **go_nogo_metric = 15.4%** (domain_range_violation_rate), 3× 超过 5% 阈值 → GO\\n- Violation 分布极不均匀: Used-for 0.76% vs Compare 42.4% vs Feature-of 33.5%\\n- Feature-of + Compare 贡献 72% 的 domain/range violations\\n- Relation vocabulary violations 仅 1.4%\\n- 关键 insight: OntoCoDec 的价值在于精确靶向高违规 relation types\\n\\n### SciERC Phase 0 — Schema-informed (2026-05-13)\\n- **domain_range_violation_rate = 5.78%**（vs minimal 15.37%, -62.4%）\\n- 仍高于 5% 阈值 → prompt 级干预不足以替代 decoding-time enforcement\\n- Entity type violations 降到 0%，relation vocabulary 降到 0.30%\\n- Per-relation: Feature-of -22.3pp, Part-of -22.5pp, Compare -14.8pp\\n- ⚠️ Evaluate-for 反而退步 +5.8pp — prompt 复杂度反而干扰\\n- McNemar 四类全显著 p<0.01\\n- **论文 story**: LLM 能理解约束（-62%）但执行不完美（仍>5%），需要 hard constraint\\n\\n### DocRED Phase 0 — Minimal (2026-05-13)\\n- **domain_range_violation_rate = 18.7%** (16,540 triples, 998 docs)\\n- Relation vocabulary violation = 28.9% (4,775 triples) — 远高于 SciERC 1.4%\\n- Entity type violation = 7.5% (vs SciERC 0.4%)\\n- JSON parse rate = 96.4% (36 docs 解析失败)\\n- Top violators: P31 instance_of (60.4%, 322/533), P1001 applies_to_jurisdiction (44.4%)\\n- 约束更紧(avg 5.68 pairs)确实导致更高违规(18.7% vs 15.4%)\\n\\n### SciERC vs DocRED 对比 (2026-05-13)\\n| 指标 | SciERC (7 rels) | DocRED (96 rels) |\\n|------|----------------|-----------------|\\n| D/R violation | 15.4% | 18.7% (+3.3pp) |\\n| Relation vocab | 1.4% | 28.9% (+27.5pp) |\\n| Entity type | 0.4% | 7.5% (+7.1pp) |\\n| Avg valid pairs | 26.1 | 5.68 |\\n两个数据集都远超 5% 阈值 → 强 GO 信号。Vocabulary layer 在复杂 schema 上尤为关键。\\n\\n### SciERC Phase 2 — Grammar-only (2026-05-13)\\n- **Grammar 层约束是\\\"免费\\\"的**：零 F1 代价完全消除 rv (1.4%→0%) 和 et (0.4%→0%) violations\\n- entity_f1 delta = -0.03pp ≈ 0，relation_f1 delta = 0\\n- **论文 claim**: \\\"Structural constraints can be enforced at zero quality cost\\\"\\n- DR violation 基本不变 (15.37%→14.84%, -0.53pp) — 符合预期，grammar 不含 D/R 约束\\n- DR 热点: Compare 40.85%, Feature-of 31.98%, Part-of 23.38% — 这些是 semantic 层的目标\\n- **决策依据**: grammar 层可以 always-on，无需 ablation 它的\\\"代价\\\"。论文只需关注 semantic 层的 F1 trade-off。\\n\\n### SciERC Phase 2 — 全量最终结果 (2026-05-14, _v2 干净数据)\\n\\n| Mode | R-F1 | E-F1 | DR% | RV% | ET% | ΔDR |\\n|------|------|------|-----|-----|-----|-----|\\n| unconstrained | 0.0823 | 0.3101 | 15.37% | 1.39% | 0.4% | — |\\n| grammar_only | 0.0823 | 0.3098 | 14.84% | 0% | 0% | -0.53pp |\\n| semantic_only | 0.0815 | 0.3101 | 11.65% | 1.51% | 0.4% | -3.72pp |\\n| **full_s1** | **0.0836** | **0.3098** | **0.93%** | **0%** | **0%** | **-14.44pp (↓94%)** |\\n\\n**核心发现**:\\n- **full_s1 是论文核心结果**: DR 15.37%→0.93% (消除 94%), F1 反而微升 +0.0013, 零质量代价\\n- **semantic_only 有效但不够**: DR -3.72pp (↓24%), 但 RV/ET 未消除（需 grammar 层配合）\\n- 早期污染数据 (108样本) 显示 semantic_only DR=16.43%（误导），干净数据实际 11.65%\\n- **Ablation story**: grammar 处理结构约束 (RV, ET), semantic 处理类型约束 (DR), 合并达最佳效果\\n\\n**Per-relation DR (full_s1)**: Used-for/Hyponym-of/Part-of/Conjunction = 0%, Feature-of 1.21%, Compare 2.82%, Evaluate-for 5.76% (残留最多)\\n\\n### SciERC Phase 2 — S2 全量结果 (2026-05-14)\\n| Mode | R-F1 | E-F1 | DR% | CF% |\\n|------|------|------|-----|-----|\\n| full_s1 | 0.0836 | 0.3098 | 0.93% | 9.90% |\\n| full_s2 | 0.0803 | 0.3190 | 0.97% | 8.03% |\\nS1 全面略优 (R-F1 +0.33pp, DR 持平)，S2 降级为 ablation。\\n\\n### DocRED Phase 2 — Grammar-only (2026-05-14)\\n- ET: 7.5%→0%, RV: 28.9%→0.03%, DR 26.17%（grammar 不含 D/R 约束，DR 高于 unconstrained 是因为 grammar 强制合法 relation name 后改变了 triple 分布）\\n- Grammar 层在复杂 schema 上同样完美消除 ET/RV\\n\\n### DocRED Phase 2 — Full S1 结果 (2026-05-14) ⚠️ 关键\\n| 指标 | Phase 0 Unconstrained | Grammar Only | Schema Informed | Full S1 |\\n|------|----------------------|-------------|-----------------|---------|\\n| ET | 7.50% | 0% | 0.61% | **0%** |\\n| RV | 28.90% | 0.03% | 18.40% | **0.03%** |\\n| DR | 18.70% | 26.17% | 12.80% | **10.19%** |\\n| CF | 0.08% | — | 0.15% | 2.57% |\\n| Entity F1 | — | — | — | 0.6534 |\\n| Relation F1 | — | — | — | 0.082 |\\n\\n**关键发现**:\\n1. ✅ Grammar 层在 DocRED 完美泛化: ET/RV→0%（与 SciERC 一致）\\n2. ⚠️ **DR 降幅 scaling gap**: SciERC ↓94% (15.37→0.93%) vs DocRED ↓45.5% (18.7→10.19%)\\n3. 残余 DR 集中在特定关系: P190_sister_city 58%, P582_end_time 43.5%, P205_basin_country 37%, P276_location 28.4%\\n4. Top-10 高 DR 关系贡献 27% 的总 violations (478/1771)\\n5. Semantic 层在 grammar 基础上额外贡献: DR 26.17→10.19% (↓61%)\\n6. CF 从 0.08% 升到 2.57%（低于 SciERC 的 9.9%）\\n7. **Framing 影响**: \\\"near-elimination\\\" 对 ET/RV 成立，DR 需改为 \\\"significant reduction\\\"。复杂 schema 下 entity type 边界模糊是 DR 残余的主因\\n\\n### Constraint Tightness ↔ DR Violation Scaling (2026-05-14) ⚠️ 论文核心 insight\\n**根因分析确认：DR 差异由约束紧度驱动，非 semantic 层失效。**\\n\\n| Tightness 区间 | Valid pairs | DocRED 聚合 DR | SciERC 对应 |\\n|---------------|-------------|---------------|------------|\\n| ≥ 0.95 (极紧) | 1-2 pairs | 30.6% | 无此类 relation |\\n| 0.90-0.94 | 3-4 pairs | 19.3% | 无此类 relation |\\n| < 0.70 (宽松) | 11+ pairs | 0.7% | SciERC 全部在此区间 |\\n\\n- DocRED avg tightness = 0.842 vs SciERC = 0.333\\n- DocRED 中位数仅允许 5/36 type pairs，SciERC 中位数 23/36\\n- 高 tightness 下 semantic∩grammar=∅ 概率高 → fallback 到 grammar-only → DR 未被约束\\n- SciERC DR 低是因为约束本身宽松，LLM 几乎不可能违规\\n- **论文定位**：effectiveness scales inversely with constraint tightness，这是 **contribution** 而非 weakness（首个 constraint scaling 实证，无文献可比）\\n- **文献确认**：无任何论文在 DocRED 上报告 constrained decoding violation rate，我们是首个 benchmark\\n\\n### CF Violation 根因分析 (2026-05-14)\\n- **CF = 跨字段一致性违规**：同一 entity mention 在 entity list 和 relation head/tail 中被标注为不同类型\\n- 根因: semantic constraint 按 per-relation 独立强制 type，导致 entity-vs-relation type drift\\n- 主要冲突: Generic ↔ OtherScientificTerm (60 次, 占比最高)\\n- grammar_only CF=0.08% → S1 CF=9.90% → **CF 100% 来自 semantic 层**\\n- **论文 limitation**: per-relation 独立 type enforcement 的固有副作用，需 future work 做跨 relation entity type 一致性约束\\n\\n### CF 指标口径澄清 (2026-05-14)\\n- violation_checker: 合并所有 type 来源 (entity list + relation head/tail)，denominator = total_entities (2474)\\n- analyze_cf: 分 WR (Within-Relations) + EVR (Entity-vs-Relation) 两维度，denominator 不同 (checked_slots=3380)\\n- **分子一致**: S1=245=245, S2=178 vs 179 (差 1 due to analyze_cf entity_type_map overwrite bug)\\n- **论文统一用 violation_checker 口径**: S1=9.90%, S2=8.03%\\n\\n### S2 Pilot 调查 (2026-05-13)\\n- **原报告 relation_f1=0 是误读**：数据来自 10 样本 dryrun 的 violation_report，非 pilot50 评估\\n- pilot50 实际 relation_f1=0.1008 (13 TP / 146 pred / 112 gold)，与 unconstrained 0.0823 持平\\n- S2 架构可行，DR violation=0% 达标，F1 瓶颈在 entity span 质量（zero-shot entity F1≈0.29）\\n- FP 根因: 52.6% head+tail 都不匹配 gold（entity span 提取错误以平方级放大到 relation）\\n\\n## 技术路线决策\\n\\n### Phase 1 Compiler 完成 (2026-05-13)\\n**HF transformers + XGrammar (standalone)**，代码在 `/root/schema_semantic_constrained_ie/compiler/`：\\n- `ontology_compiler.py`: compile_type_constraints() + build_processor()\\n- `type_mask_processor.py`: _build_first_token_map(), _mask_entity_type/head/tail_type(), _detect_position()\\n- 24 单元测试 + 12 e2e 测试全部通过\\n- SGLang 作为后续性能优化路径，vLLM 暂不可用\\n\\n### Phase 2 脚本完成 (2026-05-13)\\n`run_constrained_extraction.py` (652 行) 支持 5 模式：unconstrained/grammar_only/semantic_only/full_s1/full_s2\\n- 所有模式 dry-run 通过 + violation_checker 兼容\\n\\n### DocRED constrained decoding 就绪 (2026-05-14)\\n`run_constrained_extraction.py --dataset docred` 零代码修改即可运行 grammar_only / full_s1 模式。\\n约束文件: `data/docred/ontology_constraints_docred.json` (6 entity types, 96 relations)\\n建议命令加 `--max_new_tokens 4096`（文档级比句子级长得多）\\n\\n### Grammar-Semantic 交互 Bug 修复 (2026-05-14)\\n**根因**: `compiler/type_mask_processor.py` → `_apply_type_mask`。full_s1 模式下 XGrammar 将 grammar-invalid tokens 设为有限负值 (-1e10)，TypeConstraintProcessor 将 semantically-disallowed types 设为 -inf。当 `allowed_types` 与 grammar-valid tokens 无交集时，所有 grammar-valid tokens 变为 -inf，而 grammar-invalid tokens 仍为 -1e10 (> -inf) → argmax 选中 grammar-invalid token → XGrammar assertion failure。\\n**修复**: `_apply_type_mask` 增加 `_GRAMMAR_MASK_THRESHOLD = -1e8` 安全检查：应用 semantic mask 前验证至少一个 semantically-allowed type 有非 grammar-masked logit；若无交集则跳过 semantic masking，交由 grammar 控制。\\n**论文意义**: 此 invariant（semantic mask ⊆ grammar allowed set）是双层约束架构的关键设计约束，应在 Method section 明确描述。在 SciERC 上未触发是因为约束更松 (avg 26.1 valid pairs vs DocRED 5.68)。\\n\\n### Llama-3.1-8B 兼容性验证 (2026-05-14)\\n- 模型已在服务器: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`\\n- 零代码修改：AutoTokenizer/AutoModelForCausalLM 模型无关，chat_template 自动适配\\n- XGrammar + TypeConstraintProcessor first-token 唯一性验证通过（SciERC 6 types + DocRED 6 types）\\n- pad_token=None 已有处理逻辑\\n\\n### First-token masking 验证 (2026-05-13)\\n简单 first-token masking 安全可用，不需要 trie-based 方案。\\nSciERC: Task=6262, Method=3523, Material=13415, Metric=54310, OtherScientificTerm=11409, Generic=19964\\nDocRED: PER=9654, ORG=44927, LOC=12052, TIME=18129, NUM=17488, MISC=44\\n上下文无关性已验证。\\n\\n## 方法论决策\\n\\n### Violation 分类体系 (2026-05-13)\\n4 类独立计数：entity_type / relation_vocabulary / domain_range / cross_field_consistency\\ngo/no-go 阈值 (5%) 基于 domain_range_violation_rate\\n\\n### Fuzzy Matching (2026-05-13)\\nDocRED: token overlap >80% 或 Levenshtein ≤2\\n\\n## 踩坑记录\\n\\n### submit_training_job 必须 bash -c 包裹 (2026-05-13)\\n- tmux session 默认用 `sh` 执行命令，`source` 和 `conda activate` 是 bash built-in\\n- **直接写 `python3 ...` 会 EXIT_CODE=127 (command not found)**\\n- **正确写法**: `bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 ...\\\"`\\n\\n### 孤儿进程清理误杀活跃实验 (2026-05-14)\\n- Worker 执行孤儿进程清理时，白名单未包含所有活跃实验 PID → SIGTERM 杀掉了 mvp_phase0_docred_schema 和 semantic_only/full_s1\\n- **防护措施**: 清理前必须查 registry 所有 RUNNING 实验的 PID 全部加入白名单; Kill 前检查输出文件行数是否已达 expected count; 只 kill 具体的孤儿 PID\\n- **恢复方式**: JSONL 逐行追加，用 --resume 从断点恢复\\n\\n### 重提交实验前必须清理旧 tmux session (2026-05-13)\\n- retry 未 kill 旧 tmux → 两进程同时写同一 JSONL → null bytes 污染\\n- **规则**: 重提交前先 `tmux kill-session -t &lt;exp_id>`\\n\\n### 禁止在 allocate_and_submit 命令内放 tmux kill-session (2026-05-14)\\n- allocate_and_submit 在 tmux session 内执行命令，`tmux kill-session -t <同名session>` 导致 session 自杀\\n- cron 追踪死 session → 5× miss → 误判 DONE(failed)\\n- **正确做法**: 单独派 Worker 先清理旧 session，确认后再 allocate_and_submit\\n\\n### Cron PID 追踪不可靠 (2026-05-14)\\n- cron 系统导致 4 次假失败（grammar_only / semantic_only / full_s1 / full_s2），每次假失败触发 cleanup worker 又误杀合法进程，恶性循环\\n- **决策**: 对长期运行实验改用手动 `wc -l` 检查输出文件行数判断完成，不依赖 PID/tmux 存活\\n- 完成判断标准: 输出文件行数 = 目标样本数\\n\\n## 环境信息\\n\\n### westd-16980 (2026-05-13)\\n- GPU: 2× NVIDIA RTX PRO 6000 Blackwell (94GB each)\\n- CUDA 12.8, Python 3.12.3 (conda base)\\n- torch 2.10.0+cu128, transformers 4.57.6\\n- 环境激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 模型路径: `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`\\n- Llama 模型路径: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`\\n- XGrammar v2 已安装\\n\\n## 数据信息\\n\\n### SciERC\\n- HuggingFace `zj88zj/SCIERC`, 551 sentences, 7 relation types, 17-35 valid pairs each（约束松散）\\n\\n### DocRED\\n- HuggingFace Hub .gz, 998 docs, 96 relation types, avg 5.68 valid pairs/relation (约束紧)\\n\\n## 分析工具 (2026-05-13)\\n- `compare_prompts.py`: minimal vs schema-informed 对比 + McNemar 检验\\n- `violation_checker.py` / `violation_checker_docred.py`: 4 类 violation 分析\\n\", \"total_chars\": 11588, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "634d61f9-c524-4bb4-9ff5-88f48f2e1e89",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "17a7c9d2-a2a6-47b4-aa65-9dfd99c9a461",
  "sourceToolAssistantUUID": "634d61f9-c524-4bb4-9ff5-88f48f2e1e89",
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

_source line 25 · 2026-05-14T10:51:30.757Z_

Now let me read the actual paper sections to assess writing quality, related work, and novelty claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17a7c9d2-a2a6-47b4-aa65-9dfd99c9a461",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LKFLR7Fqck9MbYS78Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f13ee8a1-d873-4b3b-87b9-8afdc87cc250",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUJ5g1Q6LmjV7SBFfaz5Y7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9363,
      "cache_read_input_tokens": 32908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9363,
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

_source line 26 · 2026-05-14T10:51:33.222Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PkmoJ21Xmpi6RtRkbtS1ud`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f13ee8a1-d873-4b3b-87b9-8afdc87cc250",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LKFLR7Fqck9MbYS78Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "524ac702-b96e-4c0d-9906-79ee791ca036",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUJ5g1Q6LmjV7SBFfaz5Y7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9363,
      "cache_read_input_tokens": 32908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9363,
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

_source line 27 · 2026-05-14T10:51:33.227Z_

<details><summary>↩ Tool result · `toolu_01PkmoJ21Xmpi6RtRkbtS1ud`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, enabling efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for structured generation.
15	However, all of these methods operate exclusively at the syntactic level---they ensure format validity (e.g., well-formed JSON, valid enum values) but cannot enforce cross-field semantic constraints such as ontology domain/range rules that depend on previously generated content.
16	This syntactic-only limitation motivates OntoCoDec's semantic extension: our grammar layer builds on XGrammar for structural (JSON schema and enum) constraints, while a second semantic layer enforces relational type constraints that are inherently beyond the expressive power of context-free grammars.
17	
18	% ===========================================================================
19	% Paradigm 1.5: Semantic Constrained Decoding for Code
20	% ===========================================================================
21	\paragraph{Semantic Constrained Decoding for Code.}
22	In programming-language generation, constrained decoding has been extended beyond syntax to enforce semantic properties such as type correctness, demonstrating that richer-than-CFG constraints can be compiled into token-level filtering.
23	Synchromesh~\cite{synchromesh_neurips2022} pioneers Constrained Semantic Decoding (CSD), which enforces syntax, type, and scope constraints simultaneously during code generation from pre-trained LMs without fine-tuning, establishing that semantic constraints can be expressed as dynamic token masks conditioned on the generation prefix.
24	MGD~\cite{mgd_neurips2023} uses static-analysis monitors to perform incremental type checking at decode time, enabling SantaCoder-1.1B to outperform text-davinci-003 on repository-level code completion by ensuring that every generated identifier is type-correct with respect to the surrounding code context.
25	Most recently, \citet{pldi2025_type_constrained_codegen} compile full type systems---including generic types and subtyping---into prefix automata for token-level logits masking, reducing compilation errors by over 50\%.
26	This last system is the closest mechanistic analog to OntoCoDec, applying the same ``type system $\to$ automaton $\to$ logits mask'' pipeline, though in a fundamentally different domain.
27	The key technical difference lies in the constraint structure: programming-language type systems feature deep subtyping hierarchies and parametric polymorphism, whereas IE ontology axioms specify flat domain/range sets---a relation $R$ accepts head entities from set $\mathcal{D}(R)$ and tail entities from set $\mathcal{R}(R)$, with no subtype chains.
28	Conversely, IE introduces a challenge absent in code generation: the constraint target (entity type) must be inferred from free-text spans rather than read from declared type annotations, requiring a stateful entity registry that tracks extracted types during autoregressive generation.
29	These methods collectively demonstrate that semantic (type) constraints at decode time are both feasible and highly effective, but exclusively in the code domain where type systems are formally specified.
30	OntoCoDec is the first to migrate type-constrained decoding from code generation to information extraction, compiling IE ontology axioms (domain/range constraints) into an analogous decoding-time enforcement mechanism.
31	
32	% ===========================================================================
33	% Paradigm 2: Vocabulary/Type-Constrained Generation
34	% ===========================================================================
35	\paragraph{Vocabulary and Type-Constrained Generation.}
36	The idea of enforcing entity-type compatibility constraints for information extraction dates back to pre-neural methods.
37	\citet{roth_yih_2004} formulate joint entity and relation identification as an integer linear program (ILP) that enforces type constraints---e.g., \textsc{Emp-Org} only between \textsc{Per} and \textsc{Org} entities---establishing the foundational principle that relational type compatibility should be a hard constraint, not a soft preference learned from data.
38	In the autoregressive era, GENRE~\cite{decao2021genre} pioneers trie-based constrained beam search for autoregressive entity retrieval, restricting each decoding step to tokens consistent with valid entity names from a predefined catalog.
39	GenIE~\cite{josifoski2022genie} extends this approach to end-to-end information extraction with state-based constraints that enforce valid triple structures, achieving strong performance on closed-world knowledge base population, though it requires task-specific fine-tuning on the target schema.
40	AdaKGC~\cite{adakgc_emnlp2023} introduces schema-constrained dynamic decoding with trie-based prefix trees that adapt to the target schema, enforcing that generated entity and relation names belong to a predefined inventory---a vocabulary-level constraint that ensures name validity but does not verify type compatibility between a relation and its arguments.
41	GCD~\cite{geng2023gcd} provides a unified grammar-constrained decoding framework for structured NLP tasks including IE, introducing input-dependent grammars that adapt constraints based on the source text---the closest precursor to OntoCoDec in applying logits masking to IE, though limited to syntactic constraints.
42	NeuroLogic Decoding~\cite{lu2021neurologic} expresses lexical inclusion and exclusion constraints as predicate logic formulas enforced during beam search, offering a general mechanism for token-level control that can encode vocabulary membership but not relational type rules.
43	These approaches constrain \emph{which tokens} can appear (vocabulary membership) but not \emph{which type combinations} are valid for a given relation.
44	OntoCoDec's semantic layer enforces relational constraints---e.g., that the head entity of relation $R$ must belong to type set $\mathcal{D}(R)$---which cannot be expressed as static vocabulary restrictions because the valid set depends on the relation type generated earlier in the same sequence.
45	While Roth \& Yih's ILP formulation shares the same type-compatibility motivation, it operates as a post-hoc reranker over discrete candidates; OntoCoDec integrates enforcement directly into autoregressive decoding, preventing violations rather than filtering them.
46	
47	% ===========================================================================
48	% Paradigm 3: Structural Constraints for IE
49	% ===========================================================================
50	\paragraph{Structural Constraints via Training and Prompting.}
51	An orthogonal approach encodes IE output structure through model training or prompt design rather than decoding-time enforcement, relying on learned representations to produce schema-compliant outputs.
52	UIE~\cite{lu2022uie} defines a Structured Extraction Language and trains a unified text-to-structure model across 13 IE datasets, relying on large-scale pre-training to internalize output format constraints.
53	GoLLIE~\cite{sainz2024gollie} expresses annotation guidelines as Python dataclass definitions and fine-tunes Code-LLaMA to generate typed code, achieving strong zero-shot transfer to unseen IE schemas by leveraging the implicit type structure of programming languages.
54	KnowCoder~\cite{knowcoder_acl2024} takes this further by encoding 29K entity types from Wikidata as a Python class hierarchy, training a Code-LLM to generate structured extraction code that implicitly respects type inheritance---the most comprehensive schema-as-code approach to date.
55	CodeIE~\cite{li2023codeie} similarly reformulates IE as code generation, leveraging the structural regularity of programming languages to reduce output format errors.
56	ADELIE~\cite{qi2024adelie} uses SFT and DPO to align LLMs on IE tasks, achieving state-of-the-art results among open-source models while preserving general capabilities, though compliance with ontological constraints remains a learned soft preference rather than a guarantee.
57	EnriCo~\cite{zaratiana2024enrico} applies Answer Set Programming (ASP) constraints during decoding of joint entity-relation extraction models, enforcing structural type compatibility at generation time---a decoding-time approach, though with model-specific, manually authored constraints rather than ontology-driven compilation.
58	Training-based methods provide \emph{soft} structural guidance---the model learns to prefer valid outputs but cannot guarantee compliance at inference time, as demonstrated by non-trivial violation rates even in fine-tuned systems.
59	Importantly, training-based and decoding-time approaches are complementary rather than competing: a system like GoLLIE could be combined with OntoCoDec's constraint layers, using fine-tuning to maximize the probability of valid outputs while decoding-time enforcement eliminates residual violations.
60	OntoCoDec provides \emph{hard} decoding-time enforcement that is training-free, automatically compiled from ontology schemas, and composable with any of these training-based approaches.
61	
62	% ===========================================================================
63	% Paradigm 4: Type-Checking / Ontology Validation
64	% ===========================================================================
65	\paragraph{Post-hoc Ontology Validation.}
66	Rather than constraining generation, several methods validate LLM outputs against ontological rules after generation, applying a detect-then-fix paradigm.
67	ODKE+~\cite{khorshidi2025odke} dynamically generates ontology snippets containing domain/range constraints as prompt context, achieving 98.8\% precision across 195 predicates at web scale---but constraint adherence relies on prompt-level guidance, not enforcement, leaving residual violations unaddressed.
68	SPIRES/OntoGPT~\cite{spires_2024} provides an ontology-based extraction framework that grounds LLM outputs against OBO ontologies post-generation, validating extracted entities and relations through ontology lookup and correcting mismatches in a second pass---representing the prompt-then-validate paradigm in the biomedical domain.
69	OntoLogX~\cite{ontologx_2025} applies SHACL validation to LLM-generated knowledge graphs, iteratively re-prompting the LLM to correct constraint violations and reducing them by approximately 10$\times$ across multiple correction rounds---demonstrating the detect-then-fix paradigm's effectiveness but also its inherent multi-pass cost.
70	\citet{upadhyay2023openie} inject entity-type knowledge as constraints into Open IE via both constrained inference and constraint-aware training, improving F1 by 29\% on CaRB, though their constrained inference operates over a discrete candidate set rather than during autoregressive generation.
71	\citet{regino2025kgcurator} propose a multi-stage LLM pipeline for validating RDF triple insertions against RDFS domain/range constraints, where each validation step requires a separate LLM call---effective but computationally expensive at scale.
72	\citet{ekaw2024_ontology_beam} introduce ontology-constrained beam scoring for clinical summarization, applying soft biases (not hard masks) during beam search to steer outputs toward ontology-compliant terms---a middle ground between unconstrained generation and hard enforcement that reduces but cannot eliminate violations.
73	Post-hoc validation detects violations after generation, requiring rejection or correction cycles that waste compute---in our setting, 15.37\% of generated triples contain domain/range violations under unconstrained decoding, representing substantial wasted generation effort.
74	OntoCoDec \emph{prevents} violations during decoding, redirecting probability mass to valid alternatives rather than discarding invalid outputs, with only marginal overhead from logits masking compared to the cost of regenerating or correcting violated triples.
75	Soft-constraint approaches such as ontology-weighted beam scoring reduce violation frequency but cannot eliminate it, whereas OntoCoDec achieves near-complete elimination (domain/range violations $\downarrow$94\%, from 15.37\% to 0.93\%).
76	
77	% ===========================================================================
78	% Paradigm 5: Constrained Decoding Quality Concerns
79	% ===========================================================================
80	\paragraph{Quality Impact of Constrained Decoding.}
81	A growing body of work raises concerns that constrained decoding degrades LLM generation quality, particularly for reasoning-intensive tasks where format enforcement interferes with chain-of-thought processes.
82	\citet{tam2024letmespeak} conduct a comprehensive evaluation showing that rigid format constraints (JSON, XML) harm performance on math and multi-hop QA benchmarks but \emph{benefit} classification-style tasks such as slot filling---a distinction directly relevant to IE, which is fundamentally an extraction (classification-like) task rather than a reasoning task.
83	CRANE~\cite{banerjee2025crane} provides theoretical analysis of why restricting outputs to narrow grammars suppresses chain-of-thought reasoning by eliminating intermediate reasoning tokens, and proposes an alternating strategy between unconstrained reasoning phases and constrained output phases to mitigate this effect.
84	\citet{schall2025hiddencost} conduct a systematic study across 11 models and multiple benchmarks, finding 10--30\% semantic correctness degradation on reasoning tasks under structural constraints, with larger models showing greater absolute degradation.
85	\citet{zhou2026snowballing} identify ``structure snowballing''---a failure mode where format compliance cognitive load traps models in repetitive structural patterns rather than improving reasoning during self-correction iterations. % PENDING AUDIT: zhou2026snowballing may need replacement
86	These findings establish a legitimate concern for constrained decoding in reasoning-heavy applications.
87	However, information extraction occupies a fundamentally different regime: the model extracts entities and relations from input text rather than generating novel reasoning chains, and \citet{tam2024letmespeak}'s own results show that extraction-style tasks are robust to---or even benefit from---format constraints.
88	OntoCoDec addresses this concern empirically: on SciERC, domain/range violations decrease from 15.37\% to 0.93\% ($\downarrow$94\%) with \emph{zero} F1 degradation (R-F1 8.36\% vs.\ 8.23\% unconstrained, $+$0.13pp, not statistically significant).
89	Critically, OntoCoDec's constraints target only type tokens (entity types, relation labels), leaving free-text spans---entity surface forms and their boundaries---entirely unconstrained, which minimizes the distribution distortion that causes quality degradation in reasoning tasks.
90	OntoCoDec's S2 (two-pass) strategy can also be viewed as an instantiation of CRANE's alternating approach: the first pass performs unconstrained entity extraction, and the second pass applies relation-specific constraints compiled from the first pass's output, separating the extraction and constraint-enforcement phases.
91	
92	% ===========================================================================
93	% Our Approach
94	% ===========================================================================
95	\paragraph{Our Approach.}
96	OntoCoDec occupies a unique position in this landscape: it is the first system to automatically compile IE ontology schemas---including domain/range axioms---into decoding-time semantic constraints, extending grammar-constrained decoding from syntactic to semantic enforcement.
97	Unlike vocabulary-constrained methods that restrict individual tokens to a fixed set, OntoCoDec enforces \emph{cross-field relational constraints} through a stateful entity registry that tracks extracted types during autoregressive generation, enabling dynamic constraint evaluation that depends on previously decoded content.
98	Unlike training-based IE systems, OntoCoDec is training-free and achieves near-complete elimination of type violations at inference time; unlike post-hoc validation, it prevents violations rather than detecting them, redirecting probability mass to valid alternatives at near-complete elimination rates (domain/range violations 15.37\%$\to$0.93\%) and zero quality cost (R-F1 8.36\% vs.\ 8.23\% unconstrained).
99	The two constraint layers---grammar (structural) and semantic (relational)---compose via bitwise AND with an enabling dependency: the grammar layer ensures every generated type token belongs to the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type.
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "524ac702-b96e-4c0d-9906-79ee791ca036",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "51f342ad-11ce-4e05-bce7-1b4e262df0ce",
  "sourceToolAssistantUUID": "524ac702-b96e-4c0d-9906-79ee791ca036",
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

_source line 28 · 2026-05-14T10:51:34.060Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UhdJAzPVZ8rT4Ur51EuB2E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51f342ad-11ce-4e05-bce7-1b4e262df0ce",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LKFLR7Fqck9MbYS78Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d276b2f-8664-4802-acf6-0598f56451c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUJ5g1Q6LmjV7SBFfaz5Y7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9363,
      "cache_read_input_tokens": 32908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9363,
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

_source line 29 · 2026-05-14T10:51:34.065Z_

<details><summary>↩ Tool result · `toolu_01UhdJAzPVZ8rT4Ur51EuB2E`</summary>

```text
1	% Section 1: Introduction for OntoCoDec paper
2	% Target: EMNLP 2026 (ARR submission May 25, 2026)
3	
4	\section{Introduction}
5	\label{sec:introduction}
6	
7	Large language models are increasingly deployed for information extraction in zero-shot and few-shot settings, bypassing the need for task-specific training data~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}.
8	However, when an LLM generates relation triples $(h, r, t)$, neither the head entity $h$ nor the tail entity $t$ is guaranteed to carry an entity type consistent with the domain and range constraints that the target ontology prescribes for relation $r$.
9	We refer to such outputs as \emph{domain/range violations}---structurally well-formed triples that are nonetheless invalid under the ontology's type signature.
10	In a systematic study across two standard IE benchmarks, we find that these violations are pervasive: 15.4\% of generated triples on SciERC~\cite{luan2018scierc} and 18.7\% on DocRED~\cite{yao2019docred} violate domain/range constraints when no enforcement mechanism is applied.
11	Crucially, violations are not uniformly distributed across relation types.
12	Relations with tight type constraints---few valid entity-type pairs---exhibit far higher violation rates (\textsc{Compare}: 42.4\%, \textsc{Feature-of}: 33.5\%), while loosely constrained relations remain nearly violation-free (\textsc{Used-for}: 0.8\%).
13	This pattern holds across datasets of vastly different ontology sizes (7 vs.\ 96 relation types), indicating that violation severity is driven by \emph{constraint tightness} rather than ontology scale.
14	For downstream applications such as knowledge graph construction, ontology-grounded reasoning, and safety-critical extraction in biomedical or legal domains, such systematic type invalidity is unacceptable.
15	
16	Existing approaches address this problem at different levels but leave a fundamental gap.
17	Schema-informed prompting---explicitly describing domain/range constraints in the prompt---reduces violations by 62\% on average, yet leaves residual rates above 5\% and is unreliable at the per-relation level: for \textsc{Evaluate-for}, violations actually increase by 5.8 percentage points, revealing a \emph{prior-constraint conflict} where prompt-level signals interfere with the model's learned type associations.
18	Grammar-constrained decoding frameworks such as XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, and LMQL~\cite{beurer-kellner2023lmql} guarantee syntactic well-formedness (e.g., valid JSON) and can restrict output vocabularies, but do not encode cross-field semantic constraints such as ``if $r$ = \textsc{Feature-of}, then $h$ must be a \textsc{Method} or \textsc{OtherScientificTerm}.''
19	Post-hoc validation can filter invalid triples but wastes 14--15\% of generation compute on outputs that are discarded, cannot redirect probability mass toward valid alternatives during decoding, and is incompatible with streaming extraction scenarios.
20	Training-based approaches~\cite{sainz2024gollie,lu2022uie} incorporate schema knowledge through fine-tuning, but require task-specific training data and provide only soft guidance---they reduce but cannot eliminate violations.
21	
22	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that automatically compiles an IE ontology schema into two composable layers of decoding-time constraints.
23	The \emph{grammar layer} translates the ontology's entity types, relation types, and output structure into a context-free grammar via XGrammar, enforcing JSON well-formedness and vocabulary validity at every generated token.
24	The \emph{semantic layer} implements a \texttt{TypeConstraintProcessor} that maintains a stateful entity registry during generation: as entities and their types are decoded, the registry records each assignment, and when a relation's arguments are generated, dynamic logit masking restricts the output to entity types compatible with the relation's domain/range specification.
25	The two layers compose via bitwise AND of their token masks, with an \emph{enabling dependency}: the grammar layer guarantees that every generated relation type belongs to the valid vocabulary, which in turn enables the semantic layer to look up and enforce domain/range rules for that type.
26	This architecture is training-free and designed to be model-agnostic.
27	On SciERC, OntoCoDec reduces domain/range violations from 15.37\% to 0.93\% ($\downarrow$94\%) while remaining F1-neutral (relation F1 $+$0.13pp, within noise).
28	
29	Our contributions are as follows:
30	\begin{enumerate}
31	    \item We present the first systematic quantification of ontology constraint violations in LLM-based IE, revealing that violation rates are driven by constraint tightness rather than ontology size, and that prompt-level intervention is per-relation unreliable.
32	    \item We introduce OntoCoDec, a framework that compiles IE ontology domain/range constraints into semantic decoding-time constraints---the first method to enforce cross-field type validity during autoregressive generation for IE.
33	    \item We provide a decidability taxonomy of IE ontology constraints (purely local, prefix-decidable with state, truly non-local) and formalize the enabling dependency between grammar and semantic layers.
34	    \item We validate OntoCoDec on SciERC and DocRED, demonstrating near-complete violation elimination (DR 15.4\%$\rightarrow$0.93\%, $\downarrow$94\%) at zero F1 cost, with cross-dataset generalization.
35	\end{enumerate}
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d276b2f-8664-4802-acf6-0598f56451c3",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "c9f676ca-fc90-4c14-99e0-1cb94ede0607",
  "sourceToolAssistantUUID": "1d276b2f-8664-4802-acf6-0598f56451c3",
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

_source line 30 · 2026-05-14T10:51:34.198Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GjxTNES4SMD4U3DsuuFJ4J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9f676ca-fc90-4c14-99e0-1cb94ede0607",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LKFLR7Fqck9MbYS78Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "323f5fe8-243d-4167-b6ed-e5e300bb7783",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUJ5g1Q6LmjV7SBFfaz5Y7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9363,
      "cache_read_input_tokens": 32908,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9363
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 274,
          "cache_read_input_tokens": 32908,
          "cache_creation_input_tokens": 9363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9363,
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

_source line 31 · 2026-05-14T10:51:34.203Z_

<details><summary>↩ Tool result · `toolu_01GjxTNES4SMD4U3DsuuFJ4J`</summary>

```text
1	\begin{abstract}
2	LLM-based information extraction systems produce systematic ontology constraint violations during autoregressive generation.
3	On SciERC (7 relation types), 15.4\% of extracted triples violate domain/range type constraints; on DocRED (96 relation types), 18.7\%.
4	These violations concentrate on tightly constrained relations (e.g., \textsc{Compare}: 42.4\%, \textsc{Feature-of}: 33.5\%), while loosely constrained relations exhibit near-zero violation rates.
5	%
6	Schema-informed prompting reduces violations by 62\% on SciERC but only 31\% on DocRED, and is unreliable at the per-relation level---\textsc{Evaluate-for} violations \emph{increase} by 5.8 percentage points.
7	Prompt-level intervention thus scales poorly with ontology complexity.
8	%
9	We present \textsc{OntoCoDec}, which automatically compiles IE ontology schemas into two composable constraint layers for autoregressive decoding:
10	(1)~a \emph{grammar layer}, implemented via XGrammar, that enforces JSON structural validity and restricts entity-type and relation vocabularies to schema-defined values; and
11	(2)~a \emph{semantic layer} (TypeConstraintProcessor) that enforces cross-field domain/range constraints through a stateful entity registry and dynamic logit masking.
12	The two layers compose via bitwise AND on token-level masks, with an enabling dependency: the grammar layer guarantees well-formed output, upon which the semantic layer enforces relational type rules.
13	%
14	On SciERC, \textsc{OntoCoDec} reduces domain/range violations from 15.37\% to 0.93\% ($\downarrow$94\%) while completely eliminating entity-type and relation-vocabulary violations, with no degradation in extraction F1 ({+}0.13pp, not statistically significant).
15	\placeholder{DocRED results.}
16	However, cross-field consistency violations increase from 0.08\% to 9.9\%, a systematic side effect of per-relation independent type enforcement that represents an open challenge for future constraint composition.
17	\end{abstract}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "323f5fe8-243d-4167-b6ed-e5e300bb7783",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "d951deb3-b8a6-40ba-a38d-52269b6a14fc",
  "sourceToolAssistantUUID": "323f5fe8-243d-4167-b6ed-e5e300bb7783",
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

_source line 32 · 2026-05-14T10:51:38.731Z_

<details open><summary>🔧 Tool call — Read · `toolu_019J42YSevFKXA97sN2wnYep`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d951deb3-b8a6-40ba-a38d-52269b6a14fc",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LKkEjBCxrTPpWfuSaR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "425e7b68-3f6c-47f5-a54c-ff078da5a74f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xc1VSdrLUJX69WVQUQVPH5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6580,
      "cache_read_input_tokens": 42271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6580,
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

_source line 33 · 2026-05-14T10:51:38.736Z_

<details><summary>↩ Tool result · `toolu_019J42YSevFKXA97sN2wnYep`</summary>

```text
1	% Section 3 — Method (Draft)
2	% OntoCoDec: Near-Complete Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity—well-formed JSON with ontology-vocabulary membership—while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
10	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and the two decoding strategies (\S\ref{sec:strategies}).
11	Formal analysis of constraint composition and the grammar-first invariant is deferred to Section~\ref{sec:composition}.
12	
13	
14	\subsection{Problem Formulation}
15	\label{sec:formulation}
16	
17	\paragraph{IE as structured generation.}
18	Given an input text $x$, a language model generates a structured JSON output $y$ encoding the extracted information:
19	%
20	\begin{equation}\label{eq:output-schema}
21	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\},
22	\end{equation}
23	%
24	where each entity has a name $n_i$ and type $\tau_i$, and each relation triple specifies a head entity $h_j$, tail entity $t_j$, relation type $r_j$, and the corresponding head and tail entity types $\tau^h_j$ and $\tau^t_j$.
25	
26	\paragraph{Ontology schema.}
27	An ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \operatorname{dom}, \operatorname{range})$ defines the set of entity types $\mathcal{E}$, the set of relation types $\mathcal{R}$, and two functions $\operatorname{dom}: \mathcal{R} \to 2^{\mathcal{E}}$ and $\operatorname{range}: \mathcal{R} \to 2^{\mathcal{E}}$ that specify, for each relation, the entity types permitted as head and tail respectively.
28	
29	\paragraph{Ontology compliance.}
30	A relation triple $(h, r, t)$ with $\operatorname{type}(h) = \tau^h$ and $\operatorname{type}(t) = \tau^t$ is \emph{type-valid} with respect to $\mathcal{O}$ if and only if:
31	%
32	\begin{equation}\label{eq:type-valid}
33	  \tau^h \in \operatorname{dom}(r) \;\wedge\; \tau^t \in \operatorname{range}(r).
34	\end{equation}
35	%
36	We define the \emph{domain/range violation rate} (DR) as the fraction of generated triples that fail Eq.~\eqref{eq:type-valid}.
37	
38	\paragraph{Objective.}
39	We seek a decoding strategy that maximizes $P(y \mid x)$ subject to ontology compliance: all generated triples should be type-valid under $\mathcal{O}$, and the output $y$ must be structurally well-formed JSON conforming to the schema in Eq.~\eqref{eq:output-schema}.
40	
41	\paragraph{Constraint decidability.}
42	Not all ontology constraints are enforceable at every point during left-to-right generation.
43	We distinguish three classes by \emph{prefix-decidability}---i.e., when sufficient information becomes available in the generated prefix:
44	%
45	\begin{enumerate}[leftmargin=*,nosep]
46	  \item \textbf{Local constraints} depend only on the current token position.
47	    Entity-type membership ($\tau_i \in \mathcal{E}$) and relation-vocabulary membership ($r_j \in \mathcal{R}$) are local: each candidate token can be checked against the ontology vocabulary independently.
48	  \item \textbf{Prefix-decidable constraints} depend on the current token plus previously generated context.
49	    Domain/range constraints are prefix-decidable: once the head entity, its type, and the relation type have been generated, the set of valid tail types is fully determined.
50	  \item \textbf{Non-local constraints} depend on information not yet generated.
51	    Forward coreference---where a later entity mention determines the type of an earlier one---is inherently non-local and falls outside the scope of single-pass autoregressive decoding.
52	\end{enumerate}
53	%
54	OntoCoDec's two-layer design covers the first two classes: the grammar layer handles local constraints, and the semantic layer handles prefix-decidable constraints.
55	We revisit this taxonomy in Section~\ref{sec:composition} to formalize constraint composition properties.
56	
57	
58	\subsection{Grammar Layer}
59	\label{sec:grammar}
60	
61	The grammar layer compiles the ontology schema $\mathcal{O}$ into a context-free grammar (CFG) that is enforced at every decoding step via logit masking.
62	This compilation proceeds in two stages.
63	
64	\paragraph{Schema-to-grammar compilation.}
65	Given $\mathcal{O}$, we first generate a JSON Schema that encodes the output structure in Eq.~\eqref{eq:output-schema}, with \texttt{enum} constraints restricting entity types to $\mathcal{E}$, relation types to $\mathcal{R}$, and head/tail types to $\mathcal{E}$.
66	The JSON Schema is then compiled into an EBNF grammar using XGrammar~\cite{xgrammar}, which converts the schema into a pushdown automaton that tracks JSON nesting, field names, string boundaries, and enum membership.
67	
68	\paragraph{Logit masking.}
69	At each decoding step $t$, the grammar processor computes the set of grammar-valid tokens $G(t) \subseteq V$ based on the automaton state, and masks all tokens outside $G(t)$ by setting their logits to $-\infty$.
70	This enforces three categories of constraints simultaneously:
71	(i)~\emph{structural validity}---the output is always well-formed JSON with correct field names and nesting;
72	(ii)~\emph{relation vocabulary membership}---$r_j \in \mathcal{R}$ for all generated relations; and
73	(iii)~\emph{entity type membership}---$\tau_i \in \mathcal{E}$ for all generated entity types.
74	
75	\paragraph{What grammar does not enforce.}
76	The grammar layer does not encode domain/range constraints ($\operatorname{dom}$, $\operatorname{range}$), because these depend on the specific entity types appearing in each triple---information that is only available during generation.
77	This is precisely the gap that the semantic layer fills.
78	
79	\paragraph{Empirical profile.}
80	On SciERC, grammar-only constraints eliminate relation vocabulary violations entirely (1.39\%\,$\to$\,0\%) and entity type violations entirely (0.40\%\,$\to$\,0\%), with no measurable F1 impact (R-F1 8.23, E-F1 30.98 vs.\ unconstrained R-F1 8.23, E-F1 31.01).
81	Domain/range violations remain effectively unchanged (15.37\%\,$\to$\,14.84\%), confirming that grammar constraints enforce structural but not semantic validity.
82	
83	
84	\subsection{Semantic Layer}
85	\label{sec:semantic}
86	
87	The semantic layer enforces domain/range type constraints through a stateful logits processor that maintains an entity registry during generation.
88	
89	\subsubsection{Entity Registry}
90	\label{sec:entity-registry}
91	
92	As the model generates the entity list portion of the output, the semantic layer builds an \emph{entity registry} $\mathcal{D}: \text{name} \to \text{type}$ that maps each entity mention to its declared type.
93	This registry is populated incrementally: when the model completes an entity entry $\{n_i, \tau_i\}$, the pair $(n_i, \tau_i)$ is added to $\mathcal{D}$.
94	The registry is then consulted during relation generation to look up the declared types of head and tail entities.
95	
96	\subsubsection{Position Detection}
97	\label{sec:position-detection}
98	
99	At each decoding step $t$, the processor determines which field is currently being generated by pattern-matching on the decoded text prefix.
100	We define a set of field positions $\mathcal{F} = \{\textsc{EntityType}, \textsc{RelationType}, \textsc{HeadType}, \textsc{TailType}, \textsc{FreeText}\}$.
101	The detector examines the trailing context of the decoded output to identify the active field based on JSON key patterns (e.g., the token sequence following \texttt{"head\_type":} indicates a \textsc{HeadType} position).
102	Only at type-bearing positions (\textsc{HeadType}, \textsc{TailType}) does the semantic layer activate its constraint masks.
103	
104	\subsubsection{Dynamic Masking}
105	\label{sec:dynamic-masking}
106	
107	When a type-bearing position is detected, the processor computes a semantic mask $S(t) \subseteq V$ that restricts generation to type-valid tokens.
108	The masking rules differ by position:
109	
110	\paragraph{Head type masking.}
111	At a \textsc{HeadType} position within a relation triple, the processor considers two information sources: the entity registry $\mathcal{D}$ and the current relation type $r_j$ (if already generated).
112	If $h_j \in \mathcal{D}$ and the registered type $\mathcal{D}[h_j] \in \operatorname{dom}(r_j)$, the mask allows only that type: $S(t) = \{\operatorname{tok}(\mathcal{D}[h_j])\}$, ensuring consistency with both the entity list and domain constraints.
113	Otherwise, if $r_j$ is known, the mask falls back to all domain-valid head types: $S(t) = \{\operatorname{tok}(\tau) : \tau \in \operatorname{dom}(r_j)\}$.
114	If $r_j$ is not yet available, no semantic mask is applied and the grammar layer's entity-type membership constraint remains the sole guard.
115	
116	\paragraph{Tail type masking.}
117	At a \textsc{TailType} position, the processor has access to the current relation type $r_j$ and head type $\tau^h_j$ from the already-generated prefix.
118	It computes the set of valid tail types as $\operatorname{range}(r_j)$ and, if the tail entity $t_j$ is found in $\mathcal{D}$, further restricts to the registered type if it is domain/range-valid.
119	This implements the core prefix-decidable constraint: once $(h_j, r_j, \tau^h_j)$ are known, the valid $\tau^t_j$ values are fully determined by $\operatorname{range}(r_j)$.
120	
121	\paragraph{Implementation.}
122	Each type $\tau \in \mathcal{E}$ is mapped to the token ID of its first subword token under the model's tokenizer.
123	We pre-verify that these first-token IDs are unique across all entity types, which holds for both SciERC (6 types) and DocRED (6 types) with the Qwen3-8B tokenizer.
124	The semantic mask is applied by setting the logits of disallowed first-token IDs to $-\infty$.
125	
126	\subsubsection{Grammar-Semantic Interaction}
127	\label{sec:interaction}
128	
129	The semantic mask $S(t)$ is combined with the grammar mask $G(t)$ via conjunction:
130	%
131	\begin{equation}\label{eq:mask-conjunction}
132	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
133	\end{equation}
134	%
135	so a token is permitted only if it satisfies both structural and type-level constraints.
136	This conjunction embodies an \emph{enabling dependency}: the semantic layer's constraint lookup requires the relation type to be a valid member of $\mathcal{R}$---a property guaranteed only when the grammar layer is active.
137	Without grammar enforcement, the model may generate out-of-vocabulary relation types for which no $\operatorname{dom}$/$\operatorname{range}$ rules exist, rendering semantic masking ineffective.
138	Empirically, semantic-only constraints reduce DR by only 24\% (15.37\%\,$\to$\,11.65\%) and fail to eliminate RV (1.51\%) or ET (0.40\%) violations, whereas the full combination achieves 94\% DR reduction.
139	
140	When $S(t) \cap G(t) = \emptyset$---the semantic layer would mask out all grammar-valid tokens---the system falls back to grammar-only control, preserving structural validity at the cost of a potential type violation.
141	This \emph{grammar-first invariant} reflects a deliberate priority ordering: structural integrity is a hard constraint, while a type violation is a soft error detectable by downstream validation.
142	We formalize this invariant and analyze constraint composition in detail in Section~\ref{sec:composition}.
143	
144	
145	\subsection{Decoding Strategies}
146	\label{sec:strategies}
147	
148	We consider two decoding strategies that differ in how entity and relation generation are orchestrated.
149	
150	\paragraph{S1: Single-pass decoding.}
151	Both constraint layers are active throughout a single generation pass.
152	The entity registry is populated as entities are generated and is immediately available for relation-level type checking within the same pass.
153	This is the simpler and recommended strategy.
154	
155	\paragraph{S2: Two-pass decoding.}
156	In the first pass, the model generates only the entity list under grammar-only constraints.
157	The extracted entities are then used to compile an input-dependent grammar that additionally constrains head and tail entity names to match declared entities.
158	In the second pass, the model generates relations under this tighter grammar plus semantic constraints.
159	The two-pass separation aims to provide a more complete entity registry before relation generation begins, potentially improving type consistency.
160	
161	\paragraph{Comparison.}
162	On SciERC, S1 and S2 achieve comparable DR reduction (0.93\% vs.\ 0.97\%) but S1 yields higher relation F1 (8.36 vs.\ 8.03) and generates more triples (1,729 vs.\ 1,644).
163	S2 does not resolve the cross-field consistency trade-off introduced by semantic enforcement (CF 8.03\% vs.\ 9.90\% for S1, both elevated from 0.08\% unconstrained).
164	We adopt S1 as the primary configuration; S2 is retained as an ablation variant.
165	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "425e7b68-3f6c-47f5-a54c-ff078da5a74f",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "31227e2a-dadc-4cbf-82b5-90f76847885d",
  "sourceToolAssistantUUID": "425e7b68-3f6c-47f5-a54c-ff078da5a74f",
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

_source line 34 · 2026-05-14T10:51:39.745Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TbGPD5LTFMARRaX5pCMXfp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31227e2a-dadc-4cbf-82b5-90f76847885d",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LKkEjBCxrTPpWfuSaR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e5a6462-9849-411a-9714-4b135a669cd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xc1VSdrLUJX69WVQUQVPH5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6580,
      "cache_read_input_tokens": 42271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6580,
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

_source line 35 · 2026-05-14T10:51:39.757Z_

<details><summary>↩ Tool result · `toolu_01TbGPD5LTFMARRaX5pCMXfp`</summary>

```text
1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Results on SciERC}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC,
11	evaluating each constraint layer independently and in combination.
12	All experiments use Qwen3-8B in a zero-shot setting on 551 test documents
13	with identical prompts and decoding parameters;
14	only the active constraint layers differ.
15	
16	% ──────────────────────────────────────────
17	%  Table: SciERC five-way ablation
18	% ──────────────────────────────────────────
19	\begin{table}[t]
20	\centering
21	\small
22	\setlength{\tabcolsep}{3.6pt}
23	\begin{tabular}{@{}l rrrrr rr@{}}
24	\toprule
25	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
26	& \multicolumn{2}{c}{\textbf{F1}} \\
27	\cmidrule(lr){2-6} \cmidrule(l){7-8}
28	\textbf{Mode}
29	  & DR\,$\downarrow$ & $\Delta$DR
30	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
31	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
32	\midrule
33	Unconstrained
34	  & 15.37 & ---
35	  & 1.39  & 0.40
36	  & 0.08
37	  & 8.23  & 31.01 \\
38	Grammar
39	  & 14.84 & $\downarrow$3\%
40	  & \textbf{0} & \textbf{0}
41	  & 0.08
42	  & 8.23  & 30.98 \\
43	Semantic
44	  & 11.65 & $\downarrow$24\%
45	  & 1.51  & 0.40
46	  & 2.71
47	  & 8.15  & 31.01 \\
48	Full (S1)
49	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
50	  & \textbf{0} & \textbf{0}
51	  & 9.90
52	  & \textbf{8.36} & 30.98 \\
53	Full (S2)
54	  & 0.97  & $\downarrow$94\%
55	  & \textbf{0} & \textbf{0}
56	  & 8.03
57	  & 8.03  & \textbf{31.90} \\
58	\bottomrule
59	\end{tabular}
60	\caption{Five-way ablation on SciERC (551 documents, Qwen3-8B, zero-shot).
61	DR: domain/range violation rate;
62	RV: relation vocabulary violation rate;
63	ET: entity type violation rate;
64	CF: cross-field consistency violation rate.
65	$\Delta$DR: relative DR reduction vs.\ the unconstrained baseline.
66	$\downarrow$\,/\,$\uparrow$: lower\,/\,higher is better.
67	Best per column in \textbf{bold} (CF excluded---see text).
68	F1 scores are multiplied by 100.}
69	\label{tab:scierc-ablation}
70	\end{table}
71	
72	% ──────────────────────────────────────────
73	%  (a) Core result
74	% ──────────────────────────────────────────
75	\paragraph{Core result: near-complete DR elimination at zero F1 cost.}
76	The full two-layer constraint configuration (S1) reduces domain/range
77	violations from 15.37\% to 0.93\%, a 94\% relative reduction,
78	% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
79	while relation F1 moves from 8.23 to 8.36 (+0.13\,pp).
80	% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
81	This difference is not statistically significant and is best
82	characterized as F1-neutral: constraint enforcement neither improves
83	nor degrades extraction quality.
84	At the per-relation level, violations drop from 42.42\% to 2.82\% on
85	\textsc{Compare}, from 33.54\% to 1.21\% on \textsc{Feature-of}, and
86	reach 0\% on four of seven relation types
87	(\textsc{Conjunction}, \textsc{Hyponym-of}, \textsc{Part-of},
88	\textsc{Used-for}).
89	% phase2_scierc_full_s1 per_relation_dr: Compare=0.0282,
90	%   Feature-of=0.0121, Hyponym-of=0, Part-of=0, Used-for=0, Conjunction=0
91	However, full constraint enforcement elevates cross-field consistency
92	violations from 0.08\% to 9.90\%;
93	% phase2_scierc_unconstrained: CF=0.0008; phase2_scierc_full_s1: CF=0.099
94	we analyze this trade-off in Section~\ref{sec:discussion}.
95	
96	% ──────────────────────────────────────────
97	%  (b) Grammar layer
98	% ──────────────────────────────────────────
99	\paragraph{Grammar layer: cost-free structural guarantees.}
100	Grammar-only constraints completely eliminate both relation vocabulary
101	violations (1.39\%\,$\to$\,0\%) and entity type violations
102	(0.40\%\,$\to$\,0\%), with no measurable impact on F1
103	(R-F1 8.23, E-F1 30.98).
104	% phase2_scierc_grammar_only: RV=0, ET=0, R-F1=0.0823, E-F1=0.3098
105	Domain/range violations remain effectively unchanged
106	(15.37\%\,$\to$\,14.84\%, $-$0.53\,pp), confirming that grammar
107	constraints enforce output structure---valid JSON, correct relation
108	vocabulary, valid entity types---but do not address cross-field
109	semantic constraints.
110	% phase2_scierc_grammar_only: DR=0.1484
111	The grammar layer thus provides two categories of violation elimination
112	at zero cost, establishing the structural preconditions on which the
113	semantic layer depends.
114	
115	% ──────────────────────────────────────────
116	%  (c) Enabling dependency
117	% ──────────────────────────────────────────
118	\paragraph{Enabling dependency: grammar enables semantic enforcement.}
119	Applying semantic constraints alone reduces DR by only 24\%
120	(15.37\%\,$\to$\,11.65\%) and, critically, cannot eliminate
121	relation vocabulary violations (RV\,=\,1.51\%) or entity type
122	violations (ET\,=\,0.40\%).
123	% phase2_scierc_semantic_only: DR=0.1165, RV=0.0151, ET=0.004
124	When the grammar layer is added (Full S1), DR drops a further 92\%
125	relative to the semantic-only configuration
126	(11.65\%\,$\to$\,0.93\%).
127	% phase2_scierc_full_s1: DR=0.0093; delta=(11.65-0.93)/11.65=0.920
128	This demonstrates an \emph{enabling dependency} rather than mere
129	additivity: without grammar-enforced vocabulary constraints, the
130	semantic layer encounters out-of-vocabulary relation types for which
131	no domain/range rules exist, rendering its type checking ineffective.
132	The two layers are therefore complementary with a prerequisite
133	structure---grammar must be active for semantic constraints to reach
134	their full enforcement capacity.
135	
136	% ──────────────────────────────────────────
137	%  (d) S1 vs S2
138	% ──────────────────────────────────────────
139	\paragraph{S1 vs.\ S2: single-pass suffices.}
140	The two-pass strategy (S2) achieves comparable DR
141	(0.97\% vs.\ 0.93\%) but lower relation F1
142	(8.03 vs.\ 8.36, $-$0.33\,pp) and generates fewer relation triples
143	(1{,}644 vs.\ 1{,}729).
144	% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, triples=1644
145	% phase2_scierc_full_s1: DR=0.0093, R-F1=0.0836, triples=1729
146	S2 shows a modestly lower CF rate (8.03\% vs.\ 9.90\%), but both
147	configurations exhibit substantially elevated CF relative to the
148	unconstrained baseline (0.08\%), indicating that two-pass decoding
149	does not resolve the cross-field consistency trade-off
150	(Section~\ref{sec:discussion}).
151	% phase2_scierc_full_s2: CF=0.0803; phase2_scierc_full_s1: CF=0.099
152	The two-pass separation offers no clear advantage over single-pass
153	enforcement; we adopt S1 as the primary configuration for its
154	simplicity and marginally stronger extraction performance.
155	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e5a6462-9849-411a-9714-4b135a669cd1",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "4f34d67d-df29-4b63-bb36-0a4629563a43",
  "sourceToolAssistantUUID": "5e5a6462-9849-411a-9714-4b135a669cd1",
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

_source line 36 · 2026-05-14T10:51:45.977Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KMynxHcEDrssWqRqz9TtRk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f34d67d-df29-4b63-bb36-0a4629563a43",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LKkEjBCxrTPpWfuSaR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3d2d01b-990b-4351-b48a-2154f45d233e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xc1VSdrLUJX69WVQUQVPH5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6580,
      "cache_read_input_tokens": 42271,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6580
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 259,
          "cache_read_input_tokens": 42271,
          "cache_creation_input_tokens": 6580,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6580,
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

_source line 37 · 2026-05-14T10:51:45.982Z_

<details><summary>↩ Tool result · `toolu_01KMynxHcEDrssWqRqz9TtRk`</summary>

```text
1	\section{Violation Landscape}
2	\label{sec:violation_landscape}
3	
4	Before presenting our constrained decoding framework, we first quantify how frequently LLMs violate ontological constraints during information extraction.
5	This analysis serves two purposes: it establishes the practical severity of unconstrained generation and identifies which constraint categories demand enforcement at decoding time versus those addressable through prompting alone.
6	
7	\subsection{Experimental Setup}
8	\label{sec:violation_setup}
9	
10	We evaluate a strong open-weight model, Qwen3-8B~\cite{qwen2025qwen3}, under zero-shot greedy decoding on two IE benchmarks that differ substantially in ontological complexity:
11	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relation types, avg.\ 26.1 valid type pairs per relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents, 96 relation types, avg.\ 5.68 valid type pairs per relation).
12	Both datasets ship with typed entity and relation schemas, enabling automatic constraint checking.
13	
14	We measure four categories of ontological violation:
15	\begin{itemize}[nosep,leftmargin=*]
16	    \item \textbf{Domain/Range (DR):} a predicted triple $(h,r,t)$ satisfies $(\mathrm{type}(h), \mathrm{type}(t)) \notin \sigma(r)$, where $\sigma(r)$ is the set of valid subject--object type pairs for relation $r$.
17	    \item \textbf{Relation Vocabulary (RV):} the predicted relation type $r \notin \mathcal{R}$.
18	    \item \textbf{Entity Type (ET):} the predicted entity type $e \notin \mathcal{E}$.
19	    \item \textbf{Cross-Field Consistency (CF):} the same entity span is assigned different types across distinct triples within one instance.
20	\end{itemize}
21	
22	\subsection{Violation Distribution}
23	\label{sec:violation_distribution}
24	
25	Table~\ref{tab:prompt_comparison} reports violation rates on both benchmarks.
26	On SciERC (1{,}724 predicted triples, 2{,}474 entities), domain/range violations affect 15.37\% of triples, while RV, ET, and CF violations are comparatively rare at 1.39\%, 0.40\%, and 0.08\%, respectively.
27	On DocRED (16{,}540 triples, 19{,}099 entities), DR violations reach 18.70\%---comparable to SciERC despite DocRED's ontology being 14$\times$ larger.
28	This parity suggests that DR violation rates are driven primarily by \emph{constraint tightness} (valid type pairs per relation) rather than ontology size: DocRED averages only 5.68 valid pairs per relation versus SciERC's 26.1.
29	
30	RV violations on DocRED are dramatically higher (28.90\% vs.\ 1.39\%), indicating that 96 relation types exceed the model's capacity to faithfully reproduce a target vocabulary from a single in-context specification.
31	ET violations follow a similar trend (7.50\% vs.\ 0.40\%).
32	CF violations remain negligible on both datasets (0.08\%), suggesting that within-instance type coherence is largely maintained even without explicit enforcement.
33	
34	\subsection{Per-Relation Analysis}
35	\label{sec:per_relation}
36	
37	Figure~\ref{fig:per_relation_dr} breaks down DR violation rates by relation type on SciERC.
38	Violation rates vary by over 40 percentage points across relations:
39	\textsc{Compare} exhibits the highest rate at 42.4\% (28/66 triples), followed by \textsc{Feature-of} at 33.5\% (163/486), \textsc{Part-of} at 25.0\% (18/72), and \textsc{Evaluate-for} at 24.1\% (32/133).
40	At the other extreme, \textsc{Used-for} violates at only 0.76\% (6/787) and \textsc{Conjunction} at 0\% (0/32).
41	
42	This distribution correlates with constraint tightness: \textsc{Compare} permits only a few valid type pairs in the SciERC schema, leaving minimal room for type substitution, whereas \textsc{Used-for} and \textsc{Conjunction} accept a broad range of subject--object type combinations.
43	The pattern implies that violations are not random generation noise but systematic failures to satisfy narrow type constraints---precisely the setting where decoding-time enforcement is most needed.
44	
45	\subsection{Prompt Insufficiency}
46	\label{sec:prompt_insufficiency}
47	
48	A natural question is whether explicitly stating domain/range constraints in the prompt suffices to eliminate violations.
49	We test \emph{schema-informed prompting}, which augments the extraction prompt with the full list of valid type pairs for each relation.
50	
51	On SciERC, schema-informed prompting reduces DR violations from 15.37\% to 5.78\% (a 62.4\% relative reduction) and lowers RV from 1.39\% to 0.30\% and ET from 0.40\% to 0\% (Table~\ref{tab:prompt_comparison}).
52	On DocRED, the reduction is weaker: DR drops from 18.70\% to 12.84\% ($-$31.3\%), RV from 28.90\% to 18.40\%, and ET from 7.50\% to 0.61\%.
53	McNemar's test confirms that all four violation-category improvements are statistically significant ($p < 0.01$) on both datasets.
54	
55	However, aggregate improvements mask per-relation instability.
56	On SciERC, schema-informed prompting reduces DR for \textsc{Feature-of} by 22.3 percentage points and \textsc{Part-of} by 22.5~pp, but \emph{increases} DR for \textsc{Evaluate-for} by 5.8~pp (Figure~\ref{fig:per_relation_dr}).
57	This reversal---where adding constraint information to the prompt worsens compliance on a specific relation---demonstrates that prompt-based approaches lack the guarantee of monotonic improvement across all constraint categories.
58	
59	Two findings emerge from this analysis.
60	First, prompt-based schema enforcement scales poorly with ontological complexity: the relative DR reduction on DocRED (31.3\%) is roughly half that on SciERC (62.4\%), and RV violations remain at 18.40\% even after prompting.
61	Second, even on the simpler SciERC ontology, prompt interventions are unreliable at the per-relation level.
62	These limitations motivate a decoding-time mechanism that enforces constraints \emph{by construction} rather than by instruction, which we present in Section~\ref{sec:method}.
63	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3d2d01b-990b-4351-b48a-2154f45d233e",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "5a6c1f12-7c41-48bd-be54-97eca15d200f",
  "sourceToolAssistantUUID": "d3d2d01b-990b-4351-b48a-2154f45d233e",
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

_source line 38 · 2026-05-14T10:51:50.914Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RZ1AqkG7zANxzfgL44rLG5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a6c1f12-7c41-48bd-be54-97eca15d200f",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LLcaPT2o1ck6ch7sn7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e8b19ce-9818-4b5c-9b63-5cbe353f6e66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Ta18wGhAPfjWMTcJPbW26",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8892,
      "cache_read_input_tokens": 48851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8892,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 39 · 2026-05-14T10:51:50.919Z_

<details><summary>↩ Tool result · `toolu_01RZ1AqkG7zANxzfgL44rLG5`</summary>

```text
1	% Section 4 subsection: Constraint Composition
2	% Draft — OntoCoDec Framework
3	
4	\paragraph{Constraint Composition.}
5	
6	At each decoding step $t$, both layers produce a binary token mask over the vocabulary $V$.
7	Let $G(t) \subseteq V$ denote the set of tokens permitted by the grammar layer (valid JSON structure and ontology-vocabulary membership),
8	and $S(t) \subseteq V$ the set permitted by the semantic layer (domain/range type compliance given the current entity registry state).
9	The final mask is their conjunction:
10	%
11	\begin{equation}\label{eq:composition}
12	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
13	\end{equation}
14	%
15	so that a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
16	The conjunction is asymmetric in an important sense: the semantic layer operates \emph{strictly within} the grammar-valid set, i.e., $S(t)$ is defined only over $G(t)$.
17	This reflects the enabling dependency described in \S\ref{sec:overview}: grammar validity is a precondition for semantic enforcement, because the semantic layer must identify the current relation type to look up its domain/range rules—an operation that is only well-defined when the relation type belongs to the ontology vocabulary.
18	
19	\paragraph{Grammar-First Fallback.}
20	
21	The conjunction in Eq.~\eqref{eq:composition} requires the precondition $S(t) \cap G(t) \neq \emptyset$: at least one token must be simultaneously grammar-valid and semantically valid.
22	When this precondition is violated—which can occur under tight ontology constraints where the allowed entity types for a relation do not overlap with the grammar-valid tokens at a particular position—na\"{\i}ve application of the semantic mask sets all grammar-valid tokens to $-\infty$ while grammar-invalid tokens retain finite (though heavily penalized) logits.
23	The resulting argmax selects a grammar-invalid token, breaking JSON structure.
24	We enforce a \emph{grammar-first fallback rule}: before applying the semantic mask, we verify that at least one semantically allowed type token has a logit above a grammar-validity threshold $\tau_g = -10^{8}$.
25	If $S(t) \cap G(t) = \emptyset$, semantic masking is skipped entirely, and the grammar layer alone controls token selection.
26	This reflects a deliberate priority ordering: structural integrity (grammar) is a hard constraint, while a type violation is a soft error detectable by downstream validation.
27	
28	
29	\paragraph{Decidability Taxonomy.}
30	
31	Not all ontology constraints can be enforced at the same point during autoregressive generation.
32	We classify them by \emph{when} sufficient information becomes available:
33	%
34	\begin{enumerate}[leftmargin=*,nosep]
35	  \item \textbf{Local constraints} require only the current token. Entity-type and relation-vocabulary membership fall in this class: each candidate token can be checked against the ontology vocabulary independently, which the grammar layer handles via CFG and enum rules.
36	  \item \textbf{Prefix-decidable constraints} require the current token plus previously generated context. Domain/range constraints are prefix-decidable: once the head entity type and relation type have been generated, the valid tail entity types are fully determined. The semantic layer implements this via a stateful entity registry that tracks decoded types and activates the appropriate logit mask at each type-bearing position.
37	  \item \textbf{Non-local constraints} require information not yet generated. Forward coreference—where a later mention determines the type of an earlier one—is inherently non-local and falls outside the scope of single-pass left-to-right decoding.
38	\end{enumerate}
39	%
40	OntoCoDec's two-layer design covers the first two classes: grammar for local, semantic for prefix-decidable. The non-local class motivates the two-pass strategy (S2, \S\ref{sec:s2}), which partially addresses cross-field consistency by separating entity extraction from relation generation, though it does not fully resolve forward coreference (\S\ref{sec:limitations}).
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e8b19ce-9818-4b5c-9b63-5cbe353f6e66",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "84814c4d-f792-4b48-b076-6b14f0db0ed5",
  "sourceToolAssistantUUID": "4e8b19ce-9818-4b5c-9b63-5cbe353f6e66",
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

_source line 40 · 2026-05-14T10:51:51.307Z_

<details open><summary>🔧 Tool call — Read · `toolu_015mArrQzfqhkR7UEzMKXEGQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84814c4d-f792-4b48-b076-6b14f0db0ed5",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LLcaPT2o1ck6ch7sn7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75fdb0b7-da05-46b9-92df-48ec184484d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Ta18wGhAPfjWMTcJPbW26",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8892,
      "cache_read_input_tokens": 48851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8892,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 41 · 2026-05-14T10:51:51.312Z_

<details><summary>↩ Tool result · `toolu_015mArrQzfqhkR7UEzMKXEGQ`</summary>

```text
1	% Section 2: Background for OntoCoDec paper
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\subsection{IE Ontology Structure}
7	\label{sec:bg:ontology}
8	
9	An information extraction ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines a set of entity types $\mathcal{E}$, a set of relation types $\mathcal{R}$, and a domain/range mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ that specifies, for each relation type $r \in \mathcal{R}$, the set of valid (head type, tail type) pairs.
10	A triple $(h, r, t)$ is \emph{type-valid} under $\mathcal{O}$ if and only if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
11	For example, SciERC~\citep{luan2018scierc} defines $|\mathcal{E}|=6$ entity types, $|\mathcal{R}|=7$ relation types, and $|\sigma(r)|$ ranges from 17 (\textsc{Compare}) to 35 (\textsc{Used-for}) valid type pairs per relation, out of $|\mathcal{E}|^2 = 36$ possible.
12	We define the \emph{constraint tightness} of a relation $r$ as the fraction of the type-pair space it excludes: $1 - |\sigma(r)| / |\mathcal{E}|^2$.
13	Tighter constraints leave fewer valid options for the model, increasing the likelihood of violations.
14	Empirically, constraint tightness varies substantially both within and across datasets.
15	Within SciERC, the overall average of 24.0 valid pairs (out of 36) masks sharp per-relation differences: \textsc{Compare} admits only 17 pairs (tightness 0.53), while \textsc{Used-for} admits 35 (tightness 0.03).
16	DocRED~\citep{yao2019docred} exhibits far tighter constraints overall, with relations averaging only 5.68 valid pairs (out of 36; tightness 0.84), reflecting fundamentally different ontology designs.
17	
18	\subsection{Grammar-Constrained Decoding}
19	\label{sec:bg:gcd}
20	
21	In autoregressive language model generation, each token $y_t$ is sampled from $p(\cdot \mid y_{<t}, x)$ where $x$ is the input prompt.
22	Grammar-constrained decoding restricts this distribution at each step by applying a token-level mask $M_g \in \{0, 1\}^{|V|}$ that zeros out tokens incompatible with a target grammar.
23	XGrammar~\citep{dong2025xgrammar} compiles a JSON Schema into a pushdown automaton, computing the set of valid next tokens from the current automaton state at each decoding step.
24	This enables enforcement of structural constraints---valid JSON syntax, enumerated vocabularies---with negligible latency overhead by precomputing context-independent token sets and caching adaptive token sets per grammar state.
25	Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} provide similar capabilities through finite-state machine and interleaved grammar-based approaches, respectively.
26	
27	However, grammar-constrained decoding is inherently limited to constraints expressible as context-free grammars.
28	Cross-field semantic constraints---such as ``if the relation is \textsc{Feature-of}, then the head entity type must be \textsc{Method} or \textsc{OtherScientificTerm}''---depend on previously generated field values and cannot be captured by a static CFG.
29	This limitation motivates a second constraint layer that tracks generation state and enforces semantic validity dynamically.
30	
31	\subsection{Problem Statement}
32	\label{sec:bg:problem}
33	
34	Given an IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ and an autoregressive language model $\mathcal{M}$, we seek to compile $\mathcal{O}$ into decoding-time constraints $\mathcal{C}$ such that the constrained output of $\mathcal{M}$ satisfies:
35	\begin{enumerate}[label=(\alph*)]
36	    \item \textbf{Structural validity}: the output is well-formed JSON conforming to the IE schema, with all entity types $\in \mathcal{E}$ and relation types $\in \mathcal{R}$;
37	    \item \textbf{Type validity}: for every extracted triple $(h, r, t)$, the type assignment is ontology-consistent: $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
38	\end{enumerate}
39	
40	Condition (a) is context-free and directly expressible via grammar-constrained decoding.
41	Condition (b) is context-sensitive: enforcing domain/range constraints for a relation requires knowing the types of its argument entities, which are generated earlier in the sequence.
42	Crucially, however, (b) is \emph{prefix-decidable}---at the point where a relation's argument type is being generated, all information needed to evaluate the constraint (the relation type and the entity registry built from prior tokens) is available in the already-generated prefix.
43	This prefix-decidability property, combined with a stateful entity registry, makes (b) amenable to token-level enforcement during autoregressive decoding, despite being beyond the expressiveness of context-free grammars.
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75fdb0b7-da05-46b9-92df-48ec184484d6",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "2cf039db-81be-4e63-9a15-e94f28c1f628",
  "sourceToolAssistantUUID": "75fdb0b7-da05-46b9-92df-48ec184484d6",
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

_source line 42 · 2026-05-14T10:51:51.685Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CzgHyKFeWEWmXwuKwQc9Z3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cf039db-81be-4e63-9a15-e94f28c1f628",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LLcaPT2o1ck6ch7sn7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0837e9f8-4fb7-489c-b476-9e1ef4f02ce8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Ta18wGhAPfjWMTcJPbW26",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8892,
      "cache_read_input_tokens": 48851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8892,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 43 · 2026-05-14T10:51:51.689Z_

<details><summary>↩ Tool result · `toolu_01CzgHyKFeWEWmXwuKwQc9Z3`</summary>

```text
1	% Section 7 — Conclusion
2	% Data source: Phase 2 SciERC registry experiments + Phase 0 DocRED
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
4	%          phase0_scierc_unconstrained, phase0_docred_unconstrained
5	% All numbers verified against registry 2026-05-14.
6	
7	We presented OntoCoDec, a framework that automatically compiles IE ontology schemas into token-level decoding constraints to enforce type validity at generation time.
8	Our work makes three contributions.
9	
10	First, we conducted the first systematic study of ontological constraint violations in LLM-based IE (\S\ref{sec:violation_landscape}).
11	Across two benchmarks with substantially different ontology sizes---SciERC (7~relations) and DocRED (96~relations)---we found that domain/range violation rates are comparable (15.37\% vs.\ 18.70\%), % exp_ids: phase0_scierc_unconstrained, phase0_docred_unconstrained
12	indicating that violation severity is driven by \emph{constraint tightness} (valid type pairs per relation) rather than ontology scale.
13	
14	Second, we introduced a two-layer constraint architecture that decomposes ontological enforcement into complementary mechanisms:
15	a \emph{grammar layer} (XGrammar CFG) that eliminates structural violations (RV, ET\,$\to$\,0\%) and a \emph{semantic layer} (TypeConstraintProcessor with a stateful entity registry) that enforces domain/range constraints at the token level. % exp_id: phase2_scierc_grammar_only
16	The grammar layer serves as an enabling prerequisite for the semantic layer; the two compose via bitwise AND over candidate token sets.
17	
18	Third, we validated OntoCoDec empirically.
19	On SciERC, the full system reduces domain/range violations from 15.37\% to 0.93\%---a 94\% relative reduction---while completely eliminating RV and ET violations, with no significant impact on relation F1 ($+$0.13 percentage points, $p > 0.05$). % exp_id: phase2_scierc_full_s1
20	\placeholder{DocRED DR result: unconstrained DR=18.70\% $\to$ full system DR=??\%, with RV 28.90\%$\to$??\% and ET 7.50\%$\to$??\%.}
21	
22	\paragraph{Limitations.}
23	Several limitations qualify these findings.
24	The semantic layer introduces cross-field consistency (CF) violations: CF rises from 0.08\% under unconstrained decoding to 9.90\% with full constraints. % exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1
25	This is a systematic consequence of per-relation independent type enforcement---when the same entity appears across multiple triples, each relation's domain/range constraint may assign it a different type, producing entity-versus-relation type drift.
26	The grammar layer alone does not elevate CF (0.08\%, matching the unconstrained baseline), confirming that CF is entirely attributable to the semantic layer. % exp_id: phase2_scierc_grammar_only
27	Resolving this cross-relation type coherence problem is an open challenge, not a trivial implementation fix.
28	Beyond CF, all experiments use a single model (Qwen3-8B); while the constraint compiler is model-agnostic by design, cross-model validation remains incomplete.
29	Results are reported on two datasets under zero-shot prompting only, and integration with fine-tuned models has not been explored.
30	
31	\paragraph{Future Work.}
32	We identify four directions.
33	(1)~Cross-model validation on architectures such as Llama-3.1-8B and quantized 70B-class models to verify model-agnostic generalization.
34	(2)~Global entity-level type consensus during decoding---maintaining a shared entity registry across all relations within an instance---to resolve CF violations.
35	(3)~Integration with fine-tuned models, combining constraint-aware training objectives with decoding-time enforcement.
36	(4)~Extension to non-English ontologies to evaluate cross-lingual applicability.
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0837e9f8-4fb7-489c-b476-9e1ef4f02ce8",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "a6401a74-3390-4ab7-8ac8-b83c61ff74df",
  "sourceToolAssistantUUID": "0837e9f8-4fb7-489c-b476-9e1ef4f02ce8",
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

_source line 44 · 2026-05-14T10:51:54.459Z_

Now let me check the literature survey artifacts for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6401a74-3390-4ab7-8ac8-b83c61ff74df",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LM2w6ZM2WUx87S4NGf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "588afe73-7e57-4fb9-8584-0df02c61da1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7LXVqNf46azLP3u844e8z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4076,
      "cache_read_input_tokens": 57743,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4076,
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

_source line 45 · 2026-05-14T10:51:56.563Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01W5keKxXz57wBXtssHBUa6F`</summary>

```json
{
  "pattern": "**/literature_survey*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "588afe73-7e57-4fb9-8584-0df02c61da1e",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LM2w6ZM2WUx87S4NGf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a917df89-311d-436c-9f84-d151b20e7230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7LXVqNf46azLP3u844e8z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4076,
      "cache_read_input_tokens": 57743,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4076,
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

_source line 46 · 2026-05-14T10:51:56.577Z_

<details><summary>↩ Tool result · `toolu_01W5keKxXz57wBXtssHBUa6F`</summary>

```text
artifacts/literature_survey_constrained_decoding_ie.md
artifacts/literature_survey_ontology_constrained_ie.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a917df89-311d-436c-9f84-d151b20e7230",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "7ad376a4-997a-4f25-b4c2-bb0c0d249d26",
  "sourceToolAssistantUUID": "a917df89-311d-436c-9f84-d151b20e7230",
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

_source line 47 · 2026-05-14T10:51:56.981Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SUVqWXVYTikEvua2RQuHVh`</summary>

```json
{
  "pattern": "**/literature_map*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ad376a4-997a-4f25-b4c2-bb0c0d249d26",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LM2w6ZM2WUx87S4NGf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e66b433a-7762-4dc5-989d-812e31a430a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7LXVqNf46azLP3u844e8z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4076,
      "cache_read_input_tokens": 57743,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4076
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 57743,
          "cache_creation_input_tokens": 4076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4076,
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

_source line 48 · 2026-05-14T10:51:56.993Z_

<details><summary>↩ Tool result · `toolu_01SUVqWXVYTikEvua2RQuHVh`</summary>

```text
artifacts/literature_map.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e66b433a-7762-4dc5-989d-812e31a430a7",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "807af991-3c22-4df2-8c64-e9c8a7238a35",
  "sourceToolAssistantUUID": "e66b433a-7762-4dc5-989d-812e31a430a7",
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

_source line 49 · 2026-05-14T10:51:59.743Z_

<details open><summary>🔧 Tool call — Read · `toolu_014v45HFu9wLnL1PujXrGvGW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "807af991-3c22-4df2-8c64-e9c8a7238a35",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LMRYPex2dcQc4XoggU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1bb7989d-6407-4afc-b699-f5f0990616b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCtrhdjyrSBk383iWZFSao",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 302,
      "cache_read_input_tokens": 61819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 302,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 50 · 2026-05-14T10:51:59.750Z_

<details><summary>↩ Tool result · `toolu_014v45HFu9wLnL1PujXrGvGW`</summary>

```text
1	# OntoCoDec Literature Map
2	# Generated: 2026-05-13
3	# Scope: Constrained Decoding for IE / Schema-Guided IE / Type Constraint Enforcement (2020-2026)
4	
5	novelty_assessment:
6	  claim: "Compile ontology domain/range axioms into decoding-time semantic constraints (LogitsProcessor) for LLM-based IE"
7	  verdict: "Novel — no prior work does this"
8	  gap_table:
9	    - level: "Syntactic (valid JSON)"
10	      ie_task: true
11	      decode_time: true
12	      prior_work: "GCD (EMNLP'23), XGrammar, Outlines, SGLang"
13	    - level: "Vocabulary (valid entity/relation names)"
14	      ie_task: true
15	      decode_time: true
16	      prior_work: "GENRE (ICLR'21), iNERD (SLT'24), AdaKGC (EMNLP'23)"
17	    - level: "Structural (generation order)"
18	      ie_task: true
19	      decode_time: true
20	      prior_work: "ATG (AAAI'24), JoinER-BART (TASLP'23), EnriCo (2024)"
21	    - level: "Semantic (domain/range type compatibility)"
22	      ie_task: false  # <-- THE GAP
23	      decode_time: false
24	      prior_work: "NONE for IE"
25	    - level: "Semantic (type checking)"
26	      ie_task: false  # code gen only
27	      decode_time: true
28	      prior_work: "MGD (NeurIPS'23), Synchromesh (NeurIPS'22), PLDI'25"
29	    - level: "Semantic (ontology compliance)"
30	      ie_task: true  # KG construction
31	      decode_time: false  # post-hoc only
32	      prior_work: "RELATE (2025), ODKE+ (Apple 2025), OntoLogX (2025)"
33	  framing: >
34	    OntoCoDec brings type-constrained generation — previously applied only to
35	    programming languages — to information extraction, by compiling IE ontology
36	    axioms into decoding-time semantic constraints that prevent, rather than
37	    detect, type violations.
38	
39	most_relevant_papers:
40	  - id: pldi2025_type_constrained_codegen
41	    title: "Type-Constrained Code Generation via Prefix Automata"
42	    venue: PLDI
43	    year: 2025
44	    arxiv: "2504.09246"
45	    method: "Compiles type systems into prefix automata for token-level logits masking during code generation. Reduces compilation errors >50%."
46	    relation: "Closest analog — same mechanism (type system → automaton → logits mask) but for programming language types, not IE ontology types."
47	    category: competitor_analog
48	    must_cite: true
49	
50	  - id: mgd_neurips2023
51	    title: "Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context"
52	    venue: NeurIPS
53	    year: 2023
54	    method: "Uses static analysis monitors to enforce type-checking during code generation. SantaCoder-1.1B + MGD outperforms text-davinci-003."
55	    relation: "Type checking at decode time for code; OntoCoDec does type checking at decode time for IE."
56	    category: competitor_analog
57	    must_cite: true
58	
59	  - id: synchromesh_neurips2022
60	    title: "Synchromesh: Reliable Code Generation from Pre-trained Language Models"
61	    venue: NeurIPS
62	    year: 2022
63	    method: "Constrained Semantic Decoding (CSD) enforcing syntax + types + scope simultaneously for code generation."
64	    relation: "Pioneer of semantic constraints at decode time. Foundational reference."
65	    category: foundational
66	    must_cite: true
67	
68	  - id: geng_emnlp2023
69	    title: "Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning"
70	    venue: EMNLP
71	    year: 2023
72	    method: "Input-dependent CFGs for NER, RE, entity disambiguation. Syntactic constraints only."
73	    relation: "Direct precursor for constrained decoding in IE, but no semantic constraints."
74	    category: precursor
75	    must_cite: true
76	
77	  - id: odke_apple2025
78	    title: "ODKE+: Ontology-Driven Knowledge Extraction at Scale"
79	    venue: arXiv (Apple)
80	    year: 2025
81	    method: "Ontology snippet prompting + Grounder LLM post-validation. 98.8% precision on 19M facts."
82	    relation: "Production-scale ontology-guided IE, but post-processing not decode-time. Key baseline."
83	    category: competitor_baseline
84	    must_cite: true
85	
86	papers_by_dimension:
87	
88	  constrained_decoding_for_ie:
89	    - id: geng_emnlp2023
90	      title: "Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning"
91	      venue: EMNLP 2023
92	      constraint_level: syntactic
93	      must_cite: true
94	
95	    - id: inerd_slt2024
96	      title: "iNERD: Token Masking for NER with Constrained Decoding"
97	      venue: IEEE SLT 2024
98	      constraint_level: vocabulary
99	      must_cite: false
100	
101	    - id: adakgc_emnlp2023
102	      title: "AdaKGC: Schema-Constrained Dynamic Decoding"
103	      venue: EMNLP 2023 Findings
104	      constraint_level: vocabulary_trie
105	      must_cite: true
106	
107	    - id: atg_aaai2024
108	      title: "ATG: Joint Entity-RE with Autoregressive Text Generation"
109	      venue: AAAI 2024
110	      constraint_level: structural
111	      must_cite: false
112	
113	    - id: codeie_acl2023
114	      title: "CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors"
115	      venue: ACL 2023
116	      constraint_level: code_structure
117	      must_cite: false
118	
119	    - id: gollie_iclr2024
120	      title: "GoLLIE: Annotation Guidelines as Code for Zero-Shot IE"
121	      venue: ICLR 2024
122	      constraint_level: code_structure
123	      must_cite: true
124	
125	    - id: grammar_cd_clinical_2024
126	      title: "Grammar-Constrained Decoding for Clinical Trial IE"
127	      venue: Frontiers in AI 2024
128	      constraint_level: syntactic
129	      must_cite: false
130	
131	    - id: slot_emnlp2025
132	      title: "SLOT: Structured LLM Output Toolkit"
133	      venue: EMNLP 2025 Industry
134	      constraint_level: syntactic
135	      must_cite: false
136	
137	    - id: enrico_2024
138	      title: "EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction"
139	      venue: 2024
140	      constraint_level: structural_asp
141	      must_cite: false
142	
143	  constrained_decoding_frameworks:
144	    - id: xgrammar
145	      title: "XGrammar: Flexible and Efficient Grammar-Guided Generation"
146	      year: 2024
147	      constraint_level: syntactic
148	      note: "100x faster than prior methods. JSON Schema / CFG."
149	      must_cite: true
150	
151	    - id: outlines
152	      title: "Outlines: Structured Text Generation"
153	      year: 2024
154	      constraint_level: syntactic
155	      must_cite: false
156	
157	    - id: guidance
158	      title: "Guidance (Microsoft): Constrained Generation"
159	      year: 2023
160	      constraint_level: syntactic
161	      must_cite: false
162	
163	    - id: lmql
164	      title: "LMQL: Programming Large Language Models"
165	      year: 2023
166	      constraint_level: syntactic_scripting
167	      must_cite: false
168	
169	  semantic_constrained_decoding_non_ie:
170	    - id: pldi2025_type_constrained_codegen
171	      title: "Type-Constrained Code Generation via Prefix Automata"
172	      venue: PLDI 2025
173	      constraint_level: semantic_type_checking
174	      must_cite: true
175	
176	    - id: mgd_neurips2023
177	      title: "Monitor-Guided Decoding"
178	      venue: NeurIPS 2023
179	      constraint_level: semantic_type_checking
180	      must_cite: true
181	
182	    - id: synchromesh_neurips2022
183	      title: "Synchromesh: Constrained Semantic Decoding"
184	      venue: NeurIPS 2022
185	      constraint_level: semantic_full
186	      must_cite: true
187	
188	    - id: itergen_iclr2025
189	      title: "IterGen: Grammar-Guided Generation with Semantic-Aware Backtracking"
190	      venue: ICLR 2025
191	      constraint_level: semantic_backtracking
192	      must_cite: false
193	
194	    - id: crane_icml2025
195	      title: "CRANE: Balancing Syntactic+Semantic Constraints with Reasoning"
196	      venue: ICML 2025
197	      constraint_level: semantic
198	      note: "Shows strict constraints can degrade reasoning — relevant risk for OntoCoDec."
199	      must_cite: true
200	
201	    - id: smc_iclr2025
202	      title: "SMC-based Syntactic+Semantic Control for LLM Generation"
203	      venue: ICLR 2025 Oral
204	      constraint_level: semantic
205	      note: "Small models beat 8x larger ones with constraints."
206	      must_cite: false
207	
208	    - id: grammar_aligned_neurips2024
209	      title: "Grammar-Aligned Decoding"
210	      venue: NeurIPS 2024
211	      note: "Addresses distribution distortion from naive grammar masking."
212	      must_cite: true
213	
214	  schema_ontology_guided_ie:
215	    - id: odke_apple2025
216	      title: "ODKE+: Ontology-Driven Knowledge Extraction"
217	      venue: arXiv 2025 (Apple)
218	      schema_usage: prompt + post_validation
219	      must_cite: true
220	
221	    - id: knowcoder_acl2024
222	      title: "KnowCoder: Coding Structured Knowledge from LLMs"
223	      venue: ACL 2024
224	      schema_usage: training_code_hierarchy
225	      note: "29K entity types from Wikidata as Python class hierarchy"
226	      must_cite: true
227	
228	    - id: spires_2024
229	      title: "SPIRES/OntoGPT: Ontology-Based LLM Extraction"
230	      venue: Bioinformatics 2024
231	      schema_usage: prompt + post_grounding
232	      must_cite: true
233	
234	    - id: oneke_www2025
235	      title: "OneKE: Multi-Agent Knowledge Extraction"
236	      venue: WWW 2025
237	      schema_usage: agent_reflection
238	      must_cite: false
239	
240	    - id: relate_2025
241	      title: "RELATE: Biomedical Relation Extraction with Ontology Mapping"
242	      venue: arXiv 2025
243	      schema_usage: post_mapping
244	      must_cite: false
245	
246	    - id: ontologx_2025
247	      title: "OntoLogX: SHACL Validation for LLM-Generated KGs"
248	      venue: arXiv 2025
249	      schema_usage: post_validation_shacl
250	      note: "Iterative correction reduces violations ~10x"
251	      must_cite: true
252	
253	    - id: instructuie_2023
254	      title: "InstructUIE: Multi-Task Instruction Tuning for UIE"
255	      venue: 2023
256	      schema_usage: instruction_prompt
257	      must_cite: false
258	
259	    - id: ekaw2024_ontology_beam
260	      title: "Ontology-Constrained Clinical Summaries"
261	      venue: EKAW 2024
262	      arxiv: "2411.15666"
263	      schema_usage: soft_beam_bias
264	      note: "Soft constraint via beam scoring, not hard logits masking. Summarization not IE."
265	      must_cite: true
266	
267	    - id: scidc_2026
268	      title: "SciDC: Scientific Knowledge as Constrained Decoding Rules"
269	      venue: arXiv 2026
270	      arxiv: "2604.06603"
271	      schema_usage: rule_to_decoding
272	      note: "+12% accuracy. Scientific reasoning not IE. No domain/range type constraints."
273	      must_cite: false
274	
275	    - id: dialogue_ontology_re_sigdial2024
276	      title: "Ontology-Constrained RE for Dialogue"
277	      venue: SIGDIAL 2024
278	      arxiv: "2408.02361"
279	      schema_usage: vocabulary_constraint
280	      note: "Constrains which relation names are valid, not which entity type combos satisfy domain/range."
281	      must_cite: false
282	
283	  type_constraint_enforcement:
284	    - id: roth_yih_2004
285	      title: "Global Inference for Entity and Relation Identification via a Linear Programming Formulation"
286	      venue: "AAAI 2004 / MIT 2007"
287	      method: "ILP enforcing type compatibility (e.g., EMP-ORG only between PER+ORG)"
288	      constraint_time: inference_ilp
289	      note: "Pre-LLM. The original domain/range enforcement idea for IE."
290	      must_cite: true
291	
292	    - id: li_ji_2014
293	      title: "Incremental Joint Extraction with Type Constraints"
294	      venue: AIJ 2014
295	      method: "Mines type+cardinality constraints from data, ILP encoding"
296	      constraint_time: inference_ilp
297	      must_cite: false
298	
299	    - id: knowprompt_www2022
300	      title: "KnowPrompt: Knowledge-aware Prompt-tuning"
301	      venue: WWW 2022
302	      method: "Virtual type words + synergistic optimization with structural constraints"
303	      constraint_time: training
304	      must_cite: false
305	
306	    - id: etcgn_2024
307	      title: "Entity Type-Constrained Graph Networks for Doc-level RE"
308	      venue: IJMLC 2024
309	      constraint_time: training_architecture
310	      must_cite: false
311	
312	    - id: genre_iclr2021
313	      title: "GENRE: Autoregressive Entity Retrieval"
314	      venue: ICLR 2021
315	      method: "Trie-based constrained beam search for entity linking"
316	      constraint_time: decoding_vocabulary
317	      must_cite: false
318	
319	    - id: hidden_cost_ranlp2025
320	      title: "Hidden Cost of Structured Output"
321	      venue: RANLP 2025
322	      note: "Constrained decoding can degrade output quality. Important risk for OntoCoDec design."
323	      must_cite: true
324	
325	suggested_related_work_citations:
326	  must_cite:
327	    - "Synchromesh (NeurIPS'22) — pioneer of semantic constrained decoding"
328	    - "MGD (NeurIPS'23) — type checking at decode time for code"
329	    - "Type-Constrained Code Gen (PLDI'25) — type system → automaton → logits mask"
330	    - "GCD for IE (EMNLP'23) — grammar-constrained decoding applied to NER/RE"
331	    - "AdaKGC (EMNLP'23) — schema-constrained trie decoding for IE"
332	    - "GoLLIE (ICLR'24) — annotation guidelines as code for IE"
333	    - "KnowCoder (ACL'24) — Wikidata type hierarchy as Python classes"
334	    - "ODKE+ (Apple'25) — ontology-guided IE at scale (post-processing baseline)"
335	    - "SPIRES/OntoGPT (Bioinformatics'24) — ontology-based LLM extraction"
336	    - "OntoLogX (2025) — SHACL post-validation (detect-then-fix baseline)"
337	    - "EKAW'24 — ontology-constrained beam search (soft constraint baseline)"
338	    - "XGrammar (2024) — fastest grammar-constrained decoding framework"
339	    - "CRANE (ICML'25) — constraint vs reasoning tradeoff"
340	    - "Grammar-Aligned Decoding (NeurIPS'24) — distribution distortion from masking"
341	    - "Roth & Yih (AAAI'04) — original ILP type constraint enforcement for IE"
342	    - "Hidden Cost of Structure (RANLP'25) — risks of constrained decoding"
343	  should_cite:
344	    - "Outlines/Guidance — constrained decoding ecosystem"
345	    - "iNERD (SLT'24) — token masking for NER"
346	    - "CodeIE (ACL'23) — code generation for IE"
347	    - "RELATE (2025) — biomedical ontology mapping"
348	    - "OneKE (WWW'25) — multi-agent IE with reflection"
349	    - "IterGen (ICLR'25) — semantic-aware backtracking"
350	    - "SMC-based control (ICLR'25 Oral) — probabilistic semantic control"
351	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bb7989d-6407-4afc-b699-f5f0990616b3",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "2093e54f-4ef2-416d-b052-133a60a3d3f6",
  "sourceToolAssistantUUID": "1bb7989d-6407-4afc-b699-f5f0990616b3",
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

_source line 51 · 2026-05-14T10:52:00.090Z_

<details open><summary>🔧 Tool call — Read · `toolu_0139WY6s8ifMjEqz8Vqqtm7W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/literature_survey_constrained_decoding_ie.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2093e54f-4ef2-416d-b052-133a60a3d3f6",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LMRYPex2dcQc4XoggU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e20f1e57-555b-440a-af19-efd94839b194",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCtrhdjyrSBk383iWZFSao",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 302,
      "cache_read_input_tokens": 61819,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 302
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 61819,
          "cache_creation_input_tokens": 302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 302,
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

_source line 52 · 2026-05-14T10:52:00.096Z_

<details><summary>↩ Tool result · `toolu_0139WY6s8ifMjEqz8Vqqtm7W`</summary>

```text
1	# Literature Survey: Constrained Decoding for Information Extraction (2022-2026)
2	
3	Survey date: 2026-05-13
4	
5	---
6	
7	## Category A: Grammar-Constrained Decoding Directly Applied to IE Tasks
8	
9	### A1. Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning
10	- **Authors**: Saibo Geng, Martin Josifoski, Maxime Peyrard, Robert West
11	- **Venue**: EMNLP 2023
12	- **ArXiv**: 2305.13971
13	- **Core method**: Uses context-free grammars (via Grammatical Framework) to constrain LLM decoding for structured NLP tasks. Introduces **input-dependent grammars** that adapt the grammar to each input.
14	- **IE tasks**: NER, relation extraction, entity disambiguation, constituency parsing
15	- **Semantic constraints**: No. Purely syntactic (CFG-level). Ensures valid output structure but not ontological validity of extracted content.
16	- **Key result**: GCD-enhanced LLMs substantially outperform unconstrained LLMs and even beat task-specific finetuned models.
17	- **Relevance**: **HIGH** — Most direct precursor. Demonstrates GCD for IE but stops at syntactic validity. Our work extends to semantic (type) constraints.
18	- **Code**: https://github.com/epfl-dlab/GCD
19	
20	### A2. iNERD: Informed Named Entity Recognition Decoding for Generative Language Models
21	- **Authors**: Deussel, Hillebrand, et al.
22	- **Venue**: IEEE SLT 2024 (arXiv 2308.07791, Aug 2023)
23	- **Core method**: Treats NER as generative process; uses informed decoding that masks impossible tokens based on NER structure constraints during prediction.
24	- **IE tasks**: NER only
25	- **Semantic constraints**: Partial — masks tokens that are structurally impossible for NER (e.g., entity type vocabulary), but does not enforce ontological constraints like domain/range.
26	- **Key result**: Eliminates hallucinated entity types, improves NER performance across 5 LLMs on 8 datasets.
27	- **Relevance**: **HIGH** — Shows token masking for IE-specific constraints works. But constraints are NER-structural, not ontology-semantic.
28	
29	### A3. Grammar-Constrained Decoding for Structured IE with Fine-tuned Models (Clinical Trial Abstracts)
30	- **Authors**: (Frontiers in AI, 2024)
31	- **Venue**: Frontiers in Artificial Intelligence, Jan 2025 (published online)
32	- **Core method**: Investigates grammar-constrained decoding impact on fine-tuned generative models for structured information extraction from clinical trial abstracts.
33	- **IE tasks**: Structured extraction from clinical text (PICO elements)
34	- **Semantic constraints**: No. Focuses on ensuring well-formedness of output structure via grammar rules.
35	- **Key result**: Grammar constraints ensure valid output format even in low-resource settings; investigates trade-off between format compliance and extraction accuracy.
36	- **Relevance**: MEDIUM — Domain-specific application of GCD to IE, but no semantic constraints.
37	
38	### A4. Generative Biomedical Event Extraction with Constrained Decoding Strategy
39	- **Authors**: (IEEE/ACM Trans. Comp. Bio. Bioinformatics, 2024)
40	- **Venue**: IEEE/ACM TCBB, 2024
41	- **Core method**: T5-based seq2seq model with trie-based constrained decoding for biomedical event extraction. Uses curriculum learning.
42	- **IE tasks**: Biomedical event extraction (Genia 2011, Genia 2013)
43	- **Semantic constraints**: Partial — the trie constrains argument roles to valid options, which is a form of schema-level constraint beyond pure syntax.
44	- **Key result**: Outperforms extraction-based approaches; avoids cascading errors of pipeline systems.
45	- **Relevance**: MEDIUM-HIGH — Trie-constrained decoding for event extraction with role constraints is conceptually related to our type constraints.
46	
47	### A5. An Autoregressive Text-to-Graph Framework for Joint Entity and Relation Extraction (ATG)
48	- **Authors**: Zaratiana, Tomeh, et al.
49	- **Venue**: AAAI 2024
50	- **ArXiv**: 2401.01326
51	- **Core method**: Encoder-decoder with pointing mechanism on dynamic vocabulary of spans and relation types. Decoder transitions through states with constraints (no relation before entities, no repeated spans, head != tail).
52	- **IE tasks**: Joint entity and relation extraction (CoNLL04, SciERC, ACE05)
53	- **Semantic constraints**: Minimal — structural constraints on generation order, but no type-compatibility checking.
54	- **Relevance**: MEDIUM — Constrained generation for RE but constraints are structural/ordering, not ontological.
55	
56	### A6. CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors
57	- **Authors**: Peng Li, Tianxiang Sun, et al.
58	- **Venue**: ACL 2023
59	- **ArXiv**: 2305.05711
60	- **Core method**: Recasts IE structured output as Python code (dicts, lists); uses Code-LLMs (Codex) with code-style prompts.
61	- **IE tasks**: NER, relation extraction (7 benchmarks)
62	- **Semantic constraints**: No. Code structure provides implicit constraints but no ontology-level enforcement during decoding.
63	- **Relevance**: MEDIUM — Alternative approach to structured IE output; Python type hints could potentially encode ontological constraints but this is not explored.
64	
65	### A7. GoLLIE: Annotation Guidelines improve Zero-Shot Information Extraction
66	- **Authors**: Sainz et al. (HiTZ Center)
67	- **Venue**: ICLR 2024
68	- **ArXiv**: 2310.03668
69	- **Core method**: Fine-tunes Code-LLama to follow annotation guidelines defined as Python classes. Type constraints (str, list, Optional) defined in schema.
70	- **IE tasks**: NER, RE, event extraction (zero-shot generalization)
71	- **Semantic constraints**: Partial — Python type annotations serve as soft constraints during generation. However, these are format-level types (str, list), not ontological types (e.g., Person can only be head of "born_in" → Location).
72	- **Relevance**: MEDIUM-HIGH — Schema-as-code approach. Close in spirit but constraints are format-level, not ontology-level.
73	
74	---
75	
76	## Category B: Constrained Decoding Frameworks/Engines (Tooling Layer)
77	
78	### B1. XGrammar: Flexible and Efficient Structured Generation Engine
79	- **Authors**: Dong, Ruan, et al. (MLC-AI)
80	- **Venue**: Preprint, Nov 2024 (arXiv 2411.15100)
81	- **Core method**: CFG-based constrained decoding with context-independent/dependent token split for efficiency. Supports JSON Schema, regex, custom CFG.
82	- **Semantic constraints**: No. Pure syntactic grammar enforcement.
83	- **Key result**: Up to 100x speedup over traditional grammar-constrained methods.
84	- **Relevance**: **HIGH as infrastructure** — This is the tool we use for the grammar layer in our system. Our semantic constraints sit on top of XGrammar.
85	
86	### B2. Outlines (dottxt)
87	- **Venue**: Open-source library (2023-)
88	- **Core method**: Pioneered grammar-based constrained generation for HuggingFace models. JSON Schema, regex, CFG/EBNF.
89	- **Semantic constraints**: No.
90	- **Relevance**: Infrastructure layer. Outlines was the first widely-adopted tool; XGrammar succeeds it in performance.
91	
92	### B3. LMQL: Language Model Query Language
93	- **Authors**: Beurer-Kellner et al. (ETH Zurich SRI Lab)
94	- **Venue**: PLDI 2023
95	- **Core method**: SQL-like query language for LLM interaction with constraints (regex, data types, choice sets). Novel evaluation semantics for character-to-token constraint translation.
96	- **Semantic constraints**: Partial — supports data type constraints (INT, FLOAT) and choice constraints, but not ontological/relational constraints.
97	- **Key result**: 75-85% fewer billable tokens vs unconstrained decoding.
98	- **Relevance**: LOW-MEDIUM — Different paradigm (query language vs grammar). Could theoretically express type constraints but not designed for IE ontology enforcement.
99	
100	### B4. JsonFormer
101	- **Venue**: Open-source (2023)
102	- **Core method**: Generates only content tokens; fills in structure tokens deterministically based on JSON Schema. Works with HuggingFace pipelines.
103	- **Semantic constraints**: No. Schema compliance only.
104	- **Relevance**: LOW — Simple tool, limited expressiveness compared to grammar-based approaches.
105	
106	### B5. Guidance (Microsoft)
107	- **Venue**: Open-source library (2023-)
108	- **Core method**: Constrained decoding framework supporting regex, CFG, JSON Schema. Integrated into vLLM/SGLang via llguidance backend.
109	- **Semantic constraints**: No.
110	- **Relevance**: Infrastructure layer.
111	
112	### B6. llama.cpp GBNF Grammars
113	- **Venue**: Open-source
114	- **Core method**: GBNF grammar format for constrained generation in llama.cpp inference engine.
115	- **Semantic constraints**: No.
116	- **Relevance**: Infrastructure layer.
117	
118	---
119	
120	## Category C: Semantic-Level Constrained Decoding (Beyond Syntax — Not IE-Specific)
121	
122	### C1. Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context
123	- **Authors**: Agrawal et al. (Microsoft)
124	- **Venue**: NeurIPS 2023
125	- **Core method**: Uses static analysis monitors during decoding to enforce type-checking, argument validity, and stateful API protocols in code generation.
126	- **Semantic constraints**: **YES** — Enforces type correctness, argument count, API protocol ordering. This is genuine semantic constraint enforcement at decode time.
127	- **Key result**: SantaCoder-1.1B + MGD outperforms text-davinci-003. Generalizes to Java, C#, Rust.
128	- **Relevance**: **CRITICAL REFERENCE** — Most analogous to our approach. They do type-checking during decoding for code; we do type-checking during decoding for IE. Key difference: their "ontology" is a programming language type system; ours is a domain ontology.
129	- **Code**: https://github.com/microsoft/monitors4codegen
130	
131	### C2. Synchromesh: Reliable Code Generation from Pre-trained Language Models
132	- **Authors**: Poesia, Polozov, et al.
133	- **Venue**: NeurIPS 2022 (arXiv 2201.11227)
134	- **Core method**: Constrained Semantic Decoding (CSD) — enforces syntax, typing, and scoping constraints simultaneously during code generation. Target Similarity Tuning for example selection.
135	- **Semantic constraints**: **YES** — Type-checking and scope validation at decode time.
136	- **Key result**: Reduces SQL and DSL errors via rich constraint enforcement without fine-tuning.
137	- **Relevance**: **CRITICAL REFERENCE** — Pioneer of semantic constraints in decoding. Our work can be framed as "Synchromesh for IE" — bringing CSD from code to information extraction.
138	
139	### C3. IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking
140	- **Authors**: Ugare et al.
141	- **Venue**: ICLR 2025
142	- **ArXiv**: 2410.07295
143	- **Core method**: First framework combining grammar-guided generation with backtracking. Allows forward/backward navigation by grammar symbols. Semantic checks trigger backtracking when violations detected.
144	- **Semantic constraints**: **YES** — Semantic checks (privacy leakage, SQL validity) can trigger regeneration via backtracking.
145	- **Key result**: 18.5% improvement over SOTA grammar-guided generation; reduces privacy leaks from 51.4% to 0%.
146	- **Relevance**: **HIGH** — Backtracking mechanism for semantic violations is complementary to our approach. We could potentially use backtracking when grammar ∧ semantic mask produces empty set.
147	
148	### C4. CRANE: Reasoning with Constrained LLM Generation
149	- **Authors**: Banerjee et al.
150	- **Venue**: ICML 2025
151	- **ArXiv**: 2502.09061
152	- **Core method**: Balances constraint enforcement with reasoning flexibility. Augments grammar with additional rules to preserve reasoning capability. Handles both syntactic (CFG) and semantic constraints (valid variables).
153	- **Semantic constraints**: **YES** — Ensures generated expressions contain only valid problem-defined variables (a semantic property).
154	- **Key result**: Up to 10% improvement on symbolic reasoning (GSM-symbolic, FOLIO).
155	- **Relevance**: MEDIUM — Addresses the fundamental tension between constraint strictness and generation quality, relevant to our approach.
156	
157	### C5. Syntactic and Semantic Control of LLMs via Sequential Monte Carlo
158	- **Authors**: Loula, LeBrun, et al.
159	- **Venue**: ICLR 2025 (Oral)
160	- **ArXiv**: 2504.13139
161	- **Core method**: SMC-based framework for controlled LLM generation. Flexibly incorporates domain-specific syntactic and semantic constraints. Efficiently reallocates computation during generation.
162	- **Semantic constraints**: **YES** — Supports arbitrary semantic constraints as probabilistic conditioning.
163	- **Key result**: Small open-source models outperform 8x larger models on code gen, text-to-SQL, molecule synthesis.
164	- **Relevance**: MEDIUM-HIGH — Elegant theoretical framework. Could be an alternative to our token masking approach, but SMC is computationally heavier.
165	
166	### C6. Grammar-Aligned Decoding (GAD)
167	- **Authors**: Park, Wang, Berg-Kirkpatrick, et al.
168	- **Venue**: NeurIPS 2024
169	- **ArXiv**: 2405.21047
170	- **Core method**: ASAp algorithm — guarantees grammatical output while matching the LLM's conditional distribution. Addresses distortion problem of naive grammar-constrained decoding.
171	- **Semantic constraints**: No. Focuses on preserving distribution quality under syntactic constraints.
172	- **Key result**: Higher-likelihood outputs than existing GCD techniques while maintaining constraints.
173	- **Relevance**: MEDIUM — Addresses a problem we also face: naive token masking can distort generation quality. ASAp could improve our semantic masking quality.
174	
175	### C7. Relation-Constrained Decoding for Text Generation (RESEAL)
176	- **Authors**: (NeurIPS 2022)
177	- **Core method**: Ensures output contains given word pairs with specified relations (syntactic or factual). RESEAL algorithm uses relation-guided probability surgery and beam allocation.
178	- **Semantic constraints**: **Partial** — Enforces relational constraints between words (dependency relations, KG relations), but for text generation, not extraction.
179	- **Relevance**: MEDIUM — Conceptually related (relation constraints during decoding) but for generation, not extraction.
180	
181	---
182	
183	## Category D: Ontology-Constrained IE (Post-Processing, Not Decode-Time)
184	
185	### D1. RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints
186	- **Authors**: Olasunkanmi et al.
187	- **Venue**: ArXiv 2509.19057 (Nov 2025)
188	- **Core method**: Three-stage pipeline: (1) ontology preprocessing with predicate embeddings, (2) similarity-based retrieval with SapBERT, (3) LLM-based reranking with negation handling. Maps extracted relations to standardized ontology predicates.
189	- **Semantic constraints**: **YES but post-hoc** — Ontology alignment happens after extraction, not during decoding.
190	- **Relevance**: HIGH as comparison — Shows the need for ontology compliance in IE but addresses it via post-processing. Our approach integrates constraints into decoding.
191	
192	### D2. ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs
193	- **Authors**: Khorshidi, Nikfarjam et al. (Apple)
194	- **Venue**: ArXiv 2509.04696 (Sep 2025)
195	- **Core method**: Production-grade system using ontology snippets (dynamically selected ontology subsets) as prompting context. Grounder validates facts post-extraction.
196	- **Semantic constraints**: **YES but prompt-level + post-hoc validation** — Ontology snippets guide prompting; a separate Grounder LLM validates. Not decode-time enforcement.
197	- **Key result**: 98.8% precision on 19M facts from 9M Wikipedia pages.
198	- **Relevance**: HIGH as comparison — Production system showing ontology-guided IE. But constraints are prompt-level and post-validation, not decode-time masking.
199	
200	### D3. OntoKG: Ontology-Oriented Knowledge Graph Construction with Intrinsic-Relational Routing
201	- **Authors**: (ArXiv 2604.02618, Apr 2026)
202	- **Core method**: Ontology-first KG construction with intrinsic-relational routing (classifies properties as node attributes vs graph edges). LLM-guided extraction with schema modules.
203	- **Semantic constraints**: Schema-level routing but post-extraction.
204	- **Relevance**: LOW-MEDIUM — Large-scale KG construction, not focused on decoding constraints.
205	
206	---
207	
208	## Category E: Benchmarks and Analysis
209	
210	### E1. JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for LLMs
211	- **Authors**: (Guidance team + EPFL)
212	- **Venue**: ArXiv 2501.10868 (Jan 2025)
213	- **Core method**: 10K real-world JSON schemas evaluating constrained decoding on efficiency, coverage, quality. Tests Guidance, Outlines, llama.cpp, XGrammar, OpenAI, Gemini.
214	- **Key findings**: Constrained decoding speeds up generation by 50%; best framework supports 2x more schemas than worst; consistent 4% downstream improvement.
215	- **Relevance**: MEDIUM — Benchmark for syntactic constraint quality. Does not evaluate semantic constraints.
216	
217	### E2. The Hidden Cost of Structure: How Constrained Decoding Affects LM Performance
218	- **Venue**: RANLP 2025
219	- **Key findings**: Fundamental divergence between base and instruction-tuned models under structural constraints. Successful constrained generation requires adapted prompts + few-shot examples. Constrained models show steeper gains from demonstrations.
220	- **Relevance**: HIGH — Warns about quality degradation from constraint enforcement. Our semantic masking must be carefully designed to avoid this.
221	
222	### E3. SLOT: Structuring the Output of Large Language Models
223	- **Venue**: EMNLP 2025 Industry Track
224	- **Core method**: Fine-tuned lightweight LM as post-processing layer for structured output. Alternative to constrained decoding.
225	- **Key result**: Mistral-7B + constrained decoding: 99.5% schema accuracy.
226	- **Relevance**: LOW — Post-processing approach, alternative paradigm to our decode-time constraints.
227	
228	---
229	
230	## Category F: Surveys and Resource Lists
231	
232	### F1. Awesome-LLM-Constrained-Decoding (GitHub)
233	- **Maintainer**: Saibo Geng (first author of A1)
234	- **URL**: https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding
235	- **Content**: Curated list of ~50 papers on constrained decoding, categorized and regularly updated.
236	- **Relevance**: Excellent reference list. Confirms no paper on ontology-semantic constrained decoding for IE.
237	
238	### F2. Awesome-LLM4IE-Papers (GitHub)
239	- **URL**: https://github.com/quqxui/Awesome-LLM4IE-Papers
240	- **Content**: Papers on generative IE using LLMs.
241	- **Relevance**: Complementary resource for IE-specific papers.
242	
243	### F3. A Survey of Generative Information Extraction (COLING 2025)
244	- **Venue**: COLING 2025
245	- **Content**: Comprehensive survey of generative approaches to IE.
246	- **Relevance**: Survey context.
247	
248	---
249	
250	## Summary: Gap Analysis
251	
252	| Constraint Level | IE Application | Decode-Time Enforcement | Existing Work |
253	|---|---|---|---|
254	| Syntactic (valid JSON/format) | Yes | Yes | Geng et al. (A1), iNERD (A2), Clinical IE (A3) |
255	| Structural (valid schema fields) | Yes | Yes | XGrammar/Outlines + JSON Schema |
256	| Vocabulary (valid entity/relation types) | Yes | Yes | iNERD (A2), trie-based (A4) |
257	| **Semantic (domain/range type compatibility)** | **No** | **No** | **GAP — Our contribution** |
258	| Semantic (type checking) | Code gen only | Yes | MGD (C1), Synchromesh (C2) |
259	| Semantic (ontology compliance) | KG construction | Post-hoc only | RELATE (D1), ODKE+ (D2) |
260	
261	**Core novelty confirmed**: No prior work enforces ontology-level semantic constraints (domain/range type checking) during the token-level decoding process for information extraction tasks. The closest analogues are Monitor-Guided Decoding and Synchromesh in code generation, and RELATE/ODKE+ in KG construction (post-processing only).
262	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e20f1e57-555b-440a-af19-efd94839b194",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "df8978bc-e67e-42b1-9d48-1689ff4b6558",
  "sourceToolAssistantUUID": "e20f1e57-555b-440a-af19-efd94839b194",
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

_source line 53 · 2026-05-14T10:52:03.532Z_

Now let me also check the dream review reports to see the range of review scores the paper received.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df8978bc-e67e-42b1-9d48-1689ff4b6558",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LMetpPUbVmauPoCmA7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fc517a8-7366-4eb8-9a5e-203ac4e0f847",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRux8HRhEEZi1xg6ZvNvEJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11058,
      "cache_read_input_tokens": 62121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11058,
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

_source line 54 · 2026-05-14T10:52:06.419Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PDp5waH3tZGHVboGYGNkjG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fc517a8-7366-4eb8-9a5e-203ac4e0f847",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LMetpPUbVmauPoCmA7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05b7a13e-d6b2-4a62-b0a1-50b40ee25b22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRux8HRhEEZi1xg6ZvNvEJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11058,
      "cache_read_input_tokens": 62121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11058,
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

_source line 55 · 2026-05-14T10:52:06.425Z_

<details><summary>↩ Tool result · `toolu_01PDp5waH3tZGHVboGYGNkjG`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05b7a13e-d6b2-4a62-b0a1-50b40ee25b22",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "78ed6c26-4931-485f-aae6-63857baea44b",
  "sourceToolAssistantUUID": "05b7a13e-d6b2-4a62-b0a1-50b40ee25b22",
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

_source line 56 · 2026-05-14T10:52:07.003Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016gncDcR95t7mqxm562Xrrm`</summary>

```json
{
  "pattern": "**/dream_*/*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78ed6c26-4931-485f-aae6-63857baea44b",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LMetpPUbVmauPoCmA7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a259f249-80bf-44e3-b5e2-c946005da18e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GRux8HRhEEZi1xg6ZvNvEJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11058,
      "cache_read_input_tokens": 62121,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11058
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 62121,
          "cache_creation_input_tokens": 11058,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11058,
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

_source line 57 · 2026-05-14T10:52:07.020Z_

<details><summary>↩ Tool result · `toolu_016gncDcR95t7mqxm562Xrrm`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a259f249-80bf-44e3-b5e2-c946005da18e",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "47d9f580-7fb3-4243-b9ee-efa505593395",
  "sourceToolAssistantUUID": "a259f249-80bf-44e3-b5e2-c946005da18e",
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

_source line 58 · 2026-05-14T10:52:17.698Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LBRpuoNZGjBd8Ua1d7SCFm`</summary>

```json
{
  "pattern": "**/dream_*/**/*report*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47d9f580-7fb3-4243-b9ee-efa505593395",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LNASpMDKJjCfLTnRg6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7419020-7ce9-4c59-8de4-e926141dd52c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136cXHM91BcHmFVP2jmQuv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 73179,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1318,
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

_source line 59 · 2026-05-14T10:52:17.724Z_

<details><summary>↩ Tool result · `toolu_01LBRpuoNZGjBd8Ua1d7SCFm`</summary>

```text
artifacts/dream_reports/dream_20260514T094226/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7419020-7ce9-4c59-8de4-e926141dd52c",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "f6be384c-1334-48e2-89b9-57f952905023",
  "sourceToolAssistantUUID": "f7419020-7ce9-4c59-8de4-e926141dd52c",
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

_source line 60 · 2026-05-14T10:52:30.547Z_

<details open><summary>🔧 Tool call — Read · `toolu_011a63gch6UoReAs1qKnWRVu`</summary>

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
  "parentUuid": "f6be384c-1334-48e2-89b9-57f952905023",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LNxMpVbJVLC2s3Gd5Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6fe65cf-509c-4890-9d90-8e74810dac1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Re6VZK9ucZg5GaoEU7ih4e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 140,
      "cache_read_input_tokens": 74497,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 140
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 105,
          "cache_read_input_tokens": 74497,
          "cache_creation_input_tokens": 140,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 140,
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

_source line 61 · 2026-05-14T10:52:30.561Z_

<details><summary>↩ Tool result · `toolu_011a63gch6UoReAs1qKnWRVu`</summary>

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
  "parentUuid": "a6fe65cf-509c-4890-9d90-8e74810dac1a",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "3f89371d-dcb2-4725-9fd4-5bffd90108bb",
  "sourceToolAssistantUUID": "a6fe65cf-509c-4890-9d90-8e74810dac1a",
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

_source line 62 · 2026-05-14T10:52:34.446Z_

Now I have a comprehensive understanding of the paper. Let me also check if the title was updated as mentioned in the paper_framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f89371d-dcb2-4725-9fd4-5bffd90108bb",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LPuJ3kHTKCXEohEs7Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b419b75a-c15b-4b39-87c8-7ad9f3a879bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFw18MYWHPiJ3PfNrU4tc1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6363,
      "cache_read_input_tokens": 74637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6363,
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

_source line 63 · 2026-05-14T10:52:36.546Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NyCfw5scT7MuH28UtRQupc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b419b75a-c15b-4b39-87c8-7ad9f3a879bf",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LPuJ3kHTKCXEohEs7Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f28d72d-0ed1-404c-b7e7-da471cae7358",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFw18MYWHPiJ3PfNrU4tc1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6363,
      "cache_read_input_tokens": 74637,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6363
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 127,
          "cache_read_input_tokens": 74637,
          "cache_creation_input_tokens": 6363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6363,
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

_source line 64 · 2026-05-14T10:52:36.553Z_

<details><summary>↩ Tool result · `toolu_01NyCfw5scT7MuH28UtRQupc`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, ensuring structural validity of generated text.
9	%
10	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens, achieving 100$\times$ speedup over prior CFG-constrained decoding via persistent pushdown automata.
11	%
12	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, while LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks.
13	%
14	A parallel line addresses the \emph{distribution distortion} introduced by naive token masking: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement, and ASAp~\cite{park2024grammar} provides an unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
15	%
16	\textbf{Distinction:} OntoCoDec's grammar layer builds on XGrammar for structural (JSON schema + enum) constraints, but these methods operate exclusively at the syntactic level---they ensure format validity but cannot enforce cross-field semantic constraints such as ontology domain/range rules.
17	
18	% TODO: Expand with 2-3 sentences on how grammar-constrained decoding has become
19	% the de facto standard for structured output, and why the syntactic-only limitation
20	% motivates our semantic extension.
21	
22	% ===========================================================================
23	% Paradigm 1.5: Semantic Constrained Decoding for Code
24	% ===========================================================================
25	\paragraph{Semantic Constrained Decoding for Code.}
26	In programming-language generation, constrained decoding has been extended beyond syntax to enforce semantic properties such as type correctness.
27	%
28	Synchromesh~\cite{synchromesh_neurips2022} pioneers Constrained Semantic Decoding (CSD), which enforces syntax, type, and scope constraints simultaneously during code generation from pre-trained LMs, establishing that semantic constraints can be compiled into token-level filtering without fine-tuning.
29	%
30	MGD~\cite{mgd_neurips2023} uses static-analysis monitors to perform type checking at decode time, enabling SantaCoder-1.1B to outperform text-davinci-003 on repository-level code completion by enforcing type-correct identifier usage.
31	%
32	Most recently, \citet{pldi2025_type_constrained_codegen} compile full type systems into prefix automata for token-level logits masking, reducing compilation errors by over 50\%---the closest mechanistic analog to OntoCoDec, applying the same ``type system $\to$ automaton $\to$ logits mask'' pipeline.
33	%
34	\textbf{Distinction:} These methods demonstrate that semantic (type) constraints at decode time are both feasible and highly effective---but exclusively in the code domain, where type systems are formally specified. OntoCoDec is the first to migrate this paradigm to information extraction, compiling IE ontology axioms (domain/range constraints) into an analogous decoding-time enforcement mechanism.
35	
36	% TODO: Expand with 1-2 sentences on the technical differences between PL type
37	% systems and IE ontology axioms (e.g., subtyping vs. domain/range), and how
38	% OntoCoDec bridges this gap.
39	
40	% ===========================================================================
41	% Paradigm 2: Vocabulary/Type-Constrained Generation
42	% ===========================================================================
43	\paragraph{Vocabulary and Type-Constrained Generation.}
44	The idea of enforcing entity-type compatibility constraints for IE dates back to pre-neural methods: \citet{roth_yih_2004} formulate joint entity and relation identification as an integer linear program (ILP) that enforces type constraints---e.g., EMP-ORG only between PER and ORG entities---establishing the principle that relational type compatibility should be a hard constraint, not a soft preference.
45	%
46	In the autoregressive era, GENRE~\cite{decao2021genre} pioneers trie-based constrained beam search for autoregressive entity retrieval, limiting each decoding step to tokens consistent with valid entity names.
47	%
48	GenIE~\cite{josifoski2022genie} extends this to end-to-end IE with state-based constraints that enforce valid triple structures, though it requires task-specific fine-tuning.
49	%
50	AdaKGC~\cite{adakgc_emnlp2023} introduces schema-constrained dynamic decoding with trie-based prefix trees that adapt to the target schema, enforcing that generated entity and relation names belong to a predefined inventory---a vocabulary-level constraint that ensures name validity but not type compatibility.
51	%
52	GCD~\cite{geng2023gcd} provides a unified grammar-constrained decoding framework for structured NLP tasks including IE, introducing input-dependent grammars for greater flexibility.
53	%
54	NeuroLogic Decoding~\cite{lu2021neurologic} expresses lexical inclusion/exclusion constraints as predicate logic formulas enforced during beam search.
55	%
56	\textbf{Distinction:} These approaches constrain \emph{which tokens} can appear (vocabulary membership) but not \emph{which type combinations} are valid for a given relation. OntoCoDec's semantic layer enforces relational constraints---e.g., that the head entity of relation $R$ must belong to type set $\mathcal{D}(R)$---which cannot be expressed as static vocabulary restrictions. Roth \& Yih's ILP formulation shares the same type-compatibility motivation but operates as a post-hoc reranker over discrete candidates, whereas OntoCoDec integrates enforcement directly into autoregressive decoding.
57	
58	% TODO: Add 1-2 sentences positioning GCD as the closest precursor (same logits-masking
59	% mechanism for IE) and clarifying that OntoCoDec extends from syntactic to semantic constraints.
60	
61	% ===========================================================================
62	% Paradigm 3: Structural Constraints for IE
63	% ===========================================================================
64	\paragraph{Structural Constraints via Training and Prompting.}
65	An orthogonal approach encodes IE output structure through model training or prompt design rather than decoding-time enforcement.
66	%
67	UIE~\cite{lu2022uie} defines a Structured Extraction Language and trains a unified text-to-structure model across 13 IE datasets, relying on large-scale pre-training to produce schema-compliant outputs.
68	%
69	GoLLIE~\cite{sainz2024gollie} expresses annotation guidelines as Python dataclass definitions, fine-tuning Code-LLaMA to generate typed code, achieving strong zero-shot transfer to unseen IE schemas.
70	%
71	KnowCoder~\cite{knowcoder_acl2024} takes this further by encoding 29K entity types from Wikidata as a Python class hierarchy, training a Code-LLM to generate structured extraction code that implicitly respects type inheritance---the most comprehensive schema-as-code approach to date.
72	%
73	CodeIE~\cite{li2023codeie} reformulates IE as code generation, leveraging the implicit type structure of programming languages.
74	%
75	ADELIE~\cite{qi2024adelie} uses SFT and DPO to align LLMs on IE tasks, achieving SOTA among open-source models while preserving general capabilities.
76	%
77	EnriCo~\cite{zaratiana2024enrico} applies Answer Set Programming (ASP) constraints during decoding of joint entity-relation extraction models, enforcing structural type compatibility at generation time---a decoding-time approach, though with model-specific (non-ontology-driven) constraints.
78	%
79	\textbf{Distinction:} Training-based methods provide \emph{soft} structural guidance---the model learns to prefer valid outputs but offers no compliance guarantee at inference time. EnriCo's ASP constraints are hard but model-specific and require manual rule authoring. OntoCoDec provides \emph{hard} decoding-time enforcement that is training-free, automatically compiled from ontology schemas, and composable with any of these approaches.
80	
81	% TODO: Expand with discussion of how training-based and decoding-time approaches
82	% are complementary (e.g., GoLLIE + OntoCoDec), not competing.
83	
84	% ===========================================================================
85	% Paradigm 4: Type-Checking / Ontology Validation
86	% ===========================================================================
87	\paragraph{Post-hoc Ontology Validation.}
88	Rather than constraining generation, several methods validate LLM outputs against ontological rules after generation.
89	%
90	ODKE+~\cite{khorshidi2025odke} dynamically generates ontology snippets containing domain/range constraints as prompt context, achieving 98.8\% precision across 195 predicates at web scale---but constraint adherence relies on prompt-level guidance, not enforcement.
91	%
92	SPIRES/OntoGPT~\cite{spires_2024} provides an ontology-based extraction framework that grounds LLM outputs against OBO ontologies post-generation, representing the prompt-then-validate paradigm in the biomedical domain.
93	%
94	OntoLogX~\cite{ontologx_2025} applies SHACL validation to LLM-generated knowledge graphs, iteratively correcting constraint violations and reducing them by approximately 10$\times$---demonstrating the detect-then-fix paradigm's effectiveness but also its inherent multi-pass cost.
95	%
96	\citet{upadhyay2023openie} inject entity-type knowledge as constraints into Open IE via both constrained inference and constraint-aware training, improving F1 by 29\% on CaRB.
97	%
98	\citet{regino2025kgcurator} propose a multi-stage LLM pipeline for validating RDF triple insertions against domain/range constraints, representing the post-hoc validation paradigm.
99	%
100	\citet{ekaw2024_ontology_beam} introduce ontology-constrained beam scoring for clinical summarization, applying soft biases (not hard masks) during beam search to steer outputs toward ontology-compliant terms---a middle ground between unconstrained generation and hard enforcement.
101	%
102	\textbf{Distinction:} Post-hoc validation detects violations after generation, requiring rejection or correction cycles that waste compute (14--15\% of generated triples contain domain/range violations in our setting). OntoCoDec \emph{prevents} violations during decoding, redirecting probability mass to valid alternatives rather than discarding invalid outputs. Soft-constraint approaches like EKAW'24 reduce but cannot eliminate violations, whereas OntoCoDec achieves near-complete type compliance (domain/range violations reduced from 15.37\% to 0.93\%).
103	
104	% TODO: Add quantitative comparison of compute cost: post-hoc rejection vs.
105	% preventive enforcement (marginal overhead of logits masking vs. wasted tokens).
106	
107	% ===========================================================================
108	% Paradigm 5: Constrained Decoding Quality Concerns
109	% ===========================================================================
110	\paragraph{Quality Impact of Constrained Decoding.}
111	A growing body of work raises concerns that constrained decoding degrades LLM generation quality, particularly for reasoning-intensive tasks.
112	%
113	\citet{tam2024letmespeak} show that rigid format constraints (JSON, XML) harm performance on math and multi-hop QA but benefit classification-style tasks such as slot filling.
114	%
115	CRANE~\cite{banerjee2025crane} provides theoretical analysis of why restricting outputs to narrow grammars suppresses chain-of-thought reasoning, proposing an alternating strategy between unconstrained reasoning and constrained output phases.
116	%
117	\citet{schall2025hiddencost} conduct a systematic study across 11 models, finding 10--30\% semantic correctness degradation on reasoning tasks under structural constraints.
118	%
119	\citet{zhou2026snowballing} identify ``structure snowballing''---a failure mode where format compliance cognitive load traps models in structural patterns rather than improving reasoning during self-correction.
120	%
121	\textbf{Distinction:} OntoCoDec addresses this concern empirically: on SciERC, domain/range violations decrease from 15.4\% to 0.93\% ($\downarrow$94\%) with \emph{zero} F1 degradation (R-F1 +0.13pp, not significant). IE is an extraction task where constrained decoding's impact is minimal~\cite{tam2024letmespeak}, and OntoCoDec's constraints target only type tokens, leaving free-text spans unconstrained.
122	
123	% TODO: Add 1-2 sentences connecting to S2 strategy as an instantiation of
124	% CRANE's alternating approach, and noting that IE's extraction nature
125	% inherently avoids the reasoning-degradation regime.
126	
127	% ===========================================================================
128	% Our Approach
129	% ===========================================================================
130	\paragraph{Our Approach.}
131	OntoCoDec occupies a unique position in this landscape: it is the first system to automatically compile IE ontology schemas---including domain/range axioms---into decoding-time semantic constraints, extending grammar-constrained decoding from syntactic to semantic enforcement.
132	%
133	Unlike vocabulary-constrained methods that restrict individual tokens, OntoCoDec enforces \emph{cross-field relational constraints} through a stateful entity registry that tracks extracted types during autoregressive generation.
134	%
135	Unlike training-based IE systems, OntoCoDec is training-free and achieves near-complete elimination of type violations; unlike post-hoc validation, it prevents violations rather than detecting them, redirecting probability mass to valid alternatives at zero quality cost.
136	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f28d72d-0ed1-404c-b7e7-da471cae7358",
  "isSidechain": true,
  "promptId": "de950a36-29bd-407d-b7cc-a0f7c107be64",
  "agentId": "aa8b4c8fb42cb17c7",
  "type": "user",
  "uuid": "eb10ef0a-e639-41d4-ab84-c46c12e34527",
  "sourceToolAssistantUUID": "1f28d72d-0ed1-404c-b7e7-da471cae7358",
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

_source line 65 · 2026-05-14T10:54:23.492Z_

Now I have a thorough understanding of the paper. Let me produce my review as R2 (Novelty and Related Work focus).

---

## Review: Type-Valid IE via Compiled Ontology Constraints

**Reviewer R2 -- Focus: Novelty and Related Work**

---

### 1. Novelty Assessment

**Core idea: compiling ontology schemas into constrained decoding layers.**
The high-level idea of using ontology type constraints to mask logits during autoregressive decoding is a natural migration of techniques well-established in the code generation domain (Synchromesh, MGD, PLDI'25) to the IE domain. The paper acknowledges this lineage. The question is whether the domain transfer introduces sufficient technical novelty or whether it amounts to applying known mechanisms to a new application. My assessment: the transfer is largely straightforward. IE ontology constraints (flat domain/range sets over a small type inventory) are structurally simpler than programming language type systems (subtyping hierarchies, parametric polymorphism, scope rules). The semantic layer is a LogitsProcessor that maintains a dictionary `{entity_name -> type}` and performs set membership checks. This is not algorithmically complex.

**Two-layer decomposition (grammar + semantic).**
The decomposition is natural and arguably the only reasonable design. Grammar-constrained decoding (via XGrammar, Outlines, etc.) is an off-the-shelf capability. The semantic layer is a standard `LogitsProcessor` pattern in HuggingFace. The composition via bitwise AND is the obvious choice. I do not consider this decomposition a design innovation; it is what any competent practitioner would arrive at given the problem formulation.

**Violation landscape study.**
This is the paper's most novel empirical contribution. No prior work has systematically measured the per-relation distribution of ontology constraint violations in LLM-based IE, nor established the tightness-violation correlation. The finding that violation rates are driven by constraint tightness rather than ontology size (SciERC 15.4% vs. DocRED 18.7% despite 14x ontology size difference) is a genuine insight. The Evaluate-for regression under schema-informed prompting (24.1% to 29.9%) is a compelling finding motivating decoding-time enforcement. This study would stand as a useful contribution even without the OntoCoDec framework.

**Enabling dependency.**
The observation that the grammar layer is a prerequisite for semantic enforcement (semantic-only achieves only 24% DR reduction because OOV relation types bypass domain/range lookups) is a useful empirical finding. However, it is an *observation*, not a *design innovation*. The fact that you need valid relation types before you can look up their domain/range constraints is self-evident from the system's architecture. Quantifying the gap (3.88x enabling ratio) adds empirical substance but does not constitute methodological novelty.

**Constraint tightness analysis.**
The Spearman correlation (rho=0.52 on DocRED) between constraint tightness and residual DR is a useful diagnostic contribution. However, rho=0.52 explains only ~27% of rank variance, which limits its practical predictive value. The claim in the abstract that this provides "a priori estimates of constraint effectiveness" overstates the result. This is a moderate correlation, not a reliable prediction tool.

**Comparison to GCD (Geng et al., 2024).**
The paper correctly identifies GCD as a direct precursor operating at the syntactic level. The distinction (OntoCoDec adds cross-field semantic constraints) is clearly drawn. However, the paper should more explicitly address whether GCD's "input-dependent grammars" could be extended to encode domain/range constraints by dynamically modifying the grammar at each step -- this would be the natural GCD-based alternative to OntoCoDec's LogitsProcessor approach.

**Does the paper clearly articulate what is NEW vs. what is engineering?**
Partially. The paper correctly positions the violation landscape study and tightness correlation as novel empirical contributions. However, it overclaims the framework's novelty. Phrases like "the first method to enforce cross-field type validity during autoregressive generation for IE" are technically accurate but obscure the fact that the underlying techniques (grammar-constrained decoding, logit masking with state tracking) are well-established in other domains and the transfer is technically straightforward.

### 2. Related Work Assessment

**Coverage quality.**
The related work section is extensive (5 paradigms, ~30 references) and well-structured. The five-paradigm organization (grammar-constrained decoding, semantic constrained decoding for code, vocabulary/type-constrained generation, structural constraints via training, post-hoc validation, quality concerns) provides good coverage. The positioning within each paradigm is generally accurate. The "Our Approach" summary paragraph effectively synthesizes the distinctions.

**Important missing references:**

1. **PICARD (Scholak et al., EMNLP 2021):** This is the most significant omission. PICARD performs incremental parsing for SQL constrained decoding, maintaining state during decoding to enforce cross-field constraints (column types must match SQL operation requirements). This is methodologically very close to OntoCoDec's semantic layer -- both maintain generation state and enforce cross-field type constraints during autoregressive decoding. The paper cites PICARD's domain (SQL) but should explicitly discuss the methodological parallels.

2. **SynCode (Ugare et al., 2024):** Grammar-augmented generation with semantic actions is directly comparable to the grammar+semantic layering in OntoCoDec.

3. **REBEL (Cabot & Navigli, 2021) and TANL (Paolini et al., 2021):** End-to-end RE models that implicitly learn type constraints through training. The paper discusses UIE and GoLLIE but omits these influential baselines. The question of whether fine-tuned models already achieve low violation rates (making decoding-time enforcement unnecessary) is not addressed.

4. **DeepStruct (Wang et al., 2022):** Structure-aware pretraining for IE that learns to produce structurally valid outputs. Relevant to the training-vs-decoding discussion.

5. **Type-constrained knowledge graph embedding methods (TransE with type constraints, TransR, TKRL):** The paper claims this is the "first systematic study of ontology constraint violations in LLM-based IE," but type constraint enforcement has been studied extensively in KG embedding literature. The paper should acknowledge this broader context even if the LLM-based setting is new.

6. **Schema-guided dialogue systems (SGD, Rastogi et al., 2020):** Schema-guided generation with slot/intent constraints during dialogue, conceptually related to ontology-guided IE.

**Positioning against GoLLIE.**
The paper's positioning against GoLLIE is fair: GoLLIE provides soft structural guidance through fine-tuning on schema-as-code, while OntoCoDec provides hard decoding-time enforcement. The paper correctly notes these are complementary. However, a critical missing comparison is: what are GoLLIE's violation rates on SciERC/DocRED? If GoLLIE already achieves low DR through training, the motivation for decoding-time enforcement weakens substantially.

**Positioning against post-hoc validation.**
The positioning is adequate. The paper correctly identifies the compute waste argument (14-15% rejection rate) and the inability to redirect probability mass. However, the comparison lacks quantitative cost analysis -- how much overhead does OntoCoDec's logit masking add per token vs. the cost of regenerating 15% of triples?

**Overclaiming novelty.**
The following claims border on overclaiming:
- "the first systematic quantification of ontology constraint violations in LLM-based IE" -- type constraint violation rates have been implicitly studied in KG completion work with entity type constraints. "First for LLM-based generative IE" would be more precise.
- The decidability taxonomy (local, prefix-decidable, non-local) is presented as a contribution but is a straightforward classification that follows directly from the problem structure. Similar taxonomies exist in constraint-based code generation (Synchromesh, PICARD).

### 3. Clarity and Presentation

The paper is well-written overall. Specific observations:

- **Structure:** The violation landscape section (Section 3) preceding the method section is an effective narrative choice -- it establishes the problem's severity before presenting the solution.
- **Notation:** Consistent use of O, E, R, sigma, dom, range throughout. The shift from sigma(r) in background/violation landscape to dom(r)/range(r) in the method section creates minor notational inconsistency.
- **Tables:** The five-way ablation table (Table 1) is effective and well-designed. The cross-dataset prompt comparison table consolidating SciERC and DocRED is useful.
- **Figures:** The per-relation DR bar chart is informative. The architecture overview figure (fig1) is referenced but I did not see its content.
- **Abstract:** Includes a DocRED placeholder `\placeholder{DocRED results.}`, indicating the paper is incomplete.
- **Title:** "Type-Valid IE via Compiled Ontology Constraints" is accurate. The earlier "Near-Complete" variant was misleading for DocRED (46% reduction, 10.19% residual DR).
- **CF disclosure:** The proactive disclosure of CF trade-off (0.08% to 9.9%) in the abstract is commendable intellectual honesty.
- **Notation inconsistency:** Section 2 uses sigma: R -> P(E x E), while Section 4 uses dom: R -> 2^E and range: R -> 2^E. These are equivalent but the paper should standardize.

### 4. Strengths

- The violation landscape study (Section 3) is a genuine empirical contribution with independent value. The per-relation analysis and tightness-violation correlation provide actionable insights.
- The finding that schema-informed prompting can *increase* violations for specific relations (Evaluate-for +5.8pp) is a compelling motivation for decoding-time enforcement.
- Grammar layer generalization is a clean result: ET/RV -> 0% across both datasets with zero F1 cost.
- The ablation design (5 configurations) cleanly decomposes each layer's contribution and convincingly demonstrates the enabling dependency.
- Proactive disclosure of the CF trade-off with root cause analysis (EVR subtype, top conflict patterns) shows intellectual honesty.
- The paper correctly positions OntoCoDec as complementary to, rather than competing with, training-based approaches like GoLLIE.
- The graceful degradation mechanism (grammar-first fallback when semantic AND grammar mask is empty) is a sound engineering decision, documented with cross-dataset frequency (1/998 DocRED, 0/551 SciERC).

### 5. Weaknesses

- **Limited technical novelty of the framework itself.** The grammar layer is an application of XGrammar to an IE-specific JSON schema. The semantic layer is a standard HuggingFace LogitsProcessor maintaining a dictionary with set membership lookup. The composition is trivial bitwise AND. The enabling dependency is an empirical observation, not an algorithmic contribution. The decidability taxonomy is a straightforward classification. Collectively, this is competent engineering integration of known techniques, not a research advance in constrained decoding methodology.
- **DocRED results undermine the paper's claims.** 46% DR reduction with 10.19% residual on the more realistic 96-relation dataset is "partial improvement," not "near-complete elimination." The constraint tightness analysis explains *why* this happens but does not resolve it. For practitioners working with complex ontologies (which is the common case), the method leaves substantial violations unaddressed.
- **CF trade-off shifts rather than eliminates constraint violations.** On SciERC, DR drops from 15.37% to 0.93% but CF rises from 0.08% to 9.90%. The total violation burden is redistributed, not eliminated. The paper's argument that DR is a "hard" error while CF is "soft" is valid in principle but is not empirically substantiated through downstream task evaluation.
- **~8% relation F1 raises practical relevance questions.** In the zero-shot regime, ~92% of extracted triples are factually wrong regardless of type validity. Enforcing type constraints on predominantly incorrect extractions has limited practical value. The paper does not discuss this elephant in the room.
- **Narrow experimental scope.** Two datasets, one model (Qwen3-8B; Llama cross-model validation planned but not completed), zero-shot only. No evaluation in the few-shot or fine-tuned setting where the violation landscape may differ substantially. The "model-agnostic" claim rests on N=1 completed model.
- **PICARD omission in related work.** PICARD's incremental parsing for SQL with cross-field state maintenance is methodologically very close. This omission weakens the related work's completeness.
- **No statistical significance testing.** All results are single-seed, single-run. F1-neutrality is claimed without bootstrap confidence intervals. With ~1700 triples on SciERC, the +0.13pp difference requires statistical backing.
- **Incomplete paper.** The abstract contains `\placeholder{DocRED results.}` and the conclusion contains a placeholder. Cross-model validation (Llama-3.1-8B) is listed as "planned but NOT completed." This is not a finished manuscript.

### 6. Questions for Authors

1. How does the semantic layer differ technically from a standard HuggingFace LogitsProcessor with a dictionary lookup? What is the algorithmic contribution beyond the application to IE ontologies?

2. PICARD (Scholak et al., 2021) maintains cross-field state during SQL decoding to enforce column-type compatibility -- a direct parallel to your entity registry enforcing domain/range constraints. How does OntoCoDec's approach differ from or improve upon PICARD's methodology?

3. If GoLLIE or another fine-tuned IE model already achieves low violation rates through training, does OntoCoDec provide additional value on top of that? This is the critical practical question for the framework's utility. Have you measured violation rates for fine-tuned baselines?

4. The ~8% relation F1 means ~92% of extracted triples are factually wrong. What is the practical benefit of ensuring type validity for predominantly incorrect triples? In what scenario does a practitioner care about type-valid but factually wrong extraction?

5. The CF trade-off shifts the violation burden: DR drops by 14.4pp while CF rises by 9.8pp on SciERC. Have you measured the impact of 9.9% CF on any downstream task (KG construction, QA, reasoning)?

6. GCD (Geng et al., 2023) introduces input-dependent grammars. Could domain/range constraints be encoded as input-dependent grammar rules rather than a separate LogitsProcessor? If so, what is the advantage of the two-layer decomposition over a unified grammar approach?

7. The Spearman correlation (rho=0.52) between constraint tightness and residual DR explains only ~27% of variance. What other factors drive residual violations? Have you examined per-relation model confidence or entity type confusion patterns?

8. All reported results use a single seed. What is the variance across different random seeds or sampling strategies? Is the 0.93% DR on SciERC stable?

### 7. Preliminary Score and Confidence

**Score: 3/6 (Weak Reject)**

**Confidence: 4/5**

**Rationale:** The violation landscape study is a genuine empirical contribution and the most valuable part of this work. The tightness-violation correlation is useful analytical finding. However, the core framework -- which is presented as the main contribution -- represents competent engineering integration of known techniques (XGrammar + LogitsProcessor + bitwise AND) rather than a research advance in constrained decoding methodology. The technical novelty of migrating type-constrained decoding from code generation to IE, where the constraint structure is simpler (flat domain/range sets vs. rich type systems), does not clear the bar for a top ML venue at ~25% acceptance rate. The DocRED results (46% DR reduction, 10.19% residual) undermine the headline claims, and the CF trade-off partially offsets gains without downstream validation. The paper is also incomplete (placeholders, missing cross-model validation). The omission of PICARD -- a methodologically close predecessor -- is a notable related work gap. This work would be appropriate for a workshop, findings track, or industry track, but falls below the novelty threshold for a main conference at a top venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb10ef0a-e639-41d4-ab84-c46c12e34527",
  "isSidechain": true,
  "agentId": "aa8b4c8fb42cb17c7",
  "requestId": "req_011Cb2LQLY6LztiaTgLNtYxw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e687e74-1fe2-4cf6-9690-8749affe944c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "7202ddb9-6ca1-4076-af31-515440525a70",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DiFsSWNqUyBcyPTiESKFfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3669,
      "cache_read_input_tokens": 81000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3669,
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
