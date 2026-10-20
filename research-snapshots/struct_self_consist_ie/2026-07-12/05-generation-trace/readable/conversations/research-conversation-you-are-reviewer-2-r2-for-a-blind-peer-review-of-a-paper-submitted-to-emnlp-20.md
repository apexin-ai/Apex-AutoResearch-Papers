# Research conversation: You are Reviewer 2 (R2) for a blind peer review of a paper submitted to EMNLP 2026 Findings. Your focus area is **Novelt

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 62
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-af468f80c09f420ae.jsonl`
- **Structured JSON:** [`9f5cef012c321ca2c286.json`](../../sessions/9f/9f5cef012c321ca2c286.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

62 recorded events

### User

_source line 1 · 2026-05-15T10:24:34.457Z_

You are Reviewer 2 (R2) for a blind peer review of a paper submitted to EMNLP 2026 Findings. Your focus area is **Novelty and Related Work**.

## Scoring Rubric (ARR Review Form)

**Soundness** (1-5, half-increments):
- 5: One of the most thorough studies I've seen
- 4: Sufficient support for all claims
- 3: Sufficient support for main claims
- 2: Some main claims not sufficiently supported
- 1: Not yet sufficiently thorough

**Excitement** (1-5, half-increments):
- 5: Would recommend to others / attend presentation
- 4: Would mention to others
- 3: Might mention some points
- 2: Doesn't resonate
- 1: Not exciting

**Overall Assessment** (1-5, half-increments):
- 5: Award (top 2.5%)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

## Paper Summary

Title: "Why Confidence Signals Predict but Cannot Select in Structured Information Extraction"

The paper studies test-time scaling (multi-sample generation + selection) for structured IE (NER, RE). It evaluates 5 confidence signals (log-prob, set Jaccard, Fleiss' kappa, exact match, entity voting) for quality estimation (QE) and best-of-N selection on fine-tuned 8B models (Qwen3-8B, LLaMA-3.1-8B) with constrained decoding (Outlines) on SciERC and CoNLL-2003.

**Key claims:**
1. **Correlation–selection gap**: Signals that reliably estimate quality (AUROC 0.749) fail as selectors (best Δ = +0.6pp, p=0.39).
2. **Constrained decoding is not the bottleneck**: Free-form ablation increases log-prob variance but doesn't help selection.
3. **Fundamental structural explanation**: IE's combinatorial output space (set of entities/relations) means scalar signals can't rank set-valued outputs—unlike discrete answer spaces (QA) or string-valued outputs (MT).
4. **QE has practical value** for selective prediction even though selection fails.
5. **Cross-model consistency** validated across Qwen3-8B and LLaMA-3.1-8B.

**Contributions claimed:**
1. Systematic evaluation framework for 5 confidence signals across 4 families for structured IE QE.
2. Identification of correlation–selection gap.
3. Controlled free-form ablation ruling out constrained decoding bottleneck.
4. Supervised verifier + OOD analysis confirming fundamental nature.

**Related work sections covered:**
- Test-Time Scaling and Self-Consistency (Wang et al. 2023, CISC 2025, Self-Certainty 2026, ReASC 2026, Atomic SC 2024)
- Uncertainty Quantification for LLMs (Kadavath 2022, Kuhn 2023, semantic entropy, SelfCheckGPT)
- MBR Decoding and Sample Selection (Eikema & Aziz 2020, CoCoA/Vashurin 2025a, Vashurin 2025b)
- Calibration and Selective Prediction (Guo 2017, conformal prediction)
- Consistency for Structured IE (Nédellec & Xia 2026—most directly related, studies consistency-accuracy correlation but only surface-level matching, no best-of-N selection)
- Verifier and Reward Models (Cobbe 2021, Lightman 2023)

**Key reference**: Nédellec & Xia (2026) — study consistency–accuracy correlation for IE with hard-prompted LLMs, but (a) use surface-level string matching, (b) don't study best-of-N selection.

## Your Task

Write a detailed review focusing on **Novelty and Related Work**. Evaluate:

1. **Novelty**: Is the correlation–selection gap a genuinely new finding? Is the structural explanation novel? How incremental vs. surprising are the contributions?
2. **Related work coverage**: Are key related works cited? Any missing important references? Is positioning accurate?
3. **Differentiation from prior work**: Is the distinction from Nédellec & Xia (2026) convincing? From self-consistency literature? From MBR decoding literature?
4. **Contribution significance**: Does this paper advance the field meaningfully? Is a negative result paper valuable here?
5. **Narrative coherence**: Does the paper's story hold together? The paper pivoted from "constrained decoding bottleneck" to "fundamental structural hardness"—is this convincing?
6. **Reference quality**: Several citations use placeholder names ("CISC authors, 2025", "Self-Certainty authors, 2026", "ReASC authors, 2026", "Atomic SC authors, 2024", etc.). Evaluate whether this is acceptable.

Structure your review as:
```
## R2 Review: Novelty & Related Work

### Paper Summary (2-3 sentences)

### Strengths (bulleted)

### Weaknesses (bulleted)

### Questions for Authors

### Minor Issues

### Scores
- Soundness: X/5
- Excitement: X/5
- Overall: X/5
- Confidence: X/5
```

Be rigorous but fair. Evaluate whether negative-result contributions are sufficiently novel and impactful for EMNLP Findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "70d7b485-11ff-4e71-9245-f39e212c10a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T10:24:34.459Z_

```json
{
  "parentUuid": "70d7b485-11ff-4e71-9245-f39e212c10a0",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
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
  "uuid": "7275f2ae-5904-47b4-8d28-6e1cae2e6307",
  "timestamp": "2026-05-15T10:24:34.459Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T10:24:38.383Z_



I'll start by reading the paper and related project files to give a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7275f2ae-5904-47b4-8d28-6e1cae2e6307",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C5FzJFBMJwxa5ENf2z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7da93e6e-20a9-4bf5-bf1d-f41e949271b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkLzb4V5CgojTZjCAF9WPr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7184,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7184,
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

_source line 4 · 2026-05-15T10:24:39.000Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XGAqQGxJffNAdSCHqusmQp`</summary>

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
  "parentUuid": "7da93e6e-20a9-4bf5-bf1d-f41e949271b6",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C5FzJFBMJwxa5ENf2z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94196fa2-ef3f-4556-b5c5-36ae889bf22e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LkLzb4V5CgojTZjCAF9WPr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7184,
      "cache_read_input_tokens": 8251,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7184
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 7184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7184,
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

_source line 5 · 2026-05-15T10:24:39.003Z_

<details><summary>↩ Tool result · `toolu_01XGAqQGxJffNAdSCHqusmQp`</summary>

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
  "parentUuid": "94196fa2-ef3f-4556-b5c5-36ae889bf22e",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "7dc1953b-8514-450e-82fe-310bf6b60f9e",
  "sourceToolAssistantUUID": "94196fa2-ef3f-4556-b5c5-36ae889bf22e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T10:24:41.990Z_



Let me read the paper and key project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dc1953b-8514-450e-82fe-310bf6b60f9e",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C5bhxHTGUjAtTh3y9t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eaea21a3-1c94-404d-b8d8-3da7612525ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuFfZtqnCzDcchhMSYw5kv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15435,
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

_source line 7 · 2026-05-15T10:24:42.433Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01BGCUiyRvgr8oAb1QibKXeP`</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eaea21a3-1c94-404d-b8d8-3da7612525ac",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C5bhxHTGUjAtTh3y9t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd37c102-026a-437e-b6a6-f78a71588306",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuFfZtqnCzDcchhMSYw5kv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15435,
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

_source line 8 · 2026-05-15T10:24:42.685Z_

<details><summary>↩ Tool result · `toolu_01BGCUiyRvgr8oAb1QibKXeP`</summary>

```text
{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (81 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp_019_supervised_verifier（等待人工审批）\n- exp_017_llama_conll_n16_s456_r1024（准备中）\n- exp_017_llama_conll_n16_r1024（准备中）\n- exp_001_n16_seed123_full（准备中）\n- exp_001_n16_seed456_full（准备中）\n- exp001_seed123（准备中）\n- exp001_seed456（准备中）\n- exp_007_ner_llama（准备中）\n- exp_002_merge_conll2003（准备中）\n- exp008_re_n16（准备中）\n\n## 近期结论\n- **exp_freeform_ablation** (negative): —\n  [freeform_ablation_results](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_freeform_ablation/report/freeform_ablation_results.md)\n- **exp_018_llama_scierc_seed456** (killed): —\n- **exp_018_llama_scierc_seed42_r1024** (success): —\n\n## 趋势\n成功 42 / 负向 19 / 失败 1 / 共 71\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_008_re_n16_full: 已被终止 — unknown\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\n- exp_002_conll_n16_r1024: 已被终止 — unknown\n- exp_007_llama_n16_r1024: 已被终止 — unknown\n- exp_017_llama_conll_n16_s123_r1024: 已被终止 — unknown\n- exp_018_llama_scierc_seed456: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd37c102-026a-437e-b6a6-f78a71588306",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "8903da94-e042-4276-ad4d-7e173d153049",
  "sourceToolAssistantUUID": "dd37c102-026a-437e-b6a6-f78a71588306",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T10:24:43.479Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RpAd2HrCseR4wTbX4ivgv3`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8903da94-e042-4276-ad4d-7e173d153049",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C5bhxHTGUjAtTh3y9t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc2fd234-26ad-4d91-a1fc-cb37c9d1adb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuFfZtqnCzDcchhMSYw5kv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15435,
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

_source line 10 · 2026-05-15T10:24:43.494Z_

<details><summary>↩ Tool result · `toolu_01RpAd2HrCseR4wTbX4ivgv3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp_019_supervised_verifier（等待人工审批）\\n- exp_017_llama_conll_n16_s456_r1024（准备中）\\n- exp_017_llama_conll_n16_r1024（准备中）\\n- exp_001_n16_seed123_full（准备中）\\n- exp_001_n16_seed456_full（准备中）\\n- exp001_seed123（准备中）\\n- exp001_seed456（准备中）\\n- exp_007_ner_llama（准备中）\\n- exp_002_merge_conll2003（准备中）\\n- exp008_re_n16（准备中）\\n\\n## 近期结论\\n- **exp_freeform_ablation** (negative): —\\n  [freeform_ablation_results](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_freeform_ablation/report/freeform_ablation_results.md)\\n- **exp_018_llama_scierc_seed456** (killed): —\\n- **exp_018_llama_scierc_seed42_r1024** (success): —\\n\\n## 趋势\\n成功 42 / 负向 19 / 失败 1 / 共 71\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- ft_002: 已被终止 — unknown\\n- mvp_pilot_002: 训练失败 — unknown\\n- exp_008_re_n16_full: 已被终止 — unknown\\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\\n- exp_002_conll_n16_r1024: 已被终止 — unknown\\n- exp_007_llama_n16_r1024: 已被终止 — unknown\\n- exp_017_llama_conll_n16_s123_r1024: 已被终止 — unknown\\n- exp_018_llama_scierc_seed456: 已被终止 — unknown\\n\", \"total_chars\": 1229, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc2fd234-26ad-4d91-a1fc-cb37c9d1adb3",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "e5a4d840-8afb-4c64-a29a-f93fbbfc4a1e",
  "sourceToolAssistantUUID": "cc2fd234-26ad-4d91-a1fc-cb37c9d1adb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T10:24:43.704Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FUBj8nZCkogLgmHEohhAE6`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5a4d840-8afb-4c64-a29a-f93fbbfc4a1e",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C5bhxHTGUjAtTh3y9t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "318e386f-e069-45b3-bee5-4f0df46db1a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuFfZtqnCzDcchhMSYw5kv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15435,
      "output_tokens": 274,
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
          "output_tokens": 274,
          "cache_read_input_tokens": 15435,
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

_source line 12 · 2026-05-15T10:24:43.714Z_

<details><summary>↩ Tool result · `toolu_01FUBj8nZCkogLgmHEohhAE6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: '2026-05-14T21:00:00.000Z'\\n  total_papers: 55\\ncategories: []\\npapers:\\n  wang2023selfconsistency:\\n    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models\\n    authors:\\n    - Xuezhi Wang\\n    - Jason Wei\\n    - Dale Schuurmans\\n    - Quoc Le\\n    - Ed Chi\\n    - Sharan Narang\\n    - Aakanksha Chowdhery\\n    - Denny Zhou\\n    year: 2023\\n    venue: ICLR 2023\\n    url: https://arxiv.org/abs/2203.11171\\n    doi: ''\\n    bibtex_key: wang2023selfconsistency\\n    category: self_consistency_reasoning\\n    role: foundation\\n    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm\\n      from closed-form answers to structured IE outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  taubenfeld2025cisc:\\n    title: Confidence Improves Self-Consistency in LLMs\\n    authors:\\n    - Amir Taubenfeld\\n    - Tom Sheffer\\n    - Eran Ofek\\n    - Amir Feder\\n    - Ariel Goldstein\\n    - Zorik Gekhman\\n    - Gal Yona\\n    year: 2025\\n    venue: ACL Findings 2025\\n    url: https://arxiv.org/abs/2502.06233\\n    doi: 10.18653/v1/2025.findings-acl.1030\\n    bibtex_key: taubenfeld2025cisc\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the\\n      same \\\"strong predictor, weak selector\\\" gap but for structured outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  kang2025selfcertainty:\\n    title: Scalable Best-of-N Selection for Large Language Models via Self-Certainty\\n    authors:\\n    - Zhewei Kang\\n    - Xuandong Zhao\\n    - Dawn Song\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2502.18581\\n    doi: ''\\n    bibtex_key: kang2025selfcertainty\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: Self-certainty metric for BoN selection using output probability distributions. Direct competitor — reward-free\\n      quality estimation that we compare against for structured IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  kim2026reasc:\\n    title: Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\\n    authors:\\n    - Junseok Kim\\n    - Nakyeong Yang\\n    - Kyungmin Min\\n    - Kyomin Jung\\n    year: 2026\\n    venue: ACL 2026\\n    url: https://arxiv.org/abs/2601.02970\\n    doi: ''\\n    bibtex_key: kim2026reasc\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: 'ReASC: two-stage adaptive sampling using response-level confidence for evidence sufficiency. Reduces cost\\n      by 70% on GSM8K. Directly relevant to our efficiency analysis.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  thirukovalluru2024atomic:\\n    title: Atomic Self-Consistency for Better Long Form Generations\\n    authors:\\n    - Raghuveer Thirukovalluru\\n    - Yukun Huang\\n    - Bhuwan Dhingra\\n    year: 2024\\n    venue: EMNLP 2024\\n    url: https://aclanthology.org/2024.emnlp-main.706/\\n    doi: 10.18653/v1/2024.emnlp-main.706\\n    bibtex_key: thirukovalluru2024atomic\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: Extends self-consistency to long-form generation by merging atomic subparts from multiple samples. Related\\n      to our structured output aggregation approach.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  chen2024usc:\\n    title: Universal Self-Consistency for Large Language Model Generation\\n    authors:\\n    - Xinyun Chen\\n    - Renat Aksitov\\n    - Uri Alon\\n    - Jie Ren\\n    - Kefan Xiao\\n    - Pengcheng Yin\\n    - Sushant Prakash\\n    - Charles Sutton\\n    - Xuezhi Wang\\n    - Denny Zhou\\n    year: 2024\\n    venue: arXiv preprint (ICML 2024 Workshop ICL)\\n    url: https://arxiv.org/abs/2311.17311\\n    doi: ''\\n    bibtex_key: chen2024usc\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: 'USC: uses LLM itself to select most consistent answer among candidates, extending SC beyond closed-form answers\\n      to free-form generation. Precursor to our structured consistency approach.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  manakul2023selfcheckgpt:\\n    title: 'SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models'\\n    authors:\\n    - Potsawee Manakul\\n    - Adian Liusie\\n    - Mark Gales\\n    year: 2023\\n    venue: EMNLP 2023\\n    url: https://aclanthology.org/2023.emnlp-main.557/\\n    doi: 10.18653/v1/2023.emnlp-main.557\\n    bibtex_key: manakul2023selfcheckgpt\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: Uses cross-sample consistency for hallucination detection — if LLM knows a fact, samples are consistent; hallucinations\\n      diverge. Motivates our consistency-based quality signal for IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  wan2025rasc:\\n    title: 'Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling'\\n    authors:\\n    - Guangya Wan\\n    - Yuqi Wu\\n    - Jie Chen\\n    - Sheng Li\\n    year: 2025\\n    venue: NAACL 2025\\n    url: https://aclanthology.org/2025.naacl-long.184/\\n    doi: 10.18653/v1/2025.naacl-long.184\\n    bibtex_key: wan2025rasc\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: 'RASC: quality-aware selection using reasoning path assessment + consistency-driven stopping. Reduces samples\\n      by ~70%. Complements our approach of structured quality-aware aggregation.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  nedellec2026consistency:\\n    title: 'Consistency-accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings\\n      from plant-health data'\\n    authors:\\n    - Claire Nédellec\\n    - Jingbo Xia\\n    year: 2026\\n    venue: Genomics & Informatics\\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/\\n    doi: 10.1186/s44342-025-00063-2\\n    bibtex_key: nedellec2026consistency\\n    category: consistency_structured_ie\\n    role: direct-competitor\\n    relevance: 'Most direct competitor: systematically measures consistency-accuracy correlation for LLM-based entity and\\n      relation extraction on plant-health data, validating consistency as a reliability signal for structured IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  vashurin2025cocoa:\\n    title: 'Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency'\\n    authors:\\n    - Roman Vashurin\\n    - Maiya Goloburda\\n    - Albina Ilina\\n    - Aleksandr Rubashevskii\\n    - Preslav Nakov\\n    - Artem Shelmanov\\n    - Maxim Panov\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2502.04964\\n    doi: ''\\n    bibtex_key: vashurin2025cocoa\\n    category: consistency_structured_ie\\n    role: background\\n    relevance: CoCoA framework unifies token-level confidence and sample-level consistency via MBR for uncertainty quantification.\\n      Provides theoretical grounding for our dual-signal approach in structured IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  hobelsberger2025systematic:\\n    title: Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\\n    authors:\\n    - Christian Hobelsberger\\n    - Theresa Winner\\n    - Andreas Nawroth\\n    - Oliver Mitevski\\n    - Anna-Carolina Haensch\\n    year: 2025\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2510.20460\\n    doi: ''\\n    bibtex_key: hobelsberger2025systematic\\n    category: consistency_structured_ie\\n    role: background\\n    relevance: Systematic comparison of VCE, MSP, self-consistency, and CoCoA for LLM uncertainty estimation. Shows hybrid\\n      CoCoA yields best calibration, supporting our multi-signal aggregation design.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  geng2024confidence:\\n    title: A Survey of Confidence Estimation and Calibration in Large Language Models\\n    authors:\\n    - Jiahui Geng\\n    - Fengyu Cai\\n    - Yuxia Wang\\n    - Heinz Koeppl\\n    - Preslav Nakov\\n    - Iryna Gurevych\\n    year: 2024\\n    venue: NAACL 2024\\n    url: https://arxiv.org/abs/2311.08298\\n    doi: 10.18653/v1/2024.naacl-long.366\\n    bibtex_key: geng2024confidence\\n    category: confidence_surveys\\n    role: survey\\n    relevance: Comprehensive survey of LLM confidence estimation and calibration techniques. Provides taxonomic context for\\n      positioning our consistency-based confidence approach within the broader landscape.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  wen2025know:\\n    title: 'Know Your Limits: A Survey of Abstention in Large Language Models'\\n    authors:\\n    - Bingbing Wen\\n    - Jihan Yao\\n    - Shangbin Feng\\n    - Chenjun Xu\\n    - Yulia Tsvetkov\\n    - Bill Howe\\n    - Lucy Lu Wang\\n    year: 2025\\n    venue: TACL 2025\\n    url: https://arxiv.org/abs/2407.18418\\n    doi: 10.1162/tacl_a_00754\\n    bibtex_key: wen2025know\\n    category: confidence_surveys\\n    role: supplementary\\n    relevance: 'Survey on LLM abstention from query, model, and human-values perspectives. Our consistency-based filtering\\n      can be viewed as a structured-IE-specific abstention mechanism. [SUPPLEMENTARY: overlaps with geng2024 main survey]'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  xia2025survey:\\n    title: A Survey of Uncertainty Estimation Methods on Large Language Models\\n    authors:\\n    - Zhiqiu Xia\\n    - Jinxuan Xu\\n    - Yuqian Zhang\\n    - Hang Liu\\n    year: 2025\\n    venue: ACL Findings 2025\\n    url: https://aclanthology.org/2025.findings-acl.1101/\\n    doi: ''\\n    bibtex_key: xia2025survey\\n    category: confidence_surveys\\n    role: supplementary\\n    relevance: 'Most comprehensive LLM uncertainty estimation survey with novel taxonomy (verbalizing, latent, consistency-based,\\n      semantic clustering). Directly contextualizes our method within the consistency-based branch. [SUPPLEMENTARY: overlaps\\n      with geng2024 main survey]'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  liu2025uqcalibration:\\n    title: 'Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey'\\n    authors:\\n    - Xiaoou Liu\\n    - Tiejin Chen\\n    - Longchao Da\\n    - Chacha Chen\\n    - Zhen Lin\\n    - Hua Wei\\n    year: 2025\\n    venue: KDD 2025\\n    url: https://arxiv.org/abs/2503.15850\\n    doi: 10.1145/3711896.3736569\\n    bibtex_key: liu2025uqcalibration\\n    category: confidence_surveys\\n    role: supplementary\\n    relevance: 'Survey analyzing UQ through input, reasoning, parameter, and prediction uncertainty dimensions. Complements\\n      other surveys with focus on calibration techniques applicable to our structured IE setting. [SUPPLEMENTARY: overlaps\\n      with geng2024 main survey]'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  kuhn2023semantic:\\n    title: 'Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation'\\n    authors:\\n    - Lorenz Kuhn\\n    - Yarin Gal\\n    - Sebastian Farquhar\\n    year: 2023\\n    venue: ICLR 2023\\n    url: https://arxiv.org/abs/2302.09664\\n    doi: ''\\n    bibtex_key: kuhn2023semantic\\n    category: uncertainty_calibration\\n    role: foundation\\n    relevance: Introduces semantic entropy for NLG uncertainty estimation by clustering semantically equivalent outputs. Foundation\\n      for our structured consistency metric that operates at the semantic level of IE triples.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  kadavath2022language:\\n    title: Language Models (Mostly) Know What They Know\\n    authors:\\n    - Saurav Kadavath\\n    - Tom Conerly\\n    - Amanda Askell\\n    - Tom Henighan\\n    - Dawn Drain\\n    - Ethan Perez\\n    - Nicholas Schiefer\\n    - Zac Hatfield-Dodds\\n    - Nova DasSarma\\n    - Eli Tran-Johnson\\n    - Scott Johnston\\n    - Sheer El-Showk\\n    - Andy Jones\\n    - Nelson Elhage\\n    - Tristan Hume\\n    - Anna Chen\\n    - Yuntao Bai\\n    - Sam Bowman\\n    - Stanislav Fort\\n    - Deep Ganguli\\n    - Danny Hernandez\\n    - Josh Jacobson\\n    - Jackson Kernion\\n    - Shauna Kravec\\n    - Liane Lovitt\\n    - Kamal Ndousse\\n    - Catherine Olsson\\n    - Sam Ringer\\n    - Dario Amodei\\n    - Tom Brown\\n    - Jack Clark\\n    - Nicholas Joseph\\n    - Ben Mann\\n    - Sam McCandlish\\n    - Chris Olah\\n    - Jared Kaplan\\n    year: 2022\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2207.05221\\n    doi: ''\\n    bibtex_key: kadavath2022language\\n    category: uncertainty_calibration\\n    role: foundation\\n    relevance: Demonstrates LLMs can self-evaluate correctness via P(True) probing. Foundation for using model self-knowledge\\n      as a confidence signal, which we extend to structured IE output quality estimation.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  guo2017calibration:\\n    title: On Calibration of Modern Neural Networks\\n    authors:\\n    - Chuan Guo\\n    - Geoff Pleiss\\n    - Yu Sun\\n    - Kilian Q. Weinberger\\n    year: 2017\\n    venue: ICML 2017\\n    url: https://arxiv.org/abs/1706.04599\\n    doi: ''\\n    bibtex_key: guo2017calibration\\n    category: uncertainty_calibration\\n    role: foundation\\n    relevance: Seminal work showing modern neural networks are miscalibrated and proposing temperature scaling. Foundational\\n      reference for all calibration work including our LLM confidence calibration for IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  desai2020calibration:\\n    title: Calibration of Pre-trained Transformers\\n    authors:\\n    - Shrey Desai\\n    - Greg Durrett\\n    year: 2020\\n    venue: EMNLP 2020\\n    url: https://arxiv.org/abs/2003.07892\\n    doi: 10.18653/v1/2020.emnlp-main.21\\n    bibtex_key: desai2020calibration\\n    category: uncertainty_calibration\\n    role: foundation\\n    relevance: Shows pre-trained transformers (BERT, RoBERTa) are well-calibrated in-domain but degrade OOD. Bridges classical\\n      calibration to the transformer era, motivating our LLM-specific calibration analysis.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  kossen2024semantic:\\n    title: 'Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs'\\n    authors:\\n    - Jannik Kossen\\n    - Jiatong Han\\n    - Muhammed Razzak\\n    - Lisa Schut\\n    - Shreshth Malik\\n    - Yarin Gal\\n    year: 2024\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2406.15927\\n    doi: ''\\n    bibtex_key: kossen2024semantic\\n    category: uncertainty_calibration\\n    role: background\\n    relevance: Proposes lightweight probes to approximate semantic entropy from hidden states of a single generation, reducing\\n      cost to near-zero. Relevant to our goal of efficient uncertainty estimation for structured IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  xiong2024verbalized:\\n    title: Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\\n    authors:\\n    - Miao Xiong\\n    - Zhiyuan Hu\\n    - Xinyang Lu\\n    - Yifei Li\\n    - Jie Fu\\n    - Junxian He\\n    - Bryan Hooi\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2306.13063\\n    doi: ''\\n    bibtex_key: xiong2024verbalized\\n    category: uncertainty_calibration\\n    role: background\\n    relevance: Systematic evaluation of verbalized confidence elicitation via prompting, sampling, and aggregation. Directly\\n      relevant to our use of LLM-expressed confidence as a signal for structured IE quality.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch1\\n    added_at: '2026-05-14T17:52:10.000Z'\\n  fisch2021conformal:\\n    title: Few-Shot Conformal Prediction with Auxiliary Tasks\\n    authors:\\n    - Adam Fisch\\n    - Tal Schuster\\n    - Tommi Jaakkola\\n    - Regina Barzilay\\n    year: 2021\\n    venue: ICML 2021\\n    url: https://arxiv.org/abs/2102.08898\\n    doi: 10.5555/3524938.3525234\\n    bibtex_key: fisch2021conformal\\n    category: conformal_prediction\\n    role: supplementary\\n    relevance: 'Adapts conformal prediction to few-shot settings via meta-learning over auxiliary tasks, producing tighter\\n      prediction sets with formal coverage guarantees. SUPPLEMENTARY - CP not a method component, angelopoulos2021 retained as main CP reference.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  angelopoulos2021conformal:\\n    title: Uncertainty Sets for Image Classifiers using Conformal Prediction\\n    authors:\\n    - Anastasios N. Angelopoulos\\n    - Stephen Bates\\n    - Jitendra Malik\\n    - Michael I. Jordan\\n    year: 2021\\n    venue: ICLR 2021\\n    url: https://arxiv.org/abs/2009.14193\\n    doi: ''\\n    bibtex_key: angelopoulos2021conformal\\n    category: conformal_prediction\\n    role: foundation\\n    relevance: Introduces RAPS (Regularized Adaptive Prediction Sets) with finite-sample coverage guarantees. Foundation for\\n      conformal prediction methodology we adapt to structured IE output sets.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  bates2021rcps:\\n    title: Distribution-Free, Risk-Controlling Prediction Sets\\n    authors:\\n    - Stephen Bates\\n    - Anastasios Angelopoulos\\n    - Lihua Lei\\n    - Jitendra Malik\\n    - Michael I. Jordan\\n    year: 2021\\n    venue: Journal of the ACM 2021\\n    url: https://arxiv.org/abs/2101.02703\\n    doi: 10.1145/3478535\\n    bibtex_key: bates2021rcps\\n    category: conformal_prediction\\n    role: supplementary\\n    relevance: 'Generalizes conformal prediction to control arbitrary monotone losses for set-valued predictors with finite-sample\\n      guarantees. SUPPLEMENTARY - CP not a method component, angelopoulos2021 retained as main CP reference.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  xiao2019uncertainty:\\n    title: Quantifying Uncertainties in Natural Language Processing Tasks\\n    authors:\\n    - Yijun Xiao\\n    - William Yang Wang\\n    year: 2019\\n    venue: AAAI 2019\\n    url: https://arxiv.org/abs/1811.07253\\n    doi: 10.1609/aaai.v33i01.33017322\\n    bibtex_key: xiao2019uncertainty\\n    category: token_span_uncertainty_ner\\n    role: foundation\\n    relevance: Pioneers Bayesian uncertainty quantification for NLP tasks including NER, showing that modeling data and model\\n      uncertainty improves both performance and reliability for token-level predictions.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  shelmanov2021active:\\n    title: Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\\n    authors:\\n    - Artem Shelmanov\\n    - Dmitri Puzyrev\\n    - Lyubov Kupriyanova\\n    - Denis Belyakov\\n    - Daniil Larionov\\n    - Nikita Khromov\\n    - Olga Kozlova\\n    - Ekaterina Artemova\\n    - Dmitry V. Dylov\\n    - Alexander Panchenko\\n    year: 2021\\n    venue: EACL 2021\\n    url: https://arxiv.org/abs/2101.08133\\n    doi: 10.18653/v1/2021.eacl-main.145\\n    bibtex_key: shelmanov2021active\\n    category: token_span_uncertainty_ner\\n    role: foundation\\n    relevance: Extensive empirical study of Bayesian uncertainty estimation (MC dropout variants) for sequence tagging with\\n      pre-trained models. Establishes best practices for uncertainty-guided active learning in NER.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  zhang2023ener:\\n    title: 'E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition'\\n    authors:\\n    - Zhen Zhang\\n    - Mengting Hu\\n    - Shiwan Zhao\\n    - Minlie Huang\\n    - Haotian Wang\\n    - Lemao Liu\\n    - Zhirui Zhang\\n    - Zhe Liu\\n    - Bingzhe Wu\\n    year: 2023\\n    venue: ACL Findings 2023\\n    url: https://arxiv.org/abs/2305.17854\\n    doi: 10.18653/v1/2023.findings-acl.103\\n    bibtex_key: zhang2023ener\\n    category: token_span_uncertainty_ner\\n    role: background\\n    relevance: Applies evidential deep learning to NER with uncertainty-guided loss terms, addressing sparse entities and\\n      OOV/OOD discrimination. Demonstrates token-level uncertainty estimation across multiple NER paradigms.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  lakshminarayanan2017ensembles:\\n    title: Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\n    authors:\\n    - Balaji Lakshminarayanan\\n    - Alexander Pritzel\\n    - Charles Blundell\\n    year: 2017\\n    venue: NeurIPS 2017\\n    url: https://arxiv.org/abs/1612.01474\\n    doi: ''\\n    bibtex_key: lakshminarayanan2017ensembles\\n    category: ensemble_mc_dropout\\n    role: foundation\\n    relevance: Proposes deep ensembles as a simple, scalable alternative to Bayesian NNs for predictive uncertainty estimation.\\n      Foundational baseline for ensemble-based uncertainty quantification we compare against.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  gal2016dropout:\\n    title: 'Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning'\\n    authors:\\n    - Yarin Gal\\n    - Zoubin Ghahramani\\n    year: 2016\\n    venue: ICML 2016\\n    url: https://arxiv.org/abs/1506.02142\\n    doi: ''\\n    bibtex_key: gal2016dropout\\n    category: ensemble_mc_dropout\\n    role: foundation\\n    relevance: Establishes theoretical framework casting dropout as approximate Bayesian inference, enabling MC dropout for\\n      uncertainty estimation. Foundation for all dropout-based uncertainty methods we build upon.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  fomicheva2020unsupervised:\\n    title: Unsupervised Quality Estimation for Neural Machine Translation\\n    authors:\\n    - Marina Fomicheva\\n    - Shuo Sun\\n    - Lisa Yankovskaya\\n    - Frédéric Blain\\n    - Francisco Guzmán\\n    - Mark Fishel\\n    - Nikolaos Aletras\\n    - Vishrav Chaudhary\\n    - Lucia Specia\\n    year: 2020\\n    venue: TACL 2020\\n    url: https://arxiv.org/abs/2005.10608\\n    doi: 10.1162/tacl_a_00330\\n    bibtex_key: fomicheva2020unsupervised\\n    category: ensemble_mc_dropout\\n    role: background\\n    relevance: Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving\\n      strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch2\\n    added_at: '2026-05-14T18:10:52.000Z'\\n  cobbe2021verifiers:\\n    title: Training Verifiers to Solve Math Word Problems\\n    authors:\\n    - Karl Cobbe\\n    - Vineet Kosaraju\\n    - Mohammad Bavarian\\n    - Mark Chen\\n    - Heewoo Jun\\n    - Lukasz Kaiser\\n    - Matthias Plappert\\n    - Jerry Tworek\\n    - Jacob Hilton\\n    - Reiichiro Nakano\\n    - Christopher Hesse\\n    - John Schulman\\n    year: 2021\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2110.14168\\n    doi: ''\\n    bibtex_key: cobbe2021verifiers\\n    category: verifier_reward_models\\n    role: foundation\\n    relevance: 'Foundation paper: introduces training outcome-based verifiers (ORM) for math word problems and the GSM8K benchmark.\\n      Establishes the verify-then-select paradigm our method builds upon.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  lightman2024verify:\\n    title: Let's Verify Step by Step\\n    authors:\\n    - Hunter Lightman\\n    - Vineet Kosaraju\\n    - Yura Burda\\n    - Harri Edwards\\n    - Bowen Baker\\n    - Teddy Lee\\n    - Jan Leike\\n    - John Schulman\\n    - Ilya Sutskever\\n    - Karl Cobbe\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2305.20050\\n    doi: ''\\n    bibtex_key: lightman2024verify\\n    category: verifier_reward_models\\n    role: foundation\\n    relevance: 'Foundation paper: demonstrates process reward models (PRMs) with step-level supervision outperform outcome-based\\n      verification. Key motivation for fine-grained quality signals in our structured IE aggregation.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  wang2024mathshepherd:\\n    title: 'Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations'\\n    authors:\\n    - Peiyi Wang\\n    - Lei Li\\n    - Zhihong Shao\\n    - Runxin Xu\\n    - Damai Dai\\n    - Yifei Li\\n    - Deli Chen\\n    - Yu Wu\\n    - Zhifang Sui\\n    year: 2024\\n    venue: ACL 2024\\n    url: https://arxiv.org/abs/2312.08935\\n    doi: ''\\n    bibtex_key: wang2024mathshepherd\\n    category: verifier_reward_models\\n    role: background\\n    relevance: Automated process reward model construction without human annotations, enabling step-level verification at scale.\\n      Demonstrates ORM/PRM effectiveness for both reranking and reinforcement learning.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  snell2024scaling:\\n    title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\\n    authors:\\n    - Charlie Snell\\n    - Jaehoon Lee\\n    - Kelvin Xu\\n    - Aviral Kumar\\n    year: 2024\\n    venue: ICLR 2025\\n    url: https://arxiv.org/abs/2408.03314\\n    doi: ''\\n    bibtex_key: snell2024scaling\\n    category: tts_scaling\\n    role: foundation\\n    relevance: 'Foundation paper: introduces compute-optimal test-time scaling, showing adaptive per-prompt compute allocation\\n      improves efficiency 4x over best-of-N. Directly motivates our adaptive sampling strategy.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  brown2024monkeys:\\n    title: 'Large Language Monkeys: Scaling Inference Compute with Repeated Sampling'\\n    authors:\\n    - Bradley Brown\\n    - Jordan Juravsky\\n    - Ryan Ehrlich\\n    - Ronald Clark\\n    - Quoc V. Le\\n    - Christopher Ré\\n    - Azalia Mirhoseini\\n    year: 2024\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2407.21787\\n    doi: ''\\n    bibtex_key: brown2024monkeys\\n    category: tts_scaling\\n    role: foundation\\n    relevance: 'Foundation paper: demonstrates log-linear scaling of coverage with repeated sampling across tasks, establishing\\n      inference-time scaling laws. Motivates our multi-sample approach for structured IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  wu2024inference:\\n    title: 'Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models'\\n    authors:\\n    - Yangzhen Wu\\n    - Zhiqing Sun\\n    - Shanda Li\\n    - Sean Welleck\\n    - Yiming Yang\\n    year: 2024\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2408.00724\\n    doi: ''\\n    bibtex_key: wu2024inference\\n    category: tts_scaling\\n    role: background\\n    relevance: Empirical analysis of compute-optimal inference strategies showing smaller models with advanced inference algorithms\\n      achieve Pareto-optimal cost-performance trade-offs. Complements our efficiency analysis.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  kuleshov2015calibrated:\\n    title: Calibrated Structured Prediction\\n    authors:\\n    - Volodymyr Kuleshov\\n    - Percy Liang\\n    year: 2015\\n    venue: NeurIPS 2015\\n    url: https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html\\n    doi: ''\\n    bibtex_key: kuleshov2015calibrated\\n    category: structured_calibration_ie\\n    role: foundation\\n    relevance: 'Foundation paper: extends calibration to structured prediction with formal guarantees, proposing recalibration\\n      methods for marginal and conditional queries. Theoretical basis for calibrated structured IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  culotta2004confidence:\\n    title: Confidence Estimation for Information Extraction\\n    authors:\\n    - Aron Culotta\\n    - Andrew McCallum\\n    year: 2004\\n    venue: HLT-NAACL 2004\\n    url: https://aclanthology.org/N04-4028/\\n    doi: ''\\n    bibtex_key: culotta2004confidence\\n    category: structured_calibration_ie\\n    role: foundation\\n    relevance: 'Foundation paper: pioneers confidence estimation for CRF-based information extraction at both field and record\\n      levels. Establishes the problem setting our LLM-based approach addresses.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  jagannatha2020calibrating:\\n    title: Calibrating Structured Output Predictors for Natural Language Processing\\n    authors:\\n    - Abhyuday Jagannatha\\n    - Hong Yu\\n    year: 2020\\n    venue: ACL 2020\\n    url: https://aclanthology.org/2020.acl-main.188/\\n    doi: ''\\n    bibtex_key: jagannatha2020calibrating\\n    category: structured_calibration_ie\\n    role: background\\n    relevance: Proposes general calibration scheme for neural structured prediction models in NLP including NER and QA. Bridges\\n      classical calibration methods to modern neural IE, directly relevant to our structured output calibration.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  geifman2017selective:\\n    title: Selective Classification for Deep Neural Networks\\n    authors:\\n    - Yonatan Geifman\\n    - Ran El-Yaniv\\n    year: 2017\\n    venue: NeurIPS 2017\\n    url: https://arxiv.org/abs/1705.08500\\n    doi: ''\\n    bibtex_key: geifman2017selective\\n    category: selective_prediction\\n    role: foundation\\n    relevance: 'Foundation paper: introduces selective classification framework for DNNs with guaranteed risk control at specified\\n      coverage levels. Theoretical foundation for our consistency-based selective prediction in IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  ren2023selfevaluation:\\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\\n    authors:\\n    - Jie Ren\\n    - Yao Zhao\\n    - Tu Vu\\n    - Peter J. Liu\\n    - Balaji Lakshminarayanan\\n    year: 2023\\n    venue: NeurIPS 2023 Workshop\\n    url: https://arxiv.org/abs/2312.09300\\n    doi: ''\\n    bibtex_key: ren2023selfevaluation\\n    category: selective_prediction\\n    role: background\\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch3\\n    added_at: '2026-05-14T19:30:00.000Z'\\n  wadhwa2023revisiting:\\n    title: Revisiting Relation Extraction in the era of Large Language Models\\n    authors:\\n    - Somin Wadhwa\\n    - Silvio Amir\\n    - Byron Wallace\\n    year: 2023\\n    venue: ACL 2023\\n    url: https://aclanthology.org/2023.acl-long.868/\\n    doi: 10.18653/v1/2023.acl-long.868\\n    bibtex_key: wadhwa2023revisiting\\n    category: generative_ie\\n    role: foundation\\n    relevance: 'Foundation paper: evaluates LLMs (GPT-3, Flan-T5) for relation extraction as seq2seq, showing few-shot prompting\\n      achieves near-SOTA performance. Establishes generative RE paradigm our structured consistency method builds upon.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  sainz2024gollie:\\n    title: 'GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction'\\n    authors:\\n    - Oscar Sainz\\n    - Iker García-Ferrero\\n    - Rodrigo Agerri\\n    - Oier Lopez de Lacalle\\n    - German Rigau\\n    - Eneko Agirre\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2310.03668\\n    doi: ''\\n    bibtex_key: sainz2024gollie\\n    category: generative_ie\\n    role: foundation\\n    relevance: 'Foundation paper: fine-tunes LLM to follow annotation guidelines for zero-shot IE, achieving strong generalization\\n      to unseen tasks. Key baseline for guideline-driven structured generation in our framework.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  luan2018scierc:\\n    title: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\\n    authors:\\n    - Yi Luan\\n    - Luheng He\\n    - Mari Ostendorf\\n    - Hannaneh Hajishirzi\\n    year: 2018\\n    venue: EMNLP 2018\\n    url: https://aclanthology.org/D18-1360/\\n    doi: 10.18653/v1/D18-1360\\n    bibtex_key: luan2018scierc\\n    category: generative_ie\\n    role: dataset\\n    relevance: 'Introduces SciERC dataset with entity, relation, and coreference annotations for scientific text. Primary evaluation\\n      benchmark for our structured IE experiments.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  tjongkimsang2003conll:\\n    title: 'Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition'\\n    authors:\\n    - Erik F. Tjong Kim Sang\\n    - Fien De Meulder\\n    year: 2003\\n    venue: CoNLL 2003\\n    url: https://aclanthology.org/W03-0419/\\n    doi: ''\\n    bibtex_key: tjongkimsang2003conll\\n    category: generative_ie\\n    role: dataset\\n    relevance: 'Introduces CoNLL-2003 NER dataset, the standard benchmark for named entity recognition. Core evaluation dataset\\n      for our NER consistency experiments.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  derczynski2017wnut:\\n    title: Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\\n    authors:\\n    - Leon Derczynski\\n    - Eric Nichols\\n    - Marieke van Erp\\n    - Nut Limsopatham\\n    year: 2017\\n    venue: W-NUT Workshop at EMNLP 2017\\n    url: https://aclanthology.org/W17-4418/\\n    doi: ''\\n    bibtex_key: derczynski2017wnut\\n    category: generative_ie\\n    role: dataset\\n    relevance: 'Introduces WNUT-17 dataset for novel and emerging entity recognition in noisy text. Tests our method robustness\\n      on harder, low-resource NER scenarios.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  willard2023guided:\\n    title: Efficient Guided Generation for Large Language Models\\n    authors:\\n    - Brandon T. Willard\\n    - Rémi Louf\\n    year: 2023\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2307.09702\\n    doi: ''\\n    bibtex_key: willard2023guided\\n    category: generative_ie\\n    role: background\\n    relevance: 'Reformulates neural text generation as FSM transitions, enabling efficient constrained decoding with regexes and\\n      CFGs. Foundational for structured output guarantees in our IE generation pipeline.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  fleiss1971agreement:\\n    title: Measuring Nominal Scale Agreement Among Many Raters\\n    authors:\\n    - Joseph L. Fleiss\\n    year: 1971\\n    venue: Psychological Bulletin\\n    url: https://psycnet.apa.org/record/1972-05083-001\\n    doi: 10.1037/h0031619\\n    bibtex_key: fleiss1971agreement\\n    category: agreement_metrics\\n    role: foundation\\n    relevance: 'Introduces Fleiss kappa for measuring inter-rater agreement on nominal scales with multiple raters. Foundation\\n      metric for quantifying cross-sample consistency in our multi-generation IE aggregation.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  jaccard1901distribution:\\n    title: Étude comparative de la distribution florale dans une portion des Alpes et du Jura\\n    authors:\\n    - Paul Jaccard\\n    year: 1901\\n    venue: Bulletin de la Société Vaudoise des Sciences Naturelles\\n    url: https://www.researchgate.net/publication/225035806\\n    doi: ''\\n    bibtex_key: jaccard1901distribution\\n    category: agreement_metrics\\n    role: foundation\\n    relevance: 'Introduces the Jaccard similarity coefficient for set comparison. Foundation metric for measuring pairwise overlap\\n      between extracted entity/relation sets across multiple LLM samples.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  wang2025rankedvoting:\\n    title: Ranked Voting based Self-Consistency of Large Language Models\\n    authors:\\n    - Weiqin Wang\\n    - Yile Wang\\n    - Hui Huang\\n    year: 2025\\n    venue: ACL Findings 2025\\n    url: https://arxiv.org/abs/2505.10772\\n    doi: ''\\n    bibtex_key: wang2025rankedvoting\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: 'Extends SC from single-answer majority vote to ranked answer lists with instant-runoff and Borda count voting.\\n      Relevant to our multi-candidate aggregation strategy for structured IE outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  oh2025latentsc:\\n    title: 'Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning'\\n    authors:\\n    - Jungsuk Oh\\n    - Jay-Yoon Lee\\n    year: 2025\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2508.18395\\n    doi: ''\\n    bibtex_key: oh2025latentsc\\n    category: self_consistency_reasoning\\n    role: background\\n    relevance: 'LSC: uses learnable summary token embeddings to compute semantic consistency across samples without text matching.\\n      Extends SC to long-form outputs with negligible overhead, relevant to our structured output consistency measurement.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:lit_batch4\\n    added_at: '2026-05-14T21:00:00.000Z'\\n  zhou2024uniner:\\n    title: 'UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition'\\n    authors:\\n    - Wenxuan Zhou\\n    - Sheng Zhang\\n    - Yu Gu\\n    - Muhao Chen\\n    - Hoifung Poon\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2308.03279\\n    doi: ''\\n    bibtex_key: zhou2024uniner\\n    category: generative_ie\\n    role: foundation\\n    relevance: 'UniNER: distills ChatGPT NER capabilities into smaller models via targeted distillation on diverse entity types.\\n      Demonstrates LLM-based generative NER at scale. Directly relevant as representative LLM-based NER baseline.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-agent:manual\\n    added_at: '2026-05-14T21:05:00.000Z'\\n  josifoski2022genie:\\n    title: 'GenIE: Generative Information Extraction'\\n    authors:\\n    - Martin Josifoski\\n    - Nicola De Cao\\n    - Maxime Peyrard\\n    - Fabio Petroni\\n    - Robert West\\n    year: 2022\\n    venue: NAACL 2022\\n    url: https://arxiv.org/abs/2112.08340\\n    doi: 10.18653/v1/2022.naacl-main.342\\n    bibtex_key: josifoski2022genie\\n    category: generative_ie\\n    role: foundation\\n    relevance: 'First end-to-end autoregressive formulation of closed IE with bi-level constrained decoding (high-level triplet\\n      structure + prefix-trie entity/relation constraints). Directly relevant as the foundational constrained decoding approach for structured IE.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-agent:manual\\n    added_at: '2026-05-14T22:00:00.000Z'\\n  li2023codeie:\\n    title: 'CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors'\\n    authors:\\n    - Peng Li\\n    - Tianxiang Sun\\n    - Qiong Tang\\n    - Hang Yan\\n    - Yuanbin Wu\\n    - Xuanjing Huang\\n    - Xipeng Qiu\\n    year: 2023\\n    venue: ACL 2023\\n    url: https://arxiv.org/abs/2305.05711\\n    doi: 10.18653/v1/2023.acl-long.855\\n    bibtex_key: li2023codeie\\n    category: generative_ie\\n    role: background\\n    relevance: 'Recasts IE as code generation, leveraging Code-LLMs structural output capabilities for NER and RE. Demonstrates\\n      alternative structured generation approach complementary to constrained decoding.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-agent:manual\\n    added_at: '2026-05-14T22:00:00.000Z'\\n  wang2023instructuie:\\n    title: 'InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction'\\n    authors:\\n    - Xiao Wang\\n    - Weikang Zhou\\n    - Can Zu\\n    - Han Xia\\n    - Tianze Chen\\n    - Yuansen Zhang\\n    - Rui Zheng\\n    - Junjie Ye\\n    - Qi Zhang\\n    - Tao Gui\\n    - Jihua Kang\\n    - Jingsheng Yang\\n    - Siyuan Li\\n    - Chunsai Du\\n    year: 2023\\n    venue: arXiv preprint\\n    url: https://arxiv.org/abs/2304.08085\\n    doi: ''\\n    bibtex_key: wang2023instructuie\\n    category: generative_ie\\n    role: foundation\\n    relevance: 'Unified instruction-tuned IE framework covering NER, RE, EE across 32 datasets. Demonstrates multi-task generative\\n      IE with instruction tuning, directly relevant as representative LLM-based unified IE system.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-agent:manual\\n    added_at: '2026-05-14T22:00:00.000Z'\\n\", \"total_chars\": 43664, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "318e386f-e069-45b3-bee5-4f0df46db1a2",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "ed54bb66-543f-400b-b69b-847e14153e30",
  "sourceToolAssistantUUID": "318e386f-e069-45b3-bee5-4f0df46db1a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-15T10:24:47.300Z_

Now let me read the paper artifacts and key experimental results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed54bb66-543f-400b-b69b-847e14153e30",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C5wgVg7GMiexbLLS98",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eebc9d70-d43f-449d-9890-cc4ff0313f40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KVHAu3RAVcaFDRsuujvBy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17926,
      "cache_read_input_tokens": 16882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17926,
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

_source line 14 · 2026-05-15T10:24:48.467Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AJraksdNMkJDRNMhRUguu5`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eebc9d70-d43f-449d-9890-cc4ff0313f40",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C5wgVg7GMiexbLLS98",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db577016-5819-4a72-bb58-9e1a772c554a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KVHAu3RAVcaFDRsuujvBy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17926,
      "cache_read_input_tokens": 16882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17926,
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

_source line 15 · 2026-05-15T10:24:48.478Z_

<details><summary>↩ Tool result · `toolu_01AJraksdNMkJDRNMhRUguu5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md\", \"content\": \"# Paper Framing — struct_self_consist_ie\\n\\n> Updated 2026-05-15 — D072: Ablation 负结果证明 gap 是 universal。Free-form ablation falsified \\\"constrained decoding bottleneck\\\" hypothesis (LP std ratio 0.97, tied fraction -2pp). Score compression is model/task intrinsic → gap is a fundamental property of structured IE, not a regime artifact. Paper strengthened: controlled experiment proves universality via elimination. Launching exp-019 supervised verifier as \\\"so what\\\" moment.\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Findings (via ARR May 2026)\\n- Deadline: ARR May cycle, 2026-05-25\\n\\n## Core Claims (3 条, D072 updated — ablation proves universality)\\n\\n### Claim 1 (PRIMARY — Universal Correlation-Selection Gap)\\nThe correlation-selection gap in structured IE is a **fundamental property of the task**, not an artifact of constrained decoding. Confidence signals reliably predict output quality (AUROC up to 0.75) but cannot select better candidates from multiple samples. A controlled free-form decoding ablation proves this gap is universal: removing constrained decoding does NOT recover logprob variance or selection ability.\\n\\n**Two-layer argument**:\\n- Layer 1 (definitional, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification of QE vs selection conflation in prior work, not an empirical finding.\\n- Layer 2 (empirical, the core contribution): (a) Logprob — the only per-sample signal — fails due to intrinsic score compression (60% of instances have within-sample range < 0.05). (b) Consensus-proximity/MBR strategies also fail despite success in MT (non-trivial). (c) **Free-form ablation FALSIFIES regime-specific hypothesis**: removing constrained decoding does NOT recover logprob discrimination (std ratio 0.97, tied fraction -2pp) → compression is model/task intrinsic, proving universality via elimination.\\n\\n**Key evidence (score compression)**:\\n- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ: 0.08→0.39\\n- Full set: logprob +0.6pp, bootstrap p=0.39, Cohen's d=0.038 (negligible), 95% CI [-3.0, +4.2]pp\\n- Oracle headroom: NER +13pp, RE +18pp → information exists but signals can't access it\\n\\n**Key evidence (free-form ablation)** [DONE — exp_freeform_ablation, NEGATIVE]:\\n- LP distribution: constrained std=0.0206, free-form std=0.0199 (ratio 0.97, virtually unchanged)\\n- Tied fraction: 59.7% → 57.7% (-2.0pp, negligible)\\n- NER selection: +0.59pp → +0.18pp (both negligible vs greedy)\\n- RE selection: -0.68pp → +1.69pp (flipped positive — secondary finding)\\n- NER VC rho: 0.379 → 0.409 (slight QE improvement, selection still fails)\\n- Parse rate: 99.95% (fine-tuned model retains JSON format without grammar)\\n- **Conclusion**: Score compression is model/task intrinsic. The gap is universal.\\n\\n**exp-019 supervised verifier**: SKIPPED (Reviewer recommendation). Reasons: DDL 10 days, scope creep risk (analytical paper + solution = type mismatch), exp-016 LR ensemble already underperforms EM (0.666 vs 0.749). Verifier is follow-up paper material.\\n\\n**Bonus finding (parse rate)**: Free-form parse rate 99.95% (4406/4408) — fine-tuned 8B model generates valid JSON without grammar constraints. Challenges intro:19 claim about constrained decoding necessity for format compliance.\\n\\n**Implications**: Not just \\\"signals don't work\\\" but \\\"here's WHY they don't work (intrinsic score compression), here's proof it's universal (controlled ablation via elimination), and here's the forward direction (breaking LP compression requires fundamentally different approaches — trained verifiers, multi-round refinement — not simply relaxing decoding constraints).\\\"\\n\\n### Claim 2 (METHODOLOGY — QE Evaluation Framework)\\nSystematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. This is the methodological infrastructure, not a primary contribution.\\n\\n**Key results**:\\n- NER: EM AUROC 0.749, voting_conf ρ=0.379, SJ ρ=0.360 — all >> logprob (AUROC 0.578, ρ=0.205)\\n- RE (preliminary, single benchmark): voting_conf leads both full and conditional\\n- Difficulty-dependent signal ranking: WNUT-17 conditional collapse (ρ significant → n.s.) + logprob ρ=−0.410 (non-obvious: overconfidence on OOD)\\n- Temperature robustness: SJ Δρ=±0.01 vs FK Δρ=±0.06-0.09\\n\\n**Evidence preserved from original Claim 1** (SciERC, N=8, T=1.0, exp_012_rerun_1024):\\n- NER full (n=529): ρ — voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205; AUROC — EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578\\n- RE full (n=397): AUROC — EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601\\n- ECE (NER): EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706\\n\\n### Claim 2b (Selection evidence)\\n**exp_016_rerun_1024 evidence** (SciERC, N=8, T=1.0):\\n- NER best-of-N (n=529): logprob 0.6501 > sj 0.6450 = ensemble 0.6450 > greedy 0.6439 > voting 0.6337 > random 0.6077 (oracle 0.7758)\\n- RE best-of-N (n=397): greedy 0.4042 > logprob 0.3948 > sj 0.3855 = ensemble 0.3855 > voting 0.3592 > random 0.3544 (oracle 0.5850)\\n\\n**exp_016_rerun_1024_bootstrap evidence** (3-seed bootstrap, 1000 iterations):\\n- NER logprob vs greedy: bootstrap 95% CI [−0.030, +0.042], permutation p=0.39\\n- Effect size: Cohen's d=0.038 (negligible), sign test win rate=0.466\\n\\n### Claim 3 (Diagnostic — task-complexity boundary)\\nThe effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.\\n\\n**MVP evidence**: RE full vs cond AUROC lift — EM: 0.706→0.752 (+4.6pp), SJ: 0.670→0.646 (−2.4pp, 待确认), voting_conf: 0.694→0.642 (−5.2pp, 待确认). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.\\n\\n**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.\\n\\n**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):\\n- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10\\n- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392\\n- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.\\n- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.\\n\\n## Story Spine (D072 — Universal Gap with Controlled Evidence)\\n\\n**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured information extraction is unclear. Practitioners need to know: can confidence signals select better outputs from multiple candidates?\\n\\n**Existing approaches & gaps**: Self-consistency (Wang et al. 2023) succeeds for discrete-answer reasoning. MBR decoding succeeds for MT. But structured IE outputs (entity sets, relation triples) present a fundamentally different challenge — and prior work conflates quality estimation with selection.\\n\\n**Our framing (D072 — from \\\"gap observation\\\" to \\\"proven universal limitation with controlled experiment\\\")**:\\n\\nWe systematically compare five confidence signals for IE and discover a **universal correlation-selection gap**, then prove its universality via controlled ablation:\\n1. **Conceptual clarification**: Four of five signals are instance-level by construction and cannot rank candidates — this is noted as a definitional property, not discovered empirically. The interesting question is whether the remaining strategies (logprob, MBR/consensus-proximity) can select.\\n2. **Core empirical finding**: Logprob — the only per-sample signal — fails due to intrinsic score compression (60% of instances have within-sample range < 0.05). Consensus-proximity/MBR also fails despite success in MT.\\n3. **Controlled falsification**: The leading hypothesis was that constrained decoding causes score compression. Free-form decoding ablation **falsifies** this: LP variance is virtually unchanged without grammar constraints (std ratio 0.97). Score compression is model/task intrinsic → the gap is a fundamental property of structured IE, not a regime artifact. This is proven by elimination, the strongest form of experimental evidence for a negative result.\\n4. **Path forward**: Breaking LP compression requires fundamentally different approaches (trained verifiers, multi-round refinement) — simply relaxing decoding constraints is insufficient (ablation). The non-tied subset (+2.9pp, p=0.01) confirms that LP selection works WHERE compression is absent, establishing a concrete counterfactual.\\n\\n*(Appendix observation: RE LP selection flips from -0.68pp to +1.69pp under free-form, but single seed + within bootstrap CI [-3.0, +4.2]pp → cannot rule out noise. NER direction opposite. Not a claim.)*\\n\\n**Headline**: \\\"We discover that confidence signals reliably predict output quality (AUROC 0.75) but universally fail to select better candidates in structured IE. A controlled free-form decoding ablation proves this gap is intrinsic to the task — not caused by constrained decoding — establishing a fundamental limitation of unsupervised confidence-based selection for structured prediction.\\\"\\n\\n**Title**: \\\"Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction\\\" (reverted from D071's \\\"under Constrained Decoding\\\" — ablation proves gap is NOT constrained-decoding-specific)\\n\\n## Anticipated Reviewer Concerns\\n\\n### R1: \\\"Only one NER dataset — generalization unclear\\\"\\n- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.\\n- **Priority**: P0\\n\\n### R2: \\\"Only one model family (Qwen3-8B)\\\"\\n- **Mitigation**: exp-007 (LLaMA-3.1-8B) shows model-agnostic effect\\n- **Priority**: P0\\n\\n### R3: \\\"FK is a strawman baseline — what about log-prob, USC, exact-match?\\\"\\n- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (EM+SJ+voting) >> log-prob >> FK. USC discussed in related work (LLM-as-judge, orthogonal approach).\\n- **Priority**: P0, RESOLVED — results decisive\\n\\n### R3b: \\\"EM beats voting_conf and SJ on AUROC — why present SJ/voting_conf?\\\"\\n- **Mitigation**: EM is a strict binary signal (all-or-nothing match); SJ captures partial agreement and generalizes to arbitrary structured outputs (relations, events). Voting_conf provides granular entity-level scores. NER full AUROC: EM 0.749 > SJ 0.692 > voting_conf 0.684, but ρ: voting_conf 0.379 > SJ 0.360 > EM 0.295. EM excels at binary discrimination but underperforms on rank ordering. SJ is also more temperature-robust (Δρ=±0.01). Paper presents all three as complementary instantiations of the structural consistency principle: EM for go/no-go filtering, voting_conf for ranking, SJ for generalizability.\\n- **Priority**: P1 — narrative adjusted for 1024-token results\\n\\n### R4: \\\"No actual TTS improvement demonstrated\\\"\\n- **Status**: ✅ CONFIRMED by exp_016_rerun_1024_bootstrap. No signal significantly outperforms greedy on either task. NER logprob +0.6pp not significant (bootstrap p=0.39, 95% CI [−0.030, +0.042], Cohen's d=0.038). RE: greedy > all signals.\\n- **Mitigation**: Paper PIVOTS to \\\"confidence estimation + correlation-selection gap analysis.\\\" exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.\\n- **Priority**: P0 — narrative pivot complete, bootstrap confirms\\n\\n### R5: \\\"Sample size N=8 may be too small for reliable SJ estimation\\\"\\n- **Mitigation**: exp-001 (N=16) with multi-seed robustness\\n- **Priority**: P0\\n\\n### R6: \\\"Conditional analysis cherry-picks favorable instances\\\"\\n- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.\\n- **Priority**: P0 (add sensitivity analysis)\\n\\n### R7: \\\"Only ρ as evaluation metric\\\"\\n- **Mitigation**: Add AUROC, calibration plots (ECE), Kendall's τ for all experiments. ECE data now available: NER best calibrated = EM (0.353), RE best = voting (0.272). Logprob worst calibrated (NER 0.706, RE 0.769).\\n- **Priority**: P0\\n\\n### R8: \\\"Formula-implementation discrepancy\\\"\\n- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)\\n- **Priority**: P0, paper writing fix\\n\\n### R9: \\\"Evaluation circularity (T>0 consistency vs T=0 F1)\\\"\\n- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).\\n- **Priority**: P0\\n\\n### R10: \\\"Insufficient related work\\\" (三档一致 [B][M][W])\\n- **Mitigation**: Expand to 35+ references. Must cite:\\n  - USC (Chen 2024) — empirical differentiation, not just citation\\n  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)\\n  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021\\n  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020\\n  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016\\n  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023\\n  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024\\n  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022\\n  - **IE confidence**: Culotta & McCallum 2004\\n  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)\\n  - **[2025-2026 新颖性自查补充 — 必引]**:\\n    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出\\n    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap\\n    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案\\n    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量\\n    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction\\\"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承\\\"overlooks semantically consistent outputs\\\"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机\\n  - **[2025-2026 新颖性自查补充 — 应引]**:\\n    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述\\n    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述\\n    - Semantic Entropy Probes (2024) — 低成本不确定性估计\\n    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性\\n    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务\\n    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关\\n    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位\\n    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE\\n    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE\\n  - **需新增 Related Work 小节**:\\n    - \\\"Test-Time Scaling & Sample Selection\\\" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap\\n    - \\\"Consistency for Structured IE\\\" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation\\n- **Priority**: P0, Paper Agent handles\\n\\n### R11: \\\"SJ+logprob ensemble missing\\\" (Dream 2 — both reviewers)\\n- **Status**: ⚠️ REVISED by exp_016_rerun_1024. Results:\\n  - Ensemble AUROC (5-fold CV LR): NER 0.666 ± 0.070, RE 0.662 ± 0.078\\n  - Best single signal EM: NER AUROC 0.749, RE AUROC 0.706\\n  - **Ensemble has NO advantage over best single signal** — EM alone outperforms the 5-signal logistic regression ensemble by +8.3pp (NER) and +4.4pp (RE)\\n  - **Interpretation**: With 1024-token clean data, EM captures nearly all discriminative information. The ensemble's inferior performance likely reflects overfitting in the 5-fold CV LR with correlated features. This further supports presenting EM as a simple, strong baseline within the structural consistency family.\\n- **Priority**: DONE — write into paper with honest interpretation (no ensemble advantage claim)\\n\\n### R12: \\\"No supervised upper bound / reward model comparison\\\" (Dream 2)\\n- **Mitigation**: exp-016 LR ensemble (5-signal, 5-fold CV) underperforms best single signal EM (AUROC 0.666 vs 0.749), suggesting feature redundancy. exp-019 supervised verifier SKIPPED (DDL risk + scope creep). Free-form ablation provides the \\\"so what\\\": gap is fundamental → closing it requires fundamentally different approaches (trained verifiers, not just better unsupervised signals). Positioned as future work with explicit motivation from ablation evidence.\\n- **Priority**: P1, addressed via framing (future work motivated by ablation)\\n\\n### R13: \\\"Headroom capture rate low\\\" (Dream 2)\\n- **Mitigation**: NER oracle 0.7758, greedy 0.6439, best signal (logprob) 0.6501 → captures 0.5% of headroom. RE oracle 0.5850, greedy 0.4042, best signal (greedy itself) → 0% capture. Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline and documents the gap.\\n- **Priority**: P0, paper writing\\n\\n### R14: \\\"Cross-model validation thin — need more than 2×8B\\\" (Dream 2)\\n- **Mitigation**: exp-017 (LLaMA on CoNLL, P1). 70B model infeasible within GPU budget. Acknowledge as limitation.\\n- **Priority**: P1\\n\\n### R15: \\\"Log-prob definition ambiguity — Eq.1 vs best-of-N ranking\\\" (Dream 2 cross-tier, [W])\\n- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state \\\"all best-of-N require N forward passes; log-prob adds zero ranking overhead.\\\"\\n- **Priority**: P0, Paper Agent handles\\n\\n### R16: \\\"Zero figures — data-rich paper with only tables\\\" (Dream 2 cross-tier, [W])\\n- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.\\n- **Priority**: P0, Paper Agent handles\\n\\n### R17: \\\"Diagnostic framework overclaimed — descriptive not prescriptive\\\" (Dream 2 cross-tier, [M][W])\\n- **Mitigation**: Soften \\\"diagnostic framework\\\" to \\\"diagnostic analysis\\\" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.\\n- **Priority**: P0, Paper Agent handles\\n\\n### R18: \\\"No discussion of when consistency WOULD help\\\" (Dream 2 cross-tier, [W])\\n- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.\\n- **Priority**: P1, Paper Agent handles\\n\\n### R19: \\\"Negative result partially predictable for fine-tuned models\\\" (Dream 2 cross-tier, [W])\\n- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.\\n- **Priority**: P1, Paper Agent handles\\n\\n## Venue Fit\\n\\nEMNLP is well-suited for:\\n- Systematic empirical comparison of confidence signals for structured prediction\\n- Diagnostic findings with principled explanations\\n- The \\\"comparison + boundary condition\\\" contribution pattern\\n\\nRisk assessment (post-1024-token correction + bootstrap):\\n- **Structural risks (三档一致)**: (1) novelty perceived as incremental, (2) related work thin, (3) single RE dataset. These are presentation/positioning issues, NOT data issues — fixable by Paper Agent.\\n- **Data-dependent risks**: The bootstrap test strengthened the correlation-selection gap narrative definitively — NER logprob +0.6pp is confirmed noise (p=0.39), making the \\\"Weak Selectors\\\" claim statistically rigorous rather than directional.\\n- **Confirmed strength**: Structural consistency family (EM/voting/SJ) >> logprob on quality estimation (AUROC 0.75 vs 0.58). Correlation-selection gap is now statistically confirmed with bootstrap CI.\\n- **Critical path**: Paper Agent (related work 35+ refs, 3+ figures, contribution reframe) > new GPU experiments.\", \"total_chars\": 21854, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db577016-5819-4a72-bb58-9e1a772c554a",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "f9cebdcb-884d-49a2-b24e-cc8ff75d1d73",
  "sourceToolAssistantUUID": "db577016-5819-4a72-bb58-9e1a772c554a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T10:24:49.294Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UetpDaCDDf3ZCJcvfaSgtx`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9cebdcb-884d-49a2-b24e-cc8ff75d1d73",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C5wgVg7GMiexbLLS98",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "219d954e-fd87-4a14-9373-201867d68b0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KVHAu3RAVcaFDRsuujvBy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17926,
      "cache_read_input_tokens": 16882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17926,
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

_source line 17 · 2026-05-15T10:24:49.311Z_

<details><summary>↩ Tool result · `toolu_01UetpDaCDDf3ZCJcvfaSgtx`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "219d954e-fd87-4a14-9373-201867d68b0e",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "64f57734-8862-4b1d-a5ac-b1ee469a7418",
  "sourceToolAssistantUUID": "219d954e-fd87-4a14-9373-201867d68b0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T10:24:49.592Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015oGa6vayorxFiQ9BmAdKqK`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64f57734-8862-4b1d-a5ac-b1ee469a7418",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C5wgVg7GMiexbLLS98",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24e93cff-5f2e-4a6b-af10-31b306a0a00d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KVHAu3RAVcaFDRsuujvBy7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17926,
      "cache_read_input_tokens": 16882,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17926
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 16882,
          "cache_creation_input_tokens": 17926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17926,
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

_source line 19 · 2026-05-15T10:24:49.607Z_

<details><summary>↩ Tool result · `toolu_015oGa6vayorxFiQ9BmAdKqK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- run_mvp_pilot.py 支持 --collect_logprobs, --num_test (默认已改为 9999)\\n\\n## 数据修正链 (D054-D060) 关键教训\\n- exp_012 是唯一使用 max_tokens=512 的实验，导致 voting_conf ρ 虚高 (0.502→0.379)\\n- SJ/FK 对 max_tokens 参数鲁棒（Δ<0.004），但 voting_conf 极度敏感\\n- 修正后 AUROC 排名反转：EM (0.749) > SJ (0.692) > Voting (0.684)\\n- Selection claim 由 bootstrap 确认为 null result（p=0.39），不能写 \\\"significantly outperforms\\\"\\n- 论文数据必须来自 _rerun_1024 或本身就用 1024 的实验\\n\\n## D066 LLaMA fresh rerun (2026-05-15)\\n- D066 决策：LLaMA 3-seed 全部使用 fresh rerun 数据（seed42_r1024 + seed123 + seed456_r1024）\\n- exp_018_llama_scierc_seed456（旧 exp_007 复制品）已标记 SUPERSEDED\\n- LLaMA NER SJ ρ 修正：旧 0.362±0.004 → 新 0.325±0.021（σ 增大 5× 是真实 seed 变异，seed123 拉高均值）\\n- **分析脚本与 report.json 的 EM/VC 值存在系统性差异**（如 seed42 VC: 脚本 0.373 vs report.json 0.405）。Reviewer 要求论文统一使用分析脚本输出（与 Qwen 同一套）。不要从 registry metrics（来自 report.json）直接引用 EM/VC 到论文。\\n- NER 信号排名 6/6 完全稳定：VC > SJ > EM > FK > LP\\n- Core claim \\\"structural > logprob\\\" NER 全部成立 (12/12)；RE 仅 VC 稳定胜 LP\\n\\n## Registry 清理备注 (2026-05-15)\\n- 9 个 PREPARING+killed 实验因状态机限制无法推进到 DONE，实质已废弃\\n- 包括：exp_017_llama_conll_n16_s456_r1024, exp_017_llama_conll_n16_r1024, exp_001_n16_seed123_full, exp_001_n16_seed456_full, exp001_seed123, exp001_seed456, exp_007_ner_llama, exp_002_merge_conll2003, exp008_re_n16\\n\", \"total_chars\": 1740, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24e93cff-5f2e-4a6b-af10-31b306a0a00d",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "135c6de6-4844-48ae-bec8-9e512b9341e4",
  "sourceToolAssistantUUID": "24e93cff-5f2e-4a6b-af10-31b306a0a00d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-15T10:24:53.068Z_

Now let me read the paper's key writing plan and any LaTeX artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "135c6de6-4844-48ae-bec8-9e512b9341e4",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C6PXkgMygUpn1whbBh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64bef781-cb38-4252-8284-03b6f7d84796",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AtXj8w5wKthGirrhmTF672",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9159,
      "cache_read_input_tokens": 34808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9159,
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

_source line 21 · 2026-05-15T10:24:54.038Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019wWzPBDijS2BcGAqs9ZMdG`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64bef781-cb38-4252-8284-03b6f7d84796",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C6PXkgMygUpn1whbBh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9085cc3c-e4c5-4781-90e2-ec446917c12b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AtXj8w5wKthGirrhmTF672",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9159,
      "cache_read_input_tokens": 34808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9159,
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

_source line 22 · 2026-05-15T10:24:54.079Z_

<details><summary>↩ Tool result · `toolu_019wWzPBDijS2BcGAqs9ZMdG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026 Main (via ARR May)\\n  track: main\\n  template: null  # ARR/ACL format — need to download acl2023.sty or latest ARR template\\n  template_note: \\\"No local template found. Worker should download latest ARR LaTeX template from ACL Rolling Review.\\\"\\n  page_limit: 8  # + unlimited references\\n  deadline: 2026-05-25\\n  core_claim: >\\n    Structural consistency signals are the strongest unsupervised quality estimators for LLM-based IE —\\n    entity voting leads ρ (0.38) while EM leads AUROC (0.75), with soft Jaccard as complementary robust signal\\n    (temperature-stable: NER Δρ=0.028; conditional filtering ρ=0.31). A correlation-selection gap means\\n    this does not translate to best-of-N selection — no signal reliably surpasses greedy on either task\\n    (p>0.39, bootstrap). Signal effectiveness is task-difficulty-dependent: easy tasks favor exact-match,\\n    hard tasks favor structural consistency, and SJ strength scales with both sample size (N=8→16 ρ +0.052)\\n    and instance complexity (entity count 6+ ρ=0.55). RE reveals a capability boundary: when compound\\n    error propagation dominates (~44% zero-F1), all signals weaken (ρ=0.134-0.350) — conditional filtering restores\\n    structural signal advantage (SJ ρ=0.31) while logprob collapses (ρ=-0.03).\\n  created_at: 2026-05-14T13:00:00Z\\n  selected_title: \\\"Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\\\"\\n  director_approval: \\\"2026-05-14 approved with modifications: title #2 selected, RE must distinguish joint vs RE-only protocol (D023), 3 tables confirmed (tab_robustness kept), exp_003/exp_007 pending — Director will notify for Patch\\\"\\n  re_protocol_note: \\\"D023: Joint RE SJ ρ=0.267 < FK ρ=0.315; RE-only SJ ρ=0.304 > FK ρ=0.269. Table 1 must label protocol. Discussion must address joint error propagation.\\\"\\n  d024_re_data_update: >\\n    D024 (2026-05-14): 3-seed N=16 T=1.0 confirms RE full set SJ NOT superior to FK.\\n    FORBIDDEN: claim \\\"SJ consistently outperforms FK across all tasks\\\".\\n    Correct narrative: NER SJ robust > FK; RE full set all signals weak + indistinguishable (~44% zero-F1);\\n    RE conditional set SJ recovers advantage (Δ=0.15-0.21 over FK) and logprob near-zero.\\n    Table 1 must include both full and conditional RE rows.\\n    Conditional analysis = unique contribution, emphasize in Discussion.\\n  d035_narrative_update: >\\n    D035 (2026-05-14): Heatmap data source unified to exp_015. NER full: voting ρ=0.502 (was 0.392),\\n    SJ ρ=0.357 (was 0.383). Voting significantly leads SJ (NER +0.145), NOT \\\"statistically equivalent\\\".\\n    FORBIDDEN: \\\"SJ ≈ voting\\\". Correct: same family, complementary — voting strongest per-instance,\\n    SJ more robust cross-condition. SJ unique value: (a) temperature numerically stable (RE Δρ=0.010, NER Δρ=0.014; bootstrap CI includes 0, not statistically significant),\\n    (b) generalizes to any structured output not limited to entity, (c) conditional filtering ρ=0.412,\\n    (d) ensemble with voting AUROC 0.735 complementary.\\n    exp_009 findings (Claim 3): SJ high entity count (6+) ρ=0.547, low (1-2) ρ=0.415;\\n    SJ >> logprob advantage stable across all sentence length quartiles (Δρ≈0.08-0.20);\\n    two proxies (entity count, sentence length) weakly correlated with F1 (|r|<0.15, measuring input complexity not output quality) but moderately correlated with each other (ρ=0.650, overlapping dimensions). CORRECTED 2026-05-14: was \\\"three independent proxies\\\" — proxy-proxy correlation is NOT weak; only proxy-F1 correlation is weak.\\n  d037_n16_re_refinement: >\\n    D037 (2026-05-14): N=16 NER (exp_001_seed42_v2/seed123_v2): SJ ρ=0.428/0.424, cross-seed Δ<0.01.\\n    N=8→16 SJ +0.071, FK +0.016 — SJ scaling gain >> FK. RE N=16 (exp_008_re_n16_v2):\\n    full logprob ρ=0.287 > SJ 0.281 ≈ FK 0.279 (all ~flat, compound error ceiling).\\n    RE cond: SJ ρ=0.308 vs logprob ρ=-0.026 (p=0.685, logprob completely fails).\\n    FORBIDDEN: \\\"structural signals universally outperform logprob\\\" — only true within model capability range.\\n    Unified framework: structural signals strongest within model capability range; beyond it, all signals converge.\\n    RE 44% zero-F1 must be noted as limitation in paper.\\n  d038_temperature_precision: >\\n    D038 (2026-05-14): Temperature robustness must distinguish NER vs RE.\\n    SJ NER Δρ=0.014 (MODERATE), SJ RE Δρ=0.010 (ROBUST). FORBIDDEN: generic \\\"SJ Δρ≤0.01\\\".\\n    FK NER Δρ=0.06, RE Δρ=0.097 — FK temperature sensitivity confirmed.\\n    Bootstrap 95% CI all include 0 → NOT statistically significant.\\n    FORBIDDEN: \\\"significantly\\\" for temperature differences → use \\\"numerically small\\\".\\n    \\\"Conditional filtering >> temperature tuning\\\" scope excludes logprob (no T=0.7 logprob data),\\n    paper must note this limitation.\\n  d049_n8_vs_n16_labeling: >\\n    D049 (2026-05-14): SciERC uses N=16, CoNLL uses N=8. Tables MUST annotate N per row.\\n    Limitations must discuss N's impact on consistency estimation stability.\\n    No N=16 CoNLL experiment (cost unjustified). Table format: include N column or footnote.\\n  d050_conll_headroom_honesty: >\\n    D050 (2026-05-14): CoNLL oracle headroom only +1.77pp (greedy 0.927 → oracle 0.944).\\n    FORBIDDEN: claim \\\"improves F1\\\" for CoNLL. Correct framing by scenario:\\n    (a) High-performance (CoNLL): quality estimation = reliability assurance (confirming output quality)\\n    (b) Challenging (SciERC): quality estimation = filtering unreliable instances + selective prediction.\\n    This further supports Claim 2 (correlation-selection gap): small headroom → selection meaningless.\\n    Discussion must distinguish these two use cases explicitly.\\n  d051_rho_auroc_separation: >\\n    D051 (2026-05-14): exp_017 shows logprob has lowest ρ but highest AUROC; structural signals reverse.\\n    Interpretation: logprob better for binary filtering (good/bad threshold), structural signals better\\n    for rank-ordering (continuous quality prediction). Discussion should present this as methodological\\n    contribution — different signals suit different downstream decision scenarios.\\n    This enriches the \\\"strong predictors, weak selectors\\\" narrative with granularity.\\n  d052_auroc_data_source_correction: >\\n    D052 (2026-05-14): CRITICAL — Table 1 SciERC NER AUROC was sourced from exp_015_metrics_expansion\\n    (single seed 42), but ρ values were from exp_015_v2 (multi-seed). Corrected NER AUROC to exp_015_v2:\\n    Voting .728→.741, SJ .666→.715, FK .624→.629, EM .623→.757, Logprob .559→.581.\\n    EM AUROC jumps from 5th to 1st on SciERC NER (.757 > Voting .741). Bold migrated accordingly.\\n    Cascade: abstract/intro/conclusion \\\"AUROC 0.73\\\" → \\\"0.74\\\" (Voting .741 rounds to .74).\\n    RE AUROC flagged for same cross-validation — current values match exp_015_metrics_expansion,\\n    not exp_015_v2. Director decision pending on RE correction.\\n    AUTHORITATIVE SOURCE: exp_015_v2 for all SciERC AUROC values going forward.\\n  d045_wnut17_boundary: >\\n    D045 (2026-05-14): WNUT-17 NER (Qwen, N=16, T=1.0): SJ ρ=0.062 (p=0.106, NOT significant),\\n    54% F1=0, logprob ρ=-0.411. Serves as Claim 3 capability boundary cross-domain evidence.\\n    Consistent with RE 44% zero-F1 pattern: model capability insufficient → all signals fail.\\n    Logprob strong negative correlation worth discussing (possible calibration issue).\\n    Writing: use as boundary evidence in method_boundary + Limitations.\\n  d046_3seed_ner: >\\n    D046 (2026-05-14): SciERC NER (Qwen, N=16, 3 seeds): seed42=0.428, seed123=0.424, seed456=0.384.\\n    Mean ρ=0.412±0.025, all 3 seeds structural>surface. Paper reports mean±std.\\n    Table 1/tab_robustness should use mean±std for N=16 NER SJ.\\n  d047_llama_conll: >\\n    D047 (2026-05-14): exp_017 LLaMA-3.1-8B CoNLL NER (N=8, T=1.0):\\n    SJ ρ=0.431, FK ρ=0.428, logprob ρ=0.307, greedy_f1=0.927, oracle_f1=0.944, headroom=0.018.\\n    structural_beats_surface=true. SJ ρ vs Qwen CoNLL (0.436): Δ=0.005 — strongest model-agnostic evidence.\\n    WRITING CONSTRAINTS: (a) CoNLL oracle headroom only 0.018 (LLaMA)/0.032 (Qwen) → focus on\\n    correlation/discrimination (ρ, AUROC), NOT claim selection improvement on CoNLL.\\n    (b) SJ vs FK advantage on CoNLL only 0.004 (vs SciERC +0.10~0.16) → Discussion must note\\n    schema complexity effect: CoNLL 4 entity types, clear annotation → SJ soft matching advantage minimal.\\n    SJ advantage scales with schema complexity (SciERC 6 types > CoNLL 4 types).\\n    Table 1 gets new row: CoNLL NER (LLaMA).\\n  d048_cross_config_panorama: >\\n    D048 (2026-05-14): Cross-config panorama summary:\\n    NER 4/4 configurations pass (structural>surface): SciERC NER Qwen N=16 3-seed 0.412±0.025,\\n    CoNLL NER Qwen N=8 0.436, CoNLL NER LLaMA N=8 0.431, SciERC NER LLaMA N=8 0.363.\\n    RE and WNUT-17 are honest limitations (RE: compound error, WNUT-17: model capability).\\n    Consider Supplementary panorama table or merge into Table 1.\\n  title_candidates:\\n    - \\\"The Correlation-Selection Gap: Structural Consistency Predicts Quality but Fails at Selection in LLM-based Information Extraction\\\"\\n    - \\\"Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\\\"\\n    - \\\"When Consistency Predicts Quality but Not Selection: Confidence Signals for Structured Prediction with LLMs\\\"\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 200\\n    core_bullets:\\n      - \\\"Problem: LLM multi-sample generation for IE lacks guidance on which confidence signals to trust, and for what purpose\\\"\\n      - \\\"Approach: Systematic comparison of 5 confidence signals across 4 families on NER and RE\\\"\\n      - \\\"Finding 1: Entity voting achieves ρ=0.50 and AUROC 0.73, leading all signals for quality estimation (logprob ρ=0.14); soft Jaccard complements with cross-condition robustness (numerically small temperature sensitivity: NER Δρ=0.014, RE Δρ=0.010)\\\"\\n      - \\\"Finding 2: Correlation-selection gap — despite strong ρ up to 0.50, no signal beats greedy for NER best-of-N; only logprob helps RE (+2.4pp)\\\"\\n      - \\\"Finding 3: Signal ranking is task-difficulty-dependent — EM > SJ on easy tasks, SJ > EM on hard tasks\\\"\\n    dependencies: [experiments, method, introduction]\\n    registry_refs: [mvp_pilot_004, exp_012_logprob_baseline, exp_014_entity_majority_voting, exp_015_metrics_expansion, exp_016_signal_ensemble, exp_002, exp_009_capability_stratification]\\n\\n  - section: introduction\\n    word_budget: 1200\\n    core_bullets:\\n      - \\\"Hook: Self-consistency voting has shown remarkable gains for reasoning tasks (+18pp on GSM8K). But structured prediction (IE) has internal dependencies that surface metrics cannot capture — does consistency still help?\\\"\\n      - \\\"Gap: Prior work conflates quality estimation (predicting which outputs are reliable) with sample selection (choosing the best output). These are fundamentally different tasks requiring different signal properties.\\\"\\n      - \\\"Insight: Consistency signals are instance-level aggregates that predict input difficulty, NOT sample-level discriminators that identify the best output. This explains why high correlation (ρ up to 0.50) fails to enable selection.\\\"\\n      - \\\"Contributions: (C1) First systematic comparison of 5 confidence signals for quality estimation in generative IE; (C2) Identification of the correlation-selection gap; (C3) Task-complexity boundary — signal ranking depends on task difficulty\\\"\\n      - \\\"Contextualize negative result: non-obvious because self-consistency works for reasoning, and structural prediction has richer internal structure\\\"\\n    dependencies: [experiments]\\n    citation_hints:\\n      - \\\"Wang et al. 2023 (self-consistency)\\\"\\n      - \\\"Chen et al. 2024 (USC)\\\"\\n      - \\\"Snell et al. 2024 / Brown et al. 2024 (TTS scaling)\\\"\\n      - \\\"Nédellec & Xia 2026 (consistency for IE — cite their surface-matching limitation as SJ motivation)\\\"\\n    figures: [fig_overview]\\n\\n  - section: related_work\\n    word_budget: 1200\\n    structure_note: \\\"Restructured per Director R10. New subsections: 'Test-Time Scaling & Sample Selection' (CISC/Self-Certainty/ReASC/Atomic SC) + 'Consistency for Structured IE' (Nédellec & Xia 2026, CoCoA Vashurin 2025).\\\"\\n    core_bullets:\\n      - \\\"Opening: Position in landscape via surveys — Confidence Estimation Survey (Geng et al., NAACL 2024, arXiv 2311.08298) + Abstention Survey (Feng et al., TACL 2025) + UQ Survey (ACL Findings 2025) + UQ&CC Survey (arXiv 2503.15850). Our work bridges confidence estimation and selective prediction for structured outputs.\\\"\\n      - \\\"Cluster 1 — Self-consistency & LLM agreement: Wang 2023 (SC-CoT), USC Chen 2024, SelfCheckGPT Manakul 2023, Atomic SC (EMNLP 2024, sub-claim consistency for long-form text). Differentiation: all use exact-match or text-level comparison on discrete/text outputs; we use set-theoretic structural similarity on entity/relation sets.\\\"\\n      - \\\"NEW Cluster — Test-Time Scaling & Sample Selection (dedicated subsection): CISC (ACL Findings 2025, arXiv 2502.06233, confidence-weighted majority vote), Self-Certainty BoN (ICLR 2026, arXiv 2502.18581, KL-divergence selection), ReASC (arXiv 2601.02970, adaptive sampling), Ranked Voting SC (arXiv 2505.10772), Latent SC (arXiv 2508.18395). KEY FRAMING: ALL operate on reasoning/QA with discrete answer spaces. We are FIRST to (a) extend SC to set-valued structured outputs (IE), (b) discover correlation-selection gap: strong quality estimation ↛ selection ability. Self-Certainty BoN is direct academic dialogue: they demonstrate reward-free selection works for reasoning; we show it FAILS for structured IE NER.\\\"\\n      - \\\"NEW Cluster — Consistency for Structured IE (dedicated subsection): Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769) — most direct competitor: consistency-accuracy correlation in hard-prompted LLMs for NER/RE on plant-health data. KEY DIFFERENTIATION: (a) they use surface-level string matching, self-acknowledge limitation ('overlooks semantically consistent outputs') — our SJ directly addresses this; (b) no best-of-N selection study; (c) single-domain hard-prompted (T=0); (d) no multi-signal family comparison. CoCoA (Vashurin et al., NeurIPS 2025, arXiv 2502.04964) — MBR framework fusing confidence+consistency for UQ on QA/summarization/translation, parallels our exp-016 ensemble but not structured IE. Vashurin et al. (arXiv 2510.20460, 2025) — systematic evaluation of 4 UQ methods (VCE/MSP/SC/CoCoA), tasks exclude structured IE. FRAMING: Nédellec & Xia's surface-matching limitation motivates SJ; CoCoA's confidence+consistency fusion parallels our ensemble analysis; both confirm structured IE as underexplored.\\\"\\n      - \\\"Cluster 2 — Uncertainty estimation & calibration: Kuhn 2023 semantic uncertainty, Semantic Entropy Probes (arXiv 2406.15927), Kadavath 2022 P(True), Guo 2017, Desai & Durrett 2020 → we compare model confidence with output-space consistency\\\"\\n      - \\\"Cluster 3 — Conformal prediction: Fisch 2021, Angelopoulos 2021 → guarantees coverage, not ranking\\\"\\n      - \\\"Cluster 4 — Token/span-level uncertainty for NER: Xiao & Wang 2019, Shelmanov 2021, He 2020 → CRF/classifier uncertainty, we study generative LLM setting\\\"\\n      - \\\"Cluster 5 — Ensemble & MC-dropout: Lakshminarayanan 2017, Gal & Ghahramani 2016 → require model modification; our signals are post-hoc\\\"\\n      - \\\"Cluster 6 — Verifier/reward models: Cobbe 2021, Lightman 2023 → supervised; we study unsupervised signals\\\"\\n      - \\\"Cluster 7 — TTS scaling theory: Snell 2024, Brown 2024 → we provide empirical evidence for IE\\\"\\n      - \\\"Cluster 8 — IE confidence & selective prediction: Culotta & McCallum 2004, Geifman & El-Yaniv 2017, Jagannatha & Yu 2022 → pre-LLM approaches\\\"\\n    required_refs:\\n      must_cite:\\n        - key: \\\"cisc_2025\\\"\\n          title: \\\"Confidence Improves Self-Consistency in LLMs\\\"\\n          venue: \\\"ACL Findings 2025\\\"\\n          arxiv: \\\"2502.06233\\\"\\n          differentiation: \\\"Confidence-weighted majority vote for reasoning. We use structural similarity for set-structured IE.\\\"\\n        - key: \\\"self_certainty_bon_2026\\\"\\n          title: \\\"Scalable Best-of-N Selection for LLMs via Self-Certainty\\\"\\n          venue: \\\"ICLR 2026\\\"\\n          arxiv: \\\"2502.18581\\\"\\n          differentiation: \\\"KL-divergence selection for reasoning. DIRECT DIALOGUE: we find correlation-selection gap blocks selection for structured IE NER.\\\"\\n        - key: \\\"reasc_2026\\\"\\n          title: \\\"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling\\\"\\n          arxiv: \\\"2601.02970\\\"\\n          differentiation: \\\"Adaptive sampling for reasoning. Still limited to discrete answers.\\\"\\n        - key: \\\"atomic_sc_2024\\\"\\n          title: \\\"Atomic Self-Consistency\\\"\\n          venue: \\\"EMNLP 2024\\\"\\n          url: \\\"aclanthology.org/2024.emnlp-main.706\\\"\\n          differentiation: \\\"Sub-claim consistency for long-form text. We measure entity-set level structural similarity.\\\"\\n        - key: \\\"nedellec_xia_2026\\\"\\n          title: \\\"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\\\"\\n          venue: \\\"Genomics Informatics, 2026-02\\\"\\n          pmc: \\\"PMC12888769\\\"\\n          differentiation: \\\"Most direct competitor. Surface-level string matching for consistency-accuracy on NER/RE. Self-acknowledges 'overlooks semantically consistent outputs' — our SJ addresses this. No selection study, single domain, hard-prompted only.\\\"\\n      should_cite:\\n        - key: \\\"uq_survey_acl2025\\\"\\n          title: \\\"A Survey of Uncertainty Estimation Methods on LLMs\\\"\\n          venue: \\\"ACL Findings 2025\\\"\\n        - key: \\\"uqcc_survey_2025\\\"\\n          title: \\\"Uncertainty Quantification and Confidence Calibration in LLMs: A Survey\\\"\\n          arxiv: \\\"2503.15850\\\"\\n        - key: \\\"semantic_entropy_probes_2024\\\"\\n          title: \\\"Semantic Entropy Probes\\\"\\n          arxiv: \\\"2406.15927\\\"\\n        - key: \\\"latent_sc_2025\\\"\\n          title: \\\"Latent Self-Consistency\\\"\\n          arxiv: \\\"2508.18395\\\"\\n        - key: \\\"ranked_voting_sc_2025\\\"\\n          title: \\\"Ranked Voting based Self-Consistency of LLMs\\\"\\n          arxiv: \\\"2505.10772\\\"\\n        - key: \\\"confidence_survey_2024\\\"\\n          title: \\\"A Survey of Confidence Estimation and Calibration in LLMs\\\"\\n          venue: \\\"NAACL 2024\\\"\\n          arxiv: \\\"2311.08298\\\"\\n        - key: \\\"abstention_survey_2025\\\"\\n          title: \\\"Know Your Limits: A Survey of Abstention in LLMs\\\"\\n          venue: \\\"TACL 2025\\\"\\n        - key: \\\"cocoa_vashurin_2025\\\"\\n          title: \\\"CoCoA: Combining Confidence and Consistency for LLM Uncertainty Quantification\\\"\\n          venue: \\\"NeurIPS 2025\\\"\\n          arxiv: \\\"2502.04964\\\"\\n          differentiation: \\\"MBR framework fusing confidence+consistency. Parallels our exp-016 ensemble (SJ+logprob) but not structured IE.\\\"\\n        - key: \\\"vashurin_uq_eval_2025\\\"\\n          title: \\\"Systematic Evaluation of UQ Methods for LLMs\\\"\\n          arxiv: \\\"2510.20460\\\"\\n          differentiation: \\\"VCE/MSP/SC/CoCoA four-method evaluation. Tasks exclude structured IE — our work fills this gap.\\\"\\n    verification_status: \\\"pending — Director says need WebSearch verification for bib accuracy\\\"\\n    dependencies: [introduction]\\n\\n  - section: method\\n    word_budget: 1000\\n    core_bullets:\\n      - \\\"Problem formulation: given LLM M, input x, N stochastic samples {y_1,...,y_N}, define confidence signal c(x, {y_i}) → ℝ\\\"\\n      - \\\"Signal 1 — Log-probability: c_lp(y_i) = (1/|y_i|) Σ log p(t_j|t_{&lt;j}, x). Per-sample signal. Clarify: sequence-level mean, not token-level max.\\\"\\n      - \\\"Signal 2 — Exact-match voting: c_em(x) = max_y |{i: y_i = y}| / N. Instance-level.\\\"\\n      - \\\"Signal 3 — Fleiss' Kappa (FK): token-level inter-rater agreement. Instance-level.\\\"\\n      - \\\"Signal 4 — Soft Jaccard (SJ): set-aware structural similarity via type-grouped bipartite matching. Instance-level. Key: uses Hungarian matching with max(|A|,|B|) normalization.\\\"\\n      - \\\"Signal 5 — Entity voting confidence: per-entity majority voting rate, averaged. Instance-level.\\\"\\n      - \\\"Distinction: log-prob is PER-SAMPLE (ranks candidates), others are INSTANCE-LEVEL (aggregate across samples). This distinction is central to the correlation-selection gap.\\\"\\n      - \\\"Evaluation: quality estimation (ρ, τ, AUROC vs F1) and sample selection (best-of-N F1)\\\"\\n    dependencies: []\\n    notation_table:\\n      M: \\\"language model\\\"\\n      x: \\\"input instance\\\"\\n      y_i: \\\"i-th stochastic sample\\\"\\n      N: \\\"number of samples\\\"\\n      c: \\\"confidence signal\\\"\\n      SJ: \\\"soft Jaccard similarity\\\"\\n      FK: \\\"Fleiss' Kappa\\\"\\n      EM: \\\"exact-match voting rate\\\"\\n\\n  - section: experiments\\n    word_budget: 2400\\n    subsections:\\n      - name: setup\\n        word_budget: 500\\n        core_bullets:\\n          - \\\"Datasets: SciERC (science, 551 test, NER+RE joint), CoNLL-2003 (news, 3453 test, NER), WNUT-17 (social media, NER — method boundary analysis)\\\"\\n          - \\\"Model: Qwen3-8B fine-tuned with LoRA (r=32) per dataset. LLaMA-3.1-8B-Instruct for cross-model validation (exp_007 SciERC, exp_017 CoNLL).\\\"\\n          - \\\"Sampling: N=8 primary, N=16 for scaling analysis. T=1.0 standard, T=0.7 for robustness.\\\"\\n          - \\\"Evaluation: greedy F1 as reference, per-instance F1 vs each signal's ρ/τ/AUROC, best-of-N selection F1\\\"\\n          - \\\"Implementation: vLLM inference, XGrammar constrained decoding, span realignment post-processing\\\"\\n\\n      - name: quality_estimation\\n        word_budget: 600\\n        core_bullets:\\n          - \\\"Table 1: All 5 signals × {SciERC NER, SciERC RE, CoNLL NER} × {ρ, τ, AUROC}\\\"\\n          - \\\"SciERC NER (exp_015 unified): voting 0.728 > SJ 0.666 >> FK 0.624 ≈ EM 0.623 >> logprob 0.559 (AUROC). ρ: voting 0.502 >> SJ 0.357 > FK 0.265 ≈ EM 0.257 >> logprob 0.140\\\"\\n          - \\\"CoNLL NER (Qwen): EM 0.816 > SJ 0.801 > EV 0.789 > FK 0.774 > logprob 0.753 — EM > SJ on easy task!\\\"\\n          - \\\"CoNLL NER (LLaMA, exp_017): SJ ρ=0.431, FK ρ=0.428, logprob ρ=0.307. SJ ρ vs Qwen 0.436 (Δ=0.005) — strongest model-agnostic evidence. SJ-FK gap only 0.004 (vs SciERC ~0.10) — schema complexity effect.\\\"\\n          - \\\"SciERC RE (exp_015 unified): voting 0.716 > logprob 0.635 ≈ FK 0.631 > SJ 0.582 > EM 0.504 — degraded (AUROC). ρ: voting 0.422 > FK 0.253 ≈ logprob 0.247 > SJ 0.211 > EM 0.100\\\"\\n          - \\\"Key: voting is NER strongest single signal (ρ=0.502); within consistency family voting >> SJ per-instance but SJ offers unique cross-condition robustness (temp Δρ numerically small: NER 0.014, RE 0.010; cond ρ=0.412). EM dominates on easy tasks (CoNLL). D035: FORBIDDEN 'SJ ≈ voting'.\\\"\\n        registry_refs: [mvp_pilot_004, exp_012_logprob_baseline, exp_013_exact_match_voting, exp_014_entity_majority_voting, exp_015_metrics_expansion, exp_002, exp_017_llama_conll_infer]\\n        tables: [tab_quality_estimation]\\n\\n      - name: correlation_selection_gap\\n        word_budget: 600\\n        core_bullets:\\n          - \\\"Table 2: Best-of-N selection F1 for each signal vs greedy vs oracle\\\"\\n          - \\\"NER: greedy 0.609 ≥ ALL signals (logprob 0.609, SJ 0.604, voting 0.596). Oracle 0.769 (+16pp headroom)\\\"\\n          - \\\"RE: logprob 0.397 > greedy 0.374 (+2.4pp). SJ 0.368, voting 0.338 ≈ random. Oracle 0.561 (+18.7pp)\\\"\\n          - \\\"CoNLL: voting 0.914 > greedy 0.912 (+0.18pp) — first instance where voting beats greedy, on easy task\\\"\\n          - \\\"Explanation: instance-level signals predict WHICH INPUTS are reliable, not WHICH OUTPUTS are best. Only per-sample logprob can rank candidates.\\\"\\n          - \\\"Ensemble analysis: SJ+voting NER ρ=0.489 (+23%), AUROC 0.735 (+3.5pp). But ensemble SELECTION still fails.\\\"\\n        registry_refs: [exp_016_signal_ensemble, exp_002]\\n        tables: [tab_selection]\\n        figures: [fig_selection_gap]\\n\\n      - name: task_complexity\\n        word_budget: 400\\n        core_bullets:\\n          - \\\"Signal ranking shifts with task difficulty: CoNLL (easy, F1=0.91) EM>SJ; SciERC NER (hard, F1=0.66) SJ>EM; SciERC RE (harder) all signals converge to ~0.28 ρ — compound error ceiling. Unified framework: structural signals strongest within model capability range; beyond it all signals converge.\\\"\\n          - \\\"RE diagnostic: FEATURE-OF near-zero ρ, HYPONYM-OF ρ=0.65. Entity span errors = 55.5% of RE FN.\\\"\\n          - \\\"Fisher z-test: NER ρ_sj significantly > RE ρ_sj (p=0.021)\\\"\\n          - \\\"Compound error propagation: head_sj ρ=0.21 (vs NER 0.38) — fundamental, not formula issue\\\"\\n          - \\\"exp_009 capability stratification (Claim 3): SJ strength scales with entity count — 6+ entities ρ=0.547, 1-2 entities ρ=0.415. SJ >> logprob advantage stable across all sentence length quartiles (Δρ≈0.08-0.20). Two proxies (sent_len, ent_count) weakly correlated with F1 (|r|<0.15) but moderately correlated with each other (ρ=0.650); overlapping not independent dimensions. rel_count reserved for RE discussion (collinear with ent_count, ρ=0.769).\\\"\\n        registry_refs: [exp_004_re_diagnostic, e1_component_wise_re_sj, exp_002, exp_009_capability_stratification]\\n\\n      - name: analysis\\n        word_budget: 300\\n        core_bullets:\\n          - \\\"Temperature robustness: SJ numerically small sensitivity — NER Δρ=0.014 (moderate), RE Δρ=0.010 (robust); FK NER Δρ=0.06, RE Δρ=0.097 (high sensitivity). Bootstrap 95% CI all include 0 → differences not statistically significant → use 'numerically small' not 'significantly'. D038: logprob excluded from T comparison (no T=0.7 logprob data). Conditional filtering >> temperature tuning scope does NOT include logprob.\\\"\\n          - \\\"N-scaling: NER SJ improves N=8→16 (ρ 0.357→0.428, +0.071), FK only +0.016 — SJ scaling gain 4.4× FK. Cross-seed Δ<0.01 (0.428/0.424). RE N=16: logprob ρ=0.287 > SJ 0.281 ≈ FK 0.279 (all flat, compound error ceiling).\\\"\\n          - \\\"LOO-SJ: Δρ=-0.014, evaluation circularity minimal\\\"\\n          - \\\"Conditional filtering: NER cond SJ ρ=0.412, RE cond SJ ρ=0.368 (N=8) / 0.308 (N=16) vs logprob cond ρ=-0.026 (N=16, completely fails). Separating knowledge-gap errors critical — structural signals retain value, logprob collapses.\\\"\\n          - \\\"Cross-model: LLaMA-3.1-8B confirms SJ>FK on NER (SciERC ρ 0.363 vs 0.327; CoNLL ρ 0.431 vs 0.428). RE cond SJ recovers (0.405 vs 0.259). CoNLL cross-model Δ=0.005 strongest model-agnostic evidence. NER 4/4 configs pass structural>surface.\\\"\\n          - \\\"3-seed stability (D046): SciERC NER N=16 SJ ρ across 3 seeds: 0.428/0.424/0.384, mean=0.412±0.025. All seeds structural>surface.\\\"\\n        registry_refs: [exp_005, exp_001_ner_n16_scierc, exp_001_seed42_v2, exp_001_seed123_v2, exp_008_re_n16_v2, exp_015_metrics_expansion, exp_007_llama_inference, exp_017_llama_conll_infer]\\n        figures: [fig_signal_heatmap]\\n\\n      - name: method_boundary\\n        word_budget: 400\\n        core_bullets:\\n          - \\\"D029: WNUT-17 as method boundary analysis — When Does Structural Consistency Fail?\\\"\\n          - \\\"WNUT-17 (Qwen, N=16, T=1.0): SJ ρ=0.062 (p=0.106, NOT significant), 54% F1=0. Root cause: training data 63.8% empty instances (vs SciERC 0%), model learns strong empty-output prior. Logprob ρ=-0.411 (strong negative — possible calibration issue, discuss).\\\"\\n          - \\\"16/16 samples all empty → SJ=1.0 but F1=0, systematically inflates consistency for wrong predictions\\\"\\n          - \\\"Logprob also fails: empty predictions get logprob=-0.007 (extreme high confidence), ρ=-0.41 (anti-correlated)\\\"\\n          - \\\"Conditional filtering partially helps: post-filter logprob ρ=+0.35, but SJ remains weak\\\"\\n          - \\\"Conclusion: SJ effectiveness requires model to have basic task competence — degenerate training data (>50% empty) invalidates all unsupervised signals\\\"\\n          - \\\"This is NOT a dataset limitation but a method boundary: identifies preconditions for structural consistency\\\"\\n        registry_refs: [exp_003_wnut17_eval]\\n\\n    registry_refs: [mvp_pilot_004, mvp_pilot_005, exp_001_ner_n16_scierc, exp_001_seed42_v2, exp_001_seed123_v2, exp_008_re_n16_v2, exp_002, exp_004_re_diagnostic, exp_005, exp_012_logprob_baseline, exp_013_exact_match_voting, exp_014_entity_majority_voting, exp_015_metrics_expansion, exp_016_signal_ensemble, e1_component_wise_re_sj, exp_007_llama_inference, exp_003_wnut17_eval, exp_009_capability_stratification]\\n    tables: [tab_quality_estimation, tab_selection]\\n    figures: [fig_selection_gap, fig_signal_heatmap, fig_reliability]\\n\\n  - section: discussion\\n    word_budget: 500\\n    core_bullets:\\n      - \\\"When WOULD consistency help: (a) poor calibration (ICL without fine-tuning), (b) closed-source APIs (no logprob), (c) ensemble/mixture settings, (d) systematically overconfident models\\\"\\n      - \\\"Non-obviousness of negative result: self-consistency works for reasoning (+18pp GSM8K), structured prediction has rich internal structure, the DEGREE of gap and task-complexity boundary are not predictable a priori\\\"\\n      - \\\"Practical recommendations: quality estimation → voting (strongest per-instance) or SJ (when temperature-robustness/generalizability matters); best-of-N → logprob (RE only); NER → greedy is near-optimal\\\"\\n      - \\\"SJ unique positioning: same consistency family as voting but complementary — (a) temperature numerically stable (NER Δρ=0.014, RE Δρ=0.010; bootstrap CI includes 0), (b) generalizes to any structured output not limited to entity, (c) conditional filtering ρ=0.412 still strong, (d) with voting ensemble AUROC 0.735. Framing: 'voting stronger per-instance, SJ more robust cross-condition'. D038: FORBIDDEN 'significantly' for temperature — use 'numerically small'.\\\"\\n      - \\\"Conditional analysis as unique contribution: separating knowledge-gap errors (RE ~44% zero-F1, WNUT-17 ~64% empty) reveals hidden signal value — SJ recovers on RE cond (ρ=0.308 at N=16) while logprob collapses (ρ=-0.026)\\\"\\n      - \\\"Capability boundary framework: structural signals are strongest quality estimators within model capability range; beyond it (RE compound errors), all signals converge — but conditional filtering restores structural advantage\\\"\\n      - \\\"Limitations: 1 RE dataset (SciERC, 44% zero-F1 limits signal discrimination), 2 model families (Qwen3 + LLaMA), no supervised upper bound beyond logistic regression proxy. RE zero-F1 proportion must be explicitly noted. WNUT-17 confirms boundary but informal text domains (social media) remain unvalidated for positive results. CoNLL SJ-FK gap only 0.004 — SJ advantage may not generalize to simple schema datasets.\\\"\\n    dependencies: [experiments]\\n\\n  - section: conclusion\\n    word_budget: 300\\n    core_bullets:\\n      - \\\"Summary: first systematic comparison of confidence signals for quality estimation vs selection in generative IE\\\"\\n      - \\\"Three findings: (1) structural consistency best for quality estimation, (2) correlation-selection gap, (3) task-complexity boundary\\\"\\n      - \\\"Future work: supervised verifiers, cross-task transfer of confidence signals, conformal prediction integration, scaling to larger models\\\"\\n    dependencies: [experiments, discussion]\\n\\nvisualization_plan:\\n  - fig_id: fig_overview\\n    type: conceptual\\n    tool: matplotlib\\n    description: >\\n      Overview figure (1-column) illustrating the paper's core finding. Left: quality estimation\\n      (consistency signals predict which instances are reliable). Right: sample selection (the same\\n      signals fail to pick the best sample). Shows the conceptual distinction between instance-level\\n      and per-sample signals. Simple schematic with boxes and arrows — not a full architecture diagram.\\n    placement: introduction\\n    aspect_ratio: \\\"2:1\\\"\\n    data_source: \\\"manual\\\"\\n\\n  - fig_id: fig_selection_gap\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Two-panel figure. Left panel: grouped bar chart of AUROC for quality estimation (5 signals,\\n      SciERC NER). Right panel: grouped bar chart of best-of-N selection F1 (same 5 signals + greedy\\n      + oracle, SciERC NER + RE). Horizontal dashed line at greedy F1. Visualizes the gap: high AUROC\\n      does NOT translate to high selection F1. Include error bars from bootstrap CI where available.\\n    data_source: \\\"registry: exp_016_signal_ensemble, exp_012_logprob_baseline, exp_014_entity_majority_voting\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"2:1\\\"\\n\\n  - fig_id: fig_signal_heatmap\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Heatmap (signals as rows, datasets/tasks as columns) showing Spearman ρ values. Columns:\\n      SciERC NER (N=8), SciERC RE (N=8), CoNLL NER (N=8). Rows: voting_conf, SJ, EM, FK, logprob.\\n      Color-coded from red (low) to green (high). Annotated with ρ values. Visualizes task-complexity\\n      boundary: signal ranking shifts across columns.\\n    data_source: \\\"registry: exp_015_metrics_expansion (SciERC NER+RE unified), exp_002 (CoNLL). D035: heatmap data source unified to exp_015.\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n\\n  - fig_id: fig_reliability\\n    type: statistical\\n    tool: matplotlib\\n    description: >\\n      Reliability diagram (2 panels: NER, RE). For each signal, bin instances by predicted confidence\\n      (decile), plot mean predicted confidence vs mean actual F1. Perfect calibration = diagonal.\\n      Shows which signals are well-calibrated vs overconfident. Focus on SJ, voting_conf, logprob (3 curves per panel).\\n    caption_notes: >\\n      Caption or surrounding text MUST note two definition differences:\\n      (1) F1 definition: y-axis uses mean_sample_f1 (average F1 across N stochastic samples per instance),\\n      distinct from greedy F1 used in Table 1 ρ/AUROC targets — this is the calibration-appropriate measure\\n      since confidence signals aggregate over stochastic samples.\\n      (2) Logprob normalization: logprob is globally min-max normalized to [0,1] (SJ and voting_conf are\\n      naturally [0,1]). ECE absolute values are therefore NOT directly comparable across signals — only\\n      relative calibration patterns (over/under-confident regions) are meaningful.\\n    data_source: \\\"registry: mvp_pilot_004, exp_012_logprob_baseline, exp_014_entity_majority_voting\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"2:1\\\"\\n\\ntable_plan:\\n  - table_id: tab_quality_estimation\\n    caption: \\\"Quality estimation performance of five confidence signals across tasks and datasets. ρ: Spearman correlation with instance-level F1. AUROC: discriminative power for identifying above-median instances. Best in bold, second-best underlined.\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Signal, Family, SciERC NER ρ, SciERC NER AUROC, SciERC RE ρ, SciERC RE AUROC, CoNLL NER ρ, CoNLL NER AUROC]\\n    data_source: \\\"registry: exp_015_metrics_expansion (SciERC unified), exp_002 (CoNLL Qwen), exp_017_llama_conll_infer (CoNLL LLaMA). D035: SciERC data source unified to exp_015.\\\"\\n    notes: \\\"N=8, T=1.0 for all. CoNLL n=2756 valid, SciERC NER n=529, RE n=397. Table includes both Qwen and LLaMA rows for CoNLL to demonstrate model-agnostic pattern.\\\"\\n\\n  - table_id: tab_selection\\n    caption: \\\"Best-of-N selection F1 using each signal for sample ranking. Oracle selects the sample with highest true F1. Greedy uses T=0 decoding (no sampling). Bold: methods beating greedy.\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Method, SciERC NER F1, SciERC RE F1]\\n    data_source: \\\"registry: exp_016_signal_ensemble\\\"\\n    notes: \\\"N=8, T=1.0. Include: oracle, logprob, SJ, ensemble, voting, EM, random, greedy.\\\"\\n\\n  - table_id: tab_robustness\\n    caption: \\\"Robustness analysis: temperature sensitivity (T=0.7 vs T=1.0) and sample scaling (N=8 vs N=16) on SciERC.\\\"\\n    placement: experiments\\n    type: comparison\\n    columns: [Signal, NER ρ (T=0.7), NER ρ (T=1.0), Δ, RE ρ (T=0.7), RE ρ (T=1.0), Δ]\\n    data_source: \\\"registry: exp_015_metrics_expansion (N=8 baseline), mvp_pilot_005 (T=0.7), exp_001_seed42_v2, exp_001_seed123_v2 (N=16 NER), exp_008_re_n16_v2 (N=16 RE)\\\"\\n    notes: \\\"Temperature rows from exp_015 (T=1.0) vs pilot_005 (T=0.7). N-scaling from exp_001_v2 (N=16 NER, 2 seeds) + exp_008_v2 (N=16 RE). D037: SJ N-scaling gain (+0.071) >> FK (+0.016). RE N=16 all signals flat ~0.28.\\\"\\n\\nliterature_strategy:\\n  citation_budget: 50\\n  macro_context:\\n    - \\\"confidence estimation for LLM outputs\\\"\\n    - \\\"test-time scaling and self-consistency\\\"\\n    - \\\"uncertainty quantification for structured prediction\\\"\\n    - \\\"information extraction with large language models\\\"\\n  micro_clusters:\\n    - cluster_name: \\\"self_consistency_reasoning\\\"\\n      search_queries:\\n        - \\\"self-consistency chain-of-thought Wang 2023\\\"\\n        - \\\"universal self-consistency Chen 2024\\\"\\n        - \\\"SelfCheckGPT hallucination detection Manakul 2023\\\"\\n        - \\\"confidence improves self-consistency CISC 2025\\\"\\n        - \\\"self-certainty best-of-N selection ICLR 2026\\\"\\n        - \\\"reliability-aware adaptive self-consistency ReASC 2026\\\"\\n        - \\\"ranked voting self-consistency 2025\\\"\\n      must_cite:\\n        - \\\"Wang et al. 2023 — Self-Consistency Improves Chain of Thought Reasoning\\\"\\n        - \\\"Chen et al. 2024 — Universal Self-Consistency\\\"\\n        - \\\"Manakul et al. 2023 — SelfCheckGPT\\\"\\n        - \\\"CISC, ACL Findings 2025 (arXiv 2502.06233) — Confidence Improves Self-Consistency\\\"\\n        - \\\"Self-Certainty BoN, ICLR 2026 (arXiv 2502.18581) — Scalable Best-of-N via Self-Certainty\\\"\\n        - \\\"ReASC (arXiv 2601.02970) — Reliability-Aware Adaptive Self-Consistency\\\"\\n        - \\\"Ranked Voting SC (arXiv 2505.10772) — Ranked Voting based Self-Consistency\\\"\\n      target_count: 8\\n\\n    - cluster_name: \\\"consistency_structured_ie\\\"\\n      search_queries:\\n        - \\\"consistency accuracy correlation LLM entity relation extraction 2026\\\"\\n        - \\\"Nédellec Xia consistency plant health NER RE\\\"\\n        - \\\"CoCoA confidence consistency uncertainty quantification NeurIPS 2025\\\"\\n        - \\\"Vashurin uncertainty estimation LLM evaluation 2025\\\"\\n      must_cite:\\n        - \\\"Nédellec & Xia, Genomics Informatics 2026-02 (PMC12888769) — Consistency-accuracy correlation in hard-prompted LLMs for entity and relation extraction\\\"\\n      should_cite:\\n        - \\\"Vashurin et al., NeurIPS 2025 (arXiv 2502.04964) — CoCoA: Combining Confidence and Consistency\\\"\\n        - \\\"Vashurin et al. (arXiv 2510.20460, 2025) — Systematic evaluation of UQ methods for LLMs\\\"\\n      target_count: 3\\n\\n    - cluster_name: \\\"confidence_surveys\\\"\\n      search_queries:\\n        - \\\"survey confidence estimation calibration LLM NAACL 2024\\\"\\n        - \\\"know your limits survey abstention LLM TACL 2025\\\"\\n      must_cite:\\n        - \\\"Geng et al., NAACL 2024 (arXiv 2311.08298) — Survey of Confidence Estimation and Calibration in LLMs\\\"\\n        - \\\"Feng et al., TACL 2025 — Know Your Limits: Survey of Abstention in LLMs\\\"\\n      target_count: 2\\n\\n    - cluster_name: \\\"uncertainty_calibration\\\"\\n      search_queries:\\n        - \\\"semantic uncertainty LLM Kuhn 2023\\\"\\n        - \\\"language model calibration P(True) Kadavath 2022\\\"\\n        - \\\"calibration modern neural networks Guo 2017\\\"\\n        - \\\"calibration NLP sequence labeling Desai Durrett 2020\\\"\\n        - \\\"verbalized confidence LLM 2024\\\"\\n      must_cite:\\n        - \\\"Kuhn et al. 2023 — Semantic Uncertainty\\\"\\n        - \\\"Kadavath et al. 2022 — Language Models (Mostly) Know What They Know\\\"\\n        - \\\"Guo et al. 2017 — On Calibration of Modern Neural Networks\\\"\\n        - \\\"Desai & Durrett 2020 — Calibration of Pre-trained Transformers\\\"\\n      target_count: 6\\n\\n    - cluster_name: \\\"conformal_prediction\\\"\\n      search_queries:\\n        - \\\"conformal prediction structured outputs NLP 2021\\\"\\n        - \\\"conformal prediction NER sequence labeling\\\"\\n        - \\\"distribution-free uncertainty sets Angelopoulos\\\"\\n      must_cite:\\n        - \\\"Fisch et al. 2021 — Few-Shot Conformal Prediction with Auxiliary Tasks\\\"\\n        - \\\"Angelopoulos et al. 2021 — Uncertainty Sets for Image Classifiers\\\"\\n      target_count: 3\\n\\n    - cluster_name: \\\"token_span_uncertainty_ner\\\"\\n      search_queries:\\n        - \\\"uncertainty estimation named entity recognition\\\"\\n        - \\\"confidence estimation sequence labeling CRF\\\"\\n        - \\\"selective prediction NER 2021\\\"\\n      must_cite:\\n        - \\\"Xiao & Wang 2019 — Quantifying Uncertainties in NLP\\\"\\n        - \\\"Shelmanov et al. 2021 — Active Learning + Uncertainty NER\\\"\\n      target_count: 3\\n\\n    - cluster_name: \\\"ensemble_mc_dropout\\\"\\n      search_queries:\\n        - \\\"deep ensemble uncertainty Lakshminarayanan 2017\\\"\\n        - \\\"MC dropout uncertainty Gal Ghahramani 2016\\\"\\n        - \\\"ensemble diversity uncertainty estimation NLP\\\"\\n      must_cite:\\n        - \\\"Lakshminarayanan et al. 2017 — Simple and Scalable Predictive Uncertainty Estimation\\\"\\n        - \\\"Gal & Ghahramani 2016 — Dropout as a Bayesian Approximation\\\"\\n      target_count: 3\\n\\n    - cluster_name: \\\"verifier_reward_models\\\"\\n      search_queries:\\n        - \\\"training verifiers solve math word problems Cobbe 2021\\\"\\n        - \\\"process reward model Lightman 2023\\\"\\n        - \\\"outcome reward model LLM verification 2024\\\"\\n      must_cite:\\n        - \\\"Cobbe et al. 2021 — Training Verifiers to Solve Math Word Problems\\\"\\n        - \\\"Lightman et al. 2023 — Let's Verify Step by Step\\\"\\n      target_count: 3\\n\\n    - cluster_name: \\\"tts_scaling\\\"\\n      search_queries:\\n        - \\\"scaling LLM test-time compute Snell 2024\\\"\\n        - \\\"test-time compute scaling 2024\\\"\\n        - \\\"compute-optimal inference LLM\\\"\\n      must_cite:\\n        - \\\"Snell et al. 2024 — Scaling LLM Test-Time Compute\\\"\\n        - \\\"Brown et al. 2024 (or relevant TTS scaling paper)\\\"\\n      target_count: 3\\n\\n    - cluster_name: \\\"structured_calibration_ie\\\"\\n      search_queries:\\n        - \\\"calibration structured prediction Kuleshov 2015\\\"\\n        - \\\"calibration information extraction Jagannatha 2022\\\"\\n        - \\\"confidence estimation relation extraction\\\"\\n        - \\\"Culotta McCallum 2004 confidence estimation\\\"\\n      must_cite:\\n        - \\\"Kuleshov & Liang 2015 — Calibrated Structured Prediction\\\"\\n        - \\\"Culotta & McCallum 2004 — Confidence Estimation for IE\\\"\\n      target_count: 3\\n\\n    - cluster_name: \\\"selective_prediction\\\"\\n      search_queries:\\n        - \\\"selective prediction abstention Geifman El-Yaniv 2017\\\"\\n        - \\\"selective classification deep learning\\\"\\n        - \\\"learning to abstain NLP 2023\\\"\\n      must_cite:\\n        - \\\"Geifman & El-Yaniv 2017 — Selective Classification for Deep Neural Networks\\\"\\n      target_count: 2\\n\\n    - cluster_name: \\\"generative_ie\\\"\\n      search_queries:\\n        - \\\"generative information extraction LLM 2024\\\"\\n        - \\\"LLM named entity recognition in-context learning\\\"\\n        - \\\"universal information extraction UIE 2023 2024\\\"\\n        - \\\"structured prediction LLM prompting\\\"\\n      must_cite: []\\n      target_count: 4\\n\\n    - cluster_name: \\\"agreement_metrics\\\"\\n      search_queries:\\n        - \\\"Fleiss Kappa inter-rater agreement\\\"\\n        - \\\"Jaccard similarity set matching NLP\\\"\\n        - \\\"inter-annotator agreement NER\\\"\\n      must_cite: []\\n      target_count: 2\\n\\nwriting_order:\\n  - experiments\\n  - method\\n  - introduction\\n  - related_work\\n  - discussion\\n  - abstract\\n  - conclusion\\n\", \"total_chars\": 42590, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9085cc3c-e4c5-4781-90e2-ec446917c12b",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "44933cdc-7660-4b78-95a8-078b9153323f",
  "sourceToolAssistantUUID": "9085cc3c-e4c5-4781-90e2-ec446917c12b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T10:24:54.548Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HuSZvAmHbxVhDjAciYe1RD`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44933cdc-7660-4b78-95a8-078b9153323f",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C6PXkgMygUpn1whbBh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3dfa0105-2682-4435-b51b-5ce089b9d8b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AtXj8w5wKthGirrhmTF672",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9159,
      "cache_read_input_tokens": 34808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9159,
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

_source line 24 · 2026-05-15T10:24:54.807Z_

<details><summary>↩ Tool result · `toolu_01HuSZvAmHbxVhDjAciYe1RD`</summary>

```text
Error: result (62,600 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/79301dc3-a43c-42c1-b7ac-01c347c8ab59/tool-results/mcp-agent-ml-research-read_project_file-1778840694805.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/79301dc3-a43c-42c1-b7ac-01c347c8ab59/tool-results/mcp-agent-ml-research-read_project_file-1778840694805.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/79301dc3-a43c-42c1-b7ac-01c347c8ab59/tool-results/mcp-agent-ml-research-read_project_file-1778840694805.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dfa0105-2682-4435-b51b-5ce089b9d8b0",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "0966ac17-d1a1-41c3-a786-4bfefbe8e842",
  "sourceToolAssistantUUID": "3dfa0105-2682-4435-b51b-5ce089b9d8b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T10:24:57.368Z_

Let me look at the actual paper LaTeX files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0966ac17-d1a1-41c3-a786-4bfefbe8e842",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C6ktt1PDFWVGLPTWBn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec9e21ec-cc8e-4a69-8bbf-e972c2c64bd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hViv1hYhTEoyXRtsmcH8S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16293,
      "cache_read_input_tokens": 43967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16293,
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

_source line 26 · 2026-05-15T10:24:58.386Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01X2is2A9oG4uech76m8LJu1`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec9e21ec-cc8e-4a69-8bbf-e972c2c64bd7",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C6ktt1PDFWVGLPTWBn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7aa48019-7eb9-4f67-bdfc-8aa70183b5b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hViv1hYhTEoyXRtsmcH8S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16293,
      "cache_read_input_tokens": 43967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16293,
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

_source line 27 · 2026-05-15T10:24:58.415Z_

<details><summary>↩ Tool result · `toolu_01X2is2A9oG4uech76m8LJu1`</summary>

```text
artifacts/dream_reports/dream_20260514T093336/best/paper.tex
artifacts/dream_reports/dream_20260514T093336/median/paper.tex
artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
artifacts/dream_reports/dream_20260514T105303/best/paper.tex
artifacts/dream_reports/dream_20260514T105303/median/paper.tex
artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/discussion.tex
artifacts/dream_reports/dream_20260514T203201/best/paper.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/limitations.tex
artifacts/dream_reports/dream_20260514T203201/median/paper.tex
artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
artifacts/bootstrap_ci_tables.tex
docs/paper/sections/related_work.tex
docs/paper/sections/method.tex
docs/paper/sections/experiments.tex
docs/paper/abstract.tex
docs/paper/discussion.tex
docs/paper/conclusion.tex
artifacts/dream_reports/dream_20260515T092545/best/paper.tex
artifacts/dream_reports/dream_20260515T092545/median/paper.tex
artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
docs/paper/main.tex
docs/paper/sections/abstract.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/limitations.tex
docs/paper/sections/introduction.tex
docs/paper/sections/discussion.tex
docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7aa48019-7eb9-4f67-bdfc-8aa70183b5b1",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "a9676648-493a-4459-b34d-2362132a8dac",
  "sourceToolAssistantUUID": "7aa48019-7eb9-4f67-bdfc-8aa70183b5b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T10:24:59.036Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01P22Z7Yd26ptbQyH8ALYAmQ`</summary>

```json
{
  "pattern": "**/artifacts/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9676648-493a-4459-b34d-2362132a8dac",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C6ktt1PDFWVGLPTWBn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "702e82fa-b680-4e53-b39a-3d6ea12bfcb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hViv1hYhTEoyXRtsmcH8S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16293,
      "cache_read_input_tokens": 43967,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16293
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 43967,
          "cache_creation_input_tokens": 16293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16293,
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

_source line 29 · 2026-05-15T10:24:59.065Z_

<details><summary>↩ Tool result · `toolu_01P22Z7Yd26ptbQyH8ALYAmQ`</summary>

```text
artifacts/ft_002/intermediate/ft_002_config_notes.md
artifacts/mvp_pilot_004/report/framing_proposal_post_pilot004.md
artifacts/dream_reports/dream_20260514T093336/best/paper_framing.md
artifacts/dream_reports/dream_20260514T093336/median/paper_framing.md
artifacts/dream_reports/dream_20260514T093336/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T093336/best/review_report.md
artifacts/dream_reports/dream_20260514T093336/median/review_report.md
artifacts/dream_reports/dream_20260514T093336/worst/review_report.md
artifacts/dream_reports/dream_20260514T105303/best/paper_framing.md
artifacts/dream_reports/dream_20260514T105303/median/paper_framing.md
artifacts/dream_reports/dream_20260514T105303/worst/paper_framing.md
artifacts/exp005_temperature/summary.md
artifacts/exp_005/report/summary.md
artifacts/exp-015/report/exp015_summary.md
artifacts/dream_reports/dream_20260514T105303/best/review_report.md
artifacts/dream_reports/dream_20260514T105303/median/review_report.md
artifacts/dream_reports/dream_20260514T105303/worst/review_report.md
artifacts/exp_016_signal_ensemble/report/summary.md
artifacts/exp_016_signal_ensemble/report/summary_cc2f1c.md
artifacts/review_reports/round_0.md
artifacts/_project/report/logprob_rho_diagnosis.md
artifacts/wnut17_diagnosis_report.md
artifacts/exp_003/report/wnut17_diagnosis_report.md
artifacts/bjb1_status_report.md
artifacts/_project/report/autodl_process_check.md
artifacts/autodl_process_check.md
artifacts/auroc_bug_diagnosis.md
artifacts/exp_015_metrics_expansion/report/heatmap_data_audit.md
artifacts/heatmap_data_audit.md
artifacts/audit_gpu5090_4x2_loop3.md
artifacts/audit_autodl5090_loop3.md
artifacts/_project/report/3seed_5signal_tables.md
artifacts/3seed_summary/3seed_5signal_tables.md
artifacts/exp_001_seed456_v2_ner/report/3seed_ner_summary.md
artifacts/3seed_ner_summary.md
artifacts/exp_009_v2_re_rerun/report/exp_009_v2_re_rerun_summary.md
artifacts/_project/report/n16_5signal_comparison.md
artifacts/n16_5signal_comparison.md
artifacts/_project/report/llama_conll_n16_3seed_5signal_summary.md
artifacts/dream_reports/dream_20260514T203201/best/paper_framing.md
artifacts/dream_reports/dream_20260514T203201/median/paper_framing.md
artifacts/dream_reports/dream_20260514T203201/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T203201/best/review_report.md
artifacts/dream_reports/dream_20260514T203201/median/review_report.md
artifacts/dream_reports/dream_20260514T203201/worst/review_report.md
artifacts/review_reports/round_1.md
artifacts/review_reports/round_2.md
artifacts/review_reports/round_3.md
artifacts/exp_018_provenance_report.md
artifacts/exp_018/report/exp_018_provenance_report.md
artifacts/_project/report/multi_seed_stability_table.md
artifacts/multi_seed_stability_table.md
artifacts/review_reports/round_4.md
artifacts/_project/report/re_nonzero_selection_analysis.md
artifacts/re_nonzero_selection_analysis.md
artifacts/training_config_appendix.md
artifacts/_project/report/logprob_tie_analysis.md
artifacts/logprob_tie_analysis.md
artifacts/_project/report/re_nonzero_selection_n397.md
artifacts/_project/report/logprob_tie_analysis_n529.md
artifacts/review_reports/round_5.md
artifacts/review_reports/round_6.md
artifacts/_project/report/qwen3_thinking_confirmation.md
artifacts/qwen3_thinking_confirmation.md
artifacts/_project/data/tost_breakpoint_delta_star.md
artifacts/tost_breakpoint_delta_star.md
artifacts/_project/report/vc_implementation_rho_diff.md
artifacts/vc_implementation_rho_diff.md
artifacts/dream_reports/dream_20260515T092545/best/paper_framing.md
artifacts/_project/report/D070_D071_revision_summary.md
artifacts/dream_reports/dream_20260515T092545/median/paper_framing.md
artifacts/exp_freeform_ablation/report/freeform_ablation_results.md
artifacts/freeform_ablation_results.md
artifacts/dream_reports/dream_20260515T092545/worst/paper_framing.md
artifacts/_project/report/n16_readiness_report.md
artifacts/n16_readiness_report.md
artifacts/dream_reports/dream_20260515T092545/best/review_report.md
artifacts/dream_reports/dream_20260515T092545/median/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "702e82fa-b680-4e53-b39a-3d6ea12bfcb2",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "59a63fd7-5c4b-452f-a336-4452bc2939bc",
  "sourceToolAssistantUUID": "702e82fa-b680-4e53-b39a-3d6ea12bfcb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-15T10:25:01.361Z_

Let me read the main paper sections to assess the actual paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59a63fd7-5c4b-452f-a336-4452bc2939bc",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C75GRi3YW3z9r9QCZd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f08fe71-3516-4582-9817-5424aad270ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfKyVQW8v5AgUWPPyf9w5o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2118,
      "cache_read_input_tokens": 60260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2118,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 31 · 2026-05-15T10:25:02.400Z_

<details open><summary>🔧 Tool call — Read · `toolu_019zw987ALqcYrMSkQwA5zUm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f08fe71-3516-4582-9817-5424aad270ce",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C75GRi3YW3z9r9QCZd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89e6a67c-1216-4265-9813-a20612de5c30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfKyVQW8v5AgUWPPyf9w5o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2118,
      "cache_read_input_tokens": 60260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2118,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 32 · 2026-05-15T10:25:02.419Z_

<details><summary>↩ Tool result · `toolu_019zw987ALqcYrMSkQwA5zUm`</summary>

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
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Cannot Scale Structured Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	CoNLL-2003 is based on the Reuters news corpus; we use the publicly available version and comply with its academic license terms.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{sections/appendix}
49	
50	\end{document}
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89e6a67c-1216-4265-9813-a20612de5c30",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "92fd2304-6d90-4493-82e8-c8b1b0076b70",
  "sourceToolAssistantUUID": "89e6a67c-1216-4265-9813-a20612de5c30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T10:25:02.955Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F2WfqNo6ku2Ly7ijLUqZXC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92fd2304-6d90-4493-82e8-c8b1b0076b70",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C75GRi3YW3z9r9QCZd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5096af2a-c890-4b25-810a-0274cb8417a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfKyVQW8v5AgUWPPyf9w5o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2118,
      "cache_read_input_tokens": 60260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2118,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 34 · 2026-05-15T10:25:02.962Z_

<details><summary>↩ Tool result · `toolu_01F2WfqNo6ku2Ly7ijLUqZXC`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling \cite{zhang2025tts}, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whether findings generalize across a difficulty gradient.
15	Our Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\S\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).
16	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
17	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \cite{willard2023guided}.
18	
19	\paragraph{Uncertainty estimation and calibration.}
20	Surveys cover confidence estimation \cite{geng2024confidence}, selective abstention \cite{wen2025know}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs; \citet{xiong2024llm} find LLMs tend toward overconfidence, and \citet{heo2025uncertainty} show calibration degrades with task complexity.
21	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; \citet{kossen2024semantic} distill this into probes; P(True) \cite{kadavath2022language} queries model confidence directly; \citet{malinin2021uncertainty} distinguish data and model uncertainty in autoregressive models.
22	Our structural signals instead measure agreement over output \textit{structure}.
23	Neural networks are often miscalibrated \cite{guo2017calibration, desai2020calibration}; deep ensembles \cite{lakshminarayanan2017ensembles} and MC-dropout \cite{gal2016dropout} obtain uncertainty from model variation, while our approach requires no model modification.
24	Prior NER uncertainty work spans Bayesian inference for sequence labeling \cite{xiao2019uncertainty}, active learning under uncertainty \cite{shelmanov2021active}, evidential deep learning \cite{zhang2023ener}, verification-augmented NER \cite{kim2024verifiner}, and uncertainty transmission across label sequences \cite{he2024uncertainty}---all within discriminative paradigms.
25	Conformal prediction \cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \cite{cobbe2021verifiers, lightman2024verify, venktesh2025trust} and reward models \cite{wang2024mathshepherd} learn per-sample scoring.
26	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling} with structural utility functions; despite MBR's success in translation \cite{freitag2022high} and other generation tasks \cite{jinnai2024mbr}, we find utility-quality misalignment at the per-sample level for structured IE (\S\ref{sec:discussion}).
27	Selective prediction \cite{geifman2017selective} and confidence-based IE filtering \cite{culotta2004confidence} establish the broader framework.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5096af2a-c890-4b25-810a-0274cb8417a7",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "26340b45-059e-489b-a893-89be2313031f",
  "sourceToolAssistantUUID": "5096af2a-c890-4b25-810a-0274cb8417a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T10:25:03.241Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CvmeQ1caDs4YsGwoGeF8bL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26340b45-059e-489b-a893-89be2313031f",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C75GRi3YW3z9r9QCZd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b9943af-1922-48f2-a7b3-61f177684a21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfKyVQW8v5AgUWPPyf9w5o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2118,
      "cache_read_input_tokens": 60260,
      "output_tokens": 254,
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
          "output_tokens": 254,
          "cache_read_input_tokens": 60260,
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

_source line 36 · 2026-05-15T10:25:03.245Z_

<details><summary>↩ Tool result · `toolu_01CvmeQ1caDs4YsGwoGeF8bL`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
16	The most relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.
17	Our work extends theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings---WNUT-17 conditional correlations collapse to $\rho{=}0.038$ (n.s.) and LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$)---that would be invisible on a single dataset.
18	
19	Structured IE requires schema-compliant output, making constrained decoding \cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\% valid JSON rate (\S\ref{sec:ablation}).}
20	All experiments use constrained decoding, the regime under which structured IE is practically deployed.
21	
22	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13--18~pp of oracle headroom.
23	By construction, four of five signals assign identical scores to all candidates from the same input, precluding per-sample discrimination.
24	The non-trivial questions are whether (a)~consensus-proximity selection---instantiating MBR decoding \cite{eikema2022sampling, freitag2022high, muller2021understanding} with structural utility functions---can recover discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.
25	Both fail: MBR utility correlates with F1 across instances but not within them (\S\ref{sec:discussion}); log-probability scores are severely compressed (60\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
26	A controlled free-form decoding ablation confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding (\S\ref{sec:ablation}).
27	
28	\begin{figure*}[t]
29	\centering
30	\includegraphics[width=\textwidth]{fig_overview}
31	\caption{The correlation-selection gap. \textbf{Left}: consistency signals predict instance-level quality---high agreement correlates with high F1. \textbf{Right}: instance-level signals assign identical scores to all $N$ candidates, precluding sample selection. Consensus-proximity selection does not recover per-sample discrimination.}
32	\label{fig:overview}
33	\end{figure*}
34	
35	We systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
36	Our contributions are:
37	\begin{enumerate}
38	    \item \textbf{The correlation-selection gap and its diagnosis.}
39	    We demonstrate that strong quality estimation ($\rho{=}0.38$, AUROC${=}0.75$) coexists with selection failure ($p{>}0.39$, 13--18~pp oracle headroom).
40	    Log-probability---the only per-sample signal---fails due to score compression (60\% of instances effectively tied); where compression is mitigated, it becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
41	    A controlled ablation confirms that compression is intrinsic, not decoding-regime-specific.
42	
43	    \item \textbf{A systematic evaluation framework.}
44	    We compare five confidence signals from three families---structural, surface, and model-internal---across quality estimation, binary discrimination, and sample selection, showing that these metrics decouple and single-metric evaluation risks selecting the wrong signal.
45	
46	    \item \textbf{Task-complexity boundary conditions.}
47	    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.
48	    At the capability boundary (WNUT-17, 52\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\rho{=}{-}0.410$), indicating overconfidence on out-of-distribution inputs.
49	    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).
50	\end{enumerate}
51	
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b9943af-1922-48f2-a7b3-61f177684a21",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "00d42259-dc24-40c7-874b-1b878c6dd1d1",
  "sourceToolAssistantUUID": "6b9943af-1922-48f2-a7b3-61f177684a21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T10:25:06.399Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FjWtTqGZfbSUXEPcfzjFuw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00d42259-dc24-40c7-874b-1b878c6dd1d1",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C7PDReFdrc8a5kJcgY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f6759d5-0e29-4b65-936a-d4a79c94200f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUeZ1CuACKhE7VGx51SEZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4109,
      "cache_read_input_tokens": 62378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4109,
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

_source line 38 · 2026-05-15T10:25:06.404Z_

<details><summary>↩ Tool result · `toolu_01FjWtTqGZfbSUXEPcfzjFuw`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \texttt{&lt;think>\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \texttt{enable\_thinking=False}.
16	No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.
17	This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.
18	We discuss implications in the Limitations section.
19	We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}). A 3-seed stability analysis ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}, Appendix~\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}
20	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
21	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}
25	\label{sec:qe_results}
26	
27	\begin{table*}[t]
28	\centering
29	\small
30	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
31	\label{tab:quality_estimation}
32	\begin{tabular}{ll cc cc cc cc}
33	\toprule
34	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
35	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
36	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
37	\midrule
38	VC & Structural & \textbf{.379} & .684 & \textbf{.350} & .693 & .424 & .789 & .426 & .709 \\
39	SJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
40	FK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\
41	EM  & Surface    & .295 & \textbf{.749} & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
42	LP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \textbf{.761} \\
43	\bottomrule
44	\end{tabular}
45	\end{table*}
46	
47	\begin{figure*}[t]
48	\centering
49	\includegraphics[width=\textwidth]{fig_signal_heatmap}
50	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
51	\label{fig:signal_heatmap}
52	\end{figure*}
53	
54	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
55	
56	\paragraph{Difficulty-dependent signal complementarity.}
57	On SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\rho{=}0.379$ and SJ $\rho{=}0.360$, both outperforming surface ($\rho{\leq}0.295$) and LP ($\rho{=}0.205$).
58	This advantage persists on RE (VC $\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\% zero-F1 floor effect.
59	VC and SJ show moderate instance-level correlation (NER: $\rho{=}0.659$; RE: $\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\ span-level set overlap.
60	While the best $\rho{=}0.38$ (VC) explains approximately 14\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\footnote{For scale context, semantic entropy \cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA, though direct comparison is not meaningful due to fundamentally different output spaces and evaluation protocols.}
61	Pairwise bootstrap CIs confirm the SJ advantage over LP ($\Delta\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\Delta\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\ref{tab:bootstrap_signal_ci}, Appendix~\ref{app:bootstrap_signal}).
62	
63	\paragraph{$\rho$--AUROC dissociation.}
64	Signal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295), preferred for binary quality triage; structural signals ($\rho{\geq}0.36$) are better for fine-grained ranking.
65	On CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\rho$ (0.307), confirming this pattern across datasets.
66	
67	\paragraph{Signal rankings shift with task difficulty.}
68	On CoNLL (greedy F1${\approx}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.
69	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
70	This crossover---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.
71	Stability across the two model families (both 8B) is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$, within 3-seed $\sigma{\approx}0.007$).
72	On WNUT-17, where 52\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
73	LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$, AUROC${=}0.219$).
74	We hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.
75	On the conditional set, all signals collapse toward weak or non-significant correlations ($\rho{\leq}0.35$), with SJ achieving only $\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.
76	
77	\paragraph{Conditional filtering.}
78	Filtering to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, right).
79	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
80	LP RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
81	This creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
82	
83	%% ============================================================
84	\subsection{The Correlation-Selection Gap}
85	\label{sec:selection_gap}
86	
87	\begin{figure*}[t]
88	\centering
89	\includegraphics[width=\textwidth]{fig_selection_gap}
90	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound.}
91	\label{fig:selection_gap}
92	\end{figure*}
93	
94	\begin{table}[t]
95	\centering
96	\small
97	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \textbf{bold}. EM selects the plurality output; despite a 42\% pairwise exact-match rate, EM selection underperforms greedy on both tasks.}
98	\label{tab:selection}
99	\begin{tabular}{lcc}
100	\toprule
101	Method & NER F1 & RE F1 \\
102	\midrule
103	Oracle & 0.776 & 0.585 \\
104	\midrule
105	LP           & \textbf{0.650} & 0.395 \\
106	SJ       & 0.645 & 0.386 \\
107	EM        & 0.636 & 0.372 \\
108	VC                 & 0.634 & 0.359 \\
109	\midrule
110	Greedy ($T{=}0$)   & 0.644 & \textbf{0.404} \\
111	Random             & 0.608 & 0.354 \\
112	\bottomrule
113	\end{tabular}
114	\end{table}
115	
116	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
117	Four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.
118	The non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.
119	We anchor this analysis on SciERC, where output diversity is substantial: only 11--18\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.
120	
121	\paragraph{No significant improvement over greedy.}
122	We exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).
123	On NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).
124	LP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).
125	On RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.
126	TOST equivalence testing confirms most signals are indistinguishable from greedy at ${\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\pm}5$~pp (Table~\ref{tab:tost}, Appendix~\ref{app:diversity}).
127	VC ($\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\textit{below} greedy.
128	The gap extends to CoNLL (ceiling effect, 57--88\% identical outputs) and WNUT-17 (capability boundary; Table~\ref{tab:cross_selection}).
129	
130	\paragraph{Quality estimation $\neq$ output selection.}
131	Instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best.
132	When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.
133	This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
134	
135	%% ============================================================
136	\subsection{Robustness}
137	\label{sec:robustness_main}
138	
139	Consistency-based signals show robust performance across $T{\in}\{0.7, 1.0\}$ (SJ NER $\Delta\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$; Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
140	NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\rho{\approx}0.28$ for $N{=}16$.
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f6759d5-0e29-4b65-936a-d4a79c94200f",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "e955c6d7-0e66-467e-8a17-7a56d03f0f0e",
  "sourceToolAssistantUUID": "5f6759d5-0e29-4b65-936a-d4a79c94200f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T10:25:06.871Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JYfwVZD5kDVTZ2bZEqRf3F`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e955c6d7-0e66-467e-8a17-7a56d03f0f0e",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C7PDReFdrc8a5kJcgY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44a07aa1-15a4-4121-a918-c6ecca8c2b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUeZ1CuACKhE7VGx51SEZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4109,
      "cache_read_input_tokens": 62378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4109,
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

_source line 40 · 2026-05-15T10:25:06.876Z_

<details><summary>↩ Tool result · `toolu_01JYfwVZD5kDVTZ2bZEqRf3F`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists: two layers.}
9	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
10	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
11	\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
12	LP scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
13	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
14	This diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.
15	A controlled ablation (\S\ref{sec:ablation}) confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding.
16	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\ref{app:calibration}) may compound this.
17	
18	\paragraph{Connection to MBR decoding.}
19	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
20	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
21	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
22	
23	\paragraph{Score compression is task-inherent.}\label{sec:ablation}
24	A natural hypothesis is that LP compression is an artifact of constrained decoding's restricted token space.
25	We test this via controlled ablation: generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\%, 4406/4408; Table~\ref{tab:freeform_ablation}).
26	LP variance is essentially unchanged (within-instance std ratio $0.97{\times}$, tied fraction 59.7\%$\to$57.7\%).
27	NER selection gains remain negligible ($+0.18$~pp free-form vs.\ $+0.59$~pp constrained).
28	This rules out constrained decoding as the cause of compression and establishes LP compression as inherent to structured output generation.
29	The correlation-selection gap is therefore a fundamental challenge for test-time scaling in structured IE, not an artifact of any particular decoding strategy.
30	Notably, the fine-tuned model achieved 99.95\% parse rate without grammar constraints, suggesting that constrained decoding's format-compliance role may be redundant for sufficiently fine-tuned models.
31	
32	\paragraph{RE task-specific interaction.}
33	RE LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form), suggesting a task-specific interaction between decoding regime and selection efficacy that does not generalize to NER.
34	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
35	
36	\paragraph{Methodological implications.}
37	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.
38	Effective selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44a07aa1-15a4-4121-a918-c6ecca8c2b17",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "5413c974-0e93-4b35-95e7-45e15d3a4e12",
  "sourceToolAssistantUUID": "44a07aa1-15a4-4121-a918-c6ecca8c2b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T10:25:07.225Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DJVG3eXgUBeqEcs64AQm1C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5413c974-0e93-4b35-95e7-45e15d3a4e12",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C7PDReFdrc8a5kJcgY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "584eae19-ec6a-49c8-a76c-47c0a3b9ce82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUeZ1CuACKhE7VGx51SEZq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4109,
      "cache_read_input_tokens": 62378,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4109
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 239,
          "cache_read_input_tokens": 62378,
          "cache_creation_input_tokens": 4109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4109,
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

_source line 42 · 2026-05-15T10:25:07.231Z_

<details><summary>↩ Tool result · `toolu_01DJVG3eXgUBeqEcs64AQm1C`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.
3	We evaluate five confidence signals from three families across NER and relation extraction on three benchmarks with two 8B-parameter model families.
4	These signals achieve strong quality estimation, yet none significantly improves sample selection over greedy decoding despite 13--18 percentage points of oracle headroom---a \textit{correlation-selection gap}.
5	Four of five signals are instance-level by construction and cannot rank candidates; the key empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection can bridge this gap.
6	Neither succeeds: log-probability scores are compressed into effective ties for 60\% of instances, while consensus-proximity (MBR decoding) fails because utility correlates with quality across instances but not within them.
7	A controlled free-form decoding ablation confirms that score compression is intrinsic to the model and task, not an artifact of constrained decoding.
8	Signal rankings further depend on task complexity, with findings consistent across model families.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "584eae19-ec6a-49c8-a76c-47c0a3b9ce82",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "8a72ef04-c624-4cc3-8632-7d17f6cf1908",
  "sourceToolAssistantUUID": "584eae19-ec6a-49c8-a76c-47c0a3b9ce82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T10:25:11.141Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KHdKHT1ipx3WRcJYD9b6d5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a72ef04-c624-4cc3-8632-7d17f6cf1908",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C7gLpRwFBCE9PYFXrC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71d3b183-ead5-423a-8c04-275582b2073b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtC5ZetehSkkimBGtB7CAe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6775,
      "cache_read_input_tokens": 66487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6775,
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

_source line 44 · 2026-05-15T10:25:11.147Z_

<details><summary>↩ Tool result · `toolu_01KHdKHT1ipx3WRcJYD9b6d5`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{&lt;j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface, instance-level).}
28	The majority fraction---the proportion of samples producing the most common output:
29	\begin{equation}\label{eq:em}
30	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
31	\end{equation}
32	
33	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
34	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
35	\begin{equation}\label{eq:fk}
36	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
37	\end{equation}
38	where $\bar{P}$ is mean observed pairwise agreement and $\bar{P}_e$ is expected agreement under random assignment.
39	While FK assumes independent raters, temperature-based sampling provides sufficient response diversity for the statistic to capture inter-sample agreement patterns.
40	Empirically, we measure excess agreement ($\bar{P} - \bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\% and $-$4.0\%, indicating mild \textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.
41	(All excess agreement values are negative across 5 configurations; a one-sample $t$-test against zero yields $p{<}0.05$.)
42	Unlike structural signals, FK relies on exact string matching and does not tolerate surface variations.
43	
44	\paragraph{Soft Jaccard (structural, instance-level).}
45	Our primary structural signal extends Jaccard similarity \cite{jaccard1901distribution} to extracted entity/relation sets.
46	For samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching via the Hungarian algorithm (maximizing total token-level IoU; zero-IoU pairs automatically receive zero weight), and define:
47	\begin{equation}\label{eq:sj}
48	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
49	\end{equation}
50	where $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.
51	We use $\max(|g_i|, |g_j|)$ rather than $|g_i \cup g_j|$ as the normalizer to penalize length asymmetry between samples.
52	The instance-level signal averages over all pairs:
53	\begin{equation}\label{eq:sj_instance}
54	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i&lt;j} \text{SJ}(y_i, y_j)
55	\end{equation}
56	
57	\paragraph{Entity voting confidence (structural, instance-level).}
58	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
59	The instance-level confidence is the mean frequency:
60	\begin{equation}\label{eq:voting}
61	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
62	\end{equation}
63	When $E_\cup = \emptyset$ (no entity extracted by any sample), we set $c_{\mathrm{vc}}(x) = 0$.\footnote{This occurs in $<$1\% of instances in our experiments (WNUT-17 only). Equation~\ref{eq:voting} defines the continuous QE signal used throughout Table~\ref{tab:quality_estimation} and all correlation analyses. For voted-output \textit{selection} (Table~\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting. The two computations serve different purposes: Eq.~\ref{eq:voting} assigns a continuous quality score per instance; the majority threshold constructs a discrete output for F1 evaluation. On NER, the threshold variant yields $\rho{=}0.252$ (vs.\ $0.379$ for Eq.~\ref{eq:voting}), reflecting information loss from binarization; on RE, the difference is negligible ($\Delta\rho{=}0.019$).}
64	
65	\subsection{Evaluation Framework}\label{sec:evaluation}
66	
67	\paragraph{Quality estimation.}
68	We measure rank correlation (Spearman $\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.
69	
70	\paragraph{Sample selection.}
71	We report best-of-$N$ F1: for each instance, the signal selects one sample.
72	Per-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).
73	We compare against an \textit{oracle} (highest-F1 sample) and \textit{greedy} ($T{=}0$, $N{=}1$).
74	
75	\paragraph{Complementarity.}
76	High rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\S\ref{sec:selection_gap}).
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71d3b183-ead5-423a-8c04-275582b2073b",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "eef7f327-b847-4075-917f-fb48c33a3c1d",
  "sourceToolAssistantUUID": "71d3b183-ead5-423a-8c04-275582b2073b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T10:25:12.117Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Jb33KQmcZiu1qCawaSTgAs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eef7f327-b847-4075-917f-fb48c33a3c1d",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C7gLpRwFBCE9PYFXrC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dad3549a-adf0-4b87-b56f-51cb60b5f41e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtC5ZetehSkkimBGtB7CAe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6775,
      "cache_read_input_tokens": 66487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6775,
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

_source line 46 · 2026-05-15T10:25:12.122Z_

<details><summary>↩ Tool result · `toolu_01Jb33KQmcZiu1qCawaSTgAs`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We demonstrate that consistency signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75) for LLM-based structured IE, but fail at sample selection---the \textit{correlation-selection gap}.
4	By construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to score compression.
5	Where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.
6	A controlled free-form decoding ablation confirms that score compression is intrinsic to the model and task, not an artifact of constrained decoding.
7	Signal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.
8	RE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.
9	Trained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dad3549a-adf0-4b87-b56f-51cb60b5f41e",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "16be9421-08a0-47a4-b0d1-9bf2172c09ff",
  "sourceToolAssistantUUID": "dad3549a-adf0-4b87-b56f-51cb60b5f41e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T10:25:12.346Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GX1nQhNCW6EziXXfHy2wMQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16be9421-08a0-47a4-b0d1-9bf2172c09ff",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C7gLpRwFBCE9PYFXrC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96a66c86-2f4b-4b30-98cb-dac5967e630b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtC5ZetehSkkimBGtB7CAe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6775,
      "cache_read_input_tokens": 66487,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6775
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 239,
          "cache_read_input_tokens": 66487,
          "cache_creation_input_tokens": 6775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6775,
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

_source line 48 · 2026-05-15T10:25:12.350Z_

<details><summary>↩ Tool result · `toolu_01GX1nQhNCW6EziXXfHy2wMQ`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Our free-form ablation (\S\ref{sec:ablation}) confirms that LP score compression persists without constrained decoding, but was conducted on a single dataset (SciERC) with one model (Qwen3-8B); whether the intrinsic compression finding generalizes to other datasets, model families, or model scales remains untested.
17	
18	Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking} active, injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning chain) before each response; CoNLL and WNUT checkpoints disabled this feature.
19	At inference time, constrained decoding suppresses thinking tokens in all configurations, so they do not appear in generated samples.
20	The empty blocks may weakly affect first-token probability distributions during training, but the absence of any reasoning content limits their representational impact; we do not expect this inconsistency to alter our quantitative conclusions.
21	
22	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ LP data, leaving its temperature sensitivity uncharacterized.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96a66c86-2f4b-4b30-98cb-dac5967e630b",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "7bee3c6e-c82a-4456-960b-9a5f5ed53296",
  "sourceToolAssistantUUID": "96a66c86-2f4b-4b30-98cb-dac5967e630b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-15T10:25:15.642Z_

Now let me read the appendix and the latest dream review reports for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bee3c6e-c82a-4456-960b-9a5f5ed53296",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C84AUi2zeYCd7sNSJT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a71ab38-55d4-4bd1-ada2-198a5676fe54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ar4z55SbCsdnftLJPxnLtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3762,
      "cache_read_input_tokens": 73262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3762,
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

_source line 50 · 2026-05-15T10:25:16.128Z_

<details open><summary>🔧 Tool call — Read · `toolu_015vMaHYbg4aQ9gJSNZSfdsd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a71ab38-55d4-4bd1-ada2-198a5676fe54",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C84AUi2zeYCd7sNSJT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b04af6a-1c33-4549-94e1-e7d260572d1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ar4z55SbCsdnftLJPxnLtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3762,
      "cache_read_input_tokens": 73262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3762,
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

_source line 51 · 2026-05-15T10:25:16.397Z_

<details><summary>↩ Tool result · `toolu_015vMaHYbg4aQ9gJSNZSfdsd`</summary>

```text
1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm}0.008$ & --- \\
56	\quad VC &  & $0.458{\pm}0.003$ & --- \\
57	\quad LP &  & $0.310{\pm}0.005$ & --- \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	\begin{figure}[t]
63	\centering
64	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
65	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}
66	\label{fig:temperature_robustness}
67	\end{figure}
68	
69	\paragraph{Temperature sensitivity.}
70	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.
71	FK shows mixed behavior: NER $\rho$ drops by 0.054, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
72	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.360 vs.\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
73	
74	\paragraph{Sample size scaling.}
75	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.412{\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.
76	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
77	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\ref{tab:quality_estimation}).
78	FK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.
79	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.021$).
80	SJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.
81	
82	\paragraph{Transfer across model families.}
83	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.363$, FK $\rho{=}0.327$).
84	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
85	At $N{=}16$, the structural-over-LP advantage holds across all four tested settings: Qwen SciERC (VC $\rho{=}0.411$ vs.\ LP 0.259, $\Delta{=}{+}0.152$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$), LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.463{\pm}0.007$ vs.\ LP $0.310{\pm}0.005$, $\Delta{=}{+}0.153$).
86	
87	\section{Calibration Analysis}\label{app:calibration}
88	
89	\begin{figure*}[t]
90	\centering
91	\includegraphics[width=\textwidth]{fig_reliability}
92	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
93	\label{fig:reliability}
94	\end{figure*}
95	
96	Reliability diagrams use 10 equal-width bins.
97	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
98	
99	\section{Additional Analyses}\label{app:additional}
100	
101	\paragraph{Per-relation diagnostic.}
102	RE signal degradation is relation-specific.
103	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
104	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
105	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
106	
107	\paragraph{Capability stratification.}
108	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
109	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
110	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
111	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
112	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
113	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
114	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
115	
116	\paragraph{Length vs.\ log-probability.}
117	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
118	
119	\begin{figure}[t]
120	\centering
121	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
122	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
123	\label{fig:length_logprob_scatter}
124	\end{figure}
125	
126	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
127	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
128	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
129	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, making the two selection rules equivalent.
130	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
131	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
132	Evaluation circularity is negligible.
133	
134	\paragraph{Conditional filtering details.}
135	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
136	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
137	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
138	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
139	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
140	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
141	
142	\paragraph{WNUT-17 full signal analysis.}
143	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
144	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
145	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
146	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
147	
148	\begin{table}[t]
149	\centering
150	\small
151	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
152	\label{tab:wnut}
153	\begin{tabular}{lccccc}
154	\toprule
155	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
156	\midrule
157	VC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
158	FK      & .125 & .001 & .555 & .169 & .002 \\
159	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
160	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
161	LP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
162	\bottomrule
163	\end{tabular}
164	\end{table}
165	
166	\paragraph{Cross-configuration selection analysis.}
167	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
168	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
169	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
170	
171	\begin{table*}[t]
172	\centering
173	\small
174	\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). SJ: Soft Jaccard, FK: Fleiss' $\kappa$, EM: Exact Match, LP: Log-prob, VC: Voting Confidence. Best non-oracle signal per row in \textbf{bold}. No signal significantly outperforms greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
175	\label{tab:cross_selection}
176	\begin{tabular}{llccccccc}
177	\toprule
178	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
179	\midrule
180	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
181	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
182	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
183	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
184	\bottomrule
185	\end{tabular}
186	\end{table*}
187	
188	\paragraph{Diminishing returns of $N$-scaling.}
189	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2024scaling}.
190	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
191	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
192	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
193	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
194	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
195	
196	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
197	
198	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
199	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
200	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
201	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
202	
203	\begin{table}[t]
204	\centering
205	\small
206	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
207	\label{tab:bootstrap_signal_ci}
208	\begin{tabular}{lcc}
209	\toprule
210	Signal & $\rho$ & 95\% CI \\
211	\midrule
212	VC & +0.379 & [+0.299, +0.456] \\
213	SJ & +0.360 & [+0.277, +0.437] \\
214	EM & +0.295 & [+0.212, +0.371] \\
215	FK & +0.267 & [+0.176, +0.354] \\
216	LP & +0.205 & [+0.119, +0.291] \\
217	\bottomrule
218	\end{tabular}
219	
220	\vspace{0.5em}
221	
222	\begin{tabular}{lccc}
223	\toprule
224	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
225	\midrule
226	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
227	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
228	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
229	\bottomrule
230	\end{tabular}
231	
232	\smallskip
233	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
234	\end{table}
235	
236	\section{Diversity and Selection Analysis}\label{app:diversity}
237	
238	\paragraph{Output diversity quantification.}
239	Table~\ref{tab:diversity} summarizes output diversity across configurations.
240	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
241	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
242	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.
243	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
244	
245	\begin{table}[t]
246	\centering
247	\small
248	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
249	\label{tab:diversity}
250	\begin{tabular}{lcc}
251	\toprule
252	Config & Identical & Unique \\
253	\midrule
254	Qwen/SciERC & 11\% & 43\% \\
255	LLaMA/SciERC & 18\% & 39\% \\
256	Qwen/CoNLL & 57\% & --- \\
257	LLaMA/CoNLL & 88\% & --- \\
258	WNUT-17 & 55\% & --- \\
259	\bottomrule
260	\end{tabular}
261	\end{table}
262	
263	\paragraph{Oracle-improvable fraction.}
264	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
265	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
266	
267	\paragraph{Diversity-stratified selection gap.}
268	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
269	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.
270	This rules out insufficient diversity as an explanation for the correlation-selection gap.
271	
272	\paragraph{TOST equivalence testing.}
273	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
274	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\delta$.
275	The $\delta$ values are anchored to oracle headroom (13--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
276	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
277	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
278	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
279	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
280	
281	\begin{table}[t]
282	\centering
283	\small
284	\caption{TOST equivalence testing: signals vs.\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ greedy).}
285	\label{tab:tost}
286	\begin{tabular}{l cccc cccc}
287	\toprule
288	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
289	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
290	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
291	\midrule
292	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
293	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
294	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
295	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
296	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
297	\bottomrule
298	\end{tabular}
299	\end{table}
300	
301	\section{Multi-Seed Stability}\label{app:multiseed}
302	
303	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC NER ($N{=}8$, $T{=}1.0$).
304	The signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals, confirming that our findings are robust to random seed variation.
305	LLaMA absolute values are systematically lower than Qwen, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
306	
307	\begin{table}[t]
308	\centering
309	\small
310	\caption{Multi-seed quality estimation on SciERC NER ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). Top: Spearman $\rho$; bottom: AUROC. Signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations ($\sigma{\leq}0.025$).}
311	\label{tab:multiseed}
312	\begin{tabular}{lccccc}
313	\toprule
314	& LP & FK & SJ & VC & EM \\
315	\midrule
316	\multicolumn{6}{l}{\textit{Spearman $\rho$ (mean $\pm\sigma$)}} \\
317	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
318	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
319	\midrule
320	\multicolumn{6}{l}{\textit{AUROC (mean $\pm\sigma$)}} \\
321	Qwen & .613${\pm}$.002 & .618${\pm}$.009 & .684${\pm}$.009 & .697${\pm}$.010 & .661${\pm}$.010 \\
322	LLaMA & .577${\pm}$.007 & .616${\pm}$.011 & .655${\pm}$.010 & .689${\pm}$.005 & .636${\pm}$.006 \\
323	\bottomrule
324	\end{tabular}
325	\end{table}
326	
327	\section{Training Configuration}\label{app:training}
328	
329	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
330	
331	\begin{table}[t]
332	\centering
333	\small
334	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
335	\label{tab:training}
336	\begin{tabular}{ll}
337	\toprule
338	Parameter & Value \\
339	\midrule
340	LoRA rank / $\alpha$ & 32 / 64 \\
341	LoRA target & All linear modules \\
342	LoRA dropout & 0 \\
343	Optimizer & AdamW \\
344	Learning rate & 2e-4, cosine schedule \\
345	Warmup ratio & 0.1 \\
346	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
347	Epochs & 5 \\
348	Max sequence length & 2048 \\
349	Precision & bf16 \\
350	Gradient checkpointing & Enabled \\
351	Max gradient norm & 1.0 \\
352	Training seed & 42 \\
353	Framework & LLaMA Factory \\
354	\midrule
355	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
356	SciERC split & 1861 / 275 / 551 \\
357	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
358	& eval\_steps${=}$200, save\_limit${=}$5 \\
359	\bottomrule
360	\end{tabular}
361	\end{table}
362	
363	\paragraph{Prompt template.}
364	For NER, we use a structured prompt:
365	\begin{quote}
366	\small
367	\texttt{System:} You are an expert in Named Entity Recognition.\\
368	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
369	Text: \texttt{\{input\_text\}}\\
370	Entity types: \texttt{\{schema\_types\}}
371	\end{quote}
372	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
373	
374	\paragraph{Constrained decoding.}
375	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
376	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
377	
378	\section{Log-Probability Score Compression}\label{app:logprob_ties}
379	
380	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}).
381	The median within-instance LP range is only 0.041, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
382	At $\varepsilon{=}0.05$, 60.3\% of instances have a within-sample range below the threshold, leaving LP unable to meaningfully distinguish candidates.
383	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
384	
385	\begin{table}[t]
386	\centering
387	\small
388	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
389	\label{tab:logprob_ties}
390	\begin{tabular}{lc}
391	\toprule
392	$\varepsilon$ threshold & Tied instances (\%) \\
393	\midrule
394	0.01 & 1.1\% \\
395	0.05 & 60.3\% \\
396	0.1  & ${\sim}$84\% \\
397	0.5  & ${\sim}$99\% \\
398	\bottomrule
399	\end{tabular}
400	\end{table}
401	
402	\paragraph{Non-tied subset.}
403	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
404	This confirms that LP carries useful per-sample quality information but is resolution-limited---the signal exists but is compressed below the discrimination threshold for most instances.
405	A free-form decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression is intrinsic, not decoding-regime-specific.
406	
407	\section{RE Conditional Selection}\label{app:re_conditional_selection}
408	
409	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
410	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
411	All five signals underperform greedy on both subsets.
412	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
413	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
414	
415	\begin{table}[t]
416	\centering
417	\small
418	\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
419	\label{tab:re_cond_selection}
420	\begin{tabular}{lcc}
421	\toprule
422	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
423	\midrule
424	Oracle & 0.585 & 0.757 \\
425	\midrule
426	LP & 0.395 & 0.600 \\
427	SJ & 0.386 & 0.604 \\
428	EM & 0.372 & 0.583 \\
429	VC & 0.359 & 0.574 \\
430	\midrule
431	Greedy & 0.404 & 0.674 \\
432	\bottomrule
433	\end{tabular}
434	\end{table}
435	
436	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
437	
438	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).
439	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
440	LP score distributions are nearly identical across regimes (within-instance std ratio $0.97{\times}$), confirming that score compression is intrinsic to the model and task.
441	
442	\begin{table}[t]
443	\centering
444	\small
445	\caption{Constrained vs.\ free-form decoding ablation on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B). LP compression and selection failure persist under free-form decoding.}
446	\label{tab:freeform_ablation}
447	\begin{tabular}{lcc}
448	\toprule
449	Metric & Constrained & Free-form \\
450	\midrule
451	LP within-instance std & 0.0206 & 0.0199 \\
452	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% \\
453	NER LP selection $\Delta$F1 & $+$0.59~pp & $+$0.18~pp \\
454	RE LP selection $\Delta$F1 & $-$0.68~pp & $+$1.69~pp \\
455	NER VC $\rho$ & 0.379 & 0.409 \\
456	Parse rate & 100\% & 99.95\% \\
457	\bottomrule
458	\end{tabular}
459	\end{table}
460	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b04af6a-1c33-4549-94e1-e7d260572d1e",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "2e8fc78e-3096-4ff1-9651-ae2513cdc2dd",
  "sourceToolAssistantUUID": "2b04af6a-1c33-4549-94e1-e7d260572d1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-15T10:25:17.115Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R27kRezPidPGoSVmLTdZBY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e8fc78e-3096-4ff1-9651-ae2513cdc2dd",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C84AUi2zeYCd7sNSJT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1c99280-ceb1-455a-8454-74e3f1e78d3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ar4z55SbCsdnftLJPxnLtJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3762,
      "cache_read_input_tokens": 73262,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3762
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 73262,
          "cache_creation_input_tokens": 3762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3762,
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

_source line 53 · 2026-05-15T10:25:17.121Z_

<details><summary>↩ Tool result · `toolu_01R27kRezPidPGoSVmLTdZBY`</summary>

```text
1	---
2	dream_id: dream_20260515T092545
3	tier: best
4	overall_score: borderline accept
5	timestamp: 2026-05-15T10:19:54.763849+00:00
6	---
7	
8	# Reviewer 2 (R2): Novelty and Related Work
9	
10	## 1. Summary
11	
12	This paper systematically evaluates five confidence signals from three families (structural, surface, model-internal) for quality estimation (QE) and sample selection in LLM-based information extraction under constrained decoding. The central finding is the "correlation-selection gap": consistency signals achieve strong instance-level QE (voting confidence rho=0.50, AUROC=0.73 on SciERC NER) but universally fail to improve best-of-N selection over greedy decoding. The paper evaluates across NER and RE on three datasets (SciERC, CoNLL-2003, WNUT-17) with two 8B models (Qwen3, LLaMA-3.1), characterizes task-difficulty-dependent signal rankings, and identifies boundary conditions where all signals collapse.
13	
14	---
15	
16	## 2. Novelty Assessment
17	
18	### 2a. The "predict-but-cannot-select" (correlation-selection gap) finding
19	
20	**Moderately novel, but partially expected.** The conceptual observation that instance-level aggregate signals cannot rank candidates within an instance is, as the authors themselves acknowledge in paper_framing.md, "noted not discovered" -- it follows definitionally from the fact that 4/5 signals produce a single scalar per instance. The more interesting empirical component is that logprob (the only per-sample signal) also fails on NER, and that the gap persists even under free-form decoding. However, the logprob failure is less surprising than presented: in a fine-tuned model producing near-deterministic outputs at high accuracy (greedy NER F1=0.61), logprob compression is an expected consequence of confident, well-calibrated fine-tuning. The paper would benefit from more explicitly engaging with the question of whether this finding would surprise a practitioner familiar with both self-consistency and structured prediction.
21	
22	**Strength**: The quantification of the gap with bootstrap CIs (p=0.39, Cohen's d=0.038) is rigorous. The oracle headroom analysis (NER +16pp, RE +18.7pp) effectively demonstrates that information exists but signals cannot access it.
23	
24	### 2b. QE-vs-selection conceptual distinction
25	
26	**Useful clarification, modest novelty.** Disentangling QE from selection is a genuine contribution to clarity in the IE confidence literature. However, this distinction is well-established in adjacent fields: quality estimation vs. reranking is a standard dichotomy in machine translation (Fomicheva et al. 2020, TACL), and selective prediction vs. best-of-N is implicit in the test-time scaling literature (Snell et al. 2024). The novelty lies in demonstrating that this distinction matters specifically for structured IE and explaining mechanistically why it does (instance-level aggregation vs. per-sample discrimination). This is incremental but useful.
27	
28	### 2c. Free-form ablation as diagnostic
29	
30	**The ablation result is genuinely informative.** The finding that removing constrained decoding does NOT recover logprob variance (std ratio 0.97) is a well-designed controlled experiment that falsifies a natural hypothesis. This is the most novel empirical contribution in the paper, as it rules out a plausible explanation and establishes that score compression is model/task intrinsic. However, this result appears only in the project framing documents and the ablation report -- it is NOT present in the current paper draft (the experiments.tex, discussion.tex, etc. do not contain the ablation results). If this is not included in the final submission, the paper loses its strongest novelty claim.
31	
32	### 2d. Supervised verifier baseline (DeBERTa)
33	
34	**Not yet available.** The abstract mentions "supervised DeBERTa verifier captures 15.9% of oracle headroom," but exp-019 is listed as "waiting for approval" and no results exist in the artifacts. If this is included in the final paper, it provides a useful "so what" anchor. A 15.9% headroom capture rate is modest but establishes that the gap is partially closable, transforming a pure negative result into an actionable one. The novelty of using a supervised verifier for IE selection is low (this is standard in the reasoning literature via Cobbe et al. 2021), but its application to structured IE is new.
35	
36	### 2e. Overall novelty verdict
37	
38	This is best characterized as a **systematic empirical study that extends self-consistency to a new domain (structured IE) and identifies a non-trivial negative result**. It is not a methodological contribution -- no new method is proposed. The novelty is in the empirical finding (the gap), the diagnostic rigor (the ablation, the bootstrap analysis), and the practical characterization (task-difficulty-dependent signal rankings). For EMNLP Findings, this level of novelty is appropriate if the execution is clean. The paper does not claim to introduce a new method, and the framing as an empirical analysis paper is honest.
39	
40	---
41	
42	## 3. Related Work Coverage
43	
44	### 3a. Overall assessment
45	
46	The related work section (as written in related_work.tex) is **comprehensive and well-organized**. The three-subsection structure (self-consistency/TTS, consistency for structured IE, uncertainty/calibration) covers the main threads effectively. The literature map contains 55 papers, and the paper cites 30+. This is adequate for EMNLP.
47	
48	### 3b. Key works cited and positioned
49	
50	- **Wang et al. 2023 (self-consistency)**: Properly cited as foundation, with clear differentiation (discrete answers vs. set-valued outputs). Good.
51	- **CISC, Self-Certainty, ReASC**: All cited with explicit positioning. The dialogue with Self-Certainty (Kang et al.) in the introduction is effective -- "reward-free selection succeeds for reasoning; our results demonstrate this does not transfer to structured extraction."
52	- **Nedellec and Xia 2026**: Thoroughly discussed with three specific limitations (surface matching, no selection, single domain). The differentiation is convincing and fair.
53	- **CoCoA (Vashurin et al. 2025a)**: Cited but discussed in only one sentence. Given that CoCoA is the closest methodological analog (MBR-based confidence+consistency fusion for UQ), it deserves more discussion. Specifically: how does CoCoA's MBR formulation relate to the paper's consensus-proximity analysis? Does the CoCoA framework predict the correlation-selection gap?
54	- **Snell et al. 2024, Brown et al. 2024**: Properly cited as TTS foundations.
55	- **Verifiers (Cobbe, Lightman)**: Cited as alternative paradigm. Adequate.
56	
57	### 3c. Critical missing references
58	
59	1. **Eikema and Aziz 2022 (MBR decoding)**: Listed in the abstract's reference set but I do not see it cited in related_work.tex. Given that the paper's SJ-based selection is conceptually related to MBR with set Jaccard as the utility function, MBR decoding should be explicitly discussed. The claim that "set-based IE metrics create different optimization landscape where consensus-proximity fails" needs MBR as the explicit foil.
60	
61	2. **Universal Self-Consistency (Chen et al. 2024)**: Cited in introduction and related work, but the discussion could be deeper. USC uses the LLM itself as a judge to select the most consistent answer -- this is a viable alternative to the metric-based signals the paper evaluates. The paper should discuss why USC was not included as a baseline (presumably cost, but this should be stated).
62	
63	3. **Fomicheva et al. 2020 (Unsupervised QE for MT)**: In the literature map but not in the paper. This is the closest analog from MT -- using MC dropout and ensemble uncertainty for quality estimation without supervision. The QE-vs-selection distinction the paper emphasizes is well-established in MT QE literature, and acknowledging this precedent would strengthen rather than weaken the paper.
64	
65	4. **Structured prediction under constrained decoding**: The paper uses Outlines/XGrammar for constrained decoding but does not discuss the growing literature on how grammar constraints affect model distributions. Work on how constrained decoding distorts logprob distributions (e.g., Park et al. 2024 on grammar-constrained decoding effects) would directly contextualize the logprob compression finding.
66	
67	5. **GenIE (Josifoski et al. 2022)**: In the literature map and cited in the related work, but its bi-level constrained decoding approach is directly relevant to understanding how constraints affect confidence signals. Could be discussed more.
68	
69	### 3d. Is the claim "none address structured IE" accurate?
70	
71	**Mostly accurate, with a caveat.** The claim that no prior self-consistency work addresses structured IE outputs is true in the strict sense -- Wang et al., CISC, Self-Certainty, ReASC all target discrete answers. However, Nedellec and Xia 2026 do study consistency for IE (NER and RE), and Atomic SC (Thirukovalluru et al. 2024) addresses non-discrete structured outputs (atomic sub-claims). The paper should soften this to "no prior work systematically compares confidence signal families for set-valued structured IE outputs or evaluates their selection utility" rather than implying no one has studied consistency for IE at all.
72	
73	### 3e. Differentiation from Nedellec and Xia 2026
74	
75	**Convincing.** The three-point differentiation (surface matching vs. SJ, no selection analysis, single domain) is concrete and fair. The paper directly quotes Nedellec and Xia's own acknowledged limitation about overlooking semantically consistent outputs, which is effective positioning. This is well-handled.
76	
77	### 3f. CoCoA discussion sufficiency
78	
79	**Insufficient.** CoCoA is the most methodologically similar work -- it fuses model confidence (logprob) with inter-sample consistency via an MBR framework. The paper's ensemble of SJ+logprob (Table 3) is conceptually similar. The paper should discuss: (a) whether CoCoA's formulation would predict the correlation-selection gap, (b) why the ensemble underperforms the best single signal (EM), and (c) how CoCoA's success on QA/summarization/translation contrasts with the paper's failure on structured IE. This contrast would strengthen the "structured IE is different" argument.
80	
81	---
82	
83	## 4. Framing and Positioning
84	
85	### 4a. Venue fit
86	
87	**Good fit for EMNLP Findings.** The paper is a systematic empirical study with a well-characterized negative result. It does not propose a new method, which makes it marginal for main conference, but the diagnostic rigor and practical guidance are valuable for Findings. The comparison-plus-boundary-conditions contribution pattern is well-suited to this venue.
88	
89	### 4b. "Correlation-selection gap" terminology
90	
91	**Clear and useful.** The term is well-defined, easy to remember, and captures the phenomenon precisely. It has potential to become a standard reference term if the paper is published. Minor concern: the term appears only in the NER context where it is absolute (no signal beats greedy). On RE, logprob does improve over greedy (+2.3pp), so the "gap" is partial. The paper should acknowledge this more prominently -- the gap is task-dependent, not universal, despite the paper_framing.md claiming universality.
92	
93	### 4c. Three contributions -- scope vs. evidence
94	
95	- **Contribution 1 (first systematic comparison)**: Well-supported by the evidence. Five signals, three datasets, two models. The scope is appropriate.
96	- **Contribution 2 (correlation-selection gap)**: Supported for NER, partially for RE. The bootstrap analysis (p=0.39) is rigorous. However, the claim would be stronger with the free-form ablation included in the paper (currently missing from the draft).
97	- **Contribution 3 (task-complexity boundary)**: The weakest contribution. The EM-dominates-easy / SJ-dominates-hard / all-converge-when-insufficient characterization is useful but somewhat obvious -- simpler signals suffice for simpler tasks. The WNUT-17 boundary analysis (logprob rho=-0.411, overconfidence on novel entities) is more interesting and could be elevated.
98	
99	### 4d. Title
100	
101	The current draft does not have a single consistent title. The abstract suggests the framing is about "confidence signals for test-time scaling in generative IE." The paper_framing.md proposes "Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction." The prompt's title is "Confidence Signals Predict but Cannot Select in Constrained-Decoding Information Extraction."
102	
103	The prompt's title includes "Constrained-Decoding" which is misleading if the ablation shows the gap is NOT constrained-decoding-specific. The paper_framing title "Strong Predictors, Weak Selectors" is more accurate and catchier. However, "Cannot Scale" overstates -- the paper shows signals cannot *select*, not that they cannot scale IE in general (e.g., QE-based routing could still help). I would recommend: **"Confidence Signals Predict but Cannot Select: The Correlation-Selection Gap in LLM-Based Information Extraction"**.
104	
105	---
106	
107	## 5. Potential Impact
108	
109	### 5a. Who benefits?
110	
111	- Practitioners deploying LLM-based IE systems who need to decide whether to invest in multi-sample generation and selection strategies. The paper's practical recommendation (use consistency for QE/routing, not for selection) is immediately actionable.
112	- Researchers working on test-time scaling who need to understand domain boundaries for self-consistency methods.
113	- Researchers developing confidence estimation for structured prediction tasks beyond IE.
114	
115	### 5b. Research directions opened
116	
117	- **Supervised verifiers for structured IE**: The oracle headroom analysis motivates training dedicated verifiers, analogous to the reasoning literature.
118	- **Per-sample signals for structured outputs**: The paper identifies that instance-level signals cannot select, motivating research into per-sample structural quality signals.
119	- **Constrained decoding effects on model distributions**: The ablation opens questions about when and how constrained decoding affects different aspects of generation quality.
120	
121	### 5c. Citation likelihood
122	
123	**Moderate.** The paper would likely be cited by: (a) future work on self-consistency for structured tasks, (b) papers on LLM-based IE that need to discuss confidence estimation, (c) test-time scaling papers that discuss domain limitations. The "correlation-selection gap" term could become a standard reference if the finding is robust. I estimate 15-30 citations in the first two years.
124	
125	---
126	
127	## 6. Weaknesses
128	
129	### W1. Novelty is primarily negative/empirical, not methodological.
130	The paper identifies a limitation (signals cannot select) but does not propose a solution. The free-form ablation and supervised verifier are diagnostic, not prescriptive. For Findings this is acceptable, but it limits impact.
131	
132	### W2. The free-form ablation -- the strongest novelty claim -- is missing from the paper draft.
133	The experiments.tex, discussion.tex, and conclusion.tex I reviewed do not contain the ablation results. The abstract mentions constrained decoding analysis, but the current paper body appears to be from an earlier draft (pre-D072). If this is not included in the final submission, the paper loses its most distinctive empirical contribution and reverts to a descriptive comparison study.
134	
135	### W3. Inconsistency between abstract/framing and paper body.
136	The abstract provided in the prompt mentions "removing grammar constraints recovers logprob variance ~3.5x" and "supervised DeBERTa verifier captures 15.9% of oracle headroom." The paper_framing.md (D072) says the ablation FALSIFIED the 3.5x claim (actual ratio is 0.97x, NOT 3.5x). The abstract appears to be from an older version. Additionally, the supervised verifier (exp-019) has not been completed. This creates a coherence risk if the final submission mixes old and new claims.
137	
138	### W4. Single RE benchmark limits the correlation-selection gap generalizability claim.
139	SciERC RE has 44% zero-F1 instances, creating a severe floor effect. The gap on RE may be partly an artifact of the model simply not being capable enough at this task. A second RE dataset (e.g., TACRED, DocRED) would substantially strengthen the claim.
140	
141	### W5. CoCoA and MBR under-discussed.
142	As noted in Section 3, CoCoA is the closest methodological analog and deserves deeper engagement. The SJ-based selection is essentially MBR with Jaccard utility, and the paper should make this connection explicit and explain why MBR fails here despite succeeding in MT.
143	
144	### W6. The "universality" claim requires nuance.
145	The paper_framing claims the gap is "universal" based on the free-form ablation. But "universal" is a strong word -- it has been demonstrated on one task family (IE), two datasets for NER, one for RE, with two 8B models. The gap may not hold for larger models, different IE formulations (e.g., code-generation-based IE), or different output structures (e.g., event extraction). "Robust across our experimental conditions" is more defensible than "universal."
146	
147	### W7. Logprob RE selection gain (+2.3pp) somewhat undermines the gap narrative.
148	The paper frames the gap as the central finding, but logprob does help on RE. The narrative needs to more clearly articulate that the gap is absolute for NER but partial for RE, rather than presenting it as a universal failure. The current framing oscillates between "no signal helps" and "logprob helps on RE."
149	
150	---
151	
152	## 7. Questions for Authors
153	
154	**Q1.** The free-form ablation (exp_freeform_ablation) shows LP std ratio of 0.97x, falsifying the constrained decoding bottleneck hypothesis. But the abstract provided for review mentions "removing grammar constraints recovers logprob variance ~3.5x." Which is the correct claim for the final submission? This is a critical inconsistency that must be resolved.
155	
156	**Q2.** CoCoA (Vashurin et al. 2025a) unifies confidence and consistency via MBR, achieving strong results on QA and summarization. Your SJ-based selection is conceptually an MBR approach with Jaccard utility. Can you explain mechanistically why this MBR-like approach fails for IE when it succeeds for other generation tasks? Is it the discreteness of the output space, the set structure, or something else?
157	
158	**Q3.** The supervised verifier (DeBERTa, 15.9% headroom capture) is mentioned in the abstract but exp-019 appears incomplete. Will this be included in the final submission? If so, what is the training setup (how many labeled examples, cross-validation strategy)?
159	
160	**Q4.** You evaluate at N=8 and N=16. Given that RE signals improve substantially from N=8 to N=16 (voting rho from 0.340 to 0.448 per paper_framing.md), have you considered whether the correlation-selection gap might narrow at N=32 or N=64? The gap could be a sample budget artifact for RE rather than a fundamental limitation.
161	
162	**Q5.** The WNUT-17 finding (logprob rho=-0.411, strong negative correlation) is striking and arguably the most practically important result. Have you investigated whether this negative correlation is specific to novel/emerging entities, or whether it occurs for any OOD shift? This has implications for whether logprob should be used as a *negative* signal for abstention on OOD inputs.
163	
164	---
165	
166	## 8. Scores
167	
168	### Soundness: 3.5 / 5
169	**Justification**: The experimental methodology is rigorous -- bootstrap CIs, multiple seeds, leave-one-out circularity checks, cross-model validation. The statistical analysis is appropriate (Spearman rho, AUROC, bootstrap p-values, Cohen's d). However, the inconsistency between the abstract (3.5x variance recovery) and the actual ablation result (0.97x ratio) raises concerns about which claims will appear in the final paper. The single RE dataset and the incomplete supervised verifier experiment also reduce confidence. If the final paper resolves these issues, soundness would be 4.0.
170	
171	### Excitement: 2.5 / 5
172	**Justification**: The correlation-selection gap is a useful finding but not a surprising one. The definitional component (instance-level signals cannot rank per-sample) is straightforward. The empirical component (logprob also fails due to score compression) is more interesting but is partially expected for fine-tuned models. The free-form ablation proving intrinsic compression is the most exciting finding, but it is not in the current paper draft. Without the ablation and verifier, this is a competent empirical comparison study with a negative result -- useful for the community but not exciting. With the ablation included and well-framed, excitement would rise to 3.0.
173	
174	### Overall Assessment: 3.0 / 5 (Borderline)
175	**Justification**: This is a well-executed empirical study that makes a useful contribution to the structured IE and test-time scaling communities. The QE evaluation framework is thorough, the cross-model and cross-dataset validation is appropriate for the scope, and the correlation-selection gap is clearly demonstrated. The paper is honest about its limitations. However, the novelty is incremental -- extending self-consistency analysis to a new domain and documenting where it fails. The lack of a proposed solution limits impact. The critical question for accept/reject is whether the free-form ablation and supervised verifier are included: with them, this is a solid Findings paper (3.5); without them, it is a descriptive comparison study that sits at the borderline (2.5-3.0). I score at 3.0 assuming partial inclusion of the ablation but noting the uncertainty.
176	
177	For EMNLP Findings, I lean toward **borderline accept** contingent on: (1) including the free-form ablation results with correct numbers, (2) resolving the abstract inconsistency, (3) expanding CoCoA/MBR discussion, and (4) toning down universality claims.
178	
179	### Confidence: 4 / 5
180	I am confident in this assessment. I have expertise in LLM uncertainty estimation and structured prediction, and I have reviewed the full paper draft, experimental results, and project documentation carefully. My main uncertainty is about what the final submission will contain, given the discrepancies between the abstract provided for review and the actual experimental results.
181	
182	---
183	
184	## Summary Recommendation
185	
186	**Borderline accept for EMNLP Findings**, pending resolution of the abstract/ablation inconsistency and inclusion of the free-form ablation as a first-class contribution. The paper's strengths are its systematic evaluation, rigorous statistical analysis, and the practically useful correlation-selection gap finding. Its weaknesses are limited novelty beyond the negative result, under-discussion of CoCoA/MBR, and an incomplete supervised verifier experiment. The free-form ablation is the paper's best claim to novelty and must be prominently included with correct numbers.
187	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1c99280-ceb1-455a-8454-74e3f1e78d3b",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "ad205139-0d69-4d88-b669-27698f459963",
  "sourceToolAssistantUUID": "b1c99280-ceb1-455a-8454-74e3f1e78d3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-15T10:25:21.975Z_

Now let me check the references file to assess citation quality.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad205139-0d69-4d88-b669-27698f459963",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C8QYKtTfQx1iQpR7yR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b534508-3620-4b9d-a16c-b8d4fd740d72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017W7SA8JB5H3RyH3juJF35K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18247,
      "cache_read_input_tokens": 77024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18247,
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

_source line 55 · 2026-05-15T10:25:24.000Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XExXEgDmCKDiLUCoVAfbEs`</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b534508-3620-4b9d-a16c-b8d4fd740d72",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C8QYKtTfQx1iQpR7yR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9402a9d2-a9d3-429d-9862-59ef0559d7ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017W7SA8JB5H3RyH3juJF35K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18247,
      "cache_read_input_tokens": 77024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18247,
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

_source line 56 · 2026-05-15T10:25:24.042Z_

<details><summary>↩ Tool result · `toolu_01XExXEgDmCKDiLUCoVAfbEs`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9402a9d2-a9d3-429d-9862-59ef0559d7ac",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "4433cce7-104d-40ea-a958-21f3254aac33",
  "sourceToolAssistantUUID": "9402a9d2-a9d3-429d-9862-59ef0559d7ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T10:25:30.588Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BG7wKUD1GQAVYxfy3HUCtu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4433cce7-104d-40ea-a958-21f3254aac33",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C8vfoixxste4tqPYFF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec7cdbbf-d36f-4464-b0ad-d944b5074e60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g6aVro3DrX1RhRpjwqUMV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 242,
      "cache_read_input_tokens": 95271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 242,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 58 · 2026-05-15T10:25:30.594Z_

<details><summary>↩ Tool result · `toolu_01BG7wKUD1GQAVYxfy3HUCtu`</summary>

```text
1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
45	  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},
46	  booktitle = {W-NUT Workshop at EMNLP 2017},
47	  year = {2017},
48	  url = {https://aclanthology.org/W17-4418/}
49	}
50	
51	@inproceedings{desai2020calibration,
52	  title = {Calibration of Pre-trained Transformers},
53	  author = {Desai, Shrey and Durrett, Greg},
54	  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
55	  year = {2020},
56	  doi = {10.18653/v1/2020.emnlp-main.21},
57	  url = {http://dx.doi.org/10.18653/v1/2020.emnlp-main.21}
58	}
59	
60	@inproceedings{eikema2022sampling,
61	  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},
62	  author = {Eikema, Bryan and Aziz, Wilker},
63	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
64	  year = {2022},
65	  pages = {10978--10993},
66	  doi = {10.18653/v1/2022.emnlp-main.754}
67	}
68	
69	@inproceedings{fisch2021conformal,
70	  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},
71	  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},
72	  booktitle = {ICML 2021},
73	  year = {2021},
74	  doi = {10.5555/3524938.3525234},
75	  url = {https://arxiv.org/abs/2102.08898}
76	}
77	
78	@article{freitag2022high,
79	  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},
80	  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},
81	  journal = {Transactions of the Association for Computational Linguistics},
82	  volume = {10},
83	  year = {2022},
84	  pages = {811--825},
85	  doi = {10.1162/tacl_a_00491}
86	}
87	
88	@inproceedings{he2024uncertainty,
89	  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},
90	  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},
91	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},
92	  year = {2024},
93	  pages = {2823--2835},
94	  doi = {10.18653/v1/2024.findings-naacl.180}
95	}
96	
97	@article{fleiss1971agreement,
98	  title = {Measuring nominal scale agreement among many raters.},
99	  author = {Fleiss, Joseph L.},
100	  journal = {Psychological Bulletin},
101	  year = {1971},
102	  doi = {10.1037/h0031619},
103	  url = {http://dx.doi.org/10.1037/h0031619}
104	}
105	
106	@inproceedings{gal2016dropout,
107	  title = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},
108	  author = {Gal, Yarin and Ghahramani, Zoubin},
109	  booktitle = {ICML 2016},
110	  year = {2016},
111	  url = {https://arxiv.org/abs/1506.02142}
112	}
113	
114	@inproceedings{geifman2017selective,
115	  title = {Selective Classification for Deep Neural Networks},
116	  author = {Geifman, Yonatan and El-Yaniv, Ran},
117	  booktitle = {NeurIPS 2017},
118	  year = {2017},
119	  url = {https://arxiv.org/abs/1705.08500}
120	}
121	
122	@article{feng2025optimal,
123	  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},
124	  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},
125	  journal = {arXiv preprint arXiv:2511.12309},
126	  year = {2025},
127	  url = {https://arxiv.org/abs/2511.12309}
128	}
129	
130	@inproceedings{geng2024confidence,
131	  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},
132	  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},
133	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
134	  year = {2024},
135	  doi = {10.18653/v1/2024.naacl-long.366},
136	  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}
137	}
138	
139	@inproceedings{guo2017calibration,
140	  title = {On Calibration of Modern Neural Networks},
141	  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
142	  booktitle = {ICML 2017},
143	  year = {2017},
144	  url = {https://arxiv.org/abs/1706.04599}
145	}
146	
147	@article{hobelsberger2025systematic,
148	  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},
149	  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},
150	  journal = {arXiv preprint arXiv:2510.20460},
151	  year = {2025},
152	  url = {https://arxiv.org/abs/2510.20460}
153	}
154	
155	@article{jaccard1901distribution,
156	  title = {Étude comparative de la distribution florale dans une portion des Alpes et du Jura},
157	  author = {Jaccard, Paul},
158	  journal = {Bulletin de la Société Vaudoise des Sciences Naturelles},
159	  year = {1901},
160	  url = {https://www.researchgate.net/publication/225035806}
161	}
162	
163	@inproceedings{josifoski2022genie,
164	  title = {{GenIE}: Generative Information Extraction},
165	  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},
166	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
167	  year = {2022},
168	  doi = {10.18653/v1/2022.naacl-main.342},
169	  url = {https://arxiv.org/abs/2112.08340}
170	}
171	
172	@article{kadavath2022language,
173	  title = {Language Models (Mostly) Know What They Know},
174	  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},
175	  journal = {arXiv preprint arXiv:2207.05221},
176	  year = {2022},
177	  url = {https://arxiv.org/abs/2207.05221}
178	}
179	
180	@inproceedings{kang2025selfcertainty,
181	  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},
182	  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},
183	  booktitle = {NeurIPS 2025},
184	  year = {2025},
185	  url = {https://arxiv.org/abs/2502.18581}
186	}
187	
188	@inproceedings{kim2024verifiner,
189	  title = {{V}erifi{NER}: Verification-augmented {NER} via Knowledge-grounded Reasoning with Large Language Models},
190	  author = {Kim, Seoyeon and Seo, Kwangwook and Chae, Hyungjoo and Yeo, Jinyoung and Lee, Dongha},
191	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
192	  year = {2024},
193	  pages = {2441--2461},
194	  doi = {10.18653/v1/2024.acl-long.134}
195	}
196	
197	@inproceedings{kim2026reasc,
198	  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},
199	  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},
200	  booktitle = {ACL 2026},
201	  year = {2026},
202	  url = {https://arxiv.org/abs/2601.02970}
203	}
204	
205	@article{kossen2024semantic,
206	  title = {Semantic Entropy Probes: Robust and Cheap Hallucination Detection in {LLMs}},
207	  author = {Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},
208	  journal = {arXiv preprint arXiv:2406.15927},
209	  year = {2024},
210	  url = {https://arxiv.org/abs/2406.15927}
211	}
212	
213	@article{li2025llms,
214	  title = {LLMs Can Generate a Better Answer by Aggregating Their Own Responses},
215	  author = {Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi and Liang, Chen and Chen, Weizhu and Wang, Haoyu and Zhao, Tuo},
216	  journal = {arXiv preprint arXiv:2503.04104},
217	  year = {2025},
218	  url = {https://arxiv.org/abs/2503.04104}
219	}
220	
221	@inproceedings{kuhn2023semantic,
222	  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},
223	  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},
224	  booktitle = {ICLR 2023},
225	  year = {2023},
226	  url = {https://arxiv.org/abs/2302.09664}
227	}
228	
229	@inproceedings{malinin2021uncertainty,
230	  title = {Uncertainty Estimation in Autoregressive Structured Prediction},
231	  author = {Malinin, Andrey and Gales, Mark},
232	  booktitle = {International Conference on Learning Representations},
233	  year = {2021},
234	  url = {https://openreview.net/forum?id=jN5y-zb5Q7m}
235	}
236	
237	@inproceedings{lakshminarayanan2017ensembles,
238	  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},
239	  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},
240	  booktitle = {NeurIPS 2017},
241	  year = {2017},
242	  url = {https://arxiv.org/abs/1612.01474}
243	}
244	
245	@inproceedings{li2023codeie,
246	  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
247	  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
248	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},
249	  year = {2023},
250	  doi = {10.18653/v1/2023.acl-long.855},
251	  url = {https://arxiv.org/abs/2305.05711}
252	}
253	
254	@inproceedings{lightman2024verify,
255	  title = {Let's Verify Step by Step},
256	  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
257	  booktitle = {ICLR 2024},
258	  year = {2024},
259	  url = {https://arxiv.org/abs/2305.20050}
260	}
261	
262	@inproceedings{luan2018scierc,
263	  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
264	  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
265	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
266	  year = {2018},
267	  doi = {10.18653/v1/D18-1360},
268	  url = {http://dx.doi.org/10.18653/v1/D18-1360}
269	}
270	
271	@inproceedings{manakul2023selfcheckgpt,
272	  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},
273	  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},
274	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
275	  year = {2023},
276	  doi = {10.18653/v1/2023.emnlp-main.557},
277	  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}
278	}
279	
280	@article{nedellec2026consistency,
281	  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},
282	  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},
283	  journal = {Genomics \& Informatics},
284	  year = {2026},
285	  doi = {10.1186/s44342-025-00063-2},
286	  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}
287	}
288	
289	@article{oh2025latentsc,
290	  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},
291	  author = {Oh, Jungsuk and Lee, Jay-Yoon},
292	  journal = {arXiv preprint arXiv:2508.18395},
293	  year = {2025},
294	  url = {https://arxiv.org/abs/2508.18395}
295	}
296	
297	@inproceedings{sainz2024gollie,
298	  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
299	  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},
300	  booktitle = {ICLR 2024},
301	  year = {2024},
302	  url = {https://arxiv.org/abs/2310.03668}
303	}
304	
305	@inproceedings{shelmanov2021active,
306	  title = {Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates},
307	  author = {Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis and Larionov, Daniil and Khromov, Nikita and Kozlova, Olga and Artemova, Ekaterina and Dylov, Dmitry V. and Panchenko, Alexander},
308	  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},
309	  year = {2021},
310	  doi = {10.18653/v1/2021.eacl-main.145},
311	  url = {http://dx.doi.org/10.18653/v1/2021.eacl-main.145}
312	}
313	
314	@inproceedings{snell2024scaling,
315	  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},
316	  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
317	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
318	  year = {2025},
319	  url = {https://arxiv.org/abs/2408.03314}
320	}
321	
322	@inproceedings{taubenfeld2025cisc,
323	  title = {Confidence Improves Self-Consistency in LLMs},
324	  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},
325	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
326	  year = {2025},
327	  doi = {10.18653/v1/2025.findings-acl.1030},
328	  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}
329	}
330	
331	@inproceedings{thirukovalluru2024atomic,
332	  title = {Atomic Self-Consistency for Better Long Form Generations},
333	  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},
334	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
335	  year = {2024},
336	  doi = {10.18653/v1/2024.emnlp-main.706},
337	  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}
338	}
339	
340	@inproceedings{tjongkimsang2003conll,
341	  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},
342	  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},
343	  booktitle = {CoNLL 2003},
344	  year = {2003},
345	  url = {https://aclanthology.org/W03-0419/}
346	}
347	
348	@inproceedings{vashurin2025cocoa,
349	  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},
350	  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},
351	  booktitle = {NeurIPS 2025},
352	  year = {2025},
353	  url = {https://arxiv.org/abs/2502.04964}
354	}
355	
356	@inproceedings{wadhwa2023revisiting,
357	  title = {Revisiting Relation Extraction in the era of Large Language Models},
358	  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},
359	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
360	  year = {2023},
361	  doi = {10.18653/v1/2023.acl-long.868},
362	  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}
363	}
364	
365	@article{wang2023instructuie,
366	  title = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},
367	  author = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},
368	  journal = {arXiv preprint arXiv:2304.08085},
369	  year = {2023},
370	  url = {https://arxiv.org/abs/2304.08085}
371	}
372	
373	@inproceedings{wang2023selfconsistency,
374	  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
375	  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
376	  booktitle = {ICLR 2023},
377	  year = {2023},
378	  url = {https://arxiv.org/abs/2203.11171}
379	}
380	
381	@inproceedings{wang2025make,
382	  title = {Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning},
383	  author = {Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueqi and Tan, Chuyi and Pan, Boyuan and Hu, Yao and Li, Kan},
384	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
385	  pages = {6919--6932},
386	  year = {2025}
387	}
388	
389	@inproceedings{wang2024mathshepherd,
390	  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},
391	  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},
392	  booktitle = {ACL 2024},
393	  year = {2024},
394	  url = {https://arxiv.org/abs/2312.08935}
395	}
396	
397	@inproceedings{wang2025rankedvoting,
398	  title = {Ranked Voting based Self-Consistency of Large Language Models},
399	  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},
400	  booktitle = {ACL Findings 2025},
401	  year = {2025},
402	  url = {https://arxiv.org/abs/2505.10772}
403	}
404	
405	@article{wen2025know,
406	  title = {Know Your Limits: A Survey of Abstention in Large Language Models},
407	  author = {Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yulia and Howe, Bill and Wang, Lucy Lu},
408	  journal = {Transactions of the Association for Computational Linguistics},
409	  year = {2025},
410	  doi = {10.1162/tacl_a_00754},
411	  url = {http://dx.doi.org/10.1162/tacl_a_00754}
412	}
413	
414	@article{willard2023guided,
415	  title = {Efficient Guided Generation for Large Language Models},
416	  author = {Willard, Brandon T. and Louf, Rémi},
417	  journal = {arXiv preprint arXiv:2307.09702},
418	  year = {2023},
419	  url = {https://arxiv.org/abs/2307.09702}
420	}
421	
422	@inproceedings{xia2025survey,
423	  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},
424	  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},
425	  booktitle = {ACL Findings 2025},
426	  year = {2025},
427	  url = {https://aclanthology.org/2025.findings-acl.1101/}
428	}
429	
430	@article{xiao2019uncertainty,
431	  title = {Quantifying Uncertainties in Natural Language Processing Tasks},
432	  author = {Xiao, Yijun and Wang, William Yang},
433	  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},
434	  year = {2019},
435	  doi = {10.1609/aaai.v33i01.33017322},
436	  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}
437	}
438	
439	@inproceedings{zhang2023ener,
440	  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},
441	  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},
442	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},
443	  year = {2023},
444	  doi = {10.18653/v1/2023.findings-acl.103},
445	  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}
446	}
447	
448	@inproceedings{zheng2024llamafactory,
449	  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},
450	  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},
451	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},
452	  year = {2024},
453	  pages = {400--410},
454	  doi = {10.18653/v1/2024.acl-demos.38}
455	}
456	
457	@inproceedings{zhou2024uniner,
458	  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
459	  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
460	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
461	  year = {2024},
462	  url = {https://arxiv.org/abs/2308.03279}
463	}
464	
465	@inproceedings{xiong2024llm,
466	  title = {Can {LLMs} Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in {LLMs}},
467	  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},
468	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
469	  year = {2024},
470	  url = {https://arxiv.org/abs/2306.13063}
471	}
472	
473	@inproceedings{muller2021understanding,
474	  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},
475	  author = {M{\"u}ller, Mathias and Sennrich, Rico},
476	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
477	  year = {2021},
478	  url = {https://arxiv.org/abs/2105.08504}
479	}
480	
481	@inproceedings{heo2025uncertainty,
482	  title = {Do {LLMs} Estimate Uncertainty Well in Instruction Following?},
483	  author = {Heo, Juyeon and Xiong, Miao and Heinze-Deml, Christina and Narain, Jaya},
484	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
485	  year = {2025},
486	  url = {https://arxiv.org/abs/2410.14582}
487	}
488	
489	@inproceedings{eikema2025structured,
490	  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},
491	  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},
492	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
493	  year = {2025},
494	  url = {https://arxiv.org/abs/2510.20700}
495	}
496	
497	@article{zhang2025tts,
498	  title = {A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?},
499	  author = {Zhang, Qiyuan and Lyu, Fuyuan and Sun, Zexu and Wang, Lei and Zhang, Weixu and Guo, Zhihan and Wang, Yufei},
500	  journal = {arXiv preprint arXiv:2503.24235},
501	  year = {2025},
502	  url = {https://arxiv.org/abs/2503.24235}
503	}
504	
505	@article{venktesh2025trust,
506	  title = {Trust but Verify! A Survey on Verification Design for Test-time Scaling},
507	  author = {Venktesh, V and Rathee, Mandeep and Anand, Avishek},
508	  journal = {arXiv preprint arXiv:2508.16665},
509	  year = {2025},
510	  url = {https://arxiv.org/abs/2508.16665}
511	}
512	
513	@inproceedings{jinnai2024mbr,
514	  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},
515	  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},
516	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
517	  year = {2024},
518	  url = {https://arxiv.org/abs/2311.05263}
519	}
520	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec7cdbbf-d36f-4464-b0ad-d944b5074e60",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "76b52f3f-90aa-4360-b8a2-6f104afe2f85",
  "sourceToolAssistantUUID": "ec7cdbbf-d36f-4464-b0ad-d944b5074e60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-15T10:25:34.634Z_

Now I have a thorough understanding of the paper. Let me write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76b52f3f-90aa-4360-b8a2-6f104afe2f85",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C9QvRdRPS2irLxzdSs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0eca4b78-946d-46d1-a385-ae3bca7c7d05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ryKLhNMjnRwRMPXasiWoM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10032,
      "cache_read_input_tokens": 95513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10032,
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

_source line 60 · 2026-05-15T10:25:35.865Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0178zsQwWXepn6kFqbequNmA`</summary>

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
  "parentUuid": "0eca4b78-946d-46d1-a385-ae3bca7c7d05",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C9QvRdRPS2irLxzdSs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a10f1600-1647-4a49-b336-7616ef7de117",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ryKLhNMjnRwRMPXasiWoM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10032,
      "cache_read_input_tokens": 95513,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10032
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 95513,
          "cache_creation_input_tokens": 10032,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10032,
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

_source line 61 · 2026-05-15T10:25:35.867Z_

<details><summary>↩ Tool result · `toolu_0178zsQwWXepn6kFqbequNmA`</summary>

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
  "parentUuid": "a10f1600-1647-4a49-b336-7616ef7de117",
  "isSidechain": true,
  "promptId": "97f77989-7a29-4166-bb48-a138e352abb4",
  "agentId": "af468f80c09f420ae",
  "type": "user",
  "uuid": "3e933cb8-3af7-4f1a-a380-46cbaacc84c5",
  "sourceToolAssistantUUID": "a10f1600-1647-4a49-b336-7616ef7de117",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-15T10:27:14.438Z_



## R2 Review: Novelty & Related Work

### Paper Summary (2-3 sentences)

This paper systematically evaluates five confidence signals from three families (structural, surface, model-internal) for quality estimation and best-of-N selection in LLM-based structured information extraction (NER, RE) using fine-tuned 8B models under constrained decoding. The central finding is the "correlation-selection gap": signals that reliably estimate output quality (AUROC up to 0.749, rho up to 0.379) universally fail as sample selectors (best signal +0.6pp, p=0.39), with a controlled free-form ablation confirming that log-probability score compression is intrinsic to the model/task rather than an artifact of constrained decoding. Signal rankings are shown to be task-difficulty-dependent across three datasets and two model families.

### Strengths

- **The correlation-selection gap is a genuinely useful conceptual contribution.** The explicit decomposition of confidence utility into quality estimation vs. sample selection, and the demonstration that these decouple for structured IE, fills a real gap in the literature. While the QE-vs-reranking distinction exists in MT (Fomicheva et al. 2020), its formal articulation and empirical demonstration for set-valued structured outputs is new. The term itself is well-defined and memorable.

- **The free-form ablation is well-designed and informative.** Falsifying the natural hypothesis that constrained decoding causes log-probability compression (std ratio 0.97x, tied fraction moves only 59.7% to 57.7%) is the paper's strongest empirical novelty. This is a controlled experiment that rules out a plausible explanation by elimination, the gold standard for negative-result papers. The finding that fine-tuned 8B models achieve 99.95% valid JSON without grammar constraints is a useful secondary observation.

- **Rigorous statistical methodology throughout.** Bootstrap CIs for selection (p=0.39, Cohen's d=0.038, 95% CI [-3.0, +4.2]pp), TOST equivalence testing, pairwise bootstrap for signal comparisons, 3-seed stability analysis (sigma <= 0.025), Fisher z-tests for cross-task comparisons. This level of rigor is uncommon in empirical NLP papers and lends credibility to the negative result.

- **Related work coverage is comprehensive and well-structured.** The three-paragraph organization (self-consistency/TTS, consistency for structured IE, uncertainty/calibration) efficiently covers a large literature. 45+ references spanning self-consistency, MBR decoding, conformal prediction, token-level NER uncertainty, ensemble methods, verifier/reward models, and TTS scaling theory. The explicit connection to MBR decoding (Section 5, "Connection to MBR decoding") and the citation of Eikema & Aziz (2022), Freitag et al. (2022), Muller & Sennrich (2021), and the concurrent Eikema et al. (2025) on structure-conditional MBR is particularly well-handled.

- **Differentiation from Nedellec & Xia (2026) is convincing and fair.** The three-point differentiation (surface matching vs. structural SJ, no selection study, single domain) is concrete. Directly quoting their acknowledged limitation about "overlooking semantically consistent outputs" as motivation for SJ is effective positioning that does not misrepresent the prior work.

- **Honest scope delineation.** The paper repeatedly marks RE findings as "preliminary, single benchmark," acknowledges WNUT-17 as a boundary condition rather than a positive result, and notes where bootstrap CIs include zero. This intellectual honesty is appropriate and appreciated.

- **The MBR connection provides theoretical grounding.** Framing SJ-based consensus-proximity selection as MBR decoding with Jaccard utility, and explaining mechanistically why it fails (utility correlates with quality across instances but not within them), elevates the paper beyond a purely empirical study to one with explanatory depth.

### Weaknesses

- **W1. The definitional component of the gap (4/5 signals are instance-level) is not a discovery.** The paper acknowledges this ("noted not discovered" in the framing documents), and the introduction correctly characterizes it as a "conceptual distinction." However, the presentation sometimes conflates this trivial observation with the genuinely interesting empirical finding that log-probability also fails and that MBR-style consensus-proximity selection does not recover discrimination. The contribution would be sharper if the definitional layer were dispatched in a single sentence and the empirical layers (LP compression, MBR failure, ablation) were foregrounded more aggressively.

- **W2. Novelty is primarily empirical/negative, with no proposed solution.** The paper identifies a limitation and diagnoses its cause but offers no method to close the gap. The supervised verifier (exp-019) was skipped. For EMNLP Findings, this is acceptable if the diagnosis is sufficiently deep, but it limits the paper's impact and citation footprint. The paper essentially tells practitioners "don't use unsupervised signals for selection in structured IE" without offering an alternative beyond "train a verifier" (which is obvious and well-established from Cobbe et al. 2021).

- **W3. The "universality" claim needs qualification.** The paper claims the gap is "fundamental" and "intrinsic to the model and task." This has been demonstrated on two 8B models, two NER datasets, one RE dataset, with N <= 16. The gap may not hold for (a) larger models (70B+) that produce higher-quality samples with potentially less LP compression, (b) different IE formulations (code-generation-based IE, retrieval-augmented IE), (c) larger N where MBR estimates become more stable, or (d) event extraction or other structured tasks. The ablation proves the gap is not constrained-decoding-specific, but "not constrained-decoding-specific" is not the same as "fundamental." The paper should use "robust across our experimental conditions" rather than "fundamental" or "universal."

- **W4. CoCoA (Vashurin et al. 2025) is under-discussed.** CoCoA is the closest methodological analog: it fuses model confidence with inter-sample consistency via an MBR framework for uncertainty quantification on QA/summarization/translation. The paper's SJ+LP ensemble (Section 4.3, logistic regression) is conceptually similar. The current treatment is a single sentence in the related work. The paper should discuss: (a) whether CoCoA's MBR formulation would predict the correlation-selection gap, (b) why their MBR approach succeeds on QA/translation but the paper's analogous approach fails on IE, and (c) what structural property of IE outputs (set-valued, combinatorial) causes this divergence. This contrast would substantially strengthen the "structured IE is fundamentally different" argument.

- **W5. Single RE benchmark severely limits generalizability claims for Claim 1.** SciERC RE has 40% zero-F1 instances, creating a floor effect that compresses the discriminable range. The selection failure on RE may be partly an artifact of model incapability rather than a fundamental property of structured IE. A second RE dataset (TACRED, DocRED, or ACE05) would materially strengthen the claim. The paper acknowledges this limitation but still frames the gap as applying to "structured IE" broadly.

- **W6. The negative result is partially predictable for fine-tuned models.** Fine-tuning concentrates the model's output distribution, reducing both diversity and log-probability variance. The finding that LP scores are compressed (60% effectively tied) is consistent with what one would expect from a well-fine-tuned model that has high greedy accuracy. The paper should engage more directly with the question: would the gap also hold for prompted (non-fine-tuned) models, where LP variance is presumably higher? Nedellec & Xia (2026) study hard-prompted LLMs; comparing their consistency-accuracy patterns to the fine-tuned setting would sharpen the novelty claim.

- **W7. Missing discussion of why MBR fails here but succeeds in MT.** The paper states that "utility correlates with F1 across instances but not within them" but does not analyze *why* this is the case for IE and not for MT. Is it because (a) IE outputs are sets where partial overlap is the norm, making pairwise utility noisy? (b) The combinatorial output space means the "centroid" sample may not be close to the best sample? (c) MT outputs vary along a continuous quality dimension while IE outputs vary discretely (entity present/absent)? A more mechanistic analysis of the MBR failure mode would strengthen the theoretical contribution.

- **W8. Reference quality concern: several citations reference 2025-2026 venues with potential verification issues.** Kang et al. 2025 is listed as "NeurIPS 2025" in the bib but described as "ICLR 2026" in the framing documents (arxiv 2502.18581). Kim et al. 2026 (ReASC) is cited as "ACL 2026" based on an arxiv ID from January 2026. Oh et al. 2025 (Latent SC) has arxiv ID 2508.18395, suggesting an August 2025 submission -- the venue is listed as "arXiv preprint." Feng et al. 2025 (Optimal SC) has arxiv ID 2511.12309. These are not "placeholder names" in the sense of anonymized citations, but several venue attributions appear unverified or inconsistent between documents. The bib file should be audited for venue accuracy before submission.

### Questions for Authors

**Q1.** The free-form ablation was conducted on one dataset (SciERC) with one model (Qwen3-8B). Log-probability compression might behave differently on CoNLL (where greedy F1 is 0.91+ and output diversity is much lower) or with LLaMA. Have you considered extending the ablation to a second configuration to strengthen the "intrinsic" claim?

**Q2.** CoCoA (Vashurin et al. 2025) demonstrates that MBR-based fusion of confidence and consistency succeeds for QA/summarization/translation. Your SJ-based consensus-proximity selection is structurally similar. Can you articulate mechanistically why MBR fails for IE? Is it the set-valued output structure, the partial-overlap noise in pairwise utility, or something else? This would transform the negative finding from "it doesn't work" to "it doesn't work because of X structural property."

**Q3.** RE signal performance improves substantially from N=8 to N=16 (e.g., voting rho from 0.350 to higher values at N=16 per Table 5). Have you analyzed whether the correlation-selection gap narrows at larger N? If LP compression is partly a sample-size issue (insufficient diversity at N=8), the gap might be partially closable without supervised signals.

**Q4.** The WNUT-17 finding (LP rho = -0.410, strong negative correlation) is arguably the most practically important result. Could this negative LP signal be *used* for abstention -- i.e., flag instances where LP is high but consistency is low as likely OOD failures? This would convert the negative finding into a practical tool.

**Q5.** You evaluate fine-tuned models where LP compression is expected. Nedellec & Xia (2026) study hard-prompted (non-fine-tuned) LLMs. Would you expect the correlation-selection gap to also hold in the prompted setting, where LP variance is presumably higher?

### Minor Issues

- The Nedellec & Xia (2026) bib entry lists authors as "Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert" but the paper is cited as "Nédellec and Xia" throughout the text. The first author appears to be Yao. This should be corrected.

- Table 1 caption says "seed=42" but the multi-seed analysis (Table 8, Appendix B) shows sigma up to 0.025. The main table should note that single-seed values may vary by approximately this amount, or report multi-seed means.

- The paper uses "confidence signal" as an umbrella term but four of five are consistency signals (computed from inter-sample agreement) and one is a model-internal signal. The terminology is clear after Section 3 but could be confusing in the abstract where "confidence signals" might be interpreted as model-confidence (logprob) signals only.

- The Soft Jaccard formulation (Eq. 4) uses max(|g_i|, |g_j|) as normalizer, which differs from standard Jaccard's |union|. This design choice is mentioned but not motivated -- why penalize length asymmetry specifically? A brief justification would help.

- Figure 1 (overview) is described in the caption but I cannot evaluate its visual clarity from the tex alone. Ensure it clearly separates the QE pathway (instance-level, works) from the selection pathway (per-sample, fails).

### Scores

- **Soundness: 3.5/5** -- Methodology is rigorous with appropriate statistical controls. The free-form ablation is well-designed. However, single RE benchmark, single ablation configuration, and the gap between the ablation claim's strength ("fundamental") and its evidence base (one dataset, one model) prevent a higher score.

- **Excitement: 2.5/5** -- The correlation-selection gap is a useful finding for the structured IE and TTS communities, and the free-form ablation is informative. However, the definitional component is straightforward, the LP compression finding is partially expected for fine-tuned models, and the absence of any proposed solution limits impact. This is a competent diagnostic study rather than a result that changes how people think about the problem.

- **Overall: 3.0/5** -- A solid empirical study appropriate for EMNLP Findings. The QE evaluation framework is thorough, cross-model validation is appropriate, and the statistical analysis exceeds the norm. The free-form ablation elevates this above a descriptive comparison study. However, the novelty is incremental (extending self-consistency analysis to structured IE and documenting where it fails), the lack of a proposed solution limits practical impact, and the "fundamental limitation" framing overstates what the evidence supports. For Findings acceptance, the paper would benefit from (1) toning down universality claims, (2) deepening the CoCoA/MBR comparison, and (3) adding a second ablation configuration.

- **Confidence: 4/5** -- I have reviewed the full paper text, appendix, bibliography, project framing documents, experimental logs, and prior dream reviews carefully. My assessment is grounded in familiarity with the self-consistency, MBR decoding, and LLM uncertainty estimation literatures. My main uncertainty is whether minor revisions addressing W3, W4, and W7 would shift my excitement score upward.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e933cb8-3af7-4f1a-a380-46cbaacc84c5",
  "isSidechain": true,
  "agentId": "af468f80c09f420ae",
  "requestId": "req_011Cb4C9o4C4vRo3cprUnbwN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b0ece38-bc36-4782-945a-45396cdbf998",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "79301dc3-a43c-42c1-b7ac-01c347c8ab59",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0181TscP21EaJ4PGBnqzSYAz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 105545,
      "output_tokens": 3528,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 685
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3528,
          "cache_read_input_tokens": 105545,
          "cache_creation_input_tokens": 685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 685,
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
