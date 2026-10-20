# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a60984db3486f111c.jsonl`
- **Structured JSON:** [`52b63a0b7edc4239eaf3.json`](../../sessions/52/52b63a0b7edc4239eaf3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-14T10:59:24.142Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus: **novelty, significance, positioning against related work, and writing quality**.

## Paper Summary

Title: "How LLMs Violate Ontology Constraints: A Landscape Study and Grammar-Based Mitigation"

The paper makes three contributions:
1. **Violation Landscape Study**: Systematic measurement of how LLMs violate ontology type constraints in zero-shot IE across SciERC (7 relations) and DocRED (96 relations), with two models (Qwen3-8B, Llama-3.1-8B). Finds DR violations concentrate on specific relations; constraint tightness predicts violation rate on SciERC (ρ=0.85) but not DocRED (ρ=0.14, p=0.18).
2. **Grammar-Constrained Decoding**: Compiles ontology schemas into CFGs via XGrammar for autoregressive decoding. Universally eliminates ET (→0%) and RV (→0%) at 14% latency overhead and zero F1 cost across both datasets.
3. **Semantic Constraint Layer (proof-of-concept)**: Per-relation domain/range enforcement via dynamic logit masking. 94% DR reduction on SciERC but only 35.5% on DocRED. Explicitly marks complex ontology scaling as open problem.

## Paper Structure (10 pages)
- §1 Introduction (contributions framed clearly)
- §2 Experimental Setup (datasets, models, violation taxonomy)
- §3 Violation Landscape Study (§3.1 rates across complexity, §3.2 per-relation distribution + tightness, §3.3 cross-model consistency)
- §4 Grammar-Constrained Decoding (§4.1 compilation, §4.2 results, §4.3 latency)
- §5 Semantic Constraint Layer (§5.1 architecture, §5.2 SciERC results, §5.3 DocRED results, §5.4 CF side effects)
- §6 Discussion
- §7 Related Work
- §8 Conclusion + Limitations
- Appendix A: S1 vs S2

## Key Results

**Table 1** (Unconstrained baselines): SciERC DR=15.4%/RV=1.39%/ET=0.4%, DocRED DR=15.8%/RV=26.5%/ET=6.8%

**Table 4** (Cross-model): Qwen DR=15.4% vs Llama DR=9.8%, rank ρ=0.82, but Llama parse=92%

**Table 6** (Grammar): ET→0%, RV→0% universally, 14% overhead, zero F1 cost. DocRED grammar-only DR=26.17% (explained as measurement artifact — RV violations previously masked DR)

**Table 8** (SciERC ablation): Full system DR=0.93% (94% reduction), CF=9.9%, enabling ratio=12.5×

**Table 9** (DocRED ablation): Full system DR=10.19% (35.5% reduction), CF=2.99%, enabling ratio=1.1×

**Table 10** (CF breakdown): EVR=380, entity duplication=85 (new side effect)

## Related Work Section (§7, brief — 4 short paragraphs)
- Grammar-constrained decoding: XGrammar [Dong et al., 2024], prior work on code gen / structured output
- Constrained text generation: NeuroLogic [Lu et al., 2022], FLAN-based instruction tuning
- Ontology-aware IE: Schema-informed prompting [Li et al., 2023], post-hoc filtering
- Type-constrained KB completion: [Krompass et al., 2015]

References: Only 7 papers cited total.

## Your Review Task

Provide a detailed review covering:

1. **Novelty Assessment**
   - How novel is each of the three contributions?
   - Is grammar-constrained decoding for IE a genuine contribution or straightforward application of XGrammar?
   - Is the violation landscape study sufficiently novel as an empirical contribution?
   - Does the semantic layer offer enough novelty given its limited effectiveness on DocRED?

2. **Significance and Impact**
   - Who would use these findings?
   - Is the grammar layer finding actionable enough to justify publication?
   - Does the violation landscape data have reuse value?
   - Is the paper positioned as empirical study or method paper — and is that positioning effective?

3. **Related Work Coverage**
   - Only 7 references — is this sufficient?
   - Missing related work areas? (structured prediction for IE, ontology learning, schema-guided generation, other constrained decoding methods like PICARD/Synchromesh, KG completion with type constraints, error analysis in IE)
   - Is the positioning against existing work fair and accurate?

4. **Writing Quality**
   - Clarity of exposition
   - Organization and flow
   - Are negative results presented honestly?
   - Title/abstract alignment with actual contributions

5. **Weaknesses** (numbered, specific)

6. **Questions for Authors** (numbered)

7. **Minor Issues**

8. **Score** (1-6) with justification

Format your review as a structured reviewer report. Be rigorous but fair. Consider whether this paper, as positioned (empirical study + targeted solution), meets the bar for a top ML venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "581709e1-d204-4142-8033-04cb68069265",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T10:59:24.145Z_

```json
{
  "parentUuid": "581709e1-d204-4142-8033-04cb68069265",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
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
  "uuid": "51504562-5533-4c4a-a3a7-4ba2d6872430",
  "timestamp": "2026-05-14T10:59:24.145Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T10:59:26.750Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51504562-5533-4c4a-a3a7-4ba2d6872430",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LvP8x86jxX4PFBHYVU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1067f2a9-b533-4c93-ad9f-9ef971556e78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015R279wfZGZSy3Ap1uDH8WD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7204,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7204,
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

_source line 4 · 2026-05-14T10:59:28.550Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EZAd9qE4Z7d9vAt8KJxqy2`</summary>

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
  "parentUuid": "1067f2a9-b533-4c93-ad9f-9ef971556e78",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LvP8x86jxX4PFBHYVU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33a86f9c-0926-48da-817a-1e8407c9c91a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015R279wfZGZSy3Ap1uDH8WD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7204,
      "cache_read_input_tokens": 8252,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7204
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 141,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 7204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7204,
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

_source line 5 · 2026-05-14T10:59:28.557Z_

<details><summary>↩ Tool result · `toolu_01EZAd9qE4Z7d9vAt8KJxqy2`</summary>

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
  "parentUuid": "33a86f9c-0926-48da-817a-1e8407c9c91a",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "bc725d28-49a0-44b7-9375-a655e05166fb",
  "sourceToolAssistantUUID": "33a86f9c-0926-48da-817a-1e8407c9c91a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T10:59:32.232Z_



Let me read the paper and project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc725d28-49a0-44b7-9375-a655e05166fb",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LviEA1oEaW47jy8CJx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90010cbf-7ac0-4034-ac56-d91d1160f174",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ye468mK1pgYSSUTax8dcD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2015,
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

_source line 7 · 2026-05-14T10:59:33.309Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TXpSfzeswiMAxcFViD7ENk`</summary>

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
  "parentUuid": "90010cbf-7ac0-4034-ac56-d91d1160f174",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LviEA1oEaW47jy8CJx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5478aa25-e754-4985-a97b-b95524af520c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ye468mK1pgYSSUTax8dcD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2015,
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

_source line 8 · 2026-05-14T10:59:33.320Z_

<details><summary>↩ Tool result · `toolu_01TXpSfzeswiMAxcFViD7ENk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| phase2_docred_semantic_only | Semantic-only constrained decoding 在 DocRED (96 relations, avg 5.68 valid pairs) 上的 DR 降低幅度。SciERC semantic_only DR↓24% (15.37→11.65%)，DocRED 约束更紧预期效果更明显。关键验证 Claim 3 enabling dependency：semantic_only 无法消除 RV/ET（需 grammar），证明两层互补非替代。 | — | — | — |\\n| phase2_docred_unconstrained | DocRED Phase 2 unconstrained baseline — 使用与 constrained 实验完全相同的 Phase 2 pipeline 和 prompt，确保消融表 F1/violation 对比公平。预期 DR~18.7%, RV~28.9%, ET~7.5%（接近 Phase 0）。 | — | — | — |\\n\\n## 待处理\\n- llama_docred_full_s1（排队等待 GPU）\\n- llama_docred_unconstrained（排队等待 GPU）\\n- llama_scierc_full_s1（排队等待 GPU）\\n- llama_scierc_unconstrained（排队等待 GPU）\\n\\n## 近期结论\\n- **phase2_docred_full_s1** (success): Grammar+Semantic 双层约束 (S1) 在 DocRED (96 relations) 上能否复现 SciERC 的 DR 消除效果 (15.37%→0.93%)？DocRED 约束更紧 (avg 5.68 valid pairs)，DR baseline 更高 (18.7%)，验证 OntoCoDec 在复杂 schema 上的泛化性。\\n  [DocRED full_s1 violation report](/api/workspace-files/projects/schema_semantic_constrained_ie/artifacts/phase2_docred_full_s1/report/violation_report_docred_full_s1.json)\\n- **phase2_docred_grammar_only** (success): Grammar-only constrained decoding 在 DocRED (96 relation types) 上能否消除 RV violations (28.9%) 和 ET violations (7.5%)？与 SciERC grammar_only (RV 1.4%→0%, ET 0.4%→0%) 对比，验证 grammar 层在复杂 schema 上的泛化性。\\n- **mvp_phase0_docred_schema_r2** (killed): Schema-informed prompt 在 DocRED (96 relation types) 上的违规率降低幅度是否小于 SciERC (7 types)？验证约束空间越大 prompt 级干预越力不从心。（从被误杀的 mvp_phase0_docred_schema 恢复，--resume）\\n\\n## 趋势\\n成功 12 / 负向 0 / 失败 0 / 共 13\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-16980: 无 GPU 信息\\n\\n## 告警\\n- mvp_phase0_docred_schema_r2: 已被终止 — unknown\\n\", \"total_chars\": 1767, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5478aa25-e754-4985-a97b-b95524af520c",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "ebffdfbe-27f3-42c6-bba4-4c508e051c70",
  "sourceToolAssistantUUID": "5478aa25-e754-4985-a97b-b95524af520c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T10:59:34.255Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016Bu6vqcdnZjst7cF2hRfLS`</summary>

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
  "parentUuid": "ebffdfbe-27f3-42c6-bba4-4c508e051c70",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LviEA1oEaW47jy8CJx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1bde9814-0eff-4161-9b09-df57f149fb93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ye468mK1pgYSSUTax8dcD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2015,
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

_source line 10 · 2026-05-14T10:59:34.268Z_

<details><summary>↩ Tool result · `toolu_016Bu6vqcdnZjst7cF2hRfLS`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bde9814-0eff-4161-9b09-df57f149fb93",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "b0fe55a2-b7ca-4d82-a974-4e65ac902c1e",
  "sourceToolAssistantUUID": "1bde9814-0eff-4161-9b09-df57f149fb93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T10:59:34.773Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KhJq3W8n4YsDb9hBE893iJ`</summary>

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
  "parentUuid": "b0fe55a2-b7ca-4d82-a974-4e65ac902c1e",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LviEA1oEaW47jy8CJx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18d5994c-75c2-4ea0-a835-61952563eb65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ye468mK1pgYSSUTax8dcD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2015,
      "cache_read_input_tokens": 15456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2015,
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

_source line 12 · 2026-05-14T10:59:34.787Z_

<details><summary>↩ Tool result · `toolu_01KhJq3W8n4YsDb9hBE893iJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper_framing.md\", \"content\": \"# OntoCoDec — Paper Framing\\n\\n## Target Venue\\nEMNLP 2026 (ARR submission May 25, 2026)\\n\\n## Title\\nOntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints\\n(Note: \\\"Guaranteed\\\" dropped per Reviewer — S1 DR=0.93%, S2 DR=0.97%, neither achieves 0%. \\\"Near-Complete\\\" is honest and defensible.)\\n\\n## Core Insight\\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero F1 cost** through automatic ontology-to-decoder constraint compilation with two complementary layers.\\n\\n**Phase 2 confirmed**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%), and is **F1-neutral** (R-F1 +0.13pp, not statistically significant — correctly framed as \\\"zero cost\\\", not \\\"improvement\\\").\\n\\n## Core Claims\\n\\n### Claim 1 (Empirical): Violation Landscape\\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\\n\\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\\n\\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\\n\\n### Claim 2 (Empirical): Prompt Insufficiency\\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\\n\\n**Narrative**: This is NOT about \\\"5.78% barely above 5%\\\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\\n\\n### Claim 3 (Methodological): Composable Constraint Framework\\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\\n\\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \\\"synergistic\\\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\\n\\nThe two layers compose via bitwise AND of token masks. Recommended framing: \\\"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\\\"\\n\\n**Graceful degradation** (per Reviewer assessment, D008): When $M_{semantic} \\\\cap M_{grammar} = \\\\emptyset$ (semantic layer would mask all grammar-valid tokens), the system falls back to grammar-only control. Occurred 1/998 DocRED docs (0.1%), 0/551 SciERC sentences — consistent with tighter constraints increasing empty-intersection likelihood. Implementation is error recovery (fallback), NOT formal invariant guarantee. Do NOT frame as \\\"provable composition\\\" — fallback's existence is counter-evidence. Frame as \\\"engineering robustness\\\" in §4; mention cross-dataset observation in §5 Discussion (1-2 sentences, N=1 too weak for dedicated analysis).\\n\\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\\n\\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\\n\\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\\n\\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\\n\\n## Anticipated Reviewer Concerns\\n\\n### C1: \\\"5.78% is barely above 5% — threshold is arbitrary\\\"\\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\\n\\n### C2: \\\"Why not just post-hoc filter?\\\"\\n**Response**: (a) Post-hoc wastes compute on invalid outputs (14-15% rejection rate); (b) cannot redirect probability mass to valid alternatives; (c) for streaming/real-time extraction, post-hoc filtering is too late. Post-hoc approaches (e.g., SHACL/DL reasoner-based validation, Alviano et al. IJCAI 2025 ASP-based structured knowledge verification) validate constraints after generation but cannot correct invalid outputs during decoding. ⚠️ 原引用 \\\"LLM+ASP (ICLP 2025)\\\" 已核实为不准确（venue/方法描述均有误），已修正。\\n\\n### C3: \\\"Bitwise AND of two masks is not novel\\\"\\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\\n\\n### C4: \\\"Evaluate-for violation rate increases with schema-informed prompt\\\"\\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\\\"Method X evaluates for Task Y\\\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \\\"harder instances\\\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\\n\\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\\n\\n### C5: \\\"Only tested on one model (Qwen3-8B)\\\"\\n**Response**: Phase 0 establishes methodology; cross-model validation (Llama-3.1-8B, 70B quantized) planned for Phase 2 if time permits. The constraint compiler is model-agnostic — only the tokenizer-specific first-token verification needs re-running per model.\\n\\n### C6: \\\"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\\\"\\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Phase 2 confirms F1-neutral**: S1 R-F1 0.0836 (+0.13pp vs unconstrained 0.0823), S2 R-F1 0.0803 (-0.20pp vs unconstrained). Both within noise on ~1700 triples. Frame as: \\\"Constraint enforcement is F1-neutral — extraction quality is preserved while violations are near-eliminated.\\\" Do NOT claim F1 improvement (single seed, no bootstrap CI). Note: S2 shows marginally lower F1 and fewer triples (1644 vs 1729) — two-pass does not improve quality.\\n\\n### C7: \\\"Your method trades DR violations for CF violations (cross-field consistency)\\\"\\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\\n\\n**CF 子类型分析（根因已确认）**：\\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\\n\\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\\n\\n**论证层次**：\\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\\n\\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \\\"CF 是 semantic type enforcement 的系统性副作用\\\" 提供干净的消融证据。\\n\\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\\n\\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\\n\\n### C8: \\\"Absolute F1 is too low (~8%) — results are not meaningful\\\"\\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \\\"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\\\"\\n\\n## Paper Structure (Draft)\\n1. Introduction: Violation landscape motivation + composable constraint framework overview\\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\\n5. Experiments: Constrained vs unconstrained vs post-hoc vs prompt-based\\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology)\\n7. Conclusion\\n\\n## Claim Calibration (per Reviewer assessment)\\n\\n**Safe to claim (sufficient evidence from Phase 2)**:\\n- \\\"First systematic study of ontology constraint violations in LLM-based IE\\\"\\n- \\\"Violation rate correlates with constraint tightness, not ontology size\\\"\\n- \\\"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\\\" ✅ Phase 2 confirmed\\n- \\\"Two-layer architecture provides complementary coverage — grammar enables semantic\\\" ✅ Ablation confirmed\\n- \\\"Prompt-level intervention scales poorly with ontology complexity\\\" ✅ SciERC ↓62% vs DocRED ↓32%\\n\\n**Claim with caution**:\\n- \\\"Near-complete type-valid IE\\\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \\\"Near-Complete\\\"\\n- \\\"Principled framework applicable to arbitrary IE ontologies\\\" — validated on 2 datasets + 1 model only\\n- \\\"F1 improvement\\\" — NOT statistically significant, frame as F1-neutral only\\n- \\\"CF reveals type system ambiguity\\\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\\\"因为是 type ambiguity 所以 CF 可接受\\\"\\n\\n**Do NOT claim**:\\n- \\\"General infrastructure for IE\\\" — only zero-shot extraction validated\\n- \\\"State-of-the-art\\\" — F1 is control variable, not optimization target (see C8)\\n- \\\"Synergistic effect\\\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\\n- \\\"S2 solves CF\\\" or \\\"S2 mitigates Structure Snowballing\\\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\\n- \\\"Pilot50 DR=0%\\\" — small-sample artifact, full S2 has DR=0.97%\\n- \\\"Grammar-first invariant\\\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\\n- \\\"Robust dual-layer composition across schema complexities\\\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\\n\\n## Risk Ranking (ordered by reject probability)\\n\\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\\n2. **Single model limitation** (MEDIUM-HIGH): Only Qwen3-8B tested. Mitigation: Llama-3.1-8B cross-model validation if time permits.\\n3. **Novelty perception** (MEDIUM): \\\"PLDI'25 for code → OntoCoDec for IE\\\" attack line. Must argue IE constraint structure differs fundamentally.\\n4. **DocRED Phase 2 weak** (MEDIUM): If constrained decoding on DocRED (96 types) shows weaker gains or higher CF, claim generality is weakened.\\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral. No longer a risk.\\n\\n## Critical Path to EMNLP Submission (May 25)\\n\\n- **May 13-14**: Phase 0 complete ✅ + Phase 1 integration ✅\\n- **May 14 (now)**: Phase 2 SciERC core results confirmed ✅ (unconstrained/grammar/semantic/full_s1). full_s2 running, DocRED Phase 2 starting.\\n- **May 15-17**: DocRED Phase 2 (grammar_only + full_s1) + S2 analysis + CF deep dive + Evaluate-for error cases\\n- **May 17-19**: Cross-model (Llama-3.1-8B) if time permits + ablation gaps\\n- **May 19-24**: Paper writing (Paper Agent) + submission\\n\\n**Current bottleneck**: DocRED Phase 2 cross-dataset validation. GPU 0 should be running DocRED grammar_only NOW.\\n\\n## Status\\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\\n- Phase 2 SciERC S1: ✅ Complete (full_s1 DR↓94%, F1-neutral)\\n- Phase 2 SciERC S2: ✅ Complete (551/551, DR=0.97%, CF=8.03%, R-F1=8.03% — no advantage over S1)\\n- Phase 2 DocRED: 🔄 grammar_only running on cuda:0 (29/998)\\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9%, S2 8.03%, both from independent per-relation enforcement)\\n\", \"total_chars\": 16503, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18d5994c-75c2-4ea0-a835-61952563eb65",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "e83b2285-ef72-4a9c-8647-3f47e396036e",
  "sourceToolAssistantUUID": "18d5994c-75c2-4ea0-a835-61952563eb65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T10:59:38.735Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019u5BNpsacDCzUYB3fEVDnF`</summary>

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
  "parentUuid": "e83b2285-ef72-4a9c-8647-3f47e396036e",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LwAuGuya3ZQTAk1njt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d7a2487-e766-4627-8ede-322962858e63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017sfBeBrdEp2r3ZujyjraGr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7008,
      "cache_read_input_tokens": 17471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7008,
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

_source line 14 · 2026-05-14T10:59:38.756Z_

<details><summary>↩ Tool result · `toolu_019u5BNpsacDCzUYB3fEVDnF`</summary>

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
  "parentUuid": "7d7a2487-e766-4627-8ede-322962858e63",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "f07e94ca-fda4-4e71-9870-4df445e8cf84",
  "sourceToolAssistantUUID": "7d7a2487-e766-4627-8ede-322962858e63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T10:59:39.549Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012vXZ8n5unfUFM7xz37saJt`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f07e94ca-fda4-4e71-9870-4df445e8cf84",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LwAuGuya3ZQTAk1njt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75e262fc-f16a-4f1f-a8a1-5ff05db264ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017sfBeBrdEp2r3ZujyjraGr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7008,
      "cache_read_input_tokens": 17471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7008,
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

_source line 16 · 2026-05-14T10:59:39.567Z_

<details><summary>↩ Tool result · `toolu_012vXZ8n5unfUFM7xz37saJt`</summary>

```text
figures/paper/fig1_overview.pdf
artifacts/_project/chart/fig1_overview.pdf
figures/paper/fig2_per_relation_dr.pdf
artifacts/_project/chart/fig2_per_relation_dr.pdf
figures/paper/fig3_ablation_layers.pdf
artifacts/dream_reports/dream_20260514T094226/best/paper.pdf
artifacts/dream_reports/dream_20260514T094226/median/paper.pdf
artifacts/dream_reports/dream_20260514T094226/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75e262fc-f16a-4f1f-a8a1-5ff05db264ad",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "15db16db-2416-447c-ac54-ebe86de3ae59",
  "sourceToolAssistantUUID": "75e262fc-f16a-4f1f-a8a1-5ff05db264ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T10:59:40.150Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RhoHJLQQCdCnNsgUNzr4cj`</summary>

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
  "parentUuid": "15db16db-2416-447c-ac54-ebe86de3ae59",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LwAuGuya3ZQTAk1njt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f84ab17e-da5d-4c7c-9422-3387bc7efda5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017sfBeBrdEp2r3ZujyjraGr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7008,
      "cache_read_input_tokens": 17471,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7008,
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

_source line 18 · 2026-05-14T10:59:40.174Z_

<details><summary>↩ Tool result · `toolu_01RhoHJLQQCdCnNsgUNzr4cj`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f84ab17e-da5d-4c7c-9422-3387bc7efda5",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "6844a008-d623-477e-b5a4-a94898da93c0",
  "sourceToolAssistantUUID": "f84ab17e-da5d-4c7c-9422-3387bc7efda5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T10:59:40.720Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Ggz2MUEGFqNguMtE4nq185`</summary>

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
  "parentUuid": "6844a008-d623-477e-b5a4-a94898da93c0",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LwAuGuya3ZQTAk1njt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "627bcfda-4563-48e6-908a-0f9c3e945292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017sfBeBrdEp2r3ZujyjraGr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7008,
      "cache_read_input_tokens": 17471,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7008
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 369,
          "cache_read_input_tokens": 17471,
          "cache_creation_input_tokens": 7008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7008,
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

_source line 20 · 2026-05-14T10:59:40.735Z_

<details><summary>↩ Tool result · `toolu_01Ggz2MUEGFqNguMtE4nq185`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/ROADMAP.md\", \"content\": \"# schema_semantic_constrained_ie — Research Dashboard\\n\\n> 最后更新: 2026-05-14 06:19 UTC | 更新原因: Reviewer 实测时间线修正 + D009 cross-model 升级为 should-have\\n\\n## 核心方向\\nSchema-semantic constrained decoding for information extraction：利用 ontology schema 在 LLM 解码时施加 grammar + semantic 双层约束，近乎消除 domain/range 违规且不损失 F1。详见 paper_framing.md。\\n\\n## 当前进展\\n**阶段**: Research — Phase 2 SciERC 完成，DocRED 跨数据集验证中 + 论文写作并行\\n**投稿目标**: EMNLP 2026 ARR May 25 | 内部初稿 DDL May 19（距今 5 天）\\n\\n**SciERC Phase 2 核心结果**（全部完成）：\\n- Full S1 (grammar+semantic): DR 15.37%→0.93% (↓94%), R-F1 +0.13pp, ET/RV→0% ← **主推策略**\\n- Full S2 (two-pass): 降级为 ablation (D007)\\n- Grammar only / Semantic only: 两层互补确认\\n\\n**DocRED Phase 2**（4 实验消融）：\\n- grammar_only: RUNNING cuda:0 (653/998, ~20s/doc, 预计 May 14 ~17:00 UTC)\\n- full_s1: RUNNING cuda:1 (568/998, 预计 May 14 ~16:30 UTC)\\n- semantic_only + unconstrained: QUEUED → 预计 May 14 晚至 May 15 凌晨完成\\n- **全部 4 实验预计 May 15 早间就绪**（Reviewer 实测，比初估提前 2-3 天）\\n\\n**Cross-model 验证** (D009, should-have)：\\n- Llama-3.1-8B SciERC: unconstrained + full_s1（2 组，4-6 GPU·h）\\n- 安排在 DocRED 完成后 (May 15)，预计 May 15-16 完成\\n\\n**论文写作进度**：\\n- ✅ §1 Intro, §4 Method, §4.x Composition, §5 SciERC, §6 RelWork, Tables×4, Figs×3\\n- ✅ §2 Background（3 subsections, ~580 words）\\n- ✅ §3 Violation Landscape（4 subsections, per-relation + prompt insufficiency）\\n- ✅ .bib 全部完成（RelWork 9篇 + 新论文 9篇，WebSearch 验证）\\n- ✅ Abstract 初稿（~231 words, DocRED placeholder）\\n- ✅ §7 Conclusion 初稿（~400 words, DocRED placeholder）\\n- ❌ §5 DocRED subsection（等实验结果 → 填 placeholder）\\n- ❌ §5 Cross-model（等 Llama 结果）\\n- May 18-19: 全文校对 + 一致性 → May 19 内部稿\\n\\n## 近期任务\\n- [ ] DocRED grammar_only + full_s1 完成 → 立即提交 QUEUED 两个\\n- [ ] §2 Background + §3 Violation Landscape 完成\\n- [ ] .bib 完成 + 引用验证\\n- [ ] DocRED 4 实验全部完成 → §5 DocRED subsection\\n- [ ] Llama-3.1-8B SciERC 环境准备 + 2 组实验 (D009)\\n- [ ] §5 Cross-model subsection\\n- [ ] Abstract + §7 Conclusion\\n- [ ] experiment_plan.yaml 补全（低优先级，提交前）\\n- [ ] 全文校对 + 一致性检查\\n\\n## GPU 预算\\n- 分配: westd-16980 cuda:0 + cuda:1 (2× GPU)\\n- 当前: 2/2 满载（grammar_only + full_s1）\\n- 预计释放: May 14 ~17:00 UTC → 立即接 QUEUED\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D009 | 2026-05-14 | Llama-3.1-8B cross-model 验证升级为 should-have，SciERC- | phase2_scierc_full_s1, phase2_scierc_unconstrained |\\n| D008 | 2026-05-14 | 补跑 DocRED semantic_only 完成跨数据集全消融；论文写作提前至 DocRED 分 | phase2_docred_grammar_only, phase2_docred_full_s1, phase2_scierc_semantic_only |\\n| D007 | 2026-05-14 | S2 降级为架构 ablation，S1 为主推策略；标题去掉 \\\"Guaranteed\\\" 改 \\\"Ne | phase2_scierc_full_s2, phase2_scierc_full_s1 |\\n| D006 | 2026-05-14 | Phase 2 SciERC 核心结果确认：Full S1 DR -94% 且 F1 无损，CF v | phase2_scierc_unconstrained, phase2_scierc_grammar_only, phase2_scierc_semantic_only, phase2_scierc_full_s1, mvp_phase0_docred_schema |\\n| D005 | 2026-05-14 | Phase 2 SciERC 核心结果确认：Full S1 DR↓94% F1无损，CF viola | phase2_scierc_unconstrained, phase2_scierc_grammar_only, phase2_scierc_semantic_only, phase2_scierc_full_s1 |\\n| D004 | 2026-05-14 | Phase 2 SciERC 核心结果确认：grammar+semantic (full_s1) D | phase2_scierc_unconstrained, phase2_scierc_grammar_only, phase2_scierc_semantic_only, phase2_scierc_full_s1 |\\n| D003 | 2026-05-13 | MVP 通过，进入 Research 阶段，立即启动 Phase 2 constrained dec | mvp_phase0_violation_rate, mvp_phase0_scierc_schema, mvp_phase0_violation_rate_docred |\\n| D002 | 2026-05-13 | SciERC Phase 0 结果确认 GO — domain_range violation ra | mvp_phase0_violation_rate |\\n| D001 | 2026-05-13 | 主目标调整为 EMNLP 2026 ARR (5/25), AAAI 2027 为后备 | — |\\n\\n\\n\", \"total_chars\": 3432, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "627bcfda-4563-48e6-908a-0f9c3e945292",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "effb3af6-b51a-44d2-a819-f5c66a0d1eb0",
  "sourceToolAssistantUUID": "627bcfda-4563-48e6-908a-0f9c3e945292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-14T10:59:44.331Z_

Let me read the actual paper (the "best" tier dream report) and the individual paper sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "effb3af6-b51a-44d2-a819-f5c66a0d1eb0",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LwcJVDoYEdZA32HGSE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af18281a-5e3e-4f84-9c1a-b154d3d02f51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bc6W2eM6Ds9nWsuyL3fZs5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3143,
      "cache_read_input_tokens": 24479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3143,
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

_source line 22 · 2026-05-14T10:59:47.168Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Jq4ZLMxbLNjnSRxfGnWsMm`</summary>

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
  "parentUuid": "af18281a-5e3e-4f84-9c1a-b154d3d02f51",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LwcJVDoYEdZA32HGSE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6181bf67-6e31-4458-8e8b-d5c31ef02bf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bc6W2eM6Ds9nWsuyL3fZs5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3143,
      "cache_read_input_tokens": 24479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3143,
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

_source line 23 · 2026-05-14T10:59:47.174Z_

<details><summary>↩ Tool result · `toolu_01Jq4ZLMxbLNjnSRxfGnWsMm`</summary>

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
  "parentUuid": "6181bf67-6e31-4458-8e8b-d5c31ef02bf1",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "a2132529-52cc-44b4-a53f-5cd72b66065d",
  "sourceToolAssistantUUID": "6181bf67-6e31-4458-8e8b-d5c31ef02bf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T10:59:47.601Z_

<details open><summary>🔧 Tool call — Read · `toolu_014PGc3h5SmdjrbyLDVwdDWC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/median/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2132529-52cc-44b4-a53f-5cd72b66065d",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LwcJVDoYEdZA32HGSE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cdf7fc13-7a8f-4718-836d-bab42d2b2a4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bc6W2eM6Ds9nWsuyL3fZs5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3143,
      "cache_read_input_tokens": 24479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3143,
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

_source line 25 · 2026-05-14T10:59:47.622Z_

<details><summary>↩ Tool result · `toolu_014PGc3h5SmdjrbyLDVwdDWC`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=2.5cm]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{amsmath}
8	\usepackage{amssymb}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{tabularx}
12	\usepackage{enumitem}
13	\usepackage{natbib}
14	\usepackage{hyperref}
15	
16	\title{Type-Valid IE via Compiled Ontology Constraints}
17	
18	\author{Anonymous}
19	
20	\date{}
21	
22	\begin{document}
23	\maketitle
24	
25	% ===========================================================================
26	% ABSTRACT
27	% ===========================================================================
28	\begin{abstract}
29	Large language models used for zero-shot information extraction systematically violate ontology type constraints---15.4\% of extracted triples on SciERC and 18.7\% on DocRED contain domain/range violations.
30	These violations are not uniformly distributed: they concentrate on relation types with tight type signatures, while loose-constraint relations exhibit near-zero violation rates.
31	We present \textsc{OntoCoDec}, a framework that automatically compiles IE ontology schemas into two composable constrained decoding layers: (1) a \emph{grammar layer} that enforces JSON structure and valid relation/entity-type vocabularies via context-free grammar constraints, and (2) a \emph{semantic layer} that enforces cross-field domain/range constraints through a stateful entity registry with dynamic logit masking.
32	The grammar layer eliminates entity-type and relation-vocabulary violations entirely (0\%) across both datasets---a result that generalizes perfectly regardless of ontology complexity.
33	On SciERC, the full system reduces domain/range violations by 94\% (15.4\%$\to$0.93\%) at zero F1 cost.
34	On DocRED, a complex 96-relation ontology stress test, violations decrease by 46\% (18.7\%$\to$10.2\%), with 55\% of relation types reaching near-zero residual violation rates.
35	A per-relation analysis reveals that constraint tightness significantly predicts residual violation rate (Spearman $\rho{=}0.82$ on SciERC, $\rho{=}0.37$ on DocRED, both $p{<}0.05$), establishing ontology structure as the primary determinant of constraint effectiveness.
36	\end{abstract}
37	
38	% ===========================================================================
39	% 1. INTRODUCTION
40	% ===========================================================================
41	\section{Introduction}
42	
43	Information extraction (IE) systems built on large language models (LLMs) increasingly operate in a zero-shot or few-shot paradigm, using natural language prompts to specify extraction schemas.
44	While this paradigm eliminates the need for task-specific training data, it introduces a systematic failure mode: \emph{ontology constraint violations}---extracted triples whose subject or object entity types fall outside the domain/range specifications of their relation type.
45	
46	Consider a scientific IE ontology that defines the relation \textsc{Feature-of} with domain \{Method, OtherScientificTerm\} and range \{Task, Method, Material\}.
47	An LLM extracting from ``\emph{BERT achieves state-of-the-art on NER}'' might produce the triple (BERT\textsubscript{Method}, Feature-of, NER\textsubscript{Task})---a valid extraction.
48	But it might equally produce (BERT\textsubscript{Generic}, Feature-of, NER\textsubscript{Metric})---a triple that violates both domain and range constraints, yielding a structurally invalid knowledge graph entry that downstream systems cannot consume.
49	
50	How prevalent are such violations?
51	Our systematic measurement across two standard IE benchmarks reveals that they are both common and concentrated.
52	On SciERC \cite{luan2018multi}, 15.4\% of triples extracted by Qwen3-8B violate domain/range constraints.
53	On DocRED \cite{yao2019docred}, with a substantially larger 96-relation ontology, the rate is 18.7\%.
54	Critically, these violations are not uniformly distributed across relation types: on SciERC, \textsc{Compare} exhibits a 42.4\% violation rate while \textsc{Used-for} shows only 0.8\%.
55	The driving factor is \emph{constraint tightness}---the ratio of valid type pairs to all possible type pairs for a given relation---not ontology size.
56	
57	Schema-informed prompting (explicitly describing type constraints in the prompt) reduces violations by 62\% on SciERC but only 32\% on DocRED, and can even increase violations for specific relations where prompt-level constraint signals conflict with the model's distributional priors.
58	This motivates a decoding-time approach that operates on logits rather than reasoning.
59	
60	We propose \textsc{OntoCoDec}, a framework that automatically compiles IE ontology schemas into constrained decoding configurations.
61	\textsc{OntoCoDec} provides two composable constraint layers:
62	
63	\begin{enumerate}[leftmargin=*,nosep]
64	\item \textbf{Grammar layer}: Compiles the ontology's relation names and entity type vocabulary into a context-free grammar enforced via XGrammar \cite{dong2024xgrammar}, ensuring every generated token sequence forms valid JSON with in-vocabulary relation and entity types.
65	\item \textbf{Semantic layer}: Maintains a stateful entity registry during autoregressive generation and dynamically masks logits to enforce domain/range constraints, ensuring that entity types in relation triples are compatible with the declared type signature of the relation.
66	\end{enumerate}
67	
68	These layers exhibit an \emph{enabling dependency}: the grammar layer ensures every generated relation name is in the valid vocabulary, which is a prerequisite for the semantic layer to look up and enforce domain/range rules.
69	This enabling effect is strong on tight ontologies (SciERC: 3.9$\times$ amplification) and attenuated on loose ontologies (DocRED: 1.6$\times$), where semantic constraints achieve meaningful reduction even without perfect grammar support.
70	
71	Our contributions are:
72	\begin{enumerate}[leftmargin=*,nosep]
73	\item A systematic \textbf{violation landscape study} establishing that LLM-based IE violates ontology constraints at non-trivial rates, with violation concentration driven by constraint tightness (\S\ref{sec:landscape}).
74	\item The \textbf{grammar layer}'s perfect generalization: entity-type and relation-vocabulary violations drop to 0\% on both SciERC and DocRED---a co-equal contribution alongside semantic DR reduction (\S\ref{sec:experiments}).
75	\item A composable \textbf{constrained decoding framework} that compiles ontology schemas into grammar + semantic constraint layers, reducing domain/range violations by 94\% on SciERC at zero F1 cost, demonstrated on SciERC and partially confirmed on DocRED (\S\ref{sec:method}, \S\ref{sec:experiments}).
76	\end{enumerate}
77	
78	% ===========================================================================
79	% 2. BACKGROUND
80	% ===========================================================================
81	\section{Background}
82	
83	\paragraph{IE Ontology Constraints.}
84	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ consists of entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a type signature function $\sigma: \mathcal{R} \to 2^{\mathcal{E}} \times 2^{\mathcal{E}}$ mapping each relation to its valid domain and range type sets.
85	A triple $(e_s, r, e_o)$ with $\text{type}(e_s) = t_s$ and $\text{type}(e_o) = t_o$ satisfies domain/range constraints iff $t_s \in \sigma_d(r)$ and $t_o \in \sigma_r(r)$.
86	
87	We define the \emph{constraint tightness} of a relation $r$ as:
88	\begin{equation}
89	\tau(r) = 1 - \frac{|\sigma_d(r)| \cdot |\sigma_r(r)|}{|\mathcal{E}|^2}
90	\end{equation}
91	where $\tau(r) \to 1$ indicates tight constraints (few valid type pairs) and $\tau(r) \to 0$ indicates loose constraints (most type pairs valid).
92	
93	\paragraph{Grammar-Constrained Decoding.}
94	Grammar-constrained decoding restricts LLM generation to strings accepted by a formal grammar, typically a context-free grammar (CFG).
95	At each decoding step, a token mask $M_t \in \{0,1\}^{|V|}$ is computed from the current grammar automaton state, zeroing out logits for tokens that would lead to grammatically invalid continuations.
96	XGrammar \cite{dong2024xgrammar} implements this efficiently via compiled pushdown automata with adaptive token mask caching, achieving per-token overhead proportional to cache miss rate rather than grammar size.
97	
98	\paragraph{Decidability Taxonomy.}
99	We classify IE ontology constraints by their amenability to enforcement during forward-only autoregressive decoding:
100	\begin{itemize}[leftmargin=*,nosep]
101	\item \textbf{Purely local}: Entity type $\in \mathcal{E}$, relation name $\in \mathcal{R}$ --- decidable from grammar alone.
102	\item \textbf{Prefix-decidable with state}: Domain/range constraints --- decidable given an entity registry tracking types assigned earlier in the sequence.
103	\item \textbf{Truly non-local}: Forward coreference consistency --- requires future context, out of scope for forward-only decoding.
104	\end{itemize}
105	
106	% ===========================================================================
107	% 3. VIOLATION LANDSCAPE STUDY
108	% ===========================================================================
109	\section{Violation Landscape Study}
110	\label{sec:landscape}
111	
112	Before developing constrained decoding methods, we conduct a systematic measurement of ontology constraint violations in LLM-based zero-shot IE.
113	This study constitutes an independent empirical contribution: to our knowledge, no prior work has characterized the distribution of type constraint violations across relation types in LLM-generated IE outputs.
114	
115	\subsection{Setup}
116	
117	We evaluate Qwen3-8B \cite{qwen2025qwen3} on two standard IE benchmarks:
118	\begin{itemize}[leftmargin=*,nosep]
119	\item \textbf{SciERC} \cite{luan2018multi}: 551 scientific abstracts, 7 relation types, 6 entity types. A tight ontology where most relations have restricted type signatures.
120	\item \textbf{DocRED} \cite{yao2019docred}: 998 Wikipedia documents, 96 relation types, 6 entity types. A loose ontology where many relations accept multiple type pairs.
121	\end{itemize}
122	
123	Extraction uses a minimal zero-shot prompt requesting structured JSON output with entity lists and relation triples.
124	We measure four violation types: \textbf{domain/range (DR)} --- entity type outside the relation's valid domain or range; \textbf{relation vocabulary (RV)} --- relation name not in ontology; \textbf{entity type (ET)} --- entity type not in ontology; \textbf{cross-field consistency (CF)} --- same entity assigned different types across mentions.
125	
126	\subsection{Overall Violation Rates}
127	
128	\begin{table}[t]
129	\centering
130	\small
131	\begin{tabular}{lcccccc}
132	\toprule
133	\textbf{Dataset} & $|\mathcal{R}|$ & \textbf{DR} & \textbf{RV} & \textbf{ET} & \textbf{CF} & \textbf{R-F1} \\
134	\midrule
135	SciERC & 7 & 15.4\% & 1.4\% & 0.4\% & 0.1\% & 8.23\% \\
136	DocRED & 96 & 18.7\% & 28.9\% & 7.5\% & 0.1\% & 8.24\% \\
137	\bottomrule
138	\end{tabular}
139	\caption{Baseline violation rates for zero-shot IE with Qwen3-8B. DR and RV rates are comparable despite 14$\times$ ontology size difference, while DocRED shows substantially higher RV and ET rates due to the model's difficulty with 96 relation names.}
140	\label{tab:baseline-violations}
141	\end{table}
142	
143	Table~\ref{tab:baseline-violations} reveals two key findings.
144	First, domain/range violation rates are comparable across the two datasets (15.4\% vs 18.7\%) despite a 14$\times$ difference in ontology size, suggesting that violation rate is not primarily driven by ontology complexity.
145	Second, DocRED exhibits dramatically higher RV (28.9\% vs 1.4\%) and ET (7.5\% vs 0.4\%) rates---the model frequently generates relation names and entity types outside the valid vocabulary when confronted with 96 relation types.
146	
147	\subsection{Per-Relation Violation Distribution}
148	
149	The aggregate rates mask a highly non-uniform distribution across relation types.
150	On SciERC, \textsc{Compare} exhibits a 42.4\% DR rate and \textsc{Feature-of} 33.5\%, while \textsc{Used-for} shows only 0.8\%.
151	The pattern is clear: relations with tight type signatures (few valid domain-range pairs relative to total possible pairs) concentrate violations.
152	
153	\begin{table}[t]
154	\centering
155	\small
156	\begin{tabular}{lrrrl}
157	\toprule
158	\textbf{DR Range} & \textbf{Count} & \textbf{Frac.} & \textbf{Cum. V\%} & \textbf{Examples} \\
159	\midrule
160	$= 0$ & 28 & .318 & 0\% & P17, P131, P27 \\
161	$(0, .02]$ & 20 & .227 & 3\% & P26, P22, P30 \\
162	$(.02, .10]$ & 15 & .170 & 16\% & P159, P36, P150 \\
163	$(.10, .25]$ & 13 & .148 & 39\% & P361, P527, P37 \\
164	$(.25, .50]$ & 10 & .114 & 82\% & P31, P1001, P1344 \\
165	$> .50$ & 2 & .023 & 100\% & P710, P172 \\
166	\bottomrule
167	\end{tabular}
168	\caption{Per-relation DR distribution on DocRED (full\_s1, 88 active relations). Over half of relation types achieve near-zero residual DR, while the top 12 relations contribute 82\% of all violations.}
169	\label{tab:docred-per-relation-dr}
170	\end{table}
171	
172	On DocRED, Table~\ref{tab:docred-per-relation-dr} shows that 54.5\% of relation types (48/88 with predictions) achieve near-zero DR ($\leq$0.02) under full constrained decoding, while a long tail of 12 relations accounts for 82\% of all remaining violations.
173	The most violated relation, P31 (instance\_of), has a DR of 41.9\% despite moderate constraint tightness (55th percentile), driven by extreme subject polysemy---the same entity is typed ORG, LOC, or MISC depending on context.
174	
175	\subsection{Constraint Tightness Predicts Violation Rate}
176	
177	\begin{table}[t]
178	\centering
179	\small
180	\begin{tabular}{lcccl}
181	\toprule
182	\textbf{Dataset} & $N$ & $\rho$ & $p$ & \textbf{Interpretation} \\
183	\midrule
184	SciERC & 7 & 0.82 & .023 & Strong positive \\
185	DocRED & 88 & 0.37 & .018 & Weak--moderate \\
186	\bottomrule
187	\end{tabular}
188	\caption{Spearman rank correlation between constraint tightness and residual DR. The relationship is significant on both datasets but substantially weaker on DocRED due to outlier noise from model priors and entity polysemy.}
189	\label{tab:spearman}
190	\end{table}
191	
192	Table~\ref{tab:spearman} reports Spearman rank correlations between constraint tightness and residual DR.
193	On SciERC, the correlation is strong ($\rho{=}0.82$, $p{=}0.023$), consistent with the clear per-relation gradient from \textsc{Used-for} (loose, low DR) to \textsc{Compare} (tight, high DR).
194	On DocRED, the correlation is weaker but significant ($\rho{=}0.37$, $p{=}0.018$), explaining only $\sim$14\% of DR variance.
195	
196	The attenuation on DocRED arises from two classes of outliers.
197	\textbf{Tight-but-low-DR} relations (P26 \textsc{spouse}, P22 \textsc{father}) have extremely restricted type signatures (PER$\to$PER only) but near-zero violation rates because the model has strong distributional priors for kinship relations.
198	\textbf{Loose-but-high-DR} relations (P31 \textsc{instance\_of}, P361 \textsc{part\_of}) have many valid type pairs but high violation rates due to entity polysemy and ORG/LOC boundary confusion.
199	These outliers indicate that constraint tightness is a necessary but not sufficient predictor---model prior alignment and entity type ambiguity are additional factors (\S\ref{sec:discussion}).
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cdf7fc13-7a8f-4718-836d-bab42d2b2a4b",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "8fab5de1-6319-4d22-826f-84f23df4d3ba",
  "sourceToolAssistantUUID": "cdf7fc13-7a8f-4718-836d-bab42d2b2a4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T10:59:54.441Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XofZPjTAaG5KFXCMaxspwJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fab5de1-6319-4d22-826f-84f23df4d3ba",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2Lx7vTrJTYVdXWPX8kt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d20b739-40de-4348-a76a-0f59c0d86cbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mchX4Ft2qWV7xmjeznFLT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9676,
      "cache_read_input_tokens": 27622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9676,
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

_source line 27 · 2026-05-14T10:59:54.452Z_

<details><summary>↩ Tool result · `toolu_01XofZPjTAaG5KFXCMaxspwJ`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d20b739-40de-4348-a76a-0f59c0d86cbc",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "41bcebe2-2442-440b-a63c-71f38bfb92c6",
  "sourceToolAssistantUUID": "2d20b739-40de-4348-a76a-0f59c0d86cbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T10:59:55.103Z_

<details open><summary>🔧 Tool call — Read · `toolu_018kvNi34zAZeqzTAKfsGjFS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/median/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41bcebe2-2442-440b-a63c-71f38bfb92c6",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2Lx7vTrJTYVdXWPX8kt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d68a512-9201-48ae-ac2f-21a772603ee7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013mchX4Ft2qWV7xmjeznFLT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9676,
      "cache_read_input_tokens": 27622,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9676
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 27622,
          "cache_creation_input_tokens": 9676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9676,
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

_source line 29 · 2026-05-14T10:59:55.116Z_

<details><summary>↩ Tool result · `toolu_018kvNi34zAZeqzTAKfsGjFS`</summary>

```text
200	
201	\subsection{Prompt-Level Intervention is Insufficient}
202	
203	Schema-informed prompting---explicitly describing domain/range constraints in the prompt---reduces DR by 62\% on SciERC (15.4\%$\to$5.78\%) but only 32\% on DocRED.
204	Moreover, intervention is unreliable at the per-relation level: on SciERC, \textsc{Evaluate-for} violation rate \emph{increases} from 24.1\% to 29.9\% with schema-informed prompting, due to prior-constraint conflict where the model's learned type associations interfere with prompt-level constraint signals.
205	Three relation types retain $>$10\% violation rates even with explicit constraint descriptions.
206	For applications requiring per-instance compliance (biomedical, legal, regulatory IE), statistical reduction through prompting is insufficient.
207	
208	% ===========================================================================
209	% 4. ONTOCODEC FRAMEWORK
210	% ===========================================================================
211	\section{OntoCoDec Framework}
212	\label{sec:method}
213	
214	\textsc{OntoCoDec} takes an IE ontology $\mathcal{O}$ and a tokenizer $\mathcal{T}$ as input and produces a constrained decoding configuration.
215	The compilation is fully automatic---no manual rule writing is required.
216	
217	\subsection{Grammar Layer}
218	
219	The grammar layer compiles $\mathcal{O}$ into a context-free grammar $G$ that enforces:
220	\begin{itemize}[leftmargin=*,nosep]
221	\item Valid JSON structure for the extraction output format (entity lists, relation triples).
222	\item Relation names restricted to $\mathcal{R}$: the grammar's relation-name production enumerates exactly the valid relation strings.
223	\item Entity types restricted to $\mathcal{E}$: the grammar's entity-type production enumerates exactly the valid type strings.
224	\end{itemize}
225	
226	$G$ is compiled into an XGrammar pushdown automaton, producing per-token masks $M^{gram}_t$ that zero out logits for tokens leading to grammatically invalid continuations.
227	The compiled automaton's adaptive token mask caching makes per-token overhead approximately constant regardless of grammar size.
228	
229	\subsection{Semantic Layer}
230	
231	The semantic layer implements a \texttt{TypeConstraintProcessor} that maintains a stateful entity registry $\mathcal{A}$ during generation:
232	
233	\begin{enumerate}[leftmargin=*,nosep]
234	\item As the model generates entities in the entity list section, $\mathcal{A}$ records each entity's assigned type: $\mathcal{A}[e] = t$.
235	\item When the model begins generating a relation triple, the processor identifies the current relation name $r$ (already guaranteed to be in $\mathcal{R}$ by the grammar layer).
236	\item For subject/object entity type positions, the processor computes a semantic mask $M^{sem}_t$ that zeros out logits for entity types $t \notin \sigma_d(r)$ (subject) or $t \notin \sigma_r(r)$ (object).
237	\end{enumerate}
238	
239	\subsection{Layer Composition}
240	
241	The two layers compose via bitwise AND of token masks:
242	\begin{equation}
243	M_t = M^{gram}_t \wedge M^{sem}_t
244	\end{equation}
245	
246	This composition has an \emph{enabling dependency}: grammar ensures structural validity (valid relation names in $\mathcal{R}$), which enables semantic constraints to look up and enforce domain/range rules for the identified relation type.
247	Without grammar ensuring valid relation names, the semantic layer encounters out-of-vocabulary relations and cannot enforce constraints.
248	
249	When $M^{sem}_t \cap M^{gram}_t = \emptyset$ (the semantic layer would mask all grammar-valid tokens), the system falls back to grammar-only constraints, maintaining structural validity as a guaranteed floor.
250	This occurred in 1/998 DocRED documents (0.1\%) and 0/551 SciERC sentences.
251	
252	\subsection{Decoding Strategies}
253	
254	We evaluate two decoding strategies:
255	\begin{itemize}[leftmargin=*,nosep]
256	\item \textbf{S1 (single-pass)}: Both grammar and semantic layers applied throughout a single generation pass.
257	\item \textbf{S2 (two-pass)}: Pass 1 extracts entities with grammar-only constraints; Pass 2 generates relation triples using an input-dependent grammar compiled from Pass 1 entities, combined with semantic constraints.
258	\end{itemize}
259	
260	S2 is an architectural variant demonstrating framework flexibility.
261	As shown in \S\ref{sec:experiments}, S1 is the recommended default: it is simpler, faster, and performs comparably or better across all metrics.
262	
263	% ===========================================================================
264	% 5. EXPERIMENTS
265	% ===========================================================================
266	\section{Experiments}
267	\label{sec:experiments}
268	
269	\subsection{Setup}
270	
271	\paragraph{Model.} Qwen3-8B with greedy decoding, evaluated on a single NVIDIA RTX PRO 6000 GPU.
272	We evaluate in a zero-shot setting to demonstrate constraint enforcement without task-specific training.
273	F1 is reported to verify that constraints do not degrade extraction quality, not as a claim of state-of-the-art performance.
274	
275	\paragraph{Configurations.} We compare four constraint configurations: \textbf{unconstrained} (no constraint layers), \textbf{grammar\_only} (grammar layer only), \textbf{semantic\_only} (semantic layer only, no grammar), and \textbf{full\_s1} (both layers, single-pass).
276	On SciERC, we additionally report \textbf{full\_s2} (two-pass).
277	
278	\subsection{SciERC Results}
279	
280	\begin{table}[t]
281	\centering
282	\small
283	\begin{tabular}{lccccc}
284	\toprule
285	\textbf{Config} & \textbf{DR} & \textbf{RV} & \textbf{ET} & \textbf{CF} & \textbf{R-F1} \\
286	\midrule
287	unconstrained & 15.4\% & 1.4\% & 0.4\% & 0.1\% & 8.23\% \\
288	grammar\_only & 14.8\% & 0\% & 0\% & 0.1\% & 8.23\% \\
289	semantic\_only & 11.7\% & 1.5\% & 0.4\% & --- & 8.12\% \\
290	full\_s1 & \textbf{0.93\%} & \textbf{0\%} & \textbf{0\%} & 9.9\% & 8.36\% \\
291	full\_s2 & 0.97\% & 0\% & 0\% & 8.0\% & 8.03\% \\
292	\bottomrule
293	\end{tabular}
294	\caption{SciERC constraint configuration comparison (551 sentences, Qwen3-8B). Full S1 achieves 94\% DR reduction (15.4\%$\to$0.93\%) with F1-neutral performance (+0.13pp, not significant). Grammar alone eliminates ET and RV violations entirely.}
295	\label{tab:scierc-results}
296	\end{table}
297	
298	Table~\ref{tab:scierc-results} presents the primary results.
299	The grammar layer alone eliminates entity-type (ET) and relation-vocabulary (RV) violations entirely---from 0.4\% and 1.4\% to 0\%---while leaving DR unchanged (15.4\%$\to$14.8\%).
300	This perfect elimination of ET and RV violations generalizes across both datasets (see \S\ref{sec:docred}) and represents a guaranteed structural compliance floor.
301	
302	The full S1 system reduces DR from 15.4\% to 0.93\%---a 94\% reduction---while maintaining F1-neutral extraction quality (R-F1 8.36\% vs 8.23\% unconstrained, $\Delta{=}$+0.13pp, not statistically significant on $\sim$1700 triples).
303	
304	S2 achieves comparable DR (0.97\%) and slightly lower CF (8.0\% vs 9.9\%) but at 153\% latency overhead versus 62\% for S1, with marginally lower F1 (8.03\%).
305	S2 does not solve CF and offers no meaningful advantage over S1; we include it as an architectural ablation.
306	
307	\subsection{DocRED Results: Complex Ontology Stress Test}
308	\label{sec:docred}
309	
310	\begin{table}[t]
311	\centering
312	\small
313	\begin{tabular}{lcccccc}
314	\toprule
315	\textbf{Config} & \textbf{DR} & \textbf{RV} & \textbf{ET} & \textbf{CF} & \textbf{R-F1} & \textbf{Triples} \\
316	\midrule
317	uncons. & 18.7\% & 28.9\% & 7.5\% & 0.1\% & 8.24\% & 16550 \\
318	gram. & 26.2\% & 0.03\% & 0\% & 0.1\% & 8.24\% & 17341 \\
319	sem. & 13.4\% & 28.5\% & 7.2\% & 3.0\% & 8.12\% & 16600 \\
320	full\_s1 & 10.2\% & 0.03\% & 0\% & 2.6\% & 8.17\% & 17372 \\
321	\bottomrule
322	\end{tabular}
323	\caption{DocRED Phase 2 results (962 documents, Qwen3-8B). Grammar perfectly eliminates ET (7.5\%$\to$0\%) and near-eliminates RV (28.9\%$\to$0.03\%). Full S1 reduces DR by 46\% (18.7\%$\to$10.2\%), a substantial but attenuated effect compared to SciERC.}
324	\label{tab:docred-results}
325	\end{table}
326	
327	DocRED serves as a stress test for constraint effectiveness on a complex ontology.
328	Table~\ref{tab:docred-results} shows that the grammar layer again achieves near-perfect ET and RV elimination (ET: 7.5\%$\to$0\%, RV: 28.9\%$\to$0.03\%), confirming that this result generalizes regardless of ontology complexity.
329	This is particularly significant on DocRED, where RV violations are 28.9\% of triples in the unconstrained baseline---the grammar layer alone eliminates a major class of structural errors.
330	
331	The full S1 system reduces DR by 46\% (18.7\%$\to$10.2\%), a meaningful but attenuated effect compared to SciERC's 94\%.
332	This attenuation reflects DocRED's loose ontology: many relations accept most type pairs, limiting the scope for semantic constraint enforcement.
333	
334	\paragraph{Interpreting the grammar\_only DR increase.}
335	The apparent DR increase under grammar\_only (18.7\%$\to$26.2\%) is a denominator effect: grammar eliminates 28.9\% RV violations (triples with invalid relation names that could not be checked for DR), increasing the pool of DR-checkable triples.
336	The ``checkable-triple DR'' is $\sim$26\% under both unconstrained and grammar\_only configurations; the semantic layer then reduces this to 10.2\% (a 61\% reduction on checkable triples).
337	
338	\subsection{Enabling Dependency: Grammar Enables Semantics}
339	
340	\begin{table}[t]
341	\centering
342	\small
343	\begin{tabular}{lcccccc}
344	\toprule
345	\textbf{Dataset} & $|\mathcal{R}|$ & \textbf{Sem. DR} & \textbf{Full DR} & \textbf{Sem. $\downarrow$} & \textbf{Full $\downarrow$} & \textbf{Ratio} \\
346	\midrule
347	SciERC & 7 & 11.7\% & 0.93\% & 24\% & 94\% & 3.9$\times$ \\
348	DocRED & 96 & 13.4\% & 10.2\% & 28\% & 46\% & 1.6$\times$ \\
349	\bottomrule
350	\end{tabular}
351	\caption{Enabling dependency analysis. The enabling ratio (full reduction / semantic-only reduction) measures how much grammar amplifies semantic effectiveness. The effect is strong on SciERC (3.9$\times$) and attenuated on DocRED (1.6$\times$).}
352	\label{tab:enabling}
353	\end{table}
354	
355	Table~\ref{tab:enabling} quantifies the enabling dependency between layers.
356	On SciERC, the semantic layer alone reduces DR by 24\% (15.4\%$\to$11.7\%), but when enabled by grammar, the full system achieves 94\% reduction---a 3.9$\times$ amplification.
357	The mechanism is clear: grammar ensures valid relation names, allowing the semantic layer to look up and enforce domain/range rules for every triple.
358	
359	On DocRED, the enabling ratio is 1.6$\times$ (28\%$\to$46\%), confirming the dependency's existence but showing substantial attenuation.
360	The semantic layer's absolute reduction on DocRED (28\%) is actually \emph{slightly higher} than on SciERC (24\%), indicating that the semantic layer itself is not weaker on large ontologies.
361	Rather, the full system's ceiling is lower because loose constraints limit the scope for enforcement.
362	The enabling dependency is thus demonstrated on SciERC and partially confirmed on DocRED.
363	
364	\subsection{CF Violation Analysis}
365	
366	\begin{table}[t]
367	\centering
368	\small
369	\begin{tabular}{lcc}
370	\toprule
371	\textbf{Metric} & \textbf{SciERC} & \textbf{DocRED} \\
372	\midrule
373	CF rate (per-entity) & 9.9\% & 2.6\% \\
374	Total CF violations & 245 & 519 \\
375	EVR fraction & 92\% & 82\% \\
376	WR fraction & 8\% & 18\% \\
377	Ambiguity-driven & $\sim$85\% & $\sim$72\% \\
378	Systematic error & $\sim$15\% & $\sim$18\% \\
379	Top conflict pair & Generic$\leftrightarrow$OtherSciTerm & MISC$\leftrightarrow$ORG \\
380	\bottomrule
381	\end{tabular}
382	\caption{Cross-field consistency violation composition under full\_s1. CF violations are 100\% attributable to the semantic layer (grammar\_only CF $\approx$ 0.1\%). The majority are entity-vs-relation type drift (EVR) driven by type system ambiguity.}
383	\label{tab:cf-analysis}
384	\end{table}
385	
386	The full constraint system introduces elevated CF rates (Table~\ref{tab:cf-analysis}): 9.9\% on SciERC and 2.6\% on DocRED.
387	CF violations are 100\% attributable to the semantic layer---grammar\_only CF matches the unconstrained baseline ($\sim$0.1\%).
388	This is an inherent side effect of per-relation independent type enforcement: the semantic layer enforces type constraints for each relation triple independently, which can assign different types to the same entity across different relation contexts.
389	
390	The majority of CF violations (85\% SciERC, 72\% DocRED) are ambiguity-driven, reflecting genuine type system boundary cases.
391	On SciERC, Generic$\leftrightarrow$OtherScientificTerm accounts for 60 conflicts---these terms genuinely admit dual typing in different academic contexts.
392	On DocRED, MISC$\leftrightarrow$ORG (82 conflicts) and LOC$\leftrightarrow$ORG (68 conflicts) reflect the well-known geopolitical entity typing ambiguity.
393	
394	\begin{table}[t]
395	\centering
396	\small
397	\begin{tabular}{lcccc}
398	\toprule
399	\textbf{Type Pair} & \textbf{Count} & \textbf{\% of CF} & \textbf{Category} & \textbf{Defensible} \\
400	\midrule
401	MISC$\leftrightarrow$ORG & 82 & 15.8\% & ambiguity & yes \\
402	LOC$\leftrightarrow$ORG & 68 & 13.1\% & ambiguity & yes \\
403	PER$\leftrightarrow$MISC & 42 & 8.1\% & partial & partially \\
404	NUM$\leftrightarrow$TIME & 35 & 6.7\% & systematic & no \\
405	PER$\leftrightarrow$LOC & 25 & 4.8\% & systematic & no \\
406	ORG$\leftrightarrow$TIME & 18 & 3.5\% & systematic & no \\
407	\bottomrule
408	\end{tabular}
409	\caption{Top CF conflict patterns on DocRED with error classification. Approximately 18\% of CF violations are systematic errors without defensible ambiguity.}
410	\label{tab:docred-cf-patterns}
411	\end{table}
412	
413	However, approximately 18\% of DocRED CF violations are systematic errors without defensible ambiguity (Table~\ref{tab:docred-cf-patterns}).
414	NUM$\leftrightarrow$TIME conflicts (35 cases: years like ``1990'' typed as NUM in entity lists but requiring TIME in relation contexts) and PER$\leftrightarrow$LOC conflicts (25 cases: toponymic surnames) represent genuine method limitations addressed in \S\ref{sec:discussion}.
415	
416	\subsection{Latency Analysis}
417	
418	\begin{table}[t]
419	\centering
420	\small
421	\begin{tabular}{lcccl}
422	\toprule
423	\textbf{Config} & \textbf{SciERC} & \textbf{DocRED} & \textbf{Overhead} & \textbf{Value} \\
424	\midrule
425	uncons. & 850ms & 3200ms & --- & baseline \\
426	gram. & 1050ms & 3950ms & $\sim$23\% & ET/RV$\to$0\% \\
427	full\_s1 & 1380ms & 5250ms & $\sim$62\% & 94\%/46\% DR$\downarrow$ \\
428	full\_s2 & 2150ms & --- & $\sim$153\% & $\approx$S1, 2.5$\times$ cost \\
429	\bottomrule
430	\end{tabular}
431	\caption{Inference latency per sample/document (Qwen3-8B, RTX PRO 6000). Grammar-only provides ET/RV elimination at 23\% overhead; full S1 adds semantic enforcement at 62\% overhead.}
432	\label{tab:latency}
433	\end{table}
434	
435	Table~\ref{tab:latency} reports inference latency.
436	The grammar layer adds $\sim$23\% overhead (XGrammar's compiled automaton with adaptive caching makes cost approximately constant regardless of grammar size---SciERC and DocRED show nearly identical overhead percentages).
437	The full S1 system adds $\sim$62\% overhead from the semantic layer's entity registry lookup and dynamic logit masking.
438	For latency-sensitive deployments, grammar-only provides ET/RV$\to$0\% at 23\% overhead, serving as a lightweight compliance floor.
439	Throughput decreases from 82 to 52 tokens/second ($-$37\%), a modest cost that compares favorably to post-hoc filtering's effective throughput loss from rejecting 14--15\% of generated outputs.
440	
441	% ===========================================================================
442	% 6. RELATED WORK
443	% ===========================================================================
444	\section{Related Work}
445	
446	\paragraph{Constrained Decoding for Structured Generation.}
447	Grammar-constrained decoding has been applied to JSON generation \cite{willard2023efficient}, code generation \cite{scholak2021picard}, and SQL synthesis.
448	XGrammar \cite{dong2024xgrammar} provides efficient CFG-based token masking.
449	Recent work extends constrained decoding to semantic constraints beyond CFG expressiveness: GCD \cite{geng2024grammar} integrates grammar and semantic constraints for code generation.
450	Our work applies this paradigm to IE ontology constraints, introducing a stateful entity registry for cross-field constraint enforcement.
451	
452	\paragraph{LLM-based Information Extraction.}
453	LLMs have been applied to IE in zero-shot \cite{wei2023zeroshot}, few-shot \cite{li2023codeie}, and instruction-tuned settings \cite{wang2023instructuie}.
454	Most work focuses on extraction quality (F1) rather than structural validity.
455	GoLLIE \cite{sainz2024gollie} uses code-style schemas to guide extraction but does not enforce type constraints at decoding time.
456	Our work is complementary: \textsc{OntoCoDec} can wrap any LLM-based IE system to enforce ontology compliance.
457	
458	\paragraph{Ontology-Based Validation.}
459	Post-hoc validation approaches use SHACL constraints or description logic reasoners to verify extracted knowledge graphs.
460	These approaches validate after generation but cannot redirect probability mass to valid alternatives during decoding.
461	\textsc{OntoCoDec} operates during generation, avoiding wasted compute on invalid outputs.
462	
463	\paragraph{Structured Output Quality.}
464	CRANE \cite{zheng2024openchat} and the ``Structure Snowballing'' phenomenon \cite{wu2024structure} show that overly aggressive structural constraints can degrade generation quality.
465	\textsc{OntoCoDec}'s semantic constraints are narrow---only type tokens are masked, free text spans are unconstrained---and our experiments confirm F1-neutral performance.
466	
467	% ===========================================================================
468	% 7. DISCUSSION AND LIMITATIONS
469	% ===========================================================================
470	\section{Discussion and Limitations}
471	\label{sec:discussion}
472	
473	\paragraph{CF as a Systematic Side Effect.}
474	Cross-field consistency violations are the primary limitation of per-relation independent type enforcement.
475	While the majority of CF violations reflect genuine type system ambiguity, $\sim$18\% on DocRED are systematic errors (NUM$\leftrightarrow$TIME, PER$\leftrightarrow$LOC) that represent real method deficiencies.
476	We distinguish violation severity: DR violations produce structurally invalid triples that downstream systems cannot consume (hard constraint); CF violations produce individually type-valid triples with cross-triple inconsistency (soft preference).
477	A natural extension is a global entity-type consensus pass---disambiguating entity types before relation-specific enforcement---which we leave to future work.
478	
479	\paragraph{Constraint Effectiveness Scaling with Ontology Complexity.}
480	The contrast between SciERC (94\% DR reduction) and DocRED (46\%) raises a fundamental open question: how does constraint effectiveness scale with ontology complexity?
481	Our tightness-DR correlation analysis (\S\ref{sec:landscape}) provides a partial answer---tighter constraints yield greater reduction---but explains only 14\% of variance on DocRED.
482	Model prior alignment (kinship relations with strong PER$\to$PER priors) and entity polysemy (P31 instance\_of) are additional factors not captured by tightness alone.
483	Understanding this scaling relationship is essential for predicting constraint effectiveness on new ontologies and for developing tightness-adjusted constraint prioritization strategies.
484	
485	\paragraph{Single Model Limitation.}
486	All experiments use Qwen3-8B.
487	The constraint compilation pipeline is model-agnostic by design---only the tokenizer-to-grammar mapping is model-specific.
488	Cross-model validation on Llama-3.1-8B and Mistral-7B is planned; preliminary work (tokenizer adaptation code) is complete but full evaluation was not completed within the experimental timeline.
489	
490	\paragraph{DocRED's Honest Degradation.}
491	DocRED's attenuated results are not a failure of the method but an honest characterization of constraint enforcement on loose ontologies.
492	When most type pairs are valid for a given relation, there is simply less room for semantic constraints to operate.
493	The grammar layer's perfect generalization (ET/RV$\to$0\% on DocRED, eliminating 28.9\% RV and 7.5\% ET violations) demonstrates that structural compliance is achievable regardless of ontology complexity; semantic compliance is ontology-dependent.
494	
495	\paragraph{Zero-Shot Setting.}
496	We evaluate exclusively in a zero-shot setting.
497	Constrained decoding is orthogonal to model capability---it can be applied on top of fine-tuned or few-shot models.
498	Whether constraint enforcement provides diminishing returns as base model quality improves (i.e., better models make fewer violations) is an empirical question we do not address.
499	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d68a512-9201-48ae-ac2f-21a772603ee7",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "bf9855e3-f2dc-44ee-9061-ad57365ae2c0",
  "sourceToolAssistantUUID": "3d68a512-9201-48ae-ac2f-21a772603ee7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T11:00:01.231Z_

<details open><summary>🔧 Tool call — Read · `toolu_019tcxUxKkF2dtkMp9VSeY33`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/median/paper.tex",
  "offset": 499,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf9855e3-f2dc-44ee-9061-ad57365ae2c0",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2Lxfo7USqP5RmRXab5k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40fd3d32-b67e-4792-ac10-c1cdd03819ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtSKZ5DdneQUShUQjm2Kp1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13456,
      "cache_read_input_tokens": 37298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13456,
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

_source line 31 · 2026-05-14T11:00:01.237Z_

<details><summary>↩ Tool result · `toolu_019tcxUxKkF2dtkMp9VSeY33`</summary>

```text
499	
500	% ===========================================================================
501	% 8. CONCLUSION
502	% ===========================================================================
503	\section{Conclusion}
504	
505	We presented \textsc{OntoCoDec}, a framework for automatically compiling IE ontology schemas into composable constrained decoding layers.
506	Our violation landscape study establishes that LLM-based IE systems violate ontology type constraints at non-trivial rates concentrated on relation types with tight type signatures.
507	The grammar layer eliminates entity-type and relation-vocabulary violations entirely on both SciERC and DocRED, providing a universal structural compliance floor.
508	The full grammar+semantic system reduces domain/range violations by 94\% on SciERC at zero F1 cost, with graceful degradation to 46\% reduction on DocRED's complex 96-relation ontology.
509	Constraint tightness significantly predicts residual violation rate, establishing ontology structure as a primary determinant of enforcement effectiveness.
510	The framework introduces elevated cross-field consistency violations as a systematic side effect of independent per-relation enforcement, motivating future work on global entity-type consensus mechanisms.
511	
512	\bibliographystyle{plainnat}
513	\bibliography{references}
514	
515	\end{document}
516	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40fd3d32-b67e-4792-ac10-c1cdd03819ed",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "1ce94e58-e67f-4497-bf27-2bb2b1d7ce81",
  "sourceToolAssistantUUID": "40fd3d32-b67e-4792-ac10-c1cdd03819ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T11:00:01.751Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XdNZF2LPAJYHjCkHxQvzL7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/paper.tex",
  "offset": 499,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ce94e58-e67f-4497-bf27-2bb2b1d7ce81",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2Lxfo7USqP5RmRXab5k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2eed350-e470-46da-bb38-7221db3af8f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtSKZ5DdneQUShUQjm2Kp1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13456,
      "cache_read_input_tokens": 37298,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13456
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 37298,
          "cache_creation_input_tokens": 13456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13456,
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

_source line 33 · 2026-05-14T11:00:01.758Z_

<details><summary>↩ Tool result · `toolu_01XdNZF2LPAJYHjCkHxQvzL7`</summary>

```text
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
  "parentUuid": "b2eed350-e470-46da-bb38-7221db3af8f6",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "1efa99a9-dcc5-40af-b54a-77b7a191a1a2",
  "sourceToolAssistantUUID": "b2eed350-e470-46da-bb38-7221db3af8f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-14T11:00:07.191Z_

Now let me check the individual paper sections that have been drafted separately for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1efa99a9-dcc5-40af-b54a-77b7a191a1a2",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LyAG8Ts1XhmnPjg15t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07777b4c-9007-4269-a5e5-80a9f6522cfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJEEJzE4YYYAcEH6utTad7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 50754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1390,
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

_source line 35 · 2026-05-14T11:00:09.628Z_

<details open><summary>🔧 Tool call — Read · `toolu_017mQXJ5zdaZUKtWcNvgqGF2`</summary>

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
  "parentUuid": "07777b4c-9007-4269-a5e5-80a9f6522cfb",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LyAG8Ts1XhmnPjg15t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79fb0959-107c-4b4f-af93-dfc692e89546",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJEEJzE4YYYAcEH6utTad7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 50754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1390,
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

_source line 36 · 2026-05-14T11:00:09.635Z_

<details><summary>↩ Tool result · `toolu_017mQXJ5zdaZUKtWcNvgqGF2`</summary>

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
  "parentUuid": "79fb0959-107c-4b4f-af93-dfc692e89546",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "bdd12ad8-19fd-4bf1-94af-f8a06238eef2",
  "sourceToolAssistantUUID": "79fb0959-107c-4b4f-af93-dfc692e89546",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T11:00:10.127Z_

<details open><summary>🔧 Tool call — Read · `toolu_0126h6dSMc4BojGTCEJzdgPo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdd12ad8-19fd-4bf1-94af-f8a06238eef2",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LyAG8Ts1XhmnPjg15t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83f061ff-bd71-4556-9294-3e09f863fcf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJEEJzE4YYYAcEH6utTad7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 50754,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1390
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 50754,
          "cache_creation_input_tokens": 1390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1390,
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

_source line 38 · 2026-05-14T11:00:10.133Z_

<details><summary>↩ Tool result · `toolu_0126h6dSMc4BojGTCEJzdgPo`</summary>

```text
1	% =============================================================
2	% Paper Tables Draft — Schema-Semantic Constrained IE
3	% Generated from experiment registry, 2026-05-14
4	% Model: Qwen3-8B (zero-shot), all percentages to 1 d.p.
5	% =============================================================
6	
7	% ------------------------------------------------------------
8	% Table 1: SciERC 5-way Ablation
9	% ------------------------------------------------------------
10	\begin{table}[t]
11	\centering
12	\caption{Ablation study on SciERC test set (551 samples, Qwen3-8B zero-shot).
13	DR = Domain/Range violation rate, RV = Relation Vocabulary violation rate,
14	ET = Entity Type violation rate, CF = Cross-Field consistency violation rate.
15	$\downarrow$: lower is better; $\uparrow$: higher is better.
16	$\Delta$DR shows the absolute change (pp) relative to the unconstrained baseline.}
17	\label{tab:scierc-ablation}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{l cccc cc c}
20	\toprule
21	Mode & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ & R-F1$\uparrow$ & E-F1$\uparrow$ & $\Delta$DR (pp) \\
22	\midrule
23	Unconstrained      & 15.4 & 1.4          & 0.4          & \textbf{0.1} & 8.2          & 31.0          & ---                    \\
24	Grammar-only       & 14.8 & \textbf{0.0} & \textbf{0.0} & \textbf{0.1} & 8.2          & 31.0          & $-$0.5                 \\
25	Semantic-only      & 11.7 & 1.5          & 0.4          & 2.7          & 8.2          & 31.0          & $-$3.7                 \\
26	Full (S1)          & \textbf{0.9} & \textbf{0.0} & \textbf{0.0} & 9.9  & \textbf{8.4} & 31.0          & \textbf{$-$14.4}       \\
27	Full (S2)          & 1.0  & \textbf{0.0} & \textbf{0.0} & 8.0          & 8.0          & \textbf{31.9} & $-$14.4                \\
28	\bottomrule
29	\end{tabular}%
30	}
31	\vspace{2pt}
32	{\footnotesize
33	\textit{Exp IDs:}
34	\texttt{phase2\_scierc\_unconstrained},
35	\texttt{phase2\_scierc\_grammar\_only},
36	\texttt{phase2\_scierc\_semantic\_only},
37	\texttt{phase2\_scierc\_full\_s1},
38	\texttt{phase2\_scierc\_full\_s2}.
39	}
40	\end{table}
41	
42	
43	% ------------------------------------------------------------
44	% Table 2: Per-Relation DR Violation Analysis (SciERC)
45	% ------------------------------------------------------------
46	\begin{table}[t]
47	\centering
48	\caption{Per-relation Domain/Range violation rates on SciERC:
49	Unconstrained baseline vs.\ Full (S1) constrained decoding.
50	$n$ = predicted triples of that relation type (unconstrained).
51	$\Delta$ = absolute change in violation rate (pp).}
52	\label{tab:scierc-per-relation-dr}
53	\begin{tabular}{l r rr r}
54	\toprule
55	Relation & $n$ & Uncon.\ (\%) & S1 (\%) & $\Delta$ (pp) \\
56	\midrule
57	Compare      &  66 & 42.4 &  2.8 & $-$39.6 \\
58	Feature-of   & 486 & 33.5 &  1.2 & $-$32.3 \\
59	Part-of      &  72 & 25.0 & \textbf{0.0} & $-$25.0 \\
60	Evaluate-for & 133 & 24.1 &  5.8 & $-$18.3 \\
61	Hyponym-of   & 124 & 14.5 & \textbf{0.0} & $-$14.5 \\
62	Used-for     & 787 &  0.8 & \textbf{0.0} & $-$0.8  \\
63	Conjunction  &  32 &  0.0 & \textbf{0.0} &    0.0  \\
64	\midrule
65	\textit{Overall} & \textit{1724} & \textit{15.4} & \textit{0.9} & \textit{$-$14.4} \\
66	\bottomrule
67	\end{tabular}
68	\vspace{2pt}
69	{\footnotesize
70	\textit{Exp IDs:}
71	\texttt{phase2\_scierc\_unconstrained} (Uncon.),
72	\texttt{phase2\_scierc\_full\_s1} (S1).
73	}
74	\end{table}
75	
76	
77	% ------------------------------------------------------------
78	% Table 3: DocRED Phase 0 — Prompt-level Intervention
79	% ------------------------------------------------------------
80	\begin{table}[t]
81	\centering
82	\caption{Prompt-level intervention on DocRED dev set (998 documents, 96 relation types, Qwen3-8B zero-shot).
83	Comparing minimal prompt vs.\ schema-informed prompt that explicitly lists valid relation types
84	and domain/range constraints.}
85	\label{tab:docred-phase0}
86	\begin{tabular}{l cccc}
87	\toprule
88	Mode & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & JSON Parse$\uparrow$ \\
89	\midrule
90	Minimal          & 18.7          & 28.9          & 7.5          & \textbf{96.4} \\
91	Schema-informed  & \textbf{12.8} & \textbf{18.4} & \textbf{0.6} & 94.5          \\
92	\midrule
93	$\Delta$         & $-$5.9        & $-$10.5       & $-$6.9       & $-$1.9        \\
94	\bottomrule
95	\end{tabular}
96	\vspace{2pt}
97	{\footnotesize
98	\textit{Exp IDs:}
99	\texttt{mvp\_phase0\_violation\_rate\_docred} (Minimal),
100	\texttt{mvp\_phase0\_docred\_schema} (Schema-informed).
101	}
102	\end{table}
103	
104	
105	% ------------------------------------------------------------
106	% Table 4: Cross-dataset Violation Comparison
107	% ------------------------------------------------------------
108	\begin{table}[t]
109	\centering
110	\caption{Cross-dataset comparison of ontology violation rates.
111	Baseline = unconstrained Qwen3-8B zero-shot; S1 = Grammar + Semantic constrained decoding.
112	DocRED S1 results are pending (experiment in progress).}
113	\label{tab:cross-dataset}
114	\begin{tabular}{l c ccc cc}
115	\toprule
116	Dataset & \#Rels & DR\textsubscript{base} & RV\textsubscript{base} & ET\textsubscript{base} & DR\textsubscript{S1} & $\Delta$DR (pp) \\
117	\midrule
118	SciERC & 7  & 15.4 & 1.4  & 0.4 & 0.9          & $-$14.4 \\
119	DocRED & 96 & 18.7 & 28.9 & 7.5 & \textit{TBD} & \textit{TBD} \\
120	\bottomrule
121	\end{tabular}
122	\vspace{2pt}
123	{\footnotesize
124	\textit{Exp IDs:}
125	SciERC base = \texttt{phase2\_scierc\_unconstrained},
126	SciERC S1 = \texttt{phase2\_scierc\_full\_s1},
127	DocRED base = \texttt{mvp\_phase0\_violation\_rate\_docred},
128	DocRED S1 = \texttt{phase2\_docred\_full\_s1} (RUNNING).
129	}
130	\end{table}
131	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83f061ff-bd71-4556-9294-3e09f863fcf6",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "6eb5f381-9026-4e1c-a5c3-00ded99eeb2b",
  "sourceToolAssistantUUID": "83f061ff-bd71-4556-9294-3e09f863fcf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-14T11:00:13.845Z_

Now let me check the reference/bib file and any additional experimental details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6eb5f381-9026-4e1c-a5c3-00ded99eeb2b",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LynDbkpPzkqjQspYYp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "def2e9c2-1265-4a0d-9231-5083292c1cc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSYMaiKcm5Qr7vwpPNjZK1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6960,
      "cache_read_input_tokens": 52144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6960,
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

_source line 40 · 2026-05-14T11:00:16.361Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FDQmzLzY2zr4mm5Vvhcvvz`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "def2e9c2-1265-4a0d-9231-5083292c1cc8",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LynDbkpPzkqjQspYYp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d70318c-c8c4-4eaf-ac21-e2cf2c555723",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSYMaiKcm5Qr7vwpPNjZK1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6960,
      "cache_read_input_tokens": 52144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6960,
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

_source line 41 · 2026-05-14T11:00:16.382Z_

<details><summary>↩ Tool result · `toolu_01FDQmzLzY2zr4mm5Vvhcvvz`</summary>

```text
artifacts/_project/paper/relwork_new_entries.bib
artifacts/dream_reports/dream_20260514T094226/median/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d70318c-c8c4-4eaf-ac21-e2cf2c555723",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "cf9431ff-52b1-4723-9979-a48ae0fc6fc5",
  "sourceToolAssistantUUID": "7d70318c-c8c4-4eaf-ac21-e2cf2c555723",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T11:00:16.945Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019Q4tyDm7qYuvFVaF3jVZTN`</summary>

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
  "parentUuid": "cf9431ff-52b1-4723-9979-a48ae0fc6fc5",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LynDbkpPzkqjQspYYp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dea6c2dd-e0f9-40ed-ab03-cd260200073c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSYMaiKcm5Qr7vwpPNjZK1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6960,
      "cache_read_input_tokens": 52144,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6960
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 52144,
          "cache_creation_input_tokens": 6960,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6960,
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

_source line 43 · 2026-05-14T11:00:16.959Z_

<details><summary>↩ Tool result · `toolu_019Q4tyDm7qYuvFVaF3jVZTN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/memory.md\", \"content\": \"# Memory — schema_semantic_constrained_ie\\n\\n## 文献调研 (2026-05-13)\\n\\n### 核心结论: OntoCoDec 的 novelty 成立\\n**没有人做过 \\\"compile IE ontology domain/range → decoding-time logits masking\\\" 的完整 pipeline。**\\n\\nGap 结构：\\n- Syntactic constrained decoding for IE: well-explored (GCD, XGrammar, Outlines)\\n- Vocabulary-level: exists (GENRE, iNERD, AdaKGC)\\n- **Semantic (domain/range) decoding for IE: OPEN GAP** ← OntoCoDec\\n- Semantic type checking at decode time: only for code gen (MGD NeurIPS'23, PLDI'25)\\n- Ontology compliance for IE: only post-processing (ODKE+ Apple'25, OntoLogX'25)\\n\\n最近竞争者：PLDI'25 Type-Constrained Code Gen（同机制但领域是代码生成，必须引用并区分）\\n\\n风险：CRANE (ICML'25) 严格约束可能降低推理质量；Grammar-Aligned Decoding (NeurIPS'24) naive masking 扭曲分布\\n\\nNovelty 定位：\\\"OntoCoDec 将 type-constrained generation 引入信息抽取，编译 IE ontology axioms 为解码时语义约束，预防而非检测 type violations。\\\"\\n\\n详细报告: `artifacts/literature_map.yaml`, `artifacts/literature_survey_*.md`\\n\\n## 实验发现\\n\\n### SciERC Phase 0 — Minimal (2026-05-13)\\n- **go_nogo_metric = 15.4%** (domain_range_violation_rate), 3× 超过 5% 阈值 → GO\\n- Violation 分布极不均匀: Used-for 0.76% vs Compare 42.4% vs Feature-of 33.5%\\n- Feature-of + Compare 贡献 72% 的 domain/range violations\\n- Relation vocabulary violations 仅 1.4%\\n- 关键 insight: OntoCoDec 的价值在于精确靶向高违规 relation types\\n\\n### SciERC Phase 0 — Schema-informed (2026-05-13)\\n- **domain_range_violation_rate = 5.78%**（vs minimal 15.37%, -62.4%）\\n- 仍高于 5% 阈值 → prompt 级干预不足以替代 decoding-time enforcement\\n- Entity type violations 降到 0%，relation vocabulary 降到 0.30%\\n- Per-relation: Feature-of -22.3pp, Part-of -22.5pp, Compare -14.8pp\\n- ⚠️ Evaluate-for 反而退步 +5.8pp — prompt 复杂度反而干扰\\n- McNemar 四类全显著 p<0.01\\n- **论文 story**: LLM 能理解约束（-62%）但执行不完美（仍>5%），需要 hard constraint\\n\\n### DocRED Phase 0 — Minimal (2026-05-13)\\n- **domain_range_violation_rate = 18.7%** (16,540 triples, 998 docs)\\n- Relation vocabulary violation = 28.9% (4,775 triples) — 远高于 SciERC 1.4%\\n- Entity type violation = 7.5% (vs SciERC 0.4%)\\n- JSON parse rate = 96.4% (36 docs 解析失败)\\n- Top violators: P31 instance_of (60.4%, 322/533), P1001 applies_to_jurisdiction (44.4%)\\n- 约束更紧(avg 5.68 pairs)确实导致更高违规(18.7% vs 15.4%)\\n\\n### SciERC vs DocRED 对比 (2026-05-13)\\n| 指标 | SciERC (7 rels) | DocRED (96 rels) |\\n|------|----------------|-----------------|\\n| D/R violation | 15.4% | 18.7% (+3.3pp) |\\n| Relation vocab | 1.4% | 28.9% (+27.5pp) |\\n| Entity type | 0.4% | 7.5% (+7.1pp) |\\n| Avg valid pairs | 26.1 | 5.68 |\\n两个数据集都远超 5% 阈值 → 强 GO 信号。Vocabulary layer 在复杂 schema 上尤为关键。\\n\\n### SciERC Phase 2 — Grammar-only (2026-05-13)\\n- **Grammar 层约束是\\\"免费\\\"的**：零 F1 代价完全消除 rv (1.4%→0%) 和 et (0.4%→0%) violations\\n- entity_f1 delta = -0.03pp ≈ 0，relation_f1 delta = 0\\n- **论文 claim**: \\\"Structural constraints can be enforced at zero quality cost\\\"\\n- DR violation 基本不变 (15.37%→14.84%, -0.53pp) — 符合预期，grammar 不含 D/R 约束\\n- DR 热点: Compare 40.85%, Feature-of 31.98%, Part-of 23.38% — 这些是 semantic 层的目标\\n- **决策依据**: grammar 层可以 always-on，无需 ablation 它的\\\"代价\\\"。论文只需关注 semantic 层的 F1 trade-off。\\n\\n### SciERC Phase 2 — 全量最终结果 (2026-05-14, _v2 干净数据)\\n\\n| Mode | R-F1 | E-F1 | DR% | RV% | ET% | ΔDR |\\n|------|------|------|-----|-----|-----|-----|\\n| unconstrained | 0.0823 | 0.3101 | 15.37% | 1.39% | 0.4% | — |\\n| grammar_only | 0.0823 | 0.3098 | 14.84% | 0% | 0% | -0.53pp |\\n| semantic_only | 0.0815 | 0.3101 | 11.65% | 1.51% | 0.4% | -3.72pp |\\n| **full_s1** | **0.0836** | **0.3098** | **0.93%** | **0%** | **0%** | **-14.44pp (↓94%)** |\\n\\n**核心发现**:\\n- **full_s1 是论文核心结果**: DR 15.37%→0.93% (消除 94%), F1 反而微升 +0.0013, 零质量代价\\n- **semantic_only 有效但不够**: DR -3.72pp (↓24%), 但 RV/ET 未消除（需 grammar 层配合）\\n- 早期污染数据 (108样本) 显示 semantic_only DR=16.43%（误导），干净数据实际 11.65%\\n- **Ablation story**: grammar 处理结构约束 (RV, ET), semantic 处理类型约束 (DR), 合并达最佳效果\\n\\n**Per-relation DR (full_s1)**: Used-for/Hyponym-of/Part-of/Conjunction = 0%, Feature-of 1.21%, Compare 2.82%, Evaluate-for 5.76% (残留最多)\\n\\n### SciERC Phase 2 — S2 全量结果 (2026-05-14)\\n| Mode | R-F1 | E-F1 | DR% | CF% |\\n|------|------|------|-----|-----|\\n| full_s1 | 0.0836 | 0.3098 | 0.93% | 9.90% |\\n| full_s2 | 0.0803 | 0.3190 | 0.97% | 8.03% |\\nS1 全面略优 (R-F1 +0.33pp, DR 持平)，S2 降级为 ablation。\\n\\n### DocRED Phase 2 — Grammar-only (2026-05-14)\\n- ET: 7.5%→0%, RV: 28.9%→0.03%, DR 26.17%（grammar 不含 D/R 约束，DR 高于 unconstrained 是因为 grammar 强制合法 relation name 后改变了 triple 分布）\\n- Grammar 层在复杂 schema 上同样完美消除 ET/RV\\n\\n### DocRED Phase 2 — Full S1 结果 (2026-05-14) ⚠️ 关键\\n| 指标 | Phase 0 Unconstrained | Grammar Only | Schema Informed | Full S1 |\\n|------|----------------------|-------------|-----------------|---------|\\n| ET | 7.50% | 0% | 0.61% | **0%** |\\n| RV | 28.90% | 0.03% | 18.40% | **0.03%** |\\n| DR | 18.70% | 26.17% | 12.80% | **10.19%** |\\n| CF | 0.08% | — | 0.15% | 2.57% |\\n| Entity F1 | — | — | — | 0.6534 |\\n| Relation F1 | — | — | — | 0.082 |\\n\\n**关键发现**:\\n1. ✅ Grammar 层在 DocRED 完美泛化: ET/RV→0%（与 SciERC 一致）\\n2. ⚠️ **DR 降幅 scaling gap**: SciERC ↓94% (15.37→0.93%) vs DocRED ↓45.5% (18.7→10.19%)\\n3. 残余 DR 集中在特定关系: P190_sister_city 58%, P582_end_time 43.5%, P205_basin_country 37%, P276_location 28.4%\\n4. Top-10 高 DR 关系贡献 27% 的总 violations (478/1771)\\n5. Semantic 层在 grammar 基础上额外贡献: DR 26.17→10.19% (↓61%)\\n6. CF 从 0.08% 升到 2.57%（低于 SciERC 的 9.9%）\\n7. **Framing 影响**: \\\"near-elimination\\\" 对 ET/RV 成立，DR 需改为 \\\"significant reduction\\\"。复杂 schema 下 entity type 边界模糊是 DR 残余的主因\\n\\n### Constraint Tightness ↔ DR Violation Scaling (2026-05-14) ⚠️ 论文核心 insight\\n**根因分析确认：DR 差异由约束紧度驱动，非 semantic 层失效。**\\n\\n| Tightness 区间 | Valid pairs | DocRED 聚合 DR | SciERC 对应 |\\n|---------------|-------------|---------------|------------|\\n| ≥ 0.95 (极紧) | 1-2 pairs | 30.6% | 无此类 relation |\\n| 0.90-0.94 | 3-4 pairs | 19.3% | 无此类 relation |\\n| < 0.70 (宽松) | 11+ pairs | 0.7% | SciERC 全部在此区间 |\\n\\n- DocRED avg tightness = 0.842 vs SciERC = 0.333\\n- DocRED 中位数仅允许 5/36 type pairs，SciERC 中位数 23/36\\n- 高 tightness 下 semantic∩grammar=∅ 概率高 → fallback 到 grammar-only → DR 未被约束\\n- SciERC DR 低是因为约束本身宽松，LLM 几乎不可能违规\\n- **论文定位**：effectiveness scales inversely with constraint tightness，这是 **contribution** 而非 weakness（首个 constraint scaling 实证，无文献可比）\\n- **文献确认**：无任何论文在 DocRED 上报告 constrained decoding violation rate，我们是首个 benchmark\\n\\n### CF Violation 根因分析 (2026-05-14)\\n- **CF = 跨字段一致性违规**：同一 entity mention 在 entity list 和 relation head/tail 中被标注为不同类型\\n- 根因: semantic constraint 按 per-relation 独立强制 type，导致 entity-vs-relation type drift\\n- 主要冲突: Generic ↔ OtherScientificTerm (60 次, 占比最高)\\n- grammar_only CF=0.08% → S1 CF=9.90% → **CF 100% 来自 semantic 层**\\n- **论文 limitation**: per-relation 独立 type enforcement 的固有副作用，需 future work 做跨 relation entity type 一致性约束\\n\\n### CF 指标口径澄清 (2026-05-14)\\n- violation_checker: 合并所有 type 来源 (entity list + relation head/tail)，denominator = total_entities (2474)\\n- analyze_cf: 分 WR (Within-Relations) + EVR (Entity-vs-Relation) 两维度，denominator 不同 (checked_slots=3380)\\n- **分子一致**: S1=245=245, S2=178 vs 179 (差 1 due to analyze_cf entity_type_map overwrite bug)\\n- **论文统一用 violation_checker 口径**: S1=9.90%, S2=8.03%\\n\\n### S2 Pilot 调查 (2026-05-13)\\n- **原报告 relation_f1=0 是误读**：数据来自 10 样本 dryrun 的 violation_report，非 pilot50 评估\\n- pilot50 实际 relation_f1=0.1008 (13 TP / 146 pred / 112 gold)，与 unconstrained 0.0823 持平\\n- S2 架构可行，DR violation=0% 达标，F1 瓶颈在 entity span 质量（zero-shot entity F1≈0.29）\\n- FP 根因: 52.6% head+tail 都不匹配 gold（entity span 提取错误以平方级放大到 relation）\\n\\n## 技术路线决策\\n\\n### Phase 1 Compiler 完成 (2026-05-13)\\n**HF transformers + XGrammar (standalone)**，代码在 `/root/schema_semantic_constrained_ie/compiler/`：\\n- `ontology_compiler.py`: compile_type_constraints() + build_processor()\\n- `type_mask_processor.py`: _build_first_token_map(), _mask_entity_type/head/tail_type(), _detect_position()\\n- 24 单元测试 + 12 e2e 测试全部通过\\n- SGLang 作为后续性能优化路径，vLLM 暂不可用\\n\\n### Phase 2 脚本完成 (2026-05-13)\\n`run_constrained_extraction.py` (652 行) 支持 5 模式：unconstrained/grammar_only/semantic_only/full_s1/full_s2\\n- 所有模式 dry-run 通过 + violation_checker 兼容\\n\\n### DocRED constrained decoding 就绪 (2026-05-14)\\n`run_constrained_extraction.py --dataset docred` 零代码修改即可运行 grammar_only / full_s1 模式。\\n约束文件: `data/docred/ontology_constraints_docred.json` (6 entity types, 96 relations)\\n建议命令加 `--max_new_tokens 4096`（文档级比句子级长得多）\\n\\n### Grammar-Semantic 交互 Bug 修复 (2026-05-14)\\n**根因**: `compiler/type_mask_processor.py` → `_apply_type_mask`。full_s1 模式下 XGrammar 将 grammar-invalid tokens 设为有限负值 (-1e10)，TypeConstraintProcessor 将 semantically-disallowed types 设为 -inf。当 `allowed_types` 与 grammar-valid tokens 无交集时，所有 grammar-valid tokens 变为 -inf，而 grammar-invalid tokens 仍为 -1e10 (> -inf) → argmax 选中 grammar-invalid token → XGrammar assertion failure。\\n**修复**: `_apply_type_mask` 增加 `_GRAMMAR_MASK_THRESHOLD = -1e8` 安全检查：应用 semantic mask 前验证至少一个 semantically-allowed type 有非 grammar-masked logit；若无交集则跳过 semantic masking，交由 grammar 控制。\\n**论文意义**: 此 invariant（semantic mask ⊆ grammar allowed set）是双层约束架构的关键设计约束，应在 Method section 明确描述。在 SciERC 上未触发是因为约束更松 (avg 26.1 valid pairs vs DocRED 5.68)。\\n\\n### Llama-3.1-8B 兼容性验证 (2026-05-14)\\n- 模型已在服务器: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`\\n- 零代码修改：AutoTokenizer/AutoModelForCausalLM 模型无关，chat_template 自动适配\\n- XGrammar + TypeConstraintProcessor first-token 唯一性验证通过（SciERC 6 types + DocRED 6 types）\\n- pad_token=None 已有处理逻辑\\n\\n### First-token masking 验证 (2026-05-13)\\n简单 first-token masking 安全可用，不需要 trie-based 方案。\\nSciERC: Task=6262, Method=3523, Material=13415, Metric=54310, OtherScientificTerm=11409, Generic=19964\\nDocRED: PER=9654, ORG=44927, LOC=12052, TIME=18129, NUM=17488, MISC=44\\n上下文无关性已验证。\\n\\n## 方法论决策\\n\\n### Violation 分类体系 (2026-05-13)\\n4 类独立计数：entity_type / relation_vocabulary / domain_range / cross_field_consistency\\ngo/no-go 阈值 (5%) 基于 domain_range_violation_rate\\n\\n### Fuzzy Matching (2026-05-13)\\nDocRED: token overlap >80% 或 Levenshtein ≤2\\n\\n## 踩坑记录\\n\\n### submit_training_job 必须 bash -c 包裹 (2026-05-13)\\n- tmux session 默认用 `sh` 执行命令，`source` 和 `conda activate` 是 bash built-in\\n- **直接写 `python3 ...` 会 EXIT_CODE=127 (command not found)**\\n- **正确写法**: `bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 ...\\\"`\\n\\n### 孤儿进程清理误杀活跃实验 (2026-05-14)\\n- Worker 执行孤儿进程清理时，白名单未包含所有活跃实验 PID → SIGTERM 杀掉了 mvp_phase0_docred_schema 和 semantic_only/full_s1\\n- **防护措施**: 清理前必须查 registry 所有 RUNNING 实验的 PID 全部加入白名单; Kill 前检查输出文件行数是否已达 expected count; 只 kill 具体的孤儿 PID\\n- **恢复方式**: JSONL 逐行追加，用 --resume 从断点恢复\\n\\n### 重提交实验前必须清理旧 tmux session (2026-05-13)\\n- retry 未 kill 旧 tmux → 两进程同时写同一 JSONL → null bytes 污染\\n- **规则**: 重提交前先 `tmux kill-session -t &lt;exp_id>`\\n\\n### 禁止在 allocate_and_submit 命令内放 tmux kill-session (2026-05-14)\\n- allocate_and_submit 在 tmux session 内执行命令，`tmux kill-session -t <同名session>` 导致 session 自杀\\n- cron 追踪死 session → 5× miss → 误判 DONE(failed)\\n- **正确做法**: 单独派 Worker 先清理旧 session，确认后再 allocate_and_submit\\n\\n### Cron PID 追踪不可靠 (2026-05-14)\\n- cron 系统导致 4 次假失败（grammar_only / semantic_only / full_s1 / full_s2），每次假失败触发 cleanup worker 又误杀合法进程，恶性循环\\n- **决策**: 对长期运行实验改用手动 `wc -l` 检查输出文件行数判断完成，不依赖 PID/tmux 存活\\n- 完成判断标准: 输出文件行数 = 目标样本数\\n\\n## 环境信息\\n\\n### westd-16980 (2026-05-13)\\n- GPU: 2× NVIDIA RTX PRO 6000 Blackwell (94GB each)\\n- CUDA 12.8, Python 3.12.3 (conda base)\\n- torch 2.10.0+cu128, transformers 4.57.6\\n- 环境激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 模型路径: `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`\\n- Llama 模型路径: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`\\n- XGrammar v2 已安装\\n\\n## 数据信息\\n\\n### SciERC\\n- HuggingFace `zj88zj/SCIERC`, 551 sentences, 7 relation types, 17-35 valid pairs each（约束松散）\\n\\n### DocRED\\n- HuggingFace Hub .gz, 998 docs, 96 relation types, avg 5.68 valid pairs/relation (约束紧)\\n\\n## 分析工具 (2026-05-13)\\n- `compare_prompts.py`: minimal vs schema-informed 对比 + McNemar 检验\\n- `violation_checker.py` / `violation_checker_docred.py`: 4 类 violation 分析\\n\", \"total_chars\": 11588, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dea6c2dd-e0f9-40ed-ab03-cd260200073c",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "805717f9-d9e3-4a17-a1f8-6072d530dbe4",
  "sourceToolAssistantUUID": "dea6c2dd-e0f9-40ed-ab03-cd260200073c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-14T11:00:22.035Z_

<details open><summary>🔧 Tool call — Read · `toolu_0111kZS5VSP1eU7sGZ5izw9P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "805717f9-d9e3-4a17-a1f8-6072d530dbe4",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LzH6vNMkUGSbQ4jpcr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70bcc675-1100-43bc-8765-4faf82127f8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019yLXpb3me8rYGpkufKV52g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6811,
      "cache_read_input_tokens": 59104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6811,
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

_source line 45 · 2026-05-14T11:00:22.054Z_

<details><summary>↩ Tool result · `toolu_0111kZS5VSP1eU7sGZ5izw9P`</summary>

```text
1	% ============================================================
2	% Merged authoritative BibTeX references (9 entries)
3	% Merged 2026-05-14 from relwork_new_entries.bib + new_references.bib
4	% ============================================================
5	
6	% Confirmed via: Semantic Scholar, arXiv:2201.11227, OpenReview
7	% WARNING: cite key says neurips2022, but actual venue is ICLR 2022
8	@inproceedings{synchromesh_neurips2022,
9	  title     = {Synchromesh: Reliable Code Generation from Pre-trained Language Models},
10	  author    = {Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares, Gustavo and Meek, Christopher and Gulwani, Sumit},
11	  booktitle = {International Conference on Learning Representations},
12	  year      = {2022},
13	  url       = {https://openreview.net/forum?id=KmtVD97J43e}
14	}
15	
16	% Confirmed via: NeurIPS 2023 proceedings, microsoft/monitors4codegen GitHub
17	@inproceedings{mgd_neurips2023,
18	  title     = {Monitor-Guided Decoding of Code {LMs} with Static Analysis of Repository Context},
19	  author    = {Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. and Rajamani, Sriram K.},
20	  booktitle = {Advances in Neural Information Processing Systems},
21	  volume    = {36},
22	  year      = {2023},
23	  url       = {https://proceedings.neurips.cc/paper_files/paper/2023/hash/662b1774ba8845fc1fa3d1fc0177ceeb-Abstract-Conference.html}
24	}
25	
26	% Confirmed via: ACM DL doi:10.1145/3729274, arXiv:2504.09246, SRI Lab ETH
27	@article{pldi2025_type_constrained_codegen,
28	  title     = {Type-Constrained Code Generation with Language Models},
29	  author    = {M\"{u}ndler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn and Vechev, Martin},
30	  journal   = {Proceedings of the ACM on Programming Languages},
31	  volume    = {9},
32	  number    = {PLDI},
33	  year      = {2025},
34	  doi       = {10.1145/3729274},
35	  url       = {https://dl.acm.org/doi/10.1145/3729274}
36	}
37	
38	% Confirmed via: ACL Anthology W04-2401, scottyih.org
39	% WARNING: cite key suggests AAAI 2004, but actual venue is CoNLL 2004 at HLT-NAACL
40	@inproceedings{roth_yih_2004,
41	  title     = {A Linear Programming Formulation for Global Inference in Natural Language Tasks},
42	  author    = {Roth, Dan and Yih, Wen-tau},
43	  booktitle = {Proceedings of the Eighth Conference on Computational Natural Language Learning ({CoNLL}-2004) at {HLT}-{NAACL} 2004},
44	  pages     = {1--8},
45	  year      = {2004},
46	  address   = {Boston, Massachusetts, USA},
47	  url       = {https://aclanthology.org/W04-2401/}
48	}
49	
50	% Confirmed via: ACL Anthology 2023.findings-emnlp.425, zjunlp/AdaKGC GitHub
51	@inproceedings{adakgc_emnlp2023,
52	  title     = {Schema-adaptable Knowledge Graph Construction},
53	  author    = {Ye, Hongbin and Gui, Honghao and Xu, Xin and Chen, Xi and Chen, Huajun and Zhang, Ningyu},
54	  booktitle = {Findings of the Association for Computational Linguistics: {EMNLP} 2023},
55	  pages     = {6408--6431},
56	  year      = {2023},
57	  url       = {https://aclanthology.org/2023.findings-emnlp.425/}
58	}
59	
60	% Confirmed via: ACL Anthology 2024.acl-long.475, arXiv:2403.07969
61	@inproceedings{knowcoder_acl2024,
62	  title     = {{KnowCoder}: Coding Structured Knowledge into {LLMs} for Universal Information Extraction},
63	  author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
64	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
65	  pages     = {8758--8779},
66	  year      = {2024},
67	  address   = {Bangkok, Thailand},
68	  url       = {https://aclanthology.org/2024.acl-long.475/}
69	}
70	
71	% Confirmed via: Oxford Academic Bioinformatics btae104, PubMed 38383067
72	@article{spires_2024,
73	  title     = {Structured Prompt Interrogation and Recursive Extraction of Semantics ({SPIRES}): A Method for Populating Knowledge Bases Using Zero-shot Learning},
74	  author    = {Caufield, J. Harry and Hegde, Harshad and Emonet, Vincent and Harris, Nomi L. and Joachimiak, Marcin P. and Matentzoglu, Nicolas and Kim, HyeongSik and Moxon, Sierra and Reese, Justin T. and Haendel, Melissa A. and Robinson, Peter N. and Mungall, Christopher J.},
75	  journal   = {Bioinformatics},
76	  volume    = {40},
77	  number    = {3},
78	  pages     = {btae104},
79	  year      = {2024},
80	  doi       = {10.1093/bioinformatics/btae104},
81	  url       = {https://academic.oup.com/bioinformatics/article/40/3/btae104/7612230}
82	}
83	
84	% Confirmed via: arXiv:2510.01409, Wiley Advanced Intelligent Systems doi:10.1002/aisy.202501381
85	@misc{ontologx_2025,
86	  title         = {{OntoLogX}: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models},
87	  author        = {Cotti, Luca and Drago, Idilio and Rula, Anisa and Bianchini, Devis and Cerutti, Federico},
88	  year          = {2025},
89	  eprint        = {2510.01409},
90	  archiveprefix = {arXiv},
91	  primaryclass  = {cs.AI},
92	  url           = {https://arxiv.org/abs/2510.01409}
93	}
94	
95	% Confirmed via: Springer LNCS 15370, arXiv:2411.15666, Lama-West GitHub
96	@inproceedings{ekaw2024_ontology_beam,
97	  title     = {Ontology-Constrained Generation of Domain-Specific Clinical Summaries},
98	  author    = {Mehenni, Gaya and Zouaq, Amal},
99	  booktitle = {Knowledge Engineering and Knowledge Management ({EKAW} 2024)},
100	  series    = {Lecture Notes in Computer Science},
101	  volume    = {15370},
102	  pages     = {382--398},
103	  year      = {2024},
104	  publisher = {Springer},
105	  doi       = {10.1007/978-3-031-77792-9_23}
106	}
107	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70bcc675-1100-43bc-8765-4faf82127f8b",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "0d5afe58-a876-43bd-b132-e521bfc12354",
  "sourceToolAssistantUUID": "70bcc675-1100-43bc-8765-4faf82127f8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T11:00:23.118Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DnpWpuxByxriLTohNQgriv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/median/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d5afe58-a876-43bd-b132-e521bfc12354",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LzH6vNMkUGSbQ4jpcr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "807727ed-02dd-4821-abac-95ab59f7ed76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019yLXpb3me8rYGpkufKV52g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6811,
      "cache_read_input_tokens": 59104,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6811
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 59104,
          "cache_creation_input_tokens": 6811,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6811,
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

_source line 47 · 2026-05-14T11:00:23.125Z_

<details><summary>↩ Tool result · `toolu_01DnpWpuxByxriLTohNQgriv`</summary>

```text
1	@inproceedings{luan2018multi,
2	  title={Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
3	  author={Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
4	  booktitle={EMNLP},
5	  year={2018}
6	}
7	
8	@inproceedings{yao2019docred,
9	  title={{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},
10	  author={Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},
11	  booktitle={ACL},
12	  year={2019}
13	}
14	
15	@article{dong2024xgrammar,
16	  title={{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},
17	  author={Dong, Yixin and Shi, Charlie and Shrivastava, Anirudh and Li, Yiming and Wang, Zhuonan and Chen, Tianqi},
18	  journal={arXiv preprint arXiv:2411.15100},
19	  year={2024}
20	}
21	
22	@article{qwen2025qwen3,
23	  title={Qwen3 Technical Report},
24	  author={{Qwen Team}},
25	  journal={arXiv preprint},
26	  year={2025}
27	}
28	
29	@article{willard2023efficient,
30	  title={Efficient Guided Generation for Large Language Models},
31	  author={Willard, Brandon T and Louf, R{\'e}mi},
32	  journal={arXiv preprint arXiv:2307.09702},
33	  year={2023}
34	}
35	
36	@inproceedings{scholak2021picard,
37	  title={{PICARD}: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models},
38	  author={Scholak, Torsten and Schucher, Nathan and Bahdanau, Dzmitry},
39	  booktitle={EMNLP},
40	  year={2021}
41	}
42	
43	@article{geng2024grammar,
44	  title={Grammar-Aligned Decoding},
45	  author={Geng, Kanghee and Pailoor, Sumanth and Tan, Shankara Pailoor and Dillig, Isil},
46	  journal={arXiv preprint},
47	  year={2024}
48	}
49	
50	@article{wei2023zeroshot,
51	  title={Zero-Shot Information Extraction via Chatting with {ChatGPT}},
52	  author={Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and Huang, Shen and Xie, Pengjun and Xu, Jinan and Chen, Yufeng and Zhang, Meishan and Jiang, Yong and Han, Wenjuan},
53	  journal={arXiv preprint arXiv:2302.10205},
54	  year={2023}
55	}
56	
57	@inproceedings{li2023codeie,
58	  title={{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
59	  author={Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
60	  booktitle={ACL},
61	  year={2023}
62	}
63	
64	@inproceedings{wang2023instructuie,
65	  title={{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},
66	  author={Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuan and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and others},
67	  booktitle={ACL},
68	  year={2023}
69	}
70	
71	@inproceedings{sainz2024gollie,
72	  title={{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
73	  author={Sainz, Oscar and Garc{\'\i}a-Ferrero, Iker and Agerri, Rodrigo and de Lacalle, Oier Lopez and Rigau, German and Agirre, Eneko},
74	  booktitle={ICLR},
75	  year={2024}
76	}
77	
78	@article{zheng2024openchat,
79	  title={{CRANE}: Mitigating Structural Hallucination in Grammar-Constrained Large Language Model Decoding},
80	  author={Zheng, Kangrui and others},
81	  journal={arXiv preprint},
82	  year={2024}
83	}
84	
85	@article{wu2024structure,
86	  title={Structure Snowballing in Grammar-Constrained Decoding},
87	  author={Wu, Yifan and others},
88	  journal={arXiv preprint},
89	  year={2024}
90	}
91	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "807727ed-02dd-4821-abac-95ab59f7ed76",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "437f72b6-32e8-447d-8710-6cf1e51322d8",
  "sourceToolAssistantUUID": "807727ed-02dd-4821-abac-95ab59f7ed76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-14T11:00:27.590Z_

I now have a comprehensive understanding of the paper, its experimental results, related work, and internal project documentation. Let me now compose the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "437f72b6-32e8-447d-8710-6cf1e51322d8",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LzjSh7AckGjZ8GET8f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5da53935-68c2-454b-a448-5135a883c8d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lt4LnSP64zfxdEmNzo1fsK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3972,
      "cache_read_input_tokens": 65915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3972,
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

_source line 49 · 2026-05-14T11:02:35.224Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_015ZeMWRMJV4ViwM1Qawfh61`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "tier": "best",
  "dream_id": "dream_20260514T094226",
  "overall_score": "Weak Reject (3)",
  "report": "# Reviewer R2 — Novelty, Significance, Related Work, Writing Quality\n\n## Paper: \"How LLMs Violate Ontology Constraints: A Landscape Study and Grammar-Based Mitigation\" / \"OntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints\"\n\n**Note**: The \"best\" and \"median\" tier drafts differ in title and some numerical details. This review covers both, noting discrepancies where material.\n\n---\n\n## 1. Novelty Assessment\n\n### 1.1 Violation Landscape Study (Contribution 1)\n**Moderate novelty.** The systematic measurement of ontology constraint violations in LLM-based IE is, to my knowledge, genuinely new — no prior work has characterized the per-relation distribution of type constraint violations in LLM-generated IE outputs. The finding that constraint tightness predicts violation rate is a useful empirical insight.\n\nHowever, measuring error rates of LLM outputs against a known schema is conceptually straightforward. The landscape study is descriptive rather than explanatory: the tightness-violation correlation is intuitive (tighter constraints leave less room for valid outputs, so violations are more likely) and does not reveal deeper mechanisms about *why* LLMs produce these violations (e.g., distributional prior conflicts, attention patterns, or training data biases). The \"prior-constraint conflict\" analysis for Evaluate-for is suggestive but underdeveloped.\n\nThe landscape study spans only 2 datasets and 1-2 models, which limits its generality as a standalone empirical contribution. A landscape study claiming to characterize \"how LLMs violate ontology constraints\" should ideally include more diverse ontologies, model families, and scales.\n\n### 1.2 Grammar-Constrained Decoding for IE (Contribution 2)\n**Low novelty.** Applying XGrammar to enforce JSON structure and vocabulary compliance is a straightforward engineering application of an existing tool. The paper itself acknowledges that grammar-constrained decoding is the \"de facto standard for structured output\" from LLMs. Compiling an IE ontology's entity types and relation names into a CFG and feeding it to XGrammar is exactly what the tool was designed for.\n\nThe result (ET→0%, RV→0%) is expected by construction — this is the definition of grammar-constrained decoding. Reporting that it works is necessary for completeness but does not constitute a research contribution. The latency overhead measurement (13-14%) has some practical value.\n\n### 1.3 Semantic Constraint Layer (Contribution 3)\n**Moderate novelty with significant caveats.** The stateful entity registry + dynamic logit masking for cross-field domain/range enforcement during autoregressive generation is the most novel component. The key idea — maintaining state across generation positions to enforce constraints beyond CFG expressiveness — is technically sound and fills a genuine gap.\n\nHowever:\n- The mechanism (bitwise AND of two mask vectors) is elementary.\n- The concept of type-constrained decoding with stateful monitors already exists in the code generation domain (Synchromesh ICLR'22, MGD NeurIPS'23, PLDI'25). The paper's own related work section acknowledges this. The transfer from code generation to IE is the claimed novelty, but the technical delta is modest — IE ontologies have flat domain/range sets (simpler than programming language type systems), and the main new challenge (inferring entity types from free text) is handled by simply recording types from the entity list, not by a novel inference mechanism.\n- Effectiveness degrades substantially on DocRED (only 46% DR reduction vs 94% on SciERC), and the paper introduces a new class of violations (CF: 9.9% on SciERC) that did not exist in the unconstrained baseline. This trade-off weakens the practical value proposition.\n\n### 1.4 Overall Novelty Verdict\nThe paper's novelty is spread thin across three contributions, none of which is individually strong enough for a top venue. The landscape study is useful but shallow; the grammar layer is engineering; the semantic layer is the most novel but has limited effectiveness and introduces side effects. The \"decidability taxonomy\" (local / prefix-decidable / non-local) is a reasonable framing but not a deep theoretical contribution — it is a restatement of well-known properties of autoregressive generation.\n\n---\n\n## 2. Significance and Impact\n\n### 2.1 Who would use these findings?\nPractitioners building LLM-based IE pipelines who need ontology compliance. The grammar layer is immediately deployable. The semantic layer requires implementing the TypeConstraintProcessor per ontology.\n\n### 2.2 Is the grammar layer finding actionable enough to justify publication?\nNo. \"Use XGrammar to enforce JSON schema\" is good engineering advice, not a research contribution. This belongs in a technical blog post or toolkit documentation, not a top-venue paper.\n\n### 2.3 Does the violation landscape data have reuse value?\nModerate. The per-relation violation data for SciERC and DocRED could inform future work on targeted constraint enforcement. However, the landscape is model-specific (Qwen3-8B) and setting-specific (zero-shot). Different models, prompt strategies, or fine-tuning would produce different violation landscapes.\n\n### 2.4 Is the positioning effective?\nThe paper tries to be both an empirical study and a method paper, but this dual positioning weakens both aspects. As an empirical study, it lacks breadth (2 datasets, 1-2 models). As a method paper, the method's effectiveness is partial (46% on DocRED) and introduces a new failure mode (CF violations). The paper would be stronger if it committed fully to one identity.\n\n### 2.5 Practical Significance Concern\nThe absolute R-F1 is ~8% across all configurations. The paper correctly notes this is a zero-shot setting and F1 is a control variable. However, this means the constraint enforcement is being evaluated on a system whose extraction quality is far below practical utility. It is unclear whether constrained decoding would provide the same benefits (or introduce the same CF trade-offs) on a fine-tuned model with R-F1 in the 40-50% range where the outputs actually matter. This limits the practical significance of the findings.\n\n---\n\n## 3. Related Work Coverage\n\n### 3.1 Reference Count\nThe \"median\" tier paper cites ~13 references; the extended related work section (section6_related_work.tex) cites ~25. The extended version is adequate; the short versions are insufficient. A paper making claims about being \"the first\" to do something must demonstrate thorough coverage of prior art.\n\n### 3.2 Missing or Underrepresented Areas\n\n**Structured prediction for IE (critical gap):**\n- Roth & Yih (2004) is cited in the extended version but absent from the main drafts. This is the foundational work on enforcing type constraints in IE via ILP — the paper should explicitly position against it.\n- Joint entity-relation extraction models (e.g., SpERT, PURE, PFN, UniRel) that implicitly enforce type constraints through shared representations are entirely absent.\n- CasRel, TPLinker, and other structured prediction approaches for RE that handle type constraints architecturally.\n\n**Other constrained decoding methods:**\n- PICARD (Scholak et al., 2021) is cited in the median bib but not discussed. PICARD does incremental parsing for SQL — a highly relevant constrained decoding approach.\n- Guidance (Microsoft) and Instructor — practical tools for structured LLM output that compete with the grammar layer.\n- JSON mode / structured output features built into commercial APIs (OpenAI, Anthropic) that solve the grammar-layer problem out of the box.\n\n**Schema-guided generation:**\n- SGD (Schema-Guided Dialogue) and schema-guided approaches in dialogue systems.\n- TANL (Paolini et al., 2021) — structured generation for IE.\n\n**KG completion with type constraints:**\n- TransE/TransR/RotatE with type constraints are not discussed. Type-constrained KG completion (Krompass et al., 2015, mentioned in the task description but absent from the paper) is a relevant precedent.\n\n**Error analysis in IE:**\n- Prior work on error analysis of IE systems (e.g., detailed error taxonomies for RE, NER error analysis) is not cited. The violation taxonomy presented is novel in the specific context of ontology constraints but should be positioned against existing error analysis frameworks.\n\n### 3.3 Is the positioning fair?\nThe claim \"first systematic study of ontology constraint violations in LLM-based IE\" appears defensible based on my knowledge. However, the claim \"first to migrate type-constrained decoding from code generation to IE\" (from the extended related work) may be overly strong — EnriCo (Zaratiana et al., AAAI 2024) applies ASP constraints during decoding for joint entity-relation extraction, which is a form of semantic-constrained decoding for IE, even if it uses different formalism.\n\n---\n\n## 4. Writing Quality\n\n### 4.1 Clarity of Exposition\nGenerally clear. The violation taxonomy (ET/RV/DR/CF) is well-defined. The enabling dependency between grammar and semantic layers is explained well. The constraint tightness definition is intuitive.\n\n### 4.2 Organization and Flow\nThe paper is well-organized with a logical progression from landscape study to method to experiments. The \"best\" tier draft has better flow than the \"median\" tier, with section numbering and cross-references more consistently applied.\n\n### 4.3 Negative Results Presentation\n**A strength of this paper.** The honest presentation of:\n- DocRED's attenuated results (46% vs 94%)\n- CF violation trade-off (9.9% on SciERC)\n- S2 offering no improvement over S1\n- Evaluate-for regression under schema-informed prompting\n\n...is commendable and reflects scientific integrity. The paper does not oversell its findings.\n\n### 4.4 Title/Abstract Alignment\nThe \"best\" tier title (\"Near-Complete Type-Valid IE via Compiled Ontology Constraints\") overpromises slightly — \"near-complete\" applies to SciERC but not DocRED where 10.19% DR remains. The \"median\" tier title (\"Type-Valid IE via Compiled Ontology Constraints\") is more appropriate.\n\nThe landscape study title variant (\"How LLMs Violate Ontology Constraints: A Landscape Study and Grammar-Based Mitigation\") better reflects the paper's actual balance of contributions but undersells the semantic layer.\n\n### 4.5 Specific Writing Issues\n- The paper inconsistently uses \"14%\" and \"62%\" for latency overhead across drafts (the \"best\" tier says 37%, the \"median\" says 62% for full S1). These numbers need reconciliation.\n- Some tables present \"---\" for values that should be reported (e.g., grammar-only DR on DocRED in Table 5 of the median draft).\n- The \"enabling ratio\" metric (full DR reduction / semantic-only DR reduction) is introduced without adequate motivation for why this specific ratio is informative.\n\n---\n\n## 5. Weaknesses (Numbered)\n\n**W1 (Major): Limited experimental scope undermines generality claims.** Two datasets, one primary model (Qwen3-8B), zero-shot only. The cross-model validation with Llama-3.1-8B is SciERC-only and appears incomplete in the current drafts. For a paper claiming to present a general framework, this is insufficient. Critical missing experiments: (a) a fine-tuned model where F1 is practically meaningful; (b) at least one additional ontology domain (biomedical, financial); (c) larger models (70B+) where violation patterns may differ.\n\n**W2 (Major): The CF violation trade-off is inadequately addressed.** The semantic layer eliminates 94% of DR violations on SciERC but introduces 9.9% CF violations that did not exist before. The paper argues CF violations are \"softer\" than DR violations, but this is assertion rather than demonstrated. In a knowledge graph, an entity with inconsistent types across relations creates downstream inference failures. The net benefit calculation (DR reduction per CF increase) is not grounded in any downstream task evaluation.\n\n**W3 (Major): DocRED results are weak and inconsistent across drafts.** The \"best\" tier claims 46% DR reduction; the paper_framing.md mentions 35.5%. The grammar-only DR on DocRED *increases* from 18.7% to 26.17%, which the paper explains as a \"denominator effect\" — but this explanation itself reveals that the violation measurement is confounded by the constraint intervention. The tightness-violation correlation on DocRED is weak (rho=0.37 in one draft, 0.52 in another, 0.14 in the task description). These inconsistencies across drafts suggest the results are still in flux.\n\n**W4 (Moderate): No downstream task evaluation.** All evaluation is intrinsic (violation rates, F1 against gold labels). There is no evaluation of whether reduced violations actually improve downstream KG quality, question answering, or reasoning. The motivation section argues violations matter for \"downstream knowledge graph population, reasoning engines, and regulatory compliance systems\" — but this claim is never empirically validated.\n\n**W5 (Moderate): The decidability taxonomy is underexploited.** The three-level taxonomy (local / prefix-decidable / non-local) is presented as a contribution but only Type (a) and Type (b) constraints are addressed. Type (c) — forward coreference — is acknowledged as out of scope. The taxonomy itself is a straightforward observation about autoregressive generation and does not offer deep insight.\n\n**W6 (Moderate): Insufficient comparison with simpler baselines.** The paper compares against unconstrained generation and schema-informed prompting. Missing baselines: (a) post-hoc filtering (reject + regenerate invalid triples); (b) self-consistency voting across multiple samples; (c) few-shot prompting with constraint examples; (d) simple regex-based type checking during generation (without the full semantic layer machinery).\n\n**W7 (Minor): The paper conflates two different papers.** The \"best\" and \"median\" tier drafts present materially different numbers, framings, and even titles. The Spearman rho for tightness-DR on DocRED varies from 0.14 to 0.52 across documents. This suggests the experimental results are not yet settled, which is concerning for review.\n\n---\n\n## 6. Questions for Authors (Numbered)\n\n**Q1.** The DocRED Spearman rho for tightness-DR correlation is reported as 0.14 (p=0.18) in one place and 0.52 (p<0.001) in another. Which is correct? Is the discrepancy due to measuring unconstrained vs. constrained (full_s1) DR? If so, why does the correlation change so dramatically?\n\n**Q2.** Have you measured whether CF violations actually harm downstream tasks? The severity distinction (DR = hard, CF = soft) is intuitive but unvalidated. In what downstream application would CF violations be acceptable?\n\n**Q3.** What happens when this framework is applied to a fine-tuned IE model with R-F1 in the 40-50% range? Does the violation rate decrease (making constraints less necessary) or does the constraint framework still provide meaningful benefit?\n\n**Q4.** The grammar-only DR on DocRED *increases* (18.7% → 26.17%). You explain this as a denominator effect. But could it also reflect that grammar constraints force the model into generation patterns that produce more DR violations? Have you analyzed whether the set of DR-violating triples under grammar-only overlaps with the unconstrained set?\n\n**Q5.** Why is no post-hoc filtering baseline reported? The paper argues against post-hoc filtering in the introduction but never empirically compares against it. A reject-and-regenerate baseline would clarify whether the decoding-time approach offers genuine advantages beyond computational efficiency.\n\n**Q6.** The CF analysis attributes 85% of SciERC CF violations to \"type system ambiguity.\" How do you distinguish genuine ambiguity from method-induced errors? Is there human annotation to validate this claim?\n\n**Q7.** How sensitive are the results to the output JSON format? If the entity list were generated *after* relations (or interleaved), would the semantic layer's entity registry mechanism still work?\n\n---\n\n## 7. Minor Issues\n\n- M1: The latency overhead numbers are inconsistent across drafts (14% vs 23% vs 37% vs 62% for various configurations). These need to be reconciled into a single coherent set.\n- M2: Table 4 in paper_tables_draft.tex has \"TBD\" entries for DocRED S1, suggesting the paper is not yet complete.\n- M3: The bib file has cite key naming issues (e.g., `synchromesh_neurips2022` is actually ICLR 2022; `roth_yih_2004` suggests AAAI but is CoNLL at HLT-NAACL).\n- M4: The `zhou2026snowballing` reference has a \"PENDING AUDIT\" comment in the extended related work, suggesting unverified citations.\n- M5: The \"Conjunction\" relation in SciERC has 0% DR both before and after constraints — including it in the ablation table adds noise without information.\n- M6: No confidence intervals, bootstrap estimates, or significance tests are reported for the main DR reduction numbers. The paper correctly notes F1 differences are not significant but does not apply the same rigor to violation rate differences.\n- M7: The paper should report wall-clock times for the full pipeline (compilation + inference), not just per-token overhead, since compilation cost matters for deployment.\n\n---\n\n## 8. Score and Justification\n\n**Score: 3 (Weak Reject)**\n\n**Justification:**\n\nThe paper addresses a real and practical problem — LLM-based IE systems do produce ontology violations, and constrained decoding is a reasonable approach. The honest presentation of negative results (DocRED degradation, CF trade-off) is commendable.\n\nHowever, the paper falls short of the acceptance bar for a top ML venue for several reasons:\n\n1. **Novelty is insufficient.** The grammar layer is engineering; the semantic layer transfers an existing idea (type-constrained decoding) from code generation to IE with modest technical delta; the landscape study is descriptive but shallow.\n\n2. **Experimental scope is narrow.** Two datasets, one primary model, zero-shot only. The DocRED results are weak and internally inconsistent across drafts.\n\n3. **The CF trade-off undermines the core value proposition.** Eliminating one violation type while introducing another is a net unclear benefit without downstream evaluation.\n\n4. **Related work coverage is thin** in the main paper drafts (7-13 references), missing important prior work on structured prediction for IE, joint extraction models, and alternative constrained decoding methods.\n\n5. **No downstream evaluation.** The practical motivation (KG quality, reasoning, compliance) is never empirically validated.\n\nThe paper could be strengthened by: (a) committing to either a thorough empirical study (more models, datasets, settings) OR a method paper with downstream evaluation; (b) addressing CF violations with a concrete solution rather than just analysis; (c) including post-hoc filtering and few-shot baselines; (d) expanding related work significantly.\n\nAs currently positioned, the paper is a competent technical report that would be appropriate for a workshop or a systems/demo track, but does not meet the novelty and significance bar for a main conference paper at a top ML/NLP venue.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5da53935-68c2-454b-a448-5135a883c8d2",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2LzjSh7AckGjZ8GET8f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "568058bd-45fd-40fb-9e36-9608f2ec430a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lt4LnSP64zfxdEmNzo1fsK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3972,
      "cache_read_input_tokens": 65915,
      "output_tokens": 4778,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3972
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4778,
          "cache_read_input_tokens": 65915,
          "cache_creation_input_tokens": 3972,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3972,
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

_source line 50 · 2026-05-14T11:02:36.051Z_

<details><summary>↩ Tool result · `toolu_015ZeMWRMJV4ViwM1Qawfh61`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/review_report.md\", \"dream_id\": \"dream_20260514T094226\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "568058bd-45fd-40fb-9e36-9608f2ec430a",
  "isSidechain": true,
  "promptId": "965d5c44-a370-4beb-b701-af844cec963d",
  "agentId": "a60984db3486f111c",
  "type": "user",
  "uuid": "4832a3c2-7e60-49d4-bafe-e3cd3f6ae6ec",
  "sourceToolAssistantUUID": "568058bd-45fd-40fb-9e36-9608f2ec430a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-14T11:02:48.975Z_

The review has been submitted. Here is a summary of the key findings:

**Score: 3 (Weak Reject)**

**Core assessment:** The paper addresses a genuine practical problem (LLM-based IE producing ontology violations) with a reasonable two-layer constrained decoding approach. The honest reporting of negative results (DocRED degradation, CF trade-offs) is a strength.

**Main reasons for the score:**

1. **Thin novelty across three contributions** -- the grammar layer is straightforward XGrammar application; the semantic layer transfers type-constrained decoding from code gen (Synchromesh, MGD, PLDI'25) to IE with modest technical delta; the landscape study is descriptive but shallow (2 datasets, 1-2 models).

2. **Narrow experimental scope** -- zero-shot only, ~8% R-F1 far below practical utility, no fine-tuned model experiments, DocRED results internally inconsistent across draft tiers (Spearman rho varies from 0.14 to 0.52).

3. **CF violation trade-off unresolved** -- 94% DR reduction on SciERC but 9.9% CF introduced. No downstream evaluation validates the claimed DR>CF severity distinction.

4. **Related work gaps** -- main drafts cite only 7-13 references, missing structured prediction for IE (joint models), alternative constrained decoding (PICARD, Guidance), KG completion with type constraints, and commercial structured output features.

5. **No downstream task evaluation** despite motivating the work with KG quality, reasoning, and compliance use cases.

The review was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260514T094226/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4832a3c2-7e60-49d4-bafe-e3cd3f6ae6ec",
  "isSidechain": true,
  "agentId": "a60984db3486f111c",
  "requestId": "req_011Cb2MAXcKe88cp43F8n8G5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf842223-ba40-400b-b8c6-f8be8ea1d015",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "8810d8ca-95df-4cbf-a0e9-6349587d15d7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrbPutayq5aFYjp318jXnh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4907,
      "cache_read_input_tokens": 69887,
      "output_tokens": 432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4907
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 432,
          "cache_read_input_tokens": 69887,
          "cache_creation_input_tokens": 4907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4907,
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
