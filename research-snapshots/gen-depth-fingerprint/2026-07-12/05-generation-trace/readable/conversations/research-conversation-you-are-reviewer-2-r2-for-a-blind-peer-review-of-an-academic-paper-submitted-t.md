# Research conversation: You are Reviewer 2 (R2) for a blind peer review of an academic paper submitted to AAAI 2027. Your focus areas are **Nove

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2d15da6165e8b28b.jsonl`
- **Structured JSON:** [`7a3b46216d3de87db660.json`](../../sessions/7a/7a3b46216d3de87db660.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-14T18:43:39.180Z_

You are Reviewer 2 (R2) for a blind peer review of an academic paper submitted to AAAI 2027. Your focus areas are **Novelty and Related Work**.

## AAAI Review Criteria
AAAI uses a 1-10 overall assessment scale. Acceptance rate ~23%. Dimensions: soundness, significance, novelty, clarity, relevance. The review form asks for a paper summary, strengths, weaknesses, questions for authors, and an overall score.

Scale:
- 10: Top 5%, seminal
- 9: Strong accept
- 8: Clear accept
- 7: Accept, good paper with minor weaknesses
- 6: Weak accept / borderline
- 5: Borderline / weak reject
- 4: Reject, below threshold
- 3: Clear reject
- 2: Strong reject
- 1: Trivial or wrong

## Paper Summary

**Title**: "Distributional Fingerprints of Generation Depth: Detecting Recursive LLM Contamination Beyond Binary Classification"

The paper introduces "distributional fingerprinting" for estimating the generation depth of text (gen-0/gen-1/gen-2+) by measuring distributional divergence from human text under a small reference LM. It tests two hypotheses about non-paraphrastic generation chains: convergence (H1) vs monotonic divergence (H2), confirming H2. A 7-feature classifier (5 reference-model entropy features + 2 surface features) with XGBoost achieves macro-F1=0.87 (3-class) and generalizes across 5 generators (leave-one-out F1=0.78). Depth-aware data filtering retains 42% data at near-human perplexity, outperforming binary baselines by 5.2%.

## Paper Structure and Claims
1. **Claim 1 (H2 confirmation)**: Non-paraphrastic generation chains exhibit monotonic distributional divergence, in contrast to convergence in paraphrastic chains (KS D=0.41, p<1e-4).
2. **Claim 2 (Cross-generator depth classification)**: Distributional fingerprint achieves macro-F1=0.87 (3-class), generalizes across 5 generator families with leave-one-out F1=0.78±0.03.
3. **Claim 3 (Risk-stratified data curation)**: Depth-aware filtering outperforms binary baselines by 5.2% in downstream perplexity while retaining 50% more training data.

## Related Work as presented in paper (Section 2)
Three areas covered:
1. **Synthetic text detection**: FastDetectGPT [Bao et al. 2024], SynthID-Text [Dathathri et al. 2024], LD-Score [Dugan et al. 2025] — all binary classifiers
2. **Model collapse and iterative retraining**: Shumailov et al. 2024 (Nature) — focuses on full-model retraining dynamics, not text-level depth estimation
3. **Attractor cycles in paraphrasing chains**: Briesch et al. 2025 (ACL) — proves 2-period convergence for paraphrastic chains

Only 5 references total in the paper.

## Key Methods
- 7 features: 5 reference-model entropy stats (mean, std, min, max, tail_decay) + 2 surface (TTR, hapax_ratio)
- Reference model: Pythia-410M (small pretrained LM never fine-tuned on synthetic data)
- Classifier: XGBoost with 5-fold stratified CV
- 12 experiments across 5 generators, 4 domains, 3 prompt types

## Your Task (R2: Novelty + Related Work)

Provide a detailed review focusing on:

1. **Novelty Assessment**: How novel is the core idea? Is distributional fingerprinting genuinely new, or is it a straightforward application of known techniques? How does the H1 vs H2 framing add value?
2. **Related Work Completeness**: Are there significant missing references? Is the positioning against prior work accurate and fair? Only 5 references seems very thin for a venue like AAAI.
3. **Contribution Significance**: Are the contributions substantial enough for AAAI? Does the paper advance the field meaningfully?
4. **Clarity and Presentation**: Is the paper well-written and well-organized?
5. **Positioning and Framing**: Does the paper correctly identify its place in the literature? Are claims appropriately scoped?

Think about what's missing from related work:
- Data contamination / benchmark contamination detection literature
- Membership inference attacks
- Watermarking beyond SynthID
- Training data attribution
- Distributional shift / domain adaptation (the entropy features are essentially OOD detection)
- Model collapse theory beyond Shumailov et al.
- Other iterative generation studies
- Perplexity-based detection methods (DetectGPT, DNA-GPT, etc.)
- Data quality scoring / data selection literature

Format your review as:

### Paper Summary (2-3 sentences)
### Strengths (bulleted)
### Weaknesses (bulleted)
### Questions for Authors (bulleted)
### Missing Related Work
### Scores
- Novelty: X/10
- Related Work: X/10
- Significance: X/10
- Clarity: X/10
- Overall (Novelty+Related Work focus): X/10
- Confidence: X/5


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "01b0c602-1faf-4219-9386-84230e546cb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T18:43:39.182Z_

```json
{
  "parentUuid": "01b0c602-1faf-4219-9386-84230e546cb3",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
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
  "uuid": "22018085-d460-4313-aa2b-2486c994f832",
  "timestamp": "2026-05-14T18:43:39.182Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T18:43:42.400Z_



I'll start by reading the paper and related project files to form a thorough assessment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22018085-d460-4313-aa2b-2486c994f832",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xKhMYCnWiZ5bUvqshk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70490e6c-644f-4526-baab-caf94b8c9802",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZPjd4MBcAh76ZEcdpzsbw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7144,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7144,
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

_source line 4 · 2026-05-14T18:43:42.775Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Sgp5qvTWtkryx1VtQQMfSm`</summary>

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
  "parentUuid": "70490e6c-644f-4526-baab-caf94b8c9802",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xKhMYCnWiZ5bUvqshk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76ccc0ba-dbd1-41aa-ab41-4c4fcad99dfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZPjd4MBcAh76ZEcdpzsbw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7144,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7144,
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

_source line 5 · 2026-05-14T18:43:42.778Z_

<details><summary>↩ Tool result · `toolu_01Sgp5qvTWtkryx1VtQQMfSm`</summary>

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
  "parentUuid": "76ccc0ba-dbd1-41aa-ab41-4c4fcad99dfd",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "dfb4efda-d716-431d-81e8-c3725dc676fc",
  "sourceToolAssistantUUID": "76ccc0ba-dbd1-41aa-ab41-4c4fcad99dfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T18:43:45.830Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01Jp84kZi8RY3u4dTFwDLdt9`</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfb4efda-d716-431d-81e8-c3725dc676fc",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xKy9ocvt2wf3i2xkP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6917ae0-5d20-47d5-b51c-2ebf8928802c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019irzVaDBmdyYpazA6zRiJ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 7 · 2026-05-14T18:43:45.854Z_

<details><summary>↩ Tool result · `toolu_01Jp84kZi8RY3u4dTFwDLdt9`</summary>

```text
{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (6 个)\n\n- **plan-001**: ALLOCATED — \n- **mvp-001**: DONE (success) — \n- **mvp-001-gen-s0**: PREPARING — \n- **mvp-001-gen-s3**: PREPARING (failed) — \n- **mvp-001-gen-s2**: PREPARING (failed) — \n- **mvp-001-gen-s1**: PREPARING (failed) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan-001: Feature ablation: 模型级特征（entropy系列+tail_decay）独立于表面特征仍能区分生成深度；H1/H2趋势分析确认特征随depth的变化模式；perplexity随depth显著变化（已分配 ? GPU:?，等待提交）\n- mvp-001-gen-s0（准备中）\n- mvp-001-gen-s3（准备中）\n- mvp-001-gen-s2（准备中）\n- mvp-001-gen-s1（准备中）\n\n## 近期结论\n- **mvp-001** (success): Pythia-410M 参考模型的分布特征（entropy stats, tail-decay, TTR, hapax）能区分 Pythia-2.8B continuation 链的 gen-0/gen-1/gen-2+，3-class macro-F1 ≥ 0.45\n  [MVP Results](/api/workspace-files/projects/gen-depth-fingerprint/artifacts/mvp-001/data/mvp_results_pointer.txt) | [MVP-001 Results](autodl-5090:/root/gen-depth-fingerprint/results/mvp_results.json)\n\n## 趋势\n成功 1 / 负向 0 / 失败 0 / 共 1\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6917ae0-5d20-47d5-b51c-2ebf8928802c",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "24f4ba5e-9168-4ee7-8933-1f4455cb5aa9",
  "sourceToolAssistantUUID": "b6917ae0-5d20-47d5-b51c-2ebf8928802c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T18:43:46.286Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011aiEDdza6z2V119eGauW3J`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24f4ba5e-9168-4ee7-8933-1f4455cb5aa9",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xKy9ocvt2wf3i2xkP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98446708-a8de-4228-94e0-5eec0ee63d54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019irzVaDBmdyYpazA6zRiJ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 9 · 2026-05-14T18:43:46.294Z_

<details><summary>↩ Tool result · `toolu_011aiEDdza6z2V119eGauW3J`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- plan-001: Feature ablation: 模型级特征（entropy系列+tail_decay）独立于表面特征仍能区分生成深度；H1/H2趋势分析确认特征随depth的变化模式；perplexity随depth显著变化（已分配 ? GPU:?，等待提交）\\n- mvp-001-gen-s0（准备中）\\n- mvp-001-gen-s3（准备中）\\n- mvp-001-gen-s2（准备中）\\n- mvp-001-gen-s1（准备中）\\n\\n## 近期结论\\n- **mvp-001** (success): Pythia-410M 参考模型的分布特征（entropy stats, tail-decay, TTR, hapax）能区分 Pythia-2.8B continuation 链的 gen-0/gen-1/gen-2+，3-class macro-F1 ≥ 0.45\\n  [MVP Results](/api/workspace-files/projects/gen-depth-fingerprint/artifacts/mvp-001/data/mvp_results_pointer.txt) | [MVP-001 Results](autodl-5090:/root/gen-depth-fingerprint/results/mvp_results.json)\\n\\n## 趋势\\n成功 1 / 负向 0 / 失败 0 / 共 1\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 810, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98446708-a8de-4228-94e0-5eec0ee63d54",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "b3bbcec8-d03f-4386-8c2f-0635035976f9",
  "sourceToolAssistantUUID": "98446708-a8de-4228-94e0-5eec0ee63d54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T18:43:46.891Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PMaTYFApmapL5PCEwJt6vn`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3bbcec8-d03f-4386-8c2f-0635035976f9",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xKy9ocvt2wf3i2xkP9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05324a54-deb2-4fef-96c2-d3bf5903cf8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019irzVaDBmdyYpazA6zRiJ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 11 · 2026-05-14T18:43:46.903Z_

<details><summary>↩ Tool result · `toolu_01PMaTYFApmapL5PCEwJt6vn`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05324a54-deb2-4fef-96c2-d3bf5903cf8d",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "6156e069-8bbb-42e6-a358-d860597fdc06",
  "sourceToolAssistantUUID": "05324a54-deb2-4fef-96c2-d3bf5903cf8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T18:43:50.183Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012YB9vzn1euj79fdm6i8TVg`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6156e069-8bbb-42e6-a358-d860597fdc06",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xLGu9ZRJR9PnWF7i3m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "224898c9-82ed-4023-9f1e-e49bdc0f57a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGDyWULThK2Mh4KkDhrd94",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1685,
      "cache_read_input_tokens": 16840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1685,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 13 · 2026-05-14T18:43:50.191Z_

<details><summary>↩ Tool result · `toolu_012YB9vzn1euj79fdm6i8TVg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ROADMAP.md\", \"content\": \"# gen-depth-fingerprint — Research Dashboard\\n\\n> 最后更新: 2026-05-14 18:12 UTC | 更新原因: Post-MVP: research 阶段启动，引用 paper_framing.md + experiment_plan.yaml\\n\\n## 核心方向\\n估计文本的\\\"生成深度\\\"（gen-0 / gen-1 / gen-2+），实现风险分层数据治理。非释义生成链打破 attractor 收敛约束，分布漂移随深度累积，留下可检测的\\\"分布指纹\\\"。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-14 通过，macro-F1=0.84，binary-F1=0.87）\\n- **服务器**: autodl-5090 (4× RTX 5090 32GB)\\n- **Venue**: AAAI 2027 (DDL Aug 2) primary / EMNLP 2026 ARR (May 25) stretch\\n- **Dream**: dream_20260514T181213 pending（full review mode）\\n- **覆盖率**: MVP 验证了 Claim 1 单生成器场景；Claim 2/3 待验证\\n\\n## Core Claims (from paper_framing.md)\\n1. **Depth Discriminability** — 分布特征能跨生成器区分 gen-0/gen-1/gen-2+\\n2. **Distributional Fingerprint Independence** — 参考模型特征独立于表面词汇统计\\n3. **Downstream Utility** — 深度感知过滤优于二分类过滤\\n\\n## 实验计划 (from experiment_plan.yaml)\\n| ID | Name | Claim | Pri | GPU·h | Status |\\n|----|------|-------|-----|-------|--------|\\n| mvp-001 | mvp_validation | 1 | — | 3 | ✅ DONE |\\n| plan_001 | feature_ablation | 2 | P0 | 1 | pending |\\n| plan_002 | cross_generator_evaluation | 1 | P0 | 20 | pending |\\n| plan_003 | cross_family_reference_model | 1 | P0 | 8 | pending |\\n| plan_004 | downstream_utility | 3 | P0 | 15 | pending |\\n| plan_005 | prompt_type_comparison | 1 | P1 | 10 | pending |\\n| plan_006 | paraphrastic_comparison | 1 | P1 | 8 | pending |\\n| plan_007 | cross_model_chains | 1 | P1 | 12 | pending |\\n| plan_008 | multi_domain_seeds | 1 | P1 | 10 | pending |\\n| plan_009-012 | P2 experiments | 1,2 | P2 | 23 | pending |\\n\\n**GPU 预算**: P0 ~44h / P1 ~40h / P2 ~23h / Total ~107h (≤200h budget)\\n\\n## 近期任务\\n- [ ] 等待 Dream 回调 → 分析审稿反馈 → 决定是否调整 framing/plan\\n- [ ] Dream 通过后：批准 plan_001 (feature_ablation) — 用现有 MVP 数据，无需新 generation\\n- [ ] plan_001 结果确认 Claim 2 后：批准 plan_002 (cross_generator，需下载 4 个新模型)\\n\\n## GPU 预算\\n本项目分配: autodl-5090 4× RTX 5090 (32GB)\\n已用: ~3 GPU·h (MVP generation + feature extraction)\\n剩余: ~197 GPU·h\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D004 | 2026-05-14 | Claim 2 framing 调整：从 \\\"Fingerprint Independence\\\" 转为 | plan_001 |\\n| D003 | 2026-05-14 | Claim 2 准备 Plan B framing：若 ablation 显示表面特征足够，叙事从  | — |\\n| D002 | 2026-05-14 | MVP PASS → 进入研究阶段。首要任务：特征 ablation + depth signal  | mvp-001 |\\n| D001 | 2026-05-14 | MVP 方案：Pythia-2.8B continuation 链 + Pythia-410M 参考 | — |\\n\\n\", \"total_chars\": 2298, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "224898c9-82ed-4023-9f1e-e49bdc0f57a6",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "ac1505cf-4424-4f9b-bdd5-1d2e874c5040",
  "sourceToolAssistantUUID": "224898c9-82ed-4023-9f1e-e49bdc0f57a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T18:43:51.016Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JoMRkggos32pYHQBLyYgG7`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac1505cf-4424-4f9b-bdd5-1d2e874c5040",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xLGu9ZRJR9PnWF7i3m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dfec050-a74b-4ffb-8528-8ccf5b169569",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGDyWULThK2Mh4KkDhrd94",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1685,
      "cache_read_input_tokens": 16840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1685,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 15 · 2026-05-14T18:43:51.026Z_

<details><summary>↩ Tool result · `toolu_01JoMRkggos32pYHQBLyYgG7`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dfec050-a74b-4ffb-8528-8ccf5b169569",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "fa5c1129-e346-4038-81d7-a11603aea82a",
  "sourceToolAssistantUUID": "0dfec050-a74b-4ffb-8528-8ccf5b169569",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T18:43:51.504Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Na7eYv5sUZeAirj68acB7g`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa5c1129-e346-4038-81d7-a11603aea82a",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xLGu9ZRJR9PnWF7i3m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c6cdcfe-ca56-40dd-a176-4136e3815106",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGDyWULThK2Mh4KkDhrd94",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1685,
      "cache_read_input_tokens": 16840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1685,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 17 · 2026-05-14T18:43:51.513Z_

<details><summary>↩ Tool result · `toolu_01Na7eYv5sUZeAirj68acB7g`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-fingerprint\\n\\n## Target Venue\\n- Primary: AAAI 2027 (deadline: August 2, 2026)\\n- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4\\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\\n\\n## Core Insight\\nNon-paraphrastic LLM generation chains exhibit **feature-dependent depth dynamics**: vocabulary/surface features (TTR, hapax ratio) and aggregate entropy drift monotonically with depth (H₂), while distributional shape features (tail decay, entropy variance) remain near-stationary (H₁). This dual pattern — surface impoverishment + stable distributional shape — creates a rich, complementary feature space for depth estimation. The combination of surface and reference-model features significantly outperforms either alone (macro-F1 0.82 vs 0.76/0.72), enabling risk-stratified data curation beyond binary real/synthetic filtering.\\n\\n## Core Claims (3 条，均可证伪)\\n\\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).\\n\\n**Claim 2 — Feature Complementarity & Dual Dynamics**: Surface features (vocabulary impoverishment) and reference-model features (distributional shape) capture **different aspects** of depth-dependent signal. Neither alone matches the full feature set (ablation: full 0.82 > surface 0.76 > reference 0.72, p<0.001 for full vs surface). Moreover, these two feature families exhibit distinct depth dynamics: surface features drift monotonically (H₂), while distributional shape features remain stationary (H₁) — revealing that recursive generation simultaneously impoverishes vocabulary and preserves distributional structure.\\n\\n**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.\\n\\n## Story Spine\\n\\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\\n\\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.\\n\\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing a **dual dynamics** pattern: vocabulary features drift monotonically with depth (supporting H₂) while distributional shape features remain stationary (supporting H₁). This is not H₁-vs-H₂ — both coexist in different feature families, suggesting distinct mechanisms: vocabulary impoverishment accumulates via mode collapse in the lexical space, while the reference model's token-level probability structure is robust to recursive generation. This dual pattern is practically useful: combining both feature types yields significantly better depth estimation than either alone, enabling risk-stratified data curation.\\n\\n**Headline result template**: \\\"On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines.\\\"\\n\\n## Anticipated Reviewer Concerns\\n\\n**RC1 — \\\"Is this just vocabulary impoverishment?\\\"**: Surface features alone achieve 0.76 macro-F1, but full features achieve 0.82 (p<0.001). We don't claim reference features are \\\"better\\\" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting vocabulary). The dual dynamics finding is itself a scientific contribution.\\n\\n**RC2 — \\\"Does this generalize beyond Pythia?\\\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\\n\\n**RC3 — \\\"Is 3-class sufficient? Why not finer-grained?\\\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\\n\\n**RC4 — \\\"How realistic are single-model chains?\\\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\\n\\n**RC5 — \\\"What about human editing / post-processing?\\\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\\n\\n**RC6 — \\\"Ecological validity — continuation vs real web content\\\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\\n\\n## Venue Fit\\n- AAAI 2027: Strong fit — data governance + ML methodology. The dual dynamics (H₁+H₂ coexistence) finding positions it as empirical science with theoretical insight, not just a classifier paper.\\n- EMNLP 2026: Excellent fit — directly addresses special theme \\\"New Missions for NLP Research\\\" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work.\\n\", \"total_chars\": 5969, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c6cdcfe-ca56-40dd-a176-4136e3815106",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "07c217bf-ada1-4452-9976-68a2daa0bf6b",
  "sourceToolAssistantUUID": "9c6cdcfe-ca56-40dd-a176-4136e3815106",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T18:43:52.042Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AiDkAZ2XnzuVhxh3k8VDsC`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07c217bf-ada1-4452-9976-68a2daa0bf6b",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xLGu9ZRJR9PnWF7i3m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e73f2033-95ec-4b99-90df-6d098574b293",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGDyWULThK2Mh4KkDhrd94",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1685,
      "cache_read_input_tokens": 16840,
      "output_tokens": 384,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1685
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 384,
          "cache_read_input_tokens": 16840,
          "cache_creation_input_tokens": 1685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1685,
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

_source line 19 · 2026-05-14T18:43:52.054Z_

<details><summary>↩ Tool result · `toolu_01AiDkAZ2XnzuVhxh3k8VDsC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/memory.md\", \"content\": \"# gen-depth-fingerprint — Memory\\n\\n## 关键发现\\n\\n### MVP-001 结果（2026-05-14）\\n- **PASS**: macro-F1=0.8408 (阈值 0.45), binary F1=0.8653 (阈值 0.65)\\n- 词汇多样性特征（hapax_ratio, ttr）区分力最强，feature importance 分别 0.30 和 0.17\\n- entropy_mean 是最强的模型级特征（importance 0.22）\\n- tail_decay 区分力最弱（importance 0.057），但仍统计显著\\n- gen-0 几乎完美分离（F1=0.95），gen-1 vs gen-2+ 有一定混淆（45 个 gen-2+ 误判为 gen-1）\\n- 深度衰减 17.4%：部分 continuation 产生空文本导致链条中断（995→822 from depth 0→4）\\n- **洞察**：表面特征（hapax/ttr）可能过于强势，掩盖了模型级特征的真实区分力。后续实验应考虑：(a) 只用模型级特征的 ablation (b) 跨模型泛化测试\\n\\n## 经验教训\\n\\n### submit_training_job + CUDA_VISIBLE_DEVICES 映射（2026-05-14）\\n`submit_training_job` 自动注入 `CUDA_VISIBLE_DEVICES=N`（物理卡号）。注入后进程只看到 1 张卡，脚本内必须用 `--device cuda:0`（逻辑设备 0），不能用 `cuda:N`。否则 shard 1/2/3 会报 \\\"CUDA device ordinal out of range\\\"。\\n\\n### AutoDL 网络 + 数据源（2026-05-14）\\nWikipedia 数据集在 AutoDL 上流式加载失败。解决方案：预下载到本地 JSONL（`wiki_seed_1000.jsonl`），脚本用 `--input` 参数读本地文件。ModelScope 下载 HF 模型时路径名会转换（如 `pythia-2.8b` → `pythia-2___8b`）。\\n\\n### nohup vs submit_training_job（2026-05-14）\\nWorker 用 nohup 提交后台任务会导致 orphan 进程（无监控、无回调）。必须用 `submit_training_job`（tmux + cron 自动监控）。\\n\\n### 生成参数敏感性（2026-05-14）\\ntemperature=0.7/top_p=0.9（IDEA_BRIEF 规定）。不能用 temp=1.0——高温度使生成文本更随机、分类更容易，MVP 通过不能证明假设。\\n\\n## 决策记录\\n\\n### MVP 生成参数（2026-05-14，Director 指定）\\n- temperature=0.7, top_p=0.9, max_new_tokens=256, do_sample=True, seed=42\\n- 种子数据：wiki_seed_1000.jsonl（1000 条 Wikipedia，本地预下载）\\n- 判定标准：二值 PASS/FAIL（无 MARGINAL），macro-F1 ≥ 0.45 AND binary F1 ≥ 0.65\\n\", \"total_chars\": 1434, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e73f2033-95ec-4b99-90df-6d098574b293",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "aefa8c6e-4cb4-4683-a061-a3779f567c75",
  "sourceToolAssistantUUID": "e73f2033-95ec-4b99-90df-6d098574b293",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T18:43:55.288Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01D9umizjJgLx2wgj3ZvBhew`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aefa8c6e-4cb4-4683-a061-a3779f567c75",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xLef6HqpssmzuQk9UZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54713e8a-59d3-4f56-8def-7835fb32fd38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SWVAVt5oJ76PqhhET14xZ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4716,
      "cache_read_input_tokens": 18525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4716,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 21 · 2026-05-14T18:43:55.295Z_

<details><summary>↩ Tool result · `toolu_01D9umizjJgLx2wgj3ZvBhew`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/decisions.yaml\", \"content\": \"_next_id: 5\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:15 UTC\\n  summary: MVP 方案：Pythia-2.8B continuation 链 + Pythia-410M 参考模型 + XGBoost 3-class\\n    分类\\n  rationale: '选择 continuation（最低语义偏离）作为最可能保留 depth 信号的生成类型；单生成器简化变量；Pythia-410M 作为参考模型避免与生成器的规模/架构循环；XGBoost\\n    快速验证无需 GPU 训练。Pass: macro-F1≥0.45 且 gen-0 vs gen-2+ F1≥0.65。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 18:10 UTC\\n  summary: MVP PASS → 进入研究阶段。首要任务：特征 ablation + depth signal 增量验证\\n  rationale: macro-F1=0.84 远超 0.45 阈值，binary F1=0.87 远超 0.65，7/7 特征显著。核心假设成立。但 Reviewer\\n    指出 hapax_ratio（表面特征）贡献最大，需 ablation 验证分布指纹的独立价值；gen-1 vs gen-2+ 混淆率高，需量化 depth\\n    信号超越 binary 分类的增量。\\n  related_experiments:\\n  - exp_id: mvp-001\\n    role: primary\\n    result: 'PASS: macro-F1=0.8408, binary-F1=0.8653'\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 18:15 UTC\\n  summary: Claim 2 准备 Plan B framing：若 ablation 显示表面特征足够，叙事从 \\\"independent signal\\\"\\n    调整为 \\\"complementary signal\\\"\\n  rationale: Reviewer 指出 Claim 2 是整个叙事的 single point of failure。MVP 中 hapax_ratio\\n    importance=0.30，表面特征贡献 47%。Plan B 不 kill 项目，只调 framing 强度——从\\\"分布指纹独立于表面统计\\\"降为\\\"分布指纹提供互补信号\\\"，核心叙事转为\\n    vocabulary impoverishment as primary depth signal。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 18:38 UTC\\n  summary: Claim 2 framing 调整：从 \\\"Fingerprint Independence\\\" 转为 \\\"Feature Complementarity\\n    & Dual Dynamics\\\"；H1/H2 从二选一转为共存\\n  rationale: plan_001 ablation 结果：surface_only (0.76) > reference_only (0.72)，但 full\\n    (0.82) 显著优于 surface_only (p=0.0008)。原 Claim 2 \\\"independent signal\\\" 被否定，触发 Plan\\n    B (D003)。新发现更强：表面特征呈 H2 drift、分布形状特征呈 H1 stationary，dual dynamics 是比原 framing\\n    更丰富的科学贡献。\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: primary\\n    result: surface_only 0.76 > reference_only 0.72; full 0.82 显著优于两者; H1/H2 按特征类型共存\\n  depends_on:\\n  - D002\\n  - D003\\n\", \"total_chars\": 1852, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54713e8a-59d3-4f56-8def-7835fb32fd38",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "3733dbe6-088b-4fc6-bb5d-4bc2bd92a198",
  "sourceToolAssistantUUID": "54713e8a-59d3-4f56-8def-7835fb32fd38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T18:43:56.231Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018GsFU1ABtWtc4x5XM927Y5`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3733dbe6-088b-4fc6-bb5d-4bc2bd92a198",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xLef6HqpssmzuQk9UZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79a7b97d-fc50-4068-830b-6428c1c7039b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SWVAVt5oJ76PqhhET14xZ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4716,
      "cache_read_input_tokens": 18525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4716,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 23 · 2026-05-14T18:43:56.244Z_

<details><summary>↩ Tool result · `toolu_018GsFU1ABtWtc4x5XM927Y5`</summary>

```text
artifacts/_project/data/generate_chain.py
artifacts/generate_chain.py
artifacts/ablation_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79a7b97d-fc50-4068-830b-6428c1c7039b",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "f1bc1c24-5763-408f-84a5-b7f4a40967c1",
  "sourceToolAssistantUUID": "79a7b97d-fc50-4068-830b-6428c1c7039b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T18:43:56.435Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VQ3r4qXbuCPCjAXdMA5SMW`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1bc1c24-5763-408f-84a5-b7f4a40967c1",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xLef6HqpssmzuQk9UZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a5fa97b-d562-4c8f-8afa-07ca535f40ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SWVAVt5oJ76PqhhET14xZ5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4716,
      "cache_read_input_tokens": 18525,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4716
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 269,
          "cache_read_input_tokens": 18525,
          "cache_creation_input_tokens": 4716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4716,
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

_source line 25 · 2026-05-14T18:43:56.447Z_

<details><summary>↩ Tool result · `toolu_01VQ3r4qXbuCPCjAXdMA5SMW`</summary>

```text
artifacts/dream_reports/dream_20260514T181213/best/paper.tex
artifacts/dream_reports/dream_20260514T181213/median/paper.tex
artifacts/dream_reports/dream_20260514T181213/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a5fa97b-d562-4c8f-8afa-07ca535f40ca",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "2a5aebaa-05c5-4a45-a9d8-c1b1cf16320c",
  "sourceToolAssistantUUID": "7a5fa97b-d562-4c8f-8afa-07ca535f40ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-14T18:43:58.885Z_

Let me read the paper drafts to understand the full content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a5aebaa-05c5-4a45-a9d8-c1b1cf16320c",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xLyTCBDL3y7A7qvn7e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8091747b-6d5e-4114-9e81-492ef518a04a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmAZxoTpoSNVRaZJ3EvkgU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1706,
      "cache_read_input_tokens": 23241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1706,
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

_source line 27 · 2026-05-14T18:43:59.455Z_

<details open><summary>🔧 Tool call — Read · `toolu_015eaZZ1FXocMp4mNjse6cW9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8091747b-6d5e-4114-9e81-492ef518a04a",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xLyTCBDL3y7A7qvn7e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "863539fe-9546-4227-ab77-ee596103c1f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmAZxoTpoSNVRaZJ3EvkgU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1706,
      "cache_read_input_tokens": 23241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1706,
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

_source line 28 · 2026-05-14T18:43:59.764Z_

<details><summary>↩ Tool result · `toolu_015eaZZ1FXocMp4mNjse6cW9`</summary>

```text
1	\documentclass[letterpaper, 10pt]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{helvet}
5	\usepackage{courier}
6	\usepackage[hyphens]{url}
7	\usepackage{graphicx}
8	\usepackage{amsmath,amssymb}
9	\usepackage{booktabs}
10	\usepackage{multirow}
11	\usepackage{xcolor}
12	\usepackage{hyperref}
13	\usepackage{enumitem}
14	
15	\title{Distributional Fingerprints of Generation Depth:\\Detecting Recursive LLM Contamination Beyond Binary Classification}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\begin{abstract}
23	Web-scraped training corpora increasingly contain LLM-generated text of unknown provenance depth---text generated by models that were themselves trained on synthetic data.
24	Current detection methods provide only binary real-vs-synthetic classification, forcing all-or-nothing filtering that either discards useful first-generation content or admits deeply contaminated text with compounding distributional drift.
25	We introduce \emph{distributional fingerprinting}, a method that estimates the generation depth of text by measuring its distributional divergence from human text under a small reference language model.
26	We formalize and test two competing hypotheses for non-paraphrastic generation chains: convergence to a distributional fixed point (H$_1$) versus monotonic divergence (H$_2$).
27	Our experiments across 5 generators, 4 text domains, and 3 prompt types confirm H$_2$: non-paraphrastic chains exhibit monotonic distributional drift detectable via reference-model entropy features.
28	On multi-generator continuation chains, our 7-feature classifier achieves macro-F1 of 0.87 for 3-class depth estimation (gen-0/gen-1/gen-2+) and generalizes to unseen generators with leave-one-out F1 of 0.78.
29	Feature ablation shows reference-model entropy features carry independent signal beyond surface vocabulary impoverishment ($\Delta$F1 = +0.16, McNemar $p < 10^{-4}$).
30	Depth-aware data filtering retains 42\% of training data while achieving perplexity within 0.7 points of human-only baselines---outperforming binary detection baselines by 5.2\% while retaining 50\% more data.
31	\end{abstract}
32	
33	\section{Introduction}
34	
35	The recursive contamination of training data by LLM outputs is an accelerating concern.
36	As language models are deployed at scale, their outputs enter the web, are scraped into training corpora, and are used to train the next generation of models~\cite{shumailov2024model}.
37	This creates generation chains: text at \emph{depth~0} is human-written, depth~1 is generated from human text, depth~2 is generated from depth-1 text, and so forth.
38	The distributional consequences of this recursive process are poorly understood.
39	
40	Existing detection methods---FastDetectGPT, SynthID-Text, LD-Score~\cite{bao2024fastdetectgpt, dathathri2024synthid, dugan2024ldscore}---operate in a binary paradigm: text is classified as real or synthetic.
41	This forces a lossy tradeoff.
42	Aggressive filtering discards all flagged text, including first-generation content that is distributionally close to human text and useful for training.
43	Permissive filtering admits deeply generated text with compounding distributional artifacts.
44	Neither approach is adequate for risk-stratified data governance.
45	
46	Attractor cycle theory~\cite{briesch2025attractor} has established that \emph{paraphrastic} generation chains converge to 2-period distributional cycles, bounding depth discriminability to roughly 3 classes.
47	However, this result depends on the semantic-preservation constraint inherent to paraphrasing.
48	Non-paraphrastic chains---continuations, elaborations, and other open-ended generation tasks---operate in an unbounded semantic state space.
49	Whether distributional drift in such chains converges (H$_1$) or diverges monotonically (H$_2$) remains an open empirical question.
50	
51	We address this question by introducing \emph{distributional fingerprinting}: computing token-level statistics under a small reference language model to characterize the distributional displacement of text from the human-text manifold.
52	Our method extracts 7 features---5 reference-model entropy statistics and 2 surface vocabulary statistics---and uses an XGBoost classifier for ordinal depth estimation.
53	
54	Our contributions are:
55	\begin{enumerate}
56	    \item \textbf{Empirical confirmation of H$_2$}: Non-paraphrastic generation chains exhibit monotonic distributional divergence, in contrast to the convergence observed in paraphrastic chains. This is demonstrated by direct comparison of continuation vs.\ paraphrasing chains (KS statistic $D = 0.41$, $p < 10^{-4}$).
57	    \item \textbf{Cross-generator depth classification}: Our distributional fingerprint achieves macro-F1 = 0.87 (3-class) and generalizes across 5 generator families with leave-one-generator-out F1 = 0.78 $\pm$ 0.03.
58	    \item \textbf{Risk-stratified data curation}: Depth-aware filtering outperforms binary baselines by 5.2\% in downstream perplexity while retaining 50\% more training data.
59	\end{enumerate}
60	
61	\section{Related Work}
62	
63	\paragraph{Synthetic text detection.}
64	Binary detection methods assign a real/synthetic label to text.
65	FastDetectGPT~\cite{bao2024fastdetectgpt} uses conditional probability curvature, SynthID-Text~\cite{dathathri2024synthid} embeds statistical watermarks, and LD-Score~\cite{dugan2024ldscore} uses character-level distributional signatures.
66	All are binary classifiers that cannot distinguish generation depth.
67	
68	\paragraph{Model collapse and iterative retraining.}
69	Shumailov et al.~\cite{shumailov2024model} demonstrate that iterative retraining on model outputs leads to distributional collapse, with progressive loss of low-frequency modes.
70	Their analysis focuses on full-model retraining dynamics rather than individual text-level depth estimation.
71	
72	\paragraph{Attractor cycles in paraphrasing chains.}
73	Briesch et al.~\cite{briesch2025attractor} prove that iterative paraphrasing converges to 2-period distributional cycles, where semantic content oscillates between two attractors.
74	This convergence limits depth discriminability for paraphrastic chains.
75	Our work complements theirs by studying non-paraphrastic chains, where the absence of semantic preservation constraints leads to qualitatively different dynamics.
76	
77	\section{Method}
78	
79	\subsection{Problem Formulation}
80	
81	Let $\mathcal{G}$ be a text generator and $x^{(0)}$ be a human-authored seed text.
82	A \emph{generation chain} of depth $d$ produces a sequence $x^{(0)}, x^{(1)}, \ldots, x^{(d)}$ where $x^{(k)} = \mathcal{G}(x^{(k-1)})$.
83	Given a text sample $x$ drawn from an unknown depth, the depth estimation task is to predict $\hat{d} \in \{0, 1, 2, \ldots\}$.
84	We operationalize this as classification into depth classes: gen-0 (human), gen-1 (first-generation synthetic), and gen-2+ (depth $\geq 2$).
85	
86	\subsection{Distributional Fingerprint Features}
87	
88	We extract features by scoring text under a \emph{reference model} $p_{\text{ref}}$---a small pretrained language model (Pythia-410M by default) that was never fine-tuned on synthetic data.
89	For each token $t_i$ in a text of length $n$, we compute the reference-model negative log-likelihood $\ell_i = -\log p_{\text{ref}}(t_i | t_{&lt;i})$.
90	
91	\paragraph{Reference-model features (5).}
92	We compute: (1) $\texttt{entropy\_mean} = \frac{1}{n}\sum_i \ell_i$, the average surprise under the reference model; (2) $\texttt{entropy\_std}$, the standard deviation of per-token surprises; (3--4) $\texttt{entropy\_min}$, $\texttt{entropy\_max}$, capturing the range; and (5) $\texttt{tail\_decay}$, the fraction of tokens in the top-10\% surprise quantile, measuring how much text mass falls in the distributional tail.
93	
94	The intuition is that deeper-generation text progressively occupies lower-probability regions of the reference model's distribution.
95	As drift accumulates, $\texttt{entropy\_mean}$ increases because the reference model is increasingly ``surprised'' by text that has drifted from the human-text manifold.
96	The variance ($\texttt{entropy\_std}$) increases because deeper text alternates between familiar patterns and novel drift artifacts.
97	
98	\paragraph{Surface features (2).}
99	We include type-token ratio ($\texttt{ttr}$) and hapax legomenon ratio ($\texttt{hapax\_ratio}$) as vocabulary diversity measures.
100	These capture the well-known vocabulary impoverishment effect of language model generation but, as we show, provide weaker and less fine-grained depth signal than reference-model features.
101	
102	\subsection{Classifier}
103	
104	We train an XGBoost classifier on the 7-dimensional feature vector with 5-fold stratified cross-validation.
105	We chose XGBoost over neural alternatives for interpretability and computational efficiency (training in $\sim$3 minutes vs.\ 12 GPU-hours for a fine-tuned LLM baseline; see Section~\ref{sec:e2e}).
106	
107	\subsection{Hypotheses}
108	
109	We formalize two competing hypotheses about distributional dynamics in recursive generation:
110	
111	\noindent\textbf{H$_1$ (Convergence):} Non-paraphrastic chains converge to a distributional fixed point, analogous to paraphrastic attractor cycles.
112	Under H$_1$, depth signal saturates after a few generations.
113	
114	\noindent\textbf{H$_2$ (Divergence):} Non-paraphrastic chains accumulate monotonic distributional drift from the human-text manifold.
115	Under H$_2$, depth signal grows with generation depth, enabling ordinal depth estimation.
116	
117	\section{Experimental Setup}
118	
119	\paragraph{Data generation.}
120	We construct generation chains from 2{,}000 seed texts spanning 4 domains (Wikipedia, CNN/DailyMail news, S2ORC scientific abstracts, WritingPrompts creative fiction), 500 seeds per domain.
121	Each seed is extended to depth 5 using 5 generators: Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, and Pythia-1B.
122	Three prompt types are used: continuation, elaboration, and inspired rewriting.
123	The resulting dataset contains $\sim$24{,}200 chains after $\sim$3.2\% attrition from generation failures.
124	
125	\paragraph{Feature extraction.}
126	All features are extracted using Pythia-410M as the default reference model.
127	Cross-reference experiments additionally use OLMo-2-1B and Qwen3.5-0.8B.
128	
129	\paragraph{Evaluation protocol.}
130	Unless otherwise stated, we report macro-F1 over 5-fold stratified cross-validation for the 3-class task (gen-0/gen-1/gen-2+).
131	For generalization experiments, we use leave-one-generator-out and leave-one-domain-out protocols.
132	
133	\section{Experiments}
134	
135	\subsection{Feature Ablation (Claim 2)}
136	\label{sec:ablation}
137	
138	We ablate the 7-feature set into three conditions: (A) reference-only features (5 entropy statistics), (B) surface-only features (TTR, hapax ratio), and (C) the full 7-feature set.
139	All use the same XGBoost classifier with 5-fold stratified CV on the MVP dataset (4{,}609 records, Pythia-2.8B generator, Wikipedia seeds).
140	
141	\begin{table}[t]
142	\centering
143	\caption{Feature ablation results (3-class depth classification). Reference-model features alone substantially outperform surface-only features, and the full set achieves the best performance.}
144	\label{tab:ablation}
145	\small
146	\begin{tabular}{@{}lcccc@{}}
147	\toprule
148	Feature Set & Macro-F1 & gen-0 & gen-1 & gen-2+ \\
149	\midrule
150	Reference-only (5) & 0.79 {\scriptsize$\pm$0.018} & 0.91 & 0.71 & 0.74 \\
151	Surface-only (2) & 0.63 {\scriptsize$\pm$0.022} & 0.82 & 0.52 & 0.55 \\
152	Full (7) & \textbf{0.87} {\scriptsize$\pm$0.012} & \textbf{0.96} & \textbf{0.81} & \textbf{0.83} \\
153	\midrule
154	$\Delta$ (ref $-$ surface) & +0.16 & +0.09 & +0.19 & +0.19 \\
155	\bottomrule
156	\end{tabular}
157	\end{table}
158	
159	Table~\ref{tab:ablation} shows that reference-only features achieve macro-F1 = 0.79, substantially outperforming surface-only features at 0.63 ($\Delta$ = +0.16, McNemar $p = 3 \times 10^{-5}$).
160	The advantage is largest for gen-1 and gen-2+ ($\Delta$ = +0.19 each), precisely the classes where surface features struggle.
161	This is because vocabulary impoverishment (captured by TTR, hapax ratio) saturates between gen-0 and gen-1, while reference-model entropy features capture cumulative distributional drift that continues to grow at deeper depths.
162	
163	Permutation importance analysis (Table~\ref{tab:importance}) confirms this pattern: under permutation (which avoids XGBoost's split-gain bias toward high-cardinality features), $\texttt{entropy\_mean}$ emerges as the dominant feature (importance = 0.28), while $\texttt{hapax\_ratio}$ drops from its inflated XGBoost gain rank.
164	
165	\begin{table}[t]
166	\centering
167	\caption{Permutation importance vs.\ XGBoost gain.}
168	\label{tab:importance}
169	\small
170	\begin{tabular}{@{}lcc@{}}
171	\toprule
172	Feature & Perm.\ Importance & XGB Gain \\
173	\midrule
174	entropy\_mean & \textbf{0.28} & 0.22 \\
175	entropy\_std & 0.19 & 0.13 \\
176	hapax\_ratio & 0.14 & 0.30 \\
177	tail\_decay & 0.13 & 0.06 \\
178	ttr & 0.09 & 0.17 \\
179	entropy\_max & 0.09 & 0.07 \\
180	entropy\_min & 0.08 & 0.06 \\
181	\bottomrule
182	\end{tabular}
183	\end{table}
184	
185	\subsection{Cross-Generator Generalization (Claim 1)}
186	\label{sec:crossgen}
187	
188	To test whether distributional fingerprints generalize beyond any single generator family, we evaluate using leave-one-generator-out cross-validation across 5 generators.
189	
190	\begin{table}[t]
191	\centering
192	\caption{Leave-one-generator-out cross-validation. The classifier trained on 4 generators generalizes to the held-out generator.}
193	\label{tab:crossgen}
194	\small
195	\begin{tabular}{@{}lcccc@{}}
196	\toprule
197	Held-out Generator & Macro-F1 & gen-0 & gen-1 & gen-2+ \\
198	\midrule
199	Pythia-2.8B & 0.81 & 0.91 & 0.75 & 0.77 \\
200	OLMo-2-1B & 0.77 & 0.87 & 0.72 & 0.73 \\
201	Qwen3.5-2B & 0.76 & 0.86 & 0.71 & 0.72 \\
202	Qwen3.5-0.8B & 0.74 & 0.84 & 0.68 & 0.70 \\
203	Pythia-1B & 0.82 & 0.92 & 0.76 & 0.78 \\
204	\midrule
205	Mean $\pm$ std & 0.78 $\pm$ 0.03 & 0.88 & 0.73 & 0.75 \\
206	\bottomrule
207	\end{tabular}
208	\end{table}
209	
210	Table~\ref{tab:crossgen} demonstrates consistent generalization: mean leave-one-out F1 = 0.78 $\pm$ 0.03 across all 5 generators, with gen-0 separation remaining strong ($\geq$0.84) in all cases.
211	Cross-family transfer (e.g., Pythia-trained classifier tested on Qwen) maintains F1 $\geq$ 0.74, confirming that the distributional fingerprint is a property of the generation process rather than a generator-specific artifact.
212	In-distribution pooled performance reaches 0.86, suggesting that multi-generator training improves robustness (Table~\ref{tab:indist}).
213	
214	\begin{table}[t]
215	\centering
216	\caption{Per-generator in-distribution 5-fold CV.}
217	\label{tab:indist}
218	\small
219	\begin{tabular}{@{}lcc@{}}
220	\toprule
221	Generator & Macro-F1 & CV std \\
222	\midrule
223	Pythia-2.8B & 0.85 & 0.014 \\
224	OLMo-2-1B & 0.84 & 0.016 \\
225	Qwen3.5-2B & 0.86 & 0.013 \\
226	Qwen3.5-0.8B & 0.83 & 0.019 \\
227	Pythia-1B & 0.84 & 0.015 \\
228	\midrule
229	Pooled (all 5) & 0.86 & 0.011 \\
230	\bottomrule
231	\end{tabular}
232	\end{table}
233	
234	\subsection{Cross-Family Reference Models}
235	
236	A natural concern is whether the fingerprint depends on the choice of reference model.
237	We re-extract features using OLMo-2-1B and Qwen3.5-0.8B as alternative reference models, and compare classification performance.
238	
239	\begin{table}[t]
240	\centering
241	\caption{Reference model comparison on pooled 5-generator data.}
242	\label{tab:crossref}
243	\small
244	\begin{tabular}{@{}llcccc@{}}
245	\toprule
246	Reference Model & Params & F1 & gen-0 & gen-1 & gen-2+ \\
247	\midrule
248	Pythia-410M & 410M & 0.86 & 0.95 & 0.80 & 0.82 \\
249	OLMo-2-1B & 1B & 0.76 & 0.88 & 0.69 & 0.72 \\
250	Qwen3.5-0.8B & 0.8B & 0.74 & 0.86 & 0.66 & 0.70 \\
251	Ensemble (3 refs) & --- & \textbf{0.88} & \textbf{0.96} & \textbf{0.83} & \textbf{0.85} \\
252	\bottomrule
253	\end{tabular}
254	\end{table}
255	
256	All three reference models detect depth signal (F1 $\geq$ 0.74; Table~\ref{tab:crossref}), confirming that the fingerprint is not a Pythia-specific artifact.
257	High cross-reference correlations in entropy features (Spearman $\rho$ = 0.78--0.82 for $\texttt{entropy\_mean}$) indicate that different reference models measure the same underlying drift phenomenon through slightly different lenses.
258	The 3-reference ensemble achieves F1 = 0.88, suggesting that diverse reference models capture complementary drift aspects.
259	
260	\subsection{Paraphrastic vs.\ Non-Paraphrastic Chains (H$_1$ vs.\ H$_2$)}
261	\label{sec:h1h2}
262	
263	We directly test H$_1$ vs.\ H$_2$ by constructing parallel paraphrasing and continuation chains from the same 1{,}000 seeds.
264	
265	\begin{table}[t]
266	\centering
267	\caption{Paraphrastic vs.\ continuation chain comparison. Continuation chains show monotonic divergence (H$_2$); paraphrastic chains converge (H$_1$).}
268	\label{tab:h1h2}
269	\small
270	\begin{tabular}{@{}lccc@{}}
271	\toprule
272	Chain Type & Macro-F1 & Entropy Drift @d3 & Cycle \% \\
273	\midrule
274	Continuation & 0.85 & 0.52 nats & $<5\%$ \\
275	Paraphrasing & 0.58 & 0.06 nats & 68\% \\
276	\midrule
277	$\Delta$ & +0.27 & +0.46 nats & --- \\
278	\bottomrule
279	\end{tabular}
280	\end{table}
281	
282	Table~\ref{tab:h1h2} provides definitive evidence.
283	Continuation chains accumulate substantial entropy drift (0.52 nats by depth 3) with strong depth classification (F1 = 0.85), while paraphrastic chains show near-zero drift (0.06 nats) and weak classification (F1 = 0.58).
284	The 68\% cycle detection rate in paraphrastic chains---where text at depth $d$ is more similar to depth $d{-}2$ than $d{-}1$---directly corroborates the attractor cycle prediction of~\cite{briesch2025attractor}.
285	A two-sample Kolmogorov-Smirnov test on the depth-3 entropy distributions yields $D = 0.41$, $p < 10^{-4}$, confirming that the two chain types occupy distinct distributional regimes.
286	H$_2$ holds for non-paraphrastic chains; H$_1$ holds for paraphrastic chains.
287	
288	\subsection{Downstream Utility (Claim 3)}
289	\label{sec:downstream}
290	
291	We validate the practical value of depth estimation by fine-tuning Pythia-410M on depth-stratified data subsets and measuring perplexity on a held-out human test set.
292	
293	\begin{table}[t]
294	\centering
295	\caption{Fine-tuning perplexity by training data depth. Perplexity increases monotonically with depth ($\rho = 0.72$).}
296	\label{tab:ppl}
297	\small
298	\begin{tabular}{@{}llcc@{}}
299	\toprule
300	Training Data & Depth & PPL ($\downarrow$) & Samples \\
301	\midrule
302	Human-only & gen-0 & 28.3 & $\sim$4{,}800 \\
303	gen-1 only & gen-1 & 30.1 & $\sim$4{,}750 \\
304	gen-2 only & gen-2 & 34.7 & $\sim$4{,}500 \\
305	gen-3 only & gen-3 & 38.9 & $\sim$4{,}200 \\
306	gen-4 only & gen-4 & 43.2 & $\sim$3{,}900 \\
307	Uniform mix & gen-0--4 & 35.8 & $\sim$22{,}000 \\
308	\midrule
309	Depth-filtered (ours) & gen-0+1 & \textbf{29.0} & $\sim$9{,}500 \\
310	FastDetectGPT filter & binary & 31.8 & $\sim$6{,}300 \\
311	LD-Score filter & binary & 32.1 & $\sim$6{,}100 \\
312	\midrule
313	Human test baseline & --- & 27.5 & --- \\
314	\bottomrule
315	\end{tabular}
316	\end{table}
317	
318	Table~\ref{tab:ppl} demonstrates a monotonic relationship between training data depth and downstream perplexity (Spearman $\rho = 0.72$), providing an intuitive translation of distributional drift into a metric practitioners care about.
319	Depth-aware filtering (keep gen-0 + gen-1) achieves perplexity 29.0---within 0.7 points of the human-only baseline---while binary baselines achieve 31.8--32.1.
320	
321	\begin{table}[t]
322	\centering
323	\caption{Depth-aware vs.\ binary filtering. Depth-aware filtering retains more data at lower perplexity.}
324	\label{tab:filter}
325	\small
326	\begin{tabular}{@{}lccc@{}}
327	\toprule
328	Method & PPL & Retained & $\Delta$ Human \\
329	\midrule
330	Depth-filtered (gen-0+1) & \textbf{29.0} & 42\% & +0.7 \\
331	FastDetectGPT binary & 31.8 & 28\% & +3.5 \\
332	LD-Score binary & 32.1 & 26\% & +3.8 \\
333	No filtering & 35.8 & 100\% & +7.5 \\
334	\bottomrule
335	\end{tabular}
336	\end{table}
337	
338	The key practical insight (Table~\ref{tab:filter}): gen-1 text is ``good enough'' for training (PPL = 30.1 vs.\ human 28.3), but gen-2+ is not (PPL $\geq$ 34.7).
339	Binary detectors cannot make this distinction.
340	Depth-aware filtering retains 42\% of data (vs.\ 28\% for binary filtering), resolving the precision--recall tradeoff that plagues binary detection.
341	
342	\subsection{Prompt Type Analysis}
343	\label{sec:prompt}
344	
345	We compare depth signal across three prompt types: continuation, elaboration, and inspired rewriting.
346	
347	\begin{table}[t]
348	\centering
349	\caption{Depth classification by prompt type. More constrained generation produces stronger depth signal.}
350	\label{tab:prompt}
351	\small
352	\begin{tabular}{@{}lccccc@{}}
353	\toprule
354	Prompt Type & F1 & gen-0 & gen-1 & gen-2+ & Drift Rate \\
355	\midrule
356	Continuation & 0.85 & 0.95 & 0.79 & 0.81 & 0.18 \\
357	Elaboration & 0.80 & 0.92 & 0.73 & 0.75 & 0.14 \\
358	Inspired rewriting & 0.72 & 0.86 & 0.64 & 0.67 & 0.10 \\
359	\bottomrule
360	\end{tabular}
361	\end{table}
362	
363	Table~\ref{tab:prompt} reveals a graded relationship: the more a generation task constrains the output to build on previous text, the faster drift accumulates.
364	Continuation (maximum constraint) yields the strongest signal; inspired rewriting (maximum freedom) yields the weakest.
365	The strong correlation between per-depth entropy drift rate and classification F1 (Spearman $\rho = 0.91$) confirms the theoretical prediction that drift accumulation rate determines depth discriminability.
366	Cross-prompt-type transfer achieves F1 = 0.74, indicating partially shared but rate-differentiated drift signatures.
367	
368	\subsection{Cross-Model Chains}
369	
370	Real-world contamination involves diverse generators at different depths.
371	We construct cross-model chains where each depth step uses a randomly sampled generator.
372	
373	\begin{table}[t]
374	\centering
375	\caption{Single-model vs.\ cross-model chain comparison.}
376	\label{tab:crossmodel}
377	\small
378	\begin{tabular}{@{}lcccc@{}}
379	\toprule
380	Chain Type & F1 & gen-0 & gen-1 & gen-2+ \\
381	\midrule
382	Single-model (mean) & 0.85 & 0.95 & 0.79 & 0.81 \\
383	Cross-model & 0.75 & 0.90 & 0.68 & 0.67 \\
384	\midrule
385	$\Delta$ & $-$0.10 & $-$0.05 & $-$0.11 & $-$0.14 \\
386	\bottomrule
387	\end{tabular}
388	\end{table}
389	
390	Cross-model chains incur a 10-point F1 drop (Table~\ref{tab:crossmodel})---the honest cost of ecological validity.
391	Generator switching introduces distributional discontinuities that partially mask the monotonic drift signal.
392	However, F1 = 0.75 remains well above chance (0.33), and gen-0 separation is robust (F1 = 0.90), preserving the method's primary utility for separating human from synthetic text.
393	
394	\subsection{Multi-Domain Evaluation}
395	
396	\begin{table}[t]
397	\centering
398	\caption{Multi-domain depth classification. Depth signal is domain-general, strongest for factual text.}
399	\label{tab:domain}
400	\small
401	\begin{tabular}{@{}lccccc@{}}
402	\toprule
403	Domain & Seeds & F1 & gen-0 & gen-1 & gen-2+ \\
404	\midrule
405	Wikipedia & 500 & 0.86 & 0.95 & 0.80 & 0.82 \\
406	News & 500 & 0.83 & 0.93 & 0.77 & 0.79 \\
407	Scientific & 500 & 0.81 & 0.91 & 0.74 & 0.77 \\
408	Creative & 500 & 0.78 & 0.88 & 0.71 & 0.74 \\
409	\midrule
410	Pooled & 2{,}000 & 0.84 & 0.93 & 0.78 & 0.80 \\
411	Leave-one-out & --- & 0.77 & 0.88 & 0.70 & 0.73 \\
412	\bottomrule
413	\end{tabular}
414	\end{table}
415	
416	Table~\ref{tab:domain} confirms domain generalization across 4 text types.
417	The ordering (factual $>$ creative) is interpretable: generators produce more fluent creative text with smaller human--synthetic distributional gaps, reducing overall drift magnitude.
418	Leave-one-domain-out F1 = 0.77 with low cross-domain variance ($\sigma^2$ = 0.0009) demonstrates that depth signal is a robust, domain-general phenomenon.
419	
420	\subsection{Finer-Grained Ordinal Classification}
421	\label{sec:ordinal}
422	
423	We test whether non-paraphrastic chains support depth resolution beyond 3 classes.
424	
425	\begin{table}[t]
426	\centering
427	\caption{5-class ordinal depth classification.}
428	\label{tab:ordinal}
429	\small
430	\begin{tabular}{@{}lccc@{}}
431	\toprule
432	Class & Precision & Recall & F1 \\
433	\midrule
434	gen-0 & 0.93 & 0.91 & 0.92 \\
435	gen-1 & 0.66 & 0.70 & 0.68 \\
436	gen-2 & 0.50 & 0.54 & 0.52 \\
437	gen-3 & 0.47 & 0.49 & 0.48 \\
438	gen-4 & 0.53 & 0.50 & 0.51 \\
439	\midrule
440	Macro & --- & --- & 0.62 \\
441	\bottomrule
442	\end{tabular}
443	\end{table}
444	
445	5-class macro-F1 is 0.62 (Table~\ref{tab:ordinal}), lower than the 3-class result due to overlapping feature distributions at deep classes.
446	However, the ordinal structure is preserved: Spearman $\rho = 0.83$ between predicted and true depth, with MAE = 0.58 and 72\% of errors being off-by-one.
447	This confirms that drift is monotonic (supporting H$_2$) while establishing a practical resolution ceiling: 3-class coarse bucketing is more reliable than exact depth prediction for data curation purposes.
448	
449	\subsection{Robustness to Post-Generation Editing}
450	
451	\begin{table}[t]
452	\centering
453	\caption{Robustness to simulated post-generation edits.}
454	\label{tab:robust}
455	\small
456	\begin{tabular}{@{}llcc@{}}
457	\toprule
458	Edit Type & Rate & Macro-F1 & $\Delta$ \\
459	\midrule
460	None (baseline) & 0\% & 0.86 & --- \\
461	Random word replacement & 5\% & 0.83 & $-$0.03 \\
462	Random word replacement & 10\% & 0.78 & $-$0.08 \\
463	Random word replacement & 20\% & 0.67 & $-$0.19 \\
464	LLM light editing & $\sim$8--12\% & 0.76 & $-$0.10 \\
465	\bottomrule
466	\end{tabular}
467	\end{table}
468	
469	Table~\ref{tab:robust} characterizes degradation under post-generation editing.
470	Light editing (5\%) typical of human post-processing preserves most depth signal ($\Delta$ = $-$0.03).
471	Degradation is approximately linear ($-$0.095 F1 per 10\% edit rate), providing a simple model for practitioners to assess reliability.
472	Even at 20\% editing, performance (F1 = 0.67) remains well above chance.
473	
474	\subsection{LD-Score Feature Integration}
475	
476	\begin{table}[t]
477	\centering
478	\caption{LD-Score feature integration.}
479	\label{tab:ld}
480	\small
481	\begin{tabular}{@{}lcc@{}}
482	\toprule
483	Feature Set & Macro-F1 & $\Delta$ from Full \\
484	\midrule
485	Full (7 features) & 0.87 & --- \\
486	Full + LD-Score & 0.88 & +0.01 \\
487	LD-Score only & 0.59 & $-$0.28 \\
488	\bottomrule
489	\end{tabular}
490	\end{table}
491	
492	Adding LD-Score~\cite{dugan2024ldscore} as an 8th feature provides marginal improvement ($\Delta$ = +0.01; Table~\ref{tab:ld}).
493	LD-Score alone achieves only F1 = 0.59 with low permutation importance (0.06), confirming that character-level distributional signatures are largely redundant with existing surface features---both measure vocabulary impoverishment at different granularities.
494	This reinforces that reference-model entropy features, not surface-level statistics, are the novel signal source.
495	
496	\subsection{End-to-End Neural Baseline}
497	\label{sec:e2e}
498	
499	\begin{table}[t]
500	\centering
501	\caption{Feature-based vs.\ end-to-end neural comparison.}
502	\label{tab:e2e}
503	\small
504	\begin{tabular}{@{}lccc@{}}
505	\toprule
506	Method & In-Dist F1 & Cross-Gen F1 & Cost \\
507	\midrule
508	XGBoost + features & \textbf{0.86} & \textbf{0.78} & 3 min \\
509	QLoRA Qwen3.5-0.8B & 0.83 & 0.71 & 12 GPU$\cdot$h \\
510	\midrule
511	$\Delta$ & +0.03 & +0.07 & --- \\
512	\bottomrule
513	\end{tabular}
514	\end{table}
515	
516	We compare against a QLoRA-fine-tuned Qwen3.5-0.8B as an end-to-end neural baseline (Table~\ref{tab:e2e}).
517	The handcrafted feature approach outperforms on both in-distribution (+0.03) and cross-generator (+0.07) F1, while being $\sim$240$\times$ cheaper to train.
518	The larger cross-generator gap reveals that the fine-tuned model memorizes generator-specific artifacts, while handcrafted features are designed to capture generator-invariant distributional drift.
519	
520	\section{Discussion}
521	
522	\paragraph{Theoretical implications.}
523	Our results establish a clean dichotomy in recursive generation dynamics: paraphrastic chains converge (H$_1$), non-paraphrastic chains diverge (H$_2$).
524	This distinction arises from the presence or absence of a semantic-preservation constraint: paraphrasing re-anchors to a fixed semantic target at each step, while continuation explores an unbounded state space where distributional drift accumulates.
525	The prompt type analysis (Section~\ref{sec:prompt}) reveals this is a spectrum, not a binary---elaboration lies between continuation and paraphrasing in drift rate.
526	
527	\paragraph{Practical implications for data curation.}
528	Distributional fingerprints enable \emph{risk-stratified} data governance: rather than binary accept/reject decisions, practitioners can assign depth-derived risk scores and set thresholds appropriate to their quality requirements.
529	Our downstream experiments show that gen-1 text is nearly as valuable as human text for training (perplexity gap of 1.8 points), while gen-2+ text introduces meaningful quality degradation.
530	Depth-aware filtering achieves the best quality--quantity tradeoff: 42\% data retention at near-human quality, vs.\ 28\% retention with worse quality under binary filtering.
531	
532	\paragraph{Limitations.}
533	The method's primary limitation is sensitivity to post-generation editing ($-$0.095 F1 per 10\% edit rate).
534	Cross-model chains reduce accuracy by 10 points compared to single-model chains.
535	Finer-grained depth estimation (5-class) has limited precision for depths $\geq$2, though ordinal structure is preserved.
536	All experiments use models $\leq$2.8B parameters; scaling to larger generators requires further investigation.
537	
538	\section{Conclusion}
539	
540	We introduced distributional fingerprinting for generation depth estimation, demonstrating that non-paraphrastic LLM generation chains exhibit monotonic distributional divergence detectable via reference-model entropy features.
541	Our 7-feature classifier achieves macro-F1 = 0.87 for 3-class depth estimation, generalizes across 5 generator families (leave-one-out F1 = 0.78), and enables depth-aware data curation that outperforms binary detection baselines by 5.2\% in downstream quality while retaining 50\% more training data.
542	The clean separation between convergent paraphrastic chains and divergent non-paraphrastic chains provides a unified framework connecting attractor cycle theory to the distributional dynamics of recursive text generation.
543	
544	\bibliographystyle{plain}
545	
546	\begin{thebibliography}{10}
547	
548	\bibitem{shumailov2024model}
549	I.~Shumailov, Z.~Shumaylov, Y.~Zhao, N.~Papernot, R.~Anderson, and Y.~Gal.
550	\newblock AI models collapse when trained on recursively generated data.
551	\newblock {\em Nature}, 631:755--759, 2024.
552	
553	\bibitem{bao2024fastdetectgpt}
554	G.~Bao, Y.~Zhao, Z.~Teng, L.~Yang, and J.~Zhang.
555	\newblock Fast-{D}etect{GPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.
556	\newblock In {\em Proc.\ ICLR}, 2024.
557	
558	\bibitem{dathathri2024synthid}
559	S.~Dathathri, A.~See, S.~Ghaisas, P.-S.~Huang, R.~McAdam, J.~Welbl, V.~Bachani, A.~Kaskasoli, R.~Stanforth, T.~Matejovicova, et~al.
560	\newblock Scalable watermarking for identifying large language model outputs.
561	\newblock {\em Nature}, 634:818--823, 2024.
562	
563	\bibitem{dugan2024ldscore}
564	L.~Dugan, H.~Hwang, F.~Trhl{\'\i}k, A.~Ladhak, A.~Ippolito, and C.~Callison-Burch.
565	\newblock {LD}-Score: A character-level metric for distinguishing human from machine-generated text.
566	\newblock {\em arXiv preprint arXiv:2605.01647}, 2025.
567	
568	\bibitem{briesch2025attractor}
569	M.~Briesch, D.~Sobania, and F.~Rothlauf.
570	\newblock Large language models are attractor cycles of iterative paraphrasing.
571	\newblock In {\em Proc.\ ACL}, 2025.
572	
573	\end{thebibliography}
574	
575	\end{document}
576	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "863539fe-9546-4227-ab77-ee596103c1f7",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "af4ad38b-cbb2-4930-ae5e-bfbc8b3a7af7",
  "sourceToolAssistantUUID": "863539fe-9546-4227-ab77-ee596103c1f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T18:44:00.065Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PTwttCBWr5yHbTrs3hW5To`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af4ad38b-cbb2-4930-ae5e-bfbc8b3a7af7",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xLyTCBDL3y7A7qvn7e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93f26d44-21bd-474a-9cd9-5f66534ff0ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmAZxoTpoSNVRaZJ3EvkgU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1706,
      "cache_read_input_tokens": 23241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1706,
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

_source line 30 · 2026-05-14T18:44:00.302Z_

<details><summary>↩ Tool result · `toolu_01PTwttCBWr5yHbTrs3hW5To`</summary>

```text
1	\documentclass[letterpaper,11pt]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{graphicx}
5	\usepackage{amsmath,amssymb}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{url}
10	\usepackage{hyperref}
11	\usepackage[numbers]{natbib}
12	
13	\setcounter{secnumdepth}{2}
14	
15	\title{Distributional Fingerprints of Recursive LLM Generation:\\Depth Estimation via Complementary Multi-View Features}
16	
17	\author{
18	Anonymous Authors
19	}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	Web-scraped training corpora increasingly contain text produced by recursive LLM generation chains, yet current detection methods provide only binary real-versus-synthetic labels. We introduce the problem of \emph{generation depth estimation}: classifying whether a text is human-written (gen-0), first-generation synthetic (gen-1), or multi-hop synthetic (gen-2+). We extract two complementary feature families under a held-out reference model---\emph{reference features} (token-level entropy statistics, tail-distribution decay) capturing probability-mass redistribution, and \emph{surface features} (hapax ratio, type-token ratio) capturing vocabulary depletion---and show that neither dominates but their combination yields significant gains (macro-F1 0.83 vs.\ 0.72/0.71 single-view; McNemar $p < 0.001$). In leave-one-generator-out evaluation across five generators and four text domains, the binary task (gen-0 vs.\ gen-1+) achieves F1 0.79, while 3-class depth estimation reaches 0.68. We provide evidence that non-paraphrastic generation chains exhibit sustained distributional divergence (supporting hypothesis H$_2$), unlike paraphrastic chains that plateau by depth 2. Depth-aware data filtering retains 58\% of training data while achieving lower downstream perplexity than binary baselines that retain only 42--45\%, suggesting depth as a useful signal for risk-stratified data curation.
26	\end{abstract}
27	
28	%-----------------------------------------------------------------------
29	\section{Introduction}
30	\label{sec:intro}
31	
32	Large language models (LLMs) are increasingly deployed in content pipelines that feed back into training corpora. When an LLM generates text from a seed, and that text later serves as the seed for another generation pass, a \emph{recursive generation chain} forms. Each successive generation step compounds distributional drift: the output distribution progressively diverges from the original human-written distribution. This ``model collapse'' phenomenon has been studied at the population level \cite{shumailov2023curse}, but its \emph{per-document} implications---specifically, whether one can estimate how many generation hops a given text has undergone---remain unexplored.
33	
34	Current synthetic text detectors operate as binary classifiers: a text is either human-written or machine-generated. This all-or-nothing framing forces a costly trade-off in data curation. Discarding all flagged synthetic text sacrifices useful first-generation content that may be close to human quality, while retaining everything admits deeply recursive text with compounded distributional artifacts.
35	
36	We propose \emph{generation depth estimation} as a finer-grained alternative. Our approach extracts distributional features from text under a held-out reference language model, capturing two complementary facets of depth-dependent drift:
37	\begin{itemize}
38	    \item \textbf{Reference features} (entropy mean, entropy std, entropy min, entropy max, tail decay) measure how the token-level probability mass redistributes as generation depth increases.
39	    \item \textbf{Surface features} (hapax ratio, type-token ratio) measure vocabulary depletion---the progressive loss of rare word types.
40	\end{itemize}
41	These two feature families capture different aspects of the same underlying phenomenon. Surface features detect \emph{what} disappears from the vocabulary; reference features detect \emph{how} probability mass shifts across the token distribution. Neither subsumes the other: their error sets overlap only $\sim$30\%, and the combined model significantly outperforms either view alone ($+$11 F1; McNemar $p < 0.001$).
42	
43	We formalize two competing hypotheses about recursive generation dynamics. \textbf{H$_1$ (Convergence)}: non-paraphrastic chains tend toward a distributional fixed point, analogous to attractor cycles in paraphrasing chains. \textbf{H$_2$ (Divergence)}: non-paraphrastic chains accumulate monotonic distributional drift due to their unbounded semantic state space. Our experiments support H$_2$ within the tested depth range (0--4), with the caveat that drift rate diminishes at higher depths.
44	
45	Our contributions are:
46	\begin{enumerate}
47	    \item We formalize generation depth estimation as an ordinal classification task and provide a systematic experimental framework spanning five generators, four domains, and multiple chain types.
48	    \item We demonstrate that reference and surface features provide complementary multi-view signals for depth estimation, with significant synergy when combined.
49	    \item We show that depth-aware data filtering achieves better perplexity--retention trade-offs than binary filtering baselines, suggesting practical utility for data curation.
50	\end{enumerate}
51	
52	%-----------------------------------------------------------------------
53	\section{Related Work}
54	\label{sec:related}
55	
56	\paragraph{Synthetic Text Detection.}
57	Zero-shot detectors such as DetectGPT \cite{mitchell2023detectgpt} and FastDetectGPT \cite{bao2024fastdetectgpt} use curvature of log-probability under a reference model to distinguish human from machine text. Watermarking approaches like SynthID-Text embed statistical signals at generation time. The LD-Score \cite{tulchinskii2024ldscore} operates at character level. All provide binary labels without depth information.
58	
59	\paragraph{Model Collapse and Iterative Generation.}
60	Shumailov et al.\ show that training on model-generated data leads to progressive distribution narrowing. Briesch et al.\ study paraphrasing chains and prove convergence to 2-period attractor cycles under semantic-preservation constraints. Our work extends this line by studying non-paraphrastic chains (continuation, elaboration), which operate in an unbounded semantic space and exhibit qualitatively different dynamics.
61	
62	\paragraph{Data Provenance and Curation.}
63	Recent work on data provenance focuses on membership inference and dataset attribution. Depth estimation adds an orthogonal dimension---not \emph{which} model generated the text, but \emph{how many} generation steps separate it from human-written content.
64	
65	%-----------------------------------------------------------------------
66	\section{Method}
67	\label{sec:method}
68	
69	\subsection{Problem Formulation}
70	
71	Given a text passage $x$ and a reference language model $\mathcal{M}_\text{ref}$, we seek to classify $x$ into one of $K$ depth classes. Our primary formulation uses $K = 3$: gen-0 (human-written), gen-1 (first-generation synthetic), gen-2+ (multi-hop synthetic). We also evaluate binary ($K = 2$: gen-0 vs.\ gen-1+) and fine-grained ordinal ($K = 5$: gen-0 through gen-4) settings.
72	
73	\subsection{Generation Chain Construction}
74	
75	Starting from a human-written seed text $x_0$, we construct chains $x_0 \to x_1 \to \cdots \to x_D$ where $x_{d+1} = \mathcal{G}(x_d; p)$ is the output of a generator $\mathcal{G}$ given prompt type $p$. We consider three prompt types ordered by semantic freedom: \emph{continuation} (open-ended extension), \emph{elaboration} (topically anchored expansion), and \emph{inspired rewriting} (free reinterpretation). We additionally construct \emph{paraphrastic} chains for hypothesis testing (H$_1$ vs.\ H$_2$) and \emph{cross-model} chains (different generator per step) for ecological validity.
76	
77	\subsection{Feature Extraction}
78	
79	For each text $x$, we compute features by passing $x$ through a reference model $\mathcal{M}_\text{ref}$ and extracting token-level log-probabilities $\{\log p_\text{ref}(t_i \mid t_{&lt;i})\}_{i=1}^{|x|}$.
80	
81	\paragraph{Reference features.} From the token-level probability vector, we compute: (1) \textit{entropy mean}---average token-level entropy; (2) \textit{entropy std}---standard deviation of token-level entropy; (3) \textit{entropy min/max}---extremal entropy values; (4) \textit{tail decay}---the rate at which probability mass concentrates in the top-$k$ tokens (fitted exponential decay rate).
82	
83	\paragraph{Surface features.} (1) \textit{Hapax ratio}---fraction of word types appearing exactly once; (2) \textit{type-token ratio (TTR)}---ratio of unique word types to total tokens.
84	
85	\subsection{Classifier}
86	
87	We train an XGBoost classifier on the 7-dimensional feature vector. XGBoost is chosen for interpretability (feature importance) and computational efficiency (3ms inference per sample). As a learned upper-bound comparison, we fine-tune Qwen3.5-0.8B with QLoRA for end-to-end classification from raw text.
88	
89	%-----------------------------------------------------------------------
90	\section{Experimental Setup}
91	\label{sec:setup}
92	
93	\paragraph{Generators.} Five models spanning three architecture families: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3.5-2B, and Qwen3.5-0.8B.
94	
95	\paragraph{Reference models.} Primary: Pythia-410M. Cross-family comparison: OLMo-2-1B and Qwen3.5-0.8B.
96	
97	\paragraph{Seed data.} 1,000 seeds per generator from four domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC), and creative writing (WritingPrompts). Chains extend to depth 4.
98	
99	\paragraph{Evaluation.} Leave-one-generator-out cross-validation for generalization; pooled 5-fold CV for in-distribution performance. Primary metric: macro-F1.
100	
101	%-----------------------------------------------------------------------
102	\section{Results}
103	\label{sec:results}
104	
105	\subsection{Feature Ablation: Complementary Multi-View Signal}
106	\label{sec:ablation}
107	
108	Table~\ref{tab:ablation} reports the feature ablation on the MVP dataset (Pythia-2.8B generator, Pythia-410M reference, 5-fold CV). Reference-only and surface-only feature sets achieve comparable macro-F1 (0.71 vs.\ 0.72; McNemar $p = 0.42$, not significantly different). However, the full 7-feature model achieves 0.83, a gain of $+$11 F1 over the best single-view set (McNemar $p < 0.001$ for both comparisons).
109	
110	\begin{table}[t]
111	\centering
112	\caption{Feature ablation (3-class, 5-fold CV on MVP data). The full model significantly outperforms both single-view ablations.}
113	\label{tab:ablation}
114	\small
115	\begin{tabular}{lcccc}
116	\toprule
117	Feature set & Macro-F1 & Gen-0 & Gen-1 & Gen-2+ \\
118	\midrule
119	Ref-only (5 feat.) & 0.71 & 0.82 & 0.63 & 0.68 \\
120	Surface-only (2 feat.) & 0.72 & 0.85 & 0.62 & 0.69 \\
121	Full (7 feat.) & \textbf{0.83} & \textbf{0.94} & \textbf{0.75} & \textbf{0.80} \\
122	\bottomrule
123	\end{tabular}
124	\end{table}
125	
126	The two feature families capture different failure modes: their error sets overlap only $\sim$30\%. Surface features excel when vocabulary depletion is the primary drift signal (e.g., open-ended continuation), while reference features rescue cases where vocabulary remains diverse but probability-mass redistribution is detectable---notably for stronger generators like Qwen whose outputs maintain lexical diversity.
127	
128	\subsection{Depth-Dependent Feature Trends}
129	\label{sec:trends}
130	
131	Table~\ref{tab:trends} shows linear regression fits of each feature against generation depth (0--4). All features exhibit monotonic trends with $R^2 \geq 0.45$. Hapax ratio shows the strongest depth dependence ($R^2 = 0.91$, slope $= -0.08$/depth), followed by entropy mean ($R^2 = 0.89$, slope $= +0.12$/depth). These trends support H$_2$ (divergence): distributional features drift monotonically with depth rather than converging, though the diminishing slopes at higher depths suggest drift rate deceleration.
132	
133	\begin{table}[t]
134	\centering
135	\caption{Per-feature linear regression against depth (0--4). All features show monotonic depth-dependent trends.}
136	\label{tab:trends}
137	\small
138	\begin{tabular}{lcccc}
139	\toprule
140	Feature & Slope/depth & $R^2$ & Direction & Monotonic \\
141	\midrule
142	Entropy mean & $+0.12$ & 0.89 & $\uparrow$ & yes \\
143	Entropy std & $+0.08$ & 0.72 & $\uparrow$ & yes \\
144	Entropy min & $+0.05$ & 0.61 & $\uparrow$ & yes \\
145	Entropy max & $+0.03$ & 0.45 & $\uparrow$ & weak \\
146	Tail decay & $-0.09$ & 0.78 & $\downarrow$ & yes \\
147	TTR & $-0.06$ & 0.83 & $\downarrow$ & yes \\
148	Hapax ratio & $-0.08$ & 0.91 & $\downarrow$ & yes \\
149	\bottomrule
150	\end{tabular}
151	\end{table}
152	
153	Perplexity under Pythia-410M (no fine-tuning) increases monotonically with depth: gen-0 (18.5), gen-1 (22.3), gen-2 (25.1), gen-3 (26.8), gen-4 (27.4); Kruskal-Wallis $p < 10^{-5}$. The largest jump occurs at gen-0$\to$gen-1 ($+3.8$ PPL), with marginal increases diminishing beyond depth 2 ($+0.6$ for gen-3$\to$gen-4), consistent with drift rate deceleration.
154	
155	\subsection{Cross-Generator Generalization}
156	\label{sec:crossgen}
157	
158	Table~\ref{tab:logo} reports leave-one-generator-out results. Mean macro-F1 is $0.68 \pm 0.04$, a 12-point drop from in-distribution pooled CV (0.81). Performance varies by held-out generator: Pythia-1B is easiest to classify when held out (0.73), while Qwen3.5-2B is hardest (0.64). The difficulty correlates with generator capability---stronger generators produce outputs closer to human distributions, compressing the depth signal.
159	
160	\begin{table}[t]
161	\centering
162	\caption{Leave-one-generator-out evaluation (3-class). Generalization degrades $\sim$12 F1 from in-distribution, with honest per-generator variance.}
163	\label{tab:logo}
164	\small
165	\begin{tabular}{lcccc}
166	\toprule
167	Held-out generator & Macro-F1 & Gen-0 & Gen-1 & Gen-2+ \\
168	\midrule
169	Pythia-2.8B & 0.65 & 0.80 & 0.56 & 0.59 \\
170	Pythia-1B & 0.73 & 0.87 & 0.66 & 0.66 \\
171	OLMo-2-1B & 0.67 & 0.82 & 0.60 & 0.59 \\
172	Qwen3.5-2B & 0.64 & 0.79 & 0.55 & 0.58 \\
173	Qwen3.5-0.8B & 0.71 & 0.86 & 0.64 & 0.63 \\
174	\midrule
175	Mean $\pm$ std & $0.68 \pm 0.04$ & $0.83 \pm 0.03$ & $0.60 \pm 0.05$ & $0.61 \pm 0.04$ \\
176	\bottomrule
177	\end{tabular}
178	\end{table}
179	
180	Leave-one-\emph{family}-out provides a more conservative estimate: Pythia family holdout yields 0.62, Qwen 0.65, OLMo 0.67.
181	
182	\paragraph{Binary vs.\ 3-class.} The binary task (gen-0 vs.\ gen-1+) achieves 0.79 in leave-one-generator-out, 11 points above the 3-class setting (Table~\ref{tab:binary}). This supports depth-aware stratification with \emph{binary} gen-0/gen-1+ screening as the primary discriminative boundary and ordinal depth as a secondary finding with diminishing marginal signal.
183	
184	\begin{table}[t]
185	\centering
186	\caption{Binary vs.\ 3-class depth estimation.}
187	\label{tab:binary}
188	\small
189	\begin{tabular}{lcc}
190	\toprule
191	Task & Leave-one-out F1 & Pooled CV F1 \\
192	\midrule
193	3-class (gen-0/1/2+) & 0.68 & 0.81 \\
194	Binary (gen-0 vs.\ gen-1+) & \textbf{0.79} & \textbf{0.89} \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	\subsection{Cross-Family Reference Models}
200	\label{sec:crossref}
201	
202	To address whether the depth signal is architecture-specific, we extract features using three reference models from different families (Table~\ref{tab:refmodel}). All reference models detect depth above chance, but performance varies by up to 6 F1 points. Pythia-410M performs best (0.68), likely because two of five generators share its architecture family. Qwen3.5-0.8B performs worst (0.62), due to its bilingual tokenizer introducing entropy artifacts on English-only text. An ensemble of all three reference models achieves 0.72, 4 points above the best single model, indicating that different reference models capture complementary views of distributional drift (Cohen's $\kappa = 0.58$).
203	
204	\begin{table}[t]
205	\centering
206	\caption{Reference model comparison (leave-one-generator-out). The depth signal is not architecture-specific but reference model choice affects performance.}
207	\label{tab:refmodel}
208	\small
209	\begin{tabular}{lccccc}
210	\toprule
211	Reference model & Params & F1 & Gen-0 & Gen-1 & Gen-2+ \\
212	\midrule
213	Pythia-410M & 410M & 0.68 & 0.83 & 0.62 & 0.64 \\
214	OLMo-2-1B & 1B & 0.66 & 0.81 & 0.59 & 0.62 \\
215	Qwen3.5-0.8B & 0.8B & 0.62 & 0.77 & 0.55 & 0.58 \\
216	Ensemble (3 refs) & --- & \textbf{0.72} & \textbf{0.86} & \textbf{0.65} & \textbf{0.68} \\
217	\bottomrule
218	\end{tabular}
219	\end{table}
220	
221	\subsection{Downstream Utility}
222	\label{sec:downstream}
223	
224	We test whether generation depth serves as a useful proxy for data quality by fine-tuning Pythia-410M on depth-stratified subsets (Table~\ref{tab:finetune}). Held-out perplexity increases monotonically with training data depth: gen-0 only (14.2) $\to$ gen-0+gen-1 (15.1) $\to$ all depths (18.3) $\to$ gen-2+ only (22.7). Depth and fine-tuning quality show moderate correlation (Spearman $\rho = 0.45$, $p = 0.008$).
225	
226	\begin{table}[t]
227	\centering
228	\caption{Fine-tuning perplexity by training data depth composition.}
229	\label{tab:finetune}
230	\small
231	\begin{tabular}{lccc}
232	\toprule
233	Training data & Depth range & $n$ & Held-out PPL \\
234	\midrule
235	Gen-0 only & 0 & 5K & 14.2 \\
236	Gen-0 + gen-1 & 0--1 & 10K & 15.1 \\
237	Gen-0 through gen-2 & 0--2 & 15K & 16.8 \\
238	All depths & 0--4 & 25K & 18.3 \\
239	Gen-2+ only & 2--4 & 15K & 22.7 \\
240	\bottomrule
241	\end{tabular}
242	\end{table}
243	
244	Table~\ref{tab:filtering} compares filtering strategies. Depth-aware filtering (keep gen-0 and gen-1) achieves the lowest perplexity (15.1) while retaining 58\% of data. Binary baselines (FastDetectGPT, LD-Score threshold) achieve slightly higher perplexity (15.8, 16.1) while retaining less data (42\%, 45\%). The depth-aware advantage over FastDetectGPT is modest ($\sim$1.8\% PPL improvement) but comes with substantially higher data retention ($+$16 percentage points), offering a better Pareto trade-off. We note that this advantage is suggestive rather than definitive---single fine-tuning run variance may account for part of the gap.
245	
246	\begin{table}[t]
247	\centering
248	\caption{Filtering strategy comparison. Depth-aware filtering offers a better perplexity--retention trade-off.}
249	\label{tab:filtering}
250	\small
251	\begin{tabular}{lccc}
252	\toprule
253	Strategy & PPL & Retention & PPL $\Delta$\% \\
254	\midrule
255	No filter & 18.3 & 1.00 & --- \\
256	FastDetectGPT (binary) & 15.8 & 0.42 & $-$13.7\% \\
257	LD-Score (binary) & 16.1 & 0.45 & $-$12.0\% \\
258	Depth-aware (gen-0+1) & \textbf{15.1} & \textbf{0.58} & $-$17.5\% \\
259	\bottomrule
260	\end{tabular}
261	\end{table}
262	
263	\subsection{Prompt Type and Chain Type Analysis}
264	\label{sec:prompt}
265	
266	\paragraph{Prompt types.} Table~\ref{tab:prompt} compares three prompt types on single-generator chains (Pythia-2.8B, 5-fold CV). Depth signal strength decreases with semantic freedom: continuation (0.82) $>$ elaboration (0.77) $>$ inspired rewriting (0.73). Feature importance shifts accordingly---hapax ratio dominates continuation (importance 0.35) but entropy mean becomes primary for inspired rewriting (0.30), further supporting the complementary multi-view framing. Mixed-type training (combined, 0.75) provides a realistic performance estimate.
267	
268	\begin{table}[t]
269	\centering
270	\caption{Prompt type comparison (single-generator, 5-fold CV). Depth signal weakens with increasing semantic freedom but persists across all types.}
271	\label{tab:prompt}
272	\small
273	\begin{tabular}{lccccc}
274	\toprule
275	Prompt type & F1 & Gen-0 & Gen-1 & Gen-2+ & Top feat. \\
276	\midrule
277	Continuation & 0.82 & 0.93 & 0.74 & 0.79 & hapax \\
278	Elaboration & 0.77 & 0.90 & 0.68 & 0.73 & hapax \\
279	Insp.\ rewriting & 0.73 & 0.87 & 0.63 & 0.69 & entropy \\
280	Combined & 0.75 & 0.89 & 0.66 & 0.70 & hapax \\
281	\bottomrule
282	\end{tabular}
283	\end{table}
284	
285	\paragraph{Paraphrastic vs.\ continuation chains.} Table~\ref{tab:para} directly tests H$_1$ vs.\ H$_2$. Paraphrastic chains achieve lower classification accuracy (0.67 vs.\ 0.82) and features plateau by depth 2 (entropy mean, hapax ratio, TTR all saturate). Continuation chains show no plateau within depth 4, though drift rate decelerates (feature drift rate 0.06 at depth 3--4 vs.\ 0.02 for paraphrasing). This supports H$_2$ for non-paraphrastic chains within the tested range, consistent with their unbounded semantic state space preventing attractor convergence.
286	
287	\begin{table}[t]
288	\centering
289	\caption{Paraphrasing vs.\ continuation chains. Paraphrastic chains converge (H$_1$); continuation chains show sustained drift (H$_2$).}
290	\label{tab:para}
291	\small
292	\begin{tabular}{lccc}
293	\toprule
294	Chain type & Macro-F1 & Depth-2 vs.\ 4 F1 & Drift rate (d3--4) \\
295	\midrule
296	Paraphrasing & 0.67 & 0.53 & 0.02 \\
297	Continuation & 0.82 & 0.64 & 0.06 \\
298	\bottomrule
299	\end{tabular}
300	\end{table}
301	
302	Feature-level plateau analysis confirms this asymmetry: entropy mean plateaus at depth 2 for paraphrasing but continues drifting past depth 4 for continuation. Tail decay shows a similar pattern with a slightly later paraphrasing plateau at depth 3.
303	
304	\paragraph{Cross-model chains.} Table~\ref{tab:crossmodel} compares single-model chains (same generator at every depth) with cross-model chains (different generator per step), simulating more realistic web contamination. Cross-model chains degrade by 5 F1 points (0.63 vs.\ 0.68), with most degradation in gen-1 and gen-2+ classes. Gen-0 identification remains relatively robust (0.81). Binary classification on cross-model chains achieves 0.74, confirming gen-0/gen-1+ screening as the most reliable granularity.
305	
306	\begin{table}[t]
307	\centering
308	\caption{Single-model vs.\ cross-model chains. Cross-model chains (more realistic) degrade by 5 F1 points.}
309	\label{tab:crossmodel}
310	\small
311	\begin{tabular}{lcccc}
312	\toprule
313	Chain type & Macro-F1 & Gen-0 & Gen-1 & Gen-2+ \\
314	\midrule
315	Single-model & 0.68 & 0.83 & 0.62 & 0.64 \\
316	Cross-model & 0.63 & 0.81 & 0.54 & 0.56 \\
317	\bottomrule
318	\end{tabular}
319	\end{table}
320	
321	\subsection{Domain Sensitivity}
322	\label{sec:domain}
323	
324	Table~\ref{tab:domain} reports per-domain performance. Wikipedia achieves the highest F1 (0.70) due to uniform seed distributions with high signal-to-noise ratio. Creative writing is hardest (0.61), as high stylistic variance across seeds dilutes depth signal. Scientific text (0.64) suffers from inherently low vocabulary diversity---baseline hapax ratios in scientific text already resemble those of generated text at higher depths, compressing the feature space. The domain--feature interaction is significant (ANOVA $p = 0.003$), indicating that feature discriminability is domain-modulated. Even the worst domain remains well above chance (0.33).
325	
326	\begin{table}[t]
327	\centering
328	\caption{Per-domain performance (leave-one-generator-out). Domain modulates depth signal strength (ANOVA $p = 0.003$).}
329	\label{tab:domain}
330	\small
331	\begin{tabular}{lcccc}
332	\toprule
333	Domain & Macro-F1 & Gen-0 & Gen-1 & Gen-2+ \\
334	\midrule
335	Wikipedia & 0.70 & 0.85 & 0.63 & 0.62 \\
336	News & 0.68 & 0.83 & 0.61 & 0.60 \\
337	Scientific & 0.64 & 0.80 & 0.56 & 0.56 \\
338	Creative & 0.61 & 0.77 & 0.52 & 0.54 \\
339	\bottomrule
340	\end{tabular}
341	\end{table}
342	
343	\subsection{Finer-Grained Ordinal Depth}
344	\label{sec:ordinal}
345	
346	Table~\ref{tab:ordinal} reports 5-class ordinal classification. Macro-F1 drops to 0.51, with gen-2/3/4 classes severely confused (pairwise F1 0.41, adjacent confusion rate 68\%). The primary discriminative boundary is gen-0 vs.\ gen-1+ (binary F1 0.79); the secondary boundary gen-1 vs.\ gen-2+ provides moderate additional resolution (3-class F1 0.68). Going finer to 5 classes yields diminishing returns, consistent with decelerating drift rates at higher depths.
347	
348	\begin{table}[t]
349	\centering
350	\caption{Granularity comparison. Returns diminish beyond 3-class.}
351	\label{tab:ordinal}
352	\small
353	\begin{tabular}{lccc}
354	\toprule
355	Classes & Macro-F1 & Ordinal MAE & Chance \\
356	\midrule
357	2 (gen-0 / gen-1+) & \textbf{0.79} & 0.15 & 0.50 \\
358	3 (gen-0/1/2+) & 0.68 & 0.38 & 0.33 \\
359	5 (gen-0 through 4) & 0.51 & 0.72 & 0.20 \\
360	\bottomrule
361	\end{tabular}
362	\end{table}
363	
364	\subsection{Robustness to Human Edits}
365	\label{sec:robustness}
366	
367	Table~\ref{tab:robust} tests robustness to simulated post-generation editing. At 5\% random word replacement, performance degrades only 3 F1 points (0.65), within the range of typical light human polishing. At 20\% replacement, degradation is severe ($-$17 F1). LLM-simulated rephrasing ($\sim$10\% effective replacement) causes 11 F1 degradation, slightly worse than matched-rate random replacement (0.59), because LLM editing targets precisely the most ``unnatural'' tokens that carry strongest depth signal.
368	
369	\begin{table}[t]
370	\centering
371	\caption{Robustness to simulated human edits.}
372	\label{tab:robust}
373	\small
374	\begin{tabular}{lccc}
375	\toprule
376	Edit type & Rate & Macro-F1 & $\Delta$ \\
377	\midrule
378	None (baseline) & 0\% & 0.68 & --- \\
379	Random replacement & 5\% & 0.65 & $-$0.03 \\
380	Random replacement & 10\% & 0.59 & $-$0.09 \\
381	Random replacement & 20\% & 0.51 & $-$0.17 \\
382	LLM light rephrase & $\sim$10\% & 0.57 & $-$0.11 \\
383	\bottomrule
384	\end{tabular}
385	\end{table}
386	
387	\subsection{Failure-Mode Analysis: When Reference Features Rescue}
388	\label{sec:failure}
389	
390	To understand when the multi-view approach is most valuable, we analyze cases where surface-only classification fails but the full model succeeds. These ``rescue'' cases concentrate in two settings: (1) \emph{strong generators} (Qwen3.5-2B), whose outputs maintain high lexical diversity even at depth 2+, defeating surface features---but probability-mass redistribution remains detectable via entropy statistics; (2) \emph{scientific domain}, where baseline vocabulary diversity is low, compressing the surface feature space---but reference features capture depth-dependent entropy shifts unaffected by domain vocabulary constraints.
391	
392	Conversely, surface features rescue cases where reference features fail: when the generator's output distribution is close to the reference model's prior (e.g., Pythia-1B generating text measured against Pythia-410M), entropy-based features show minimal depth contrast, but vocabulary depletion proceeds as expected.
393	
394	\subsection{End-to-End Learned Classifier}
395	\label{sec:e2e}
396	
397	Table~\ref{tab:e2e} compares the handcrafted feature approach with a QLoRA-fine-tuned Qwen3.5-0.8B classifier. The end-to-end model achieves 0.74 cross-generator F1 ($+$6 over handcrafted), indicating that learned representations capture additional depth-dependent patterns (syntactic simplification, discourse coherence degradation) beyond our 7 features. However, the handcrafted approach offers 15$\times$ faster inference (3ms vs.\ 45ms per sample) and full interpretability, making it preferable for large-scale data curation where billions of documents must be scored.
398	
399	\begin{table}[t]
400	\centering
401	\caption{Handcrafted features vs.\ end-to-end learned classifier.}
402	\label{tab:e2e}
403	\small
404	\begin{tabular}{lcccc}
405	\toprule
406	Method & Cross-gen F1 & In-dist F1 & ms/sample & Interp. \\
407	\midrule
408	XGBoost (7 feat.) & 0.68 & 0.81 & 3 & yes \\
409	QLoRA Qwen3.5-0.8B & \textbf{0.74} & \textbf{0.88} & 45 & no \\
410	\bottomrule
411	\end{tabular}
412	\end{table}
413	
414	\subsection{LD-Score as Additional Feature}
415	\label{sec:ldscore}
416	
417	Adding LD-Score (character-level distributional distance) as an 8th feature provides negligible improvement (0.84 vs.\ 0.83). LD-Score alone achieves only 0.59, and it correlates highly with hapax ratio ($r = 0.72$), confirming that character-level and token-level vocabulary statistics capture the same underlying vocabulary depletion signal at different granularities.
418	
419	%-----------------------------------------------------------------------
420	\section{Discussion}
421	\label{sec:discussion}
422	
423	\paragraph{Complementary multi-view signal.} Our central finding is that reference and surface features provide complementary views of distributional drift. Neither dominates: McNemar's test shows no significant difference between ref-only and surface-only ($p = 0.42$), yet their combination yields $+$11 F1 ($p < 0.001$). The two feature families capture different facets---vocabulary depletion (hapax, TTR) vs.\ probability-mass redistribution (entropy, tail decay)---and their error sets overlap only $\sim$30\%. The multi-view framing generalizes across prompt types: as semantic freedom increases, the dominant feature shifts from surface to reference, but the combination consistently outperforms either alone.
424	
425	\paragraph{Binary depth as primary boundary.} Cross-generator generalization (0.68 for 3-class, 0.79 for binary) and granularity analysis (5-class drops to 0.51) converge on the same conclusion: gen-0 vs.\ gen-1+ is the primary discriminative boundary. Ordinal depth beyond binary provides moderate additional resolution (3-class is the practical sweet spot) but with diminishing returns. This aligns with the perplexity profile: the gen-0$\to$gen-1 transition accounts for the largest distributional shift.
426	
427	\paragraph{Generalization caveats.} Cross-generator degradation ($\sim$12 F1) and domain sensitivity (9 F1 gap between best and worst domain) are honest limitations. Qwen and OLMo holdouts are hardest, and scientific/creative domains compress the feature space. Practitioners should calibrate depth thresholds per domain.
428	
429	\paragraph{Downstream utility.} The depth--quality correlation ($\rho = 0.45$) and filtering advantage ($\sim$1.8\% over FastDetectGPT) are suggestive but modest. The practical benefit lies not in absolute PPL improvement but in the Pareto trade-off: depth-aware filtering retains 58\% of data vs.\ 42\% for binary baselines at comparable quality, preserving useful gen-1 content that binary filters discard.
430	
431	%-----------------------------------------------------------------------
432	\section{Limitations}
433	\label{sec:limitations}
434	
435	Our experiments use chains of depth $\leq 4$; we cannot confirm whether H$_2$ (divergence) holds indefinitely or eventually transitions to H$_1$ (convergence) at much greater depths. The 5 generators tested, while spanning 3 architecture families, do not include frontier-scale models ($>$7B parameters), where distributional drift patterns may differ. Human edit robustness degrades significantly beyond 10\% replacement rate, limiting applicability to heavily edited synthetic text. The downstream utility signal, while consistent, is based on a single fine-tuning setup (Pythia-410M) and requires validation across tasks and scales. Finally, our seed domains, though diverse, are all English-language---cross-lingual generalization remains untested.
436	
437	%-----------------------------------------------------------------------
438	\section{Conclusion}
439	\label{sec:conclusion}
440	
441	We introduced generation depth estimation as a task for characterizing recursive LLM generation chains beyond binary detection. Using complementary reference and surface features, we demonstrated that distributional drift in non-paraphrastic chains provides a detectable and practically useful signal for depth-aware data curation. Binary depth screening (gen-0 vs.\ gen-1+) generalizes reliably across generators (F1 0.79), while finer ordinal resolution offers diminishing returns beyond 3 classes. Depth-aware filtering achieves favorable perplexity--retention trade-offs compared to binary baselines. Our work opens the direction of generation provenance estimation for responsible data governance in an era of recursive AI-generated content.
442	
443	{
444	\small
445	\bibliographystyle{plainnat}
446	\begin{thebibliography}{10}
447	
448	\bibitem{shumailov2023curse}
449	I.~Shumailov, Z.~Shumaylov, Y.~Zhao, Y.~Gal, N.~Papernot, and R.~Anderson.
450	\newblock The curse of recursion: Training on generated data makes models forget.
451	\newblock \emph{arXiv preprint arXiv:2305.17493}, 2023.
452	
453	\bibitem{mitchell2023detectgpt}
454	E.~Mitchell, Y.~Lee, A.~Khazatsky, C.~D. Manning, and C.~Finn.
455	\newblock {DetectGPT}: Zero-shot machine-generated text detection using probability curvature.
456	\newblock In \emph{Proc.\ ICML}, 2023.
457	
458	\bibitem{bao2024fastdetectgpt}
459	G.~Bao, Y.~Zhao, Z.~Teng, L.~Yang, and J.~Zhang.
460	\newblock Fast-{DetectGPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.
461	\newblock In \emph{Proc.\ ICLR}, 2024.
462	
463	\bibitem{tulchinskii2024ldscore}
464	E.~Tulchinskii, K.~Kuznetsov, L.~Kushnareva, D.~Cherniavskii, S.~Nikolenko, E.~Burnaev, S.~Barannikov, and I.~Piontkovskaya.
465	\newblock Intrinsic dimension estimation for robust detection of {AI}-generated texts.
466	\newblock In \emph{Proc.\ NeurIPS}, 2024.
467	
468	\bibitem{briesch2023attractor}
469	M.~Briesch, D.~Sobania, and F.~Rothlauf.
470	\newblock Large language models suffer from their own output: An analysis of the self-consuming generative process.
471	\newblock \emph{arXiv preprint arXiv:2311.16822}, 2023.
472	
473	\end{thebibliography}
474	}
475	
476	\end{document}
477	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93f26d44-21bd-474a-9cd9-5f66534ff0ae",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "fe6da3ad-315e-4ef8-8089-488e365455f2",
  "sourceToolAssistantUUID": "93f26d44-21bd-474a-9cd9-5f66534ff0ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-14T18:44:05.205Z_

Now let me also read the "worst" version and any additional project artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe6da3ad-315e-4ef8-8089-488e365455f2",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xMFnhbQA4Eg34TpDmA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5895eaf-a69b-4463-93e3-38420a40fe79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPr3wZUnegXz1WgQbQ7phF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23227,
      "cache_read_input_tokens": 24947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23227,
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

_source line 32 · 2026-05-14T18:44:07.460Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LmkDZtz9wEpnCgpApA1GHC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/worst/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5895eaf-a69b-4463-93e3-38420a40fe79",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xMFnhbQA4Eg34TpDmA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6322a740-2fc8-4168-bc7c-18b88c6b61bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPr3wZUnegXz1WgQbQ7phF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23227,
      "cache_read_input_tokens": 24947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23227,
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

_source line 33 · 2026-05-14T18:44:07.734Z_

<details><summary>↩ Tool result · `toolu_01LmkDZtz9wEpnCgpApA1GHC`</summary>

```text
1	\documentclass[letterpaper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{amsmath,amssymb}
4	\usepackage{booktabs}
5	\usepackage{graphicx}
6	\usepackage{multirow}
7	\usepackage{xcolor}
8	\usepackage{hyperref}
9	\usepackage{natbib}
10	\usepackage{enumitem}
11	
12	\title{Vocabulary Impoverishment as a Shallow Fingerprint of Recursive LLM Generation:\\An Empirical Characterization of Convergence in Non-Paraphrastic Chains}
13	
14	\author{Anonymous}
15	
16	\date{}
17	
18	\begin{document}
19	\maketitle
20	
21	%==============================================================================
22	\begin{abstract}
23	%==============================================================================
24	Recursive application of large language models---where model outputs become inputs to subsequent generations---is an increasingly common pathway for web-scale data contamination. We investigate whether the \emph{generation depth} of such recursively produced text (gen-0 = human, gen-1 = first-pass synthetic, gen-2+ = deeper) can be estimated from distributional features, enabling risk-stratified data curation beyond binary real-vs-synthetic filtering. We formalize two competing hypotheses: \textbf{H$_1$} (convergence), where recursive generation tends toward a distributional fixed point even for non-paraphrastic chains, and \textbf{H$_2$} (divergence), where non-paraphrastic chains accumulate monotonic distributional drift. Through systematic experiments across 5 generators, 4 domains, 3 prompt types, and 25K+ generation chains, we find strong evidence for H$_1$: non-paraphrastic chains converge within 2 generation steps, with detectable differences confined primarily to vocabulary impoverishment---a surface-level phenomenon measured by type-token ratio and hapax ratio. Reference-model entropy statistics, hypothesized to capture deeper distributional shifts, carry no independent signal (surface-only F1 = 0.82 vs.\ full F1 = 0.83, $p = 0.18$). Cross-generator generalization collapses from 0.81 to 0.48 macro-F1, and depth-aware filtering provides no advantage over binary detection baselines. Our results extend attractor cycle theory from paraphrastic to non-paraphrastic settings and establish clear boundary conditions for depth-based approaches to synthetic text governance.
25	\end{abstract}
26	
27	%==============================================================================
28	\section{Introduction}
29	\label{sec:intro}
30	%==============================================================================
31	
32	The proliferation of LLM-generated text on the web creates a recursive contamination problem: models trained on web data ingest outputs of previous models, and their own outputs re-enter the training pipeline at increasing \emph{generation depth}. Unlike the binary real-vs-synthetic distinction addressed by existing detectors \citep{mitchell2023detectgpt,bao2024fastdetectgpt,tulchinskii2024ldscore}, the depth dimension carries additional risk information---deeply recursive text may exhibit compounding distributional artifacts that degrade downstream model quality.
33	
34	Recent theoretical work on \emph{attractor cycles} \citep{anonymous2025attractor} demonstrates that paraphrastic generation chains (where each step paraphrases the previous output) converge to periodic orbits in distributional space within 2--3 steps. This convergence bounds the depth signal available in paraphrastic settings. However, non-paraphrastic chains---continuations, elaborations, and inspired rewrites---operate in an unbounded semantic state space, raising the question: does distributional drift accumulate monotonically in these chains, or does autoregressive sampling impose its own convergence?
35	
36	We formalize this as two competing hypotheses:
37	\begin{itemize}[nosep,leftmargin=*]
38	    \item \textbf{H$_1$ (Convergence)}: Recursive non-paraphrastic generation converges to a near-stationary distribution within a small number of steps, driven by autoregressive sampling concentrating probability mass on preferred tokens.
39	    \item \textbf{H$_2$ (Divergence)}: Non-paraphrastic chains accumulate monotonic distributional drift, producing increasingly distinctive depth fingerprints that enable fine-grained ordinal depth estimation.
40	\end{itemize}
41	
42	We test these hypotheses through a comprehensive empirical study spanning 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B), 4 text domains (Wikipedia, news, scientific, creative writing), and 3 non-paraphrastic prompt types (continuation, elaboration, inspired rewriting), generating over 25,000 recursive chains of depth 0--4.
43	
44	Our findings decisively support H$_1$ and yield a negative-but-informative result: \textbf{non-paraphrastic chains also converge rapidly in distributional space, with detectable differences confined primarily to vocabulary impoverishment.} Specifically:
45	\begin{enumerate}[nosep,leftmargin=*]
46	    \item Surface vocabulary features (hapax ratio, type-token ratio) explain 98.8\% of classifier performance; reference-model entropy statistics add no significant independent signal.
47	    \item Cross-generator depth estimation collapses to near-chance (macro-F1 = 0.48) because vocabulary statistics are generator-specific artifacts, not universal depth markers.
48	    \item Depth-aware data filtering provides no practical advantage over binary real/synthetic baselines for downstream quality preservation.
49	\end{enumerate}
50	
51	These results extend attractor cycle theory to non-paraphrastic settings and establish vocabulary impoverishment as a universal but shallow fingerprint of recursive generation---theoretically motivated by entropy convergence under autoregressive sampling, but practically limited by its generator-specificity.
52	
53	%==============================================================================
54	\section{Related Work}
55	\label{sec:related}
56	%==============================================================================
57	
58	\paragraph{Machine-generated text detection.}
59	Binary detection methods assign a real/synthetic label based on statistical signatures. Log-likelihood approaches \citep{mitchell2023detectgpt,bao2024fastdetectgpt} use perturbation-based curvature estimates under a scoring model. Watermarking methods \citep{kirchenbauer2023watermark} embed detectable patterns during generation. LD-Score \citep{tulchinskii2024ldscore} exploits character-level distributional signatures. All these operate at the binary level; none attempt ordinal depth estimation.
60	
61	\paragraph{Model collapse and recursive generation.}
62	Shumailov et al.\ (\citeyear{shumailov2024modelcollapse}) demonstrate that iterative training on self-generated data leads to model collapse---progressive loss of distributional tails. Dohmatob et al.\ (\citeyear{dohmatob2024tale}) provide theoretical analysis of this phenomenon. Our work examines the \emph{text-level} distributional changes across generation depth, rather than the model-level degradation from recursive training.
63	
64	\paragraph{Attractor cycle theory.}
65	Recent work \citep{anonymous2025attractor} proves that paraphrastic generation chains converge to periodic orbits, bounding depth-discriminable classes to approximately 3 for paraphrasing. We extend this investigation to non-paraphrastic settings, testing whether the convergence phenomenon generalizes beyond the semantic-preservation constraint of paraphrasing.
66	
67	%==============================================================================
68	\section{Method}
69	\label{sec:method}
70	%==============================================================================
71	
72	\subsection{Chain Construction}
73	\label{sec:chains}
74	
75	Given a seed text $x_0$ (human-written, gen-0), we construct recursive generation chains by repeatedly applying a generator $G$:
76	\begin{equation}
77	    x_{d+1} = G(x_d; p_\text{type})
78	\end{equation}
79	where $p_\text{type} \in \{\text{continuation, elaboration, inspired\_rewriting}\}$ specifies the prompt template. We generate chains of depth 0 through 4, yielding 5-class ordinal labels.
80	
81	\paragraph{Generators.} We use 5 autoregressive models spanning 3 families: Pythia-2.8B, Pythia-1B \citep{biderman2023pythia}, OLMo-2-1B \citep{groeneveld2024olmo}, Qwen3.5-2B, and Qwen3.5-0.8B \citep{bai2023qwen}. All generation uses nucleus sampling ($p = 0.95$, $T = 1.0$).
82	
83	\paragraph{Seed domains.} We draw 500 seeds per domain from 4 sources: Wikipedia, CNN/DailyMail (news), S2ORC (scientific abstracts), and WritingPrompts (creative writing).
84	
85	\paragraph{Cross-model chains.} To simulate realistic web contamination where different generators produce each depth step, we also construct cross-model chains with generators randomly assigned per step.
86	
87	\subsection{Feature Extraction}
88	\label{sec:features}
89	
90	We extract two categories of features from each text $x_d$:
91	
92	\paragraph{Surface vocabulary features.}
93	\begin{itemize}[nosep,leftmargin=*]
94	    \item \textbf{Type-token ratio (TTR)}: $|\mathcal{V}(x)| / |x|$, measuring lexical diversity.
95	    \item \textbf{Hapax ratio}: fraction of word types appearing exactly once, capturing vocabulary richness at the distributional tail.
96	\end{itemize}
97	
98	\paragraph{Reference-model features.}
99	Given a reference model $M_\text{ref}$ (default: Pythia-410M), we compute the token-level log-probability sequence $\{-\log p_{M_\text{ref}}(t_i \mid t_{<i})\}_{i=1}^{|x|}$ and extract:
100	\begin{itemize}[nosep,leftmargin=*]
101	    \item \textbf{Entropy statistics}: mean, standard deviation, minimum, and maximum of the token-level surprise distribution.
102	    \item \textbf{Tail decay}: rate of exponential decay in the sorted surprise values, capturing distributional tail behavior.
103	\end{itemize}
104	
105	We additionally evaluate OLMo-2-1B and Qwen3.5-0.8B as alternative reference models, and LD-Score \citep{tulchinskii2024ldscore} as a character-level feature.
106	
107	\subsection{Classification}
108	\label{sec:classifiers}
109	
110	We train ordinal logistic regression and random forest classifiers with 5-fold cross-validation, reporting macro-F1 as the primary metric. For cross-generator evaluation, we use leave-one-generator-out (LOO) cross-validation. As an upper bound, we fine-tune Qwen3.5-0.8B with QLoRA for end-to-end depth classification from raw text.
111	
112	%==============================================================================
113	\section{Experiments}
114	\label{sec:experiments}
115	%==============================================================================
116	
117	We organize our experiments around the two competing hypotheses and three practical questions: (1) what features carry the depth signal, (2) does the signal generalize, and (3) does it provide downstream utility?
118	
119	%--- 4.1 Feature Ablation ---
120	\subsection{Feature Ablation: What Carries the Signal?}
121	\label{sec:ablation}
122	
123	We compare surface-only, reference-only, and full (surface + reference) feature sets on single-generator data (Pythia-2.8B, Pythia-410M reference, 3-class depth: gen-0/gen-1/gen-2+).
124	
125	\begin{table}[h]
126	\centering
127	\caption{Feature ablation results (3-class, Pythia-2.8B generator).}
128	\label{tab:ablation}
129	\begin{tabular}{lcccc}
130	\toprule
131	Feature Set & Macro-F1 & Gen-0 F1 & Gen-1 F1 & Gen-2+ F1 \\
132	\midrule
133	Surface only & 0.82 & 0.94 & 0.75 & 0.77 \\
134	Reference only & 0.47 & 0.58 & 0.38 & 0.44 \\
135	Full (surface + ref) & 0.83 & 0.95 & 0.76 & 0.78 \\
136	Chance & 0.33 & 0.33 & 0.33 & 0.33 \\
137	\bottomrule
138	\end{tabular}
139	\end{table}
140	
141	\begin{table}[h]
142	\centering
143	\caption{Permutation feature importance (full model).}
144	\label{tab:importance}
145	\begin{tabular}{lcc}
146	\toprule
147	Feature & Importance & Std \\
148	\midrule
149	hapax\_ratio & 0.31 & 0.04 \\
150	TTR & 0.24 & 0.03 \\
151	entropy\_mean & 0.04 & 0.02 \\
152	entropy\_std & 0.03 & 0.01 \\
153	entropy\_min & 0.02 & 0.01 \\
154	entropy\_max & 0.01 & 0.01 \\
155	tail\_decay & 0.02 & 0.01 \\
156	\bottomrule
157	\end{tabular}
158	\end{table}
159	
160	Surface features alone achieve F1 = 0.82, recovering 98.8\% of the full model's performance (0.83). Adding reference-model features yields a non-significant improvement of +0.01 ($p = 0.18$, paired bootstrap). Reference-only features perform near chance (0.47). Permutation importance (Table~\ref{tab:importance}) confirms that hapax ratio (0.31) and TTR (0.24) dominate, while all entropy features combined contribute $< 0.12$. The ``distributional fingerprint'' framing is not supported: what the classifier detects is vocabulary impoverishment, not a deeper distributional shift.
161	
162	%--- 4.2 Cross-Generator Generalization ---
163	\subsection{Cross-Generator Generalization}
164	\label{sec:crossgen}
165	
166	We evaluate generalization across 5 generators using leave-one-generator-out cross-validation on 25K chains (1000 seeds $\times$ 5 generators $\times$ 5 depths).
167	
168	\begin{table}[h]
169	\centering
170	\caption{Cross-generator generalization (leave-one-out).}
171	\label{tab:crossgen}
172	\begin{tabular}{lcccc}
173	\toprule
174	Held-Out Generator & Macro-F1 & Gen-0 F1 & Gen-1 F1 & Gen-2+ F1 \\
175	\midrule
176	Pythia-2.8B & 0.52 & 0.71 & 0.40 & 0.45 \\
177	OLMo-2-1B & 0.44 & 0.65 & 0.34 & 0.38 \\
178	Qwen3.5-2B & 0.43 & 0.64 & 0.35 & 0.39 \\
179	Qwen3.5-0.8B & 0.50 & 0.70 & 0.38 & 0.43 \\
180	Pythia-1B & 0.53 & 0.72 & 0.42 & 0.46 \\
181	\midrule
182	\textbf{Average} & \textbf{0.48} & \textbf{0.68} & \textbf{0.38} & \textbf{0.42} \\
183	\bottomrule
184	\end{tabular}
185	\end{table}
186	
187	\begin{table}[h]
188	\centering
189	\caption{Within- vs.\ cross-generator comparison.}
190	\label{tab:within_vs_cross}
191	\begin{tabular}{lcc}
192	\toprule
193	Setting & Macro-F1 & $\Delta$ vs.\ Within \\
194	\midrule
195	Within-generator avg & 0.81 & --- \\
196	Leave-one-out avg & 0.48 & $-0.33$ \\
197	Pooled all generators & 0.62 & $-0.19$ \\
198	\bottomrule
199	\end{tabular}
200	\end{table}
201	
202	Cross-generator macro-F1 drops catastrophically from 0.81 to 0.48---barely above chance (0.33). The collapse is most severe for cross-family transfer: holding out Qwen models yields 0.43--0.44, while holding out Pythia-1B yields 0.53 due to shared vocabulary statistics with Pythia-2.8B in the training fold. Gen-0 identification is partially preserved (0.68) because human text maintains a distinct surface profile regardless of generator, but gen-1 vs.\ gen-2+ discrimination is near chance. The surface vocabulary statistics that carry the depth signal are generator-specific calibration artifacts, not universal depth markers.
203	
204	%--- 4.3 Reference Model Choice ---
205	\subsection{Reference Model Choice}
206	\label{sec:refmodel}
207	
208	We test whether the reference model architecture contributes to the generalization failure by evaluating Pythia-410M, OLMo-2-1B, and Qwen3.5-0.8B as reference models.
209	
210	\begin{table}[h]
211	\centering
212	\caption{Reference model comparison (leave-one-generator-out).}
213	\label{tab:refmodel}
214	\begin{tabular}{lccc}
215	\toprule
216	Reference Model & LOO Macro-F1 & Ref-Only F1 & Surface-Only F1 \\
217	\midrule
218	Pythia-410M & 0.48 & 0.47 & 0.82 \\
219	OLMo-2-1B & 0.45 & 0.43 & 0.82 \\
220	Qwen3.5-0.8B & 0.44 & 0.41 & 0.82 \\
221	Ensemble (3 refs) & 0.50 & 0.49 & 0.82 \\
222	\bottomrule
223	\end{tabular}
224	\end{table}
225	
226	All three reference models produce similarly uninformative entropy distributions for cross-generator depth estimation. The surface-only F1 remains constant at 0.82 regardless of reference model, confirming that surface features are the sole discriminative mechanism. Ensembling three reference models yields only +0.02 over the best single model. The generalization bottleneck is not reference model choice---it is the fundamental convergence of generation entropy to near-stationary levels by gen-1, leaving no depth-discriminative signal for the reference model to capture.
227	
228	%--- 4.4 H1 vs H2: Convergence Testing ---
229	\subsection{Hypothesis Testing: Convergence vs.\ Divergence}
230	\label{sec:convergence}
231	
232	We directly test H$_1$ vs.\ H$_2$ by comparing paraphrastic and non-paraphrastic chains on matched seeds (Pythia-2.8B, 1000 seeds, 5 depths).
233	
234	\begin{table}[h]
235	\centering
236	\caption{Paraphrastic vs.\ non-paraphrastic chain comparison.}
237	\label{tab:convergence}
238	\begin{tabular}{lcccc}
239	\toprule
240	Chain Type & Macro-F1 (3-class) & Gen-1 vs.\ Gen-2+ F1 & Conv.\ Depth & KL$_{d2 \to d3}$ \\
241	\midrule
242	Paraphrasing & 0.64 & 0.41 & 1 & 0.008 \\
243	Continuation & 0.82 & 0.58 & 2 & 0.031 \\
244	Elaboration & 0.78 & 0.52 & 2 & 0.024 \\
245	Inspired rewriting & 0.69 & 0.44 & 1 & 0.012 \\
246	\bottomrule
247	\end{tabular}
248	\end{table}
249	
250	\textbf{H$_1$ is confirmed.} All chain types converge within 1--2 generation steps. Paraphrasing chains converge fastest (by depth 1), consistent with attractor cycle theory, while continuation chains converge by depth 2. The KL divergence between depth-2 and depth-3 distributions is negligible across all chain types ($< 0.04$ nats). Non-paraphrastic generation does \emph{not} produce the unbounded divergence hypothesized in H$_2$; instead, autoregressive sampling from a fixed model concentrates probability mass on preferred tokens regardless of prompt type, creating a universal vocabulary attractor. The depth signal is fundamentally bounded at $\sim$2--3 discriminable classes.
251	
252	%--- 4.5 Prompt Type Sensitivity ---
253	\subsection{Prompt Type Sensitivity}
254	\label{sec:prompt}
255	
256	We compare three non-paraphrastic prompt types within and across settings.
257	
258	\begin{table}[h]
259	\centering
260	\caption{Prompt type comparison (Pythia-2.8B, 1000 seeds).}
261	\label{tab:prompt}
262	\begin{tabular}{lccc}
263	\toprule
264	Prompt Type & Within-Gen F1 & Cross-Prompt F1 & Conv.\ Depth \\
265	\midrule
266	Continuation & 0.82 & 0.61 & 2 \\
267	Elaboration & 0.78 & 0.58 & 2 \\
268	Inspired rewriting & 0.69 & 0.52 & 1 \\
269	\bottomrule
270	\end{tabular}
271	\end{table}
272	
273	Continuation chains yield the highest within-generator F1 (0.82) because they preserve topic continuity, making vocabulary depletion the dominant and cleanest signal. Inspired rewriting shows the weakest signal (0.69) because each generation step introduces substantially new vocabulary, partially resetting the depletion. Cross-prompt transfer is poor (0.52--0.61), revealing that each prompt type induces a different vocabulary depletion rate. This adds a second axis of non-generalization beyond generator specificity: the depth signal is both generator-specific and prompt-type-specific.
274	
275	%--- 4.6 Ecological Validity ---
276	\subsection{Ecological Validity: Cross-Model Chains and Multi-Domain Seeds}
277	\label{sec:ecological}
278	
279	\paragraph{Cross-model chains.}
280	We construct chains where a different generator (randomly selected from 5) produces each depth step, simulating realistic web contamination.
281	
282	\begin{table}[h]
283	\centering
284	\caption{Single-model vs.\ cross-model chains.}
285	\label{tab:crossmodel}
286	\begin{tabular}{lcccc}
287	\toprule
288	Setting & Macro-F1 & Gen-0 F1 & Gen-1 F1 & Gen-2+ F1 \\
289	\midrule
290	Single-model chains & 0.81 & 0.94 & 0.75 & 0.77 \\
291	Cross-model chains & 0.42 & 0.65 & 0.32 & 0.35 \\
292	Chance & 0.33 & 0.33 & 0.33 & 0.33 \\
293	\bottomrule
294	\end{tabular}
295	\end{table}
296	
297	Cross-model chains produce near-chance depth estimation (0.42). When different generators produce each depth step, the vocabulary statistics at any given depth reflect the current generator's preferences more than cumulative chain depth. Gen-0 identification survives partially (0.65) because human text remains distinct, but gen-1/gen-2+ classification is effectively random.
298	
299	\paragraph{Multi-domain seeds.}
300	We expand to 4 domains with 500 seeds each using Pythia-2.8B.
301	
302	\begin{table}[h]
303	\centering
304	\caption{Multi-domain results.}
305	\label{tab:domain}
306	\begin{tabular}{lcccc}
307	\toprule
308	Domain & Within-Domain F1 & Gen-0 hapax$_\text{med}$ & Gen-2+ hapax$_\text{med}$ & $\Delta$hapax \\
309	\midrule
310	Wikipedia & 0.83 & 0.47 & 0.26 & 0.21 \\
311	News & 0.80 & 0.44 & 0.27 & 0.17 \\
312	Scientific & 0.76 & 0.52 & 0.35 & 0.17 \\
313	Creative & 0.72 & 0.38 & 0.28 & 0.10 \\
314	Cross-domain avg & 0.59 & --- & --- & --- \\
315	\bottomrule
316	\end{tabular}
317	\end{table}
318	
319	Within-domain performance correlates with the hapax ratio gap ($\Delta$hapax) between gen-0 and gen-2+: Wikipedia/news have the largest gaps (0.21/0.17) and highest F1 (0.83/0.80), while creative writing has the smallest gap (0.10) and lowest F1 (0.72). Cross-domain transfer drops to 0.59 because baseline vocabulary statistics differ across domains---scientific gen-0 text (hapax median 0.52) overlaps with other domains' synthetic ranges, confounding domain and depth.
320	
321	%--- 4.7 Depth Resolution Ceiling ---
322	\subsection{Depth Resolution Ceiling}
323	\label{sec:ordinal}
324	
325	We test 5-class ordinal classification (gen-0 through gen-4) on continuation chains.
326	
327	\begin{table}[h]
328	\centering
329	\caption{5-class ordinal classification results.}
330	\label{tab:ordinal}
331	\begin{tabular}{lccc}
332	\toprule
333	Class & Precision & Recall & F1 \\
334	\midrule
335	gen-0 & 0.93 & 0.90 & 0.91 \\
336	gen-1 & 0.54 & 0.62 & 0.58 \\
337	gen-2 & 0.36 & 0.40 & 0.38 \\
338	gen-3 & 0.29 & 0.33 & 0.31 \\
339	gen-4 & 0.31 & 0.35 & 0.33 \\
340	\midrule
341	\multicolumn{3}{l}{5-class macro-F1} & 0.52 \\
342	\multicolumn{3}{l}{3-class macro-F1 (same data)} & 0.82 \\
343	\multicolumn{3}{l}{Adjacent confusion rate} & 0.44 \\
344	\bottomrule
345	\end{tabular}
346	\end{table}
347	
348	\begin{table}[h]
349	\centering
350	\caption{5-class confusion matrix (row = true, column = predicted; values are proportions).}
351	\label{tab:confusion}
352	\begin{tabular}{lccccc}
353	\toprule
354	 & gen-0 & gen-1 & gen-2 & gen-3 & gen-4 \\
355	\midrule
356	gen-0 & \textbf{0.90} & 0.07 & 0.02 & 0.01 & 0.00 \\
357	gen-1 & 0.09 & \textbf{0.62} & 0.18 & 0.07 & 0.04 \\
358	gen-2 & 0.03 & 0.21 & \textbf{0.40} & 0.22 & 0.14 \\
359	gen-3 & 0.02 & 0.10 & 0.24 & \textbf{0.33} & 0.31 \\
360	gen-4 & 0.01 & 0.07 & 0.16 & 0.28 & \textbf{0.48} \\
361	\bottomrule
362	\end{tabular}
363	\end{table}
364	
365	5-class macro-F1 drops to 0.52 (from 0.82 for 3-class). Gen-2 through gen-4 collapse into mutual confusion: gen-3 and gen-4 F1 scores (0.31, 0.33) are at chance level. The confusion matrix shows a diagonal-plus-adjacent pattern (44\% of errors are off-by-one) consistent with a smoothly converging feature distribution rather than discrete depth categories. This directly reflects H$_1$ convergence: by depth 2, the feature distributions have stabilized, making deeper classes statistically indistinguishable. The practical depth resolution ceiling is $\sim$2--3 classes.
366	
367	%--- 4.8 Robustness Analysis ---
368	\subsection{Robustness to Human Edits and Character-Level Features}
369	\label{sec:robustness}
370	
371	\paragraph{Edit robustness.}
372	We test robustness to simulated human edits via random word replacement (5\%, 10\%, 20\%) and LLM-simulated light rephrasing.
373	
374	\begin{table}[h]
375	\centering
376	\caption{Robustness to human edits.}
377	\label{tab:edits}
378	\begin{tabular}{lccc}
379	\toprule
380	Edit Type & Edit Rate & Macro-F1 & $\Delta$ vs.\ Baseline \\
381	\midrule
382	None & 0\% & 0.82 & --- \\
383	Random replace & 5\% & 0.77 & $-0.05$ \\
384	Random replace & 10\% & 0.70 & $-0.12$ \\
385	Random replace & 20\% & 0.58 & $-0.24$ \\
386	LLM-simulated & light & 0.63 & $-0.19$ \\
387	\bottomrule
388	\end{tabular}
389	\end{table}
390	
391	Surface features are fragile under editing. At 10\% word replacement, F1 drops by 0.12; LLM-simulated light editing causes a 0.19 drop because the editing model introduces its own vocabulary preferences, adding a second generator's fingerprint. The crossover where depth estimation becomes worse than binary detection occurs at approximately 12\% replacement rate. Real-world synthetic text is routinely edited at or above this level.
392	
393	\paragraph{LD-Score features.}
394	We evaluate LD-Score \citep{tulchinskii2024ldscore} as a character-level complement.
395	
396	\begin{table}[h]
397	\centering
398	\caption{LD-Score feature analysis.}
399	\label{tab:ldscore}
400	\begin{tabular}{lcc}
401	\toprule
402	Feature Set & Macro-F1 & LOO Cross-Gen F1 \\
403	\midrule
404	Surface only & 0.82 & 0.48 \\
405	LD-Score only & 0.61 & 0.46 \\
406	Surface + LD & 0.83 & 0.49 \\
407	Full + LD & 0.83 & 0.50 \\
408	\bottomrule
409	\end{tabular}
410	\end{table}
411	
412	LD-Score achieves moderate standalone performance (0.61) but provides no complementary signal when combined with surface features (+0.01). Character-level distributions partially capture vocabulary depletion through character frequency shifts but are redundant with word-level statistics. Cross-generator transfer with LD-Score (0.46) remains poor.
413	
414	%--- 4.9 Learned Representations ---
415	\subsection{End-to-End Learned Representations}
416	\label{sec:e2e}
417	
418	We fine-tune Qwen3.5-0.8B with QLoRA for end-to-end depth classification to test whether learned representations can discover depth signal beyond handcrafted features.
419	
420	\begin{table}[h]
421	\centering
422	\caption{End-to-end vs.\ handcrafted features.}
423	\label{tab:e2e}
424	\begin{tabular}{lccc}
425	\toprule
426	Model & Within-Gen F1 & Cross-Gen LOO F1 & $\Delta$ Cross-Gen \\
427	\midrule
428	Handcrafted (surface + ref) & 0.83 & 0.48 & --- \\
429	QLoRA Qwen3.5-0.8B & 0.87 & 0.53 & +0.05 \\
430	Handcrafted surface only & 0.82 & 0.48 & --- \\
431	\bottomrule
432	\end{tabular}
433	\end{table}
434	
435	The end-to-end model achieves marginally higher within-generator F1 (0.87 vs.\ 0.82) by learning soft vocabulary depletion features beyond hapax ratio and TTR. However, cross-generator transfer shows only +0.05 improvement (0.53 vs.\ 0.48), meaning learned representations are also predominantly generator-specific. Attention analysis reveals the model focuses on high-frequency function words and punctuation---tokens whose usage patterns shift under vocabulary impoverishment. Even with 0.8B parameters and full sequence access, the model does not discover hidden distributional structure beyond surface statistics. This closes the ``bigger model'' escape hatch: the cross-generator signal genuinely is not present.
436	
437	%--- 4.10 Downstream Utility ---
438	\subsection{Downstream Utility}
439	\label{sec:downstream}
440	
441	We test whether depth-aware filtering improves downstream model quality by fine-tuning Pythia-410M on depth-stratified data subsets and comparing against binary detection baselines.
442	
443	\begin{table}[h]
444	\centering
445	\caption{Downstream fine-tuning perplexity.}
446	\label{tab:downstream}
447	\begin{tabular}{lcc}
448	\toprule
449	Training Data & Perplexity & Data Size (\%) \\
450	\midrule
451	Gen-0 only & 18.2 & 33 \\
452	Gen-0 + gen-1 & 18.8 & 67 \\
453	All depths unfiltered & 19.5 & 100 \\
454	Depth-aware filter ($\leq$gen-1) & 18.5 & 38 \\
455	FastDetectGPT binary filter & 18.4 & 42 \\
456	LD-Score binary filter & 18.6 & 40 \\
457	\bottomrule
458	\end{tabular}
459	\end{table}
460	
461	\begin{table}[h]
462	\centering
463	\caption{Depth--quality correlation.}
464	\label{tab:correlation}
465	\begin{tabular}{lc}
466	\toprule
467	Metric & Value \\
468	\midrule
469	Spearman $\rho$ (depth vs.\ ppl degradation) & 0.19 \\
470	$p$-value & 0.04 \\
471	Depth filter vs.\ best binary gap & $-0.3\%$ \\
472	\bottomrule
473	\end{tabular}
474	\end{table}
475	
476	A weak positive correlation exists between generation depth and quality degradation ($\rho = 0.19$, $p = 0.04$), but the effect size is negligible. Depth-aware filtering achieves perplexity 18.5, compared to 18.4 for FastDetectGPT binary filtering---a $-0.3\%$ gap favoring the simpler baseline. The ordinal depth information provides no practical advantage over binary classification for data curation. This is the expected consequence of the preceding results: if depth estimation relies on generator-specific surface features with poor cross-generator transfer, the noisy depth predictions cannot outperform binary detection for downstream filtering.
477	
478	%==============================================================================
479	\section{Discussion}
480	\label{sec:discussion}
481	%==============================================================================
482	
483	\paragraph{Extending attractor cycle theory.}
484	Our central finding---that H$_1$ holds for non-paraphrastic chains---extends the attractor cycle theory of \citet{anonymous2025attractor} beyond its original paraphrastic setting. The convergence mechanism is distinct: paraphrastic chains converge because the semantic-preservation constraint restricts the output space, while non-paraphrastic chains converge because autoregressive sampling from a fixed model concentrates probability mass on preferred tokens regardless of semantic constraints. Both mechanisms produce the same practical outcome: depth-discriminable classes are bounded at $\sim$2--3.
485	
486	\paragraph{Vocabulary impoverishment as a universal but shallow fingerprint.}
487	Recursive generation progressively depletes rare vocabulary---a mechanical consequence of sampling from a fixed token distribution. This creates a detectable but shallow fingerprint: type-token ratio and hapax ratio decrease monotonically with depth but stabilize by gen-2, and their absolute values are determined by the generator's vocabulary preferences rather than chain depth per se. The fingerprint is ``universal'' in that all tested generators exhibit vocabulary depletion, but ``shallow'' in that it does not encode generator-invariant depth information.
488	
489	\paragraph{Implications for data governance.}
490	Our results suggest that binary real-vs-synthetic detection remains the practically optimal granularity for data filtering in the current paradigm. Depth-aware approaches face a three-way non-generalization barrier: the signal is generator-specific, prompt-type-specific, and domain-specific. Until depth features are identified that generalize across these axes, binary filtering with established detectors \citep{bao2024fastdetectgpt,tulchinskii2024ldscore} is both simpler and more effective.
491	
492	\paragraph{Limitations.}
493	Our study is limited to 5 open-weight models up to 2.8B parameters; larger or closed-source models may exhibit different vocabulary dynamics. The simulated editing is a lower bound on real-world post-processing. We do not test instruction-tuned or RLHF-aligned models, which may have different distributional properties. Our cross-model chains use random generator assignment; real contamination may have structured patterns.
494	
495	%==============================================================================
496	\section{Conclusion}
497	\label{sec:conclusion}
498	%==============================================================================
499	
500	We tested two hypotheses about distributional dynamics in recursive non-paraphrastic LLM generation chains. Our experiments across 5 generators, 4 domains, and 3 prompt types provide strong evidence for H$_1$ (convergence): non-paraphrastic chains converge to near-stationary distributions within 2 generation steps, extending attractor cycle theory beyond paraphrastic settings. The detectable depth signal is confined to vocabulary impoverishment---surface features (hapax ratio, TTR) that explain 98.8\% of classifier performance but are generator-specific, prompt-type-specific, and fragile under editing. Cross-generator depth estimation is near chance (macro-F1 = 0.48), and depth-aware filtering provides no advantage over binary baselines.
501	
502	These negative results establish clear boundary conditions: vocabulary impoverishment is a universal consequence of autoregressive generation but not a viable basis for general-purpose depth estimation. Future work should investigate whether training-time features (model weights, sampling parameters) or generation-aware watermarking can provide the generator-invariant depth signal that distributional post-hoc analysis cannot.
503	
504	%==============================================================================
505	% References
506	%==============================================================================
507	\bibliographystyle{plainnat}
508	
509	\begin{thebibliography}{10}
510	
511	\bibitem[Anonymous(2025)]{anonymous2025attractor}
512	Anonymous.
513	\newblock Attractor cycles in paraphrastic generation chains.
514	\newblock In \emph{Proceedings of ACL}, 2025.
515	
516	\bibitem[Bai et~al.(2023)]{bai2023qwen}
517	Jinze Bai et~al.
518	\newblock Qwen technical report.
519	\newblock \emph{arXiv preprint arXiv:2309.16609}, 2023.
520	
521	\bibitem[Bao et~al.(2024)]{bao2024fastdetectgpt}
522	Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi Yang, and Yue Zhang.
523	\newblock Fast-{D}etect{GPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.
524	\newblock In \emph{Proceedings of ICLR}, 2024.
525	
526	\bibitem[Biderman et~al.(2023)]{biderman2023pythia}
527	Stella Biderman et~al.
528	\newblock Pythia: A suite for analyzing large language models across training and scaling.
529	\newblock In \emph{Proceedings of ICML}, 2023.
530	
531	\bibitem[Dohmatob et~al.(2024)]{dohmatob2024tale}
532	Elvis Dohmatob, Yunzhen Feng, and Julia Kempe.
533	\newblock A tale of tails: Model collapse as a change of scaling laws.
534	\newblock In \emph{Proceedings of ICML}, 2024.
535	
536	\bibitem[Groeneveld et~al.(2024)]{groeneveld2024olmo}
537	Dirk Groeneveld et~al.
538	\newblock {OLMo}: Accelerating the science of language models.
539	\newblock In \emph{Proceedings of ACL}, 2024.
540	
541	\bibitem[Kirchenbauer et~al.(2023)]{kirchenbauer2023watermark}
542	John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein.
543	\newblock A watermark for large language models.
544	\newblock In \emph{Proceedings of ICML}, 2023.
545	
546	\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}
547	Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher~D. Manning, and Chelsea Finn.
548	\newblock {DetectGPT}: Zero-shot machine-generated text detection using probability curvature.
549	\newblock In \emph{Proceedings of ICML}, 2023.
550	
551	\bibitem[Shumailov et~al.(2024)]{shumailov2024modelcollapse}
552	Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, and Ross Anderson.
553	\newblock The curse of recursion: Training on generated data makes models forget.
554	\newblock \emph{Nature}, 2024.
555	
556	\bibitem[Tulchinskii et~al.(2024)]{tulchinskii2024ldscore}
557	Eduard Tulchinskii et~al.
558	\newblock Intrinsic dimension estimation for robust detection of {AI}-generated texts.
559	\newblock In \emph{Proceedings of NeurIPS}, 2024.
560	
561	\end{thebibliography}
562	
563	\end{document}
564	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6322a740-2fc8-4168-bc7c-18b88c6b61bd",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "03fba61a-1f12-45b5-a5c1-fae5f4ee143a",
  "sourceToolAssistantUUID": "6322a740-2fc8-4168-bc7c-18b88c6b61bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T18:44:07.936Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01U5DNVMoBEGbLvY8xEYbnYd`</summary>

```json
{
  "pattern": "artifacts/dream_reports/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03fba61a-1f12-45b5-a5c1-fae5f4ee143a",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xMFnhbQA4Eg34TpDmA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8881c639-0708-46bd-86f9-94da48b5c065",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LPr3wZUnegXz1WgQbQ7phF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23227,
      "cache_read_input_tokens": 24947,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23227
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 24947,
          "cache_creation_input_tokens": 23227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23227,
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

_source line 35 · 2026-05-14T18:44:07.949Z_

<details><summary>↩ Tool result · `toolu_01U5DNVMoBEGbLvY8xEYbnYd`</summary>

```text
artifacts/dream_reports/dream_20260514T181213/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260514T181213/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260514T181213/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260514T181213/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T181213/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T181213/best/experiment_data.json
artifacts/dream_reports/dream_20260514T181213/best/paper_framing.md
artifacts/dream_reports/dream_20260514T181213/best/paper.tex
artifacts/dream_reports/dream_20260514T181213/best/paper.aux
artifacts/dream_reports/dream_20260514T181213/best/paper.out
artifacts/dream_reports/dream_20260514T181213/best/paper.pdf
artifacts/dream_reports/dream_20260514T181213/best/paper.log
artifacts/dream_reports/dream_20260514T181213/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T181213/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T181213/median/experiment_data.json
artifacts/dream_reports/dream_20260514T181213/median/paper_framing.md
artifacts/dream_reports/dream_20260514T181213/median/paper.tex
artifacts/dream_reports/dream_20260514T181213/median/paper.aux
artifacts/dream_reports/dream_20260514T181213/median/paper.out
artifacts/dream_reports/dream_20260514T181213/median/paper.pdf
artifacts/dream_reports/dream_20260514T181213/median/paper.log
artifacts/dream_reports/dream_20260514T181213/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T181213/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T181213/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T181213/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T181213/worst/paper.tex
artifacts/dream_reports/dream_20260514T181213/worst/paper.aux
artifacts/dream_reports/dream_20260514T181213/worst/paper.out
artifacts/dream_reports/dream_20260514T181213/worst/paper.pdf
artifacts/dream_reports/dream_20260514T181213/worst/paper.log
artifacts/dream_reports/dream_20260514T181213/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T181213/best/review_context.yaml
artifacts/dream_reports/dream_20260514T181213/logs/orchestrator.log
artifacts/dream_reports/dream_20260514T181213/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8881c639-0708-46bd-86f9-94da48b5c065",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "d992a01f-96e0-4a0b-a787-9e6142805a9c",
  "sourceToolAssistantUUID": "8881c639-0708-46bd-86f9-94da48b5c065",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-14T18:44:11.280Z_

Let me read the review context and the imagined experiments data for the "best" scenario (which appears to be the primary paper under review).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d992a01f-96e0-4a0b-a787-9e6142805a9c",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xMpWhfZZue7J8SHFqT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "480d01c9-1f1d-4aa6-b88d-5540b9104f6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEdNKXm3uC3LEcy3yUJk3g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12679,
      "cache_read_input_tokens": 48174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12679,
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

_source line 37 · 2026-05-14T18:44:12.731Z_

<details open><summary>🔧 Tool call — Read · `toolu_018i15CBCRmvCYXAMLpVCR8j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "480d01c9-1f1d-4aa6-b88d-5540b9104f6b",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xMpWhfZZue7J8SHFqT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "527e66b2-00a1-47a3-8f11-b9af33b134e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEdNKXm3uC3LEcy3yUJk3g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12679,
      "cache_read_input_tokens": 48174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12679,
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

_source line 38 · 2026-05-14T18:44:13.007Z_

<details><summary>↩ Tool result · `toolu_018i15CBCRmvCYXAMLpVCR8j`</summary>

```text
1	narrative_guidance: 'Original framing fully intact. Story: non-paraphrastic chains
2	  exhibit monotonic distributional divergence (H₂ confirmed), detectable via reference-model
3	  entropy features that capture drift beyond surface vocabulary impoverishment. Headline:
4	  "distributional fingerprints enable risk-stratified data curation," with clean ablation
5	  separating signal from shortcut. All three claims stated at full strength. AAAI
6	  submission with no scope reduction.
7	
8	  '
9	imagined_experiments:
10	- name: feature_ablation
11	  plan_id: plan_001
12	  description: 'Ablation on existing MVP data (4609 records, Pythia-2.8B generator,
13	    Pythia-410M reference, Wikipedia seeds). Three conditions: (A) reference-only
14	    features (entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay), (B)
15	    surface-only features (ttr, hapax_ratio), (C) full 7-feature set. Same XGBoost
16	    classifier, 5-fold stratified CV, 3-class (gen-0/gen-1/gen-2+).
17	
18	    '
19	  expected_results:
20	    ref_only_macro_f1: 0.79
21	    ref_only_cv_std: 0.018
22	    ref_only_gen0_f1: 0.91
23	    ref_only_gen1_f1: 0.71
24	    ref_only_gen2plus_f1: 0.74
25	    surface_only_macro_f1: 0.63
26	    surface_only_cv_std: 0.022
27	    surface_only_gen0_f1: 0.82
28	    surface_only_gen1_f1: 0.52
29	    surface_only_gen2plus_f1: 0.55
30	    full_macro_f1: 0.87
31	    full_cv_std: 0.012
32	    full_gen0_f1: 0.96
33	    full_gen1_f1: 0.81
34	    full_gen2plus_f1: 0.83
35	    ref_minus_surface_delta: 0.16
36	    mcnemar_p_ref_vs_surface: 3.0e-05
37	    permutation_importance_entropy_mean: 0.28
38	    permutation_importance_entropy_std: 0.19
39	    permutation_importance_hapax_ratio: 0.14
40	    permutation_importance_ttr: 0.09
41	  result_rationale: 'MVP feature importance (hapax_ratio=0.30) was inflated by XGBoost''s
42	    split-gain metric, which overweights high-cardinality continuous features with
43	    many useful split points. When surface features are ablated, the 5 reference-model
44	    features retain macro-F1=0.79 because they directly measure the generator''s deviation
45	    from the reference model''s next-token distribution — a signal that accumulates
46	    monotonically with depth as the generator''s output drifts further from human
47	    text. Entropy_mean captures the average surprise under the reference model (increases
48	    with depth as generated text occupies lower-probability regions), while entropy_std
49	    captures the increasing variance of surprise (deeper text alternates between familiar
50	    patterns and novel drift). Surface features alone (F1=0.63) capture only vocabulary
51	    impoverishment — TTR and hapax_ratio decline with depth as generators recycle
52	    high-frequency tokens — but this is a weaker, noisier proxy. The 0.16 delta and
53	    significant McNemar test confirm reference features carry independent, dominant
54	    signal. The full set achieves F1=0.87 (up from MVP''s 0.84) because retuned hyperparameters
55	    on the same data with proper ablation awareness extract slightly more complementary
56	    value. Permutation importance (which avoids split-gain bias) reranks entropy_mean
57	    as the top feature.
58	
59	    '
60	  tables:
61	  - name: 'Table 1: Feature Ablation Results (3-class depth classification)'
62	    columns:
63	    - Feature Set
64	    - Features
65	    - Macro-F1
66	    - gen-0 F1
67	    - gen-1 F1
68	    - gen-2+ F1
69	    - CV std
70	    rows:
71	    - - Reference-only
72	      - entropy_{mean,std,min,max}, tail_decay
73	      - 0.79
74	      - 0.91
75	      - 0.71
76	      - 0.74
77	      - 0.018
78	    - - Surface-only
79	      - ttr, hapax_ratio
80	      - 0.63
81	      - 0.82
82	      - 0.52
83	      - 0.55
84	      - 0.022
85	    - - Full
86	      - All 7 features
87	      - 0.87
88	      - 0.96
89	      - 0.81
90	      - 0.83
91	      - 0.012
92	    - - Δ (ref − surface)
93	      - —
94	      - '+0.16'
95	      - '+0.09'
96	      - '+0.19'
97	      - '+0.19'
98	      - —
99	  - name: 'Table 2: Permutation Importance (Full model, 5-fold mean)'
100	    columns:
101	    - Feature
102	    - Permutation Importance
103	    - XGBoost Gain (MVP)
104	    rows:
105	    - - entropy_mean
106	      - 0.28
107	      - 0.22
108	    - - entropy_std
109	      - 0.19
110	      - 0.13
111	    - - hapax_ratio
112	      - 0.14
113	      - 0.3
114	    - - tail_decay
115	      - 0.13
116	      - 0.06
117	    - - ttr
118	      - 0.09
119	      - 0.17
120	    - - entropy_max
121	      - 0.09
122	      - 0.07
123	    - - entropy_min
124	      - 0.08
125	      - 0.06
126	  figures_description:
127	  - 'Fig 1a: Grouped bar chart — Macro-F1 for ref-only / surface-only / full, with
128	    95% CI error bars from CV. Clear visual gap between ref-only and surface-only.'
129	  - 'Fig 1b: Per-class F1 heatmap (3 feature sets × 3 classes). Shows that the surface→ref
130	    gap is largest for gen-1 and gen-2+ (the harder classes), confirming reference
131	    features add discriminability precisely where surface shortcuts fail.'
132	  - 'Fig 1c: Permutation importance bar chart (full model) vs XGBoost gain bar chart
133	    (MVP). Side-by-side comparison reveals hapax_ratio''s gain was inflated; entropy_mean
134	    is the true top feature under permutation.'
135	  analysis: 'The ablation cleanly validates Claim 2. The ref-only advantage is strongest
136	    on gen-1 (Δ=+0.19) and gen-2+ (Δ=+0.19), the classes where surface features struggle
137	    most — TTR/hapax can separate human text from any synthetic text but cannot distinguish
138	    depth levels within synthetic text, because vocabulary impoverishment saturates
139	    quickly (mostly between gen-0→gen-1). Reference-model entropy features, by contrast,
140	    capture cumulative distributional drift that continues to grow between gen-1 and
141	    gen-2+. The reranking of feature importance under permutation (entropy_mean rises
142	    to 0.28, hapax_ratio drops to 0.14) directly addresses RC1 ("Is this just vocabulary
143	    impoverishment?") — it is not. The full model''s improvement to 0.87 suggests
144	    the two feature families capture partially orthogonal information: surface features
145	    provide a cheap gen-0 vs rest shortcut, while reference features provide the finer
146	    gen-1 vs gen-2+ signal.
147	
148	    '
149	- name: cross_generator_evaluation
150	  plan_id: plan_002
151	  description: 'Generate 25K chains: 1000 Wikipedia seeds × 5 generators (Pythia-2.8B,
152	    OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, Pythia-1B) × 5 depths. Feature extraction
153	    with Pythia-410M reference model. Leave-one-generator-out CV (train on 4 generators,
154	    test on held-out generator). Also report per-generator in-distribution results
155	    and per-class breakdowns.
156	
157	    '
158	  expected_results:
159	    leave_one_out_macro_f1_mean: 0.78
160	    leave_one_out_macro_f1_std: 0.03
161	    leave_one_out_gen1_f1_mean: 0.73
162	    leave_one_out_gen2plus_f1_mean: 0.75
163	    leave_one_out_gen0_f1_mean: 0.88
164	    in_distribution_5fold_macro_f1: 0.86
165	    per_generator_held_out:
166	      pythia_2_8b: 0.81
167	      olmo_2_1b: 0.77
168	      qwen3_5_2b: 0.76
169	      qwen3_5_0_8b: 0.74
170	      pythia_1b: 0.82
171	    total_chains_generated: 24200
172	    attrition_rate_pct: 3.2
173	    generation_gpu_hours: 18.5
174	  result_rationale: 'Cross-generator generalization holds (mean leave-one-out F1=0.78)
175	    because distributional drift is measured from the reference model''s perspective,
176	    not the generator''s. All generators produce text that progressively deviates
177	    from human text distribution as measured by Pythia-410M; the drift trajectory
178	    differs in magnitude but shares the same directional pattern (entropy increases,
179	    tail probability mass shifts). Pythia-family generators (2.8B, 1B) transfer best
180	    to each other (F1=0.81–0.82) due to shared pretraining distribution. Qwen3.5-0.8B
181	    is the hardest held-out case (F1=0.74) because its smaller capacity produces qualitatively
182	    different text that drifts faster at early depths — the classifier trained on
183	    larger models underestimates Qwen-0.8B''s depth. The gen-1 vs gen-2+ boundary
184	    remains the bottleneck (gen-1 F1=0.73) because gen-1 text from some generators
185	    overlaps with gen-2+ text from others in feature space. In-distribution pooled
186	    performance (0.86) is close to MVP (0.84) despite mixing generators, confirming
187	    that generator diversity adds training signal rather than noise. Attrition (~3.2%)
188	    is lower than MVP (3.7%) due to improved generation pipeline with retry logic.
189	
190	    '
191	  tables:
192	  - name: 'Table 3: Leave-One-Generator-Out Cross-Validation'
193	    columns:
194	    - Held-out Generator
195	    - Macro-F1
196	    - gen-0 F1
197	    - gen-1 F1
198	    - gen-2+ F1
199	    rows:
200	    - - Pythia-2.8B
201	      - 0.81
202	      - 0.91
203	      - 0.75
204	      - 0.77
205	    - - OLMo-2-1B
206	      - 0.77
207	      - 0.87
208	      - 0.72
209	      - 0.73
210	    - - Qwen3.5-2B
211	      - 0.76
212	      - 0.86
213	      - 0.71
214	      - 0.72
215	    - - Qwen3.5-0.8B
216	      - 0.74
217	      - 0.84
218	      - 0.68
219	      - 0.7
220	    - - Pythia-1B
221	      - 0.82
222	      - 0.92
223	      - 0.76
224	      - 0.78
225	    - - Mean ± std
226	      - 0.78 ± 0.03
227	      - 0.88 ± 0.03
228	      - 0.73 ± 0.03
229	      - 0.75 ± 0.03
230	  - name: 'Table 4: Per-Generator In-Distribution 5-Fold CV'
231	    columns:
232	    - Generator
233	    - Macro-F1
234	    - CV std
235	    rows:
236	    - - Pythia-2.8B
237	      - 0.85
238	      - 0.014
239	    - - OLMo-2-1B
240	      - 0.84
241	      - 0.016
242	    - - Qwen3.5-2B
243	      - 0.86
244	      - 0.013
245	    - - Qwen3.5-0.8B
246	      - 0.83
247	      - 0.019
248	    - - Pythia-1B
249	      - 0.84
250	      - 0.015
251	    - - Pooled (all 5)
252	      - 0.86
253	      - 0.011
254	  figures_description:
255	  - 'Fig 2a: Leave-one-out macro-F1 bar chart with error bars, generators ordered
256	    by held-out performance. Horizontal dashed line at 0.78 (mean). Shows Pythia-family
257	    clusters above mean, Qwen-0.8B below.'
258	  - 'Fig 2b: Confusion matrix heatmaps (5 panels, one per held-out generator). Highlights
259	    that gen-1↔gen-2+ confusion is the primary failure mode across all generators.'
260	  - 'Fig 2c: t-SNE of reference-model features colored by depth, faceted by generator.
261	    Shows that depth clusters are geometrically similar across generators despite
262	    generator-specific offsets in feature space.'
263	  analysis: 'The 0.78 mean leave-one-out F1 with narrow std (0.03) strongly supports
264	    Claim 1''s cross-generator generalization. The pattern is consistent: gen-0 is
265	    always well-separated (F1≥0.84), while gen-1 and gen-2+ form a harder boundary.
266	    Pythia-family transfer is strongest, suggesting some same-family distributional
267	    similarity, but even cross-family transfer (Pythia→Qwen) maintains F1≥0.74. This
268	    confirms the distributional fingerprint is a property of the generation process,
269	    not a generator-specific artifact. The pooled in-distribution result (0.86) exceeding
270	    any single-generator result suggests that multi-generator training improves robustness.
271	    For the paper, this table is the centerpiece of Claim 1 and directly addresses
272	    RC2.
273	
274	    '
275	- name: cross_family_reference_model
276	  plan_id: plan_003
277	  description: 'Re-extract features using non-Pythia reference models (OLMo-2-1B,
278	    Qwen3.5-0.8B) on the plan_002 dataset (25K chains). Compare classification performance
279	    across 3 reference model families. Tests whether the fingerprint is reference-model-agnostic.
280	
281	    '
282	  expected_results:
283	    pythia_410m_ref_macro_f1: 0.86
284	    olmo_2_1b_ref_macro_f1: 0.76
285	    qwen3_5_0_8b_ref_macro_f1: 0.74
286	    ensemble_3refs_macro_f1: 0.88
287	    cross_ref_leave_one_out_macro_f1: 0.75
288	    feature_correlation_pythia_olmo_entropy_mean: 0.82
289	    feature_correlation_pythia_qwen_entropy_mean: 0.78
290	  result_rationale: 'All three reference models detect depth signal (F1≥0.74) because
291	    any well-trained LM assigns progressively lower probability to deeper-generation
292	    text — the drift is a property of the text, not the measuring instrument. Pythia-410M
293	    performs best (0.86) because it was the reference model used during pipeline development
294	    and its capacity is calibrated for sensitivity to distributional shifts (small
295	    enough to be "surprised" by drift, large enough to model human text well). OLMo-2-1B
296	    (0.76) and Qwen3.5-0.8B (0.74) are slightly weaker because their different pretraining
297	    distributions create different baselines for "expected" text, adding noise to
298	    depth features. High cross-reference entropy_mean correlations (0.78–0.82) confirm
299	    that all three models agree on the direction of drift even if magnitudes differ.
300	    The 3-reference ensemble (0.88) exceeds any single reference, indicating that
301	    diverse reference models capture complementary aspects of distributional drift.
302	    This decisively addresses RC2 — the signal is not a Pythia-specific artifact.
303	
304	    '
305	  tables:
306	  - name: 'Table 5: Reference Model Comparison (pooled 5-generator data)'
307	    columns:
308	    - Reference Model
309	    - Family
310	    - Params
311	    - Macro-F1
312	    - gen-0 F1
313	    - gen-1 F1
314	    - gen-2+ F1
315	    rows:
316	    - - Pythia-410M
317	      - Pythia
318	      - 410M
319	      - 0.86
320	      - 0.95
321	      - 0.8
322	      - 0.82
323	    - - OLMo-2-1B
324	      - OLMo
325	      - 1B
326	      - 0.76
327	      - 0.88
328	      - 0.69
329	      - 0.72
330	    - - Qwen3.5-0.8B
331	      - Qwen
332	      - 0.8B
333	      - 0.74
334	      - 0.86
335	      - 0.66
336	      - 0.7
337	    - - Ensemble (3 refs)
338	      - Mixed
339	      - —
340	      - 0.88
341	      - 0.96
342	      - 0.83
343	      - 0.85
344	  - name: 'Table 6: Pairwise Feature Correlation (Spearman ρ) Across Reference Models'
345	    columns:
346	    - Feature
347	    - Pythia↔OLMo
348	    - Pythia↔Qwen
349	    - OLMo↔Qwen
350	    rows:
351	    - - entropy_mean
352	      - 0.82
353	      - 0.78
354	      - 0.8
355	    - - entropy_std
356	      - 0.79
357	      - 0.74
358	      - 0.76
359	    - - tail_decay
360	      - 0.71
361	      - 0.66
362	      - 0.69
363	  figures_description:
364	  - 'Fig 3a: Parallel coordinates plot showing entropy_mean distributions by depth,
365	    one panel per reference model. Monotonic increase with depth visible in all three,
366	    confirming H₂ across reference architectures.'
367	  - 'Fig 3b: Scatter matrix of entropy_mean values across reference model pairs, colored
368	    by depth. Strong positive correlation with depth-dependent clustering confirms
369	    cross-reference consistency.'
370	  analysis: 'The cross-family validation eliminates the concern that Pythia-410M has
371	    some idiosyncratic sensitivity to synthetic text. All three reference architectures
372	    detect monotonic distributional drift. The ensemble''s improvement to 0.88 provides
373	    an optional "best-effort" configuration for practitioners, though the single-reference
374	    Pythia-410M result (0.86) is sufficient for the paper''s claims. The correlation
375	    analysis (Table 6) is particularly informative: high but imperfect correlations
376	    indicate that reference models measure the same underlying phenomenon through
377	    slightly different lenses, explaining why ensembling helps. For the paper, this
378	    experiment transforms a potential weakness (Pythia-only evaluation) into a strength
379	    (reference-model-agnostic signal).
380	
381	    '
382	- name: downstream_utility
383	  plan_id: plan_004
384	  description: 'Fine-tune Pythia-410M on depth-stratified subsets of the plan_002
385	    data. Measure perplexity on held-out human test set as function of training data
386	    depth composition. Compare depth-aware filtering (keep gen-0 + gen-1, discard
387	    gen-2+) vs binary baselines (FastDetectGPT threshold, LD-Score threshold) for
388	    preserving downstream model quality.
389	
390	    '
391	  expected_results:
392	    depth_quality_spearman_rho: 0.72
393	    ppl_gen0_only: 28.3
394	    ppl_gen1_only: 30.1
395	    ppl_gen2_only: 34.7
396	    ppl_gen3_only: 38.9
397	    ppl_gen4_only: 43.2
398	    ppl_mixed_uniform: 35.8
399	    ppl_depth_filtered_gen01: 29.0
400	    ppl_binary_fastdetectgpt: 31.8
401	    ppl_binary_ldscore: 32.1
402	    ppl_human_baseline: 27.5
403	    depth_filter_vs_binary_gap_pct: 5.2
404	    training_samples_kept_depth_filter: 0.42
405	    training_samples_kept_binary: 0.28
406	  result_rationale: 'Perplexity increases monotonically with training data depth (28.3→43.2
407	    from gen-0→gen-4) because deeper-generation text has compounded distributional
408	    drift from human text — fine-tuning on it shifts the model''s learned distribution
409	    away from the human test set. The Spearman ρ=0.72 between depth and perplexity
410	    is strong but not perfect because individual samples vary in drift magnitude (some
411	    gen-3 texts are less drifted than some gen-2 texts). Depth-aware filtering (keep
412	    gen-0+gen-1, perplexity=29.0) outperforms binary baselines (~31.8–32.1) by 5.2%
413	    because binary detectors discard all synthetic text including useful gen-1 content
414	    that is distributionally close to human text. Binary filtering retains only 28%
415	    of data (mostly gen-0) while depth filtering retains 42% (gen-0 + gen-1), providing
416	    more training data of acceptable quality. The gap between gen-0-only (28.3) and
417	    depth-filtered (29.0) is small, confirming that gen-1 text is nearly as good as
418	    human text for training — the key practical insight for data curation.
419	
420	    '
421	  tables:
422	  - name: 'Table 7: Fine-tuning Perplexity by Training Data Depth'
423	    columns:
424	    - Training Data
425	    - Depth Composition
426	    - PPL (↓)
427	    - Samples Used
428	    rows:
429	    - - Human-only
430	      - gen-0
431	      - 28.3
432	      - ~4800
433	    - - gen-1 only
434	      - gen-1
435	      - 30.1
436	      - ~4750
437	    - - gen-2 only
438	      - gen-2
439	      - 34.7
440	      - ~4500
441	    - - gen-3 only
442	      - gen-3
443	      - 38.9
444	      - ~4200
445	    - - gen-4 only
446	      - gen-4
447	      - 43.2
448	      - ~3900
449	    - - Uniform mix
450	      - gen-0–4 equal
451	      - 35.8
452	      - ~22000
453	    - - Depth-filtered (ours)
454	      - gen-0 + gen-1
455	      - 29.0
456	      - ~9500
457	    - - FastDetectGPT filter
458	      - binary threshold
459	      - 31.8
460	      - ~6300
461	    - - LD-Score filter
462	      - binary threshold
463	      - 32.1
464	      - ~6100
465	    - - Human test baseline
466	      - —
467	      - 27.5
468	      - —
469	  - name: 'Table 8: Depth-Aware vs Binary Filtering Comparison'
470	    columns:
471	    - Method
472	    - PPL
473	    - Data Retained (%)
474	    - PPL Gap to Human-Only
475	    rows:
476	    - - Depth-filtered (gen-0+1)
477	      - 29.0
478	      - 42%
479	      - '+0.7'
480	    - - FastDetectGPT binary
481	      - 31.8
482	      - 28%
483	      - '+3.5'
484	    - - LD-Score binary
485	      - 32.1
486	      - 26%
487	      - '+3.8'
488	    - - No filtering (all data)
489	      - 35.8
490	      - 100%
491	      - '+7.5'
492	  figures_description:
493	  - 'Fig 4a: Line plot — perplexity vs generation depth (gen-0 through gen-4). Monotonic
494	    increase with 95% CI bands from 3 random seeds. Confirms H₂''s downstream consequence.'
495	  - 'Fig 4b: Bar chart comparing filtering strategies (depth-aware, FastDetectGPT,
496	    LD-Score, no filter) on perplexity and data retention. Dual y-axis: bars for perplexity,
497	    overlaid line for % data retained.'
498	  - 'Fig 4c: Scatter plot — predicted depth score vs actual fine-tuning perplexity
499	    contribution per sample, with Spearman ρ annotation. Shows the sample-level correlation
500	    between depth estimate and quality impact.'
501	  analysis: 'This experiment validates Claim 3 and provides the practical punchline
502	    of the paper. The monotonic perplexity curve (Fig 4a) is the most intuitive visualization
503	    of H₂ — it translates distributional drift into a metric practitioners care about.
504	    The 5.2% gap between depth-aware and binary filtering is meaningful because it
505	    comes with MORE data retained (42% vs 28%), resolving the precision-recall tradeoff
506	    that plagues binary detection. The key insight is that gen-1 text is "good enough"
507	    for training (PPL=30.1 vs human 28.3), but gen-2+ is not (PPL≥34.7). Binary detectors
508	    cannot make this distinction. For AAAI reviewers, this experiment connects the
509	    theoretical contribution (distributional drift characterization) to a practical
510	    application (data curation), which is important for venue fit.
511	
512	    '
513	- name: prompt_type_comparison
514	  plan_id: plan_005
515	  description: 'Generate chains with 3 prompt types (continuation, elaboration, inspired_rewriting)
516	    using Pythia-2.8B on 1000 Wikipedia seeds × 5 depths. Compare depth signal preservation
517	    across prompt types. Tests whether semantic divergence from source correlates
518	    with depth signal.
519	
520	    '
521	  expected_results:
522	    continuation_macro_f1: 0.85
523	    elaboration_macro_f1: 0.8
524	    inspired_rewriting_macro_f1: 0.72
525	    continuation_entropy_drift_per_depth: 0.18
526	    elaboration_entropy_drift_per_depth: 0.14
527	    inspired_rewriting_entropy_drift_per_depth: 0.1
528	    cross_prompt_train_test_macro_f1: 0.74
529	    prompt_type_drift_rate_spearman: 0.91
530	  result_rationale: 'Continuation preserves the strongest depth signal (F1=0.85) because
531	    each generation step continues directly from the previous output, maximizing the
532	    accumulation of distributional drift. Elaboration (F1=0.80) injects some new semantic
533	    direction via the prompt instruction, which partially resets the drift trajectory
534	    at each step — drift still accumulates but at a slower rate. Inspired rewriting
535	    (F1=0.72) has the most semantic freedom: the model is instructed to produce text
536	    "inspired by" the input, allowing it to diverge from the drift trajectory and
537	    partially re-anchor to its pretraining distribution. The strong correlation between
538	    per-depth entropy drift rate and classification F1 (Spearman ρ=0.91) confirms
539	    the theoretical prediction: more constrained generation → faster drift accumulation
540	    → stronger depth signal. Cross-prompt-type transfer (F1=0.74) is moderate, indicating
541	    that the drift signature is partially shared across prompt types but the rate
542	    differences create distribution shift in feature space.
543	
544	    '
545	  tables:
546	  - name: 'Table 9: Depth Classification by Prompt Type'
547	    columns:
548	    - Prompt Type
549	    - Macro-F1
550	    - gen-0 F1
551	    - gen-1 F1
552	    - gen-2+ F1
553	    - Entropy Drift Rate
554	    rows:
555	    - - Continuation
556	      - 0.85
557	      - 0.95
558	      - 0.79
559	      - 0.81
560	      - 0.18 nats/depth
561	    - - Elaboration
562	      - 0.8
563	      - 0.92
564	      - 0.73
565	      - 0.75
566	      - 0.14 nats/depth
567	    - - Inspired rewriting
568	      - 0.72
569	      - 0.86
570	      - 0.64
571	      - 0.67
572	      - 0.10 nats/depth
573	  figures_description:
574	  - 'Fig 5a: Line plots — entropy_mean vs depth for each prompt type, showing different
575	    drift rates. Continuation has steepest slope.'
576	  - 'Fig 5b: Scatter plot — prompt type drift rate vs macro-F1, confirming linear
577	    relationship. Three points with regression line and ρ annotation.'
578	  analysis: 'This experiment decomposes the depth signal by generation modality. The
579	    ordering (continuation > elaboration > inspired rewriting) aligns with the theoretical
580	    framework: the more the generation task constrains the output to build on previous
581	    text, the more drift accumulates. Inspired rewriting''s lower F1 is not a failure
582	    — it confirms the mechanism. For the paper, this comparison strengthens the theoretical
583	    story by showing that depth signal is graded, not binary, and correlates with
584	    the degree of semantic coupling between successive generation steps.
585	
586	    '
587	- name: paraphrastic_comparison
588	  plan_id: plan_006
589	  description: 'Construct parallel paraphrasing chains (same 1000 seeds, Pythia-2.8B,
590	    5 depths) alongside continuation chains. Measure whether paraphrastic chains converge
591	    (per attractor theory) while continuation chains diverge (our H₂). Direct empirical
592	    test of H₁ vs H₂.
593	
594	    '
595	  expected_results:
596	    paraphrase_macro_f1_3class: 0.58
597	    paraphrase_gen0_f1: 0.81
598	    paraphrase_gen1_f1: 0.46
599	    paraphrase_gen2plus_f1: 0.47
600	    continuation_macro_f1_3class: 0.85
601	    paraphrase_entropy_drift_depth3: 0.06
602	    continuation_entropy_drift_depth3: 0.52
603	    paraphrase_cycle_detection_pct: 68.0
604	    divergence_test_ks_statistic: 0.41
605	    divergence_test_p_value: 1.0e-05
606	  result_rationale: 'Paraphrastic chains show weak depth signal (F1=0.58) because
607	    the semantic preservation constraint of paraphrasing creates attractor dynamics
608	    — the text oscillates around a fixed semantic point, and distributional features
609	    converge after ~2 steps (confirming ACL 2025 attractor cycle theory). By depth
610	    3, paraphrastic entropy drift has nearly plateaued (0.06 nats) while continuation
611	    drift continues growing (0.52 nats). The 68% cycle detection rate in paraphrastic
612	    chains (text at depth d is more similar to depth d-2 than d-1) directly corroborates
613	    the 2-period attractor cycle prediction. Continuation chains show no such periodicity
614	    — drift is monotonic. The KS test between depth-3 entropy distributions of paraphrastic
615	    vs continuation chains (D=0.41, p<0.001) provides the statistical test of H₁ vs
616	    H₂. This is the most theoretically clean result in the paper: H₂ (divergence)
617	    holds for non-paraphrastic chains, H₁ (convergence) holds for paraphrastic chains,
618	    exactly as predicted by the semantic constraint difference.
619	
620	    '
621	  tables:
622	  - name: 'Table 10: Paraphrastic vs Continuation Chain Comparison'
623	    columns:
624	    - Chain Type
625	    - Macro-F1
626	    - Entropy Drift @depth3
627	    - Cycle Detection %
628	    rows:
629	    - - Continuation
630	      - 0.85
631	      - 0.52 nats
632	      - < 5%
633	    - - Paraphrasing
634	      - 0.58
635	      - 0.06 nats
636	      - 68%
637	    - - Δ
638	      - '+0.27'
639	      - +0.46 nats
640	      - —
641	  figures_description:
642	  - 'Fig 6a: Dual-panel line plot — entropy_mean vs depth for continuation (diverging)
643	    and paraphrasing (converging). The visual contrast is the paper''s most compelling
644	    figure.'
645	  - 'Fig 6b: Autocorrelation plot of entropy_mean sequence across depths for paraphrastic
646	    chains, showing the period-2 oscillation pattern predicted by attractor theory.'
647	  analysis: 'This is the experiment that elevates the paper from "a depth classifier"
648	    to "an empirical test of distributional dynamics in recursive generation." The
649	    clean separation between convergent (paraphrastic) and divergent (non-paraphrastic)
650	    chains validates the core theoretical insight and connects our work to the ACL
651	    2025 attractor cycle literature. H₂ is confirmed for non-paraphrastic chains:
652	    drift accumulates monotonically, enabling depth estimation. H₁ is confirmed for
653	    paraphrastic chains: convergence limits depth signal to ~2 classes. This dual
654	    result explains WHY our approach works and WHY prior work on paraphrasing chains
655	    found limited depth discriminability.
656	
657	    '
658	- name: cross_model_chains
659	  plan_id: plan_007
660	  description: 'Generate cross-model chains where each depth step uses a different
661	    generator (randomly sampled from the 5 generators). 1000 seeds × 5 depths. Compares
662	    cross-model chain depth classification to single-model chains. More realistic
663	    scenario — real web contamination involves diverse generators.
664	
665	    '
666	  expected_results:
667	    cross_model_chain_macro_f1: 0.75
668	    single_model_chain_macro_f1_mean: 0.85
669	    cross_model_gen0_f1: 0.9
670	    cross_model_gen1_f1: 0.68
671	    cross_model_gen2plus_f1: 0.67
672	    cross_model_entropy_drift_per_depth: 0.13
673	    cross_vs_single_model_delta: -0.1
674	  result_rationale: 'Cross-model chains are harder to classify (F1=0.75 vs single-model
675	    0.85) because generator switching introduces distributional discontinuities —
676	    each new generator has its own distributional signature that partially masks the
677	    monotonic drift signal. However, F1=0.75 is still well above chance (0.33) and
678	    practically useful, because the underlying drift phenomenon persists: even when
679	    generators change, the cumulative deviation from human text distribution still
680	    increases with depth. The gen-1 and gen-2+ classes are most affected (F1=0.68,
681	    0.67) because generator-switching noise is most confusing for the middle classes.
682	    Gen-0 remains well-separated (F1=0.90) because human text is fundamentally different
683	    from any generator''s output. The 10-point drop from single-model is a known cost
684	    that should be reported transparently — it bounds the method''s real-world applicability
685	    but does not invalidate the approach. Entropy drift rate (0.13 nats/depth) is
686	    lower than single-model continuation (0.18) because generator transitions partially
687	    reset drift.
688	
689	    '
690	  tables:
691	  - name: 'Table 11: Single-Model vs Cross-Model Chain Comparison'
692	    columns:
693	    - Chain Type
694	    - Macro-F1
695	    - gen-0 F1
696	    - gen-1 F1
697	    - gen-2+ F1
698	    rows:
699	    - - Single-model (mean of 5)
700	      - 0.85
701	      - 0.95
702	      - 0.79
703	      - 0.81
704	    - - Cross-model (random switch)
705	      - 0.75
706	      - 0.9
707	      - 0.68
708	      - 0.67
709	    - - Δ
710	      - '-0.10'
711	      - '-0.05'
712	      - '-0.11'
713	      - '-0.14'
714	  figures_description:
715	  - 'Fig 7: Box plot of entropy_mean by depth for cross-model chains. Wider boxes
716	    than single-model chains reflect generator-switching variance, but median still
717	    increases monotonically.'
718	  analysis: 'The 10-point F1 drop is the honest cost of ecological validity. Reviewers
719	    (RC4) will ask about this — reporting it transparently strengthens the paper.
720	    The key takeaway is that depth signal survives cross-model chains despite generator-switching
721	    noise, maintaining F1=0.75. For practical data curation, this means depth-aware
722	    filtering still provides value even when contamination sources are diverse. The
723	    fact that gen-0 F1 remains at 0.90 means the method''s primary utility (separating
724	    human from any-depth synthetic) is robust; the finer-grained depth estimation
725	    within synthetic text is where accuracy degrades.
726	
727	    '
728	- name: multi_domain_seeds
729	  plan_id: plan_008
730	  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific
731	    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5
732	    generators × 5 depths. Tests domain generalization of depth signal.
733	
734	    '
735	  expected_results:
736	    wikipedia_macro_f1: 0.86
737	    news_macro_f1: 0.83
738	    scientific_macro_f1: 0.81
739	    creative_macro_f1: 0.78
740	    cross_domain_leave_one_out_f1: 0.77
741	    pooled_all_domains_f1: 0.84
742	    domain_variance_of_f1: 0.0009
743	  result_rationale: 'Wikipedia performs best (0.86) because it matches the MVP setting
744	    and has the most structured, information-dense text that generators struggle to
745	    faithfully continue. News is close (0.83) due to similar factual density. Scientific
746	    text (0.81) has domain-specific vocabulary that somewhat masks depth drift in
747	    surface features, but reference-model features still capture the signal. Creative
748	    writing is hardest (0.78) because generators produce more fluent, human-like creative
749	    text — the distributional gap between human and generated creative writing is
750	    smaller than for factual domains, reducing the overall drift magnitude. Cross-domain
751	    leave-one-out (0.77) confirms that the depth signal generalizes across domains,
752	    though some domain-specific calibration is lost. The low variance (0.0009) across
753	    domains indicates that depth signal is a robust, domain-general phenomenon. Pooled
754	    performance (0.84) suggests that multi-domain training is beneficial — diverse
755	    training data helps the classifier learn domain-invariant depth features.
756	
757	    '
758	  tables:
759	  - name: 'Table 12: Multi-Domain Depth Classification'
760	    columns:
761	    - Domain
762	    - Seeds
763	    - Macro-F1
764	    - gen-0 F1
765	    - gen-1 F1
766	    - gen-2+ F1
767	    rows:
768	    - - Wikipedia
769	      - 500
770	      - 0.86
771	      - 0.95
772	      - 0.8
773	      - 0.82
774	    - - News
775	      - 500
776	      - 0.83
777	      - 0.93
778	      - 0.77
779	      - 0.79
780	    - - Scientific
781	      - 500
782	      - 0.81
783	      - 0.91
784	      - 0.74
785	      - 0.77
786	    - - Creative
787	      - 500
788	      - 0.78
789	      - 0.88
790	      - 0.71
791	      - 0.74
792	    - - Pooled (all)
793	      - 2000
794	      - 0.84
795	      - 0.93
796	      - 0.78
797	      - 0.8
798	    - - Leave-one-domain-out
799	      - —
800	      - 0.77
801	      - 0.88
802	      - 0.7
803	      - 0.73
804	  figures_description:
805	  - 'Fig 8: Faceted violin plot of entropy_mean by depth, one panel per domain. All
806	    domains show monotonic drift but with different baseline offsets and drift rates.'
807	  analysis: 'Domain generalization confirms that distributional drift is not an artifact
808	    of Wikipedia-style text. The ordering (factual > creative) is interpretable and
809	    provides nuance for practitioners: depth estimation is most reliable for factual
810	    domains where generators have clear distributional signatures. The cross-domain
811	    leave-one-out result (0.77) is strong enough to claim domain generalization in
812	    the paper. For AAAI, including 4 domains in the evaluation addresses RC6 and demonstrates
813	    ecological validity.
814	
815	    '
816	- name: finer_grained_ordinal
817	  plan_id: plan_009
818	  description: '5-class ordinal classification (gen-0 through gen-4) on the plan_002
819	    data. Tests whether non-paraphrastic chains support finer-grained depth estimation
820	    beyond the 3-class setup.
821	
822	    '
823	  expected_results:
824	    ordinal_5class_macro_f1: 0.62
825	    ordinal_5class_gen0_f1: 0.92
826	    ordinal_5class_gen1_f1: 0.68
827	    ordinal_5class_gen2_f1: 0.52
828	    ordinal_5class_gen3_f1: 0.48
829	    ordinal_5class_gen4_f1: 0.51
830	    ordinal_mae: 0.58
831	    ordinal_spearman_rho: 0.83
832	    adjacent_class_confusion_pct: 72.0
833	  result_rationale: '5-class F1 (0.62) is lower than 3-class (0.86) because deeper
834	    classes (gen-2/gen-3/gen-4) have progressively overlapping feature distributions
835	    — drift accumulates but with diminishing marginal signal per step. Gen-0 remains
836	    easy (F1=0.92), gen-1 is moderate (F1=0.68), and gen-2/3/4 are difficult (F1≈0.48–0.52)
837	    because the distributional differences between adjacent deep classes are small.
838	    However, the high Spearman ρ (0.83) and low MAE (0.58) indicate that the classifier''s
839	    errors are ordinal — when it misclassifies, it predicts an adjacent class (72%
840	    of errors are off-by-one), not a distant one. This supports ordinal regression
841	    as a natural formulation and suggests that while exact depth prediction is noisy
842	    for deep classes, the relative ordering is preserved. For the paper, this result
843	    supports the claim that drift is monotonic (H₂) while honestly reporting the practical
844	    ceiling on depth resolution.
845	
846	    '
847	  tables:
848	  - name: 'Table 13: 5-Class Ordinal Depth Classification'
849	    columns:
850	    - Class
851	    - Precision
852	    - Recall
853	    - F1
854	    rows:
855	    - - gen-0
856	      - 0.93
857	      - 0.91
858	      - 0.92
859	    - - gen-1
860	      - 0.66
861	      - 0.7
862	      - 0.68
863	    - - gen-2
864	      - 0.5
865	      - 0.54
866	      - 0.52
867	    - - gen-3
868	      - 0.47
869	      - 0.49
870	      - 0.48
871	    - - gen-4
872	      - 0.53
873	      - 0.5
874	      - 0.51
875	    - - Macro
876	      - —
877	      - —
878	      - 0.62
879	  - name: 'Table 13b: Ordinal Error Analysis'
880	    columns:
881	    - Metric
882	    - Value
883	    rows:
884	    - - MAE
885	      - 0.58
886	    - - Spearman ρ (pred vs true depth)
887	      - 0.83
888	    - - Adjacent-class confusion (%)
889	      - 72%
890	  figures_description:
891	  - 'Fig 9a: 5×5 confusion matrix heatmap. Diagonal + adjacent-diagonal cells are
892	    dark, confirming ordinal error structure.'
893	  - 'Fig 9b: Predicted depth (box plot) vs true depth. Boxes overlap for gen-2/3/4
894	    but medians increase monotonically.'
895	  analysis: 'The 5-class result characterizes the resolution ceiling of distributional
896	    fingerprints. While exact depth-4 vs depth-3 discrimination is weak, the ordinal
897	    structure is strong (ρ=0.83). This has practical implications: for data curation,
898	    coarse depth buckets (gen-0 / gen-1 / gen-2+) are more useful than exact depth
899	    anyway — the key decision boundary is "how much drift is tolerable." The result
900	    also differentiates our work from attractor theory: paraphrastic chains converge
901	    to ~2 distinguishable classes, while our non-paraphrastic chains support at least
902	    3 clean classes and 5 ordinal classes. This directly addresses RC3.
903	
904	    '
905	- name: human_edit_robustness
906	  plan_id: plan_010
907	  description: 'Robustness test on plan_002 data with simulated edits: (A) random
908	    word replacement at 5%, 10%, 20% rates, (B) LLM-simulated light editing (rephrase
909	    random sentences). Tests depth signal persistence under post-generation editing.
910	
911	    '
912	  expected_results:
913	    no_edit_macro_f1: 0.86
914	    random_5pct_macro_f1: 0.83
915	    random_10pct_macro_f1: 0.78
916	    random_20pct_macro_f1: 0.67
917	    llm_light_edit_macro_f1: 0.76
918	    degradation_slope_per_10pct: -0.095
919	  result_rationale: 'Random word replacement at 5% has minimal impact (F1=0.83, Δ=-0.03)
920	    because replacing 5% of tokens introduces noise uniformly across all depth classes,
921	    preserving the relative distributional differences. At 10% (F1=0.78), the noise
922	    begins to mask depth-specific features — entropy statistics become noisier as
923	    random words inject unpredictable surprise values. At 20% (F1=0.67), substantial
924	    text corruption disrupts the distributional fingerprint significantly but performance
925	    remains above chance (0.33). LLM-simulated editing (F1=0.76) is comparable to
926	    10% random replacement because light rephrasing changes surface statistics but
927	    largely preserves the underlying distributional structure — the edited text still
928	    occupies the same region of reference-model feature space. The degradation is
929	    approximately linear (-0.095 F1 per 10% edit rate), providing a simple model for
930	    practitioners to assess signal reliability given estimated editing rates. These
931	    results address RC5 while honestly reporting the method''s sensitivity to post-generation
932	    modification.
933	
934	    '
935	  tables:
936	  - name: 'Table 14: Robustness to Simulated Edits'
937	    columns:
938	    - Edit Type
939	    - Edit Rate
940	    - Macro-F1
941	    - Δ from No-Edit
942	    rows:
943	    - - None (baseline)
944	      - 0%
945	      - 0.86
946	      - —
947	    - - Random word replacement
948	      - 5%
949	      - 0.83
950	      - '-0.03'
951	    - - Random word replacement
952	      - 10%
953	      - 0.78
954	      - '-0.08'
955	    - - Random word replacement
956	      - 20%
957	      - 0.67
958	      - '-0.19'
959	    - - LLM light editing
960	      - ~8–12%
961	      - 0.76
962	      - '-0.10'
963	  figures_description:
964	  - 'Fig 10: Line plot — macro-F1 vs edit rate. Linear degradation with 95% CI band.
965	    Horizontal dashed line at chance level (0.33). Annotation at 10% edit rate: ''typical
966	    human editing range.'''
967	  analysis: 'The robustness profile is realistic for practical deployment. Light editing
968	    (5–10%) typical of human post-processing preserves most of the depth signal. Heavy
969	    editing (20%) degrades performance significantly but remains above chance, suggesting
970	    that even heavily edited text retains some distributional fingerprint. For the
971	    paper, this experiment provides the necessary caveat about real-world applicability
972	    while showing that the method is viable for the most common use case (lightly
973	    edited or unedited synthetic text in web-scraped data).
974	
975	    '
976	- name: ld_score_feature
977	  plan_id: plan_011
978	  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)
979	    as an additional feature to the plan_001 ablation framework. Tests whether character-level
980	    features provide complementary depth signal beyond token-level distributional
981	    features.
982	
983	    '
984	  expected_results:
985	    full_plus_ld_macro_f1: 0.88
986	    ld_score_only_macro_f1: 0.59
987	    ld_score_permutation_importance: 0.06
988	    full_plus_ld_vs_full_delta: 0.01
989	  result_rationale: 'LD-Score alone achieves modest depth discrimination (F1=0.59)
990	    because character-level distributional signatures capture some depth-dependent
991	    patterns — deeper generation text has slightly more uniform character distributions
992	    as vocabulary impoverishment affects character-level statistics. However, adding
993	    LD-Score to the full feature set provides only marginal improvement (Δ=+0.01)
994	    because LD-Score''s signal is largely redundant with existing surface features
995	    (TTR, hapax_ratio) — both measure vocabulary impoverishment, just at different
996	    granularities (character vs word level). The low permutation importance (0.06)
997	    confirms that LD-Score is not providing new information. This is a useful negative-ish
998	    result: it shows that character-level features do not add a fundamentally new
999	    signal modality, reinforcing that the key complementary feature families are surface
1000	    vocabulary statistics and reference-model distributional features.
1001	
1002	    '
1003	  tables:
1004	  - name: 'Table 15: LD-Score Feature Integration'
1005	    columns:
1006	    - Feature Set
1007	    - Macro-F1
1008	    - Δ from Full
1009	    rows:
1010	    - - Full (7 features)
1011	      - 0.87
1012	      - —
1013	    - - Full + LD-Score (8 features)
1014	      - 0.88
1015	      - '+0.01'
1016	    - - LD-Score only
1017	      - 0.59
1018	      - '-0.28'
1019	  figures_description:
1020	  - 'Fig S1 (supplementary): Feature importance bar chart with LD-Score included.
1021	    LD-Score ranks below all reference-model features.'
1022	  analysis: 'A clean but unexciting result that belongs in the supplementary material.
1023	    It confirms the two-modality structure of depth signal (reference-model entropy
1024	    + surface vocabulary) and shows that adding more surface-level features (even
1025	    at a different granularity) does not expand the signal envelope. For the paper,
1026	    this addresses potential questions about "what about other feature types" and
1027	    justifies the focus on reference-model features as the novel contribution.
1028	
1029	    '
1030	- name: end_to_end_classifier
1031	  plan_id: plan_012
1032	  description: 'QLoRA fine-tune Qwen3.5-0.8B for end-to-end depth classification (directly
1033	    from text, no handcrafted features). Compares learned representations vs handcrafted
1034	    distributional features on the plan_002 dataset.
1035	
1036	    '
1037	  expected_results:
1038	    qwen_qlora_macro_f1: 0.83
1039	    qwen_qlora_gen0_f1: 0.94
1040	    qwen_qlora_gen1_f1: 0.77
1041	    qwen_qlora_gen2plus_f1: 0.79
1042	    handcrafted_features_macro_f1: 0.86
1043	    qwen_qlora_cross_gen_leave_one_out_f1: 0.71
1044	    handcrafted_cross_gen_leave_one_out_f1: 0.78
1045	    qwen_qlora_training_gpu_hours: 12.0
1046	    handcrafted_training_time_minutes: 3.0
1047	  result_rationale: 'The QLoRA fine-tuned model achieves competitive in-distribution
1048	    performance (F1=0.83 vs handcrafted 0.86) because the transformer can implicitly
1049	    learn distributional features from raw text. However, it underperforms the handcrafted
1050	    approach for two reasons: (1) the handcrafted features distill the reference model''s
1051	    perspective into compact statistics that directly measure what matters (distributional
1052	    drift from human text), while the fine-tuned model must learn this implicitly
1053	    from text patterns; (2) the XGBoost classifier on 7 features is harder to overfit
1054	    than a 0.8B parameter model on ~25K training examples. The larger gap in cross-generator
1055	    leave-one-out (0.71 vs 0.78) reveals that the fine-tuned model memorizes generator-specific
1056	    artifacts more than the handcrafted features, which are designed to be generator-invariant.
1057	    The 4000× training time difference (12 GPU-hours vs 3 minutes) makes the handcrafted
1058	    approach clearly preferable for practical deployment. This result validates the
1059	    feature engineering approach over brute-force fine-tuning and justifies the paper''s
1060	    focus on interpretable distributional features.
1061	
1062	    '
1063	  tables:
1064	  - name: 'Table 16: End-to-End vs Feature-Based Comparison'
1065	    columns:
1066	    - Method
1067	    - In-Dist F1
1068	    - Cross-Gen F1
1069	    - Training Cost
1070	    rows:
1071	    - - XGBoost + handcrafted features
1072	      - 0.86
1073	      - 0.78
1074	      - 3 min
1075	    - - QLoRA Qwen3.5-0.8B
1076	      - 0.83
1077	      - 0.71
1078	      - 12 GPU·h
1079	    - - Δ (handcrafted − QLoRA)
1080	      - '+0.03'
1081	      - '+0.07'
1082	      - —
1083	  figures_description:
1084	  - 'Fig S2 (supplementary): Paired bar chart — in-distribution vs cross-generator
1085	    F1 for both methods. Handcrafted features show smaller generalization gap.'
1086	  analysis: 'This is a strategically important result. Reviewers might ask "why not
1087	    just fine-tune a model?" — this experiment shows that handcrafted features outperform,
1088	    generalize better, are 4000× cheaper to train, and are interpretable (you can
1089	    point to specific features and explain why they work). The fine-tuned model''s
1090	    worse cross-generator generalization is the most telling result: it confirms that
1091	    the handcrafted features capture the right abstraction (distributional drift as
1092	    measured by a reference model) while the fine-tuned model takes shortcuts via
1093	    generator-specific patterns. This result belongs in the supplementary material
1094	    and reinforces the paper''s methodological choice.'
1095	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "527e66b2-00a1-47a3-8f11-b9af33b134e0",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "86d208c1-ae90-408e-a1b4-fb9dd103a0a2",
  "sourceToolAssistantUUID": "527e66b2-00a1-47a3-8f11-b9af33b134e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T18:44:13.110Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SRTZEiNNsyjR1JG8A1Vid7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86d208c1-ae90-408e-a1b4-fb9dd103a0a2",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xMpWhfZZue7J8SHFqT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bc6d653-4346-4f08-a54d-3b8e997821d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEdNKXm3uC3LEcy3yUJk3g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12679,
      "cache_read_input_tokens": 48174,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12679
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 48174,
          "cache_creation_input_tokens": 12679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12679,
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

_source line 40 · 2026-05-14T18:44:13.467Z_

<details><summary>↩ Tool result · `toolu_01SRTZEiNNsyjR1JG8A1Vid7`</summary>

```text
1	tier: best
2	narrative_guidance: 'Original framing fully intact. Story: non-paraphrastic chains
3	  exhibit monotonic distributional divergence (H₂ confirmed), detectable via reference-model
4	  entropy features that capture drift beyond surface vocabulary impoverishment. Headline:
5	  "distributional fingerprints enable risk-stratified data curation," with clean ablation
6	  separating signal from shortcut. All three claims stated at full strength. AAAI
7	  submission with no scope reduction.
8	
9	  '
10	imagined_experiments:
11	- name: feature_ablation
12	  plan_id: plan_001
13	  description: 'Ablation on existing MVP data (4609 records, Pythia-2.8B generator,
14	    Pythia-410M reference, Wikipedia seeds). Three conditions: (A) reference-only
15	    features (entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay), (B)
16	    surface-only features (ttr, hapax_ratio), (C) full 7-feature set. Same XGBoost
17	    classifier, 5-fold stratified CV, 3-class (gen-0/gen-1/gen-2+).
18	
19	    '
20	  expected_results:
21	    ref_only_macro_f1: 0.79
22	    ref_only_cv_std: 0.018
23	    ref_only_gen0_f1: 0.91
24	    ref_only_gen1_f1: 0.71
25	    ref_only_gen2plus_f1: 0.74
26	    surface_only_macro_f1: 0.63
27	    surface_only_cv_std: 0.022
28	    surface_only_gen0_f1: 0.82
29	    surface_only_gen1_f1: 0.52
30	    surface_only_gen2plus_f1: 0.55
31	    full_macro_f1: 0.87
32	    full_cv_std: 0.012
33	    full_gen0_f1: 0.96
34	    full_gen1_f1: 0.81
35	    full_gen2plus_f1: 0.83
36	    ref_minus_surface_delta: 0.16
37	    mcnemar_p_ref_vs_surface: 3.0e-05
38	    permutation_importance_entropy_mean: 0.28
39	    permutation_importance_entropy_std: 0.19
40	    permutation_importance_hapax_ratio: 0.14
41	    permutation_importance_ttr: 0.09
42	  result_rationale: 'MVP feature importance (hapax_ratio=0.30) was inflated by XGBoost''s
43	    split-gain metric, which overweights high-cardinality continuous features with
44	    many useful split points. When surface features are ablated, the 5 reference-model
45	    features retain macro-F1=0.79 because they directly measure the generator''s deviation
46	    from the reference model''s next-token distribution — a signal that accumulates
47	    monotonically with depth as the generator''s output drifts further from human
48	    text. Entropy_mean captures the average surprise under the reference model (increases
49	    with depth as generated text occupies lower-probability regions), while entropy_std
50	    captures the increasing variance of surprise (deeper text alternates between familiar
51	    patterns and novel drift). Surface features alone (F1=0.63) capture only vocabulary
52	    impoverishment — TTR and hapax_ratio decline with depth as generators recycle
53	    high-frequency tokens — but this is a weaker, noisier proxy. The 0.16 delta and
54	    significant McNemar test confirm reference features carry independent, dominant
55	    signal. The full set achieves F1=0.87 (up from MVP''s 0.84) because retuned hyperparameters
56	    on the same data with proper ablation awareness extract slightly more complementary
57	    value. Permutation importance (which avoids split-gain bias) reranks entropy_mean
58	    as the top feature.
59	
60	    '
61	  tables:
62	  - name: 'Table 1: Feature Ablation Results (3-class depth classification)'
63	    columns:
64	    - Feature Set
65	    - Features
66	    - Macro-F1
67	    - gen-0 F1
68	    - gen-1 F1
69	    - gen-2+ F1
70	    - CV std
71	    rows:
72	    - - Reference-only
73	      - entropy_{mean,std,min,max}, tail_decay
74	      - 0.79
75	      - 0.91
76	      - 0.71
77	      - 0.74
78	      - 0.018
79	    - - Surface-only
80	      - ttr, hapax_ratio
81	      - 0.63
82	      - 0.82
83	      - 0.52
84	      - 0.55
85	      - 0.022
86	    - - Full
87	      - All 7 features
88	      - 0.87
89	      - 0.96
90	      - 0.81
91	      - 0.83
92	      - 0.012
93	    - - Δ (ref − surface)
94	      - —
95	      - '+0.16'
96	      - '+0.09'
97	      - '+0.19'
98	      - '+0.19'
99	      - —
100	  - name: 'Table 2: Permutation Importance (Full model, 5-fold mean)'
101	    columns:
102	    - Feature
103	    - Permutation Importance
104	    - XGBoost Gain (MVP)
105	    rows:
106	    - - entropy_mean
107	      - 0.28
108	      - 0.22
109	    - - entropy_std
110	      - 0.19
111	      - 0.13
112	    - - hapax_ratio
113	      - 0.14
114	      - 0.3
115	    - - tail_decay
116	      - 0.13
117	      - 0.06
118	    - - ttr
119	      - 0.09
120	      - 0.17
121	    - - entropy_max
122	      - 0.09
123	      - 0.07
124	    - - entropy_min
125	      - 0.08
126	      - 0.06
127	  figures_description:
128	  - 'Fig 1a: Grouped bar chart — Macro-F1 for ref-only / surface-only / full, with
129	    95% CI error bars from CV. Clear visual gap between ref-only and surface-only.'
130	  - 'Fig 1b: Per-class F1 heatmap (3 feature sets × 3 classes). Shows that the surface→ref
131	    gap is largest for gen-1 and gen-2+ (the harder classes), confirming reference
132	    features add discriminability precisely where surface shortcuts fail.'
133	  - 'Fig 1c: Permutation importance bar chart (full model) vs XGBoost gain bar chart
134	    (MVP). Side-by-side comparison reveals hapax_ratio''s gain was inflated; entropy_mean
135	    is the true top feature under permutation.'
136	  analysis: 'The ablation cleanly validates Claim 2. The ref-only advantage is strongest
137	    on gen-1 (Δ=+0.19) and gen-2+ (Δ=+0.19), the classes where surface features struggle
138	    most — TTR/hapax can separate human text from any synthetic text but cannot distinguish
139	    depth levels within synthetic text, because vocabulary impoverishment saturates
140	    quickly (mostly between gen-0→gen-1). Reference-model entropy features, by contrast,
141	    capture cumulative distributional drift that continues to grow between gen-1 and
142	    gen-2+. The reranking of feature importance under permutation (entropy_mean rises
143	    to 0.28, hapax_ratio drops to 0.14) directly addresses RC1 ("Is this just vocabulary
144	    impoverishment?") — it is not. The full model''s improvement to 0.87 suggests
145	    the two feature families capture partially orthogonal information: surface features
146	    provide a cheap gen-0 vs rest shortcut, while reference features provide the finer
147	    gen-1 vs gen-2+ signal.
148	
149	    '
150	- name: cross_generator_evaluation
151	  plan_id: plan_002
152	  description: 'Generate 25K chains: 1000 Wikipedia seeds × 5 generators (Pythia-2.8B,
153	    OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, Pythia-1B) × 5 depths. Feature extraction
154	    with Pythia-410M reference model. Leave-one-generator-out CV (train on 4 generators,
155	    test on held-out generator). Also report per-generator in-distribution results
156	    and per-class breakdowns.
157	
158	    '
159	  expected_results:
160	    leave_one_out_macro_f1_mean: 0.78
161	    leave_one_out_macro_f1_std: 0.03
162	    leave_one_out_gen1_f1_mean: 0.73
163	    leave_one_out_gen2plus_f1_mean: 0.75
164	    leave_one_out_gen0_f1_mean: 0.88
165	    in_distribution_5fold_macro_f1: 0.86
166	    per_generator_held_out:
167	      pythia_2_8b: 0.81
168	      olmo_2_1b: 0.77
169	      qwen3_5_2b: 0.76
170	      qwen3_5_0_8b: 0.74
171	      pythia_1b: 0.82
172	    total_chains_generated: 24200
173	    attrition_rate_pct: 3.2
174	    generation_gpu_hours: 18.5
175	  result_rationale: 'Cross-generator generalization holds (mean leave-one-out F1=0.78)
176	    because distributional drift is measured from the reference model''s perspective,
177	    not the generator''s. All generators produce text that progressively deviates
178	    from human text distribution as measured by Pythia-410M; the drift trajectory
179	    differs in magnitude but shares the same directional pattern (entropy increases,
180	    tail probability mass shifts). Pythia-family generators (2.8B, 1B) transfer best
181	    to each other (F1=0.81–0.82) due to shared pretraining distribution. Qwen3.5-0.8B
182	    is the hardest held-out case (F1=0.74) because its smaller capacity produces qualitatively
183	    different text that drifts faster at early depths — the classifier trained on
184	    larger models underestimates Qwen-0.8B''s depth. The gen-1 vs gen-2+ boundary
185	    remains the bottleneck (gen-1 F1=0.73) because gen-1 text from some generators
186	    overlaps with gen-2+ text from others in feature space. In-distribution pooled
187	    performance (0.86) is close to MVP (0.84) despite mixing generators, confirming
188	    that generator diversity adds training signal rather than noise. Attrition (~3.2%)
189	    is lower than MVP (3.7%) due to improved generation pipeline with retry logic.
190	
191	    '
192	  tables:
193	  - name: 'Table 3: Leave-One-Generator-Out Cross-Validation'
194	    columns:
195	    - Held-out Generator
196	    - Macro-F1
197	    - gen-0 F1
198	    - gen-1 F1
199	    - gen-2+ F1
200	    rows:
201	    - - Pythia-2.8B
202	      - 0.81
203	      - 0.91
204	      - 0.75
205	      - 0.77
206	    - - OLMo-2-1B
207	      - 0.77
208	      - 0.87
209	      - 0.72
210	      - 0.73
211	    - - Qwen3.5-2B
212	      - 0.76
213	      - 0.86
214	      - 0.71
215	      - 0.72
216	    - - Qwen3.5-0.8B
217	      - 0.74
218	      - 0.84
219	      - 0.68
220	      - 0.7
221	    - - Pythia-1B
222	      - 0.82
223	      - 0.92
224	      - 0.76
225	      - 0.78
226	    - - Mean ± std
227	      - 0.78 ± 0.03
228	      - 0.88 ± 0.03
229	      - 0.73 ± 0.03
230	      - 0.75 ± 0.03
231	  - name: 'Table 4: Per-Generator In-Distribution 5-Fold CV'
232	    columns:
233	    - Generator
234	    - Macro-F1
235	    - CV std
236	    rows:
237	    - - Pythia-2.8B
238	      - 0.85
239	      - 0.014
240	    - - OLMo-2-1B
241	      - 0.84
242	      - 0.016
243	    - - Qwen3.5-2B
244	      - 0.86
245	      - 0.013
246	    - - Qwen3.5-0.8B
247	      - 0.83
248	      - 0.019
249	    - - Pythia-1B
250	      - 0.84
251	      - 0.015
252	    - - Pooled (all 5)
253	      - 0.86
254	      - 0.011
255	  figures_description:
256	  - 'Fig 2a: Leave-one-out macro-F1 bar chart with error bars, generators ordered
257	    by held-out performance. Horizontal dashed line at 0.78 (mean). Shows Pythia-family
258	    clusters above mean, Qwen-0.8B below.'
259	  - 'Fig 2b: Confusion matrix heatmaps (5 panels, one per held-out generator). Highlights
260	    that gen-1↔gen-2+ confusion is the primary failure mode across all generators.'
261	  - 'Fig 2c: t-SNE of reference-model features colored by depth, faceted by generator.
262	    Shows that depth clusters are geometrically similar across generators despite
263	    generator-specific offsets in feature space.'
264	  analysis: 'The 0.78 mean leave-one-out F1 with narrow std (0.03) strongly supports
265	    Claim 1''s cross-generator generalization. The pattern is consistent: gen-0 is
266	    always well-separated (F1≥0.84), while gen-1 and gen-2+ form a harder boundary.
267	    Pythia-family transfer is strongest, suggesting some same-family distributional
268	    similarity, but even cross-family transfer (Pythia→Qwen) maintains F1≥0.74. This
269	    confirms the distributional fingerprint is a property of the generation process,
270	    not a generator-specific artifact. The pooled in-distribution result (0.86) exceeding
271	    any single-generator result suggests that multi-generator training improves robustness.
272	    For the paper, this table is the centerpiece of Claim 1 and directly addresses
273	    RC2.
274	
275	    '
276	- name: cross_family_reference_model
277	  plan_id: plan_003
278	  description: 'Re-extract features using non-Pythia reference models (OLMo-2-1B,
279	    Qwen3.5-0.8B) on the plan_002 dataset (25K chains). Compare classification performance
280	    across 3 reference model families. Tests whether the fingerprint is reference-model-agnostic.
281	
282	    '
283	  expected_results:
284	    pythia_410m_ref_macro_f1: 0.86
285	    olmo_2_1b_ref_macro_f1: 0.76
286	    qwen3_5_0_8b_ref_macro_f1: 0.74
287	    ensemble_3refs_macro_f1: 0.88
288	    cross_ref_leave_one_out_macro_f1: 0.75
289	    feature_correlation_pythia_olmo_entropy_mean: 0.82
290	    feature_correlation_pythia_qwen_entropy_mean: 0.78
291	  result_rationale: 'All three reference models detect depth signal (F1≥0.74) because
292	    any well-trained LM assigns progressively lower probability to deeper-generation
293	    text — the drift is a property of the text, not the measuring instrument. Pythia-410M
294	    performs best (0.86) because it was the reference model used during pipeline development
295	    and its capacity is calibrated for sensitivity to distributional shifts (small
296	    enough to be "surprised" by drift, large enough to model human text well). OLMo-2-1B
297	    (0.76) and Qwen3.5-0.8B (0.74) are slightly weaker because their different pretraining
298	    distributions create different baselines for "expected" text, adding noise to
299	    depth features. High cross-reference entropy_mean correlations (0.78–0.82) confirm
300	    that all three models agree on the direction of drift even if magnitudes differ.
301	    The 3-reference ensemble (0.88) exceeds any single reference, indicating that
302	    diverse reference models capture complementary aspects of distributional drift.
303	    This decisively addresses RC2 — the signal is not a Pythia-specific artifact.
304	
305	    '
306	  tables:
307	  - name: 'Table 5: Reference Model Comparison (pooled 5-generator data)'
308	    columns:
309	    - Reference Model
310	    - Family
311	    - Params
312	    - Macro-F1
313	    - gen-0 F1
314	    - gen-1 F1
315	    - gen-2+ F1
316	    rows:
317	    - - Pythia-410M
318	      - Pythia
319	      - 410M
320	      - 0.86
321	      - 0.95
322	      - 0.8
323	      - 0.82
324	    - - OLMo-2-1B
325	      - OLMo
326	      - 1B
327	      - 0.76
328	      - 0.88
329	      - 0.69
330	      - 0.72
331	    - - Qwen3.5-0.8B
332	      - Qwen
333	      - 0.8B
334	      - 0.74
335	      - 0.86
336	      - 0.66
337	      - 0.7
338	    - - Ensemble (3 refs)
339	      - Mixed
340	      - —
341	      - 0.88
342	      - 0.96
343	      - 0.83
344	      - 0.85
345	  - name: 'Table 6: Pairwise Feature Correlation (Spearman ρ) Across Reference Models'
346	    columns:
347	    - Feature
348	    - Pythia↔OLMo
349	    - Pythia↔Qwen
350	    - OLMo↔Qwen
351	    rows:
352	    - - entropy_mean
353	      - 0.82
354	      - 0.78
355	      - 0.8
356	    - - entropy_std
357	      - 0.79
358	      - 0.74
359	      - 0.76
360	    - - tail_decay
361	      - 0.71
362	      - 0.66
363	      - 0.69
364	  figures_description:
365	  - 'Fig 3a: Parallel coordinates plot showing entropy_mean distributions by depth,
366	    one panel per reference model. Monotonic increase with depth visible in all three,
367	    confirming H₂ across reference architectures.'
368	  - 'Fig 3b: Scatter matrix of entropy_mean values across reference model pairs, colored
369	    by depth. Strong positive correlation with depth-dependent clustering confirms
370	    cross-reference consistency.'
371	  analysis: 'The cross-family validation eliminates the concern that Pythia-410M has
372	    some idiosyncratic sensitivity to synthetic text. All three reference architectures
373	    detect monotonic distributional drift. The ensemble''s improvement to 0.88 provides
374	    an optional "best-effort" configuration for practitioners, though the single-reference
375	    Pythia-410M result (0.86) is sufficient for the paper''s claims. The correlation
376	    analysis (Table 6) is particularly informative: high but imperfect correlations
377	    indicate that reference models measure the same underlying phenomenon through
378	    slightly different lenses, explaining why ensembling helps. For the paper, this
379	    experiment transforms a potential weakness (Pythia-only evaluation) into a strength
380	    (reference-model-agnostic signal).
381	
382	    '
383	- name: downstream_utility
384	  plan_id: plan_004
385	  description: 'Fine-tune Pythia-410M on depth-stratified subsets of the plan_002
386	    data. Measure perplexity on held-out human test set as function of training data
387	    depth composition. Compare depth-aware filtering (keep gen-0 + gen-1, discard
388	    gen-2+) vs binary baselines (FastDetectGPT threshold, LD-Score threshold) for
389	    preserving downstream model quality.
390	
391	    '
392	  expected_results:
393	    depth_quality_spearman_rho: 0.72
394	    ppl_gen0_only: 28.3
395	    ppl_gen1_only: 30.1
396	    ppl_gen2_only: 34.7
397	    ppl_gen3_only: 38.9
398	    ppl_gen4_only: 43.2
399	    ppl_mixed_uniform: 35.8
400	    ppl_depth_filtered_gen01: 29.0
401	    ppl_binary_fastdetectgpt: 31.8
402	    ppl_binary_ldscore: 32.1
403	    ppl_human_baseline: 27.5
404	    depth_filter_vs_binary_gap_pct: 5.2
405	    training_samples_kept_depth_filter: 0.42
406	    training_samples_kept_binary: 0.28
407	  result_rationale: 'Perplexity increases monotonically with training data depth (28.3→43.2
408	    from gen-0→gen-4) because deeper-generation text has compounded distributional
409	    drift from human text — fine-tuning on it shifts the model''s learned distribution
410	    away from the human test set. The Spearman ρ=0.72 between depth and perplexity
411	    is strong but not perfect because individual samples vary in drift magnitude (some
412	    gen-3 texts are less drifted than some gen-2 texts). Depth-aware filtering (keep
413	    gen-0+gen-1, perplexity=29.0) outperforms binary baselines (~31.8–32.1) by 5.2%
414	    because binary detectors discard all synthetic text including useful gen-1 content
415	    that is distributionally close to human text. Binary filtering retains only 28%
416	    of data (mostly gen-0) while depth filtering retains 42% (gen-0 + gen-1), providing
417	    more training data of acceptable quality. The gap between gen-0-only (28.3) and
418	    depth-filtered (29.0) is small, confirming that gen-1 text is nearly as good as
419	    human text for training — the key practical insight for data curation.
420	
421	    '
422	  tables:
423	  - name: 'Table 7: Fine-tuning Perplexity by Training Data Depth'
424	    columns:
425	    - Training Data
426	    - Depth Composition
427	    - PPL (↓)
428	    - Samples Used
429	    rows:
430	    - - Human-only
431	      - gen-0
432	      - 28.3
433	      - ~4800
434	    - - gen-1 only
435	      - gen-1
436	      - 30.1
437	      - ~4750
438	    - - gen-2 only
439	      - gen-2
440	      - 34.7
441	      - ~4500
442	    - - gen-3 only
443	      - gen-3
444	      - 38.9
445	      - ~4200
446	    - - gen-4 only
447	      - gen-4
448	      - 43.2
449	      - ~3900
450	    - - Uniform mix
451	      - gen-0–4 equal
452	      - 35.8
453	      - ~22000
454	    - - Depth-filtered (ours)
455	      - gen-0 + gen-1
456	      - 29.0
457	      - ~9500
458	    - - FastDetectGPT filter
459	      - binary threshold
460	      - 31.8
461	      - ~6300
462	    - - LD-Score filter
463	      - binary threshold
464	      - 32.1
465	      - ~6100
466	    - - Human test baseline
467	      - —
468	      - 27.5
469	      - —
470	  - name: 'Table 8: Depth-Aware vs Binary Filtering Comparison'
471	    columns:
472	    - Method
473	    - PPL
474	    - Data Retained (%)
475	    - PPL Gap to Human-Only
476	    rows:
477	    - - Depth-filtered (gen-0+1)
478	      - 29.0
479	      - 42%
480	      - '+0.7'
481	    - - FastDetectGPT binary
482	      - 31.8
483	      - 28%
484	      - '+3.5'
485	    - - LD-Score binary
486	      - 32.1
487	      - 26%
488	      - '+3.8'
489	    - - No filtering (all data)
490	      - 35.8
491	      - 100%
492	      - '+7.5'
493	  figures_description:
494	  - 'Fig 4a: Line plot — perplexity vs generation depth (gen-0 through gen-4). Monotonic
495	    increase with 95% CI bands from 3 random seeds. Confirms H₂''s downstream consequence.'
496	  - 'Fig 4b: Bar chart comparing filtering strategies (depth-aware, FastDetectGPT,
497	    LD-Score, no filter) on perplexity and data retention. Dual y-axis: bars for perplexity,
498	    overlaid line for % data retained.'
499	  - 'Fig 4c: Scatter plot — predicted depth score vs actual fine-tuning perplexity
500	    contribution per sample, with Spearman ρ annotation. Shows the sample-level correlation
501	    between depth estimate and quality impact.'
502	  analysis: 'This experiment validates Claim 3 and provides the practical punchline
503	    of the paper. The monotonic perplexity curve (Fig 4a) is the most intuitive visualization
504	    of H₂ — it translates distributional drift into a metric practitioners care about.
505	    The 5.2% gap between depth-aware and binary filtering is meaningful because it
506	    comes with MORE data retained (42% vs 28%), resolving the precision-recall tradeoff
507	    that plagues binary detection. The key insight is that gen-1 text is "good enough"
508	    for training (PPL=30.1 vs human 28.3), but gen-2+ is not (PPL≥34.7). Binary detectors
509	    cannot make this distinction. For AAAI reviewers, this experiment connects the
510	    theoretical contribution (distributional drift characterization) to a practical
511	    application (data curation), which is important for venue fit.
512	
513	    '
514	- name: prompt_type_comparison
515	  plan_id: plan_005
516	  description: 'Generate chains with 3 prompt types (continuation, elaboration, inspired_rewriting)
517	    using Pythia-2.8B on 1000 Wikipedia seeds × 5 depths. Compare depth signal preservation
518	    across prompt types. Tests whether semantic divergence from source correlates
519	    with depth signal.
520	
521	    '
522	  expected_results:
523	    continuation_macro_f1: 0.85
524	    elaboration_macro_f1: 0.8
525	    inspired_rewriting_macro_f1: 0.72
526	    continuation_entropy_drift_per_depth: 0.18
527	    elaboration_entropy_drift_per_depth: 0.14
528	    inspired_rewriting_entropy_drift_per_depth: 0.1
529	    cross_prompt_train_test_macro_f1: 0.74
530	    prompt_type_drift_rate_spearman: 0.91
531	  result_rationale: 'Continuation preserves the strongest depth signal (F1=0.85) because
532	    each generation step continues directly from the previous output, maximizing the
533	    accumulation of distributional drift. Elaboration (F1=0.80) injects some new semantic
534	    direction via the prompt instruction, which partially resets the drift trajectory
535	    at each step — drift still accumulates but at a slower rate. Inspired rewriting
536	    (F1=0.72) has the most semantic freedom: the model is instructed to produce text
537	    "inspired by" the input, allowing it to diverge from the drift trajectory and
538	    partially re-anchor to its pretraining distribution. The strong correlation between
539	    per-depth entropy drift rate and classification F1 (Spearman ρ=0.91) confirms
540	    the theoretical prediction: more constrained generation → faster drift accumulation
541	    → stronger depth signal. Cross-prompt-type transfer (F1=0.74) is moderate, indicating
542	    that the drift signature is partially shared across prompt types but the rate
543	    differences create distribution shift in feature space.
544	
545	    '
546	  tables:
547	  - name: 'Table 9: Depth Classification by Prompt Type'
548	    columns:
549	    - Prompt Type
550	    - Macro-F1
551	    - gen-0 F1
552	    - gen-1 F1
553	    - gen-2+ F1
554	    - Entropy Drift Rate
555	    rows:
556	    - - Continuation
557	      - 0.85
558	      - 0.95
559	      - 0.79
560	      - 0.81
561	      - 0.18 nats/depth
562	    - - Elaboration
563	      - 0.8
564	      - 0.92
565	      - 0.73
566	      - 0.75
567	      - 0.14 nats/depth
568	    - - Inspired rewriting
569	      - 0.72
570	      - 0.86
571	      - 0.64
572	      - 0.67
573	      - 0.10 nats/depth
574	  figures_description:
575	  - 'Fig 5a: Line plots — entropy_mean vs depth for each prompt type, showing different
576	    drift rates. Continuation has steepest slope.'
577	  - 'Fig 5b: Scatter plot — prompt type drift rate vs macro-F1, confirming linear
578	    relationship. Three points with regression line and ρ annotation.'
579	  analysis: 'This experiment decomposes the depth signal by generation modality. The
580	    ordering (continuation > elaboration > inspired rewriting) aligns with the theoretical
581	    framework: the more the generation task constrains the output to build on previous
582	    text, the more drift accumulates. Inspired rewriting''s lower F1 is not a failure
583	    — it confirms the mechanism. For the paper, this comparison strengthens the theoretical
584	    story by showing that depth signal is graded, not binary, and correlates with
585	    the degree of semantic coupling between successive generation steps.
586	
587	    '
588	- name: paraphrastic_comparison
589	  plan_id: plan_006
590	  description: 'Construct parallel paraphrasing chains (same 1000 seeds, Pythia-2.8B,
591	    5 depths) alongside continuation chains. Measure whether paraphrastic chains converge
592	    (per attractor theory) while continuation chains diverge (our H₂). Direct empirical
593	    test of H₁ vs H₂.
594	
595	    '
596	  expected_results:
597	    paraphrase_macro_f1_3class: 0.58
598	    paraphrase_gen0_f1: 0.81
599	    paraphrase_gen1_f1: 0.46
600	    paraphrase_gen2plus_f1: 0.47
601	    continuation_macro_f1_3class: 0.85
602	    paraphrase_entropy_drift_depth3: 0.06
603	    continuation_entropy_drift_depth3: 0.52
604	    paraphrase_cycle_detection_pct: 68.0
605	    divergence_test_ks_statistic: 0.41
606	    divergence_test_p_value: 1.0e-05
607	  result_rationale: 'Paraphrastic chains show weak depth signal (F1=0.58) because
608	    the semantic preservation constraint of paraphrasing creates attractor dynamics
609	    — the text oscillates around a fixed semantic point, and distributional features
610	    converge after ~2 steps (confirming ACL 2025 attractor cycle theory). By depth
611	    3, paraphrastic entropy drift has nearly plateaued (0.06 nats) while continuation
612	    drift continues growing (0.52 nats). The 68% cycle detection rate in paraphrastic
613	    chains (text at depth d is more similar to depth d-2 than d-1) directly corroborates
614	    the 2-period attractor cycle prediction. Continuation chains show no such periodicity
615	    — drift is monotonic. The KS test between depth-3 entropy distributions of paraphrastic
616	    vs continuation chains (D=0.41, p<0.001) provides the statistical test of H₁ vs
617	    H₂. This is the most theoretically clean result in the paper: H₂ (divergence)
618	    holds for non-paraphrastic chains, H₁ (convergence) holds for paraphrastic chains,
619	    exactly as predicted by the semantic constraint difference.
620	
621	    '
622	  tables:
623	  - name: 'Table 10: Paraphrastic vs Continuation Chain Comparison'
624	    columns:
625	    - Chain Type
626	    - Macro-F1
627	    - Entropy Drift @depth3
628	    - Cycle Detection %
629	    rows:
630	    - - Continuation
631	      - 0.85
632	      - 0.52 nats
633	      - < 5%
634	    - - Paraphrasing
635	      - 0.58
636	      - 0.06 nats
637	      - 68%
638	    - - Δ
639	      - '+0.27'
640	      - +0.46 nats
641	      - —
642	  figures_description:
643	  - 'Fig 6a: Dual-panel line plot — entropy_mean vs depth for continuation (diverging)
644	    and paraphrasing (converging). The visual contrast is the paper''s most compelling
645	    figure.'
646	  - 'Fig 6b: Autocorrelation plot of entropy_mean sequence across depths for paraphrastic
647	    chains, showing the period-2 oscillation pattern predicted by attractor theory.'
648	  analysis: 'This is the experiment that elevates the paper from "a depth classifier"
649	    to "an empirical test of distributional dynamics in recursive generation." The
650	    clean separation between convergent (paraphrastic) and divergent (non-paraphrastic)
651	    chains validates the core theoretical insight and connects our work to the ACL
652	    2025 attractor cycle literature. H₂ is confirmed for non-paraphrastic chains:
653	    drift accumulates monotonically, enabling depth estimation. H₁ is confirmed for
654	    paraphrastic chains: convergence limits depth signal to ~2 classes. This dual
655	    result explains WHY our approach works and WHY prior work on paraphrasing chains
656	    found limited depth discriminability.
657	
658	    '
659	- name: cross_model_chains
660	  plan_id: plan_007
661	  description: 'Generate cross-model chains where each depth step uses a different
662	    generator (randomly sampled from the 5 generators). 1000 seeds × 5 depths. Compares
663	    cross-model chain depth classification to single-model chains. More realistic
664	    scenario — real web contamination involves diverse generators.
665	
666	    '
667	  expected_results:
668	    cross_model_chain_macro_f1: 0.75
669	    single_model_chain_macro_f1_mean: 0.85
670	    cross_model_gen0_f1: 0.9
671	    cross_model_gen1_f1: 0.68
672	    cross_model_gen2plus_f1: 0.67
673	    cross_model_entropy_drift_per_depth: 0.13
674	    cross_vs_single_model_delta: -0.1
675	  result_rationale: 'Cross-model chains are harder to classify (F1=0.75 vs single-model
676	    0.85) because generator switching introduces distributional discontinuities —
677	    each new generator has its own distributional signature that partially masks the
678	    monotonic drift signal. However, F1=0.75 is still well above chance (0.33) and
679	    practically useful, because the underlying drift phenomenon persists: even when
680	    generators change, the cumulative deviation from human text distribution still
681	    increases with depth. The gen-1 and gen-2+ classes are most affected (F1=0.68,
682	    0.67) because generator-switching noise is most confusing for the middle classes.
683	    Gen-0 remains well-separated (F1=0.90) because human text is fundamentally different
684	    from any generator''s output. The 10-point drop from single-model is a known cost
685	    that should be reported transparently — it bounds the method''s real-world applicability
686	    but does not invalidate the approach. Entropy drift rate (0.13 nats/depth) is
687	    lower than single-model continuation (0.18) because generator transitions partially
688	    reset drift.
689	
690	    '
691	  tables:
692	  - name: 'Table 11: Single-Model vs Cross-Model Chain Comparison'
693	    columns:
694	    - Chain Type
695	    - Macro-F1
696	    - gen-0 F1
697	    - gen-1 F1
698	    - gen-2+ F1
699	    rows:
700	    - - Single-model (mean of 5)
701	      - 0.85
702	      - 0.95
703	      - 0.79
704	      - 0.81
705	    - - Cross-model (random switch)
706	      - 0.75
707	      - 0.9
708	      - 0.68
709	      - 0.67
710	    - - Δ
711	      - '-0.10'
712	      - '-0.05'
713	      - '-0.11'
714	      - '-0.14'
715	  figures_description:
716	  - 'Fig 7: Box plot of entropy_mean by depth for cross-model chains. Wider boxes
717	    than single-model chains reflect generator-switching variance, but median still
718	    increases monotonically.'
719	  analysis: 'The 10-point F1 drop is the honest cost of ecological validity. Reviewers
720	    (RC4) will ask about this — reporting it transparently strengthens the paper.
721	    The key takeaway is that depth signal survives cross-model chains despite generator-switching
722	    noise, maintaining F1=0.75. For practical data curation, this means depth-aware
723	    filtering still provides value even when contamination sources are diverse. The
724	    fact that gen-0 F1 remains at 0.90 means the method''s primary utility (separating
725	    human from any-depth synthetic) is robust; the finer-grained depth estimation
726	    within synthetic text is where accuracy degrades.
727	
728	    '
729	- name: multi_domain_seeds
730	  plan_id: plan_008
731	  description: 'Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific
732	    (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5
733	    generators × 5 depths. Tests domain generalization of depth signal.
734	
735	    '
736	  expected_results:
737	    wikipedia_macro_f1: 0.86
738	    news_macro_f1: 0.83
739	    scientific_macro_f1: 0.81
740	    creative_macro_f1: 0.78
741	    cross_domain_leave_one_out_f1: 0.77
742	    pooled_all_domains_f1: 0.84
743	    domain_variance_of_f1: 0.0009
744	  result_rationale: 'Wikipedia performs best (0.86) because it matches the MVP setting
745	    and has the most structured, information-dense text that generators struggle to
746	    faithfully continue. News is close (0.83) due to similar factual density. Scientific
747	    text (0.81) has domain-specific vocabulary that somewhat masks depth drift in
748	    surface features, but reference-model features still capture the signal. Creative
749	    writing is hardest (0.78) because generators produce more fluent, human-like creative
750	    text — the distributional gap between human and generated creative writing is
751	    smaller than for factual domains, reducing the overall drift magnitude. Cross-domain
752	    leave-one-out (0.77) confirms that the depth signal generalizes across domains,
753	    though some domain-specific calibration is lost. The low variance (0.0009) across
754	    domains indicates that depth signal is a robust, domain-general phenomenon. Pooled
755	    performance (0.84) suggests that multi-domain training is beneficial — diverse
756	    training data helps the classifier learn domain-invariant depth features.
757	
758	    '
759	  tables:
760	  - name: 'Table 12: Multi-Domain Depth Classification'
761	    columns:
762	    - Domain
763	    - Seeds
764	    - Macro-F1
765	    - gen-0 F1
766	    - gen-1 F1
767	    - gen-2+ F1
768	    rows:
769	    - - Wikipedia
770	      - 500
771	      - 0.86
772	      - 0.95
773	      - 0.8
774	      - 0.82
775	    - - News
776	      - 500
777	      - 0.83
778	      - 0.93
779	      - 0.77
780	      - 0.79
781	    - - Scientific
782	      - 500
783	      - 0.81
784	      - 0.91
785	      - 0.74
786	      - 0.77
787	    - - Creative
788	      - 500
789	      - 0.78
790	      - 0.88
791	      - 0.71
792	      - 0.74
793	    - - Pooled (all)
794	      - 2000
795	      - 0.84
796	      - 0.93
797	      - 0.78
798	      - 0.8
799	    - - Leave-one-domain-out
800	      - —
801	      - 0.77
802	      - 0.88
803	      - 0.7
804	      - 0.73
805	  figures_description:
806	  - 'Fig 8: Faceted violin plot of entropy_mean by depth, one panel per domain. All
807	    domains show monotonic drift but with different baseline offsets and drift rates.'
808	  analysis: 'Domain generalization confirms that distributional drift is not an artifact
809	    of Wikipedia-style text. The ordering (factual > creative) is interpretable and
810	    provides nuance for practitioners: depth estimation is most reliable for factual
811	    domains where generators have clear distributional signatures. The cross-domain
812	    leave-one-out result (0.77) is strong enough to claim domain generalization in
813	    the paper. For AAAI, including 4 domains in the evaluation addresses RC6 and demonstrates
814	    ecological validity.
815	
816	    '
817	- name: finer_grained_ordinal
818	  plan_id: plan_009
819	  description: '5-class ordinal classification (gen-0 through gen-4) on the plan_002
820	    data. Tests whether non-paraphrastic chains support finer-grained depth estimation
821	    beyond the 3-class setup.
822	
823	    '
824	  expected_results:
825	    ordinal_5class_macro_f1: 0.62
826	    ordinal_5class_gen0_f1: 0.92
827	    ordinal_5class_gen1_f1: 0.68
828	    ordinal_5class_gen2_f1: 0.52
829	    ordinal_5class_gen3_f1: 0.48
830	    ordinal_5class_gen4_f1: 0.51
831	    ordinal_mae: 0.58
832	    ordinal_spearman_rho: 0.83
833	    adjacent_class_confusion_pct: 72.0
834	  result_rationale: '5-class F1 (0.62) is lower than 3-class (0.86) because deeper
835	    classes (gen-2/gen-3/gen-4) have progressively overlapping feature distributions
836	    — drift accumulates but with diminishing marginal signal per step. Gen-0 remains
837	    easy (F1=0.92), gen-1 is moderate (F1=0.68), and gen-2/3/4 are difficult (F1≈0.48–0.52)
838	    because the distributional differences between adjacent deep classes are small.
839	    However, the high Spearman ρ (0.83) and low MAE (0.58) indicate that the classifier''s
840	    errors are ordinal — when it misclassifies, it predicts an adjacent class (72%
841	    of errors are off-by-one), not a distant one. This supports ordinal regression
842	    as a natural formulation and suggests that while exact depth prediction is noisy
843	    for deep classes, the relative ordering is preserved. For the paper, this result
844	    supports the claim that drift is monotonic (H₂) while honestly reporting the practical
845	    ceiling on depth resolution.
846	
847	    '
848	  tables:
849	  - name: 'Table 13: 5-Class Ordinal Depth Classification'
850	    columns:
851	    - Class
852	    - Precision
853	    - Recall
854	    - F1
855	    rows:
856	    - - gen-0
857	      - 0.93
858	      - 0.91
859	      - 0.92
860	    - - gen-1
861	      - 0.66
862	      - 0.7
863	      - 0.68
864	    - - gen-2
865	      - 0.5
866	      - 0.54
867	      - 0.52
868	    - - gen-3
869	      - 0.47
870	      - 0.49
871	      - 0.48
872	    - - gen-4
873	      - 0.53
874	      - 0.5
875	      - 0.51
876	    - - Macro
877	      - —
878	      - —
879	      - 0.62
880	  - name: 'Table 13b: Ordinal Error Analysis'
881	    columns:
882	    - Metric
883	    - Value
884	    rows:
885	    - - MAE
886	      - 0.58
887	    - - Spearman ρ (pred vs true depth)
888	      - 0.83
889	    - - Adjacent-class confusion (%)
890	      - 72%
891	  figures_description:
892	  - 'Fig 9a: 5×5 confusion matrix heatmap. Diagonal + adjacent-diagonal cells are
893	    dark, confirming ordinal error structure.'
894	  - 'Fig 9b: Predicted depth (box plot) vs true depth. Boxes overlap for gen-2/3/4
895	    but medians increase monotonically.'
896	  analysis: 'The 5-class result characterizes the resolution ceiling of distributional
897	    fingerprints. While exact depth-4 vs depth-3 discrimination is weak, the ordinal
898	    structure is strong (ρ=0.83). This has practical implications: for data curation,
899	    coarse depth buckets (gen-0 / gen-1 / gen-2+) are more useful than exact depth
900	    anyway — the key decision boundary is "how much drift is tolerable." The result
901	    also differentiates our work from attractor theory: paraphrastic chains converge
902	    to ~2 distinguishable classes, while our non-paraphrastic chains support at least
903	    3 clean classes and 5 ordinal classes. This directly addresses RC3.
904	
905	    '
906	- name: human_edit_robustness
907	  plan_id: plan_010
908	  description: 'Robustness test on plan_002 data with simulated edits: (A) random
909	    word replacement at 5%, 10%, 20% rates, (B) LLM-simulated light editing (rephrase
910	    random sentences). Tests depth signal persistence under post-generation editing.
911	
912	    '
913	  expected_results:
914	    no_edit_macro_f1: 0.86
915	    random_5pct_macro_f1: 0.83
916	    random_10pct_macro_f1: 0.78
917	    random_20pct_macro_f1: 0.67
918	    llm_light_edit_macro_f1: 0.76
919	    degradation_slope_per_10pct: -0.095
920	  result_rationale: 'Random word replacement at 5% has minimal impact (F1=0.83, Δ=-0.03)
921	    because replacing 5% of tokens introduces noise uniformly across all depth classes,
922	    preserving the relative distributional differences. At 10% (F1=0.78), the noise
923	    begins to mask depth-specific features — entropy statistics become noisier as
924	    random words inject unpredictable surprise values. At 20% (F1=0.67), substantial
925	    text corruption disrupts the distributional fingerprint significantly but performance
926	    remains above chance (0.33). LLM-simulated editing (F1=0.76) is comparable to
927	    10% random replacement because light rephrasing changes surface statistics but
928	    largely preserves the underlying distributional structure — the edited text still
929	    occupies the same region of reference-model feature space. The degradation is
930	    approximately linear (-0.095 F1 per 10% edit rate), providing a simple model for
931	    practitioners to assess signal reliability given estimated editing rates. These
932	    results address RC5 while honestly reporting the method''s sensitivity to post-generation
933	    modification.
934	
935	    '
936	  tables:
937	  - name: 'Table 14: Robustness to Simulated Edits'
938	    columns:
939	    - Edit Type
940	    - Edit Rate
941	    - Macro-F1
942	    - Δ from No-Edit
943	    rows:
944	    - - None (baseline)
945	      - 0%
946	      - 0.86
947	      - —
948	    - - Random word replacement
949	      - 5%
950	      - 0.83
951	      - '-0.03'
952	    - - Random word replacement
953	      - 10%
954	      - 0.78
955	      - '-0.08'
956	    - - Random word replacement
957	      - 20%
958	      - 0.67
959	      - '-0.19'
960	    - - LLM light editing
961	      - ~8–12%
962	      - 0.76
963	      - '-0.10'
964	  figures_description:
965	  - 'Fig 10: Line plot — macro-F1 vs edit rate. Linear degradation with 95% CI band.
966	    Horizontal dashed line at chance level (0.33). Annotation at 10% edit rate: ''typical
967	    human editing range.'''
968	  analysis: 'The robustness profile is realistic for practical deployment. Light editing
969	    (5–10%) typical of human post-processing preserves most of the depth signal. Heavy
970	    editing (20%) degrades performance significantly but remains above chance, suggesting
971	    that even heavily edited text retains some distributional fingerprint. For the
972	    paper, this experiment provides the necessary caveat about real-world applicability
973	    while showing that the method is viable for the most common use case (lightly
974	    edited or unedited synthetic text in web-scraped data).
975	
976	    '
977	- name: ld_score_feature
978	  plan_id: plan_011
979	  description: 'Add LD-Score (character-distribution signature from arXiv:2605.01647)
980	    as an additional feature to the plan_001 ablation framework. Tests whether character-level
981	    features provide complementary depth signal beyond token-level distributional
982	    features.
983	
984	    '
985	  expected_results:
986	    full_plus_ld_macro_f1: 0.88
987	    ld_score_only_macro_f1: 0.59
988	    ld_score_permutation_importance: 0.06
989	    full_plus_ld_vs_full_delta: 0.01
990	  result_rationale: 'LD-Score alone achieves modest depth discrimination (F1=0.59)
991	    because character-level distributional signatures capture some depth-dependent
992	    patterns — deeper generation text has slightly more uniform character distributions
993	    as vocabulary impoverishment affects character-level statistics. However, adding
994	    LD-Score to the full feature set provides only marginal improvement (Δ=+0.01)
995	    because LD-Score''s signal is largely redundant with existing surface features
996	    (TTR, hapax_ratio) — both measure vocabulary impoverishment, just at different
997	    granularities (character vs word level). The low permutation importance (0.06)
998	    confirms that LD-Score is not providing new information. This is a useful negative-ish
999	    result: it shows that character-level features do not add a fundamentally new
1000	    signal modality, reinforcing that the key complementary feature families are surface
1001	    vocabulary statistics and reference-model distributional features.
1002	
1003	    '
1004	  tables:
1005	  - name: 'Table 15: LD-Score Feature Integration'
1006	    columns:
1007	    - Feature Set
1008	    - Macro-F1
1009	    - Δ from Full
1010	    rows:
1011	    - - Full (7 features)
1012	      - 0.87
1013	      - —
1014	    - - Full + LD-Score (8 features)
1015	      - 0.88
1016	      - '+0.01'
1017	    - - LD-Score only
1018	      - 0.59
1019	      - '-0.28'
1020	  figures_description:
1021	  - 'Fig S1 (supplementary): Feature importance bar chart with LD-Score included.
1022	    LD-Score ranks below all reference-model features.'
1023	  analysis: 'A clean but unexciting result that belongs in the supplementary material.
1024	    It confirms the two-modality structure of depth signal (reference-model entropy
1025	    + surface vocabulary) and shows that adding more surface-level features (even
1026	    at a different granularity) does not expand the signal envelope. For the paper,
1027	    this addresses potential questions about "what about other feature types" and
1028	    justifies the focus on reference-model features as the novel contribution.
1029	
1030	    '
1031	- name: end_to_end_classifier
1032	  plan_id: plan_012
1033	  description: 'QLoRA fine-tune Qwen3.5-0.8B for end-to-end depth classification (directly
1034	    from text, no handcrafted features). Compares learned representations vs handcrafted
1035	    distributional features on the plan_002 dataset.
1036	
1037	    '
1038	  expected_results:
1039	    qwen_qlora_macro_f1: 0.83
1040	    qwen_qlora_gen0_f1: 0.94
1041	    qwen_qlora_gen1_f1: 0.77
1042	    qwen_qlora_gen2plus_f1: 0.79
1043	    handcrafted_features_macro_f1: 0.86
1044	    qwen_qlora_cross_gen_leave_one_out_f1: 0.71
1045	    handcrafted_cross_gen_leave_one_out_f1: 0.78
1046	    qwen_qlora_training_gpu_hours: 12.0
1047	    handcrafted_training_time_minutes: 3.0
1048	  result_rationale: 'The QLoRA fine-tuned model achieves competitive in-distribution
1049	    performance (F1=0.83 vs handcrafted 0.86) because the transformer can implicitly
1050	    learn distributional features from raw text. However, it underperforms the handcrafted
1051	    approach for two reasons: (1) the handcrafted features distill the reference model''s
1052	    perspective into compact statistics that directly measure what matters (distributional
1053	    drift from human text), while the fine-tuned model must learn this implicitly
1054	    from text patterns; (2) the XGBoost classifier on 7 features is harder to overfit
1055	    than a 0.8B parameter model on ~25K training examples. The larger gap in cross-generator
1056	    leave-one-out (0.71 vs 0.78) reveals that the fine-tuned model memorizes generator-specific
1057	    artifacts more than the handcrafted features, which are designed to be generator-invariant.
1058	    The 4000× training time difference (12 GPU-hours vs 3 minutes) makes the handcrafted
1059	    approach clearly preferable for practical deployment. This result validates the
1060	    feature engineering approach over brute-force fine-tuning and justifies the paper''s
1061	    focus on interpretable distributional features.
1062	
1063	    '
1064	  tables:
1065	  - name: 'Table 16: End-to-End vs Feature-Based Comparison'
1066	    columns:
1067	    - Method
1068	    - In-Dist F1
1069	    - Cross-Gen F1
1070	    - Training Cost
1071	    rows:
1072	    - - XGBoost + handcrafted features
1073	      - 0.86
1074	      - 0.78
1075	      - 3 min
1076	    - - QLoRA Qwen3.5-0.8B
1077	      - 0.83
1078	      - 0.71
1079	      - 12 GPU·h
1080	    - - Δ (handcrafted − QLoRA)
1081	      - '+0.03'
1082	      - '+0.07'
1083	      - —
1084	  figures_description:
1085	  - 'Fig S2 (supplementary): Paired bar chart — in-distribution vs cross-generator
1086	    F1 for both methods. Handcrafted features show smaller generalization gap.'
1087	  analysis: 'This is a strategically important result. Reviewers might ask "why not
1088	    just fine-tune a model?" — this experiment shows that handcrafted features outperform,
1089	    generalize better, are 4000× cheaper to train, and are interpretable (you can
1090	    point to specific features and explain why they work). The fine-tuned model''s
1091	    worse cross-generator generalization is the most telling result: it confirms that
1092	    the handcrafted features capture the right abstraction (distributional drift as
1093	    measured by a reference model) while the fine-tuned model takes shortcuts via
1094	    generator-specific patterns. This result belongs in the supplementary material
1095	    and reinforces the paper''s methodological choice.'
1096	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bc6d653-4346-4f08-a54d-3b8e997821d2",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "1ca4300a-3fc2-4786-9baf-d36624045658",
  "sourceToolAssistantUUID": "7bc6d653-4346-4f08-a54d-3b8e997821d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-14T18:44:18.142Z_

Now I have a comprehensive understanding of the paper across all three scenario versions (best/median/worst). Let me now submit my review. I'll load the submission tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ca4300a-3fc2-4786-9baf-d36624045658",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xNDy6TKVgassEg5ipi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96831a6c-0820-4612-a48a-18ac85667319",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Taj8YJxK4FUt1TypMwWra1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32792,
      "cache_read_input_tokens": 60853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32792,
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

_source line 42 · 2026-05-14T18:44:18.740Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MR8Qwq4qLomutxRQhSV9Mr`</summary>

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
  "parentUuid": "96831a6c-0820-4612-a48a-18ac85667319",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xNDy6TKVgassEg5ipi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "927dd0a9-a82e-439b-925a-4fac60eb566b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Taj8YJxK4FUt1TypMwWra1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32792,
      "cache_read_input_tokens": 60853,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 32792
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 60853,
          "cache_creation_input_tokens": 32792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 32792,
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

_source line 43 · 2026-05-14T18:44:18.743Z_

<details><summary>↩ Tool result · `toolu_01MR8Qwq4qLomutxRQhSV9Mr`</summary>

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
  "parentUuid": "927dd0a9-a82e-439b-925a-4fac60eb566b",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "145f22fa-1c39-4620-8eda-a93b2591a0e2",
  "sourceToolAssistantUUID": "927dd0a9-a82e-439b-925a-4fac60eb566b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-14T18:44:22.792Z_



Now I have thoroughly read all three paper versions (best/median/worst), the project framing, experimental plans, and imagined results. Let me compose and submit my R2 review focusing on Novelty and Related Work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "145f22fa-1c39-4620-8eda-a93b2591a0e2",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xNciZdEy7KSzCG8zcC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fbf2a7e-e1f6-4648-8be0-96f8d904718c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SmrxK4nRke55FE83cv7wwU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 93645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 805,
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

_source line 45 · 2026-05-14T18:45:56.249Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01NFRGaxhbaEbQRXhqo2cdvs`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "tier": "best",
  "dream_id": "dream_20260514T181213",
  "overall_score": "5 - Borderline / Weak Reject",
  "report": "# Reviewer 2 (R2): Novelty and Related Work\n\n## Paper Summary (2-3 sentences)\n\nThis paper introduces \"distributional fingerprinting\" for estimating the generation depth of text (gen-0/gen-1/gen-2+) by computing token-level entropy statistics under a small reference language model. The method uses a 7-feature XGBoost classifier (5 reference-model entropy features + 2 surface vocabulary features) and tests two hypotheses about non-paraphrastic generation chains, confirming monotonic divergence (H2). The approach achieves macro-F1=0.87 (3-class) with cross-generator generalization (leave-one-out F1=0.78), and demonstrates downstream utility via depth-aware data filtering.\n\n## Strengths\n\n- **Novel problem formulation.** Framing generation depth estimation as a graded, ordinal classification task (rather than binary real/synthetic detection) is a genuinely useful reframing with clear practical motivation for data curation pipelines. The paper correctly identifies a real gap: binary detectors force a lossy all-or-nothing decision. This problem formulation alone has value for the community.\n\n- **Clean theoretical framing via H1/H2 dichotomy.** The contrast between convergent paraphrastic chains (H1, connecting to Briesch et al. 2025 attractor cycle theory) and divergent non-paraphrastic chains (H2) provides a satisfying conceptual structure. The direct empirical comparison (Table 5 / Section 4.4) with KS statistics is well-executed and produces a clear result. The insight that the presence or absence of a semantic-preservation constraint determines the dynamics regime is theoretically interesting.\n\n- **Comprehensive experimental coverage.** The paper tests across 5 generators, 4 domains, 3 prompt types, cross-model chains, cross-reference models, robustness to editing, and finer-grained ordinal classification. This breadth is commendable and addresses many obvious reviewer concerns preemptively.\n\n- **Honest reporting of limitations.** The cross-model chain degradation (-10 F1), the editing robustness degradation curve, and the 5-class resolution ceiling are transparently reported. This increases credibility.\n\n- **Practical interpretability.** The 7-feature XGBoost approach is lightweight (3 minutes training), interpretable, and outperforms the QLoRA neural baseline on cross-generator transfer. This is a practical strength for real-world deployment.\n\n## Weaknesses\n\n### W1: The \"distributional fingerprint\" is largely perplexity-based OOD detection repackaged (Major)\n\nThe 5 reference-model features (mean, std, min, max of token-level NLL + tail decay) are essentially summary statistics of the text's perplexity profile under a reference model. This is functionally equivalent to well-established out-of-distribution detection via likelihood-based statistics. The paper does not cite or differentiate from:\n\n- **DetectGPT (Mitchell et al. 2023)**: Uses perturbation-based log-probability curvature under a reference model -- the same conceptual apparatus of \"measuring distributional displacement from a reference model's expectations.\" The \"best\" paper cites FastDetectGPT but never discusses DetectGPT itself or explains how the entropy features differ from log-probability curvature.\n- **DNA-GPT (Yang et al. 2023)**: Uses divergent N-gram analysis for machine text detection, directly relevant to measuring distributional divergence.\n- **Perplexity-based detection** more broadly (Solaiman et al. 2019; Gehrmann et al. 2019 GLTR): These foundational works established that perplexity under a reference model distinguishes human from machine text. The entropy features in this paper are direct descendants of this idea, extended to the ordinal depth setting. The paper should acknowledge this lineage and articulate what is genuinely new beyond applying known perplexity-based features to a new (depth) classification target.\n\nThe novelty of the features themselves is limited. What is new is the *application* to depth estimation rather than binary detection. The paper should be more forthright about this distinction.\n\n### W2: Critically thin related work -- only 5 references (Major)\n\nFor a venue like AAAI, a related work section with only 5 references is unacceptable. Entire subfields that are directly relevant are omitted:\n\n**Missing: Data contamination and benchmark contamination.**\n- Sainz et al. (2023), \"NLP Evaluation in Trouble\": benchmark contamination from LLM outputs\n- Oren et al. (2024), \"Proving Test Set Contamination in Black Box Language Models\"\n- Golchin & Surdeanu (2024), \"Time Travel in LLMs: Tracing Data Contamination in Large Language Models\"\n- The entire line on data decontamination in LLM training pipelines\n\n**Missing: Membership inference and training data attribution.**\n- Shi et al. (2024), \"Detecting Pretraining Data from Large Language Models\" (Min-K% Prob)\n- Carlini et al. (2021/2023) on extracting training data and memorization\n- These methods are conceptually adjacent: they also use likelihood-based statistics under a reference model to infer provenance\n\n**Missing: Watermarking beyond SynthID.**\n- Kirchenbauer et al. (2023), \"A Watermark for Large Language Models\" -- the foundational LLM watermarking paper\n- Christ et al. (2024), Zhao et al. (2024) -- undetectable watermarks\n- Watermarking is a competing paradigm for tracking generation provenance. Omitting it entirely is a gap.\n\n**Missing: Model collapse theory beyond Shumailov et al.**\n- Dohmatob et al. (2024), \"A Tale of Tails\" -- theoretical analysis of model collapse as tail distribution loss. Directly relevant to tail_decay feature.\n- Alemohammad et al. (2024), \"Self-Consuming Generative Models Go MAD\" -- recursive generation dynamics\n- Gerstgrasser et al. (2024) -- model collapse with data mixing\n\n**Missing: Perplexity-based and likelihood-based detection.**\n- Mitchell et al. (2023), DetectGPT\n- Solaiman et al. (2019), \"Release Strategies and Social Impacts of Language Models\" -- original GPT-2 output detection via likelihood\n- Gehrmann et al. (2019), GLTR -- statistical detection using token-level likelihood\n- Su et al. (2023), \"DetectLLM\"\n- Bao et al. (2024) is cited but the broader perplexity-detection lineage is not\n\n**Missing: Data quality scoring and data selection.**\n- Xie et al. (2023), \"Data Selection with DSIR\" -- distributional shift for data curation\n- Wettig et al. (2024), \"QuRating\" -- quality-based data selection\n- The downstream utility claim (Claim 3) directly competes with this literature. Depth-aware filtering should be compared against quality scoring methods, not just binary detectors.\n\n**Missing: Distributional shift and OOD detection.**\n- The entropy features are functionally OOD detection features. The connection to OOD detection (Hendrycks & Gimpel 2017; Liang et al. 2018 ODIN; Liu et al. 2020 energy-based) should be discussed. The paper's core technical contribution -- measuring distributional displacement from a reference model -- is standard in this literature.\n\n### W3: Novelty of the method is incremental (Moderate)\n\nThe technical method consists of: (1) compute NLL statistics under a reference LM, (2) add TTR and hapax ratio, (3) train XGBoost. Each component is well-established. The reference-model features are textbook perplexity statistics. The surface features (TTR, hapax) are standard lexical diversity measures used since the 1940s. XGBoost is off-the-shelf. The novelty lies in the problem formulation (depth estimation) and the empirical finding (H2 for non-paraphrastic chains), not in any methodological innovation. This is not necessarily fatal, but the paper oversells the method as a \"distributional fingerprinting\" technique when it is more accurately described as \"perplexity profiling applied to depth estimation.\"\n\n### W4: Ablation results are internally inconsistent across paper versions (Moderate)\n\nComparing the \"best\" paper's ablation (ref-only=0.79 >> surface-only=0.63) against the actual MVP results in memory.md (hapax_ratio importance=0.30, top feature; macro-F1=0.84), there is a large discrepancy. The MVP actually showed surface features dominating (hapax_ratio=0.30 importance), and the paper_framing.md acknowledges the framing had to pivot from \"independence\" to \"complementarity\" after the ablation showed surface features were strong. The \"best\" paper presents an optimistic scenario where reference features dominate, but the actual MVP data showed the opposite pattern. The paper's narrative that reference-model entropy features are the \"novel signal source\" carrying \"independent signal beyond surface vocabulary impoverishment\" needs to survive the actual ablation; the MVP data suggests surface features may be stronger than the best-case paper implies.\n\n### W5: The downstream utility comparison is not apples-to-apples (Minor)\n\nThe depth-aware filter keeps gen-0+gen-1 (42% data), while the binary baselines retain 28% data. The comparison conflates two effects: (a) depth-awareness and (b) more training data. A fairer comparison would match data retention rates. At matched 42% retention, how does a binary detector's top-42%-confidence subset compare? Without this control, the 5.2% improvement claim is confounded by data quantity.\n\n### W6: All generators are small (<3B parameters) (Minor)\n\nThe paper acknowledges this in limitations but the absence of any frontier-scale model (7B+, let alone 70B+) is a significant gap for practical claims about data curation. Larger models produce text that is much closer to human text distributions; the depth signal may vanish or change qualitatively. The claim \"distributional fingerprints enable risk-stratified data curation\" is overstated without evidence at the scales where data curation actually matters.\n\n## Questions for Authors\n\n- How do you distinguish your reference-model entropy features from standard perplexity-based detection features (DetectGPT, GLTR)? Is the novelty purely in applying these features to depth estimation rather than binary detection?\n\n- Have you tested whether simply using raw perplexity (mean NLL) as a single feature achieves comparable depth classification? Given that entropy_mean is your top feature by permutation importance, what is the marginal value of the other 4 reference-model features beyond mean perplexity?\n\n- The comparison against binary baselines (FastDetectGPT, LD-Score) in the downstream utility experiment uses the baselines' default thresholds. Were these thresholds optimized for the data curation task, or are they generic detection thresholds? An unfair baseline comparison would undermine Claim 3.\n\n- What happens with instruction-tuned or RLHF-aligned generators? These are the models most commonly deployed in practice and may have very different distributional properties than base models like Pythia.\n\n- The 68% cycle detection rate in paraphrastic chains is interesting. Does this metric exist for continuation chains? If continuation chains show 0% cycle detection at all depths, that would strongly support H2; if there is some periodicity at deeper depths, H2 may be more nuanced than presented.\n\n- Can you provide a theoretical argument (not just empirical observation) for why non-paraphrastic chains should diverge monotonically? The paper gestures at \"unbounded semantic state space\" but does not formalize this.\n\n## Missing Related Work\n\nThe paper cites only 5 references. A minimally adequate related work section for AAAI should cite approximately 25-40 references. The following areas need coverage:\n\n1. **Perplexity-based detection lineage**: DetectGPT, GLTR, Solaiman et al. 2019, Su et al. 2023 DetectLLM\n2. **Data contamination detection**: Sainz et al. 2023, Oren et al. 2024, Golchin & Surdeanu 2024\n3. **Membership inference / training data attribution**: Shi et al. 2024 Min-K%, Carlini et al. 2021/2023\n4. **LLM watermarking**: Kirchenbauer et al. 2023, Christ et al. 2024, Zhao et al. 2024\n5. **Model collapse theory**: Dohmatob et al. 2024, Alemohammad et al. 2024, Gerstgrasser et al. 2024\n6. **Data quality/selection for LLM training**: Xie et al. 2023 DSIR, Wettig et al. 2024 QuRating, Penedo et al. 2024 FineWeb\n7. **OOD detection** (the technical parent of the reference-model features): Hendrycks & Gimpel 2017, energy-based OOD\n8. **Iterative self-improvement / self-consuming models**: Huang et al. 2023, Alemohammad et al. 2024\n\n## Scores\n\n- **Novelty: 5/10** -- The problem formulation (depth estimation) is new and well-motivated. The H1/H2 framing adds theoretical structure. However, the method itself (perplexity statistics + lexical diversity + XGBoost) is not novel. The \"distributional fingerprinting\" framing overclaims the methodological contribution.\n\n- **Related Work: 3/10** -- Five references is critically inadequate for AAAI. Multiple directly relevant subfields (perplexity-based detection, data contamination, membership inference, watermarking, OOD detection, data quality scoring, model collapse theory beyond one paper) are entirely absent. The paper fails to position itself within the broader landscape.\n\n- **Significance: 6/10** -- The problem matters. Depth estimation is a useful framing for data governance. The H2 confirmation for non-paraphrastic chains is a genuine empirical contribution. The practical utility (depth-aware filtering) is modest but real. However, the limited model scale and the downstream comparison confounds temper significance.\n\n- **Clarity: 7/10** -- Well-structured with comprehensive experiments. The H1/H2 framing is clear. Tables are informative. The writing is direct. However, the paper would benefit from acknowledging its methodological simplicity rather than dressing it up as \"distributional fingerprinting.\"\n\n- **Overall (Novelty+Related Work focus): 5/10** -- The problem formulation and empirical findings are valuable, but the paper is not ready for AAAI in its current form. The related work is unacceptably thin. The methodological novelty is incremental. The framing overclaims relative to what is actually new (applying known perplexity features to a new classification target). With a substantially expanded related work section, honest positioning of methodological novelty, and results at larger model scales, this could become a solid paper.\n\n- **Confidence: 4/5** -- I am familiar with the synthetic text detection, OOD detection, and model collapse literatures. I am confident in my assessment of the missing related work and the novelty calibration. I have some uncertainty about whether the best-case experimental results would hold in practice, given the discrepancy between the MVP data and the paper's optimistic ablation narrative.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fbf2a7e-e1f6-4648-8be0-96f8d904718c",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xNciZdEy7KSzCG8zcC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30a7b652-5317-4a8b-aa1b-27ca55e72ec9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SmrxK4nRke55FE83cv7wwU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 93645,
      "output_tokens": 3901,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 805
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3901,
          "cache_read_input_tokens": 93645,
          "cache_creation_input_tokens": 805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 805,
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

_source line 46 · 2026-05-14T18:45:57.051Z_

<details><summary>↩ Tool result · `toolu_01NFRGaxhbaEbQRXhqo2cdvs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/review_report.md\", \"dream_id\": \"dream_20260514T181213\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30a7b652-5317-4a8b-aa1b-27ca55e72ec9",
  "isSidechain": true,
  "promptId": "c0df1650-b51d-4322-970b-209c8e60f1c6",
  "agentId": "a2d15da6165e8b28b",
  "type": "user",
  "uuid": "e9b93603-648c-49f9-b1ce-99abe2feb7ca",
  "sourceToolAssistantUUID": "30a7b652-5317-4a8b-aa1b-27ca55e72ec9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-14T18:46:07.091Z_

Review submitted successfully. Here is a summary of the key findings:

**Overall Score: 5/10 (Borderline / Weak Reject)**

**Core assessment:** The paper introduces a genuinely useful problem formulation (generation depth estimation beyond binary detection) and provides a clean empirical framework (H1/H2 dichotomy, comprehensive cross-generator/domain/prompt evaluation). However, it has two critical weaknesses from the Novelty + Related Work perspective:

1. **Critically thin related work (3/10):** Only 5 references for an AAAI submission. Entire directly relevant subfields are missing: perplexity-based detection lineage (DetectGPT, GLTR), data contamination detection, membership inference, LLM watermarking beyond SynthID, model collapse theory beyond Shumailov, OOD detection, and data quality scoring.

2. **Incremental methodological novelty (5/10):** The "distributional fingerprinting" framing overclaims. The 5 reference-model features are standard perplexity/NLL summary statistics -- functionally equivalent to established OOD detection features. The surface features (TTR, hapax) date to the 1940s. XGBoost is off-the-shelf. The genuine novelty is in the *application* to depth estimation and the H2 empirical finding, not in the method itself.

**Additional concerns:** The downstream utility comparison conflates depth-awareness with data quantity effects. All generators tested are under 3B parameters, limiting practical significance claims. The MVP data in `memory.md` shows surface features dominating (hapax_ratio importance=0.30), which tensions with the best-case paper's narrative that reference features carry the primary signal.

The review report was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9b93603-648c-49f9-b1ce-99abe2feb7ca",
  "isSidechain": true,
  "agentId": "a2d15da6165e8b28b",
  "requestId": "req_011Cb2xVrr55yyad3QF8kYvc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1dacc61-1f99-4c5e-ad1f-79073d1d38c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "176da81f-308c-4dd6-ae97-a751123aff6c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PoCLi6BAR7hDBvSydJrSNR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4031,
      "cache_read_input_tokens": 94450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4031,
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
