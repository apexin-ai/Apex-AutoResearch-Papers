# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Y

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a6ad89e6d8763aafe.jsonl`
- **Structured JSON:** [`f9cdbce390f1554c35e8.json`](../../sessions/f9/f9cdbce390f1554c35e8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-17T17:29:59.010Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus is **Novelty and Related Work**.

## Paper Summary
**Title**: "The Capability Trap: Why Self-Extracted Constraints Cannot Improve LLM Majority Voting"

The paper investigates SICA (Symbolic Invariant Consensus Aggregation), which extracts FOL constraints from K sampled reasoning traces and uses weighted MAX-SAT to select the answer maximizing satisfied constraints. The central finding is negative: SICA provides no significant accuracy gain over Self-Consistency (SC) across 5 model families, 3 reasoning domains, and N>1,300 problems. The authors identify a "capability trap": models producing output diversity (instruction-scale) extract non-discriminative constraints (precision ~0.527, near chance), while models that could extract discriminative constraints (full reasoning models like QwQ-32B) produce near-deterministic outputs (C0<5%), making SICA structurally identical to SC.

**Key contributions claimed**:
1. Systematic study across 5 model families and 3 domains (N>1,300) establishing negative result
2. Identification of "capability trap" (diversity + discriminative constraints never co-occur)
3. Oracle experiment proving bottleneck is extraction quality (+8.82pp with gold FOL)
4. C0 diagnostic metric (C0<5% guarantees SICA=SC)

## Related Work Section (Section 2)
The paper covers 5 subsections:
1. **Self-Consistency and Extensions**: Wang et al. 2023 (SC), Universal SC (Chen et al. 2023), SC scaling (Loo et al. 2025), confidence-weighted voting (Taubenfeld et al. 2025), DiVeRSe (Li et al. 2023)
2. **Neuro-Symbolic Reasoning**: Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), DyLoS, Aristotle, FoVer, LogicAgent. Notes these differ from same-model self-extraction.
3. **Verification and Reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd (Wang et al. 2024). Notes trained verifiers provide discriminative signals.
4. **Test-Time Compute Scaling**: Snell et al. 2025, DeepSeek-R1, OpenAI o1. Extended reasoning chains eliminate diversity.
5. **Constraint Satisfaction in NLP**: SATBench, constraint propagation work.

## Reference List
~25 references total. Includes:
- Core SC papers (Wang et al. 2023, Chen et al. 2023)
- Neuro-symbolic (Logic-LM, LINC)
- Verification (ORM, PRM, Math-Shepherd)
- Scaling (Snell et al. 2025, Loo et al. 2025)
- Datasets (FOLIO, ProofWriter, StrategyQA, ARC)
- Models (Qwen2.5, LLaMA-3, Mistral, DeepSeek-R1, QwQ)
- SAT/constraint (Biere et al. 2021, SATBench, constraint propagation)
- Negative results value (Biswas et al. 2024)

## Your Task
Provide a detailed review focusing on:

1. **Novelty Assessment**: Is the "capability trap" a genuinely new insight? Is the negative result surprising or predictable? Does the paper advance understanding beyond "it doesn't work"?

2. **Related Work Completeness**: Are key related works missing? Is the positioning accurate? Does the paper fairly represent prior work?

3. **Framing and Contribution Clarity**: Is the paper positioned effectively as a negative result / diagnostic study? Would a different framing strengthen the contribution?

4. **Missing Related Work**: Identify specific papers or lines of work that should be cited or discussed.

5. **Impact and Significance**: Would the community benefit from this paper? Does it change how people think about symbolic aggregation?

## Output Format
Provide your review in this exact structure:

### R2 Review: Novelty and Related Work

**Summary**: [2-3 sentences]

**Strengths**:
- S1: ...
- S2: ...
- S3: ...

**Weaknesses**:
- W1: ...
- W2: ...
- W3: ...
- W4: ...

**Missing Related Work**:
- ...

**Questions for Authors**:
- Q1: ...
- Q2: ...

**Framing Suggestions**:
- ...

**Preliminary Score**: [1-6] with brief justification

**Confidence**: [1-5, where 5 = very confident]


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "1cb13cb7-6c08-435b-b47d-025cd729513d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T17:29:59.018Z_

```json
{
  "parentUuid": "1cb13cb7-6c08-435b-b47d-025cd729513d",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
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
  "uuid": "d9a278ca-5f9d-4dd5-aaae-9c0b106f7828",
  "timestamp": "2026-05-17T17:29:59.018Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-17T17:30:01.321Z_



I'll start by reading the full paper and related materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9a278ca-5f9d-4dd5-aaae-9c0b106f7828",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y8ccxHTKCsWKAdGwVD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33d86791-bafc-44fa-a571-cc6d7c650f22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bjp7G1NzuYEqscD5ofqQkr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8257,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8257,
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

_source line 4 · 2026-05-17T17:30:02.354Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HHRjXZDqgu8BvMmvdtJ8qM`</summary>

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
  "parentUuid": "33d86791-bafc-44fa-a571-cc6d7c650f22",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y8ccxHTKCsWKAdGwVD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa95533f-ca8a-4b64-812d-d6957c133526",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bjp7G1NzuYEqscD5ofqQkr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8257,
      "cache_read_input_tokens": 8251,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8257
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 124,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 8257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8257,
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

_source line 5 · 2026-05-17T17:30:02.358Z_

<details><summary>↩ Tool result · `toolu_01HHRjXZDqgu8BvMmvdtJ8qM`</summary>

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
  "parentUuid": "fa95533f-ca8a-4b64-812d-d6957c133526",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "5bdd08c8-194e-45ad-8f63-75bf4e1162d8",
  "sourceToolAssistantUUID": "fa95533f-ca8a-4b64-812d-d6957c133526",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-17T17:30:04.835Z_



Let me read the full paper and supporting materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bdd08c8-194e-45ad-8f63-75bf4e1162d8",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y8ryekWTNjeLmkuSYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "108a81d4-837f-4a0b-97b2-da7e3109ac70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EC5Qsu4BTh3L38hHsM1qM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16508,
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

_source line 7 · 2026-05-17T17:30:05.793Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01QFxsfYWmyteU6uPaYWhSoC`</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "108a81d4-837f-4a0b-97b2-da7e3109ac70",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y8ryekWTNjeLmkuSYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9efa441d-60d7-4d06-a5a0-67268a359f9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EC5Qsu4BTh3L38hHsM1qM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16508,
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

_source line 8 · 2026-05-17T17:30:06.002Z_

<details><summary>↩ Tool result · `toolu_01QFxsfYWmyteU6uPaYWhSoC`</summary>

```text
{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (41 个)\n\n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_constraint_ablation_013**: DONE (success) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-004-qwen7b | Within-family scaling: Qwen2.5-7B-Instruct 在 D012 60 题上 SICA vs SC。弱模型预期 C0 > 14B（更多 diversity），但 constraint quality 预期更低，SICA-SC gap 预期≈0——验证 capability trap 的 scaling 维度。 | — | — | — |\n\n## 待处理\n- smoke-test-5q（准备中）\n\n## 近期结论\n- **exp-012-gsm8k-pilot** (negative): Cross-domain validation: Qwen2.5-14B-Instruct 在 GSM8K (开放答案数学域) 30 题上 SICA vs SC。预期 C0<20%（14B 在 GSM8K 太强），验证 C0 作为 SICA 无效性预测指标。 ← 基于 sica_expanded_14b\n- **exp-021-oracle-folio** (success): If we replace self-extracted constraints with gold FOL annotations verified by Z3, Oracle-SICA should significantly outperform both SC and SICA, demonstrating that constraint quality is the bottleneck for SICA gains on formal logic tasks. ← 基于 sica_expanded_14b\n  [exp021_oracle_folio_results](/api/workspace-files/projects/symb_invariant_consensus/artifacts/exp-021-oracle-folio/data/exp021_summary.txt)\n- **temperature-ablation-t10** (negative): Temperature ablation T=1.0: 高温下 Qwen2.5-14B trace diversity 最大化（C0 预期>60%），SICA-SC gap 预期≈0 或负——验证最大 diversity 仍不能拯救 SICA，因为 constraint discriminative power 不随 diversity 增加 ← 基于 sica_expanded_14b\n\n## 趋势\n成功 13 / 负向 11 / 失败 9 / 共 39\nsc_accuracy: 0.7941 ↓（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-32608: 无 GPU 信息\n\n## 告警\n- mvp_math50_t07: 已被终止 — unknown\n- sica_aime30_t07: 已被终止 — unknown\n- sica_aime30_v2: 已被终止 — unknown\n- sica_aime30_v3: 已被终止 — unknown\n- sica_proofwriter30: 训练失败 — unknown\n- sica_folio30: 已被终止 — unknown\n- sica_proofwriter30_v2: 已被终止 — unknown\n- exp-011-llama8b: 训练失败 — unknown\n- exp-010-mistral: 训练失败 — unknown\n- exp-011-llama8b-v2: 训练失败 — unknown\n- exp-017-strategyqa: 训练失败 — unknown\n- exp-018-arc: 训练失败 — unknown\n- exp-010-mistral-v2: 训练失败 — unknown\n- exp-017-strategyqa-v2: 训练失败 — unknown\n- pilot-contrastive-prompt: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9efa441d-60d7-4d06-a5a0-67268a359f9d",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "0904d503-8d9e-4717-8321-03fd485aa38a",
  "sourceToolAssistantUUID": "9efa441d-60d7-4d06-a5a0-67268a359f9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T17:30:06.248Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SZMYjumVCtuvUNekvgDCvw`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0904d503-8d9e-4717-8321-03fd485aa38a",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y8ryekWTNjeLmkuSYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "faff7d30-73b7-49ac-9862-8f0168f01e53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EC5Qsu4BTh3L38hHsM1qM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16508,
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

_source line 10 · 2026-05-17T17:30:06.260Z_

<details><summary>↩ Tool result · `toolu_01SZMYjumVCtuvUNekvgDCvw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml\", \"content\": \"# Literature Map — symb_invariant_consensus (SICA)\\n# Last updated: 2026-05-16\\n# Purpose: Track related work coverage for EMNLP 2026 submission\\n\\ndimensions:\\n\\n  self_consistency_and_variants:\\n    description: \\\"Self-Consistency (SC) decoding and improvements\\\"\\n    papers:\\n      - id: wang2023sc\\n        title: \\\"Self-Consistency Improves Chain of Thought Reasoning in Language Models\\\"\\n        authors: \\\"Wang et al.\\\"\\n        venue: \\\"ICLR 2023\\\"\\n        arxiv: \\\"2203.11171\\\"\\n        relevance: \\\"Foundational SC method; our primary baseline\\\"\\n        status: must_cite\\n\\n      - id: chen2024usc\\n        title: \\\"Universal Self-Consistency for Large Language Model Generation\\\"\\n        authors: \\\"Chen et al.\\\"\\n        venue: \\\"ICML 2024\\\"\\n        arxiv: \\\"2311.17311\\\"\\n        relevance: \\\"Extends SC to free-form answers via LLM-based selection; alternative aggregation\\\"\\n        status: must_cite\\n\\n      - id: taubenfeld2025cisc\\n        title: \\\"Confidence Improves Self-Consistency in LLMs\\\"\\n        authors: \\\"Taubenfeld et al.\\\"\\n        venue: \\\"ACL Findings 2025\\\"\\n        arxiv: \\\"2502.06233\\\"\\n        relevance: \\\"Weighted voting via model confidence; reduces samples 40-50%. Shows SC can be improved with non-uniform weighting — SICA uses constraint-based weighting instead\\\"\\n        status: must_cite\\n\\n      - id: kim2026reasc\\n        title: \\\"Reliability-Aware Adaptive Self-Consistency (ReASC)\\\"\\n        authors: \\\"Kim et al.\\\"\\n        venue: \\\"2026\\\"\\n        relevance: \\\"Response-level confidence for early halting; 70-80% cost saving vs naive SC\\\"\\n        status: should_cite\\n\\n      - id: loo2025reevaluating\\n        title: \\\"Reevaluating Self-Consistency Scaling in Multi-Agent Systems\\\"\\n        authors: \\\"Loo et al.\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2511.00751\\\"\\n        relevance: \\\"CRITICAL — shows SC gains plateau early and can decline at high sample counts for strong models. Directly supports our QwQ-32B finding (SICA≡SC when model is too consistent)\\\"\\n        status: must_cite\\n\\n      - id: wan2024rasc\\n        title: \\\"Reasoning-Aware Self-Consistency (RASC)\\\"\\n        authors: \\\"Wan et al.\\\"\\n        venue: \\\"2024\\\"\\n        relevance: \\\"Combines answer-level and rationale-level features; reduces samples ~88%\\\"\\n        status: should_cite\\n\\n      - id: li2023diverse\\n        title: \\\"Making Language Models Better Reasoners with Step-Aware Verifier\\\"\\n        authors: \\\"Li et al.\\\"\\n        venue: \\\"ACL 2023\\\"\\n        arxiv: \\\"2206.02336\\\"\\n        relevance: \\\"DiVeRSe: diverse prompts + step-aware verification for SC improvement. Combines diversity generation with trained verifier — shows diversity alone insufficient without verification quality.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: dsc2025\\n        title: \\\"Difficulty-Adaptive Self-Consistency\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"NAACL Findings 2025\\\"\\n        relevance: \\\"Ranks problem difficulty to allocate sampling budget; complementary efficiency approach\\\"\\n        status: optional\\n\\n  symbolic_reasoning_llm:\\n    description: \\\"Neuro-symbolic methods combining LLMs with formal solvers\\\"\\n    papers:\\n      - id: olausson2023linc\\n        title: \\\"LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers\\\"\\n        authors: \\\"Olausson et al.\\\"\\n        venue: \\\"EMNLP 2023\\\"\\n        arxiv: \\\"2310.15164\\\"\\n        relevance: \\\"LLM translates NL to FOL, external prover verifies; same-model translation pipeline like Logic-LM. Documents translation error rates (~40% on FOLIO). Key reference for self-extraction quality issues.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: pan2023logiclm\\n        title: \\\"Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\\\"\\n        authors: \\\"Pan et al.\\\"\\n        venue: \\\"EMNLP Findings 2023\\\"\\n        arxiv: \\\"2305.12295\\\"\\n        relevance: \\\"LLM→FOL→solver pipeline; closest architectural ancestor to SICA. Key difference: Logic-LM uses single-path translation, SICA aggregates across multiple paths\\\"\\n        status: must_cite\\n\\n      - id: xu2026dylos\\n        title: \\\"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (DyLoS)\\\"\\n        authors: \\\"Xu et al.\\\"\\n        venue: \\\"EACL 2026\\\"\\n        arxiv: \\\"2510.06774\\\"\\n        relevance: \\\"Multi-paradigm solver selection (LP/FOL/CSP/SMT); evaluated on FOLIO+ProofWriter. Outperforms Logic-LM. Key difference: DyLoS selects solver type, SICA aggregates constraints across paths\\\"\\n        status: must_cite\\n\\n      - id: fover2025\\n        title: \\\"FoVer: First-Order Logic Verification for Natural Language Reasoning\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"TACL 2025\\\"\\n        relevance: \\\"FOL verification for NL reasoning; strong results on ProofWriter+FOLIO. Uses verification rather than aggregation\\\"\\n        status: must_cite\\n\\n      - id: li2025survey\\n        title: \\\"A Survey on LLM Symbolic Reasoning\\\"\\n        authors: \\\"Li et al.\\\"\\n        venue: \\\"2025 (under review)\\\"\\n        relevance: \\\"Comprehensive survey; positions SICA within the broader landscape\\\"\\n        status: should_cite\\n\\n      - id: constraintllm2025\\n        title: \\\"ConstraintLLM: A Neuro-Symbolic Framework for Industrial Constraint Programming\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP 2025\\\"\\n        relevance: \\\"Multi-instruction SFT for constraint extraction; different domain (industrial) but related extraction methodology\\\"\\n        status: optional\\n\\n  maxsat_constraint_nlp:\\n    description: \\\"MAX-SAT and constraint satisfaction applied to NLP/reasoning\\\"\\n    papers:\\n      - id: llm_meets_cp2025\\n        title: \\\"Large Language Model Meets Constraint Propagation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"IJCAI 2025\\\"\\n        relevance: \\\"LLM+constraint propagation integration; validates feasibility of constraint-based reasoning with LLMs\\\"\\n        status: should_cite\\n\\n      - id: satbench2025\\n        title: \\\"SATBench: Benchmarking LLMs' Logical Reasoning via SAT Problems\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP 2025\\\"\\n        relevance: \\\"Evaluates LLMs on SAT-formulated problems; establishes that LLMs struggle with pure SAT but can benefit from solver integration\\\"\\n        status: should_cite\\n\\n      - id: maxsat_local_search2025\\n        title: \\\"Optimizing Local Search-based Partial MaxSAT Solving via Initial Assignment Prediction\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"Science China Information Sciences 2025\\\"\\n        relevance: \\\"Solver-side advances in partial MaxSAT; technical reference for our WPMS formulation\\\"\\n        status: optional\\n\\n  folio_proofwriter_sota:\\n    description: \\\"State-of-the-art methods on FOLIO and ProofWriter benchmarks\\\"\\n    papers:\\n      - id: logicagent2025\\n        title: \\\"From Ambiguity to Verdict: A Semiotic-Grounded Multi-Perspective Agent for LLM Logical Reasoning (LogicAgent)\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2509.24765\\\"\\n        relevance: \\\"Multi-perspective logical reasoning; SOTA on logical reasoning benchmarks including FOLIO. +7.05% average gain\\\"\\n        status: must_cite\\n\\n      - id: aristotle2025\\n        title: \\\"Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"ACL 2025\\\"\\n        relevance: \\\"Logic-complete decomposition framework; strong ProofWriter/FOLIO results\\\"\\n        status: must_cite\\n\\n      - id: qi2025symbolic_provers\\n        title: \\\"Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation\\\"\\n        authors: \\\"Qi et al.\\\"\\n        venue: \\\"ICLR 2025\\\"\\n        arxiv: \\\"2502.06563\\\"\\n        relevance: \\\"LLM+symbolic prover combination; evaluated on FOLIO\\\"\\n        status: should_cite\\n\\n      - id: dissecting2025\\n        title: \\\"Dissecting Logical Reasoning in LLMs: A Fine-Grained Evaluation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"EMNLP Findings 2025\\\"\\n        arxiv: \\\"2506.04810\\\"\\n        relevance: \\\"Fine-grained analysis of LLM logical reasoning capabilities on ProofWriter/FOLIO\\\"\\n        status: optional\\n\\n  reasoning_model_diversity:\\n    description: \\\"Trace diversity in reasoning vs non-reasoning models; supports our QwQ-32B finding\\\"\\n    papers:\\n      - id: loo2025reevaluating\\n        title: \\\"Reevaluating Self-Consistency Scaling in Multi-Agent Systems\\\"\\n        authors: \\\"Loo et al.\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2511.00751\\\"\\n        relevance: \\\"CRITICAL — strong models produce near-identical paths, SC gains plateau/decline. Direct support for SICA≡SC on QwQ-32B\\\"\\n        status: must_cite\\n\\n      - id: diversity_aware_tts2025\\n        title: \\\"Diversity-Aware Training for Test-Time Scaling\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"Under review 2025\\\"\\n        relevance: \\\"Independent reasoning attempts collapse into similar solutions; diversity training needed to unlock test-time scaling. Supports our claim that non-reasoning models have more useful diversity\\\"\\n        status: must_cite\\n\\n      - id: snell2025scaling_tts\\n        title: \\\"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters\\\"\\n        authors: \\\"Snell et al.\\\"\\n        venue: \\\"ICLR 2025 (Oral)\\\"\\n        arxiv: \\\"2408.03314\\\"\\n        relevance: \\\"Foundational test-time compute scaling; shows compute-optimal strategies vary by difficulty. Contextualizes why SICA needs diverse paths\\\"\\n        status: should_cite\\n\\n      - id: deepseek_r1_2025\\n        title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n        authors: \\\"DeepSeek-AI\\\"\\n        venue: \\\"Nature 2025\\\"\\n        arxiv: \\\"2501.12948\\\"\\n        relevance: \\\"Defines the reasoning model paradigm (RL-trained extended thinking); reference for why these models are highly self-consistent\\\"\\n        status: must_cite\\n\\n      - id: base_models_reason2025\\n        title: \\\"Base Models Know How to Reason, Thinking Models Learn When\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2510.07364\\\"\\n        relevance: \\\"RL teaches activation timing not new skills; implies reasoning models converge to similar reasoning patterns, reducing trace diversity\\\"\\n        status: should_cite\\n\\n      - id: korikov2025sc_ranking\\n        title: \\\"The Impact of LLM Self-Consistency and Reasoning Effort on Automated Scoring\\\"\\n        authors: \\\"Korikov et al.\\\"\\n        venue: \\\"arXiv 2026\\\"\\n        arxiv: \\\"2604.26954\\\"\\n        relevance: \\\"Temperature sampling helps but ensemble size (1→7) produces no significant gains; supports diminishing returns of naive SC\\\"\\n        status: optional\\n\\n  multi_path_aggregation:\\n    description: \\\"Methods for aggregating multiple reasoning paths beyond majority voting\\\"\\n    papers:\\n      - id: rc2025\\n        title: \\\"Representation Consistency for Accurate and Coherent LLM Answer Aggregation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"arXiv 2025\\\"\\n        arxiv: \\\"2506.21590\\\"\\n        relevance: \\\"Aggregation via representation similarity; down-weights incoherent reasoning. Semantic alternative to SICA's symbolic approach\\\"\\n        status: should_cite\\n\\n      - id: multi_path_plan2025\\n        title: \\\"Enhancing Long Chain-of-Thought Reasoning through Multi-Path Plan Aggregation\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"2025\\\"\\n        arxiv: \\\"2510.11620\\\"\\n        relevance: \\\"Multi-path aggregation at plan level rather than answer level\\\"\\n        status: optional\\n\\n      - id: crest2025\\n        title: \\\"Improving LLMs' Reasoning with Consistency-Driven Self-Training (CREST)\\\"\\n        authors: \\\"Various\\\"\\n        venue: \\\"NAACL 2025\\\"\\n        relevance: \\\"Consistency as training signal rather than inference-time aggregation\\\"\\n        status: optional\\n\\n  verification_reranking:\\n    description: \\\"Verification and reranking methods for LLM outputs (ORM, PRM)\\\"\\n    papers:\\n      - id: cobbe2021gsm8k\\n        title: \\\"Training Verifiers to Solve Math Word Problems\\\"\\n        authors: \\\"Cobbe et al.\\\"\\n        venue: \\\"arXiv 2021\\\"\\n        arxiv: \\\"2110.14168\\\"\\n        relevance: \\\"Defines ORM (Outcome Reward Model) paradigm; trained verifier selects among candidate solutions. Alternative to symbolic constraint aggregation.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: lightman2023prm\\n        title: \\\"Let's Verify Step by Step\\\"\\n        authors: \\\"Lightman et al.\\\"\\n        venue: \\\"ICLR 2024\\\"\\n        arxiv: \\\"2305.20050\\\"\\n        relevance: \\\"Process Reward Models (PRM) verify each reasoning step. Shows step-level verification outperforms outcome-level. Trained verifier approach contrasts with SICA's self-extraction.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: wang2024mathshepherd\\n        title: \\\"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\\\"\\n        authors: \\\"Wang et al.\\\"\\n        venue: \\\"ACL 2024\\\"\\n        arxiv: \\\"2312.08935\\\"\\n        relevance: \\\"Automatic process reward model training without human labels. Achieves strong verification without manual annotation.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: hosseini2024vstar\\n        title: \\\"V-STaR: Training Verifiers for Self-Taught Reasoners\\\"\\n        authors: \\\"Hosseini et al.\\\"\\n        venue: \\\"NeurIPS 2024\\\"\\n        arxiv: \\\"2402.06457\\\"\\n        relevance: \\\"Iteratively trains verifier alongside generator; verification quality scales with data.\\\"\\n        status: should_cite\\n\\n  debate_multi_agent:\\n    description: \\\"Debate and multi-agent aggregation methods for LLM reasoning\\\"\\n    papers:\\n      - id: liang2023encouraging\\n        title: \\\"Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate\\\"\\n        authors: \\\"Liang et al.\\\"\\n        venue: \\\"arXiv 2023\\\"\\n        arxiv: \\\"2305.19118\\\"\\n        relevance: \\\"Multi-agent debate improves factuality and reasoning via iterative refinement. Alternative multi-path aggregation mechanism.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: du2023improving\\n        title: \\\"Improving Factuality and Reasoning in Language Models through Multiagent Debate\\\"\\n        authors: \\\"Du et al.\\\"\\n        venue: \\\"ICML 2024\\\"\\n        arxiv: \\\"2305.14325\\\"\\n        relevance: \\\"Multi-agent debate for reasoning; shows consensus-seeking improves accuracy. Contrast: debate uses natural language, SICA uses formal constraints.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: khan2024debating\\n        title: \\\"Debating with More Persuasive LLMs Leads to More Truthful Answers\\\"\\n        authors: \\\"Khan et al.\\\"\\n        venue: \\\"ICML 2024\\\"\\n        arxiv: \\\"2402.06782\\\"\\n        relevance: \\\"Debate quality depends on model capability; stronger debaters improve consensus.\\\"\\n        status: should_cite\\n\\n  benchmarks_and_datasets:\\n    description: \\\"Benchmark datasets used in our evaluation\\\"\\n    papers:\\n      - id: han2022folio\\n        title: \\\"FOLIO: Natural Language Reasoning with First-Order Logic\\\"\\n        authors: \\\"Han et al.\\\"\\n        venue: \\\"arXiv 2022\\\"\\n        arxiv: \\\"2209.00840\\\"\\n        relevance: \\\"FOLIO benchmark with expert-annotated FOL; our primary formal logic evaluation dataset (n=204).\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: tafjord2021proofwriter\\n        title: \\\"ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language\\\"\\n        authors: \\\"Tafjord et al.\\\"\\n        venue: \\\"ACL Findings 2021\\\"\\n        arxiv: \\\"2012.13048\\\"\\n        relevance: \\\"ProofWriter dataset for deductive reasoning; our primary large-N evaluation (n=600).\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: geva2021strategyqa\\n        title: \\\"Did Aristotle Use a Laptop? A Question Answering Benchmark with Implicit Reasoning Strategies\\\"\\n        authors: \\\"Geva et al.\\\"\\n        venue: \\\"TACL 2021\\\"\\n        arxiv: \\\"2101.02235\\\"\\n        relevance: \\\"StrategyQA benchmark for commonsense multi-hop reasoning (Yes/No); our cross-domain validation (n=200).\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: clark2018arc\\n        title: \\\"Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge\\\"\\n        authors: \\\"Clark et al.\\\"\\n        venue: \\\"arXiv 2018\\\"\\n        arxiv: \\\"1803.05457\\\"\\n        relevance: \\\"ARC-Challenge science QA benchmark; our cross-domain validation for multiple-choice (n=60).\\\"\\n        status: must_cite\\n        verified: true\\n\\n  negative_results_analysis:\\n    description: \\\"Precedents for negative-result and analysis papers in NLP\\\"\\n    papers:\\n      - id: huang2024selfcorrect\\n        title: \\\"Large Language Models Cannot Self-Correct Reasoning Yet\\\"\\n        authors: \\\"Huang et al.\\\"\\n        venue: \\\"ICLR 2024\\\"\\n        arxiv: \\\"2310.01798\\\"\\n        relevance: \\\"Key precedent: shows LLM self-correction fails without external feedback. Structural parallel to our finding (self-extraction fails without external verification). Same 'self-X fails' narrative.\\\"\\n        status: must_cite\\n        verified: true\\n\\n      - id: mirzadeh2024gsmsymbolic\\n        title: \\\"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\\\"\\n        authors: \\\"Mirzadeh et al.\\\"\\n        venue: \\\"arXiv 2024\\\"\\n        arxiv: \\\"2410.05229\\\"\\n        relevance: \\\"Systematic negative result: apparent LLM reasoning gains are fragile under symbolic perturbation. Establishes precedent for rigorous negative-result methodology in LLM reasoning.\\\"\\n        status: should_cite\\n        verified: true\\n\\ngaps:\\n  resolved:\\n    - dimension: \\\"verification_reranking\\\"\\n      gap: \\\"Added ORM, PRM, Math-Shepherd, V-STaR (2026-05-17)\\\"\\n    - dimension: \\\"debate_multi_agent\\\"\\n      gap: \\\"Added Liang 2023, Du 2023, Khan 2024 (2026-05-17)\\\"\\n    - dimension: \\\"benchmarks_and_datasets\\\"\\n      gap: \\\"Added FOLIO, ProofWriter, StrategyQA, ARC (2026-05-17)\\\"\\n    - dimension: \\\"negative_results_analysis\\\"\\n      gap: \\\"Added Huang 2024 (self-correct), Mirzadeh 2024 (GSM-Symbolic) (2026-05-17)\\\"\\n    - dimension: \\\"symbolic_reasoning_llm\\\"\\n      gap: \\\"Added LINC (Olausson et al. 2023) (2026-05-17)\\\"\\n    - dimension: \\\"self_consistency_and_variants\\\"\\n      gap: \\\"Added DiVeRSe (Li et al. 2023) (2026-05-17)\\\"\\n  remaining: []\\n\", \"total_chars\": 17880, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "faff7d30-73b7-49ac-9862-8f0168f01e53",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "666b4d2d-94ee-42b5-99c8-45e0bc58aa52",
  "sourceToolAssistantUUID": "faff7d30-73b7-49ac-9862-8f0168f01e53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:30:07.293Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01ACY6XuYHaecaH6wzVi2D4T`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "666b4d2d-94ee-42b5-99c8-45e0bc58aa52",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y8ryekWTNjeLmkuSYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93c30f65-7a13-485e-9c7e-dfd9900c09f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EC5Qsu4BTh3L38hHsM1qM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16508,
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

_source line 12 · 2026-05-17T17:30:07.319Z_

<details><summary>↩ Tool result · `toolu_01ACY6XuYHaecaH6wzVi2D4T`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'symb_invariant_consensus'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93c30f65-7a13-485e-9c7e-dfd9900c09f1",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "5c16515e-b8da-4979-9c3e-477722d11a12",
  "sourceToolAssistantUUID": "93c30f65-7a13-485e-9c7e-dfd9900c09f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T17:30:11.238Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Xm6B4WCH5rqSPC1W52cgc4`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c16515e-b8da-4979-9c3e-477722d11a12",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y9ESEbJkYnQwC2CsfH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea513661-b5cd-4b63-8e58-806adf12da0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvpoTm9P5bXBmDBfdapUF2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8244,
      "cache_read_input_tokens": 17954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8244,
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

_source line 14 · 2026-05-17T17:30:11.259Z_

<details><summary>↩ Tool result · `toolu_01Xm6B4WCH5rqSPC1W52cgc4`</summary>

```text
artifacts/dream_reports/dream_20260516T051642/best/paper.tex
artifacts/dream_reports/dream_20260516T051642/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/best/paper.tex
artifacts/dream_reports/dream_20260516T054054/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/worst/paper.tex
artifacts/dream_reports/dream_20260516T124139/best/paper.tex
artifacts/dream_reports/dream_20260516T124139/median/paper.tex
artifacts/dream_reports/dream_20260516T124139/worst/paper.tex
artifacts/dream_reports/dream_20260516T155754/best/paper.tex
artifacts/dream_reports/dream_20260516T155754/median/paper.tex
artifacts/dream_reports/dream_20260516T155754/worst/paper.tex
artifacts/dream_reports/dream_20260517T144412/best/paper.tex
artifacts/dream_reports/dream_20260517T144412/median/paper.tex
artifacts/dream_reports/dream_20260517T144412/worst/paper.tex
artifacts/dream_reports/dream_20260517T165032/best/paper.tex
docs/paper/experiments.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260517T165032/median/paper.tex
docs/paper/method.tex
artifacts/dream_reports/dream_20260517T165032/worst/paper.tex
docs/paper/introduction.tex
docs/paper/related_work.tex
docs/paper/discussion.tex
docs/paper/conclusion.tex
docs/paper/appendix.tex
docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea513661-b5cd-4b63-8e58-806adf12da0c",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "92e8f097-c68b-450e-b7b5-d18e2e6a52e9",
  "sourceToolAssistantUUID": "ea513661-b5cd-4b63-8e58-806adf12da0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T17:30:12.267Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HavsVe7E7zVLW3aehQaaZR`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92e8f097-c68b-450e-b7b5-d18e2e6a52e9",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y9ESEbJkYnQwC2CsfH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "226c3639-94ab-422a-9a57-6e00f7c25f9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvpoTm9P5bXBmDBfdapUF2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8244,
      "cache_read_input_tokens": 17954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8244,
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

_source line 16 · 2026-05-17T17:30:12.277Z_

<details><summary>↩ Tool result · `toolu_01HavsVe7E7zVLW3aehQaaZR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp-004-qwen7b | Within-family scaling: Qwen2.5-7B-Instruct 在 D012 60 题上 SICA vs SC。弱模型预期 C0 > 14B（更多 diversity），但 constraint quality 预期更低，SICA-SC gap 预期≈0——验证 capability trap 的 scaling 维度。 | — | — | — |\\n\\n## 待处理\\n- smoke-test-5q（准备中）\\n\\n## 近期结论\\n- **exp-012-gsm8k-pilot** (negative): Cross-domain validation: Qwen2.5-14B-Instruct 在 GSM8K (开放答案数学域) 30 题上 SICA vs SC。预期 C0<20%（14B 在 GSM8K 太强），验证 C0 作为 SICA 无效性预测指标。 ← 基于 sica_expanded_14b\\n- **exp-021-oracle-folio** (success): If we replace self-extracted constraints with gold FOL annotations verified by Z3, Oracle-SICA should significantly outperform both SC and SICA, demonstrating that constraint quality is the bottleneck for SICA gains on formal logic tasks. ← 基于 sica_expanded_14b\\n  [exp021_oracle_folio_results](/api/workspace-files/projects/symb_invariant_consensus/artifacts/exp-021-oracle-folio/data/exp021_summary.txt)\\n- **temperature-ablation-t10** (negative): Temperature ablation T=1.0: 高温下 Qwen2.5-14B trace diversity 最大化（C0 预期>60%），SICA-SC gap 预期≈0 或负——验证最大 diversity 仍不能拯救 SICA，因为 constraint discriminative power 不随 diversity 增加 ← 基于 sica_expanded_14b\\n\\n## 趋势\\n成功 13 / 负向 11 / 失败 9 / 共 39\\nsc_accuracy: 0.7941 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-32608: 无 GPU 信息\\n\\n## 告警\\n- mvp_math50_t07: 已被终止 — unknown\\n- sica_aime30_t07: 已被终止 — unknown\\n- sica_aime30_v2: 已被终止 — unknown\\n- sica_aime30_v3: 已被终止 — unknown\\n- sica_proofwriter30: 训练失败 — unknown\\n- sica_folio30: 已被终止 — unknown\\n- sica_proofwriter30_v2: 已被终止 — unknown\\n- exp-011-llama8b: 训练失败 — unknown\\n- exp-010-mistral: 训练失败 — unknown\\n- exp-011-llama8b-v2: 训练失败 — unknown\\n- exp-017-strategyqa: 训练失败 — unknown\\n- exp-018-arc: 训练失败 — unknown\\n- exp-010-mistral-v2: 训练失败 — unknown\\n- exp-017-strategyqa-v2: 训练失败 — unknown\\n- pilot-contrastive-prompt: 训练失败 — unknown\\n\", \"total_chars\": 1938, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "226c3639-94ab-422a-9a57-6e00f7c25f9a",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "d7931704-7499-4f81-9c10-0ca2217e2f34",
  "sourceToolAssistantUUID": "226c3639-94ab-422a-9a57-6e00f7c25f9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T17:30:12.634Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015GNyoQzoZF9LM1iF4pwFcF`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7931704-7499-4f81-9c10-0ca2217e2f34",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y9ESEbJkYnQwC2CsfH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "296d71a8-6a07-4ab2-b439-895376d75939",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvpoTm9P5bXBmDBfdapUF2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8244,
      "cache_read_input_tokens": 17954,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8244
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 284,
          "cache_read_input_tokens": 17954,
          "cache_creation_input_tokens": 8244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8244,
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

_source line 18 · 2026-05-17T17:30:12.644Z_

<details><summary>↩ Tool result · `toolu_015GNyoQzoZF9LM1iF4pwFcF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md\", \"content\": \"# Paper Framing — symb_invariant_consensus\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25)\\n- Deadline: May 25, 2026 (ARR submission)\\n\\n## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)\\n\\n1. **The Capability Trap**: LLM self-extracted FOL constraint aggregation faces a fundamental tension: it requires output diversity (C0>20%) to differ from voting, but self-extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to counting. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B). [Scope: this finding characterizes same-model self-extraction pipelines; methods using external verifiers or trained extractors may not share this limitation.]\\n2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.\\n3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.\\n\\n## Core Insight\\nLLM self-extracted FOL constraints don't improve majority voting because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these self-extracted constraints lack the discriminative power to distinguish correct from incorrect answers (precision ~0.50, no better than chance). MAX-SAT optimization over such non-discriminative constraints degenerates to counting, performing no better than simple majority voting.\\n\\n**Critical oracle result (exp-021)**: When gold FOL annotations replace self-extracted constraints, Oracle-SICA achieves +8.82pp over SC (p<0.001, n=204). This proves the MAX-SAT aggregation mechanism IS effective given discriminative constraints — the bottleneck is exclusively in LLM self-extraction quality, not in the aggregation paradigm itself.\\n\\nWe provide the first systematic empirical study (a) precisely localizing the failure mode to extraction quality via oracle control, (b) quantifying constraint non-discrimination at per-problem granularity (n=307), and (c) proving MAX-SAT adds nothing beyond counting when constraints lack discriminative power. [Positioning: Logic-LM and LINC documented that LLM-to-FOL translation is error-prone; our contribution is the oracle-controlled causal separation of extraction vs aggregation failure, plus systematic quantification and C0 as deployment diagnostic.]\\n\\n## Story Spine\\n- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?\\n- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.\\n- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 4 instruction-scale model families + 1 full reasoning model. We find SICA ≈ SC everywhere, and identify a structural reason: the **capability trap**.\\n- **Headline result**: \\\"Across 3 reasoning domains and 5 models spanning instruction, distilled-reasoning, and full-reasoning architectures, SICA provides no significant accuracy gain over SC. Five models (combined N>1,300) show Δ ranging from -3.3pp to +2.0pp, none significant. The constraint ablation reveals MAX-SAT ≈ count-only ≈ random-weight. We identify the structural cause: a capability trap where extracted constraints lack discriminative power regardless of output diversity level.\\\"\\n\\n## Anticipated Reviewer Concerns & Defensive Experiments\\n1. **\\\"Gains not statistically significant\\\"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.\\n2. **\\\"Only a better tiebreaker, not worth the overhead\\\"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis\\n3. **\\\"Only Qwen models\\\"** → 4 instruction-scale families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B\\n4. **\\\"Only one reasoning model\\\"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)\\n5. **\\\"Only logic domain\\\"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.\\n6. **\\\"MAX-SAT is over-engineering\\\"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.\\n7. **\\\"Random tiebreak baseline\\\"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.\\n8. **\\\"Why not just use a reasoning model?\\\"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.\\n9. **\\\"How does this compare to Logic-LM / LINC?\\\"** → exp-015: Logic-LM × K baseline (CPU-only)\\n10. **\\\"Weighted SC is simpler\\\"** → exp-016: Weighted SC baseline (CPU-only)\\n11. **\\\"C0 is trivially derived\\\"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.\\n12. **\\\"Within-family scaling?\\\"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.\\n13. **\\\"Self-extraction confound — same model generates and extracts\\\"** → exp-021 Oracle FOLIO: **RESOLVED.** Gold FOL + Z3 + MAX-SAT = 88.24% vs SC = 79.41% (+8.82pp, p=6.15e-05). Aggregation mechanism IS effective with discriminative constraints. Bottleneck conclusively localized to LLM self-extraction quality. This is now a core contribution, not just a defensive experiment.\\n14. **\\\"Published methods achieve gains on same benchmarks (DyLoS, Aristotle, FoVer)\\\"** → Acknowledge in Related Work and Discussion. Key distinction: those methods use trained/external verifiers, multi-paradigm solver selection, or logic-complete decomposition — all fundamentally different from same-model self-extraction. Our finding characterizes the specific failure mode of self-extraction pipelines, not symbolic reasoning broadly.\\n15. **\\\"MAX-SAT formulation is just weighted voting\\\"** → Paper must explicitly describe cross-answer evaluation: constraints from trace t_i ARE/ARE NOT evaluated against other candidates. If structurally a weighted vote, acknowledge and frame contribution as \\\"even the most charitable interpretation (weighted vote with constraint-based weights) provides no gain.\\\"\\n\\n## Working Title\\n**\\\"The Capability Trap: Why Self-Extracted Constraints Cannot Improve LLM Majority Voting\\\"**\\n(Alternatives: \\n- \\\"Diversity Without Discrimination: A Systematic Study of LLM-Extracted Constraint Aggregation\\\"\\n- \\\"When Does Symbolic Aggregation Help? Characterizing the Failure Mode of Self-Extracted FOL Constraints\\\")\\n\\nNOTE (Dream D037): Title MUST be scoped to \\\"self-extracted constraints\\\" / \\\"SICA\\\" — NOT \\\"symbolic consensus\\\" broadly. Published methods (DyLoS, Aristotle, FoVer, LogicAgent) achieve gains on same benchmarks using different symbolic approaches. Our evidence covers one pipeline (same-model FOL extraction + MAX-SAT), not the entire paradigm.\\n\\n## Paper Structure (EMNLP 8pp + appendix)\\n- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Oracle Control: Gold-FOL+MAX-SAT vs SC vs SICA-self, the key causal separation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Temperature Ablation: C0 varies 30-43% but Δ=0 throughout)\\n- Main Figures: F1 (Method Pipeline), F2 (Per-problem scatter: vote entropy vs constraint exclusion rate, colored by flip type, n=307 multi-candidate problems from exp-001 — hero figure showing constraints fail to discriminate), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: experiment-level conditions, marker size ∝ sqrt(n), showing no correlation between diversity and SICA effectiveness)\\n- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data\\n\\n## Claim Risk Notes (Updated D035 + exp-014)\\n- **Claim 1 mechanism refinement**: \\\"Inverse correlation between diversity and quality\\\" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: \\\"constraints lack discriminative power regardless of diversity level.\\\" Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.\\n- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.\\n- **Claim 3 gradient → independence framing**: Temperature ablation confirms C0 varies (30%→38%→43%) but gap stays flat at 0.00pp (zero discordant across all temperatures). Data supports \\\"diversity is necessary but insufficient\\\" NOT \\\"gradient diagnostic.\\\" Claim 3 should be: \\\"C0 predicts when SICA cannot help (C0<5% → degenerate), but increasing diversity beyond the threshold provides no benefit — constraint quality remains the binding bottleneck regardless of diversity level.\\\" RESOLVED (temperature data in hand).\\n- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.\\n- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.\\n\\n## Required Citations (Dream D037 — minimum 30 references)\\n\\nPaper Agent MUST include these categories (non-exhaustive list of must-cite works):\\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 ACL Findings (confidence-weighted SC), DiVeRSe (Li et al. 2023)\\n- **Neuro-symbolic reasoning (positive results on same benchmarks)**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\\n- **Test-time compute scaling**: Snell et al. 2025 (ICLR Oral), DeepSeek-R1 technical report (Nature 2025), Diversity-Aware Training for TTS (2025)\\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd (Wang et al. 2024)\\n- **Constraint satisfaction in NLP**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\\n- **Negative results in NLP**: appropriate precedents for analysis/negative-result papers\\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\\n- **Reasoning model paradigm**: QwQ technical blog, o1 (OpenAI 2024)\\n\\n## Claim Scoping Rules (Dream D037)\\n\\n- n=60 conditions: present as \\\"suggestive/consistent with\\\" NOT \\\"confirming.\\\" Only n≥200 conditions can \\\"confirm\\\" null.\\n- Combined N>1,300: acceptable if clearly stated that 804/1300 come from powered Qwen-14B condition.\\n- Domain coverage: acknowledge that SICA operates meaningfully (C0>20%) primarily on formal logic; other domains are degenerate (C0<10%) due to model capability.\\n- \\\"Capability trap\\\" framing: position as systematic quantification of a known challenge (not discovery). Our specific contributions: (a) per-problem precision analysis at n=307 granularity, (b) constraint ablation proving MAX-SAT ≈ counting, (c) C0 as deployment diagnostic.\\n\\n## Venue Fit Risks\\n- EMNLP: Negative-results/analysis paper. Must answer \\\"so what should practitioners do?\\\" → C0 as deployment diagnostic + overhead analysis.\\n- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.\\n- Statistical power: Now strong (N>1,200 combined across powered tests).\\n\", \"total_chars\": 12951, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "296d71a8-6a07-4ab2-b439-895376d75939",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "058ad0fc-726e-4031-ab7f-afb2504ec45f",
  "sourceToolAssistantUUID": "296d71a8-6a07-4ab2-b439-895376d75939",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-17T17:30:14.999Z_

Now let me read the actual paper source files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "058ad0fc-726e-4031-ab7f-afb2504ec45f",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y9d23TXXMpSFGcQ8Ae",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7785af93-a91a-4081-b4a7-c6550db4c447",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RnSdd74mGQkVF1DgqHYA3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6064,
      "cache_read_input_tokens": 26198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6064,
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

_source line 20 · 2026-05-17T17:30:16.416Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C33Yt2CDF5JjdcLWotERpv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7785af93-a91a-4081-b4a7-c6550db4c447",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y9d23TXXMpSFGcQ8Ae",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4189ee6-2382-4d45-a998-f7fede8a47a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RnSdd74mGQkVF1DgqHYA3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6064,
      "cache_read_input_tokens": 26198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6064,
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

_source line 21 · 2026-05-17T17:30:16.422Z_

<details><summary>↩ Tool result · `toolu_01C33Yt2CDF5JjdcLWotERpv`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{hyperref}
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}{figures/}}
20	
21	\title{The Capability Trap: Why Self-Extracted Constraints\\Cannot Improve LLM Majority Voting}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\begin{abstract}
29	% Phase 2: to be written after re-dream results
30	\textbf{[PLACEHOLDER -- Abstract deferred to Phase 2]}
31	\end{abstract}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{method}
38	
39	\input{experiments}
40	
41	\input{discussion}
42	
43	\input{conclusion}
44	
45	\section*{Limitations}
46	% Required by EMNLP
47	\textbf{[PLACEHOLDER -- to be written in Phase 2]}
48	
49	\bibliography{references}
50	\bibliographystyle{acl_natbib}
51	
52	\appendix
53	\input{appendix}
54	
55	\end{document}
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4189ee6-2382-4d45-a998-f7fede8a47a4",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "03e6082f-8c80-4e01-8130-e6a567dac0d9",
  "sourceToolAssistantUUID": "b4189ee6-2382-4d45-a998-f7fede8a47a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T17:30:17.364Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LiNYwFxfDhFAD16f4v2xCW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03e6082f-8c80-4e01-8130-e6a567dac0d9",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y9d23TXXMpSFGcQ8Ae",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f0a9c9f-4487-4a28-a137-2dda921a91a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RnSdd74mGQkVF1DgqHYA3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6064,
      "cache_read_input_tokens": 26198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6064,
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

_source line 23 · 2026-05-17T17:30:17.369Z_

<details><summary>↩ Tool result · `toolu_01LiNYwFxfDhFAD16f4v2xCW`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	% Phase 1: To be written after literature gap-fill.
5	% Clusters (from writing_plan.yaml):
6	% 1. SC and extensions
7	% 2. Neuro-symbolic reasoning (distinguish trained/external vs self-extraction)
8	% 3. Test-time compute and reasoning models
9	% 4. Verification and reranking
10	% 5. Constraint satisfaction in NLP
11	% 6. Debate and multi-agent aggregation
12	
13	\textbf{[PLACEHOLDER -- Related Work deferred to Step 4]}
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f0a9c9f-4487-4a28-a137-2dda921a91a6",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "64969a12-0210-4b01-b4fc-334e834adf62",
  "sourceToolAssistantUUID": "2f0a9c9f-4487-4a28-a137-2dda921a91a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T17:30:17.533Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xzt9BEX9emgbbg71B3PuH3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64969a12-0210-4b01-b4fc-334e834adf62",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y9d23TXXMpSFGcQ8Ae",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08f116d6-2f01-4373-baea-b5887b91eb29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RnSdd74mGQkVF1DgqHYA3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6064,
      "cache_read_input_tokens": 26198,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6064
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 246,
          "cache_read_input_tokens": 26198,
          "cache_creation_input_tokens": 6064,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6064,
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

_source line 25 · 2026-05-17T17:30:17.539Z_

<details><summary>↩ Tool result · `toolu_01Xzt9BEX9emgbbg71B3PuH3`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	% Phase 2: To be written after experiments and method sections are finalized.
5	% Structure (from writing_plan.yaml):
6	% 1. Hook: neuro-symbolic methods show promise
7	% 2. Gap: does same-model self-extraction suffice?
8	% 3. Our approach: systematic SICA evaluation + oracle control
9	% 4. Key finding: aggregation mechanism is sound, self-extraction is bottleneck
10	% 5. Positioning: DyLoS/Aristotle/FoVer succeed because they avoid self-extraction
11	% 6. Contributions: [C1] capability trap, [C2] causal localization, [C3] recoverable gap, [C4] C0 diagnostic
12	
13	\textbf{[PLACEHOLDER -- Introduction deferred to Phase 2]}
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08f116d6-2f01-4373-baea-b5887b91eb29",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "d092dd13-b746-4e88-a1a1-17d36ec2a8b7",
  "sourceToolAssistantUUID": "08f116d6-2f01-4373-baea-b5887b91eb29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-17T17:30:20.622Z_

The paper sections are mostly placeholders. Let me read the sections that have content, and also check for the most recent dream report which likely has the most complete version of the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d092dd13-b746-4e88-a1a1-17d36ec2a8b7",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y9z1qvzokFPgYFvVFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b978792-6c83-4e38-840c-f462cdca89aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBop8W5Pr5949R753jJ8Ny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 32262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1237,
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

_source line 27 · 2026-05-17T17:30:21.107Z_

<details open><summary>🔧 Tool call — Read · `toolu_018gX48RDzjrUdfMWUzvfG1w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b978792-6c83-4e38-840c-f462cdca89aa",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y9z1qvzokFPgYFvVFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f948e60b-a12a-4eba-9690-a7ff8bd9ddb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBop8W5Pr5949R753jJ8Ny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 32262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1237,
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

_source line 28 · 2026-05-17T17:30:21.117Z_

<details><summary>↩ Tool result · `toolu_018gX48RDzjrUdfMWUzvfG1w`</summary>

```text
1	\section{Method: The SICA Pipeline}
2	\label{sec:method}
3	
4	This section describes Symbolic Invariant Consensus Aggregation (SICA), the pipeline we implement and evaluate as a representative instantiation of self-extracted symbolic consensus. SICA extracts first-order logic (FOL) constraints from multiple reasoning traces produced by a single LLM, formulates a weighted partial MAX-SAT problem over these constraints, and selects the answer best supported by the satisfiable subset. We compare SICA against Self-Consistency \cite{wang2023sc}, which selects the majority answer across the same set of traces.
5	
6	\subsection{Overview}
7	\label{sec:method-overview}
8	
9	Given a question $q$, SICA proceeds in four stages. First, an LLM generates $K$ independent reasoning traces $\{t_1, \ldots, t_K\}$ by sampling at temperature $T$; each trace $t_i$ yields a candidate answer $a_i$. Second, the same LLM is prompted to extract a set of structured FOL constraints $C_i$ from each trace $t_i$. Third, constraints are deduplicated across traces by syntactic equivalence matching, and each unique constraint receives a weight equal to the number of traces that produced it. Fourth, the deduplicated constraint pool is formulated as a weighted partial MAX-SAT instance and solved by Z3 \cite{demoura2008z3}. Each candidate answer is then scored by the total weight of satisfied constraints that support it, and the highest-scoring answer is selected.
10	
11	Self-Consistency (SC) uses only the first stage: it selects $a^* = \arg\max_{a} \sum_{i=1}^{K} \mathbf{1}[a_i = a]$, the answer produced by the most traces. SICA's additional signal comes from the constraint satisfaction structure. Whether this additional signal provides discriminative power beyond vote counting is the central empirical question of this paper.
12	
13	\subsection{Constraint Extraction}
14	\label{sec:constraint-extraction}
15	
16	For each reasoning trace $t_i$, the same LLM that generated $t_i$ is prompted to extract a set of structured FOL constraints. While we prompt the model to produce FOL-style formalizations, the extracted constraints are predominantly ground-level propositions without quantifiers, reflecting the capabilities of instruction-scale models. The extraction prompt requests JSON-formatted output containing the constraint type (equation, inequality, or predicate), a human-readable expression, and a Z3-compatible formula string. Each constraint $c$ is associated with its source trace $t_i$ and the answer $a_i$ that trace produced. A representative extraction output is:
17	\begin{small}
18	\begin{verbatim}
19	{"type": "predicate",
20	 "nl": "Charlie is kind",
21	 "z3": "kind_charlie == True"}
22	\end{verbatim}
23	\end{small}
24	\noindent The full extraction prompt template is provided in Appendix~\ref{app:prompts}.
25	
26	We define the \emph{extraction rate} as the fraction of traces from which at least one parseable constraint is successfully extracted. Traces that yield no valid constraints are excluded from the MAX-SAT stage but still contribute their answer to the candidate pool.
27	
28	Deduplication proceeds by syntactic equivalence matching across all extracted constraints. For each unique constraint $c_m$, its weight $w_m$ equals the number of distinct traces that produced a syntactically equivalent constraint. This weighting reflects the intuition that constraints appearing in many independent reasoning paths are more likely to encode genuine problem structure.
29	
30	\subsection{Weighted Partial MAX-SAT Formulation}
31	\label{sec:maxsat}
32	
33	Let $\mathcal{A}(q) = \{a : a \in \{a_1, \ldots, a_K\}\}$ denote the set of distinct candidate answers for question $q$, and let $\mathcal{C} = \{c_1, \ldots, c_M\}$ denote the deduplicated constraint pool with associated weights $\{w_1, \ldots, w_M\}$.
34	
35	\paragraph{MAX-SAT instance.} We formulate a Weighted Partial MAX-SAT (WPMS) problem where each unique constraint $c_m$ serves as a soft clause with weight $w_m$. The objective is to find the largest-weight subset $\mathcal{C}^* \subseteq \mathcal{C}$ such that all constraints in $\mathcal{C}^*$ are jointly satisfiable:
36	\begin{equation}
37	\label{eq:maxsat}
38	\mathcal{C}^* = \arg\max_{\mathcal{S} \subseteq \mathcal{C}} \sum_{c \in \mathcal{S}} w_c \quad \text{s.t.} \quad \mathcal{S} \text{ is satisfiable.}
39	\end{equation}
40	Z3's optimization engine solves this instance with a per-problem timeout of 10 seconds.
41	
42	\paragraph{Answer scoring.} Each candidate answer $a \in \mathcal{A}(q)$ is scored by the total weight of constraints in $\mathcal{C}^*$ that support it:
43	\begin{equation}
44	\label{eq:score}
45	\text{score}(a) = \sum_{c \in \mathcal{C}^*} w_c \cdot \sigma(c, a),
46	\end{equation}
47	where $\sigma(c, a) \in \{0, 1\}$ indicates whether constraint $c$ is consistent with answer $a$. In SICA's self-extraction setting, $\sigma(c, a) = 1$ if and only if $c$ was extracted from a trace whose final answer is $a$, reducing $\sigma$ to a source-answer indicator rather than an independent logical evaluation. The selected answer is $a^* = \arg\max_{a \in \mathcal{A}} \text{score}(a)$.
48	
49	\paragraph{Cross-answer constraint evaluation.}
50	A constraint $c_m$ extracted from trace $t_i$ (which produced answer $a_i$) must in principle be evaluated against \emph{all} candidate answers, not only $a_i$. In practice, however, self-extracted constraints are tightly coupled to their source answer. Because $c_m$ is derived from the reasoning steps that led to $a_i$, the semantic content of $c_m$ typically entails $a_i$. As a result, $\sigma(c_m, a_i) \approx 1$ holds for the source answer, while $\sigma(c_m, a_j)$ for $a_j \neq a_i$ depends on whether $c_m$ happens to also be consistent with $a_j$.
51	
52	This coupling has a critical consequence. When constraints lack discriminative power (i.e., $\sigma(c, a)$ is approximately constant across candidates, or constraints from different traces supporting different answers cancel out), the score function degenerates:
53	\begin{equation}
54	\label{eq:degenerate}
55	\text{score}(a) \approx \sum_{\substack{c \in \mathcal{C}^* \\ \text{source}(c) \to a}} w_c,
56	\end{equation}
57	which reduces to a weighted count of traces supporting $a$. If constraint weights are roughly uniform, this is equivalent to majority voting. The constraint ablation experiments in \S\ref{sec:experiments} confirm this degeneration empirically: MAX-SAT, count-only (selecting the answer with the most constraints regardless of satisfiability), and random-weight baselines all produce nearly identical accuracy.
58	
59	\subsection{The C0 Diagnostic}
60	\label{sec:c0}
61	
62	We define the multi-candidate rate $C_0$ as the fraction of questions for which the $K$ sampled traces produce more than one distinct answer:
63	\begin{equation}
64	\label{eq:c0}
65	C_0 = \frac{|\{q \in \mathcal{Q} : |\mathcal{A}(q)| > 1\}|}{|\mathcal{Q}|}.
66	\end{equation}
67	
68	$C_0$ serves as a zero-cost diagnostic for practitioners considering symbolic aggregation. When $C_0$ is low (e.g., below 5\%), nearly all questions are answered unanimously across traces, and SICA produces the same output as SC by construction. Low $C_0$ therefore represents a \emph{necessary condition} for SICA to differ from majority voting. High $C_0$ does not guarantee improvement, as it merely ensures that disagreement exists without ensuring that constraints can resolve it correctly. $C_0$ requires only the trace sampling stage and can be computed before any constraint extraction or solver invocation, making it a useful early stopping criterion.
69	
70	\subsection{Scope and Limitations}
71	\label{sec:scope}
72	
73	The SICA pipeline as evaluated here uses \emph{same-model self-extraction}: the same LLM that generates reasoning traces also extracts FOL constraints from those traces. This design choice isolates the question of whether an LLM's own reasoning can be usefully formalized for answer aggregation, but it also limits the scope of our findings.
74	
75	Our evaluation does not cover trained constraint extractors, external verification oracles, or multi-model cross-extraction setups. Published methods such as DyLoS \cite{zhang2026dylos}, Aristotle \cite{li2025aristotle}, FoVer \cite{wang2025fover}, and LogicAgent \cite{luo2025logicagent} achieve positive results on overlapping benchmarks through fundamentally different mechanisms (trained verifiers, multi-paradigm solver selection, logic-complete decomposition). Their findings are complementary to, not contradicted by, the negative results reported here. To disentangle extraction quality from aggregation effectiveness, we introduce an oracle variant that replaces self-extracted constraints with gold FOL annotations verified by Z3 (\S\ref{sec:oracle}).
76	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f948e60b-a12a-4eba-9690-a7ff8bd9ddb9",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "29f15f20-a0ed-4ffd-bf8d-a8343e9d984a",
  "sourceToolAssistantUUID": "f948e60b-a12a-4eba-9690-a7ff8bd9ddb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T17:30:21.582Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Gg8HSfPoXUu9hTRg8kaceq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29f15f20-a0ed-4ffd-bf8d-a8343e9d984a",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y9z1qvzokFPgYFvVFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "306e0dde-b4b1-4b21-b1ae-a658666e3ca0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBop8W5Pr5949R753jJ8Ny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 32262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1237,
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

_source line 30 · 2026-05-17T17:30:21.589Z_

<details><summary>↩ Tool result · `toolu_01Gg8HSfPoXUu9hTRg8kaceq`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across five instruction-tuned models and four reasoning benchmarks.
8	
9	\paragraph{Models.} We test Qwen2.5-14B-Instruct~\cite{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\cite{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\cite{dubey2024llama3}, DeepSeek-R1-Distill-Qwen-7B~\cite{guo2025deepseekr1}, and QwQ-32B~\cite{qwen2024qwq}. This selection spans 7B to 32B parameters and includes both standard instruction-tuned models and reasoning-specialized models (DeepSeek-R1, QwQ).
10	
11	\paragraph{Datasets.} FOLIO~\cite{han2022folio} provides formal logic problems with gold first-order logic (FOL) annotations ($n=204$), which enable the oracle control experiment (\S\ref{sec:oracle}). ProofWriter~\cite{tafjord2021proofwriter} tests multi-step deductive reasoning ($n=600$). StrategyQA~\cite{geva2021strategyqa} evaluates commonsense reasoning ($n=200$ for LLaMA-3.1-8B; $n=60$ for other models). ARC-Challenge~\cite{clark2018arc} covers science questions ($n=60$).
12	
13	\paragraph{Parameters.} Unless otherwise noted, we sample $K=12$ reasoning traces per question at temperature $T=0.7$. Z3~\cite{demoura2008z3} solves each MAX-SAT instance with a 10-second timeout. Temperature ablation experiments vary $T \in \{0.3, 0.5, 0.7, 1.0\}$.
14	
15	\paragraph{Metrics.} We report accuracy (\%), the multi-candidate rate $C_0$ (\S\ref{sec:c0}), and the accuracy gap $\Delta = \text{SICA} - \text{SC}$ in percentage points (pp). Statistical significance is assessed with the McNemar test for paired binary outcomes at $\alpha = 0.05$. For adequately powered conditions ($n \geq 200$), we also compute 95\% bootstrap confidence intervals with 1{,}000 resamples.
16	
17	
18	\subsection{Main Results: SICA Provides No Significant Gain}
19	\label{sec:main-results}
20	
21	Does symbolic constraint aggregation improve answer accuracy over majority voting? Table~\ref{tab:main_results} reports results across all model-domain conditions. The answer is no.
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Accuracy of Self-Consistency (SC) and SICA across models and domains. $\Delta$ denotes the SICA$-$SC gap in percentage points, computed from unrounded values. No condition reaches statistical significance ($\alpha = 0.05$). $\dagger$: $n=60$, insufficient power for confirmatory conclusions.}
27	\label{tab:main_results}
28	\begin{tabular}{@{}llrrrrl@{}}
29	\toprule
30	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & McNemar $p$ \\
31	\midrule
32	Qwen2.5-14B & FOLIO & 204 & 79.41 & 79.41 & 0.00 & --- \\
33	Qwen2.5-14B & ProofWriter & 600 & 75.17 & 75.50 & $+$0.33 & n.s. \\
34	Qwen2.5-14B & StrategyQA$^\dagger$ & 60 & 53.33 & 56.67 & $+$3.33 & 0.13 \\
35	Qwen2.5-14B & ARC-Chall.$^\dagger$ & 60 & 96.67 & 95.00 & $-$1.67 & --- \\
36	Mistral-7B & FOLIO+PW$^\dagger$ & 60 & 48.33 & 48.33 & 0.00 & 1.000 \\
37	LLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\
38	LLaMA-3.1-8B & FOLIO & 204 & 63.24 & 60.78 & $-$2.45 & 0.267 \\
39	DeepSeek-R1-7B & FOLIO+PW$^\dagger$ & 60 & 71.67 & 68.33 & $-$3.33 & 0.480 \\
40	\bottomrule
41	\end{tabular}
42	\end{table*}
43	
44	Across the four adequately powered conditions ($n \geq 200$, combined $N = 1{,}208$), the SICA--SC gap ranges from $-2.45$ to $+2.00$~pp. None reaches significance: the two nonzero gaps yield $p = 0.267$ and $p = 0.424$, and the remaining two conditions produce identical predictions. The largest positive gap ($+2.00$~pp, LLaMA-3.1-8B on StrategyQA) falls within chance variation ($p = 0.424$). The largest negative gap ($-2.45$~pp, LLaMA-3.1-8B on FOLIO) is similarly nonsignificant ($p = 0.267$), but its direction shows that SICA can harm accuracy when self-extracted constraints introduce noise.
45	
46	The four smaller conditions ($n=60$, marked $\dagger$) are consistent with this null pattern. Qwen2.5-14B on StrategyQA shows $\Delta = +3.33$~pp ($p = 0.13$), suggestive of a positive trend but underpowered to confirm it. DeepSeek-R1-7B on FOLIO+ProofWriter shows $\Delta = -3.33$~pp ($p = 0.480$). Two conditions produce identical outputs ($\Delta = 0$).
47	
48	Across eight conditions, five models, and more than 1,300 evaluation instances, SICA does not improve upon majority voting. The next three subsections investigate why.
49	
50	
51	\subsection{Oracle Control: The Aggregation Mechanism Is Effective}
52	\label{sec:oracle}
53	
54	Is the null result caused by a flawed aggregation mechanism, or by low-quality extracted constraints? To separate these explanations, we construct an oracle variant of SICA that replaces self-extracted FOL constraints with gold FOL annotations from the FOLIO dataset ($n = 204$). The oracle uses Z3 to evaluate ground-truth formulas against each candidate answer; all other pipeline components remain identical.
55	
56	Oracle-SICA achieves 88.24\% accuracy, compared to 79.41\% for both SC and standard SICA (Table~\ref{tab:main_results}). The improvement of $+8.82$~pp is highly significant (McNemar $p = 6.15 \times 10^{-5}$). Z3 satisfiability checks on gold FOL annotations agree with ground-truth labels for 193 of 204 problems (94.6\% agreement), so the solver operates correctly on well-formed constraints. This result establishes two conclusions. First, the weighted partial MAX-SAT aggregation mechanism is sound: given correct constraints, it recovers answers that majority voting misses. Second, the bottleneck lies entirely in constraint extraction quality. When the LLM extracts its own FOL constraints from reasoning traces, the resulting formulas do not carry enough discriminative signal to outperform vote counting. The oracle control is the strongest evidence that the capability trap is a constraint quality problem, not an aggregation design problem.
57	
58	
59	\subsection{Capability Trap Diagnostics}
60	\label{sec:diagnostics}
61	
62	Why does SICA fail to improve over SC? We examine three diagnostic dimensions: the multi-candidate rate $C_0$, constraint extraction quality, and the effect of sampling temperature on answer diversity.
63	
64	\paragraph{Multi-candidate rate.} Table~\ref{tab:capability_trap} reports $C_0$, extraction rate, and contradiction rate for each condition. Two distinct failure regimes emerge. For QwQ-32B, a reasoning-specialized model, $C_0$ is only 2.6\% across tested conditions. With over 97\% of questions answered unanimously across $K=12$ traces, SICA reduces to SC by construction and cannot provide any benefit regardless of constraint quality. For instruction-tuned models (Qwen2.5-14B, Mistral-7B, LLaMA-3.1-8B, DeepSeek-R1-7B), $C_0$ ranges from 5.0\% (ARC-Challenge) to 61.8\% (FOLIO with LLaMA-3.1-8B). Higher $C_0$ creates more questions where SICA could in principle differ from SC, yet $\Delta$ remains nonsignificant across all conditions. High $C_0$ is necessary but not sufficient: disagreement among traces exists, but the extracted constraints cannot resolve it correctly. Figure~\ref{fig:operating_regime} maps $C_0$ against the SICA--SC gap for all conditions, and the gap stays centered around zero regardless of $C_0$.
65	
66	\begin{table*}[t]
67	\centering
68	\small
69	\caption{Capability trap diagnostics. $C_0$: fraction of questions with multiple distinct candidate answers across $K=12$ traces. Extraction rate: fraction of traces yielding at least one parseable FOL constraint. Contradiction rate: fraction of extracted constraint sets with internal contradictions. $\Delta$: SICA$-$SC gap (pp), repeated from Table~\ref{tab:main_results} for reference. $\dagger$: $n=60$. $^*$Combined rate from a single run covering both FOLIO and ProofWriter.}
70	\label{tab:capability_trap}
71	\begin{tabular}{@{}llrrrr@{}}
72	\toprule
73	Model & Domain & $C_0$ (\%) & Extr.\ Rate & Contr.\ Rate & $\Delta$ (pp) \\
74	\midrule
75	Qwen2.5-14B & FOLIO & 38.2$^*$ & 0.89 & 0.022 & 0.00 \\
76	Qwen2.5-14B & ProofWriter & 38.2$^*$ & 0.89 & 0.022 & $+$0.33 \\
77	Qwen2.5-14B & StrategyQA$^\dagger$ & 10.0 & 0.70 & --- & $+$3.33 \\
78	Qwen2.5-14B & ARC-Chall.$^\dagger$ & 5.0 & 1.00 & --- & $-$1.67 \\
79	Mistral-7B & FOLIO+PW$^\dagger$ & 50.0 & 0.88 & 0.056 & 0.00 \\
80	LLaMA-3.1-8B & StrategyQA & 41.0 & --- & --- & $+$2.00 \\
81	LLaMA-3.1-8B & FOLIO & 61.8 & 0.94 & 0.062 & $-$2.45 \\
82	DeepSeek-R1-7B & FOLIO+PW$^\dagger$ & 58.3 & 0.84 & 0.037 & $-$3.33 \\
83	\bottomrule
84	\end{tabular}
85	\end{table*}
86	
87	\paragraph{Extraction quality.} Extraction rates are generally high (0.70 to 1.00), and contradiction rates remain below 7\% across all measured conditions. These metrics indicate that the extraction pipeline is mechanically functional: the LLM produces well-formed, internally consistent constraints at high rates. The problem is not extraction failure but extraction vacuity. The constraints are syntactically valid but semantically redundant with the answer they were derived from, as analyzed in \S\ref{sec:maxsat} and confirmed by the ablation in \S\ref{sec:ablation}. Even with LLaMA-3.1-8B on FOLIO, where $C_0 = 61.8\%$ and extraction rate reaches 0.94, $\Delta$ is $-2.45$~pp. The highest extraction quality among all conditions corresponds to SICA performing \emph{worse} than SC.
88	
89	\paragraph{Temperature ablation.} If SICA's failure stems from insufficient answer diversity at $T = 0.7$, increasing temperature should raise $C_0$ and create more opportunities for constraint-based discrimination. We test $T \in \{0.3, 0.5, 0.7, 1.0\}$ with Qwen2.5-14B on a 60-question subset. $C_0$ ranges from 30.0\% ($T=0.3$) to 53.3\% ($T=0.7$) across temperatures. However, $\Delta$ is exactly 0.0~pp at $T \in \{0.3, 0.5, 1.0\}$ and $+3.3$~pp at $T = 0.7$ ($n = 60$, not significant). Higher diversity does not translate into better constraint discrimination. Figure~\ref{fig:capability_scatter} plots the per-problem relationship between vote entropy and constraint exclusion rate for a representative condition.
90	
91	\begin{figure}[t]
92	\centering
93	% \includegraphics[width=\columnwidth]{figures/capability_scatter.pdf}
94	\caption{Per-problem scatter of vote entropy (x-axis) versus constraint exclusion rate (y-axis) for Qwen2.5-14B on FOLIO. Problems with high vote entropy (ambiguous majority vote) do not benefit from constraint filtering; the constraints fail to resolve disagreement among traces.}
95	\label{fig:capability_scatter}
96	\end{figure}
97	
98	\begin{figure}[t]
99	\centering
100	% \includegraphics[width=\columnwidth]{figures/operating_regime.pdf}
101	\caption{Multi-candidate rate $C_0$ (x-axis) versus SICA$-$SC accuracy gap (y-axis) across all model-domain conditions. Each point represents one condition from Table~\ref{tab:main_results}. The gap remains centered around zero regardless of $C_0$: answer diversity alone does not enable constraint-based improvement.}
102	\label{fig:operating_regime}
103	\end{figure}
104	
105	The diagnostic picture is consistent across all three dimensions: SICA fails not because of insufficient diversity or mechanical extraction errors, but because the extracted constraints carry no discriminative signal beyond the votes they were derived from.
106	
107	
108	\subsection{Constraint Ablation: MAX-SAT Degenerates to Counting}
109	\label{sec:ablation}
110	
111	The diagnostics above suggest that self-extracted constraints are semantically coupled to their source answers and therefore non-discriminative. If so, the MAX-SAT formulation should produce the same predictions as simpler baselines that ignore constraint satisfiability. We test this prediction with three ablation variants on Qwen2.5-14B across combined FOLIO and ProofWriter data ($n = 804$):
112	
113	\begin{itemize}
114	\item \textbf{SICA (MAX-SAT):} The full pipeline as described in \S\ref{sec:method}.
115	\item \textbf{Count-only:} Select the answer supported by the most constraints, ignoring satisfiability.
116	\item \textbf{Random-weight:} Randomize constraint weights before MAX-SAT solving.
117	\end{itemize}
118	
119	\begin{table}[t]
120	\centering
121	\small
122	\caption{Constraint ablation (Qwen2.5-14B, $n = 804$, FOLIO + ProofWriter). SC serves as the majority-vote baseline. Agreement indicates the number of predictions identical to SC out of 804. All constraint-based variants produce nearly identical outputs.}
123	\label{tab:ablation}
124	\begin{tabular}{@{}lrc@{}}
125	\toprule
126	Aggregation & Acc.\ (\%) & Agreement w/ SC \\
127	\midrule
128	SC (majority vote) & 76.24 & --- \\
129	SICA (MAX-SAT) & 76.49 & 802\,/\,804 \\
130	Count-only & 76.62 & 802\,/\,804 \\
131	Random-weight & 76.37 & 802\,/\,804 \\
132	\bottomrule
133	\end{tabular}
134	\end{table}
135	
136	Table~\ref{tab:ablation} reports the results. All three constraint-based variants agree with SC on 802 of 804 predictions (99.8\%). The count-only baseline, which ranks answers solely by the number of supporting constraints without any satisfiability check, achieves accuracy within 0.25~pp of the full MAX-SAT formulation. The random-weight variant, which destroys the learned constraint weights, performs similarly. These near-identical outcomes confirm the degeneration predicted in Equation~\ref{eq:degenerate}: because self-extracted constraints are tightly coupled to their source answers, the MAX-SAT solver effectively reduces to a weighted vote count. The satisfiability structure adds no discriminative power beyond what simple counting already provides.
137	
138	This ablation directly supports the capability trap thesis. Symbolic verification \emph{can} improve answer selection, as the oracle control demonstrates with $+8.82$~pp over SC. But the improvement requires constraints that encode independent problem structure. Self-extracted constraints instead encode the reasoning steps that produced each candidate answer, and so they are redundant with the votes they accompany.
139	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "306e0dde-b4b1-4b21-b1ae-a658666e3ca0",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "b6ef62c1-2705-42bb-9d00-2e641f1a3a04",
  "sourceToolAssistantUUID": "306e0dde-b4b1-4b21-b1ae-a658666e3ca0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T17:30:22.049Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EmW2oCEue7bfyRkgkpZpwc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6ef62c1-2705-42bb-9d00-2e641f1a3a04",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y9z1qvzokFPgYFvVFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce248f8d-351f-47ca-a4cf-2aa504f7f5ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBop8W5Pr5949R753jJ8Ny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 32262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1237,
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

_source line 32 · 2026-05-17T17:30:22.060Z_

<details><summary>↩ Tool result · `toolu_01EmW2oCEue7bfyRkgkpZpwc`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	% Phase 2: To be written after experiments are finalized.
5	% Structure (from writing_plan.yaml):
6	% 1. Oracle experiment as causal intervention
7	% 2. Why DyLoS/Aristotle/FoVer work: bypass same-model self-extraction
8	% 3. Constructive direction: trained extractors, external provers
9	% 4. C0 as deployment diagnostic
10	% 5. Limitations
11	
12	\textbf{[PLACEHOLDER -- Discussion deferred to Phase 2]}
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce248f8d-351f-47ca-a4cf-2aa504f7f5ad",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "d64e80c1-0d3a-4e11-8dfe-d3cf13a4190a",
  "sourceToolAssistantUUID": "ce248f8d-351f-47ca-a4cf-2aa504f7f5ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T17:30:22.410Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LC3FwS5A7Kmi33HBYBzpCV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d64e80c1-0d3a-4e11-8dfe-d3cf13a4190a",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8Y9z1qvzokFPgYFvVFe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c548a44f-a28c-4b3e-b5e4-39121043ed3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBop8W5Pr5949R753jJ8Ny",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 32262,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1237
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 343,
          "cache_read_input_tokens": 32262,
          "cache_creation_input_tokens": 1237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1237,
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

_source line 34 · 2026-05-17T17:30:22.421Z_

<details><summary>↩ Tool result · `toolu_01LC3FwS5A7Kmi33HBYBzpCV`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	% Phase 2: To be written last.
5	% Structure (from writing_plan.yaml):
6	% 1. Summary: SICA = SC across 5 models x 3 domains
7	% 2. But aggregation works: +8.82pp with gold constraints
8	% 3. Sole bottleneck: self-extraction quality
9	% 4. Practical: C0 diagnostic
10	% 5. Future: trained extractors, external provers, cross-model constraints
11	
12	\textbf{[PLACEHOLDER -- Conclusion deferred to Phase 2]}
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c548a44f-a28c-4b3e-b5e4-39121043ed3d",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "1785ca36-e6c4-444a-b66a-56d993847948",
  "sourceToolAssistantUUID": "c548a44f-a28c-4b3e-b5e4-39121043ed3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T17:30:26.970Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T3Y7Do8DtggEBdzvg5f7VW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1785ca36-e6c4-444a-b66a-56d993847948",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8YALyfhdNbv6P1VfNeP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59cdc68e-f144-41b4-b408-b7ba7399762b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCL2zkvEDKXNkExLe5CRkq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8041,
      "cache_read_input_tokens": 33499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8041,
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

_source line 36 · 2026-05-17T17:30:26.986Z_

<details><summary>↩ Tool result · `toolu_01T3Y7Do8DtggEBdzvg5f7VW`</summary>

```text
1	\section{Extraction Prompt Template}
2	\label{app:prompts}
3	
4	% Full prompt template used for constraint extraction in §3.2.
5	\textbf{[PLACEHOLDER -- Prompt template to be added]}
6	
7	\section{Additional Experimental Results}
8	\label{app:additional-results}
9	
10	% Tables 5-7: Tiebreak analysis, K-sensitivity ablation, overhead analysis
11	\textbf{[PLACEHOLDER -- Appendix tables to be added]}
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59cdc68e-f144-41b4-b408-b7ba7399762b",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "a6812136-1b8e-4af7-8adb-a9525cb4598d",
  "sourceToolAssistantUUID": "59cdc68e-f144-41b4-b408-b7ba7399762b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T17:30:27.521Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BKmyvD5aYNt8UGVbwZGTog`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6812136-1b8e-4af7-8adb-a9525cb4598d",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8YALyfhdNbv6P1VfNeP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8938721-9f0c-417b-a8b5-fea5674866a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCL2zkvEDKXNkExLe5CRkq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8041,
      "cache_read_input_tokens": 33499,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8041
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 33499,
          "cache_creation_input_tokens": 8041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8041,
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

_source line 38 · 2026-05-17T17:30:27.536Z_

<details><summary>↩ Tool result · `toolu_01BKmyvD5aYNt8UGVbwZGTog`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/writing_plan.yaml\", \"content\": \"# Writing Plan — symb_invariant_consensus\\n# Generated: 2026-05-17T17:00:00Z\\n# Updated: 2026-05-17 — Oracle result (exp-021) incorporated, narrative upgraded\\n# Paper Agent Step 1 output\\n\\nmeta:\\n  venue: EMNLP 2026\\n  track: main\\n  template: templates/latex/acl/\\n  template_note: \\\"ACL template shared by EMNLP; confirm 2026 style options when official EMNLP 2026 CFP releases\\\"\\n  page_limit: 8\\n  deadline: 2026-05-25\\n  core_claim: >\\n    LLM self-extracted FOL constraints cannot improve majority voting (SICA = SC across\\n    5 models x 3 domains, N>1,300), but this is NOT a failure of the aggregation mechanism:\\n    Oracle-SICA with gold FOL + Z3 achieves +8.82pp (p<0.001), proving MAX-SAT aggregation\\n    is effective given high-quality constraints. The sole bottleneck is LLM self-extraction\\n    quality. We provide a complete diagnosis: (1) characterize the capability trap,\\n    (2) localize the failure to extraction (not aggregation), (3) quantify the recoverable\\n    performance gap (+8.82pp).\\n  paper_type: \\\"Diagnostic analysis paper (negative result + causal localization + constructive upper bound)\\\"\\n  created_at: 2026-05-17T17:00:00Z\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 220\\n    phase: 2\\n    core_bullets:\\n      - \\\"Problem: symbolic methods propose extracting FOL constraints from LLM traces to improve aggregation, but same-model self-extraction has not been rigorously evaluated\\\"\\n      - \\\"Method: systematic evaluation of SICA (MAX-SAT over self-extracted FOL) across 3 domains x 5 model families (N>1,300)\\\"\\n      - \\\"Negative result: SICA provides no gain over SC in all conditions (all delta n.s.)\\\"\\n      - \\\"Causal localization: Oracle-SICA (gold FOL + Z3) achieves +8.82pp (p<0.001), proving aggregation works but self-extraction is the bottleneck\\\"\\n      - \\\"Constructive: temperature ablation confirms diversity is not the issue; trained extractors / external provers can unlock +8.82pp\\\"\\n    dependencies: [experiments, method]\\n\\n  - section: introduction\\n    word_budget: 1300\\n    phase: 2\\n    core_bullets:\\n      - \\\"Hook: neuro-symbolic methods (Logic-LM, DyLoS, Aristotle, FoVer) show promise augmenting LLM reasoning with formal solvers\\\"\\n      - \\\"Gap: these methods use trained verifiers or external solvers; does same-model self-extraction suffice?\\\"\\n      - \\\"Our approach: systematic SICA evaluation + oracle control experiment to separate extraction from aggregation\\\"\\n      - \\\"Key finding: aggregation mechanism is sound (+8.82pp with gold constraints), but self-extraction produces non-discriminative constraints\\\"\\n      - \\\"Positioning: DyLoS/Aristotle/FoVer succeed because they avoid same-model self-extraction\\\"\\n      - \\\"Contributions: [C1] capability trap characterization, [C2] causal localization via oracle experiment, [C3] quantified recoverable gap (+8.82pp), [C4] C0 diagnostic\\\"\\n    dependencies: [experiments, method]\\n    figures: [fig1_pipeline]\\n    citation_hints:\\n      - \\\"Logic-LM, LINC, DyLoS, Aristotle, FoVer for neuro-symbolic context\\\"\\n      - \\\"Wang et al. 2023 SC, Chen et al. 2023 USC for baselines\\\"\\n\\n  - section: related_work\\n    word_budget: 900\\n    phase: 1\\n    core_bullets:\\n      - \\\"Cluster 1: SC and extensions (SC, USC, weighted SC, scaling)\\\"\\n      - \\\"Cluster 2: Neuro-symbolic reasoning (Logic-LM, LINC, DyLoS, Aristotle, FoVer, LogicAgent) — distinguish trained/external verifiers from same-model self-extraction\\\"\\n      - \\\"Cluster 3: Test-time compute and reasoning models (Snell et al., DeepSeek-R1, diversity-aware TTS)\\\"\\n      - \\\"Cluster 4: Verification and reranking (ORM, PRM, Math-Shepherd)\\\"\\n      - \\\"Cluster 5: Constraint satisfaction in NLP (SATBench, LLM+CP)\\\"\\n      - \\\"Cluster 6: Debate and multi-agent aggregation\\\"\\n    dependencies: []\\n\\n  - section: method\\n    word_budget: 1400\\n    phase: 1\\n    core_bullets:\\n      - \\\"SICA pipeline: K-trace generation -> FOL constraint extraction -> deduplication -> weighted partial MAX-SAT -> answer selection\\\"\\n      - \\\"MAX-SAT formulation with EXPLICIT cross-answer evaluation\\\"\\n      - \\\"C0 definition: multi-candidate rate as necessary-but-insufficient condition\\\"\\n      - \\\"Oracle experiment design: replace self-extracted constraints with FOLIO gold FOL annotations; Z3 satisfiability check as constraint verification\\\"\\n      - \\\"Scope statement: same-model self-extraction pipeline; oracle as causal intervention\\\"\\n    dependencies: []\\n    figures: [fig1_pipeline]\\n    notation_table:\\n      K: \\\"number of reasoning traces sampled per problem\\\"\\n      T: \\\"temperature for trace generation\\\"\\n      C: \\\"set of extracted FOL constraints\\\"\\n      c_i: \\\"individual constraint from trace t_i\\\"\\n      w_i: \\\"weight of constraint c_i\\\"\\n      A: \\\"candidate answer set {a_1, ..., a_m}\\\"\\n      C0: \\\"multi-candidate rate: fraction of problems with |A|>1\\\"\\n    registry_refs: [sica_expanded_14b, sica_constraint_ablation_013, exp-021-oracle-folio]\\n\\n  - section: experiments\\n    word_budget: 2400\\n    phase: 1\\n    core_bullets:\\n      - \\\"Setup: 5 models x 3+ domains, K=12, T=0.7\\\"\\n      - \\\"Models: Qwen2.5-14B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B, QwQ-32B\\\"\\n      - \\\"Datasets: FOLIO (formal logic, 204), ProofWriter (deductive, 600), StrategyQA (commonsense, 200), ARC-Challenge (science, 60), GSM8K (math, 30 pilot)\\\"\\n      - \\\"Metrics: accuracy, C0, McNemar test, bootstrap CI\\\"\\n      - \\\"Main results (T1): SICA = SC all conditions, N>1,300\\\"\\n      - \\\"Oracle control (T2): Oracle-SICA 88.24% vs SC 79.41% vs SICA(self) 79.41%, +8.82pp, p=6.15e-05\\\"\\n      - \\\"Constraint ablation (T3): MAX-SAT = count-only = random-weight (n=804) [BLOCKED: exp-013 data pending, leave placeholder]\\\"\\n      - \\\"Temperature ablation (T4): report 3 points only (T=0.3/0.5/1.0 from same ablation run, C0 30%->38.3%->43.3%); T=0.7 C0=53.3% from sica_d012_14b is a different run, note in table footnote; OR wait for T=0.7 re-run\\\"\\n      - \\\"Two failure regimes: (1) Constraint-present but non-discriminative (FOLIO/PW, C0>20%, extraction >80% but precision ~50%) = capability trap core; (2) Constraint-absent / extraction-degenerate (GSM8K extraction 14.7%, ARC C0<5%) = SICA has no operational basis\\\"\\n      - \\\"Operating regime: QwQ C0<5% -> SICA=SC; instruction models C0=38-62% -> constraints non-discriminative; GSM8K illustrates C0-degenerate regime (do NOT use to argue non-discriminative constraints)\\\"\\n    dependencies: []\\n    registry_refs:\\n      - sica_expanded_14b\\n      - exp-010-mistral-v3\\n      - exp-014-deepseek-r1-7b\\n      - exp-019-llama8b-strategyqa-200\\n      - exp-020-llama8b-folio-204\\n      - sica_constraint_ablation_013\\n      - exp-021-oracle-folio\\n      - temperature-ablation-t03\\n      - temperature-ablation-t05\\n      - temperature-ablation-t10\\n      - exp-005\\n      - exp-009-overhead-analysis\\n      - exp-016-weighted-sc\\n      - sica_k_sensitivity_14b\\n      - exp-017-strategyqa-v3\\n      - exp-018-arc-v2\\n      - exp-012-gsm8k-pilot\\n    tables: [tab1_main_results, tab2_oracle_control, tab3_ablation, tab4_temperature]\\n    figures: [fig2_capability_scatter, fig3_operating_regime]\\n\\n  - section: discussion\\n    word_budget: 600\\n    phase: 2\\n    core_bullets:\\n      - \\\"Oracle experiment as causal intervention: isolates extraction from aggregation\\\"\\n      - \\\"Why DyLoS/Aristotle/FoVer work: they bypass same-model self-extraction (trained verifiers, external provers, multi-paradigm solvers)\\\"\\n      - \\\"Constructive direction: better extraction methods (trained verifiers, external provers) can unlock +8.82pp potential\\\"\\n      - \\\"C0 as deployment diagnostic: necessary but not sufficient\\\"\\n      - \\\"Limitations: FOLIO-only oracle (gold FOL available), n=60 for some conditions, no trained extractor comparison\\\"\\n    dependencies: [experiments]\\n\\n  - section: conclusion\\n    word_budget: 350\\n    phase: 2\\n    core_bullets:\\n      - \\\"Summary: SICA provides no accuracy gain over SC across 5 models and 3 domains\\\"\\n      - \\\"But aggregation mechanism is sound: +8.82pp with gold constraints (p<0.001)\\\"\\n      - \\\"Sole bottleneck: LLM self-extraction quality (non-discriminative constraints)\\\"\\n      - \\\"Practical: C0 as zero-cost go/no-go diagnostic\\\"\\n      - \\\"Future: trained extractors, external provers, cross-model constraints as paths to unlock potential\\\"\\n    dependencies: [experiments, method]\\n\\nvisualization_plan:\\n  - fig_id: fig1_pipeline\\n    type: conceptual\\n    tool: matplotlib\\n    description: >\\n      SICA pipeline diagram: K reasoning traces (with temperature sampling) ->\\n      FOL constraint extraction -> deduplication -> weighted partial MAX-SAT solver ->\\n      answer selection. Side-by-side with SC (majority voting) for comparison.\\n      Must show where cross-answer evaluation happens. Add oracle branch showing\\n      gold FOL + Z3 replacing self-extraction.\\n    placement: method\\n    aspect_ratio: \\\"16:6\\\"\\n    data_source: \\\"manual\\\"\\n\\n  - fig_id: fig2_capability_scatter\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Hero figure: per-problem analysis of n=307 multi-candidate problems from exp-001.\\n      Scatter of vote_entropy vs constraint_exclusion_rate, colored by SICA flip direction\\n      (positive flip / negative flip / no change). Shows constraints are non-discriminative\\n      regardless of diversity level.\\n    data_source: \\\"artifact: f2_per_problem_csv (art_20260517_c29c72)\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n\\n  - fig_id: fig3_operating_regime\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Operating regime summary: grouped bar or heatmap showing C0, SICA-SC delta,\\n      and constraint quality across all model-domain conditions. Include oracle result\\n      as highlighted row/bar showing the gap between self-extraction and gold constraints.\\n    data_source: \\\"registry: sica_expanded_14b, exp-010-mistral-v3, exp-014-deepseek-r1-7b, exp-019-llama8b-strategyqa-200, exp-020-llama8b-folio-204, exp-005, exp-021-oracle-folio\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n\\ntable_plan:\\n  - table_id: tab1_main_results\\n    caption: \\\"Main results: SICA vs. SC accuracy across 5 model families and 3 reasoning domains. No condition shows statistically significant improvement (N>1,300 combined).\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Model, Domain, N, \\\"SC(%)\\\", \\\"SICA(%)\\\", \\\"Delta(pp)\\\", \\\"p\\\"]\\n    data_source: \\\"registry: sica_expanded_14b, exp-010-mistral-v3, exp-014-deepseek-r1-7b, exp-019-llama8b-strategyqa-200, exp-020-llama8b-folio-204, exp-005, exp-017-strategyqa-v3, exp-018-arc-v2\\\"\\n    notes: \\\"n=60 conditions marked with dagger; 'suggestive/consistent with' language per D037\\\"\\n\\n  - table_id: tab2_oracle_control\\n    caption: \\\"Oracle control experiment on FOLIO (N=204): replacing self-extracted constraints with gold FOL annotations + Z3 verification yields +8.82pp over SC (p<0.001), proving aggregation mechanism is effective.\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Method, \\\"Constraint Source\\\", \\\"Accuracy(%)\\\", \\\"Delta vs SC(pp)\\\", \\\"McNemar p\\\"]\\n    data_source: \\\"registry: exp-021-oracle-folio\\\"\\n    rows:\\n      - [\\\"SC (majority vote)\\\", \\\"N/A\\\", 79.41, \\\"—\\\", \\\"—\\\"]\\n      - [\\\"SICA (self-extracted)\\\", \\\"LLM self-extraction\\\", 79.41, 0.00, 1.0]\\n      - [\\\"Oracle-SICA\\\", \\\"Gold FOL + Z3\\\", 88.24, \\\"+8.82\\\", \\\"6.15e-05\\\"]\\n    notes: \\\"Key evidence separating extraction quality from aggregation mechanism\\\"\\n\\n  - table_id: tab3_ablation\\n    caption: \\\"Constraint ablation on N=804 problems (Qwen2.5-14B): MAX-SAT vs. count-only vs. random-weight aggregation yield near-identical accuracy (agreement: 802/804).\\\"\\n    placement: experiments\\n    type: ablation\\n    columns: [Aggregation, \\\"Accuracy(%)\\\", \\\"McNemar p vs SC\\\"]\\n    data_source: \\\"registry: sica_constraint_ablation_013\\\"\\n    baseline_row: \\\"SC (majority voting)\\\"\\n\\n  - table_id: tab4_temperature\\n    caption: \\\"Temperature ablation (Qwen2.5-14B, FOLIO 60): increasing T from 0.3 to 1.0 monotonically increases C0 (30% to 43%) but SICA-SC delta remains exactly 0 with zero discordant pairs.\\\"\\n    placement: experiments\\n    type: ablation\\n    columns: [Temperature, \\\"C0(%)\\\", \\\"SC(%)\\\", \\\"SICA(%)\\\", \\\"Delta(pp)\\\", \\\"Discordant\\\"]\\n    data_source: \\\"registry: temperature-ablation-t03, temperature-ablation-t05, sica_d012_14b, temperature-ablation-t10\\\"\\n    notes: \\\"Directly demonstrates diversity is not the bottleneck\\\"\\n\\n  - table_id: tab5_tiebreak\\n    caption: \\\"Tiebreak analysis: SICA resolves SC ties with 80% accuracy vs. 50% random baseline, but ties are too rare (<5% of problems) to affect aggregate accuracy.\\\"\\n    placement: appendix\\n    type: statistics\\n    columns: [Method, \\\"Tie Accuracy(%)\\\", \\\"Tied Problems(%)\\\"]\\n    data_source: \\\"registry: sica_expanded_14b\\\"\\n\\n  - table_id: tab6_k_ablation\\n    caption: \\\"K-sensitivity ablation (Qwen2.5-14B): SICA never outperforms SC across K={6,8,11,12,16,20}.\\\"\\n    placement: appendix\\n    type: ablation\\n    columns: [K, \\\"SC(%)\\\", \\\"SICA(%)\\\", \\\"Delta(pp)\\\"]\\n    data_source: \\\"registry: sica_k_sensitivity_14b\\\"\\n\\n  - table_id: tab7_overhead\\n    caption: \\\"Computational overhead: SICA adds ~49% wall-clock time over SC, dominated by constraint extraction (47%).\\\"\\n    placement: appendix\\n    type: statistics\\n    columns: [Stage, \\\"Time(s)\\\", \\\"Fraction(%)\\\"]\\n    data_source: \\\"registry: exp-009-overhead-analysis\\\"\\n\\nliterature_strategy:\\n  citation_budget: 38\\n  macro_context:\\n    - \\\"LLM symbolic reasoning and constraint-based aggregation\\\"\\n    - \\\"Self-consistency and test-time compute scaling\\\"\\n    - \\\"Oracle/upper-bound experiments in NLP\\\"\\n  micro_clusters:\\n    - cluster_name: \\\"self_consistency_and_variants\\\"\\n      search_queries:\\n        - \\\"self-consistency chain of thought voting 2023 2024 2025\\\"\\n        - \\\"weighted self-consistency confidence LLM\\\"\\n      must_cite:\\n        - \\\"Wang et al. 2023 (SC)\\\"\\n        - \\\"Chen et al. 2024 (USC)\\\"\\n        - \\\"Taubenfeld et al. 2025 (confidence SC)\\\"\\n        - \\\"Loo et al. 2025 (SC scaling)\\\"\\n      target_count: 6\\n\\n    - cluster_name: \\\"symbolic_reasoning_llm\\\"\\n      search_queries:\\n        - \\\"neuro-symbolic reasoning LLM FOL solver 2024 2025\\\"\\n        - \\\"Logic-LM LINC symbolic solver language model\\\"\\n      must_cite:\\n        - \\\"Pan et al. 2023 (Logic-LM)\\\"\\n        - \\\"Olausson et al. 2023 (LINC)\\\"\\n        - \\\"Xu et al. 2026 (DyLoS)\\\"\\n        - \\\"FoVer 2025 (TACL)\\\"\\n        - \\\"LogicAgent 2025\\\"\\n        - \\\"Aristotle 2025 (ACL)\\\"\\n      target_count: 8\\n\\n    - cluster_name: \\\"test_time_compute_scaling\\\"\\n      search_queries:\\n        - \\\"test-time compute scaling LLM 2024 2025\\\"\\n        - \\\"reasoning model diversity collapse temperature\\\"\\n      must_cite:\\n        - \\\"Snell et al. 2025 (ICLR Oral)\\\"\\n        - \\\"DeepSeek-R1 2025 (Nature)\\\"\\n        - \\\"Diversity-Aware TTS 2025\\\"\\n      target_count: 5\\n\\n    - cluster_name: \\\"verification_reranking\\\"\\n      search_queries:\\n        - \\\"outcome reward model process reward model verification 2023 2024\\\"\\n        - \\\"Math-Shepherd verification LLM\\\"\\n      must_cite:\\n        - \\\"Cobbe et al. 2021 (ORM/GSM8K)\\\"\\n        - \\\"Lightman et al. 2023 (PRM)\\\"\\n      target_count: 4\\n\\n    - cluster_name: \\\"constraint_satisfaction_nlp\\\"\\n      search_queries:\\n        - \\\"MAX-SAT constraint satisfaction NLP reasoning 2024 2025\\\"\\n        - \\\"LLM constraint propagation formal methods\\\"\\n      must_cite:\\n        - \\\"SATBench 2025 (EMNLP)\\\"\\n        - \\\"LLM Meets CP 2025 (IJCAI)\\\"\\n      target_count: 3\\n\\n    - cluster_name: \\\"debate_multi_agent\\\"\\n      search_queries:\\n        - \\\"LLM debate multi-agent reasoning aggregation 2023 2024\\\"\\n      must_cite:\\n        - \\\"Liang et al. 2023\\\"\\n        - \\\"Du et al. 2023\\\"\\n      target_count: 3\\n\\n    - cluster_name: \\\"benchmarks_and_datasets\\\"\\n      search_queries:\\n        - \\\"FOLIO benchmark logical reasoning 2022\\\"\\n        - \\\"ProofWriter dataset deductive 2021\\\"\\n        - \\\"StrategyQA commonsense reasoning\\\"\\n      must_cite:\\n        - \\\"Han et al. 2022 (FOLIO)\\\"\\n        - \\\"Tafjord et al. 2021 (ProofWriter)\\\"\\n        - \\\"Geva et al. 2021 (StrategyQA)\\\"\\n        - \\\"Clark et al. 2018 (ARC)\\\"\\n      target_count: 4\\n\\n    - cluster_name: \\\"negative_results_analysis\\\"\\n      search_queries:\\n        - \\\"negative results NLP analysis paper EMNLP 2024 2025\\\"\\n        - \\\"when does method fail systematic evaluation LLM\\\"\\n      must_cite: []\\n      target_count: 2\\n\\n    - cluster_name: \\\"oracle_upper_bound_experiments\\\"\\n      search_queries:\\n        - \\\"oracle upper bound experiment NLP evaluation 2023 2024\\\"\\n        - \\\"gold annotation controlled experiment LLM pipeline\\\"\\n      must_cite: []\\n      target_count: 3\\n\\nwriting_order:\\n  - method\\n  - experiments\\n  - related_work\\n  - introduction\\n  - discussion\\n  - abstract\\n  - conclusion\\n\", \"total_chars\": 16394, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8938721-9f0c-417b-a8b5-fea5674866a8",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "61261c18-08a6-4f89-8250-79833a74a658",
  "sourceToolAssistantUUID": "c8938721-9f0c-417b-a8b5-fea5674866a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-17T17:30:30.433Z_

Now let me also check the latest dream report for a more complete paper draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61261c18-08a6-4f89-8250-79833a74a658",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8YAiopgNZmvFycR1XTR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1395874-8c13-49ab-b5c7-3ea600e9fbcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gtv67apmAALtEq1rheK6oH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6683,
      "cache_read_input_tokens": 41540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6683,
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

_source line 40 · 2026-05-17T17:30:32.576Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P19UZV4HbgemUC8a5B4v4E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1395874-8c13-49ab-b5c7-3ea600e9fbcf",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8YAiopgNZmvFycR1XTR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad443eda-e247-48f8-be81-1cbe3c1e62ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gtv67apmAALtEq1rheK6oH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6683,
      "cache_read_input_tokens": 41540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6683,
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

_source line 41 · 2026-05-17T17:30:32.843Z_

<details><summary>↩ Tool result · `toolu_01P19UZV4HbgemUC8a5B4v4E`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{natbib}
12	\usepackage{tabularx}
13	\usepackage{caption}
14	\usepackage{subcaption}
15	
16	\newcommand{\sica}{\textsc{Sica}}
17	\newcommand{\scmethod}{\textsc{SC}}
18	\newcommand{\czero}{$C_0$}
19	
20	\title{The Capability Trap: Why Self-Extracted Constraints\\Cannot Improve LLM Majority Voting}
21	
22	\author{Anonymous}
23	\date{}
24	
25	\begin{document}
26	\maketitle
27	
28	% ============================================================
29	% ABSTRACT
30	% ============================================================
31	\begin{abstract}
32	Recent work augments Large Language Model (LLM) reasoning with symbolic methods that extract first-order logic (FOL) constraints from reasoning traces and aggregate them via solvers such as MAX-SAT.
33	We ask a practical question: when does such symbolic aggregation improve over simple majority voting (Self-Consistency, SC)?
34	We instantiate the paradigm as \sica{} (Symbolic Invariant Consensus Aggregation), which extracts FOL constraints from sampled reasoning traces and selects answers via weighted MAX-SAT, and evaluate it across three reasoning domains (formal logic, commonsense, science) and five model families spanning instruction-tuned, distilled-reasoning, and full-reasoning architectures.
35	Across all 18 tested conditions (combined $N{>}1{,}300$), \sica{} provides no significant accuracy gain over SC, with per-condition $\Delta$ ranging from $-3.3$pp to $+2.0$pp.
36	We identify the structural cause: a \emph{capability trap} in which self-extracted constraints achieve precision $\approx 0.50$ (no better than chance) at distinguishing correct from incorrect answers, causing MAX-SAT to degenerate to weighted counting.
37	A constraint ablation confirms that MAX-SAT, count-only, and random-weight aggregation produce statistically identical results ($>$99.6\% agreement).
38	We propose $C_0$ (multi-candidate rate) as a zero-cost diagnostic: $C_0{<}5\%$ predicts method degeneracy, while high $C_0$ is necessary but insufficient for gains.
39	These findings provide practitioners with a principled early-stopping criterion before investing in symbolic aggregation overhead.
40	\end{abstract}
41	
42	% ============================================================
43	% 1. INTRODUCTION
44	% ============================================================
45	\section{Introduction}
46	\label{sec:intro}
47	
48	Self-Consistency (SC) \citep{wang2023selfconsistency} improves LLM reasoning by sampling multiple reasoning traces and selecting the majority answer.
49	A natural extension is to extract richer structure from these traces: formal constraints, logical invariants, or symbolic representations that a solver can aggregate more intelligently than simple voting \citep{pan2023logiclm,olausson2023linc}.
50	Several recent systems pursue this direction, using FOL translation, constraint satisfaction, or symbolic verification to rerank or select answers \citep{pan2023logiclm,olausson2023linc,dylos2026,aristotle2025,fover2025}.
51	The appeal is clear: if reasoning traces contain more information than just the final answer, a solver that exploits that information should outperform voting.
52	
53	But when does this actually work?
54	Prior systems report gains on specific benchmarks, yet use trained verifiers, external oracles, or multi-paradigm solver selection.
55	A fundamental question remains open: can the \emph{same} LLM that generates reasoning traces also extract constraints of sufficient quality to improve its own voting?
56	We call this the \emph{self-extraction} setting, where a single model both reasons and formalizes.
57	
58	We instantiate self-extraction as \sica{} (Symbolic Invariant Consensus Aggregation): sample $K$ reasoning traces, extract FOL constraints from each via the same LLM, and solve a weighted MAX-SAT instance to select the best answer.
59	We evaluate \sica{} across three reasoning domains (FOLIO, StrategyQA, ARC-Challenge, with GSM8K and ProofWriter as supplementary) and five model families (Qwen-14B, LLaMA-8B, Mistral-7B, DeepSeek-R1-Distill-7B, QwQ-32B), spanning instruction-tuned, distilled-reasoning, and full-reasoning architectures.
60	
61	Our central finding is negative: \sica{} provides no significant improvement over SC in any tested condition.
62	We identify the structural cause as a \emph{capability trap}:
63	\begin{itemize}
64	    \item \sica{} requires output diversity (multiple candidate answers) to differ from voting. We quantify this via $C_0$, the fraction of problems with more than one candidate answer across $K$ traces.
65	    \item When $C_0$ is low ($<$5\%, as with full reasoning models), \sica{} structurally degenerates to SC because there is only one candidate.
66	    \item When $C_0$ is high (38--62\%, as with instruction-tuned models), self-extracted constraints achieve precision $\approx 0.50$ at discriminating correct from incorrect answers, making MAX-SAT equivalent to counting.
67	    \item No tested condition achieves both sufficient diversity AND discriminative constraints simultaneously.
68	\end{itemize}
69	
70	Our contributions are:
71	\begin{enumerate}
72	    \item \textbf{Systematic negative result}: We show that self-extracted FOL constraint aggregation via MAX-SAT provides no significant accuracy gain over majority voting across 3 domains, 5 model families, and 18 experimental conditions (combined $N{>}1{,}300$).
73	    \item \textbf{Capability trap characterization}: We identify and quantify the structural failure mode: self-extracted constraints achieve chance-level discriminative precision ($\bar{p}=0.50$, $n=307$ multi-candidate problems), causing MAX-SAT to degenerate to counting (confirmed by three-way ablation: MAX-SAT $\equiv$ count-only $\equiv$ random-weight, $>$99.6\% agreement).
74	    \item \textbf{$C_0$ deployment diagnostic}: We propose the multi-candidate rate $C_0$ as a zero-cost early-stopping criterion. $C_0{<}5\%$ reliably predicts degeneracy; high $C_0$ is necessary but insufficient for gains (Pearson $r=0.05$, $p=0.84$ across 18 conditions).
75	\end{enumerate}
76	
77	% ============================================================
78	% 2. RELATED WORK
79	% ============================================================
80	\section{Related Work}
81	\label{sec:related}
82	
83	\paragraph{Self-Consistency and extensions.}
84	SC \citep{wang2023selfconsistency} established majority voting over sampled reasoning traces as a strong baseline for LLM reasoning.
85	Universal SC (USC) \citep{chen2023usc} extends this to free-form answers.
86	\citet{loo2025sc} demonstrate that SC scaling plateaus with increased samples, motivating richer aggregation.
87	Confidence-weighted SC \citep{taubenfeld2025weighted} assigns trace-level weights but remains within the voting paradigm.
88	DiVeRSe \citep{li2023diverse} combines diverse prompting with verification.
89	
90	\paragraph{Neuro-symbolic reasoning.}
91	Logic-LM \citep{pan2023logiclm} and LINC \citep{olausson2023linc} translate natural language to FOL for symbolic solving, documenting that LLM-to-FOL translation is error-prone.
92	Recent systems achieve gains using trained verifiers or multi-paradigm approaches: DyLoS \citep{dylos2026} uses dynamic logic-solver selection, Aristotle \citep{aristotle2025} employs logic-complete decomposition, and FoVer \citep{fover2025} trains a dedicated verifier.
93	Our work differs by studying the specific failure mode of \emph{same-model self-extraction} pipelines rather than these richer architectures.
94	
95	\paragraph{Verification and reranking.}
96	Outcome Reward Models (ORM) \citep{cobbe2021gsm8k} and Process Reward Models (PRM) \citep{lightman2023prm} use trained verifiers to rerank solutions.
97	Math-Shepherd \citep{wang2024mathshepherd} extends process supervision.
98	These approaches train separate verifiers, sidestepping the self-extraction bottleneck we characterize.
99	
100	\paragraph{Test-time compute scaling.}
101	\citet{snell2025scaling} analyze optimal test-time compute allocation.
102	DeepSeek-R1 \citep{deepseekr1} and OpenAI o1 \citep{openai2024o1} demonstrate that extended reasoning chains can substitute for external verification.
103	Our finding that full reasoning models (QwQ-32B) produce near-zero diversity ($C_0{<}5\%$) is consistent with this paradigm: models that ``think longer'' converge to consistent answers, eliminating the operating regime for symbolic aggregation.
104	
105	\paragraph{Constraint satisfaction in NLP.}
106	SATBench \citep{satbench2025} evaluates LLM performance on satisfiability problems.
107	Recent work explores constraint propagation with LLMs \citep{llmcp2025}.
108	Our MAX-SAT formulation draws on this line but applies it to answer aggregation rather than direct problem solving.
109	
110	% ============================================================
111	% 3. METHOD
112	% ============================================================
113	\section{Method: SICA}
114	\label{sec:method}
115	
116	\sica{} (Symbolic Invariant Consensus Aggregation) aggregates LLM reasoning traces via symbolic constraint satisfaction.
117	The pipeline has four stages.
118	
119	\paragraph{Stage 1: Trace generation.}
120	Given a problem $q$, sample $K$ reasoning traces $\{t_1, \ldots, t_K\}$ from an LLM with temperature $\tau > 0$.
121	Extract the final answer $a_i$ from each trace $t_i$.
122	Let $\mathcal{A} = \{a_1, \ldots, a_m\}$ be the set of distinct candidate answers.
123	
124	\paragraph{Stage 2: Constraint extraction.}
125	For each trace $t_i$, prompt the same LLM to extract a set of FOL constraints $\mathcal{C}_i = \{c_{i,1}, \ldots, c_{i,n_i}\}$ that formalize key reasoning steps.
126	Each constraint $c_{i,j}$ is a FOL formula intended to capture an invariant of the reasoning process.
127	
128	\paragraph{Stage 3: Constraint evaluation.}
129	For each candidate answer $a \in \mathcal{A}$ and each constraint $c_{i,j}$, evaluate whether $a$ satisfies $c_{i,j}$.
130	Define $\text{sat}(a, c_{i,j}) \in \{0, 1\}$.
131	This produces a satisfaction matrix of size $|\mathcal{A}| \times |\mathcal{C}|$ where $\mathcal{C} = \bigcup_i \mathcal{C}_i$.
132	
133	\paragraph{Stage 4: MAX-SAT aggregation.}
134	Formulate a weighted MAX-SAT instance where each constraint-answer pair contributes a weighted clause.
135	The answer maximizing total satisfied constraint weight is selected:
136	\begin{equation}
137	    a^* = \arg\max_{a \in \mathcal{A}} \sum_{c \in \mathcal{C}} w_c \cdot \text{sat}(a, c)
138	\end{equation}
139	where $w_c$ is the weight assigned to constraint $c$ (default: uniform).
140	In case of ties, \sica{} selects the answer supported by the trace with the highest individual constraint satisfaction count.
141	
142	\paragraph{Baseline: Self-Consistency (SC).}
143	SC selects $a^* = \arg\max_{a \in \mathcal{A}} |\{i : a_i = a\}|$, using only final answers.
144	
145	\paragraph{$C_0$ diagnostic.}
146	We define $C_0$ as the fraction of problems where $|\mathcal{A}| > 1$ (i.e., traces produce more than one distinct answer).
147	When $C_0 = 0$, all traces agree and \sica{} trivially equals SC.
148	$C_0$ is computable from Stage 1 alone, before any constraint extraction, making it a zero-cost diagnostic.
149	
150	% ============================================================
151	% 4. EXPERIMENTS
152	% ============================================================
153	\section{Experiments}
154	\label{sec:experiments}
155	
156	\subsection{Setup}
157	\label{sec:setup}
158	
159	\paragraph{Domains.}
160	We evaluate on three primary domains: \textbf{FOLIO} (formal deductive logic, 204 problems), \textbf{StrategyQA} (commonsense reasoning, 200 problems for powered tests), and \textbf{ARC-Challenge} (science reasoning, 60 problems).
161	Supplementary domains include \textbf{GSM8K} (arithmetic, 200 problems) and \textbf{ProofWriter} (included in QwQ-32B evaluation).
162	
163	\paragraph{Models.}
164	We test five model families:
165	(1) \textbf{Qwen2.5-14B-Instruct} as the primary model ($n=804$ powered evaluation across domains);
166	(2) \textbf{LLaMA-3.1-8B-Instruct} on StrategyQA ($n=200$) and FOLIO ($n=204$);
167	(3) \textbf{DeepSeek-R1-Distill-Qwen-7B} ($n=60$);
168	(4) \textbf{QwQ-32B} as a full reasoning model ($n=46$);
169	(5) Within-family scaling with \textbf{Qwen2.5-7B} and \textbf{Qwen2.5-72B-AWQ}.
170	
171	All experiments use $K=12$ sampled traces unless otherwise noted.
172	
173	\paragraph{Metrics.}
174	We report accuracy for both \sica{} and SC, their difference $\Delta$ (in percentage points), McNemar's test $p$-value for significance, and 95\% bootstrap confidence intervals for powered tests.
175	We also report $C_0$ (multi-candidate rate), constraint extraction rate, and constraint precision (fraction of constraints that correctly distinguish the gold answer from incorrect candidates).
176	
177	% ============================================================
178	% 4.2 MAIN RESULTS
179	% ============================================================
180	\subsection{Main Results}
181	\label{sec:main_results}
182	
183	Table~\ref{tab:main} summarizes results across all model-domain combinations.
184	Across every tested condition, \sica{} provides no statistically significant improvement over SC.
185	
186	\begin{table*}[t]
187	\centering
188	\caption{Main results: \sica{} vs.\ SC across models and domains. $\Delta$ = \sica{} $-$ SC in percentage points. $C_0$ = multi-candidate rate. All $p$-values from McNemar's test. No condition achieves significance at $\alpha=0.05$.}
189	\label{tab:main}
190	\small
191	\begin{tabular}{llrrrrrl}
192	\toprule
193	\textbf{Model} & \textbf{Domain} & \textbf{$n$} & \textbf{\sica{} Acc} & \textbf{SC Acc} & \textbf{$\Delta$pp} & \textbf{$C_0$\%} & \textbf{$p$} \\
194	\midrule
195	Qwen2.5-14B & FOLIO+SQA+ARC & 804 & 76.5 & 76.2 & +0.25 & 38 & -- \\
196	Qwen2.5-14B & StrategyQA & 60 & 56.7 & 53.3 & +3.33 & 10 & 0.50 \\
197	Qwen2.5-14B & ARC-Challenge & 60 & 95.0 & 96.7 & $-$1.67 & 5 & 1.00 \\
198	Qwen2.5-14B & GSM8K & 30 & 86.7 & 86.7 & 0.0 & 13 & -- \\
199	Qwen2.5-14B & GSM8K (expanded) & 200 & 89.0 & 89.0 & 0.0 & 12 & 1.00 \\
200	\midrule
201	LLaMA-3.1-8B & StrategyQA & 200 & -- & -- & +2.0 & 62 & 0.424 \\
202	LLaMA-3.1-8B & FOLIO & 204 & -- & -- & $-$2.45 & 62 & 0.267 \\
203	\midrule
204	DeepSeek-R1-7B & D012 (pilot) & 60 & 68.3 & 71.7 & $-$3.33 & 58 & 0.48 \\
205	\midrule
206	Qwen2.5-7B & D012 (pilot) & 60 & 58.3 & 58.3 & 0.0 & 70 & 1.00 \\
207	Qwen2.5-72B-AWQ & D012 (pilot) & 60 & 80.0 & 80.0 & 0.0 & 22 & 1.00 \\
208	\midrule
209	QwQ-32B & All domains & 46 & -- & -- & 0.0 & 2.6 & -- \\
210	\bottomrule
211	\end{tabular}
212	\end{table*}
213	
214	Three patterns emerge from Table~\ref{tab:main}:
215	
216	\textbf{Instruction-scale models show high diversity but zero gain.}
217	Qwen-14B on its primary evaluation ($n=804$) achieves $C_0=38\%$, meaning over a third of problems produce multiple candidate answers.
218	Yet $\Delta=+0.25$pp, well within noise.
219	LLaMA-8B shows the highest diversity ($C_0=62\%$) with powered tests ($n\geq200$) yielding $\Delta=+2.0$pp on StrategyQA (CI: [$-1.5$, $+5.5$]) and $\Delta=-2.45$pp on FOLIO (CI: [$-5.88$, $+0.98$]), both non-significant and in opposite directions.
220	The meta-analytic $\Delta$ across LLaMA-8B conditions is $+0.3$pp.
221	
222	\textbf{Full reasoning models produce near-zero diversity.}
223	QwQ-32B achieves an effective $C_0$ of 2.6\% across all domains (AIME, ProofWriter, FOLIO), with $\Delta=0.0$pp in every domain.
224	Extended reasoning chains produce consistent answers, structurally eliminating the operating regime for \sica{}.
225	
226	\textbf{Within-family scaling confirms the trap from both ends.}
227	In the Qwen family, scaling from 7B ($C_0=70\%$, $\Delta=0.0$) through 14B ($C_0=38\%$, $\Delta=+0.25$pp) to 72B ($C_0=22\%$, $\Delta=0.0$) traces a capability-diversity tradeoff: weaker models produce more diversity but worse constraints, while stronger models produce better constraints but less diversity.
228	Neither end benefits from \sica{}.
229	
230	% ============================================================
231	% 4.3 CONSTRAINT ABLATION
232	% ============================================================
233	\subsection{Constraint Ablation: MAX-SAT Adds Nothing Beyond Counting}
234	\label{sec:ablation}
235	
236	If constraints carry discriminative information, the MAX-SAT solver should outperform simpler aggregation.
237	We test this by comparing three aggregation strategies on the Qwen-14B $n=804$ evaluation (Table~\ref{tab:ablation}).
238	
239	\begin{table}[t]
240	\centering
241	\caption{Constraint ablation ($n=804$, Qwen-14B). Three aggregation methods produce statistically identical results, confirming that MAX-SAT adds nothing when constraints lack discriminative power.}
242	\label{tab:ablation}
243	\small
244	\begin{tabular}{lrr}
245	\toprule
246	\textbf{Aggregation} & \textbf{Accuracy} & \textbf{Agreement w/ MAX-SAT} \\
247	\midrule
248	MAX-SAT (full \sica{}) & 76.49 & -- \\
249	Count-only & 76.49 & 803/804 \\
250	Random-weight & 76.37 & 801/804 \\
251	SC (majority vote) & 76.24 & -- \\
252	\bottomrule
253	\end{tabular}
254	\end{table}
255	
256	MAX-SAT and count-only agree on 803 of 804 problems (McNemar $p=1.0$).
257	Random-weight agrees on 801/804 (McNemar $p=0.82$).
258	The three-way equivalence is the mechanistic signature of the capability trap: when constraint precision $\approx 0.50$, each answer's satisfied constraint count is approximately proportional to its vote count.
259	The MAX-SAT solver, despite its computational machinery, reduces to counting, which reduces to voting.
260	
261	% ============================================================
262	% 4.4 PER-PROBLEM CONSTRAINT ANALYSIS
263	% ============================================================
264	\subsection{Per-Problem Constraint Analysis}
265	\label{sec:constraint_analysis}
266	
267	To understand \emph{why} constraints fail to discriminate, we analyze constraint precision at per-problem granularity across $n=307$ multi-candidate problems from the Qwen-14B evaluation.
268	
269	\paragraph{Constraint precision is indistinguishable from random.}
270	Mean constraint precision is $0.50$ ($\sigma=0.12$), with 89\% of problems falling in the $[0.4, 0.6]$ range.
271	There is zero correlation between problem-level diversity and constraint quality (Pearson $r=0.03$, $p=0.58$).
272	Even among the 34 problems with precision $> 0.6$, \sica{} wins only 56\% of the time (barely above chance).
273	
274	\paragraph{Constraints between positive and negative flips.}
275	Problems where \sica{} flips from incorrect to correct (positive flips) have mean constraint precision $0.52$; problems where \sica{} flips from correct to incorrect (negative flips) have precision $0.48$.
276	The difference is negligible, confirming that constraints do not systematically identify correct answers.
277	
278	\paragraph{Qualitative analysis.}
279	We examine 8 representative problems in detail.
280	Of extracted constraints, 75\% are semantically meaningful FOL formulas, and 52\% correctly evaluate against their source answer.
281	However, only 12\% are \emph{discriminative}, producing different satisfaction values for different candidate answers.
282	The typical failure mode is tautological constraints: a formula like $\forall x (P(x) \rightarrow Q(x))$ may be logically valid but evaluates to TRUE for all candidates (e.g., both ``Proved'' and ``Unknown'' in a deduction task).
283	The extraction process produces logically correct but epistemically vacuous constraints.
284	
285	% ============================================================
286	% 4.5 C0 DIAGNOSTIC
287	% ============================================================
288	\subsection{$C_0$ as a Deployment Diagnostic}
289	\label{sec:c0}
290	
291	We validate $C_0$ as a predictor of \sica{} effectiveness across all 18 experimental conditions, spanning $C_0$ from 2.6\% (QwQ-32B) to 70\% (Qwen-7B).
292	
293	\paragraph{$C_0$ is necessary but not sufficient.}
294	All conditions with $C_0 < 5\%$ show $\Delta = 0.0$pp exactly, confirming that low diversity makes \sica{} structurally degenerate.
295	However, among conditions with $C_0 > 20\%$, the mean $|\Delta|$ is only 0.1pp with max $|\Delta| = 2.5$pp.
296	The correlation between $C_0$ and $\Delta$ across all 18 conditions is $r = 0.05$ ($p = 0.84$), confirming that diversity provides no gradient of improvement.
297	
298	\paragraph{Practical interpretation.}
299	$C_0$ functions as a gate, not a dial.
300	Below 5\%, practitioners can skip symbolic aggregation entirely with confidence.
301	Above 5\%, $C_0$ provides no guidance on whether gains will materialize, because the binding constraint shifts to extraction quality, which $C_0$ does not measure.
302	Crucially, $C_0$ is computable from trace generation alone (Stage 1), before any constraint extraction, making it a zero-cost early-stopping criterion.
303	
304	% ============================================================
305	% 4.6 TIEBREAK AND K-ABLATION
306	% ============================================================
307	\subsection{Tiebreak Analysis and K Ablation}
308	\label{sec:tiebreak}
309	
310	\paragraph{Tiebreak is locally effective but globally irrelevant.}
311	On the 5 problems (out of 804) where SC produces an exact tie between candidates, \sica{}'s constraint-based tiebreak achieves 80\% accuracy vs.\ 50\% for random tiebreak and 58\% for alphabetical tiebreak.
312	However, ties occur in only 0.6\% of problems, contributing $<0.3$pp to overall accuracy, which is statistically negligible.
313	
314	\paragraph{K ablation.}
315	We test $K \in \{6, 8, 11, 12, 16, 20\}$ on Qwen-14B ($n=60$).
316	\sica{} $\leq$ SC at all values of $K$, including odd $K=11$ where exact ties are structurally impossible.
317	The $K=11$ result ($\Delta = 0.0$pp) directly rules out the hypothesis that \sica{}'s value lies solely in tiebreaking.
318	Larger $K$ marginally degrades \sica{} (e.g., $K=20$: $\Delta = -1.7$pp), consistent with noise accumulation from additional non-discriminative constraints.
319	
320	% ============================================================
321	% 4.7 ADDITIONAL BASELINES
322	% ============================================================
323	\subsection{Additional Baselines}
324	\label{sec:baselines}
325	
326	\paragraph{Weighted SC.}
327	We compare four weighting schemes on the $n=804$ Qwen-14B data (Table~\ref{tab:weighted_sc}).
328	No scheme achieves significant improvement over uniform SC.
329	Inverse-length weighting shows the largest (but non-significant) edge at $+0.5$pp ($p=0.453$).
330	This eliminates the concern that simpler weighting could succeed where MAX-SAT fails: the bottleneck is signal quality, not aggregation sophistication.
331	
332	\begin{table}[t]
333	\centering
334	\caption{Weighted SC variants ($n=804$, Qwen-14B). No weighting achieves significant improvement.}
335	\label{tab:weighted_sc}
336	\small
337	\begin{tabular}{lrr}
338	\toprule
339	\textbf{Weighting} & \textbf{Accuracy (\%)} & \textbf{$\Delta$ vs.\ SC (pp)} \\
340	\midrule
341	Uniform (SC) & 76.24 & -- \\
342	Inverse-length & 76.74 & +0.50 \\
343	Trace-length & 75.25 & $-$0.99 \\
344	Constraint-count & 75.25 & $-$0.99 \\
345	\bottomrule
346	\end{tabular}
347	\end{table}
348	
349	\paragraph{Logic-LM $\times$ K baseline.}
350	On FOLIO ($n=204$), applying Logic-LM-style single-trace FOL verification $K$ times and voting produces accuracy identical to both SC (79.4\%) and \sica{} (79.4\%).
351	Whether using MAX-SAT (\sica{}), majority vote (SC), or single-trace verification (Logic-LM $\times K$), same-model extraction produces equivalent results.
352	The bottleneck is extraction quality, not aggregation mechanism.
353	
354	% ============================================================
355	% 4.8 OVERHEAD
356	% ============================================================
357	\subsection{Overhead Analysis}
358	\label{sec:overhead}
359	
360	\sica{} nearly doubles inference cost for negligible accuracy gain (Table~\ref{tab:overhead}).
361	
362	\begin{table}[t]
363	\centering
364	\caption{Wall-time breakdown per problem ($n=804$, Qwen-14B). \sica{} adds $\sim$49\% overhead, dominated by LLM-based constraint extraction.}
365	\label{tab:overhead}
366	\small
367	\begin{tabular}{lrr}
368	\toprule
369	\textbf{Stage} & \textbf{Mean time (s)} & \textbf{Fraction (\%)} \\
370	\midrule
371	Trace generation & 31.6 & 51.3 \\
372	Constraint extraction & 29.0 & 47.0 \\
373	MAX-SAT solving & 0.003 & $<$0.01 \\
374	\midrule
375	Total & 61.6 & 100.0 \\
376	\bottomrule
377	\end{tabular}
378	\end{table}
379	
380	The overhead is dominated by LLM calls for constraint extraction (47\% of total time), while MAX-SAT solving itself is negligible ($<$0.01\%).
381	The cost multiplier is $1.95\times$ compared to SC alone.
382	Combined with zero effectiveness, this definitively answers the practitioner question: \sica{} is not worth the overhead in any tested condition.
383	
384	% ============================================================
385	% 5. DISCUSSION
386	% ============================================================
387	\section{Discussion}
388	\label{sec:discussion}
389	
390	\paragraph{Anatomy of the capability trap.}
391	The capability trap has a precise mechanistic explanation.
392	Self-extracted constraints are logically correct in 75\% of cases and correctly evaluate against their source answer 52\% of the time.
393	However, only 12\% of constraints are \emph{discriminative}: they produce different satisfaction outcomes for different candidate answers.
394	The remaining 88\% are tautological or overly general, evaluating identically across all candidates.
395	When most constraints are non-discriminative, the MAX-SAT objective $\sum_c w_c \cdot \text{sat}(a, c)$ becomes proportional to the number of supporting traces, reducing the solver to a weighted vote.
396	The three-way equivalence of MAX-SAT, count-only, and random-weight aggregation (Section~\ref{sec:ablation}) is the direct consequence: constraint weights carry no information when the constraints themselves do not discriminate.
397	
398	\paragraph{Why does self-extraction fail?}
399	The extraction process asks the LLM to formalize its own reasoning steps as FOL constraints.
400	The resulting formulas tend to capture general reasoning patterns (e.g., modus ponens applications, domain axioms) that are valid regardless of the specific answer.
401	This is structurally different from constraints designed to test specific answer candidates, which would require the model to reason \emph{about} its own uncertainty, a metacognitive capability that current LLMs lack in the self-extraction setting.
402	
403	\paragraph{Within-family scaling.}
404	The Qwen scaling results (7B: $C_0=70\%$, 14B: $C_0=38\%$, 72B: $C_0=22\%$) reveal that capability and diversity trade off within a model family.
405	Weaker models produce more diverse (and thus more frequently disagreeing) outputs but extract worse constraints (precision 0.49 for 7B vs.\ 0.51 for 72B).
406	Stronger models extract marginally better constraints but produce insufficient diversity to exercise them.
407	This tradeoff is structural: it arises from the same capability that determines both answer consistency and constraint quality.
408	
409	\paragraph{Relationship to published systems.}
410	Systems like DyLoS, Aristotle, FoVer, and LogicAgent achieve gains on benchmarks overlapping with ours.
411	The key distinction is architectural: these systems employ trained verifiers, external oracles, logic-complete decomposition, or multi-paradigm solver selection.
412	Our finding characterizes the specific failure mode of \emph{same-model self-extraction} pipelines, not symbolic reasoning broadly.
413	The capability trap may be breakable by decoupling the extraction and reasoning models, as these systems implicitly do.
414	
415	\paragraph{Reasoning models bypass the need entirely.}
416	QwQ-32B, as a full reasoning model, achieves $C_0=2.6\%$, making \sica{} structurally degenerate.
417	This is consistent with the test-time compute scaling paradigm \citep{snell2025scaling,deepseekr1}: models that invest compute in extended chains achieve consistency through deliberation rather than aggregation.
418	For reasoning models, the question of symbolic aggregation is moot.
419	
420	\paragraph{Practical recommendations.}
421	Practitioners considering symbolic aggregation over self-extracted constraints should:
422	(1) Compute $C_0$ from a small pilot ($n \geq 30$, $K=12$). If $C_0 < 5\%$, the method will degenerate to SC.
423	(2) Even if $C_0 > 20\%$, do not expect gains without evidence that the extraction model produces discriminative constraints (precision $\gg 0.50$).
424	(3) Consider the $\sim$2$\times$ overhead: SC achieves the same accuracy at half the cost.
425	
426	% ============================================================
427	% 6. CONCLUSION
428	% ============================================================
429	\section{Conclusion}
430	\label{sec:conclusion}
431	
432	We presented a systematic evaluation of symbolic constraint aggregation via self-extracted FOL constraints (SICA) across 3 reasoning domains, 5 model families, and 18 experimental conditions.
433	Our central finding is a \emph{capability trap}: self-extracted constraints achieve chance-level discriminative precision, causing MAX-SAT to degenerate to counting and providing no improvement over simple majority voting.
434	We validated this through constraint ablation (MAX-SAT $\equiv$ count-only $\equiv$ random-weight), per-problem precision analysis ($n=307$, mean precision $= 0.50$), and cross-condition C0 analysis ($r = 0.05$ between diversity and gain).
435	The multi-candidate rate $C_0$ provides a zero-cost diagnostic for practitioners: it reliably predicts when symbolic aggregation cannot help, potentially saving significant inference overhead ($\sim$2$\times$ cost).
436	
437	\paragraph{Limitations.}
438	Our study is scoped to same-model self-extraction pipelines. Systems using trained verifiers, external oracles, or cross-model extraction may not share this limitation.
439	We test one MAX-SAT formulation; alternative symbolic aggregation strategies (e.g., SAT, SMT, answer set programming) could yield different results.
440	GSM8K and ARC-Challenge evaluations use smaller samples ($n \leq 200$); powered replications on these domains would strengthen conclusions.
441	
442	% ============================================================
443	% REFERENCES
444	% ============================================================
445	\bibliographystyle{plainnat}
446	
447	\begin{thebibliography}{30}
448	
449	\bibitem[Wang et~al.(2023)]{wang2023selfconsistency}
450	Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., and Zhou, D.
451	\newblock Self-Consistency Improves Chain of Thought Reasoning in Language Models.
452	\newblock In \emph{ICLR}, 2023.
453	
454	\bibitem[Chen et~al.(2023)]{chen2023usc}
455	Chen, X., Aksitov, R., Alon, U., Ren, J., Xiao, K., Yin, P., Prakash, S., Sutton, C., Wang, X., and Zhou, D.
456	\newblock Universal Self-Consistency for Large Language Model Generation.
457	\newblock \emph{arXiv preprint arXiv:2311.17311}, 2023.
458	
459	\bibitem[Pan et~al.(2023)]{pan2023logiclm}
460	Pan, L., Albalak, A., Wang, X., and Wang, W.Y.
461	\newblock Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning.
462	\newblock In \emph{Findings of EMNLP}, 2023.
463	
464	\bibitem[Olausson et~al.(2023)]{olausson2023linc}
465	Olausson, T.X., Gu, A., Lipkin, B., Zhang, C.E., Solar-Lezama, A., Tenenbaum, J.B., and Levy, R.
466	\newblock LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers.
467	\newblock In \emph{EMNLP}, 2023.
468	
469	\bibitem[Loo et~al.(2025)]{loo2025sc}
470	Loo, N., Hasanbeig, H., and Kamgarpour, M.
471	\newblock On the Scaling of Self-Consistency.
472	\newblock \emph{arXiv preprint}, 2025.
473	
474	\bibitem[Taubenfeld et~al.(2025)]{taubenfeld2025weighted}
475	Taubenfeld, A., Shayegani, E., and Goldstein, T.
476	\newblock Confidence-Weighted Self-Consistency.
477	\newblock In \emph{ACL Findings}, 2025.
478	
479	\bibitem[Li et~al.(2023)]{li2023diverse}
480	Li, Y., Lin, Z., Zhang, S., Fu, Q., Chen, B., Lou, J.-G., and Chen, W.
481	\newblock Making Language Models Better Reasoners with Step-Aware Verifier.
482	\newblock In \emph{ACL}, 2023.
483	
484	\bibitem[DyLoS(2026)]{dylos2026}
485	DyLoS: Dynamic Logic-Solver Selection for Neuro-Symbolic Reasoning.
486	\newblock In \emph{EACL}, 2026.
487	
488	\bibitem[Aristotle(2025)]{aristotle2025}
489	Aristotle: Logic-Complete Decomposition for Symbolic Reasoning.
490	\newblock In \emph{ACL}, 2025.
491	
492	\bibitem[FoVer(2025)]{fover2025}
493	FoVer: Formal Verification with Trained Verifiers for Logical Reasoning.
494	\newblock In \emph{TACL}, 2025.
495	
496	\bibitem[Cobbe et~al.(2021)]{cobbe2021gsm8k}
497	Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano, R., Hesse, C., and Schulman, J.
498	\newblock Training Verifiers to Solve Math Word Problems.
499	\newblock \emph{arXiv preprint arXiv:2110.14168}, 2021.
500	
501	\bibitem[Lightman et~al.(2023)]{lightman2023prm}
502	Lightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J., Schulman, J., Sutskever, I., and Alignment, K.
503	\newblock Let's Verify Step by Step.
504	\newblock In \emph{ICLR}, 2024.
505	
506	\bibitem[Wang et~al.(2024)]{wang2024mathshepherd}
507	Wang, P., Li, L., Shao, Z., Xu, R., Dai, D., Li, Y., Chen, D., Wu, Y., and Sui, Z.
508	\newblock Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations.
509	\newblock In \emph{ACL}, 2024.
510	
511	\bibitem[Snell et~al.(2025)]{snell2025scaling}
512	Snell, C., Lee, J., Xu, K., and Kumar, A.
513	\newblock Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters.
514	\newblock In \emph{ICLR (Oral)}, 2025.
515	
516	\bibitem[DeepSeek-AI(2025)]{deepseekr1}
517	DeepSeek-AI.
518	\newblock DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.
519	\newblock \emph{Nature}, 2025.
520	
521	\bibitem[OpenAI(2024)]{openai2024o1}
522	OpenAI.
523	\newblock Learning to Reason with LLMs.
524	\newblock OpenAI Blog, 2024.
525	
526	\bibitem[SATBench(2025)]{satbench2025}
527	SATBench: Benchmarking LLMs on Satisfiability Problems.
528	\newblock In \emph{EMNLP}, 2025.
529	
530	\bibitem[LLM-CP(2025)]{llmcp2025}
531	LLM Meets Constraint Propagation.
532	\newblock In \emph{IJCAI}, 2025.
533	
534	\bibitem[Liang et~al.(2023)]{liang2023debate}
535	Liang, T., He, Z., Jiao, W., Wang, X., Wang, Y., Wang, R., Yang, Y., Tu, Z., and Shi, S.
536	\newblock Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate.
537	\newblock \emph{arXiv preprint arXiv:2305.19118}, 2023.
538	
539	\bibitem[Du et~al.(2023)]{du2023debate}
540	Du, Y., Li, S., Torralba, A., Tenenbaum, J.B., and Mordatch, I.
541	\newblock Improving Factuality and Reasoning in Language Models through Multiagent Debate.
542	\newblock In \emph{ICML}, 2024.
543	
544	\bibitem[QwQ-Team(2024)]{qwq2024}
545	QwQ Team.
546	\newblock QwQ: Reflect Deeply on the Boundaries of the Unknown.
547	\newblock Qwen Blog, 2024.
548	
549	\bibitem[Han et~al.(2022)]{han2022folio}
550	Han, S., Schoelkopf, H., Zhao, Y., Qi, Z., Riddell, M., Benson, L., Sun, L., Zubova, E., Qiao, Y., Burtell, M., Peng, D., Fan, J., Zhuo, T.Y., Jia, Y., and Radev, D.
551	\newblock FOLIO: Natural Language Reasoning with First-Order Logic.
552	\newblock \emph{arXiv preprint arXiv:2209.00840}, 2022.
553	
554	\bibitem[Geva et~al.(2021)]{geva2021strategyqa}
555	Geva, M., Khashabi, D., Segal, E., Khot, T., Roth, D., and Berant, J.
556	\newblock Did Aristotle Use a Laptop? A Question Answering Benchmark with Implicit Reasoning Strategies.
557	\newblock In \emph{TACL}, 2021.
558	
559	\bibitem[Clark et~al.(2018)]{clark2018arc}
560	Clark, P., Cowhey, I., Etzioni, O., Khot, T., Sabharwal, A., Schoenick, C., and Tafjord, O.
561	\newblock Think You Have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge.
562	\newblock \emph{arXiv preprint arXiv:1803.05457}, 2018.
563	
564	\bibitem[Cobbe et~al.(2021b)]{cobbe2021gsm8k2}
565	Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano, R., Hesse, C., and Schulman, J.
566	\newblock Training Verifiers to Solve Math Word Problems.
567	\newblock \emph{arXiv preprint arXiv:2110.14168}, 2021.
568	
569	\bibitem[Tafjord et~al.(2021)]{tafjord2021proofwriter}
570	Tafjord, O., Dalvi, B., and Clark, P.
571	\newblock ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language.
572	\newblock In \emph{Findings of ACL}, 2021.
573	
574	\bibitem[Wei et~al.(2022)]{wei2022cot}
575	Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., Le, Q., and Zhou, D.
576	\newblock Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.
577	\newblock In \emph{NeurIPS}, 2022.
578	
579	\bibitem[Qwen-Team(2024)]{qwen2024}
580	Qwen Team.
581	\newblock Qwen2.5: A Party of Foundation Models.
582	\newblock Technical Report, 2024.
583	
584	\bibitem[Touvron et~al.(2023)]{touvron2023llama}
585	Touvron, H., Martin, L., Stone, K., et~al.
586	\newblock Llama 2: Open Foundation and Fine-Tuned Chat Models.
587	\newblock \emph{arXiv preprint arXiv:2307.09288}, 2023.
588	
589	\bibitem[DeepSeek-AI(2024)]{deepseek2024}
590	DeepSeek-AI.
591	\newblock DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model.
592	\newblock \emph{arXiv preprint arXiv:2405.04434}, 2024.
593	
594	\end{thebibliography}
595	
596	% ============================================================
597	% APPENDIX
598	% ============================================================
599	\appendix
600	\section{K Ablation Details}
601	\label{app:k_ablation}
602	
603	Table~\ref{tab:k_ablation} shows \sica{} vs.\ SC across $K$ values on Qwen-14B ($n=60$, D012 subset).
604	
605	\begin{table}[h]
606	\centering
607	\caption{K ablation (Qwen-14B, $n=60$). \sica{} $\leq$ SC at all K values.}
608	\label{tab:k_ablation}
609	\small
610	\begin{tabular}{rrrr}
611	\toprule
612	\textbf{K} & \textbf{\sica{} Acc (\%)} & \textbf{SC Acc (\%)} & \textbf{$\Delta$pp} \\
613	\midrule
614	6 & 73.3 & 73.3 & 0.0 \\
615	8 & 73.3 & 73.3 & 0.0 \\
616	11 & 73.3 & 73.3 & 0.0 \\
617	12 & 73.3 & 75.0 & $-$1.7 \\
618	16 & 71.7 & 73.3 & $-$1.7 \\
619	20 & 70.0 & 71.7 & $-$1.7 \\
620	\bottomrule
621	\end{tabular}
622	\end{table}
623	
624	\section{Tiebreak Baseline Details}
625	\label{app:tiebreak}
626	
627	On the $n=804$ Qwen-14B evaluation, only 5 problems (0.6\%) produce exact SC ties.
628	Table~\ref{tab:tiebreak} compares tiebreak strategies on these tied problems.
629	
630	\begin{table}[h]
631	\centering
632	\caption{Tiebreak accuracy on 5 tied problems (Qwen-14B, $n=804$).}
633	\label{tab:tiebreak}
634	\small
635	\begin{tabular}{lr}
636	\toprule
637	\textbf{Tiebreak Strategy} & \textbf{Accuracy (\%)} \\
638	\midrule
639	\sica{} (constraint-based) & 80.0 \\
640	Alphabetical & 58.0 \\
641	Random & 50.0 \\
642	First-seen & 42.0 \\
643	\bottomrule
644	\end{tabular}
645	\end{table}
646	
647	\sica{}'s constraint-based tiebreak is locally effective but contributes $<0.3$pp to overall accuracy due to the rarity of ties.
648	
649	\section{Overhead Breakdown}
650	\label{app:overhead}
651	
652	The $\sim$2$\times$ cost multiplier ($1.95\times$) of \sica{} over SC is dominated by constraint extraction LLM calls (47.0\% of total wall time).
653	MAX-SAT solving accounts for $<$0.01\% of computation.
654	This cost structure means that any optimization of \sica{}'s overhead must target the extraction step, not the solver.
655	
656	\section{Within-Family Scaling}
657	\label{app:scaling}
658	
659	\begin{table}[h]
660	\centering
661	\caption{Within-family scaling (Qwen, $n=60$, $K=12$). $C_0$ and constraint quality trade off, maintaining zero net gain.}
662	\label{tab:scaling}
663	\small
664	\begin{tabular}{lrrrrrr}
665	\toprule
666	\textbf{Model} & \textbf{SC (\%)} & \textbf{\sica{} (\%)} & \textbf{$\Delta$pp} & \textbf{$C_0$ (\%)} & \textbf{Extr.} & \textbf{Prec.} \\
667	\midrule
668	Qwen-7B & 58.3 & 58.3 & 0.0 & 70 & 0.78 & 0.49 \\
669	Qwen-14B & 73.3 & 73.3 & 0.0 & 38 & -- & -- \\
670	Qwen-72B & 80.0 & 80.0 & 0.0 & 22 & 0.94 & 0.51 \\
671	\bottomrule
672	\end{tabular}
673	\end{table}
674	
675	The scaling data reveals a structural tradeoff: weaker models produce higher diversity ($C_0$) but lower constraint quality (extraction rate and precision), while stronger models improve constraint quality at the expense of diversity.
676	At no point along this spectrum does \sica{} outperform SC.
677	
678	\section{Logic-LM Comparison}
679	\label{app:logiclm}
680	
681	On FOLIO ($n=204$), Logic-LM-style single-trace FOL verification applied $K=12$ times with majority voting achieves 79.4\% accuracy, identical to both SC (79.4\%) and \sica{} (79.4\%).
682	Logic-LM single-trace accuracy is 78.9\%.
683	The equivalence across all three aggregation paradigms confirms that same-model extraction quality is the binding bottleneck.
684	
685	\section{QwQ-32B Details}
686	\label{app:qwq}
687	
688	QwQ-32B produces near-deterministic outputs across all domains: effective $C_0 = 2.6\%$ (only 1 out of 46 problems produces multiple candidates).
689	Per-domain results: AIME $\Delta=0.0$pp, ProofWriter $\Delta=0.0$pp, FOLIO $\Delta=0.0$pp.
690	\sica{} structurally degenerates to SC for full reasoning models.
691	
692	\section{DeepSeek-R1-Distill-7B Details}
693	\label{app:deepseek}
694	
695	Despite being distilled from a reasoning model, DeepSeek-R1-Distill-Qwen-7B ($n=60$) behaves as an instruction-scale model: $C_0=58.3\%$, comparable to other 7--8B instruction models.
696	The 7B capacity is insufficient to maintain deterministic reasoning chains.
697	$\Delta=-3.33$pp (n.s., McNemar $p=0.48$, 0 \sica{} wins vs.\ 2 SC wins among discordant pairs).
698	72 traces were truncated due to context length, potentially contributing to the negative direction.
699	
700	\end{document}
701	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad443eda-e247-48f8-be81-1cbe3c1e62ea",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "9d05d5f0-0030-4fc6-8e0e-01a0fcde1787",
  "sourceToolAssistantUUID": "ad443eda-e247-48f8-be81-1cbe3c1e62ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-17T17:30:36.599Z_

Now I have a thorough understanding of the full paper, its claims, experimental design, related work coverage, and framing. Let me also check the oracle experiment data and the paper framing decisions more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d05d5f0-0030-4fc6-8e0e-01a0fcde1787",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8YB7Fwia9WQ19rsE6iA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68298fa2-5928-4f12-804c-58509da81bbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019msWD3pWHkT7nidW14TXnj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14799,
      "cache_read_input_tokens": 48223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14799,
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

_source line 43 · 2026-05-17T17:30:37.524Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VCQuahvTvUAkt6viyTJ8jq`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68298fa2-5928-4f12-804c-58509da81bbb",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8YB7Fwia9WQ19rsE6iA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e07e21b4-5492-48fe-9b66-8263fb01fc8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019msWD3pWHkT7nidW14TXnj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14799,
      "cache_read_input_tokens": 48223,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14799
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 48223,
          "cache_creation_input_tokens": 14799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14799,
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

_source line 44 · 2026-05-17T17:30:37.552Z_

<details><summary>↩ Tool result · `toolu_01VCQuahvTvUAkt6viyTJ8jq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/decisions.yaml\", \"content\": \"_next_id: 39\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 08:47 UTC\\n  summary: MVP 验证方案：50 题 MATH-500 分层子集，SICA vs SC@K=12\\n  rationale: SICA 核心价值取决于两个前提：(1) 能从推理 trace 可靠提取符号约束；(2) 跨路径矛盾率足够高（>5%）使形式化验证有意义。Reviewer\\n    给 impact 3/5，核心担忧是\\\"若矛盾率<5%则动机不成立\\\"。MVP 直接验证这两个前提，50 题按难度分层可同时观察 Extraction-Verification\\n    Paradox（难题提取差但矛盾多）。Pass 则进入全量实验冲 EMNLP/AAAI，Fail 则及时止损。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 08:52 UTC\\n  summary: 拒绝 CRD pivot，要求回归 SICA 原始方案\\n  rationale: Reviewer critical 审查发现 Agent 实施的是\\\"跨表征分歧诊断\\\"(CRD)，与 IDEA_BRIEF 定义的 SICA\\n    完全不同：CRD 用双表征（FOL+SymPy）做单解分歧检测，无多路径采样、无 MAX-SAT 共识——这正是 SICA 区别于 VERGE/D&P 的核心创新点。CRD\\n    的 novelty 定位与 VERGE 高度重叠（单输出验证+修复），无法支撑 EMNLP 投稿。同时 MVP 标准被静默替换，ROADMAP 的三条 pass\\n    criteria 从未测试。98GB GPU 完全能跑 QwQ-32B，无理由换 Qwen3-32B-AWQ。必须回归 SICA：K=12 多路径采样 →\\n    符号约束提取 → Z3 加权 partial MAX-SAT → 不变量共识打分。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 08:54 UTC\\n  summary: MVP 标准 v2：三档判定 + 矛盾绝对数 ≥5 + accuracy ≥SC+2pp + ProofWriter sanity check\\n  rationale: Reviewer warning 指出：(1) 5% 矛盾率阈值在 50 题上仅 2.5 题，置信区间极宽——改为绝对数 ≥5 题；(2)\\n    ≥SC+0.1pp 也过关无意义——改为 ≥2pp 或 p<0.1；(3) 灰色区间无处理——新增 Inconclusive 档，触发扩展到 100 题重测；(4)\\n    单域 MATH-500 不够——加 10 题 ProofWriter 做逻辑域 sanity check；(5) 模型不能模糊——固定 QwQ-32B，不可替换。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP T=0.7 继续跑完（需要完整数据），diagnostic 自然结束后 GPU 带宽恢复；AIME 30 题排在 MVP 之后\\n  rationale: Temperature 诊断 4/5 题显示 T=0.7/0.9/1.0 均几乎不产生答案分歧——C2/C3 高风险 FAIL。但仍决定让\\n    MVP 跑完：(1) 50 题完整数据无论正负都有价值（负面结果=SICA 在强模型上无信号，本身是发现）；(2) GPU 已分配且无其他实验排队；(3)\\n    smoke test L5 有 3 条矛盾，50 题中 L4-5 有 20 题可能产生更多信号。MVP 完成后立即跑 AIME 30 题（QwQ-32B ~79.5%，分歧应更明显），作为\\\"高难度\\n    sweet spot\\\"的补充验证。如果 MATH+AIME 均 SICA≈SC → 准备 FAIL 路径决策。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-15 12:16 UTC\\n  summary: 'D005: 采用双管齐下方案——MATH-500 MVP 继续 + AIME 30 题紧跟，暂不换模型'\\n  rationale: Temperature 诊断确认 QwQ-32B 在 T=0.7/0.9/1.0 下均产生近零答案分歧——reasoning model\\n    的确定性推理压制采样随机性。MATH-500 MVP 高概率 FAIL on C2/C3，但数据仍有价值（负面结果本身有意义）。AIME 2024 是 QwQ-32B\\n    弱项（~79.5%），更可能产生 trace 分歧——如果 SICA 在 AIME 上有信号，paper story 改为\\\"SICA 在高难度/高不确定性场景下最有价值\\\"，反而比\\\"通用提升\\\"更有深度。模型切换（Qwen2.5-7B\\n    等）改变论文定位太大，留作 AIME 也失败后的最后手段。执行顺序：MATH MVP 跑完 → AIME 30 题 → 基于两组结果做 PASS/FAIL\\n    最终判定。\\n  related_experiments: []\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-15 12:19 UTC\\n  summary: 'D006: Kill 当前 MATH MVP（有 bug + 25-30h 不可接受），修 bug 后 AIME 30 题优先'\\n  rationale: D005 假设 MVP 4-7h 出结果，但实际第一题 20min+ 未完成（serial trace gen + extraction\\n    回归 5/12 JSON parse fail），外推 25-30h。加上多样性诊断已定论（零分歧），继续烧 25-30h GPU 等一个几乎确定 FAIL\\n    的结果不合理。改为：(1) Kill 当前 MVP；(2) 修两个 bug——trace gen 用 n=K batch 而非串行、extraction 回归（ProofWriter\\n    prompt 合并后可能破坏了 math 域的 JSON parse）；(3) AIME 30 题优先跑（QwQ-32B 弱项，最可能出现分歧，30 题修复后\\n    ~3-4h）；(4) AIME 有信号 → 回来跑修复后的 MATH MVP；AIME 也无信号 → FAIL。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-15 16:31 UTC\\n  summary: 'D007: z3 parser 是 0pp 差距根因——并行修 parser + scorer，v3 继续跑后批量重打分'\\n  rationale: '7/30 题 Reviewer 分析发现 parse_z3_formula() 损失率 41-100%（P7: 72→1, 98.6%），LLM\\n    提取的约束在 z3 转换时被大量丢弃，MAX-SAT 无法工作。P7（SC 1/12 极度分散）是 SICA 理论最佳场景但因 parser 失效无法发挥。策略：v3\\n    继续跑收集全部 traces（最贵部分），并行修 parser + scorer，30 题完成后批量重打分作为真正 MVP 结果。'\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: 数据来源\\n    result: running, 7/30 done, 0pp差距但因parser bug无效\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-15 17:40 UTC\\n  summary: 'D008: P5 翻转为虚假声明（硬编码），A+C 实际翻转数=0。答案提取率过低是 C3 根本瓶颈，提升为最高优先级'\\n  rationale: '调查发现 P5 \\\"120→80 flip\\\" 是 rescore_pure.py 硬编码的对照值，v3 P5 实际仅 1 个候选答案 \\\"80\\\"。P7\\n    的 72→1 也是 parser 仍无法处理（2.8% parse rate），非 dedup 逻辑 bug。11/30 中 SICA=SC 的根因是答案提取率极低（P5:\\n    1/12, P2/P8/P9/P11: 0/12），多候选竞争场景不存在，任何 scorer 都无法差异化。将答案提取改进提升为最高优先级。'\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: 数据来源\\n    result: 11/30 done, SICA=SC=63.6%, 0pp\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-15 17:53 UTC\\n  summary: 'D009: max_tokens=10240 截断是 0-vote 根因，修为 16384 + fallback extraction +\\n    save intermediates，v3 完成后 v4 重跑截断题'\\n  rationale: P8/P9/P11 的 0/12 答案提取全因 trace 在 10240 tokens 截断，\\\\boxed{} 未生成。P11 有 60\\n    raw constraints（11/12 提取成功）证明模型推理充分但 token 不够。trace 耗时与截断强相关：350-435s→12/12 votes,\\n    730-810s→0-1/12 votes。修复 max_tokens + fallback extraction 预计恢复 P8/P9/P11 答案，创造多候选场景让\\n    SICA 有差异化空间。v3 继续跑（非截断题有效），v4 只重跑截断题，合并为最终 MVP。\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: 数据来源\\n    result: 12/30 done, P8/P9/P11 confirmed truncated at 10240 tokens\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-15 19:11 UTC\\n  summary: 'D010: AIME 0pp gap 是结构性的——QwQ-32B 单候选主导，SICA≡SC。MATH-50 升为关键判定实验'\\n  rationale: Reviewer 审查 22/30 题发现：所有非空 SC vote 分布仅含 1 个候选答案（unanimous among voting\\n    traces）。SICA 只能在多候选竞争时产生差异，单候选场景下无论约束打分如何都选同一答案。这不是 parser/scorer bug，是 QwQ-32B\\n    在 AIME 上答案高度一致的结构性特征（temp_diversity 实验已佐证）。v4 修复 max_tokens+fallback 可能恢复截断题的答案，但如果恢复的仍是同一答案则\\n    0pp 不变。MATH-500 Level 1-5 混合难度可能存在更多答案多样性（模型错误率 ~9.4%，错题上不同 trace 可能给出不同错答案），是验证\\n    SICA 核心假设的关键实验。调整优先级：v3 完成 → vote diversity 分析 → v4 快速验证 → MATH-50（决定性实验）。\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: evidence\\n    result: 22/30 完成, SICA=SC=72.7%, 0pp gap, 0 题多候选\\n  depends_on:\\n  - D007\\n  - D009\\n- id: D011\\n  date: 2026-05-15 19:47 UTC\\n  summary: 'D011: Reviewer 预判 MATH-50 将重现单候选模式（已有 32 题零分歧证据），修订策略：MATH-10 快速诊断 → 逻辑域优先'\\n  rationale: Reviewer 指出 temp_diversity 实验是在 MATH L4-5 上做的（非 AIME），3 个温度 × 5 题 = 零答案分歧；加上\\n    smoke_5q（5 题 MATH）和 AIME 22 题，共 32 题零多候选。QwQ-32B 答案一致性是模型级特征（CoT 链逻辑约束远强于采样温度），非任务特定。全量\\n    MATH-50（7-8h GPU）几乎确定重现 0pp。修订策略：(1) v3 完成后做 vote diversity 分析；(2) 取消 v4 AIME\\n    re-run，改为 MATH-10 trace-only 诊断（v4 代码，~1h）验证修复 + 确认/否定单候选假设；(3) 如确认单候选 → 立即转向\\n    ProofWriter + FOLIO 作为主实验（逻辑域 FOL 规范化程度高、answer distribution 天然多候选、Z3 parser 损耗低）；(4)\\n    MATH/AIME 数据保留为 domain boundary 分析。\\n  related_experiments:\\n  - exp_id: sica_aime30_v3\\n    role: evidence\\n    result: 22/30 单候选\\n  - exp_id: sica_temp_diversity\\n    role: evidence\\n    result: MATH L4-5 三温度零分歧\\n  - exp_id: smoke_5q\\n    role: evidence\\n    result: 5题MATH单候选\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-15 22:24 UTC\\n  summary: 'D012: 逻辑域 MVP 判定标准——ProofWriter-30 + FOLIO-30 合并 60 题，沿用 D003 框架 + 新增多候选前置条件'\\n  rationale: 'D011 将主实验从 MATH-500 pivot 到逻辑域，但 D003 判定标准仍针对 MATH-500，ProofWriter 定位仅为\\\"sanity\\n    check 不影响 PASS/FAIL\\\"。Reviewer 指出 proofwriter30_v2 完成后无法判定。新标准沿用 D003 框架（保持一致性避免\\n    goalpost-moving），新增多候选前置条件（吸取 AIME/MATH 教训）：\\n\\n\\n    PASS（全部满足）：\\n\\n    - C1: 约束提取率 ≥ 50%\\n\\n    - C2: 跨路径矛盾检出 ≥ 5 题（绝对数）\\n\\n    - C3: SICA accuracy ≥ SC + 2pp（合并 60 题），或 paired bootstrap p < 0.1\\n\\n    - C0（前置）: 多候选率 ≥ 20%（≥12/60 题有 >1 个 unique candidate）\\n\\n\\n    INCONCLUSIVE（触发扩展重测）：\\n\\n    - C3 为 +0~2pp，其余满足\\n\\n\\n    FAIL（任一触发）：\\n\\n    - C0 < 20% 多候选 → 结构性失效，同 MATH/AIME\\n\\n    - C1 < 30%\\n\\n    - C2 < 3 题\\n\\n    - C3 < SC\\n\\n\\n    ProofWriter-30 和 FOLIO-30 合并判定（60 题），但分别报告以观察域差异。'\\n  related_experiments:\\n  - exp_id: sica_proofwriter30_v2\\n    role: target\\n    result: running\\n  - exp_id: sica_folio30\\n    role: target\\n    result: planned\\n  depends_on:\\n  - D003\\n  - D011\\n- id: D013\\n  date: 2026-05-16 01:30 UTC\\n  summary: 'D013: ProofWriter 中期 CRITICAL——MaxSAT 结构性失效(16/16 excluded=0)，终止当前实验，紧急诊断根因后再决定\\n    FOLIO'\\n  rationale: Reviewer 独立核实 16/30 题中期数据：C0/C1/C2/C3 四项全 FAIL。最关键的是 C2=0（矛盾检出为零），MaxSAT\\n    satisfied_ratio=1.000 贯穿全部问题，SICA 核心机制从未激活。C3=-6.25pp 说明 SICA 不仅无效还主动伤害准确率。继续跑剩余\\n    14 题无意义。需紧急诊断 MaxSAT 全满足的根因：(a) 约束太粗/抽象无法矛盾→设计缺陷 (b) SAT 编码 bug→可修 (c) 去重后约束太少→可调。根因决定\\n    FOLIO 是否值得跑以及 MVP 是否有救。May 19 checkpoint 仅剩 3 天。\\n  related_experiments:\\n  - exp_id: sica_proofwriter30_v2\\n    role: primary\\n    result: C2=0 structural failure, all 4 D012 criteria FAIL at midpoint\\n  depends_on:\\n  - D012\\n- id: D014\\n  date: 2026-05-16 01:39 UTC\\n  summary: 'D014: MaxSAT 结构性失效根因确认——约束编码缺 answer assertion + 提取失败率 54%。选 A 方案：L3+L1\\n    修复 → 5 题验证 → 全量'\\n  rationale: 诊断 6/6 注入测试通过证明 MaxSAT 求解器无 bug。satisfied_ratio=1.0 的根因是：(1) 不同答案的 trace\\n    未注入 answer assertion 约束，MaxSAT 无法产生冲突；(2) 提取失败率 54.4%（QwQ 重新推理而非输出 JSON）。L3 修复（注入\\n    answer==trace_answer）是 SICA 能否工作的架构前提，L1（prompt 强制 JSON）是质量保障。先 5 题验证再全量，避免浪费\\n    GPU。\\n  related_experiments:\\n  - exp_id: sica_proofwriter30_v2\\n    role: trigger\\n    result: MaxSAT 16/16 satisfied_ratio=1.0, SICA worse than SC by 6.2pp\\n  depends_on:\\n  - D013\\n- id: D015\\n  date: 2026-05-16 02:48 UTC\\n  summary: 'D015: FOLIO C0 预检 0% 多候选率——QwQ-32B 跨三域自一致性是模型级特征，SICA 核心前提（trace 分歧）不成立。等\\n    L3+L1 五题验证后做最终 MVP 判定。'\\n  rationale: FOLIO 10 题 K=6 traces 全部 unanimous（0% 多候选），与 AIME 0%、ProofWriter 18.8%\\n    汇总后，C0 合并判定确定性 FAIL（远低于 ≥20% 门槛）。QwQ-32B 在数学+逻辑+FOL 三个域均表现出极高 trace 一致性，SICA 的差异化空间不存在。5\\n    题 L3+L1 验证仍在跑，用于确认机制 soundness（与使用场景独立），完成后做最终 MVP 判定。\\n  related_experiments:\\n  - exp_id: sica_folio30\\n    role: C0 precheck\\n    result: 0/10 multi-candidate, all unanimous\\n  - exp_id: sica_proofwriter30_v2\\n    role: context\\n    result: 3/16 multi-candidate = 18.8%\\n  - exp_id: sica_temp_diversity\\n    role: context\\n    result: 0% diversity across 3 temperatures\\n  depends_on:\\n  - D012\\n  - D014\\n- id: D016\\n  date: 2026-05-16 02:51 UTC\\n  summary: 'D016: QwQ-32B MVP FAIL，模型 pivot 到 Qwen2.5-14B-Instruct——全域 C0=3.6% 远低于\\n    20% 阈值，模型级自一致性使 SICA≡SC，切换非 reasoning model 验证算法本身有效性'\\n  rationale: 全域证据（MATH 0%, AIME 0%, ProofWriter 18.75%, FOLIO 0%，合并 3/83=3.6%）确认 QwQ-32B\\n    自一致性是模型级特征而非域特征。SICA 算法需要多候选输入才能与 SC 产生差异。模型替换是唯一可测试\\\"算法本身是否有效\\\"的路径。选择 Qwen2.5-14B-Instruct：非\\n    reasoning model 采样多样性高、14B 在 98GB GPU 上轻松部署、Qwen2.5 系列逻辑能力强。预计 C0 预检 1h + 完整评估\\n    4h，May 19 checkpoint 可控。\\n  related_experiments:\\n  - exp_id: sica_folio30\\n    role: trigger\\n    result: FOLIO C0=0%\\n  - exp_id: sica_proofwriter30_v2\\n    role: evidence\\n    result: ProofWriter C0=18.75%\\n  - exp_id: sica_temp_diversity\\n    role: evidence\\n    result: 3 temps 0% diversity\\n  - exp_id: sica_aime30_v3\\n    role: evidence\\n    result: AIME 0pp gap\\n  depends_on:\\n  - D012\\n  - D015\\n- id: D017\\n  date: 2026-05-16 05:11 UTC\\n  summary: 'D017: D012 技术 PASS（C3 +3.3pp）但统计 INCONCLUSIVE（p=0.317）——全部增益来自 4 个 6:6\\n    tiebreak，SICA 机制是 principled tiebreaking 而非 constraint override。扩展实验到 200 题 +\\n    K 敏感性分析争取统计效力'\\n  rationale: 60 题中仅 4 题 SICA≠SC，全部为 6:6 精确平票。56 个非平票题 SICA=SC（约束从未推翻明确多数）。McNemar\\n    p=0.317，二项检验 p=0.3125，均不显著。FOLIO +6.7pp 但 ProofWriter 0pp，域泛化不成立。SICA 的实际贡献是 principled\\n    tiebreaking 而非原始假设的 symbolic constraint override。需要更多数据点来判断 tiebreaking 模式是否稳定可复现。扩展到全量\\n    PW+FOLIO + K=8/16/20 敏感性分析是最高效的统计加固路径。\\n  related_experiments:\\n  - exp_id: sica_d012_14b\\n    role: evidence\\n    result: C3 +3.3pp, p=0.317, 4 tiebreaks only\\n  depends_on:\\n  - D016\\n  - D012\\n- id: D018\\n  date: 2026-05-16 05:14 UTC\\n  summary: 'D017: D012 PASS, MVP 通过——SICA 在有多样性输入时确实≠SC（+3.3pp），核心假设验证。研究阶段首要任务：扩大样本量\\n    + tiebreak 基线分析 + K 消融'\\n  rationale: D012 四项标准全部技术达标：C0=53.3%, C1=100%, C2=34题, C3=+3.3pp。但 C3 实质弱点明确：全部增益来自\\n    4 个 6:6 平票（SICA 3/4 正确 vs SC 1/4），p=0.317 不显著，FOLIO +6.7pp / PW 0pp。MVP 标准以 OR\\n    条件通过（+3.3pp ≥ +2pp），核心假设\\\"SICA 在有多样性输入时≠SC\\\"已验证——机制是 principled tiebreaking via\\n    constraint weights。模型对照（QwQ-32B C0=3.6%, SICA≡SC）强化了\\\"多样性是 SICA 前提\\\"的结论。研究阶段需解决统计弱点：扩展到\\n    200+ 题、K sensitivity、random tiebreak baseline。\\n  related_experiments:\\n  - exp_id: sica_d012_14b\\n    role: primary\\n    result: SICA 73.3% vs SC 70.0%, +3.3pp, 4 tiebreaks, p=0.317\\n  depends_on:\\n  - D012\\n  - D016\\n- id: D019\\n  date: 2026-05-16 05:22 UTC\\n  summary: exp-007 (72B-AWQ) 从 P2 提升到 P1，Claim 2 至少需要 4 个模型\\n  rationale: Reviewer 指出 Claim 2 \\\"Operating Regime Characterization\\\" 仅有 QwQ-32B 和\\n    Qwen2.5-14B 两个模型，不足以支撑 \\\"model property, not task property\\\" 的论断。加上 exp-004 (7B)\\n    也只有 3 个模型。72B-AWQ 补齐后形成 7B/14B/72B instruction + 32B reasoning 的完整 scaling 证据链，4\\n    个模型是 \\\"operating regime\\\" claim 的最低门槛。GPU 时间预算 ~4h，串行排在 exp-002 和 exp-004 之后，总计\\n    ~22.5h，May 25 DDL 前充裕。\\n  related_experiments:\\n  - exp_id: exp-007\\n    role: promoted to P1\\n  - exp_id: exp-004\\n    role: P1 scaling point\\n  - exp_id: exp-005\\n    role: existing QwQ-32B data\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-16 05:29 UTC\\n  summary: 'D020: Kill 140题进程B，保留804题进程A以最大化统计力'\\n  rationale: Reviewer 发现两个进程同时请求 vLLM（违反独占规则）。进程A（PID 181491，804题 PW+FOLIO）预计~67个tie，统计力远优于进程B（140题，~12个tie）。13.4h\\n    ETA 在 May 19 checkpoint 前充裕。MVP 核心瓶颈是 p=0.317 统计不显著，最大化 N 是第一优先。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: target\\n    result: 保留804题运行，kill 140题重复进程\\n  depends_on: []\\n- id: D021\\n  date: 2026-05-16 06:16 UTC\\n  summary: 'D021: Scope 扩展——补 3 个非 Qwen 模型 + GSM8K 跨域 + constraint ablation，Claim\\n    2 reframe 为 C0=epistemic uncertainty'\\n  rationale: 用户指出 scope 不足，Reviewer 审计确认：(1) 全 Qwen 家族是 Claim 2 致命弱点 (critical)；(2)\\n    单域数据无法支撑 \\\"model property not task property\\\"；(3) 缺 constraint ablation 防御 \\\"over-engineering\\\"\\n    attack。补 Mistral-7B + LLaMA-8B + DeepSeek-R1-7B（跨 3 家族 + reasoning 第二点）+ GSM8K\\n    30题 pilot（跨域）+ CPU constraint ablation。总额外 GPU ~7h，May 25 ARR 前充裕。Claim 2 从 \\\"model\\n    architecture determines regime\\\" 升级为 \\\"C0 tracks epistemic uncertainty, correlates\\n    with but not identical to architecture\\\"。\\n  related_experiments:\\n  - exp_id: exp-010\\n    role: new\\n    result: planned\\n  - exp_id: exp-011\\n    role: new\\n    result: planned\\n  - exp_id: exp-012\\n    role: new\\n    result: planned\\n  - exp_id: exp-013\\n    role: new\\n    result: planned\\n  - exp_id: exp-014\\n    role: new\\n    result: planned\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D022\\n  date: 2026-05-16 08:18 UTC\\n  summary: 'D022: 不 kill exp-001；exp-013 ablation 改用 exp-002 数据（新 pipeline 含 raw_constraints）'\\n  rationale: pipeline.py 的 raw_constraints 修改在 exp-001 启动后（16:04 vs 13:19），运行中进程不热更新，导致\\n    exp-001 结果中 raw_constraints 全空。三个选项评估：(A) kill+resume 有风险且前 162 题仍缺数据；(B) 全量重跑浪费\\n    3h；(C) 近似模式说服力弱。选择 Option D：保持 exp-001 不动（SICA vs SC 主结果不受影响），exp-013 ablation\\n    改在 exp-002（K ablation, 60题×5K, 新 pipeline）数据上运行。exp-002 的 D012 子集 C0~53%，约 32\\n    题多候选 × 5K = 160 个多候选评估点，统计充足。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: 保持运行\\n    result: running\\n  - exp_id: exp-002\\n    role: ablation 数据源\\n    result: planned\\n  - exp_id: exp-013\\n    role: 策略变更\\n    result: planned\\n  depends_on:\\n  - D021\\n- id: D023\\n  date: 2026-05-16 08:27 UTC\\n  summary: 'D023: Contingency plan 确认——如 SICA≤SC 则 pivot 到 Analysis Paper (Option\\n    A)，FOLIO 正向则嵌入为子 claim (Option C)'\\n  rationale: exp-001 中间结果 (N=157 PW) SICA-SC gap 反转至 -1.27pp，tiebreak win 降至 50%。Reviewer\\n    评估三方案：A (Analysis Paper, Main 30-35% / Findings 60-70%)、B (Negative Result, Main\\n    15-25%)、C (Domain-Specific if FOLIO翻盘, Main 25-35%)。选 A 为主线：论文价值从\\\"SICA 提升准确率\\\"转向\\\"理解\\n    symbolic consensus 的 operating conditions\\\"。C0 threshold pattern 成为核心贡献。Option\\n    C 嵌入 A（如 FOLIO 正向则作为\\\"domain formality → effectiveness\\\"子 claim）。不选 B（天花板低、NLP 社区对负面结果接受度有限）。决策点：exp-001\\n    FOLIO 70 题的 C0 和 delta。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: 决策依赖\\n    result: running\\n  - exp_id: exp-010\\n    role: cross-family 关键数据\\n    result: planned\\n  - exp_id: exp-011\\n    role: cross-family 关键数据\\n    result: planned\\n  - exp_id: exp-014\\n    role: reasoning 泛化\\n    result: planned\\n  depends_on:\\n  - D021\\n  - D022\\n- id: D024\\n  date: 2026-05-16 18:33 UTC\\n  summary: 'D024: Dream-informed adjustments — reframe scope-to-claim gap, add odd-K/Logic-LM/Weighted-SC\\n    baselines, C0 regression methodology fix'\\n  rationale: 'Dream dream_20260516T054054 (full review mode) returned Weak Reject\\n    (3/6) across ALL three tiers (best/median/worst). Cross-tier consistent issues:\\n    (1) SICA framed as consensus but functionally a tiebreaker — scope-to-claim gap\\n    is #1 problem; (2) missing Logic-LM/LINC/weighted-SC baselines; (3) odd-K needed\\n    to validate mechanism beyond even-K ties; (4) C0 regression uses non-independent\\n    K-ablation points. Actions: added exp-002 K=11, new exp-015 Logic-LM baseline\\n    (CPU), new exp-016 Weighted SC baseline (CPU), expanded Anticipated Reviewer Concerns\\n    11-15, updated Story Spine related work. D021 cross-family/GSM8K/ablation already\\n    address other concerns. Re-dream required after exp-001 results + framing adjustments.'\\n  related_experiments:\\n  - exp_id: exp-002\\n    role: modified\\n    result: added K=11 odd-K test\\n  - exp_id: exp-015\\n    role: new\\n    result: Logic-LM baseline CPU-only\\n  - exp_id: exp-016\\n    role: new\\n    result: Weighted SC baseline CPU-only\\n  depends_on:\\n  - D021\\n  - D023\\n- id: D025\\n  date: 2026-05-16 18:35 UTC\\n  summary: 'D025: Activate D023 contingency — pivot to Analysis Paper. SICA +0.26pp\\n    at N=762 confirms no accuracy gain. Central contribution shifts to \\\"capability\\n    trap\\\" characterization + operating regime analysis across 4 domains × 7 models.'\\n  rationale: 'exp-001 at N=762/804 shows SICA=76.51% vs SC=76.25% (+0.26pp, well within\\n    noise at SE≈1.5pp). D012''s +3.3pp on N=60 was small-sample noise (SE≈6pp). Combined\\n    with Dream all-tiers Weak Reject and Reviewer''s scope evaluation: (1) Claim 1\\n    (accuracy gain) is dead — cannot claim SICA>SC; (2) Paper pivots to Analysis:\\n    \\\"When does symbolic consensus help? Empirical answer: rarely, and here''s the\\n    structural reason (capability trap)\\\"; (3) Central new insight: diversity (C0)\\n    and constraint quality are inversely correlated — symbolic methods need diversity\\n    (hard tasks) but constraint quality degrades on hard tasks; (4) Practical contribution:\\n    C0 as necessary-but-insufficient diagnostic + decision framework; (5) Scope expansion\\n    (StrategyQA + ARC) still proceeds — demonstrates capability trap across domains,\\n    not searching for positive results. exp-013 (constraint ablation) upgraded to\\n    P0 — must confirm MaxSAT mechanism is not vacuous.'\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: trigger\\n    result: SICA +0.26pp at N=762, no significant gain\\n  - exp_id: exp-013\\n    role: upgraded_P0\\n    result: Must confirm aggregation mechanism\\n  - exp_id: exp-010\\n    role: reframed\\n    result: Cross-family validation of negative result\\n  - exp_id: exp-011\\n    role: reframed\\n    result: Cross-family validation of negative result\\n  depends_on:\\n  - D023\\n  - D024\\n- id: D026\\n  date: 2026-05-16 19:21 UTC\\n  summary: exp-001 完成确认 D025 pivot：SICA≈SC (+0.25pp, n=804, n.s.)，FOLIO sub-claim\\n    dead (0.00pp)\\n  rationale: 804题全量评估确认：SICA vs SC gap仅+0.25pp（2题净差异），远低于显著性阈值。FOLIO 204题 gap=0.00pp，D012的+6.7pp确认为小样本噪声。数据坚实支持D025\\n    Analysis Paper pivot方向。FOLIO sub-claim正式放弃。\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: primary\\n    result: +0.25pp overall (n.s.), FOLIO 0.00pp\\n  depends_on:\\n  - D025\\n- id: D027\\n  date: 2026-05-16 20:29 UTC\\n  summary: exp-013 确认 MaxSAT≈count-only≈random-weight：SICA 的 aggregation mechanism\\n    无贡献 (C1 confirmed)\\n  rationale: 804题上三种 constraint aggregation 方法（MaxSAT/count-only/random-weight）802/804\\n    结果一致，McNemar p>0.7。MaxSAT 优化相对简单计数零优势，直接支持 Capability Trap 论文 C1：\\\"mechanism is\\n    vacuous when constraint quality is bounded by LLM capability\\\"。近似公式限制可接受（802/804\\n    agreement rate 压倒性）。\\n  related_experiments:\\n  - exp_id: exp-013\\n    role: primary\\n    result: MaxSAT=76.49%, count-only=76.62%, random=76.37%, SC=76.24%, all n.s.\\n  - exp_id: exp-001\\n    role: data source\\n    result: +0.25pp baseline\\n  depends_on:\\n  - D025\\n  - D026\\n- id: D028\\n  date: 2026-05-17 01:11 UTC\\n  summary: exp-002 中期：K=11 gap=0 确认 tiebreak-only；D012 vs K-ablation K=12 swing 8.33pp\\n    证明 n=60 结果为噪声\\n  rationale: K=11 (odd, no ties) SICA=SC 精确相等，证实 SICA 从不 override 清晰多数。更关键：同数据同设置\\n    K=12 两次实验结果相反（D012 +3.33pp vs K-ablation -5.00pp），8.33pp swing 直接证明小样本 gap 完全被\\n    trace 随机性淹没。FOLIO 上 SICA 恒定 76.67% 而 SC 随 K 提升——constraint quality 天花板限制了 SICA\\n    利用更多 traces 的能力。考虑升级 claim：从\\\"SICA≈SC\\\"到\\\"SICA≤SC at scale\\\"（更多 traces 帮 SC 但被 SICA\\n    constraint ceiling 限制）。\\n  related_experiments:\\n  - exp_id: exp-002\\n    role: primary\\n    result: K=11 gap=0, K=12 gap=-5pp, FOLIO SICA ceiling effect\\n  - exp_id: exp-001\\n    role: reference\\n    result: +0.25pp at K=12 n=804\\n  depends_on:\\n  - D025\\n  - D027\\n- id: D029\\n  date: 2026-05-17 02:14 UTC\\n  summary: exp-002 最终结果：SICA≤SC for all K (gap 0 to -5pp)，framing 维持\\\"SICA≈SC (mechanism\\n    vacuous)\\\"不升级为\\\"SICA&lt;SC\\\"\\n  rationale: K-ablation 6个K值全部 SICA≤SC，但 n=60 方差大（D012 vs K-ablation swing 8.33pp）。exp-001\\n    n=804 显示 +0.25pp (n.s.)。安全 framing 是\\\"gap indistinguishable from zero + mechanism\\n    introduces noise\\\"，而非\\\"SICA systematically worse\\\"。FOLIO 恒定 76.67% 是 constraint quality\\n    ceiling 的可视化证据。K=11 odd-K 确认 tiebreak-only。\\n  related_experiments:\\n  - exp_id: exp-002\\n    role: primary\\n    result: SICA≤SC all K; K=11 gap=0; FOLIO ceiling 76.67%\\n  - exp_id: exp-001\\n    role: anchor\\n    result: +0.25pp n=804 n.s.\\n  depends_on:\\n  - D028\\n- id: D030\\n  date: 2026-05-17 04:21 UTC\\n  summary: 'D030: 从 Analysis Paper 转向 Methods Paper — 利用诊断数据设计 Constraint Consistency\\n    Filtering 改进 SICA'\\n  rationale: '用户明确指示 methods paper 质量更高且更受欢迎。现有分析数据（exp-001/002/013/016）不浪费——变成论文动机和诊断部分。核心\\n    method idea: constraint consistency filtering（只保留跨多条 traces 重复出现的约束），利用已有 diversity\\n    提升 constraint quality 而不需更强模型。时间和资源充足（用户确认），pilot 可在当天 CPU-only 完成（如数据可用）。'\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: data source for pilot\\n    result: 804题 K=12 traces\\n  - exp_id: exp-013\\n    role: diagnosis\\n    result: MaxSAT≈count-only confirmed quality is bottleneck\\n  depends_on:\\n  - D025\\n  - D029\\n- id: D031\\n  date: 2026-05-17 08:06 UTC\\n  summary: 'D031: exp-011 +6.7pp 方向性正面但 p=0.22 不显著，启动 LLaMA-8B StrategyQA 200 题 powered\\n    test 验证 operating regime 假设'\\n  rationale: 'exp-011 LLaMA-8B 在 D012 60 题上 SICA +6.67pp (McNemar p=0.22, 6 discordant\\n    pairs 5:1)。n=60 检验力不足，无法排除噪声。但跨模型 pattern 清晰（弱→强: +6.7pp → +0.3pp → -1.7pp → 0pp），值得\\n    powered verification。StrategyQA 200 题 + LLaMA-8B 预期 multi-candidate rate 高（弱模型+commonsense\\n    推理），n=200 可检测 5pp 差异 (power>0.8)。若 p<0.05 → paper 升级为 Operating Regime Characterization；若\\n    p>0.1 → 维持 D025 Capability Trap analysis paper，LLaMA 作为 suggestive evidence。不在\\n    powered test 前更新 paper_framing.md。'\\n  related_experiments:\\n  - exp_id: exp-011-llama8b-v3\\n    role: 触发\\n    result: +6.67pp, p=0.22, directionally positive\\n  - exp_id: exp-010-mistral-v3\\n    role: 并行验证\\n    result: running, 9/60 done\\n  - exp_id: exp-001\\n    role: 对照\\n    result: Qwen-14B +0.25pp n.s.\\n  depends_on:\\n  - D030\\n  - D025\\n- id: D032\\n  date: 2026-05-17 08:20 UTC\\n  summary: 'D032: exp-010 Mistral 确认倒 U 型 pattern（sweet spot SC~55-65%），FOLIO 204\\n    升为最高优先级 powered test'\\n  rationale: Mistral-7B SICA≡SC (0.0pp, SC=48.3%, zero discordant)。与 LLaMA-8B (+6.7pp,\\n    SC=60%) 和 Qwen-14B (+0.25pp, SC=76%) 合看，pattern 是倒 U 型而非单调递减。Sweet spot 在 SC~55-65%：模型够弱产生多样性，但够强保证约束质量。LLaMA-8B\\n    在 FOLIO 上恰好在 sweet spot（SC=60%, +10pp at n=30），几乎必然在 n=200 时显著。StrategyQA 上 LLaMA-8B\\n    的 SC 未知，可能落在 sweet spot 外（类似 Mistral）。因此 FOLIO 204 是确定性更高的 powered test 选择。\\n  related_experiments:\\n  - exp_id: exp-010-mistral-v3\\n    role: 触发\\n    result: SICA=SC=48.3%, 0.0pp, zero discordant\\n  - exp_id: exp-011-llama8b-v3\\n    role: sweet spot 证据\\n    result: +6.67pp at SC=60%\\n  - exp_id: exp-001\\n    role: 对照\\n    result: +0.25pp at SC=76%\\n  depends_on:\\n  - D031\\n- id: D033\\n  date: 2026-05-17 09:12 UTC\\n  summary: 'D033: exp-019 StrategyQA +2pp n.s. 确认 inverted U — operating regime 取决于\\n    model×task accuracy band (SC~55-65%)，非模型强弱'\\n  rationale: 'LLaMA-8B StrategyQA: SC=72%, SICA +2.0pp (net 4题, p>0.1 几乎确定)。LLaMA-8B\\n    在 commonsense 上不弱(72%)，只在 logic 上弱(60%)。这证明 operating regime 是 model×task specific，不是\\n    model-level property。5 个数据点画出完整曲线：SC=48%(0pp) → 60%(+6.7pp) → 72%(+2pp) → 76%(+0.3pp)\\n    → 97%(-1.7pp)。Sweet spot 在 SC~55-65%。D031 的 p<0.05 门槛未达，但 exp-020 FOLIO 204 (LLaMA-8B\\n    × FOLIO, SC=60% in sweet spot, +10pp signal) 仍是 definitive test。'\\n  related_experiments:\\n  - exp_id: exp-019-llama8b-strategyqa-200\\n    role: 触发\\n    result: +2.0pp, SC=72%, p>0.1\\n  - exp_id: exp-011-llama8b-v3\\n    role: sweet spot 参照\\n    result: +6.67pp, SC=60%\\n  - exp_id: exp-010-mistral-v3\\n    role: 下界\\n    result: 0pp, SC=48%\\n  depends_on:\\n  - D032\\n  - D031\\n- id: D034\\n  date: 2026-05-17 10:04 UTC\\n  summary: 'D034: exp-020 同题对比证伪 operating regime 假设——exp-011 +10pp 不可复现（同题反转 -3.3pp），D025\\n    Capability Trap 为最终论文方向'\\n  rationale: 'exp-020 FOLIO 204 中间数据（n=78）: SICA -2.94pp（SC 领先）。同题 30 FOLIO 对比：exp-011\\n    +10pp → exp-020 -3.3pp，delta 完全反转。SICA agreement 仅 56.7%，说明 K=12 n=30 方差极大，exp-011\\n    +6.67pp 是随机波动非真实信号。结合 exp-019 StrategyQA +2pp (p=0.424)，SICA 在任何 model×task regime\\n    下都不优于 SC。D025 Capability Trap analysis paper 是唯一合理方向。下一步：等 exp-020 全 204 题完成做最终录入，然后进入论文写作。'\\n  related_experiments:\\n  - exp_id: exp-020-llama8b-folio-204\\n    role: definitive test\\n    result: n=78 intermediate -2.94pp; 同题30 FOLIO 反转 -3.3pp\\n  - exp_id: exp-011-llama8b-v3\\n    role: 被证伪\\n    result: +6.67pp 确认为 sampling noise\\n  - exp_id: exp-019-llama8b-strategyqa-200\\n    role: 佐证\\n    result: +2pp p=0.424\\n  depends_on:\\n  - D033\\n  - D032\\n  - D031\\n  - D025\\n- id: D035\\n  date: 2026-05-17 11:29 UTC\\n  summary: 'D035: exp-020 FOLIO 204 确认 SICA≤SC (-2.4pp)，Operating Regime 彻底死亡，D025\\n    Capability Trap 为最终论文方向，进入写作阶段'\\n  rationale: exp-020 LLaMA-8B FOLIO 全量 204 题：SICA 60.8% vs SC 63.2%，delta=-2.4pp，方向反转。exp-011\\n    的 +10pp 是 n=30 小样本噪声（SE≈9pp）。四个 powered test 无一支持 SICA 优势（exp-001 +0.25pp n.s.,\\n    exp-019 +2.0pp p=0.424, exp-020 -2.4pp, exp-010 0.0pp）。D031 全部条件触发\\\"维持 D025\\\"路径。不再需要更多\\n    powered tests，进入 CPU ablations + 论文写作。\\n  related_experiments:\\n  - exp_id: exp-020-llama8b-folio-204\\n    role: definitive_test\\n    result: 'negative: -2.4pp, SICA worse than SC'\\n  - exp_id: exp-019-llama8b-strategyqa-200\\n    role: powered_test\\n    result: 'negative: +2.0pp p=0.424'\\n  - exp_id: exp-011-llama8b-v3\\n    role: refuted\\n    result: +10pp was n=30 noise\\n  - exp_id: exp-001\\n    role: anchor\\n    result: +0.25pp n.s. on 804q\\n  depends_on:\\n  - D034\\n  - D031\\n  - D025\\n- id: D036\\n  date: 2026-05-17 11:51 UTC\\n  summary: 'D036: Manager 要求实验覆盖自查——补 temperature ablation (T=0.3/0.5/1.0) + GSM8K\\n    pilot + Qwen-7B scaling + Mistral StrategyQA，总计 ~10h GPU'\\n  rationale: 自查发现两个 Critical 缺口：(1) Temperature ablation 直接检验 capability trap 核心机制（diversity↑但\\n    quality↓→SICA 仍无效），审稿人必问，~3h GPU；(2) GSM8K 数学域缺失，LLM reasoning 最标准 benchmark，~1h\\n    GPU。Important 缺口：Qwen-7B 补 scaling curve（C0 gradient claim），Mistral 跨域（消除 model-specific\\n    质疑）。所有补充实验总计 ~10h GPU，1 天内可完成，不影响 ARR May 25 写作排期。\\n  related_experiments:\\n  - exp_id: temperature-ablation\\n    role: new_critical\\n    result: 'planned: T=0.3/0.5/1.0 on Qwen-14B D012'\\n  - exp_id: exp-012\\n    role: new_critical\\n    result: 'planned: GSM8K 30q pilot'\\n  - exp_id: exp-004\\n    role: new_important\\n    result: 'planned: Qwen-7B scaling'\\n  - exp_id: mistral-strategyqa\\n    role: new_important\\n    result: 'planned: Mistral-7B StrategyQA 60q'\\n  depends_on:\\n  - D035\\n- id: D037\\n  date: 2026-05-17 16:27 UTC\\n  summary: 'D037: Dream审稿分析 — 三档均3/6(Weak Reject), 结构性问题已修复framing'\\n  rationale: 'dream_20260517T144412 三档评分均为 3/6 Weak Reject（best=median=worst，评分平坦=纯结构性问题）。跨档一致的关键问题：(1)\\n    标题/claims过度泛化——只测了SICA但声称\\\"symbolic consensus\\\"整体不行，而DyLoS/Aristotle/FoVer在同benchmark上有正面结果；(2)\\n    self-extraction confound未解决——同模型生成+提取，无法区分\\\"聚合失败\\\"vs\\\"提取失败\\\"；(3) 仅8篇引用，需30+；(4) capability\\n    trap可能是Logic-LM/LINC已知局限的重新描述。\\n\\n\\n    已采取行动：(A1) 标题缩窄为self-extracted constraints范围；(A2) Claims加scope限定语；(A3) 添加oracle\\n    extraction实验(FOLIO gold FOL)到defensive experiments；(A4) 添加Required Citations清单(30+)；(A5)\\n    添加Claim Scoping Rules（n=60不能说confirm）；(A6) Core Insight加positioning说明（相对Logic-LM/LINC的增量）。\\n\\n\\n    观察项：domain coverage framing等真实温度实验+GSM8K结果再定；temperature ablation是否能称\\\"causal\\\"等T实验完成后评估。\\n\\n\\n    下一步：(1) 添加oracle extraction实验到experiment_plan；(2) 启动Paper Agent（带上述约束）；(3) re-dream验证修复效果。'\\n  related_experiments:\\n  - exp_id: exp-001\\n    role: primary_evidence\\n    result: delta=+0.3pp n.s.\\n  - exp_id: exp-013\\n    role: constraint_ablation\\n    result: MAX-SAT≈count-only 802/804\\n  - exp_id: exp-010\\n    role: cross-family\\n    result: delta=0.0pp\\n  depends_on:\\n  - D035\\n  - D036\\n- id: D038\\n  date: 2026-05-17 16:49 UTC\\n  summary: 'D038: Oracle exp-021 confirms extraction bottleneck — aggregation mechanism\\n    validated (+8.82pp with gold FOL)'\\n  rationale: 'exp-021 Oracle FOLIO (n=204, LLaMA-8B traces + FOLIO gold FOL + Z3):\\n    Oracle-SICA=88.24% vs SC=79.41% vs SICA-self=79.41%。Delta=+8.82pp, McNemar p=6.15e-05。\\n\\n\\n    关键结论：MAX-SAT 聚合机制本身有效（给定discriminative constraints可显著超越投票），瓶颈完全在 LLM 自提取约束缺乏判别力。这直接回答了\\n    Dream 审稿的核心 confound 质疑（W2/W3 across all tiers）。\\n\\n\\n    对论文影响：(1) Oracle result 升级为 main contribution（不再只是 defensive experiment）；(2) 论文narrative从\\\"symbolic\\n    consensus失败\\\"转为\\\"self-extraction是唯一瓶颈，聚合范式本身有效\\\"；(3) 为 Discussion 提供建设性方向（better\\n    extraction → +8.82pp potential）。已更新 paper_framing.md。'\\n  related_experiments:\\n  - exp_id: exp-021\\n    role: oracle_control\\n    result: +8.82pp p<0.001\\n  - exp_id: exp-001\\n    role: self_extraction_baseline\\n    result: delta=+0.3pp n.s.\\n  depends_on:\\n  - D037\\n\", \"total_chars\": 28578, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e07e21b4-5492-48fe-9b66-8263fb01fc8d",
  "isSidechain": true,
  "promptId": "7713ac7e-fee4-4a91-b43a-3599ee51bd6e",
  "agentId": "a6ad89e6d8763aafe",
  "type": "user",
  "uuid": "dd104868-0ebf-4414-848a-f19b8ecf12b3",
  "sourceToolAssistantUUID": "e07e21b4-5492-48fe-9b66-8263fb01fc8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-17T17:32:00.331Z_

I now have comprehensive understanding of the paper, its evolution, experimental results, related work coverage, framing decisions, and the complete dream report version. Let me produce the review.

---

### R2 Review: Novelty and Related Work

**Summary**: This paper evaluates SICA (Symbolic Invariant Consensus Aggregation), a pipeline that extracts FOL constraints from LLM reasoning traces and uses weighted MAX-SAT to select answers. The central finding is negative: SICA provides no gain over Self-Consistency across 5 model families and 3 domains (N>1,300). The authors attribute this to a "capability trap" where self-extracted constraints achieve chance-level discriminative precision (~0.50), causing MAX-SAT to degenerate to counting. An oracle experiment replacing self-extracted constraints with gold FOL (+8.82pp, p<0.001) localizes the bottleneck to extraction quality.

**Strengths**:

- S1: **The oracle control experiment is the paper's strongest and most novel contribution.** The causal separation of extraction quality from aggregation effectiveness (Oracle-SICA +8.82pp vs. self-extracted SICA +0.0pp on the same data) is a clean experimental design that provides genuine mechanistic insight. This goes well beyond "it doesn't work" and tells the community exactly *where* the failure lies. The choice to use FOLIO's gold FOL annotations with Z3 verification is well-motivated.

- S2: **The constraint ablation (Section 4.3/5.3) is compelling.** Showing that MAX-SAT, count-only, and random-weight aggregation agree on 802/804 predictions is an effective way to demonstrate that the satisfiability structure adds no information beyond vote counting. This is a clean diagnostic that other researchers can apply to their own symbolic aggregation systems.

- S3: **Systematic coverage across model families.** Testing 5 model families (Qwen-14B, LLaMA-8B, Mistral-7B, DeepSeek-R1-7B, QwQ-32B) spanning instruction-tuned, distilled-reasoning, and full-reasoning architectures addresses the obvious "maybe it only fails on this model" objection. The within-family scaling analysis (Qwen 7B/14B/72B) showing that C0 and constraint quality trade off is a useful empirical observation.

- S4: **Honest and well-scoped negative result.** The paper appropriately limits its claims to same-model self-extraction pipelines and explicitly acknowledges that DyLoS, Aristotle, FoVer, and LogicAgent achieve gains through different mechanisms. The scope limitation statement in Section 3.5 is well-written and prevents overclaiming.

**Weaknesses**:

- W1: **The "capability trap" concept is not as novel as presented.** The fundamental observation is that LLM-to-FOL translation is error-prone and constraints extracted by a model from its own reasoning are coupled to the source answer. Logic-LM (Pan et al. 2023) and LINC (Olausson et al. 2023) already documented that LLM FOL translation has ~40% error rates. The "self-correction fails without external feedback" finding from Huang et al. (ICLR 2024) establishes the broader pattern. The contribution is more in the *systematic quantification* (precision ~0.50, the ablation showing MAX-SAT=counting) than in the conceptual insight itself, but the paper frames the capability trap as a discovery rather than a systematic measurement of a known phenomenon.

- W2: **SICA itself is not an established method in the literature.** The paper proposes SICA, then systematically shows it doesn't work. Since SICA is the authors' own construction, the negative result is less impactful than if SICA were a widely-adopted method whose failure needed documenting. The paper would benefit from positioning SICA as "the most natural instantiation of the symbolic consensus idea" and discussing whether anyone has actually proposed this specific pipeline (or something close to it) in prior work. Currently, the reader may wonder: "Why should I care that a method nobody uses doesn't work?"

- W3: **The Related Work section is adequate but has gaps in positioning.** The paper covers the major areas (SC extensions, neuro-symbolic, verification, test-time compute, constraints), but the discussion of each cluster is thin. The neuro-symbolic paragraph does not clearly articulate what makes self-extraction structurally different from the trained-verifier paradigm. The paper says "Our work differs by studying the specific failure mode of same-model self-extraction pipelines rather than these richer architectures" but does not explain *why* this specific failure mode is interesting independent of the positive-result systems. Additionally, the debate/multi-agent literature (Liang et al. 2023, Du et al. 2023) appears only in the literature_map.yaml but receives minimal treatment in the actual related work. Multi-agent debate is a direct alternative for aggregating multiple reasoning paths and should be discussed.

- W4: **C0 as a "contribution" is overstated.** C0 (multi-candidate rate) is simply the fraction of questions with non-unanimous answers across K traces. This is a trivially computable statistic that any practitioner would naturally check before deploying a method that requires answer disagreement. Claiming it as a contribution ("deployment diagnostic") inflates a basic sanity check into a methodological advance. The correlation analysis (r=0.05 between C0 and delta) is informative but not surprising.

- W5: **The paper lacks engagement with the "why" of constraint non-discrimination at the right level.** The qualitative analysis (Section 4.4 in the dream report) mentions that only 12% of constraints are discriminative and 88% are tautological or overly general. This is the most important finding for understanding the capability trap, yet it receives shallow treatment. What types of problems produce discriminative constraints? Is there a relationship between problem structure (e.g., number of entities, depth of reasoning chain) and constraint quality? Without this analysis, the paper identifies the symptom (non-discriminative constraints) but does not diagnose the disease at sufficient depth.

- W6: **Missing the oracle experiment in the main paper sections.** The `docs/paper/experiments.tex` includes the oracle control, but the paper's Abstract and Introduction are still placeholders in the main LaTeX source. The dream report version includes the oracle result but does NOT list it as a formal contribution in the contribution list (only "systematic negative result," "capability trap characterization," and "C0 diagnostic"). The oracle result should be elevated to a top-line contribution since it is the paper's strongest differentiator from a simple "negative result" paper.

**Missing Related Work**:

- **Self-refinement / self-correction literature**: Huang et al. (2024) "Large Language Models Cannot Self-Correct Reasoning Yet" is referenced in the literature_map but absent from the dream report's bibliography. This is a critical omission because it establishes the exact same structural pattern: self-X fails without external signal. The paper should position itself explicitly relative to this work.

- **GSM-Symbolic (Mirzadeh et al. 2024)**: Another systematic negative result paper about LLM reasoning fragility. Provides precedent for the methodology of rigorous negative-result evaluation. Listed in literature_map but not cited in the paper.

- **V-STaR (Hosseini et al. 2024)**: Iterative verifier training that directly contrasts with self-extraction. Shows that verification quality scales with training data, making the case that self-extraction is fundamentally limited relative to trained approaches.

- **RASC (Wan et al. 2024) and ReASC (Kim et al. 2026)**: Reasoning-aware and reliability-aware SC variants that use richer information from traces without resorting to symbolic formalization. These are direct comparisons for the "what else can you do with trace information beyond voting" question.

- **Representation Consistency (2025)**: Aggregation via representation similarity as an alternative semantic aggregation approach. Relevant as a non-symbolic alternative to SICA.

- **Khan et al. (2024) "Debating with More Persuasive LLMs"**: Shows that debate quality depends on model capability, parallel to the capability trap finding.

- **"Base Models Know How to Reason" (2025)**: Relevant to the QwQ-32B diversity collapse finding, since it explains why RL-trained reasoning models converge to similar patterns.

- The reference list in the dream report has ~30 entries but several are incomplete (DyLoS, Aristotle, FoVer, SATBench, LLM-CP lack proper author/title information). These must be completed with full bibliographic details.

**Questions for Authors**:

- Q1: The oracle experiment uses LLaMA-8B traces with FOLIO gold FOL. Have you considered running the oracle with Qwen-14B traces (your primary model) to ensure the +8.82pp result is not model-specific? The LLaMA-8B baseline SC accuracy on FOLIO is 63.24% (from Table 1 in docs/paper) but the oracle reports SC=79.41%. This appears to use Qwen-14B traces with LLaMA-8B oracle. Please clarify the exact setup.

- Q2: The per-problem constraint precision of 0.50 is the key finding. Have you analyzed whether this is driven by (a) constraints that are universally tautological (evaluate TRUE for all candidates), (b) constraints that randomly support different answers, or (c) constraints that are correct for the source answer but also happen to be consistent with alternatives? The mechanism matters for understanding what a "better extractor" would need to do differently.

- Q3: You test one MAX-SAT formulation. Have you considered alternative symbolic aggregation strategies, such as using constraints to *filter* candidates rather than *score* them (e.g., eliminate any candidate that violates more than k constraints)? The degeneration to counting may be specific to the scoring formulation.

- Q4: The temperature ablation only uses Qwen2.5-14B on a 60-question subset. Given that this is supposed to demonstrate that diversity is not the bottleneck, why was this not run on a larger sample or across multiple models?

**Framing Suggestions**:

- The oracle experiment should be the lead contribution, not the third bullet. Reframe the narrative as: "We show that symbolic aggregation over FOL constraints CAN improve voting (+8.82pp with gold constraints), but CANNOT when constraints are self-extracted (0pp across 18 conditions). The gap between these two results precisely quantifies the extraction quality bottleneck." This is more compelling than leading with the negative result.

- The title scope is appropriate (post-D037 scoping to "self-extracted constraints"), but the framing should more explicitly connect to what practitioners might actually try. Currently SICA feels like a straw man that the authors built to knock down. Strengthening the motivation for why someone would attempt self-extraction (as opposed to trained verification) would make the negative result more valuable.

- Consider renaming "capability trap" to something more descriptive, such as "extraction-discrimination gap" or "self-extraction bottleneck." The current name implies a conceptual insight that is deeper than what the evidence supports. The finding is essentially: "self-extracted constraints are not discriminative." Calling this a "trap" suggests an unexpected or paradoxical outcome, but given the known error rates of LLM-to-FOL translation (Logic-LM, LINC), it is closer to an expected outcome that has now been rigorously quantified.

- The paper should explicitly discuss the cost-benefit analysis earlier. The overhead analysis (1.95x cost for 0pp gain) is buried late. Leading with "this method doubles your compute for zero benefit" is a strong practical message.

**Preliminary Score**: 4 (Borderline Reject)

Justification: The paper presents a systematic and well-executed empirical study with a clean oracle control experiment that provides genuine insight into the extraction-vs-aggregation decomposition. The constraint ablation is convincing. However, the novelty is limited: the core finding (LLM self-extracted FOL constraints are low quality) is a known phenomenon from Logic-LM and LINC, and the "capability trap" concept is closer to a systematic quantification of existing knowledge than a new insight. SICA is not an established method, reducing the impact of showing it fails. The C0 diagnostic is trivial. The paper would benefit from (a) elevating the oracle result to the central contribution, (b) deeper analysis of *why* constraints are non-discriminative at the problem level, and (c) a more honest positioning relative to prior work that already documented LLM-to-FOL translation failures. As an EMNLP Findings paper, this could be acceptable with revisions. For main conference, the novelty bar is not met in current form.

**Confidence**: 4 (confident, familiar with self-consistency, neuro-symbolic reasoning, and LLM reasoning aggregation literature)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd104868-0ebf-4414-848a-f19b8ecf12b3",
  "isSidechain": true,
  "agentId": "a6ad89e6d8763aafe",
  "requestId": "req_011Cb8YBTXbMpa7micfgJpNg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53b35627-2430-4b83-8f7c-617a36673b23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "23120887-6c71-42a4-97bc-58275f16ad92",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017FUgN8yTTpu15TZcTGmUrz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16592,
      "cache_read_input_tokens": 63022,
      "output_tokens": 3032,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16592
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3032,
          "cache_read_input_tokens": 63022,
          "cache_creation_input_tokens": 16592,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16592,
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
