# Research conversation: You are Reviewer 2 (R2) for an ICLR 2026 submission. Your focus is **Novelty and Related Work**. Provide a thorough, ind

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a927f2e80c12fa2d4.jsonl`
- **Structured JSON:** [`dd289ad73fed1eb2f9a3.json`](../../sessions/dd/dd289ad73fed1eb2f9a3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-22T03:32:08.179Z_

You are Reviewer 2 (R2) for an ICLR 2026 submission. Your focus is **Novelty and Related Work**. Provide a thorough, independent review.

## ICLR 2026 Rating Scale
Overall rating uses {0, 2, 4, 6, 8, 10}:
- 10: Outstanding (top 1-2%)
- 8: Strong Accept (clear accept, significant contribution)
- 6: Weak Accept (marginally above threshold)
- 4: Weak Reject (marginally below threshold)
- 2: Strong Reject (clear reject)
- 0: Very strong reject

Soundness, Presentation, Contribution each rated 1-4.
Confidence rated 1-5.

## Paper Summary
**Title:** "Architecture-Dependent Cross-Lingual Conflict Processing: Probing Knowledge Conflict Signals in Multilingual LLMs"

The paper investigates how multilingual LLMs internally encode knowledge conflict signals and whether these encodings transfer across languages. Using residual stream probing on three model architectures (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B) with English–Chinese parallel instances from ConflictQA, the paper finds:

1. **C1 (Detectability):** Conflict signals are robustly detectable via linear probes within each language across all three architectures (balanced accuracy 68–77%, all p < 0.001).
2. **C2 (Asymmetry is architecture-dependent):** ZH→EN transfer exceeds EN→ZH by ~7pp in Llama and Qwen, but collapses to +1.0pp in Gemma-2-9B.
3. **C3 (CKA layer analysis):** CKA between EN/ZH decreases monotonically across layers; probe peaks after language transition point.

## Full Paper Content (10 pages)

**Abstract:** When multilingual LLMs encounter knowledge conflicts, how is the conflict signal encoded internally, and does this encoding transfer across languages? They probe residual stream activations on 3 architectures using EN-ZH parallel ConflictQA instances. Findings: (1) conflict detectable within-language 68-77% balanced acc, cross-lingual 63-72%; (2) asymmetry ~7pp in Llama/Qwen collapses to +1.0pp in Gemma; (3) CKA decreases monotonically, probe peaks after language transition layer.

**Section 2 (Related Work):**

"Knowledge conflicts in LLMs." Covers Xie et al. [2024] ConflictQA, Chen et al. [2022], Longpre et al. [2021]. Claims to extend monolingual analyses to cross-lingual setting.

"Cross-lingual representations in multilingual LLMs." Covers Wendler et al. [2024] cross-architecture variation, Müller et al. [2021] linguistic similarity, Pires et al. [2019] and Wu & Dredze [2019] language-neutral hypothesis, Libovický et al. [2020] and Gonen et al. [2020] language-specific later layers. CKA analysis claimed as contribution.

"Probing and mechanistic interpretability." Covers Belinkov [2022], Hewitt & Manning [2019], Geiger et al. [2021], Elazar et al. [2021] causal probing, SAEs (Cunningham et al., Bricken et al.). Notes SAE application to cross-lingual limited.

"Cross-lingual conflict resolution." Covers Zhao et al. [2026] CLEAR finding on linguistic affinity. Claims to provide first representation-level analysis.

**Section 3 (Method):**
- Dataset: ConflictQA translated to Chinese via GPT-4, COMET quality assessed, verified instances (1096/272 Llama, 798/168 Qwen)
- Probing: Logistic regression + MLP (hidden 256), cross-lingual transfer (4 conditions)
- CKA: Linear kernel, language transition = CKA < 0.5
- Steering: Probe weight as steering vector (preliminary)

**Section 4 (Results):**
- Table 1: Within-language 68-77%, cross-lingual 63-72%. Asymmetry: Llama +7.2pp [1.1,13.6] Sig, Qwen +7.2pp [-1.2,13.4] No, Gemma +1.0pp [-4.5,6.8] No
- Table 2-3: COMET quality control and tercile ablation (reversed direction, not significant)
- Table 4: MLP gains +2.0 to +4.7pp in EN→ZH direction
- Table 5-6: CKA analysis, probe peak after language transition in all 3 models
- Table 7: Label noise ablation -3.3pp per 5%
- Table 8: Steering flip rates ≤8%, uniformly weak

**Section 5 (Discussion):** Detectability robust; asymmetry architecture-dependent; layer structure descriptive; CLEAR connection correlational.

**Section 6 (Limitations):** Single language pair. 3 models. No SAE decomposition (Track 2 incomplete). Weak steering (Track 3 incomplete). 8% label noise. ~1000 instances.

**Section 7 (Conclusion):** Empirical characterization + methodology. Future: more languages, SAE, multi-dim steering.

**Appendix A:** PCA shows 28% variance, misaligned EN/ZH conflict clusters.
**Appendix B:** Token overlap Jaccard 3-4%, no correlation with probe accuracy.

**References (15 total):** Belinkov 2022, Bricken et al. 2023, Chen et al. 2022, Cunningham et al. 2023, Dubey et al. 2024, Elazar et al. 2021, Geiger et al. 2021, Gemma Team 2024, Gonen et al. 2020, Hewitt & Manning 2019, Kornblith et al. 2019, Libovický et al. 2020, Longpre et al. 2021, Müller et al. 2021, Pires et al. 2019, Wendler et al. 2024, Wu & Dredze 2019, Xie et al. 2024, Yang et al. 2025, Zhao et al. 2026.

## Experiment Design Reference (from review_context.yaml)
The original experimental plan was far more ambitious:
- Track 2 (SAE-based mechanistic decomposition): Qwen-Scope SAE feature identification, LangFIR language feature disentangling, cross-lingual Jaccard analysis — ALL not completed
- Track 3 (Causal steering): SAE-based steering transfer, cross-lingual-specific steering, typological steering correlation — ALL not completed
- EN↔JA extension: Only 15% done, not included
- Larger dataset: Not started
- The paper was originally positioned as "mechanism discovery" but was reframed to "empirical characterization + methodology" after Track 2/3 failed to complete

## Your Review Task (R2: Novelty + Related Work)

Evaluate:
1. **Novelty:** How novel are the claims and methodology? Is probing conflict signals in a cross-lingual setting a genuinely new contribution? What's the delta over existing work?
2. **Related work coverage:** Are there important missing references? Is the positioning accurate?
3. **Claim calibration:** Are the claims appropriately scoped given the evidence? Overclaimed or underclaimed?
4. **Contribution significance:** Is the contribution substantial enough for ICLR?
5. **Narrative coherence:** Does the paper tell a convincing story? Is the "architecture-dependent" framing well-supported?
6. **Connection to CLEAR:** Is the claimed connection well-grounded or superficial?

Consider these potential issues:
- The "architecture-dependent" finding is based on only 3 models (1 significant, 1 borderline, 1 null). Is this sufficient?
- The paper admits Track 2 (SAE) and Track 3 (steering) are incomplete. Does the remaining Track 1 alone constitute sufficient novelty?
- Standard probing methodology applied to a new domain — how novel is this?
- Missing references to consider: work on knowledge editing across languages, multilingual knowledge graphs, cross-lingual NLI probing, etc.
- The paper references Zhao et al. [2026] CLEAR heavily but the connection is only correlational.

Provide your review in this format:

```
## Summary
[2-3 sentences]

## Strengths
[Bulleted list, be specific]

## Weaknesses
[Bulleted list, be specific with section references]

## Questions for Authors
[Numbered list]

## Minor Issues
[Bulleted list]

## Assessment of Novelty and Positioning
[Paragraph assessment]

## Scores
- Soundness: X/4
- Presentation: X/4
- Contribution: X/4
- Overall: X/10
- Confidence: X/5
```

Be rigorous but fair. ICLR expects significant contributions — empirical characterization papers need very strong execution to meet the bar.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "a927f2e80c12fa2d4",
  "type": "user",
  "uuid": "c9feda65-1903-4f65-8d02-e1f7730f8673",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T03:32:08.182Z_

```json
{
  "parentUuid": "c9feda65-1903-4f65-8d02-e1f7730f8673",
  "isSidechain": true,
  "agentId": "a927f2e80c12fa2d4",
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
  "uuid": "bf64d514-f11d-4f8c-af3b-b6d50a27f741",
  "timestamp": "2026-05-22T03:32:08.182Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-22T03:32:11.868Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JGB9GAKg9FSApXfNqB2zJd`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf64d514-f11d-4f8c-af3b-b6d50a27f741",
  "isSidechain": true,
  "agentId": "a927f2e80c12fa2d4",
  "requestId": "req_011CbGuHX7YAvzwvHkmfMt1d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27068af5-d629-4fb6-8b76-bf9a25461b88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLEm2RsP1NDgQ4iHxFp2Ct",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8174,
      "cache_read_input_tokens": 8247,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8174
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 88,
          "cache_read_input_tokens": 8247,
          "cache_creation_input_tokens": 8174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8174,
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

_source line 4 · 2026-05-22T03:32:11.871Z_

<details><summary>↩ Tool result · `toolu_01JGB9GAKg9FSApXfNqB2zJd`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27068af5-d629-4fb6-8b76-bf9a25461b88",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "a927f2e80c12fa2d4",
  "type": "user",
  "uuid": "5a036972-958f-4d9d-a877-e9d0fa17008c",
  "sourceToolAssistantUUID": "27068af5-d629-4fb6-8b76-bf9a25461b88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T03:32:16.793Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SzFkpT6tWY8Eu7VTqm3Psw`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a036972-958f-4d9d-a877-e9d0fa17008c",
  "isSidechain": true,
  "agentId": "a927f2e80c12fa2d4",
  "requestId": "req_011CbGuHngAYkCmopL5woxGZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c78007d9-c958-4235-bba4-a586ff37752f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSvvhe2kVy3vDZBmLomWG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 16421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1270,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 6 · 2026-05-22T03:32:16.804Z_

<details><summary>↩ Tool result · `toolu_01SzFkpT6tWY8Eu7VTqm3Psw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/report.md\", \"content\": \"# Handover — 2026-05-22\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| comet_llama_v5 | — | — | — | — |\\n| comet_qwen_v5 | — | — | — | — |\\n| comet_llama_v6 | COMET back-translation 质量验证 Llama ZH 翻译（v6: 跟踪 nohup 进程，v5 被 tmux 监控误标 failed） | — | — | — |\\n\\n## 待处理\\n- comet_llama_v4（准备中）\\n- comet_llama_v3（准备中）\\n- comet_llama_v2（准备中）\\n- comet_llama（准备中）\\n- comet_qwen_v4（准备中）\\n- comet_qwen_v3（准备中）\\n- comet_qwen_v2（准备中）\\n- comet_qwen（准备中）\\n- qwen_zh_act_v2: 用 v2 re-verified 数据（966条，enable_thinking=False）重采 Qwen3-8B ZH 激活，替换 v1 污染数据（1116条）（准备中）\\n- probe_qwen_full（准备中）\\n- …另有 13 项\\n\\n## 近期结论\\n- **mvp_probe_v1** (success): 跨语言知识冲突信号可在 Qwen3-8B-Instruct 残差流中被线性探针检测（EN acc ≥ 80%），且展现有意义的跨语言迁移（EN→ZH binomial p < 0.01, point > 60%）\\n  [bootstrap_asymmetry_corrected_qwen](/api/workspace-files/projects/clkc_mech_interp/artifacts/mvp_probe_v1/data/bootstrap_qwen.json)\\n- **mvp_probe_llama_v1** (success): 跨语言知识冲突信号可在 Llama-3.1-8B-Instruct 残差流中被线性探针检测（EN acc ≥ 80%），且展现跨语言迁移（EN→ZH binomial p < 0.01, point > 60%）——与 Qwen3-8B 形成跨模型验证 ← 基于 mvp_probe_v1\\n  [bootstrap_asymmetry_corrected_llama](/api/workspace-files/projects/clkc_mech_interp/artifacts/mvp_probe_llama_v1/data/bootstrap_llama.json)\\n\\n## 趋势\\n成功 2 / 负向 0 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-41302: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1352, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c78007d9-c958-4235-bba4-a586ff37752f",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "a927f2e80c12fa2d4",
  "type": "user",
  "uuid": "b38d3478-4eef-48ba-a9d8-3dc98fde6dc9",
  "sourceToolAssistantUUID": "c78007d9-c958-4235-bba4-a586ff37752f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T03:32:17.382Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01K9769gwYZmKaLaeDLB81QM`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b38d3478-4eef-48ba-a9d8-3dc98fde6dc9",
  "isSidechain": true,
  "agentId": "a927f2e80c12fa2d4",
  "requestId": "req_011CbGuHngAYkCmopL5woxGZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d6d851f-feae-4678-87ea-f7694d855197",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSvvhe2kVy3vDZBmLomWG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 16421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1270,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 8 · 2026-05-22T03:32:17.397Z_

<details><summary>↩ Tool result · `toolu_01K9769gwYZmKaLaeDLB81QM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: '2026-05-21T12:04:50.276Z'\\n  total_papers: 10\\ncategories: []\\npapers:\\n  zhao2026when:\\n    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'\\n    authors:\\n    - Zhao, J.\\n    - et al.\\n    year: 2026\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2601.07041\\n    doi: ''\\n    bibtex_key: zhao2026when\\n    category: cross-lingual-conflict\\n    role: direct-competitor\\n    relevance: 'CLEAR benchmark: 10-language cross-lingual conflict evaluation. Behavioral\\n      finding that linguistic similarity governs entity-centric conflict resolution.\\n      Our work provides mechanistic explanation.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: director-bootstrap\\n    added_at: '2026-05-21T12:04:50.273Z'\\n  zhao2025steering:\\n    title: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation\\n      Engineering\\n    authors:\\n    - Zhao, Y.\\n    - Devoto, A.\\n    - Hong, G.\\n    - et al.\\n    year: 2025\\n    venue: NAACL 2025 Oral\\n    url: https://arxiv.org/abs/2410.15999\\n    doi: ''\\n    bibtex_key: zhao2025steering\\n    category: sae-steering\\n    role: direct-competitor\\n    relevance: 'SpARE: SAE-based conflict feature selection + steering. Core methodology\\n      we extend to cross-lingual setting. MI-based feature selection, constraint-aware\\n      activation editing.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: director-bootstrap\\n    added_at: '2026-05-21T12:04:50.273Z'\\n  boer2026probing:\\n    title: Probing for Knowledge Attribution in Large Language Models\\n    authors:\\n    - Boer, A.\\n    - Brink, I.\\n    - Ulmer, D.\\n    year: 2026\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2602.22787\\n    doi: ''\\n    bibtex_key: boer2026probing\\n    category: probing\\n    role: direct-competitor\\n    relevance: 0.96 Macro-F1 parametric-vs-contextual attribution probe on Llama/Mistral/Qwen.\\n      Monolingual performance ceiling for our Track 1. Cross-domain transfer 0.94-0.99\\n      F1.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: director-bootstrap\\n    added_at: '2026-05-21T12:04:50.273Z'\\n  kialy2026universal:\\n    title: A Universal Vibe? Finding and Controlling Language-Agnostic Informal Register\\n      with SAEs\\n    authors:\\n    - Kialy, U.Z.\\n    - Shtarkberg, A.\\n    - Klein, A.\\n    year: 2026\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2603.26236\\n    doi: ''\\n    bibtex_key: kialy2026universal\\n    category: cross-lingual-sae\\n    role: direct-competitor\\n    relevance: First cross-lingual SAE feature discovery. Shows cross-linguistic core\\n      for register features + zero-shot steering transfer. We test whether this extends\\n      to knowledge conflict features.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: director-bootstrap\\n    added_at: '2026-05-21T12:04:50.273Z'\\n  wong2026langfir:\\n    title: 'LangFIR: Discovering Sparse Language-Specific Features from Monolingual\\n      Data for Language Steering'\\n    authors:\\n    - Wong, S.H.\\n    - Siddique, A.B.\\n    - Sajjad, H.\\n    year: 2026\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2604.03532\\n    doi: ''\\n    bibtex_key: wong2026langfir\\n    category: cross-lingual-sae\\n    role: direct-competitor\\n    relevance: Random-token filtering isolates <5 language-specific SAE features/language.\\n      Our Track 2 uses this as control to disentangle language-identity from conflict\\n      features.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: director-bootstrap\\n    added_at: '2026-05-21T12:04:50.273Z'\\n  wang2025lost:\\n    title: 'Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency\\n      in Transformer Language Models'\\n    authors:\\n    - Wang, M.\\n    - Adel, H.\\n    - Lange, L.\\n    - et al.\\n    year: 2025\\n    venue: ACL 2025 (SAC Highlights)\\n    url: https://arxiv.org/abs/2504.04264\\n    doi: ''\\n    bibtex_key: wang2025lost\\n    category: cross-lingual-mechanism\\n    role: foundation\\n    relevance: Language-independent concept space through most layers, language-specific\\n      only in final layers. Key mechanistic finding our H1/H2 hypotheses build on.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: director-bootstrap\\n    added_at: '2026-05-21T12:04:50.273Z'\\n  team2026qwen:\\n    title: 'Qwen-Scope: Turning Sparse Features into Development Tools for Large Language\\n      Models'\\n    authors:\\n    - Qwen Team\\n    year: 2026\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2605.11887\\n    doi: ''\\n    bibtex_key: team2026qwen\\n    category: sae-tools\\n    role: foundation\\n    relevance: Pretrained SAEs for Qwen3 family. Our Track 2 uses Qwen-Scope SAEs\\n      on Qwen3-8B-Base. Documents cross-lingual transfer for toxicity features (Section\\n      5.2).\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: director-bootstrap\\n    added_at: '2026-05-21T12:04:50.273Z'\\n  zhao2024analysing:\\n    title: Analysing the Residual Stream of Language Models Under Knowledge Conflicts\\n    authors:\\n    - Zhao, Y.\\n    - Du, X.\\n    - Hong, G.\\n    - et al.\\n    year: 2024\\n    venue: NeurIPS 2024 FMI Workshop\\n    url: https://arxiv.org/abs/2410.16090\\n    doi: ''\\n    bibtex_key: zhao2024analysing\\n    category: probing\\n    role: foundation\\n    relevance: 'Original conflict probing work: ~90% accuracy detecting conflicts\\n      in residual stream. Foundation for our Track 1 cross-lingual extension.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: director-bootstrap\\n    added_at: '2026-05-21T12:04:50.273Z'\\n  pham2026where:\\n    title: 'Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge\\n      Conflict in Language Models'\\n    authors:\\n    - Pham, M.V.\\n    - Borkakoty, H.\\n    - Hou, Y.\\n    year: 2026\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2601.09445\\n    doi: ''\\n    bibtex_key: pham2026where\\n    category: conflict-mechanism\\n    role: direct-competitor\\n    relevance: Activation patching + CMAP for intra-memory conflicts. Attention layers\\n      21-47 dominate conflict resolution in Qwen3-4B. Closest methodological parallel\\n      for within-parametric conflicts.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: director-bootstrap\\n    added_at: '2026-05-21T12:04:50.273Z'\\n  basu2026interpretability:\\n    title: 'Interpretability without actionability: mechanistic methods cannot correct\\n      language model errors despite near-perfect internal representations'\\n    authors:\\n    - Basu, S.\\n    - et al.\\n    year: 2026\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2603.18353\\n    doi: ''\\n    bibtex_key: basu2026interpretability\\n    category: sae-steering\\n    role: direct-competitor\\n    relevance: 'SAE steering failure in clinical triage despite 98.2% AUROC probes.\\n      Critical negative result: defines boundary conditions for when SAE steering\\n      works. Our Track 3 design addresses their methodological gaps.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: director-bootstrap\\n    added_at: '2026-05-21T12:04:50.273Z'\\n\", \"total_chars\": 7107, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d6d851f-feae-4678-87ea-f7694d855197",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "a927f2e80c12fa2d4",
  "type": "user",
  "uuid": "e8d3a45e-b1aa-4cd4-b32b-96649e0c745c",
  "sourceToolAssistantUUID": "7d6d851f-feae-4678-87ea-f7694d855197",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T03:32:20.867Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JxsFzBAumjrKjWovcZvab2`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8d3a45e-b1aa-4cd4-b32b-96649e0c745c",
  "isSidechain": true,
  "agentId": "a927f2e80c12fa2d4",
  "requestId": "req_011CbGuJCHyYYz1XEMSw8YEM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff3c3f1e-20b0-41e0-9186-9e6f12cb174f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QprWnYhsRPrhdYTB8a2z46",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3926,
      "cache_read_input_tokens": 17691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3926,
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

_source line 10 · 2026-05-22T03:32:20.878Z_

<details><summary>↩ Tool result · `toolu_01JxsFzBAumjrKjWovcZvab2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/paper_framing.md\", \"content\": \"# Paper Framing — clkc_mech_interp\\n\\n> 最后更新: 2026-05-22 | 目标: ICLR 2027 (DDL ~2026-09-24)\\n\\n## Core Insight\\n\\n多语言 LLM 中，跨语言知识冲突的检测信号可在残差流中被线性探针检测，且跨语言迁移呈现**方向性不对称**（ZH→EN >> EN→ZH ~7.2pp），该不对称性跨架构高度一致（Llama-3.1-8B 与 Qwen3-8B）。这为 CLEAR (Zhao et al. 2026) 发现的 \\\"entity-centric factual conflicts 中 linguistic affinity 决定冲突解决\\\" 提供了首个**机制层面的解释**。\\n\\n**注意**: CLEAR 的发现是 task-dependent 的——entity-centric factual conflicts 由 linguistic affinity 主导，reasoning-intensive tasks 由 resource abundance 主导。我们使用 ConflictQA（entity-centric），引用 CLEAR 时必须限定为 entity-centric 场景。\\n\\n## Narrative Structure\\n\\n**现象驱动的机制解释**（非 \\\"applying X to Y\\\"）：\\n\\n1. **Phenomenon**: CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity（而非 resource abundance）决定跨语言冲突解决，但未提供机制解释\\n2. **Mechanistic question**: 冲突信号在模型内部如何编码？是 language-universal 还是 language-specific？为什么 similarity 起决定作用？\\n3. **Our answer**: 通过残差流探针、SAE 特征分析、激活干预三条互补分析轨道，揭示冲突检测信号的跨语言结构——是否共享、在哪些层出现、能否用于干预\\n\\n**Secondary framing**: SAE-based mechanistic interpretability 工具在跨语言条件下的 stress test——probing / SAE / steering 三种工具的跨语言适用性边界\\n\\n## Competing Hypotheses (pre-registered)\\n\\n**H1 — English-anchored universal detection**:\\n冲突检测信号本身是 language-independent 的（\\\"是否存在冲突\\\" 是语言无关判断），编码在 mid-layer 共享表征空间中。final-layer language transition 引入 similarity-dependent 干扰，影响 resolution 但不影响 detection。\\n- 预测: mid-layer conflict feature 跨语言 Jaccard >> late-layer Jaccard (paired permutation test p < 0.05)\\n- 预测: 英语探针跨语言迁移更强（英语作为训练数据主导语言，表征空间以英语为锚点）\\n\\n**H2 — Language-pair-specific encoding**:\\n冲突特征从 mid-layer 起即为 language-pair-specific 的，linguistic distance 直接编码在冲突表征中。\\n- 预测: mid-layer 和 late-layer Jaccard 无显著差异，或 mid < late\\n- 预测: 探针迁移准确率与语言对 typological distance 强相关\\n\\n**MVP 证据倾向**:\\n当前双模型结果倾向 **H1 的变体**——ZH→EN 迁移（71-72%）显著强于 EN→ZH（64-65%），暗示冲突信号以英语表征空间为锚点编码。非线性成分（MLP EN→ZH +9.2pp vs linear）提示 EN→ZH 方向的跨语言映射更复杂。\\n\\n## Core Claims\\n\\n### Claim 1: Cross-lingual conflict detectability\\n**Statement**: 跨语言知识冲突信号可在残差流中被线性探针检测，准确率显著高于随机基线。\\n**Evidence needed**:\\n- ≥2 model architectures 的 within-language probe acc > 70% (balanced) ✅ (Llama 77.1%, Qwen 75.3%)\\n- Permutation test p < 0.001 ✅ (all directions)\\n- Cross-lingual transfer acc > chance (50%) with statistical significance ✅ (all directions 64-72%)\\n**Status**: MVP 已验证 ✅\\n\\n### Claim 2: Asymmetric cross-lingual transfer\\n**Statement**: 跨语言探针迁移呈方向一致的不对称：ZH→EN 迁移强于 EN→ZH（~7.2pp），效果量跨架构高度一致（Llama 显著，Qwen 方向一致但未达显著）。\\n**Evidence needed**:\\n- Bootstrap CI for asymmetry gap (corrected, plan_099 ✅):\\n  - Llama: +7.22pp, CI [1.1%, 13.6%] — 排除零但 borderline ✅\\n  - Qwen: +7.18pp, CI [-1.2%, 13.4%] — 含零，方向一致 ⚠️\\n- ≥2 models show consistent effect size ✅ (7.22pp vs 7.18pp)\\n- Token overlap analysis 排除词汇重叠驱动的虚假迁移 ✅ (plan_101 完成: per-sample Jaccard 3-4%, Qwen 无相关 p>0.4, Llama 显著负相关 r=-0.15 p=0.012 — RC2 排除)\\n- ≥1 additional model architecture 验证跨架构一致性 ❌ (planned P0)\\n**Status**: 初步验证 ⚠️ (需补 token overlap + 第三模型)\\n\\n### Claim 3: Direction-dependent non-linear components\\n**Statement**: 跨语言冲突信号的弱迁移方向（EN→ZH）包含方向依赖的非线性成分，MLP 探针在该方向提升最大。跨架构一致方向但幅度不同（Llama +9.2pp single-seed / ~+4.7pp bootstrap-corrected, Qwen +2.3pp），暗示非线性成分与模型的跨语言对齐程度相关。\\n**Evidence needed**:\\n- MLP vs linear probe comparison on ≥2 models ✅ (both show EN→ZH direction gains)\\n- MLP 不使用 test set 做 early stopping ✅ (已修复)\\n- 控制实验排除 MLP 过拟合 ❌ (需 train/test accuracy gap 分析)\\n- 解释跨架构幅度差异 (Llama 4x > Qwen) ❌ (可能与 Qwen 更强的跨语言对齐有关——ZH 训练数据占比更高)\\n**Status**: 初步验证 ⚠️ (方向一致但幅度差异需解释)\\n\\n### Claim 4: Layer-wise conflict signal structure\\n**Statement**: 冲突信号在 mid-to-upper layers 集中，峰值层在不同模型架构中占比一致（Llama ~88% depth, Qwen ~67% depth 有差异——需更多模型确认 pattern）。\\n**Evidence needed**:\\n- Layer-wise probe accuracy curves for ≥3 models ❌\\n- Layer-wise CKA/SVCCA 量化 EN vs ZH 表征相似度 ❌\\n- 与 \\\"Lost in Multilinguality\\\" 的 language transition 层对比 ❌\\n**Status**: 未验证 ❌\\n\\n### Claim 5: Cross-lingual SAE conflict features (Track 2)\\n**Statement**: SAE 特征空间中存在跨语言共享的冲突编码特征，可与 language-identity 特征解耦。\\n**Evidence needed**:\\n- Qwen-Scope SAE 特征分析 on Qwen3-8B-Base ❌\\n- LangFIR random-token filtering 控制 ❌\\n- Cross-lingual feature Jaccard 分析 ❌\\n**Status**: 未开始 ❌\\n\\n### Claim 6: Cross-lingual conflict steering (Track 3)\\n**Statement**: 通过 SAE 特征干预可以定向操控跨语言冲突解决行为。\\n**Evidence needed**:\\n- SpARE 框架跨语言扩展 ❌\\n- Monolingual → cross-lingual steering transfer ❌\\n- Steering effectiveness vs linguistic distance correlation ❌\\n**Status**: 未开始 ❌ (依赖 Track 2)\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Translation quality confound [RESOLVED ✅]\\n**Concern**: 中文翻译质量差可能导致虚假的冲突信号或迁移失败\\n**Result**: Plan_105 COMET tercile ablation 证明翻译质量非 confounder。Qwen test: Low COMET (mean 0.585) → 66.35% acc, High COMET (mean 0.816) → 60.71% acc, delta=-5.64pp (反向), Fisher p=0.695。冲突信号检测不依赖翻译质量。Back-translation COMET ≥0.80 阈值过严（两步翻译天然拉低），但 ablation 实证排除了翻译质量 confound。\\n**Remaining**: Llama test COMET 完成后重复此分析确认一致性。\\n\\n### RC2: Token overlap confound [RESOLVED ✅]\\n**Concern**: 跨语言迁移可能由 EN-ZH 共享 token（数字、专有名词、标点）驱动\\n**Result**: Per-sample Jaccard 仅 3-4%（type-level 10-15% 被膨胀）。Qwen 无相关 (p>0.4)，Llama 显著负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。高 overlap 反而降低准确率，方向与 RC2 相反。**共享 token 不驱动跨语言迁移，迁移发生在语义表示层。**\\n\\n### RC3: Model coverage insufficient [HIGH]\\n**Concern**: 只有 2 个模型，无法声称 \\\"架构无关\\\"\\n**Mitigation**: 加 ≥1 不同架构（Mistral/Gemma），验证 ~7.2pp 不对称性\\n**Experiment**: P0 — additional model verification\\n\\n### RC4: Dataset size and diversity [MEDIUM]\\n**Concern**: ConflictQA 覆盖面有限（~1000 samples/model），只有 EN-ZH 一个语言对\\n**Mitigation**: Phase 1 聚焦 EN-ZH 验证核心机制，Phase 2 扩展多语言（≥1 额外语言对）\\n**Experiment**: P0 — multilingual extension (EN↔JA or EN↔DE)\\n\\n### RC5: Linear probe expressiveness [LOW]\\n**Concern**: 线性探针可能遗漏复杂非线性信号\\n**Mitigation**: MLP 对比实验已完成 ✅，非线性成分已量化\\n**Experiment**: Done — MLP vs Linear comparison\\n\\n### RC6: SAE base/instruct mismatch [MEDIUM]\\n**Concern**: Qwen-Scope SAE 训练在 base model 上，用于 instruct model 分析可能失配\\n**Mitigation**: Track 2 用 base model 做 SAE 分析 + 与 Track 1 instruct probe 交叉验证\\n**Experiment**: Track 2 设计已考虑\\n\\n### RC7: Steering failure precedent [MEDIUM]\\n**Concern**: \\\"Interpretability without actionability\\\" 证明 SAE steering 可能完全无效\\n**Mitigation**: 知识冲突与临床分诊的 5 维差异（SpARE 已证明知识冲突场景 steering 有效）；Track 3 显式报告失败模式\\n**Experiment**: Track 3 包含 negative result framing\\n\\n### RC8: Causal claims without intervention [HIGH]\\n**Concern**: 探针只证明信号可检测，不证明因果关系\\n**Mitigation**: Track 3 steering 实验提供因果证据；Track 1 permutation test 提供统计控制\\n**Experiment**: Track 3 steering + representation steering (P1)\\n\\n## Paper Structure (Tentative)\\n\\n1. **Introduction**: CLEAR gap → mechanistic question → H1 vs H2 → three-track approach → key findings preview\\n2. **Related Work**: Monolingual conflict mechanisms → Cross-lingual processing → SAE steering (successes & failures) → Cross-lingual SAE features\\n3. **Method**: Data construction (ConflictQA + translation + verification pipeline) → Track 1 probing → Track 2 SAE analysis → Track 3 steering\\n4. **Experiments & Results**:\\n   - 4.1 Cross-lingual conflict detectability (C1)\\n   - 4.2 Asymmetric transfer analysis (C2) + token overlap controls\\n   - 4.3 Non-linear components (C3) + layer-wise structure (C4)\\n   - 4.4 SAE feature analysis (C5) [if Track 2 ready]\\n   - 4.5 Steering experiments (C6) [if Track 3 ready]\\n5. **Discussion**: H1 vs H2 resolution → mechanism implications → limitations → connection to CLEAR\\n6. **Conclusion**\\n\\n## Scope Control\\n\\n**投稿最低要求 (must-have for submission)**:\\n- Claims 1-3 fully supported (cross-lingual detectability + asymmetry + non-linearity)\\n- Claim 4 partially supported (layer-wise analysis on ≥2 models)\\n- ≥3 model architectures\\n- ≥2 language pairs (EN-ZH + one more)\\n- Token overlap control\\n- COMET translation quality validation\\n\\n**理想状态 (nice-to-have)**:\\n- Track 2 SAE analysis (Claim 5)\\n- Track 3 steering (Claim 6)\\n- 5+ language pairs covering multiple typological families\\n- Full CKA/SVCCA layer analysis\\n\\n**不做 (out of scope)**:\\n- 10-language full CLEAR replication\\n- Custom SAE training\\n- MoE model analysis\\n\", \"total_chars\": 7801, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff3c3f1e-20b0-41e0-9186-9e6f12cb174f",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "a927f2e80c12fa2d4",
  "type": "user",
  "uuid": "96fd003d-21ea-4cc4-ac5e-d3aebc675e28",
  "sourceToolAssistantUUID": "ff3c3f1e-20b0-41e0-9186-9e6f12cb174f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T03:32:21.095Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013Wp8qn39QQfVpEmZCciXjX`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96fd003d-21ea-4cc4-ac5e-d3aebc675e28",
  "isSidechain": true,
  "agentId": "a927f2e80c12fa2d4",
  "requestId": "req_011CbGuJCHyYYz1XEMSw8YEM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cfe9cf4-c232-423c-9eea-9ca440eb37f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QprWnYhsRPrhdYTB8a2z46",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3926,
      "cache_read_input_tokens": 17691,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3926
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 17691,
          "cache_creation_input_tokens": 3926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3926,
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

_source line 12 · 2026-05-22T03:32:21.104Z_

<details><summary>↩ Tool result · `toolu_013Wp8qn39QQfVpEmZCciXjX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ROADMAP.md\", \"content\": \"# clkc_mech_interp — Research Dashboard\\n\\n> 最后更新: 2026-05-22 02:38 UTC | 更新原因: MVP 通过，进入 Research 阶段，Dream 已提交\\n\\n## 核心方向\\n多语言 LLM 中跨语言知识冲突的机制可解释性研究。核心发现：冲突信号可线性检测，跨语言迁移存在方向性不对称（~7.2pp），跨架构一致。目标 ICLR 2027（DDL 2026-09-24）。详见 paper_framing.md。\\n\\n## 当前阶段：Research（MVP 已通过 ✅）\\n\\nMVP 通过条件：双模型探针验证 + 两个 confounder 排除（token overlap + COMET ablation）。\\n\\n### 双模型 Bootstrap n=100 结果（可引用）\\n\\n| 方向 | Llama-3.1-8B (mean±std) | Qwen3-8B (mean±std) |\\n|------|------------------------|---------------------|\\n| EN→EN | **77.1±1.2%** | **75.3±1.7%** |\\n| ZH→ZH | **71.2±1.3%** | **71.6±1.8%** |\\n| EN→ZH | **64.1±2.5%** | **65.0±2.7%** |\\n| ZH→EN | **71.3±2.7%** | **72.2±2.6%** |\\n\\n不对称性 (corrected): Llama +7.22pp CI [1.1%, 13.6%] sig | Qwen +7.18pp CI [-1.2%, 13.4%] trending\\n\\n### Confounder 排除\\n- **RC1 翻译质量**: plan_105 COMET tercile ablation → delta=-5.64pp (反向), p=0.695, 非 confounder ✅\\n- **RC2 Token overlap**: plan_101 → per-sample Jaccard 3-4%, Llama 负相关 r=-0.15, 非 confounder ✅\\n\\n### 近期任务\\n- [x] ~~complete_mvp()~~ ✅\\n- [ ] dream_simulate(review_mode=\\\"full\\\") — dream_20260522T023801 pending (10-25 min)\\n- [ ] Llama test COMET 完成后跑 Llama 版 tercile ablation（确认一致性）\\n- [ ] COMET train 继续跑（Qwen ~3.8h, Llama ~7h）\\n- [ ] Dream 完成后审阅 → 批准 P0 实验启动\\n\\n### Post-MVP P0 实验（等 Dream 审阅后启动）\\n1. ~~Token overlap (plan_101)~~ ✅\\n2. ~~Bootstrap CI 修正 (plan_099)~~ ✅\\n3. ~~COMET tercile ablation (plan_105)~~ ✅ (Qwen done, Llama pending)\\n4. 第三模型 Gemma-2-9B-IT (plan_102) — 模型已下载, 等 GPU\\n5. 多语言扩展 EN↔JA (plan_103) — planned, ~20 GPU·h\\n6. Layer-wise CKA/SVCCA (plan_104) — planned, ~4 GPU·h\\n7. Representation steering (plan_107) — planned, ~8 GPU·h\\n\\n## GPU 预算\\nwestd-41302: 4× RTX PRO 6000 Blackwell 96GB（cuda:0-3）\\n当前: cuda:0,2 COMET train; cuda:3 COMET Llama test; cuda:1 空闲\\n\\n## 风险\\n1. Llama CI 下界 borderline (1.1pp) — 第三模型 Gemma 结果决定 C2 强度\\n2. 只有 Track 1 时论文贡献可能偏 analysis paper — Dream 审稿将评估\\n3. COMET train 仍需 4-8h 完成\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-22 | COMET 0.80 阈值不直接适用 back-translation：提升 plan_105 至  | comet_qwen_v5, mvp_probe_v1 |\\n| D005 | 2026-05-21 | 双模型 MVP CONDITIONAL PASS：Llama EN→EN 77.6% + Qwen  | mvp_probe_llama_v1, mvp_probe_v1 |\\n| D004 | 2026-05-21 | Llama MVP CONDITIONAL PASS → EXTEND：EN→EN 77.6%, 跨 | mvp_probe_llama_v1 |\\n| D003 | 2026-05-21 | 补采样至 2000 条 + 取消强制交集，每个模型用各自 verified 数据集 | mvp_probe_llama_v1 |\\n| D002 | 2026-05-21 | 采纳 Reviewer 5 条 warning，细化 MVP gate：增加 70-79% cond | — |\\n| D001 | 2026-05-21 | MVP 方案：EN+ZH 双语探针迁移实验验证跨语言冲突信号可检测性 | — |\\n\\n\\n\", \"total_chars\": 2474, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8cfe9cf4-c232-423c-9eea-9ca440eb37f8",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "a927f2e80c12fa2d4",
  "type": "user",
  "uuid": "e58e0fde-b04e-4b88-a729-5ac25435fe18",
  "sourceToolAssistantUUID": "8cfe9cf4-c232-423c-9eea-9ca440eb37f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-22T03:32:25.007Z_

Now I have sufficient context to write a thorough review. Let me also check the paper's artifacts to understand the actual experimental results better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e58e0fde-b04e-4b88-a729-5ac25435fe18",
  "isSidechain": true,
  "agentId": "a927f2e80c12fa2d4",
  "requestId": "req_011CbGuJU9y5s148TwNt24Ge",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38230495-356e-46d6-8277-607948f9ee78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkCNYsRpkAyUoVtMoGjdry",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6095,
      "cache_read_input_tokens": 21617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6095,
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

_source line 14 · 2026-05-22T03:32:25.423Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Xom25trWXqJbbXCNdE9ahg`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38230495-356e-46d6-8277-607948f9ee78",
  "isSidechain": true,
  "agentId": "a927f2e80c12fa2d4",
  "requestId": "req_011CbGuJU9y5s148TwNt24Ge",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9cc2ae1-fbc6-4662-836b-a12e83b13b72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkCNYsRpkAyUoVtMoGjdry",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6095,
      "cache_read_input_tokens": 21617,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6095
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 21617,
          "cache_creation_input_tokens": 6095,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6095,
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

_source line 15 · 2026-05-22T03:32:25.512Z_

<details><summary>↩ Tool result · `toolu_01Xom25trWXqJbbXCNdE9ahg`</summary>

```text
artifacts/dream_reports/dream_20260522T023801/best/paper.tex
artifacts/dream_reports/dream_20260522T023801/median/paper.tex
artifacts/dream_reports/dream_20260522T023801/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9cc2ae1-fbc6-4662-836b-a12e83b13b72",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "a927f2e80c12fa2d4",
  "type": "user",
  "uuid": "4fd717c2-d98c-431b-adaf-7c2744e7e07a",
  "sourceToolAssistantUUID": "d9cc2ae1-fbc6-4662-836b-a12e83b13b72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T03:32:34.143Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T5SMyLv1yxzqTQZcPC73Yg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fd717c2-d98c-431b-adaf-7c2744e7e07a",
  "isSidechain": true,
  "agentId": "a927f2e80c12fa2d4",
  "requestId": "req_011CbGuJnpNdhGLdRG6dPx5m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6b1e9e7-bedd-40e4-90c5-1acdac825eac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WoXdqja1rJhqfwHS3DCgne",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 200,
      "cache_read_input_tokens": 27712,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 200
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 27712,
          "cache_creation_input_tokens": 200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 200,
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

_source line 17 · 2026-05-22T03:32:34.151Z_

<details><summary>↩ Tool result · `toolu_01T5SMyLv1yxzqTQZcPC73Yg`</summary>

```text
1	\documentclass{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{hyperref}
9	\usepackage[margin=1in]{geometry}
10	\usepackage{xcolor}
11	\usepackage{natbib}
12	\usepackage{caption}
13	\usepackage{subcaption}
14	
15	\title{Cross-Lingual Conflict Detection in Multilingual LLMs:\\
16	Mechanistic Evidence for English-Anchored Representations}
17	
18	\author{
19	Anonymous Authors
20	}
21	
22	\date{}
23	
24	\begin{document}
25	
26	\maketitle
27	
28	% ============================================================
29	% ABSTRACT
30	% ============================================================
31	\begin{abstract}
32	Multilingual large language models resolve entity-centric knowledge conflicts in ways that depend on linguistic affinity rather than resource abundance, yet the internal mechanisms underlying this behavior remain unexplored. We present a mechanistic investigation of cross-lingual conflict detection signals in the residual stream of three transformer architectures (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B-IT) across two typologically distinct language pairs (EN$\leftrightarrow$ZH, EN$\leftrightarrow$JA). Linear probes trained on residual stream activations detect conflict signals at 70--77\% balanced accuracy, with cross-lingual transfer exhibiting a consistent directional asymmetry: transfer toward English (X$\to$EN) outperforms transfer away from English (EN$\to$X) by 6.3--7.9 percentage points across all model--language-pair combinations tested. Sparse autoencoder (SAE) analysis reveals 18 cross-lingually shared conflict features concentrated in middle layers (Jaccard = 0.28) that diverge in late layers (Jaccard = 0.12, $p = 0.008$), while language-identity features occupy early layers with minimal overlap (4.3\%). Representation steering using probe directions and SAE features causally shifts model outputs from parametric to contextual answers, with cross-lingual flip rates reproducing the same directional asymmetry. These converging lines of evidence---probing, feature decomposition, and causal intervention---support an English-anchored hypothesis: conflict detection is encoded in a language-universal mid-layer representation anchored to English, while language-specific resolution occurs during late-layer language transition.
33	\end{abstract}
34	
35	% ============================================================
36	% 1. INTRODUCTION
37	% ============================================================
38	\section{Introduction}
39	
40	When multilingual LLMs encounter factual knowledge conflicts---cases where contextual information contradicts parametric knowledge---the language of presentation systematically influences which knowledge source prevails. Recent work by Zhao et al.\ (2026) (CLEAR) demonstrated that for entity-centric factual conflicts, linguistic affinity between the context and query languages determines conflict resolution outcomes, rather than the absolute resource abundance of either language. This finding raises a fundamental mechanistic question: \emph{how are cross-lingual conflict signals encoded in the model's internal representations, and why does linguistic similarity play a decisive role?}
41	
42	We investigate this question through three complementary analysis tracks applied to the residual stream of multilingual transformers. \textbf{Track 1} (probing) trains linear and MLP classifiers on residual stream activations to detect and transfer conflict signals across languages. \textbf{Track 2} (SAE decomposition) uses pre-trained sparse autoencoders to identify monosemantic conflict features and characterize their cross-lingual sharing patterns. \textbf{Track 3} (causal intervention) steers model behavior by manipulating conflict-related directions in activation space.
43	
44	We formulate two competing hypotheses about the encoding of cross-lingual conflict signals:
45	
46	\begin{itemize}
47	    \item \textbf{H1 (English-anchored universal detection)}: Conflict detection signals are language-independent, encoded in a mid-layer shared representation space anchored to English. Late-layer language transition introduces language-specific interference that affects resolution but not detection. This predicts: (a) mid-layer cross-lingual feature sharing significantly exceeds late-layer sharing; (b) transfer toward English is consistently stronger than transfer away.
48	
49	    \item \textbf{H2 (Language-pair-specific encoding)}: Conflict features are language-pair-specific from mid-layers onward, with linguistic distance directly encoded in conflict representations. This predicts: (a) no significant difference between mid-layer and late-layer feature sharing; (b) transfer patterns differ qualitatively across language pairs.
50	\end{itemize}
51	
52	Our experiments on three architectures (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B-IT) and two language pairs (EN$\leftrightarrow$ZH, EN$\leftrightarrow$JA) yield four principal findings:
53	
54	\begin{enumerate}
55	    \item Cross-lingual conflict signals are linearly detectable in the residual stream at 64--77\% balanced accuracy across all directions and models, with permutation test $p < 0.001$.
56	    \item Cross-lingual transfer is directionally asymmetric: X$\to$EN exceeds EN$\to$X by 6.3--7.9pp across all 4 model$\times$language-pair combinations (3/4 statistically significant at 95\% CI, 4/4 directionally consistent).
57	    \item SAE conflict features are cross-lingually shared in middle layers (Jaccard = 0.28) but diverge in late layers (Jaccard = 0.12), with language-identity features occupying a distinct early-layer subspace (overlap rate 4.3\%).
58	    \item Representation steering causally shifts conflict resolution behavior, with cross-lingual flip rate asymmetry mirroring the probe transfer asymmetry.
59	\end{enumerate}
60	
61	These results collectively support H1: conflict detection is encoded in an English-anchored language-universal representation, with language-specific processing emerging during late-layer transition.
62	
63	% ============================================================
64	% 2. RELATED WORK
65	% ============================================================
66	\section{Related Work}
67	
68	\paragraph{Knowledge conflicts in LLMs.}
69	Knowledge conflicts arise when contextual information contradicts a model's parametric knowledge. Prior work has characterized monolingual conflict resolution behavior and identified internal signals predictive of which knowledge source prevails. However, the cross-lingual dimension remains largely unexplored. CLEAR (Zhao et al., 2026) established that for entity-centric conflicts, linguistic affinity---not resource abundance---determines resolution outcomes across 10 languages, but provided no mechanistic account.
70	
71	\paragraph{Cross-lingual representations in multilingual models.}
72	Multilingual transformers develop shared cross-lingual representations in middle layers before diverging in late layers for language-specific decoding. Wendler et al.\ (2024) documented this ``language transition'' phenomenon across model families, finding that mid-layers form language-agnostic conceptual representations. Our work builds on this finding by examining how conflict-specific signals interact with this layer-wise structure.
73	
74	\paragraph{Sparse autoencoders for mechanistic interpretability.}
75	Sparse autoencoders (SAEs) decompose neural activations into interpretable monosemantic features. Recent work has applied SAEs to identify knowledge-related features and demonstrated that manipulating these features can steer model behavior (SpARE). We extend this line to the cross-lingual setting, using pre-trained SAEs (Qwen-Scope) to decompose conflict signals into shared and language-specific components.
76	
77	\paragraph{Representation steering.}
78	Activation steering modifies model behavior by adding direction vectors to the residual stream. While effective for monolingual settings, cross-lingual steering introduces additional challenges. We use both probe-derived directions and SAE feature directions for cross-lingual conflict steering, providing complementary causal evidence.
79	
80	% ============================================================
81	% 3. METHOD
82	% ============================================================
83	\section{Method}
84	
85	\subsection{Data Construction}
86	
87	We construct cross-lingual knowledge conflict datasets from ConflictQA, which contains entity-centric factual questions where contextual and parametric answers diverge. For each question, we obtain model responses in English (EN) and generate high-quality translations in Chinese (ZH) and Japanese (JA) using the target models themselves, followed by back-translation quality verification using COMET (wmt22-comet-da).
88	
89	\paragraph{Translation quality validation.}
90	Back-translation COMET scores are computed for all translated samples. We perform tercile ablation analysis to verify that translation quality does not confound conflict detection: samples are split into low, medium, and high COMET terciles, and balanced accuracy is compared across groups. As shown in Table~\ref{tab:comet}, both Llama-3.1-8B and Qwen3-8B show no positive correlation between COMET score and probe accuracy (Fisher $p > 0.69$), with the high-COMET tercile actually producing \emph{lower} accuracy than the low-COMET tercile. This rules out translation quality as a confound.
91	
92	\begin{table}[t]
93	\centering
94	\caption{COMET tercile ablation. Probe accuracy does not increase with translation quality, ruling out translation quality as a confound.}
95	\label{tab:comet}
96	\small
97	\begin{tabular}{llcccc}
98	\toprule
99	Model & Tercile & $N$ & COMET$_{\text{mean}}$ & Bal.\ Acc. & $\Delta$ vs Low \\
100	\midrule
101	\multirow{3}{*}{Llama-3.1-8B} & Low & 91 & 0.582 & 64.8\% & --- \\
102	 & Med & 91 & 0.714 & 66.1\% & +1.3pp \\
103	 & High & 90 & 0.821 & 63.2\% & $-$1.6pp \\
104	\midrule
105	\multirow{3}{*}{Qwen3-8B} & Low & 56 & 0.585 & 66.4\% & --- \\
106	 & Med & 56 & 0.700 & 67.7\% & +1.3pp \\
107	 & High & 56 & 0.816 & 60.7\% & $-$5.6pp \\
108	\bottomrule
109	\end{tabular}
110	\end{table}
111	
112	\subsection{Track 1: Residual Stream Probing}
113	
114	For each model, we extract residual stream activations at every layer for conflict and non-conflict samples in each language. We train logistic regression probes (L2-regularized) to classify conflict vs.\ non-conflict, using 5-fold stratified cross-validation with balanced accuracy as the metric. Cross-lingual transfer is evaluated by training on language A and testing on language B without fine-tuning. We assess significance using permutation tests ($n = 1000$) and bootstrap confidence intervals ($n = 100$) for the asymmetry gap.
115	
116	MLP probes (single hidden layer, 256 units) are trained with identical splits to quantify non-linear components. Statistical significance is determined at $\alpha = 0.05$.
117	
118	\subsection{Track 2: SAE Feature Analysis}
119	
120	We apply pre-trained sparse autoencoders from Qwen-Scope to Qwen3-8B-Base activations. Conflict-relevant features are identified via mutual information between feature activations and conflict labels, yielding a ranked list from which the top 128 candidates are selected and filtered to retain features with robust conflict--non-conflict discrimination.
121	
122	To disentangle conflict features from language-identity features, we apply LangFIR-style random-token filtering: features that activate consistently across random token sequences in a given language are classified as language-identity features, and their overlap with conflict features is quantified.
123	
124	Cross-lingual feature sharing is measured by the Jaccard index of EN and ZH conflict feature sets, computed separately for early (0--33\%), mid (33--67\%), and late (67--100\%) layer groups. The H1 vs.\ H2 prediction is tested by a paired permutation test comparing mid-layer and late-layer Jaccard.
125	
126	\subsection{Track 3: Causal Intervention via Steering}
127	
128	\paragraph{Probe-based steering.}
129	The weight vector of the best-layer linear probe defines a conflict direction in activation space. We add $\alpha \cdot \mathbf{v}$ to the residual stream at the optimal layer (where $\alpha$ is tuned to maximize flip rate while preserving coherence) and measure the rate at which model outputs shift from parametric to contextual answers.
130	
131	\paragraph{SAE feature steering.}
132	We construct steering vectors from SAE conflict features (shared, EN-only, ZH-only, and combined sets) by clamping selected feature activations. Cross-lingual transfer is evaluated by applying EN-derived steering vectors to ZH inputs and vice versa.
133	
134	% ============================================================
135	% 4. EXPERIMENTS AND RESULTS
136	% ============================================================
137	\section{Experiments and Results}
138	
139	\subsection{Cross-Architecture Conflict Detectability}
140	\label{sec:detectability}
141	
142	We train linear probes on residual stream activations from three model architectures: Llama-3.1-8B, Qwen3-8B, and Gemma-2-9B-IT. Table~\ref{tab:cross_arch} reports balanced accuracy for all four transfer directions (within-language and cross-lingual) along with the asymmetry gap and bootstrap confidence intervals.
143	
144	\begin{table}[t]
145	\centering
146	\caption{Cross-architecture probe results. EN$\to$EN and ZH$\to$ZH are within-language; EN$\to$ZH and ZH$\to$EN are cross-lingual transfer. Asym.\ gap = (ZH$\to$EN) $-$ (EN$\to$ZH). All permutation test $p < 0.001$.}
147	\label{tab:cross_arch}
148	\small
149	\begin{tabular}{lccccccl}
150	\toprule
151	Model & EN$\to$EN & ZH$\to$ZH & EN$\to$ZH & ZH$\to$EN & Gap & 95\% CI & Sig. \\
152	\midrule
153	Llama-3.1-8B & 77.1\% & 71.2\% & 64.1\% & 71.3\% & +7.2pp & [1.1, 13.6] & Yes \\
154	Qwen3-8B & 75.3\% & 71.6\% & 65.0\% & 72.2\% & +7.2pp & [$-$1.2, 13.4] & No (trend) \\
155	Gemma-2-9B-IT & 76.4\% & 70.8\% & 64.7\% & 72.6\% & +7.9pp & [2.3, 13.8] & Yes \\
156	\bottomrule
157	\end{tabular}
158	\end{table}
159	
160	All within-language probes achieve 70--77\% balanced accuracy, substantially above the 50\% chance baseline (permutation $p < 0.001$ for all). Cross-lingual transfer succeeds in all directions (64--73\%), confirming that conflict signals are partially shared across languages.
161	
162	The asymmetry gap is remarkably consistent: +7.2pp (Llama), +7.2pp (Qwen), and +7.9pp (Gemma), with a coefficient of variation below 6\%. Two of three models reach statistical significance at 95\% confidence; Qwen shows the same direction but the CI includes zero at $N \approx 1000$. We address this power issue in Section~\ref{sec:scaling}.
163	
164	\paragraph{MLP non-linearity.}
165	MLP probes reveal direction-dependent non-linear components in the weak transfer direction (EN$\to$ZH), as shown in Table~\ref{tab:mlp}. The gain is largest for Gemma (+6.1pp), moderate for Llama (+4.7pp), and smallest for Qwen (+2.3pp). This gradient anti-correlates with each model's Chinese pre-training data proportion, suggesting that stronger cross-lingual alignment reduces the non-linear component of cross-lingual conflict mapping.
166	
167	\begin{table}[t]
168	\centering
169	\caption{MLP gain in the weak transfer direction (EN$\to$ZH). Models with better Chinese alignment show smaller non-linear gains.}
170	\label{tab:mlp}
171	\small
172	\begin{tabular}{lcccc}
173	\toprule
174	Model & Linear & MLP & Gain & Interpretation \\
175	\midrule
176	Llama-3.1-8B & 64.1\% & 68.8\% & +4.7pp & Strong non-linear component \\
177	Qwen3-8B & 65.0\% & 67.3\% & +2.3pp & Weak (better ZH alignment) \\
178	Gemma-2-9B-IT & 64.7\% & 70.8\% & +6.1pp & Moderate non-linear component \\
179	\bottomrule
180	\end{tabular}
181	\end{table}
182	
183	\subsection{Multilingual Extension: EN$\leftrightarrow$JA}
184	\label{sec:multilingual}
185	
186	To test whether the asymmetry generalizes beyond EN$\leftrightarrow$ZH, we replicate the full probe experiment on the EN$\leftrightarrow$JA language pair using Qwen3-8B and Llama-3.1-8B. Japanese is typologically distinct from Chinese (SOV word order, complex morphology, multiple writing systems) while belonging to the same CJK cultural sphere.
187	
188	\begin{table}[t]
189	\centering
190	\caption{Multi-lingual asymmetry comparison. All four model$\times$language-pair combinations show X$\to$EN $>$ EN$\to$X.}
191	\label{tab:multilingual}
192	\small
193	\begin{tabular}{llccccc}
194	\toprule
195	Model & Pair & X$\to$EN & EN$\to$X & Gap & 95\% CI & Direction \\
196	\midrule
197	Qwen3-8B & EN$\leftrightarrow$ZH & 72.2\% & 65.0\% & +7.2pp & [$-$1.2, 13.4] & ZH$\to$EN wins \\
198	Qwen3-8B & EN$\leftrightarrow$JA & 68.1\% & 61.8\% & +6.3pp & [0.4, 12.5] & JA$\to$EN wins \\
199	Llama-3.1-8B & EN$\leftrightarrow$ZH & 71.3\% & 64.1\% & +7.2pp & [1.1, 13.6] & ZH$\to$EN wins \\
200	Llama-3.1-8B & EN$\leftrightarrow$JA & 66.8\% & 60.1\% & +6.7pp & [0.8, 13.1] & JA$\to$EN wins \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6b1e9e7-bedd-40e4-90c5-1acdac825eac",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "a927f2e80c12fa2d4",
  "type": "user",
  "uuid": "4e33efb2-2211-47ae-a721-861fd7e07b29",
  "sourceToolAssistantUUID": "e6b1e9e7-bedd-40e4-90c5-1acdac825eac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T03:32:38.859Z_

<details open><summary>🔧 Tool call — Read · `toolu_012RbmdkWoHJ9qSXWv8zzPgP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e33efb2-2211-47ae-a721-861fd7e07b29",
  "isSidechain": true,
  "agentId": "a927f2e80c12fa2d4",
  "requestId": "req_011CbGuKRy2mLmXmBcaZSCvN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "458f306d-25c1-45ba-9d16-ab7db680be2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MgYERzcYRwgfzqngw8HPez",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5227,
      "cache_read_input_tokens": 27912,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5227
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 27912,
          "cache_creation_input_tokens": 5227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5227,
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

_source line 19 · 2026-05-22T03:32:38.865Z_

<details><summary>↩ Tool result · `toolu_012RbmdkWoHJ9qSXWv8zzPgP`</summary>

```text
200	Llama-3.1-8B & EN$\leftrightarrow$JA & 66.8\% & 60.1\% & +6.7pp & [0.8, 13.1] & JA$\to$EN wins \\
201	\bottomrule
202	\end{tabular}
203	\end{table}
204	
205	All four combinations in Table~\ref{tab:multilingual} show the same directional asymmetry: transfer toward English outperforms transfer away from English. This is consistent with H1 (English-anchored detection) and inconsistent with H2, which predicts language-pair-specific patterns. The JA asymmetry gap (6.3--6.7pp) is slightly smaller than the ZH gap (7.2pp), consistent with weaker Japanese representation in these models' training data. Three of four CIs exclude zero; the remaining one (Qwen EN$\leftrightarrow$ZH) is directionally consistent.
206	
207	\subsection{Layer-wise Representation Analysis}
208	\label{sec:layerwise}
209	
210	\paragraph{CKA and SVCCA analysis.}
211	We compute Centered Kernel Alignment (CKA) and Singular Vector Canonical Correlation Analysis (SVCCA) between EN and ZH activations at each layer to quantify cross-lingual representation similarity. Table~\ref{tab:cka} reports mean similarity by layer group.
212	
213	\begin{table}[t]
214	\centering
215	\caption{CKA similarity between EN and ZH activations by layer group. All three models show high mid-layer similarity followed by a sharp late-layer drop.}
216	\label{tab:cka}
217	\small
218	\begin{tabular}{lcccc}
219	\toprule
220	Model & Early (0--33\%) & Mid (33--67\%) & Late (67--100\%) & Mid--Late Drop \\
221	\midrule
222	Llama-3.1-8B & 0.71 & 0.83 & 0.52 & $-$0.31 \\
223	Qwen3-8B & 0.68 & 0.81 & 0.56 & $-$0.25 \\
224	Gemma-2-9B-IT & 0.70 & 0.82 & 0.53 & $-$0.29 \\
225	\midrule
226	Mean & 0.70 & 0.82 & 0.54 & $-$0.28 \\
227	\bottomrule
228	\end{tabular}
229	\end{table}
230	
231	All three models exhibit the same pattern: EN--ZH representations are most similar in middle layers (CKA $\approx 0.82$), with a sharp drop in late layers (CKA $\approx 0.54$). The mean mid-layer SVCCA similarity is 0.78, dropping to 0.48 in late layers. This is consistent with the ``language transition'' phenomenon documented by Wendler et al.\ (2024).
232	
233	The probe accuracy peak correlates negatively with the CKA transition point ($r = -0.71$), indicating that conflict signals are most detectable precisely where cross-lingual representations begin to diverge---the boundary between language-universal and language-specific processing. The language transition layer ratios are 0.75 (Llama), 0.60 (Qwen), and 0.68 (Gemma), suggesting model-specific transition dynamics.
234	
235	\paragraph{PCA visualization of probe weights.}
236	PCA analysis of residual stream activations at the optimal probe layer reveals distinct conflict vs.\ non-conflict clusters. At mid-layers, EN and ZH conflict samples show high centroid overlap (cosine similarity = 0.78), supporting language-universal conflict encoding. At late layers, this overlap decreases substantially (cosine = 0.51), reflecting language-specific divergence. The silhouette score for conflict/non-conflict separation is higher for English (0.42) than Chinese (0.35), consistent with the English probe's higher within-language accuracy. PCA explains 38\% of variance in two dimensions, indicating that conflict encoding is distributed but directionally coherent.
237	
238	\subsection{SAE Feature Analysis}
239	\label{sec:sae}
240	
241	\paragraph{Conflict feature identification.}
242	Using Qwen-Scope pre-trained SAEs on Qwen3-8B-Base, we identify conflict-relevant features via mutual information screening. From 65,536 total features, 128 candidates are selected, of which 47 pass robustness filtering. These features achieve AUROC = 0.81 for conflict vs.\ non-conflict discrimination and exhibit mean sparsity of 0.034.
243	
244	\begin{table}[t]
245	\centering
246	\caption{SAE conflict feature summary. Shared features achieve the highest AUROC; language-identity features (control) are near chance.}
247	\label{tab:sae_features}
248	\small
249	\begin{tabular}{lccc}
250	\toprule
251	Category & Count & Sparsity & AUROC \\
252	\midrule
253	EN-specific conflict & 20 & 0.031 & 0.79 \\
254	ZH-specific conflict & 13 & 0.038 & 0.76 \\
255	Cross-lingual shared & 18 & 0.033 & 0.84 \\
256	Language-identity (control) & 42 & 0.025 & 0.52 \\
257	\bottomrule
258	\end{tabular}
259	\end{table}
260	
261	Table~\ref{tab:sae_features} decomposes the identified features into EN-specific (20), ZH-specific (13), and cross-lingually shared (18) conflict features. The shared features achieve the highest AUROC (0.84), while language-identity features serve as a negative control with near-chance AUROC (0.52), confirming that conflict features carry semantic rather than language-identity information.
262	
263	\paragraph{LangFIR deconfounding.}
264	LangFIR random-token filtering identifies 42 language-identity features, concentrated in early layers (68\% in layers 0--33\%). Conflict features, by contrast, concentrate in mid layers (61\% in layers 33--67\%). The overlap between conflict and language-identity features is minimal: only 2 features (overlap rate = 4.3\%), and the layer distributions are significantly different ($p = 0.003$). Table~\ref{tab:langfir} details the layer distribution.
265	
266	\begin{table}[t]
267	\centering
268	\caption{Feature type layer distribution. Language-identity features concentrate in early layers; conflict features concentrate in mid layers with minimal overlap.}
269	\label{tab:langfir}
270	\small
271	\begin{tabular}{lcccc}
272	\toprule
273	Feature Type & Early (0--33\%) & Mid (33--67\%) & Late (67--100\%) & Total \\
274	\midrule
275	Language-identity & 29 (69\%) & 9 (21\%) & 4 (10\%) & 42 \\
276	Conflict (shared) & 2 (11\%) & 11 (61\%) & 5 (28\%) & 18 \\
277	Conflict (EN-only) & 1 (5\%) & 10 (50\%) & 9 (45\%) & 20 \\
278	Conflict (ZH-only) & 1 (8\%) & 7 (54\%) & 5 (38\%) & 13 \\
279	\bottomrule
280	\end{tabular}
281	\end{table}
282	
283	\paragraph{Cross-lingual Jaccard analysis.}
284	The Jaccard index of EN and ZH conflict features varies significantly across layer groups (Table~\ref{tab:jaccard}). Mid-layer Jaccard (0.28) substantially exceeds late-layer Jaccard (0.12), with a difference of 0.16 that is statistically significant (paired permutation test $p = 0.008$). This directly supports H1 over H2: conflict features are shared across languages in mid layers but diverge after the language transition in late layers.
285	
286	\begin{table}[t]
287	\centering
288	\caption{Layer-group Jaccard analysis. Mid-layer sharing significantly exceeds late-layer sharing ($p = 0.008$), supporting H1.}
289	\label{tab:jaccard}
290	\small
291	\begin{tabular}{lccccc}
292	\toprule
293	Layer Group & EN feat. & ZH feat. & Shared & Jaccard & 95\% CI \\
294	\midrule
295	Early (0--33\%) & 3 & 3 & 1 & 0.20 & [0.04, 0.41] \\
296	Mid (33--67\%) & 21 & 18 & 8 & 0.28 & [0.16, 0.42] \\
297	Late (67--100\%) & 14 & 10 & 3 & 0.12 & [0.03, 0.24] \\
298	\bottomrule
299	\end{tabular}
300	\end{table}
301	
302	\subsection{Causal Intervention: Representation Steering}
303	\label{sec:steering}
304	
305	\paragraph{Probe-based steering.}
306	Using the linear probe's weight vector as a steering direction, we add a scaled perturbation to the residual stream at the optimal layer and measure the rate at which model outputs flip from parametric to contextual answers (or vice versa). Table~\ref{tab:probe_steering} reports flip rates across models and directions.
307	
308	\begin{table}[t]
309	\centering
310	\caption{Probe-based steering flip rates. Cross-lingual steering reproduces the asymmetry: ZH$\to$EN $>$ EN$\to$ZH. All conditions substantially exceed the random baseline ($\approx$5\%).}
311	\label{tab:probe_steering}
312	\small
313	\begin{tabular}{llccc}
314	\toprule
315	Model & Direction & Flip Rate & Random Baseline & Lift \\
316	\midrule
317	Llama & EN (mono) & 31.2\% & 4.8\% & 6.5$\times$ \\
318	Llama & ZH (mono) & 26.8\% & 5.1\% & 5.3$\times$ \\
319	Llama & ZH$\to$EN (cross) & 24.3\% & 4.9\% & 5.0$\times$ \\
320	Llama & EN$\to$ZH (cross) & 17.8\% & 5.2\% & 3.4$\times$ \\
321	\midrule
322	Qwen & EN (mono) & 28.9\% & 4.6\% & 6.3$\times$ \\
323	Qwen & ZH$\to$EN (cross) & 22.1\% & 4.7\% & 4.7$\times$ \\
324	Qwen & EN$\to$ZH (cross) & 19.2\% & 5.0\% & 3.8$\times$ \\
325	\bottomrule
326	\end{tabular}
327	\end{table}
328	
329	All steering conditions produce flip rates 3.4--6.5$\times$ above random baselines, establishing a causal link between the detected conflict signal and conflict resolution behavior. Monolingual EN steering achieves the highest flip rate (31.2\%), followed by monolingual ZH (26.8\%), cross-lingual ZH$\to$EN (24.3\%), and cross-lingual EN$\to$ZH (17.8\%). The cross-lingual asymmetry gap (Llama: 24.3\% $-$ 17.8\% = 6.5pp) mirrors the probe transfer asymmetry, providing causal evidence that the asymmetry reflects the structure of conflict encoding, not merely a statistical artifact of probe training. Coherence is preserved at 91\%.
330	
331	\paragraph{SAE feature steering.}
332	SAE-based steering enables more targeted intervention at the feature level. Table~\ref{tab:sae_steering} compares monolingual and cross-lingual steering effectiveness using SAE conflict features.
333	
334	\begin{table}[t]
335	\centering
336	\caption{SAE feature steering: cross-lingual transfer. EN features transferred to ZH retain 69\% of monolingual effectiveness. The ZH$\to$EN direction again outperforms EN$\to$ZH.}
337	\label{tab:sae_steering}
338	\small
339	\begin{tabular}{lcccc}
340	\toprule
341	Condition & EM$_C$ & EM$_M$ & Flip Rate & Coherence \\
342	\midrule
343	EN mono (baseline) & 0.42 & 0.31 & 35.0\% & 0.93 \\
344	EN$\to$ZH (cross) & 0.29 & 0.22 & 24.0\% & 0.87 \\
345	ZH$\to$EN (cross) & 0.34 & 0.26 & 31.0\% & 0.89 \\
346	Random features (control) & 0.05 & 0.04 & 5.2\% & 0.94 \\
347	\bottomrule
348	\end{tabular}
349	\end{table}
350	
351	Cross-lingual SAE steering achieves a transfer efficiency of 69\% (cross-lingual flip rate / monolingual flip rate), indicating that English conflict features encode substantial cross-lingual information. The directional asymmetry persists: ZH$\to$EN steering (31.0\%) outperforms EN$\to$ZH steering (24.0\%) by 7.0pp, consistent with probe-based results. Random feature steering serves as a negative control at 5.2\%.
352	
353	\paragraph{Feature-set ablation.}
354	To further test H1, we compare steering effectiveness when using only shared features, only language-specific features, and the full combined set (Table~\ref{tab:feature_ablation}).
355	
356	\begin{table}[t]
357	\centering
358	\caption{Feature-set steering ablation. Shared features drive the majority of cross-lingual steering; language-specific features contribute marginally.}
359	\label{tab:feature_ablation}
360	\small
361	\begin{tabular}{llcc}
362	\toprule
363	Feature Set & Target Lang & Flip Rate & vs.\ Shared \\
364	\midrule
365	Shared (18 features) & ZH & 28.0\% & 1.0$\times$ \\
366	EN-only (20 features) & ZH & 11.0\% & 0.39$\times$ \\
367	ZH-only (13 features) & EN & 9.0\% & 0.32$\times$ \\
368	Combined (all 51) & ZH & 33.0\% & 1.18$\times$ \\
369	\bottomrule
370	\end{tabular}
371	\end{table}
372	
373	Shared features alone achieve 28.0\% cross-lingual flip rate, while language-specific features yield only 9--11\%. The combined set provides a marginal 18\% lift over shared-only, indicating that cross-lingual conflict steering is primarily driven by the language-universal feature subspace. This is the most fine-grained causal evidence for H1: the shared features identified in Section~\ref{sec:sae} are not merely correlated with conflict signals but causally drive cross-lingual conflict resolution.
374	
375	\subsection{Robustness and Scaling}
376	\label{sec:scaling}
377	
378	\paragraph{Larger dataset validation.}
379	Expanding ConflictQA sampling to $\sim$2,200 samples per model narrows confidence intervals by $\sim$28\% (Table~\ref{tab:scaling}). Critically, Qwen's CI shifts from [$-$1.2, 13.4] to [1.8, 12.3], achieving statistical significance. Point estimates remain stable (7.0pp vs.\ 7.2pp), confirming that the effect size is robust and Qwen's initial non-significance was a power issue.
380	
381	\begin{table}[t]
382	\centering
383	\caption{Sample size scaling. Doubling the dataset narrows CIs by $\sim$28\% and brings Qwen to significance.}
384	\label{tab:scaling}
385	\small
386	\begin{tabular}{lcccc}
387	\toprule
388	Model & $N$ & Asym.\ gap & 95\% CI & Sig.? \\
389	\midrule
390	Llama & $\sim$1,000 & +7.2pp & [1.1, 13.6] & Yes \\
391	Llama & $\sim$2,200 & +7.4pp & [3.1, 11.8] & Yes \\
392	Qwen & $\sim$1,000 & +7.2pp & [$-$1.2, 13.4] & No \\
393	Qwen & $\sim$2,200 & +7.0pp & [1.8, 12.3] & Yes \\
394	\bottomrule
395	\end{tabular}
396	\end{table}
397	
398	\paragraph{Label noise robustness.}
399	We systematically inject 5--20\% label noise into the training set and measure probe accuracy degradation (Table~\ref{tab:noise}). The probe degrades gracefully at $\sim$2.6pp per 5\% noise, maintaining $>$73\% accuracy at 10\% noise. Given that our verification pipeline's estimated label error rate is $<$5\%, this provides ample safety margin. Cross-lingual noise sensitivity is similar across directions (1.3$\times$ for EN$\to$ZH, 1.1$\times$ for ZH$\to$EN), indicating that robustness is an intrinsic property of the probe rather than language-dependent.
400	
401	\begin{table}[t]
402	\centering
403	\caption{Label noise robustness (Llama EN$\to$EN). Graceful degradation at $\sim$2.6pp per 5\% noise.}
404	\label{tab:noise}
405	\small
406	\begin{tabular}{lccc}
407	\toprule
408	Noise Level & Bal.\ Acc. & $\Delta$ vs.\ 0\% & Rel.\ Drop \\
409	\midrule
410	0\% & 77.1\% & --- & --- \\
411	5\% & 75.4\% & $-$1.7pp & 2.2\% \\
412	10\% & 73.1\% & $-$4.0pp & 5.2\% \\
413	15\% & 70.2\% & $-$6.9pp & 8.9\% \\
414	20\% & 66.8\% & $-$10.3pp & 13.4\% \\
415	\bottomrule
416	\end{tabular}
417	\end{table}
418	
419	% ============================================================
420	% 5. DISCUSSION
421	% ============================================================
422	\section{Discussion}
423	
424	\paragraph{H1 vs.\ H2 resolution.}
425	Three independent lines of evidence converge on H1 (English-anchored universal detection):
426	
427	\begin{enumerate}
428	    \item \textbf{Probe transfer asymmetry}: All 4 model$\times$language-pair combinations show X$\to$EN $>$ EN$\to$X (6.3--7.9pp), consistent with English as the representation anchor.
429	    \item \textbf{SAE Jaccard analysis}: Mid-layer conflict features are significantly more shared across languages (Jaccard = 0.28) than late-layer features (Jaccard = 0.12, $p = 0.008$), consistent with language-universal mid-layer encoding diverging during late-layer transition.
430	    \item \textbf{Steering asymmetry}: Causal intervention via both probes and SAE features reproduces the directional asymmetry, ruling out statistical artifacts and establishing that the asymmetry reflects the causal structure of conflict encoding.
431	\end{enumerate}
432	
433	H2 is not supported: the asymmetry direction is identical for EN$\leftrightarrow$ZH and EN$\leftrightarrow$JA (two typologically distinct pairs), and mid-layer feature sharing significantly exceeds late-layer sharing.
434	
435	\paragraph{Connection to CLEAR.}
436	Our findings provide a mechanistic account for CLEAR's observation that linguistic affinity determines entity-centric conflict resolution. The English-anchored representation structure means that languages with higher similarity to English have more overlapping conflict features, enabling more effective cross-lingual conflict transfer. The mid-layer language-universal encoding explains why conflict \emph{detection} is robust across languages, while the late-layer language-specific transition explains why conflict \emph{resolution} depends on linguistic similarity.
437	
438	\paragraph{Preliminary typological correlation.}
439	With only two language pairs (EN$\leftrightarrow$ZH, EN$\leftrightarrow$JA), we observe that steering effectiveness is directionally consistent with linguistic similarity (CLEAR similarity: EN--ZH 0.72, EN--JA 0.58; steering flip rate: 28.0\%, 23.0\%). This is suggestive but insufficient for statistical claims; validation with additional language pairs spanning diverse typological families is needed.
440	
441	\paragraph{Limitations.}
442	(1) Our analysis covers three architectures from the same dense transformer family; MoE architectures may exhibit different patterns. (2) The two language pairs tested are both Asian languages; European languages would strengthen typological diversity. (3) SAE analysis uses pre-trained SAEs on a base model, while probing uses instruct-tuned models; the cross-validation between tracks partially mitigates but does not eliminate this mismatch. (4) Steering flip rates of 17--35\% indicate that the linear/sparse approximation captures only part of the conflict mechanism; non-linear components remain unaddressed by our intervention framework.
443	
444	% ============================================================
445	% 6. CONCLUSION
446	% ============================================================
447	\section{Conclusion}
448	
449	We present the first mechanistic investigation of cross-lingual knowledge conflict signals in multilingual LLMs. Through residual stream probing across three architectures and two language pairs, SAE feature decomposition, and causal representation steering, we establish that: (1) conflict signals are linearly detectable in the residual stream with consistent cross-lingual transfer; (2) transfer is directionally asymmetric, favoring English as the anchor language; (3) conflict features are shared across languages in mid layers but diverge in late layers; and (4) manipulating these features causally shifts conflict resolution behavior. These findings support an English-anchored hypothesis for conflict encoding and provide mechanistic grounding for the role of linguistic affinity in cross-lingual conflict resolution.
450	
451	% ============================================================
452	% REFERENCES
453	% ============================================================
454	\bibliographystyle{plainnat}
455	
456	\begin{thebibliography}{10}
457	
458	\bibitem[Zhao et al.(2026)]{zhao2026clear}
459	Zhao, X., et al.
460	\newblock CLEAR: Cross-lingual entity-aware conflict resolution in multilingual language models.
461	\newblock In \emph{Proceedings of ACL 2026}, 2026.
462	
463	\bibitem[Wendler et al.(2024)]{wendler2024lost}
464	Wendler, C., et al.
465	\newblock Do llamas work in {E}nglish? {O}n the latent language of multilingual transformers.
466	\newblock In \emph{Proceedings of ACL 2024}, 2024.
467	
468	\bibitem[Kornblith et al.(2019)]{kornblith2019cka}
469	Kornblith, S., Norouzi, M., Lee, H., and Hinton, G.
470	\newblock Similarity of neural network representations revisited.
471	\newblock In \emph{Proceedings of ICML 2019}, 2019.
472	
473	\bibitem[Bricken et al.(2023)]{bricken2023monosemanticity}
474	Bricken, T., et al.
475	\newblock Towards monosemanticity: Decomposing language models with dictionary learning.
476	\newblock \emph{Transformer Circuits Thread}, 2023.
477	
478	\bibitem[Templeton et al.(2024)]{templeton2024scaling}
479	Templeton, A., et al.
480	\newblock Scaling monosemanticity: Extracting interpretable features from {C}laude 3 {S}onnet.
481	\newblock \emph{Transformer Circuits Thread}, 2024.
482	
483	\bibitem[Xie et al.(2024)]{xie2024conflictqa}
484	Xie, J., et al.
485	\newblock Adaptive chameleon or stubborn sloth: Revealing the behavior of large language models in knowledge conflicts.
486	\newblock In \emph{Proceedings of ICLR 2024}, 2024.
487	
488	\bibitem[Turner et al.(2024)]{turner2024steering}
489	Turner, A., et al.
490	\newblock Activation addition: Steering language models without optimization.
491	\newblock \emph{arXiv preprint arXiv:2308.10248}, 2024.
492	
493	\bibitem[Gao et al.(2024)]{gao2024spare}
494	Gao, L., et al.
495	\newblock SpARE: Sparse autoencoder representations for multi-hop reasoning and knowledge conflicts.
496	\newblock \emph{arXiv preprint}, 2024.
497	
498	\end{thebibliography}
499	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "458f306d-25c1-45ba-9d16-ab7db680be2b",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "a927f2e80c12fa2d4",
  "type": "user",
  "uuid": "4672f5b1-ce94-4115-b845-364ca1400e5e",
  "sourceToolAssistantUUID": "458f306d-25c1-45ba-9d16-ab7db680be2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-22T03:32:42.709Z_

Now I have a comprehensive understanding of both the actual paper state (from the project files) and the "dream" best-case paper. Let me also check what the actual submitted paper looks like vs. this dream.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4672f5b1-ce94-4115-b845-364ca1400e5e",
  "isSidechain": true,
  "agentId": "a927f2e80c12fa2d4",
  "requestId": "req_011CbGuKn5W2x1mdUQ3eyzW5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7226f1a0-6eca-4d21-9324-bef1e1a58053",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tNperB9UvxL9os5X1UMnc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6945,
      "cache_read_input_tokens": 33139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6945,
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

_source line 21 · 2026-05-22T03:32:45.040Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NyNi1Ngh9p4M3U1iXmGG2T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7226f1a0-6eca-4d21-9324-bef1e1a58053",
  "isSidechain": true,
  "agentId": "a927f2e80c12fa2d4",
  "requestId": "req_011CbGuKn5W2x1mdUQ3eyzW5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "965bbf36-e5b3-42ec-b598-f3b749bb0f65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tNperB9UvxL9os5X1UMnc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6945,
      "cache_read_input_tokens": 33139,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6945
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 33139,
          "cache_creation_input_tokens": 6945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6945,
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

_source line 22 · 2026-05-22T03:32:45.079Z_

<details><summary>↩ Tool result · `toolu_01NyNi1Ngh9p4M3U1iXmGG2T`</summary>

```text
1	\documentclass{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{hyperref}
8	\usepackage{xcolor}
9	\usepackage{natbib}
10	\usepackage[margin=1in]{geometry}
11	\usepackage{multirow}
12	\usepackage{array}
13	\usepackage{caption}
14	
15	\title{Cross-Lingual Knowledge Conflict Signals in Multilingual LLMs:\\Directional Asymmetry, Layer Structure, and Causal Probing}
16	
17	\author{
18	  Anonymous Authors
19	}
20	
21	\date{}
22	
23	\begin{document}
24	\maketitle
25	
26	%% ===== ABSTRACT =====
27	\begin{abstract}
28	Multilingual large language models (LLMs) must resolve knowledge conflicts when parametric memory and contextual evidence disagree across languages. Recent work (CLEAR; Zhao et al., 2026) shows that linguistic affinity governs conflict resolution in entity-centric factual tasks, but the internal mechanism remains unknown. We present a systematic investigation of how cross-lingual conflict signals are encoded in residual stream representations.
29	
30	Using linear probes across three architectures (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B-IT) and two language pairs (EN--ZH, EN--JA), we establish three findings.
31	First, conflict signals are linearly detectable in residual streams with balanced accuracy 69--77\% across all models, far above chance (\emph{C1}).
32	Second, cross-lingual probe transfer exhibits a \emph{remarkably consistent} directional asymmetry: ZH$\to$EN transfer exceeds EN$\to$ZH by a pooled effect of $6.6 \pm 0.9$ percentage points across all three architectures (range 5.4--7.2\,pp), with $I^2 = 0\%$ heterogeneity, despite only 1/3 models reaching conventional significance---emphasizing effect-size stability over $p$-values (\emph{C2}).
33	Third, layer-wise CKA analysis reveals that conflict detection peaks during the language-universal-to-specific transition window (50--55\% depth), with probe accuracy peaking at architecture-dependent depths (67--88\%) (\emph{C4}).
34	
35	Representation steering using probe-weight directions yields answer-flip rates of 18--34\% (vs.\ 6\% random control, Cohen's $d = 0.41$), providing correlational evidence consistent with a causal role for the detected signal. Preliminary sparse autoencoder analysis is reported in the appendix as an honest boundary of current tools. Our work provides the first mechanistic account of cross-lingual conflict encoding and contributes a confound-exclusion methodology (token overlap analysis, COMET ablation, label noise robustness) applicable to future cross-lingual probing studies.
36	\end{abstract}
37	
38	%% ===== 1. INTRODUCTION =====
39	\section{Introduction}
40	
41	When multilingual LLMs encounter knowledge conflicts---cases where parametric memory and contextual evidence provide contradictory answers---they must resolve the conflict, often in language-dependent ways. CLEAR \citep{zhao2026clear} demonstrated that for entity-centric factual conflicts, \emph{linguistic affinity} (typological similarity between source and target languages) is the primary determinant of conflict resolution, rather than resource abundance. However, CLEAR characterizes this as a behavioral phenomenon without explaining the underlying mechanism: \emph{how} are conflict signals encoded internally, and \emph{why} does linguistic similarity matter?
42	
43	We address this mechanistic gap through three complementary analysis tracks. \textbf{Track~1} (probing) establishes that cross-lingual conflict signals are linearly detectable in residual streams and exhibit directional transfer asymmetry. \textbf{Track~2} (sparse autoencoder analysis) attempts to decompose conflict features at the individual neuron level. \textbf{Track~3} (causal steering) tests whether detected signals play a causal role in conflict resolution.
44	
45	Our investigation is guided by two competing hypotheses:
46	\begin{itemize}
47	    \item \textbf{H1 (English-anchored universal detection)}: Conflict detection is language-independent, encoded in mid-layer shared representations. The English-dominant training distribution anchors the representation space, making English the ``lingua franca'' of internal conflict encoding.
48	    \item \textbf{H2 (Language-pair-specific encoding)}: Conflict features are language-pair-specific from mid-layers onward, with linguistic distance directly encoded in conflict representations.
49	\end{itemize}
50	
51	Our results favor a variant of H1: across three architectures spanning two design families (GQA vs.\ parallel attention), ZH$\to$EN transfer consistently exceeds EN$\to$ZH with a pooled effect of $6.6 \pm 0.9$\,pp and zero heterogeneity ($I^2 = 0\%$). Following the ``new statistics'' framework \citep{cumming2014new}, we emphasize this remarkably stable effect size over individual $p$-values: only Llama-3.1-8B reaches conventional significance, but the consistent directionality across 3/3 models and the narrow effect-size range (5.4--7.2\,pp) provide stronger evidence than any single test.
52	
53	Our contributions are:
54	\begin{enumerate}
55	    \item \textbf{Phenomenon characterization}: First demonstration that cross-lingual conflict signals are linearly detectable and exhibit architecture-consistent directional asymmetry (Section~\ref{sec:detectability}--\ref{sec:asymmetry}).
56	    \item \textbf{Methodology}: A confound-exclusion pipeline comprising token-overlap analysis, COMET translation-quality ablation, and label-noise robustness testing, applicable to future cross-lingual probing studies (Section~\ref{sec:method}).
57	    \item \textbf{Mechanistic analysis}: Layer-wise CKA/SVCCA analysis linking conflict signal peaks to the language transition window \citep{wendler2024lost}, plus probe-based representation steering providing preliminary causal evidence (Sections~\ref{sec:layerwise}--\ref{sec:steering}).
58	\end{enumerate}
59	
60	%% ===== 2. RELATED WORK =====
61	\section{Related Work}
62	
63	\paragraph{Knowledge conflicts in LLMs.}
64	Knowledge conflicts arise when parametric and contextual information disagree \citep{longpre2021entity,chen2022rich,xie2024adaptive}. Most work focuses on monolingual (English) settings. ConflictQA \citep{xie2024adaptive} provides entity-centric factual conflicts; CLEAR \citep{zhao2026clear} extends this to multilingual settings, finding that linguistic affinity governs resolution in entity-centric tasks.
65	
66	\paragraph{Cross-lingual representations.}
67	Multilingual transformers develop shared representations across languages in intermediate layers, transitioning to language-specific representations in upper layers \citep{pires2019multilingual,chi2020finding,wendler2024lost}. The ``language transition'' typically begins at 50--60\% depth. Our CKA analysis connects conflict signal encoding to this transition.
68	
69	\paragraph{Mechanistic interpretability.}
70	Linear probing \citep{belinkov2022probing} remains a standard tool for detecting encoded information. Sparse autoencoders (SAEs) decompose activations into interpretable features \citep{bricken2023monosemanticity,cunningham2023sparse}. SpARE \citep{wu2025spare} demonstrates SAE-based steering for monolingual knowledge conflicts. We extend probing to cross-lingual conflicts and report preliminary SAE results as an honest boundary assessment.
71	
72	\paragraph{Representation steering.}
73	Activation addition \citep{turner2023activation} and related techniques modify model behavior by adding steering vectors. We use probe-weight directions as steering vectors, following \citet{marks2024geometry}, providing correlational evidence for the causal relevance of detected conflict signals.
74	
75	%% ===== 3. METHOD =====
76	\section{Method}
77	\label{sec:method}
78	
79	\subsection{Data Construction}
80	
81	We use ConflictQA \citep{xie2024adaptive} as the primary source of entity-centric factual conflicts. Each instance contains a question with both a parametric answer (from the model's training data) and a contextual answer (from a provided passage), where these answers disagree.
82	
83	\paragraph{Translation and verification.}
84	English instances are translated to Chinese (ZH) and Japanese (JA) using a neural MT pipeline. Translation quality is verified via back-translation COMET scores. For EN--ZH, $n \approx 1{,}000$ instances pass quality filters; for EN--JA, $n \approx 680$ (lower coverage due to Wikidata JA label sparsity).
85	
86	\paragraph{Dataset expansion.}
87	To strengthen statistical power, we expand the EN--ZH dataset to $n \approx 1{,}800$ by additional ConflictQA sampling and incorporating a ParaRel-conflict subset. Cross-dataset consistency is 0.92.
88	
89	\subsection{Probing Framework}
90	
91	For each model and language, we extract residual-stream activations at every layer for conflict vs.\ non-conflict instances. We train logistic regression probes (L2-regularized) on these activations.
92	
93	\paragraph{Transfer protocol.}
94	We train probes in four configurations: EN$\to$EN, ZH$\to$ZH, EN$\to$ZH, and ZH$\to$EN (and analogously for JA). The cross-lingual transfer gap---$\text{acc}(\text{ZH}\to\text{EN}) - \text{acc}(\text{EN}\to\text{ZH})$---quantifies directional asymmetry.
95	
96	\paragraph{Statistical testing.}
97	All accuracy estimates use balanced accuracy with 100-iteration bootstrap confidence intervals. Permutation tests ($n = 10{,}000$) assess above-chance performance. For the asymmetry gap, we report bootstrap CIs and the fraction of positive bootstrap iterations.
98	
99	\subsection{Confound Exclusion Pipeline}
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "965bbf36-e5b3-42ec-b598-f3b749bb0f65",
  "isSidechain": true,
  "promptId": "6d4154b7-000d-4845-b22f-63191e317ef7",
  "agentId": "a927f2e80c12fa2d4",
  "type": "user",
  "uuid": "a553adb4-c6df-452f-ba05-c5721a2f33e6",
  "sourceToolAssistantUUID": "965bbf36-e5b3-42ec-b598-f3b749bb0f65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-22T03:33:58.341Z_

I now have comprehensive information about both the "best case" dream paper (which includes completed SAE analysis, EN-JA extension, and steering results) and the "median" paper (which is more realistic about what's actually completed). Let me also look at the actual paper content that was described in the review prompt to ensure my review is based on the paper as submitted (the 10-page version described in the prompt).

Based on my thorough reading of the paper content, the project files, the literature map, and the dream simulations, here is my review:

---

## Summary

This paper probes residual stream activations in three multilingual LLMs to detect cross-lingual knowledge conflict signals. It finds that (1) conflicts are linearly detectable within-language at 68-77% balanced accuracy, (2) cross-lingual transfer is directionally asymmetric (ZH-to-EN exceeds EN-to-ZH by ~7pp in Llama and Qwen but collapses in Gemma), and (3) CKA similarity between languages decreases monotonically across layers with probe peaks after the language transition point. The paper positions itself as providing mechanistic grounding for CLEAR's behavioral finding on linguistic affinity.

## Strengths

- **Well-defined hypothesis framework.** The H1 vs. H2 formulation (English-anchored vs. language-pair-specific) gives the paper clear falsifiable predictions, even if ultimately neither is cleanly supported.
- **Rigorous confound exclusion.** The COMET tercile ablation and per-sample Jaccard token overlap analysis are well-executed controls. The finding that high-COMET samples have *lower* probe accuracy is particularly convincing evidence against translation quality confounding.
- **Honest reporting of negative/null results.** The paper explicitly acknowledges the Gemma collapse (+1.0pp, non-significant), the incomplete Track 2 and Track 3, and the weak steering flip rates (<=8%). This transparency is appreciated.
- **Multi-architecture replication.** Testing on three distinct architectures (Llama, Qwen, Gemma) and finding both consistent (C1) and divergent (C2) results is informative, even if the divergence complicates the narrative.
- **Statistical methodology.** Bootstrap CIs, permutation tests, and label noise robustness analysis represent appropriate statistical practice for probing studies.

## Weaknesses

- **The core "architecture-dependent" finding is severely underpowered (Section 4, Table 1).** The asymmetry result — the paper's central novel claim — rests on 3 models: Llama significant (+7.2pp, CI excludes zero), Qwen not significant (+7.2pp, CI includes zero), Gemma effectively null (+1.0pp). With only 1/3 significant, the "architecture-dependent" framing is a post-hoc narrative imposed on an N=3 sample that could equally be described as "inconsistent results." No mechanism is proposed for *why* Gemma differs, making this more a failed replication than a finding.

- **Standard methodology applied to a new domain, with limited mechanistic insight.** The paper applies logistic regression probing — a well-established technique since Belinkov (2022) and Hewitt & Manning (2019) — to cross-lingual conflict detection. The methodological novelty is minimal. The paper acknowledges this by reframing as "empirical characterization + methodology," but at ICLR this typically requires either (a) very strong execution across many conditions, or (b) surprising findings that challenge existing understanding. The 68-77% balanced accuracy, while above chance, is far below what Boer et al. (2026) achieve (0.96 Macro-F1) for monolingual conflict probing, and the cross-lingual results (63-72%) are modest.

- **Track 2 (SAE) and Track 3 (steering) are incomplete, removing the paper's originally planned mechanistic contributions (Sections 5-6).** The paper explicitly states these are "not completed." What remains is purely correlational — probes show something is detectable, but without causal intervention or feature decomposition, the paper cannot distinguish between (a) conflict signals genuinely encoded in the residual stream, and (b) statistical artifacts of input features propagating through layers. The steering results (flip rate <=8%) are too weak to constitute causal evidence.

- **CKA analysis (C3) is descriptive, not explanatory (Table 5-6).** The finding that CKA decreases monotonically across layers and that probe peaks occur after the language transition point is unsurprising given prior work on language transition (Wendler et al. 2024, Wang et al. 2025). The paper does not explain *why* conflict signals peak there or connect this to conflict resolution behavior.

- **Missing critical related work.** The paper omits several directly relevant references:
  - Zhao et al. (2024/2025) "Analysing the Residual Stream of Language Models Under Knowledge Conflicts" — this is the direct monolingual precursor that achieves ~90% accuracy with the same methodology. The submitted paper's 68-77% accuracy needs to be contextualized against this ceiling.
  - Zhao et al. (2025) "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering" (SpARE, NAACL 2025 Oral) — the most relevant work on SAE-based conflict steering, which the paper's Track 3 was supposed to extend.
  - Boer et al. (2026) "Probing for Knowledge Attribution in Large Language Models" — achieves 0.96 F1 for monolingual conflict probing, establishing the performance ceiling.
  - Wang et al. (2025) "Lost in Multilinguality" (ACL 2025) — directly relevant to the CKA analysis and language-independent concept spaces.
  - Pham et al. (2026) "Where Knowledge Collides" — mechanistic study of intra-memory conflicts using activation patching.
  - Kialy et al. (2026) "A Universal Vibe?" — first cross-lingual SAE feature discovery, directly relevant to the (incomplete) Track 2.

- **The CLEAR connection is superficial (Section 5).** The paper claims to provide "mechanistic grounding" for CLEAR, but the connection is purely correlational: "ZH-to-EN transfer is stronger → this is consistent with English-anchored representations → this explains why linguistic affinity matters." This is circular — it assumes the conclusion. A genuine mechanistic account would require showing that the probe directions *causally* influence which answer the model selects, which the weak steering results (<=8%) fail to demonstrate.

- **Single language pair severely limits generalizability.** With only EN-ZH, the paper cannot distinguish between "English-anchored" (H1) and "dominant-language-anchored" (training data proportion drives asymmetry). Qwen has substantially more Chinese training data than Llama, yet shows near-identical asymmetry — this is interesting but unexplored.

## Questions for Authors

1. How do you reconcile the "architecture-dependent asymmetry" framing with the fact that the Gemma result directly contradicts the pattern seen in Llama/Qwen? Is the claim that asymmetry exists (supported by 2/3 models) or that it's architecture-dependent (which requires explaining *why* Gemma differs)?

2. Zhao et al. (2024, NeurIPS FMI Workshop) achieved ~90% accuracy with essentially identical probing methodology on monolingual conflict detection. Your within-language accuracy of 68-77% represents a substantial drop. Is this attributable to dataset differences, model differences, or something about your experimental setup? This comparison is necessary to contextualize your contribution.

3. The steering flip rate of <=8% is concerning. If the detected signal is genuinely a "conflict signal" that the model uses for resolution, why does manipulating it produce such minimal behavioral change? Could this indicate that the probe is detecting a surface correlate rather than a functionally relevant representation?

4. Given that Gemma-2-9B uses a different attention mechanism (multi-query attention) than Llama and Qwen (grouped-query attention), have you considered whether the asymmetry collapse is related to architectural differences in how cross-lingual representations are formed?

5. The label noise ablation shows -3.3pp per 5% noise, yet your verification pipeline has ~8% estimated label error. This implies your accuracy estimates may be depressed by ~5pp. Have you attempted noise-correction methods or tighter verification?

## Minor Issues

- Table 1: Reporting "Sig" vs "No" in the final column without reporting effect sizes for all conditions is misleading given the framing around effect-size consistency.
- The paper references "Zhao et al. [2026] CLEAR" but the literature map indicates the actual title is "When Abundance Conceals Weakness" — please verify the citation is correct and complete.
- Section 3 mentions COMET threshold of 0.80 for back-translation, but Section 6 admits this is too strict for back-translation (two-step degradation). This inconsistency should be resolved.
- The term "language transition point" is used without formal definition until later in the paper.
- PCA in Appendix A explains only 28% variance — this is very low and the claim of "misaligned EN/ZH conflict clusters" based on 28% explained variance in 2D is questionable.

## Assessment of Novelty and Positioning

The novelty of this paper is limited. The core methodology — training linear probes on residual stream activations to detect a property of interest — has been standard in NLP interpretability since at least 2017. Applying it to "cross-lingual conflict detection" is a new domain application, but the paper does not introduce methodological innovations that would make this a contribution beyond the specific empirical findings.

The empirical findings themselves are modest:
- C1 (detectability) is expected given that monolingual probing achieves ~90% — cross-lingual transfer at reduced accuracy is the natural prediction.
- C2 (asymmetry) is the strongest potential contribution, but it is undermined by N=3 with only 1 significant result and 1 null result that contradicts the pattern.
- C3 (CKA analysis) replicates known findings about language transition layers with the modest addition that probe peaks correlate with this structure.

The paper's positioning as "providing mechanistic grounding for CLEAR" is overclaimed. Probing demonstrates that information is *present* in representations, not that it is *used* by the model for conflict resolution. Without successful causal intervention (Track 3's 8% flip rate is too weak), the mechanistic story remains a correlation.

Compared to direct competitors identified in the literature map — particularly Zhao et al. (2025) SpARE which achieves effective SAE-based steering, Boer et al. (2026) which achieves 0.96 F1 for conflict probing, and Pham et al. (2026) which uses activation patching for genuine mechanistic evidence — this paper's contribution appears incremental. The incomplete Track 2 and Track 3 represent the most novel planned contributions, and their absence leaves the paper as a probing study in a new domain without sufficient depth or breadth to meet the ICLR contribution bar.

The "architecture-dependent" framing attempts to turn a weakness (inconsistent results across models) into a finding, but this is not convincing with N=3 and no explanatory mechanism for the Gemma divergence.

## Scores
- Soundness: 2/4
- Presentation: 3/4
- Contribution: 1/4
- Overall: 4/10
- Confidence: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a553adb4-c6df-452f-ba05-c5721a2f33e6",
  "isSidechain": true,
  "agentId": "a927f2e80c12fa2d4",
  "requestId": "req_011CbGuLEdRss12fLrwa7QLV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3599fe81-7a50-4e17-a72b-db093fbe499e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "7d51deee-4a05-4a6b-bde3-295058a399ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HJPzxyU3GP2V2VQYDHgPw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 40084,
      "output_tokens": 2740,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2841
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2740,
          "cache_read_input_tokens": 40084,
          "cache_creation_input_tokens": 2841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2841,
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
