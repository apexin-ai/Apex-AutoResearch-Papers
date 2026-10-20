# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Y

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 76
- **Recorded user turns:** 1
- **Tool calls:** 31
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ab33643faef5b2735.jsonl`
- **Structured JSON:** [`da78737598842545d94d.json`](../../sessions/da/da78737598842545d94d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

76 recorded events

### User

_source line 1 · 2026-05-18T17:32:01.090Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus areas are **novelty/contribution** and **related work positioning**.

## Paper Summary
Title: "How and When Do LLMs Violate Ontology Constraints? An Empirical Study with Decoding-Time Enforcement"

The paper presents a large-scale empirical study of ontology constraint violations in LLM-based information extraction (IE) across 3 tasks (RE on SciERC/DocRED, EE on WikiEvents), 4 model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.1-70B), and 2 training regimes (zero-shot, fine-tuned). Key claims:
1. Violation severity is determined by constraint tightness × task complexity, not model scale alone
2. A prefix-decidability taxonomy classifies constraints into 3 categories: (a) purely local, (b) prefix-decidable with state, (c) truly non-local
3. OntoCoDec compiles ontology schemas into grammar (CFG) + semantic (stateful logit masking) constraint layers
4. Cross-field consistency (CF) violations are a systematic trade-off

## Key Results
- SciERC 70B: DR 6.5%→0% (100% reduction), ΔR-F1 +0.02pp
- DocRED 70B: DR 1.8%→0.3% (83.3% reduction, absolute Δ=1.5pp on 17K triples, ~265→44 violating triples)
- WikiEvents EE 8B: RoV 64-89%, grammar-only RoV 64-77%, full system RoV→0%
- FT composability: total violations 9.2%→1.9%, but CF 0.1%→1.8%
- CF trade-off: 1.8-21.1% CF introduced across configurations
- Trigger F1 improvements NOT significant; Entity F1 improvements are format compliance effects
- Latency overhead: 13-32% scaling with schema complexity

## Related Work Section (from paper)
- Constrained Decoding: References Willard & Louf 2023, Geng et al. 2024, XGrammar, DOMINO. Claims OntoCoDec extends to IE-specific ontology constraints with semantic layer.
- LLM IE: Mentions GoLLIE, CodeIE, InstructUIE, UniEX. Claims they lack constraint enforcement.
- Ontology-Guided IE: Claims classical IE had hard-coded validation; neural approaches abandoned it; OntoCoDec bridges the gap.
- Type Systems for Neural Generation: Notes the analogy has been observed in code generation.

## Experiment Design Reference
Full plan included 70B experiments on both datasets, error analysis, FT composability on EE, grammar-only ablation across 3 models, bootstrap CI, and latency measurements. Most are present in the paper. WikiEvents latency is estimated, not measured.

## Your Task
Provide a detailed review covering:

1. **Novelty Assessment**
   - Is the prefix-decidability taxonomy a genuine contribution, or a straightforward formalization of known distinctions?
   - Is OntoCoDec technically novel, or is it a combination of existing techniques (CFG masking + lookup-table logit masking)?
   - Is the empirical study itself a sufficient contribution even if the method is incremental?
   - Does "constraint tightness determines violation severity" provide new insight, or is it obvious in hindsight?

2. **Related Work Adequacy**
   - Are there important missing references? (Consider: structured prediction with constraints, ontology alignment, knowledge graph completion with type constraints, constrained beam search, semantic parsing with type checking, neuro-symbolic IE)
   - Is the positioning against prior work accurate and fair?
   - Only 2 references in the bibliography — is this severely insufficient?
   - How well does the paper differentiate from grammar-constrained decoding (Willard & Louf, XGrammar)?

3. **Contribution Significance**
   - At 70B scale on DocRED, the method provides 1.5pp absolute improvement while introducing 3.8% CF. Is this net positive?
   - The "type checking for neural generation" framing — is this compelling?
   - Is the work more of an engineering contribution or a research contribution?

4. **Strengths** (bullet list)
5. **Weaknesses** (bullet list)  
6. **Questions for Authors**
7. **Score** (1-6) with justification
8. **Confidence** (1-5)

Be critical but fair. Focus on whether the novelty and positioning meet the bar for a top ML venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "c4459262-7a5e-477a-bfdb-5991c157b476",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T17:32:01.094Z_

```json
{
  "parentUuid": "c4459262-7a5e-477a-bfdb-5991c157b476",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
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
  "uuid": "1f78c4f9-b5e0-4ae3-bd82-eee84d2b5b01",
  "timestamp": "2026-05-18T17:32:01.094Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T17:32:03.933Z_



I'll start by reading the paper and related project files to provide a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f78c4f9-b5e0-4ae3-bd82-eee84d2b5b01",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS6XgYJGY5wcBzHunCR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba5fda2b-d5b1-4c4a-b9c8-8c90cfb046f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHovd2U232LUA76FFHJ4Gq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8530,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8530,
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

_source line 4 · 2026-05-18T17:32:04.819Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SR6XY5twn2U6hsrm5Mx1Kp`</summary>

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
  "parentUuid": "ba5fda2b-d5b1-4c4a-b9c8-8c90cfb046f8",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS6XgYJGY5wcBzHunCR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03bd7281-b0a4-4110-9f4e-194b1f0f0d21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YHovd2U232LUA76FFHJ4Gq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8530,
      "cache_read_input_tokens": 8252,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8530
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 8530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8530,
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

_source line 5 · 2026-05-18T17:32:04.835Z_

<details><summary>↩ Tool result · `toolu_01SR6XY5twn2U6hsrm5Mx1Kp`</summary>

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
  "parentUuid": "03bd7281-b0a4-4110-9f4e-194b1f0f0d21",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "c32ad125-29e9-46d4-8555-3cad4d0aa2aa",
  "sourceToolAssistantUUID": "03bd7281-b0a4-4110-9f4e-194b1f0f0d21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T17:32:07.786Z_



Let me read the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c32ad125-29e9-46d4-8555-3cad4d0aa2aa",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS6ooQUMZcYc1mFDkQU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "508b2947-8b77-44b8-a0ae-f8b5cf32e58d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GprXUGYir43mfFocUoYP4e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16782,
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

_source line 7 · 2026-05-18T17:32:07.896Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01N4kia3KDuENCsXn9XuTUZD`</summary>

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
  "parentUuid": "508b2947-8b77-44b8-a0ae-f8b5cf32e58d",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS6ooQUMZcYc1mFDkQU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73c599e3-1f8e-48b5-9188-b6be0fb969b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GprXUGYir43mfFocUoYP4e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16782,
      "output_tokens": 92,
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
          "output_tokens": 92,
          "cache_read_input_tokens": 16782,
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

_source line 8 · 2026-05-18T17:32:09.545Z_

<details><summary>↩ Tool result · `toolu_01N4kia3KDuENCsXn9XuTUZD`</summary>

```text
{"result":"# 项目 schema_semantic_constrained_ie 概况\n\n## 实验状态 (88 个)\n\n- **llama_scierc_full_s1**: DONE (success) — \n- **llama_scierc_unconstrained**: DONE (success) — \n- **phase2_scierc_full_s1**: DONE (success) — \n- **phase2_scierc_semantic_only**: DONE (success) — \n- **phase2_scierc_grammar_only**: DONE (success) — \n- **phase2_scierc_unconstrained**: DONE (success) — \n- **phase2_docred_full_s1**: DONE (success) — \n- **phase2_docred_semantic_only**: DONE (success) — \n- **phase2_docred_unconstrained**: DONE (success) — \n- **mvp_phase0_docred_schema_r2**: DONE (killed) — \n- **phase2_s2_pilot50**: DONE (success) — \n- **mvp_phase0_docred_schema**: DONE (success) — \n- **mvp_phase0_violation_rate_docred**: DONE (success) — \n- **mvp_phase0_scierc_schema**: DONE (success) — \n- **mvp_phase0_violation_rate**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| w9_qwen_docred_zs_sampling_r2 | Continuation of w9 DocRED sampling from doc 106, testing OntoCoDec full_s1 with temperature sampling (T=0.7) on remaining 892 DocRED documents | — | — | — |\n| p8b_docred_latency | OntoCoDec constrained decoding overhead on Qwen3-8B DocRED (200-doc subset) measured on same GPU as P8 SciERC will confirm moderate overhead (<2x), providing consistent timing data for paper | — | — | — |\n| 70b_docred_constrained | 70B AWQ-INT4 model with OntoCoDec constrained decoding on DocRED will achieve 0% ET/RV violations while maintaining F1, demonstrating cross-dataset scalability | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **w9_qwen_docred_zs_sampling** (failed): Temperature sampling (T=0.7, top_p=0.9) with OntoCoDec full_s1 on Qwen3-8B DocRED will maintain low violation rates while exploring output diversity on cross-sentence RE with 96 relation types\n- **w9_qwen_scierc_zs_sampling** (success): Temperature sampling (T=0.7, top_p=0.9) with OntoCoDec full_s1 on Qwen3-8B SciERC will maintain low violation rates while potentially improving F1 through output diversity compared to greedy decoding\n  [w9_scierc_sampling_analysis](/api/workspace-files/projects/schema_semantic_constrained_ie/artifacts/w9_qwen_scierc_zs_sampling/report/w9_scierc_sampling_analysis.md)\n- **p8_latency_overhead** (success): OntoCoDec constrained decoding overhead on Qwen3-8B SciERC is moderate (<2x), demonstrating practical deployability\n\n## 趋势\n成功 75 / 负向 4 / 失败 1 / 共 84\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-16980: 无 GPU 信息\nwestd-21461: 空闲 cuda:0, cuda:1\n\n## 告警\n- mvp_phase0_docred_schema_r2: 已被终止 — unknown\n- w1_cf_fallback_docred: 已被终止 — unknown\n- w1_cf_fallback_llama_scierc: 已被终止 — unknown\n- w1_cf_fallback_llama_docred: 已被终止 — unknown\n- w9_qwen_docred_zs_sampling: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73c599e3-1f8e-48b5-9188-b6be0fb969b3",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "b8f8ed99-2a04-4a16-8467-bed9767f8d46",
  "sourceToolAssistantUUID": "73c599e3-1f8e-48b5-9188-b6be0fb969b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T17:32:13.373Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HpeMQfjD9qQxN4EQFzJ2G2`</summary>

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
  "parentUuid": "b8f8ed99-2a04-4a16-8467-bed9767f8d46",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS7A92DFBnWz2F4vNsa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1172b16a-cc17-4f62-86fa-84a47e8bd4ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131Vq3Wh4tDBWKys7cV9qK6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 18229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1318,
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

_source line 10 · 2026-05-18T17:32:13.385Z_

<details><summary>↩ Tool result · `toolu_01HpeMQfjD9qQxN4EQFzJ2G2`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1172b16a-cc17-4f62-86fa-84a47e8bd4ec",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "adbf29c4-c7cf-42ad-8301-c7f0fd125f50",
  "sourceToolAssistantUUID": "1172b16a-cc17-4f62-86fa-84a47e8bd4ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T17:32:13.878Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01F3i6XEUvgEdkHGVpxVeakd`</summary>

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
  "parentUuid": "adbf29c4-c7cf-42ad-8301-c7f0fd125f50",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS7A92DFBnWz2F4vNsa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d156eb1-61db-4b48-a0c0-59d287717c85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131Vq3Wh4tDBWKys7cV9qK6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 18229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1318,
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

_source line 12 · 2026-05-18T17:32:13.894Z_

<details><summary>↩ Tool result · `toolu_01F3i6XEUvgEdkHGVpxVeakd`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'schema_semantic_constrained_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d156eb1-61db-4b48-a0c0-59d287717c85",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "eaca89b5-2486-46a3-abfb-170146d7a91f",
  "sourceToolAssistantUUID": "7d156eb1-61db-4b48-a0c0-59d287717c85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T17:32:14.352Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Cn45AzPsTzn7qTdc6z3Q4L`</summary>

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
  "parentUuid": "eaca89b5-2486-46a3-abfb-170146d7a91f",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS7A92DFBnWz2F4vNsa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6d0e735-a5f5-4cd9-bdcd-1e22b14d7a50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131Vq3Wh4tDBWKys7cV9qK6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 18229,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1318
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 298,
          "cache_read_input_tokens": 18229,
          "cache_creation_input_tokens": 1318,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1318,
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

_source line 14 · 2026-05-18T17:32:14.364Z_

<details><summary>↩ Tool result · `toolu_01Cn45AzPsTzn7qTdc6z3Q4L`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/paper_framing.md\", \"content\": \"# OntoCoDec — Paper Framing\\n\\n## Target Venue\\nEMNLP 2026 (ARR submission May 25, 2026) — **目标: conference main**（D040, 用户明确指示）\\n\\n## Title\\nOntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints\\n(D015: \\\"Near-Complete\\\" dropped — DocRED residual DR=10.21% (Qwen) 不算 near-complete。论文贡献是方法，不是特定消除率。SciERC 0.93% 和 DocRED 2.55% (Llama) 可在正文中描述为 near-complete，但 title 不宜 overclaim。)\\n\\n**D040 Story 升级方向**: 从 \\\"IE-specific constrained decoding\\\" → \\\"universal ontology-constrained structured generation framework\\\"。WikiEvents Event Extraction 验证跨任务泛化。Continuation masking v2 突破（10-doc: RoV 0%, semantic violations ↓95.8%）初步确认跨任务有效性，全量实验进行中。最终 title 待全量结果后调整。\\n\\n## Core Insight\\nLLM-based IE systems produce systematic ontology constraint violations concentrated in specific relation types. Prompt-level intervention (schema-informed prompting) reduces violations by ~62% but cannot eliminate them — certain relation types retain 25-30% violation rates even with explicit constraint descriptions. OntoCoDec provides **near-complete elimination (DR 15.4%→0.93%, ↓94%) at zero or positive F1 impact** through automatic ontology-to-decoder constraint compilation with two complementary layers.\\n\\n**Phase 2 confirmed (D012 bootstrap CI, v2 fix)**: Grammar+Semantic dual-layer constrained decoding reduces domain/range violations by 94%, eliminates entity-type and relation-vocabulary violations entirely (→0%). F1 impact is **dataset-dependent**:\\n- SciERC: Rel F1 neutral (+0.13pp, p=0.58), Ent F1 neutral (-0.03pp, p=0.53)\\n- DocRED: Rel F1 **significantly improved** (+0.50pp, p<0.001, 95% CI [+0.23, +0.81]); Ent F1 **significantly improved** (+1.23pp, p<0.001, 95% CI [+0.94, +1.55])\\n- Mechanism: grammar 消除 OOV relation names (DocRED RV 29.66%→0.03%) + 非标 entity types (ET 2.48%→0%)。all_set F1 方法下 OOV=FP → fewer FP → higher precision/F1。SciERC baseline RV/ET 已很低，效果不显著。\\n- **Grammar 层是 F1 提升的唯一来源**: grammar_only Ent F1=59.38% ≈ full_s1 59.37% (Δ+0.01pp, p=0.66)。Semantic 层对 F1 无额外贡献，专注 DR reduction。\\n\\n## Core Claims\\n\\n### Claim 1 (Empirical): Violation Landscape\\nLLM-based IE systems violate ontology type constraints at non-trivial rates (15.4% per-triple on SciERC, 18.7% on DocRED). Violations are **not uniformly distributed** — they concentrate on relation types with tight domain/range constraints (Feature-of 33.5%, Compare 42.4%) while loose-constraint relations show near-zero violation (Used-for 0.8%).\\n\\n**Key insight**: Violation rate is driven by **constraint tightness**, not ontology size. A small ontology with tight constraints can produce more violations than a large ontology with loose constraints.\\n\\n**D014 修订**: DR reduction ceiling 由 **tightness × model RV baseline** 共同决定，非 tightness 单因素。Llama DocRED DR↓90.2% vs Qwen DR↓44.7%（同一 ontology τ̄=0.842）。机制：Qwen RV=29.66% >> Llama RV=16.03% → grammar 层将 OOV triples 强制匹配有效关系名 → 揭露大量 latent DR violations → 残余 DR 更高。这是比单一 tightness 更深的 insight。\\n\\n**Evidence**: SciERC (7 relations) 15.4%; DocRED (96 relations) 18.7% — comparable rates despite 14× ontology size difference. Schema-informed prompt on DocRED only achieves DR↓32% (vs SciERC ↓62%), confirming **prompt-level intervention scales poorly with ontology complexity**.\\n\\n### Claim 2 (Empirical): Prompt Insufficiency\\nSchema-informed prompting (explicitly describing domain/range constraints in the prompt) reduces but does not eliminate violations:\\n- Overall: 15.4% → 5.78% (-62.4%), still above 5%\\n- Per-relation: Compare 42.4% → 27.6%, Evaluate-for 24.1% → 29.9% (**worse**)\\n- Prompt intervention is unreliable at the per-relation level — some relations improve, one regresses\\n\\n**Narrative**: This is NOT about \\\"5.78% barely above 5%\\\". The story is: **prompt-level intervention is fundamentally unreliable as a guarantee mechanism**. It works statistically but cannot provide per-instance compliance. Three specific relation types retain >10% violation rates with schema-informed prompts. For safety-critical IE (biomedical, legal, regulatory), statistical reduction is insufficient — guaranteed compliance is required.\\n\\n### Claim 3 (Methodological): Composable Constraint Framework\\nOntoCoDec automatically compiles IE ontology schemas into two composable constraint layers:\\n1. **Grammar layer** (XGrammar): JSON structure + type vocabulary constraints (CFG-expressible)\\n2. **Semantic layer** (TypeConstraintProcessor): Cross-field domain/range constraints via stateful entity registry + dynamic logit masking\\n\\nThe two layers are **complementary with enabling dependency**: grammar ensures every generated relation type is in the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type. Without grammar, the semantic layer encounters unknown relation types and cannot enforce constraints (explaining why semantic_only achieves only ↓24% vs full_s1 ↓94%). This is NOT \\\"synergistic\\\" (mutual amplification) — grammar is a prerequisite for semantic, not vice versa.\\n\\nThe two layers compose via bitwise AND of token masks. Recommended framing: \\\"Grammar and semantic constraints compose via bitwise AND with an enabling dependency: grammar ensures structural validity, enabling semantic constraints to enforce domain/range rules. When constraint tightness creates empty intersection between layers, the system degrades gracefully to grammar-only constraints, maintaining structural validity as a guaranteed floor.\\\"\\n\\n**Graceful degradation + Fallback 频率量化** (D008 + Reviewer 发现):\\nWhen $M_{semantic} \\\\cap M_{grammar} = \\\\emptyset$, the system falls back to grammar-only control.\\n\\n**关键量化数据（Reviewer 从日志挖掘）**:\\n- Llama DocRED full_s1: **32,921 次 fallback / 577 docs = ~57 次/doc**\\n- Llama SciERC full_s1: **5,882 次 fallback / 550 docs = ~10.7 次/doc**\\n- DocRED fallback 频率是 SciERC 的 **5.3×**\\n- Qwen DocRED fallback 率未知（日志当时无 fallback logging，需估算）\\n\\n**这直接解释了 DocRED DR 残余 10.19% vs SciERC 0.93%**: 更多 token 位置退化为 grammar-only → grammar-only 的 DR 已知为 26.17% → 高 fallback = 高残余 DR。\\n\\n**论文建议**: 在 §5 tightness 段报告 fallback 率，定义 \\\"Constraint Coverage\\\" 指标（semantic masking 实际生效的 token 比例）。这把 \\\"10.19% DR 残余\\\" 从弱点变成可量化分析的 finding。Frame as \\\"engineering robustness\\\" in §4; fallback 频率 + tightness 作为 §5 定量分析。\\n\\n**Decidability taxonomy**: Constraints classified by prefix-decidability:\\n- (a) Purely local: entity type ∈ vocabulary (grammar layer)\\n- (b) Prefix-decidable with state: relation argument types compatible with domain/range (semantic layer, requires entity registry)\\n- (c) Truly non-local: forward coreference — out of scope for forward-only decoding\\n\\n### Claim 4 (Methodological): S1 vs S2 Decoding Strategies — Architectural Ablation\\n- S1 (single-pass): Both layers applied throughout generation. **Recommended primary strategy** — simpler, slightly better metrics across the board.\\n- S2 (two-pass): Pass 1 extracts entities (grammar-only), Pass 2 generates relations with input-dependent grammar compiled from Pass 1 entities.\\n\\n**S2 full results (551/551 SciERC)**: DR 0.97% (vs S1 0.93%), CF 8.03% (vs S1 9.9%), R-F1 8.03% (vs S1 8.36%). S2 does NOT solve CF — the 1.87pp reduction is not significant. S2 also slightly worse on DR and F1. **S2 is an architectural variant demonstrating framework flexibility, not a CF solution.** Position in paper as ablation (Section 5 or Appendix), not as a core contribution.\\n\\n⚠️ **Do NOT cite pilot50 DR=0% as S2 evidence** — small-sample artifact; full run shows DR=0.97%. Per-relation S2 DR is worse than S1 on Compare (4.6% vs 2.82%), Part-of (1.25% vs 0%), Used-for (0.12% vs 0%).\\n\\n### Claim 5 (Empirical): Cross-Task Generalization — Event Extraction (D040, NEW)\\n**Status**: ✅ All 3 models × 246 docs complete (v3 with collision fix + exact-match fix)\\n\\nOntoCoDec generalizes beyond Relation Extraction to **Event Extraction** (WikiEvents, Li et al. NAACL 2021), demonstrating that the framework is task-agnostic for any IE task with ontology-defined type constraints.\\n\\n**Cross-task framing (Reviewer 评估 confirmed)**:\\n- **RoV 是 DR 的正确对应物**（不是 RV）：EE 中 per-type violation rate 是 RE 的 3-5×，支持 \\\"more complex ontology → more critical constraint enforcement\\\" claim\\n- **三层级联 Grammar→RoV→AC**（比 RE 的 Grammar→DR 两层更丰富）：grammar 消除 EV，使 semantic layer 可以 enforce role restriction (RoV→0%)，进而暴露 AC violations。这强化 architecture contribution 论证。\\n- **Semantic layer 是 EE 的唯一防线**：grammar 层对 role vocabulary 无能力，只有 semantic layer + continuation masking 能 enforce per-event-type role constraints\\n- **\\\"Practical value\\\" 防线**：Arg F1 ≈ 0% 不削弱 claim，因为 (a) mechanism generalization 是 contribution 不是 SOTA performance，(b) FT composability 已在 RE 中证明 high-F1 场景有效\\n\\n**WikiEvents specifics** (DARPA KAIROS ontology):\\n- 56 event types × 80 argument roles × 27 entity types（含 5 个补充 Contact 子类型 + CRM entity type）\\n- 245 组显式 (event_type, role) → allowed_entity_types 约束\\n- Maps directly to OntoCoDec's semantic layer: argument role type constraints ≡ domain/range constraints\\n- 27 entity types（比 ACE05 的 7 个更丰富）→ constraint space 更大，更能展示 semantic layer 价值\\n- 99.98% 数据满足约束 → 约束定义是真实有效的\\n- Hierarchical event names (e.g., Conflict.Attack.DetonateExplode) → 扁平化为 leaf-node 解决 first-token collision（96.1%→3.9%）\\n\\n**数据集选择理由**（MAVEN/RAMS 排除）：\\n- MAVEN (168 types): 无 argument extraction，不适用\\n- MAVEN-Arg (162 types): FrameNet-based，无 role→entity_type schema 约束\\n- RAMS (139 types): 仅 cardinality 约束，无 entity type binding\\n- ACE05 (33 types): LDC 付费，采购周期来不及\\n- **WikiEvents 是唯一同时满足 \\\"免费 + 有显式 role→entity_type 约束\\\" 的数据集**\\n\\n**Violation 分类** (5 类，从 RE 的 4 类扩展):\\n- ET (Entity Type): entity type 不在 ontology 合法类型列表中\\n- EV (Event Vocabulary): event type 不在 ontology 定义中\\n- RoV (Role Vocabulary): argument role 不在该 event type 定义中\\n- AC (Argument Constraint): argument entity type 不满足 role→entity_type 约束（DR 的自然推广）\\n- CF (Cross-Field): 同一 entity 跨 event 被赋予不同 type\\n\\n**Full results (246 docs, v3 final — collision fix + exact-match fix)**:\\n\\n| Metric | Qwen3-8B uncon. | Qwen3-8B Full S1 | Llama-3.1-8B uncon. | Llama-3.1-8B Full S1 | Mistral-7B uncon. | Mistral-7B Full S1 |\\n|--------|-----------------|-------------------|---------------------|----------------------|-------------------|---------------------|\\n| Parse | 88.6% | 83.7% | 91.9% | 84.1% | 88.6% | 88.6% |\\n| EV | 24.0% | **0%** | 10.5% | **0%** | 37.3% | **0%** |\\n| RoV | 74.9% | **0%** | 88.8% | **0%** | 63.9% | **0%** |\\n| AC | 0.3% | 2.1% | 0.1% | 3.8% | 0% | 1.3% |\\n| CF | 0% | 21.1% | 0% | 17.2% | 0% | 14.9% |\\n| Trigger F1 | 11.8% | 13.4% | 5.7% | 7.5% | 2.4% | 3.9% |\\n| Ent F1 | 0% | 14.1% | 0% | 17.6% | 0% | 11.7% |\\n\\n**Grammar-only ablation (Mistral v3, all 3 models)**:\\n- Grammar eliminates EV→0% but RoV remains 64-77%: grammar CFG cannot constrain 80 argument roles conditioned on event context\\n- AC rises to 8-14% under grammar-only (latent violation surfacing pattern, same as DocRED RE)\\n- Proves semantic layer is essential for EE: two-layer architecture is necessary, not just convenient\\n\\n**Post-hoc filtering comparison (devastating)**:\\n- Qwen: 5,467→23 arguments (99.6% discarded) to reach 0% violation\\n- Llama: 5,053→3 arguments (99.9% discarded)\\n- Mistral: 6,034→0 arguments (100% discarded)\\n- Post-hoc is not viable for EE (contrasts with RE where it's expensive but functional)\\n\\n**BPE collision diagnostic (confirmed 2026-05-18)**:\\n- Qwen (BPE, ~152K vocab): **0 collision groups** — all 27 entity types have unique first tokens\\n- Llama (BPE, ~128K vocab): **0 collision groups** — same\\n- Mistral (SentencePiece, ~32K vocab): **2 collision groups** (SID/SEN/SIDE→'S', BAL/BOD→'B')\\n- **Residual AC narrative**: Mistral AC 1.3% = residual after collision fix (was 16.6%); Qwen/Llama AC 2.1-3.8% = purely model semantic confusion (confuses similar entity types like SID vs SEN), NOT tokenizer collision\\n\\n**关键 findings**:\\n- RoV 是压倒性违规（64-89%），远超 RE 的 RV（1-30%）→ 更强力展示 constraint 需求\\n- EV 显著（10-37%）→ grammar 层直接消除\\n- **Entity F1 从 0% 恢复到 11.7-17.6%**: 不是语义改进，是 format compliance 恢复——grammar enforcement 产生 schema-valid JSON，parser 才能识别 entity mentions\\n- Trigger F1 +1.5 to +1.8pp: elimination of OOV event types counted as FP\\n- CF 15-21% 比 RE 更高（EE argument structure 更复杂），沿用 RE 的 CF tradeoff framing\\n\\n**Story upgrade**: WikiEvents results confirm paper narrative: \\\"universal ontology-constrained structured generation framework applicable to any IE task with formal type constraints\\\". Three evidence lines: (1) EV/RoV→0% across all models, (2) grammar-only ablation proves two-layer necessity, (3) post-hoc filtering is non-viable for EE. This is the key differentiator for conference main vs Findings.\\n\\n**70B scale experiment** (P029-P030, in progress): Qwen3-70B AWQ-INT4 on SciERC + DocRED to demonstrate scale generalization. If successful, adds a 4th model to cross-model evidence, strengthening C5.\\n\\n**Remaining risk**:\\n- CF 15-21% higher than RE → continues CF tradeoff framing\\n- 70B experiment timeline tight (need results by May 20 for paper integration)\\n\\n## Anticipated Reviewer Concerns\\n\\n### C1: \\\"5.78% is barely above 5% — threshold is arbitrary\\\"\\n**Response**: Don't argue about the threshold. Argue about per-relation distribution: Compare (27.6%), Evaluate-for (29.9%), Feature-of (11.3%) have double-digit violation rates with schema-informed prompt. The value proposition is per-relation guaranteed compliance, not overall statistical rate.\\n\\n### C2: \\\"Why not just post-hoc filter?\\\"\\n**Response (D013, 实验结果已出)**:\\n\\nPost-hoc filtering 实验结果：post-hoc F1 > OntoCoDec F1（SciERC 8.63 vs 8.36, DocRED 9.61 vs 8.24）——因 low F1 regime 下移除 FP 大幅提升 precision。\\n\\n**论文 framing（不以 F1 论高低，多维对比）**:\\n1. **Recall 维度（核心论点）**: OntoCoDec recall 上升 (SciERC +0.20pp, DocRED +0.56pp) = 概率质量重分配到合法 token 生效。Post-hoc recall 下降 (SciERC -0.72pp, DocRED -1.06pp) = 正确 triple 被误删。\\n2. **Information coverage**: DocRED post-hoc 丢弃 **48.1%** triples（近半数信息丢失），SciERC 16.8%。OntoCoDec 保留全部 triple slots。\\n3. **Operational**: OntoCoDec 产出即合规、无需后处理、支持流式。Post-hoc 需额外管线、不适用实时场景。\\n4. **Precision trade-off（诚实承认）**: \\\"Post-hoc achieves higher precision by removing a large fraction of triples, many of which are incorrect. This trades information coverage for precision — valid when FP are costly, but inadequate when completeness matters.\\\"\\n\\n数据表：SciERC post-hoc rejection 16.8%, OntoCoDec recall 11.60 vs post-hoc 10.68; DocRED post-hoc rejection 48.1%, OntoCoDec recall 10.02 vs post-hoc 8.40。\\n\\n**Reviewer 补充发现（D013 后）**:\\n5. **ET 残余**：post-hoc 只删 triples 不改 entity list，残余 ET=0.4% (SciERC) / 2.47% (DocRED)。OntoCoDec ET=0%。Post-hoc 无法解决 entity type 违规。\\n6. **127 个被删 TP (DocRED)**：过滤前 TP=1137，过滤后 TP=1010。丢失的 127 个 TP（11.2%）是正确提取但 entity type 违规的 triple。OntoCoDec 通过生成时强制合法 type 保留这些 TP——\\\"prevent vs detect\\\" 核心论据的具体数据。\\n7. **OntoCoDec+post-hoc 组合**（future work idea）：先 constrain 再 filter 残余 DR。低优先级，May 19 前不做。\\n\\n### C3: \\\"Bitwise AND of two masks is not novel\\\"\\n**Response**: The novelty is not the AND operation — it's (a) the automatic compilation from ontology definitions (zero-code schema compliance), (b) the stateful entity registry enabling cross-field constraints during autoregressive generation, (c) the decidability taxonomy providing theoretical guidance, and (d) the systematic violation landscape measurement motivating the approach.\\n\\n### C4: \\\"Evaluate-for violation rate increases with schema-informed prompt\\\"\\n**Response (prior-constraint conflict framework)**: Evaluate-for has 23/36 valid pairs; Method→Task is invalid for Evaluate-for but natural in the LLM's distributional prior (\\\"Method X evaluates for Task Y\\\" is semantically plausible). Schema-informed prompting creates a **prior-constraint conflict**: the model learns to avoid Method→Task for Evaluate-for (reducing count 133→87, -34.6%), but the remaining instances are harder boundary cases where the model's type assignment strategy becomes less stable. This is not just \\\"harder instances\\\" — it's an active interference between prompt-level constraint signals and the model's learned type associations.\\n\\n**This strengthens the paper's claim**: prompt-level intervention is not merely insufficient but potentially **counterproductive** for specific constraint configurations. Decoding-time enforcement avoids this issue entirely — it operates on logits, not on the model's reasoning process, so there is no prior-constraint conflict.\\n\\n### C5: \\\"Only tested on one model (Qwen3-8B)\\\"\\n**Response**: Cross-model validation DONE (D016 bootstrap verified). Llama-3.1-8B 零代码修改：\\n- SciERC: DR 13.34%→0.08% (↓99.4%), R-F1 -0.14pp (p=0.011, negligible), E-F1 NS\\n- DocRED: DR 26.07%→2.55% (↓90.2%), R-F1 +0.29pp (p=0.013, significant), E-F1 -0.64pp (p=0.022, modest decline)\\n- Parse failures: unconstrained 68 vs full_s1 91 (6.8% vs 9.1%)\\n\\n**Cross-model claim 指导（Reviewer 专项评估）**:\\n- ✅ 可声明：\\\"OntoCoDec generalizes across model families without code modification\\\"（程序性事实，铁证）\\n- ❌ 不可声明：\\\"consistently achieves the same reduction rate\\\"（仅 2 模型，不足以量化声明）\\n- **RV↓DR↑ 正交性 finding**: Llama RV baseline 低(16%) 但 DR baseline 高(26%)，反向于 Qwen。证明两层约束解决正交 failure modes——vocabulary compliance ≠ semantic compliance。应作为 §5 cross-model 独立 finding 展开。\\n- **Parse failure 偏差**: checker skip parse failures (不计入 F1)，Llama 68/998=6.8% vs Qwen 12/998=1.2%。偏差方向保守（不利于 constrained），不威胁 claim。但需 footnote 披露 + cross-model 表增加 parse failure rate 行。\\n- **Llama SciERC CF=6.56%**: 比 Qwen 同量级更高，non-local constraint 问题在 Llama 上更突出，limitations 提及。\\n- 等 llama_docred_full_s1 出来后定最终 claim 措辞。\\n\\n### C6: \\\"Constrained decoding degrades generation quality (CRANE, Structure Snowballing)\\\"\\n**Response**: OntoCoDec's semantic constraints are narrower than full grammar constraints — only type tokens are masked, free text is unconstrained. **Bootstrap CI (10000×, D012 Qwen + D016 Llama, all registry-aligned)**:\\n\\n**Qwen3-8B**: SciERC R-F1 +0.13pp (p=0.58, NS), E-F1 -0.03pp (NS). DocRED R-F1 +0.50pp (p<0.001), E-F1 +1.23pp (p<0.001).\\n**Llama-3.1-8B**: SciERC R-F1 -0.14pp (p=0.011, negligible), E-F1 NS. DocRED R-F1 +0.29pp (p=0.013), E-F1 -0.64pp (p=0.022).\\n\\n**Cross-model pattern**: DocRED R-F1 显著提升（两个模型）。E-F1 model-dependent（Qwen +1.23pp, Llama -0.64pp）。\\n- 机制：grammar 消除 OOV relation names + 非标 entity types → all_set 方法下减少 FP → precision 提升。Grammar 是 F1 提升的唯一来源（grammar_only Ent F1=59.38% ≈ full_s1 59.37%, Δ=0.01pp, p=0.66）。Semantic 层对 F1 无额外贡献。\\n- Frame as: \\\"On DocRED, R-F1 gains are significant for both models. Entity F1 impact is model-dependent.\\\"\\n- 不升级为 core claim，但如实报告。\\n\\n### C7: \\\"Your method trades DR violations for CF violations (cross-field consistency)\\\"\\n**Response**: Both S1 and S2 show elevated CF (per-triple rate ~8-10%). This is an inherent limitation of per-relation independent type enforcement. Must be proactively reported as a limitation. Defense:\\n\\n**CF 子类型分析（根因已确认）**：\\n- **EVR（entity-vs-relation type drift）**: 占 CF 的 >90%。同一 entity 在 entity list 和 relation triple 中被赋予不同 type。S1: 245 entities (7.34%), S2: 178 entities (5.54%, -27%)\\n- **Within-rel（同 entity 跨 relation type 不一致）**: S1: 10 (0.36%), S2: 18 (0.72%)\\n- S2 减少 EVR 但增加 within-rel——trade-off 更复杂，不是单纯好/差\\n\\n**Top 冲突模式**: Generic↔OtherScientificTerm (60次), Material↔OtherScientificTerm (28次), Material↔Method (20次)。**这些是 SciERC type system 固有的语义边界模糊区**——同一术语在不同学术语境下确实可以被合理归类为不同 type。CF 在相当程度上是 type system 模糊性的体现，非纯粹的方法缺陷。\\n\\n**论证层次**：\\n1. DR violations = structurally invalid triples（下游系统不可用）→ hard constraint\\n2. CF violations = same entity gets different types across relations → individual triples remain type-valid, only cross-triple consistency broken → soft preference\\n3. CF 的根因是 type system 语义边界模糊 + per-relation 独立 enforcement，非 bug\\n4. Future work: cross-relation global consistency pass (entity-level type consensus before relation-specific enforcement)\\n\\n**机制归因（口径对账确认）**：grammar_only CF=0.08%（与 unconstrained 持平），full_s1 CF=9.90%，full_s2 CF=8.03%。**CF 100% 由 semantic 层引入，grammar 层无贡献。** 这为 \\\"CF 是 semantic type enforcement 的系统性副作用\\\" 提供干净的消融证据。\\n\\n**论文数字口径**：CF rate 用 violation_checker 口径（denominator=total_entities，与 DR/RV/ET 一致）。分析段落额外给 entity-level EVR 率 + 受影响样本比例。注意：analyze_cf 脚本的 EVR/WR 两维度不是独立的（WR⊂EVR），论文中不要作为两个独立维度报告。\\n\\n**Do NOT hide this data.** Proactive disclosure + severity distinction + root cause analysis + type ambiguity evidence + 消融归因 = 最强防御策略。\\n\\n### C8: \\\"Absolute F1 is too low (~8%) — results are not meaningful\\\"\\n**Response**: This is a zero-shot extraction setting (no training data, no fine-tuning). Low F1 is expected — supervised SOTA on SciERC relation F1 is ~40-50%. Our contribution is the constraint enforcement method, not extraction quality. F1 is a control variable verifying constraints don't degrade quality, not an optimization target. Recommended framing: \\\"We evaluate in a zero-shot setting to demonstrate that our constraint enforcement method works without task-specific training. F1 is reported to verify that constraint enforcement does not degrade extraction quality, not as a claim of state-of-the-art performance.\\\"\\n\\n## Paper Structure (Draft — D040 updated)\\n1. Introduction: Ontology constraint violations in LLM-based structured generation + composable framework overview (story: not just RE, general ontology-constrained generation)\\n2. Background: Grammar-constrained decoding (XGrammar) + IE ontology structure\\n3. Violation Landscape Study (Phase 0 empirics — independent contribution)\\n4. OntoCoDec Framework: Compiler + TypeConstraintProcessor + S1/S2 strategies\\n5. Experiments:\\n   - §5.1-5.3: RE experiments (SciERC + DocRED, 3 models, constrained vs unconstrained vs post-hoc vs prompt-based)\\n   - §5.4: **Event Extraction (WikiEvents)** — cross-task generalization (D040)\\n   - §5.5: Ablation + analysis (composability, latency, beam search, etc.)\\n6. Related Work: 5 constraint paradigms (grammar, vocabulary, structural, type-checking, ontology) + event extraction methods\\n7. Conclusion: Framework generality across IE tasks\\n\\n## Claim Calibration (per Reviewer assessment)\\n\\n**Safe to claim (sufficient evidence from Phase 2)**:\\n- \\\"First systematic study of ontology constraint violations in LLM-based IE\\\"\\n- \\\"Violation rate correlates with constraint tightness, not ontology size\\\" (D014: DR reduction ceiling 由 tightness × model RV baseline 共同决定)\\n- \\\"Grammar+semantic constrained decoding eliminates 94% of DR violations at zero F1 cost\\\" ✅ Phase 2 confirmed\\n- \\\"Two-layer architecture provides complementary coverage — grammar enables semantic\\\" ✅ Ablation confirmed\\n- \\\"Prompt-level intervention scales poorly with ontology complexity\\\" ✅ SciERC ↓62% vs DocRED ↓32%\\n\\n**Claim with caution**:\\n- \\\"Near-complete type-valid IE\\\" — S1 0.93%, S2 0.97% residual, not truly 0%. Title updated to \\\"Near-Complete\\\"\\n- \\\"Principled framework applicable to arbitrary IE ontologies\\\" — RE validated on 2 datasets × 2 models; EE (WikiEvents) 10-doc preliminary shows ↓95.8% semantic violations, full results pending\\n- \\\"F1 improvement\\\" — SciERC: not significant (p=0.58), frame as F1-neutral; DocRED: significant (+0.50pp, p<0.001), 可报告但不升级为 core claim，归因于 OOV elimination 而非约束解码本身的提升\\n- \\\"CF reveals type system ambiguity\\\" — 可在 §5.3 作为 analysis finding 展开（Generic↔OtherScientificTerm 等模式有独立 insight 价值），但 §7 必须同时保留 CF 作为 limitation + future work。**两处都要有，缺一不可。** 不能暗示\\\"因为是 type ambiguity 所以 CF 可接受\\\"\\n\\n**Do NOT claim**:\\n- \\\"General infrastructure for IE\\\" — only zero-shot extraction validated\\n- \\\"State-of-the-art\\\" — F1 is control variable, not optimization target (see C8)\\n- \\\"Synergistic effect\\\" — mechanism is enabling dependency, not mutual amplification (see Claim 3)\\n- \\\"S2 solves CF\\\" or \\\"S2 mitigates Structure Snowballing\\\" — data shows S2 ≈ S1 on all metrics; position as architectural variant only\\n- \\\"Pilot50 DR=0%\\\" — small-sample artifact, full S2 has DR=0.97%\\n- \\\"Grammar-first invariant\\\" 作为独立 claim — 证据不足（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。写入 §4 方法论设计原则（1-2 句），不升级为 claim\\n- \\\"Robust dual-layer composition across schema complexities\\\" — 等 DocRED 完成。最终如 fallback ≤5/998，可写经验性陈述，不做泛化 claim\\n\\n## Risk Ranking (ordered by reject probability)\\n\\n1. **CF violation trade-off under-addressed** (MEDIUM-HIGH): S1 9.9%, S2 8.03% — both elevated. **S2 confirmed: does NOT solve CF.** This is the #1 attack surface. Mitigated by proactive disclosure + severity distinction + root cause analysis (C7). Must be reported as explicit limitation with future work direction (global entity-type consensus).\\n2. ~~**Single model limitation**~~ (RESOLVED): Llama-3.1-8B SciERC ✅ (DR↓99.4%) + DocRED ✅ (DR↓90.2%). 2 模型 × 2 数据集全矩阵完成。\\n3. **Novelty perception** (MEDIUM): \\\"PLDI'25 for code → OntoCoDec for IE\\\" attack line. Must argue IE constraint structure differs fundamentally.\\n4. ~~**DocRED Phase 2 weak**~~ (RESOLVED → reframed as D014): Qwen DR↓44.7%, Llama DR↓90.2% — both substantial. Weaker Qwen reduction explained by RV baseline interaction (D014), not method failure.\\n5. ~~**Phase 2 F1 drop**~~ (RESOLVED): F1 confirmed neutral (SciERC) or positive (DocRED, p<0.001). Bootstrap CI D012 confirms. No longer a risk.\\n\\n## Critical Path to EMNLP Submission (May 25)\\n\\n- **May 13-14**: Phase 0 + Phase 1 + Phase 2 SciERC ✅\\n- **May 14**: Phase 2 DocRED 4-way ablation ✅ + Llama SciERC cross-model ✅ + Dream 完成 (3/6)\\n- **May 14-15**: Llama DocRED ✅ + Checker 修正 ✅ + post-hoc ✅ + bootstrap CI ✅ + related work ✅\\n- **May 15-17**: Prompt sensitivity ✅ + WikiEvents pipeline 开发 + continuation v2 突破\\n- **May 17-18**: WikiEvents 3 模型 unconstrained baselines (进行中) + constrained 全量\\n- **May 18-19**: WikiEvents 结果分析 + §5.4 Event Extraction 章节撰写\\n- **May 19-20**: Intro/Abstract/Conclusion 升级（cross-task story）+ 内部稿 → submit_paper_to_review\\n- **May 20-24**: Review 修改 + 最终提交\\n\\n**当前瓶颈**: WikiEvents 全量实验完成是关键路径。3 模型 unconstrained baselines 并行进行中（Qwen ~68/246, Mistral ~31/246, Llama 重启中），constrained 实验随后立即启动。\\n\\n## Status\\n- Phase 0 SciERC: ✅ Complete (minimal + schema-informed)\\n- Phase 0 DocRED: ✅ Complete (minimal 18.7% DR + schema-informed 12.8% DR)\\n- Phase 1 Compiler: ✅ Complete (grammar + semantic layers integrated)\\n- Phase 2 SciERC (5 configs): ✅ Complete (S1 DR↓94% F1-neutral, S2 降级为 ablation)\\n- Phase 2 DocRED (4 configs): ✅ Complete (full_s1 DR↓45%, grammar ET/RV→0%)\\n- Llama SciERC cross-model: ✅ Complete (DR↓99.4%, F1-neutral, 零代码修改)\\n- Llama DocRED cross-model: ✅ Complete (full_s1 DR↓90.2%, unconstrained DR=26.07%)\\n- Checker v2 (D011): ✅ Fixed (ET triple-counting → unique entity dedup)\\n- Bootstrap CI (D012): ✅ Fixed + confirmed (entity filter bug resolved)\\n- Post-hoc baseline (D013): ✅ Complete (multi-dimensional framing)\\n- Related work: ✅ 42 bib entries, 4 additions merged\\n- Dream 6/6 actions: ✅ All complete\\n- CF violation analysis: ✅ Confirmed inherent limitation (S1 9.9% SciERC / 2.57% DocRED / 12.02% Llama DocRED)\\n- D014 tightness revision: ✅ Complete (tightness × RV baseline dual-factor)\\n- Llama bootstrap CI (D016): ✅ Fixed + verified (registry-aligned ≤0.05pp, all p-values in paper)\\n- Paper compilation: ✅ 8 pages正文 + appendix\\n- R5 text fixes (N1/N2/N3/W1-W6): ✅ All complete and verified\\n- Prompt sensitivity analysis: ✅ Complete (3 prompts × 2 modes, DR reduction 94.0-94.6%, σ=0.3pp; appendix written)\\n- Doc length breakdown: ✅ Complete (appendix written)\\n- **WikiEvents Event Extraction (D040)**: 🔄 Continuation v2 突破 (10-doc: RoV 0%, semantic ↓95.8%); 3 模型 unconstrained baselines 进行中; constrained 全量待启动\\n\", \"total_chars\": 26924, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6d0e735-a5f5-4cd9-bdcd-1e22b14d7a50",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "cdcd3576-699d-4e68-b5c7-36cd61ef971b",
  "sourceToolAssistantUUID": "b6d0e735-a5f5-4cd9-bdcd-1e22b14d7a50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-18T17:32:17.576Z_

Now let me read the actual paper and key source files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdcd3576-699d-4e68-b5c7-36cd61ef971b",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS7Wi2oioVKrYCW1w1F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43f94458-08fd-4dbf-8565-a4929566b530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KENvkzz3bSFvss4Nxo392A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11377,
      "cache_read_input_tokens": 19547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11377,
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

_source line 16 · 2026-05-18T17:32:19.601Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WbkbVToGKX8kHQdbdWH8Wv`</summary>

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
  "parentUuid": "43f94458-08fd-4dbf-8565-a4929566b530",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS7Wi2oioVKrYCW1w1F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "072a8886-b8f8-4b3e-a228-518dd651f198",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KENvkzz3bSFvss4Nxo392A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11377,
      "cache_read_input_tokens": 19547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11377,
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

_source line 17 · 2026-05-18T17:32:19.616Z_

<details><summary>↩ Tool result · `toolu_01WbkbVToGKX8kHQdbdWH8Wv`</summary>

```text
artifacts/_project/paper/section5_scierc_draft_4796e8.tex
artifacts/_project/paper/abstract_fd4b26.tex
artifacts/_project/paper/abstract_d3264e.tex
artifacts/_project/paper/section7_conclusion_550cbf.tex
artifacts/dream_reports/dream_20260514T094226/best/paper.tex
artifacts/dream_reports/dream_20260514T094226/median/paper.tex
artifacts/dream_reports/dream_20260514T094226/worst/paper.tex
artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
artifacts/_project/paper/section6_relwork_additions.tex
artifacts/_project/paper/discussion_paragraphs.tex
artifacts/dream_reports/dream_20260514T205155/best/paper.tex
artifacts/dream_reports/dream_20260514T205155/median/paper.tex
artifacts/dream_reports/dream_20260514T205155/worst/paper.tex
artifacts/_project/paper/section6_relwork_outline.tex
artifacts/_project/paper/section7_conclusion.tex
artifacts/dream_reports/dream_20260516T021434/best/paper.tex
artifacts/dream_reports/dream_20260516T021434/median/paper.tex
artifacts/dream_reports/dream_20260516T021434/worst/paper.tex
artifacts/dream_reports/dream_20260516T173022/best/paper.tex
artifacts/dream_reports/dream_20260516T173022/median/paper.tex
artifacts/_project/paper/paper_tables_draft.tex
artifacts/appendix_sampling_table.tex
artifacts/_project/paper/appendix_sampling_table.tex
artifacts/_project/paper/appendix_prompts.tex
artifacts/_project/paper/appendix_related_work.tex
artifacts/_project/paper/section2_background.tex
artifacts/_project/paper/section5_docred_draft_9b84f1.tex
artifacts/_project/paper/appendix_doc_length.tex
artifacts/_project/paper/appendix_prompt_sensitivity.tex
artifacts/_project/paper/section3_method_draft.tex
artifacts/_project/paper/appendix_llama_per_relation.tex
artifacts/_project/paper/section5_crossmodel_draft.tex
artifacts/_project/paper/section5_scierc_draft.tex
artifacts/_project/paper/section4_composition_draft.tex
artifacts/_project/paper/section3_violation_landscape.tex
artifacts/_project/paper/section5_wikievents_draft.tex
artifacts/_project/paper/section7_conclusion_compressed.tex
artifacts/_project/paper/appendix_beam_search.tex
artifacts/_project/paper/p3_case_studies.tex
artifacts/_project/paper/p3_case_studies_861a0d.tex
artifacts/p3_case_studies.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix_case_studies.tex
artifacts/_project/paper/section1_introduction_draft.tex
artifacts/_project/paper/section5_docred_draft.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/section6_related_work.tex
artifacts/dream_reports/dream_20260518T162745/best/paper.tex
artifacts/dream_reports/dream_20260518T162745/median/paper.tex
artifacts/dream_reports/dream_20260518T162745/worst/paper.tex
artifacts/_project/paper/section5_runtime.tex
artifacts/_project/paper/appendix_discussion.tex
artifacts/_project/paper/appendix_reproducibility.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "072a8886-b8f8-4b3e-a228-518dd651f198",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "fbcea55c-73bc-4399-8a4a-2840e4862576",
  "sourceToolAssistantUUID": "072a8886-b8f8-4b3e-a228-518dd651f198",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T17:32:19.895Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UTjZf4c3uStGXsGtRPVGPQ`</summary>

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
  "parentUuid": "fbcea55c-73bc-4399-8a4a-2840e4862576",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS7Wi2oioVKrYCW1w1F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a14d29d-f5fe-43d9-8b43-02711d69db8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KENvkzz3bSFvss4Nxo392A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11377,
      "cache_read_input_tokens": 19547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11377,
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

_source line 19 · 2026-05-18T17:32:19.917Z_

<details><summary>↩ Tool result · `toolu_01UTjZf4c3uStGXsGtRPVGPQ`</summary>

```text
artifacts/dream_reports/dream_20260514T094226/median/references.bib
artifacts/_project/paper/new_citations.bib
artifacts/new_citations.bib
artifacts/_project/paper/relwork_new_entries.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a14d29d-f5fe-43d9-8b43-02711d69db8b",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "30c95558-2110-4392-afdc-31e41ed0e904",
  "sourceToolAssistantUUID": "7a14d29d-f5fe-43d9-8b43-02711d69db8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T17:32:22.990Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q4vUU2QdxwWyP7m8xqSwUX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30c95558-2110-4392-afdc-31e41ed0e904",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS7w7DuiKGDdPiQewLZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbabf6e6-fbf1-4f3a-a15f-360653de72e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015SNJbS3KH83AgWvUXjbDXp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1201,
      "cache_read_input_tokens": 30924,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1201
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 30924,
          "cache_creation_input_tokens": 1201,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1201,
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

_source line 21 · 2026-05-18T17:32:22.999Z_

<details><summary>↩ Tool result · `toolu_01Q4vUU2QdxwWyP7m8xqSwUX`</summary>

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	\usepackage{pifont}
18	
19	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
20	
21	\author{Anonymous ACL submission}
22	
23	\begin{document}
24	\maketitle
25	
26	% === Abstract ===
27	\input{abstract}
28	
29	% === §1 Introduction ===
30	\input{section1_introduction_draft}
31	
32	% === §2 Background ===
33	\input{section2_background}
34	
35	% === §3 Method ===
36	\input{section3_method_draft}
37	
38	% === §4 Constraint Composition ===
39	\section{Constraint Composition}
40	\label{sec:composition}
41	\input{section4_composition_draft}
42	
43	% === §5 Experiments ===
44	\section{Experiments}
45	\label{sec:experiments}
46	
47	\subsection{Violation Landscape}
48	\input{section3_violation_landscape}
49	
50	\input{section5_scierc_draft}
51	\input{section5_docred_draft}
52	\input{section5_crossmodel_draft}
53	\input{section5_wikievents_draft}
54	\input{section5_runtime}
55	
56	% === §6 Related Work ===
57	\input{section6_related_work}
58	
59	% === §7 Discussion and Conclusion ===
60	\section{Discussion and Conclusion}
61	\label{sec:discussion}
62	\input{section7_conclusion_compressed}
63	
64	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
65	\clearpage
66	\section*{Limitations}
67	
68	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
69	CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13.85\,pp). CF$\leftrightarrow$DR thus represents a fundamental trade-off in composable constraint systems rather than an independently resolvable limitation (Appendix~\ref{app:cf-dr-tradeoff}).
70	Entity F1 impact is model-dependent ($+$1.22\,pp for Qwen vs.\ $-$0.64\,pp for Llama on DocRED), partially confounded by increased parse failures under constraints (Llama: 9.1\% vs.\ 6.8\%).
71	Zero-shot results cover three 7--8B-class models, where relation F1 remains around 4--8\% compared to $\sim$45\% for fine-tuned systems.
72	Composability with fine-tuned models is validated on both SciERC and DocRED with Qwen3-8B and Llama-3.1-8B (DR\,$\leq$\,0.20\%, R-F1 change within $\pm$0.6\,pp), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\% on SciERC) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
73	The continuation masking approach (\S\ref{sec:dynamic-masking}) handles multi-token type names and prefix-shared types on the ontologies tested (6--27 entity types); scalability to ontologies with hundreds of entity types has not been validated, and the prefix-map size may grow substantially.
74	Global entity-level type consensus during decoding offers the most direct path to resolving CF violations.
75	All models tested are 7--8B-parameter class; scaling behavior to larger (70B+) or smaller models has not been verified, and the dual-factor pattern's predictive scope may differ at other scales.
76	CF type inconsistencies may propagate to downstream tasks that consume extracted triples (e.g., knowledge graph construction, question answering); the impact of such propagation has not been evaluated.
77	Residual DR under fine-tuning (36 violations across all fine-tuned settings, both models and both datasets) decomposes into entity type errors (39\%), schema coverage gaps (33\%), and model generation errors correctly caught by constraints (28\%); Llama DocRED alone accounts for 33 of 36 residual violations (92\%), reflecting weaker entity typing (Appendix~\ref{app:residual-dr-analysis}).
78	Schema coverage gaps (one-third of residual violations) are irreducible by decoding-time constraints alone (training-set frequency coverage); complementary approaches such as global type consensus or post-hoc correction may address this limitation.
79	All main experiments use greedy decoding; our evaluation of beam search on the full SciERC test set (551 documents) and a DocRED subset across three models confirms compatibility (Appendices~\ref{app:sampling},~\ref{app:beam-search}), but comprehensive evaluation across all decoding configurations remains future work.
80	Validation with fine-tuned models, larger scales, and non-English ontologies remains to be explored.
81	
82	% === Ethics Statement ===
83	\section*{Ethics Statement}
84	
85	This work uses publicly available benchmark datasets (SciERC and DocRED) with no personally identifiable information.
86	No human subjects were involved in the experiments.
87	The constrained decoding method operates on model outputs and does not introduce new privacy or safety risks beyond those inherent in the base language models.
88	Code and data will be released upon acceptance.
89	
90	% === Bibliography ===
91	\bibliography{relwork_new_entries}
92	
93	% === Appendix ===
94	\appendix
95	
96	\input{appendix_prompts}
97	\input{appendix_related_work}
98	\input{appendix_discussion}
99	\input{appendix_llama_per_relation}
100	\input{appendix_sampling_table}
101	\input{appendix_beam_search}
102	\input{appendix_reproducibility}
103	\input{appendix_doc_length}
104	\input{appendix_prompt_sensitivity}
105	\input{appendix_case_studies}
106	
107	\end{document}
108	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbabf6e6-fbf1-4f3a-a15f-360653de72e3",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "eca96217-7b5e-40b2-9152-d39d7d1f86cc",
  "sourceToolAssistantUUID": "dbabf6e6-fbf1-4f3a-a15f-360653de72e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-18T17:32:25.269Z_

Let me now read the key paper sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eca96217-7b5e-40b2-9152-d39d7d1f86cc",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS89LBfWhhwobxALRL6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94e640cb-6ffe-4fbd-ab05-40edf3d82084",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2UCxmDAB2EVc69fPcYyJL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1952,
      "cache_read_input_tokens": 32125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1952,
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

_source line 23 · 2026-05-18T17:32:25.891Z_

<details open><summary>🔧 Tool call — Read · `toolu_0196WLEePwwPSQZmQHHQGzct`</summary>

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
  "parentUuid": "94e640cb-6ffe-4fbd-ab05-40edf3d82084",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS89LBfWhhwobxALRL6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7acc19d-528a-42c7-a276-856d217b4e74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2UCxmDAB2EVc69fPcYyJL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1952,
      "cache_read_input_tokens": 32125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1952,
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

_source line 24 · 2026-05-18T17:32:25.895Z_

<details><summary>↩ Tool result · `toolu_0196WLEePwwPSQZmQHHQGzct`</summary>

```text
1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) ontology schemas into two composable token-level decoding constraints that provide formal guarantees during autoregressive generation:
3	(1)~a \emph{grammar layer} (XGrammar context-free grammar) guaranteeing JSON structural validity and entity/relation vocabulary membership (virtually eliminating entity type and relation vocabulary violations); and
4	(2)~a \emph{semantic layer} guaranteeing per-triple domain/range type compliance via a stateful entity registry and dynamic logit masking.
5	%
6	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations: 15.37\% on SciERC (7 relations) and 18.46\% on DocRED (96 relations), comparable rates governed by \emph{constraint tightness} rather than ontology scale.
7	\textsc{OntoCoDec} reduces DR by 42--99\% across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) with no significant F1 cost (DocRED: $+$0.50\,pp, $p{<}0.001$; \S\ref{sec:cross-model}).
8	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_docred
9	Composed with Low-Rank Adaptation (LoRA) fine-tuning, DR reaches $\leq$\,0.09\% (SciERC) and 0.20\% (DocRED) with relation F1 within $\pm$0.6\,pp, a near-lossless composition.
10	With beam search ($k{=}4$), the full stack eliminates all four violation types under fine-tuned beam decoding (SciERC, both Qwen3-8B and Llama-3.1-8B) while preserving extraction quality (R-F1 44.23 and 46.11, respectively); in zero-shot beam decoding, DR reaches 0\% for calibrated models on both RE datasets.
11	The framework generalizes to event extraction (WikiEvents: 56 event types, 80 roles) without architectural modification and eliminates event-vocabulary and role-vocabulary violations ($\to$ 0\%); where unconstrained outputs are severely off-schema, format compliance additionally enables entity extraction (Entity F1: 0\%\,$\to$\,12--18\%).
12	Per-slot enforcement introduces a cross-field consistency trade-off (up to 12\% in zero-shot, resolved to $\leq$1.2\% by fine-tuning).
13	OntoCoDec demonstrates that ontology schemas can be compiled into decoding-time guarantees, bridging the gap between flexible generative extraction and the type-safety requirements of downstream knowledge systems.
14	\end{abstract}
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7acc19d-528a-42c7-a276-856d217b4e74",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "3eb0ccde-eed1-4b4b-9e26-dc27813e5de7",
  "sourceToolAssistantUUID": "d7acc19d-528a-42c7-a276-856d217b4e74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T17:32:26.680Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BQBJguac63yWTRaAo5L7qr`</summary>

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
  "parentUuid": "3eb0ccde-eed1-4b4b-9e26-dc27813e5de7",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS89LBfWhhwobxALRL6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51ebbfa0-e8c1-463f-9ac4-e760d5f0f02a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2UCxmDAB2EVc69fPcYyJL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1952,
      "cache_read_input_tokens": 32125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1952,
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

_source line 26 · 2026-05-18T17:32:26.685Z_

<details><summary>↩ Tool result · `toolu_01BQBJguac63yWTRaAo5L7qr`</summary>

```text
1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	For downstream systems in safety-critical domains (biomedical entity extraction, legal document analysis), statistical reduction of violations is insufficient; type-safety guarantees are needed to prevent error propagation into knowledge graphs and decision-support pipelines.
11	
12	Existing approaches leave a fundamental gap.
13	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
14	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
15	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs, making it impractical.
16	OntoCoDec preserves recall by enforcing constraints during generation rather than discarding non-compliant outputs.
17	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
18	
19	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE ontology into two composable layers of decoding-time constraints.
20	Our two-layer architecture reflects the observation that structural violations (malformed output, unknown types) and semantic violations (type-constraint breaches) require fundamentally different enforcement mechanisms.
21	The \emph{grammar layer} enforces JSON well-formedness and vocabulary validity via XGrammar.
22	The \emph{semantic layer} maintains a stateful entity registry during generation: as entities are decoded, the registry records type assignments; when relation arguments are generated, dynamic logit masking restricts output to types compatible with the relation's domain/range specification.
23	The layers compose via bitwise AND with an \emph{enabling dependency}: the grammar layer guarantees vocabulary membership, so the semantic layer can look up domain/range rules.
24	Unlike type-constrained code generation where types are statically declared, IE requires a dynamic entity registry built during generation, with constraint targets that depend on the co-occurring relation.
25	On SciERC, OntoCoDec reduces DR violations from 15.37\% to 0.93\% ($\downarrow$94\%) while remaining F1-neutral ($+$0.13\,pp).
26	
27	Our contributions:
28	\begin{enumerate}
29	    \item The first systematic study of ontological constraint violations in LLM-based IE (spanning per-relation tightness analysis, dual-factor characterization, and post-hoc baseline comparison), violation rates are driven by constraint tightness rather than ontology size, and prompt-level intervention is per-relation unreliable.
30	    \item OntoCoDec, a two-layer compiled constraint framework that is the first to enforce pair-based domain/range type constraints via compiled stateful logit masks during autoregressive IE.
31	    Unlike type-constrained decoding in code generation, where output types are statically determined by the grammar, IE requires stateful cross-field constraints because entity type validity depends on the co-occurring relation within each triple.
32	    \item Empirical validation on 3 models $\times$ 3 datasets (2 RE + 1 EE): DR $\downarrow$76--99\% on SciERC and $\downarrow$42--90\% on DocRED with significant R-F1 gains (Qwen $p{<}0.001$, Llama $p{=}0.013$); cross-task generalization to WikiEvents (vocabulary violations $\to$\,0\%; Entity F1 0\%\,$\to$\,12--18\%); composability with LoRA (DR\,$\leq$\,0.20\% at $<$0.6\,pp F1 cost).
33	    \item Characterization of the CF$\leftrightarrow$DR trade-off inherent in per-slot enforcement (resolved by fine-tuning to CF\,$\leq$\,1.2\%); beam search ($k{=}4$) as an orthogonal path that eliminates all four violation types under fine-tuned beam decoding (SciERC, both Qwen3-8B and Llama-3.1-8B) and reduces DR to 0\% for calibrated models in zero-shot settings.
34	\end{enumerate}
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51ebbfa0-e8c1-463f-9ac4-e760d5f0f02a",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "dde8d031-fe52-47a3-8468-73a08564b475",
  "sourceToolAssistantUUID": "51ebbfa0-e8c1-463f-9ac4-e760d5f0f02a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T17:32:27.153Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UNq1R1FqKSAw9Y4iFsE4E2`</summary>

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
  "parentUuid": "dde8d031-fe52-47a3-8468-73a08564b475",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS89LBfWhhwobxALRL6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6699e653-0416-486e-9ba5-1ee3250ebdc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2UCxmDAB2EVc69fPcYyJL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1952,
      "cache_read_input_tokens": 32125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1952,
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

_source line 28 · 2026-05-18T17:32:27.158Z_

<details><summary>↩ Tool result · `toolu_01UNq1R1FqKSAw9Y4iFsE4E2`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar} (benchmarked in JSONSchemaBench~\cite{jsonschemabench2025}), Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, DOMINO~\cite{beurer-kellner2024domino}, SynCode~\cite{ugare2024syncode}, and ASAp~\cite{park2024grammar} guarantee format validity but cannot enforce cross-field semantic constraints such as domain/range rules.
6	
7	\paragraph{Type-Constrained Generation for IE and Code.}
8	Synchromesh~\cite{synchromesh_iclr2022}, PICARD~\cite{scholak2021picard}, and \citet{pldi2025_type_constrained_codegen} enforce type constraints in code generation; OntoCoDec migrates this to IE.
9	GCD~\cite{geng2023gcd}, GoLLIE~\cite{sainz2024gollie}, and GUIDEX~\cite{guidex2025} constrain \emph{which tokens} appear but not \emph{which type combinations} are valid per relation.
10	DORE~\cite{vukovic2024dore} uses generate-then-select with confidence thresholds; GenIE~\cite{josifoski2022genie} constrains entities via a trie without relation-specific type enforcement; EnriCo~\cite{zaratiana2024enrico} applies ASP constraints with task-specific manually authored rules.
11	BoostCD~\cite{boostcd2025} combines constrained and unconstrained IE outputs via a trained boosting model; OntoCoDec is training-free and provides per-instance type guarantees rather than statistical improvement.
12	Training-based methods~\cite{paolini2021tanl,cabot2021rebel,lu2022uie,knowcoder_acl2024,li2023codeie,schema_rl2025} provide only soft guidance; post-hoc approaches~\cite{khorshidi2025odke,spires_2024,ontologx_2025,slot2025} validate or restructure outputs after generation rather than preventing violations.
13	
14	\paragraph{Quality Impact.}
15	Recent work shows constrained decoding can degrade reasoning and distort output distributions~\cite{banerjee2025crane,grammar_aligned_2024,schall2025hiddencost,formattax2026}; DCCD~\cite{dccd2026} proposes unconstrained-then-constrained correction as an alternative.
16	However, extraction tasks are robust to constraints~\cite{tam2024letmespeak}: OntoCoDec's narrow type-slot constraints yield neutral F1 on SciERC and significant improvement on DocRED ($+$0.50\,pp, $p{<}0.001$); post-hoc filtering is impractical for EE (99.6\% argument loss; extended survey in Appendix~\ref{app:related_work}).
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6699e653-0416-486e-9ba5-1ee3250ebdc1",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "b77c980d-cece-479d-af07-43538a4b91ef",
  "sourceToolAssistantUUID": "6699e653-0416-486e-9ba5-1ee3250ebdc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T17:32:27.664Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GqbdxRbksndieKwVHXknvh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b77c980d-cece-479d-af07-43538a4b91ef",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS89LBfWhhwobxALRL6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc5b556e-3803-4489-bdc6-85adc699eb05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2UCxmDAB2EVc69fPcYyJL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1952,
      "cache_read_input_tokens": 32125,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1952
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 360,
          "cache_read_input_tokens": 32125,
          "cache_creation_input_tokens": 1952,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1952,
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

_source line 30 · 2026-05-18T17:32:27.974Z_

<details><summary>↩ Tool result · `toolu_01GqbdxRbksndieKwVHXknvh`</summary>

```text
1	% ============================================================
2	% Merged authoritative BibTeX references (9 entries)
3	% Merged 2026-05-14 from relwork_new_entries.bib + new_references.bib
4	% ============================================================
5	
6	% Confirmed via: Semantic Scholar, arXiv:2201.11227, OpenReview
7	% Venue: ICLR 2022 (cite key corrected from synchromesh_neurips2022)
8	@inproceedings{synchromesh_iclr2022,
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
108	% ============================================================
109	% New entries added 2026-05-14 for §6 related work expansion
110	% ============================================================
111	
112	% Confirmed via: ACL Anthology 2021.emnlp-main.779, arXiv:2109.05093, GitHub ServiceNow/picard
113	@inproceedings{scholak2021picard,
114	  title     = {{PICARD}: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models},
115	  author    = {Scholak, Torsten and Schucher, Nathan and Bahdanau, Dzmitry},
116	  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},
117	  year      = {2021},
118	  url       = {https://aclanthology.org/2021.emnlp-main.779/}
119	}
120	
121	% Confirmed via: arXiv:2509.19057, ResearchGate, OpenReview gcG8dmAUNh
122	@article{olasunkanmi2025relate,
123	  title   = {{RELATE}: Relation Extraction in Biomedical Abstracts with {LLMs} and Ontology Constraints},
124	  author  = {Olasunkanmi, Olawumi and Satusky, Mathew and Yi, Hong and Bizon, Chris and Lee, Harlin and Ahalt, Stanley},
125	  journal = {arXiv preprint arXiv:2509.19057},
126	  year    = {2025},
127	  url     = {https://arxiv.org/abs/2509.19057}
128	}
129	
130	% Confirmed via: arXiv:2602.03439, University of Cambridge / The World Avatar project
131	@article{zhou2026ontologytools,
132	  title   = {Ontology-to-tools compilation for executable semantic constraint enforcement in {LLM} agents},
133	  author  = {Zhou, Xiaochi and Bulter, Patrick and Yang, Changxuan and Rihm, Simon D. and Angkanaporn, Thitikarn and Akroyd, Jethro and Mosbach, Sebastian and Kraft, Markus},
134	  journal = {arXiv preprint arXiv:2602.03439},
135	  year    = {2026},
136	  url     = {https://arxiv.org/abs/2602.03439}
137	}
138	
139	% Confirmed via: IOS Press ECAI 2020 FAIA vol.325, arXiv:1909.07755, GitHub lavis-nlp/spert
140	@inproceedings{eberts2020spert,
141	  title     = {Span-based Joint Entity and Relation Extraction with Transformer Pre-training},
142	  author    = {Eberts, Markus and Ulges, Adrian},
143	  booktitle = {Proceedings of the 24th European Conference on Artificial Intelligence ({ECAI} 2020)},
144	  series    = {Frontiers in Artificial Intelligence and Applications},
145	  volume    = {325},
146	  pages     = {2006--2013},
147	  year      = {2020},
148	  doi       = {10.3233/FAIA200321}
149	}
150	
151	% Confirmed via: ACL Anthology 2021.emnlp-main.17, arXiv:2108.12202
152	% NOTE: venue is EMNLP 2021 (NOT AAAI 2021)
153	@inproceedings{yan2021pfn,
154	  title     = {A Partition Filter Network for Joint Entity and Relation Extraction},
155	  author    = {Yan, Zhiheng and Zhang, Chong and Fu, Jinlan and Zhang, Qi and Wei, Zhongyu},
156	  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing},
157	  pages     = {185--197},
158	  year      = {2021},
159	  url       = {https://aclanthology.org/2021.emnlp-main.17/}
160	}
161	
162	% Confirmed via: ACL Anthology 2021.naacl-main.5, GitHub princeton-nlp/PURE
163	@inproceedings{zhong2021frustratingly,
164	  title     = {A Frustratingly Easy Approach for Entity and Relation Extraction},
165	  author    = {Zhong, Zexuan and Chen, Danqi},
166	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
167	  pages     = {50--61},
168	  year      = {2021},
169	  address   = {Online},
170	  publisher = {Association for Computational Linguistics},
171	  url       = {https://aclanthology.org/2021.naacl-main.5}
172	}
173	
174	% Confirmed via: ACL Anthology 2022.acl-long.337, GitHub thunlp/PL-Marker
175	@inproceedings{ye2022packed,
176	  title     = {Packed Levitated Marker for Entity and Relation Extraction},
177	  author    = {Ye, Deming and Lin, Yankai and Li, Peng and Sun, Maosong},
178	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
179	  pages     = {4904--4917},
180	  year      = {2022},
181	  address   = {Dublin, Ireland},
182	  publisher = {Association for Computational Linguistics},
183	  url       = {https://aclanthology.org/2022.acl-long.337}
184	}
185	
186	% Confirmed via: arXiv:2604.06066 (previously PENDING AUDIT — now verified)
187	@article{zhou2026snowballing,
188	  title   = {From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in {LLM} Reflection},
189	  author  = {Zhou, Hongxu},
190	  journal = {arXiv preprint arXiv:2604.06066},
191	  year    = {2026},
192	  url     = {https://arxiv.org/abs/2604.06066}
193	}
194	
195	% ============================================================
196	% Batch 1: Constrained decoding + IE foundations (10 entries)
197	% ============================================================
198	
199	% Confirmed via: arXiv 2411.15100, MLSys 2025 proceedings
200	@inproceedings{dong2025xgrammar,
201	  title     = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},
202	  author    = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},
203	  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},
204	  year      = {2025},
205	  url       = {https://arxiv.org/abs/2411.15100}
206	}
207	
208	% Confirmed via: arXiv 2307.09702
209	@article{willard2023outlines,
210	  title   = {Efficient Guided Generation for Large Language Models},
211	  author  = {Willard, Brandon T. and Louf, R{\'e}mi},
212	  journal = {arXiv preprint arXiv:2307.09702},
213	  year    = {2023},
214	  url     = {https://arxiv.org/abs/2307.09702}
215	}
216	
217	% Confirmed via: ACM DL 10.1145/3591300, PLDI 2023
218	@inproceedings{beurer-kellner2023lmql,
219	  title     = {Prompting Is Programming: A Query Language for Large Language Models},
220	  author    = {Beurer-Kellner, Luca and Fischer, Marc and Vechev, Martin},
221	  booktitle = {Proceedings of the ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI)},
222	  year      = {2023},
223	  url       = {https://doi.org/10.1145/3591300}
224	}
225	
226	% Confirmed via: PMLR v235, ICML 2024
227	@inproceedings{beurer-kellner2024domino,
228	  title     = {Guiding {LLMs} The Right Way: Fast, Non-Invasive Constrained Generation},
229	  author    = {Beurer-Kellner, Luca and Fischer, Marc and Vechev, Martin},
230	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
231	  pages     = {3658--3673},
232	  year      = {2024},
233	  series    = {PMLR},
234	  volume    = {235},
235	  url       = {https://proceedings.mlr.press/v235/beurer-kellner24a.html}
236	}
237	
238	% Confirmed via: NeurIPS 2024 proceedings, OpenReview
239	@inproceedings{park2024grammar,
240	  title     = {Grammar-Aligned Decoding},
241	  author    = {Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadia and D'Antoni, Loris},
242	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
243	  year      = {2024},
244	  url       = {https://arxiv.org/abs/2405.21047}
245	}
246	
247	% Confirmed via: OpenReview, ICLR 2021
248	@inproceedings{decao2021genre,
249	  title     = {Autoregressive Entity Retrieval},
250	  author    = {De Cao, Nicola and Izacard, Gautier and Riedel, Sebastian and Petroni, Fabio},
251	  booktitle = {International Conference on Learning Representations (ICLR)},
252	  year      = {2021},
253	  url       = {https://openreview.net/forum?id=5k8F6UU39V}
254	}
255	
256	% Confirmed via: ACL Anthology 2022.naacl-main.342
257	@inproceedings{josifoski2022genie,
258	  title     = {{GenIE}: Generative Information Extraction},
259	  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},
260	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
261	  pages     = {4626--4643},
262	  year      = {2022},
263	  url       = {https://aclanthology.org/2022.naacl-main.342/}
264	}
265	
266	% Confirmed via: ACL Anthology 2023.emnlp-main.674
267	@inproceedings{geng2023gcd,
268	  title     = {Grammar-Constrained Decoding for Structured {NLP} Tasks without Finetuning},
269	  author    = {Geng, Saibo and Josifoski, Martin and Peyrard, Maxime and West, Robert},
270	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
271	  year      = {2023},
272	  url       = {https://aclanthology.org/2023.emnlp-main.674/}
273	}
274	
275	% Confirmed via: ACL Anthology 2021.naacl-main.339
276	@inproceedings{lu2021neurologic,
277	  title     = {{NeuroLogic} Decoding: (Un)supervised Neural Text Generation with Predicate Logic Constraints},
278	  author    = {Lu, Ximing and West, Peter and Zellers, Rowan and Le Bras, Ronan and Bhagavatula, Chandra and Choi, Yejin},
279	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
280	  pages     = {4288--4299},
281	  year      = {2021},
282	  url       = {https://aclanthology.org/2021.naacl-main.339/}
283	}
284	
285	% Confirmed via: ACL Anthology 2022.acl-long.395
286	@inproceedings{lu2022uie,
287	  title     = {Unified Structure Generation for Universal Information Extraction},
288	  author    = {Lu, Yaojie and Liu, Qing and Dai, Dai and Xiao, Xinyan and Lin, Hongyu and Han, Xianpei and Sun, Le and Wu, Hua},
289	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL)},
290	  pages     = {5755--5772},
291	  year      = {2022},
292	  url       = {https://aclanthology.org/2022.acl-long.395/}
293	}
294	
295	% ============================================================
296	% Batch 2: 10 entries added 2026-05-14
297	% ============================================================
298	
299	% Confirmed via: ICLR 2024 proceedings, OpenReview Y3wpuxd7u9, arXiv:2310.03668
300	@inproceedings{sainz2024gollie,
301	  title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction Modeling},
302	  author    = {Sainz, Oscar and Garc{\'\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},
303	  booktitle = {The Twelfth International Conference on Learning Representations},
304	  year      = {2024},
305	  url       = {https://openreview.net/forum?id=Y3wpuxd7u9}
306	}
307	
308	% Confirmed via: ACL Anthology 2023.acl-long.855, arXiv:2305.05711
309	@inproceedings{li2023codeie,
310	  title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
311	  author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
312	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
313	  pages     = {15339--15353},
314	  year      = {2023},
315	  address   = {Toronto, Canada},
316	  url       = {https://aclanthology.org/2023.acl-long.855/}
317	}
318	
319	% Confirmed via: ACL Anthology 2024.emnlp-main.419, arXiv:2405.05008, GitHub THU-KEG/ADELIE
320	@inproceedings{qi2024adelie,
321	  title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},
322	  author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},
323	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
324	  year      = {2024},
325	  address   = {Miami, Florida, USA},
326	  url       = {https://aclanthology.org/2024.emnlp-main.419/}
327	}
328	
329	% Confirmed via: arXiv:2404.12493, GitHub urchade/EnriCo
330	% NOTE: arXiv preprint; no conference publication found
331	@article{zaratiana2024enrico,
332	  title   = {{EnriCo}: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction},
333	  author  = {Zaratiana, Urchade and Tomeh, Nadi and Dauxais, Yann and Holat, Pierre and Charnois, Thierry},
334	  journal = {arXiv preprint arXiv:2404.12493},
335	  year    = {2024},
336	  url     = {https://arxiv.org/abs/2404.12493}
337	}
338	
339	% Confirmed via: arXiv:2509.04696, Apple ML Research machinelearning.apple.com/research/odke
340	% NOTE: cite key uses "odke"; actual paper title is "ODKE+"
341	@article{khorshidi2025odke,
342	  title   = {{ODKE+}: Ontology-Guided Open-Domain Knowledge Extraction with {LLMs}},
343	  author  = {Khorshidi, Samira and Nikfarjam, Azadeh and Shankar, Suprita and Sang, Yisi and Govind, Yash and Jang, Hyun and Kasgari, Ali and McClimans, Alexis and Soliman, Mohamed and Konda, Vishnu and Fakhry, Ahmed and Qi, Xiaoguang},
344	  journal = {arXiv preprint arXiv:2509.04696},
345	  year    = {2025},
346	  url     = {https://arxiv.org/abs/2509.04696}
347	}
348	
349	% Confirmed via: ACL Anthology 2023.findings-eacl.95
350	@inproceedings{upadhyay2023openie,
351	  title     = {Open Information Extraction with Entity Focused Constraints},
352	  author    = {Upadhyay, Prajna and Balalau, Oana and Manolescu, Ioana},
353	  booktitle = {Findings of the Association for Computational Linguistics: {EACL} 2023},
354	  year      = {2023},
355	  url       = {https://aclanthology.org/2023.findings-eacl.95/}
356	}
357	
358	% Confirmed via: ACL Anthology 2025.genaik-1.10, GenAIK Workshop at COLING 2025
359	@inproceedings{regino2025kgcurator,
360	  title     = {Can {LLMs} be Knowledge Graph Curators for Validating Triple Insertions?},
361	  author    = {Regino, Andr{\'e} Gomes and dos Reis, Julio Cesar},
362	  booktitle = {Proceedings of the Workshop on Generative {AI} and Knowledge Graphs ({GenAIK})},
363	  pages     = {87--99},
364	  year      = {2025},
365	  address   = {Abu Dhabi, UAE},
366	  url       = {https://aclanthology.org/2025.genaik-1.10/}
367	}
368	
369	% Confirmed via: ACL Anthology 2024.emnlp-industry.91, arXiv:2408.02442
370	@inproceedings{tam2024letmespeak,
371	  title     = {Let Me Speak Freely? {A} Study on the Impact of Format Restrictions on Performance of Large Language Models},
372	  author    = {Tam, Zhi Rui and Wu, Cheng-Kuang and Tsai, Yi-Lin and Lin, Chieh-Yen and Lee, Hung-yi and Chen, Yun-Nung},
373	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track},
374	  pages     = {1218--1236},
375	  year      = {2024},
376	  address   = {Miami, Florida, US},
377	  url       = {https://aclanthology.org/2024.emnlp-industry.91/}
378	}
379	
380	% Confirmed via: PMLR v267/banerjee25a, ICML 2025, arXiv:2502.09061
381	@inproceedings{banerjee2025crane,
382	  title     = {{CRANE}: Reasoning with Constrained {LLM} Generation},
383	  author    = {Banerjee, Debangshu and Suresh, Tarun and Ugare, Shubham and Misailovic, Sasa and Singh, Gagandeep},
384	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
385	  pages     = {2836--2857},
386	  year      = {2025},
387	  url       = {https://proceedings.mlr.press/v267/banerjee25a.html}
388	}
389	
390	% Confirmed via: ACL Anthology 2025.ranlp-1.124
391	@inproceedings{schall2025hiddencost,
392	  title     = {The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance},
393	  author    = {Schall, Maximilian and de Melo, Gerard},
394	  booktitle = {Proceedings of the 15th International Conference on Recent Advances in Natural Language Processing ({RANLP} 2025)},
395	  year      = {2025},
396	  address   = {Varna, Bulgaria},
397	  url       = {https://aclanthology.org/2025.ranlp-1.124/}
398	}
399	
400	% ============================================================
401	% D015 reviewer-requested references (5 entries)
402	% ============================================================
403	
404	% Confirmed via: GitHub guidance-ai/guidance, Microsoft Research project page
405	@misc{guidance2023,
406	  title        = {Guidance: A Guidance Language for Controlling Large Language Models},
407	  author       = {Lundberg, Scott and Ribeiro, Marco Tulio},
408	  year         = {2023},
409	  url          = {https://github.com/guidance-ai/guidance},
410	  note         = {Microsoft Research}
411	}
412	
413	% Confirmed via: OpenReview US-TP-xnXI, arXiv:2101.05779, Amazon Science
414	@inproceedings{paolini2021tanl,
415	  title     = {Structured Prediction as Translation between Augmented Natural Languages},
416	  author    = {Paolini, Giovanni and Athiwaratkun, Ben and Krone, Jason and Ma, Jie and Achille, Alessandro and Anubhai, Rishita and dos Santos, Cicero Nogueira and Xiang, Bing and Soatto, Stefano},
417	  booktitle = {International Conference on Learning Representations},
418	  year      = {2021},
419	  url       = {https://openreview.net/forum?id=US-TP-xnXI}
420	}
421	
422	% Confirmed via: ACL Anthology 2021.findings-emnlp.204, GitHub Babelscape/rebel
423	@inproceedings{cabot2021rebel,
424	  title     = {{REBEL}: Relation Extraction By End-to-end Language Generation},
425	  author    = {Huguet Cabot, Pere-Llu{\'\i}s and Navigli, Roberto},
426	  booktitle = {Findings of the Association for Computational Linguistics: {EMNLP} 2021},
427	  pages     = {2370--2381},
428	  year      = {2021},
429	  url       = {https://aclanthology.org/2021.findings-emnlp.204/}
430	}
431	
432	% Confirmed via: IJCAI 2016 Proceedings/16/Papers/421, GitHub thunlp/TKRL
433	@inproceedings{xie2016tkrl,
434	  title     = {Representation Learning of Knowledge Graphs with Hierarchical Types},
435	  author    = {Xie, Ruobing and Liu, Zhiyuan and Sun, Maosong},
436	  booktitle = {Proceedings of the 25th International Joint Conference on Artificial Intelligence ({IJCAI})},
437	  pages     = {2965--2971},
438	  year      = {2016},
439	  url       = {https://www.ijcai.org/Proceedings/16/Papers/421.pdf}
440	}
441	
442	% ============================================================
443	% Batch 3: New entries added 2026-05-16 (3 entries, Director-requested)
444	% ============================================================
445	
446	% Confirmed via: arXiv:2403.01632, OpenReview HiUZtgAPoH, Illinois Experts page
447	% NOTE: Director specified ICML 2024 — verify volume/pages
448	@inproceedings{ugare2024syncode,
449	  title     = {{SynCode}: {LLM} Generation with Grammar Augmentation},
450	  author    = {Ugare, Shubham and Suresh, Tarun and Kang, Hangoo and Misailovic, Sasa and Singh, Gagandeep},
451	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
452	  year      = {2024},
453	  series    = {PMLR},
454	  volume    = {235},
455	  url       = {https://arxiv.org/abs/2403.01632}
456	}
457	
458	% Confirmed via: OpenReview ac93gRzxxV, ICLR 2025 poster page, arXiv:2410.07295
459	@inproceedings{ugare2025itergen,
460	  title     = {{IterGen}: Iterative Semantic-aware Structured {LLM} Generation with Backtracking},
461	  author    = {Ugare, Shubham and Suresh, Tarun and Banerjee, Debangshu and Misailovic, Sasa and Singh, Gagandeep},
462	  booktitle = {The Thirteenth International Conference on Learning Representations},
463	  year      = {2025},
464	  url       = {https://openreview.net/forum?id=ac93gRzxxV}
465	}
466	
467	% Confirmed via: ACL Anthology 2025.emnlp-main.926, arXiv:2506.14901, EPFL dlab
468	@inproceedings{boostcd2025,
469	  title     = {Combining Constrained and Unconstrained Decoding via Boosting: {BoostCD} and Its Application to Information Extraction},
470	  author    = {Sakota, Marija and Geng, Saibo and Josifoski, Martin and West, Robert},
471	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
472	  year      = {2025},
473	  url       = {https://aclanthology.org/2025.emnlp-main.926/}
474	}
475	
476	% ============================================================
477	% Dataset & model references (5 entries)
478	% ============================================================
479	
480	% Confirmed via: ACL Anthology D18-1360, arXiv:1808.09602
481	@inproceedings{luan2018scierc,
482	  title     = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
483	  author    = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
484	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
485	  pages     = {3219--3232},
486	  year      = {2018},
487	  address   = {Brussels, Belgium},
488	  url       = {https://aclanthology.org/D18-1360/}
489	}
490	
491	% Confirmed via: ACL Anthology P19-1074, arXiv:1906.06127
492	@inproceedings{yao2019docred,
493	  title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},
494	  author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},
495	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
496	  pages     = {764--777},
497	  year      = {2019},
498	  address   = {Florence, Italy},
499	  url       = {https://aclanthology.org/P19-1074/}
500	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc5b556e-3803-4489-bdc6-85adc699eb05",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "5a5f3a95-e3bc-4cfa-9ef4-a26fd01ad68d",
  "sourceToolAssistantUUID": "fc5b556e-3803-4489-bdc6-85adc699eb05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T17:32:32.556Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MfAyKjE261uYop86shaxEn`</summary>

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
  "parentUuid": "5a5f3a95-e3bc-4cfa-9ef4-a26fd01ad68d",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS8WcrLAckNPzyozhxy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b559b438-293c-4cec-af09-6c8eb3f7969f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GpkBxNEk5B9SnD5EHDS4iW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13456,
      "cache_read_input_tokens": 34077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13456,
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

_source line 32 · 2026-05-18T17:32:32.567Z_

<details><summary>↩ Tool result · `toolu_01MfAyKjE261uYop86shaxEn`</summary>

```text
1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity (well-formed JSON with ontology-vocabulary membership), while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}
16	\label{sec:formulation}
17	
18	\paragraph{IE as structured generation.}
19	Given an input text $x$, a language model generates a structured JSON output $y$:
20	%
21	\begin{equation}\label{eq:output-schema}
22	\resizebox{.88\columnwidth}{!}{$\displaystyle
23	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
24	$}
25	\end{equation}
26	%
27	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
28	The output JSON Schema (\S\ref{sec:grammar}) enforces a fixed field ordering (head $\to$ tail $\to$ relation $\to$ head\_type $\to$ tail\_type) via deterministic grammar compilation.
29	This ordering ensures that the relation type $r_j$ is known before entity type fields are generated, which enables domain and range lookups in sequential masking (\S\ref{sec:dynamic-masking}).
30	
31	\paragraph{Ontology compliance.}
32	Using the ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defined in \S\ref{sec:background}, we write $\operatorname{dom}(r) = \{\tau^h : \exists \tau^t,\, (\tau^h, \tau^t) \in \sigma(r)\}$ for domain-valid head types and $\operatorname{range}(r, \tau^h) = \{\tau^t : (\tau^h, \tau^t) \in \sigma(r)\}$ for the conditional range given head type $\tau^h$.
33	Our enforcement target is \emph{pair-based} type validity: $(\tau^h, \tau^t) \in \sigma(r)$ for every triple.
34	The decoder enforces this sequentially: $\tau^h \in \operatorname{dom}(r)$ at head position, then $\tau^t \in \operatorname{range}(r, \tau^h)$ at tail position. This is equivalent to the full pair check and strictly stronger than independent domain/range enforcement, because most relations have non-rectangular type signatures ($\sigma(r) \subsetneq \operatorname{dom}(r) \times \operatorname{range}(r)$ for all 7 SciERC and 73/96 DocRED relations; see \S\ref{sec:rectangularity}).\footnote{An independent check ($\tau^h \in \operatorname{dom}(r) \wedge \tau^t \in \operatorname{range}(r)$) would over-permit type pairs by $1.50\times$ on SciERC and $1.58\times$ on DocRED, corresponding to 33.3\% and 36.8\% spurious type pairs.}
35	Our goal is maximizing $P(y \mid x)$ subject to all triples being type-valid and $y$ being well-formed JSON conforming to Eq.~\eqref{eq:output-schema}.
36	
37	
38	\subsection{Grammar Layer}
39	\label{sec:grammar}
40	
41	The grammar layer compiles $\mathcal{O}$ into a context-free grammar (CFG) enforced at every decoding step via logit masking.
42	This compilation proceeds in two stages.
43	
44	\paragraph{Schema-to-grammar compilation.}
45	We generate a JSON Schema encoding the structure in Eq.~\eqref{eq:output-schema} with \texttt{enum} constraints restricting entity types to $\mathcal{E}$ and relation types to $\mathcal{R}$.
46	This schema is compiled into an EBNF grammar via XGrammar~\cite{dong2025xgrammar}, producing a pushdown automaton tracking JSON structure and enum membership.
47	
48	\paragraph{Logit masking.}
49	At step $t$, the automaton computes grammar-valid tokens $G(t) \subseteq V$; all others receive logits $-\infty$.
50	This simultaneously enforces: (i)~structural validity (well-formed JSON), (ii)~relation vocabulary membership ($r_j \in \mathcal{R}$), and (iii)~entity type membership ($\tau_i \in \mathcal{E}$).
51	Domain/range constraints are \emph{not} enforced, as they depend on entity types within each triple; this gap is filled by the semantic layer.
52	
53	\paragraph{Empirical profile.}
54	On SciERC, grammar constraints eliminate relation vocabulary violations entirely (1.39\%\,$\to$\,0\%) and entity type violations entirely (0.40\%\,$\to$\,0\%), with no measurable F1 impact.
55	Domain/range violations remain effectively unchanged (15.37\%\,$\to$\,14.84\%). This confirms that grammar constraints enforce structural but not semantic validity.
56	
57	
58	\subsection{Semantic Layer}
59	\label{sec:semantic}
60	
61	The semantic layer enforces domain/range constraints through a stateful logits processor maintaining an entity registry during generation.
62	
63	\subsubsection{Entity Registry}
64	\label{sec:entity-registry}
65	
66	As the model generates the entity list, the semantic layer builds a registry $\mathcal{D}: \text{name} \to \text{type}$ mapping each entity to its declared type.
67	This registry is populated incrementally: when the model completes an entry $\{n_i, \tau_i\}$, the pair $(n_i, \tau_i)$ is added to $\mathcal{D}$.
68	The registry is then consulted during relation generation to look up the declared types of head and tail entities.
69	
70	\subsubsection{Position Detection}
71	\label{sec:position-detection}
72	
73	At each step $t$, the processor determines which field is currently being generated by pattern-matching on the decoded prefix.
74	We define five field positions (\textsc{EntityType}, \textsc{RelationType}, \textsc{HeadType}, \textsc{TailType}, and \textsc{FreeText}), identified via JSON key patterns (e.g., tokens following \texttt{"head\_type":} indicate \textsc{HeadType}).
75	Semantic masks activate only at type-bearing positions (\textsc{HeadType}, \textsc{TailType}).
76	
77	\subsubsection{Dynamic Masking}
78	\label{sec:dynamic-masking}
79	
80	At type-bearing positions, the processor computes a semantic mask $S(t) \subseteq V$ restricting generation to type-valid tokens.
81	
82	\paragraph{Head type masking.}
83	At a \textsc{HeadType} position, the processor considers the entity registry $\mathcal{D}$ and the current relation type $r_j$ (if already generated).
84	If $h_j \in \mathcal{D}$ and $\mathcal{D}[h_j] \in \operatorname{dom}(r_j)$, the mask allows only that registered type: $S(t) = \{\operatorname{tok}(\mathcal{D}[h_j])\}$, ensuring consistency with both the entity list and domain constraints.
85	Otherwise, if $r_j$ is known, the mask falls back to all domain-valid types: $S(t) = \{\operatorname{tok}(\tau) : \tau \in \operatorname{dom}(r_j)\}$.
86	If $r_j$ is unavailable, no semantic mask is applied.
87	
88	\paragraph{Tail type masking.}
89	At a \textsc{TailType} position, the head type $\tau^h_j$ is already determined from the decoded prefix.
90	The processor computes $\operatorname{range}(r_j, \tau^h_j)$, the valid tail types conditioned on the generated head type (\S\ref{sec:formulation}).
91	If $t_j \in \mathcal{D}$, the mask further restricts to the registered type when it belongs to this set.
92	This sequential check ($\tau^h \in \operatorname{dom}(r)$, then $\tau^t \in \operatorname{range}(r, \tau^h)$) achieves exact pair-based enforcement, strictly tighter than an independent range check $\tau^t \in \operatorname{range}(r)$.
93	
94	\paragraph{Tokenizer-agnostic type masking.}
95	Each type name $\tau \in \mathcal{E}$ must be mapped to token IDs for logit masking.
96	A naive approach maps $\tau$ to its first subword token and sets disallowed IDs to $-\infty$, but this fails in two scenarios:
97	(1)~SentencePiece tokenizers produce context-dependent tokenizations where the same string yields different token IDs depending on preceding context (e.g., after a JSON delimiter), and
98	(2)~ontologies with prefix-shared type names (e.g., \textsc{Sen}, \textsc{Sid}, \textsc{Side} in WikiEvents) map to the same first token, making single-token disambiguation impossible.
99	We resolve both with \emph{continuation masking}: at compile time, we scan the full vocabulary to build a prefix map identifying, for each type name, all tokens whose decoded text is a valid prefix.
100	At decode time, the semantic mask allows any token that continues a partially-generated type name, disambiguating over multiple steps.
101	This is tokenizer-agnostic, handling byte-level BPE (Qwen, Llama) and SentencePiece (Mistral) without tokenizer-specific logic.
102	
103	\subsubsection{Grammar-Semantic Interaction}
104	\label{sec:interaction}
105	
106	The final mask is the conjunction of $G(t)$ and $S(t)$, permitting only tokens satisfying both layers (formalized in \S\ref{sec:composition}).
107	This embodies an \emph{enabling dependency}: semantic lookup requires relation types to be valid members of $\mathcal{R}$, guaranteed only by the grammar layer.
108	Without grammar enforcement, the model may generate out-of-vocabulary relation types for which no $\sigma(r)$ rules exist.
109	Empirically, semantic-only constraints reduce DR by only 24\% (15.37\%\,$\to$\,11.65\%) while failing to eliminate vocabulary violations; the full combination achieves 94\% DR reduction.
110	When $S(t) \cap G(t) = \emptyset$ (the semantic layer would mask out all grammar-valid tokens), the system falls back to grammar-only control, preserving structural validity at the cost of a potential type violation.
111	This \emph{grammar-first invariant} reflects a deliberate priority ordering: structural integrity is a hard constraint, while type violations are soft errors detectable by downstream validation.
112	
113	
114	\subsection{Decoding Strategies}
115	\label{sec:strategies}
116	
117	\paragraph{S1: Single-pass decoding.}
118	Both constraint layers are active throughout a single generation pass.
119	The entity registry is populated as entities are generated and immediately available for relation-level type checking.
120	This is the simpler and recommended strategy. It achieves strong constraint enforcement with higher relation F1 than the two-pass alternative.
121	
122	\paragraph{S2: Two-pass decoding.}\label{sec:s2}
123	The first pass generates only entities under grammar constraints; the extracted entities compile an input-dependent grammar that additionally constrains head and tail names to match declared entities.
124	The second pass generates relations under this tighter grammar plus semantic constraints.
125	Detailed comparison is provided in the appendix.
126	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b559b438-293c-4cec-af09-6c8eb3f7969f",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "662447e5-4139-4391-9a96-5574147d3b74",
  "sourceToolAssistantUUID": "b559b438-293c-4cec-af09-6c8eb3f7969f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T17:32:33.435Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y1QBFYDnqGrzsj6JuBPxB4`</summary>

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
  "parentUuid": "662447e5-4139-4391-9a96-5574147d3b74",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS8WcrLAckNPzyozhxy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86b81f2b-1d79-4b63-bf51-241eaf38b288",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GpkBxNEk5B9SnD5EHDS4iW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13456,
      "cache_read_input_tokens": 34077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13456,
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

_source line 34 · 2026-05-18T17:32:33.442Z_

<details><summary>↩ Tool result · `toolu_01Y1QBFYDnqGrzsj6JuBPxB4`</summary>

```text
1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	
18	\paragraph{Constraint Tightness.}
19	We define the tightness of relation $r$ as:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \kappa(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{E}|^2},
23	\end{equation}
24	%
25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{E}$ the entity type vocabulary.
26	The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor pattern (tightness $\times$ baseline model violation rate) is consistent with the cross-dataset results: for calibrated models (Qwen, Llama), SciERC ($\bar{\kappa}{=}0.333$, 24 valid pairs/relation) achieves 94--99\% DR reduction, while DocRED ($\bar{\kappa}{=}0.842$, 5.68 pairs) achieves 45--90\%; including Mistral (whose high baseline ET shifts the regime), the full range across all three models is 42--99\% (\S\ref{sec:cross-model}; quantitative analysis in Appendix~\ref{app:dual-factor}).
29	This pattern is observed across four model-dataset configurations; additional settings would be needed to establish statistical robustness.
30	
31	\paragraph{Non-Rectangularity and Sequential Masking.}
32	\label{sec:rectangularity}
33	% Data source: artifacts/rebuttal/w2_rectangularity_report.md
34	Sequential masking ($\tau^h \in \operatorname{dom}(r)$, then $\tau^t \in \operatorname{range}(r, \tau^h)$) is necessary because real ontology type signatures are non-rectangular: 0/7 SciERC and only 23/96 DocRED relations satisfy $\sigma(r) = \operatorname{dom}(r) \times \operatorname{range}(r)$.
35	Independent enforcement would admit 33--37\% spurious type pairs; on SciERC, 100\% of residual DR under S1 are pairs that pass independent checks but violate $\sigma(r)$.
36	
37	\paragraph{Decidability Taxonomy.}
38	We classify constraints by when sufficient information becomes available: \emph{local} (current token only, e.g., vocabulary membership; grammar layer), \emph{prefix-decidable} (decoded prefix, e.g., domain/range; semantic layer), and \emph{non-local} (forward coreference; outside single-pass decoding, partially addressed by S2, \S\ref{sec:s2}).
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86b81f2b-1d79-4b63-bf51-241eaf38b288",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "fb912187-19ff-4dea-b1c3-efc706f1278a",
  "sourceToolAssistantUUID": "86b81f2b-1d79-4b63-bf51-241eaf38b288",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T17:32:33.588Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JKuvFP3DXVTYpZLoQd8xeG`</summary>

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
  "parentUuid": "fb912187-19ff-4dea-b1c3-efc706f1278a",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS8WcrLAckNPzyozhxy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8d535f2-7f09-452a-ab74-669bc6bb6de1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GpkBxNEk5B9SnD5EHDS4iW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13456,
      "cache_read_input_tokens": 34077,
      "output_tokens": 255,
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
          "output_tokens": 255,
          "cache_read_input_tokens": 34077,
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

_source line 36 · 2026-05-18T17:32:33.593Z_

<details><summary>↩ Tool result · `toolu_01JKuvFP3DXVTYpZLoQd8xeG`</summary>

```text
1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{E}|^2$: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''), which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}, i.e., well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}, i.e., $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}: at the point where a type token is generated, all information needed (relation type, entity registry) is available in the decoded prefix.
22	This requires that each entity type name maps to a unique first subword token (\S\ref{sec:semantic}, Implementation), a design assumption verified for all tested configurations.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8d535f2-7f09-452a-ab74-669bc6bb6de1",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "d2343ef3-cc23-4a8a-bf7b-ab5cc846f056",
  "sourceToolAssistantUUID": "d8d535f2-7f09-452a-ab74-669bc6bb6de1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-18T17:32:36.450Z_

Now let me read the experiment sections and the remaining key content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2343ef3-cc23-4a8a-bf7b-ab5cc846f056",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS8wAj6d64uhK9gse1T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ce078c3-794b-4c00-bbe7-6a3f706f8dd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8kbJmfUBLb9A6QtEriPsg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5676,
      "cache_read_input_tokens": 47533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5676,
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

_source line 38 · 2026-05-18T17:32:38.338Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WpG7iFod67E4e8mqFjAwoQ`</summary>

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
  "parentUuid": "6ce078c3-794b-4c00-bbe7-6a3f706f8dd7",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS8wAj6d64uhK9gse1T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7aec035a-db7c-41f7-a0bc-44f57d03d986",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8kbJmfUBLb9A6QtEriPsg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5676,
      "cache_read_input_tokens": 47533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5676,
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

_source line 39 · 2026-05-18T17:32:38.343Z_

<details><summary>↩ Tool result · `toolu_01WpG7iFod67E4e8mqFjAwoQ`</summary>

```text
1	% §5.1 Experimental Setup and Violation Landscape (compressed)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	\paragraph{Setup.}
8	We evaluate on two IE benchmarks:
9	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs/relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, avg.\ 5.68 valid pairs).
10	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}.
11	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
12	Violation rates are computed over successfully parsed documents; including failures as zero-violation instances adjusts rates by at most 0.23\,pp.
13	
14	\paragraph{Baseline violations and motivation.}
15	DR violations affect 15.37\% of triples on SciERC and 18.46\% on DocRED, comparable rates despite 14$\times$ ontology size difference; severity is driven by \emph{constraint tightness} rather than scale.
16	Per-relation rates vary by over 40\,pp (Appendix~\ref{app:per-relation-landscape}), correlating with tightness $\kappa(r)$.
17	RV on DocRED reaches 29.66\%: large vocabularies exceed prompt-based reproduction capacity.
18	Schema-informed prompting reduces DR by 62\% on SciERC but only 30\% on DocRED and is per-relation unreliable (DR for \textsc{Evaluate-for} \emph{increases} by 5.8\,pp). These limitations motivate decoding-time enforcement.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7aec035a-db7c-41f7-a0bc-44f57d03d986",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "2d735829-af40-46a2-b36e-dd5ebeeaeb7d",
  "sourceToolAssistantUUID": "7aec035a-db7c-41f7-a0bc-44f57d03d986",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-18T17:32:39.281Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ST7QLq1EVdZmMZDGFpPGAy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d735829-af40-46a2-b36e-dd5ebeeaeb7d",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS8wAj6d64uhK9gse1T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7d0972c-1065-44db-8ad4-4c5d43822f77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8kbJmfUBLb9A6QtEriPsg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5676,
      "cache_read_input_tokens": 47533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5676,
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

_source line 41 · 2026-05-18T17:32:39.287Z_

<details><summary>↩ Tool result · `toolu_01ST7QLq1EVdZmMZDGFpPGAy`</summary>

```text
1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	Table~\ref{tab:cross-model} replicates full S1 with Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3 under identical prompts and evaluation.
11	Mistral serves as a third zero-shot verification point; composability evaluation (\S\ref{sec:composability}) uses LoRA, available only for Qwen and Llama.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\setlength{\tabcolsep}{3.4pt}
17	\resizebox{\columnwidth}{!}{%
18	\begin{tabular}{@{}ll rrrr r@{}}
19	\toprule
20	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
21	& \textbf{R-F1} \\
22	\cmidrule(lr){3-6} \cmidrule(l){7-7}
23	\textbf{Dataset} & \textbf{Model}
24	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
25	  & $\uparrow$ \\
26	\midrule
27	\multirow{6}{*}{SciERC}
28	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
29	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
30	  \cmidrule(l){2-7}
31	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
32	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
33	  \cmidrule(l){2-7}
34	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
35	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
36	\midrule
37	\multirow{6}{*}{DocRED}
38	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
39	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
40	  \cmidrule(l){2-7}
41	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
42	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
43	  \cmidrule(l){2-7}
44	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
45	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
46	\bottomrule
47	\end{tabular}}%
48	\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
49	Parse failures: Llama DocRED 9.1\%; others $\leq$1.1\%.
50	$^\dagger$Mistral: poor zero-shot calibration causes pervasive type inconsistencies.
51	F1 $\times$100.}
52	\label{tab:cross-model}
53	\end{table}
54	
55	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_scierc, mistral_docred
56	\paragraph{Results.}
57	RV and ET are eliminated ($\leq$0.03\%) for all models on both datasets.
58	DR drops 76--99\% on SciERC and 42--90\% on DocRED; R-F1 improves in five of six settings (DocRED: Qwen $+$0.50\,pp, $p{<}0.001$; Llama $+$0.29\,pp, $p{=}0.013$).
59	Cross-model DR asymmetry reflects baseline RV: Llama's lower RV (16.03\% vs.\ 29.66\%) limits latent violation surfacing, yielding 2.55\% residual DR vs.\ 10.21\%.
60	CF direction depends on baseline calibration: S1 introduces CF for calibrated models (up to 12.02\%; \S\ref{sec:discussion}), while reducing CF for poorly-calibrated Mistral (56.87\%\,$\to$\,1.27\%).
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7d0972c-1065-44db-8ad4-4c5d43822f77",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "dadd1707-e2d7-406f-8a10-c47b613dc9ba",
  "sourceToolAssistantUUID": "a7d0972c-1065-44db-8ad4-4c5d43822f77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-18T17:32:39.643Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LPaBuhv59s8KEvtS9gJXXx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dadd1707-e2d7-406f-8a10-c47b613dc9ba",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS8wAj6d64uhK9gse1T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "747e7891-a3d5-4abe-9c55-22546e597308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8kbJmfUBLb9A6QtEriPsg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5676,
      "cache_read_input_tokens": 47533,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5676
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 274,
          "cache_read_input_tokens": 47533,
          "cache_creation_input_tokens": 5676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5676,
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

_source line 43 · 2026-05-18T17:32:39.655Z_

<details><summary>↩ Tool result · `toolu_01LPaBuhv59s8KEvtS9gJXXx`</summary>

```text
1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Cross-Task Validation: Event Extraction}
8	\label{sec:wikievents}
9	
10	To test generality beyond RE, we apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document} (56 event types, 80 argument roles, 27 entity types, 245 role$\to$type constraints; Appendix~\ref{app:wikievents}).
11	The framework requires no modification: grammar compiles event/role vocabularies into a CFG; the semantic layer enforces role-conditioned type constraints via the same registry.
12	Violations extend to Event Vocabulary (EV), Role Vocabulary (RoV), and Argument Constraint (AC, analogous to DR).
13	
14	% ──────────────────────────────────────────
15	%  Table: WikiEvents three-model comparison (v3 final)
16	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
17	% ──────────────────────────────────────────
18	\begin{table}[t]
19	\centering
20	\small
21	\setlength{\tabcolsep}{2.8pt}
22	\resizebox{\columnwidth}{!}{%
23	\begin{tabular}{@{}ll rrrr rr@{}}
24	\toprule
25	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
26	& \multicolumn{2}{c}{\textbf{F1}} \\
27	\cmidrule(lr){3-6} \cmidrule(l){7-8}
28	\textbf{Model} & \textbf{Mode}
29	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
30	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
31	\midrule
32	\multirow{3}{*}{Qwen3-8B}
33	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
34	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
35	  & Full S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
36	\midrule
37	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
38	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
39	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
40	  & Full S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
41	\midrule
42	\multirow{3}{*}{\shortstack[l]{Mistral\\7B}}
43	  & Unconstr.\ & 37.3 & 63.9 & 0 & 0 & 2.4 & 0 \\
44	  & Grammar    & \textbf{0} & 64.0 & 13.8 & --- & --- & --- \\
45	  & Full S1    & \textbf{0} & \textbf{0} & 1.3 & 14.9 & 3.9 & 11.7 \\
46	\bottomrule
47	\end{tabular}}%
48	\caption{WikiEvents EE results (246 documents, zero-shot).
49	Violation rates over parsed documents.
50	---: not applicable (grammar-only has no semantic-layer metrics).
51	F1 $\times$ 100.}
52	\label{tab:wikievents}
53	\end{table}
54	
55	\paragraph{Results.}
56	Unconstrained generation produces extreme vocabulary violations (EV+RoV exceeding 85\% combined; Table~\ref{tab:wikievents}), and all models yield entity F1\,=\,0 because the parser cannot identify well-formed mentions in off-schema output.
57	Full S1 eliminates EV and RoV across all three models ($\to$\,0\%), which validates tokenizer-agnostic design across byte-level BPE (Qwen, Llama) and SentencePiece (Mistral).
58	Grammar-only ablation isolates each layer: grammar eliminates EV ($\to$\,0\%) but leaves RoV at 64--77\% because the CFG cannot constrain 80 argument roles conditioned on event context; AC rises from near-zero to 8--14\%, the same latent-violation surfacing pattern observed in DocRED (\S\ref{sec:docred-results}).
59	Full S1 then drives RoV to 0\%, which demonstrates layer complementarity.
60	Residual AC (1.3--3.8\%) traces to confusion between semantically similar entity types (e.g., SID vs.\ SEN) where grammar-first fallback permits the incorrect type; CF rises to 15--21\%, consistent with the per-slot enforcement trade-off in RE.
61	
62	Post-hoc filtering is impractical for EE: it retains only 23/5{,}467 arguments for Qwen (99.6\% discarded), 3/5{,}053 for Llama, and 0/6{,}034 for Mistral, because unconstrained models generate generic role names rather than ontology-specific ones.
63	Unlike RE, where constraints are F1-neutral, EE shows measurable gains: entity F1 rises from 0\% to 11.7--17.6\% and trigger F1 increases by $+$1.5--1.8\,pp, because grammar enforcement produces schema-valid JSON that the parser can process.
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "747e7891-a3d5-4abe-9c55-22546e597308",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "a3f6afc7-d48e-46d2-8cbc-f0d370ccba23",
  "sourceToolAssistantUUID": "747e7891-a3d5-4abe-9c55-22546e597308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-18T17:32:42.610Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C4cn6VP1Vnknu4dDQAWcC3`</summary>

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
  "parentUuid": "a3f6afc7-d48e-46d2-8cbc-f0d370ccba23",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS9NzzANmD4ZNmBpDy7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64aa0e9b-69dc-4970-91ec-3818738149ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AiyARgEZs3Dzciwb8xn4Dt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4299,
      "cache_read_input_tokens": 53209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4299,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 45 · 2026-05-18T17:32:42.622Z_

<details><summary>↩ Tool result · `toolu_01C4cn6VP1Vnknu4dDQAWcC3`</summary>

```text
1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrr rr@{}}
21	\toprule
22	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-6} \cmidrule(l){7-8}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Best per column in \textbf{bold} (CF excluded).
60	F1 $\times$100. Bootstrap: 10{,}000 iterations.}
61	\label{tab:scierc-ablation}
62	\end{table}
63	
64	% ──────────────────────────────────────────
65	%  (a) Core result
66	% ──────────────────────────────────────────
67	\paragraph{Core result: DR elimination at zero F1 cost.}
68	The full two-layer constraint configuration (S1) reduces domain/range
69	violations from 15.37\% to 0.93\%, a 94\% relative reduction,
70	% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
71	while relation F1 moves from 8.23 to 8.36 ($+$0.13\,pp; bootstrap 95\% CI [$-$0.24, $+$0.58]\,pp, $p = 0.58$, 10{,}000 iterations).
72	% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
73	% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824
74	The difference is not statistically significant ($p = 0.58$); constraint enforcement is F1-neutral on this dataset.
75	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains from aggressive violation removal (SciERC: 8.63 vs.\ 8.36; DocRED: 9.61 vs.\ 8.23), but at the cost of discarding up to 48\% of predictions including true positives (Appendix~\ref{app:posthoc-extended}); OntoCoDec preserves recall by enforcing constraints during generation.
76	Per-relation DR drops to $\leq$2.82\% on all types, reaching 0\% on four of seven (Appendix~\ref{app:per-relation-landscape}).
77	However, constraint enforcement elevates CF from 0.08\% to 9.90\% (\S\ref{sec:discussion}).
78	
79	% ──────────────────────────────────────────
80	%  (b) Grammar layer
81	% ──────────────────────────────────────────
82	\paragraph{Grammar layer: cost-free structural guarantees.}
83	Grammar-only constraints eliminate RV (1.39\%\,$\to$\,0\%) and ET (0.40\%\,$\to$\,0\%) with no F1 impact, while DR remains unchanged (15.37\%\,$\to$\,14.84\%).
84	This configuration represents the capability ceiling of grammar-based constrained decoding~\cite{geng2023gcd}, which enforces JSON structure and vocabulary membership but cannot reason about cross-field semantic constraints.
85	% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823
86	
87	% ──────────────────────────────────────────
88	%  (c) Enabling dependency
89	% ──────────────────────────────────────────
90	\paragraph{Enabling dependency.}
91	Semantic-only reduces DR by only 24\% (11.65\%) and cannot eliminate RV (1.51\%) or ET (0.40\%), which establishes the \emph{enabling dependency}: without grammar-enforced vocabulary, the semantic layer encounters OOV types with no domain/range rules.
92	Adding the grammar layer yields a further 92\% reduction (11.65\%\,$\to$\,0.93\%).
93	
94	% ──────────────────────────────────────────
95	%  (d) S1 vs S2
96	% ──────────────────────────────────────────
97	\paragraph{S1 vs.\ S2.}
98	S2 achieves comparable DR (0.97\%) but lower R-F1 (8.03 vs.\ 8.36) with fewer triples (1{,}644 vs.\ 1{,}729) and does not resolve the CF trade-off (8.03\% vs.\ 9.90\%); we adopt S1 as the primary configuration.
99	% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644
100	
101	% ──────────────────────────────────────────
102	%  (e) Composability with Fine-Tuning
103	%  exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
104	% ──────────────────────────────────────────
105	\paragraph{Composability with fine-tuning.}
106	\label{sec:composability}
107	Table~\ref{tab:composability} tests composability across zero-shot vs.\ LoRA $\times$ unconstrained vs.\ S1 for Qwen3-8B and Llama-3.1-8B.
108	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
109	%          w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,
110	%          llama_scierc_unconstrained, llama_scierc_full_s1,
111	%          w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval
112	
113	Fine-tuning alone reduces DR to 1--2\% but leaves residual violations on tight-constraint relations (Table~\ref{tab:composability}).
114	Adding S1 eliminates these: Qwen DR 1.95\%\,$\to$\,0\% ($-$0.09\,pp R-F1), Llama DR 1.11\%\,$\to$\,0.09\% ($+$0.02\,pp).
115	On DocRED, the same pattern holds: Qwen DR 0.76\%\,$\to$\,0.01\% ($-$0.30\,pp), Llama DR 0.49\%\,$\to$\,0.20\% ($+$0.51\,pp).
116	% w5_qwen_docred_lora_constrained_eval: DR=0.01%, R-F1=40.56; w5_llama_docred_lora_constrained_eval: DR=0.20%, R-F1=44.23
117	
118	Across all settings, fine-tuned + S1 yields DR\,$\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp, which supports orthogonal composability.
119	Post-fine-tuning, grammar is a no-op; the semantic layer alone reduces DR by 39--72\% (Appendix~\ref{app:ft-ablation}).
120	CF interference drops from $+$9.82\,pp (zero-shot) to $+$1.18\,pp (fine-tuned), tracing to \textsc{Generic}$\leftrightarrow$X schema ambiguity (Appendix~\ref{app:cf-distribution}).
121	Beam search ($k{=}4$) eliminates residual DR and reduces CF to $<$1\% for both Qwen and Llama (Appendix~\ref{app:beam-search}).
122	
123	\begin{table}[t]
124	\centering
125	\small
126	\setlength{\tabcolsep}{3pt}
127	\resizebox{\columnwidth}{!}{%
128	\begin{tabular}{@{}lll rrrr r@{}}
129	\toprule
130	\textbf{Model} & \textbf{Setting} & \textbf{Mode}
131	  & \textbf{DR\,$\downarrow$} & \textbf{CF}
132	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
133	  & \textbf{$\Delta$DR} \\
134	\midrule
135	\multirow{4}{*}{Qwen3-8B}
136	  & \multirow{2}{*}{Zero-shot}
137	    & Unconstr.\ & 15.37 & 0.08 & 8.23  & 31.01 & --- \\
138	  & & Full S1    &  0.93 & 9.90 & 8.36  & 30.98 & $\downarrow$94\% \\
139	\cmidrule(l){2-8}
140	  & \multirow{2}{*}{LoRA}
141	    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
142	  & & Full S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
143	\midrule
144	\multirow{4}{*}{Llama-3.1-8B}
145	  & \multirow{2}{*}{Zero-shot}
146	    & Unconstr.\ & 13.34 & 0.24 & 2.68  & 23.56 & --- \\
147	  & & Full S1    &  0.08 & 6.56 & 2.54  & 23.49 & $\downarrow$99\% \\
148	\cmidrule(l){2-8}
149	  & \multirow{2}{*}{LoRA}
150	    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
151	  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
152	\bottomrule
153	\end{tabular}}%
154	\caption{Composability on SciERC (551 docs): zero-shot vs.\ LoRA $\times$ unconstrained vs.\ S1.
155	Adding S1 to LoRA: DR\,$\leq$\,0.09\%, R-F1 within $\pm$0.1\,pp.
156	DocRED: Qwen DR $-$99\%, Llama DR $-$59\%.
157	F1\,$\times$100.}
158	\label{tab:composability}
159	\end{table}
160	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64aa0e9b-69dc-4970-91ec-3818738149ec",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "300be6e5-43ef-4a06-b6d6-5beee2f45c98",
  "sourceToolAssistantUUID": "64aa0e9b-69dc-4970-91ec-3818738149ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-18T17:32:42.988Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A7NkQQxyHNaL8hTbjYwfe9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "300be6e5-43ef-4a06-b6d6-5beee2f45c98",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS9NzzANmD4ZNmBpDy7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9551610d-9af1-48a2-9337-3f20846f002e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AiyARgEZs3Dzciwb8xn4Dt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4299,
      "cache_read_input_tokens": 53209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4299,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 47 · 2026-05-18T17:32:42.992Z_

<details><summary>↩ Tool result · `toolu_01A7NkQQxyHNaL8hTbjYwfe9`</summary>

```text
1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED (96 Wikidata relation types, 14$\times$ SciERC; Qwen3-8B, zero-shot, 998 documents).
10	
11	% ──────────────────────────────────────────
12	%  Table: DocRED four-way ablation
13	% ──────────────────────────────────────────
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.6pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}l rrrrr rr@{}}
20	\toprule
21	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
22	& \multicolumn{2}{c}{\textbf{F1}} \\
23	\cmidrule(lr){2-6} \cmidrule(l){7-8}
24	\textbf{Mode}
25	  & DR\,$\downarrow$ & $\Delta$DR
26	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
27	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
28	\midrule
29	Unconstrained
30	  & 18.46 & ---
31	  & 29.66 & 2.48
32	  & 0.10
33	  & 7.74  & 58.15 \\
34	Grammar
35	  & 26.17 & $\uparrow$42\%
36	  & \textbf{0.03} & \textbf{0}
37	  & 0.07
38	  & \textbf{8.31}  & \textbf{59.38} \\
39	Semantic
40	  & 13.84 & $\downarrow$25\%
41	  & 29.87 & 4.22
42	  & 1.05
43	  & 7.70  & 57.81 \\
44	Full (S1)
45	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
46	  & \textbf{0.03} & \textbf{0}
47	  & 2.57
48	  & 8.23  & 59.37 \\
49	\bottomrule
50	\end{tabular}}%
51	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
52	$\Delta$DR: relative change vs.\ unconstrained.
53	Best per column in \textbf{bold} (CF excluded).
54	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
55	\label{tab:docred-ablation}
56	\end{table}
57	
58	% exp_ids: phase2_docred_unconstrained, phase2_docred_full_s1
59	\paragraph{Core result.}
60	Full S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates ET ($\to$\,0\%), and near-eliminates RV (29.66\%\,$\to$\,0.03\%).\footnote{The residual 0.03\% RV traces to a rare XGrammar automaton edge case where subword tokens from different enum entries combine into chimeric values (e.g., \texttt{member} + \texttt{icipant\_of} from \texttt{member\_of} and \texttt{participant\_of}). This is not a fundamental limitation of the approach.}
61	R-F1 improves from 7.74 to 8.23 ($+$0.50\,pp; $p < 0.001$), attributable to elimination of 5{,}189 OOV relation predictions.
62	CF increases modestly (0.10\%\,$\to$\,2.57\%), consistent with the CF$\leftrightarrow$DR trade-off (\S\ref{sec:discussion}).
63	
64	% exp_ids: phase2_docred_grammar_only
65	\paragraph{Grammar layer surfaces latent violations.}
66	Grammar-only constraints eliminate RV and ET but \emph{increase} DR to 26.17\% ($+$42\%): the baseline's 29.66\% OOV triples cannot be evaluated for DR; grammar enforcement assigns valid relation names whose domain/range rules the associated types frequently violate, \emph{revealing} latent incompatibilities that motivate the semantic layer.
67	
68	% exp_ids: phase2_docred_semantic_only, phase2_docred_full_s1
69	\paragraph{Enabling dependency and tightness ceiling.}
70	Semantic-only reduces DR by 25\% but cannot eliminate RV (29.87\%) or prevent ET increases (2.48\%\,$\to$\,4.22\%), which replicates SciERC's enabling dependency.
71	Residual DR (10.21\%) exceeds SciERC's (0.93\%) due to higher constraint tightness ($\bar{\kappa}{=}0.842$ vs.\ 0.333): residual DR of 10.21\% implies effective semantic coverage of approximately 90\%, consistent with tight constraints forcing frequent grammar-first fallback (Appendix~\ref{app:fallback-coverage}).
72	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9551610d-9af1-48a2-9337-3f20846f002e",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "be5c87fe-63f2-49bd-9964-19a7645dacd9",
  "sourceToolAssistantUUID": "9551610d-9af1-48a2-9337-3f20846f002e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-18T17:32:43.797Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AQVjCMsKTTVJgQMkdb4LAz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be5c87fe-63f2-49bd-9964-19a7645dacd9",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS9NzzANmD4ZNmBpDy7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77682af4-c5f8-49a8-bc12-c97bd6ce2e33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AiyARgEZs3Dzciwb8xn4Dt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4299,
      "cache_read_input_tokens": 53209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4299,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 49 · 2026-05-18T17:32:43.804Z_

<details><summary>↩ Tool result · `toolu_01AQVjCMsKTTVJgQMkdb4LAz`</summary>

```text
1	% Section 7 — Discussion and Conclusion (maximally compressed)
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints that achieve 42--99\% DR reduction across three models $\times$ three datasets with no significant F1 cost.
5	Composed with LoRA fine-tuning, DR reaches $\leq$\,0.20\% ($<$0.6\,pp F1 cost); beam search ($k{=}4$) further eliminates both residual DR and CF for calibrated models (\S\ref{sec:beam-results}).
6	CF remains an open challenge for per-slot enforcement; global entity-level type consensus during decoding offers the most direct resolution path.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77682af4-c5f8-49a8-bc12-c97bd6ce2e33",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "74bbc627-f7a7-49bb-9c44-55641c6bd394",
  "sourceToolAssistantUUID": "77682af4-c5f8-49a8-bc12-c97bd6ce2e33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-18T17:32:47.217Z_

Now let me check the appendix for related work extensions and look at the runtime section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74bbc627-f7a7-49bb-9c44-55641c6bd394",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS9grXxgtiZzh38fLmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02d9aa6f-4fab-49f7-89c9-a697276450d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UQ1UNrRZ1jeYJoJyWarTV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5888,
      "cache_read_input_tokens": 57508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5888,
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

_source line 51 · 2026-05-18T17:32:49.256Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SpoWm9waqVZGGy2AKynNjU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02d9aa6f-4fab-49f7-89c9-a697276450d6",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS9grXxgtiZzh38fLmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13c539a8-ec1a-4c7e-becf-120511780f23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UQ1UNrRZ1jeYJoJyWarTV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5888,
      "cache_read_input_tokens": 57508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5888,
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

_source line 52 · 2026-05-18T17:32:49.269Z_

<details><summary>↩ Tool result · `toolu_01SpoWm9waqVZGGy2AKynNjU`</summary>

```text
1	\section{Extended Related Work}
2	\label{app:related_work}
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
15	However, all of these methods operate exclusively at the syntactic level: they ensure format validity (e.g., well-formed JSON, valid enum values) but cannot enforce cross-field semantic constraints such as ontology domain/range rules that depend on previously generated content.
16	This syntactic-only limitation motivates OntoCoDec's semantic extension: our grammar layer builds on XGrammar for structural (JSON schema and enum) constraints, while a second semantic layer enforces relational type constraints that are inherently beyond the expressive power of context-free grammars.
17	
18	% ===========================================================================
19	% Paradigm 1.5: Semantic Constrained Decoding for Code
20	% ===========================================================================
21	\paragraph{Semantic Constrained Decoding for Code.}
22	In programming-language generation, constrained decoding has been extended beyond syntax to enforce semantic properties such as type correctness, demonstrating that richer-than-CFG constraints can be compiled into token-level filtering.
23	In the text-to-SQL domain, PICARD~\cite{scholak2021picard} maintains an incremental SQL parsing state that rejects tokens violating syntax or referencing non-existent database columns at each decoding step, achieving state-of-the-art results on Spider and CoSQL without modifying model weights.
24	While mechanistically similar to OntoCoDec's token-level filtering, PICARD operates over a \emph{fixed, fully enumerated} schema (database table and column names known before decoding begins).
25	In contrast, OntoCoDec's entity registry is populated \emph{during} generation as entity spans are extracted from free text, requiring constraint sets that evolve with the decoding prefix, a fundamental distinction between querying a known schema and extracting from unstructured text.
26	Synchromesh~\cite{synchromesh_iclr2022} pioneers Constrained Semantic Decoding (CSD), which enforces syntax, type, and scope constraints simultaneously during code generation from pre-trained LMs without fine-tuning, establishing that semantic constraints can be expressed as dynamic token masks conditioned on the generation prefix.
27	MGD~\cite{mgd_neurips2023} uses static-analysis monitors to perform incremental type checking at decode time, enabling SantaCoder-1.1B to outperform text-davinci-003 on repository-level code completion by ensuring that every generated identifier is type-correct with respect to the surrounding code context.
28	Most recently, \citet{pldi2025_type_constrained_codegen} compile full type systems, including generic types and subtyping, into prefix automata for token-level logits masking, reducing compilation errors by over 50\%.
29	This last system is the closest mechanistic analog to OntoCoDec, applying the same ``type system $\to$ automaton $\to$ logits mask'' pipeline, though in a fundamentally different domain.
30	The key technical difference lies in the constraint structure: programming-language type systems feature deep subtyping hierarchies and parametric polymorphism, whereas IE ontology axioms specify flat domain/range sets; a relation $R$ accepts head entities from set $\mathcal{D}(R)$ and tail entities from set $\mathcal{R}(R)$, with no subtype chains.
31	Conversely, IE introduces a challenge absent in code generation: the constraint target (entity type) must be inferred from free-text spans rather than read from declared type annotations, requiring a stateful entity registry that tracks extracted types during autoregressive generation.
32	These methods collectively demonstrate that semantic (type) constraints at decode time are both feasible and highly effective, but exclusively in the code domain where type systems are formally specified.
33	OntoCoDec is the first to \emph{automatically compile} IE ontology axioms, including domain/range constraints, into token-level decoding masks for information extraction, migrating the type-constrained decoding paradigm from code generation to IE.
34	
35	% ===========================================================================
36	% Paradigm 2: Vocabulary/Type-Constrained Generation
37	% ===========================================================================
38	\paragraph{Vocabulary and Type-Constrained Generation.}
39	The idea of enforcing entity-type compatibility constraints for information extraction dates back to pre-neural methods.
40	\citet{roth_yih_2004} formulate joint entity and relation identification as an integer linear program (ILP) that enforces type constraints (e.g., \textsc{Emp-Org} only between \textsc{Per} and \textsc{Org} entities), establishing the foundational principle that relational type compatibility should be a hard constraint, not a soft preference learned from data.
41	In the autoregressive era, GENRE~\cite{decao2021genre} pioneers trie-based constrained beam search for autoregressive entity retrieval, restricting each decoding step to tokens consistent with valid entity names from a predefined catalog.
42	GenIE~\cite{josifoski2022genie} extends this approach to end-to-end information extraction with state-based constraints that enforce valid triple structures, achieving strong performance on closed-world knowledge base population, though it requires task-specific fine-tuning on the target schema.
43	AdaKGC~\cite{adakgc_emnlp2023} introduces schema-constrained dynamic decoding with trie-based prefix trees that adapt to the target schema, enforcing that generated entity and relation names belong to a predefined inventory, a vocabulary-level constraint that ensures name validity but does not verify type compatibility between a relation and its arguments.
44	GCD~\cite{geng2023gcd} provides a unified grammar-constrained decoding framework for structured NLP tasks including IE, introducing input-dependent grammars that adapt constraints based on the source text. GCD is the closest precursor to OntoCoDec in applying logits masking to IE, though limited to syntactic constraints.
45	NeuroLogic Decoding~\cite{lu2021neurologic} expresses lexical inclusion and exclusion constraints as predicate logic formulas enforced during beam search, offering a general mechanism for token-level control that can encode vocabulary membership but not relational type rules.
46	These approaches constrain \emph{which tokens} can appear (vocabulary membership) but not \emph{which type combinations} are valid for a given relation.
47	OntoCoDec's semantic layer enforces relational constraints (e.g., that the head entity of relation $R$ must belong to type set $\mathcal{D}(R)$) which cannot be expressed as static vocabulary restrictions because the valid set depends on the relation type generated earlier in the same sequence.
48	While Roth \& Yih's ILP formulation shares the same type-compatibility motivation, it operates as a post-hoc reranker over discrete candidates; OntoCoDec integrates enforcement directly into autoregressive decoding, preventing violations rather than filtering them.
49	
50	% ===========================================================================
51	% Paradigm 3: Structural Constraints for IE
52	% ===========================================================================
53	\paragraph{Structural Constraints via Training and Prompting.}
54	An orthogonal approach encodes IE output structure through model training or prompt design rather than decoding-time enforcement, relying on learned representations to produce schema-compliant outputs.
55	UIE~\cite{lu2022uie} defines a Structured Extraction Language and trains a unified text-to-structure model across 13 IE datasets, relying on large-scale pre-training to internalize output format constraints.
56	GoLLIE~\cite{sainz2024gollie} expresses annotation guidelines as Python dataclass definitions and fine-tunes Code-LLaMA to generate typed code, achieving strong zero-shot transfer to unseen IE schemas by leveraging the implicit type structure of programming languages.
57	KnowCoder~\cite{knowcoder_acl2024} takes this further by encoding 29K entity types from Wikidata as a Python class hierarchy, training a Code-LLM to generate structured extraction code that implicitly respects type inheritance, the most comprehensive schema-as-code approach to date.
58	CodeIE~\cite{li2023codeie} similarly reformulates IE as code generation, leveraging the structural regularity of programming languages to reduce output format errors.
59	ADELIE~\cite{qi2024adelie} uses SFT and DPO to align LLMs on IE tasks, achieving state-of-the-art results among open-source models while preserving general capabilities, though compliance with ontological constraints remains a learned soft preference rather than a guarantee.
60	In the supervised setting, joint entity-relation architectures such as SpERT~\cite{eberts2020spert} and PFN~\cite{yan2021pfn} enforce type consistency implicitly through shared representations: SpERT classifies entity spans and relation pairs in a single BERT pass with span-level negative sampling, while PFN decomposes feature encoding into entity-specific, relation-specific, and shared partitions via gating mechanisms.
61	These models achieve strong performance but are limited to fixed, predefined schemas and cannot generalize to unseen ontologies without retraining, precisely the zero-shot, ontology-portable scenario that OntoCoDec targets.
62	EnriCo~\cite{zaratiana2024enrico} applies Answer Set Programming (ASP) constraints during decoding of joint entity-relation extraction models, enforcing structural type compatibility at generation time. This is a decoding-time approach, though with model-specific, manually authored constraints rather than ontology-driven compilation.
63	Training-based methods provide \emph{soft} structural guidance: the model learns to prefer valid outputs but cannot guarantee compliance at inference time, as demonstrated by non-trivial violation rates even in fine-tuned systems.
64	Importantly, training-based and decoding-time approaches are complementary rather than competing: a system like GoLLIE could be combined with OntoCoDec's constraint layers, using fine-tuning to maximize the probability of valid outputs while decoding-time enforcement eliminates residual violations.
65	OntoCoDec provides \emph{hard} decoding-time enforcement that is training-free, automatically compiled from ontology schemas, and composable with any of these training-based approaches.
66	
67	% ===========================================================================
68	% Paradigm 4: Type-Checking / Ontology Validation
69	% ===========================================================================
70	\paragraph{Post-hoc Ontology Validation.}
71	Rather than constraining generation, several methods validate LLM outputs against ontological rules after generation, applying a detect-then-fix paradigm.
72	ODKE+~\cite{khorshidi2025odke} dynamically generates ontology snippets containing domain/range constraints as prompt context, achieving 98.8\% precision across 195 predicates at web scale, but constraint adherence relies on prompt-level guidance, not enforcement, leaving residual violations unaddressed.
73	SPIRES/OntoGPT~\cite{spires_2024} provides an ontology-based extraction framework that grounds LLM outputs against OBO ontologies post-generation, validating extracted entities and relations through ontology lookup and correcting mismatches in a second pass, representing the prompt-then-validate paradigm in the biomedical domain.
74	OntoLogX~\cite{ontologx_2025} applies SHACL validation to LLM-generated knowledge graphs, iteratively re-prompting the LLM to correct constraint violations and reducing them by approximately 10$\times$ across multiple correction rounds. This demonstrates the detect-then-fix paradigm's effectiveness but also its inherent multi-pass cost.
75	\citet{upadhyay2023openie} inject entity-type knowledge as constraints into Open IE via both constrained inference and constraint-aware training, improving F1 by 29\% on CaRB, though their constrained inference operates over a discrete candidate set rather than during autoregressive generation.
76	\citet{regino2025kgcurator} propose a multi-stage LLM pipeline for validating RDF triple insertions against RDFS domain/range constraints, where each validation step requires a separate LLM call, effective but computationally expensive at scale.
77	RELATE~\cite{olasunkanmi2025relate} addresses the alignment gap between LLM-extracted biomedical relations and standardized ontology predicates through a three-stage pipeline: ontology preprocessing with predicate embeddings, similarity-based retrieval via SapBERT, and LLM-based reranking with negation handling, achieving 94\% accuracy@10 on ChemProt.
78	While RELATE demonstrates effective ontology grounding for relation extraction, its constraints are applied \emph{post-extraction} through retrieval and reranking rather than during generation, and it requires domain-specific embedding models trained on biomedical corpora.
79	OntoCoDec enforces ontology constraints \emph{during} autoregressive decoding and requires no additional trained components beyond the base LLM.
80	Concurrently, \citet{zhou2026ontologytools} compile OWL ontologies into executable tool interfaces within The World Avatar framework, requiring LLM agents to invoke ontology-aware tools that enforce semantic constraints during knowledge graph construction from scientific text.
81	This ``ontology-to-tools'' approach shares OntoCoDec's philosophy of compiling formal ontological knowledge into runtime enforcement mechanisms, but operates at the tool-call level (constraining which API functions the agent invokes) rather than at the token level (constraining which tokens the decoder produces), and requires an agentic multi-step workflow rather than single-pass autoregressive generation.
82	\citet{ekaw2024_ontology_beam} introduce ontology-constrained beam scoring for clinical summarization, applying soft biases (not hard masks) during beam search to steer outputs toward ontology-compliant terms, a middle ground between unconstrained generation and hard enforcement that reduces but cannot eliminate violations.
83	Post-hoc validation detects violations after generation, requiring rejection or correction cycles that waste compute. In our setting, 15.37\% of generated triples contain domain/range violations under unconstrained decoding, representing substantial wasted generation effort.
84	OntoCoDec \emph{prevents} violations during decoding, redirecting probability mass to valid alternatives rather than discarding invalid outputs, with only marginal overhead from logits masking compared to the cost of regenerating or correcting violated triples.
85	Soft-constraint approaches such as ontology-weighted beam scoring reduce violation frequency but cannot eliminate it, whereas OntoCoDec substantially reduces violations (DR$\downarrow$94\% on SciERC, $\downarrow$45--90\% on DocRED depending on model).
86	
87	% ===========================================================================
88	% Paradigm 5: Constrained Decoding Quality Concerns
89	% ===========================================================================
90	\paragraph{Quality Impact of Constrained Decoding.}
91	A growing body of work raises concerns that constrained decoding degrades LLM generation quality, particularly for reasoning-intensive tasks where format enforcement interferes with chain-of-thought processes.
92	\citet{tam2024letmespeak} conduct a comprehensive evaluation showing that rigid format constraints (JSON, XML) harm performance on math and multi-hop QA benchmarks but \emph{benefit} classification-style tasks such as slot filling, a distinction directly relevant to IE, which is fundamentally an extraction (classification-like) task rather than a reasoning task.
93	CRANE~\cite{banerjee2025crane} provides theoretical analysis of why restricting outputs to narrow grammars suppresses chain-of-thought reasoning by eliminating intermediate reasoning tokens, and proposes an alternating strategy between unconstrained reasoning phases and constrained output phases to mitigate this effect.
94	\citet{schall2025hiddencost} conduct a systematic study across 11 models and multiple benchmarks, finding 10--30\% semantic correctness degradation on reasoning tasks under structural constraints, with larger models showing greater absolute degradation.
95	\citet{zhou2026snowballing} identify ``structure snowballing,'' a failure mode where format compliance cognitive load traps models in repetitive structural patterns rather than improving reasoning during self-correction iterations.
96	These findings establish a legitimate concern for constrained decoding in reasoning-heavy applications.
97	However, information extraction occupies a fundamentally different regime: the model extracts entities and relations from input text rather than generating novel reasoning chains, and \citet{tam2024letmespeak}'s own results show that extraction-style tasks are robust to, or even benefit from, format constraints.
98	OntoCoDec addresses this concern empirically: domain/range violations decrease by 94\% on SciERC (15.37\%$\to$0.93\%) and 45--90\% on DocRED across two models, with F1-neutral impact on SciERC ($+$0.13pp, $p{=}0.58$) and significant R-F1 gains on DocRED (Qwen $p{<}0.001$, Llama $p{=}0.013$).
99	Critically, OntoCoDec's constraints target only type tokens (entity types, relation labels), leaving free-text spans (entity surface forms and their boundaries) entirely unconstrained, which minimizes the distribution distortion that causes quality degradation in reasoning tasks.
100	A two-pass variant (S2), explored in ablation (Section~5), separates extraction and constraint enforcement into distinct passes, analogous to CRANE's alternating strategy; however, our primary single-pass approach already avoids reasoning interference by constraining only type tokens while leaving free-text spans unconstrained.
101	
102	% ===========================================================================
103	% Our Approach
104	% ===========================================================================
105	\paragraph{Our Approach.}
106	OntoCoDec occupies a unique position in this landscape: it is the first system to \emph{automatically compile} IE ontology schemas, including domain/range axioms, into token-level semantic masks, extending grammar-constrained decoding from syntactic to semantic enforcement without manually authored rules.
107	Unlike vocabulary-constrained methods that restrict individual tokens to a fixed set, OntoCoDec enforces \emph{cross-field relational constraints} through a stateful entity registry that tracks extracted types during autoregressive generation, enabling dynamic constraint evaluation that depends on previously decoded content.
108	This approach is orthogonal to supervised IE methods and applicable to any autoregressive LM without model modification or additional training.
109	Unlike training-based IE systems, OntoCoDec is training-free and substantially reduces type violations at inference time (DR$\downarrow$94\% on SciERC, $\downarrow$45--90\% on DocRED); unlike post-hoc validation, it prevents violations rather than detecting them, redirecting probability mass to valid alternatives with significant R-F1 gains on DocRED ($p \leq 0.013$) and F1-neutral impact on SciERC.
110	The two constraint layers, grammar (structural) and semantic (relational), compose via bitwise AND with an enabling dependency: the grammar layer ensures every generated type token belongs to the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type.
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13c539a8-ec1a-4c7e-becf-120511780f23",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "669a34d0-b209-4474-9067-4076bc0bfd10",
  "sourceToolAssistantUUID": "13c539a8-ec1a-4c7e-becf-120511780f23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-18T17:32:49.577Z_

<details open><summary>🔧 Tool call — Read · `toolu_016CtKbcDFrH4H2p8kghmrmf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "669a34d0-b209-4474-9067-4076bc0bfd10",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS9grXxgtiZzh38fLmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0044836-591e-4f5e-91ef-41931a4f7bf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UQ1UNrRZ1jeYJoJyWarTV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5888,
      "cache_read_input_tokens": 57508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5888,
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

_source line 54 · 2026-05-18T17:32:49.588Z_

<details><summary>↩ Tool result · `toolu_016CtKbcDFrH4H2p8kghmrmf`</summary>

```text
1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	Full S1 overhead varies with document length: $+$13.1\% on SciERC (short documents) and $+$2.43\% on DocRED (long documents), as the fixed per-token constraint cost is amortized over longer generation sequences (Qwen3-8B, zero-shot greedy, RTX PRO 6000 Blackwell). Under fine-tuning on SciERC, overhead drops to $+$2.3\% (61\,ms/doc).
6	Grammar compile is a one-time 44\,ms cost.
7	Details in Appendix~\ref{app:runtime}.
8	
9	\paragraph{Beam search compatibility.}
10	\label{sec:beam-results}
11	Beam search ($k{=}4$) addresses greedy decoding's two residual limitations on SciERC (551 documents): DR drops to 0\% for calibrated models (Qwen 0.93\%\,$\to$\,0\%; Llama 0.08\%\,$\to$\,0\%) and CF decreases substantially (Qwen 9.90\%\,$\to$\,0.53\%; Llama 6.56\%\,$\to$\,0.93\%).
12	Combined with LoRA, both calibrated models achieve zero violations across all four metrics on SciERC (Qwen3-8B R-F1\,=\,44.23; Llama-3.1-8B R-F1\,=\,46.11; Appendix~\ref{app:beam-search}).
13	
14	% === 70B cross-scale (PLACEHOLDER — awaiting DocRED 70B results) ===
15	%\paragraph{Cross-scale generalizability.}
16	%\label{sec:70b-results}
17	%To evaluate cross-scale generalizability, we test OntoCoDec on Llama-3.1-70B-Instruct (AWQ INT4 quantization).
18	%On SciERC, the 70B model produces fewer baseline violations than its 8B counterpart (DR 6.5\% vs.\ 13.3\%), yet violations persist; OntoCoDec eliminates them entirely (DR$\to$0\%, R-F1 $-$0.03\,pp).
19	%On DocRED, [PLACEHOLDER for 70B DocRED results].
20	%Case studies comparing 8B and 70B behavior appear in Appendix~\ref{app:case-scale}.
21	
22	Appendix~\ref{app:case-studies} presents representative case studies illustrating constraint behavior across violation types.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0044836-591e-4f5e-91ef-41931a4f7bf8",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "068eedaa-99e7-41e6-ab08-c44725427814",
  "sourceToolAssistantUUID": "c0044836-591e-4f5e-91ef-41931a4f7bf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-18T17:32:50.138Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VZ6BombkZbZgoM8oYxnJ3u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "068eedaa-99e7-41e6-ab08-c44725427814",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbAS9grXxgtiZzh38fLmu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1300aa9-6fb8-472b-87e1-0110267c83cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UQ1UNrRZ1jeYJoJyWarTV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5888,
      "cache_read_input_tokens": 57508,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5888
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 272,
          "cache_read_input_tokens": 57508,
          "cache_creation_input_tokens": 5888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5888,
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

_source line 56 · 2026-05-18T17:32:50.397Z_

<details><summary>↩ Tool result · `toolu_01VZ6BombkZbZgoM8oYxnJ3u`</summary>

```text
1	% Appendix B — Extended Discussion
2	% Contains discussion paragraphs moved from the main text during compression.
3	
4	\section{Extended Discussion}\label{app:discussion}
5	
6	%%% CF Dual Mechanism %%%
7	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1
8	
9	\paragraph{CF Dual Mechanism.}
10	CF violations arise from two distinct mechanisms:
11	(1)~\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.
12	The entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.
14	
15	These mechanisms have sharply different model profiles.
16	Qwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\% of its CF violations to registry override.
17	Llama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.
18	This asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\,=\,2.57\% on DocRED vs.\ Llama's 12.02\%, despite both using identical constraint configurations.
19	The difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.
20	
21	%%% Fallback Behavior and Effective Coverage %%%
22	% exp_ids: cf_fallback_ablation_scierc (final data)
23	
24	\paragraph{Fallback Behavior and Effective Coverage.}
25	\label{app:fallback-coverage}
26	The two-layer architecture produces two distinct fallback mechanisms with different semantic consequences.
27	\emph{Grammar-first fallback} (36.6\% of type-bearing positions on SciERC) occurs when $S(t) \cap G(t) = \emptyset$: the semantic layer deactivates as a safety valve, preserving structural validity at the cost of potential type violations. These events account for the residual DR that persists after constraint enforcement.
28	\emph{Registry-consistent fallback} (4.5\%) occurs when the entity's registered type conflicts with domain/range constraints; the system defaults to the registered type for cross-triple consistency.
29	Together, these mechanisms produce the characteristic profile of composable constraint systems: residual DR traces to grammar-first fallback events, while CF violations arise from registry override events where per-relation enforcement assigns conflicting types.
30	
31	We define \emph{effective semantic constraint coverage} as $1 - f_{\text{gf}}$, where $f_{\text{gf}}$ is the grammar-first fallback rate.
32	On SciERC, Llama-3.1-8B shows $f_{\text{gf}} = 36.6\%$ (6{,}237 of 17{,}024 mask calls), yielding 63.4\% effective coverage.
33	On DocRED, by contrast, Qwen3-8B shows $f_{\text{gf}} = 0.08\%$ (46 of 54{,}859), yielding 99.9\% coverage.
34	The large discrepancy is primarily a tokenization artifact: SciERC entity types are multi-token (e.g., \textsc{OtherScientificTerm}, averaging 2.87 mask calls per type field), and continuation tokens necessarily conflict with the semantic mask, inflating the per-mask-call fallback rate.
35	DocRED types (\textsc{PER}, \textsc{ORG}, \textsc{LOC}, \textsc{TIME}, \textsc{NUM}, \textsc{MISC}) are all single-token, eliminating this inflation.
36	This metric directly quantifies the enabling dependency (\S\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.
37	Qwen3-8B, with zero grammar-first fallbacks, achieves 100\% effective coverage on SciERC, consistent with its lower residual DR (0.93\% vs.\ Llama's 0.08\%).
38	
39	%%% CF-DR Trade-off Analysis %%%
40	% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)
41	
42	\paragraph{CF-DR Trade-off Analysis.}
43	\label{app:cf-dr-tradeoff}
44	
45	CF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\% on SciERC, up to 12.02\% on Llama DocRED).
46	We treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.
47	Table~\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\sigma(r)$.
48	
49	\begin{table}[t]
50	\centering
51	\small
52	\begin{tabular}{@{}l rrrr@{}}
53	\toprule
54	\textbf{Configuration} & \textbf{DR\,(\%)} & \textbf{CF\,(\%)} & \textbf{DR+CF} & \textbf{$f_{\text{gf}}$\,(\%)} \\
55	\midrule
56	Full S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\
57	CF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\
58	\midrule
59	$\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\
60	\bottomrule
61	\end{tabular}
62	\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \texttt{w1\_cf\_fallback\_scierc\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\,pp. $f_{\text{gf}}$: grammar-first fallback rate at type-bearing positions.}
63	\label{tab:cf-dr-tradeoff}
64	\end{table}
65	
66	The CF fallback variant nearly eliminates CF (9.90\%\,$\to$\,0.04\%, $-$9.86\,pp) but at the cost of a 15.9$\times$ increase in DR (0.93\%\,$\to$\,14.78\%, $+$13.85\,pp).
67	% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664
68	This is not a net improvement: total violations (DR+CF) rise from 10.83\% to 14.82\% ($+$3.99\,pp), so the change \emph{re-routes} violations rather than reducing them.
69	The mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.
70	The grammar-first fallback is triggered at 36.64\% of type-bearing positions, indicating that this conflict is structural, not a tunable hyperparameter.
71	
72	We interpret this as a fundamental tension in composable constraint systems with \emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.
73	Within this design, the current full S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\% DR at the cost of 9.90\% CF.
74	The direction of the trade-off is consistent beyond SciERC/Qwen3-8B: across all six zero-shot configurations (3 models $\times$ 2 datasets), DR and CF are inversely associated (Spearman $\rho = -0.77$, $n{=}6$), with no setting showing both high DR and high CF simultaneously (Table~\ref{tab:cross-model}).
75	The pattern is a structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact; we select SciERC/Qwen3-8B for detailed ablation because it exhibits the highest CF (9.90\%), making the trade-off most visible.
76	While the inverse association holds across all configurations, the absolute trade-off magnitude may differ in settings with higher baseline CF, such as Llama DocRED (CF = 12.02\%), where the larger CF headroom could yield proportionally larger shifts under alternative fallback priorities.
77	The CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\% of CF violations on SciERC involve the catch-all \textsc{Generic} type (Table~\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\ referential use, a distinction the per-slot decoder cannot resolve without document-level coreference.
78	
79	Two complementary paths can lower CF without re-routing it to DR.
80	(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\% relative to the zero-shot setting (9.90\%\,$\to$\,1.18\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
81	% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118
82	The remaining 1.18\% still traces to \textsc{Generic}$\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.
83	(ii)~\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.
84	
85	%%% Dual-Factor Quantitative Analysis %%%
86	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,
87	%          llama_scierc_full_s1, llama_docred_full_s1
88	
89	\paragraph{Dual-Factor Quantitative Analysis.}
90	\label{app:dual-factor}
91	
92	Figure~\ref{fig:dual-factor-scatter} plots residual DR against the product $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ for model$\times$dataset configurations.
93	For \emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test.
94	The strong fit supports the dual-factor pattern from \S\ref{sec:composition}: residual DR is governed by the product of schema tightness and baseline violation rate.
95	Mistral-7B (unconstrained ET${=}$7.58\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\%) substantially exceeds the linear prediction, confirming that when model calibration is insufficient (ET${>}$5\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.
96	This motivates a principled exclusion criterion: models with unconstrained ET${>}$5\% on either dataset fall outside the regime where the tightness$\times$RV product is the primary DR driver.
97	The two DocRED points (high $\bar{\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\bar{\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.
98	
99	\begin{figure}[t]
100	\centering
101	\includegraphics[width=0.75\columnwidth]{figures/dual_factor_scatter.pdf}
102	\caption{Residual DR vs.\ $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ across four model$\times$dataset configurations.
103	Linear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$; Mistral deviates due to entity misclassification.}
104	\label{fig:dual-factor-scatter}
105	\end{figure}
106	
107	%%% Dataset-Dependent F1 Impact (moved from §7) %%%
108	% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
109	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
110	
111	\paragraph{Dataset-Dependent F1 Impact.}
112	The divergence in F1 significance between DocRED ($+$0.50\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
113	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.
114	SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
115	Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.50\,pp), confirming that F1 gain magnitude is proportional to baseline OOV rate.
116	% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained
117	% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)
118	
119	%%% Paragraph 1: Low F1 Practical Significance %%%
120	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
121	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
122	
123	\paragraph{Practical Significance of Zero-Shot F1.}
124	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
125	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
126	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
127	When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary: Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC, 18.46\% on DocRED).
128	% exp_ids: phase0_scierc_unconstrained, phase2_docred_unconstrained
129	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
130	The contribution of this work is the constraint enforcement method itself; the zero-shot setting isolates its effect from confounds introduced by task-specific fine-tuning.
131	
132	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
133	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
134	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
135	
136	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
137	Post-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
138	% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
139	However, this precision gain comes at substantial cost.
140	On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions), reducing recall from 9.46\% to 8.40\%.
141	% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
142	Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
143	% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
144	OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
145	The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.
146	
147	%%% CF Violation Distribution %%%
148	% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),
149	%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)
150	
151	\paragraph{Cross-Field Violation Distribution.}
152	\label{app:cf-distribution}
153	
154	Table~\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC full S1 (245 CF violations, all pairwise; no mention triggered $\geq$3 types).
155	Conflicts involving the \textsc{Generic} type account for 63.3\% (155/245) of all violations.
156	\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially, a distinction the per-slot constrained decoder cannot resolve without document-level coreference.
157	
158	The pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\%); on DocRED, the analogous catch-all type \textsc{MISC} drives 76.6\% of Qwen's CF violations.
159	Under unconstrained decoding, CF rates collapse to $\leq$1\% on both datasets, confirming that CF violations are a side-effect of per-slot type commitment rather than a model deficiency.
160	
161	\begin{table}[t]
162	\centering
163	\small
164	\begin{tabular}{@{}lr r@{}}
165	\toprule
166	\textbf{Conflicting Type Pair} & \textbf{Count} & \textbf{\%} \\
167	\midrule
168	Generic $\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\
169	Generic $\leftrightarrow$ Material & 35 & 14.3 \\
170	Generic $\leftrightarrow$ Metric & 30 & 12.2 \\
171	Method $\leftrightarrow$ Task & 20 & 8.2 \\
172	Material $\leftrightarrow$ Method & 17 & 6.9 \\
173	OtherScientificTerm $\leftrightarrow$ Task & 12 & 4.9 \\
174	\midrule
175	10 further pairs (each $\leq$3.3\%) & 46 & 18.8 \\
176	\midrule
177	\textbf{Total} & \textbf{245} & 100.0 \\
178	\bottomrule
179	\end{tabular}
180	\caption{CF violation distribution on SciERC full S1 (Qwen3-8B, 551 documents).
181	All 245 violations are pairwise conflicts.
182	Conflicts involving \textsc{Generic} account for 63.3\%.}
183	\label{tab:cf-distribution}
184	\end{table}
185	
186	%%% Per-Relation DR Elimination under Fine-Tuning %%%
187	% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
188	
189	\paragraph{Per-Relation DR Elimination under Fine-Tuning.}
190	\label{app:lora-per-relation}
191	
192	Table~\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.
193	Fine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \textsc{Evaluate-for} ($\kappa{=}0.361$, 13.13\%), \textsc{Part-of} ($\kappa{=}0.417$, 5.77\%), and \textsc{Compare} ($\kappa{=}0.528$, 5.00\%).
194	Adding OntoCoDec constraints eliminates all remaining violations across all relations.
195	One \textsc{Evaluate-for} triple (99\,$\to$\,98) is redirected to \textsc{Used-for} (634\,$\to$\,635) by token-level masking: the head entity's registered type falls outside \textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.
196	
197	\begin{table}[t]
198	\centering
199	\small
200	\begin{tabular}{@{}l r rr rr@{}}
201	\toprule
202	& & \multicolumn{2}{c}{\textbf{LoRA Unconstr.}} & \multicolumn{2}{c}{\textbf{LoRA + S1}} \\
203	\cmidrule(lr){3-4} \cmidrule(l){5-6}
204	\textbf{Relation} & $\kappa$ & DR\,(\%) & $n$ & DR\,(\%) & $n$ \\
205	\midrule
206	Evaluate-for & 0.361 & 13.13 & 99 & \textbf{0} & 98 \\
207	Part-of      & 0.417 & 5.77  & 52 & \textbf{0} & 52 \\
208	Compare      & 0.528 & 5.00  & 40 & \textbf{0} & 40 \\
209	Conjunction  & 0.306 & 1.31  & 153 & \textbf{0} & 153 \\
210	Feature-of   & 0.278 & 1.35  & 74 & \textbf{0} & 74 \\
211	Used-for     & 0.028 & 0.16  & 634 & \textbf{0} & 635 \\
212	Hyponym-of   & 0.417 & 0     & --- & \textbf{0} & --- \\
213	\bottomrule
214	\end{tabular}
215	\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).
216	$\kappa$: constraint tightness; $n$: predicted triple count.
217	Used-for gains one triple from Evaluate-for redirection.}
218	\label{tab:lora-per-relation}
219	\end{table}
220	
221	%%% Fine-Tuned Four-Way Ablation %%%
222	% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*
223	
224	\paragraph{Fine-Tuned Four-Way Ablation.}
225	\label{app:ft-ablation}
226	
227	Table~\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.
228	
229	\begin{table}[t]
230	\centering
231	\small
232	\setlength{\tabcolsep}{3pt}
233	\resizebox{\columnwidth}{!}{%
234	\begin{tabular}{@{}lll rrrrr rr@{}}
235	\toprule
236	\textbf{Dataset} & \textbf{Model} & \textbf{Mode} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{PF} & \textbf{E-F1\,$\uparrow$} & \textbf{R-F1\,$\uparrow$} \\
237	\midrule
238	\multirow{8}{*}{SciERC}
239	  & \multirow{4}{*}{Qwen3-8B}
240	    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
241	  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
242	  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\
243	  & & Full S1       & \textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\
244	  \cmidrule(l){2-10}
245	  & \multirow{4}{*}{Llama-3.1-8B}
246	    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
247	  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
248	  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\
249	  & & Full S1       & \textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\
250	\midrule
251	\multirow{8}{*}{DocRED}
252	  & \multirow{4}{*}{Qwen3-8B}
253	    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.12 & 7.11 & 82.15 & 40.86 \\
254	  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\
255	  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.89 \\
256	  & & Full S1       & \textbf{0.01} & 0.00 & 0.00 & 0.41 & 8.52 & 81.43 & 40.56 \\
257	  \cmidrule(l){2-10}
258	  & \multirow{4}{*}{Llama-3.1-8B}
259	    & Unconstrained & 0.49 & 0.15 & 0.00 & ---  & 2.30 & 83.93 & 43.72 \\
260	  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\
261	  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\
262	  & & Full S1       & \textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 85.23 & 44.23 \\
263	\bottomrule
264	\end{tabular}}%
265	\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\times$ 2 datasets).
266	DR/RV/ET/CF: violation rates (\%); PF: parse failure rate (\%); F1 $\times$100.
267	Grammar layer is a no-op post-fine-tuning (DR change $<$0.2\,pp in all 4 settings; RV and ET already 0\% without constraints).
268	Semantic layer is the sole effective DR defense, providing 39--72\% reduction.
269	F1 cost is negligible: max $\Delta$R-F1 = $-$0.30\,pp (Qwen DocRED full vs.\ unconstrained).}
270	\label{tab:ft-ablation}
271	\end{table}
272	
273	The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\% without constraints, and grammar-only DR change is $<$0.2\,pp (4/4 settings).
274	The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\% across all settings (SciERC: Qwen $-$69\%, Llama $-$41\%; DocRED: Qwen $-$72\%, Llama $-$39\%).
275	Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.20\% in all 4 settings), confirming that even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.
276	F1 cost is negligible: the maximum R-F1 decrease across all 16 model$\times$dataset$\times$mode combinations is $-$0.30\,pp (Qwen DocRED, full vs.\ unconstrained), attributable to parse failure increase (7.11\%\,$\to$\,8.52\%) rather than constraint-induced extraction degradation.
277	
278	%%% Residual DR Error Analysis (Fine-Tuned) %%%
279	% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*
280	
281	\paragraph{Residual DR Error Analysis.}
282	\label{app:residual-dr-analysis}
283	
284	Across all fine-tuned settings (2 models $\times$ 2 datasets $\times$ full S1), only 36 domain/range violations remain.
285	Manual inspection reveals four root causes:
286	
287	\begin{enumerate}[nosep,leftmargin=*]
288	\item \emph{Entity type errors} (39\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \textsc{LOC} when the gold standard requires \textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.
289	\item \emph{Schema coverage gaps} (33\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.
290	\item \emph{Incorrect relation selection} (17\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.
291	\item \emph{Direction reversal} (11\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.
292	\end{enumerate}
293	
294	Two dataset-specific patterns emerge.
295	Outside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.
296	On DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\%), with entity type errors as the dominant cause (14/33, 42\%).
297	This asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 7 entity types) compared to Qwen, which achieves near-zero residual.
298	The implication is twofold: (i)~the irreducible floor from schema gaps is small ($\sim$3 violations across 4 settings), confirming that the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.
299	
300	%%% Post-Hoc Filtering Comparison (Extended) %%%
301	% exp_ids: posthoc_*_zs, posthoc_*_ft
302	
303	\paragraph{Post-Hoc Filtering: Extended Comparison.}
304	\label{app:posthoc-extended}
305	
306	Table~\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.
307	
308	\begin{table}[t]
309	\centering
310	\small
311	\setlength{\tabcolsep}{3pt}
312	\resizebox{\columnwidth}{!}{%
313	\begin{tabular}{@{}lll rrr l@{}}
314	\toprule
315	\textbf{Setting} & \textbf{Model} & \textbf{Dataset} & \textbf{Reject\%} & \textbf{R-F1$_{\text{ph}}$} & \textbf{R-F1$_{\text{cd}}$} & \textbf{Winner} \\
316	\midrule
317	\multirow{6}{*}{ZS}
318	  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\
319	  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\
320	  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\
321	  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\
322	  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\
323	  & Mistral & DocRED & \textbf{73.7} & 3.85  & \textbf{5.52} & cd \\
324	\midrule
325	\multirow{4}{*}{FT}
326	  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\
327	  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\
328	  & Qwen    & DocRED & 1.03 & 41.11 & 40.56 & ph \\
329	  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\
330	\bottomrule
331	\end{tabular}}%
332	\caption{Post-hoc filtering (ph) vs.\ constrained decoding (cd).
333	In zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.
334	At reject rate $>$70\% (Mistral DocRED), post-hoc F1 collapses below constrained.
335	Under fine-tuning, rejection rates drop to 0.6--2.0\% and the two strategies are equivalent ($\Delta \leq 0.55$\,pp; each wins two groups).
336	F1 $\times$100.}
337	\label{tab:posthoc-extended}
338	\end{table}
339	
340	The crossover point occurs when post-hoc rejection exceeds $\sim$70\%: Mistral DocRED rejects 73.7\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\,pp).
341	OntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.
342	Under fine-tuning, both strategies converge because few violations remain to filter or constrain ($\Delta \leq 0.55$\,pp across all four FT groups, with each strategy winning two).
343	
344	%%% Zero-Shot Runtime Profiling %%%
345	
346	\paragraph{Zero-Shot Runtime Profiling.}
347	\label{app:runtime}
348	
349	On SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\,s/doc and Full S1 constrained decoding averages 4.710\,s/doc ($+$13.1\% overhead).
350	On DocRED (same configuration), unconstrained inference averages 19.34\,s/doc and Full S1 averages 19.81\,s/doc ($+$2.43\% overhead).
351	The lower relative overhead on DocRED reflects amortization: the fixed per-token constraint cost is spread over longer generation sequences.
352	Grammar compile is a one-time 0.044\,s cost (amortized to zero).
353	
354	%%% FT Latency %%%
355	
356	\paragraph{Fine-Tuned Latency Profiling.}
357	\label{app:ft-latency}
358	Under LoRA fine-tuning (Qwen3-8B, SciERC, 100 documents, RTX PRO 6000), per-document inference times are: unconstrained 2.594\,s, grammar-only 2.637\,s ($+$1.7\%), semantic-only 2.625\,s ($+$1.2\%), full S1 2.655\,s ($+$2.3\%, $p{<}0.0001$ paired $t$-test).
359	The combined overhead is sub-additive (2.3\% $<$ 1.7\%$+$1.2\%) because fine-tuned models produce fewer grammar-first fallback events (the semantic mask conflicts with grammar-valid tokens less often when per-slot predictions are better calibrated), reducing the number of active masking calls per document.
360	Compared to the zero-shot regime (\S\ref{app:runtime}), absolute overhead decreases from seconds-scale to milliseconds-scale: the fine-tuned model generates shorter, more structured outputs, compressing total generation time from 4.163\,s (zero-shot) to 2.594\,s (fine-tuned) per document on the same GPU.
361	
362	%%% Fuzzy Relation Matching %%%
363	
364	\paragraph{Relation Matching Protocol.}
365	\label{app:fuzzy-matching}
366	Relation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\ spaces, abbreviations).
367	A predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\% \emph{and} edit distance $\leq 2$.
368	This protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\_of\_government'' for ``head of government'').
369	On Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\,pp R-F1; strict R-F1\,=\,3.50\% vs.\ fuzzy 4.34\%).
370	For Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).
371	All F1 figures in the main text use fuzzy normalization consistently across all models and conditions.
372	
373	%%% Per-Relation Violation Landscape %%%
374	
375	\paragraph{Per-Relation Violation Landscape.}
376	\label{app:per-relation-landscape}
377	
378	Table~\ref{tab:prompt_comparison} compares violation rates under unconstrained and schema-informed prompting.
379	Figure~\ref{fig:per_relation_dr} shows the per-relation DR distribution on SciERC.
380	
381	\begin{table}[t]
382	\centering
383	\small
384	\caption{Violation rates (\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}
385	\label{tab:prompt_comparison}
386	\begin{tabular}{ll cccc}
387	\toprule
388	Dataset & Prompt & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ \\
389	\midrule
390	\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\
391	 & Schema-informed & 5.8 & 0.3 & \textbf{0.0} & --- \\
392	\midrule
393	\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\
394	 & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\
395	\bottomrule
396	\end{tabular}
397	\end{table}
398	
399	\begin{figure}[t]
400	\centering
401	\includegraphics[width=\columnwidth]{figures/fig2_per_relation_dr.pdf}
402	\caption{Per-relation DR violation rates on SciERC (Qwen3-8B, unconstrained). Rates correlate with constraint tightness $\kappa(r)$.}
403	\label{fig:per_relation_dr}
404	\end{figure}
405	
406	%%% WikiEvents Extended %%%
407	
408	\paragraph{WikiEvents Dataset Details.}
409	\label{app:wikievents}
410	WikiEvents~\cite{li2021document} is a document-level event argument extraction benchmark grounded in the DARPA KAIROS ontology.
411	It defines 56 event types, 80 argument roles, and 27 entity types, with 245 (event\_type, role)$\to$allowed\_entity\_types constraints.
412	The grammar layer targets EV (event vocabulary), RoV (role vocabulary), and ET; the semantic layer enforces AC (argument constraint) via role-conditioned masking, analogous to RE domain/range enforcement.
413	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1300aa9-6fb8-472b-87e1-0110267c83cd",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "ccd2b0fd-24d8-4786-b4fb-e36ca73b551e",
  "sourceToolAssistantUUID": "a1300aa9-6fb8-472b-87e1-0110267c83cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-18T17:32:53.907Z_

Now let me also check how many references are actually in the bibliography.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccd2b0fd-24d8-4786-b4fb-e36ca73b551e",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbASAAt1ZSiQojqLrpJ3R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f128fcc8-35a8-4e9a-b5a5-eff13f666b7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SUcPxFPnPw4vs34tVdvZJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18016,
      "cache_read_input_tokens": 63396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18016,
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

_source line 58 · 2026-05-18T17:32:56.255Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018ZZKdaE6YeB78omAMDG9Yy`</summary>

```json
{
  "command": "grep -c '@' /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib",
  "description": "Count bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f128fcc8-35a8-4e9a-b5a5-eff13f666b7d",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbASAAt1ZSiQojqLrpJ3R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6a4784a-f7d2-4e78-b14a-950b71b9e07a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SUcPxFPnPw4vs34tVdvZJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18016,
      "cache_read_input_tokens": 63396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18016,
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

_source line 59 · 2026-05-18T17:32:56.467Z_

<details><summary>↩ Tool result · `toolu_018ZZKdaE6YeB78omAMDG9Yy`</summary>

```text
59
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6a4784a-f7d2-4e78-b14a-950b71b9e07a",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "2be8a318-0701-48bf-a313-2af299f32191",
  "sourceToolAssistantUUID": "c6a4784a-f7d2-4e78-b14a-950b71b9e07a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-18T17:32:57.254Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01C2eynQTh4Z86uDoJT4y1TU`</summary>

```json
{
  "pattern": "@(inproceedings|article|misc)\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2be8a318-0701-48bf-a313-2af299f32191",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbASAAt1ZSiQojqLrpJ3R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a618cabb-262e-46d7-bf08-ebfe1ff9497c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SUcPxFPnPw4vs34tVdvZJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18016,
      "cache_read_input_tokens": 63396,
      "output_tokens": 264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18016
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 264,
          "cache_read_input_tokens": 63396,
          "cache_creation_input_tokens": 18016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18016,
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

_source line 61 · 2026-05-18T17:32:57.277Z_

<details><summary>↩ Tool result · `toolu_01C2eynQTh4Z86uDoJT4y1TU`</summary>

```text
59

Found 0 total occurrences across 0 files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a618cabb-262e-46d7-bf08-ebfe1ff9497c",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "1c3d5759-8005-4e3c-8aef-297067e4bd77",
  "sourceToolAssistantUUID": "a618cabb-262e-46d7-bf08-ebfe1ff9497c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-18T17:33:00.851Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015mYNo2ZWQzvNxbHFo6u4f2`</summary>

```json
{
  "pattern": "@(inproceedings|article|misc|book|phdthesis)\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib",
  "output_mode": "content",
  "head_limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c3d5759-8005-4e3c-8aef-297067e4bd77",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbASAg99NXvDiAFtdvUi9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6bce223e-57ae-4b02-91ae-e0abc69b7ac4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016svGmVcghAnjHuRvkednPg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 81412,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 341
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 81412,
          "cache_creation_input_tokens": 341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 341,
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

_source line 63 · 2026-05-18T17:33:00.883Z_

<details><summary>↩ Tool result · `toolu_015mYNo2ZWQzvNxbHFo6u4f2`</summary>

```text
8:@inproceedings{synchromesh_iclr2022,
17:@inproceedings{mgd_neurips2023,
27:@article{pldi2025_type_constrained_codegen,
40:@inproceedings{roth_yih_2004,
51:@inproceedings{adakgc_emnlp2023,
61:@inproceedings{knowcoder_acl2024,
72:@article{spires_2024,
85:@misc{ontologx_2025,
96:@inproceedings{ekaw2024_ontology_beam,
113:@inproceedings{scholak2021picard,
122:@article{olasunkanmi2025relate,
131:@article{zhou2026ontologytools,
140:@inproceedings{eberts2020spert,
153:@inproceedings{yan2021pfn,
163:@inproceedings{zhong2021frustratingly,
175:@inproceedings{ye2022packed,
187:@article{zhou2026snowballing,
200:@inproceedings{dong2025xgrammar,
209:@article{willard2023outlines,
218:@inproceedings{beurer-kellner2023lmql,
227:@inproceedings{beurer-kellner2024domino,
239:@inproceedings{park2024grammar,
248:@inproceedings{decao2021genre,
257:@inproceedings{josifoski2022genie,
267:@inproceedings{geng2023gcd,
276:@inproceedings{lu2021neurologic,
286:@inproceedings{lu2022uie,
300:@inproceedings{sainz2024gollie,
309:@inproceedings{li2023codeie,
320:@inproceedings{qi2024adelie,
331:@article{zaratiana2024enrico,
341:@article{khorshidi2025odke,
350:@inproceedings{upadhyay2023openie,
359:@inproceedings{regino2025kgcurator,
370:@inproceedings{tam2024letmespeak,
381:@inproceedings{banerjee2025crane,
391:@inproceedings{schall2025hiddencost,
405:@misc{guidance2023,
414:@inproceedings{paolini2021tanl,
423:@inproceedings{cabot2021rebel,
433:@inproceedings{xie2016tkrl,
448:@inproceedings{ugare2024syncode,
459:@inproceedings{ugare2025itergen,
468:@inproceedings{boostcd2025,
481:@inproceedings{luan2018scierc,
492:@inproceedings{yao2019docred,
503:@article{wei2023zeroshot,
512:@article{qwen2025qwen3,
521:@inproceedings{zheng2024sglang,
531:@inproceedings{zaratiana2023gliner,
540:@inproceedings{li2021document,
550:@inproceedings{vukovic2024dore,
563:@inproceedings{grammar_aligned_2024,
571:@article{formattax2026,
579:@article{dccd2026,
587:@inproceedings{slot2025,
597:@inproceedings{guidex2025,
606:@inproceedings{schema_rl2025,
616:@article{jsonschemabench2025,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bce223e-57ae-4b02-91ae-e0abc69b7ac4",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "14b6a8b2-4294-405b-b5f5-b031a3cb22e3",
  "sourceToolAssistantUUID": "6bce223e-57ae-4b02-91ae-e0abc69b7ac4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-18T17:33:03.896Z_

Good. Let me now read the remaining bib entries I haven't seen yet and check for any citations used in the main text that might be missing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14b6a8b2-4294-405b-b5f5-b031a3cb22e3",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbASAwc5Ny1TQSBfrRAvP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98d46cfb-cc1b-4cfc-9068-23f5ccb339b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LV41Gz8FxAD4YJRaUEoVHR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 81753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1108,
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

_source line 65 · 2026-05-18T17:33:04.684Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VUMYzprrLPnAnhtXM78o6J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib",
  "offset": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98d46cfb-cc1b-4cfc-9068-23f5ccb339b3",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbASAwc5Ny1TQSBfrRAvP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25998de9-5525-4618-93be-4093ba8e4e2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LV41Gz8FxAD4YJRaUEoVHR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 81753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1108,
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

_source line 66 · 2026-05-18T17:33:04.708Z_

<details><summary>↩ Tool result · `toolu_01VUMYzprrLPnAnhtXM78o6J`</summary>

```text
500	}
501	
502	% Confirmed via: arXiv:2302.10205, Semantic Scholar
503	@article{wei2023zeroshot,
504	  title   = {{ChatIE}: Zero-Shot Information Extraction via Chatting with {ChatGPT}},
505	  author  = {Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and Huang, Shen and Xie, Pengjun and Xu, Jinan and Chen, Yufeng and Zhang, Meishan and Jiang, Yong and Han, Wenjuan},
506	  journal = {arXiv preprint arXiv:2302.10205},
507	  year    = {2023},
508	  url     = {https://arxiv.org/abs/2302.10205}
509	}
510	
511	% Confirmed via: arXiv:2505.09388, Hugging Face model cards
512	@article{qwen2025qwen3,
513	  title   = {Qwen3 Technical Report},
514	  author  = {{Qwen Team}},
515	  journal = {arXiv preprint arXiv:2505.09388},
516	  year    = {2025},
517	  url     = {https://arxiv.org/abs/2505.09388}
518	}
519	
520	% Confirmed via: NeurIPS 2024 proceedings, arXiv:2312.07104
521	@inproceedings{zheng2024sglang,
522	  title     = {{SGLang}: Efficient Execution of Structured Language Model Programs},
523	  author    = {Zheng, Lianmin and Yin, Liangsheng and Xie, Zhiqiang and Sun, Chuyue and Huang, Jeff and Yu, Cody Hao and Cao, Shiyi and Kozyrakis, Christos and Stoica, Ion and Gonzalez, Joseph E. and Barrett, Clark and Sheng, Ying},
524	  booktitle = {Advances in Neural Information Processing Systems},
525	  volume    = {37},
526	  year      = {2024},
527	  url       = {https://arxiv.org/abs/2312.07104}
528	}
529	
530	% Confirmed via: arXiv, ACL 2024
531	@inproceedings{zaratiana2023gliner,
532	  title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},
533	  author    = {Zaratiana, Urchade and Ngoudi, Nadi and Aziziaden, Amir and Conf, Caleb},
534	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
535	  year      = {2024},
536	  url       = {https://arxiv.org/abs/2311.08526}
537	}
538	
539	% Confirmed via: ACL Anthology 2021.naacl-main.69
540	@inproceedings{li2021document,
541	  title     = {Document-Level Event Argument Extraction by Conditional Generation},
542	  author    = {Li, Sha and Ji, Heng and Han, Jiawei},
543	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
544	  pages     = {894--908},
545	  year      = {2021},
546	  url       = {https://aclanthology.org/2021.naacl-main.69/}
547	}
548	
549	% Confirmed via: ACL Anthology, SIGDIAL 2024
550	@inproceedings{vukovic2024dore,
551	  title     = {{DORE}: A Dataset for {Portuguese} Knowledge Graph Construction and a Reproduction of a {LLM}-based Ontology-Constrained Approach},
552	  author    = {Vukovi{\'c}, Mila and Prange, Jakob and Navigli, Roberto},
553	  booktitle = {Proceedings of the 25th Annual Meeting of the Special Interest Group on Discourse and Dialogue (SIGDIAL)},
554	  pages     = {291--303},
555	  year      = {2024},
556	  url       = {https://aclanthology.org/2024.sigdial-1.25/}
557	}
558	
559	% ============================================================
560	% New citations added 2026-05-18 (literature freshness check)
561	% ============================================================
562	
563	@inproceedings{grammar_aligned_2024,
564	    author    = {Kanghee Park and Jiayu Wang and Taylor Berg-Kirkpatrick and Nadia Polikarpova and Loris D'Antoni},
565	    title     = {Grammar-Aligned Decoding},
566	    booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS 2024)},
567	    year      = {2024},
568	    url       = {https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html},
569	}
570	
571	@article{formattax2026,
572	    author    = {Ivan Lee and Loris D'Antoni and Taylor Berg-Kirkpatrick},
573	    title     = {The Format Tax},
574	    journal   = {arXiv preprint arXiv:2604.03616},
575	    year      = {2026},
576	    url       = {https://arxiv.org/abs/2604.03616},
577	}
578	
579	@article{dccd2026,
580	    author    = {Avinash Reddy and Thayne T. Walker and James S. Ide and Amrit Singh Bedi},
581	    title     = {Draft-Conditioned Constrained Decoding for Structured Generation in {LLMs}},
582	    journal   = {arXiv preprint arXiv:2603.03305},
583	    year      = {2026},
584	    url       = {https://arxiv.org/abs/2603.03305},
585	}
586	
587	@inproceedings{slot2025,
588	    author    = {Zhengyuan Shen and Darren Yow-Bang Wang and Soumya Smruti Mishra and Zhichao Xu and Yifei Teng and Haibo Ding},
589	    title     = {{SLOT}: Structuring the Output of Large Language Models},
590	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},
591	    year      = {2025},
592	    pages     = {472--491},
593	    publisher = {Association for Computational Linguistics},
594	    url       = {https://aclanthology.org/2025.emnlp-industry.32/},
595	}
596	
597	@inproceedings{guidex2025,
598	    author    = {Neil De La Fuente and Oscar Sainz and Iker Garc{\'\i}a-Ferrero and Eneko Agirre},
599	    title     = {{GUIDEX}: Guided Synthetic Data Generation for Zero-Shot Information Extraction},
600	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
601	    year      = {2025},
602	    publisher = {Association for Computational Linguistics},
603	    url       = {https://aclanthology.org/2025.findings-acl.1245/},
604	}
605	
606	@inproceedings{schema_rl2025,
607	    author    = {Yaxi Lu and Haolun Li and Xin Cong and Zhong Zhang and Yesai Wu and Yankai Lin and Zhiyuan Liu and Fangming Liu and Maosong Sun},
608	    title     = {Learning to Generate Structured Output with Schema Reinforcement Learning},
609	    booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},
610	    year      = {2025},
611	    pages     = {4905--4918},
612	    publisher = {Association for Computational Linguistics},
613	    url       = {https://aclanthology.org/2025.acl-long.243/},
614	}
615	
616	@article{jsonschemabench2025,
617	    author    = {Saibo Geng and Hudson Cooper and Micha{\l} Moskal and Samuel Jenkins and Julian Berman and Nathan Ranchin and Robert West and Eric Horvitz and Harsha Nori},
618	    title     = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},
619	    journal   = {arXiv preprint arXiv:2501.10868},
620	    year      = {2025},
621	    url       = {https://arxiv.org/abs/2501.10868},
622	}
623	
624	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25998de9-5525-4618-93be-4093ba8e4e2f",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "61f745d3-ee9f-4619-8c26-60b16c9eea52",
  "sourceToolAssistantUUID": "25998de9-5525-4618-93be-4093ba8e4e2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-18T17:33:08.204Z_

I now have a comprehensive understanding of the paper. Let me also check if there's a 70B results section or any additional data I should consider.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61f745d3-ee9f-4619-8c26-60b16c9eea52",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbASBEJAkaMRmiLTNJfsA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fdfb1dbe-a8ff-47aa-be5d-773645e67936",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R7gT9BxbJ6ogDKioMu9R33",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2542,
      "cache_read_input_tokens": 82861,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2542,
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

_source line 68 · 2026-05-18T17:33:09.085Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01BLLbFwtZwFe2MLUcad1PHx`</summary>

```json
{
  "pattern": "70B|70b",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "head_limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdfb1dbe-a8ff-47aa-be5d-773645e67936",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbASBEJAkaMRmiLTNJfsA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd7cddac-3ebb-474f-85c8-581b2aa53ecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R7gT9BxbJ6ogDKioMu9R33",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2542,
      "cache_read_input_tokens": 82861,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2542
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 82861,
          "cache_creation_input_tokens": 2542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2542,
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

_source line 69 · 2026-05-18T17:33:09.120Z_

<details><summary>↩ Tool result · `toolu_01BLLbFwtZwFe2MLUcad1PHx`</summary>

```text
artifacts/_project/paper/p3_case_studies_861a0d.tex:17:% Source: ICCV_2003_161_abs_sent4, 70B Qwen unconstrained vs constrained
artifacts/_project/paper/p3_case_studies_861a0d.tex:90:% CASE STUDY 3: 70B vs 8B Violation Comparison
artifacts/_project/paper/p3_case_studies_861a0d.tex:91:% Shows that 70B unconstrained already has lower violations
artifacts/_project/paper/p3_case_studies_861a0d.tex:98:\noindent This sentence contains Metric entities (BLEU, NIST, WER, PER) related to ``MT evaluation methods'' via Hyponym-of. Both 8B and 70B models mistype ``MT evaluation methods'' as \textsc{Method} (gold: \textsc{Metric}), but the downstream constraint behavior differs.
artifacts/_project/paper/p3_case_studies_861a0d.tex:103:\caption{Case~3: 8B vs 70B behavior on the same input. 8B generates 4 Hyponym-of(Method, Metric) violations; 70B generates Part-of(Metric, Method) violations that OntoCoDec corrects by adjusting ``MT evaluation methods'' to Generic.}
artifacts/_project/paper/p3_case_studies_861a0d.tex:120:\multicolumn{4}{@{}l}{\textit{Qwen 70B Unconstrained}} \\
artifacts/_project/paper/p3_case_studies_861a0d.tex:124:\multicolumn{4}{@{}l}{\textit{Qwen 70B OntoCoDec}} \\
artifacts/_project/paper/main.tex:75:All models tested are 7--8B-parameter class; scaling behavior to larger (70B+) or smaller models has not been verified, and the dual-factor pattern's predictive scope may differ at other scales.
artifacts/_project/paper/p3_case_studies.tex:17:% Source: ICCV_2003_161_abs_sent4, 70B Qwen unconstrained vs constrained
artifacts/_project/paper/p3_case_studies.tex:90:% CASE STUDY 3: 70B vs 8B Violation Comparison
artifacts/_project/paper/p3_case_studies.tex:91:% Shows that 70B unconstrained already has lower violations
artifacts/_project/paper/p3_case_studies.tex:98:\noindent This sentence contains Metric entities (BLEU, NIST, WER, PER) related to ``MT evaluation methods'' via Hyponym-of. Both 8B and 70B models mistype ``MT evaluation methods'' as \textsc{Method} (gold: \textsc{Metric}), but the downstream constraint behavior differs.
artifacts/_project/paper/p3_case_studies.tex:103:\caption{Case~3: 8B vs 70B behavior on the same input. 8B generates 4 Hyponym-of(Method, Metric) violations; 70B generates Part-of(Metric, Method) violations that OntoCoDec corrects by adjusting ``MT evaluation methods'' to Generic.}
artifacts/_project/paper/p3_case_studies.tex:120:\multicolumn{4}{@{}l}{\textit{Qwen 70B Unconstrained}} \\
artifacts/_project/paper/p3_case_studies.tex:124:\multicolumn{4}{@{}l}{\textit{Qwen 70B OntoCoDec}} \\
artifacts/_project/paper/main.fdb_latexmk:61:  "/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb" 1248133631 36094 798f80770b3b148ceedd006d487db67c ""
artifacts/_project/paper/section7_conclusion_550cbf.tex:33:(1)~Cross-model validation on architectures such as Llama-3.1-8B and quantized 70B-class models to verify model-agnostic generalization.
artifacts/_project/paper/main.aux:2531:\@writefile{lot}{\contentsline {table}{\numberline {23}{\ignorespaces 8B vs.\ 70B on the same input. OntoCoDec corrects violations at both scales; CF arises when type corrections conflict with entity-list assignments.}}{27}{table.caption.94}\protected@file@percent }
artifacts/_project/paper/main.aux:2532:\newlabel{tab:case3}{{23}{27}{8B vs.\ 70B on the same input. OntoCoDec corrects violations at both scales; CF arises when type corrections conflict with entity-list assignments}{table.caption.94}{}}
artifacts/_project/paper/section7_conclusion.tex:39:(1)~Extension to larger models (quantized 70B-class) to further verify model-agnostic generalization across scales.
artifacts/_project/paper/appendix_case_studies.tex:80:Both Qwen3-8B and Llama-3.1-70B-Instruct (AWQ INT4) mistype ``MT evaluation methods'' as \textsc{Method} (gold: \textsc{Metric}), but the downstream constraint behavior differs (Table~\ref{tab:case3}). The 70B model produces fewer violations (2 vs.\ 4) and chooses a different relation (Part-of vs.\ Hyponym-of), yet OntoCoDec corrects both.
artifacts/_project/paper/appendix_case_studies.tex:85:\caption{8B vs.\ 70B on the same input. OntoCoDec corrects violations at both scales; CF arises when type corrections conflict with entity-list assignments.}
artifacts/_project/paper/appendix_case_studies.tex:102:\multicolumn{4}{@{}l}{\textit{Llama-3.1-70B Unconstrained}} \\
artifacts/_project/paper/appendix_case_studies.tex:106:\multicolumn{4}{@{}l}{\textit{Llama-3.1-70B OntoCoDec}} \\
artifacts/_project/paper/section5_runtime.tex:14:% === 70B cross-scale (PLACEHOLDER — awaiting DocRED 70B results) ===
artifacts/_project/paper/section5_runtime.tex:16:%\label{sec:70b-results}
artifacts/_project/paper/section5_runtime.tex:17:%To evaluate cross-scale generalizability, we test OntoCoDec on Llama-3.1-70B-Instruct (AWQ INT4 quantization).
artifacts/_project/paper/section5_runtime.tex:18:%On SciERC, the 70B model produces fewer baseline violations than its 8B counterpart (DR 6.5\% vs.\ 13.3\%), yet violations persist; OntoCoDec eliminates them entirely (DR$\to$0\%, R-F1 $-$0.03\,pp).
artifacts/_project/paper/section5_runtime.tex:19:%On DocRED, [PLACEHOLDER for 70B DocRED results].
artifacts/_project/paper/section5_runtime.tex:20:%Case studies comparing 8B and 70B behavior appear in Appendix~\ref{app:case-scale}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd7cddac-3ebb-474f-85c8-581b2aa53ecf",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "4f57abaa-8b4d-46c3-9b90-d88a41bab00d",
  "sourceToolAssistantUUID": "bd7cddac-3ebb-474f-85c8-581b2aa53ecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-18T17:33:12.028Z_

Now I have a thorough understanding of the entire paper. Let me also quickly check the prompt sensitivity appendix and the FT composability section on DocRED.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f57abaa-8b4d-46c3-9b90-d88a41bab00d",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbASBYY2jkptUPYH9oN5e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2bb23ea-1996-4cbe-a820-652bafa7096d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019FEb3fi33MnQfSYvUs6jZH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2009,
      "cache_read_input_tokens": 85403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2009,
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

_source line 71 · 2026-05-18T17:33:12.704Z_

<details open><summary>🔧 Tool call — Read · `toolu_013QFdUuAdpvHPFhMdsL2K4h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2bb23ea-1996-4cbe-a820-652bafa7096d",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbASBYY2jkptUPYH9oN5e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89ce9d59-24bd-4d1a-9a94-2fa786d32f37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019FEb3fi33MnQfSYvUs6jZH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2009,
      "cache_read_input_tokens": 85403,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2009
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 85403,
          "cache_creation_input_tokens": 2009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2009,
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

_source line 72 · 2026-05-18T17:33:12.716Z_

<details><summary>↩ Tool result · `toolu_013QFdUuAdpvHPFhMdsL2K4h`</summary>

```text
1	\section{Prompt Sensitivity Analysis}
2	\label{app:prompt-sensitivity}
3	
4	To verify that OntoCoDec's constraint enforcement is robust to prompt variation, we evaluate three prompt variants on SciERC using Qwen3-8B (551 test documents): \textbf{Default} (the prompt used in all main experiments), \textbf{Minimal} (a shortened version listing only entity/relation types), and \textbf{Detailed} (an extended version with type definitions and extraction guidelines). All three variants share the same output JSON schema; only the instruction text differs. Each variant is decoded in both unconstrained and constrained (full Stage~1) modes.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Prompt sensitivity results on SciERC. ET, RV, DR denote entity-type, relation-vocabulary, and domain-range violation rates (\%), respectively. $\Delta$DR shows the relative reduction from unconstrained to constrained decoding.}
10	\label{tab:prompt-sensitivity}
11	\begin{tabular}{llcccccc}
12	\toprule
13	\textbf{Prompt} & \textbf{Mode} & \textbf{ET\%} & \textbf{RV\%} & \textbf{DR\%} & \textbf{$\Delta$DR} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	\multirow{2}{*}{Default}
16	  & Unconstrained & 0.40 & 1.39 & 15.37 & \multirow{2}{*}{94.0\%} & 31.01 & 8.23 \\
17	  & Constrained   & 0.00 & 0.00 &  0.93 &                         & 30.98 & 8.36 \\
18	\midrule
19	\multirow{2}{*}{Minimal}
20	  & Unconstrained & 0.58 & 1.16 & 16.91 & \multirow{2}{*}{94.6\%} & 31.98 & 7.91 \\
21	  & Constrained   & 0.00 & 0.00 &  0.92 &                         & 31.99 & 7.85 \\
22	\midrule
23	\multirow{2}{*}{Detailed}
24	  & Unconstrained & 0.22 & 0.45 & 11.07 & \multirow{2}{*}{94.2\%} & 33.55 & 10.48 \\
25	  & Constrained   & 0.00 & 0.00 &  0.64 &                         & 33.56 & 10.48 \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:prompt-sensitivity} shows that constrained decoding eliminates entity-type and relation-vocabulary violations entirely (ET and RV drop to 0\%) for all three prompt variants. Domain-range violations are reduced by 94.0\%--94.6\%, with a standard deviation of only 0.3 percentage points across prompts. Meanwhile, F1 scores remain effectively unchanged: the largest shift is 0.13 percentage points (R-F1, Default prompt), confirming that constraint enforcement does not degrade extraction quality.
31	
32	Notably, prompt variation has a measurable effect on baseline (unconstrained) violation rates, with DR ranging from 11.1\% (Detailed) to 16.9\% (Minimal). Under constrained decoding, this range narrows to 0.64\%--0.93\%, a 20$\times$ reduction in cross-prompt variance. This convergence is expected: because OntoCoDec enforces constraints at the token level during decoding, it operates independently of prompt content. The consistent reduction rates across diverse prompt styles confirm that the mechanism is orthogonal to prompting and generalizes without prompt-specific tuning.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89ce9d59-24bd-4d1a-9a94-2fa786d32f37",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "39f407eb-66ca-4413-9e91-cae820ee41e3",
  "sourceToolAssistantUUID": "89ce9d59-24bd-4d1a-9a94-2fa786d32f37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 73 · 2026-05-18T17:33:16.401Z_

I now have all the information needed to write a comprehensive review. Let me now compose it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39f407eb-66ca-4413-9e91-cae820ee41e3",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbASBpzUoc93sGSqyowPD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "179fe6d9-24c3-4933-83ae-0522ddbede4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pssuyv2hY6AwT88uViqKJ1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1177,
      "cache_read_input_tokens": 87412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1177,
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

_source line 74 · 2026-05-18T17:33:16.760Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Gey198gPrMDN9vnNQAXib7`</summary>

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
  "parentUuid": "179fe6d9-24c3-4933-83ae-0522ddbede4d",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbASBpzUoc93sGSqyowPD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41cc04ee-cedb-484a-8f8f-77f2b11d6805",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pssuyv2hY6AwT88uViqKJ1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1177,
      "cache_read_input_tokens": 87412,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1177
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 87412,
          "cache_creation_input_tokens": 1177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1177,
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

_source line 75 · 2026-05-18T17:33:16.762Z_

<details><summary>↩ Tool result · `toolu_01Gey198gPrMDN9vnNQAXib7`</summary>

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
  "parentUuid": "41cc04ee-cedb-484a-8f8f-77f2b11d6805",
  "isSidechain": true,
  "promptId": "d3d3ba7b-eeaf-48bd-8ca0-460d6a53d3fd",
  "agentId": "ab33643faef5b2735",
  "type": "user",
  "uuid": "f3f80e1f-23f6-474d-9af1-f3a72f009201",
  "sourceToolAssistantUUID": "41cc04ee-cedb-484a-8f8f-77f2b11d6805",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 76 · 2026-05-18T17:35:11.372Z_



Here is my detailed review as Reviewer R2 (Novelty/Contribution and Related Work Positioning).

---

## Review: "OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints"

### 1. Novelty Assessment

**Prefix-decidability taxonomy.** The three-way classification (local, prefix-decidable with state, non-local) is a clean formalization, but it is not deeply novel. The observation that some constraints can be checked locally, some require accumulated state, and some require future information is a standard distinction in compiler theory and incremental parsing (cf. attribute grammars, L-attributed vs S-attributed definitions). PICARD (Scholak et al., 2021) already implements essentially the same insight for SQL: check constraints incrementally as the prefix grows, reject tokens that violate schema rules given what has been decoded so far. The taxonomy is a useful organizational device for the paper but does not constitute a standalone intellectual contribution. It would be stronger if it came with formal decidability results or complexity analysis rather than informal classification.

**OntoCoDec as a system.** The method is a composition of two known techniques: (1) CFG-based logit masking via XGrammar for structural validity, and (2) a stateful logits processor that performs lookup-table masking for domain/range constraints. The bitwise AND composition is straightforward. The entity registry is a dictionary populated during generation. The continuation masking for multi-token types is a practical engineering solution but not algorithmically novel (prefix-tree based disambiguation is standard in trie-constrained decoding, e.g., GENRE, GenIE). The paper's own framing acknowledges the close mechanistic analogy to type-constrained code generation (Mundler et al., PLDI 2025), and the differentiation ("IE requires a dynamic entity registry") is valid but incremental: the core idea of compiling type constraints into token masks is directly borrowed.

**Empirical study as contribution.** This is the strongest novelty claim. The systematic measurement of violation rates across datasets, models, and constraint configurations, the dual-factor characterization (tightness x baseline RV), the CF-DR trade-off analysis, and the cross-task generalization to EE are all genuinely useful empirical contributions. The finding that grammar-only constraints *increase* measured DR on DocRED by surfacing latent violations is a non-obvious insight. However, the "constraint tightness determines violation severity" finding, while well-quantified, is somewhat expected: tighter constraints are harder to satisfy, so violations are more frequent. The dual-factor pattern (tightness x RV baseline) is more interesting but is characterized on only 4 data points with p=0.058, which the authors correctly note is descriptive rather than confirmatory.

**Verdict on novelty:** The method is incremental (composition of known techniques adapted to a new domain). The empirical study is the primary contribution, and it is thorough and well-executed. The question is whether this combination meets the bar for a top venue.

### 2. Related Work Adequacy

**Reference count and coverage.** The bibliography contains 59 entries, which is adequate for this type of paper. The earlier claim of "only 2 references" in the task description appears to be outdated or incorrect; the actual paper has extensive citations. The extended related work in Appendix B is comprehensive, covering five paradigms with detailed positioning.

**Important missing references and gaps:**

- **Structured prediction with constraints (pre-neural).** Roth & Yih (2004) is cited, which is good. However, the broader ILP/constrained structured prediction literature is underrepresented. Work on global inference with constraints in IE (e.g., Li & Roth 2002 on entity-relation constraint propagation, Punyakanok et al. 2004/2008 on the importance of inference in NLP) would strengthen the historical lineage argument. The paper presents constraint enforcement for IE as if it were a new idea, when in fact it was standard practice in pre-neural IE that was abandoned in the neural era. This history deserves more than one sentence.

- **Knowledge graph completion with type constraints.** The paper does not cite the substantial KGC literature on type-constrained link prediction (e.g., TransE variants with type constraints, TKRL (Xie et al., 2016, which is in the bib but not cited in the text), TypeComplex, TypeDistMult). These methods enforce similar domain/range constraints during KG construction and are conceptually related.

- **Constrained beam search beyond NeuroLogic.** The paper cites NeuroLogic Decoding but does not discuss constrained beam search methods more broadly, including work on lexically constrained generation (Post & Vilar 2018, Hokamp & Liu 2017), which pioneered token-level constraint enforcement during autoregressive decoding.

- **Neuro-symbolic IE.** The paper does not engage with the neuro-symbolic reasoning literature that combines neural models with symbolic constraint satisfaction (e.g., DeepProbLog, Logic Tensor Networks, NeurASP). While these operate differently, the intellectual connection of enforcing logical constraints on neural outputs is directly relevant.

- **Semantic parsing with type checking.** Beyond PICARD and Synchromesh, there is work on type-safe semantic parsing (e.g., Krishnamurthy et al. 2017 on neural semantic parsing with type constraints) that is not discussed.

**Positioning accuracy.** The differentiation from grammar-constrained decoding (Willard & Louf, XGrammar) is clear and accurate: those methods handle CFG-expressible constraints; OntoCoDec adds cross-field semantic constraints. The differentiation from type-constrained code generation is valid but could be sharper. The paper claims the entity registry is the key difference (types inferred from text vs. declared), which is true, but the actual registry implementation is a simple dictionary, not a fundamentally new mechanism.

**Fairness of positioning.** The paper is generally fair. One concern: the framing of GoLLIE, CodeIE, and KnowCoder as providing "only soft guidance" slightly undersells these approaches. GoLLIE's Python dataclass formulation does provide a form of type structure, and KnowCoder's class hierarchy is a meaningful constraint mechanism. The distinction (soft learned preference vs. hard decoding-time guarantee) is valid but should be stated more precisely.

### 3. Contribution Significance

**70B scale results.** The 70B results mentioned in the task prompt (SciERC DR 6.5% to 0%, DocRED DR 1.8% to 0.3%) appear to be placeholder/in-progress data. The submitted paper explicitly states in Limitations that "scaling behavior to larger (70B+) or smaller models has not been verified." The 70B cross-scale section is commented out with placeholders. This is a notable gap: demonstrating that the approach scales to 70B would strengthen the paper, but the current version does not include these results in the main tables.

**Net value at 70B on DocRED.** Based on the task prompt numbers (DR 1.8% to 0.3% with 3.8% CF introduced), the trade-off is questionable. The method eliminates 1.5pp of DR violations but introduces 3.8pp of CF violations. Whether this is net positive depends entirely on downstream impact: DR violations produce structurally invalid triples, while CF violations produce internally inconsistent but individually valid triples. The paper's argument that DR is "harder" than CF is reasonable but not empirically validated for downstream tasks.

**"Type checking for neural generation" framing.** This is compelling as a conceptual contribution. Drawing the analogy between programming language type systems and IE ontology constraints is a productive intellectual connection. However, this framing has been explored in code generation (the paper's own cited references), and migrating it to IE, while useful, is a domain adaptation rather than a conceptual breakthrough.

**Engineering vs. research contribution.** The method is primarily engineering: identifying that existing grammar-constrained decoding is insufficient for IE, designing a two-layer system with a stateful registry, and implementing it with tokenizer-agnostic continuation masking. The research contribution lies in the empirical characterization of the violation landscape and the analysis of when/why constraints help or trade off. The CF-DR trade-off analysis and the dual-factor characterization are genuine analytical insights. The composability with fine-tuning and beam search are useful practical findings. Overall, this sits on the boundary: it is a strong engineering contribution with meaningful empirical analysis, but the methodological novelty is limited.

### 4. Strengths

- **Thorough experimental design.** 3 models x 3 datasets (2 RE + 1 EE), 5-way ablation on SciERC, 4-way on DocRED, cross-model validation, composability with fine-tuning, beam search, prompt sensitivity, latency profiling. This is unusually comprehensive for this type of paper.

- **Honest reporting of limitations.** The CF trade-off is proactively disclosed with detailed analysis (CF-DR ablation, per-pair distribution, root cause attribution to schema ambiguity). The paper does not hide that post-hoc filtering achieves higher F1 in 5/6 zero-shot settings. This transparency is commendable.

- **Cross-task generalization to EE.** Demonstrating that the same framework works on WikiEvents event extraction without architectural modification is a strong generality argument. The grammar-only ablation on EE clearly shows layer complementarity (grammar kills EV but not RoV; semantic kills RoV).

- **Post-hoc filtering baseline.** Including this baseline with detailed analysis (rejection rates, TP loss, recall impact) provides a fair comparison that many papers in this area omit.

- **Bootstrap confidence intervals.** Statistical rigor with 10,000-iteration bootstrap CIs for all F1 comparisons, with p-values reported. This is above average for the field.

- **Composability with fine-tuning is practically important.** Showing DR drops to 0.01-0.20% with LoRA + S1 and R-F1 within +/-0.6pp demonstrates the method's utility in realistic deployment scenarios, not just zero-shot.

- **Prompt sensitivity analysis.** DR reduction is 94.0-94.6% across three prompt variants (sigma=0.3pp), demonstrating orthogonality to prompt design.

### 5. Weaknesses

- **Limited methodological novelty.** The core method is a composition of XGrammar (existing) + lookup-table logit masking (straightforward). The entity registry is a dictionary. The continuation masking is a prefix tree. None of these components are individually novel, and their composition, while useful, is engineering rather than research. The "enabling dependency" (grammar must run first so semantic can look up valid types) is a natural design decision, not a deep insight.

- **CF trade-off undermines the core value proposition.** The paper claims to provide "type-safety guarantees," but the method introduces 2.57-12.02% CF violations in zero-shot settings. CF violations mean the same entity gets different types across triples, which can be equally problematic for downstream KG construction. The paper argues DR is "harder" than CF, but this hierarchy is asserted rather than empirically validated on actual downstream tasks.

- **Zero-shot F1 is very low (~4-8%).** While the paper correctly frames F1 as a control variable, the extremely low extraction quality raises questions about whether the constraint enforcement is operating in a meaningful regime. At 8% F1, most triples are wrong anyway; the practical value of ensuring the remaining (mostly incorrect) triples have valid types is limited. The fine-tuned results (43-46% R-F1 with DR near 0%) are more convincing, but the bulk of the paper focuses on zero-shot.

- **DocRED Qwen zero-shot: only 45% DR reduction.** On the larger, more realistic dataset, the primary model achieves only 45% DR reduction (18.46% to 10.21%), far from the near-complete elimination claimed on SciERC. The residual 10.21% is explained by constraint tightness and grammar-first fallback, but this means the method's practical effectiveness is highly dataset-dependent. The paper is honest about this but could frame it more prominently.

- **WikiEvents Entity F1 from 0% is a format compliance effect, not semantic improvement.** The paper acknowledges this, but the abstract highlights "Entity F1: 0% to 12-18%" without immediate qualification, which could mislead readers into thinking the method improves extraction quality rather than just enabling parsing.

- **Missing 70B results.** The Limitations section acknowledges this gap. For a paper claiming generality across model scales, having only 7-8B models in the main results is a limitation. The 70B placeholder in section5_runtime.tex is commented out.

- **Dual-factor pattern is descriptive, not predictive.** Characterized on only 4 data points (2 models x 2 datasets for calibrated models) with p=0.058. While suggestive, this cannot be claimed as a validated finding. More model-dataset combinations would be needed.

- **Related work does not adequately acknowledge pre-neural constraint enforcement.** The paper positions constraint enforcement as novel for IE, but ILP-based joint inference with type constraints was standard in pre-neural NLP (Roth & Yih 2004, which is cited, but the broader literature is thin). The "gap" narrative (classical IE had constraints, neural IE lost them, we bring them back) is implicit but could be made explicit and better grounded.

- **No evaluation on non-English ontologies or domains beyond scientific/Wikipedia text.** Generalization claims are based on two RE datasets (scientific abstracts, Wikipedia) and one EE dataset (news). Biomedical IE, legal IE, or non-English datasets would strengthen the practical impact story.

### 6. Questions for Authors

1. **CF downstream impact.** Have you evaluated whether CF violations actually cause problems in a downstream task (e.g., knowledge graph construction, question answering over extracted triples)? The paper's claim that DR is "harder" than CF would be much stronger with even a small downstream evaluation.

2. **Grammar-first fallback frequency.** The appendix mentions Llama triggers 57,825 fallbacks on DocRED (63.8 per document). This means the semantic layer is effectively disabled for a large fraction of type-bearing positions. Can you quantify what fraction of type tokens are actually constrained by the semantic layer vs. falling back to grammar-only across all models and datasets?

3. **Why not global type consensus?** You identify global entity-type consensus as the "most direct resolution path" for CF. Could a simple two-pass approach (first pass: entity extraction with type voting; second pass: relation extraction with fixed types) eliminate CF without the complexity of modifying the autoregressive decoding? How would this compare to S2, which already does two passes but apparently does not solve CF?

4. **Comparison with EnriCo.** EnriCo (Zaratiana et al., 2024) applies ASP constraints at decode time for joint entity-relation extraction. How does OntoCoDec compare in terms of constraint expressiveness and enforcement effectiveness? The paper mentions EnriCo uses "task-specific manually authored rules" but does not provide a direct comparison.

5. **Schema coverage gaps.** The residual DR analysis mentions that 33% of fine-tuned residual violations are due to frequency-based constraint table gaps. Would using the full ontology specification (rather than training-set frequency) eliminate these? If so, why was this not done?

6. **Latency on WikiEvents.** The paper measures latency on SciERC and DocRED but only estimates it for WikiEvents. Given that WikiEvents has a larger ontology (56 event types, 80 roles, 27 entity types), the overhead could be substantially higher. Can you provide measured WikiEvents latency?

### 7. Score: 3.5 (Borderline Conference)

**Justification.** The paper presents a thorough empirical study with an engineering system that is practical and useful. The experimental design is exemplary: multiple models, datasets, ablations, baselines, statistical tests, and honest limitation reporting. However, the methodological novelty is limited (composition of known techniques), the core method introduces a non-trivial CF trade-off that partially undermines its value proposition, and the zero-shot regime where most experiments operate produces very low F1 (4-8%), making the practical significance of constraint enforcement uncertain in that regime. The fine-tuned results (DR near 0%, R-F1 within 0.6pp) are more convincing for practical impact. The related work is comprehensive but could better situate the contribution within the historical arc of constrained inference in NLP. The cross-task generalization to EE is a clear strength. Overall, the work is solid and well-executed, sitting at the boundary between a Findings-level contribution (strong empirics, incremental method) and a main conference paper (which would require either deeper methodological innovation or more surprising empirical findings).

### 8. Confidence: 4/5

I am confident in this assessment. I have expertise in constrained decoding, structured prediction, and information extraction. I have carefully read the full paper including all appendices and experimental details. My main uncertainty is in how the community will weight the empirical thoroughness (which is genuinely above average) against the limited methodological novelty. A reviewer who values comprehensive empirical characterization more heavily might score this 0.5 points higher.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3f80e1f-23f6-474d-9af1-f3a72f009201",
  "isSidechain": true,
  "agentId": "ab33643faef5b2735",
  "requestId": "req_011CbASC7dbhBDc3ENpRK6HK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe6ff96b-ae5b-4a3b-9829-89868a8d0b0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "868768b3-db3e-406d-8db5-3414a391d999",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWXXZWMVYRmFRdD5L3Jvj5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 88589,
      "output_tokens": 4069,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 687
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4069,
          "cache_read_input_tokens": 88589,
          "cache_creation_input_tokens": 687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 687,
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
